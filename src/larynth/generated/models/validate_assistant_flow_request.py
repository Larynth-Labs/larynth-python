from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_tool import AssistantTool
    from ..models.flow_spec import FlowSpec


T = TypeVar("T", bound="ValidateAssistantFlowRequest")


@_attrs_define
class ValidateAssistantFlowRequest:
    """
    Attributes:
        flow (FlowSpec):
        tools (list[AssistantTool] | Unset): Tools to check tool nodes against; unset uses the draft's tools
    """

    flow: FlowSpec
    tools: list[AssistantTool] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        flow = self.flow.to_dict()

        tools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tools, Unset):
            tools = []
            for tools_item_data in self.tools:
                tools_item = tools_item_data.to_dict()
                tools.append(tools_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "flow": flow,
            }
        )
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assistant_tool import AssistantTool
        from ..models.flow_spec import FlowSpec

        d = dict(src_dict)
        flow = FlowSpec.from_dict(d.pop("flow"))

        _tools = d.pop("tools", UNSET)
        tools: list[AssistantTool] | Unset = UNSET
        if _tools is not UNSET:
            tools = []
            for tools_item_data in _tools:
                tools_item = AssistantTool.from_dict(tools_item_data)

                tools.append(tools_item)

        validate_assistant_flow_request = cls(
            flow=flow,
            tools=tools,
        )

        return validate_assistant_flow_request
