from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_analysis_data import CallAnalysisData


T = TypeVar("T", bound="CallAnalysis")


@_attrs_define
class CallAnalysis:
    """
    Attributes:
        call_id (str):
        cost_micro (int): Analysis cost in micro-USD
        created_at (datetime.datetime):
        data (CallAnalysisData):
        summary (str):
        tokens (int):
        model_id (UUID | Unset):
        reason (str | Unset):
        successful (bool | Unset):
    """

    call_id: str
    cost_micro: int
    created_at: datetime.datetime
    data: CallAnalysisData
    summary: str
    tokens: int
    model_id: UUID | Unset = UNSET
    reason: str | Unset = UNSET
    successful: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        cost_micro = self.cost_micro

        created_at = self.created_at.isoformat()

        data = self.data.to_dict()

        summary = self.summary

        tokens = self.tokens

        model_id: str | Unset = UNSET
        if not isinstance(self.model_id, Unset):
            model_id = str(self.model_id)

        reason = self.reason

        successful = self.successful

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "call_id": call_id,
                "cost_micro": cost_micro,
                "created_at": created_at,
                "data": data,
                "summary": summary,
                "tokens": tokens,
            }
        )
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if successful is not UNSET:
            field_dict["successful"] = successful

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_analysis_data import CallAnalysisData

        d = dict(src_dict)
        call_id = d.pop("call_id")

        cost_micro = d.pop("cost_micro")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        data = CallAnalysisData.from_dict(d.pop("data"))

        summary = d.pop("summary")

        tokens = d.pop("tokens")

        _model_id = d.pop("model_id", UNSET)
        model_id: UUID | Unset
        if isinstance(_model_id, Unset):
            model_id = UNSET
        else:
            model_id = UUID(_model_id)

        reason = d.pop("reason", UNSET)

        successful = d.pop("successful", UNSET)

        call_analysis = cls(
            call_id=call_id,
            cost_micro=cost_micro,
            created_at=created_at,
            data=data,
            summary=summary,
            tokens=tokens,
            model_id=model_id,
            reason=reason,
            successful=successful,
        )

        return call_analysis
