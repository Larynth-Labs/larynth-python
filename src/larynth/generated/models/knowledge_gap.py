from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.knowledge_gap_state import KnowledgeGapState, check_knowledge_gap_state
from ..types import UNSET, Unset

T = TypeVar("T", bound="KnowledgeGap")


@_attrs_define
class KnowledgeGap:
    """
    Attributes:
        assistant_ids (list[str]):
        call_ids (list[str]): Up to 5 most recent calls
        count (int):
        examples (list[str]): Up to 3 questions as callers asked them
        id (UUID):
        knowledge_base_ids (list[str]): Bases attached to the asking agents' versions when the question came up
        last_asked_at (datetime.datetime):
        question (str): Normalised wording of the group
        state (KnowledgeGapState):
        answered_source_id (UUID | Unset):
        decided_at (datetime.datetime | Unset):
        decided_by_name (str | Unset):
    """

    assistant_ids: list[str]
    call_ids: list[str]
    count: int
    examples: list[str]
    id: UUID
    knowledge_base_ids: list[str]
    last_asked_at: datetime.datetime
    question: str
    state: KnowledgeGapState
    answered_source_id: UUID | Unset = UNSET
    decided_at: datetime.datetime | Unset = UNSET
    decided_by_name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_ids = self.assistant_ids

        call_ids = self.call_ids

        count = self.count

        examples = self.examples

        id = str(self.id)

        knowledge_base_ids = self.knowledge_base_ids

        last_asked_at = self.last_asked_at.isoformat()

        question = self.question

        state: str = self.state

        answered_source_id: str | Unset = UNSET
        if not isinstance(self.answered_source_id, Unset):
            answered_source_id = str(self.answered_source_id)

        decided_at: str | Unset = UNSET
        if not isinstance(self.decided_at, Unset):
            decided_at = self.decided_at.isoformat()

        decided_by_name = self.decided_by_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_ids": assistant_ids,
                "call_ids": call_ids,
                "count": count,
                "examples": examples,
                "id": id,
                "knowledge_base_ids": knowledge_base_ids,
                "last_asked_at": last_asked_at,
                "question": question,
                "state": state,
            }
        )
        if answered_source_id is not UNSET:
            field_dict["answered_source_id"] = answered_source_id
        if decided_at is not UNSET:
            field_dict["decided_at"] = decided_at
        if decided_by_name is not UNSET:
            field_dict["decided_by_name"] = decided_by_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        assistant_ids = cast(list[str], d.pop("assistant_ids"))

        call_ids = cast(list[str], d.pop("call_ids"))

        count = d.pop("count")

        examples = cast(list[str], d.pop("examples"))

        id = UUID(d.pop("id"))

        knowledge_base_ids = cast(list[str], d.pop("knowledge_base_ids"))

        last_asked_at = datetime.datetime.fromisoformat(d.pop("last_asked_at"))

        question = d.pop("question")

        state = check_knowledge_gap_state(d.pop("state"))

        _answered_source_id = d.pop("answered_source_id", UNSET)
        answered_source_id: UUID | Unset
        if isinstance(_answered_source_id, Unset):
            answered_source_id = UNSET
        else:
            answered_source_id = UUID(_answered_source_id)

        _decided_at = d.pop("decided_at", UNSET)
        decided_at: datetime.datetime | Unset
        if isinstance(_decided_at, Unset):
            decided_at = UNSET
        else:
            decided_at = datetime.datetime.fromisoformat(_decided_at)

        decided_by_name = d.pop("decided_by_name", UNSET)

        knowledge_gap = cls(
            assistant_ids=assistant_ids,
            call_ids=call_ids,
            count=count,
            examples=examples,
            id=id,
            knowledge_base_ids=knowledge_base_ids,
            last_asked_at=last_asked_at,
            question=question,
            state=state,
            answered_source_id=answered_source_id,
            decided_at=decided_at,
            decided_by_name=decided_by_name,
        )

        return knowledge_gap
