from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.update_practice_test_input_body_traits_item import (
    UpdatePracticeTestInputBodyTraitsItem,
    check_update_practice_test_input_body_traits_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.practice_check import PracticeCheck


T = TypeVar("T", bound="UpdatePracticeTestInputBody")


@_attrs_define
class UpdatePracticeTestInputBody:
    """
    Attributes:
        caller_e164 (str | Unset): A test number in E.164; an empty string clears it
        must (list[PracticeCheck] | Unset):
        name (str | Unset):
        required (bool | Unset):
        traits (list[UpdatePracticeTestInputBodyTraitsItem] | Unset): Replaces the traits; an empty list clears them
        wants (str | Unset):
        who (str | Unset):
    """

    caller_e164: str | Unset = UNSET
    must: list[PracticeCheck] | Unset = UNSET
    name: str | Unset = UNSET
    required: bool | Unset = UNSET
    traits: list[UpdatePracticeTestInputBodyTraitsItem] | Unset = UNSET
    wants: str | Unset = UNSET
    who: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        caller_e164 = self.caller_e164

        must: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.must, Unset):
            must = []
            for must_item_data in self.must:
                must_item = must_item_data.to_dict()
                must.append(must_item)

        name = self.name

        required = self.required

        traits: list[str] | Unset = UNSET
        if not isinstance(self.traits, Unset):
            traits = []
            for traits_item_data in self.traits:
                traits_item: str = traits_item_data
                traits.append(traits_item)

        wants = self.wants

        who = self.who

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if caller_e164 is not UNSET:
            field_dict["caller_e164"] = caller_e164
        if must is not UNSET:
            field_dict["must"] = must
        if name is not UNSET:
            field_dict["name"] = name
        if required is not UNSET:
            field_dict["required"] = required
        if traits is not UNSET:
            field_dict["traits"] = traits
        if wants is not UNSET:
            field_dict["wants"] = wants
        if who is not UNSET:
            field_dict["who"] = who

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.practice_check import PracticeCheck

        d = dict(src_dict)
        caller_e164 = d.pop("caller_e164", UNSET)

        _must = d.pop("must", UNSET)
        must: list[PracticeCheck] | Unset = UNSET
        if _must is not UNSET:
            must = []
            for must_item_data in _must:
                must_item = PracticeCheck.from_dict(must_item_data)

                must.append(must_item)

        name = d.pop("name", UNSET)

        required = d.pop("required", UNSET)

        _traits = d.pop("traits", UNSET)
        traits: list[UpdatePracticeTestInputBodyTraitsItem] | Unset = UNSET
        if _traits is not UNSET:
            traits = []
            for traits_item_data in _traits:
                traits_item = check_update_practice_test_input_body_traits_item(
                    traits_item_data
                )

                traits.append(traits_item)

        wants = d.pop("wants", UNSET)

        who = d.pop("who", UNSET)

        update_practice_test_input_body = cls(
            caller_e164=caller_e164,
            must=must,
            name=name,
            required=required,
            traits=traits,
            wants=wants,
            who=who,
        )

        return update_practice_test_input_body
