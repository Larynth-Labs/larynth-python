from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.campaign_contact_enrolment import CampaignContactEnrolment


T = TypeVar("T", bound="AddCampaignContactsRequest")


@_attrs_define
class AddCampaignContactsRequest:
    """
    Attributes:
        contacts (list[CampaignContactEnrolment]):
    """

    contacts: list[CampaignContactEnrolment]

    def to_dict(self) -> dict[str, Any]:
        contacts = []
        for contacts_item_data in self.contacts:
            contacts_item = contacts_item_data.to_dict()
            contacts.append(contacts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contacts": contacts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.campaign_contact_enrolment import CampaignContactEnrolment

        d = dict(src_dict)
        contacts = []
        _contacts = d.pop("contacts")
        for contacts_item_data in _contacts:
            contacts_item = CampaignContactEnrolment.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        add_campaign_contacts_request = cls(
            contacts=contacts,
        )

        return add_campaign_contacts_request
