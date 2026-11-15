from typing import Literal

AlertRuleCreateTrigger = Literal["call_analyzed", "live_turn"]

ALERT_RULE_CREATE_TRIGGER_VALUES: set[AlertRuleCreateTrigger] = {
    "call_analyzed",
    "live_turn",
}


def check_alert_rule_create_trigger(value: str) -> AlertRuleCreateTrigger:
    if value in ALERT_RULE_CREATE_TRIGGER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_CREATE_TRIGGER_VALUES!r}"
    )
