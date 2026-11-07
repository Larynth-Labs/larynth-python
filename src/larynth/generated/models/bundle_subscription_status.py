from typing import Literal

BundleSubscriptionStatus = Literal["active", "none", "pending"]

BUNDLE_SUBSCRIPTION_STATUS_VALUES: set[BundleSubscriptionStatus] = {
    "active",
    "none",
    "pending",
}


def check_bundle_subscription_status(value: str) -> BundleSubscriptionStatus:
    if value in BUNDLE_SUBSCRIPTION_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUNDLE_SUBSCRIPTION_STATUS_VALUES!r}"
    )
