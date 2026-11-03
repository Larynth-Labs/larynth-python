from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.timeline_consent_kind import (
    TimelineConsentKind,
    check_timeline_consent_kind,
)

T = TypeVar("T", bound="TimelineConsent")


@_attrs_define
class TimelineConsent:
    """
    Attributes:
        covers (list[str]):
        id (UUID):
        kind (TimelineConsentKind):
    """

    covers: list[str]
    id: UUID
    kind: TimelineConsentKind

    def to_dict(self) -> dict[str, Any]:
        covers = self.covers

        id = str(self.id)

        kind: str = self.kind

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "covers": covers,
                "id": id,
                "kind": kind,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        covers = cast(list[str], d.pop("covers"))

        id = UUID(d.pop("id"))

        kind = check_timeline_consent_kind(d.pop("kind"))

        timeline_consent = cls(
            covers=covers,
            id=id,
            kind=kind,
        )

        return timeline_consent
