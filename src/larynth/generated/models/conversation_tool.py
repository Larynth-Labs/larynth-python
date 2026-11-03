from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.conversation_tool_status import (
    ConversationToolStatus,
    check_conversation_tool_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_tool_args import ConversationToolArgs
    from ..models.conversation_tool_result import ConversationToolResult


T = TypeVar("T", bound="ConversationTool")


@_attrs_define
class ConversationTool:
    """
    Attributes:
        duration_ms (int):
        name (str):
        status (ConversationToolStatus):
        args (ConversationToolArgs | Unset):
        result (ConversationToolResult | Unset):
    """

    duration_ms: int
    name: str
    status: ConversationToolStatus
    args: ConversationToolArgs | Unset = UNSET
    result: ConversationToolResult | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        duration_ms = self.duration_ms

        name = self.name

        status: str = self.status

        args: dict[str, Any] | Unset = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "duration_ms": duration_ms,
                "name": name,
                "status": status,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.conversation_tool_args import ConversationToolArgs
        from ..models.conversation_tool_result import ConversationToolResult

        d = dict(src_dict)
        duration_ms = d.pop("duration_ms")

        name = d.pop("name")

        status = check_conversation_tool_status(d.pop("status"))

        _args = d.pop("args", UNSET)
        args: ConversationToolArgs | Unset
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = ConversationToolArgs.from_dict(_args)

        _result = d.pop("result", UNSET)
        result: ConversationToolResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ConversationToolResult.from_dict(_result)

        conversation_tool = cls(
            duration_ms=duration_ms,
            name=name,
            status=status,
            args=args,
            result=result,
        )

        return conversation_tool
