from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TimezoneShare")


@_attrs_define
class TimezoneShare:
    """
    Attributes:
        share (float):
        tz (str):
    """

    share: float
    tz: str

    def to_dict(self) -> dict[str, Any]:
        share = self.share

        tz = self.tz

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "share": share,
                "tz": tz,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        share = d.pop("share")

        tz = d.pop("tz")

        timezone_share = cls(
            share=share,
            tz=tz,
        )

        return timezone_share
