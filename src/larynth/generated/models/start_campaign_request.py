from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.launch_attestation import LaunchAttestation


T = TypeVar("T", bound="StartCampaignRequest")


@_attrs_define
class StartCampaignRequest:
    """
    Attributes:
        attest (LaunchAttestation):
    """

    attest: LaunchAttestation

    def to_dict(self) -> dict[str, Any]:
        attest = self.attest.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attest": attest,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.launch_attestation import LaunchAttestation

        d = dict(src_dict)
        attest = LaunchAttestation.from_dict(d.pop("attest"))

        start_campaign_request = cls(
            attest=attest,
        )

        return start_campaign_request
