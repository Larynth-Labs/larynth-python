from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_filter import ContactFilter


T = TypeVar("T", bound="ContactSelection")


@_attrs_define
class ContactSelection:
    """
    Attributes:
        filter_ (ContactFilter | Unset):
        ids (list[str] | Unset):
    """

    filter_: ContactFilter | Unset = UNSET
    ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.contact_filter import ContactFilter

        d = dict(src_dict)
        _filter_ = d.pop("filter", UNSET)
        filter_: ContactFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ContactFilter.from_dict(_filter_)

        ids = cast(list[str], d.pop("ids", UNSET))

        contact_selection = cls(
            filter_=filter_,
            ids=ids,
        )

        return contact_selection
