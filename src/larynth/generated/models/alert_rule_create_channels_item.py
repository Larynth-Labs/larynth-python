from typing import Literal

AlertRuleCreateChannelsItem = Literal[
    "email", "in_app", "push", "slack", "sms", "telegram", "webhook"
]

ALERT_RULE_CREATE_CHANNELS_ITEM_VALUES: set[AlertRuleCreateChannelsItem] = {
    "email",
    "in_app",
    "push",
    "slack",
    "sms",
    "telegram",
    "webhook",
}


def check_alert_rule_create_channels_item(value: str) -> AlertRuleCreateChannelsItem:
    if value in ALERT_RULE_CREATE_CHANNELS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_CREATE_CHANNELS_ITEM_VALUES!r}"
    )
