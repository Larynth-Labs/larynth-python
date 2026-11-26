from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.live_model_currency import LiveModelCurrency, check_live_model_currency
from ..types import UNSET, Unset

T = TypeVar("T", bound="LiveModel")


@_attrs_define
class LiveModel:
    """
    Attributes:
        audio_formats (list[str]): Values s2s_params.audio_format accepts; g711_ulaw means the provider takes phone
            audio as is
        base_micro_per_min (int): The call-minute rate for live mode, after any launch price
        currency (LiveModelCurrency):
        display_name (str):
        id (UUID):
        languages (list[str]): Empty means the model detects the language itself
        model_key (str):
        premium_micro_per_min (int): Added to the call-minute rate for this model; 0 when it bills at the normal rate
        provider_key (str): Stable provider key, for the provider logo
        provider_name (str):
        total_micro_per_min (int): Price per started minute billing charges for this model
        default_audio_format (str | Unset):
        default_voice (str | Unset): Voice key used when s2s_params.voice is unset; GET /v1/catalog/voices?model_id=
            lists the others
        retires_on (datetime.date | Unset):
    """

    audio_formats: list[str]
    base_micro_per_min: int
    currency: LiveModelCurrency
    display_name: str
    id: UUID
    languages: list[str]
    model_key: str
    premium_micro_per_min: int
    provider_key: str
    provider_name: str
    total_micro_per_min: int
    default_audio_format: str | Unset = UNSET
    default_voice: str | Unset = UNSET
    retires_on: datetime.date | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        audio_formats = self.audio_formats

        base_micro_per_min = self.base_micro_per_min

        currency: str = self.currency

        display_name = self.display_name

        id = str(self.id)

        languages = self.languages

        model_key = self.model_key

        premium_micro_per_min = self.premium_micro_per_min

        provider_key = self.provider_key

        provider_name = self.provider_name

        total_micro_per_min = self.total_micro_per_min

        default_audio_format = self.default_audio_format

        default_voice = self.default_voice

        retires_on: str | Unset = UNSET
        if not isinstance(self.retires_on, Unset):
            retires_on = self.retires_on.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "audio_formats": audio_formats,
                "base_micro_per_min": base_micro_per_min,
                "currency": currency,
                "display_name": display_name,
                "id": id,
                "languages": languages,
                "model_key": model_key,
                "premium_micro_per_min": premium_micro_per_min,
                "provider_key": provider_key,
                "provider_name": provider_name,
                "total_micro_per_min": total_micro_per_min,
            }
        )
        if default_audio_format is not UNSET:
            field_dict["default_audio_format"] = default_audio_format
        if default_voice is not UNSET:
            field_dict["default_voice"] = default_voice
        if retires_on is not UNSET:
            field_dict["retires_on"] = retires_on

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        audio_formats = cast(list[str], d.pop("audio_formats"))

        base_micro_per_min = d.pop("base_micro_per_min")

        currency = check_live_model_currency(d.pop("currency"))

        display_name = d.pop("display_name")

        id = UUID(d.pop("id"))

        languages = cast(list[str], d.pop("languages"))

        model_key = d.pop("model_key")

        premium_micro_per_min = d.pop("premium_micro_per_min")

        provider_key = d.pop("provider_key")

        provider_name = d.pop("provider_name")

        total_micro_per_min = d.pop("total_micro_per_min")

        default_audio_format = d.pop("default_audio_format", UNSET)

        default_voice = d.pop("default_voice", UNSET)

        _retires_on = d.pop("retires_on", UNSET)
        retires_on: datetime.date | Unset
        if isinstance(_retires_on, Unset):
            retires_on = UNSET
        else:
            retires_on = datetime.date.fromisoformat(_retires_on)

        live_model = cls(
            audio_formats=audio_formats,
            base_micro_per_min=base_micro_per_min,
            currency=currency,
            display_name=display_name,
            id=id,
            languages=languages,
            model_key=model_key,
            premium_micro_per_min=premium_micro_per_min,
            provider_key=provider_key,
            provider_name=provider_name,
            total_micro_per_min=total_micro_per_min,
            default_audio_format=default_audio_format,
            default_voice=default_voice,
            retires_on=retires_on,
        )

        return live_model
