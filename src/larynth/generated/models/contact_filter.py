from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.contact_filter_purpose import (
    ContactFilterPurpose,
    check_contact_filter_purpose,
)
from ..models.contact_filter_view import ContactFilterView, check_contact_filter_view
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactFilter")


@_attrs_define
class ContactFilter:
    """
    Attributes:
        import_id (UUID | Unset):
        purpose (ContactFilterPurpose | Unset):
        q (str | Unset):
        tags (list[str] | Unset):
        view (ContactFilterView | Unset):
    """

    import_id: UUID | Unset = UNSET
    purpose: ContactFilterPurpose | Unset = UNSET
    q: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    view: ContactFilterView | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        import_id: str | Unset = UNSET
        if not isinstance(self.import_id, Unset):
            import_id = str(self.import_id)

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose

        q = self.q

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        view: str | Unset = UNSET
        if not isinstance(self.view, Unset):
            view = self.view

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if q is not UNSET:
            field_dict["q"] = q
        if tags is not UNSET:
            field_dict["tags"] = tags
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _import_id = d.pop("import_id", UNSET)
        import_id: UUID | Unset
        if isinstance(_import_id, Unset):
            import_id = UNSET
        else:
            import_id = UUID(_import_id)

        _purpose = d.pop("purpose", UNSET)
        purpose: ContactFilterPurpose | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = check_contact_filter_purpose(_purpose)

        q = d.pop("q", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _view = d.pop("view", UNSET)
        view: ContactFilterView | Unset
        if isinstance(_view, Unset):
            view = UNSET
        else:
            view = check_contact_filter_view(_view)

        contact_filter = cls(
            import_id=import_id,
            purpose=purpose,
            q=q,
            tags=tags,
            view=view,
        )

        return contact_filter
