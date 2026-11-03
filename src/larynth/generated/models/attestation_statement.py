from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AttestationStatement")


@_attrs_define
class AttestationStatement:
    """
    Attributes:
        key (str):
        text (str):
    """

    key: str
    text: str

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        text = self.text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        text = d.pop("text")

        attestation_statement = cls(
            key=key,
            text=text,
        )

        return attestation_statement
