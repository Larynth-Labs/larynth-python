from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.alert_delivery_channel import (
    AlertDeliveryChannel,
    check_alert_delivery_channel,
)
from ..models.alert_delivery_status import (
    AlertDeliveryStatus,
    check_alert_delivery_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertDelivery")


@_attrs_define
class AlertDelivery:
    """
    Attributes:
        at (datetime.datetime):
        channel (AlertDeliveryChannel):
        status (AlertDeliveryStatus):
        error (str | Unset):
    """

    at: datetime.datetime
    channel: AlertDeliveryChannel
    status: AlertDeliveryStatus
    error: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        channel: str = self.channel

        status: str = self.status

        error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "channel": channel,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        channel = check_alert_delivery_channel(d.pop("channel"))

        status = check_alert_delivery_status(d.pop("status"))

        error = d.pop("error", UNSET)

        alert_delivery = cls(
            at=at,
            channel=channel,
            status=status,
            error=error,
        )

        return alert_delivery
