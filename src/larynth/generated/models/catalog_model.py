from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.catalog_model_kind import CatalogModelKind, check_catalog_model_kind
from ..models.catalog_model_status import CatalogModelStatus, check_catalog_model_status

if TYPE_CHECKING:
    from ..models.catalog_model_defaults import CatalogModelDefaults
    from ..models.catalog_model_params_schema import CatalogModelParamsSchema


T = TypeVar("T", bound="CatalogModel")


@_attrs_define
class CatalogModel:
    """
    Attributes:
        defaults (CatalogModelDefaults):
        display_name (str):
        id (UUID):
        is_default (bool):
        is_default_fallback (bool):
        kind (CatalogModelKind):
        languages (list[str]):
        model_key (str):
        params_schema (CatalogModelParamsSchema):
        provider_key (str):
        provider_name (str):
        status (CatalogModelStatus):
        wire_rates (list[int]):
    """

    defaults: CatalogModelDefaults
    display_name: str
    id: UUID
    is_default: bool
    is_default_fallback: bool
    kind: CatalogModelKind
    languages: list[str]
    model_key: str
    params_schema: CatalogModelParamsSchema
    provider_key: str
    provider_name: str
    status: CatalogModelStatus
    wire_rates: list[int]

    def to_dict(self) -> dict[str, Any]:
        defaults = self.defaults.to_dict()

        display_name = self.display_name

        id = str(self.id)

        is_default = self.is_default

        is_default_fallback = self.is_default_fallback

        kind: str = self.kind

        languages = self.languages

        model_key = self.model_key

        params_schema = self.params_schema.to_dict()

        provider_key = self.provider_key

        provider_name = self.provider_name

        status: str = self.status

        wire_rates = self.wire_rates

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "defaults": defaults,
                "display_name": display_name,
                "id": id,
                "is_default": is_default,
                "is_default_fallback": is_default_fallback,
                "kind": kind,
                "languages": languages,
                "model_key": model_key,
                "params_schema": params_schema,
                "provider_key": provider_key,
                "provider_name": provider_name,
                "status": status,
                "wire_rates": wire_rates,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.catalog_model_defaults import CatalogModelDefaults
        from ..models.catalog_model_params_schema import CatalogModelParamsSchema

        d = dict(src_dict)
        defaults = CatalogModelDefaults.from_dict(d.pop("defaults"))

        display_name = d.pop("display_name")

        id = UUID(d.pop("id"))

        is_default = d.pop("is_default")

        is_default_fallback = d.pop("is_default_fallback")

        kind = check_catalog_model_kind(d.pop("kind"))

        languages = cast(list[str], d.pop("languages"))

        model_key = d.pop("model_key")

        params_schema = CatalogModelParamsSchema.from_dict(d.pop("params_schema"))

        provider_key = d.pop("provider_key")

        provider_name = d.pop("provider_name")

        status = check_catalog_model_status(d.pop("status"))

        wire_rates = cast(list[int], d.pop("wire_rates"))

        catalog_model = cls(
            defaults=defaults,
            display_name=display_name,
            id=id,
            is_default=is_default,
            is_default_fallback=is_default_fallback,
            kind=kind,
            languages=languages,
            model_key=model_key,
            params_schema=params_schema,
            provider_key=provider_key,
            provider_name=provider_name,
            status=status,
            wire_rates=wire_rates,
        )

        return catalog_model
