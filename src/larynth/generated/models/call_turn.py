from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.call_turn_spec_tts import CallTurnSpecTts, check_call_turn_spec_tts
from ..models.call_turn_speculation import (
    CallTurnSpeculation,
    check_call_turn_speculation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallTurn")


@_attrs_define
class CallTurn:
    """
    Attributes:
        barged_in (bool):
        created_at (datetime.datetime):
        from_interim (bool): Committed on interim STT text
        turn_index (int):
        agent_text (str | Unset): As played; truncated on barge-in
        eot_ms (float | Unset):
        eot_source (str | Unset):
        llm_ttft_ms (float | Unset):
        m2e_engine_ms (float | Unset):
        spec_tts (CallTurnSpecTts | Unset): Speculative first-chunk TTS outcome
        speculation (CallTurnSpeculation | Unset):
        stt_final_ms (float | Unset):
        tts_ttfb_ms (float | Unset):
        user_text (str | Unset):
    """

    barged_in: bool
    created_at: datetime.datetime
    from_interim: bool
    turn_index: int
    agent_text: str | Unset = UNSET
    eot_ms: float | Unset = UNSET
    eot_source: str | Unset = UNSET
    llm_ttft_ms: float | Unset = UNSET
    m2e_engine_ms: float | Unset = UNSET
    spec_tts: CallTurnSpecTts | Unset = UNSET
    speculation: CallTurnSpeculation | Unset = UNSET
    stt_final_ms: float | Unset = UNSET
    tts_ttfb_ms: float | Unset = UNSET
    user_text: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        barged_in = self.barged_in

        created_at = self.created_at.isoformat()

        from_interim = self.from_interim

        turn_index = self.turn_index

        agent_text = self.agent_text

        eot_ms = self.eot_ms

        eot_source = self.eot_source

        llm_ttft_ms = self.llm_ttft_ms

        m2e_engine_ms = self.m2e_engine_ms

        spec_tts: str | Unset = UNSET
        if not isinstance(self.spec_tts, Unset):
            spec_tts = self.spec_tts

        speculation: str | Unset = UNSET
        if not isinstance(self.speculation, Unset):
            speculation = self.speculation

        stt_final_ms = self.stt_final_ms

        tts_ttfb_ms = self.tts_ttfb_ms

        user_text = self.user_text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "barged_in": barged_in,
                "created_at": created_at,
                "from_interim": from_interim,
                "turn_index": turn_index,
            }
        )
        if agent_text is not UNSET:
            field_dict["agent_text"] = agent_text
        if eot_ms is not UNSET:
            field_dict["eot_ms"] = eot_ms
        if eot_source is not UNSET:
            field_dict["eot_source"] = eot_source
        if llm_ttft_ms is not UNSET:
            field_dict["llm_ttft_ms"] = llm_ttft_ms
        if m2e_engine_ms is not UNSET:
            field_dict["m2e_engine_ms"] = m2e_engine_ms
        if spec_tts is not UNSET:
            field_dict["spec_tts"] = spec_tts
        if speculation is not UNSET:
            field_dict["speculation"] = speculation
        if stt_final_ms is not UNSET:
            field_dict["stt_final_ms"] = stt_final_ms
        if tts_ttfb_ms is not UNSET:
            field_dict["tts_ttfb_ms"] = tts_ttfb_ms
        if user_text is not UNSET:
            field_dict["user_text"] = user_text

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        barged_in = d.pop("barged_in")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        from_interim = d.pop("from_interim")

        turn_index = d.pop("turn_index")

        agent_text = d.pop("agent_text", UNSET)

        eot_ms = d.pop("eot_ms", UNSET)

        eot_source = d.pop("eot_source", UNSET)

        llm_ttft_ms = d.pop("llm_ttft_ms", UNSET)

        m2e_engine_ms = d.pop("m2e_engine_ms", UNSET)

        _spec_tts = d.pop("spec_tts", UNSET)
        spec_tts: CallTurnSpecTts | Unset
        if isinstance(_spec_tts, Unset):
            spec_tts = UNSET
        else:
            spec_tts = check_call_turn_spec_tts(_spec_tts)

        _speculation = d.pop("speculation", UNSET)
        speculation: CallTurnSpeculation | Unset
        if isinstance(_speculation, Unset):
            speculation = UNSET
        else:
            speculation = check_call_turn_speculation(_speculation)

        stt_final_ms = d.pop("stt_final_ms", UNSET)

        tts_ttfb_ms = d.pop("tts_ttfb_ms", UNSET)

        user_text = d.pop("user_text", UNSET)

        call_turn = cls(
            barged_in=barged_in,
            created_at=created_at,
            from_interim=from_interim,
            turn_index=turn_index,
            agent_text=agent_text,
            eot_ms=eot_ms,
            eot_source=eot_source,
            llm_ttft_ms=llm_ttft_ms,
            m2e_engine_ms=m2e_engine_ms,
            spec_tts=spec_tts,
            speculation=speculation,
            stt_final_ms=stt_final_ms,
            tts_ttfb_ms=tts_ttfb_ms,
            user_text=user_text,
        )

        return call_turn
