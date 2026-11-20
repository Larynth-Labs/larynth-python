from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.price_estimate_currency import (
    PriceEstimateCurrency,
    check_price_estimate_currency,
)

if TYPE_CHECKING:
    from ..models.latency_part import LatencyPart
    from ..models.price_part import PricePart


T = TypeVar("T", bound="PriceEstimate")


@_attrs_define
class PriceEstimate:
    """
    Attributes:
        currency (PriceEstimateCurrency):
        latency_ms (int | None): STT + LLM + TTS typical latency plus overhead_ms; null when a part has no number
        latency_parts (list[LatencyPart]):
        overhead_ms (int): Platform time added to the model latencies (setting builder.latency_overhead_ms)
        parts (list[PricePart]):
        total_micro_per_min (int): The customer price per started minute billing charges for this selection: base plus
            every premium
    """

    currency: PriceEstimateCurrency
    latency_ms: int | None
    latency_parts: list[LatencyPart]
    overhead_ms: int
    parts: list[PricePart]
    total_micro_per_min: int

    def to_dict(self) -> dict[str, Any]:
        currency: str = self.currency

        latency_ms: int | None
        latency_ms = self.latency_ms

        latency_parts = []
        for latency_parts_item_data in self.latency_parts:
            latency_parts_item = latency_parts_item_data.to_dict()
            latency_parts.append(latency_parts_item)

        overhead_ms = self.overhead_ms

        parts = []
        for parts_item_data in self.parts:
            parts_item = parts_item_data.to_dict()
            parts.append(parts_item)

        total_micro_per_min = self.total_micro_per_min

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currency": currency,
                "latency_ms": latency_ms,
                "latency_parts": latency_parts,
                "overhead_ms": overhead_ms,
                "parts": parts,
                "total_micro_per_min": total_micro_per_min,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.latency_part import LatencyPart
        from ..models.price_part import PricePart

        d = dict(src_dict)
        currency = check_price_estimate_currency(d.pop("currency"))

        def _parse_latency_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        latency_ms = _parse_latency_ms(d.pop("latency_ms"))

        latency_parts = []
        _latency_parts = d.pop("latency_parts")
        for latency_parts_item_data in _latency_parts:
            latency_parts_item = LatencyPart.from_dict(latency_parts_item_data)

            latency_parts.append(latency_parts_item)

        overhead_ms = d.pop("overhead_ms")

        parts = []
        _parts = d.pop("parts")
        for parts_item_data in _parts:
            parts_item = PricePart.from_dict(parts_item_data)

            parts.append(parts_item)

        total_micro_per_min = d.pop("total_micro_per_min")

        price_estimate = cls(
            currency=currency,
            latency_ms=latency_ms,
            latency_parts=latency_parts,
            overhead_ms=overhead_ms,
            parts=parts,
            total_micro_per_min=total_micro_per_min,
        )

        return price_estimate
