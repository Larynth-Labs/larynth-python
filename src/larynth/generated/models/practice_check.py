from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.practice_check_type import PracticeCheckType, check_practice_check_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="PracticeCheck")


@_attrs_define
class PracticeCheck:
    """
    Attributes:
        key (str): Stable id within the practice call
        label (str): What must happen, in the owner's words
        text (str): The phrase, the tool name, the text that must not appear in the tool's arguments, or the statement
        type_ (PracticeCheckType): said and not_said look for a phrase in the agent's lines, tool_called and
            tool_not_called look at the tools it used, tool_args_not_contain passes when the arguments of the tool named in
            tool never contain the text, judge asks a model whether the statement holds and must quote the call as evidence,
            transferred passes when the agent transferred the call (text is unused; send -), outcome_is passes when the call
            ended with the outcome named in text (booked_appointment, rescheduled, answered_question, message_taken or
            no_resolution)
        tool (str | Unset): Only with tool_args_not_contain: the tool whose arguments are checked
    """

    key: str
    label: str
    text: str
    type_: PracticeCheckType
    tool: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label = self.label

        text = self.text

        type_: str = self.type_

        tool = self.tool

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "label": label,
                "text": text,
                "type": type_,
            }
        )
        if tool is not UNSET:
            field_dict["tool"] = tool

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        label = d.pop("label")

        text = d.pop("text")

        type_ = check_practice_check_type(d.pop("type"))

        tool = d.pop("tool", UNSET)

        practice_check = cls(
            key=key,
            label=label,
            text=text,
            type_=type_,
            tool=tool,
        )

        return practice_check
