from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flow_assignment import FlowAssignment
    from ..models.flow_edge import FlowEdge
    from ..models.flow_field import FlowField
    from ..models.flow_global_spec import FlowGlobalSpec
    from ..models.flow_llm_override import FlowLLMOverride
    from ..models.flow_node_outputs import FlowNodeOutputs
    from ..models.flow_say import FlowSay
    from ..models.flow_target import FlowTarget


T = TypeVar("T", bound="FlowNode")


@_attrs_define
class FlowNode:
    """
    Attributes:
        id (str):
        kind (str):
        name (str):
        args (Any | Unset):
        edges (list[FlowEdge] | Unset):
        fields (list[FlowField] | Unset):
        global_ (FlowGlobalSpec | Unset):
        globals_ (str | Unset):
        inherit_tools (bool | Unset):
        llm (FlowLLMOverride | Unset):
        max_attempts (int | Unset):
        max_turns (int | Unset):
        mode (str | Unset):
        on_enter (FlowSay | Unset):
        outcome (str | Unset):
        outputs (FlowNodeOutputs | Unset):
        prompt (str | Unset):
        prompt_mode (str | Unset):
        say (FlowSay | Unset):
        set_ (list[FlowAssignment] | Unset):
        speak_result (bool | Unset):
        subflow_id (str | Unset):
        target (FlowTarget | Unset):
        tool (str | Unset):
        tools (list[str] | Unset):
        ui (Any | Unset):
        warm_summary (bool | Unset):
    """

    id: str
    kind: str
    name: str
    args: Any | Unset = UNSET
    edges: list[FlowEdge] | Unset = UNSET
    fields: list[FlowField] | Unset = UNSET
    global_: FlowGlobalSpec | Unset = UNSET
    globals_: str | Unset = UNSET
    inherit_tools: bool | Unset = UNSET
    llm: FlowLLMOverride | Unset = UNSET
    max_attempts: int | Unset = UNSET
    max_turns: int | Unset = UNSET
    mode: str | Unset = UNSET
    on_enter: FlowSay | Unset = UNSET
    outcome: str | Unset = UNSET
    outputs: FlowNodeOutputs | Unset = UNSET
    prompt: str | Unset = UNSET
    prompt_mode: str | Unset = UNSET
    say: FlowSay | Unset = UNSET
    set_: list[FlowAssignment] | Unset = UNSET
    speak_result: bool | Unset = UNSET
    subflow_id: str | Unset = UNSET
    target: FlowTarget | Unset = UNSET
    tool: str | Unset = UNSET
    tools: list[str] | Unset = UNSET
    ui: Any | Unset = UNSET
    warm_summary: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind

        name = self.name

        args = self.args

        edges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.edges, Unset):
            edges = []
            for edges_item_data in self.edges:
                edges_item = edges_item_data.to_dict()
                edges.append(edges_item)

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        global_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_, Unset):
            global_ = self.global_.to_dict()

        globals_ = self.globals_

        inherit_tools = self.inherit_tools

        llm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.llm, Unset):
            llm = self.llm.to_dict()

        max_attempts = self.max_attempts

        max_turns = self.max_turns

        mode = self.mode

        on_enter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.on_enter, Unset):
            on_enter = self.on_enter.to_dict()

        outcome = self.outcome

        outputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        prompt = self.prompt

        prompt_mode = self.prompt_mode

        say: dict[str, Any] | Unset = UNSET
        if not isinstance(self.say, Unset):
            say = self.say.to_dict()

        set_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.set_, Unset):
            set_ = []
            for set_item_data in self.set_:
                set_item = set_item_data.to_dict()
                set_.append(set_item)

        speak_result = self.speak_result

        subflow_id = self.subflow_id

        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        tool = self.tool

        tools: list[str] | Unset = UNSET
        if not isinstance(self.tools, Unset):
            tools = self.tools

        ui = self.ui

        warm_summary = self.warm_summary

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "name": name,
            }
        )
        if args is not UNSET:
            field_dict["args"] = args
        if edges is not UNSET:
            field_dict["edges"] = edges
        if fields is not UNSET:
            field_dict["fields"] = fields
        if global_ is not UNSET:
            field_dict["global"] = global_
        if globals_ is not UNSET:
            field_dict["globals"] = globals_
        if inherit_tools is not UNSET:
            field_dict["inherit_tools"] = inherit_tools
        if llm is not UNSET:
            field_dict["llm"] = llm
        if max_attempts is not UNSET:
            field_dict["max_attempts"] = max_attempts
        if max_turns is not UNSET:
            field_dict["max_turns"] = max_turns
        if mode is not UNSET:
            field_dict["mode"] = mode
        if on_enter is not UNSET:
            field_dict["on_enter"] = on_enter
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if prompt_mode is not UNSET:
            field_dict["prompt_mode"] = prompt_mode
        if say is not UNSET:
            field_dict["say"] = say
        if set_ is not UNSET:
            field_dict["set"] = set_
        if speak_result is not UNSET:
            field_dict["speak_result"] = speak_result
        if subflow_id is not UNSET:
            field_dict["subflow_id"] = subflow_id
        if target is not UNSET:
            field_dict["target"] = target
        if tool is not UNSET:
            field_dict["tool"] = tool
        if tools is not UNSET:
            field_dict["tools"] = tools
        if ui is not UNSET:
            field_dict["ui"] = ui
        if warm_summary is not UNSET:
            field_dict["warm_summary"] = warm_summary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flow_assignment import FlowAssignment
        from ..models.flow_edge import FlowEdge
        from ..models.flow_field import FlowField
        from ..models.flow_global_spec import FlowGlobalSpec
        from ..models.flow_llm_override import FlowLLMOverride
        from ..models.flow_node_outputs import FlowNodeOutputs
        from ..models.flow_say import FlowSay
        from ..models.flow_target import FlowTarget

        d = dict(src_dict)
        id = d.pop("id")

        kind = d.pop("kind")

        name = d.pop("name")

        args = d.pop("args", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: list[FlowEdge] | Unset = UNSET
        if _edges is not UNSET:
            edges = []
            for edges_item_data in _edges:
                edges_item = FlowEdge.from_dict(edges_item_data)

                edges.append(edges_item)

        _fields = d.pop("fields", UNSET)
        fields: list[FlowField] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = FlowField.from_dict(fields_item_data)

                fields.append(fields_item)

        _global_ = d.pop("global", UNSET)
        global_: FlowGlobalSpec | Unset
        if isinstance(_global_, Unset):
            global_ = UNSET
        else:
            global_ = FlowGlobalSpec.from_dict(_global_)

        globals_ = d.pop("globals", UNSET)

        inherit_tools = d.pop("inherit_tools", UNSET)

        _llm = d.pop("llm", UNSET)
        llm: FlowLLMOverride | Unset
        if isinstance(_llm, Unset):
            llm = UNSET
        else:
            llm = FlowLLMOverride.from_dict(_llm)

        max_attempts = d.pop("max_attempts", UNSET)

        max_turns = d.pop("max_turns", UNSET)

        mode = d.pop("mode", UNSET)

        _on_enter = d.pop("on_enter", UNSET)
        on_enter: FlowSay | Unset
        if isinstance(_on_enter, Unset):
            on_enter = UNSET
        else:
            on_enter = FlowSay.from_dict(_on_enter)

        outcome = d.pop("outcome", UNSET)

        _outputs = d.pop("outputs", UNSET)
        outputs: FlowNodeOutputs | Unset
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = FlowNodeOutputs.from_dict(_outputs)

        prompt = d.pop("prompt", UNSET)

        prompt_mode = d.pop("prompt_mode", UNSET)

        _say = d.pop("say", UNSET)
        say: FlowSay | Unset
        if isinstance(_say, Unset):
            say = UNSET
        else:
            say = FlowSay.from_dict(_say)

        _set_ = d.pop("set", UNSET)
        set_: list[FlowAssignment] | Unset = UNSET
        if _set_ is not UNSET:
            set_ = []
            for set_item_data in _set_:
                set_item = FlowAssignment.from_dict(set_item_data)

                set_.append(set_item)

        speak_result = d.pop("speak_result", UNSET)

        subflow_id = d.pop("subflow_id", UNSET)

        _target = d.pop("target", UNSET)
        target: FlowTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = FlowTarget.from_dict(_target)

        tool = d.pop("tool", UNSET)

        tools = cast(list[str], d.pop("tools", UNSET))

        ui = d.pop("ui", UNSET)

        warm_summary = d.pop("warm_summary", UNSET)

        flow_node = cls(
            id=id,
            kind=kind,
            name=name,
            args=args,
            edges=edges,
            fields=fields,
            global_=global_,
            globals_=globals_,
            inherit_tools=inherit_tools,
            llm=llm,
            max_attempts=max_attempts,
            max_turns=max_turns,
            mode=mode,
            on_enter=on_enter,
            outcome=outcome,
            outputs=outputs,
            prompt=prompt,
            prompt_mode=prompt_mode,
            say=say,
            set_=set_,
            speak_result=speak_result,
            subflow_id=subflow_id,
            target=target,
            tool=tool,
            tools=tools,
            ui=ui,
            warm_summary=warm_summary,
        )

        return flow_node
