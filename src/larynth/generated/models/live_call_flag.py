from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.live_call_flag_kind import LiveCallFlagKind, check_live_call_flag_kind

T = TypeVar("T", bound="LiveCallFlag")


@_attrs_define
class LiveCallFlag:
    """
    Attributes:
        kind (LiveCallFlagKind):
        since (datetime.datetime):
    """

    kind: LiveCallFlagKind
    since: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        since = self.since.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "since": since,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_live_call_flag_kind(d.pop("kind"))

        since = datetime.datetime.fromisoformat(d.pop("since"))

        live_call_flag = cls(
            kind=kind,
            since=since,
        )

        return live_call_flag
