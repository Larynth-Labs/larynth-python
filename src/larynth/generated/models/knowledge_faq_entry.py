from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="KnowledgeFaqEntry")


@_attrs_define
class KnowledgeFaqEntry:
    """
    Attributes:
        a (str): Answer
        q (str): Question
    """

    a: str
    q: str

    def to_dict(self) -> dict[str, Any]:
        a = self.a

        q = self.q

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "a": a,
                "q": q,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        a = d.pop("a")

        q = d.pop("q")

        knowledge_faq_entry = cls(
            a=a,
            q=q,
        )

        return knowledge_faq_entry
