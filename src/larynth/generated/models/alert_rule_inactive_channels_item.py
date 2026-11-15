from typing import Literal

AlertRuleInactiveChannelsItem = Literal[
    "email", "in_app", "push", "slack", "sms", "telegram", "webhook"
]

ALERT_RULE_INACTIVE_CHANNELS_ITEM_VALUES: set[AlertRuleInactiveChannelsItem] = {
    "email",
    "in_app",
    "push",
    "slack",
    "sms",
    "telegram",
    "webhook",
}


def check_alert_rule_inactive_channels_item(
    value: str,
) -> AlertRuleInactiveChannelsItem:
    if value in ALERT_RULE_INACTIVE_CHANNELS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_INACTIVE_CHANNELS_ITEM_VALUES!r}"
    )
