from typing import Literal

TrialTermsCoversItem = Literal["inbound", "web_test"]

TRIAL_TERMS_COVERS_ITEM_VALUES: set[TrialTermsCoversItem] = {
    "inbound",
    "web_test",
}


def check_trial_terms_covers_item(value: str) -> TrialTermsCoversItem:
    if value in TRIAL_TERMS_COVERS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRIAL_TERMS_COVERS_ITEM_VALUES!r}"
    )
