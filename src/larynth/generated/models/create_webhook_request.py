from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.create_webhook_request_event_types_item import (
    CreateWebhookRequestEventTypesItem,
    check_create_webhook_request_event_types_item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookRequest")


@_attrs_define
class CreateWebhookRequest:
    """
    Attributes:
        event_types (list[CreateWebhookRequestEventTypesItem]):
        url (str):
        description (str | Unset):
    """

    event_types: list[CreateWebhookRequestEventTypesItem]
    url: str
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        event_types = []
        for event_types_item_data in self.event_types:
            event_types_item: str = event_types_item_data
            event_types.append(event_types_item)

        url = self.url

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event_types": event_types,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        event_types = []
        _event_types = d.pop("event_types")
        for event_types_item_data in _event_types:
            event_types_item = check_create_webhook_request_event_types_item(
                event_types_item_data
            )

            event_types.append(event_types_item)

        url = d.pop("url")

        description = d.pop("description", UNSET)

        create_webhook_request = cls(
            event_types=event_types,
            url=url,
            description=description,
        )

        return create_webhook_request
