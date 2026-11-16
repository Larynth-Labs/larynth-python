from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PracticeTotals")


@_attrs_define
class PracticeTotals:
    """
    Attributes:
        errors (int): The practice call could not run
        failed (int): No attempt passed
        mixed (int): Some attempts passed
        passed (int): Every attempt passed
        tests (int):
    """

    errors: int
    failed: int
    mixed: int
    passed: int
    tests: int

    def to_dict(self) -> dict[str, Any]:
        errors = self.errors

        failed = self.failed

        mixed = self.mixed

        passed = self.passed

        tests = self.tests

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "errors": errors,
                "failed": failed,
                "mixed": mixed,
                "passed": passed,
                "tests": tests,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        errors = d.pop("errors")

        failed = d.pop("failed")

        mixed = d.pop("mixed")

        passed = d.pop("passed")

        tests = d.pop("tests")

        practice_totals = cls(
            errors=errors,
            failed=failed,
            mixed=mixed,
            passed=passed,
            tests=tests,
        )

        return practice_totals
