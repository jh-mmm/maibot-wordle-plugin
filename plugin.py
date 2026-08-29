"""Wordle Game Plugin for MaiBot.

A minimalist, high-contrast 5-letter Wordle guessing game with rich HTML-to-PNG board rendering,
built-in phonetic and Chinese definitions, hints, and player statistics.
"""

import logging
import random
import sys
import time
from pathlib import Path
from typing import Any, Optional

_PLUGIN_DIR = str(Path(__file__).resolve().parent)
if _PLUGIN_DIR not in sys.path:
    sys.path.insert(0, _PLUGIN_DIR)

try:
    from maibot_sdk import (
        CONFIG_RELOAD_SCOPE_SELF,
        Command,
        Field,
        MaiBotPlugin,
        PluginConfigBase,
        Tool,
    )
    from maibot_sdk.types import ToolParameterInfo, ToolParamType
except ImportError:
    # Local fallback for standalone environments
    CONFIG_RELOAD_SCOPE_SELF = "self"

    def Command(*args: Any, **kwargs: Any):
        return lambda func: func

    def Tool(*args: Any, **kwargs: Any):
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


from data.words_target import TARGET_WORDS, WORD_DEFINITIONS
from data.words_valid import VALID_WORDS
from game.logic import LetterState, WordleGame
from game.storage import GameStorage, PlayerStats
from ui.renderer import render_stats_card, render_wordle_board

logger = logging.getLogger(__name__)


# ==========================================
# Configuration Models
# ==========================================

class GameSection(PluginConfigBase):
    """Wordle 游戏设置"""
    __ui_label__ = "游戏设置"
    __ui_icon__ = "sports_esports"
    __ui_order__ = 0

    max_attempts: int = Field(default=6, description="最大猜测次数 (默认 6)")
    word_length: int = Field(default=5, description="单词长度 (默认 5 字母)")
    enforce_dictionary: bool = Field(default=True, description="是否要求猜测必须是有效英文单词")
    allow_hints: bool = Field(default=True, description="是否允许获取游戏提示")
    max_hints_per_game: int = Field(default=2, description="每局最多允许获取提示次数")
    session_timeout_minutes: int = Field(default=15, description="未操作超时自动结算时间 (分钟)")


class DisplaySection(PluginConfigBase):
    """Wordle 展示设置"""
    __ui_label__ = "展示设置"
    __ui_icon__ = "palette"
    __ui_order__ = 1

    use_image_render: bool = Field(default=True, description="是否优先使用 HTML 转图片卡片展示")
    show_definition: bool = Field(default=True, description="游戏结束时是否显示中文释义与音标")


class PluginMetaSection(PluginConfigBase):
    """插件元信息"""
    __ui_label__ = "基础信息"
    __ui_order__ = 2

    config_version: str = Field(default="1.0.0", description="配置文件版本")


