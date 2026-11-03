from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call import Call


T = TypeVar("T", bound="SameCallerCalls")


@_attrs_define
class SameCallerCalls:
    """
    Attributes:
        data (list[Call]):
        total (int): All calls from this caller; the calls list filtered by caller_e164 shows them
        caller_e164 (str | Unset):
    """

    data: list[Call]
    total: int
    caller_e164: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        total = self.total

        caller_e164 = self.caller_e164

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "total": total,
            }
        )
        if caller_e164 is not UNSET:
            field_dict["caller_e164"] = caller_e164

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call import Call

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Call.from_dict(data_item_data)

            data.append(data_item)

        total = d.pop("total")

        caller_e164 = d.pop("caller_e164", UNSET)

        same_caller_calls = cls(
            data=data,
            total=total,
            caller_e164=caller_e164,
        )

        return same_caller_calls
