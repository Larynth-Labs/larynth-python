from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_resync import KnowledgeResync


T = TypeVar("T", bound="CreateWebsiteSourceRequest")


@_attrs_define
class CreateWebsiteSourceRequest:
    """
    Attributes:
        url (str): Start page; only pages on the same host are crawled and robots.txt is respected
        max_depth (int | Unset): Link hops from the start page Default: 1.
        max_pages (int | Unset):  Default: 25.
        name (str | Unset):
        resync (KnowledgeResync | Unset):
    """

    url: str
    max_depth: int | Unset = 1
    max_pages: int | Unset = 25
    name: str | Unset = UNSET
    resync: KnowledgeResync | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        max_depth = self.max_depth

        max_pages = self.max_pages

        name = self.name

        resync: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resync, Unset):
            resync = self.resync.to_dict()

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
        if resync is not UNSET:
            field_dict["resync"] = resync

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_resync import KnowledgeResync

        d = dict(src_dict)
        url = d.pop("url")

        max_depth = d.pop("max_depth", UNSET)

        max_pages = d.pop("max_pages", UNSET)

        name = d.pop("name", UNSET)

        _resync = d.pop("resync", UNSET)
        resync: KnowledgeResync | Unset
        if isinstance(_resync, Unset):
            resync = UNSET
        else:
            resync = KnowledgeResync.from_dict(_resync)

        create_website_source_request = cls(
            url=url,
            max_depth=max_depth,
            max_pages=max_pages,
            name=name,
            resync=resync,
        )

        return create_website_source_request
