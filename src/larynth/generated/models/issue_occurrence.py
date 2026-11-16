from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.issue_occurrence_evidence import IssueOccurrenceEvidence


T = TypeVar("T", bound="IssueOccurrence")


@_attrs_define
class IssueOccurrence:
    """
    Attributes:
        at (datetime.datetime):
        call_id (None | str):
        evidence (IssueOccurrenceEvidence):
        id (UUID):
    """

    at: datetime.datetime
    call_id: None | str
    evidence: IssueOccurrenceEvidence
    id: UUID

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        call_id: None | str
        call_id = self.call_id

        evidence = self.evidence.to_dict()

        id = str(self.id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "call_id": call_id,
                "evidence": evidence,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.issue_occurrence_evidence import IssueOccurrenceEvidence

        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        def _parse_call_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        call_id = _parse_call_id(d.pop("call_id"))

        evidence = IssueOccurrenceEvidence.from_dict(d.pop("evidence"))

        id = UUID(d.pop("id"))

        issue_occurrence = cls(
            at=at,
            call_id=call_id,
            evidence=evidence,
            id=id,
        )

        return issue_occurrence
