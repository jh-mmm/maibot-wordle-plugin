"""HTML template rendering and image generation for Wordle.

Clean, high-contrast, minimalist 6x5 matrix without virtual keyboard.
Colors:
- Green (Correct): Original classic Wordle green (#4b7e47)
- Yellow (Present): Current vibrant golden yellow (#eab308)
- Gray (Absent): Neutral dark slate (#3a3a3c)
- Empty (Unfilled): Dark Zinc (#18181b, border #27272a)
"""

from __future__ import annotations

import base64
import html
import inspect
import logging
import sys
from pathlib import Path
from typing import Any, Optional

_PLUGIN_DIR = str(Path(__file__).resolve().parent.parent)
if _PLUGIN_DIR not in sys.path:
    sys.path.insert(0, _PLUGIN_DIR)

from game.logic import LetterState, WordleGame
from game.storage import PlayerStats

logger = logging.getLogger(__name__)

# Color Palette
COLOR_CORRECT = "#4b7e47"   # Original classic green (绿)
COLOR_PRESENT = "#eab308"   # Current bright golden yellow (黄)
COLOR_ABSENT  = "#3a3a3c"   # Neutral dark slate (灰)
COLOR_EMPTY   = "#18181b"   # Dark Zinc (空方块背景)
COLOR_EMPTY_BORDER = "#27272a"  # 空方块边框


def build_wordle_html(game: WordleGame) -> str:
    """Build minimalist 6x5 Wordle board HTML."""
    rows_html = []
    for row_idx in range(game.max_attempts):
        if row_idx < len(game.guesses):
            guess_rec = game.guesses[row_idx]
            tiles_html = []
            for char, st in zip(guess_rec.word, guess_rec.states):
                cls_name = "tile-absent"
                if st == LetterState.CORRECT.value:
                    cls_name = "tile-correct"
                elif st == LetterState.PRESENT.value:
                    cls_name = "tile-present"

                tiles_html.append(
                    f'<div class="tile {cls_name}">{html.escape(char)}</div>'
                )
            rows_html.append(f'<div class="board-row">{"".join(tiles_html)}</div>')
        else:
            # Empty Row
            tiles_html = [
                '<div class="tile tile-empty"></div>'
                for _ in range(game.word_length)
            ]
            rows_html.append(f'<div class="board-row">{"".join(tiles_html)}</div>')

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<style>
* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}
body {{
    background: #09090b;
    display: inline-block;
    padding: 24px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}}
.board {{
    background-color: #121215;
    border: 1px solid #27272a;
    border-radius: 22px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.65);
}}
.board-row {{
    display: flex;
    gap: 12px;
}}
.tile {{
    width: 76px;
    height: 76px;
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 38px;
    font-weight: 800;
    text-transform: uppercase;
    color: #ffffff;
    user-select: none;
}}
.tile-absent {{
    background-color: {COLOR_ABSENT};
}}
.tile-present {{
    background-color: {COLOR_PRESENT};
}}
.tile-correct {{
    background-color: {COLOR_CORRECT};
}}
.tile-empty {{
    background-color: {COLOR_EMPTY};
    border: 1.5px solid {COLOR_EMPTY_BORDER};
}}
</style>
</head>
<body>
<div class="board">
    {"".join(rows_html)}
</div>
</body>
</html>
"""


def build_stats_html(stats: PlayerStats, user_name: str = "") -> str:
    """Build responsive HTML string for Wordle player statistics card."""
    display_name = user_name or stats.name or f"Player {stats.id}"

    counts = [stats.guess_distribution.get(str(i), 0) for i in range(1, 7)]
    max_count = max(counts + [1])

    dist_rows_html = []
    for i in range(1, 7):
        count = stats.guess_distribution.get(str(i), 0)
        percentage = max(8, int((count / max_count) * 100)) if count > 0 else 0
        fill_html = (
            f'<div class="dist-bar" style="width: {percentage}%; background-color: {COLOR_CORRECT};">{count}</div>'
            if count > 0
            else f'<div class="dist-bar-zero">0</div>'
        )
        dist_rows_html.append(
            f'<div class="dist-row">'
            f'<div class="dist-num">{i}</div>'
            f'<div class="dist-track">{fill_html}</div>'
            f'</div>'
        )

    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<style>
* {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}}
body {{
    background: #09090b;
    display: inline-block;
    padding: 24px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #ffffff;
}}
.card {{
    width: 480px;
    background-color: #121215;
    border: 1px solid #27272a;
    border-radius: 22px;
    padding: 28px 24px;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.65);
}}
.header {{
    text-align: center;
    margin-bottom: 24px;
    border-bottom: 1.5px solid #27272a;
    padding-bottom: 16px;
}}
.title {{
    font-size: 24px;
    font-weight: 800;
    letter-spacing: 2px;
}}
.player-name {{
    font-size: 14px;
    color: #a0a0a5;
    margin-top: 4px;
}}
.stats-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-bottom: 24px;
}}
.stat-box {{
    background-color: #18181b;
    border: 1px solid #27272a;
    border-radius: 12px;
    padding: 14px 6px;
    text-align: center;
}}
.stat-value {{
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
}}
.stat-label {{
    font-size: 12px;
    color: #a0a0a5;
    margin-top: 4px;
}}
.dist-section {{
    width: 100%;
}}
.section-title {{
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 12px;
    color: #ffffff;
}}
.dist-container {{
    display: flex;
    flex-direction: column;
    gap: 8px;
}}
.dist-row {{
    display: flex;
    align-items: center;
    gap: 10px;
}}
.dist-num {{
    width: 16px;
    font-size: 14px;
    font-weight: 700;
    color: #a0a0a5;
    text-align: right;
}}
.dist-track {{
    flex: 1;
    height: 24px;
    background-color: #18181b;
    border-radius: 6px;
    display: flex;
    align-items: center;
    overflow: hidden;
}}
.dist-bar {{
    height: 100%;
    border-radius: 6px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    padding-right: 8px;
    font-size: 12px;
    font-weight: 700;
    color: #ffffff;
}}
.dist-bar-zero {{
    padding-left: 8px;
    font-size: 12px;
    color: #a0a0a5;
}}
</style>
</head>
<body>
<div class="card">
    <div class="header">
        <div class="title">WORDLE 战绩统计</div>
        <div class="player-name">{html.escape(display_name)}</div>
    </div>

    <div class="stats-grid">
        <div class="stat-box">
            <div class="stat-value">{stats.played}</div>
            <div class="stat-label">已参赛</div>
        </div>
        <div class="stat-box">
            <div class="stat-value">{stats.win_rate:.0f}%</div>
            <div class="stat-label">胜率</div>
        </div>
        <div class="stat-box">
            <div class="stat-value">{stats.current_streak}</div>
            <div class="stat-label">当前连胜</div>
        </div>
        <div class="stat-box">
            <div class="stat-value">{stats.max_streak}</div>
            <div class="stat-label">最高连胜</div>
        </div>
    </div>

    <div class="dist-section">
        <div class="section-title">猜词步数分布 (Guess Distribution)</div>
        <div class="dist-container">
            {"".join(dist_rows_html)}
        </div>
    </div>
</div>
</body>
</html>
"""


