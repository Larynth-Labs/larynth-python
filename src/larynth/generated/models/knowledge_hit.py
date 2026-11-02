from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="KnowledgeHit")


@_attrs_define
class KnowledgeHit:
    """
    Attributes:
        chunk_id (str):
        score (float):
        source (str): Document name or page address
        text (str):
        topic (str):
    """

    chunk_id: str
    score: float
    source: str
    text: str
    topic: str

    def to_dict(self) -> dict[str, Any]:
        chunk_id = self.chunk_id

        score = self.score

        source = self.source

        text = self.text

        topic = self.topic

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "chunk_id": chunk_id,
                "score": score,
                "source": source,
                "text": text,
                "topic": topic,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        chunk_id = d.pop("chunk_id")

        score = d.pop("score")

        source = d.pop("source")

        text = d.pop("text")

        topic = d.pop("topic")

        knowledge_hit = cls(
            chunk_id=chunk_id,
            score=score,
            source=source,
            text=text,
            topic=topic,
        )

        return knowledge_hit