class WordleConfig(PluginConfigBase):
    """Wordle 插件完整配置"""
    plugin: PluginMetaSection = Field(default_factory=PluginMetaSection)
    game: GameSection = Field(default_factory=GameSection)
    display: DisplaySection = Field(default_factory=DisplaySection)


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
        self._word_defs: dict[str, dict[str, str]] = WORD_DEFINITIONS
        self._valid_words: set[str] = VALID_WORDS

    @property
    def current_config(self) -> WordleConfig:
        try:
            cfg = self.config
            if cfg is not None:
                return cfg
        except Exception:
            pass
        return self._fallback_config

    async def on_load(self) -> None:
        """Plugin initialization on load."""
        data_dir = None
        if hasattr(self.ctx, "paths") and hasattr(self.ctx.paths, "data_dir"):
            data_dir = Path(self.ctx.paths.data_dir)

        self._storage = GameStorage(data_dir=data_dir)
        self.ctx.logger.info(
            "Wordle 插件加载成功！已载入 %d 个目标词和 %d 个合法单词。",
            len(self._target_words),
            len(self._valid_words),
        )

    async def on_unload(self) -> None:
        """Plugin unload cleanup."""
        self.ctx.logger.info("Wordle 插件已卸载。")

    async def on_config_update(self, scope: str, config_data: dict, version: str) -> None:
        """Callback when configuration is reloaded."""
        if scope in (CONFIG_RELOAD_SCOPE_SELF, "self"):
            self.ctx.logger.info("Wordle 插件配置已热更新 (version=%s)", version)

    # ----------------------------------------------------
    # Command 1: Direct 5-letter word guess in chat
    # Matches: ^[a-zA-Z]{5}$ or ^(?:/w\s+|/guess\s+|/g\s+)[a-zA-Z]{5}$
    # Only intercepts when there is an active game in stream
    # ----------------------------------------------------
    @Command(
        "wordle_direct_guess",
        pattern=r"^(?:/(?:w|guess|g)\s+)?(?P<word>[a-zA-Z]{5})$",
        description="直接发送5字母英文单词进行Wordle猜测",
    )
    async def handle_direct_guess(self, **kwargs) -> tuple[bool, str, int]:
        stream_id, user_id, user_name = self._extract_stream_and_user(kwargs)
        if not stream_id:
            return False, "", 0

        # Check if there is an active game in current stream
        cfg = self.current_config
        game = self._storage.get_game(stream_id, timeout_minutes=cfg.game.session_timeout_minutes) if self._storage else None
        if not game or not game.is_active:
            # No active game -> do not intercept ordinary chat words
            return False, "", 0

        matched = kwargs.get("matched_groups", {}) or {}
        word = (matched.get("word") or "").strip().upper()
        if not word or len(word) != 5:
            return False, "", 0

        ok, msg, _ = await self._process_guess(stream_id, user_id, user_name, word)
        # Return intercept level 2 to completely suppress downstream AI/LLM replies
        return ok, msg, 2

    # ----------------------------------------------------
    # Command 2: Main /wordle command
    # Matches: ^/wordle(?:\s+(?P<arg>.+))?$
    # ----------------------------------------------------
    @Command(
        "wordle_main",
        pattern=r"^/wordle(?:\s+(?P<arg>\S+))?$",
        description="Wordle 猜单词主命令，支持开局、提示、认输、重开与战绩",
    )
    async def handle_wordle_main(self, **kwargs) -> tuple[bool, str, int]:
        """Main /wordle command handler."""
        stream_id, user_id, user_name = self._extract_stream_and_user(kwargs)
        if not stream_id:
            return False, "缺少聊天流 stream_id", 2

        matched = kwargs.get("matched_groups", {}) or {}
        arg = (matched.get("arg") or "").strip().lower()

        if not arg or arg in ("start", "开始"):
            # Start game or show current board
            active_game = self._storage.get_game(
                stream_id,
                timeout_minutes=self.current_config.game.session_timeout_minutes,
            ) if self._storage else None

            if active_game and active_game.is_active and arg != "start":
                await self._send_game_board(
                    active_game,
                    stream_id,
                    f"当前游戏进行中（第 {len(active_game.guesses)}/{active_game.max_attempts} 次尝试），请直接发送 5 字母单词继续猜测。",
                )
                return True, "已展示当前 Wordle 棋盘", 2

            return await self._start_game(stream_id, user_id, user_name, force_restart=(arg == "start"))

        if arg in ("help", "帮助"):
            return await self._show_help(stream_id)

        if arg in ("stat", "stats", "战绩", "统计"):
            return await self._show_stats(stream_id, user_id, user_name)

        if arg in ("hint", "提示"):
            return await self._give_hint(stream_id, user_id, user_name)

        if arg in ("stop", "结束", "投降"):
            return await self._stop_game(stream_id, user_id, user_name)

        if arg in ("restart", "重开"):
            return await self._start_game(stream_id, user_id, user_name, force_restart=True)

        # If user typed /wordle <5-letter-word>
        if len(arg) == 5 and arg.isalpha():
            return await self._process_guess(stream_id, user_id, user_name, arg.upper())

        # Unknown argument
        err_msg = f"未知参数 '{arg}'。用法：\n直接发送 5 字母单词进行猜测\n/wordle hint 获取提示\n/wordle stop 认输\n/wordle help 查看帮助"
        await self.ctx.send.text(err_msg, stream_id)
        return False, err_msg, 2

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
    async def handle_wordle_tool(self, action: str, stream_id: str, word: str = "", **kwargs) -> dict[str, Any]:
        """LLM tool handler for Wordle game."""
        user_id = str(kwargs.get("user_id") or kwargs.get("sender_id") or "user")
        user_name = str(kwargs.get("user_name") or kwargs.get("nickname") or "玩家")

        action_clean = action.strip().lower()
        if action_clean == "start":
            ok, msg, _ = await self._start_game(stream_id, user_id, user_name)
            return {"success": ok, "message": msg}

        if action_clean == "guess":
            if not word:
                return {"success": False, "message": "猜词时必须提供 5 字母的 word 参数"}
            ok, msg, _ = await self._process_guess(stream_id, user_id, user_name, word.upper())
            return {"success": ok, "message": msg}

        if action_clean == "hint":
            ok, msg, _ = await self._give_hint(stream_id, user_id, user_name)
            return {"success": ok, "message": msg}

        if action_clean == "stop":
            ok, msg, _ = await self._stop_game(stream_id, user_id, user_name)
            return {"success": ok, "message": msg}

        if action_clean == "stat":
            ok, msg, _ = await self._show_stats(stream_id, user_id, user_name)
            return {"success": ok, "message": msg}

        if action_clean == "help":
            ok, msg, _ = await self._show_help(stream_id)
            return {"success": ok, "message": msg}

        return {"success": False, "message": f"未知的操作类型：{action}"}

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
        cfg = self.current_config
        active = self._storage.get_game(stream_id, timeout_minutes=cfg.game.session_timeout_minutes) if self._storage else None
        if active and active.is_active and not force_restart:
            await self._send_game_board(
                active,
                stream_id,
                f"当前已有进行中的游戏！请直接发送 5 字母单词进行猜测，或发送 /wordle restart 重新开始。",
            )
            return True, "已有进行中游戏", 2

        # Pick random target word
        target = random.choice(self._target_words).upper()
        target_lower = target.lower()
        word_def = self._word_defs.get(target_lower, {})
        phonetic = word_def.get("phonetic", "")
        meaning = word_def.get("meaning", "")

        game = WordleGame(
            target_word=target,
            max_attempts=cfg.game.max_attempts,
            word_length=cfg.game.word_length,
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
            f"目标是一个 {cfg.game.word_length} 字母的秘密单词，你有 {cfg.game.max_attempts} 次机会。\n"
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
        cfg = self.current_config
        game = self._storage.get_game(stream_id, timeout_minutes=cfg.game.session_timeout_minutes) if self._storage else None

        if not game or not game.is_active:
            msg = "当前没有进行中的 Wordle 游戏。发送 /wordle 即可开启新游戏！"
            await self.ctx.send.text(msg, stream_id)
            return False, msg, 2

        success, message, record = game.guess(
            word,
            user_id=user_id,
            user_name=user_name,
            valid_words_set=self._valid_words,
            enforce_dictionary=cfg.game.enforce_dictionary,
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

            if cfg.display.show_definition:
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
        cfg = self.current_config
        if not cfg.game.allow_hints:
            msg = "当前服务器禁用了游戏提示功能。"
            await self.ctx.send.text(msg, stream_id)
            return False, msg, 2

        game = self._storage.get_game(stream_id, timeout_minutes=cfg.game.session_timeout_minutes) if self._storage else None
        if not game or not game.is_active:
            msg = "当前没有进行中的游戏，无法获取提示。发送 /wordle 开启新游戏！"
            await self.ctx.send.text(msg, stream_id)
            return False, msg, 2

        if game.hints_used >= cfg.game.max_hints_per_game:
            msg = f"本局已用完所有提示（上限 {cfg.game.max_hints_per_game} 次），请发挥你的智慧吧！"
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
        cfg = self.current_config
        game = self._storage.get_game(stream_id, timeout_minutes=cfg.game.session_timeout_minutes) if self._storage else None
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
        if cfg.display.show_definition:
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
        cfg = self.current_config

        if cfg.display.use_image_render:
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
            "• /wordle ：开启新局 / 查看当前棋盘\n"
            "• 直接发送 5 字母单词（如 right）：提交猜测\n"
            "• /wordle hint（或 /wordle 提示）：获取首字母或词义线索\n"
            "• /wordle stop（或 /wordle 投降）：认输并揭晓正确答案与释义\n"
            "• /wordle restart（或 /wordle 重开）：重新开始新一局\n"
            "• /wordle stat（或 /wordle 战绩）：查看个人胜率与连胜数据\n"
            "• /wordle help（或 /wordle 帮助）：显示本帮助信息"
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
        cfg = self.current_config

        if cfg.display.use_image_render:
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

    def _extract_stream_and_user(self, kwargs: dict[str, Any]) -> tuple[str, str, str]:
        """Extract stream_id, user_id, user_name safely from kwargs."""
        stream_id = str(kwargs.get("stream_id") or "")
        message = kwargs.get("message") or {}
        if isinstance(message, dict):
            user_info = message.get("user_info") or {}
            user_id = str(user_info.get("user_id") or message.get("sender_id") or message.get("user_id") or "")
            user_name = str(
                user_info.get("user_nickname")
                or user_info.get("nickname")
                or message.get("sender_nickname")
                or message.get("nickname")
                or user_id
                or "Player"
            )
        else:
            user_id = str(kwargs.get("user_id") or "")
            user_name = str(kwargs.get("user_name") or user_id or "Player")

        return stream_id, user_id, user_name


def create_plugin() -> WordlePlugin:
    """Plugin factory function required by MaiBot."""
    return WordlePlugin()
