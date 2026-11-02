from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ICEServer")


@_attrs_define
class ICEServer:
    """
    Attributes:
        urls (list[str]):
        credential (str | Unset):
        username (str | Unset):
    """

    urls: list[str]
    credential: str | Unset = UNSET
    username: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        urls = self.urls

        credential = self.credential

        username = self.username

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "urls": urls,
            }
        )
        if credential is not UNSET:
            field_dict["credential"] = credential
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        urls = cast(list[str], d.pop("urls"))

        credential = d.pop("credential", UNSET)

        username = d.pop("username", UNSET)

        ice_server = cls(
            urls=urls,
            credential=credential,
            username=username,
        )

        return ice_server
