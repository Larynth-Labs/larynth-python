from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.provider_fallback_kind import (
    ProviderFallbackKind,
    check_provider_fallback_kind,
)

T = TypeVar("T", bound="ProviderFallback")


@_attrs_define
class ProviderFallback:
    """
    Attributes:
        at_ms (int): Offset from the start of the call
        from_ (str): Display name of the provider the call left
        from_key (str): Catalog key of that provider
        kind (ProviderFallbackKind):
        reason (str): Error class that caused the switch, such as timeout, stall, unavailable, rate_limited or quota
        to (str): Display name of the backup provider
        to_key (str): Catalog key of the backup provider
    """

    at_ms: int
    from_: str
    from_key: str
    kind: ProviderFallbackKind
    reason: str
    to: str
    to_key: str

    def to_dict(self) -> dict[str, Any]:
        at_ms = self.at_ms

        from_ = self.from_

        from_key = self.from_key

        kind: str = self.kind

        reason = self.reason

        to = self.to

        to_key = self.to_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at_ms": at_ms,
                "from": from_,
                "from_key": from_key,
                "kind": kind,
                "reason": reason,
                "to": to,
                "to_key": to_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at_ms = d.pop("at_ms")

        from_ = d.pop("from")

        from_key = d.pop("from_key")

        kind = check_provider_fallback_kind(d.pop("kind"))

        reason = d.pop("reason")

        to = d.pop("to")

        to_key = d.pop("to_key")

        provider_fallback = cls(
            at_ms=at_ms,
            from_=from_,
            from_key=from_key,
            kind=kind,
            reason=reason,
            to=to,
            to_key=to_key,
        )

        return provider_fallback
