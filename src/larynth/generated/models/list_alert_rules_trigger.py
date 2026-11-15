from typing import Literal

ListAlertRulesTrigger = Literal["call_analyzed", "live_turn"]

LIST_ALERT_RULES_TRIGGER_VALUES: set[ListAlertRulesTrigger] = {
    "call_analyzed",
    "live_turn",
}


def check_list_alert_rules_trigger(value: str) -> ListAlertRulesTrigger:
    if value in LIST_ALERT_RULES_TRIGGER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ALERT_RULES_TRIGGER_VALUES!r}"
    )
