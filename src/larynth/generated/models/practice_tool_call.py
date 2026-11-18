from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.practice_tool_call_args import PracticeToolCallArgs


T = TypeVar("T", bound="PracticeToolCall")


@_attrs_define
class PracticeToolCall:
    """
    Attributes:
        faked (bool): true when the answer came from a stand-in, so nothing was booked or sent
        tool (str):
        args (PracticeToolCallArgs | Unset):
        result (str | Unset):
    """

    faked: bool
    tool: str
    args: PracticeToolCallArgs | Unset = UNSET
    result: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        faked = self.faked

        tool = self.tool

        args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        result = self.result

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "faked": faked,
                "tool": tool,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.practice_tool_call_args import PracticeToolCallArgs

        d = dict(src_dict)
        faked = d.pop("faked")

        tool = d.pop("tool")

        _args = d.pop("args", UNSET)
        args: PracticeToolCallArgs | Unset
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = PracticeToolCallArgs.from_dict(_args)

        result = d.pop("result", UNSET)

        practice_tool_call = cls(
            faked=faked,
            tool=tool,
            args=args,
            result=result,
        )

        return practice_tool_call
