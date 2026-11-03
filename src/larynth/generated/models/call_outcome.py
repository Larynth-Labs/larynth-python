from typing import Literal

CallOutcome = Literal[
    "answered_question",
    "booked_appointment",
    "caller_blocked",
    "caller_hung_up",
    "carrier_error",
    "line_busy",
    "message_taken",
    "no_answer",
    "no_resolution",
    "rescheduled",
    "spam_blocked",
    "transferred_to_staff",
    "voicemail_left",
]

CALL_OUTCOME_VALUES: set[CallOutcome] = {
    "answered_question",
    "booked_appointment",
    "caller_blocked",
    "caller_hung_up",
    "carrier_error",
    "line_busy",
    "message_taken",
    "no_answer",
    "no_resolution",
    "rescheduled",
    "spam_blocked",
    "transferred_to_staff",
    "voicemail_left",
}


def check_call_outcome(value: str) -> CallOutcome:
    if value in CALL_OUTCOME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_OUTCOME_VALUES!r}"
    )
