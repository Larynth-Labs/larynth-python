from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="IssueAssignee")


@_attrs_define
class IssueAssignee:
    """
    Attributes:
        name (str):
        user_id (UUID):
    """

    name: str
    user_id: UUID

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        user_id = UUID(d.pop("user_id"))

        issue_assignee = cls(
            name=name,
            user_id=user_id,
        )

        return issue_assignee
