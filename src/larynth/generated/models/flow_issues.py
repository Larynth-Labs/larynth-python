from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.flow_validation_issue import FlowValidationIssue


T = TypeVar("T", bound="FlowIssues")


@_attrs_define
class FlowIssues:
    """
    Attributes:
        issues (list[FlowValidationIssue]):
    """

    issues: list[FlowValidationIssue]

    def to_dict(self) -> dict[str, Any]:
        issues = []
        for issues_item_data in self.issues:
            issues_item = issues_item_data.to_dict()
            issues.append(issues_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "issues": issues,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flow_validation_issue import FlowValidationIssue

        d = dict(src_dict)
        issues = []
        _issues = d.pop("issues")
        for issues_item_data in _issues:
            issues_item = FlowValidationIssue.from_dict(issues_item_data)

            issues.append(issues_item)

        flow_issues = cls(
            issues=issues,
        )

        return flow_issues
