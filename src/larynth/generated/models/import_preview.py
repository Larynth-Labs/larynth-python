from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.import_problem import ImportProblem


T = TypeVar("T", bound="ImportPreview")


@_attrs_define
class ImportPreview:
    """
    Attributes:
        dnc (int): Saved but not called
        duplicate_in_file (int):
        existing_updated (int): Existing contacts keep their details and gain this import's consent record
        invalid (int):
        non_us (int):
        problems (list[ImportProblem]):
        ready (int):
        rows_total (int):
    """

    dnc: int
    duplicate_in_file: int
    existing_updated: int
    invalid: int
    non_us: int
    problems: list[ImportProblem]
    ready: int
    rows_total: int

    def to_dict(self) -> dict[str, Any]:
        dnc = self.dnc

        duplicate_in_file = self.duplicate_in_file

        existing_updated = self.existing_updated

        invalid = self.invalid

        non_us = self.non_us

        problems = []
        for problems_item_data in self.problems:
            problems_item = problems_item_data.to_dict()
            problems.append(problems_item)

        ready = self.ready

        rows_total = self.rows_total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dnc": dnc,
                "duplicate_in_file": duplicate_in_file,
                "existing_updated": existing_updated,
                "invalid": invalid,
                "non_us": non_us,
                "problems": problems,
                "ready": ready,
                "rows_total": rows_total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.import_problem import ImportProblem

        d = dict(src_dict)
        dnc = d.pop("dnc")

        duplicate_in_file = d.pop("duplicate_in_file")

        existing_updated = d.pop("existing_updated")

        invalid = d.pop("invalid")

        non_us = d.pop("non_us")

        problems = []
        _problems = d.pop("problems")
        for problems_item_data in _problems:
            problems_item = ImportProblem.from_dict(problems_item_data)

            problems.append(problems_item)

        ready = d.pop("ready")

        rows_total = d.pop("rows_total")

        import_preview = cls(
            dnc=dnc,
            duplicate_in_file=duplicate_in_file,
            existing_updated=existing_updated,
            invalid=invalid,
            non_us=non_us,
            problems=problems,
            ready=ready,
            rows_total=rows_total,
        )

        return import_preview
