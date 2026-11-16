from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcceptKnowledgeGapDraftRequest")


@_attrs_define
class AcceptKnowledgeGapDraftRequest:
    """
    Attributes:
        knowledge_base_id (UUID):
        answer (str | Unset): The owner's edit of the draft; unset uses the draft as it is
        question (str | Unset): Question to store; unset uses the draft's question
    """

    knowledge_base_id: UUID
    answer: str | Unset = UNSET
    question: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        knowledge_base_id = str(self.knowledge_base_id)

        answer = self.answer

        question = self.question

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "knowledge_base_id": knowledge_base_id,
            }
        )
        if answer is not UNSET:
            field_dict["answer"] = answer
        if question is not UNSET:
            field_dict["question"] = question

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        knowledge_base_id = UUID(d.pop("knowledge_base_id"))

        answer = d.pop("answer", UNSET)

        question = d.pop("question", UNSET)

        accept_knowledge_gap_draft_request = cls(
            knowledge_base_id=knowledge_base_id,
            answer=answer,
            question=question,
        )

        return accept_knowledge_gap_draft_request
