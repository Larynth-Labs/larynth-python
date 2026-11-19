from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.price_part_kind import PricePartKind, check_price_part_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="PricePart")


@_attrs_define
class PricePart:
    """
    Attributes:
        kind (PricePartKind): base is the call-minute rate after any launch price; the others are premiums
        micro_per_min (int):
        model_id (UUID | Unset):
        voice_id (UUID | Unset):
    """

    kind: PricePartKind
    micro_per_min: int
    model_id: UUID | Unset = UNSET
    voice_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        micro_per_min = self.micro_per_min

        model_id: str | Unset = UNSET
        if not isinstance(self.model_id, Unset):
            model_id = str(self.model_id)

        voice_id: str | Unset = UNSET
        if not isinstance(self.voice_id, Unset):
            voice_id = str(self.voice_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "micro_per_min": micro_per_min,
            }
        )
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if voice_id is not UNSET:
            field_dict["voice_id"] = voice_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_price_part_kind(d.pop("kind"))

        micro_per_min = d.pop("micro_per_min")

        _model_id = d.pop("model_id", UNSET)
        model_id: UUID | Unset
        if isinstance(_model_id, Unset):
            model_id = UNSET
        else:
            model_id = UUID(_model_id)

        _voice_id = d.pop("voice_id", UNSET)
        voice_id: UUID | Unset
        if isinstance(_voice_id, Unset):
            voice_id = UNSET
        else:
            voice_id = UUID(_voice_id)

        price_part = cls(
            kind=kind,
            micro_per_min=micro_per_min,
            model_id=model_id,
            voice_id=voice_id,
        )

        return price_part
