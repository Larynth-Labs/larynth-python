from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.compliance_text_view_kind import (
    ComplianceTextViewKind,
    check_compliance_text_view_kind,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attestation_statement import AttestationStatement


T = TypeVar("T", bound="ComplianceTextView")


@_attrs_define
class ComplianceTextView:
    """
    Attributes:
        active (bool):
        body (str):
        counsel_reviewed (bool):
        id (UUID):
        kind (ComplianceTextViewKind):
        language (str):
        version (int):
        statements (list[AttestationStatement] | Unset): inbound_ai_attestation only: the statements the owner confirms
            one by one
    """

    active: bool
    body: str
    counsel_reviewed: bool
    id: UUID
    kind: ComplianceTextViewKind
    language: str
    version: int
    statements: list[AttestationStatement] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        body = self.body

        counsel_reviewed = self.counsel_reviewed

        id = str(self.id)

        kind: str = self.kind

        language = self.language

        version = self.version

        statements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statements, Unset):
            statements = []
            for statements_item_data in self.statements:
                statements_item = statements_item_data.to_dict()
                statements.append(statements_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "active": active,
                "body": body,
                "counsel_reviewed": counsel_reviewed,
                "id": id,
                "kind": kind,
                "language": language,
                "version": version,
            }
        )
        if statements is not UNSET:
            field_dict["statements"] = statements

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.attestation_statement import AttestationStatement

        d = dict(src_dict)
        active = d.pop("active")

        body = d.pop("body")

        counsel_reviewed = d.pop("counsel_reviewed")

        id = UUID(d.pop("id"))

        kind = check_compliance_text_view_kind(d.pop("kind"))

        language = d.pop("language")

        version = d.pop("version")

        _statements = d.pop("statements", UNSET)
        statements: list[AttestationStatement] | Unset = UNSET
        if _statements is not UNSET:
            statements = []
            for statements_item_data in _statements:
                statements_item = AttestationStatement.from_dict(statements_item_data)

                statements.append(statements_item)

        compliance_text_view = cls(
            active=active,
            body=body,
            counsel_reviewed=counsel_reviewed,
            id=id,
            kind=kind,
            language=language,
            version=version,
            statements=statements,
        )

        return compliance_text_view
