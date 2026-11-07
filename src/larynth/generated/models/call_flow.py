from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_flow_variables import CallFlowVariables


T = TypeVar("T", bound="CallFlow")


@_attrs_define
class CallFlow:
    """
    Attributes:
        path (list[str]): Node ids visited, at most 200
        outcome (str | Unset): Outcome of the end node the call reached
        variables (CallFlowVariables | Unset): Flow variables at the end of the call; members and above only
    """

    path: list[str]
    outcome: str | Unset = UNSET
    variables: CallFlowVariables | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        outcome = self.outcome

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "path": path,
            }
        )
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_flow_variables import CallFlowVariables

        d = dict(src_dict)
        path = cast(list[str], d.pop("path"))

        outcome = d.pop("outcome", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: CallFlowVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = CallFlowVariables.from_dict(_variables)

        call_flow = cls(
            path=path,
            outcome=outcome,
            variables=variables,
        )

        return call_flow
