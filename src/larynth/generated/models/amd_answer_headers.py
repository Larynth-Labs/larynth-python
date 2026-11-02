from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AMDAnswerHeaders")


@_attrs_define
class AMDAnswerHeaders:
    """
    Attributes:
        diversion (list[str] | Unset):
        history_info (list[str] | Unset):
        p_early_media (list[str] | Unset):
        reason (list[str] | Unset):
    """

    diversion: list[str] | Unset = UNSET
    history_info: list[str] | Unset = UNSET
    p_early_media: list[str] | Unset = UNSET
    reason: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        diversion: list[str] | Unset = UNSET
        if not isinstance(self.diversion, Unset):
            diversion = self.diversion

        history_info: list[str] | Unset = UNSET
        if not isinstance(self.history_info, Unset):
            history_info = self.history_info

        p_early_media: list[str] | Unset = UNSET
        if not isinstance(self.p_early_media, Unset):
            p_early_media = self.p_early_media

        reason: list[str] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if diversion is not UNSET:
            field_dict["diversion"] = diversion
        if history_info is not UNSET:
            field_dict["history_info"] = history_info
        if p_early_media is not UNSET:
            field_dict["p_early_media"] = p_early_media
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        diversion = cast(list[str], d.pop("diversion", UNSET))

        history_info = cast(list[str], d.pop("history_info", UNSET))

        p_early_media = cast(list[str], d.pop("p_early_media", UNSET))

        reason = cast(list[str], d.pop("reason", UNSET))

        amd_answer_headers = cls(
            diversion=diversion,
            history_info=history_info,
            p_early_media=p_early_media,
            reason=reason,
        )

        return amd_answer_headers
