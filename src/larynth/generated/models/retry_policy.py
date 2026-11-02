from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetryPolicy")


@_attrs_define
class RetryPolicy:
    """
    Attributes:
        busy (str | Unset):
        failed (str | Unset):
        no_answer (str | Unset): Delay before retrying; absent means no retry
        voicemail_left (str | Unset):
    """

    busy: str | Unset = UNSET
    failed: str | Unset = UNSET
    no_answer: str | Unset = UNSET
    voicemail_left: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        busy = self.busy

        failed = self.failed

        no_answer = self.no_answer

        voicemail_left = self.voicemail_left

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if busy is not UNSET:
            field_dict["busy"] = busy
        if failed is not UNSET:
            field_dict["failed"] = failed
        if no_answer is not UNSET:
            field_dict["no_answer"] = no_answer
        if voicemail_left is not UNSET:
            field_dict["voicemail_left"] = voicemail_left

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        busy = d.pop("busy", UNSET)

        failed = d.pop("failed", UNSET)

        no_answer = d.pop("no_answer", UNSET)

        voicemail_left = d.pop("voicemail_left", UNSET)

        retry_policy = cls(
            busy=busy,
            failed=failed,
            no_answer=no_answer,
            voicemail_left=voicemail_left,
        )

        return retry_policy
