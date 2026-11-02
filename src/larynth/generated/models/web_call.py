from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="WebCall")


@_attrs_define
class WebCall:
    """
    Attributes:
        call_id (str):
        max_duration_s (int): The engine ends the call after this many seconds
        sdp_answer (str):
    """

    call_id: str
    max_duration_s: int
    sdp_answer: str

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        max_duration_s = self.max_duration_s

        sdp_answer = self.sdp_answer

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "call_id": call_id,
                "max_duration_s": max_duration_s,
                "sdp_answer": sdp_answer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        call_id = d.pop("call_id")

        max_duration_s = d.pop("max_duration_s")

        sdp_answer = d.pop("sdp_answer")

        web_call = cls(
            call_id=call_id,
            max_duration_s=max_duration_s,
            sdp_answer=sdp_answer,
        )

        return web_call
