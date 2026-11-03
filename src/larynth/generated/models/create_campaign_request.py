from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.create_campaign_request_amd_mode import (
    CreateCampaignRequestAmdMode,
    check_create_campaign_request_amd_mode,
)
from ..models.create_campaign_request_purpose import (
    CreateCampaignRequestPurpose,
    check_create_campaign_request_purpose,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_window import CampaignWindow
    from ..models.retry_policy import RetryPolicy


T = TypeVar("T", bound="CreateCampaignRequest")


@_attrs_define
class CreateCampaignRequest:
    """
    Attributes:
        assistant_id (UUID):
        name (str):
        purpose (CreateCampaignRequestPurpose):
        amd_mode (CreateCampaignRequestAmdMode | Unset): agent uses the agent call_handling voicemail setting; unset on
            create is agent
        amd_profile_id (UUID | Unset):
        cps (float | Unset):
        end_at (datetime.datetime | Unset):
        informational_category (str | Unset): Informational campaigns only: the category an opt-out on this campaign
            revokes (FCC 26-67). Empty means an opt-out revokes every call
        max_attempts (int | Unset):
        max_concurrent (int | Unset):
        number_ids (list[str] | Unset): Caller-ID pool
        retry_policy (RetryPolicy | Unset):
        ring_timeout_s (int | Unset):
        start_at (datetime.datetime | Unset):
        voicemail_message (str | Unset):
        windows (list[CampaignWindow] | Unset): Further restricts the legal calling windows
    """

    assistant_id: UUID
    name: str
    purpose: CreateCampaignRequestPurpose
    amd_mode: CreateCampaignRequestAmdMode | Unset = UNSET
    amd_profile_id: UUID | Unset = UNSET
    cps: float | Unset = UNSET
    end_at: datetime.datetime | Unset = UNSET
    informational_category: str | Unset = UNSET
    max_attempts: int | Unset = UNSET
    max_concurrent: int | Unset = UNSET
    number_ids: list[str] | Unset = UNSET
    retry_policy: RetryPolicy | Unset = UNSET
    ring_timeout_s: int | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET
    voicemail_message: str | Unset = UNSET
    windows: list[CampaignWindow] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        name = self.name

        purpose: str = self.purpose

        amd_mode: str | Unset = UNSET
        if not isinstance(self.amd_mode, Unset):
            amd_mode = self.amd_mode

        amd_profile_id: str | Unset = UNSET
        if not isinstance(self.amd_profile_id, Unset):
            amd_profile_id = str(self.amd_profile_id)

        cps = self.cps

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        informational_category = self.informational_category

        max_attempts = self.max_attempts

        max_concurrent = self.max_concurrent

        number_ids: list[str] | Unset = UNSET
        if not isinstance(self.number_ids, Unset):
            number_ids = self.number_ids

        retry_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_policy, Unset):
            retry_policy = self.retry_policy.to_dict()

        ring_timeout_s = self.ring_timeout_s

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        voicemail_message = self.voicemail_message

        windows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.windows, Unset):
            windows = []
            for windows_item_data in self.windows:
                windows_item = windows_item_data.to_dict()
                windows.append(windows_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "name": name,
                "purpose": purpose,
            }
        )
        if amd_mode is not UNSET:
            field_dict["amd_mode"] = amd_mode
        if amd_profile_id is not UNSET:
            field_dict["amd_profile_id"] = amd_profile_id
        if cps is not UNSET:
            field_dict["cps"] = cps
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if informational_category is not UNSET:
            field_dict["informational_category"] = informational_category
        if max_attempts is not UNSET:
            field_dict["max_attempts"] = max_attempts
        if max_concurrent is not UNSET:
            field_dict["max_concurrent"] = max_concurrent
        if number_ids is not UNSET:
            field_dict["number_ids"] = number_ids
        if retry_policy is not UNSET:
            field_dict["retry_policy"] = retry_policy
        if ring_timeout_s is not UNSET:
            field_dict["ring_timeout_s"] = ring_timeout_s
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if voicemail_message is not UNSET:
            field_dict["voicemail_message"] = voicemail_message
        if windows is not UNSET:
            field_dict["windows"] = windows

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_window import CampaignWindow
        from ..models.retry_policy import RetryPolicy

        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        name = d.pop("name")

        purpose = check_create_campaign_request_purpose(d.pop("purpose"))

        _amd_mode = d.pop("amd_mode", UNSET)
        amd_mode: CreateCampaignRequestAmdMode | Unset
        if isinstance(_amd_mode, Unset):
            amd_mode = UNSET
        else:
            amd_mode = check_create_campaign_request_amd_mode(_amd_mode)

        _amd_profile_id = d.pop("amd_profile_id", UNSET)
        amd_profile_id: UUID | Unset
        if isinstance(_amd_profile_id, Unset):
            amd_profile_id = UNSET
        else:
            amd_profile_id = UUID(_amd_profile_id)

        cps = d.pop("cps", UNSET)

        _end_at = d.pop("end_at", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)

        informational_category = d.pop("informational_category", UNSET)

        max_attempts = d.pop("max_attempts", UNSET)

        max_concurrent = d.pop("max_concurrent", UNSET)

        number_ids = cast(list[str], d.pop("number_ids", UNSET))

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

        voicemail_message = d.pop("voicemail_message", UNSET)

        _windows = d.pop("windows", UNSET)
        windows: list[CampaignWindow] | Unset = UNSET
        if _windows is not UNSET:
            windows = []
            for windows_item_data in _windows:
                windows_item = CampaignWindow.from_dict(windows_item_data)

                windows.append(windows_item)

        create_campaign_request = cls(
            assistant_id=assistant_id,
            name=name,
            purpose=purpose,
            amd_mode=amd_mode,
            amd_profile_id=amd_profile_id,
            cps=cps,
            end_at=end_at,
            informational_category=informational_category,
            max_attempts=max_attempts,
            max_concurrent=max_concurrent,
            number_ids=number_ids,
            retry_policy=retry_policy,
            ring_timeout_s=ring_timeout_s,
            start_at=start_at,
            voicemail_message=voicemail_message,
            windows=windows,
        )

        return create_campaign_request
