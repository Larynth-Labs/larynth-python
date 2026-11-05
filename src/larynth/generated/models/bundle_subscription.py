from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.bundle_subscription_status import (
    BundleSubscriptionStatus,
    check_bundle_subscription_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle import Bundle
    from ..models.bundle_lot import BundleLot


T = TypeVar("T", bound="BundleSubscription")


@_attrs_define
class BundleSubscription:
    """
    Attributes:
        credit_left_micro (int):
        lots (list[BundleLot]):
        status (BundleSubscriptionStatus):
        bundle (Bundle | Unset):
        current_period_end (datetime.datetime | Unset):
        last_failure_code (str | Unset):
        next_bundle_key (str | Unset): Size from the next renewal
        payment_method_id (str | Unset):
        renews_at (datetime.datetime | Unset):
    """

    credit_left_micro: int
    lots: list[BundleLot]
    status: BundleSubscriptionStatus
    bundle: Bundle | Unset = UNSET
    current_period_end: datetime.datetime | Unset = UNSET
    last_failure_code: str | Unset = UNSET
    next_bundle_key: str | Unset = UNSET
    payment_method_id: str | Unset = UNSET
    renews_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credit_left_micro = self.credit_left_micro

        lots = []
        for lots_item_data in self.lots:
            lots_item = lots_item_data.to_dict()
            lots.append(lots_item)

        status: str = self.status

        bundle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bundle, Unset):
            bundle = self.bundle.to_dict()

        current_period_end: str | Unset = UNSET
        if not isinstance(self.current_period_end, Unset):
            current_period_end = self.current_period_end.isoformat()

        last_failure_code = self.last_failure_code

        next_bundle_key = self.next_bundle_key

        payment_method_id = self.payment_method_id

        renews_at: str | Unset = UNSET
        if not isinstance(self.renews_at, Unset):
            renews_at = self.renews_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "credit_left_micro": credit_left_micro,
                "lots": lots,
                "status": status,
            }
        )
        if bundle is not UNSET:
            field_dict["bundle"] = bundle
        if current_period_end is not UNSET:
            field_dict["current_period_end"] = current_period_end
        if last_failure_code is not UNSET:
            field_dict["last_failure_code"] = last_failure_code
        if next_bundle_key is not UNSET:
            field_dict["next_bundle_key"] = next_bundle_key
        if payment_method_id is not UNSET:
            field_dict["payment_method_id"] = payment_method_id
        if renews_at is not UNSET:
            field_dict["renews_at"] = renews_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bundle import Bundle
        from ..models.bundle_lot import BundleLot

        d = dict(src_dict)
        credit_left_micro = d.pop("credit_left_micro")

        lots = []
        _lots = d.pop("lots")
        for lots_item_data in _lots:
            lots_item = BundleLot.from_dict(lots_item_data)

            lots.append(lots_item)

        status = check_bundle_subscription_status(d.pop("status"))

        _bundle = d.pop("bundle", UNSET)
        bundle: Bundle | Unset
        if isinstance(_bundle, Unset):
            bundle = UNSET
        else:
            bundle = Bundle.from_dict(_bundle)

        _current_period_end = d.pop("current_period_end", UNSET)
        current_period_end: datetime.datetime | Unset
        if isinstance(_current_period_end, Unset):
            current_period_end = UNSET
        else:
            current_period_end = datetime.datetime.fromisoformat(_current_period_end)

        last_failure_code = d.pop("last_failure_code", UNSET)

        next_bundle_key = d.pop("next_bundle_key", UNSET)

        payment_method_id = d.pop("payment_method_id", UNSET)

        _renews_at = d.pop("renews_at", UNSET)
        renews_at: datetime.datetime | Unset
        if isinstance(_renews_at, Unset):
            renews_at = UNSET
        else:
            renews_at = datetime.datetime.fromisoformat(_renews_at)

        bundle_subscription = cls(
            credit_left_micro=credit_left_micro,
            lots=lots,
            status=status,
            bundle=bundle,
            current_period_end=current_period_end,
            last_failure_code=last_failure_code,
            next_bundle_key=next_bundle_key,
            payment_method_id=payment_method_id,
            renews_at=renews_at,
        )

        return bundle_subscription
