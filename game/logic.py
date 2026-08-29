"""Wordle game logic and state engine."""

from __future__ import annotations

import random
import time
from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any, Optional


class LetterState(str, Enum):
    """Wordle letter feedback state."""
    CORRECT = "correct"    # 🟩 Green: Letter in correct position
    PRESENT = "present"    # 🟨 Yellow: Letter in word, wrong position
    ABSENT = "absent"      # ⬛ / ⬜ Gray: Letter not in word or matched out
    UNUSED = "unused"      # Keyboard key not pressed yet
    EMPTY = "empty"        # Grid box not filled yet


STATE_EMOJI_MAP = {
    LetterState.CORRECT: "🟩",
    LetterState.PRESENT: "🟨",
    LetterState.ABSENT: "⬛",
    LetterState.EMPTY: "⬜",
}


@dataclass
class GuessRecord:
    """A single guess attempt and its outcome."""
    word: str
    states: list[str]  # "correct", "present", "absent"
    user_id: str = ""
    user_name: str = ""
    timestamp: float = field(default_factory=time.time)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GuessRecord:
        return cls(**data)


def evaluate_guess(target_word: str, guess_word: str) -> list[str]:
    """
    Evaluate a 5-letter guess against the target word according to standard Wordle rules.

    Two-pass evaluation:
    1. First pass: Identify all exact matches (Green / CORRECT).
       Count remaining unmatched target letters.
    2. Second pass: For remaining non-exact letters, check if letter exists in
       unmatched pool. If yes, mark Yellow / PRESENT and decrement available count.
       Otherwise mark Gray / ABSENT.
    """
    target = target_word.strip().upper()
    guess = guess_word.strip().upper()
    length = len(target)

    result: list[str] = [LetterState.ABSENT.value] * length
    unmatched_counts: dict[str, int] = {}

    # Pass 1: Exact matches
    for i in range(length):
        if guess[i] == target[i]:
            result[i] = LetterState.CORRECT.value
        else:
            unmatched_counts[target[i]] = unmatched_counts.get(target[i], 0) + 1

    # Pass 2: Partial matches
    for i in range(length):
        if result[i] != LetterState.CORRECT.value:
            char = guess[i]
            if unmatched_counts.get(char, 0) > 0:
                result[i] = LetterState.PRESENT.value
                unmatched_counts[char] -= 1
            else:
                result[i] = LetterState.ABSENT.value

    return result


WORD_LENGTH = 5


