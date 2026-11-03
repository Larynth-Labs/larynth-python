from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.after_hours_target import AfterHoursTarget
    from ..models.routing_hours import RoutingHours
    from ..models.routing_target import RoutingTarget


T = TypeVar("T", bound="RoutingPlan")


@_attrs_define
class RoutingPlan:
    """
    Attributes:
        open_ (RoutingTarget):
        after_hours (AfterHoursTarget | Unset):
        fallback_e164 (str | Unset): Transfer to a person when the agent can't pick up: paused agent, agent start
            failure, and carrier failover when no engine answers (not billed). Engine-bridged minutes bill at
            transfer_minute
        hours (RoutingHours | Unset):
        revision (int | Unset):
    """

    open_: RoutingTarget
    after_hours: AfterHoursTarget | Unset = UNSET
    fallback_e164: str | Unset = UNSET
    hours: RoutingHours | Unset = UNSET
    revision: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_.to_dict()

        after_hours: dict[str, Any] | Unset = UNSET
        if not isinstance(self.after_hours, Unset):
            after_hours = self.after_hours.to_dict()

        fallback_e164 = self.fallback_e164

        hours: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hours, Unset):
            hours = self.hours.to_dict()

        revision = self.revision

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "open": open_,
            }
        )
        if after_hours is not UNSET:
            field_dict["after_hours"] = after_hours
        if fallback_e164 is not UNSET:
            field_dict["fallback_e164"] = fallback_e164
        if hours is not UNSET:
            field_dict["hours"] = hours
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.after_hours_target import AfterHoursTarget
        from ..models.routing_hours import RoutingHours
        from ..models.routing_target import RoutingTarget

        d = dict(src_dict)
        open_ = RoutingTarget.from_dict(d.pop("open"))

        _after_hours = d.pop("after_hours", UNSET)
        after_hours: AfterHoursTarget | Unset
        if isinstance(_after_hours, Unset):
            after_hours = UNSET
        else:
            after_hours = AfterHoursTarget.from_dict(_after_hours)

        fallback_e164 = d.pop("fallback_e164", UNSET)

        _hours = d.pop("hours", UNSET)
        hours: RoutingHours | Unset
        if isinstance(_hours, Unset):
            hours = UNSET
        else:
            hours = RoutingHours.from_dict(_hours)

        revision = d.pop("revision", UNSET)

        routing_plan = cls(
            open_=open_,
            after_hours=after_hours,
            fallback_e164=fallback_e164,
            hours=hours,
            revision=revision,
        )

        return routing_plan
