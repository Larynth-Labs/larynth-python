from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.practice_test_body_traits_item import (
    PracticeTestBodyTraitsItem,
    check_practice_test_body_traits_item,
)
from ..types import UNSET, Unset

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
        caller_e164 (str | Unset): The number the agent sees as the caller, in E.164. Only test numbers are allowed: +1,
            an optional area code, then 555 01 and two digits
        required (bool | Unset): Must pass before the agent can be published from the dashboard
        source_call_id (str | Unset): The call this practice call was drafted from; sets source to from_call
        traits (list[PracticeTestBodyTraitsItem] | Unset): How the caller behaves, at most 3
    """

    must: list[PracticeCheck]
    name: str
    wants: str
    who: str
    caller_e164: str | Unset = UNSET
    required: bool | Unset = UNSET
    source_call_id: str | Unset = UNSET
    traits: list[PracticeTestBodyTraitsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        must = []
        for must_item_data in self.must:
            must_item = must_item_data.to_dict()
            must.append(must_item)

        name = self.name

        wants = self.wants

        who = self.who

        caller_e164 = self.caller_e164

        required = self.required

        source_call_id = self.source_call_id

        traits: list[str] | Unset = UNSET
        if not isinstance(self.traits, Unset):
            traits = []
            for traits_item_data in self.traits:
                traits_item: str = traits_item_data
                traits.append(traits_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "must": must,
                "name": name,
                "wants": wants,
                "who": who,
            }
        )
        if caller_e164 is not UNSET:
            field_dict["caller_e164"] = caller_e164
        if required is not UNSET:
            field_dict["required"] = required
        if source_call_id is not UNSET:
            field_dict["source_call_id"] = source_call_id
        if traits is not UNSET:
            field_dict["traits"] = traits

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

        caller_e164 = d.pop("caller_e164", UNSET)

        required = d.pop("required", UNSET)

        source_call_id = d.pop("source_call_id", UNSET)

        _traits = d.pop("traits", UNSET)
        traits: list[PracticeTestBodyTraitsItem] | Unset = UNSET
        if _traits is not UNSET:
            traits = []
            for traits_item_data in _traits:
                traits_item = check_practice_test_body_traits_item(traits_item_data)

                traits.append(traits_item)

        practice_test_body = cls(
            must=must,
            name=name,
            wants=wants,
            who=who,
            caller_e164=caller_e164,
            required=required,
            source_call_id=source_call_id,
            traits=traits,
        )

        return practice_test_body
