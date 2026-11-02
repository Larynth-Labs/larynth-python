from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_contact_enrolment_variables import (
        CampaignContactEnrolmentVariables,
    )


T = TypeVar("T", bound="CampaignContactEnrolment")


@_attrs_define
class CampaignContactEnrolment:
    """
    Attributes:
        contact_id (UUID):
        variables (CampaignContactEnrolmentVariables | Unset):
    """

    contact_id: UUID
    variables: CampaignContactEnrolmentVariables | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        contact_id = str(self.contact_id)

        variables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contact_id": contact_id,
            }
        )
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_contact_enrolment_variables import (
            CampaignContactEnrolmentVariables,
        )

        d = dict(src_dict)
        contact_id = UUID(d.pop("contact_id"))

        _variables = d.pop("variables", UNSET)
        variables: CampaignContactEnrolmentVariables | Unset
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = CampaignContactEnrolmentVariables.from_dict(_variables)

        campaign_contact_enrolment = cls(
            contact_id=contact_id,
            variables=variables,
        )

        return campaign_contact_enrolment
