from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.practice_test_outcome_outcome import (
    PracticeTestOutcomeOutcome,
    check_practice_test_outcome_outcome,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PracticeTestOutcome")


@_attrs_define
class PracticeTestOutcome:
    """
    Attributes:
        failed_checks (list[str]): Labels of the checks that failed in any attempt
        name (str):
        outcome (PracticeTestOutcomeOutcome):
        test_id (UUID | Unset): Unset when the practice call was deleted after the run
    """

    failed_checks: list[str]
    name: str
    outcome: PracticeTestOutcomeOutcome
    test_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        failed_checks = self.failed_checks

        name = self.name

        outcome: str = self.outcome

        test_id: str | Unset = UNSET
        if not isinstance(self.test_id, Unset):
            test_id = str(self.test_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "failed_checks": failed_checks,
                "name": name,
                "outcome": outcome,
            }
        )
        if test_id is not UNSET:
            field_dict["test_id"] = test_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        failed_checks = cast(list[str], d.pop("failed_checks"))

        name = d.pop("name")

        outcome = check_practice_test_outcome_outcome(d.pop("outcome"))

        _test_id = d.pop("test_id", UNSET)
        test_id: UUID | Unset
        if isinstance(_test_id, Unset):
            test_id = UNSET
        else:
            test_id = UUID(_test_id)

        practice_test_outcome = cls(
            failed_checks=failed_checks,
            name=name,
            outcome=outcome,
            test_id=test_id,
        )

        return practice_test_outcome
