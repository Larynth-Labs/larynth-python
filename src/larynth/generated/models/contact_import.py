from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.contact_import_consent_kind import (
    ContactImportConsentKind,
    check_contact_import_consent_kind,
)
from ..models.contact_import_consent_source import (
    ContactImportConsentSource,
    check_contact_import_consent_source,
)
from ..models.contact_import_status import (
    ContactImportStatus,
    check_contact_import_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactImport")


@_attrs_define
class ContactImport:
    """
    Attributes:
        attested_at (datetime.datetime):
        attested_by (UUID):
        created_at (datetime.datetime):
        id (UUID):
        rows_ok (int):
        rows_rejected (int):
        rows_total (int):
        status (ContactImportStatus):
        campaign_id (UUID | Unset):
        consent_kind (ContactImportConsentKind | Unset):
        consent_source (ContactImportConsentSource | Unset):
        error (str | Unset):
        finished_at (datetime.datetime | Unset):
    """

    attested_at: datetime.datetime
    attested_by: UUID
    created_at: datetime.datetime
    id: UUID
    rows_ok: int
    rows_rejected: int
    rows_total: int
    status: ContactImportStatus
    campaign_id: UUID | Unset = UNSET
    consent_kind: ContactImportConsentKind | Unset = UNSET
    consent_source: ContactImportConsentSource | Unset = UNSET
    error: str | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attested_at = self.attested_at.isoformat()

        attested_by = str(self.attested_by)

        created_at = self.created_at.isoformat()

        id = str(self.id)

        rows_ok = self.rows_ok

        rows_rejected = self.rows_rejected

        rows_total = self.rows_total

        status: str = self.status

        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        consent_kind: str | Unset = UNSET
        if not isinstance(self.consent_kind, Unset):
            consent_kind = self.consent_kind

        consent_source: str | Unset = UNSET
        if not isinstance(self.consent_source, Unset):
            consent_source = self.consent_source

        error = self.error

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attested_at": attested_at,
                "attested_by": attested_by,
                "created_at": created_at,
                "id": id,
                "rows_ok": rows_ok,
                "rows_rejected": rows_rejected,
                "rows_total": rows_total,
                "status": status,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if consent_kind is not UNSET:
            field_dict["consent_kind"] = consent_kind
        if consent_source is not UNSET:
            field_dict["consent_source"] = consent_source
        if error is not UNSET:
            field_dict["error"] = error
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attested_at = datetime.datetime.fromisoformat(d.pop("attested_at"))

        attested_by = UUID(d.pop("attested_by"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        rows_ok = d.pop("rows_ok")

        rows_rejected = d.pop("rows_rejected")

        rows_total = d.pop("rows_total")

        status = check_contact_import_status(d.pop("status"))

        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        _consent_kind = d.pop("consent_kind", UNSET)
        consent_kind: ContactImportConsentKind | Unset
        if isinstance(_consent_kind, Unset):
            consent_kind = UNSET
        else:
            consent_kind = check_contact_import_consent_kind(_consent_kind)

        _consent_source = d.pop("consent_source", UNSET)
        consent_source: ContactImportConsentSource | Unset
        if isinstance(_consent_source, Unset):
            consent_source = UNSET
        else:
            consent_source = check_contact_import_consent_source(_consent_source)

        error = d.pop("error", UNSET)

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = datetime.datetime.fromisoformat(_finished_at)

        contact_import = cls(
            attested_at=attested_at,
            attested_by=attested_by,
            created_at=created_at,
            id=id,
            rows_ok=rows_ok,
            rows_rejected=rows_rejected,
            rows_total=rows_total,
            status=status,
            campaign_id=campaign_id,
            consent_kind=consent_kind,
            consent_source=consent_source,
            error=error,
            finished_at=finished_at,
        )

        return contact_import
