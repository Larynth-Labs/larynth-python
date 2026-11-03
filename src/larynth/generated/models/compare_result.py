from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.compare_price import ComparePrice
    from ..models.compare_section import CompareSection
    from ..models.instructions_diff import InstructionsDiff
    from ..models.number_ref import NumberRef
    from ..models.simulations_summary import SimulationsSummary


T = TypeVar("T", bound="CompareResult")


@_attrs_define
class CompareResult:
    """
    Attributes:
        from_version (int):
        instructions_diff (InstructionsDiff):
        numbers_affected (list[NumberRef]):
        price (ComparePrice):
        sections (list[CompareSection]):
        simulations (SimulationsSummary):
        to_version (int):
    """

    from_version: int
    instructions_diff: InstructionsDiff
    numbers_affected: list[NumberRef]
    price: ComparePrice
    sections: list[CompareSection]
    simulations: SimulationsSummary
    to_version: int

    def to_dict(self) -> dict[str, Any]:
        from_version = self.from_version

        instructions_diff = self.instructions_diff.to_dict()

        numbers_affected = []
        for numbers_affected_item_data in self.numbers_affected:
            numbers_affected_item = numbers_affected_item_data.to_dict()
            numbers_affected.append(numbers_affected_item)

        price = self.price.to_dict()

        sections = []
        for sections_item_data in self.sections:
            sections_item = sections_item_data.to_dict()
            sections.append(sections_item)

        simulations = self.simulations.to_dict()

        to_version = self.to_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "from_version": from_version,
                "instructions_diff": instructions_diff,
                "numbers_affected": numbers_affected,
                "price": price,
                "sections": sections,
                "simulations": simulations,
                "to_version": to_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.compare_price import ComparePrice
        from ..models.compare_section import CompareSection
        from ..models.instructions_diff import InstructionsDiff
        from ..models.number_ref import NumberRef
        from ..models.simulations_summary import SimulationsSummary

        d = dict(src_dict)
        from_version = d.pop("from_version")

        instructions_diff = InstructionsDiff.from_dict(d.pop("instructions_diff"))

        numbers_affected = []
        _numbers_affected = d.pop("numbers_affected")
        for numbers_affected_item_data in _numbers_affected:
            numbers_affected_item = NumberRef.from_dict(numbers_affected_item_data)

            numbers_affected.append(numbers_affected_item)

        price = ComparePrice.from_dict(d.pop("price"))

        sections = []
        _sections = d.pop("sections")
        for sections_item_data in _sections:
            sections_item = CompareSection.from_dict(sections_item_data)

            sections.append(sections_item)

        simulations = SimulationsSummary.from_dict(d.pop("simulations"))

        to_version = d.pop("to_version")

        compare_result = cls(
            from_version=from_version,
            instructions_diff=instructions_diff,
            numbers_affected=numbers_affected,
            price=price,
            sections=sections,
            simulations=simulations,
            to_version=to_version,
        )

        return compare_result
