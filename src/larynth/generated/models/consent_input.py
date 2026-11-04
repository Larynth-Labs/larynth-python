from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.consent_input_kind import ConsentInputKind, check_consent_input_kind
from ..models.consent_input_source import ConsentInputSource, check_consent_input_source
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsentInput")


@_attrs_define
class ConsentInput:
    """
    Attributes:
        attest (bool): Must be true: the user attests the evidence is genuine
        evidence_text (str):
        kind (ConsentInputKind):
        source (ConsentInputSource):
        covers_marketing (bool | Unset): express_written only
        evidence_ref (str | Unset):
        granted_at (datetime.datetime | Unset): Defaults to now
    """

    attest: bool
    evidence_text: str
    kind: ConsentInputKind
    source: ConsentInputSource
    covers_marketing: bool | Unset = UNSET
    evidence_ref: str | Unset = UNSET
    granted_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attest = self.attest

        evidence_text = self.evidence_text

        kind: str = self.kind

        source: str = self.source

        covers_marketing = self.covers_marketing

        evidence_ref = self.evidence_ref

        granted_at: str | Unset = UNSET
        if not isinstance(self.granted_at, Unset):
            granted_at = self.granted_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attest": attest,
                "evidence_text": evidence_text,
                "kind": kind,
                "source": source,
            }
        )
        if covers_marketing is not UNSET:
            field_dict["covers_marketing"] = covers_marketing
        if evidence_ref is not UNSET:
            field_dict["evidence_ref"] = evidence_ref
        if granted_at is not UNSET:
            field_dict["granted_at"] = granted_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        attest = d.pop("attest")

        evidence_text = d.pop("evidence_text")

        kind = check_consent_input_kind(d.pop("kind"))

        source = check_consent_input_source(d.pop("source"))

        covers_marketing = d.pop("covers_marketing", UNSET)

        evidence_ref = d.pop("evidence_ref", UNSET)

        _granted_at = d.pop("granted_at", UNSET)
        granted_at: datetime.datetime | Unset
        if isinstance(_granted_at, Unset):
            granted_at = UNSET
        else:
            granted_at = datetime.datetime.fromisoformat(_granted_at)

        consent_input = cls(
            attest=attest,
            evidence_text=evidence_text,
            kind=kind,
            source=source,
            covers_marketing=covers_marketing,
            evidence_ref=evidence_ref,
            granted_at=granted_at,
        )

        return consent_input
