from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CostPerCallRow")


@_attrs_define
class CostPerCallRow:
    """
    Attributes:
        answered_calls (int): Calls with a person on the line among the calls charged in the period: inbound answered
            and not free (short, spam, blocked and paused calls are free), outbound answered with any verdict except
            voicemail, carrier voicemail, IVR, screener, fax or SIT; no verdict counts as answered
        charge_micro (int): Settled call charges of the period; web tests and simulations excluded
        cost_micro (int | None): charge_micro divided by answered_calls, rounded to the nearest micro-USD; null when no
            call was answered
        key (str): Agent id, or none for calls without an agent; total for the whole workspace
        label (str | Unset): Agent name
    """

    answered_calls: int
    charge_micro: int
    cost_micro: int | None
    key: str
    label: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        answered_calls = self.answered_calls

        charge_micro = self.charge_micro

        cost_micro: int | None
        cost_micro = self.cost_micro

        key = self.key

        label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answered_calls": answered_calls,
                "charge_micro": charge_micro,
                "cost_micro": cost_micro,
                "key": key,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        answered_calls = d.pop("answered_calls")

        charge_micro = d.pop("charge_micro")

        def _parse_cost_micro(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cost_micro = _parse_cost_micro(d.pop("cost_micro"))

        key = d.pop("key")

        label = d.pop("label", UNSET)

        cost_per_call_row = cls(
            answered_calls=answered_calls,
            charge_micro=charge_micro,
            cost_micro=cost_micro,
            key=key,
            label=label,
        )

        return cost_per_call_row
