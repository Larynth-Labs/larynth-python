from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.practice_run_state import PracticeRunState, check_practice_run_state
from ..models.practice_run_target import PracticeRunTarget, check_practice_run_target
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.practice_totals import PracticeTotals


T = TypeVar("T", bound="PracticeRun")


@_attrs_define
class PracticeRun:
    """
    Attributes:
        assistant_id (UUID):
        attempts (int):
        created_at (datetime.datetime):
        id (UUID):
        state (PracticeRunState):
        target (PracticeRunTarget):
        totals (PracticeTotals):
        version (int):
        finished_at (datetime.datetime | Unset):
        started_at (datetime.datetime | Unset):
    """

    assistant_id: UUID
    attempts: int
    created_at: datetime.datetime
    id: UUID
    state: PracticeRunState
    target: PracticeRunTarget
    totals: PracticeTotals
    version: int
    finished_at: datetime.datetime | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        attempts = self.attempts

        created_at = self.created_at.isoformat()

        id = str(self.id)

        state: str = self.state

        target: str = self.target

        totals = self.totals.to_dict()

        version = self.version

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "attempts": attempts,
                "created_at": created_at,
                "id": id,
                "state": state,
                "target": target,
                "totals": totals,
                "version": version,
            }
        )
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.practice_totals import PracticeTotals

        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        attempts = d.pop("attempts")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        state = check_practice_run_state(d.pop("state"))

        target = check_practice_run_target(d.pop("target"))

        totals = PracticeTotals.from_dict(d.pop("totals"))

        version = d.pop("version")

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = datetime.datetime.fromisoformat(_finished_at)

        _started_at = d.pop("started_at", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)

        practice_run = cls(
            assistant_id=assistant_id,
            attempts=attempts,
            created_at=created_at,
            id=id,
            state=state,
            target=target,
            totals=totals,
            version=version,
            finished_at=finished_at,
            started_at=started_at,
        )

        return practice_run
