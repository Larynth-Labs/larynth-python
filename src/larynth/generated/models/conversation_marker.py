from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.conversation_marker_kind import (
    ConversationMarkerKind,
    check_conversation_marker_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConversationMarker")


@_attrs_define
class ConversationMarker:
    """
    Attributes:
        kind (ConversationMarkerKind):
        digits_masked (str | Unset): Keypad digits are always masked
    """

    kind: ConversationMarkerKind
    digits_masked: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        digits_masked = self.digits_masked

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )
        if digits_masked is not UNSET:
            field_dict["digits_masked"] = digits_masked

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_conversation_marker_kind(d.pop("kind"))

        digits_masked = d.pop("digits_masked", UNSET)

        conversation_marker = cls(
            kind=kind,
            digits_masked=digits_masked,
        )

        return conversation_marker
