from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlowLLMOverride")


@_attrs_define
class FlowLLMOverride:
    """
    Attributes:
        model_id (str):
        temperature (float | Unset):
    """

    model_id: str
    temperature: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        model_id = self.model_id

        temperature = self.temperature

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "model_id": model_id,
            }
        )
        if temperature is not UNSET:
            field_dict["temperature"] = temperature

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        model_id = d.pop("model_id")

        temperature = d.pop("temperature", UNSET)

        flow_llm_override = cls(
            model_id=model_id,
            temperature=temperature,
        )

        return flow_llm_override
