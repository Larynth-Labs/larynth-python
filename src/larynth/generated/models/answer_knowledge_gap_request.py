from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnswerKnowledgeGapRequest")


@_attrs_define
class AnswerKnowledgeGapRequest:
    """
    Attributes:
        answer (str):
        knowledge_base_id (UUID):
        question (str | Unset): Question to store; unset uses the group's wording
    """

    answer: str
    knowledge_base_id: UUID
    question: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        answer = self.answer

        knowledge_base_id = str(self.knowledge_base_id)

        question = self.question

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answer": answer,
                "knowledge_base_id": knowledge_base_id,
            }
        )
        if question is not UNSET:
            field_dict["question"] = question

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        answer = d.pop("answer")

        knowledge_base_id = UUID(d.pop("knowledge_base_id"))

        question = d.pop("question", UNSET)

        answer_knowledge_gap_request = cls(
            answer=answer,
            knowledge_base_id=knowledge_base_id,
            question=question,
        )

        return answer_knowledge_gap_request
