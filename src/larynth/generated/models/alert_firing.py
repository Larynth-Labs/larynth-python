from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.alert_firing_state import AlertFiringState, check_alert_firing_state
from ..models.alert_firing_trigger import AlertFiringTrigger, check_alert_firing_trigger

if TYPE_CHECKING:
    from ..models.alert_delivery import AlertDelivery
    from ..models.alert_match import AlertMatch


T = TypeVar("T", bound="AlertFiring")


@_attrs_define
class AlertFiring:
    """
    Attributes:
        call_id (str):
        deliveries (list[AlertDelivery]):
        fired_at (datetime.datetime):
        id (UUID):
        matched (AlertMatch):
        rule_id (UUID):
        rule_name (str):
        state (AlertFiringState):
        trigger (AlertFiringTrigger):
    """

    call_id: str
    deliveries: list[AlertDelivery]
    fired_at: datetime.datetime
    id: UUID
    matched: AlertMatch
    rule_id: UUID
    rule_name: str
    state: AlertFiringState
    trigger: AlertFiringTrigger

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        deliveries = []
        for deliveries_item_data in self.deliveries:
            deliveries_item = deliveries_item_data.to_dict()
            deliveries.append(deliveries_item)

        fired_at = self.fired_at.isoformat()

        id = str(self.id)

        matched = self.matched.to_dict()

        rule_id = str(self.rule_id)

        rule_name = self.rule_name

        state: str = self.state

        trigger: str = self.trigger

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "call_id": call_id,
                "deliveries": deliveries,
                "fired_at": fired_at,
                "id": id,
                "matched": matched,
                "rule_id": rule_id,
                "rule_name": rule_name,
                "state": state,
                "trigger": trigger,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_delivery import AlertDelivery
        from ..models.alert_match import AlertMatch

        d = dict(src_dict)
        call_id = d.pop("call_id")

        deliveries = []
        _deliveries = d.pop("deliveries")
        for deliveries_item_data in _deliveries:
            deliveries_item = AlertDelivery.from_dict(deliveries_item_data)

            deliveries.append(deliveries_item)

        fired_at = datetime.datetime.fromisoformat(d.pop("fired_at"))

        id = UUID(d.pop("id"))

        matched = AlertMatch.from_dict(d.pop("matched"))

        rule_id = UUID(d.pop("rule_id"))

        rule_name = d.pop("rule_name")

        state = check_alert_firing_state(d.pop("state"))

        trigger = check_alert_firing_trigger(d.pop("trigger"))

        alert_firing = cls(
            call_id=call_id,
            deliveries=deliveries,
            fired_at=fired_at,
            id=id,
            matched=matched,
            rule_id=rule_id,
            rule_name=rule_name,
            state=state,
            trigger=trigger,
        )

        return alert_firing
