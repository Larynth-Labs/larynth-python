from typing import Literal

CallHandlingVoicemailAction = Literal["hang_up", "leave_message"]

CALL_HANDLING_VOICEMAIL_ACTION_VALUES: set[CallHandlingVoicemailAction] = {
    "hang_up",
    "leave_message",
}


def check_call_handling_voicemail_action(value: str) -> CallHandlingVoicemailAction:
    if value in CALL_HANDLING_VOICEMAIL_ACTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_HANDLING_VOICEMAIL_ACTION_VALUES!r}"
    )
