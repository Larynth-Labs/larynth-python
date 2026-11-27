from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.catalog_voice_latency_basis import (
    CatalogVoiceLatencyBasis,
    check_catalog_voice_latency_basis,
)
from ..models.catalog_voice_quality_basis import (
    CatalogVoiceQualityBasis,
    check_catalog_voice_quality_basis,
)
from ..models.catalog_voice_status import CatalogVoiceStatus, check_catalog_voice_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_voice_attributes import CatalogVoiceAttributes


T = TypeVar("T", bound="CatalogVoice")


@_attrs_define
class CatalogVoice:
    """
    Attributes:
        attributes (CatalogVoiceAttributes): Provider facts such as gender (male, female, neutral) and accent when known
        language (str):
        languages (list[str]): Languages the voice speaks well; the first is its main language
        name (str):
        premium_micro_per_min (int): Added to the call-minute rate; 0 when no premium rate row exists. Equals what
            billing charges
        provider_key (str):
        status (CatalogVoiceStatus):
        tags (list[str]):
        voice_key (str):
        description (str | Unset): Plain description written by Larynth
        id (UUID | Unset): Unset when the voice was fetched live from the provider and is not in the catalog
        latency_basis (CatalogVoiceLatencyBasis | Unset): Inherited from the TTS model. live: our own calls of the last
            7 days, written nightly once 50 turns exist. Turns are attributed per call to the single model of each kind the
            call used; calls that switched models mid-call (fallback) are excluded. lab: our direct probe from a US host,
            used until live data exists. Unset when no measurement exists
        model_id (UUID | Unset):
        preview_url (str | Unset):
        quality_basis (CatalogVoiceQualityBasis | Unset): Inherited from the TTS model. wer: 100 minus word error rate
            x10 on our benchmark corpus; eval: live-call eval pass rate; humanness: listening benchmark
        quality_score (int | Unset): Inherited from the TTS model. 0 to 100, from our own measurement named by
            quality_basis; unset until measured
        typical_latency_ms (int | Unset): Inherited from the TTS model given in model_id: text to first audio
    """

    attributes: CatalogVoiceAttributes
    language: str
    languages: list[str]
    name: str
    premium_micro_per_min: int
    provider_key: str
    status: CatalogVoiceStatus
    tags: list[str]
    voice_key: str
    description: str | Unset = UNSET
    id: UUID | Unset = UNSET
    latency_basis: CatalogVoiceLatencyBasis | Unset = UNSET
    model_id: UUID | Unset = UNSET
    preview_url: str | Unset = UNSET
    quality_basis: CatalogVoiceQualityBasis | Unset = UNSET
    quality_score: int | Unset = UNSET
    typical_latency_ms: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes.to_dict()

        language = self.language

        languages = self.languages

        name = self.name

        premium_micro_per_min = self.premium_micro_per_min

        provider_key = self.provider_key

        status: str = self.status

        tags = self.tags

        voice_key = self.voice_key

        description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        latency_basis: str | Unset = UNSET
        if not isinstance(self.latency_basis, Unset):
            latency_basis = self.latency_basis

        model_id: str | Unset = UNSET
        if not isinstance(self.model_id, Unset):
            model_id = str(self.model_id)

        preview_url = self.preview_url

        quality_basis: str | Unset = UNSET
        if not isinstance(self.quality_basis, Unset):
            quality_basis = self.quality_basis

        quality_score = self.quality_score

        typical_latency_ms = self.typical_latency_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attributes": attributes,
                "language": language,
                "languages": languages,
                "name": name,
                "premium_micro_per_min": premium_micro_per_min,
                "provider_key": provider_key,
                "status": status,
                "tags": tags,
                "voice_key": voice_key,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if latency_basis is not UNSET:
            field_dict["latency_basis"] = latency_basis
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if preview_url is not UNSET:
            field_dict["preview_url"] = preview_url
        if quality_basis is not UNSET:
            field_dict["quality_basis"] = quality_basis
        if quality_score is not UNSET:
            field_dict["quality_score"] = quality_score
        if typical_latency_ms is not UNSET:
            field_dict["typical_latency_ms"] = typical_latency_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_voice_attributes import CatalogVoiceAttributes

        d = dict(src_dict)
        attributes = CatalogVoiceAttributes.from_dict(d.pop("attributes"))

        language = d.pop("language")

        languages = cast(list[str], d.pop("languages"))

        name = d.pop("name")

        premium_micro_per_min = d.pop("premium_micro_per_min")

        provider_key = d.pop("provider_key")

        status = check_catalog_voice_status(d.pop("status"))

        tags = cast(list[str], d.pop("tags"))

        voice_key = d.pop("voice_key")

        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _latency_basis = d.pop("latency_basis", UNSET)
        latency_basis: CatalogVoiceLatencyBasis | Unset
        if isinstance(_latency_basis, Unset):
            latency_basis = UNSET
        else:
            latency_basis = check_catalog_voice_latency_basis(_latency_basis)

        _model_id = d.pop("model_id", UNSET)
        model_id: UUID | Unset
        if isinstance(_model_id, Unset):
            model_id = UNSET
        else:
            model_id = UUID(_model_id)

        preview_url = d.pop("preview_url", UNSET)

        _quality_basis = d.pop("quality_basis", UNSET)
        quality_basis: CatalogVoiceQualityBasis | Unset
        if isinstance(_quality_basis, Unset):
            quality_basis = UNSET
        else:
            quality_basis = check_catalog_voice_quality_basis(_quality_basis)

        quality_score = d.pop("quality_score", UNSET)

        typical_latency_ms = d.pop("typical_latency_ms", UNSET)

        catalog_voice = cls(
            attributes=attributes,
            language=language,
            languages=languages,
            name=name,
            premium_micro_per_min=premium_micro_per_min,
            provider_key=provider_key,
            status=status,
            tags=tags,
            voice_key=voice_key,
            description=description,
            id=id,
            latency_basis=latency_basis,
            model_id=model_id,
            preview_url=preview_url,
            quality_basis=quality_basis,
            quality_score=quality_score,
            typical_latency_ms=typical_latency_ms,
        )

        return catalog_voice
