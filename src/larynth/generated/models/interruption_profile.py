from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="InterruptionProfile")


@_attrs_define
class InterruptionProfile:
    """
    Attributes:
        enabled (bool | Unset):
        false_interruption_ms (int | Unset):
        ignore_words (list[str] | Unset):
        keep_echo_words (bool | Unset): Count caller words that repeat the agent's own reply (line echo) as barge-in
            words
        min_speech_ms (int | Unset):
        min_words (int | Unset):
        vad_only_min_speech_ms (int | Unset): Barge-in on voice activity alone, before the STT has heard a word, needs
            this much speech. Unset is 1000
    """

    enabled: bool | Unset = UNSET
    false_interruption_ms: int | Unset = UNSET
    ignore_words: list[str] | Unset = UNSET
    keep_echo_words: bool | Unset = UNSET
    min_speech_ms: int | Unset = UNSET
    min_words: int | Unset = UNSET
    vad_only_min_speech_ms: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        false_interruption_ms = self.false_interruption_ms

        ignore_words: list[str] | Unset = UNSET
        if not isinstance(self.ignore_words, Unset):
            ignore_words = self.ignore_words

        keep_echo_words = self.keep_echo_words

        min_speech_ms = self.min_speech_ms

        min_words = self.min_words

        vad_only_min_speech_ms = self.vad_only_min_speech_ms

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if false_interruption_ms is not UNSET:
            field_dict["false_interruption_ms"] = false_interruption_ms
        if ignore_words is not UNSET:
            field_dict["ignore_words"] = ignore_words
        if keep_echo_words is not UNSET:
            field_dict["keep_echo_words"] = keep_echo_words
        if min_speech_ms is not UNSET:
            field_dict["min_speech_ms"] = min_speech_ms
        if min_words is not UNSET:
            field_dict["min_words"] = min_words
        if vad_only_min_speech_ms is not UNSET:
            field_dict["vad_only_min_speech_ms"] = vad_only_min_speech_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        false_interruption_ms = d.pop("false_interruption_ms", UNSET)

        ignore_words = cast(list[str], d.pop("ignore_words", UNSET))

        keep_echo_words = d.pop("keep_echo_words", UNSET)

        min_speech_ms = d.pop("min_speech_ms", UNSET)

        min_words = d.pop("min_words", UNSET)

        vad_only_min_speech_ms = d.pop("vad_only_min_speech_ms", UNSET)

        interruption_profile = cls(
            enabled=enabled,
            false_interruption_ms=false_interruption_ms,
            ignore_words=ignore_words,
            keep_echo_words=keep_echo_words,
            min_speech_ms=min_speech_ms,
            min_words=min_words,
            vad_only_min_speech_ms=vad_only_min_speech_ms,
        )

        return interruption_profile
