from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extraction_field import ExtractionField


T = TypeVar("T", bound="PostCallSettings")


@_attrs_define
class PostCallSettings:
    """
    Attributes:
        extraction_fields (list[ExtractionField] | Unset):
        success_criteria (str | Unset): When set, the analysis also returns successful and reason
        summary_enabled (bool | Unset): Unset is true
        summary_prompt (str | Unset): Overrides the default summary instruction
    """

    extraction_fields: list[ExtractionField] | Unset = UNSET
    success_criteria: str | Unset = UNSET
    summary_enabled: bool | Unset = UNSET
    summary_prompt: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        extraction_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extraction_fields, Unset):
            extraction_fields = []
            for extraction_fields_item_data in self.extraction_fields:
                extraction_fields_item = extraction_fields_item_data.to_dict()
                extraction_fields.append(extraction_fields_item)

        success_criteria = self.success_criteria

        summary_enabled = self.summary_enabled

        summary_prompt = self.summary_prompt

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if extraction_fields is not UNSET:
            field_dict["extraction_fields"] = extraction_fields
        if success_criteria is not UNSET:
            field_dict["success_criteria"] = success_criteria
        if summary_enabled is not UNSET:
            field_dict["summary_enabled"] = summary_enabled
        if summary_prompt is not UNSET:
            field_dict["summary_prompt"] = summary_prompt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.extraction_field import ExtractionField

        d = dict(src_dict)
        _extraction_fields = d.pop("extraction_fields", UNSET)
        extraction_fields: list[ExtractionField] | Unset = UNSET
        if _extraction_fields is not UNSET:
            extraction_fields = []
            for extraction_fields_item_data in _extraction_fields:
                extraction_fields_item = ExtractionField.from_dict(
                    extraction_fields_item_data
                )

                extraction_fields.append(extraction_fields_item)

        success_criteria = d.pop("success_criteria", UNSET)

        summary_enabled = d.pop("summary_enabled", UNSET)

        summary_prompt = d.pop("summary_prompt", UNSET)

        post_call_settings = cls(
            extraction_fields=extraction_fields,
            success_criteria=success_criteria,
            summary_enabled=summary_enabled,
            summary_prompt=summary_prompt,
        )

        return post_call_settings
