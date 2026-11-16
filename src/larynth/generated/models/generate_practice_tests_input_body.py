from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeneratePracticeTestsInputBody")


@_attrs_define
class GeneratePracticeTestsInputBody:
    """
    Attributes:
        template_key (str | Unset): Unset uses the template the agent was set up from, or the general set
    """

    template_key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        template_key = self.template_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if template_key is not UNSET:
            field_dict["template_key"] = template_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        template_key = d.pop("template_key", UNSET)

        generate_practice_tests_input_body = cls(
            template_key=template_key,
        )

        return generate_practice_tests_input_body
