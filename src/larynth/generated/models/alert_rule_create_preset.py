from typing import Literal

AlertRuleCreatePreset = Literal[
    "asked_for_person",
    "booking_missed",
    "callback_wanted",
    "every_call",
    "summary_failed",
    "unhappy_caller",
    "urgent_words",
]

ALERT_RULE_CREATE_PRESET_VALUES: set[AlertRuleCreatePreset] = {
    "asked_for_person",
    "booking_missed",
    "callback_wanted",
    "every_call",
    "summary_failed",
    "unhappy_caller",
    "urgent_words",
}


def check_alert_rule_create_preset(value: str) -> AlertRuleCreatePreset:
    if value in ALERT_RULE_CREATE_PRESET_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_CREATE_PRESET_VALUES!r}"
    )
