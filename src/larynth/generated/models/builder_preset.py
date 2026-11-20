from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.price_estimate import PriceEstimate


T = TypeVar("T", bound="BuilderPreset")


@_attrs_define
class BuilderPreset:
    """
    Attributes:
        description (str):
        display_name (str):
        estimate (PriceEstimate):
        key (str):
        llm_model_id (UUID):
        sort (int):
        stt_model_id (UUID):
        tts_model_id (UUID):
        voice_id (UUID | Unset):
    """

    description: str
    display_name: str
    estimate: PriceEstimate
    key: str
    llm_model_id: UUID
    sort: int
    stt_model_id: UUID
    tts_model_id: UUID
    voice_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        display_name = self.display_name

        estimate = self.estimate.to_dict()

        key = self.key

        llm_model_id = str(self.llm_model_id)

        sort = self.sort

        stt_model_id = str(self.stt_model_id)

        tts_model_id = str(self.tts_model_id)

        voice_id: str | Unset = UNSET
        if not isinstance(self.voice_id, Unset):
            voice_id = str(self.voice_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "display_name": display_name,
                "estimate": estimate,
                "key": key,
                "llm_model_id": llm_model_id,
                "sort": sort,
                "stt_model_id": stt_model_id,
                "tts_model_id": tts_model_id,
            }
        )
        if voice_id is not UNSET:
            field_dict["voice_id"] = voice_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.price_estimate import PriceEstimate

        d = dict(src_dict)
        description = d.pop("description")

        display_name = d.pop("display_name")

        estimate = PriceEstimate.from_dict(d.pop("estimate"))

        key = d.pop("key")

        llm_model_id = UUID(d.pop("llm_model_id"))

        sort = d.pop("sort")

        stt_model_id = UUID(d.pop("stt_model_id"))

        tts_model_id = UUID(d.pop("tts_model_id"))

        _voice_id = d.pop("voice_id", UNSET)
        voice_id: UUID | Unset
        if isinstance(_voice_id, Unset):
            voice_id = UNSET
        else:
            voice_id = UUID(_voice_id)

        builder_preset = cls(
            description=description,
            display_name=display_name,
            estimate=estimate,
            key=key,
            llm_model_id=llm_model_id,
            sort=sort,
            stt_model_id=stt_model_id,
            tts_model_id=tts_model_id,
            voice_id=voice_id,
        )

        return builder_preset
