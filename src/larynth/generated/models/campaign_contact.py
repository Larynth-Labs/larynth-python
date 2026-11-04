from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.campaign_contact_state import (
    CampaignContactState,
    check_campaign_contact_state,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_contact_variables import CampaignContactVariables


T = TypeVar("T", bound="CampaignContact")


@_attrs_define
class CampaignContact:
    """
    Attributes:
        attempts (int):
        contact_id (UUID):
        created_at (datetime.datetime):
        e164 (str):
        id (UUID):
        next_attempt_at (datetime.datetime):
        state (CampaignContactState):
        updated_at (datetime.datetime):
        variables (CampaignContactVariables):
        last_call_id (str | Unset):
        last_outcome (str | Unset):
        last_result (str | Unset): Plain result key for the Contacts tab
        last_rule (str | Unset): Rule id of the last compliance denial
        name (str | Unset):
    """

    attempts: int
    contact_id: UUID
    created_at: datetime.datetime
    e164: str
    id: UUID
    next_attempt_at: datetime.datetime
    state: CampaignContactState
    updated_at: datetime.datetime
    variables: CampaignContactVariables
    last_call_id: str | Unset = UNSET
    last_outcome: str | Unset = UNSET
    last_result: str | Unset = UNSET
    last_rule: str | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        contact_id = str(self.contact_id)

        created_at = self.created_at.isoformat()

        e164 = self.e164

        id = str(self.id)

        next_attempt_at = self.next_attempt_at.isoformat()

        state: str = self.state

        updated_at = self.updated_at.isoformat()

        variables = self.variables.to_dict()

        last_call_id = self.last_call_id

        last_outcome = self.last_outcome

        last_result = self.last_result

        last_rule = self.last_rule

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempts": attempts,
                "contact_id": contact_id,
                "created_at": created_at,
                "e164": e164,
                "id": id,
                "next_attempt_at": next_attempt_at,
                "state": state,
                "updated_at": updated_at,
                "variables": variables,
            }
        )
        if last_call_id is not UNSET:
            field_dict["last_call_id"] = last_call_id
        if last_outcome is not UNSET:
            field_dict["last_outcome"] = last_outcome
        if last_result is not UNSET:
            field_dict["last_result"] = last_result
        if last_rule is not UNSET:
            field_dict["last_rule"] = last_rule
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_contact_variables import CampaignContactVariables

        d = dict(src_dict)
        attempts = d.pop("attempts")

        contact_id = UUID(d.pop("contact_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        next_attempt_at = datetime.datetime.fromisoformat(d.pop("next_attempt_at"))

        state = check_campaign_contact_state(d.pop("state"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        variables = CampaignContactVariables.from_dict(d.pop("variables"))

        last_call_id = d.pop("last_call_id", UNSET)

        last_outcome = d.pop("last_outcome", UNSET)

        last_result = d.pop("last_result", UNSET)

        last_rule = d.pop("last_rule", UNSET)

        name = d.pop("name", UNSET)

        campaign_contact = cls(
            attempts=attempts,
            contact_id=contact_id,
            created_at=created_at,
            e164=e164,
            id=id,
            next_attempt_at=next_attempt_at,
            state=state,
            updated_at=updated_at,
            variables=variables,
            last_call_id=last_call_id,
            last_outcome=last_outcome,
            last_result=last_result,
            last_rule=last_rule,
            name=name,
        )

        return campaign_contact
