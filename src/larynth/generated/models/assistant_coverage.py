from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.assistant_coverage_band import AssistantCoverageBand


T = TypeVar("T", bound="AssistantCoverage")


@_attrs_define
class AssistantCoverage:
    """
    Attributes:
        bands (list[AssistantCoverageBand]):
        summary_key (str): i18n key of the plain summary, for example around_the_clock
    """

    bands: list[AssistantCoverageBand]
    summary_key: str

    def to_dict(self) -> dict[str, Any]:
        bands = []
        for bands_item_data in self.bands:
            bands_item = bands_item_data.to_dict()
            bands.append(bands_item)

        summary_key = self.summary_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bands": bands,
                "summary_key": summary_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assistant_coverage_band import AssistantCoverageBand

        d = dict(src_dict)
        bands = []
        _bands = d.pop("bands")
        for bands_item_data in _bands:
            bands_item = AssistantCoverageBand.from_dict(bands_item_data)

            bands.append(bands_item)

        summary_key = d.pop("summary_key")

        assistant_coverage = cls(
            bands=bands,
            summary_key=summary_key,
        )

        return assistant_coverage
