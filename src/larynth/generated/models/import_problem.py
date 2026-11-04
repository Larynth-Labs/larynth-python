from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.import_problem_kind import ImportProblemKind, check_import_problem_kind

T = TypeVar("T", bound="ImportProblem")


@_attrs_define
class ImportProblem:
    """
    Attributes:
        kind (ImportProblemKind):
        reason_code (str):
        row (int):
        value_masked (str):
    """

    kind: ImportProblemKind
    reason_code: str
    row: int
    value_masked: str

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        reason_code = self.reason_code

        row = self.row

        value_masked = self.value_masked

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "reason_code": reason_code,
                "row": row,
                "value_masked": value_masked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_import_problem_kind(d.pop("kind"))

        reason_code = d.pop("reason_code")

        row = d.pop("row")

        value_masked = d.pop("value_masked")

        import_problem = cls(
            kind=kind,
            reason_code=reason_code,
            row=row,
            value_masked=value_masked,
        )

        return import_problem
