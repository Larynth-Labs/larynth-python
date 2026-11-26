from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.call_unbacked_claim_claimed import (
    CallUnbackedClaimClaimed,
    check_call_unbacked_claim_claimed,
)
from ..models.call_unbacked_claim_reason import (
    CallUnbackedClaimReason,
    check_call_unbacked_claim_reason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallUnbackedClaim")


@_attrs_define
class CallUnbackedClaim:
    """
    Attributes:
        claimed (CallUnbackedClaimClaimed):
        issue_id (UUID):
        reason (CallUnbackedClaimReason):
        turn (int):
        quote (str | Unset): What the agent said; dropped when the transcript retention passes
    """

    claimed: CallUnbackedClaimClaimed
    issue_id: UUID
    reason: CallUnbackedClaimReason
    turn: int
    quote: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        claimed: str = self.claimed

        issue_id = str(self.issue_id)

        reason: str = self.reason

        turn = self.turn

        quote = self.quote

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "claimed": claimed,
                "issue_id": issue_id,
                "reason": reason,
                "turn": turn,
            }
        )
        if quote is not UNSET:
            field_dict["quote"] = quote

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        claimed = check_call_unbacked_claim_claimed(d.pop("claimed"))

        issue_id = UUID(d.pop("issue_id"))

        reason = check_call_unbacked_claim_reason(d.pop("reason"))

        turn = d.pop("turn")

        quote = d.pop("quote", UNSET)

        call_unbacked_claim = cls(
            claimed=claimed,
            issue_id=issue_id,
            reason=reason,
            turn=turn,
            quote=quote,
        )

        return call_unbacked_claim
