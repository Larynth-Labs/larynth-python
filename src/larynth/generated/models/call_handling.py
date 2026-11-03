from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.call_handling_ambient_sound import (
    CallHandlingAmbientSound,
    check_call_handling_ambient_sound,
)
from ..models.call_handling_dtmf_end_key import (
    CallHandlingDtmfEndKey,
    check_call_handling_dtmf_end_key,
)
from ..models.call_handling_max_reply import (
    CallHandlingMaxReply,
    check_call_handling_max_reply,
)
from ..models.call_handling_silence_end_s import (
    CallHandlingSilenceEndS,
    check_call_handling_silence_end_s,
)
from ..models.call_handling_voicemail_action import (
    CallHandlingVoicemailAction,
    check_call_handling_voicemail_action,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallHandling")


@_attrs_define
class CallHandling:
    """
    Attributes:
        ambient_sound (CallHandlingAmbientSound | Unset): Low background sound the caller hears; never recorded. Unset
            is off
        dtmf_end_key (CallHandlingDtmfEndKey | Unset): Key that ends a keypad entry. Unset is #
        dtmf_input (bool | Unset): Keypad entries reach the agent as caller input; digits are masked in transcripts.
            Unset is on. On outbound calls a lone 9 always opts the caller out
        dtmf_max_digits (int | Unset): An entry also ends at this many digits; 0 is no limit
        dtmf_wait_ms (int | Unset): An entry also ends this long after the last key. Unset is 3000
        end_on_goodbye (bool | Unset):
        idle_reminder (bool | Unset): Ask once whether the caller is still there before the silence hang-up. Unset is on
        ivr_goal (str | Unset): What the agent tries to reach in a phone menu, for example billing
        ivr_navigation (bool | Unset): Navigate phone menus on outbound calls, with at most 2 minutes in menus and 3
            minutes on hold; the call ends as no_resolution with label phone_menu when the menu cannot be passed. Unset is
            off
        max_reply (CallHandlingMaxReply | Unset):
        recording (bool | Unset): Record calls of this agent. Unset is on; off still keeps transcripts and the caller
            hears that the call may be transcribed
        silence_end_s (CallHandlingSilenceEndS | Unset): End the call after this much caller silence. Unset is 30
        voicemail_action (CallHandlingVoicemailAction | Unset): What the agent does on voicemail. Unset follows the
            platform suggestion: hang_up until number reputation is cleared, then leave_message
        voicemail_detection (bool | Unset): Detect voicemail and phone menus on outbound calls. Unset is on; a campaign
            or createCall amd_mode overrides it
        voicemail_message (str | Unset): The purpose part of the voicemail; the business name, AI disclosure, callback
            number and any required opt-out line are added in a fixed template
    """

    ambient_sound: CallHandlingAmbientSound | Unset = UNSET
    dtmf_end_key: CallHandlingDtmfEndKey | Unset = UNSET
    dtmf_input: bool | Unset = UNSET
    dtmf_max_digits: int | Unset = UNSET
    dtmf_wait_ms: int | Unset = UNSET
    end_on_goodbye: bool | Unset = UNSET
    idle_reminder: bool | Unset = UNSET
    ivr_goal: str | Unset = UNSET
    ivr_navigation: bool | Unset = UNSET
    max_reply: CallHandlingMaxReply | Unset = UNSET
    recording: bool | Unset = UNSET
    silence_end_s: CallHandlingSilenceEndS | Unset = UNSET
    voicemail_action: CallHandlingVoicemailAction | Unset = UNSET
    voicemail_detection: bool | Unset = UNSET
    voicemail_message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ambient_sound: str | Unset = UNSET
        if not isinstance(self.ambient_sound, Unset):
            ambient_sound = self.ambient_sound

        dtmf_end_key: str | Unset = UNSET
        if not isinstance(self.dtmf_end_key, Unset):
            dtmf_end_key = self.dtmf_end_key

        dtmf_input = self.dtmf_input

        dtmf_max_digits = self.dtmf_max_digits

        dtmf_wait_ms = self.dtmf_wait_ms

        end_on_goodbye = self.end_on_goodbye

        idle_reminder = self.idle_reminder

        ivr_goal = self.ivr_goal

        ivr_navigation = self.ivr_navigation

        max_reply: str | Unset = UNSET
        if not isinstance(self.max_reply, Unset):
            max_reply = self.max_reply

        recording = self.recording

        silence_end_s: int | Unset = UNSET
        if not isinstance(self.silence_end_s, Unset):
            silence_end_s = self.silence_end_s

        voicemail_action: str | Unset = UNSET
        if not isinstance(self.voicemail_action, Unset):
            voicemail_action = self.voicemail_action

        voicemail_detection = self.voicemail_detection

        voicemail_message = self.voicemail_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ambient_sound is not UNSET:
            field_dict["ambient_sound"] = ambient_sound
        if dtmf_end_key is not UNSET:
            field_dict["dtmf_end_key"] = dtmf_end_key
        if dtmf_input is not UNSET:
            field_dict["dtmf_input"] = dtmf_input
        if dtmf_max_digits is not UNSET:
            field_dict["dtmf_max_digits"] = dtmf_max_digits
        if dtmf_wait_ms is not UNSET:
            field_dict["dtmf_wait_ms"] = dtmf_wait_ms
        if end_on_goodbye is not UNSET:
            field_dict["end_on_goodbye"] = end_on_goodbye
        if idle_reminder is not UNSET:
            field_dict["idle_reminder"] = idle_reminder
        if ivr_goal is not UNSET:
            field_dict["ivr_goal"] = ivr_goal
        if ivr_navigation is not UNSET:
            field_dict["ivr_navigation"] = ivr_navigation
        if max_reply is not UNSET:
            field_dict["max_reply"] = max_reply
        if recording is not UNSET:
            field_dict["recording"] = recording
        if silence_end_s is not UNSET:
            field_dict["silence_end_s"] = silence_end_s
        if voicemail_action is not UNSET:
            field_dict["voicemail_action"] = voicemail_action
        if voicemail_detection is not UNSET:
            field_dict["voicemail_detection"] = voicemail_detection
        if voicemail_message is not UNSET:
            field_dict["voicemail_message"] = voicemail_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _ambient_sound = d.pop("ambient_sound", UNSET)
        ambient_sound: CallHandlingAmbientSound | Unset
        if isinstance(_ambient_sound, Unset):
            ambient_sound = UNSET
        else:
            ambient_sound = check_call_handling_ambient_sound(_ambient_sound)

        _dtmf_end_key = d.pop("dtmf_end_key", UNSET)
        dtmf_end_key: CallHandlingDtmfEndKey | Unset
        if isinstance(_dtmf_end_key, Unset):
            dtmf_end_key = UNSET
        else:
            dtmf_end_key = check_call_handling_dtmf_end_key(_dtmf_end_key)

        dtmf_input = d.pop("dtmf_input", UNSET)

        dtmf_max_digits = d.pop("dtmf_max_digits", UNSET)

        dtmf_wait_ms = d.pop("dtmf_wait_ms", UNSET)

        end_on_goodbye = d.pop("end_on_goodbye", UNSET)

        idle_reminder = d.pop("idle_reminder", UNSET)

        ivr_goal = d.pop("ivr_goal", UNSET)

        ivr_navigation = d.pop("ivr_navigation", UNSET)

        _max_reply = d.pop("max_reply", UNSET)
        max_reply: CallHandlingMaxReply | Unset
        if isinstance(_max_reply, Unset):
            max_reply = UNSET
        else:
            max_reply = check_call_handling_max_reply(_max_reply)

        recording = d.pop("recording", UNSET)

        _silence_end_s = d.pop("silence_end_s", UNSET)
        silence_end_s: CallHandlingSilenceEndS | Unset
        if isinstance(_silence_end_s, Unset):
            silence_end_s = UNSET
        else:
            silence_end_s = check_call_handling_silence_end_s(_silence_end_s)

        _voicemail_action = d.pop("voicemail_action", UNSET)
        voicemail_action: CallHandlingVoicemailAction | Unset
        if isinstance(_voicemail_action, Unset):
            voicemail_action = UNSET
        else:
            voicemail_action = check_call_handling_voicemail_action(_voicemail_action)

        voicemail_detection = d.pop("voicemail_detection", UNSET)

        voicemail_message = d.pop("voicemail_message", UNSET)

        call_handling = cls(
            ambient_sound=ambient_sound,
            dtmf_end_key=dtmf_end_key,
            dtmf_input=dtmf_input,
            dtmf_max_digits=dtmf_max_digits,
            dtmf_wait_ms=dtmf_wait_ms,
            end_on_goodbye=end_on_goodbye,
            idle_reminder=idle_reminder,
            ivr_goal=ivr_goal,
            ivr_navigation=ivr_navigation,
            max_reply=max_reply,
            recording=recording,
            silence_end_s=silence_end_s,
            voicemail_action=voicemail_action,
            voicemail_detection=voicemail_detection,
            voicemail_message=voicemail_message,
        )

        return call_handling
