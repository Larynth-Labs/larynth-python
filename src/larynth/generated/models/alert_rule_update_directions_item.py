from typing import Literal

AlertRuleUpdateDirectionsItem = Literal["inbound", "outbound", "web_test"]

ALERT_RULE_UPDATE_DIRECTIONS_ITEM_VALUES: set[AlertRuleUpdateDirectionsItem] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_alert_rule_update_directions_item(
    value: str,
) -> AlertRuleUpdateDirectionsItem:
    if value in ALERT_RULE_UPDATE_DIRECTIONS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_UPDATE_DIRECTIONS_ITEM_VALUES!r}"
    )
