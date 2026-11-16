from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.issue import Issue
    from ..models.issues_summary_by_kind import IssuesSummaryByKind


T = TypeVar("T", bound="IssuesSummary")


@_attrs_define
class IssuesSummary:
    """
    Attributes:
        by_kind (IssuesSummaryByKind):
        open_ (int):
        top (list[Issue]): At most three open issues, worst first
    """

    by_kind: IssuesSummaryByKind
    open_: int
    top: list[Issue]

    def to_dict(self) -> dict[str, Any]:
        by_kind = self.by_kind.to_dict()

        open_ = self.open_

        top = []
        for top_item_data in self.top:
            top_item = top_item_data.to_dict()
            top.append(top_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "by_kind": by_kind,
                "open": open_,
                "top": top,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.issue import Issue
        from ..models.issues_summary_by_kind import IssuesSummaryByKind

        d = dict(src_dict)
        by_kind = IssuesSummaryByKind.from_dict(d.pop("by_kind"))

        open_ = d.pop("open")

        top = []
        _top = d.pop("top")
        for top_item_data in _top:
            top_item = Issue.from_dict(top_item_data)

            top.append(top_item)

        issues_summary = cls(
            by_kind=by_kind,
            open_=open_,
            top=top,
        )

        return issues_summary
