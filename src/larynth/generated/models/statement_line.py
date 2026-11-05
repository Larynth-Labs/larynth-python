from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.statement_line_kind import StatementLineKind, check_statement_line_kind

if TYPE_CHECKING:
    from ..models.statement_line_params import StatementLineParams


T = TypeVar("T", bound="StatementLine")


@_attrs_define
class StatementLine:
    """
    Attributes:
        amount_micro (int): Signed
        at (datetime.datetime): Time of the line's last transaction
        balance_after_micro (int): Customer credit (available + held + promo + bundle) after this line
        id (UUID):
        kind (StatementLineKind):
        local_date (datetime.date): Day in the workspace time zone
        memo_key (str):
        params (StatementLineParams):
    """

    amount_micro: int
    at: datetime.datetime
    balance_after_micro: int
    id: UUID
    kind: StatementLineKind
    local_date: datetime.date
    memo_key: str
    params: StatementLineParams

    def to_dict(self) -> dict[str, Any]:
        amount_micro = self.amount_micro

        at = self.at.isoformat()

        balance_after_micro = self.balance_after_micro

        id = str(self.id)

        kind: str = self.kind

        local_date = self.local_date.isoformat()

        memo_key = self.memo_key

        params = self.params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount_micro": amount_micro,
                "at": at,
                "balance_after_micro": balance_after_micro,
                "id": id,
                "kind": kind,
                "local_date": local_date,
                "memo_key": memo_key,
                "params": params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.statement_line_params import StatementLineParams

        d = dict(src_dict)
        amount_micro = d.pop("amount_micro")

        at = datetime.datetime.fromisoformat(d.pop("at"))

        balance_after_micro = d.pop("balance_after_micro")

        id = UUID(d.pop("id"))

        kind = check_statement_line_kind(d.pop("kind"))

        local_date = datetime.date.fromisoformat(d.pop("local_date"))

        memo_key = d.pop("memo_key")

        params = StatementLineParams.from_dict(d.pop("params"))

        statement_line = cls(
            amount_micro=amount_micro,
            at=at,
            balance_after_micro=balance_after_micro,
            id=id,
            kind=kind,
            local_date=local_date,
            memo_key=memo_key,
            params=params,
        )

        return statement_line
