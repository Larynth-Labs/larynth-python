from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.issue_action_key import IssueActionKey, check_issue_action_key
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueAction")


@_attrs_define
class IssueAction:
    """
    Attributes:
        key (IssueActionKey):
        label (str):
        href (str | Unset): Dashboard path the action opens
    """

    key: IssueActionKey
    label: str
    href: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key: str = self.key

        label = self.label

        href = self.href

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "label": label,
            }
        )
        if href is not UNSET:
            field_dict["href"] = href

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = check_issue_action_key(d.pop("key"))

        label = d.pop("label")

        href = d.pop("href", UNSET)

        issue_action = cls(
            key=key,
            label=label,
            href=href,
        )

        return issue_action
