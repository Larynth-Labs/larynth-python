from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.payment_kind import PaymentKind, check_payment_kind
from ..models.payment_status import PaymentStatus, check_payment_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payment_card import PaymentCard


T = TypeVar("T", bound="Payment")


@_attrs_define
class Payment:
    """
    Attributes:
        amount_micro (int): Credit bought
        created_at (datetime.datetime):
        first_paid (bool): This payment set the workspace's first_paid_at
        id (UUID):
        kind (PaymentKind):
        price_micro (int): Charged before tax; equals amount_micro for top-ups
        refunded_micro (int):
        status (PaymentStatus):
        bundle_key (str | Unset):
        card (PaymentCard | Unset):
        credited_at (datetime.datetime | Unset):
        failure_reason_code (str | Unset):
        receipt_url (str | Unset): The payment provider's receipt
        tax_micro (int | Unset):
        total_charged_micro (int | Unset):
    """

    amount_micro: int
    created_at: datetime.datetime
    first_paid: bool
    id: UUID
    kind: PaymentKind
    price_micro: int
    refunded_micro: int
    status: PaymentStatus
    bundle_key: str | Unset = UNSET
    card: PaymentCard | Unset = UNSET
    credited_at: datetime.datetime | Unset = UNSET
    failure_reason_code: str | Unset = UNSET
    receipt_url: str | Unset = UNSET
    tax_micro: int | Unset = UNSET
    total_charged_micro: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount_micro = self.amount_micro

        created_at = self.created_at.isoformat()

        first_paid = self.first_paid

        id = str(self.id)

        kind: str = self.kind

        price_micro = self.price_micro

        refunded_micro = self.refunded_micro

        status: str = self.status

        bundle_key = self.bundle_key

        card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        credited_at: str | Unset = UNSET
        if not isinstance(self.credited_at, Unset):
            credited_at = self.credited_at.isoformat()

        failure_reason_code = self.failure_reason_code

        receipt_url = self.receipt_url

        tax_micro = self.tax_micro

        total_charged_micro = self.total_charged_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount_micro": amount_micro,
                "created_at": created_at,
                "first_paid": first_paid,
                "id": id,
                "kind": kind,
                "price_micro": price_micro,
                "refunded_micro": refunded_micro,
                "status": status,
            }
        )
        if bundle_key is not UNSET:
            field_dict["bundle_key"] = bundle_key
        if card is not UNSET:
            field_dict["card"] = card
        if credited_at is not UNSET:
            field_dict["credited_at"] = credited_at
        if failure_reason_code is not UNSET:
            field_dict["failure_reason_code"] = failure_reason_code
        if receipt_url is not UNSET:
            field_dict["receipt_url"] = receipt_url
        if tax_micro is not UNSET:
            field_dict["tax_micro"] = tax_micro
        if total_charged_micro is not UNSET:
            field_dict["total_charged_micro"] = total_charged_micro

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.payment_card import PaymentCard

        d = dict(src_dict)
        amount_micro = d.pop("amount_micro")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        first_paid = d.pop("first_paid")

        id = UUID(d.pop("id"))

        kind = check_payment_kind(d.pop("kind"))

        price_micro = d.pop("price_micro")

        refunded_micro = d.pop("refunded_micro")

        status = check_payment_status(d.pop("status"))

        bundle_key = d.pop("bundle_key", UNSET)

        _card = d.pop("card", UNSET)
        card: PaymentCard | Unset
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = PaymentCard.from_dict(_card)

        _credited_at = d.pop("credited_at", UNSET)
        credited_at: datetime.datetime | Unset
        if isinstance(_credited_at, Unset):
            credited_at = UNSET
        else:
            credited_at = datetime.datetime.fromisoformat(_credited_at)

        failure_reason_code = d.pop("failure_reason_code", UNSET)

        receipt_url = d.pop("receipt_url", UNSET)

        tax_micro = d.pop("tax_micro", UNSET)

        total_charged_micro = d.pop("total_charged_micro", UNSET)

        payment = cls(
            amount_micro=amount_micro,
            created_at=created_at,
            first_paid=first_paid,
            id=id,
            kind=kind,
            price_micro=price_micro,
            refunded_micro=refunded_micro,
            status=status,
            bundle_key=bundle_key,
            card=card,
            credited_at=credited_at,
            failure_reason_code=failure_reason_code,
            receipt_url=receipt_url,
            tax_micro=tax_micro,
            total_charged_micro=total_charged_micro,
        )

        return payment
