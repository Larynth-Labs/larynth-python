from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alert_rule_update_channels_item import (
    AlertRuleUpdateChannelsItem,
    check_alert_rule_update_channels_item,
)
from ..models.alert_rule_update_directions_item import (
    AlertRuleUpdateDirectionsItem,
    check_alert_rule_update_directions_item,
)
from ..models.alert_rule_update_recipient_roles_item import (
    AlertRuleUpdateRecipientRolesItem,
    check_alert_rule_update_recipient_roles_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_condition import AlertCondition


T = TypeVar("T", bound="AlertRuleUpdate")


@_attrs_define
class AlertRuleUpdate:
    """
    Attributes:
        assistant_ids (list[str] | Unset): An empty list sets all agents
        channel_ids (list[str] | Unset):
        channels (list[AlertRuleUpdateChannelsItem] | Unset):
        condition (AlertCondition | Unset):
        directions (list[AlertRuleUpdateDirectionsItem] | Unset):
        enabled (bool | Unset):
        include_details (bool | Unset):
        max_per_hour (int | Unset):
        name (str | Unset):
        recipient_roles (list[AlertRuleUpdateRecipientRolesItem] | Unset):
        recipient_user_ids (list[str] | Unset):
    """

    assistant_ids: list[str] | Unset = UNSET
    channel_ids: list[str] | Unset = UNSET
    channels: list[AlertRuleUpdateChannelsItem] | Unset = UNSET
    condition: AlertCondition | Unset = UNSET
    directions: list[AlertRuleUpdateDirectionsItem] | Unset = UNSET
    enabled: bool | Unset = UNSET
    include_details: bool | Unset = UNSET
    max_per_hour: int | Unset = UNSET
    name: str | Unset = UNSET
    recipient_roles: list[AlertRuleUpdateRecipientRolesItem] | Unset = UNSET
    recipient_user_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_ids: list[str] | Unset = UNSET
        if not isinstance(self.assistant_ids, Unset):
            assistant_ids = self.assistant_ids

        channel_ids: list[str] | Unset = UNSET
        if not isinstance(self.channel_ids, Unset):
            channel_ids = self.channel_ids

        channels: list[str] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item: str = channels_item_data
                channels.append(channels_item)

        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        directions: list[str] | Unset = UNSET
        if not isinstance(self.directions, Unset):
            directions = []
            for directions_item_data in self.directions:
                directions_item: str = directions_item_data
                directions.append(directions_item)

        enabled = self.enabled

        include_details = self.include_details

        max_per_hour = self.max_per_hour

        name = self.name

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

        field_dict.update({})
        if assistant_ids is not UNSET:
            field_dict["assistant_ids"] = assistant_ids
        if channel_ids is not UNSET:
            field_dict["channel_ids"] = channel_ids
        if channels is not UNSET:
            field_dict["channels"] = channels
        if condition is not UNSET:
            field_dict["condition"] = condition
        if directions is not UNSET:
            field_dict["directions"] = directions
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if include_details is not UNSET:
            field_dict["include_details"] = include_details
        if max_per_hour is not UNSET:
            field_dict["max_per_hour"] = max_per_hour
        if name is not UNSET:
            field_dict["name"] = name
        if recipient_roles is not UNSET:
            field_dict["recipient_roles"] = recipient_roles
        if recipient_user_ids is not UNSET:
            field_dict["recipient_user_ids"] = recipient_user_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_condition import AlertCondition

        d = dict(src_dict)
        assistant_ids = cast(list[str], d.pop("assistant_ids", UNSET))

        channel_ids = cast(list[str], d.pop("channel_ids", UNSET))

        _channels = d.pop("channels", UNSET)
        channels: list[AlertRuleUpdateChannelsItem] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = check_alert_rule_update_channels_item(
                    channels_item_data
                )

                channels.append(channels_item)

        _condition = d.pop("condition", UNSET)
        condition: AlertCondition | Unset
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = AlertCondition.from_dict(_condition)

        _directions = d.pop("directions", UNSET)
        directions: list[AlertRuleUpdateDirectionsItem] | Unset = UNSET
        if _directions is not UNSET:
            directions = []
            for directions_item_data in _directions:
                directions_item = check_alert_rule_update_directions_item(
                    directions_item_data
                )

                directions.append(directions_item)

        enabled = d.pop("enabled", UNSET)

        include_details = d.pop("include_details", UNSET)

        max_per_hour = d.pop("max_per_hour", UNSET)

        name = d.pop("name", UNSET)

        _recipient_roles = d.pop("recipient_roles", UNSET)
        recipient_roles: list[AlertRuleUpdateRecipientRolesItem] | Unset = UNSET
        if _recipient_roles is not UNSET:
            recipient_roles = []
            for recipient_roles_item_data in _recipient_roles:
                recipient_roles_item = check_alert_rule_update_recipient_roles_item(
                    recipient_roles_item_data
                )

                recipient_roles.append(recipient_roles_item)

        recipient_user_ids = cast(list[str], d.pop("recipient_user_ids", UNSET))

        alert_rule_update = cls(
            assistant_ids=assistant_ids,
            channel_ids=channel_ids,
            channels=channels,
            condition=condition,
            directions=directions,
            enabled=enabled,
            include_details=include_details,
            max_per_hour=max_per_hour,
            name=name,
            recipient_roles=recipient_roles,
            recipient_user_ids=recipient_user_ids,
        )

        return alert_rule_update
