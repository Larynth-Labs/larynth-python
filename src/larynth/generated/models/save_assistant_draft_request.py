from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.assistant_version_spec import AssistantVersionSpec


T = TypeVar("T", bound="SaveAssistantDraftRequest")


@_attrs_define
class SaveAssistantDraftRequest:
    """
    Attributes:
        spec (AssistantVersionSpec):
    """

    spec: AssistantVersionSpec

    def to_dict(self) -> dict[str, Any]:
        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assistant_version_spec import AssistantVersionSpec

        d = dict(src_dict)
        spec = AssistantVersionSpec.from_dict(d.pop("spec"))

        save_assistant_draft_request = cls(
            spec=spec,
        )

        return save_assistant_draft_request
