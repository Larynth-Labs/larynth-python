from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.create_contact_import_body_consent_kind import (
    CreateContactImportBodyConsentKind,
    check_create_contact_import_body_consent_kind,
)
from ..models.create_contact_import_body_consent_source import (
    CreateContactImportBodyConsentSource,
    check_create_contact_import_body_consent_source,
)
from ..models.create_contact_import_body_covers_marketing import (
    CreateContactImportBodyCoversMarketing,
    check_create_contact_import_body_covers_marketing,
)
from ..models.create_contact_import_body_mode import (
    CreateContactImportBodyMode,
    check_create_contact_import_body_mode,
)
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="CreateContactImportBody")


@_attrs_define
class CreateContactImportBody:
    """
    Attributes:
        attestation_text (str): Attestation of how consent was obtained
        campaign_id (UUID | Unset): Also enrol every imported contact in this campaign
        consent_kind (CreateContactImportBodyConsentKind | Unset):
        consent_source (CreateContactImportBodyConsentSource | Unset):
        covers_marketing (CreateContactImportBodyCoversMarketing | Unset): express_written only
        evidence_text (str | Unset): Consent wording or evidence shown to the contacts
        file (File | Unset): CSV of at most 10,000 rows and 10 MB; required unless validated_import_id is given
        mapping (str | Unset): JSON array of ImportColumnMapping; without it the fixed header names apply
        mode (CreateContactImportBodyMode | Unset): validate returns the review counts without importing; default commit
        tag (str | Unset): Added to every imported contact
        validated_import_id (UUID | Unset): Commit a validated import without sending the file again (24 h)
    """

    attestation_text: str
    campaign_id: UUID | Unset = UNSET
    consent_kind: CreateContactImportBodyConsentKind | Unset = UNSET
    consent_source: CreateContactImportBodyConsentSource | Unset = UNSET
    covers_marketing: CreateContactImportBodyCoversMarketing | Unset = UNSET
    evidence_text: str | Unset = UNSET
    file: File | Unset = UNSET
    mapping: str | Unset = UNSET
    mode: CreateContactImportBodyMode | Unset = UNSET
    tag: str | Unset = UNSET
    validated_import_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attestation_text = self.attestation_text

        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        consent_kind: str | Unset = UNSET
        if not isinstance(self.consent_kind, Unset):
            consent_kind = self.consent_kind

        consent_source: str | Unset = UNSET
        if not isinstance(self.consent_source, Unset):
            consent_source = self.consent_source

        covers_marketing: str | Unset = UNSET
        if not isinstance(self.covers_marketing, Unset):
            covers_marketing = self.covers_marketing

        evidence_text = self.evidence_text

        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        mapping = self.mapping

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        tag = self.tag

        validated_import_id: str | Unset = UNSET
        if not isinstance(self.validated_import_id, Unset):
            validated_import_id = str(self.validated_import_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attestation_text": attestation_text,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if consent_kind is not UNSET:
            field_dict["consent_kind"] = consent_kind
        if consent_source is not UNSET:
            field_dict["consent_source"] = consent_source
        if covers_marketing is not UNSET:
            field_dict["covers_marketing"] = covers_marketing
        if evidence_text is not UNSET:
            field_dict["evidence_text"] = evidence_text
        if file is not UNSET:
            field_dict["file"] = file
        if mapping is not UNSET:
            field_dict["mapping"] = mapping
        if mode is not UNSET:
            field_dict["mode"] = mode
        if tag is not UNSET:
            field_dict["tag"] = tag
        if validated_import_id is not UNSET:
            field_dict["validated_import_id"] = validated_import_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(
            (
                "attestation_text",
                (None, str(self.attestation_text).encode(), "text/plain"),
            )
        )

        if not isinstance(self.campaign_id, Unset):
            files.append(("campaign_id", (None, str(self.campaign_id), "text/plain")))

        if not isinstance(self.consent_kind, Unset):
            files.append(
                ("consent_kind", (None, str(self.consent_kind).encode(), "text/plain"))
            )

        if not isinstance(self.consent_source, Unset):
            files.append(
                (
                    "consent_source",
                    (None, str(self.consent_source).encode(), "text/plain"),
                )
            )

        if not isinstance(self.covers_marketing, Unset):
            files.append(
                (
                    "covers_marketing",
                    (None, str(self.covers_marketing).encode(), "text/plain"),
                )
            )

        if not isinstance(self.evidence_text, Unset):
            files.append(
                (
                    "evidence_text",
                    (None, str(self.evidence_text).encode(), "text/plain"),
                )
            )

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        if not isinstance(self.mapping, Unset):
            files.append(("mapping", (None, str(self.mapping).encode(), "text/plain")))

        if not isinstance(self.mode, Unset):
            files.append(("mode", (None, str(self.mode).encode(), "text/plain")))

        if not isinstance(self.tag, Unset):
            files.append(("tag", (None, str(self.tag).encode(), "text/plain")))

        if not isinstance(self.validated_import_id, Unset):
            files.append(
                (
                    "validated_import_id",
                    (None, str(self.validated_import_id), "text/plain"),
                )
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attestation_text = d.pop("attestation_text")

        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        _consent_kind = d.pop("consent_kind", UNSET)
        consent_kind: CreateContactImportBodyConsentKind | Unset
        if isinstance(_consent_kind, Unset):
            consent_kind = UNSET
        else:
            consent_kind = check_create_contact_import_body_consent_kind(_consent_kind)

        _consent_source = d.pop("consent_source", UNSET)
        consent_source: CreateContactImportBodyConsentSource | Unset
        if isinstance(_consent_source, Unset):
            consent_source = UNSET
        else:
            consent_source = check_create_contact_import_body_consent_source(
                _consent_source
            )

        _covers_marketing = d.pop("covers_marketing", UNSET)
        covers_marketing: CreateContactImportBodyCoversMarketing | Unset
        if isinstance(_covers_marketing, Unset):
            covers_marketing = UNSET
        else:
            covers_marketing = check_create_contact_import_body_covers_marketing(
                _covers_marketing
            )

        evidence_text = d.pop("evidence_text", UNSET)

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        mapping = d.pop("mapping", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: CreateContactImportBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_create_contact_import_body_mode(_mode)

        tag = d.pop("tag", UNSET)

        _validated_import_id = d.pop("validated_import_id", UNSET)
        validated_import_id: UUID | Unset
        if isinstance(_validated_import_id, Unset):
            validated_import_id = UNSET
        else:
            validated_import_id = UUID(_validated_import_id)

        create_contact_import_body = cls(
            attestation_text=attestation_text,
            campaign_id=campaign_id,
            consent_kind=consent_kind,
            consent_source=consent_source,
            covers_marketing=covers_marketing,
            evidence_text=evidence_text,
            file=file,
            mapping=mapping,
            mode=mode,
            tag=tag,
            validated_import_id=validated_import_id,
        )

        create_contact_import_body.additional_properties = d
        return create_contact_import_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
