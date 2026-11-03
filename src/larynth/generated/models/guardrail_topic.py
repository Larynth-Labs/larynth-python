from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GuardrailTopic")


@_attrs_define
class GuardrailTopic:
    """
    Attributes:
        topic (str): A topic the agent must not discuss
        response (str | Unset): What the agent says instead; unset uses the built-in polite refusal
    """

    topic: str
    response: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        topic = self.topic

        response = self.response

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "topic": topic,
            }
        )
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        topic = d.pop("topic")

        response = d.pop("response", UNSET)

        guardrail_topic = cls(
            topic=topic,
            response=response,
        )

        return guardrail_topic
