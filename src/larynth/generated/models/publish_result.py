from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.assistant import Assistant
    from ..models.assistant_publish import AssistantPublish


T = TypeVar("T", bound="PublishResult")


@_attrs_define
class PublishResult:
    """
    Attributes:
        assistant (Assistant):
        publish (AssistantPublish):
    """

    assistant: Assistant
    publish: AssistantPublish

    def to_dict(self) -> dict[str, Any]:
        assistant = self.assistant.to_dict()

        publish = self.publish.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant": assistant,
                "publish": publish,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assistant import Assistant
        from ..models.assistant_publish import AssistantPublish

        d = dict(src_dict)
        assistant = Assistant.from_dict(d.pop("assistant"))

        publish = AssistantPublish.from_dict(d.pop("publish"))

        publish_result = cls(
            assistant=assistant,
            publish=publish,
        )

        return publish_result
