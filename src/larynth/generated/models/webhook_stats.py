from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookStats")


@_attrs_define
class WebhookStats:
    """
    Attributes:
        delivered (int):
        failed (int):
        retrying (int):
    """

    delivered: int
    failed: int
    retrying: int

    def to_dict(self) -> dict[str, Any]:
        delivered = self.delivered

        failed = self.failed

        retrying = self.retrying

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "delivered": delivered,
                "failed": failed,
                "retrying": retrying,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        delivered = d.pop("delivered")

        failed = d.pop("failed")

        retrying = d.pop("retrying")

        webhook_stats = cls(
            delivered=delivered,
            failed=failed,
            retrying=retrying,
        )

        return webhook_stats
