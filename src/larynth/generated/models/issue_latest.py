from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_latest_evidence import IssueLatestEvidence


T = TypeVar("T", bound="IssueLatest")


@_attrs_define
class IssueLatest:
    """
    Attributes:
        at (datetime.datetime):
        evidence (IssueLatestEvidence): turn, at_ms, quote, tool and error where known; the quote is dropped when the
            transcript retention passes
        call_id (str | Unset):
    """

    at: datetime.datetime
    evidence: IssueLatestEvidence
    call_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        evidence = self.evidence.to_dict()

        call_id = self.call_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "evidence": evidence,
            }
        )
        if call_id is not UNSET:
            field_dict["call_id"] = call_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.issue_latest_evidence import IssueLatestEvidence

        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        evidence = IssueLatestEvidence.from_dict(d.pop("evidence"))

        call_id = d.pop("call_id", UNSET)

        issue_latest = cls(
            at=at,
            evidence=evidence,
            call_id=call_id,
        )

        return issue_latest
