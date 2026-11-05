from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UpdateKnowledgeDocumentRequest")


@_attrs_define
class UpdateKnowledgeDocumentRequest:
    """
    Attributes:
        excluded (bool):
    """

    excluded: bool

    def to_dict(self) -> dict[str, Any]:
        excluded = self.excluded

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "excluded": excluded,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        excluded = d.pop("excluded")

        update_knowledge_document_request = cls(
            excluded=excluded,
        )

        return update_knowledge_document_request
