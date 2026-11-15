from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.knowledge_gap_draft_status import (
    KnowledgeGapDraftStatus,
    check_knowledge_gap_draft_status,
)
from ..models.knowledge_gap_state import KnowledgeGapState, check_knowledge_gap_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.knowledge_gap_draft_source import KnowledgeGapDraftSource


T = TypeVar("T", bound="KnowledgeGap")


@_attrs_define
class KnowledgeGap:
    """
    Attributes:
        assistant_ids (list[str]):
        call_ids (list[str]): Up to 5 most recent calls
        count (int):
        draft_sources (list[KnowledgeGapDraftSource]):
        draft_status (KnowledgeGapDraftStatus): drafted: an answer is ready; blocked_unverified: no draft because a fact
            could not be found verbatim in the owner's sources; blocked_clinical: medical or legal question, never drafted
        examples (list[str]): Up to 3 questions as callers asked them
        id (UUID):
        knowledge_base_ids (list[str]): Bases attached to the asking agents' versions when the question came up
        last_asked_at (datetime.datetime):
        question (str): Normalised wording of the group
        reasked_count (int):
        state (KnowledgeGapState):
        answered_source_id (UUID | Unset):
        asked_again_at (datetime.datetime | Unset): Last time callers asked this after it was answered or dismissed
        decided_at (datetime.datetime | Unset):
        decided_by_name (str | Unset):
        draft_answer (str | Unset):
        drafted_at (datetime.datetime | Unset):
    """

    assistant_ids: list[str]
    call_ids: list[str]
    count: int
    draft_sources: list[KnowledgeGapDraftSource]
    draft_status: KnowledgeGapDraftStatus
    examples: list[str]
    id: UUID
    knowledge_base_ids: list[str]
    last_asked_at: datetime.datetime
    question: str
    reasked_count: int
    state: KnowledgeGapState
    answered_source_id: UUID | Unset = UNSET
    asked_again_at: datetime.datetime | Unset = UNSET
    decided_at: datetime.datetime | Unset = UNSET
    decided_by_name: str | Unset = UNSET
    draft_answer: str | Unset = UNSET
    drafted_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_ids = self.assistant_ids

        call_ids = self.call_ids

        count = self.count

        draft_sources = []
        for draft_sources_item_data in self.draft_sources:
            draft_sources_item = draft_sources_item_data.to_dict()
            draft_sources.append(draft_sources_item)

        draft_status: str = self.draft_status

        examples = self.examples

        id = str(self.id)

        knowledge_base_ids = self.knowledge_base_ids

        last_asked_at = self.last_asked_at.isoformat()

        question = self.question

        reasked_count = self.reasked_count

        state: str = self.state

        answered_source_id: str | Unset = UNSET
        if not isinstance(self.answered_source_id, Unset):
            answered_source_id = str(self.answered_source_id)

        asked_again_at: str | Unset = UNSET
        if not isinstance(self.asked_again_at, Unset):
            asked_again_at = self.asked_again_at.isoformat()

        decided_at: str | Unset = UNSET
        if not isinstance(self.decided_at, Unset):
            decided_at = self.decided_at.isoformat()

        decided_by_name = self.decided_by_name

        draft_answer = self.draft_answer

        drafted_at: str | Unset = UNSET
        if not isinstance(self.drafted_at, Unset):
            drafted_at = self.drafted_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_ids": assistant_ids,
                "call_ids": call_ids,
                "count": count,
                "draft_sources": draft_sources,
                "draft_status": draft_status,
                "examples": examples,
                "id": id,
                "knowledge_base_ids": knowledge_base_ids,
                "last_asked_at": last_asked_at,
                "question": question,
                "reasked_count": reasked_count,
                "state": state,
            }
        )
        if answered_source_id is not UNSET:
            field_dict["answered_source_id"] = answered_source_id
        if asked_again_at is not UNSET:
            field_dict["asked_again_at"] = asked_again_at
        if decided_at is not UNSET:
            field_dict["decided_at"] = decided_at
        if decided_by_name is not UNSET:
            field_dict["decided_by_name"] = decided_by_name
        if draft_answer is not UNSET:
            field_dict["draft_answer"] = draft_answer
        if drafted_at is not UNSET:
            field_dict["drafted_at"] = drafted_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.knowledge_gap_draft_source import KnowledgeGapDraftSource

        d = dict(src_dict)
        assistant_ids = cast(list[str], d.pop("assistant_ids"))

        call_ids = cast(list[str], d.pop("call_ids"))

        count = d.pop("count")

        draft_sources = []
        _draft_sources = d.pop("draft_sources")
        for draft_sources_item_data in _draft_sources:
            draft_sources_item = KnowledgeGapDraftSource.from_dict(
                draft_sources_item_data
            )

            draft_sources.append(draft_sources_item)

        draft_status = check_knowledge_gap_draft_status(d.pop("draft_status"))

        examples = cast(list[str], d.pop("examples"))

        id = UUID(d.pop("id"))

        knowledge_base_ids = cast(list[str], d.pop("knowledge_base_ids"))

        last_asked_at = datetime.datetime.fromisoformat(d.pop("last_asked_at"))

        question = d.pop("question")

        reasked_count = d.pop("reasked_count")

        state = check_knowledge_gap_state(d.pop("state"))

        _answered_source_id = d.pop("answered_source_id", UNSET)
        answered_source_id: UUID | Unset
        if isinstance(_answered_source_id, Unset):
            answered_source_id = UNSET
        else:
            answered_source_id = UUID(_answered_source_id)

        _asked_again_at = d.pop("asked_again_at", UNSET)
        asked_again_at: datetime.datetime | Unset
        if isinstance(_asked_again_at, Unset):
            asked_again_at = UNSET
        else:
            asked_again_at = datetime.datetime.fromisoformat(_asked_again_at)

        _decided_at = d.pop("decided_at", UNSET)
        decided_at: datetime.datetime | Unset
        if isinstance(_decided_at, Unset):
            decided_at = UNSET
        else:
            decided_at = datetime.datetime.fromisoformat(_decided_at)

        decided_by_name = d.pop("decided_by_name", UNSET)

        draft_answer = d.pop("draft_answer", UNSET)

        _drafted_at = d.pop("drafted_at", UNSET)
        drafted_at: datetime.datetime | Unset
        if isinstance(_drafted_at, Unset):
            drafted_at = UNSET
        else:
            drafted_at = datetime.datetime.fromisoformat(_drafted_at)

        knowledge_gap = cls(
            assistant_ids=assistant_ids,
            call_ids=call_ids,
            count=count,
            draft_sources=draft_sources,
            draft_status=draft_status,
            examples=examples,
            id=id,
            knowledge_base_ids=knowledge_base_ids,
            last_asked_at=last_asked_at,
            question=question,
            reasked_count=reasked_count,
            state=state,
            answered_source_id=answered_source_id,
            asked_again_at=asked_again_at,
            decided_at=decided_at,
            decided_by_name=decided_by_name,
            draft_answer=draft_answer,
            drafted_at=drafted_at,
        )

        return knowledge_gap
