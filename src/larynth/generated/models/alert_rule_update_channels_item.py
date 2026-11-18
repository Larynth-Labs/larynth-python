from typing import Literal

AlertRuleUpdateChannelsItem = Literal[
    "email", "in_app", "push", "slack", "sms", "telegram", "webhook"
]

ALERT_RULE_UPDATE_CHANNELS_ITEM_VALUES: set[AlertRuleUpdateChannelsItem] = {
    "email",
    "in_app",
    "push",
    "slack",
    "sms",
    "telegram",
    "webhook",
}


def check_alert_rule_update_channels_item(value: str) -> AlertRuleUpdateChannelsItem:
    if value in ALERT_RULE_UPDATE_CHANNELS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_UPDATE_CHANNELS_ITEM_VALUES!r}"
    )
