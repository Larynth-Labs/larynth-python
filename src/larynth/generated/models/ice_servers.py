from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.ice_server import ICEServer


T = TypeVar("T", bound="ICEServers")


@_attrs_define
class ICEServers:
    """
    Attributes:
        expires_at (datetime.datetime): Fetch a new set before this time
        ice_servers (list[ICEServer]): Pass as RTCConfiguration.iceServers
    """

    expires_at: datetime.datetime
    ice_servers: list[ICEServer]

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at.isoformat()

        ice_servers = []
        for ice_servers_item_data in self.ice_servers:
            ice_servers_item = ice_servers_item_data.to_dict()
            ice_servers.append(ice_servers_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expires_at": expires_at,
                "ice_servers": ice_servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ice_server import ICEServer

        d = dict(src_dict)
        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        ice_servers = []
        _ice_servers = d.pop("ice_servers")
        for ice_servers_item_data in _ice_servers:
            ice_servers_item = ICEServer.from_dict(ice_servers_item_data)

            ice_servers.append(ice_servers_item)

        ice_servers = cls(
            expires_at=expires_at,
            ice_servers=ice_servers,
        )

        return ice_servers
