from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.transfer_destination_mode import (
    TransferDestinationMode,
    check_transfer_destination_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferDestination")


@_attrs_define
class TransferDestination:
    """
    Attributes:
        mode (TransferDestinationMode): cold hands the caller over directly; warm puts the caller on hold, briefs the
            human, then bridges
        name (str): The agent picks a destination by this name
        description (str | Unset): When to use this destination; shown to the agent
        e164 (str | Unset): Phone number; set exactly one of e164 and sip_uri
        ring_timeout_seconds (int | Unset): How long to ring the human before returning to the caller. Unset is 25
        sip_uri (str | Unset): sip: or sips: URI; cold transfers only, by SIP REFER
        whisper (str | Unset): Warm only: what the agent says to the human before bridging. Variables {{summary}} and
            {{destination}}
    """

    mode: TransferDestinationMode
    name: str
    description: str | Unset = UNSET
    e164: str | Unset = UNSET
    ring_timeout_seconds: int | Unset = UNSET
    sip_uri: str | Unset = UNSET
    whisper: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: str = self.mode

        name = self.name

        description = self.description

        e164 = self.e164

        ring_timeout_seconds = self.ring_timeout_seconds

        sip_uri = self.sip_uri

        whisper = self.whisper

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if e164 is not UNSET:
            field_dict["e164"] = e164
        if ring_timeout_seconds is not UNSET:
            field_dict["ring_timeout_seconds"] = ring_timeout_seconds
        if sip_uri is not UNSET:
            field_dict["sip_uri"] = sip_uri
        if whisper is not UNSET:
            field_dict["whisper"] = whisper

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = check_transfer_destination_mode(d.pop("mode"))

        name = d.pop("name")

        description = d.pop("description", UNSET)

        e164 = d.pop("e164", UNSET)

        ring_timeout_seconds = d.pop("ring_timeout_seconds", UNSET)

        sip_uri = d.pop("sip_uri", UNSET)

        whisper = d.pop("whisper", UNSET)

        transfer_destination = cls(
            mode=mode,
            name=name,
            description=description,
            e164=e164,
            ring_timeout_seconds=ring_timeout_seconds,
            sip_uri=sip_uri,
            whisper=whisper,
        )

        return transfer_destination
