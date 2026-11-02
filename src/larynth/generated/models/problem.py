from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_detail import ErrorDetail


T = TypeVar("T", bound="Problem")


@_attrs_define
class Problem:
    """
    Attributes:
        code (str): Stable machine-readable error code; compliance denials carry the dial.* rule id
        status (int):
        title (str):
        type_ (str): Stable URI identifying the error code
        detail (str | Unset):
        errors (list[ErrorDetail] | Unset):
        instance (str | Unset):
        retry_at (datetime.datetime | Unset): Next moment the request may succeed (calling windows)
    """

    code: str
    status: int
    title: str
    type_: str
    detail: str | Unset = UNSET
    errors: list[ErrorDetail] | Unset = UNSET
    instance: str | Unset = UNSET
    retry_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        status = self.status

        title = self.title

        type_ = self.type_

        detail = self.detail

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        instance = self.instance

        retry_at: str | Unset = UNSET
        if not isinstance(self.retry_at, Unset):
            retry_at = self.retry_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "status": status,
                "title": title,
                "type": type_,
            }
        )
        if detail is not UNSET:
            field_dict["detail"] = detail
        if errors is not UNSET:
            field_dict["errors"] = errors
        if instance is not UNSET:
            field_dict["instance"] = instance
        if retry_at is not UNSET:
            field_dict["retry_at"] = retry_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.error_detail import ErrorDetail

        d = dict(src_dict)
        code = d.pop("code")

        status = d.pop("status")

        title = d.pop("title")

        type_ = d.pop("type")

        detail = d.pop("detail", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[ErrorDetail] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ErrorDetail.from_dict(errors_item_data)

                errors.append(errors_item)

        instance = d.pop("instance", UNSET)

        _retry_at = d.pop("retry_at", UNSET)
        retry_at: datetime.datetime | Unset
        if isinstance(_retry_at, Unset):
            retry_at = UNSET
        else:
            retry_at = datetime.datetime.fromisoformat(_retry_at)

        problem = cls(
            code=code,
            status=status,
            title=title,
            type_=type_,
            detail=detail,
            errors=errors,
            instance=instance,
            retry_at=retry_at,
        )

        problem.additional_properties = d
        return problem

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
