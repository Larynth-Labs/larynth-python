from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddCampaignContactsResult")


@_attrs_define
class AddCampaignContactsResult:
    """
    Attributes:
        added (int):
        skipped (int): Already enrolled
    """

    added: int
    skipped: int

    def to_dict(self) -> dict[str, Any]:
        added = self.added

        skipped = self.skipped

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "added": added,
                "skipped": skipped,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        added = d.pop("added")

        skipped = d.pop("skipped")

        add_campaign_contacts_result = cls(
            added=added,
            skipped=skipped,
        )

        return add_campaign_contacts_result
