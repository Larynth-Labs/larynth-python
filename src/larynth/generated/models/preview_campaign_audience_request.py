from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.preview_campaign_audience_request_purpose import (
    PreviewCampaignAudienceRequestPurpose,
    check_preview_campaign_audience_request_purpose,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audience import Audience


T = TypeVar("T", bound="PreviewCampaignAudienceRequest")


@_attrs_define
class PreviewCampaignAudienceRequest:
    """
    Attributes:
        audience (Audience):
        purpose (PreviewCampaignAudienceRequestPurpose):
        informational_category (str | Unset):
    """

    audience: Audience
    purpose: PreviewCampaignAudienceRequestPurpose
    informational_category: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        audience = self.audience.to_dict()

        purpose: str = self.purpose

        informational_category = self.informational_category

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "audience": audience,
                "purpose": purpose,
            }
        )
        if informational_category is not UNSET:
            field_dict["informational_category"] = informational_category

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audience import Audience

        d = dict(src_dict)
        audience = Audience.from_dict(d.pop("audience"))

        purpose = check_preview_campaign_audience_request_purpose(d.pop("purpose"))

        informational_category = d.pop("informational_category", UNSET)

        preview_campaign_audience_request = cls(
            audience=audience,
            purpose=purpose,
            informational_category=informational_category,
        )

        return preview_campaign_audience_request
