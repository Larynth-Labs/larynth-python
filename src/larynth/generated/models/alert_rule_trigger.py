from typing import Literal

AlertRuleTrigger = Literal["call_analyzed", "live_turn"]

ALERT_RULE_TRIGGER_VALUES: set[AlertRuleTrigger] = {
    "call_analyzed",
    "live_turn",
}


def check_alert_rule_trigger(value: str) -> AlertRuleTrigger:
    if value in ALERT_RULE_TRIGGER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_TRIGGER_VALUES!r}"
    )
