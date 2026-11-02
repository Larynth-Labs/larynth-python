from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.create_consent_request_kind import (
    CreateConsentRequestKind,
    check_create_consent_request_kind,
)
from ..models.create_consent_request_scope_type import (
    CreateConsentRequestScopeType,
    check_create_consent_request_scope_type,
)
from ..models.create_consent_request_source import (
    CreateConsentRequestSource,
    check_create_consent_request_source,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateConsentRequest")


@_attrs_define
class CreateConsentRequest:
    """
    Attributes:
        e164 (str):
        granted_at (datetime.datetime):
        kind (CreateConsentRequestKind):
        scope_type (CreateConsentRequestScopeType):
        source (CreateConsentRequestSource):
        captured_ip (str | Unset):
        contact_id (UUID | Unset):
        evidence_ref (str | Unset): One of evidence_ref or evidence_text is required
        evidence_text (str | Unset):
        scope_id (UUID | Unset): Campaign id; required when scope_type is campaign
    """

    e164: str
    granted_at: datetime.datetime
    kind: CreateConsentRequestKind
    scope_type: CreateConsentRequestScopeType
    source: CreateConsentRequestSource
    captured_ip: str | Unset = UNSET
    contact_id: UUID | Unset = UNSET
    evidence_ref: str | Unset = UNSET
    evidence_text: str | Unset = UNSET
    scope_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        e164 = self.e164

        granted_at = self.granted_at.isoformat()

        kind: str = self.kind

        scope_type: str = self.scope_type

        source: str = self.source

        captured_ip = self.captured_ip

        contact_id: str | Unset = UNSET
        if not isinstance(self.contact_id, Unset):
            contact_id = str(self.contact_id)

        evidence_ref = self.evidence_ref

        evidence_text = self.evidence_text

        scope_id: str | Unset = UNSET
        if not isinstance(self.scope_id, Unset):
            scope_id = str(self.scope_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "e164": e164,
                "granted_at": granted_at,
                "kind": kind,
                "scope_type": scope_type,
                "source": source,
            }
        )
        if captured_ip is not UNSET:
            field_dict["captured_ip"] = captured_ip
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if evidence_ref is not UNSET:
            field_dict["evidence_ref"] = evidence_ref
        if evidence_text is not UNSET:
            field_dict["evidence_text"] = evidence_text
        if scope_id is not UNSET:
            field_dict["scope_id"] = scope_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        e164 = d.pop("e164")

        granted_at = datetime.datetime.fromisoformat(d.pop("granted_at"))

        kind = check_create_consent_request_kind(d.pop("kind"))

        scope_type = check_create_consent_request_scope_type(d.pop("scope_type"))

        source = check_create_consent_request_source(d.pop("source"))

        captured_ip = d.pop("captured_ip", UNSET)

        _contact_id = d.pop("contact_id", UNSET)
        contact_id: UUID | Unset
        if isinstance(_contact_id, Unset):
            contact_id = UNSET
        else:
            contact_id = UUID(_contact_id)

        evidence_ref = d.pop("evidence_ref", UNSET)

        evidence_text = d.pop("evidence_text", UNSET)

        _scope_id = d.pop("scope_id", UNSET)
        scope_id: UUID | Unset
        if isinstance(_scope_id, Unset):
            scope_id = UNSET
        else:
            scope_id = UUID(_scope_id)

        create_consent_request = cls(
            e164=e164,
            granted_at=granted_at,
            kind=kind,
            scope_type=scope_type,
            source=source,
            captured_ip=captured_ip,
            contact_id=contact_id,
            evidence_ref=evidence_ref,
            evidence_text=evidence_text,
            scope_id=scope_id,
        )

        return create_consent_request
