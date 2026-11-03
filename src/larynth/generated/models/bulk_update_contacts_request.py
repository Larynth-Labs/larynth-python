from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.bulk_update_contacts_request_action import (
    BulkUpdateContactsRequestAction,
    check_bulk_update_contacts_request_action,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_selection import ContactSelection


T = TypeVar("T", bound="BulkUpdateContactsRequest")


@_attrs_define
class BulkUpdateContactsRequest:
    """
    Attributes:
        action (BulkUpdateContactsRequestAction):
        selection (ContactSelection):
        campaign_id (UUID | Unset): Draft or paused campaigns only
        tag (str | Unset):
    """

    action: BulkUpdateContactsRequestAction
    selection: ContactSelection
    campaign_id: UUID | Unset = UNSET
    tag: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action: str = self.action

        selection = self.selection.to_dict()

        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        tag = self.tag

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "selection": selection,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.contact_selection import ContactSelection

        d = dict(src_dict)
        action = check_bulk_update_contacts_request_action(d.pop("action"))

        selection = ContactSelection.from_dict(d.pop("selection"))

        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        tag = d.pop("tag", UNSET)

        bulk_update_contacts_request = cls(
            action=action,
            selection=selection,
            campaign_id=campaign_id,
            tag=tag,
        )

        return bulk_update_contacts_request
