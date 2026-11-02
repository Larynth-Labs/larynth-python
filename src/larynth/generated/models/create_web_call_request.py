from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_web_call_request_variables import CreateWebCallRequestVariables


T = TypeVar("T", bound="CreateWebCallRequest")


@_attrs_define
class CreateWebCallRequest:
    """
    Attributes:
        sdp_offer (str): Complete (non-trickle) SDP offer
        use_draft (bool | Unset): Use the latest version instead of the published one Default: False.
        variables (CreateWebCallRequestVariables | Unset):
    """

    sdp_offer: str
    use_draft: bool | Unset = False
    variables: CreateWebCallRequestVariables | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sdp_offer = self.sdp_offer

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
        if use_draft is not UNSET:
            field_dict["use_draft"] = use_draft
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_web_call_request_variables import (
            CreateWebCallRequestVariables,
        )

        d = dict(src_dict)
        sdp_offer = d.pop("sdp_offer")

        use_draft = d.pop("use_draft", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: CreateWebCallRequestVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = CreateWebCallRequestVariables.from_dict(_variables)

        create_web_call_request = cls(
            sdp_offer=sdp_offer,
            use_draft=use_draft,
            variables=variables,
        )

        return create_web_call_request
