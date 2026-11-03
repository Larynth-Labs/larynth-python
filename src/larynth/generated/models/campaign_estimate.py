from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.campaign_estimate_basis import (
    CampaignEstimateBasis,
    check_campaign_estimate_basis,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CampaignEstimate")


@_attrs_define
class CampaignEstimate:
    """
    Attributes:
        available_micro (int):
        basis (CampaignEstimateBasis): Where the answer rate and minutes came from
        billed_minutes_per_answered (float): Started minutes
        callable_ (int):
        covers_ratio (float):
        estimate_micro (int):
        expected_answer_rate (float):
        expected_answered (int):
        high_micro (int):
        low_micro (int):
        premium_micro_per_min (int):
        rate_micro_per_min (int):
        daily_spend_cap_micro (int | Unset):
        days_to_finish (float | Unset):
    """

    available_micro: int
    basis: CampaignEstimateBasis
    billed_minutes_per_answered: float
    callable_: int
    covers_ratio: float
    estimate_micro: int
    expected_answer_rate: float
    expected_answered: int
    high_micro: int
    low_micro: int
    premium_micro_per_min: int
    rate_micro_per_min: int
    daily_spend_cap_micro: int | Unset = UNSET
    days_to_finish: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        available_micro = self.available_micro

        basis: str = self.basis

        billed_minutes_per_answered = self.billed_minutes_per_answered

        callable_ = self.callable_

        covers_ratio = self.covers_ratio

        estimate_micro = self.estimate_micro

        expected_answer_rate = self.expected_answer_rate

        expected_answered = self.expected_answered

        high_micro = self.high_micro

        low_micro = self.low_micro

        premium_micro_per_min = self.premium_micro_per_min

        rate_micro_per_min = self.rate_micro_per_min

        daily_spend_cap_micro = self.daily_spend_cap_micro

        days_to_finish = self.days_to_finish

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "available_micro": available_micro,
                "basis": basis,
                "billed_minutes_per_answered": billed_minutes_per_answered,
                "callable": callable_,
                "covers_ratio": covers_ratio,
                "estimate_micro": estimate_micro,
                "expected_answer_rate": expected_answer_rate,
                "expected_answered": expected_answered,
                "high_micro": high_micro,
                "low_micro": low_micro,
                "premium_micro_per_min": premium_micro_per_min,
                "rate_micro_per_min": rate_micro_per_min,
            }
        )
        if daily_spend_cap_micro is not UNSET:
            field_dict["daily_spend_cap_micro"] = daily_spend_cap_micro
        if days_to_finish is not UNSET:
            field_dict["days_to_finish"] = days_to_finish

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        available_micro = d.pop("available_micro")

        basis = check_campaign_estimate_basis(d.pop("basis"))

        billed_minutes_per_answered = d.pop("billed_minutes_per_answered")

        callable_ = d.pop("callable")

        covers_ratio = d.pop("covers_ratio")

        estimate_micro = d.pop("estimate_micro")

        expected_answer_rate = d.pop("expected_answer_rate")

        expected_answered = d.pop("expected_answered")

        high_micro = d.pop("high_micro")

        low_micro = d.pop("low_micro")

        premium_micro_per_min = d.pop("premium_micro_per_min")

        rate_micro_per_min = d.pop("rate_micro_per_min")

        daily_spend_cap_micro = d.pop("daily_spend_cap_micro", UNSET)

        days_to_finish = d.pop("days_to_finish", UNSET)

        campaign_estimate = cls(
            available_micro=available_micro,
            basis=basis,
            billed_minutes_per_answered=billed_minutes_per_answered,
            callable_=callable_,
            covers_ratio=covers_ratio,
            estimate_micro=estimate_micro,
            expected_answer_rate=expected_answer_rate,
            expected_answered=expected_answered,
            high_micro=high_micro,
            low_micro=low_micro,
            premium_micro_per_min=premium_micro_per_min,
            rate_micro_per_min=rate_micro_per_min,
            daily_spend_cap_micro=daily_spend_cap_micro,
            days_to_finish=days_to_finish,
        )

        return campaign_estimate
