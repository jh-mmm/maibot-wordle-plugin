import asyncio
import logging
import random
import re
import sys
import time
from pathlib import Path
from typing import Any, ClassVar, Literal, Optional

_PLUGIN_DIR = str(Path(__file__).resolve().parent)
if _PLUGIN_DIR not in sys.path:
    sys.path.insert(0, _PLUGIN_DIR)

try:
    from maibot_sdk import (
        CONFIG_RELOAD_SCOPE_SELF,
        Command,
        EventHandler,
        Field,
        HookHandler,
        MaiBotPlugin,
        PluginConfigBase,
        Tool,
    )
    from maibot_sdk.types import (
        ErrorPolicy,
        EventType,
        HookMode,
        HookOrder,
        ToolParameterInfo,
        ToolParamType,
    )
except ImportError:
    # Local fallback for standalone environments
    CONFIG_RELOAD_SCOPE_SELF = "self"

    def Command(*args: Any, **kwargs: Any):
        return lambda func: func

    def Tool(*args: Any, **kwargs: Any):
        return lambda func: func

    def HookHandler(*args: Any, **kwargs: Any):
        return lambda func: func

    def EventHandler(*args: Any, **kwargs: Any):
        return lambda func: func

    def Field(default: Any = None, **kwargs: Any) -> Any:
        factory = kwargs.get("default_factory")
        return factory() if factory else default

    class PluginConfigBase:
        pass

    class MaiBotPlugin:
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            self.ctx = kwargs.get("ctx")
            self.config = kwargs.get("config")

    class ToolParameterInfo:
        def __init__(self, **kwargs: Any) -> None:
            pass

    class ToolParamType:
        STRING = "string"
        INTEGER = "integer"
        BOOLEAN = "boolean"

    class HookMode:
        BLOCKING = "blocking"
        NON_BLOCKING = "non_blocking"

    class HookOrder:
        EARLY = "early"
        NORMAL = "normal"
        LATE = "late"

    class ErrorPolicy:
        SKIP = "skip"
        RAISE = "raise"

    class EventType:
        ON_MESSAGE = "on_message"


from data.words_cet import CET_TARGET_WORDS
from data.words_target import TARGET_WORDS, WORD_DEFINITIONS
from data.words_valid import VALID_WORDS
from game.logic import LetterState, WordleGame
from game.storage import GameStorage, PlayerStats
from ui.renderer import render_stats_card, render_wordle_board

logger = logging.getLogger(__name__)


# ==========================================
# Configuration Models
# ==========================================

class PluginSectionConfig(PluginConfigBase):
    """插件基础设置"""

    __ui_label__: ClassVar[str] = "插件"
    __ui_icon__: ClassVar[str] = "package"
    __ui_order__: ClassVar[int] = 0

    config_version: str = Field(
        default="1.0.0",
        description="配置文件版本号",
        json_schema_extra={"label": "配置版本", "disabled": True, "hidden": True, "input_type": "text"},
    )
    enabled: bool = Field(
        default=True,
        description="是否启用 Wordle 猜单词插件",
        json_schema_extra={"label": "启用插件"},
    )


class GameSection(PluginConfigBase):
    """Wordle 游戏设置"""

    __ui_label__: ClassVar[str] = "游戏规则"
    __ui_icon__: ClassVar[str] = "gamepad-2"
    __ui_order__: ClassVar[int] = 1

    max_attempts: int = Field(
        default=6,
        description="每局最大允许猜测次数 (默认 6 次)",
        json_schema_extra={"label": "最大猜测次数"},
    )
    enforce_dictionary: bool = Field(
        default=True,
        description="是否要求猜测必须是词库中的有效英文单词 (关闭则允许任意合法 5 字母组合)",
        json_schema_extra={"label": "校验有效单词"},
    )
    allow_hints: bool = Field(
        default=True,
        description="是否允许玩家在游戏中通过 /wordle hint 获取字母提示",
        json_schema_extra={"label": "允许获取提示"},
    )
    max_hints_per_game: int = Field(
        default=2,
        description="单局游戏中最多允许获取提示的次数",
        json_schema_extra={"label": "每局最大提示次数"},
    )
    allow_direct_guess: bool = Field(
        default=True,
        description="当聊天流存在进行中游戏时，直接发送 5 字母单词是否自动作为猜测处理",
        json_schema_extra={"label": "允许直接发词猜测"},
    )
    session_timeout_minutes: int = Field(
        default=15,
        description="未操作超时自动结算与清理时间 (单位：分钟)",
        json_schema_extra={"label": "对局超时时间 (分钟)"},
    )
    cet_only: bool = Field(
        default=False,
        description="是否仅抽取大学英语四六级 (CET-4/6) 词汇作为目标单词 (开启后避免生僻冷门词)",
        json_schema_extra={"label": "仅限四六级词汇"},
    )


