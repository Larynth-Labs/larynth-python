from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.create_practice_run_input_body_target import (
    CreatePracticeRunInputBodyTarget,
    check_create_practice_run_input_body_target,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePracticeRunInputBody")


@_attrs_define
class CreatePracticeRunInputBody:
    """
    Attributes:
        target (CreatePracticeRunInputBodyTarget | Unset):  Default: 'draft'.
        version (int | Unset): With target version; unset is the published version
    """

    target: CreatePracticeRunInputBodyTarget | Unset = "draft"
    version: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        target: str | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if target is not UNSET:
            field_dict["target"] = target
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _target = d.pop("target", UNSET)
        target: CreatePracticeRunInputBodyTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = check_create_practice_run_input_body_target(_target)

        version = d.pop("version", UNSET)

        create_practice_run_input_body = cls(
            target=target,
            version=version,
        )

        return create_practice_run_input_body
