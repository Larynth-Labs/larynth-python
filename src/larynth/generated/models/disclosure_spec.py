from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.disclosure_spec_inbound_ai import (
    DisclosureSpecInboundAi,
    check_disclosure_spec_inbound_ai,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DisclosureSpec")


@_attrs_define
class DisclosureSpec:
    """
    Attributes:
        inbound_ai (DisclosureSpecInboundAi | Unset): The inbound AI disclosure; publishing off needs an active owner
            attestation. Unset is on
    """

    inbound_ai: DisclosureSpecInboundAi | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        inbound_ai: str | Unset = UNSET
        if not isinstance(self.inbound_ai, Unset):
            inbound_ai = self.inbound_ai

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if inbound_ai is not UNSET:
            field_dict["inbound_ai"] = inbound_ai

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _inbound_ai = d.pop("inbound_ai", UNSET)
        inbound_ai: DisclosureSpecInboundAi | Unset
        if isinstance(_inbound_ai, Unset):
            inbound_ai = UNSET
        else:
            inbound_ai = check_disclosure_spec_inbound_ai(_inbound_ai)

        disclosure_spec = cls(
            inbound_ai=inbound_ai,
        )

        return disclosure_spec
