from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.practice_check import PracticeCheck


T = TypeVar("T", bound="UpdatePracticeTestInputBody")


@_attrs_define
class UpdatePracticeTestInputBody:
    """
    Attributes:
        must (list[PracticeCheck] | Unset):
        name (str | Unset):
        wants (str | Unset):
        who (str | Unset):
    """

    must: list[PracticeCheck] | Unset = UNSET
    name: str | Unset = UNSET
    wants: str | Unset = UNSET
    who: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        must: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.must, Unset):
            must = []
            for must_item_data in self.must:
                must_item = must_item_data.to_dict()
                must.append(must_item)

        name = self.name

        wants = self.wants

        who = self.who

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if must is not UNSET:
            field_dict["must"] = must
        if name is not UNSET:
            field_dict["name"] = name
        if wants is not UNSET:
            field_dict["wants"] = wants
        if who is not UNSET:
            field_dict["who"] = who

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.practice_check import PracticeCheck

        d = dict(src_dict)
        _must = d.pop("must", UNSET)
        must: list[PracticeCheck] | Unset = UNSET
        if _must is not UNSET:
            must = []
            for must_item_data in _must:
                must_item = PracticeCheck.from_dict(must_item_data)

                must.append(must_item)

        name = d.pop("name", UNSET)

        wants = d.pop("wants", UNSET)

        who = d.pop("who", UNSET)

        update_practice_test_input_body = cls(
            must=must,
            name=name,
            wants=wants,
            who=who,
        )

        return update_practice_test_input_body
