from typing import Literal

CallAnalysisOutcome = Literal[
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

CALL_ANALYSIS_OUTCOME_VALUES: set[CallAnalysisOutcome] = {
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


def check_call_analysis_outcome(value: str) -> CallAnalysisOutcome:
    if value in CALL_ANALYSIS_OUTCOME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_ANALYSIS_OUTCOME_VALUES!r}"
    )
