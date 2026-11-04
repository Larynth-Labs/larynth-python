from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.dnc_import_status import DncImportStatus, check_dnc_import_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="DncImport")


@_attrs_define
class DncImport:
    """
    Attributes:
        created_at (datetime.datetime):
        id (UUID):
        rows_added (int):
        rows_rejected (int):
        rows_total (int):
        status (DncImportStatus):
        finished_at (datetime.datetime | Unset):
    """

    created_at: datetime.datetime
    id: UUID
    rows_added: int
    rows_rejected: int
    rows_total: int
    status: DncImportStatus
    finished_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        id = str(self.id)

        rows_added = self.rows_added

        rows_rejected = self.rows_rejected

        rows_total = self.rows_total

        status: str = self.status

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "rows_added": rows_added,
                "rows_rejected": rows_rejected,
                "rows_total": rows_total,
                "status": status,
            }
        )
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        rows_added = d.pop("rows_added")

        rows_rejected = d.pop("rows_rejected")

        rows_total = d.pop("rows_total")

        status = check_dnc_import_status(d.pop("status"))

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = datetime.datetime.fromisoformat(_finished_at)

        dnc_import = cls(
            created_at=created_at,
            id=id,
            rows_added=rows_added,
            rows_rejected=rows_rejected,
            rows_total=rows_total,
            status=status,
            finished_at=finished_at,
        )

        return dnc_import
