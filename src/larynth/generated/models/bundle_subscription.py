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
        status (BundleSubscriptionStatus): Bundles are one-time packs: pending while the payment runs, active while pack
            credit is left
        bundle (Bundle | Unset):
        ends_at (datetime.datetime | Unset): When the latest pack's unused credit becomes normal balance; packs never
            renew
    """

    credit_left_micro: int
    lots: list[BundleLot]
    status: BundleSubscriptionStatus
    bundle: Bundle | Unset = UNSET
    ends_at: datetime.datetime | Unset = UNSET

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

        ends_at: str | Unset = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

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
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at

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

        _ends_at = d.pop("ends_at", UNSET)
        ends_at: datetime.datetime | Unset
        if isinstance(_ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = datetime.datetime.fromisoformat(_ends_at)

        bundle_subscription = cls(
            credit_left_micro=credit_left_micro,
            lots=lots,
            status=status,
            bundle=bundle,
            ends_at=ends_at,
        )

        return bundle_subscription