class WordleGame:
    """Wordle single game session instance."""

    def __init__(
        self,
        target_word: str,
        max_attempts: int = 6,
        word_length: int = WORD_LENGTH,
        stream_id: str = "",
        creator_id: str = "",
        creator_name: str = "",
        phonetic: str = "",
        meaning: str = "",
    ) -> None:
        self.target_word: str = target_word.strip().upper()
        self.max_attempts: int = max_attempts
        self.word_length: int = WORD_LENGTH
        self.stream_id: str = stream_id
        self.creator_id: str = creator_id
        self.creator_name: str = creator_name
        self.phonetic: str = phonetic
        self.meaning: str = meaning

        self.guesses: list[GuessRecord] = []
        self.status: str = "playing"  # "playing", "won", "lost", "stopped"
        self.start_time: float = time.time()
        self.end_time: Optional[float] = None
        self.hints_used: int = 0
        self.hint_history: list[str] = []

    @property
    def is_active(self) -> bool:
        return self.status == "playing"

    @property
    def remaining_attempts(self) -> int:
        return max(0, self.max_attempts - len(self.guesses))

    @property
    def attempt_count(self) -> int:
        return len(self.guesses)

    def guess(
        self,
        word: str,
        user_id: str = "",
        user_name: str = "",
        valid_words_set: Optional[set[str]] = None,
        enforce_dictionary: bool = True,
    ) -> tuple[bool, str, Optional[GuessRecord]]:
        """
        Submit a guess.

        Returns:
            (success: bool, message: str, record: Optional[GuessRecord])
        """
        if not self.is_active:
            return False, "当前游戏已结束，请发送 /wordle 开启新一局游戏。", None

        clean_word = word.strip().upper()
        if len(clean_word) != self.word_length:
            return False, f"请输入 {self.word_length} 个字母的英文单词！当前输入了 {len(clean_word)} 个字母。", None

        if not clean_word.isalpha():
            return False, "单词只能包含英文字母 (A-Z)。", None

        lower_word = clean_word.lower()
        if enforce_dictionary and valid_words_set and lower_word not in valid_words_set:
            return False, f"'{clean_word}' 不是一个有效的英文单词，请重新尝试！", None

        # Check if already guessed in this game
        for g in self.guesses:
            if g.word == clean_word:
                return False, f"你已经猜过 '{clean_word}' 了，换个单词试试吧！", None

        # Evaluate guess
        states = evaluate_guess(self.target_word, clean_word)
        record = GuessRecord(
            word=clean_word,
            states=states,
            user_id=user_id,
            user_name=user_name,
            timestamp=time.time(),
        )
        self.guesses.append(record)

        # Check win or loss
        if clean_word == self.target_word:
            self.status = "won"
            self.end_time = time.time()
            msg = f"🎉 恭喜！用时 {len(self.guesses)} 步成功猜中单词 {self.target_word}！"
        elif len(self.guesses) >= self.max_attempts:
            self.status = "lost"
            self.end_time = time.time()
            msg = f"💥 游戏结束，遗憾未能在 {self.max_attempts} 次内猜中。正确单词是：{self.target_word}"
        else:
            msg = f"已记录第 {len(self.guesses)}/{self.max_attempts} 次尝试。"

        return True, msg, record

    def stop(self, reason: str = "投降") -> str:
        """Surrender or stop the current game."""
        if not self.is_active:
            return "当前没有进行中的游戏。"
        self.status = "stopped"
        self.end_time = time.time()
        return f"游戏已结束（{reason}）。正确答案是：{self.target_word}"

    def get_keyboard_states(self) -> dict[str, str]:
        """
        Calculate the best-known state for each letter A-Z on the QWERTY keyboard.
        Priority: CORRECT > PRESENT > ABSENT > UNUSED
        """
        keys: dict[str, str] = {chr(c): LetterState.UNUSED.value for c in range(ord('A'), ord('Z') + 1)}

        for g in self.guesses:
            for char, state in zip(g.word, g.states):
                current = keys.get(char, LetterState.UNUSED.value)
                if state == LetterState.CORRECT.value:
                    keys[char] = LetterState.CORRECT.value
                elif state == LetterState.PRESENT.value:
                    if current != LetterState.CORRECT.value:
                        keys[char] = LetterState.PRESENT.value
                elif state == LetterState.ABSENT.value:
                    if current not in (LetterState.CORRECT.value, LetterState.PRESENT.value):
                        keys[char] = LetterState.ABSENT.value

        return keys

    def get_hint(self) -> tuple[bool, str]:
        """
        Generate an intelligent hint based on game progress.
        Hint Level 1: First letter of target word.
        Hint Level 2: Meaning/Definition clue (if available).
        Hint Level 3: Reveal an un-revealed letter position.
        """
        if not self.is_active:
            return False, "当前没有进行中的游戏，无法获取提示。"

        self.hints_used += 1

        # Determine hint
        if self.hints_used == 1:
            first_char = self.target_word[0]
            hint = f"💡 提示 1：单词的首字母是 **{first_char}**"
        elif self.hints_used == 2:
            if self.meaning:
                # Mask out occurrences of the word in meaning if any
                clean_meaning = self.meaning
                hint = f"💡 提示 2（词义线索）：{clean_meaning}"
            else:
                # Vowels count
                vowels = [c for c in self.target_word if c in "AEIOU"]
                hint = f"💡 提示 2：单词包含 {len(vowels)} 个元音字母（{', '.join(sorted(set(vowels)))}）"
        else:
            # Find an unrevealed position
            revealed_positions = set()
            for g in self.guesses:
                for idx, (char, st) in enumerate(zip(g.word, g.states)):
                    if st == LetterState.CORRECT.value:
                        revealed_positions.add(idx)

            unrevealed = [i for i in range(self.word_length) if i not in revealed_positions]
            if unrevealed:
                target_idx = random.choice(unrevealed)
                hint = f"💡 提示 {self.hints_used}：第 {target_idx + 1} 个字母是 **{self.target_word[target_idx]}**"
            else:
                hint = f"💡 提示 {self.hints_used}：单词音标为 [{self.phonetic}]" if self.phonetic else f"💡 提示 {self.hints_used}：单词是 {self.target_word}"

        self.hint_history.append(hint)
        return True, hint

    def to_text_board(self) -> str:
        """Render an emoji/text representation of the board."""
        lines = [f"🔤 **WORDLE** ({len(self.guesses)}/{self.max_attempts})"]
        for g in self.guesses:
            emojis = "".join(STATE_EMOJI_MAP.get(LetterState(st), "⬛") for st in g.states)
            letters = " ".join(list(g.word))
            lines.append(f"{emojis}  `{letters}`")

        # Fill remaining rows
        for _ in range(self.max_attempts - len(self.guesses)):
            lines.append("⬜⬜⬜⬜⬜  `_ _ _ _ _`")

        if self.status == "won":
            lines.append(f"\n🎉 恭喜在第 {len(self.guesses)} 步猜中：**{self.target_word}**")
            if self.phonetic:
                lines.append(f"🔊 音标：`[{self.phonetic}]`")
            if self.meaning:
                lines.append(f"📖 释义：{self.meaning}")
        elif self.status == "lost":
            lines.append(f"\n💥 游戏结束！正确答案是：**{self.target_word}**")
            if self.phonetic:
                lines.append(f"🔊 音标：`[{self.phonetic}]`")
            if self.meaning:
                lines.append(f"📖 释义：{self.meaning}")

        return "\n".join(lines)

    def to_dict(self) -> dict[str, Any]:
        """Serialize game state to dict."""
        return {
            "target_word": self.target_word,
            "max_attempts": self.max_attempts,
            "word_length": self.word_length,
            "stream_id": self.stream_id,
            "creator_id": self.creator_id,
            "creator_name": self.creator_name,
            "phonetic": self.phonetic,
            "meaning": self.meaning,
            "guesses": [g.to_dict() for g in self.guesses],
            "status": self.status,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "hints_used": self.hints_used,
            "hint_history": self.hint_history,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WordleGame:
        """Deserialize game state from dict."""
        game = cls(
            target_word=data["target_word"],
            max_attempts=data.get("max_attempts", 6),
            word_length=data.get("word_length", 5),
            stream_id=data.get("stream_id", ""),
            creator_id=data.get("creator_id", ""),
            creator_name=data.get("creator_name", ""),
            phonetic=data.get("phonetic", ""),
            meaning=data.get("meaning", ""),
        )
        game.guesses = [GuessRecord.from_dict(g) for g in data.get("guesses", [])]
        game.status = data.get("status", "playing")
        game.start_time = data.get("start_time", time.time())
        game.end_time = data.get("end_time")
        game.hints_used = data.get("hints_used", 0)
        game.hint_history = data.get("hint_history", [])
        return game
