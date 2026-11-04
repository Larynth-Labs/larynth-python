from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.ledger_entry_account import LedgerEntryAccount, check_ledger_entry_account
from ..models.ledger_entry_kind import LedgerEntryKind, check_ledger_entry_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerEntry")


@_attrs_define
class LedgerEntry:
    """
    Attributes:
        account (LedgerEntryAccount):
        amount_micro (int): Signed
        created_at (datetime.datetime):
        id (UUID):
        kind (LedgerEntryKind):
        transaction_id (UUID):
        balance_after_micro (int | Unset): Balance of the account after this entry
        call_id (str | Unset):
        memo (str | Unset):
        payment_id (UUID | Unset):
    """

    account: LedgerEntryAccount
    amount_micro: int
    created_at: datetime.datetime
    id: UUID
    kind: LedgerEntryKind
    transaction_id: UUID
    balance_after_micro: int | Unset = UNSET
    call_id: str | Unset = UNSET
    memo: str | Unset = UNSET
    payment_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account: str = self.account

        amount_micro = self.amount_micro

        created_at = self.created_at.isoformat()

        id = str(self.id)

        kind: str = self.kind

        transaction_id = str(self.transaction_id)

        balance_after_micro = self.balance_after_micro

        call_id = self.call_id

        memo = self.memo

        payment_id: str | Unset = UNSET
        if not isinstance(self.payment_id, Unset):
            payment_id = str(self.payment_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account": account,
                "amount_micro": amount_micro,
                "created_at": created_at,
                "id": id,
                "kind": kind,
                "transaction_id": transaction_id,
            }
        )
        if balance_after_micro is not UNSET:
            field_dict["balance_after_micro"] = balance_after_micro
        if call_id is not UNSET:
            field_dict["call_id"] = call_id
        if memo is not UNSET:
            field_dict["memo"] = memo
        if payment_id is not UNSET:
            field_dict["payment_id"] = payment_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        account = check_ledger_entry_account(d.pop("account"))

        amount_micro = d.pop("amount_micro")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        kind = check_ledger_entry_kind(d.pop("kind"))

        transaction_id = UUID(d.pop("transaction_id"))

        balance_after_micro = d.pop("balance_after_micro", UNSET)

        call_id = d.pop("call_id", UNSET)

        memo = d.pop("memo", UNSET)

        _payment_id = d.pop("payment_id", UNSET)
        payment_id: UUID | Unset
        if isinstance(_payment_id, Unset):
            payment_id = UNSET
        else:
            payment_id = UUID(_payment_id)

        ledger_entry = cls(
            account=account,
            amount_micro=amount_micro,
            created_at=created_at,
            id=id,
            kind=kind,
            transaction_id=transaction_id,
            balance_after_micro=balance_after_micro,
            call_id=call_id,
            memo=memo,
            payment_id=payment_id,
        )

        return ledger_entry
