from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.catalog_voice_status import CatalogVoiceStatus, check_catalog_voice_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_voice_attributes import CatalogVoiceAttributes


T = TypeVar("T", bound="CatalogVoice")


@_attrs_define
class CatalogVoice:
    """
    Attributes:
        attributes (CatalogVoiceAttributes):
        id (UUID):
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
        model_id (UUID | Unset):
        preview_url (str | Unset):
    """

    attributes: CatalogVoiceAttributes
    id: UUID
    language: str
    languages: list[str]
    name: str
    premium_micro_per_min: int
    provider_key: str
    status: CatalogVoiceStatus
    tags: list[str]
    voice_key: str
    description: str | Unset = UNSET
    model_id: UUID | Unset = UNSET
    preview_url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attributes = self.attributes.to_dict()

        id = str(self.id)

        language = self.language

        languages = self.languages

        name = self.name

        premium_micro_per_min = self.premium_micro_per_min

        provider_key = self.provider_key

        status: str = self.status

        tags = self.tags

        voice_key = self.voice_key

        description = self.description

        model_id: str | Unset = UNSET
        if not isinstance(self.model_id, Unset):
            model_id = str(self.model_id)

        preview_url = self.preview_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attributes": attributes,
                "id": id,
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
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if preview_url is not UNSET:
            field_dict["preview_url"] = preview_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_voice_attributes import CatalogVoiceAttributes

        d = dict(src_dict)
        attributes = CatalogVoiceAttributes.from_dict(d.pop("attributes"))

        id = UUID(d.pop("id"))

        language = d.pop("language")

        languages = cast(list[str], d.pop("languages"))

        name = d.pop("name")

        premium_micro_per_min = d.pop("premium_micro_per_min")

        provider_key = d.pop("provider_key")

        status = check_catalog_voice_status(d.pop("status"))

        tags = cast(list[str], d.pop("tags"))

        voice_key = d.pop("voice_key")

        description = d.pop("description", UNSET)

        _model_id = d.pop("model_id", UNSET)
        model_id: UUID | Unset
        if isinstance(_model_id, Unset):
            model_id = UNSET
        else:
            model_id = UUID(_model_id)

        preview_url = d.pop("preview_url", UNSET)

        catalog_voice = cls(
            attributes=attributes,
            id=id,
            language=language,
            languages=languages,
            name=name,
            premium_micro_per_min=premium_micro_per_min,
            provider_key=provider_key,
            status=status,
            tags=tags,
            voice_key=voice_key,
            description=description,
            model_id=model_id,
            preview_url=preview_url,
        )

        return catalog_voice
