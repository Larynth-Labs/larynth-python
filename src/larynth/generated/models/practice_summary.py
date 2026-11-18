from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PracticeSummary")


@_attrs_define
class PracticeSummary:
    """
    Attributes:
        failed (int):
        mixed (int):
        passed (int):
        stale (bool): The agent changed after this run, so the line is out of date
        tests_defined (int): Practice calls the agent has; 0 means offer Make practice calls
        total (int):
        ran_at (datetime.datetime | Unset):
        run_id (UUID | Unset): Unset when the version was never practiced
    """

    failed: int
    mixed: int
    passed: int
    stale: bool
    tests_defined: int
    total: int
    ran_at: datetime.datetime | Unset = UNSET
    run_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        failed = self.failed

        mixed = self.mixed

        passed = self.passed

        stale = self.stale

        tests_defined = self.tests_defined

        total = self.total

        ran_at: str | Unset = UNSET
        if not isinstance(self.ran_at, Unset):
            ran_at = self.ran_at.isoformat()

        run_id: str | Unset = UNSET
        if not isinstance(self.run_id, Unset):
            run_id = str(self.run_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "failed": failed,
                "mixed": mixed,
                "passed": passed,
                "stale": stale,
                "tests_defined": tests_defined,
                "total": total,
            }
        )
        if ran_at is not UNSET:
            field_dict["ran_at"] = ran_at
        if run_id is not UNSET:
            field_dict["run_id"] = run_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        failed = d.pop("failed")

        mixed = d.pop("mixed")

        passed = d.pop("passed")

        stale = d.pop("stale")

        tests_defined = d.pop("tests_defined")

        total = d.pop("total")

        _ran_at = d.pop("ran_at", UNSET)
        ran_at: datetime.datetime | Unset
        if isinstance(_ran_at, Unset):
            ran_at = UNSET
        else:
            ran_at = datetime.datetime.fromisoformat(_ran_at)

        _run_id = d.pop("run_id", UNSET)
        run_id: UUID | Unset
        if isinstance(_run_id, Unset):
            run_id = UNSET
        else:
            run_id = UUID(_run_id)

        practice_summary = cls(
            failed=failed,
            mixed=mixed,
            passed=passed,
            stale=stale,
            tests_defined=tests_defined,
            total=total,
            ran_at=ran_at,
            run_id=run_id,
        )

        return practice_summary
