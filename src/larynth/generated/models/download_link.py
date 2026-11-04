from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DownloadLink")


@_attrs_define
class DownloadLink:
    """
    Attributes:
        download_url (str):
        expires_at (datetime.datetime):
    """

    download_url: str
    expires_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        download_url = self.download_url

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "download_url": download_url,
                "expires_at": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        download_url = d.pop("download_url")

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        download_link = cls(
            download_url=download_url,
            expires_at=expires_at,
        )

        return download_link
