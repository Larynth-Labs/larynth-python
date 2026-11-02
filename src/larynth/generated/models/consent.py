from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.consent_kind import ConsentKind, check_consent_kind
from ..models.consent_scope_type import ConsentScopeType, check_consent_scope_type
from ..models.consent_source import ConsentSource, check_consent_source
from ..types import UNSET, Unset

T = TypeVar("T", bound="Consent")


@_attrs_define
class Consent:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        e164 (str):
        evidence_sha256 (str):
        granted_at (datetime.datetime):
        id (UUID):
        kind (ConsentKind):
        scope_type (ConsentScopeType):
        source (ConsentSource):
        captured_ip (str | Unset):
        contact_id (UUID | Unset):
        evidence_ref (str | Unset):
        evidence_text (str | Unset):
        import_id (UUID | Unset):
        scope_id (UUID | Unset):
    """

    created_at: datetime.datetime
    created_by: str
    e164: str
    evidence_sha256: str
    granted_at: datetime.datetime
    id: UUID
    kind: ConsentKind
    scope_type: ConsentScopeType
    source: ConsentSource
    captured_ip: str | Unset = UNSET
    contact_id: UUID | Unset = UNSET
    evidence_ref: str | Unset = UNSET
    evidence_text: str | Unset = UNSET
    import_id: UUID | Unset = UNSET
    scope_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        e164 = self.e164

        evidence_sha256 = self.evidence_sha256

        granted_at = self.granted_at.isoformat()

        id = str(self.id)

        kind: str = self.kind

        scope_type: str = self.scope_type

        source: str = self.source

        captured_ip = self.captured_ip

        contact_id: str | Unset = UNSET
        if not isinstance(self.contact_id, Unset):
            contact_id = str(self.contact_id)

        evidence_ref = self.evidence_ref

        evidence_text = self.evidence_text

        import_id: str | Unset = UNSET
        if not isinstance(self.import_id, Unset):
            import_id = str(self.import_id)

        scope_id: str | Unset = UNSET
        if not isinstance(self.scope_id, Unset):
            scope_id = str(self.scope_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "e164": e164,
                "evidence_sha256": evidence_sha256,
                "granted_at": granted_at,
                "id": id,
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
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if scope_id is not UNSET:
            field_dict["scope_id"] = scope_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by = d.pop("created_by")

        e164 = d.pop("e164")

        evidence_sha256 = d.pop("evidence_sha256")

        granted_at = datetime.datetime.fromisoformat(d.pop("granted_at"))

        id = UUID(d.pop("id"))

        kind = check_consent_kind(d.pop("kind"))

        scope_type = check_consent_scope_type(d.pop("scope_type"))

        source = check_consent_source(d.pop("source"))

        captured_ip = d.pop("captured_ip", UNSET)

        _contact_id = d.pop("contact_id", UNSET)
        contact_id: UUID | Unset
        if isinstance(_contact_id, Unset):
            contact_id = UNSET
        else:
            contact_id = UUID(_contact_id)

        evidence_ref = d.pop("evidence_ref", UNSET)

        evidence_text = d.pop("evidence_text", UNSET)

        _import_id = d.pop("import_id", UNSET)
        import_id: UUID | Unset
        if isinstance(_import_id, Unset):
            import_id = UNSET
        else:
            import_id = UUID(_import_id)

        _scope_id = d.pop("scope_id", UNSET)
        scope_id: UUID | Unset
        if isinstance(_scope_id, Unset):
            scope_id = UNSET
        else:
            scope_id = UUID(_scope_id)

        consent = cls(
            created_at=created_at,
            created_by=created_by,
            e164=e164,
            evidence_sha256=evidence_sha256,
            granted_at=granted_at,
            id=id,
            kind=kind,
            scope_type=scope_type,
            source=source,
            captured_ip=captured_ip,
            contact_id=contact_id,
            evidence_ref=evidence_ref,
            evidence_text=evidence_text,
            import_id=import_id,
            scope_id=scope_id,
        )

        return consent
