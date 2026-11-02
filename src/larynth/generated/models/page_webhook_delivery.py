from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.webhook_delivery import WebhookDelivery


T = TypeVar("T", bound="PageWebhookDelivery")


@_attrs_define
class PageWebhookDelivery:
    """
    Attributes:
        data (list[WebhookDelivery]):
        next_cursor (None | str): Cursor for the next page; null on the last page
    """

    data: list[WebhookDelivery]
    next_cursor: None | str

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.webhook_delivery import WebhookDelivery

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = WebhookDelivery.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        page_webhook_delivery = cls(
            data=data,
            next_cursor=next_cursor,
        )

        return page_webhook_delivery
