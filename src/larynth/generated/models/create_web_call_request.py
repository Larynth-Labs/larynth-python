from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_web_call_request_flow_variables import (
        CreateWebCallRequestFlowVariables,
    )
    from ..models.create_web_call_request_variables import CreateWebCallRequestVariables


T = TypeVar("T", bound="CreateWebCallRequest")


@_attrs_define
class CreateWebCallRequest:
    """
    Attributes:
        sdp_offer (str): Complete (non-trickle) SDP offer
        flow_variables (CreateWebCallRequestFlowVariables | Unset): Flow agents: seed declared variables, in string form
        start_node_id (str | Unset): Flow agents: start the test call at this step
        use_draft (bool | Unset): Use the open draft (else the latest version) instead of the published one Default:
            False.
        variables (CreateWebCallRequestVariables | Unset):
    """

    sdp_offer: str
    flow_variables: CreateWebCallRequestFlowVariables | Unset = UNSET
    start_node_id: str | Unset = UNSET
    use_draft: bool | Unset = False
    variables: CreateWebCallRequestVariables | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sdp_offer = self.sdp_offer

        flow_variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flow_variables, Unset):
            flow_variables = self.flow_variables.to_dict()

        start_node_id = self.start_node_id

        use_draft = self.use_draft

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "sdp_offer": sdp_offer,
            }
        )
        if flow_variables is not UNSET:
            field_dict["flow_variables"] = flow_variables
        if start_node_id is not UNSET:
            field_dict["start_node_id"] = start_node_id
        if use_draft is not UNSET:
            field_dict["use_draft"] = use_draft
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_web_call_request_flow_variables import (
            CreateWebCallRequestFlowVariables,
        )
        from ..models.create_web_call_request_variables import (
            CreateWebCallRequestVariables,
        )

        d = dict(src_dict)
        sdp_offer = d.pop("sdp_offer")

        _flow_variables = d.pop("flow_variables", UNSET)
        flow_variables: CreateWebCallRequestFlowVariables | Unset
        if isinstance(_flow_variables, Unset):
            flow_variables = UNSET
        else:
            flow_variables = CreateWebCallRequestFlowVariables.from_dict(
                _flow_variables
            )

        start_node_id = d.pop("start_node_id", UNSET)

        use_draft = d.pop("use_draft", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: CreateWebCallRequestVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = CreateWebCallRequestVariables.from_dict(_variables)

        create_web_call_request = cls(
            sdp_offer=sdp_offer,
            flow_variables=flow_variables,
            start_node_id=start_node_id,
            use_draft=use_draft,
            variables=variables,
        )

        return create_web_call_request
