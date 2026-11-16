from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.analytics_usage_bucket import AnalyticsUsageBucket


T = TypeVar("T", bound="AnalyticsUsageSplit")


@_attrs_define
class AnalyticsUsageSplit:
    """
    Attributes:
        billed_minutes (int):
        calls (int):
        inbound (AnalyticsUsageBucket):
        outbound (AnalyticsUsageBucket):
        spend_micro (int): Charges written to the ledger, micro-USD
        web (AnalyticsUsageBucket):
    """

    billed_minutes: int
    calls: int
    inbound: AnalyticsUsageBucket
    outbound: AnalyticsUsageBucket
    spend_micro: int
    web: AnalyticsUsageBucket

    def to_dict(self) -> dict[str, Any]:
        billed_minutes = self.billed_minutes

        calls = self.calls

        inbound = self.inbound.to_dict()

        outbound = self.outbound.to_dict()

        spend_micro = self.spend_micro

        web = self.web.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billed_minutes": billed_minutes,
                "calls": calls,
                "inbound": inbound,
                "outbound": outbound,
                "spend_micro": spend_micro,
                "web": web,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_usage_bucket import AnalyticsUsageBucket

        d = dict(src_dict)
        billed_minutes = d.pop("billed_minutes")

        calls = d.pop("calls")

        inbound = AnalyticsUsageBucket.from_dict(d.pop("inbound"))

        outbound = AnalyticsUsageBucket.from_dict(d.pop("outbound"))

        spend_micro = d.pop("spend_micro")

        web = AnalyticsUsageBucket.from_dict(d.pop("web"))

        analytics_usage_split = cls(
            billed_minutes=billed_minutes,
            calls=calls,
            inbound=inbound,
            outbound=outbound,
            spend_micro=spend_micro,
            web=web,
        )

        return analytics_usage_split
