from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.webhook_event_type_group import (
    WebhookEventTypeGroup,
    check_webhook_event_type_group,
)

T = TypeVar("T", bound="WebhookEventType")


@_attrs_define
class WebhookEventType:
    """
    Attributes:
        deprecated (bool):
        description_key (str):
        group (WebhookEventTypeGroup):
        label_key (str):
        type_ (str):
    """

    deprecated: bool
    description_key: str
    group: WebhookEventTypeGroup
    label_key: str
    type_: str

    def to_dict(self) -> dict[str, Any]:
        deprecated = self.deprecated

        description_key = self.description_key

        group: str = self.group

        label_key = self.label_key

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "deprecated": deprecated,
                "description_key": description_key,
                "group": group,
                "label_key": label_key,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        deprecated = d.pop("deprecated")

        description_key = d.pop("description_key")

        group = check_webhook_event_type_group(d.pop("group"))

        label_key = d.pop("label_key")

        type_ = d.pop("type")

        webhook_event_type = cls(
            deprecated=deprecated,
            description_key=description_key,
            group=group,
            label_key=label_key,
            type_=type_,
        )

        return webhook_event_type
