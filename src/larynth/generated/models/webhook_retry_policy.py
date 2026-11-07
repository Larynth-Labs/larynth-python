from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebhookRetryPolicy")


@_attrs_define
class WebhookRetryPolicy:
    """
    Attributes:
        disable_after_consecutive_failures (int):
        max_attempts (int):
        schedule_seconds (list[int]): Delay before each retry
    """

    disable_after_consecutive_failures: int
    max_attempts: int
    schedule_seconds: list[int]

    def to_dict(self) -> dict[str, Any]:
        disable_after_consecutive_failures = self.disable_after_consecutive_failures

        max_attempts = self.max_attempts

        schedule_seconds = self.schedule_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "disable_after_consecutive_failures": disable_after_consecutive_failures,
                "max_attempts": max_attempts,
                "schedule_seconds": schedule_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        disable_after_consecutive_failures = d.pop("disable_after_consecutive_failures")

        max_attempts = d.pop("max_attempts")

        schedule_seconds = cast(list[int], d.pop("schedule_seconds"))

        webhook_retry_policy = cls(
            disable_after_consecutive_failures=disable_after_consecutive_failures,
            max_attempts=max_attempts,
            schedule_seconds=schedule_seconds,
        )

        return webhook_retry_policy
