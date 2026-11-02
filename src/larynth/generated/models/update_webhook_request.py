from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.update_webhook_request_event_types_item import (
    UpdateWebhookRequestEventTypesItem,
    check_update_webhook_request_event_types_item,
)
from ..models.update_webhook_request_status import (
    UpdateWebhookRequestStatus,
    check_update_webhook_request_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhookRequest")


@_attrs_define
class UpdateWebhookRequest:
    """
    Attributes:
        description (str | Unset):
        event_types (list[UpdateWebhookRequestEventTypesItem] | Unset):
        status (UpdateWebhookRequestStatus | Unset):
        url (str | Unset):
    """

    description: str | Unset = UNSET
    event_types: list[UpdateWebhookRequestEventTypesItem] | Unset = UNSET
    status: UpdateWebhookRequestStatus | Unset = UNSET
    url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = []
            for event_types_item_data in self.event_types:
                event_types_item: str = event_types_item_data
                event_types.append(event_types_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _event_types = d.pop("event_types", UNSET)
        event_types: list[UpdateWebhookRequestEventTypesItem] | Unset = UNSET
        if _event_types is not UNSET:
            event_types = []
            for event_types_item_data in _event_types:
                event_types_item = check_update_webhook_request_event_types_item(
                    event_types_item_data
                )

                event_types.append(event_types_item)

        _status = d.pop("status", UNSET)
        status: UpdateWebhookRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_webhook_request_status(_status)

        url = d.pop("url", UNSET)

        update_webhook_request = cls(
            description=description,
            event_types=event_types,
            status=status,
            url=url,
        )

        return update_webhook_request
