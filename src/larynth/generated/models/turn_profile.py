from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TurnProfile")


@_attrs_define
class TurnProfile:
    """
    Attributes:
        commit_prob (float | Unset):
        commit_without_words (bool | Unset): With STT end-of-turn primary, commit turns the STT heard no words in
            instead of discarding them as noise or echo
        eager_prob (float | Unset):
        hold_max_ms (int | Unset): Silence a model end-of-turn commit needs at commit_prob; confident predictions commit
            sooner. Unset is 500
        hold_min_ms (int | Unset): Silence a model end-of-turn commit needs at probability 1. Unset is 200
        max_silence_ms (int | Unset):
        min_speech_ms (int | Unset):
        stop_silence_ms (int | Unset):
        use_stt_eot (bool | Unset):
    """

    commit_prob: float | Unset = UNSET
    commit_without_words: bool | Unset = UNSET
    eager_prob: float | Unset = UNSET
    hold_max_ms: int | Unset = UNSET
    hold_min_ms: int | Unset = UNSET
    max_silence_ms: int | Unset = UNSET
    min_speech_ms: int | Unset = UNSET
    stop_silence_ms: int | Unset = UNSET
    use_stt_eot: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        commit_prob = self.commit_prob

        commit_without_words = self.commit_without_words

        eager_prob = self.eager_prob

        hold_max_ms = self.hold_max_ms

        hold_min_ms = self.hold_min_ms

        max_silence_ms = self.max_silence_ms

        min_speech_ms = self.min_speech_ms

        stop_silence_ms = self.stop_silence_ms

        use_stt_eot = self.use_stt_eot

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if commit_prob is not UNSET:
            field_dict["commit_prob"] = commit_prob
        if commit_without_words is not UNSET:
            field_dict["commit_without_words"] = commit_without_words
        if eager_prob is not UNSET:
            field_dict["eager_prob"] = eager_prob
        if hold_max_ms is not UNSET:
            field_dict["hold_max_ms"] = hold_max_ms
        if hold_min_ms is not UNSET:
            field_dict["hold_min_ms"] = hold_min_ms
        if max_silence_ms is not UNSET:
            field_dict["max_silence_ms"] = max_silence_ms
        if min_speech_ms is not UNSET:
            field_dict["min_speech_ms"] = min_speech_ms
        if stop_silence_ms is not UNSET:
            field_dict["stop_silence_ms"] = stop_silence_ms
        if use_stt_eot is not UNSET:
            field_dict["use_stt_eot"] = use_stt_eot

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        commit_prob = d.pop("commit_prob", UNSET)

        commit_without_words = d.pop("commit_without_words", UNSET)

        eager_prob = d.pop("eager_prob", UNSET)

        hold_max_ms = d.pop("hold_max_ms", UNSET)

        hold_min_ms = d.pop("hold_min_ms", UNSET)

        max_silence_ms = d.pop("max_silence_ms", UNSET)

        min_speech_ms = d.pop("min_speech_ms", UNSET)

        stop_silence_ms = d.pop("stop_silence_ms", UNSET)

        use_stt_eot = d.pop("use_stt_eot", UNSET)

        turn_profile = cls(
            commit_prob=commit_prob,
            commit_without_words=commit_without_words,
            eager_prob=eager_prob,
            hold_max_ms=hold_max_ms,
            hold_min_ms=hold_min_ms,
            max_silence_ms=max_silence_ms,
            min_speech_ms=min_speech_ms,
            stop_silence_ms=stop_silence_ms,
            use_stt_eot=use_stt_eot,
        )

        return turn_profile
