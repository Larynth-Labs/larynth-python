from typing import Literal

CallRedactedCategoriesItem = Literal["bank", "card", "dob", "gov_id", "ssn"]

CALL_REDACTED_CATEGORIES_ITEM_VALUES: set[CallRedactedCategoriesItem] = {
    "bank",
    "card",
    "dob",
    "gov_id",
    "ssn",
}


def check_call_redacted_categories_item(value: str) -> CallRedactedCategoriesItem:
    if value in CALL_REDACTED_CATEGORIES_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_REDACTED_CATEGORIES_ITEM_VALUES!r}"
    )