class DisplaySection(PluginConfigBase):
    """Wordle 展示设置"""

    __ui_label__: ClassVar[str] = "渲染与展示"
    __ui_icon__: ClassVar[str] = "palette"
    __ui_order__: ClassVar[int] = 2

    use_image_render: bool = Field(
        default=True,
        description="是否优先使用 HTML2PNG 图片卡片展示棋盘与战绩 (失败时自动降级为 Emoji 文本棋盘)",
        json_schema_extra={"label": "图片卡片渲染"},
    )
    show_definition: bool = Field(
        default=True,
        description="游戏结束时是否在结果中展示单词的中文释义与国际音标",
        json_schema_extra={"label": "展示中文释义与音标"},
    )


class AccessControlConfig(PluginConfigBase):
    """群/用户黑白名单访问控制配置。

    群维度与用户维度各自独立判定，两者都通过才会生效（AND 关系）。
    被拦截的消息不会阻止 AI 回复或后续处理，插件对该消息完全隐形。
    """

    __ui_label__: ClassVar[str] = "访问控制"
    __ui_icon__: ClassVar[str] = "shield"
    __ui_order__: ClassVar[int] = 3

    group_mode: Literal["off", "whitelist", "blacklist"] = Field(
        default="off",
        description="群名单模式：off=不限制 | whitelist=仅名单内群 | blacklist=名单内群不启用",
        json_schema_extra={
            "label": "群名单模式",
            "hint": "off=不限制 | whitelist=仅名单内群 | blacklist=名单内群不启用。私聊不受群名单影响",
            "order": 0,
        },
    )
    group_whitelist: list[str] = Field(
        default_factory=list,
        description="群白名单（群号），group_mode=whitelist 时生效；留空表示所有群都不启用",
        json_schema_extra={
            "label": "群白名单",
            "hint": "群号列表，group_mode=whitelist 时生效。注意：留空表示所有群都不启用",
            "order": 1,
        },
    )
    group_blacklist: list[str] = Field(
        default_factory=list,
        description="群黑名单（群号），group_mode=blacklist 时生效",
        json_schema_extra={
            "label": "群黑名单",
            "hint": "群号列表，group_mode=blacklist 时生效",
            "order": 2,
        },
    )
    user_mode: Literal["off", "whitelist", "blacklist"] = Field(
        default="off",
        description="用户名单模式：off=不限制 | whitelist=仅名单内用户 | blacklist=名单内用户不启用",
        json_schema_extra={
            "label": "用户名单模式",
            "hint": "off=不限制 | whitelist=仅名单内用户 | blacklist=名单内用户不启用。群聊私聊均生效",
            "order": 3,
        },
    )
    user_whitelist: list[str] = Field(
        default_factory=list,
        description="用户白名单（QQ 号），user_mode=whitelist 时生效；留空表示所有人都不启用",
        json_schema_extra={
            "label": "用户白名单",
            "hint": "QQ 号列表，user_mode=whitelist 时生效。注意：留空表示所有人都不启用",
            "order": 4,
        },
    )
    user_blacklist: list[str] = Field(
        default_factory=list,
        description="用户黑名单（QQ 号），user_mode=blacklist 时生效",
        json_schema_extra={
            "label": "用户黑名单",
            "hint": "QQ 号列表，user_mode=blacklist 时生效",
            "order": 5,
        },
    )


class WordleConfig(PluginConfigBase):
    """Wordle 插件完整配置"""

    plugin: PluginSectionConfig = Field(default_factory=PluginSectionConfig)
    game: GameSection = Field(default_factory=GameSection)
    display: DisplaySection = Field(default_factory=DisplaySection)
    access: AccessControlConfig = Field(default_factory=AccessControlConfig)


# ==========================================
# Wordle Plugin Implementation
# ==========================================

