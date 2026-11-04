from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.create_call_request_amd_mode import (
    CreateCallRequestAmdMode,
    check_create_call_request_amd_mode,
)
from ..models.create_call_request_purpose import (
    CreateCallRequestPurpose,
    check_create_call_request_purpose,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_call_request_variables import CreateCallRequestVariables


T = TypeVar("T", bound="CreateCallRequest")


@_attrs_define
class CreateCallRequest:
    """
    Attributes:
        assistant_id (UUID): The published version is used
        from_e164 (str): Must be an active number of this tenant
        purpose (CreateCallRequestPurpose):
        to_e164 (str):
        amd_mode (CreateCallRequestAmdMode | Unset): Overrides the agent voicemail setting; unset uses the agent
            call_handling
        amd_profile_id (UUID | Unset):
        contact_id (UUID | Unset):
        ring_timeout_s (int | Unset):  Default: 30.
        variables (CreateCallRequestVariables | Unset):
        voicemail_message (str | Unset): Overrides the agent voicemail message
    """

    assistant_id: UUID
    from_e164: str
    purpose: CreateCallRequestPurpose
    to_e164: str
    amd_mode: CreateCallRequestAmdMode | Unset = UNSET
    amd_profile_id: UUID | Unset = UNSET
    contact_id: UUID | Unset = UNSET
    ring_timeout_s: int | Unset = 30
    variables: CreateCallRequestVariables | Unset = UNSET
    voicemail_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        from_e164 = self.from_e164

        purpose: str = self.purpose

        to_e164 = self.to_e164

        amd_mode: str | Unset = UNSET
        if not isinstance(self.amd_mode, Unset):
            amd_mode = self.amd_mode

        amd_profile_id: str | Unset = UNSET
        if not isinstance(self.amd_profile_id, Unset):
            amd_profile_id = str(self.amd_profile_id)

        contact_id: str | Unset = UNSET
        if not isinstance(self.contact_id, Unset):
            contact_id = str(self.contact_id)

        ring_timeout_s = self.ring_timeout_s

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        voicemail_message = self.voicemail_message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "from_e164": from_e164,
                "purpose": purpose,
                "to_e164": to_e164,
            }
        )
        if amd_mode is not UNSET:
            field_dict["amd_mode"] = amd_mode
        if amd_profile_id is not UNSET:
            field_dict["amd_profile_id"] = amd_profile_id
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if ring_timeout_s is not UNSET:
            field_dict["ring_timeout_s"] = ring_timeout_s
        if variables is not UNSET:
            field_dict["variables"] = variables
        if voicemail_message is not UNSET:
            field_dict["voicemail_message"] = voicemail_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_call_request_variables import CreateCallRequestVariables

        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        from_e164 = d.pop("from_e164")

        purpose = check_create_call_request_purpose(d.pop("purpose"))

        to_e164 = d.pop("to_e164")

        _amd_mode = d.pop("amd_mode", UNSET)
        amd_mode: CreateCallRequestAmdMode | Unset
        if isinstance(_amd_mode, Unset):
            amd_mode = UNSET
        else:
            amd_mode = check_create_call_request_amd_mode(_amd_mode)

        _amd_profile_id = d.pop("amd_profile_id", UNSET)
        amd_profile_id: UUID | Unset
        if isinstance(_amd_profile_id, Unset):
            amd_profile_id = UNSET
        else:
            amd_profile_id = UUID(_amd_profile_id)

        _contact_id = d.pop("contact_id", UNSET)
        contact_id: UUID | Unset
        if isinstance(_contact_id, Unset):
            contact_id = UNSET
        else:
            contact_id = UUID(_contact_id)

        ring_timeout_s = d.pop("ring_timeout_s", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: CreateCallRequestVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = CreateCallRequestVariables.from_dict(_variables)

        voicemail_message = d.pop("voicemail_message", UNSET)

        create_call_request = cls(
            assistant_id=assistant_id,
            from_e164=from_e164,
            purpose=purpose,
            to_e164=to_e164,
            amd_mode=amd_mode,
            amd_profile_id=amd_profile_id,
            contact_id=contact_id,
            ring_timeout_s=ring_timeout_s,
            variables=variables,
            voicemail_message=voicemail_message,
        )

        return create_call_request
