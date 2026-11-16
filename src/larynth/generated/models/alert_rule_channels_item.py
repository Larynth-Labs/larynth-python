from typing import Literal

AlertRuleChannelsItem = Literal[
    "email", "in_app", "push", "slack", "sms", "telegram", "webhook"
]

ALERT_RULE_CHANNELS_ITEM_VALUES: set[AlertRuleChannelsItem] = {
    "email",
    "in_app",
    "push",
    "slack",
    "sms",
    "telegram",
    "webhook",
}


def check_alert_rule_channels_item(value: str) -> AlertRuleChannelsItem:
    if value in ALERT_RULE_CHANNELS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_CHANNELS_ITEM_VALUES!r}"
    )
