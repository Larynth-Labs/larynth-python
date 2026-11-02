from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.campaign_amd_mode import CampaignAmdMode, check_campaign_amd_mode
from ..models.campaign_paused_reason import (
    CampaignPausedReason,
    check_campaign_paused_reason,
)
from ..models.campaign_purpose import CampaignPurpose, check_campaign_purpose
from ..models.campaign_status import CampaignStatus, check_campaign_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_window import CampaignWindow
    from ..models.retry_policy import RetryPolicy


T = TypeVar("T", bound="Campaign")


@_attrs_define
class Campaign:
    """
    Attributes:
        amd_mode (CampaignAmdMode):
        assistant_id (UUID):
        cps (float):
        created_at (datetime.datetime):
        created_by (str):
        id (UUID):
        max_attempts (int):
        max_concurrent (int):
        name (str):
        number_ids (list[str]):
        purpose (CampaignPurpose):
        retry_policy (RetryPolicy):
        ring_timeout_s (int):
        status (CampaignStatus):
        updated_at (datetime.datetime):
        windows (list[CampaignWindow]):
        amd_profile_id (UUID | Unset):
        archived_at (datetime.datetime | Unset):
        end_at (datetime.datetime | Unset):
        informational_category (str | Unset):
        paused_reason (CampaignPausedReason | Unset):
        start_at (datetime.datetime | Unset):
        voicemail_message (str | Unset):
    """

    amd_mode: CampaignAmdMode
    assistant_id: UUID
    cps: float
    created_at: datetime.datetime
    created_by: str
    id: UUID
    max_attempts: int
    max_concurrent: int
    name: str
    number_ids: list[str]
    purpose: CampaignPurpose
    retry_policy: RetryPolicy
    ring_timeout_s: int
    status: CampaignStatus
    updated_at: datetime.datetime
    windows: list[CampaignWindow]
    amd_profile_id: UUID | Unset = UNSET
    archived_at: datetime.datetime | Unset = UNSET
    end_at: datetime.datetime | Unset = UNSET
    informational_category: str | Unset = UNSET
    paused_reason: CampaignPausedReason | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET
    voicemail_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amd_mode: str = self.amd_mode

        assistant_id = str(self.assistant_id)

        cps = self.cps

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        id = str(self.id)

        max_attempts = self.max_attempts

        max_concurrent = self.max_concurrent

        name = self.name

        number_ids = self.number_ids

        purpose: str = self.purpose

        retry_policy = self.retry_policy.to_dict()

        ring_timeout_s = self.ring_timeout_s

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        windows = []
        for windows_item_data in self.windows:
            windows_item = windows_item_data.to_dict()
            windows.append(windows_item)

        amd_profile_id: str | Unset = UNSET
        if not isinstance(self.amd_profile_id, Unset):
            amd_profile_id = str(self.amd_profile_id)

        archived_at: str | Unset = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        informational_category = self.informational_category

        paused_reason: str | Unset = UNSET
        if not isinstance(self.paused_reason, Unset):
            paused_reason = self.paused_reason

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        voicemail_message = self.voicemail_message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amd_mode": amd_mode,
                "assistant_id": assistant_id,
                "cps": cps,
                "created_at": created_at,
                "created_by": created_by,
                "id": id,
                "max_attempts": max_attempts,
                "max_concurrent": max_concurrent,
                "name": name,
                "number_ids": number_ids,
                "purpose": purpose,
                "retry_policy": retry_policy,
                "ring_timeout_s": ring_timeout_s,
                "status": status,
                "updated_at": updated_at,
                "windows": windows,
            }
        )
        if amd_profile_id is not UNSET:
            field_dict["amd_profile_id"] = amd_profile_id
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if informational_category is not UNSET:
            field_dict["informational_category"] = informational_category
        if paused_reason is not UNSET:
            field_dict["paused_reason"] = paused_reason
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if voicemail_message is not UNSET:
            field_dict["voicemail_message"] = voicemail_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_window import CampaignWindow
        from ..models.retry_policy import RetryPolicy

        d = dict(src_dict)
        amd_mode = check_campaign_amd_mode(d.pop("amd_mode"))

        assistant_id = UUID(d.pop("assistant_id"))

        cps = d.pop("cps")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by = d.pop("created_by")

        id = UUID(d.pop("id"))

        max_attempts = d.pop("max_attempts")

        max_concurrent = d.pop("max_concurrent")

        name = d.pop("name")

        number_ids = cast(list[str], d.pop("number_ids"))

        purpose = check_campaign_purpose(d.pop("purpose"))

        retry_policy = RetryPolicy.from_dict(d.pop("retry_policy"))

        ring_timeout_s = d.pop("ring_timeout_s")

        status = check_campaign_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        windows = []
        _windows = d.pop("windows")
        for windows_item_data in _windows:
            windows_item = CampaignWindow.from_dict(windows_item_data)

            windows.append(windows_item)

        _amd_profile_id = d.pop("amd_profile_id", UNSET)
        amd_profile_id: UUID | Unset
        if isinstance(_amd_profile_id, Unset):
            amd_profile_id = UNSET
        else:
            amd_profile_id = UUID(_amd_profile_id)

        _archived_at = d.pop("archived_at", UNSET)
        archived_at: datetime.datetime | Unset
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = datetime.datetime.fromisoformat(_archived_at)

        _end_at = d.pop("end_at", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)

        informational_category = d.pop("informational_category", UNSET)

        _paused_reason = d.pop("paused_reason", UNSET)
        paused_reason: CampaignPausedReason | Unset
        if isinstance(_paused_reason, Unset):
            paused_reason = UNSET
        else:
            paused_reason = check_campaign_paused_reason(_paused_reason)

        _start_at = d.pop("start_at", UNSET)
        start_at: datetime.datetime | Unset
        if isinstance(_start_at, Unset):
            start_at = UNSET
        else:
            start_at = datetime.datetime.fromisoformat(_start_at)

        voicemail_message = d.pop("voicemail_message", UNSET)

        campaign = cls(
            amd_mode=amd_mode,
            assistant_id=assistant_id,
            cps=cps,
            created_at=created_at,
            created_by=created_by,
            id=id,
            max_attempts=max_attempts,
            max_concurrent=max_concurrent,
            name=name,
            number_ids=number_ids,
            purpose=purpose,
            retry_policy=retry_policy,
            ring_timeout_s=ring_timeout_s,
            status=status,
            updated_at=updated_at,
            windows=windows,
            amd_profile_id=amd_profile_id,
            archived_at=archived_at,
            end_at=end_at,
            informational_category=informational_category,
            paused_reason=paused_reason,
            start_at=start_at,
            voicemail_message=voicemail_message,
        )

        return campaign
