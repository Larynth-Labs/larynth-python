from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="CampaignLaunch")


@_attrs_define
class CampaignLaunch:
    """
    Attributes:
        at (datetime.datetime):
        attest_text_version (str):
        by_name (str):
        by_user_id (UUID):
    """

    at: datetime.datetime
    attest_text_version: str
    by_name: str
    by_user_id: UUID

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        attest_text_version = self.attest_text_version

        by_name = self.by_name

        by_user_id = str(self.by_user_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "attest_text_version": attest_text_version,
                "by_name": by_name,
                "by_user_id": by_user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        attest_text_version = d.pop("attest_text_version")

        by_name = d.pop("by_name")

        by_user_id = UUID(d.pop("by_user_id"))

        campaign_launch = cls(
            at=at,
            attest_text_version=attest_text_version,
            by_name=by_name,
            by_user_id=by_user_id,
        )

        return campaign_launch
