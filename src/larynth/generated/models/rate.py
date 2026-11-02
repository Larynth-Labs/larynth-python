from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.rate_currency import RateCurrency, check_rate_currency
from ..models.rate_direction import RateDirection, check_rate_direction
from ..models.rate_kind import RateKind, check_rate_kind
from ..models.rate_mode import RateMode, check_rate_mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="Rate")


@_attrs_define
class Rate:
    """
    Attributes:
        currency (RateCurrency):
        effective_from (datetime.datetime):
        id (UUID):
        kind (RateKind):
        price_micro (int): Per minute for call_minute and transfer_minute, per month for number_month
        direction (RateDirection | Unset):
        effective_to (datetime.datetime | Unset):
        mode (RateMode | Unset):
    """

    currency: RateCurrency
    effective_from: datetime.datetime
    id: UUID
    kind: RateKind
    price_micro: int
    direction: RateDirection | Unset = UNSET
    effective_to: datetime.datetime | Unset = UNSET
    mode: RateMode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        currency: str = self.currency

        effective_from = self.effective_from.isoformat()

        id = str(self.id)

        kind: str = self.kind

        price_micro = self.price_micro

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction

        effective_to: str | Unset = UNSET
        if not isinstance(self.effective_to, Unset):
            effective_to = self.effective_to.isoformat()

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currency": currency,
                "effective_from": effective_from,
                "id": id,
                "kind": kind,
                "price_micro": price_micro,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction
        if effective_to is not UNSET:
            field_dict["effective_to"] = effective_to
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        currency = check_rate_currency(d.pop("currency"))

        effective_from = datetime.datetime.fromisoformat(d.pop("effective_from"))

        id = UUID(d.pop("id"))

        kind = check_rate_kind(d.pop("kind"))

        price_micro = d.pop("price_micro")

        _direction = d.pop("direction", UNSET)
        direction: RateDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = check_rate_direction(_direction)

        _effective_to = d.pop("effective_to", UNSET)
        effective_to: datetime.datetime | Unset
        if isinstance(_effective_to, Unset):
            effective_to = UNSET
        else:
            effective_to = datetime.datetime.fromisoformat(_effective_to)

        _mode = d.pop("mode", UNSET)
        mode: RateMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_rate_mode(_mode)

        rate = cls(
            currency=currency,
            effective_from=effective_from,
            id=id,
            kind=kind,
            price_micro=price_micro,
            direction=direction,
            effective_to=effective_to,
            mode=mode,
        )

        return rate
