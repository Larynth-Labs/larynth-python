from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.test_webhook_request_event_type import (
    TestWebhookRequestEventType,
    check_test_webhook_request_event_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TestWebhookRequest")


@_attrs_define
class TestWebhookRequest:
    """
    Attributes:
        event_type (TestWebhookRequestEventType | Unset):  Default: 'call.ended'.
    """

    event_type: TestWebhookRequestEventType | Unset = "call.ended"

    def to_dict(self) -> dict[str, Any]:
        event_type: str | Unset = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if event_type is not UNSET:
            field_dict["event_type"] = event_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _event_type = d.pop("event_type", UNSET)
        event_type: TestWebhookRequestEventType | Unset
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = check_test_webhook_request_event_type(_event_type)

        test_webhook_request = cls(
            event_type=event_type,
        )

        return test_webhook_request
