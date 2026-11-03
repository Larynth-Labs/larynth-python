from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.contact import Contact
    from ..models.contact_counts import ContactCounts


T = TypeVar("T", bound="ContactPage")


@_attrs_define
class ContactPage:
    """
    Attributes:
        counts (ContactCounts):
        data (list[Contact]):
        next_cursor (None | str):
        prev_cursor (None | str):
    """

    counts: ContactCounts
    data: list[Contact]
    next_cursor: None | str
    prev_cursor: None | str

    def to_dict(self) -> dict[str, Any]:
        counts = self.counts.to_dict()

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_cursor: None | str
        next_cursor = self.next_cursor

        prev_cursor: None | str
        prev_cursor = self.prev_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "counts": counts,
                "data": data,
                "next_cursor": next_cursor,
                "prev_cursor": prev_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.contact import Contact
        from ..models.contact_counts import ContactCounts

        d = dict(src_dict)
        counts = ContactCounts.from_dict(d.pop("counts"))

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Contact.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        def _parse_prev_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        prev_cursor = _parse_prev_cursor(d.pop("prev_cursor"))

        contact_page = cls(
            counts=counts,
            data=data,
            next_cursor=next_cursor,
            prev_cursor=prev_cursor,
        )

        return contact_page
