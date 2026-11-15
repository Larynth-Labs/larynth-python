from typing import Literal

AlertRuleCreateRecipientRolesItem = Literal["admin", "member", "owner"]

ALERT_RULE_CREATE_RECIPIENT_ROLES_ITEM_VALUES: set[
    AlertRuleCreateRecipientRolesItem
] = {
    "admin",
    "member",
    "owner",
}


def check_alert_rule_create_recipient_roles_item(
    value: str,
) -> AlertRuleCreateRecipientRolesItem:
    if value in ALERT_RULE_CREATE_RECIPIENT_ROLES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_CREATE_RECIPIENT_ROLES_ITEM_VALUES!r}"
    )
