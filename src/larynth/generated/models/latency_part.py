from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.latency_part_basis import LatencyPartBasis, check_latency_part_basis
from ..models.latency_part_kind import LatencyPartKind, check_latency_part_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="LatencyPart")


@_attrs_define
class LatencyPart:
    """
    Attributes:
        kind (LatencyPartKind):
        ms (int | None): typical_latency_ms of the model; null when no number exists
        basis (LatencyPartBasis | Unset):
    """

    kind: LatencyPartKind
    ms: int | None
    basis: LatencyPartBasis | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        ms: int | None
        ms = self.ms

        basis: str | Unset = UNSET
        if not isinstance(self.basis, Unset):
            basis = self.basis

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "ms": ms,
            }
        )
        if basis is not UNSET:
            field_dict["basis"] = basis

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_latency_part_kind(d.pop("kind"))

        def _parse_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ms = _parse_ms(d.pop("ms"))

        _basis = d.pop("basis", UNSET)
        basis: LatencyPartBasis | Unset
        if isinstance(_basis, Unset):
            basis = UNSET
        else:
            basis = check_latency_part_basis(_basis)

        latency_part = cls(
            kind=kind,
            ms=ms,
            basis=basis,
        )

        return latency_part
