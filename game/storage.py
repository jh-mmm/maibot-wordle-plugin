"""Persistent storage and session management for Wordle."""

from __future__ import annotations

import json
import logging
import os
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Optional

from .logic import WordleGame

logger = logging.getLogger(__name__)


@dataclass
class PlayerStats:
    """Player or stream gameplay statistics."""
    id: str  # user_id or stream_id
    name: str = ""
    played: int = 0
    won: int = 0
    current_streak: int = 0
    max_streak: int = 0
    guess_distribution: dict[str, int] = field(default_factory=lambda: {
        "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "fail": 0
    })
    last_played: float = 0.0

    @property
    def win_rate(self) -> float:
        if self.played <= 0:
            return 0.0
        return (self.won / self.played) * 100.0

    @property
    def avg_guesses(self) -> float:
        total_wins = self.won
        if total_wins <= 0:
            return 0.0
        total_guesses = sum(int(k) * v for k, v in self.guess_distribution.items() if k != "fail")
        return total_guesses / total_wins

    def record_game(self, is_win: bool, attempts: int, name: str = "") -> None:
        """Record the outcome of a game."""
        self.played += 1
        self.last_played = time.time()
        if name:
            self.name = name

        if is_win:
            self.won += 1
            self.current_streak += 1
            if self.current_streak > self.max_streak:
                self.max_streak = self.current_streak
            key = str(min(max(1, attempts), 6))
            self.guess_distribution[key] = self.guess_distribution.get(key, 0) + 1
        else:
            self.current_streak = 0
            self.guess_distribution["fail"] = self.guess_distribution.get("fail", 0) + 1

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> PlayerStats:
        stats = cls(id=data["id"], name=data.get("name", ""))
        stats.played = data.get("played", 0)
        stats.won = data.get("won", 0)
        stats.current_streak = data.get("current_streak", 0)
        stats.max_streak = data.get("max_streak", 0)
        stats.guess_distribution = data.get("guess_distribution", {
            "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "fail": 0
        })
        stats.last_played = data.get("last_played", 0.0)
        return stats


class GameStorage:
    """Manages active games and user stats on disk."""

    def __init__(self, data_dir: Optional[Path] = None) -> None:
        self.data_dir = data_dir or Path("data/storage")
        self._ensure_dir()

        self._active_games: dict[str, WordleGame] = {}
        self._user_stats: dict[str, PlayerStats] = {}
        self._stream_stats: dict[str, PlayerStats] = {}

        self._load_all()

    def _ensure_dir(self) -> None:
        try:
            self.data_dir.mkdir(parents=True, exist_ok=True)
        except Exception as exc:
            logger.warning("Failed to create data dir: %s", exc)

    @property
    def _active_games_file(self) -> Path:
        return self.data_dir / "active_games.json"

    @property
    def _user_stats_file(self) -> Path:
        return self.data_dir / "user_stats.json"

    @property
    def _stream_stats_file(self) -> Path:
        return self.data_dir / "stream_stats.json"

    def _load_all(self) -> None:
        # Load active games
        if self._active_games_file.exists():
            try:
                with open(self._active_games_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for sid, gdata in data.items():
                        game = WordleGame.from_dict(gdata)
                        if game.is_active:
                            self._active_games[sid] = game
            except Exception as exc:
                logger.error("Failed to load active games: %s", exc)

        # Load user stats
        if self._user_stats_file.exists():
            try:
                with open(self._user_stats_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for uid, udata in data.items():
                        self._user_stats[uid] = PlayerStats.from_dict(udata)
            except Exception as exc:
                logger.error("Failed to load user stats: %s", exc)

        # Load stream stats
        if self._stream_stats_file.exists():
            try:
                with open(self._stream_stats_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for sid, sdata in data.items():
                        self._stream_stats[sid] = PlayerStats.from_dict(sdata)
            except Exception as exc:
                logger.error("Failed to load stream stats: %s", exc)

    def _save_active_games(self) -> None:
        try:
            self._ensure_dir()
            data = {
                sid: g.to_dict()
                for sid, g in self._active_games.items()
                if g.is_active
            }
            with open(self._active_games_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as exc:
            logger.error("Failed to save active games: %s", exc)

    def _save_user_stats(self) -> None:
        try:
            self._ensure_dir()
            data = {uid: s.to_dict() for uid, s in self._user_stats.items()}
            with open(self._user_stats_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as exc:
            logger.error("Failed to save user stats: %s", exc)

    def _save_stream_stats(self) -> None:
        try:
            self._ensure_dir()
            data = {sid: s.to_dict() for sid, s in self._stream_stats.items()}
            with open(self._stream_stats_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as exc:
            logger.error("Failed to save stream stats: %s", exc)

    def get_game(self, stream_id: str, timeout_minutes: int = 15) -> Optional[WordleGame]:
        """Get the active game for a stream, automatically expiring if timed out."""
        if not stream_id:
            return None

        game = self._active_games.get(stream_id)
        if game is None:
            return None

        if not game.is_active:
            self._active_games.pop(stream_id, None)
            self._save_active_games()
            return None

        # Check timeout
        if timeout_minutes > 0:
            last_activity = game.start_time
            if game.guesses:
                last_activity = game.guesses[-1].timestamp
            if time.time() - last_activity > timeout_minutes * 60:
                game.stop(reason="超时自动结算")
                self._active_games.pop(stream_id, None)
                self._save_active_games()
                return None

        return game

    def set_game(self, stream_id: str, game: WordleGame) -> None:
        """Store or update an active game."""
        if not stream_id:
            return
        if game.is_active:
            self._active_games[stream_id] = game
        else:
            self._active_games.pop(stream_id, None)
        self._save_active_games()

    def remove_game(self, stream_id: str) -> Optional[WordleGame]:
        """Remove and return active game for a stream."""
        game = self._active_games.pop(stream_id, None)
        self._save_active_games()
        return game

    def record_outcome(
        self,
        stream_id: str,
        user_id: str,
        user_name: str,
        is_win: bool,
        attempts: int,
    ) -> None:
        """Record game results for user and chat stream."""
        if user_id:
            if user_id not in self._user_stats:
                self._user_stats[user_id] = PlayerStats(id=user_id, name=user_name)
            self._user_stats[user_id].record_game(is_win, attempts, name=user_name)
            self._save_user_stats()

        if stream_id:
            if stream_id not in self._stream_stats:
                self._stream_stats[stream_id] = PlayerStats(id=stream_id, name=f"Chat {stream_id}")
            self._stream_stats[stream_id].record_game(is_win, attempts)
            self._save_stream_stats()

    def get_user_stats(self, user_id: str) -> PlayerStats:
        """Get stats for a user (or return fresh instance)."""
        return self._user_stats.get(user_id, PlayerStats(id=user_id))

    def get_stream_stats(self, stream_id: str) -> PlayerStats:
        """Get stats for a stream."""
        return self._stream_stats.get(stream_id, PlayerStats(id=stream_id))

    def get_leaderboard(self, limit: int = 10) -> list[PlayerStats]:
        """Get top players sorted by wins and win rate."""
        valid_players = [p for p in self._user_stats.values() if p.played > 0]
        return sorted(
            valid_players,
            key=lambda x: (x.won, x.win_rate, x.max_streak),
            reverse=True,
        )[:limit]
