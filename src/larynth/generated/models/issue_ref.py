from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.issue_ref_type import IssueRefType, check_issue_ref_type

T = TypeVar("T", bound="IssueRef")


@_attrs_define
class IssueRef:
    """
    Attributes:
        id (str):
        type_ (IssueRefType):
    """

    id: str
    type_: IssueRefType

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = check_issue_ref_type(d.pop("type"))

        issue_ref = cls(
            id=id,
            type_=type_,
        )

        return issue_ref
