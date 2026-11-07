from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.mcp_auth_kind import McpAuthKind, check_mcp_auth_kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="McpAuth")


@_attrs_define
class McpAuth:
    """
    Attributes:
        kind (McpAuthKind):
        header_name (str | Unset): header only; not Host, Cookie, Content-Length or hop-by-hop headers
        secret_id (UUID | Unset): bearer and header
    """

    kind: McpAuthKind
    header_name: str | Unset = UNSET
    secret_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        header_name = self.header_name

        secret_id: str | Unset = UNSET
        if not isinstance(self.secret_id, Unset):
            secret_id = str(self.secret_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
            }
        )
        if header_name is not UNSET:
            field_dict["header_name"] = header_name
        if secret_id is not UNSET:
            field_dict["secret_id"] = secret_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = check_mcp_auth_kind(d.pop("kind"))

        header_name = d.pop("header_name", UNSET)

        _secret_id = d.pop("secret_id", UNSET)
        secret_id: UUID | Unset
        if isinstance(_secret_id, Unset):
            secret_id = UNSET
        else:
            secret_id = UUID(_secret_id)

        mcp_auth = cls(
            kind=kind,
            header_name=header_name,
            secret_id=secret_id,
        )

        return mcp_auth
