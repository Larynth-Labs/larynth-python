from typing import Literal

AlertRuleDirectionsItem = Literal["inbound", "outbound", "web_test"]

ALERT_RULE_DIRECTIONS_ITEM_VALUES: set[AlertRuleDirectionsItem] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_alert_rule_directions_item(value: str) -> AlertRuleDirectionsItem:
    if value in ALERT_RULE_DIRECTIONS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_DIRECTIONS_ITEM_VALUES!r}"
    )
