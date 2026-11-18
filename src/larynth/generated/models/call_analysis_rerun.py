from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.call_analysis_rerun_state import (
    CallAnalysisRerunState,
    check_call_analysis_rerun_state,
)

T = TypeVar("T", bound="CallAnalysisRerun")


@_attrs_define
class CallAnalysisRerun:
    """
    Attributes:
        call_id (str):
        state (CallAnalysisRerunState):
    """

    call_id: str
    state: CallAnalysisRerunState

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        state: str = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "call_id": call_id,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        call_id = d.pop("call_id")

        state = check_call_analysis_rerun_state(d.pop("state"))

        call_analysis_rerun = cls(
            call_id=call_id,
            state=state,
        )

        return call_analysis_rerun
