from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.alert_rule_channels_item import (
    AlertRuleChannelsItem,
    check_alert_rule_channels_item,
)
from ..models.alert_rule_directions_item import (
    AlertRuleDirectionsItem,
    check_alert_rule_directions_item,
)
from ..models.alert_rule_inactive_channels_item import (
    AlertRuleInactiveChannelsItem,
    check_alert_rule_inactive_channels_item,
)
from ..models.alert_rule_preset import AlertRulePreset, check_alert_rule_preset
from ..models.alert_rule_recipient_roles_item import (
    AlertRuleRecipientRolesItem,
    check_alert_rule_recipient_roles_item,
)
from ..models.alert_rule_trigger import AlertRuleTrigger, check_alert_rule_trigger

if TYPE_CHECKING:
    from ..models.alert_condition import AlertCondition


T = TypeVar("T", bound="AlertRule")


@_attrs_define
class AlertRule:
    """
    Attributes:
        assistant_ids (list[str] | None): Null means all agents
        channel_ids (list[str]): Slack and Telegram channels
        channels (list[AlertRuleChannelsItem]):
        condition (AlertCondition):
        created_at (datetime.datetime):
        directions (list[AlertRuleDirectionsItem]):
        enabled (bool):
        fired_7d (int): Read-only; firings in the last 7 days
        id (UUID):
        inactive_channels (list[AlertRuleInactiveChannelsItem]): Read-only. Saved channels that do not send right now,
            such as sms while SMS alerts are not available
        include_details (bool): False sends only the rule name and a link
        last_fired_at (datetime.datetime | None): Read-only
        max_per_hour (int):
        name (str):
        preset (AlertRulePreset): Preset it was created from; informational
        recipient_roles (list[AlertRuleRecipientRolesItem]): Everyone at or above the role
        recipient_user_ids (list[str]):
        trigger (AlertRuleTrigger):
        updated_at (datetime.datetime):
    """

    assistant_ids: list[str] | None
    channel_ids: list[str]
    channels: list[AlertRuleChannelsItem]
    condition: AlertCondition
    created_at: datetime.datetime
    directions: list[AlertRuleDirectionsItem]
    enabled: bool
    fired_7d: int
    id: UUID
    inactive_channels: list[AlertRuleInactiveChannelsItem]
    include_details: bool
    last_fired_at: datetime.datetime | None
    max_per_hour: int
    name: str
    preset: AlertRulePreset
    recipient_roles: list[AlertRuleRecipientRolesItem]
    recipient_user_ids: list[str]
    trigger: AlertRuleTrigger
    updated_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        assistant_ids: list[str] | None
        if isinstance(self.assistant_ids, list):
            assistant_ids = self.assistant_ids

        else:
            assistant_ids = self.assistant_ids

        channel_ids = self.channel_ids

        channels = []
        for channels_item_data in self.channels:
            channels_item: str = channels_item_data
            channels.append(channels_item)

        condition = self.condition.to_dict()

        created_at = self.created_at.isoformat()

        directions = []
        for directions_item_data in self.directions:
            directions_item: str = directions_item_data
            directions.append(directions_item)

        enabled = self.enabled

        fired_7d = self.fired_7d

        id = str(self.id)

        inactive_channels = []
        for inactive_channels_item_data in self.inactive_channels:
            inactive_channels_item: str = inactive_channels_item_data
            inactive_channels.append(inactive_channels_item)

        include_details = self.include_details

        last_fired_at: None | str
        if isinstance(self.last_fired_at, datetime.datetime):
            last_fired_at = self.last_fired_at.isoformat()
        else:
            last_fired_at = self.last_fired_at

        max_per_hour = self.max_per_hour

        name = self.name

        preset: str = self.preset

        recipient_roles = []
        for recipient_roles_item_data in self.recipient_roles:
            recipient_roles_item: str = recipient_roles_item_data
            recipient_roles.append(recipient_roles_item)

        recipient_user_ids = self.recipient_user_ids

        trigger: str = self.trigger

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_ids": assistant_ids,
                "channel_ids": channel_ids,
                "channels": channels,
                "condition": condition,
                "created_at": created_at,
                "directions": directions,
                "enabled": enabled,
                "fired_7d": fired_7d,
                "id": id,
                "inactive_channels": inactive_channels,
                "include_details": include_details,
                "last_fired_at": last_fired_at,
                "max_per_hour": max_per_hour,
                "name": name,
                "preset": preset,
                "recipient_roles": recipient_roles,
                "recipient_user_ids": recipient_user_ids,
                "trigger": trigger,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_condition import AlertCondition

        d = dict(src_dict)

        def _parse_assistant_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assistant_ids_type_0 = cast(list[str], data)

                return assistant_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        assistant_ids = _parse_assistant_ids(d.pop("assistant_ids"))

        channel_ids = cast(list[str], d.pop("channel_ids"))

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = check_alert_rule_channels_item(channels_item_data)

            channels.append(channels_item)

        condition = AlertCondition.from_dict(d.pop("condition"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        directions = []
        _directions = d.pop("directions")
        for directions_item_data in _directions:
            directions_item = check_alert_rule_directions_item(directions_item_data)

            directions.append(directions_item)

        enabled = d.pop("enabled")

        fired_7d = d.pop("fired_7d")

        id = UUID(d.pop("id"))

        inactive_channels = []
        _inactive_channels = d.pop("inactive_channels")
        for inactive_channels_item_data in _inactive_channels:
            inactive_channels_item = check_alert_rule_inactive_channels_item(
                inactive_channels_item_data
            )

            inactive_channels.append(inactive_channels_item)

        include_details = d.pop("include_details")

        def _parse_last_fired_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_fired_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_fired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_fired_at = _parse_last_fired_at(d.pop("last_fired_at"))

        max_per_hour = d.pop("max_per_hour")

        name = d.pop("name")

        preset = check_alert_rule_preset(d.pop("preset"))

        recipient_roles = []
        _recipient_roles = d.pop("recipient_roles")
        for recipient_roles_item_data in _recipient_roles:
            recipient_roles_item = check_alert_rule_recipient_roles_item(
                recipient_roles_item_data
            )

            recipient_roles.append(recipient_roles_item)

        recipient_user_ids = cast(list[str], d.pop("recipient_user_ids"))

        trigger = check_alert_rule_trigger(d.pop("trigger"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        alert_rule = cls(
            assistant_ids=assistant_ids,
            channel_ids=channel_ids,
            channels=channels,
            condition=condition,
            created_at=created_at,
            directions=directions,
            enabled=enabled,
            fired_7d=fired_7d,
            id=id,
            inactive_channels=inactive_channels,
            include_details=include_details,
            last_fired_at=last_fired_at,
            max_per_hour=max_per_hour,
            name=name,
            preset=preset,
            recipient_roles=recipient_roles,
            recipient_user_ids=recipient_user_ids,
            trigger=trigger,
            updated_at=updated_at,
        )

        return alert_rule
