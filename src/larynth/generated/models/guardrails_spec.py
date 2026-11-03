from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.guardrail_custom_rule import GuardrailCustomRule
    from ..models.guardrail_topic import GuardrailTopic


T = TypeVar("T", bound="GuardrailsSpec")


@_attrs_define
class GuardrailsSpec:
    """
    Attributes:
        blocked_topics (list[GuardrailTopic] | Unset):
        custom_rules (list[GuardrailCustomRule] | Unset):
    """

    blocked_topics: list[GuardrailTopic] | Unset = UNSET
    custom_rules: list[GuardrailCustomRule] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        blocked_topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blocked_topics, Unset):
            blocked_topics = []
            for blocked_topics_item_data in self.blocked_topics:
                blocked_topics_item = blocked_topics_item_data.to_dict()
                blocked_topics.append(blocked_topics_item)

        custom_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_rules, Unset):
            custom_rules = []
            for custom_rules_item_data in self.custom_rules:
                custom_rules_item = custom_rules_item_data.to_dict()
                custom_rules.append(custom_rules_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if blocked_topics is not UNSET:
            field_dict["blocked_topics"] = blocked_topics
        if custom_rules is not UNSET:
            field_dict["custom_rules"] = custom_rules

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.guardrail_custom_rule import GuardrailCustomRule
        from ..models.guardrail_topic import GuardrailTopic

        d = dict(src_dict)
        _blocked_topics = d.pop("blocked_topics", UNSET)
        blocked_topics: list[GuardrailTopic] | Unset = UNSET
        if _blocked_topics is not UNSET:
            blocked_topics = []
            for blocked_topics_item_data in _blocked_topics:
                blocked_topics_item = GuardrailTopic.from_dict(blocked_topics_item_data)

                blocked_topics.append(blocked_topics_item)

        _custom_rules = d.pop("custom_rules", UNSET)
        custom_rules: list[GuardrailCustomRule] | Unset = UNSET
        if _custom_rules is not UNSET:
            custom_rules = []
            for custom_rules_item_data in _custom_rules:
                custom_rules_item = GuardrailCustomRule.from_dict(
                    custom_rules_item_data
                )

                custom_rules.append(custom_rules_item)

        guardrails_spec = cls(
            blocked_topics=blocked_topics,
            custom_rules=custom_rules,
        )

        return guardrails_spec
