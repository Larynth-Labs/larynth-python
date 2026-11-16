from typing import Literal

AlertRuleRecipientRolesItem = Literal["admin", "member", "owner"]

ALERT_RULE_RECIPIENT_ROLES_ITEM_VALUES: set[AlertRuleRecipientRolesItem] = {
    "admin",
    "member",
    "owner",
}


def check_alert_rule_recipient_roles_item(value: str) -> AlertRuleRecipientRolesItem:
    if value in ALERT_RULE_RECIPIENT_ROLES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_RULE_RECIPIENT_ROLES_ITEM_VALUES!r}"
    )
