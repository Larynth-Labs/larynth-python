from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_rule_create_channels_item import (
    AlertRuleCreateChannelsItem,
    check_alert_rule_create_channels_item,
)
from ..models.alert_rule_create_directions_item import (
    AlertRuleCreateDirectionsItem,
    check_alert_rule_create_directions_item,
)
from ..models.alert_rule_create_preset import (
    AlertRuleCreatePreset,
    check_alert_rule_create_preset,
)
from ..models.alert_rule_create_recipient_roles_item import (
    AlertRuleCreateRecipientRolesItem,
    check_alert_rule_create_recipient_roles_item,
)
from ..models.alert_rule_create_trigger import (
    AlertRuleCreateTrigger,
    check_alert_rule_create_trigger,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_condition import AlertCondition


T = TypeVar("T", bound="AlertRuleCreate")


@_attrs_define
class AlertRuleCreate:
    """
    Attributes:
        channels (list[AlertRuleCreateChannelsItem]):
        condition (AlertCondition):
        name (str):
        trigger (AlertRuleCreateTrigger):
        assistant_ids (list[str] | Unset): Unset or null means all agents
        channel_ids (list[str] | Unset):
        directions (list[AlertRuleCreateDirectionsItem] | Unset): Unset is inbound
        enabled (bool | Unset): Unset is true
        include_details (bool | Unset): Unset is true
        max_per_hour (int | Unset): Unset is 20
        preset (AlertRuleCreatePreset | Unset):
        recipient_roles (list[AlertRuleCreateRecipientRolesItem] | Unset):
        recipient_user_ids (list[str] | Unset):
    """

    channels: list[AlertRuleCreateChannelsItem]
    condition: AlertCondition
    name: str
    trigger: AlertRuleCreateTrigger
    assistant_ids: list[str] | Unset = UNSET
    channel_ids: list[str] | Unset = UNSET
    directions: list[AlertRuleCreateDirectionsItem] | Unset = UNSET
    enabled: bool | Unset = UNSET
    include_details: bool | Unset = UNSET
    max_per_hour: int | Unset = UNSET
    preset: AlertRuleCreatePreset | Unset = UNSET
    recipient_roles: list[AlertRuleCreateRecipientRolesItem] | Unset = UNSET
    recipient_user_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channels = []
        for channels_item_data in self.channels:
            channels_item: str = channels_item_data
            channels.append(channels_item)

        condition = self.condition.to_dict()

        name = self.name

        trigger: str = self.trigger

        assistant_ids: list[str] | Unset = UNSET
        if not isinstance(self.assistant_ids, Unset):
            assistant_ids = self.assistant_ids

        channel_ids: list[str] | Unset = UNSET
        if not isinstance(self.channel_ids, Unset):
            channel_ids = self.channel_ids

        directions: list[str] | Unset = UNSET
        if not isinstance(self.directions, Unset):
            directions = []
            for directions_item_data in self.directions:
                directions_item: str = directions_item_data
                directions.append(directions_item)

        enabled = self.enabled

        include_details = self.include_details

        max_per_hour = self.max_per_hour

        preset: str | Unset = UNSET
        if not isinstance(self.preset, Unset):
            preset = self.preset

        recipient_roles: list[str] | Unset = UNSET
        if not isinstance(self.recipient_roles, Unset):
            recipient_roles = []
            for recipient_roles_item_data in self.recipient_roles:
                recipient_roles_item: str = recipient_roles_item_data
                recipient_roles.append(recipient_roles_item)

        recipient_user_ids: list[str] | Unset = UNSET
        if not isinstance(self.recipient_user_ids, Unset):
            recipient_user_ids = self.recipient_user_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "channels": channels,
                "condition": condition,
                "name": name,
                "trigger": trigger,
            }
        )
        if assistant_ids is not UNSET:
            field_dict["assistant_ids"] = assistant_ids
        if channel_ids is not UNSET:
            field_dict["channel_ids"] = channel_ids
        if directions is not UNSET:
            field_dict["directions"] = directions
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if include_details is not UNSET:
            field_dict["include_details"] = include_details
        if max_per_hour is not UNSET:
            field_dict["max_per_hour"] = max_per_hour
        if preset is not UNSET:
            field_dict["preset"] = preset
        if recipient_roles is not UNSET:
            field_dict["recipient_roles"] = recipient_roles
        if recipient_user_ids is not UNSET:
            field_dict["recipient_user_ids"] = recipient_user_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_condition import AlertCondition

        d = dict(src_dict)
        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = check_alert_rule_create_channels_item(channels_item_data)

            channels.append(channels_item)

        condition = AlertCondition.from_dict(d.pop("condition"))

        name = d.pop("name")

        trigger = check_alert_rule_create_trigger(d.pop("trigger"))

        assistant_ids = cast(list[str], d.pop("assistant_ids", UNSET))

        channel_ids = cast(list[str], d.pop("channel_ids", UNSET))

        _directions = d.pop("directions", UNSET)
        directions: list[AlertRuleCreateDirectionsItem] | Unset = UNSET
        if _directions is not UNSET:
            directions = []
            for directions_item_data in _directions:
                directions_item = check_alert_rule_create_directions_item(
                    directions_item_data
                )

                directions.append(directions_item)

        enabled = d.pop("enabled", UNSET)

        include_details = d.pop("include_details", UNSET)

        max_per_hour = d.pop("max_per_hour", UNSET)

        _preset = d.pop("preset", UNSET)
        preset: AlertRuleCreatePreset | Unset
        if isinstance(_preset, Unset):
            preset = UNSET
        else:
            preset = check_alert_rule_create_preset(_preset)

        _recipient_roles = d.pop("recipient_roles", UNSET)
        recipient_roles: list[AlertRuleCreateRecipientRolesItem] | Unset = UNSET
        if _recipient_roles is not UNSET:
            recipient_roles = []
            for recipient_roles_item_data in _recipient_roles:
                recipient_roles_item = check_alert_rule_create_recipient_roles_item(
                    recipient_roles_item_data
                )

                recipient_roles.append(recipient_roles_item)

        recipient_user_ids = cast(list[str], d.pop("recipient_user_ids", UNSET))

        alert_rule_create = cls(
            channels=channels,
            condition=condition,
            name=name,
            trigger=trigger,
            assistant_ids=assistant_ids,
            channel_ids=channel_ids,
            directions=directions,
            enabled=enabled,
            include_details=include_details,
            max_per_hour=max_per_hour,
            preset=preset,
            recipient_roles=recipient_roles,
            recipient_user_ids=recipient_user_ids,
        )

        return alert_rule_create
