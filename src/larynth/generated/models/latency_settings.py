from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LatencySettings")


@_attrs_define
class LatencySettings:
    """
    Attributes:
        force_finalize (bool | Unset): Ask the STT provider to end its turn when the turn is committed on a non-STT
            signal. Unset uses the engine node default
        short_first_chunk (bool | Unset): Cut the first TTS chunk early and send it as its own utterance for a faster
            first audio. Unset uses the engine node default
        speculative_tts (bool | Unset): Synthesise the first chunk of a speculative reply privately and play it only if
            the turn is committed. Unset uses the engine node default
        speculative_tts_min_prob (float | Unset): Minimum eager end-of-turn probability for speculative TTS. Unset uses
            the engine node default
    """

    force_finalize: bool | Unset = UNSET
    short_first_chunk: bool | Unset = UNSET
    speculative_tts: bool | Unset = UNSET
    speculative_tts_min_prob: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        force_finalize = self.force_finalize

        short_first_chunk = self.short_first_chunk

        speculative_tts = self.speculative_tts

        speculative_tts_min_prob = self.speculative_tts_min_prob

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if force_finalize is not UNSET:
            field_dict["force_finalize"] = force_finalize
        if short_first_chunk is not UNSET:
            field_dict["short_first_chunk"] = short_first_chunk
        if speculative_tts is not UNSET:
            field_dict["speculative_tts"] = speculative_tts
        if speculative_tts_min_prob is not UNSET:
            field_dict["speculative_tts_min_prob"] = speculative_tts_min_prob

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        force_finalize = d.pop("force_finalize", UNSET)

        short_first_chunk = d.pop("short_first_chunk", UNSET)

        speculative_tts = d.pop("speculative_tts", UNSET)

        speculative_tts_min_prob = d.pop("speculative_tts_min_prob", UNSET)

        latency_settings = cls(
            force_finalize=force_finalize,
            short_first_chunk=short_first_chunk,
            speculative_tts=speculative_tts,
            speculative_tts_min_prob=speculative_tts_min_prob,
        )

        return latency_settings
