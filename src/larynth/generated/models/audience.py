from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.audience_kind import AudienceKind, check_audience_kind
from ..models.audience_match import AudienceMatch, check_audience_match
from ..types import UNSET, Unset

T = TypeVar("T", bound="Audience")


@_attrs_define
class Audience:
    """
    Attributes:
        kind (AudienceKind):
        contact_ids (list[str] | Unset):
        import_id (UUID | Unset):
        match (AudienceMatch | Unset):  Default: 'any'.
        tags (list[str] | Unset):
    """

    kind: AudienceKind
    contact_ids: list[str] | Unset = UNSET
    import_id: UUID | Unset = UNSET
    match: AudienceMatch | Unset = "any"
    tags: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        contact_ids: list[str] | Unset = UNSET
        if not isinstance(self.contact_ids, Unset):
            contact_ids = self.contact_ids

        import_id: str | Unset = UNSET
        if not isinstance(self.import_id, Unset):
            import_id = str(self.import_id)

        match: str | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )
        if contact_ids is not UNSET:
            field_dict["contact_ids"] = contact_ids
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if match is not UNSET:
            field_dict["match"] = match
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_audience_kind(d.pop("kind"))

        contact_ids = cast(list[str], d.pop("contact_ids", UNSET))

        _import_id = d.pop("import_id", UNSET)
        import_id: UUID | Unset
        if isinstance(_import_id, Unset):
            import_id = UNSET
        else:
            import_id = UUID(_import_id)

        _match = d.pop("match", UNSET)
        match: AudienceMatch | Unset
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = check_audience_match(_match)

        tags = cast(list[str], d.pop("tags", UNSET))

        audience = cls(
            kind=kind,
            contact_ids=contact_ids,
            import_id=import_id,
            match=match,
            tags=tags,
        )

        return audience
