from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.update_campaign_request_amd_mode import (
    UpdateCampaignRequestAmdMode,
    check_update_campaign_request_amd_mode,
)
from ..models.update_campaign_request_purpose import (
    UpdateCampaignRequestPurpose,
    check_update_campaign_request_purpose,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audience import Audience
    from ..models.campaign_voicemail import CampaignVoicemail
    from ..models.campaign_window import CampaignWindow
    from ..models.retry_policy import RetryPolicy


T = TypeVar("T", bound="UpdateCampaignRequest")


@_attrs_define
class UpdateCampaignRequest:
    """
    Attributes:
        amd_mode (UpdateCampaignRequestAmdMode | Unset): agent uses the agent call_handling voicemail setting; unset on
            create is agent
        amd_profile_id (UUID | Unset):
        assistant_id (UUID | Unset):
        audience (Audience | Unset):
        cps (float | Unset):
        end_at (datetime.datetime | Unset):
        informational_category (str | Unset): Draft informational campaigns only; empty clears it
        max_attempts (int | Unset):
        max_calls_per_day (int | Unset): Per person per rolling 24 h; marketing is always 1
        max_concurrent (int | Unset):
        name (str | Unset):
        number_ids (list[str] | Unset): Caller-ID pool; every number must have usage.can_call_out
        purpose (UpdateCampaignRequestPurpose | Unset): Draft campaigns only; 409 campaign.locked otherwise. Switching
            to telemarketing clears informational_category
        retry_policy (RetryPolicy | Unset):
        ring_timeout_s (int | Unset):
        start_at (datetime.datetime | Unset):
        voicemail (CampaignVoicemail | Unset):
        voicemail_message (str | Unset):
        windows (list[CampaignWindow] | Unset): Further restricts the legal calling windows
    """

    amd_mode: UpdateCampaignRequestAmdMode | Unset = UNSET
    amd_profile_id: UUID | Unset = UNSET
    assistant_id: UUID | Unset = UNSET
    audience: Audience | Unset = UNSET
    cps: float | Unset = UNSET
    end_at: datetime.datetime | Unset = UNSET
    informational_category: str | Unset = UNSET
    max_attempts: int | Unset = UNSET
    max_calls_per_day: int | Unset = UNSET
    max_concurrent: int | Unset = UNSET
    name: str | Unset = UNSET
    number_ids: list[str] | Unset = UNSET
    purpose: UpdateCampaignRequestPurpose | Unset = UNSET
    retry_policy: RetryPolicy | Unset = UNSET
    ring_timeout_s: int | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET
    voicemail: CampaignVoicemail | Unset = UNSET
    voicemail_message: str | Unset = UNSET
    windows: list[CampaignWindow] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amd_mode: str | Unset = UNSET
        if not isinstance(self.amd_mode, Unset):
            amd_mode = self.amd_mode

        amd_profile_id: str | Unset = UNSET
        if not isinstance(self.amd_profile_id, Unset):
            amd_profile_id = str(self.amd_profile_id)

        assistant_id: str | Unset = UNSET
        if not isinstance(self.assistant_id, Unset):
            assistant_id = str(self.assistant_id)

        audience: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audience, Unset):
            audience = self.audience.to_dict()

        cps = self.cps

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        informational_category = self.informational_category

        max_attempts = self.max_attempts

        max_calls_per_day = self.max_calls_per_day

        max_concurrent = self.max_concurrent

        name = self.name

        number_ids: list[str] | Unset = UNSET
        if not isinstance(self.number_ids, Unset):
            number_ids = self.number_ids

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose

        retry_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_policy, Unset):
            retry_policy = self.retry_policy.to_dict()

        ring_timeout_s = self.ring_timeout_s

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        voicemail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voicemail, Unset):
            voicemail = self.voicemail.to_dict()

        voicemail_message = self.voicemail_message

        windows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.windows, Unset):
            windows = []
            for windows_item_data in self.windows:
                windows_item = windows_item_data.to_dict()
                windows.append(windows_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if amd_mode is not UNSET:
            field_dict["amd_mode"] = amd_mode
        if amd_profile_id is not UNSET:
            field_dict["amd_profile_id"] = amd_profile_id
        if assistant_id is not UNSET:
            field_dict["assistant_id"] = assistant_id
        if audience is not UNSET:
            field_dict["audience"] = audience
        if cps is not UNSET:
            field_dict["cps"] = cps
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if informational_category is not UNSET:
            field_dict["informational_category"] = informational_category
        if max_attempts is not UNSET:
            field_dict["max_attempts"] = max_attempts
        if max_calls_per_day is not UNSET:
            field_dict["max_calls_per_day"] = max_calls_per_day
        if max_concurrent is not UNSET:
            field_dict["max_concurrent"] = max_concurrent
        if name is not UNSET:
            field_dict["name"] = name
        if number_ids is not UNSET:
            field_dict["number_ids"] = number_ids
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if retry_policy is not UNSET:
            field_dict["retry_policy"] = retry_policy
        if ring_timeout_s is not UNSET:
            field_dict["ring_timeout_s"] = ring_timeout_s
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if voicemail is not UNSET:
            field_dict["voicemail"] = voicemail
        if voicemail_message is not UNSET:
            field_dict["voicemail_message"] = voicemail_message
        if windows is not UNSET:
            field_dict["windows"] = windows

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audience import Audience
        from ..models.campaign_voicemail import CampaignVoicemail
        from ..models.campaign_window import CampaignWindow
        from ..models.retry_policy import RetryPolicy

        d = dict(src_dict)
        _amd_mode = d.pop("amd_mode", UNSET)
        amd_mode: UpdateCampaignRequestAmdMode | Unset
        if isinstance(_amd_mode, Unset):
            amd_mode = UNSET
        else:
            amd_mode = check_update_campaign_request_amd_mode(_amd_mode)

        _amd_profile_id = d.pop("amd_profile_id", UNSET)
        amd_profile_id: UUID | Unset
        if isinstance(_amd_profile_id, Unset):
            amd_profile_id = UNSET
        else:
            amd_profile_id = UUID(_amd_profile_id)

        _assistant_id = d.pop("assistant_id", UNSET)
        assistant_id: UUID | Unset
        if isinstance(_assistant_id, Unset):
            assistant_id = UNSET
        else:
            assistant_id = UUID(_assistant_id)

        _audience = d.pop("audience", UNSET)
        audience: Audience | Unset
        if isinstance(_audience, Unset):
            audience = UNSET
        else:
            audience = Audience.from_dict(_audience)

        cps = d.pop("cps", UNSET)

        _end_at = d.pop("end_at", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)

        informational_category = d.pop("informational_category", UNSET)

        max_attempts = d.pop("max_attempts", UNSET)

        max_calls_per_day = d.pop("max_calls_per_day", UNSET)

        max_concurrent = d.pop("max_concurrent", UNSET)

        name = d.pop("name", UNSET)

        number_ids = cast(list[str], d.pop("number_ids", UNSET))

        _purpose = d.pop("purpose", UNSET)
        purpose: UpdateCampaignRequestPurpose | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = check_update_campaign_request_purpose(_purpose)

        _retry_policy = d.pop("retry_policy", UNSET)
        retry_policy: RetryPolicy | Unset
        if isinstance(_retry_policy, Unset):
            retry_policy = UNSET
        else:
            retry_policy = RetryPolicy.from_dict(_retry_policy)

        ring_timeout_s = d.pop("ring_timeout_s", UNSET)

        _start_at = d.pop("start_at", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at, Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)

        _voicemail = d.pop("voicemail", UNSET)
        voicemail: CampaignVoicemail | Unset
        if isinstance(_voicemail, Unset):
            voicemail = UNSET
        else:
            voicemail = CampaignVoicemail.from_dict(_voicemail)

        voicemail_message = d.pop("voicemail_message", UNSET)

        _windows = d.pop("windows", UNSET)
        windows: list[CampaignWindow] | Unset = UNSET
        if _windows is not UNSET:
            windows = []
            for windows_item_data in _windows:
                windows_item = CampaignWindow.from_dict(windows_item_data)

                windows.append(windows_item)

        update_campaign_request = cls(
            amd_mode=amd_mode,
            amd_profile_id=amd_profile_id,
            assistant_id=assistant_id,
            audience=audience,
            cps=cps,
            end_at=end_at,
            informational_category=informational_category,
            max_attempts=max_attempts,
            max_calls_per_day=max_calls_per_day,
            max_concurrent=max_concurrent,
            name=name,
            number_ids=number_ids,
            purpose=purpose,
            retry_policy=retry_policy,
            ring_timeout_s=ring_timeout_s,
            start_at=start_at,
            voicemail=voicemail,
            voicemail_message=voicemail_message,
            windows=windows,
        )

        return update_campaign_request
