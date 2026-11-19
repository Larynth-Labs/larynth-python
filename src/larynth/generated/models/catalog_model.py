from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.catalog_model_kind import CatalogModelKind, check_catalog_model_kind
from ..models.catalog_model_latency_basis import (
    CatalogModelLatencyBasis,
    check_catalog_model_latency_basis,
)
from ..models.catalog_model_quality_basis import (
    CatalogModelQualityBasis,
    check_catalog_model_quality_basis,
)
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
        latency_basis (CatalogModelLatencyBasis | Unset): measured: the p50 of the last 7 days of our own calls, written
            nightly once 50 turns exist. Turns are attributed per call to the single model of each kind the call used; calls
            that switched models mid-call (fallback), test workspaces and web tests are excluded. seeded: our seeded value
            until then. Unset when no number exists
        quality_basis (CatalogModelQualityBasis | Unset): wer: 100 minus word error rate x10 on our benchmark corpus;
            eval: live-call eval pass rate; humanness: listening benchmark
        quality_score (int | Unset): 0 to 100, from our own measurement named by quality_basis; unset until measured
        tier (CatalogModelTier | Unset): Quality tier the editor shows by default; unset for models listed only under
            Advanced
        typical_latency_ms (int | Unset): Typical latency: STT is speech end to final transcript, LLM is time to first
            token, TTS is text to first audio
        typical_reply_ms (int | Unset): Deprecated alias of typical_latency_ms, kept for one release
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
    latency_basis: CatalogModelLatencyBasis | Unset = UNSET
    quality_basis: CatalogModelQualityBasis | Unset = UNSET
    quality_score: int | Unset = UNSET
    tier: CatalogModelTier | Unset = UNSET
    typical_latency_ms: int | Unset = UNSET
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

        latency_basis: str | Unset = UNSET
        if not isinstance(self.latency_basis, Unset):
            latency_basis = self.latency_basis

        quality_basis: str | Unset = UNSET
        if not isinstance(self.quality_basis, Unset):
            quality_basis = self.quality_basis

        quality_score = self.quality_score

        tier: str | Unset = UNSET
        if not isinstance(self.tier, Unset):
            tier = self.tier

        typical_latency_ms = self.typical_latency_ms

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
        if latency_basis is not UNSET:
            field_dict["latency_basis"] = latency_basis
        if quality_basis is not UNSET:
            field_dict["quality_basis"] = quality_basis
        if quality_score is not UNSET:
            field_dict["quality_score"] = quality_score
        if tier is not UNSET:
            field_dict["tier"] = tier
        if typical_latency_ms is not UNSET:
            field_dict["typical_latency_ms"] = typical_latency_ms
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

        _latency_basis = d.pop("latency_basis", UNSET)
        latency_basis: CatalogModelLatencyBasis | Unset
        if isinstance(_latency_basis, Unset):
            latency_basis = UNSET
        else:
            latency_basis = check_catalog_model_latency_basis(_latency_basis)

        _quality_basis = d.pop("quality_basis", UNSET)
        quality_basis: CatalogModelQualityBasis | Unset
        if isinstance(_quality_basis, Unset):
            quality_basis = UNSET
        else:
            quality_basis = check_catalog_model_quality_basis(_quality_basis)

        quality_score = d.pop("quality_score", UNSET)

        _tier = d.pop("tier", UNSET)
        tier: CatalogModelTier | Unset
        if isinstance(_tier, Unset):
            tier = UNSET
        else:
            tier = check_catalog_model_tier(_tier)

        typical_latency_ms = d.pop("typical_latency_ms", UNSET)

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
            latency_basis=latency_basis,
            quality_basis=quality_basis,
            quality_score=quality_score,
            tier=tier,
            typical_latency_ms=typical_latency_ms,
            typical_reply_ms=typical_reply_ms,
        )

        return catalog_model
