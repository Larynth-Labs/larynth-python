from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.flow_validation_issue_severity import (
    FlowValidationIssueSeverity,
    check_flow_validation_issue_severity,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FlowValidationIssue")


@_attrs_define
class FlowValidationIssue:
    """
    Attributes:
        code (str): Issue code from the flow validator, for example unreachable_node
        message (str):
        path (str): JSON pointer into the flow
        severity (FlowValidationIssueSeverity):
        edge_id (str | Unset):
        node_id (str | Unset):
    """

    code: str
    message: str
    path: str
    severity: FlowValidationIssueSeverity
    edge_id: str | Unset = UNSET
    node_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        path = self.path

        severity: str = self.severity

        edge_id = self.edge_id

        node_id = self.node_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "message": message,
                "path": path,
                "severity": severity,
            }
        )
        if edge_id is not UNSET:
            field_dict["edge_id"] = edge_id
        if node_id is not UNSET:
            field_dict["node_id"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        path = d.pop("path")

        severity = check_flow_validation_issue_severity(d.pop("severity"))

        edge_id = d.pop("edge_id", UNSET)

        node_id = d.pop("node_id", UNSET)

        flow_validation_issue = cls(
            code=code,
            message=message,
            path=path,
            severity=severity,
            edge_id=edge_id,
            node_id=node_id,
        )

        return flow_validation_issue
