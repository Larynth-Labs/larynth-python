from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.practice_check import PracticeCheck


T = TypeVar("T", bound="PracticeTestBody")


@_attrs_define
class PracticeTestBody:
    """
    Attributes:
        must (list[PracticeCheck]):
        name (str):
        wants (str):
        who (str):
    """

    must: list[PracticeCheck]
    name: str
    wants: str
    who: str

    def to_dict(self) -> dict[str, Any]:
        must = []
        for must_item_data in self.must:
            must_item = must_item_data.to_dict()
            must.append(must_item)

        name = self.name

        wants = self.wants

        who = self.who

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "must": must,
                "name": name,
                "wants": wants,
                "who": who,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.practice_check import PracticeCheck

        d = dict(src_dict)
        must = []
        _must = d.pop("must")
        for must_item_data in _must:
            must_item = PracticeCheck.from_dict(must_item_data)

            must.append(must_item)

        name = d.pop("name")

        wants = d.pop("wants")

        who = d.pop("who")

        practice_test_body = cls(
            must=must,
            name=name,
            wants=wants,
            who=who,
        )

        return practice_test_body
