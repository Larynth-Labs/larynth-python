from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddIssueNoteRequest")


@_attrs_define
class AddIssueNoteRequest:
    """
    Attributes:
        note (str): Do not paste caller details
    """

    note: str

    def to_dict(self) -> dict[str, Any]:
        note = self.note

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "note": note,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        note = d.pop("note")

        add_issue_note_request = cls(
            note=note,
        )

        return add_issue_note_request
