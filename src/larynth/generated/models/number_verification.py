from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.number_verification_status import (
    NumberVerificationStatus,
    check_number_verification_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="NumberVerification")


@_attrs_define
class NumberVerification:
    """
    Attributes:
        status (NumberVerificationStatus):
        code (str | Unset): Key this code in a test call made through your trunk
        expires_at (datetime.datetime | Unset):
    """

    status: NumberVerificationStatus
    code: str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        code = self.code

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if code is not UNSET:
            field_dict["code"] = code
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = check_number_verification_status(d.pop("status"))

        code = d.pop("code", UNSET)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        number_verification = cls(
            status=status,
            code=code,
            expires_at=expires_at,
        )

        return number_verification
