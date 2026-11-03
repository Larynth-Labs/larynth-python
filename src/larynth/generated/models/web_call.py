from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.web_call_rounding import WebCallRounding, check_web_call_rounding
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebCall")


@_attrs_define
class WebCall:
    """
    Attributes:
        call_id (str):
        max_duration_s (int): The engine ends the call after this many seconds
        sdp_answer (str):
        free_under_ms (int | Unset): Calls shorter than this are not billed
        rate_micro_per_min (int | Unset): Applied per-minute rate including premiums
        rounding (WebCallRounding | Unset):
        version (int | Unset): Assistant version the call runs
    """

    call_id: str
    max_duration_s: int
    sdp_answer: str
    free_under_ms: int | Unset = UNSET
    rate_micro_per_min: int | Unset = UNSET
    rounding: WebCallRounding | Unset = UNSET
    version: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        max_duration_s = self.max_duration_s

        sdp_answer = self.sdp_answer

        free_under_ms = self.free_under_ms

        rate_micro_per_min = self.rate_micro_per_min

        rounding: str | Unset = UNSET
        if not isinstance(self.rounding, Unset):
            rounding = self.rounding

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "call_id": call_id,
                "max_duration_s": max_duration_s,
                "sdp_answer": sdp_answer,
            }
        )
        if free_under_ms is not UNSET:
            field_dict["free_under_ms"] = free_under_ms
        if rate_micro_per_min is not UNSET:
            field_dict["rate_micro_per_min"] = rate_micro_per_min
        if rounding is not UNSET:
            field_dict["rounding"] = rounding
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        call_id = d.pop("call_id")

        max_duration_s = d.pop("max_duration_s")

        sdp_answer = d.pop("sdp_answer")

        free_under_ms = d.pop("free_under_ms", UNSET)

        rate_micro_per_min = d.pop("rate_micro_per_min", UNSET)

        _rounding = d.pop("rounding", UNSET)
        rounding: WebCallRounding | Unset
        if isinstance(_rounding, Unset):
            rounding = UNSET
        else:
            rounding = check_web_call_rounding(_rounding)

        version = d.pop("version", UNSET)

        web_call = cls(
            call_id=call_id,
            max_duration_s=max_duration_s,
            sdp_answer=sdp_answer,
            free_under_ms=free_under_ms,
            rate_micro_per_min=rate_micro_per_min,
            rounding=rounding,
            version=version,
        )

        return web_call
