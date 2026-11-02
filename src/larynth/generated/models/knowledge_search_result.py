from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.knowledge_search_result_mode import (
    KnowledgeSearchResultMode,
    check_knowledge_search_result_mode,
)

if TYPE_CHECKING:
    from ..models.knowledge_hit import KnowledgeHit


T = TypeVar("T", bound="KnowledgeSearchResult")


@_attrs_define
class KnowledgeSearchResult:
    """
    Attributes:
        hits (list[KnowledgeHit]):
        mode (KnowledgeSearchResultMode): lexical when the knowledge base has no vectors or the query embedding was
            unavailable
        took_ms (int):
    """

    hits: list[KnowledgeHit]
    mode: KnowledgeSearchResultMode
    took_ms: int

    def to_dict(self) -> dict[str, Any]:
        hits = []
        for hits_item_data in self.hits:
            hits_item = hits_item_data.to_dict()
            hits.append(hits_item)

        mode: str = self.mode

        took_ms = self.took_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "hits": hits,
                "mode": mode,
                "took_ms": took_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_hit import KnowledgeHit

        d = dict(src_dict)
        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:
            hits_item = KnowledgeHit.from_dict(hits_item_data)

            hits.append(hits_item)

        mode = check_knowledge_search_result_mode(d.pop("mode"))

        took_ms = d.pop("took_ms")

        knowledge_search_result = cls(
            hits=hits,
            mode=mode,
            took_ms=took_ms,
        )

        return knowledge_search_result
