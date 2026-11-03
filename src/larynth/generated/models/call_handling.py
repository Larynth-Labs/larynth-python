from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.call_handling_max_reply import (
    CallHandlingMaxReply,
    check_call_handling_max_reply,
)
from ..models.call_handling_silence_end_s import (
    CallHandlingSilenceEndS,
    check_call_handling_silence_end_s,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallHandling")


@_attrs_define
class CallHandling:
    """
    Attributes:
        dtmf_input (bool | Unset): Accept keypad input
        end_on_goodbye (bool | Unset):
        ivr_navigation (bool | Unset): Navigate phone menus on outbound calls
        max_reply (CallHandlingMaxReply | Unset):
        silence_end_s (CallHandlingSilenceEndS | Unset): End the call after this much caller silence. Unset is 30
        voicemail_detection (bool | Unset):
        voicemail_message (str | Unset):
    """

    dtmf_input: bool | Unset = UNSET
    end_on_goodbye: bool | Unset = UNSET
    ivr_navigation: bool | Unset = UNSET
    max_reply: CallHandlingMaxReply | Unset = UNSET
    silence_end_s: CallHandlingSilenceEndS | Unset = UNSET
    voicemail_detection: bool | Unset = UNSET
    voicemail_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dtmf_input = self.dtmf_input

        end_on_goodbye = self.end_on_goodbye

        ivr_navigation = self.ivr_navigation

        max_reply: str | Unset = UNSET
        if not isinstance(self.max_reply, Unset):
            max_reply = self.max_reply

        silence_end_s: int | Unset = UNSET
        if not isinstance(self.silence_end_s, Unset):
            silence_end_s = self.silence_end_s

        voicemail_detection = self.voicemail_detection

        voicemail_message = self.voicemail_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dtmf_input is not UNSET:
            field_dict["dtmf_input"] = dtmf_input
        if end_on_goodbye is not UNSET:
            field_dict["end_on_goodbye"] = end_on_goodbye
        if ivr_navigation is not UNSET:
            field_dict["ivr_navigation"] = ivr_navigation
        if max_reply is not UNSET:
            field_dict["max_reply"] = max_reply
        if silence_end_s is not UNSET:
            field_dict["silence_end_s"] = silence_end_s
        if voicemail_detection is not UNSET:
            field_dict["voicemail_detection"] = voicemail_detection
        if voicemail_message is not UNSET:
            field_dict["voicemail_message"] = voicemail_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dtmf_input = d.pop("dtmf_input", UNSET)

        end_on_goodbye = d.pop("end_on_goodbye", UNSET)

        ivr_navigation = d.pop("ivr_navigation", UNSET)

        _max_reply = d.pop("max_reply", UNSET)
        max_reply: CallHandlingMaxReply | Unset
        if isinstance(_max_reply, Unset):
            max_reply = UNSET
        else:
            max_reply = check_call_handling_max_reply(_max_reply)

        _silence_end_s = d.pop("silence_end_s", UNSET)
        silence_end_s: CallHandlingSilenceEndS | Unset
        if isinstance(_silence_end_s, Unset):
            silence_end_s = UNSET
        else:
            silence_end_s = check_call_handling_silence_end_s(_silence_end_s)

        voicemail_detection = d.pop("voicemail_detection", UNSET)

        voicemail_message = d.pop("voicemail_message", UNSET)

        call_handling = cls(
            dtmf_input=dtmf_input,
            end_on_goodbye=end_on_goodbye,
            ivr_navigation=ivr_navigation,
            max_reply=max_reply,
            silence_end_s=silence_end_s,
            voicemail_detection=voicemail_detection,
            voicemail_message=voicemail_message,
        )

        return call_handling
