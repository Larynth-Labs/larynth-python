from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.call_amd_early_media_tone import (
    CallAmdEarlyMediaTone,
    check_call_amd_early_media_tone,
)
from ..models.call_amd_verdict import CallAmdVerdict, check_call_amd_verdict
from ..models.call_attestation import CallAttestation, check_call_attestation
from ..models.call_codec import CallCodec, check_call_codec
from ..models.call_direction import CallDirection, check_call_direction
from ..models.call_hangup_by import CallHangupBy, check_call_hangup_by
from ..models.call_mode import CallMode, check_call_mode
from ..models.call_status import CallStatus, check_call_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amd_answer_headers import AMDAnswerHeaders


T = TypeVar("T", bound="Call")


@_attrs_define
class Call:
    """
    Attributes:
        call_id (str):
        created_at (datetime.datetime):
        direction (CallDirection):
        mode (CallMode):
        opted_out (bool):
        recording_allowed (bool):
        status (CallStatus):
        updated_at (datetime.datetime):
        agent_billable_ms (int | Unset): Part of billable_ms handled by the agent
        agent_price_micro (int | Unset): Settled price of the agent part in micro-USD
        amd_after_ms (int | Unset):
        amd_answer_headers (AMDAnswerHeaders | Unset):
        amd_early_media_tone (CallAmdEarlyMediaTone | Unset):
        amd_reason (str | Unset):
        amd_ringback_cycles (int | Unset): Ringback cycles heard before answer
        amd_t200_ms (int | Unset): Originate to 200 OK; absent when not answered
        amd_verdict (CallAmdVerdict | Unset):
        answered_at (datetime.datetime | Unset):
        assistant_id (UUID | Unset):
        assistant_version (int | Unset):
        attestation (CallAttestation | Unset):
        billable_ms (int | Unset):
        bridged_ms (int | Unset): Part of billable_ms bridged to a human after a transfer
        bridged_price_micro (int | Unset): Settled price of the bridged part in micro-USD, billed at the transfer_minute
            rate
        campaign_contact_id (UUID | Unset):
        campaign_id (UUID | Unset):
        cause (str | Unset):
        codec (CallCodec | Unset):
        disclosure_played_at (datetime.datetime | Unset):
        ended_at (datetime.datetime | Unset):
        from_e164 (str | Unset):
        hangup_by (CallHangupBy | Unset):
        number_id (UUID | Unset):
        outcome (str | Unset):
        price_micro (int | Unset): Settled price in micro-USD
        recording_notice_played_at (datetime.datetime | Unset):
        sip_code (int | Unset):
        summary (str | Unset): Short post-call summary, present on list items once analysed
        to_e164 (str | Unset):
    """

    call_id: str
    created_at: datetime.datetime
    direction: CallDirection
    mode: CallMode
    opted_out: bool
    recording_allowed: bool
    status: CallStatus
    updated_at: datetime.datetime
    agent_billable_ms: int | Unset = UNSET
    agent_price_micro: int | Unset = UNSET
    amd_after_ms: int | Unset = UNSET
    amd_answer_headers: AMDAnswerHeaders | Unset = UNSET
    amd_early_media_tone: CallAmdEarlyMediaTone | Unset = UNSET
    amd_reason: str | Unset = UNSET
    amd_ringback_cycles: int | Unset = UNSET
    amd_t200_ms: int | Unset = UNSET
    amd_verdict: CallAmdVerdict | Unset = UNSET
    answered_at: datetime.datetime | Unset = UNSET
    assistant_id: UUID | Unset = UNSET
    assistant_version: int | Unset = UNSET
    attestation: CallAttestation | Unset = UNSET
    billable_ms: int | Unset = UNSET
    bridged_ms: int | Unset = UNSET
    bridged_price_micro: int | Unset = UNSET
    campaign_contact_id: UUID | Unset = UNSET
    campaign_id: UUID | Unset = UNSET
    cause: str | Unset = UNSET
    codec: CallCodec | Unset = UNSET
    disclosure_played_at: datetime.datetime | Unset = UNSET
    ended_at: datetime.datetime | Unset = UNSET
    from_e164: str | Unset = UNSET
    hangup_by: CallHangupBy | Unset = UNSET
    number_id: UUID | Unset = UNSET
    outcome: str | Unset = UNSET
    price_micro: int | Unset = UNSET
    recording_notice_played_at: datetime.datetime | Unset = UNSET
    sip_code: int | Unset = UNSET
    summary: str | Unset = UNSET
    to_e164: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        created_at = self.created_at.isoformat()

        direction: str = self.direction

        mode: str = self.mode

        opted_out = self.opted_out

        recording_allowed = self.recording_allowed

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        agent_billable_ms = self.agent_billable_ms

        agent_price_micro = self.agent_price_micro

        amd_after_ms = self.amd_after_ms

        amd_answer_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amd_answer_headers, Unset):
            amd_answer_headers = self.amd_answer_headers.to_dict()

        amd_early_media_tone: str | Unset = UNSET
        if not isinstance(self.amd_early_media_tone, Unset):
            amd_early_media_tone = self.amd_early_media_tone

        amd_reason = self.amd_reason

        amd_ringback_cycles = self.amd_ringback_cycles

        amd_t200_ms = self.amd_t200_ms

        amd_verdict: str | Unset = UNSET
        if not isinstance(self.amd_verdict, Unset):
            amd_verdict = self.amd_verdict

        answered_at: str | Unset = UNSET
        if not isinstance(self.answered_at, Unset):
            answered_at = self.answered_at.isoformat()

        assistant_id: str | Unset = UNSET
        if not isinstance(self.assistant_id, Unset):
            assistant_id = str(self.assistant_id)

        assistant_version = self.assistant_version

        attestation: str | Unset = UNSET
        if not isinstance(self.attestation, Unset):
            attestation = self.attestation

        billable_ms = self.billable_ms

        bridged_ms = self.bridged_ms

        bridged_price_micro = self.bridged_price_micro

        campaign_contact_id: str | Unset = UNSET
        if not isinstance(self.campaign_contact_id, Unset):
            campaign_contact_id = str(self.campaign_contact_id)

        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        cause = self.cause

        codec: str | Unset = UNSET
        if not isinstance(self.codec, Unset):
            codec = self.codec

        disclosure_played_at: str | Unset = UNSET
        if not isinstance(self.disclosure_played_at, Unset):
            disclosure_played_at = self.disclosure_played_at.isoformat()

        ended_at: str | Unset = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        from_e164 = self.from_e164

        hangup_by: str | Unset = UNSET
        if not isinstance(self.hangup_by, Unset):
            hangup_by = self.hangup_by

        number_id: str | Unset = UNSET
        if not isinstance(self.number_id, Unset):
            number_id = str(self.number_id)

        outcome = self.outcome

        price_micro = self.price_micro

        recording_notice_played_at: str | Unset = UNSET
        if not isinstance(self.recording_notice_played_at, Unset):
            recording_notice_played_at = self.recording_notice_played_at.isoformat()

        sip_code = self.sip_code

        summary = self.summary

        to_e164 = self.to_e164

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "call_id": call_id,
                "created_at": created_at,
                "direction": direction,
                "mode": mode,
                "opted_out": opted_out,
                "recording_allowed": recording_allowed,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if agent_billable_ms is not UNSET:
            field_dict["agent_billable_ms"] = agent_billable_ms
        if agent_price_micro is not UNSET:
            field_dict["agent_price_micro"] = agent_price_micro
        if amd_after_ms is not UNSET:
            field_dict["amd_after_ms"] = amd_after_ms
        if amd_answer_headers is not UNSET:
            field_dict["amd_answer_headers"] = amd_answer_headers
        if amd_early_media_tone is not UNSET:
            field_dict["amd_early_media_tone"] = amd_early_media_tone
        if amd_reason is not UNSET:
            field_dict["amd_reason"] = amd_reason
        if amd_ringback_cycles is not UNSET:
            field_dict["amd_ringback_cycles"] = amd_ringback_cycles
        if amd_t200_ms is not UNSET:
            field_dict["amd_t200_ms"] = amd_t200_ms
        if amd_verdict is not UNSET:
            field_dict["amd_verdict"] = amd_verdict
        if answered_at is not UNSET:
            field_dict["answered_at"] = answered_at
        if assistant_id is not UNSET:
            field_dict["assistant_id"] = assistant_id
        if assistant_version is not UNSET:
            field_dict["assistant_version"] = assistant_version
        if attestation is not UNSET:
            field_dict["attestation"] = attestation
        if billable_ms is not UNSET:
            field_dict["billable_ms"] = billable_ms
        if bridged_ms is not UNSET:
            field_dict["bridged_ms"] = bridged_ms
        if bridged_price_micro is not UNSET:
            field_dict["bridged_price_micro"] = bridged_price_micro
        if campaign_contact_id is not UNSET:
            field_dict["campaign_contact_id"] = campaign_contact_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if cause is not UNSET:
            field_dict["cause"] = cause
        if codec is not UNSET:
            field_dict["codec"] = codec
        if disclosure_played_at is not UNSET:
            field_dict["disclosure_played_at"] = disclosure_played_at
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if from_e164 is not UNSET:
            field_dict["from_e164"] = from_e164
        if hangup_by is not UNSET:
            field_dict["hangup_by"] = hangup_by
        if number_id is not UNSET:
            field_dict["number_id"] = number_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if price_micro is not UNSET:
            field_dict["price_micro"] = price_micro
        if recording_notice_played_at is not UNSET:
            field_dict["recording_notice_played_at"] = recording_notice_played_at
        if sip_code is not UNSET:
            field_dict["sip_code"] = sip_code
        if summary is not UNSET:
            field_dict["summary"] = summary
        if to_e164 is not UNSET:
            field_dict["to_e164"] = to_e164

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.amd_answer_headers import AMDAnswerHeaders

        d = dict(src_dict)
        call_id = d.pop("call_id")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        direction = check_call_direction(d.pop("direction"))

        mode = check_call_mode(d.pop("mode"))

        opted_out = d.pop("opted_out")

        recording_allowed = d.pop("recording_allowed")

        status = check_call_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        agent_billable_ms = d.pop("agent_billable_ms", UNSET)

        agent_price_micro = d.pop("agent_price_micro", UNSET)

        amd_after_ms = d.pop("amd_after_ms", UNSET)

        _amd_answer_headers = d.pop("amd_answer_headers", UNSET)
        amd_answer_headers: AMDAnswerHeaders | Unset
        if isinstance(_amd_answer_headers, Unset):
            amd_answer_headers = UNSET
        else:
            amd_answer_headers = AMDAnswerHeaders.from_dict(_amd_answer_headers)

        _amd_early_media_tone = d.pop("amd_early_media_tone", UNSET)
        amd_early_media_tone: CallAmdEarlyMediaTone | Unset
        if isinstance(_amd_early_media_tone, Unset):
            amd_early_media_tone = UNSET
        else:
            amd_early_media_tone = check_call_amd_early_media_tone(
                _amd_early_media_tone
            )

        amd_reason = d.pop("amd_reason", UNSET)

        amd_ringback_cycles = d.pop("amd_ringback_cycles", UNSET)

        amd_t200_ms = d.pop("amd_t200_ms", UNSET)

        _amd_verdict = d.pop("amd_verdict", UNSET)
        amd_verdict: CallAmdVerdict | Unset
        if isinstance(_amd_verdict, Unset):
            amd_verdict = UNSET
        else:
            amd_verdict = check_call_amd_verdict(_amd_verdict)

        _answered_at = d.pop("answered_at", UNSET)
        answered_at: datetime.datetime | Unset
        if isinstance(_answered_at, Unset):
            answered_at = UNSET
        else:
            answered_at = datetime.datetime.fromisoformat(_answered_at)

        _assistant_id = d.pop("assistant_id", UNSET)
        assistant_id: UUID | Unset
        if isinstance(_assistant_id, Unset):
            assistant_id = UNSET
        else:
            assistant_id = UUID(_assistant_id)

        assistant_version = d.pop("assistant_version", UNSET)

        _attestation = d.pop("attestation", UNSET)
        attestation: CallAttestation | Unset
        if isinstance(_attestation, Unset):
            attestation = UNSET
        else:
            attestation = check_call_attestation(_attestation)

        billable_ms = d.pop("billable_ms", UNSET)

        bridged_ms = d.pop("bridged_ms", UNSET)

        bridged_price_micro = d.pop("bridged_price_micro", UNSET)

        _campaign_contact_id = d.pop("campaign_contact_id", UNSET)
        campaign_contact_id: UUID | Unset
        if isinstance(_campaign_contact_id, Unset):
            campaign_contact_id = UNSET
        else:
            campaign_contact_id = UUID(_campaign_contact_id)

        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        cause = d.pop("cause", UNSET)

        _codec = d.pop("codec", UNSET)
        codec: CallCodec | Unset
        if isinstance(_codec, Unset):
            codec = UNSET
        else:
            codec = check_call_codec(_codec)

        _disclosure_played_at = d.pop("disclosure_played_at", UNSET)
        disclosure_played_at: datetime.datetime | Unset
        if isinstance(_disclosure_played_at, Unset):
            disclosure_played_at = UNSET
        else:
            disclosure_played_at = datetime.datetime.fromisoformat(
                _disclosure_played_at
            )

        _ended_at = d.pop("ended_at", UNSET)
        ended_at: datetime.datetime | Unset
        if isinstance(_ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = datetime.datetime.fromisoformat(_ended_at)

        from_e164 = d.pop("from_e164", UNSET)

        _hangup_by = d.pop("hangup_by", UNSET)
        hangup_by: CallHangupBy | Unset
        if isinstance(_hangup_by, Unset):
            hangup_by = UNSET
        else:
            hangup_by = check_call_hangup_by(_hangup_by)

        _number_id = d.pop("number_id", UNSET)
        number_id: UUID | Unset
        if isinstance(_number_id, Unset):
            number_id = UNSET
        else:
            number_id = UUID(_number_id)

        outcome = d.pop("outcome", UNSET)

        price_micro = d.pop("price_micro", UNSET)

        _recording_notice_played_at = d.pop("recording_notice_played_at", UNSET)
        recording_notice_played_at: datetime.datetime | Unset
        if isinstance(_recording_notice_played_at, Unset):
            recording_notice_played_at = UNSET
        else:
            recording_notice_played_at = datetime.datetime.fromisoformat(
                _recording_notice_played_at
            )

        sip_code = d.pop("sip_code", UNSET)

        summary = d.pop("summary", UNSET)

        to_e164 = d.pop("to_e164", UNSET)

        call = cls(
            call_id=call_id,
            created_at=created_at,
            direction=direction,
            mode=mode,
            opted_out=opted_out,
            recording_allowed=recording_allowed,
            status=status,
            updated_at=updated_at,
            agent_billable_ms=agent_billable_ms,
            agent_price_micro=agent_price_micro,
            amd_after_ms=amd_after_ms,
            amd_answer_headers=amd_answer_headers,
            amd_early_media_tone=amd_early_media_tone,
            amd_reason=amd_reason,
            amd_ringback_cycles=amd_ringback_cycles,
            amd_t200_ms=amd_t200_ms,
            amd_verdict=amd_verdict,
            answered_at=answered_at,
            assistant_id=assistant_id,
            assistant_version=assistant_version,
            attestation=attestation,
            billable_ms=billable_ms,
            bridged_ms=bridged_ms,
            bridged_price_micro=bridged_price_micro,
            campaign_contact_id=campaign_contact_id,
            campaign_id=campaign_id,
            cause=cause,
            codec=codec,
            disclosure_played_at=disclosure_played_at,
            ended_at=ended_at,
            from_e164=from_e164,
            hangup_by=hangup_by,
            number_id=number_id,
            outcome=outcome,
            price_micro=price_micro,
            recording_notice_played_at=recording_notice_played_at,
            sip_code=sip_code,
            summary=summary,
            to_e164=to_e164,
        )

        return call
