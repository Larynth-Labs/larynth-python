from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.assistant_source import AssistantSource, check_assistant_source
from ..models.assistant_state import AssistantState, check_assistant_state
from ..models.assistant_status import AssistantStatus, check_assistant_status
from ..models.assistant_type import AssistantType, check_assistant_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_coverage import AssistantCoverage
    from ..models.assistant_draft_info import AssistantDraftInfo
    from ..models.assistant_pause import AssistantPause
    from ..models.assistant_published import AssistantPublished


T = TypeVar("T", bound="Assistant")


@_attrs_define
class Assistant:
    """
    Attributes:
        created_at (datetime.datetime):
        has_unpublished_changes (bool):
        id (UUID):
        languages (list[str]): Main language of the current spec, then the languages it switches to
        latency_target_ms (int): Reply-time target the call pages compare against
        latest_version (int):
        name (str):
        number_ids (list[str]): Numbers routed to this assistant
        state (AssistantState):
        status (AssistantStatus):
        type_ (AssistantType): Always single_prompt until flows ship
        updated_at (datetime.datetime):
        archived_at (datetime.datetime | Unset):
        coverage (AssistantCoverage | Unset):
        description (str | Unset): The job line
        draft (AssistantDraftInfo | Unset):
        paused (AssistantPause | Unset):
        published (AssistantPublished | Unset):
        published_version (int | Unset):
        source (AssistantSource | Unset):
    """

    created_at: datetime.datetime
    has_unpublished_changes: bool
    id: UUID
    languages: list[str]
    latency_target_ms: int
    latest_version: int
    name: str
    number_ids: list[str]
    state: AssistantState
    status: AssistantStatus
    type_: AssistantType
    updated_at: datetime.datetime
    archived_at: datetime.datetime | Unset = UNSET
    coverage: AssistantCoverage | Unset = UNSET
    description: str | Unset = UNSET
    draft: AssistantDraftInfo | Unset = UNSET
    paused: AssistantPause | Unset = UNSET
    published: AssistantPublished | Unset = UNSET
    published_version: int | Unset = UNSET
    source: AssistantSource | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        has_unpublished_changes = self.has_unpublished_changes

        id = str(self.id)

        languages = self.languages

        latency_target_ms = self.latency_target_ms

        latest_version = self.latest_version

        name = self.name

        number_ids = self.number_ids

        state: str = self.state

        status: str = self.status

        type_: str = self.type_

        updated_at = self.updated_at.isoformat()

        archived_at: str | Unset = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        coverage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coverage, Unset):
            coverage = self.coverage.to_dict()

        description = self.description

        draft: dict[str, Any] | Unset = UNSET
        if not isinstance(self.draft, Unset):
            draft = self.draft.to_dict()

        paused: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paused, Unset):
            paused = self.paused.to_dict()

        published: dict[str, Any] | Unset = UNSET
        if not isinstance(self.published, Unset):
            published = self.published.to_dict()

        published_version = self.published_version

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "has_unpublished_changes": has_unpublished_changes,
                "id": id,
                "languages": languages,
                "latency_target_ms": latency_target_ms,
                "latest_version": latest_version,
                "name": name,
                "number_ids": number_ids,
                "state": state,
                "status": status,
                "type": type_,
                "updated_at": updated_at,
            }
        )
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if coverage is not UNSET:
            field_dict["coverage"] = coverage
        if description is not UNSET:
            field_dict["description"] = description
        if draft is not UNSET:
            field_dict["draft"] = draft
        if paused is not UNSET:
            field_dict["paused"] = paused
        if published is not UNSET:
            field_dict["published"] = published
        if published_version is not UNSET:
            field_dict["published_version"] = published_version
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assistant_coverage import AssistantCoverage
        from ..models.assistant_draft_info import AssistantDraftInfo
        from ..models.assistant_pause import AssistantPause
        from ..models.assistant_published import AssistantPublished

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        has_unpublished_changes = d.pop("has_unpublished_changes")

        id = UUID(d.pop("id"))

        languages = cast(list[str], d.pop("languages"))

        latency_target_ms = d.pop("latency_target_ms")

        latest_version = d.pop("latest_version")

        name = d.pop("name")

        number_ids = cast(list[str], d.pop("number_ids"))

        state = check_assistant_state(d.pop("state"))

        status = check_assistant_status(d.pop("status"))

        type_ = check_assistant_type(d.pop("type"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _archived_at = d.pop("archived_at", UNSET)
        archived_at: datetime.datetime | Unset
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = datetime.datetime.fromisoformat(_archived_at)

        _coverage = d.pop("coverage", UNSET)
        coverage: AssistantCoverage | Unset
        if isinstance(_coverage, Unset):
            coverage = UNSET
        else:
            coverage = AssistantCoverage.from_dict(_coverage)

        description = d.pop("description", UNSET)

        _draft = d.pop("draft", UNSET)
        draft: AssistantDraftInfo | Unset
        if isinstance(_draft, Unset):
            draft = UNSET
        else:
            draft = AssistantDraftInfo.from_dict(_draft)

        _paused = d.pop("paused", UNSET)
        paused: AssistantPause | Unset
        if isinstance(_paused, Unset):
            paused = UNSET
        else:
            paused = AssistantPause.from_dict(_paused)

        _published = d.pop("published", UNSET)
        published: AssistantPublished | Unset
        if isinstance(_published, Unset):
            published = UNSET
        else:
            published = AssistantPublished.from_dict(_published)

        published_version = d.pop("published_version", UNSET)

        _source = d.pop("source", UNSET)
        source: AssistantSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_assistant_source(_source)

        assistant = cls(
            created_at=created_at,
            has_unpublished_changes=has_unpublished_changes,
            id=id,
            languages=languages,
            latency_target_ms=latency_target_ms,
            latest_version=latest_version,
            name=name,
            number_ids=number_ids,
            state=state,
            status=status,
            type_=type_,
            updated_at=updated_at,
            archived_at=archived_at,
            coverage=coverage,
            description=description,
            draft=draft,
            paused=paused,
            published=published,
            published_version=published_version,
            source=source,
        )

        return assistant
