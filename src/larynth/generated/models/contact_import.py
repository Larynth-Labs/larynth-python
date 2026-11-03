from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.contact_import_consent_kind import (
    ContactImportConsentKind,
    check_contact_import_consent_kind,
)
from ..models.contact_import_consent_source import (
    ContactImportConsentSource,
    check_contact_import_consent_source,
)
from ..models.contact_import_mode import ContactImportMode, check_contact_import_mode
from ..models.contact_import_phase import ContactImportPhase, check_contact_import_phase
from ..models.contact_import_status import (
    ContactImportStatus,
    check_contact_import_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_column_mapping import ImportColumnMapping
    from ..models.import_preview import ImportPreview


T = TypeVar("T", bound="ContactImport")


@_attrs_define
class ContactImport:
    """
    Attributes:
        attested_at (datetime.datetime):
        attested_by (UUID):
        covers_marketing (bool):
        created_at (datetime.datetime):
        id (UUID):
        progress (float):
        rejects_ready (bool):
        rows_ok (int):
        rows_rejected (int):
        rows_total (int):
        status (ContactImportStatus):
        campaign_id (UUID | Unset):
        consent_kind (ContactImportConsentKind | Unset):
        consent_source (ContactImportConsentSource | Unset):
        error (str | Unset):
        evidence_text (str | Unset):
        expires_at (datetime.datetime | Unset): A validated import can be committed until then
        finished_at (datetime.datetime | Unset):
        mapping (list[ImportColumnMapping] | Unset):
        mode (ContactImportMode | Unset):
        phase (ContactImportPhase | Unset):
        preview (ImportPreview | Unset):
        tag (str | Unset):
    """

    attested_at: datetime.datetime
    attested_by: UUID
    covers_marketing: bool
    created_at: datetime.datetime
    id: UUID
    progress: float
    rejects_ready: bool
    rows_ok: int
    rows_rejected: int
    rows_total: int
    status: ContactImportStatus
    campaign_id: UUID | Unset = UNSET
    consent_kind: ContactImportConsentKind | Unset = UNSET
    consent_source: ContactImportConsentSource | Unset = UNSET
    error: str | Unset = UNSET
    evidence_text: str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET
    mapping: list[ImportColumnMapping] | Unset = UNSET
    mode: ContactImportMode | Unset = UNSET
    phase: ContactImportPhase | Unset = UNSET
    preview: ImportPreview | Unset = UNSET
    tag: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attested_at = self.attested_at.isoformat()

        attested_by = str(self.attested_by)

        covers_marketing = self.covers_marketing

        created_at = self.created_at.isoformat()

        id = str(self.id)

        progress = self.progress

        rejects_ready = self.rejects_ready

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

        evidence_text = self.evidence_text

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        mapping: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mapping, Unset):
            mapping = []
            for mapping_item_data in self.mapping:
                mapping_item = mapping_item_data.to_dict()
                mapping.append(mapping_item)

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        phase: str | Unset = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase

        preview: dict[str, Any] | Unset = UNSET
        if not isinstance(self.preview, Unset):
            preview = self.preview.to_dict()

        tag = self.tag

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attested_at": attested_at,
                "attested_by": attested_by,
                "covers_marketing": covers_marketing,
                "created_at": created_at,
                "id": id,
                "progress": progress,
                "rejects_ready": rejects_ready,
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
        if evidence_text is not UNSET:
            field_dict["evidence_text"] = evidence_text
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if mapping is not UNSET:
            field_dict["mapping"] = mapping
        if mode is not UNSET:
            field_dict["mode"] = mode
        if phase is not UNSET:
            field_dict["phase"] = phase
        if preview is not UNSET:
            field_dict["preview"] = preview
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.import_column_mapping import ImportColumnMapping
        from ..models.import_preview import ImportPreview

        d = dict(src_dict)
        attested_at = datetime.datetime.fromisoformat(d.pop("attested_at"))

        attested_by = UUID(d.pop("attested_by"))

        covers_marketing = d.pop("covers_marketing")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        progress = d.pop("progress")

        rejects_ready = d.pop("rejects_ready")

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

        evidence_text = d.pop("evidence_text", UNSET)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = datetime.datetime.fromisoformat(_finished_at)

        _mapping = d.pop("mapping", UNSET)
        mapping: list[ImportColumnMapping] | Unset = UNSET
        if _mapping is not UNSET:
            mapping = []
            for mapping_item_data in _mapping:
                mapping_item = ImportColumnMapping.from_dict(mapping_item_data)

                mapping.append(mapping_item)

        _mode = d.pop("mode", UNSET)
        mode: ContactImportMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_contact_import_mode(_mode)

        _phase = d.pop("phase", UNSET)
        phase: ContactImportPhase | Unset
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = check_contact_import_phase(_phase)

        _preview = d.pop("preview", UNSET)
        preview: ImportPreview | Unset
        if isinstance(_preview, Unset):
            preview = UNSET
        else:
            preview = ImportPreview.from_dict(_preview)

        tag = d.pop("tag", UNSET)

        contact_import = cls(
            attested_at=attested_at,
            attested_by=attested_by,
            covers_marketing=covers_marketing,
            created_at=created_at,
            id=id,
            progress=progress,
            rejects_ready=rejects_ready,
            rows_ok=rows_ok,
            rows_rejected=rows_rejected,
            rows_total=rows_total,
            status=status,
            campaign_id=campaign_id,
            consent_kind=consent_kind,
            consent_source=consent_source,
            error=error,
            evidence_text=evidence_text,
            expires_at=expires_at,
            finished_at=finished_at,
            mapping=mapping,
            mode=mode,
            phase=phase,
            preview=preview,
            tag=tag,
        )

        return contact_import
