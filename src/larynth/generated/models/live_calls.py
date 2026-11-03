from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.concurrency import Concurrency
    from ..models.live_call import LiveCall


T = TypeVar("T", bound="LiveCalls")


@_attrs_define
class LiveCalls:
    """
    Attributes:
        concurrency (Concurrency):
        data (list[LiveCall]):
    """

    concurrency: Concurrency
    data: list[LiveCall]

    def to_dict(self) -> dict[str, Any]:
        concurrency = self.concurrency.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "concurrency": concurrency,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.concurrency import Concurrency
        from ..models.live_call import LiveCall

        d = dict(src_dict)
        concurrency = Concurrency.from_dict(d.pop("concurrency"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = LiveCall.from_dict(data_item_data)

            data.append(data_item)

        live_calls = cls(
            concurrency=concurrency,
            data=data,
        )

        return live_calls
