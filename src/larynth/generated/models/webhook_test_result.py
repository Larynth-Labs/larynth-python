from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookTestResult")


@_attrs_define
class WebhookTestResult:
    """
    Attributes:
        delivered (bool): The first attempt got a 2xx answer
        event_id (UUID):
        error_code (str | Unset): Why the first attempt failed without a response (timeout, connection, TLS)
        response_code (int | Unset):
        response_ms (int | Unset):
    """

    delivered: bool
    event_id: UUID
    error_code: str | Unset = UNSET
    response_code: int | Unset = UNSET
    response_ms: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        delivered = self.delivered

        event_id = str(self.event_id)

        error_code = self.error_code

        response_code = self.response_code

        response_ms = self.response_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "delivered": delivered,
                "event_id": event_id,
            }
        )
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if response_code is not UNSET:
            field_dict["response_code"] = response_code
        if response_ms is not UNSET:
            field_dict["response_ms"] = response_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        delivered = d.pop("delivered")

        event_id = UUID(d.pop("event_id"))

        error_code = d.pop("error_code", UNSET)

        response_code = d.pop("response_code", UNSET)

        response_ms = d.pop("response_ms", UNSET)

        webhook_test_result = cls(
            delivered=delivered,
            event_id=event_id,
            error_code=error_code,
            response_code=response_code,
            response_ms=response_ms,
        )

        return webhook_test_result
