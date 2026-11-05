from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.daily_spend_limit import DailySpendLimit
    from ..models.monthly_spend_limit import MonthlySpendLimit
    from ..models.platform_spend_caps import PlatformSpendCaps


T = TypeVar("T", bound="SpendLimits")


@_attrs_define
class SpendLimits:
    """
    Attributes:
        daily (DailySpendLimit):
        monthly (MonthlySpendLimit):
        platform (PlatformSpendCaps):
        reached (None | str): daily or monthly once that limit is reached, else null
        revision (int):
        stop_inbound (bool): Reaching a limit also stops answering inbound calls
    """

    daily: DailySpendLimit
    monthly: MonthlySpendLimit
    platform: PlatformSpendCaps
    reached: None | str
    revision: int
    stop_inbound: bool

    def to_dict(self) -> dict[str, Any]:
        daily = self.daily.to_dict()

        monthly = self.monthly.to_dict()

        platform = self.platform.to_dict()

        reached: None | str
        reached = self.reached

        revision = self.revision

        stop_inbound = self.stop_inbound

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "daily": daily,
                "monthly": monthly,
                "platform": platform,
                "reached": reached,
                "revision": revision,
                "stop_inbound": stop_inbound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.daily_spend_limit import DailySpendLimit
        from ..models.monthly_spend_limit import MonthlySpendLimit
        from ..models.platform_spend_caps import PlatformSpendCaps

        d = dict(src_dict)
        daily = DailySpendLimit.from_dict(d.pop("daily"))

        monthly = MonthlySpendLimit.from_dict(d.pop("monthly"))

        platform = PlatformSpendCaps.from_dict(d.pop("platform"))

        def _parse_reached(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reached = _parse_reached(d.pop("reached"))

        revision = d.pop("revision")

        stop_inbound = d.pop("stop_inbound")

        spend_limits = cls(
            daily=daily,
            monthly=monthly,
            platform=platform,
            reached=reached,
            revision=revision,
            stop_inbound=stop_inbound,
        )

        return spend_limits