class WordlePlugin(MaiBotPlugin):
    """Wordle 猜单词游戏插件"""

    config_model = WordleConfig

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._fallback_config = WordleConfig()
        self._storage: Optional[GameStorage] = None
        self._target_words: list[str] = TARGET_WORDS
        self._cet_words: list[str] = CET_TARGET_WORDS
        self._word_defs: dict[str, dict[str, str]] = WORD_DEFINITIONS
        self._valid_words: set[str] = VALID_WORDS
        self._active_tasks: set[asyncio.Task[Any]] = set()

    @property
    def current_config(self) -> WordleConfig:
        try:
            cfg = self.config
            if cfg is not None:
                return cfg
        except Exception:
            pass
        return self._fallback_config

    @property
    def game_config(self) -> GameSection:
        """获取游戏规则配置（兼容对象与字典）。"""
        cfg = self.current_config
        if hasattr(cfg, "game") and cfg.game is not None:
            return cfg.game
        if isinstance(cfg, dict) and "game" in cfg:
            game_data = cfg.get("game", {})
            if isinstance(game_data, dict):
                return GameSection(**game_data)
        return self._fallback_config.game

    @property
    def display_config(self) -> DisplaySection:
        """获取渲染展示配置（兼容对象与字典）。"""
        cfg = self.current_config
        if hasattr(cfg, "display") and cfg.display is not None:
            return cfg.display
        if isinstance(cfg, dict) and "display" in cfg:
            display_data = cfg.get("display", {})
            if isinstance(display_data, dict):
                return DisplaySection(**display_data)
        return self._fallback_config.display

    @property
    def access_config(self) -> AccessControlConfig:
        """获取访问控制配置（兼容对象与字典）。"""
        cfg = self.current_config
        if hasattr(cfg, "access") and cfg.access is not None:
            return cfg.access
        if isinstance(cfg, dict) and "access" in cfg:
            access_data = cfg.get("access", {})
            if isinstance(access_data, dict):
                return AccessControlConfig(**access_data)
        return self._fallback_config.access

    @property
    def is_enabled(self) -> bool:
        """检查插件是否处于全局启用状态。"""
        try:
            cfg = self.current_config
            if hasattr(cfg, "plugin") and hasattr(cfg.plugin, "enabled"):
                return bool(cfg.plugin.enabled)
            if isinstance(cfg, dict):
                return bool(cfg.get("plugin", {}).get("enabled", True))
        except Exception:
            pass
        return True

    async def on_load(self) -> None:
        """Plugin initialization on load."""
        data_dir = None
        try:
            if self.ctx and hasattr(self.ctx, "paths") and hasattr(self.ctx.paths, "data_dir"):
                data_dir = Path(self.ctx.paths.data_dir)
        except Exception:
            pass

        self._storage = GameStorage(data_dir=data_dir)
        try:
            self.ctx.logger.info(
                "Wordle 插件加载成功！已载入 %d 个目标词 (%d 个四六级词) 和 %d 个合法单词。",
                len(self._target_words),
                len(self._cet_words),
                len(self._valid_words),
            )
        except Exception:
            logger.info(
                "Wordle 插件加载成功！已载入 %d 个目标词 (%d 个四六级词) 和 %d 个合法单词。",
                len(self._target_words),
                len(self._cet_words),
                len(self._valid_words),
            )

    async def on_unload(self) -> None:
        """Plugin unload cleanup."""
        try:
            self.ctx.logger.info("Wordle 插件已卸载。")
        except Exception:
            logger.info("Wordle 插件已卸载。")

    async def on_config_update(self, scope: str, config_data: dict, version: str) -> None:
        """Callback when configuration is reloaded."""
        if scope in (CONFIG_RELOAD_SCOPE_SELF, "self"):
            try:
                self.ctx.logger.info("Wordle 插件配置已热更新 (version=%s)", version)
            except Exception:
                logger.info("Wordle 插件配置已热更新 (version=%s)", version)

    # ----------------------------------------------------
    # Hook: chat.receive.before_process
    # 仅当插件启用、开启直接猜词且当前会话存在进行中游戏时才拦截 5 字母直接猜测
    # ----------------------------------------------------
    @HookHandler(
        "chat.receive.before_process",
        name="wordle_before_process_handler",
        description="有进行中游戏时拦截 5 字母纯英文单词直接猜词，避免进入普通回复链路",
        mode=HookMode.BLOCKING,
        order=HookOrder.EARLY,
        timeout_ms=3000,
        error_policy=ErrorPolicy.SKIP,
    )
    async def handle_wordle_before_process(
        self,
        message: dict | None = None,
        **kwargs: Any,
    ) -> dict[str, Any] | None:
        del kwargs
        # 1. 插件关闭时绝对不拦截
        if not self.is_enabled:
            return None

        # 2. 检查是否允许无斜杠直接发词猜测
        if not bool(getattr(self.game_config, "allow_direct_guess", True)):
            return None

        # 3. 过滤非字典消息或命令消息
        if not isinstance(message, dict) or bool(message.get("is_command")):
            return None

        # 4. 访问控制检查（未通过时直接放行给 AI 与其他插件，不拦截）
        if not self._is_access_allowed(message):
            return None

        # 5. 提取消息文本并校验是否为 5 字母纯英文单词
        raw_text = self._extract_message_text(message).strip()
        if len(raw_text) != 5 or not raw_text.isalpha():
            return None

        # 6. 提取 stream_id 并校验当前流中是否存在进行中的有效游戏
        stream_id = self._extract_message_stream_id(message)
        if not stream_id:
            return None

        game = self._storage.get_game(
            stream_id,
            timeout_minutes=self.game_config.session_timeout_minutes,
        ) if self._storage else None

        if not game or not game.is_active:
            # 没有进行中的游戏 -> 正常放行，普通聊天不受任何影响
            return None

        user_id = self._extract_message_user_id(message) or "user"
        user_name = self._extract_message_user_nickname(message) or "玩家"

        # 7. 后台异步安全执行猜词并阻断后续 AI 闲聊，异常兜底保障消息不丢失
        task = asyncio.create_task(
            self._safe_process_guess(stream_id, user_id, user_name, raw_text.upper())
        )
        self._active_tasks.add(task)
        task.add_done_callback(self._active_tasks.discard)
        return {"action": "abort"}

    async def _safe_process_guess(
        self,
        stream_id: str,
        user_id: str,
        user_name: str,
        word: str,
    ) -> None:
        """安全异步执行猜词逻辑，捕获异常并兜底提示，避免用户猜测静默丢失。"""
        try:
            await self._process_guess(stream_id, user_id, user_name, word)
        except Exception as exc:
            try:
                self.ctx.logger.exception(
                    "Wordle 处理猜词异常 (stream_id=%s, user=%s, word=%s): %s",
                    stream_id,
                    user_id,
                    word,
                    exc,
                )
            except Exception:
                logger.exception(
                    "Wordle 处理猜词异常 (stream_id=%s, user=%s, word=%s): %s",
                    stream_id,
                    user_id,
                    word,
                    exc,
                )
            try:
                if self.ctx and hasattr(self.ctx, "send") and hasattr(self.ctx.send, "text"):
                    await self.ctx.send.text(
                        f"⚠️ 处理猜词 '{word}' 时发生异常，请重试或发送 /wordle 查看当前棋盘。",
                        stream_id,
                    )
            except Exception:
                pass

    # ----------------------------------------------------
    # Event: ON_MESSAGE (Fallback Interceptor)
    # ----------------------------------------------------
    @EventHandler(
        "wordle_message_handler",
        description="Wordle 纯字母直接猜词消息拦截器（兼容事件层）",
        event_type=EventType.ON_MESSAGE,
        intercept_message=True,
        weight=50,
    )
    async def handle_wordle_message(
        self,
        message: dict | None = None,
        stream_id: str = "",
        **kwargs: Any,
    ) -> dict[str, Any]:
        del kwargs
        if not self.is_enabled:
            return {"continue_processing": True}
        if not bool(getattr(self.game_config, "allow_direct_guess", True)):
            return {"continue_processing": True}
        if not isinstance(message, dict) or bool(message.get("is_command")):
            return {"continue_processing": True}
        if not self._is_access_allowed(message):
            return {"continue_processing": True}

        raw_text = self._extract_message_text(message).strip()
        if len(raw_text) != 5 or not raw_text.isalpha():
            return {"continue_processing": True}

        target_stream_id = stream_id or self._extract_message_stream_id(message)
        if not target_stream_id:
            return {"continue_processing": True}

        game = self._storage.get_game(
            target_stream_id,
            timeout_minutes=self.game_config.session_timeout_minutes,
        ) if self._storage else None
        if not game or not game.is_active:
            return {"continue_processing": True}

        user_id = self._extract_message_user_id(message) or "user"
        user_name = self._extract_message_user_nickname(message) or "玩家"

        ok, msg, _ = await self._process_guess(target_stream_id, user_id, user_name, raw_text.upper())
        return {
            "continue_processing": False,
            "custom_result": {
                "success": ok,
                "message": msg,
            },
        }

    # ----------------------------------------------------
    # Command: /wordle, /w, /guess, /g
    # ----------------------------------------------------
    @Command(
        "wordle_command",
        pattern=r"^(?:/wordle|/w|/guess|/g)(?:\s+(?P<arg>.+))?\s*$",
        description="Wordle 猜单词主命令，支持开局、猜词、提示、认输、重开与战绩",
    )
    async def handle_wordle_command(
        self,
        stream_id: str = "",
        user_nickname: str = "",
        user_id: str = "",
        matched_groups: dict | None = None,
        message: dict | None = None,
        text: str = "",
        **kwargs: Any,
    ) -> tuple[bool, str, bool]:
        del kwargs
        if not self.is_enabled:
            return False, "Wordle 插件已处于禁用状态", True

        target_stream_id = stream_id or self._extract_message_stream_id(message)
        if not target_stream_id:
            return False, "缺少聊天流 stream_id", True

        target_user_id = user_id or self._extract_message_user_id(message) or "user"
        target_user_name = user_nickname or self._extract_message_user_nickname(message) or "玩家"

        if not self._is_access_allowed(message, user_id=target_user_id if target_user_id != "user" else None):
            return False, "当前群聊或用户无权限使用 Wordle 插件", True

        matched = matched_groups or {}
        arg = (matched.get("arg") or "").strip().lower()

        if not arg or arg == "start":
            active_game = self._storage.get_game(
                target_stream_id,
                timeout_minutes=self.game_config.session_timeout_minutes,
            ) if self._storage else None

            if active_game and active_game.is_active and arg != "start":
                await self._send_game_board(
                    active_game,
                    target_stream_id,
                    f"当前游戏进行中（第 {len(active_game.guesses)}/{active_game.max_attempts} 次尝试），请直接发送 5 字母单词继续猜测。",
                )
                return True, "已展示当前 Wordle 棋盘", True

            ok, msg, _ = await self._start_game(target_stream_id, target_user_id, target_user_name, force_restart=(arg == "start"))
            return ok, msg, True

        if arg == "help":
            ok, msg, _ = await self._show_help(target_stream_id)
            return ok, msg, True

        if arg in ("stat", "stats"):
            ok, msg, _ = await self._show_stats(target_stream_id, target_user_id, target_user_name)
            return ok, msg, True

        if arg == "hint":
            ok, msg, _ = await self._give_hint(target_stream_id, target_user_id, target_user_name)
            return ok, msg, True

        if arg == "stop":
            ok, msg, _ = await self._stop_game(target_stream_id, target_user_id, target_user_name)
            return ok, msg, True

        if arg == "restart":
            ok, msg, _ = await self._start_game(target_stream_id, target_user_id, target_user_name, force_restart=True)
            return ok, msg, True

        # If user typed /wordle <5-letter-word> or /guess <5-letter-word>
        if len(arg) == 5 and arg.isalpha():
            ok, msg, _ = await self._process_guess(target_stream_id, target_user_id, target_user_name, arg.upper())
            return ok, msg, True

        # Unknown argument
        err_msg = f"未知参数 '{arg}'。用法：\n/wordle start 开始游戏\n/wordle <5字母> 猜测单词\n/wordle hint 获取提示\n/wordle stop 认输\n/wordle stats 查看战绩\n/wordle help 查看帮助"
        await self.ctx.send.text(err_msg, target_stream_id)
        return False, err_msg, True

    # ----------------------------------------------------
    # Tool: wordle_game (for LLM and natural language)
    # ----------------------------------------------------
    @Tool(
        "wordle_game",
        brief_description="玩经典 Wordle 5 字母猜单词游戏，支持开局、猜词、求助提示、认输与战绩查询",
        detailed_description="""参数说明：
- action：string，必填。操作类型：'start'(开局), 'guess'(猜词), 'hint'(求助提示), 'stop'(认输), 'stat'(查战绩), 'help'(帮助)。
- word：string，可选。当 action 为 'guess' 时的 5 字母英文猜测单词。
- stream_id：string，必填。当前聊天流 ID。""",
        parameters=[
            ToolParameterInfo(
                name="action",
                param_type=ToolParamType.STRING,
                description="操作类型：start(开局), guess(猜词), hint(提示), stop(认输), stat(战绩), help(帮助)",
                required=True,
                enum_values=["start", "guess", "hint", "stop", "stat", "help"],
            ),
            ToolParameterInfo(
                name="word",
                param_type=ToolParamType.STRING,
                description="猜测的 5 字母英文单词（当 action=guess 时必填）",
                required=False,
            ),
            ToolParameterInfo(
                name="stream_id",
                param_type=ToolParamType.STRING,
                description="当前聊天流 ID",
                required=True,
            ),
        ],
    )
    async def handle_wordle_tool(
        self,
        action: str,
        stream_id: str,
        word: str = "",
        message: dict | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """LLM tool handler for Wordle game."""
        del kwargs
        if not self.is_enabled:
            return {"success": False, "content": "Wordle 插件已处于禁用状态"}

        target_stream_id = stream_id or self._extract_message_stream_id(message)
        user_id = self._extract_message_user_id(message) or "user"
        user_name = self._extract_message_user_nickname(message) or "玩家"

        if not self._is_access_allowed(message, user_id=user_id if user_id != "user" else None):
            return {"success": False, "content": "当前会话或用户未获得 Wordle 插件使用权限"}

        action_clean = action.strip().lower()
        if action_clean == "start":
            ok, msg, _ = await self._start_game(target_stream_id, user_id, user_name)
            return {"success": ok, "content": msg}

        if action_clean == "guess":
            if not word:
                return {"success": False, "content": "猜词时必须提供 5 字母的 word 参数"}
            ok, msg, _ = await self._process_guess(target_stream_id, user_id, user_name, word.upper())
            return {"success": ok, "content": msg}

        if action_clean == "hint":
            ok, msg, _ = await self._give_hint(target_stream_id, user_id, user_name)
            return {"success": ok, "content": msg}

        if action_clean == "stop":
            ok, msg, _ = await self._stop_game(target_stream_id, user_id, user_name)
            return {"success": ok, "content": msg}

        if action_clean == "stat":
            ok, msg, _ = await self._show_stats(target_stream_id, user_id, user_name)
            return {"success": ok, "content": msg}

        if action_clean == "help":
            ok, msg, _ = await self._show_help(target_stream_id)
            return {"success": ok, "content": msg}

        return {"success": False, "content": f"未知的操作类型：{action}"}

    # ==========================================
    # Internal Game Logic Helpers
    # ==========================================

    async def _start_game(
        self,
        stream_id: str,
        user_id: str,
        user_name: str,
        force_restart: bool = False,
    ) -> tuple[bool, str, int]:
        """Start a new Wordle game session."""
        g_cfg = self.game_config
        active = self._storage.get_game(stream_id, timeout_minutes=g_cfg.session_timeout_minutes) if self._storage else None
        if active and active.is_active and not force_restart:
            await self._send_game_board(
                active,
                stream_id,
                f"当前已有进行中的游戏！请直接发送 5 字母单词进行猜测，或发送 /wordle restart 重新开始。",
            )
            return True, "已有进行中游戏", 2

        # Pick random target word from CET-4/6 or full dictionary according to config
        use_cet_only = bool(getattr(g_cfg, "cet_only", False))
        pool = self._cet_words if use_cet_only and self._cet_words else self._target_words
        if not pool:
            pool = self._target_words

        target = random.choice(pool).upper()
        target_lower = target.lower()
        word_def = self._word_defs.get(target_lower, {})
        phonetic = word_def.get("phonetic", "")
        meaning = word_def.get("meaning", "")

        game = WordleGame(
            target_word=target,
            max_attempts=g_cfg.max_attempts,
            word_length=5,
            stream_id=stream_id,
            creator_id=user_id,
            creator_name=user_name,
            phonetic=phonetic,
            meaning=meaning,
        )

        if self._storage:
            self._storage.set_game(stream_id, game)

        welcome_msg = (
            "🎮 Wordle 猜单词游戏已开始！\n"
            f"目标是一个 5 字母的秘密单词，你有 {g_cfg.max_attempts} 次机会。\n"
            "👉 请直接发送 5 字母英文单词（如 CLASH 或 FIRST）进行猜测！"
        )
        await self._send_game_board(game, stream_id, welcome_msg)
        return True, "Wordle 游戏已开始", 2

    async def _process_guess(
        self,
        stream_id: str,
        user_id: str,
        user_name: str,
        word: str,
    ) -> tuple[bool, str, int]:
        """Process a submitted guess."""
        g_cfg = self.game_config
        d_cfg = self.display_config
        game = self._storage.get_game(stream_id, timeout_minutes=g_cfg.session_timeout_minutes) if self._storage else None

        if not game or not game.is_active:
            msg = "当前没有进行中的 Wordle 游戏。发送 /wordle 即可开启新游戏！"
            await self.ctx.send.text(msg, stream_id)
            return False, msg, 2

        success, message, record = game.guess(
            word,
            user_id=user_id,
            user_name=user_name,
            valid_words_set=self._valid_words,
            enforce_dictionary=g_cfg.enforce_dictionary,
        )

        if not success:
            await self.ctx.send.text(f"⚠️ {message}", stream_id)
            return False, message, 2

        # Check if game just ended
        end_text = ""
        if game.status in ("won", "lost"):
            is_win = (game.status == "won")
            if self._storage:
                self._storage.record_outcome(
                    stream_id=stream_id,
                    user_id=user_id,
                    user_name=user_name,
                    is_win=is_win,
                    attempts=len(game.guesses),
                )
                self._storage.remove_game(stream_id)

            if is_win:
                end_text = f"🎉 恭喜在第 {len(game.guesses)}/{game.max_attempts} 步猜中目标单词：{game.target_word}"
            else:
                end_text = f"💥 游戏结束！未能猜出单词，正确答案是：{game.target_word}"

            if d_cfg.show_definition:
                if game.phonetic:
                    end_text += f"\n🔊 音标：[{game.phonetic}]"
                if game.meaning:
                    end_text += f"\n📖 释义：{game.meaning}"

        await self._send_game_board(game, stream_id, end_text)
        return True, message, 2

    async def _give_hint(
        self,
        stream_id: str,
        user_id: str,
        user_name: str,
    ) -> tuple[bool, str, int]:
        """Provide a hint for the active game without markdown."""
        g_cfg = self.game_config
        if not g_cfg.allow_hints:
            msg = "当前服务器禁用了游戏提示功能。"
            await self.ctx.send.text(msg, stream_id)
            return False, msg, 2

        game = self._storage.get_game(stream_id, timeout_minutes=g_cfg.session_timeout_minutes) if self._storage else None
        if not game or not game.is_active:
            msg = "当前没有进行中的游戏，无法获取提示。发送 /wordle 开启新游戏！"
            await self.ctx.send.text(msg, stream_id)
            return False, msg, 2

        if game.hints_used >= g_cfg.max_hints_per_game:
            msg = f"本局已用完所有提示（上限 {g_cfg.max_hints_per_game} 次），请发挥你的智慧吧！"
            await self.ctx.send.text(msg, stream_id)
            return False, msg, 2

        ok, hint_msg = game.get_hint()
        clean_hint = hint_msg.replace("**", "").replace("*", "").replace("`", "")
        if self._storage:
            self._storage.set_game(stream_id, game)

        await self.ctx.send.text(clean_hint, stream_id)
        return True, clean_hint, 2

    async def _stop_game(
        self,
        stream_id: str,
        user_id: str,
        user_name: str,
    ) -> tuple[bool, str, int]:
        """Surrender or stop active game without markdown."""
        g_cfg = self.game_config
        d_cfg = self.display_config
        game = self._storage.get_game(stream_id, timeout_minutes=g_cfg.session_timeout_minutes) if self._storage else None
        if not game or not game.is_active:
            msg = "当前没有进行中的游戏。"
            await self.ctx.send.text(msg, stream_id)
            return False, msg, 2

        stop_msg = game.stop(reason="玩家投降")
        if self._storage:
            self._storage.record_outcome(
                stream_id=stream_id,
                user_id=user_id,
                user_name=user_name,
                is_win=False,
                attempts=len(game.guesses),
            )
            self._storage.remove_game(stream_id)

        reveal_text = f"🏳️ 游戏已结束（认输）。正确单词是：{game.target_word}"
        if d_cfg.show_definition:
            if game.phonetic:
                reveal_text += f"\n🔊 音标：[{game.phonetic}]"
            if game.meaning:
                reveal_text += f"\n📖 释义：{game.meaning}"

        await self._send_game_board(game, stream_id, reveal_text)
        return True, stop_msg, 2

    async def _show_stats(
        self,
        stream_id: str,
        user_id: str,
        user_name: str,
    ) -> tuple[bool, str, int]:
        """Show player stats card or plain text without markdown."""
        if not self._storage:
            return False, "存储模块未初始化", 2

        stats = self._storage.get_user_stats(user_id) if user_id else self._storage.get_stream_stats(stream_id)
        d_cfg = self.display_config

        if d_cfg.use_image_render:
            _, image_base64 = await render_stats_card(
                self.ctx,
                stats,
                user_name=user_name,
            )
            if image_base64:
                await self.ctx.send.image(image_base64, stream_id)
                return True, "已发送战绩卡片", 2

        # Text Fallback without Markdown
        text_lines = [
            f"📊 Wordle 个人战绩：{user_name}",
            f"🏆 参赛场次：{stats.played} 场",
            f"✨ 获胜胜率：{stats.win_rate:.1f}% ({stats.won}/{stats.played})",
            f"🔥 当前连胜：{stats.current_streak} 场",
            f"⭐ 最高连胜：{stats.max_streak} 场",
            f"📈 平均猜词步数：{stats.avg_guesses:.2f} 步",
            "\n🎯 猜词步数分布：",
        ]
        for i in range(1, 7):
            count = stats.guess_distribution.get(str(i), 0)
            bar = "🟩" * min(count, 10)
            text_lines.append(f"{i} 步: {bar} ({count})")
        fail_count = stats.guess_distribution.get("fail", 0)
        if fail_count > 0:
            text_lines.append(f"失败: {'⬛' * min(fail_count, 10)} ({fail_count})")

        await self.ctx.send.text("\n".join(text_lines), stream_id)
        return True, "已发送文字战绩", 2

    async def _show_help(self, stream_id: str) -> tuple[bool, str, int]:
        """Send gameplay instructions and command list without markdown."""
        help_text = (
            "🔤 Wordle 猜单词游戏指南\n"
            "--------------------------------\n"
            "🎮 基本规则：\n"
            "• 发送 /wordle 开始新一局游戏。\n"
            "• 游戏开始后，直接发送 5 个英文字母（如 CLASH 或 FIRST）即可进行猜测。\n"
            "• 共有 6 次机会，每次猜测后会提供颜色反馈：\n"
            "  🟩 绿色：字母与位置完全正确\n"
            "  🟨 黄色：字母在单词中，但位置不对\n"
            "  ⬛ 灰色：字母不在单词中\n\n"
            "⌨️ 常用指令：\n"
            "• /wordle：开启新局 / 查看当前棋盘\n"
            "• 直接发送 5 字母单词（如 right）：提交猜测\n"
            "• /wordle hint：获取首字母或词义线索\n"
            "• /wordle stop：认输并揭晓正确答案与释义\n"
            "• /wordle restart：重新开始新一局\n"
            "• /wordle stats：查看个人胜率与连胜数据\n"
            "• /wordle help：显示本帮助信息"
        )
        await self.ctx.send.text(help_text, stream_id)
        return True, "已发送帮助信息", 2

    async def _send_game_board(
        self,
        game: WordleGame,
        stream_id: str,
        text_suffix: str = "",
    ) -> None:
        """Render board via HTML2PNG or fallback to text."""
        d_cfg = self.display_config

        if d_cfg.use_image_render:
            _, image_base64 = await render_wordle_board(
                self.ctx,
                game,
            )
            if image_base64:
                await self.ctx.send.image(image_base64, stream_id)
                if text_suffix:
                    await self.ctx.send.text(text_suffix, stream_id)
                return

        # Fallback to Text / Emoji Board without markdown
        clean_text_board = game.to_text_board().replace("**", "").replace("*", "").replace("`", "")
        full_text = f"{clean_text_board}\n\n{text_suffix}" if text_suffix else clean_text_board
        await self.ctx.send.text(full_text.strip(), stream_id)

    def _extract_message_text(self, message: dict | None) -> str:
        """从消息字典中提取用户文本内容。"""
        if not isinstance(message, dict):
            return ""

        raw_message = message.get("raw_message")
        if isinstance(raw_message, list):
            parts: list[str] = []
            for item in raw_message:
                if not isinstance(item, dict):
                    continue
                data = item.get("data")
                if item.get("type") == "text" and isinstance(data, str):
                    parts.append(data)
                elif item.get("type") == "text" and isinstance(data, dict):
                    text_val = data.get("text") or data.get("content")
                    if isinstance(text_val, str):
                        parts.append(text_val)
            raw_text = "".join(parts)
            if raw_text.strip():
                return raw_text

        for key in ("processed_plain_text", "plain_text", "text", "content"):
            val = message.get(key)
            if isinstance(val, str) and val.strip():
                return val
        return ""

    def _extract_message_stream_id(self, message: dict | None) -> str:
        """从消息字典中提取会话流 stream_id / session_id / group_id / user_id。"""
        if not isinstance(message, dict):
            return ""

        for key in ("session_id", "stream_id", "chat_id", "group_id"):
            val = str(message.get(key) or "").strip()
            if val:
                return val

        message_info = message.get("message_info") or {}
        if isinstance(message_info, dict):
            for key in ("session_id", "stream_id", "chat_id", "group_id"):
                val = str(message_info.get(key) or "").strip()
                if val:
                    return val
            group_info = message_info.get("group_info")
            if isinstance(group_info, dict):
                gid = str(group_info.get("group_id") or "").strip()
                if gid:
                    return gid
            user_info = message_info.get("user_info")
            if isinstance(user_info, dict):
                uid = str(user_info.get("user_id") or "").strip()
                if uid:
                    return uid
        return ""

    def _extract_message_user_id(self, message: dict | None) -> str:
        """从消息字典中提取用户 ID。"""
        if not isinstance(message, dict):
            return ""
        message_info = message.get("message_info") or {}
        if not isinstance(message_info, dict):
            message_info = {}
        user_info = message_info.get("user_info") or message.get("user_info") or {}
        if not isinstance(user_info, dict):
            user_info = {}
        for obj, key in (
            (user_info, "user_id"),
            (user_info, "sender_id"),
            (message, "user_id"),
            (message, "sender_id"),
        ):
            val = str(obj.get(key) or "").strip()
            if val:
                return val
        return ""

    def _extract_message_user_nickname(self, message: dict | None) -> str:
        """从消息字典中提取用户昵称或名片。"""
        if not isinstance(message, dict):
            return ""
        message_info = message.get("message_info") or {}
        if not isinstance(message_info, dict):
            message_info = {}
        user_info = message_info.get("user_info") or message.get("user_info") or {}
        if not isinstance(user_info, dict):
            user_info = {}

        for obj, key in (
            (user_info, "user_nickname"),
            (user_info, "nickname"),
            (user_info, "user_cardname"),
            (user_info, "name"),
            (message, "user_nickname"),
            (message, "nickname"),
            (message, "sender_nickname"),
            (message, "user_cardname"),
            (message, "name"),
        ):
            val = str(obj.get(key) or "").strip()
            if val:
                return val
        return ""

    def _extract_stream_and_user(self, kwargs: dict[str, Any]) -> tuple[str, str, str]:
        """安全提取 stream_id, user_id, user_name。"""
        message = kwargs.get("message")
        msg_dict = message if isinstance(message, dict) else None

        stream_id = str(kwargs.get("stream_id") or "") or self._extract_message_stream_id(msg_dict)
        user_id = str(kwargs.get("user_id") or kwargs.get("sender_id") or "") or self._extract_message_user_id(msg_dict) or "user"
        user_name = str(kwargs.get("user_name") or kwargs.get("user_nickname") or kwargs.get("nickname") or "") or self._extract_message_user_nickname(msg_dict) or "玩家"

        return stream_id, user_id, user_name

    @staticmethod
    def _match_access_mode(
        mode: str, value: str | None, whitelist: list[str], blacklist: list[str]
    ) -> bool:
        """按 mode 判定单个维度是否放行。

        value 为 None（如私聊消息取不到 group_id）时该维度不参与判定，直接放行。
        whitelist 模式下名单为空表示全部拒绝。
        """
        if mode == "off":
            return True
        if value is None:
            return True
        if mode == "whitelist":
            return value in {str(item).strip() for item in whitelist}
        if mode == "blacklist":
            return value not in {str(item).strip() for item in blacklist}
        # 非法 mode（配置绕过校验时）按不限制处理，避免整个插件静默失效
        return True

    def _extract_message_group_id(self, message: dict | None) -> str | None:
        """从消息字典中提取群 ID（私聊消息返回 None）。"""
        if not isinstance(message, dict):
            return None

        message_info = message.get("message_info")
        if isinstance(message_info, dict):
            group_info = message_info.get("group_info")
            if isinstance(group_info, dict):
                gid = group_info.get("group_id")
                if gid is not None and str(gid).strip():
                    return str(gid).strip()
            elif group_info is None and "group_info" in message_info:
                # 明确标记为私聊（group_info 为 None）
                return None

        # 兜底：检查外层 group_id
        gid = message.get("group_id")
        if gid is not None and str(gid).strip():
            return str(gid).strip()

        return None

    def _is_access_allowed(
        self,
        message: dict | None = None,
        group_id: str | None = None,
        user_id: str | None = None,
    ) -> bool:
        """群维度与用户维度都通过才允许使用（AND 关系）。"""
        access = self.access_config

        if group_id is None and isinstance(message, dict):
            group_id = self._extract_message_group_id(message)
        if user_id is None and isinstance(message, dict):
            uid = self._extract_message_user_id(message)
            if uid and uid != "user":
                user_id = uid

        if not self._match_access_mode(
            access.group_mode, group_id, access.group_whitelist, access.group_blacklist
        ):
            try:
                self.ctx.logger.debug(
                    "Wordle 访问控制拦截：群 %s 未通过 group_mode=%s", group_id, access.group_mode
                )
            except Exception:
                logger.debug("Wordle 访问控制拦截：群 %s 未通过 group_mode=%s", group_id, access.group_mode)
            return False

        if not self._match_access_mode(
            access.user_mode, user_id, access.user_whitelist, access.user_blacklist
        ):
            try:
                self.ctx.logger.debug(
                    "Wordle 访问控制拦截：用户 %s 未通过 user_mode=%s", user_id, access.user_mode
                )
            except Exception:
                logger.debug("Wordle 访问控制拦截：用户 %s 未通过 user_mode=%s", user_id, access.user_mode)
            return False

        return True


def create_plugin() -> WordlePlugin:
    """Plugin factory function required by MaiBot."""
    return WordlePlugin()
