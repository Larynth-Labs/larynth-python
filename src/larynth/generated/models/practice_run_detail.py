from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.practice_run_detail_error_code import (
    PracticeRunDetailErrorCode,
    check_practice_run_detail_error_code,
)
from ..models.practice_run_detail_state import (
    PracticeRunDetailState,
    check_practice_run_detail_state,
)
from ..models.practice_run_detail_target import (
    PracticeRunDetailTarget,
    check_practice_run_detail_target,
)
from ..models.practice_run_detail_trigger import (
    PracticeRunDetailTrigger,
    check_practice_run_detail_trigger,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.practice_estimate import PracticeEstimate
    from ..models.practice_test_outcome import PracticeTestOutcome
    from ..models.practice_totals import PracticeTotals


T = TypeVar("T", bound="PracticeRunDetail")


@_attrs_define
class PracticeRunDetail:
    """
    Attributes:
        assistant_id (UUID):
        attempts (int):
        created_at (datetime.datetime):
        id (UUID):
        required_only (bool):
        state (PracticeRunDetailState):
        target (PracticeRunDetailTarget):
        tests (list[PracticeTestOutcome]):
        totals (PracticeTotals):
        trigger (PracticeRunDetailTrigger):
        version (int):
        error_code (PracticeRunDetailErrorCode | Unset): Why an errored run stopped, when known:
            practice_run.insufficient_balance means the balance could not cover the next attempt
        estimate (PracticeEstimate | Unset):
        finished_at (datetime.datetime | Unset):
        started_at (datetime.datetime | Unset):
    """

    assistant_id: UUID
    attempts: int
    created_at: datetime.datetime
    id: UUID
    required_only: bool
    state: PracticeRunDetailState
    target: PracticeRunDetailTarget
    tests: list[PracticeTestOutcome]
    totals: PracticeTotals
    trigger: PracticeRunDetailTrigger
    version: int
    error_code: PracticeRunDetailErrorCode | Unset = UNSET
    estimate: PracticeEstimate | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        attempts = self.attempts

        created_at = self.created_at.isoformat()

        id = str(self.id)

        required_only = self.required_only

        state: str = self.state

        target: str = self.target

        tests = []
        for tests_item_data in self.tests:
            tests_item = tests_item_data.to_dict()
            tests.append(tests_item)

        totals = self.totals.to_dict()

        trigger: str = self.trigger

        version = self.version

        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code

        estimate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimate, Unset):
            estimate = self.estimate.to_dict()

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
                "required_only": required_only,
                "state": state,
                "target": target,
                "tests": tests,
                "totals": totals,
                "trigger": trigger,
                "version": version,
            }
        )
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if estimate is not UNSET:
            field_dict["estimate"] = estimate
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if started_at is not UNSET:
            field_dict["started_at"] = started_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.practice_estimate import PracticeEstimate
        from ..models.practice_test_outcome import PracticeTestOutcome
        from ..models.practice_totals import PracticeTotals

        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        attempts = d.pop("attempts")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        required_only = d.pop("required_only")

        state = check_practice_run_detail_state(d.pop("state"))

        target = check_practice_run_detail_target(d.pop("target"))

        tests = []
        _tests = d.pop("tests")
        for tests_item_data in _tests:
            tests_item = PracticeTestOutcome.from_dict(tests_item_data)

            tests.append(tests_item)

        totals = PracticeTotals.from_dict(d.pop("totals"))

        trigger = check_practice_run_detail_trigger(d.pop("trigger"))

        version = d.pop("version")

        _error_code = d.pop("error_code", UNSET)
        error_code: PracticeRunDetailErrorCode | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = check_practice_run_detail_error_code(_error_code)

        _estimate = d.pop("estimate", UNSET)
        estimate: PracticeEstimate | Unset
        if isinstance(_estimate, Unset):
            estimate = UNSET
        else:
            estimate = PracticeEstimate.from_dict(_estimate)

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

        practice_run_detail = cls(
            assistant_id=assistant_id,
            attempts=attempts,
            created_at=created_at,
            id=id,
            required_only=required_only,
            state=state,
            target=target,
            tests=tests,
            totals=totals,
            trigger=trigger,
            version=version,
            error_code=error_code,
            estimate=estimate,
            finished_at=finished_at,
            started_at=started_at,
        )

        return practice_run_detail
