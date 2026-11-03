from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.skipped_count import SkippedCount


T = TypeVar("T", bound="BulkResult")


@_attrs_define
class BulkResult:
    """
    Attributes:
        affected (int):
        skipped (list[SkippedCount]):
        job_id (UUID | Unset): Set when the selection runs as a job; results arrive by notification
    """

    affected: int
    skipped: list[SkippedCount]
    job_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

        skipped = []
        for skipped_item_data in self.skipped:
            skipped_item = skipped_item_data.to_dict()
            skipped.append(skipped_item)

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "affected": affected,
                "skipped": skipped,
            }
        )
        if job_id is not UNSET:
            field_dict["job_id"] = job_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.skipped_count import SkippedCount

        d = dict(src_dict)
        affected = d.pop("affected")

        skipped = []
        _skipped = d.pop("skipped")
        for skipped_item_data in _skipped:
            skipped_item = SkippedCount.from_dict(skipped_item_data)

            skipped.append(skipped_item)

        _job_id = d.pop("job_id", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id, Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)

        bulk_result = cls(
            affected=affected,
            skipped=skipped,
            job_id=job_id,
        )

        return bulk_result
