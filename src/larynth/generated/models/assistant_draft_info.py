from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssistantDraftInfo")


@_attrs_define
class AssistantDraftInfo:
    """
    Attributes:
        changed_sections (list[str]): Editor sections that differ from the published version
        revision (int):
        updated_at (datetime.datetime):
        version (int):
        updated_by_name (str | Unset):
    """

    changed_sections: list[str]
    revision: int
    updated_at: datetime.datetime
    version: int
    updated_by_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        changed_sections = self.changed_sections

        revision = self.revision

        updated_at = self.updated_at.isoformat()

        version = self.version

        updated_by_name = self.updated_by_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "changed_sections": changed_sections,
                "revision": revision,
                "updated_at": updated_at,
                "version": version,
            }
        )
        if updated_by_name is not UNSET:
            field_dict["updated_by_name"] = updated_by_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        changed_sections = cast(list[str], d.pop("changed_sections"))

        revision = d.pop("revision")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        updated_by_name = d.pop("updated_by_name", UNSET)

        assistant_draft_info = cls(
            changed_sections=changed_sections,
            revision=revision,
            updated_at=updated_at,
            version=version,
            updated_by_name=updated_by_name,
        )

        return assistant_draft_info
