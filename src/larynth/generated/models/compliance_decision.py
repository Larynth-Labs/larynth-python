from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.compliance_decision_purpose import (
    ComplianceDecisionPurpose,
    check_compliance_decision_purpose,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceDecision")


@_attrs_define
class ComplianceDecision:
    """
    Attributes:
        allow (bool):
        decided_at (datetime.datetime):
        e164 (str):
        id (UUID):
        purpose (ComplianceDecisionPurpose):
        reason (str):
        rule (str): Deciding rule id, e.g. dial.window.closed
        rules_version (str):
        call_id (str | Unset):
        campaign_id (UUID | Unset):
        retry_at (datetime.datetime | Unset):
    """

    allow: bool
    decided_at: datetime.datetime
    e164: str
    id: UUID
    purpose: ComplianceDecisionPurpose
    reason: str
    rule: str
    rules_version: str
    call_id: str | Unset = UNSET
    campaign_id: UUID | Unset = UNSET
    retry_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allow = self.allow

        decided_at = self.decided_at.isoformat()

        e164 = self.e164

        id = str(self.id)

        purpose: str = self.purpose

        reason = self.reason

        rule = self.rule

        rules_version = self.rules_version

        call_id = self.call_id

        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        retry_at: str | Unset = UNSET
        if not isinstance(self.retry_at, Unset):
            retry_at = self.retry_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "allow": allow,
                "decided_at": decided_at,
                "e164": e164,
                "id": id,
                "purpose": purpose,
                "reason": reason,
                "rule": rule,
                "rules_version": rules_version,
            }
        )
        if call_id is not UNSET:
            field_dict["call_id"] = call_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if retry_at is not UNSET:
            field_dict["retry_at"] = retry_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        allow = d.pop("allow")

        decided_at = datetime.datetime.fromisoformat(d.pop("decided_at"))

        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        purpose = check_compliance_decision_purpose(d.pop("purpose"))

        reason = d.pop("reason")

        rule = d.pop("rule")

        rules_version = d.pop("rules_version")

        call_id = d.pop("call_id", UNSET)

        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        _retry_at = d.pop("retry_at", UNSET)
        retry_at: datetime.datetime | Unset
        if isinstance(_retry_at, Unset):
            retry_at = UNSET
        else:
            retry_at = datetime.datetime.fromisoformat(_retry_at)

        compliance_decision = cls(
            allow=allow,
            decided_at=decided_at,
            e164=e164,
            id=id,
            purpose=purpose,
            reason=reason,
            rule=rule,
            rules_version=rules_version,
            call_id=call_id,
            campaign_id=campaign_id,
            retry_at=retry_at,
        )

        return compliance_decision
