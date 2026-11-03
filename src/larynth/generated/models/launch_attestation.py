from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LaunchAttestation")


@_attrs_define
class LaunchAttestation:
    """
    Attributes:
        accepted (bool): Must be true
        text_version (str):
    """

    accepted: bool
    text_version: str

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        text_version = self.text_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accepted": accepted,
                "text_version": text_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        accepted = d.pop("accepted")

        text_version = d.pop("text_version")

        launch_attestation = cls(
            accepted=accepted,
            text_version=text_version,
        )

        return launch_attestation
