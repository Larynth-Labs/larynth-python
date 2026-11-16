from typing import Literal

AlertRuleUpdateRecipientRolesItem = Literal["admin", "member", "owner"]

ALERT_RULE_UPDATE_RECIPIENT_ROLES_ITEM_VALUES: set[
    AlertRuleUpdateRecipientRolesItem
] = {
    "admin",
    "member",
    "owner",
}


def check_alert_rule_update_recipient_roles_item(
    value: str,
) -> AlertRuleUpdateRecipientRolesItem:
    if value in ALERT_RULE_UPDATE_RECIPIENT_ROLES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_UPDATE_RECIPIENT_ROLES_ITEM_VALUES!r}"
    )
