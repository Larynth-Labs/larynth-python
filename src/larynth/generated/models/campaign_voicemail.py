from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.campaign_voicemail_mode import (
    CampaignVoicemailMode,
    check_campaign_voicemail_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CampaignVoicemail")


@_attrs_define
class CampaignVoicemail:
    """
    Attributes:
        mode (CampaignVoicemailMode): hangup plays the required short message for marketing; message needs the opt-out
            line for marketing; agent uses the agent's setting
        message (str | Unset): Fixed text with variables, played inside the locked compliance template
    """

    mode: CampaignVoicemailMode
    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: str = self.mode

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = check_campaign_voicemail_mode(d.pop("mode"))

        message = d.pop("message", UNSET)

        campaign_voicemail = cls(
            mode=mode,
            message=message,
        )

        return campaign_voicemail
