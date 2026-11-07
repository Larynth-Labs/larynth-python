from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="KnowledgeLimits")


@_attrs_define
class KnowledgeLimits:
    """
    Attributes:
        file_types (list[str]): Accepted file extensions, lower case without the dot
        max_bases (int):
        max_depth (int):
        max_faq_entries (int):
        max_file_bytes (int):
        max_pages_per_site (int):
        max_sources_per_base (int):
    """

    file_types: list[str]
    max_bases: int
    max_depth: int
    max_faq_entries: int
    max_file_bytes: int
    max_pages_per_site: int
    max_sources_per_base: int

    def to_dict(self) -> dict[str, Any]:
        file_types = self.file_types

        max_bases = self.max_bases

        max_depth = self.max_depth

        max_faq_entries = self.max_faq_entries

        max_file_bytes = self.max_file_bytes

        max_pages_per_site = self.max_pages_per_site

        max_sources_per_base = self.max_sources_per_base

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "file_types": file_types,
                "max_bases": max_bases,
                "max_depth": max_depth,
                "max_faq_entries": max_faq_entries,
                "max_file_bytes": max_file_bytes,
                "max_pages_per_site": max_pages_per_site,
                "max_sources_per_base": max_sources_per_base,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        file_types = cast(list[str], d.pop("file_types"))

        max_bases = d.pop("max_bases")

        max_depth = d.pop("max_depth")

        max_faq_entries = d.pop("max_faq_entries")

        max_file_bytes = d.pop("max_file_bytes")

        max_pages_per_site = d.pop("max_pages_per_site")

        max_sources_per_base = d.pop("max_sources_per_base")

        knowledge_limits = cls(
            file_types=file_types,
            max_bases=max_bases,
            max_depth=max_depth,
            max_faq_entries=max_faq_entries,
            max_file_bytes=max_file_bytes,
            max_pages_per_site=max_pages_per_site,
            max_sources_per_base=max_sources_per_base,
        )

        return knowledge_limits
