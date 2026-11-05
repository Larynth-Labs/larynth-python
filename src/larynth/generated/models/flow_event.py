from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.flow_event_kind import FlowEventKind, check_flow_event_kind
from ..models.flow_event_via import FlowEventVia, check_flow_event_via
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flow_event_variables import FlowEventVariables


T = TypeVar("T", bound="FlowEvent")


@_attrs_define
class FlowEvent:
    """
    Attributes:
        at (datetime.datetime):
        kind (FlowEventKind):
        seq (int):
        edge_id (str | Unset):
        from_node_id (str | Unset):
        node_id (str | Unset):
        outcome (str | Unset):
        path (list[str] | Unset):
        took_ms (int | Unset):
        turn_index (int | Unset):
        variables (FlowEventVariables | Unset):
        via (FlowEventVia | Unset):
    """

    at: datetime.datetime
    kind: FlowEventKind
    seq: int
    edge_id: str | Unset = UNSET
    from_node_id: str | Unset = UNSET
    node_id: str | Unset = UNSET
    outcome: str | Unset = UNSET
    path: list[str] | Unset = UNSET
    took_ms: int | Unset = UNSET
    turn_index: int | Unset = UNSET
    variables: FlowEventVariables | Unset = UNSET
    via: FlowEventVia | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        kind: str = self.kind

        seq = self.seq

        edge_id = self.edge_id

        from_node_id = self.from_node_id

        node_id = self.node_id

        outcome = self.outcome

        path: list[str] | Unset = UNSET
        if not isinstance(self.path, Unset):
            path = self.path

        took_ms = self.took_ms

        turn_index = self.turn_index

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        via: str | Unset = UNSET
        if not isinstance(self.via, Unset):
            via = self.via

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "kind": kind,
                "seq": seq,
            }
        )
        if edge_id is not UNSET:
            field_dict["edge_id"] = edge_id
        if from_node_id is not UNSET:
            field_dict["from_node_id"] = from_node_id
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if path is not UNSET:
            field_dict["path"] = path
        if took_ms is not UNSET:
            field_dict["took_ms"] = took_ms
        if turn_index is not UNSET:
            field_dict["turn_index"] = turn_index
        if variables is not UNSET:
            field_dict["variables"] = variables
        if via is not UNSET:
            field_dict["via"] = via

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flow_event_variables import FlowEventVariables

        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        kind = check_flow_event_kind(d.pop("kind"))

        seq = d.pop("seq")

        edge_id = d.pop("edge_id", UNSET)

        from_node_id = d.pop("from_node_id", UNSET)

        node_id = d.pop("node_id", UNSET)

        outcome = d.pop("outcome", UNSET)

        path = cast(list[str], d.pop("path", UNSET))

        took_ms = d.pop("took_ms", UNSET)

        turn_index = d.pop("turn_index", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: FlowEventVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = FlowEventVariables.from_dict(_variables)

        _via = d.pop("via", UNSET)
        via: FlowEventVia | Unset
        if isinstance(_via, Unset):
            via = UNSET
        else:
            via = check_flow_event_via(_via)

        flow_event = cls(
            at=at,
            kind=kind,
            seq=seq,
            edge_id=edge_id,
            from_node_id=from_node_id,
            node_id=node_id,
            outcome=outcome,
            path=path,
            took_ms=took_ms,
            turn_index=turn_index,
            variables=variables,
            via=via,
        )

        return flow_event
