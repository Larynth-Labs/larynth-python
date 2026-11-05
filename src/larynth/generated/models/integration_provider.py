from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.integration_provider_auth import (
    IntegrationProviderAuth,
    check_integration_provider_auth,
)
from ..models.integration_provider_kind import (
    IntegrationProviderKind,
    check_integration_provider_kind,
)
from ..models.integration_provider_status import (
    IntegrationProviderStatus,
    check_integration_provider_status,
)

T = TypeVar("T", bound="IntegrationProvider")


@_attrs_define
class IntegrationProvider:
    """
    Attributes:
        auth (IntegrationProviderAuth):
        display_name (str):
        id (UUID):
        kind (IntegrationProviderKind):
        logo_key (str):
        status (IntegrationProviderStatus):
    """

    auth: IntegrationProviderAuth
    display_name: str
    id: UUID
    kind: IntegrationProviderKind
    logo_key: str
    status: IntegrationProviderStatus

    def to_dict(self) -> dict[str, Any]:
        auth: str = self.auth

        display_name = self.display_name

        id = str(self.id)

        kind: str = self.kind

        logo_key = self.logo_key

        status: str = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "auth": auth,
                "display_name": display_name,
                "id": id,
                "kind": kind,
                "logo_key": logo_key,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        auth = check_integration_provider_auth(d.pop("auth"))

        display_name = d.pop("display_name")

        id = UUID(d.pop("id"))

        kind = check_integration_provider_kind(d.pop("kind"))

        logo_key = d.pop("logo_key")

        status = check_integration_provider_status(d.pop("status"))

        integration_provider = cls(
            auth=auth,
            display_name=display_name,
            id=id,
            kind=kind,
            logo_key=logo_key,
            status=status,
        )

        return integration_provider