async def render_wordle_board(
    ctx: Any,
    game: WordleGame,
) -> tuple[str, Optional[str]]:
    """
    Render Wordle game board HTML to PNG image using ctx.render.html2png.

    Returns:
        tuple[html_string: str, image_base64: Optional[str]]
    """
    html_doc = build_wordle_html(game)
    image_base64 = await _try_html2png(
        ctx,
        html_doc,
        selector=".board",
        viewport={"width": 500, "height": 600},
    )
    return html_doc, image_base64


async def render_stats_card(
    ctx: Any,
    stats: PlayerStats,
    user_name: str = "",
) -> tuple[str, Optional[str]]:
    """
    Render Player Stats HTML to PNG image using ctx.render.html2png.

    Returns:
        tuple[html_string: str, image_base64: Optional[str]]
    """
    html_doc = build_stats_html(stats, user_name=user_name)
    image_base64 = await _try_html2png(
        ctx,
        html_doc,
        selector=".card",
        viewport={"width": 520, "height": 520},
    )
    return html_doc, image_base64


async def _try_html2png(
    ctx: Any,
    html_content: str,
    selector: str = ".board",
    viewport: Optional[dict[str, int]] = None,
) -> Optional[str]:
    """Helper to call ctx.render.html2png and extract base64 string safely."""
    if ctx is None:
        return None

    renderer = getattr(ctx, "render", None)
    if renderer is None:
        return None

    html2png = getattr(renderer, "html2png", None)
    if not callable(html2png):
        return None

    try:
        if inspect.iscoroutinefunction(html2png) or inspect.isawaitable(html2png):
            result = await html2png(
                html_content,
                selector=selector,
                viewport=viewport or {"width": 500, "height": 600},
                device_scale_factor=2.0,
                full_page=False,
            )
        else:
            raw = html2png(
                html_content,
                selector=selector,
                viewport=viewport or {"width": 500, "height": 600},
                device_scale_factor=2.0,
                full_page=False,
            )
            result = await raw if inspect.isawaitable(raw) else raw

        return _extract_image_base64(result)
    except Exception as exc:
        logger.warning("html2png rendering failed or not supported: %s", exc)
        return None


def _extract_image_base64(image_result: Any) -> Optional[str]:
    """Extract clean base64 image string from varying SDK return types."""
    if not image_result:
        return None

    if isinstance(image_result, bytes):
        return base64.b64encode(image_result).decode("utf-8")

    if isinstance(image_result, dict):
        for key in ("image_base64", "base64", "data", "content", "result"):
            val = image_result.get(key)
            if isinstance(val, str) and val.strip():
                return _strip_data_url(val)
            if isinstance(val, bytes):
                return base64.b64encode(val).decode("utf-8")

        for key in ("path", "file_path", "filename"):
            val = image_result.get(key)
            if isinstance(val, str) and val.strip():
                p = Path(val)
                if p.exists() and p.is_file():
                    return base64.b64encode(p.read_bytes()).decode("utf-8")
        return None

    if isinstance(image_result, str):
        val = image_result.strip()
        if val.startswith("data:image/"):
            return _strip_data_url(val)
        if len(val) > 64 and not val.startswith("<"):
            return val

    return None


def _strip_data_url(value: str) -> str:
    if "," in value and value.lstrip().startswith("data:image/"):
        return value.split(",", 1)[1].strip()
    return value.strip()
