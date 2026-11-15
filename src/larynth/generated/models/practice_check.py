from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.practice_check_type import PracticeCheckType, check_practice_check_type

T = TypeVar("T", bound="PracticeCheck")


@_attrs_define
class PracticeCheck:
    """
    Attributes:
        key (str): Stable id within the practice call
        label (str): What must happen, in the owner's words
        text (str): The phrase, the tool name or the statement
        type_ (PracticeCheckType): said and not_said look for a phrase in the agent's lines, tool_called and
            tool_not_called look at the tools it used, judge asks a model whether the statement holds
    """

    key: str
    label: str
    text: str
    type_: PracticeCheckType

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        text = self.text

        type_: str = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "label": label,
                "text": text,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        text = d.pop("text")

        type_ = check_practice_check_type(d.pop("type"))

        practice_check = cls(
            key=key,
            label=label,
            text=text,
            type_=type_,
        )

        return practice_check
