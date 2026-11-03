from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.campaign_amd_mode import CampaignAmdMode, check_campaign_amd_mode
from ..models.campaign_display_status import (
    CampaignDisplayStatus,
    check_campaign_display_status,
)
from ..models.campaign_paused_reason import (
    CampaignPausedReason,
    check_campaign_paused_reason,
)
from ..models.campaign_purpose import CampaignPurpose, check_campaign_purpose
from ..models.campaign_status import CampaignStatus, check_campaign_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audience import Audience
    from ..models.campaign_launch import CampaignLaunch
    from ..models.campaign_progress import CampaignProgress
    from ..models.campaign_safeguard import CampaignSafeguard
    from ..models.campaign_voicemail import CampaignVoicemail
    from ..models.campaign_window import CampaignWindow
    from ..models.preflight_check import PreflightCheck
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
        spend_micro (int):
        status (CampaignStatus):
        updated_at (datetime.datetime):
        windows (list[CampaignWindow]):
        abandonment_rate_30d (float | Unset):
        agent_name (str | Unset):
        amd_profile_id (UUID | Unset):
        answer_rate (float | Unset):
        archived_at (datetime.datetime | Unset):
        audience (Audience | Unset):
        blockers (list[PreflightCheck] | Unset): Stop checks only, for list rows
        display_status (CampaignDisplayStatus | Unset):
        duplicated_from (UUID | Unset):
        end_at (datetime.datetime | Unset):
        informational_category (str | Unset):
        launch (CampaignLaunch | Unset):
        max_calls_per_day (int | Unset):
        next_window_at (datetime.datetime | Unset):
        optout_rate (float | Unset):
        paused_reason (CampaignPausedReason | Unset):
        progress (CampaignProgress | Unset):
        revision (int | Unset): Send back as If-Match on updateCampaign
        safeguard (CampaignSafeguard | Unset):
        start_at (datetime.datetime | Unset):
        voicemail (CampaignVoicemail | Unset):
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
    spend_micro: int
    status: CampaignStatus
    updated_at: datetime.datetime
    windows: list[CampaignWindow]
    abandonment_rate_30d: float | Unset = UNSET
    agent_name: str | Unset = UNSET
    amd_profile_id: UUID | Unset = UNSET
    answer_rate: float | Unset = UNSET
    archived_at: datetime.datetime | Unset = UNSET
    audience: Audience | Unset = UNSET
    blockers: list[PreflightCheck] | Unset = UNSET
    display_status: CampaignDisplayStatus | Unset = UNSET
    duplicated_from: UUID | Unset = UNSET
    end_at: datetime.datetime | Unset = UNSET
    informational_category: str | Unset = UNSET
    launch: CampaignLaunch | Unset = UNSET
    max_calls_per_day: int | Unset = UNSET
    next_window_at: datetime.datetime | Unset = UNSET
    optout_rate: float | Unset = UNSET
    paused_reason: CampaignPausedReason | Unset = UNSET
    progress: CampaignProgress | Unset = UNSET
    revision: int | Unset = UNSET
    safeguard: CampaignSafeguard | Unset = UNSET
    start_at: datetime.datetime | Unset = UNSET
    voicemail: CampaignVoicemail | Unset = UNSET
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

        spend_micro = self.spend_micro

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        windows = []
        for windows_item_data in self.windows:
            windows_item = windows_item_data.to_dict()
            windows.append(windows_item)

        abandonment_rate_30d = self.abandonment_rate_30d

        agent_name = self.agent_name

        amd_profile_id: str | Unset = UNSET
        if not isinstance(self.amd_profile_id, Unset):
            amd_profile_id = str(self.amd_profile_id)

        answer_rate = self.answer_rate

        archived_at: str | Unset = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        audience: dict[str, Any] | Unset = UNSET
        if not isinstance(self.audience, Unset):
            audience = self.audience.to_dict()

        blockers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blockers, Unset):
            blockers = []
            for blockers_item_data in self.blockers:
                blockers_item = blockers_item_data.to_dict()
                blockers.append(blockers_item)

        display_status: str | Unset = UNSET
        if not isinstance(self.display_status, Unset):
            display_status = self.display_status

        duplicated_from: str | Unset = UNSET
        if not isinstance(self.duplicated_from, Unset):
            duplicated_from = str(self.duplicated_from)

        end_at: str | Unset = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        informational_category = self.informational_category

        launch: dict[str, Any] | Unset = UNSET
        if not isinstance(self.launch, Unset):
            launch = self.launch.to_dict()

        max_calls_per_day = self.max_calls_per_day

        next_window_at: str | Unset = UNSET
        if not isinstance(self.next_window_at, Unset):
            next_window_at = self.next_window_at.isoformat()

        optout_rate = self.optout_rate

        paused_reason: str | Unset = UNSET
        if not isinstance(self.paused_reason, Unset):
            paused_reason = self.paused_reason

        progress: dict[str, Any] | Unset = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        revision = self.revision

        safeguard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.safeguard, Unset):
            safeguard = self.safeguard.to_dict()

        start_at: str | Unset = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        voicemail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voicemail, Unset):
            voicemail = self.voicemail.to_dict()

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
                "spend_micro": spend_micro,
                "status": status,
                "updated_at": updated_at,
                "windows": windows,
            }
        )
        if abandonment_rate_30d is not UNSET:
            field_dict["abandonment_rate_30d"] = abandonment_rate_30d
        if agent_name is not UNSET:
            field_dict["agent_name"] = agent_name
        if amd_profile_id is not UNSET:
            field_dict["amd_profile_id"] = amd_profile_id
        if answer_rate is not UNSET:
            field_dict["answer_rate"] = answer_rate
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if audience is not UNSET:
            field_dict["audience"] = audience
        if blockers is not UNSET:
            field_dict["blockers"] = blockers
        if display_status is not UNSET:
            field_dict["display_status"] = display_status
        if duplicated_from is not UNSET:
            field_dict["duplicated_from"] = duplicated_from
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if informational_category is not UNSET:
            field_dict["informational_category"] = informational_category
        if launch is not UNSET:
            field_dict["launch"] = launch
        if max_calls_per_day is not UNSET:
            field_dict["max_calls_per_day"] = max_calls_per_day
        if next_window_at is not UNSET:
            field_dict["next_window_at"] = next_window_at
        if optout_rate is not UNSET:
            field_dict["optout_rate"] = optout_rate
        if paused_reason is not UNSET:
            field_dict["paused_reason"] = paused_reason
        if progress is not UNSET:
            field_dict["progress"] = progress
        if revision is not UNSET:
            field_dict["revision"] = revision
        if safeguard is not UNSET:
            field_dict["safeguard"] = safeguard
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if voicemail is not UNSET:
            field_dict["voicemail"] = voicemail
        if voicemail_message is not UNSET:
            field_dict["voicemail_message"] = voicemail_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audience import Audience
        from ..models.campaign_launch import CampaignLaunch
        from ..models.campaign_progress import CampaignProgress
        from ..models.campaign_safeguard import CampaignSafeguard
        from ..models.campaign_voicemail import CampaignVoicemail
        from ..models.campaign_window import CampaignWindow
        from ..models.preflight_check import PreflightCheck
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

        spend_micro = d.pop("spend_micro")

        status = check_campaign_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        windows = []
        _windows = d.pop("windows")
        for windows_item_data in _windows:
            windows_item = CampaignWindow.from_dict(windows_item_data)

            windows.append(windows_item)

        abandonment_rate_30d = d.pop("abandonment_rate_30d", UNSET)

        agent_name = d.pop("agent_name", UNSET)

        _amd_profile_id = d.pop("amd_profile_id", UNSET)
        amd_profile_id: UUID | Unset
        if isinstance(_amd_profile_id, Unset):
            amd_profile_id = UNSET
        else:
            amd_profile_id = UUID(_amd_profile_id)

        answer_rate = d.pop("answer_rate", UNSET)

        _archived_at = d.pop("archived_at", UNSET)
        archived_at: datetime.datetime | Unset
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = datetime.datetime.fromisoformat(_archived_at)

        _audience = d.pop("audience", UNSET)
        audience: Audience | Unset
        if isinstance(_audience, Unset):
            audience = UNSET
        else:
            audience = Audience.from_dict(_audience)

        _blockers = d.pop("blockers", UNSET)
        blockers: list[PreflightCheck] | Unset = UNSET
        if _blockers is not UNSET:
            blockers = []
            for blockers_item_data in _blockers:
                blockers_item = PreflightCheck.from_dict(blockers_item_data)

                blockers.append(blockers_item)

        _display_status = d.pop("display_status", UNSET)
        display_status: CampaignDisplayStatus | Unset
        if isinstance(_display_status, Unset):
            display_status = UNSET
        else:
            display_status = check_campaign_display_status(_display_status)

        _duplicated_from = d.pop("duplicated_from", UNSET)
        duplicated_from: UUID | Unset
        if isinstance(_duplicated_from, Unset):
            duplicated_from = UNSET
        else:
            duplicated_from = UUID(_duplicated_from)

        _end_at = d.pop("end_at", UNSET)
        end_at: datetime.datetime | Unset
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = datetime.datetime.fromisoformat(_end_at)

        informational_category = d.pop("informational_category", UNSET)

        _launch = d.pop("launch", UNSET)
        launch: CampaignLaunch | Unset
        if isinstance(_launch, Unset):
            launch = UNSET
        else:
            launch = CampaignLaunch.from_dict(_launch)

        max_calls_per_day = d.pop("max_calls_per_day", UNSET)

        _next_window_at = d.pop("next_window_at", UNSET)
        next_window_at: datetime.datetime | Unset
        if isinstance(_next_window_at, Unset):
            next_window_at = UNSET
        else:
            next_window_at = datetime.datetime.fromisoformat(_next_window_at)

        optout_rate = d.pop("optout_rate", UNSET)

        _paused_reason = d.pop("paused_reason", UNSET)
        paused_reason: CampaignPausedReason | Unset
        if isinstance(_paused_reason, Unset):
            paused_reason = UNSET
        else:
            paused_reason = check_campaign_paused_reason(_paused_reason)

        _progress = d.pop("progress", UNSET)
        progress: CampaignProgress | Unset
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = CampaignProgress.from_dict(_progress)

        revision = d.pop("revision", UNSET)

        _safeguard = d.pop("safeguard", UNSET)
        safeguard: CampaignSafeguard | Unset
        if isinstance(_safeguard, Unset):
            safeguard = UNSET
        else:
            safeguard = CampaignSafeguard.from_dict(_safeguard)

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
            spend_micro=spend_micro,
            status=status,
            updated_at=updated_at,
            windows=windows,
            abandonment_rate_30d=abandonment_rate_30d,
            agent_name=agent_name,
            amd_profile_id=amd_profile_id,
            answer_rate=answer_rate,
            archived_at=archived_at,
            audience=audience,
            blockers=blockers,
            display_status=display_status,
            duplicated_from=duplicated_from,
            end_at=end_at,
            informational_category=informational_category,
            launch=launch,
            max_calls_per_day=max_calls_per_day,
            next_window_at=next_window_at,
            optout_rate=optout_rate,
            paused_reason=paused_reason,
            progress=progress,
            revision=revision,
            safeguard=safeguard,
            start_at=start_at,
            voicemail=voicemail,
            voicemail_message=voicemail_message,
        )

        return campaign
