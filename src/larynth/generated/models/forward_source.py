from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ForwardSource")


@_attrs_define
class ForwardSource:
    """
    Attributes:
        calls (int):
        e164 (str):
        first_seen_at (datetime.datetime):
        last_seen_at (datetime.datetime):
    """

    calls: int
    e164: str
    first_seen_at: datetime.datetime
    last_seen_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        calls = self.calls

        e164 = self.e164

        first_seen_at = self.first_seen_at.isoformat()

        last_seen_at = self.last_seen_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "calls": calls,
                "e164": e164,
                "first_seen_at": first_seen_at,
                "last_seen_at": last_seen_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        calls = d.pop("calls")

        e164 = d.pop("e164")

        first_seen_at = datetime.datetime.fromisoformat(d.pop("first_seen_at"))

        last_seen_at = datetime.datetime.fromisoformat(d.pop("last_seen_at"))

        forward_source = cls(
            calls=calls,
            e164=e164,
            first_seen_at=first_seen_at,
            last_seen_at=last_seen_at,
        )

        return forward_source
