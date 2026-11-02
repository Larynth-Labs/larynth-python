from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebsiteSourceRequest")


@_attrs_define
class CreateWebsiteSourceRequest:
    """
    Attributes:
        url (str): Start page; only pages on the same host are crawled and robots.txt is respected
        max_depth (int | Unset): Link hops from the start page Default: 1.
        max_pages (int | Unset):  Default: 25.
        name (str | Unset):
    """

    url: str
    max_depth: int | Unset = 1
    max_pages: int | Unset = 25
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        max_depth = self.max_depth

        max_pages = self.max_pages

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if max_depth is not UNSET:
            field_dict["max_depth"] = max_depth
        if max_pages is not UNSET:
            field_dict["max_pages"] = max_pages
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        url = d.pop("url")

        max_depth = d.pop("max_depth", UNSET)

        max_pages = d.pop("max_pages", UNSET)

        name = d.pop("name", UNSET)

        create_website_source_request = cls(
            url=url,
            max_depth=max_depth,
            max_pages=max_pages,
            name=name,
        )

        return create_website_source_request
