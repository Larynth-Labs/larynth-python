from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.catalog_model_kind import CatalogModelKind, check_catalog_model_kind
from ..models.catalog_model_status import CatalogModelStatus, check_catalog_model_status
from ..models.catalog_model_tier import CatalogModelTier, check_catalog_model_tier
from ..types import UNSET, Unset

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
        premium_micro_per_min (int): Added to the call-minute rate; 0 when no premium rate row exists. Equals what
            billing charges
        provider_key (str):
        provider_name (str):
        recommended (bool): The recommended model of its tier
        status (CatalogModelStatus):
        usable_in_flows (bool): A flow step may pick this model (cascade LLMs only, at most 3 per flow)
        wire_rates (list[int]):
        description (str | Unset): Plain description written by Larynth
        tier (CatalogModelTier | Unset): Quality tier the editor shows by default; unset for models listed only under
            Advanced
        typical_reply_ms (int | Unset): Typical time this model adds to a reply, measured on our cells
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
    premium_micro_per_min: int
    provider_key: str
    provider_name: str
    recommended: bool
    status: CatalogModelStatus
    usable_in_flows: bool
    wire_rates: list[int]
    description: str | Unset = UNSET
    tier: CatalogModelTier | Unset = UNSET
    typical_reply_ms: int | Unset = UNSET

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

        premium_micro_per_min = self.premium_micro_per_min

        provider_key = self.provider_key

        provider_name = self.provider_name

        recommended = self.recommended

        status: str = self.status

        usable_in_flows = self.usable_in_flows

        wire_rates = self.wire_rates

        description = self.description

        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier

        typical_reply_ms = self.typical_reply_ms

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
                "premium_micro_per_min": premium_micro_per_min,
                "provider_key": provider_key,
                "provider_name": provider_name,
                "recommended": recommended,
                "status": status,
                "usable_in_flows": usable_in_flows,
                "wire_rates": wire_rates,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if tier is not UNSET:
            field_dict["tier"] = tier
        if typical_reply_ms is not UNSET:
            field_dict["typical_reply_ms"] = typical_reply_ms

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

        premium_micro_per_min = d.pop("premium_micro_per_min")

        provider_key = d.pop("provider_key")

        provider_name = d.pop("provider_name")

        recommended = d.pop("recommended")

        status = check_catalog_model_status(d.pop("status"))

        usable_in_flows = d.pop("usable_in_flows")

        wire_rates = cast(list[int], d.pop("wire_rates"))

        description = d.pop("description", UNSET)

        _tier = d.pop("tier", UNSET)
        tier: CatalogModelTier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = check_catalog_model_tier(_tier)

        typical_reply_ms = d.pop("typical_reply_ms", UNSET)

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
            premium_micro_per_min=premium_micro_per_min,
            provider_key=provider_key,
            provider_name=provider_name,
            recommended=recommended,
            status=status,
            usable_in_flows=usable_in_flows,
            wire_rates=wire_rates,
            description=description,
            tier=tier,
            typical_reply_ms=typical_reply_ms,
        )

        return catalog_model
