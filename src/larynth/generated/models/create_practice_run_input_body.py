from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.create_practice_run_input_body_mode import (
    CreatePracticeRunInputBodyMode,
    check_create_practice_run_input_body_mode,
)
from ..models.create_practice_run_input_body_target import (
    CreatePracticeRunInputBodyTarget,
    check_create_practice_run_input_body_target,
)
from ..models.create_practice_run_input_body_trigger import (
    CreatePracticeRunInputBodyTrigger,
    check_create_practice_run_input_body_trigger,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePracticeRunInputBody")


@_attrs_define
class CreatePracticeRunInputBody:
    """
    Attributes:
        mode (CreatePracticeRunInputBodyMode | Unset): Only text is available; voice returns
            practice_run.mode_unavailable Default: 'text'.
        required_only (bool | Unset): Run only the required practice calls
        target (CreatePracticeRunInputBodyTarget | Unset):  Default: 'draft'.
        trigger (CreatePracticeRunInputBodyTrigger | Unset): publish marks the run as the check before publishing the
            draft Default: 'manual'.
        version (int | Unset): With target version; unset is the published version
    """

    mode: CreatePracticeRunInputBodyMode | Unset = "text"
    required_only: bool | Unset = UNSET
    target: CreatePracticeRunInputBodyTarget | Unset = "draft"
    trigger: CreatePracticeRunInputBodyTrigger | Unset = "manual"
    version: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        required_only = self.required_only

        target: str | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target

        trigger: str | Unset = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if required_only is not UNSET:
            field_dict["required_only"] = required_only
        if target is not UNSET:
            field_dict["target"] = target
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: CreatePracticeRunInputBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_create_practice_run_input_body_mode(_mode)

        required_only = d.pop("required_only", UNSET)

        _target = d.pop("target", UNSET)
        target: CreatePracticeRunInputBodyTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = check_create_practice_run_input_body_target(_target)

        _trigger = d.pop("trigger", UNSET)
        trigger: CreatePracticeRunInputBodyTrigger | Unset
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = check_create_practice_run_input_body_trigger(_trigger)

        version = d.pop("version", UNSET)

        create_practice_run_input_body = cls(
            mode=mode,
            required_only=required_only,
            target=target,
            trigger=trigger,
            version=version,
        )

        return create_practice_run_input_body
