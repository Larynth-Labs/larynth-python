from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.alert_clause_op import AlertClauseOp, check_alert_clause_op
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertClause")


@_attrs_define
class AlertClause:
    """
    Attributes:
        field (str): Platform, call, analysis or data.<name> field for call_analyzed rules; caller_said, intent.* or
            agent.* for live_turn rules
        op (AlertClauseOp):
        value (Any | Unset): Operand; omitted for exists and not_exists; a list for in, not_in and contains_any (1 to 20
            phrases of at most 40 characters)
    """

    field: str
    op: AlertClauseOp
    value: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        op: str = self.op

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "field": field,
                "op": op,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field = d.pop("field")

        op = check_alert_clause_op(d.pop("op"))

        value = d.pop("value", UNSET)

        alert_clause = cls(
            field=field,
            op=op,
            value=value,
        )

        return alert_clause
