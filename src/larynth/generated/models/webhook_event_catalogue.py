from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webhook_event_type import WebhookEventType
    from ..models.webhook_retry_policy import WebhookRetryPolicy


T = TypeVar("T", bound="WebhookEventCatalogue")


@_attrs_define
class WebhookEventCatalogue:
    """
    Attributes:
        data (list[WebhookEventType]):
        retry_policy (WebhookRetryPolicy):
    """

    data: list[WebhookEventType]
    retry_policy: WebhookRetryPolicy

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        retry_policy = self.retry_policy.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "retry_policy": retry_policy,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_event_type import WebhookEventType
        from ..models.webhook_retry_policy import WebhookRetryPolicy

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = WebhookEventType.from_dict(data_item_data)

            data.append(data_item)

        retry_policy = WebhookRetryPolicy.from_dict(d.pop("retry_policy"))

        webhook_event_catalogue = cls(
            data=data,
            retry_policy=retry_policy,
        )

        return webhook_event_catalogue
