from typing import Literal

AlertRuleCreateDirectionsItem = Literal["inbound", "outbound", "web_test"]

ALERT_RULE_CREATE_DIRECTIONS_ITEM_VALUES: set[AlertRuleCreateDirectionsItem] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_alert_rule_create_directions_item(
    value: str,
) -> AlertRuleCreateDirectionsItem:
    if value in ALERT_RULE_CREATE_DIRECTIONS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_CREATE_DIRECTIONS_ITEM_VALUES!r}"
    )
