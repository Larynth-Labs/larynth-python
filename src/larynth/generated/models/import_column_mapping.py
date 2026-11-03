from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.import_column_mapping_target import (
    ImportColumnMappingTarget,
    check_import_column_mapping_target,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportColumnMapping")


@_attrs_define
class ImportColumnMapping:
    """
    Attributes:
        column (str):
        target (ImportColumnMappingTarget):
        key (str | Unset): Variable name for attr
    """

    column: str
    target: ImportColumnMappingTarget
    key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        column = self.column

        target: str = self.target

        key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "column": column,
                "target": target,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        column = d.pop("column")

        target = check_import_column_mapping_target(d.pop("target"))

        key = d.pop("key", UNSET)

        import_column_mapping = cls(
            column=column,
            target=target,
            key=key,
        )

        return import_column_mapping
