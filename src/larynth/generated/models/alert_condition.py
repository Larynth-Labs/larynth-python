from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_clause import AlertClause


T = TypeVar("T", bound="AlertCondition")


@_attrs_define
class AlertCondition:
    """
    Attributes:
        all_ (list[AlertClause] | Unset): Every clause must match. Exactly one of all or any is set; the service rejects
            anything else with alert_rule.invalid_condition
        any_ (list[AlertClause] | Unset): At least one clause must match. Exactly one of all or any is set
    """

    all_: list[AlertClause] | Unset = UNSET
    any_: list[AlertClause] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        all_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.all_, Unset):
            all_ = []
            for all_item_data in self.all_:
                all_item = all_item_data.to_dict()
                all_.append(all_item)

        any_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.any_, Unset):
            any_ = []
            for any_item_data in self.any_:
                any_item = any_item_data.to_dict()
                any_.append(any_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if any_ is not UNSET:
            field_dict["any"] = any_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_clause import AlertClause

        d = dict(src_dict)
        _all_ = d.pop("all", UNSET)
        all_: list[AlertClause] | Unset = UNSET
        if _all_ is not UNSET:
            all_ = []
            for all_item_data in _all_:
                all_item = AlertClause.from_dict(all_item_data)

                all_.append(all_item)

        _any_ = d.pop("any", UNSET)
        any_: list[AlertClause] | Unset = UNSET
        if _any_ is not UNSET:
            any_ = []
            for any_item_data in _any_:
                any_item = AlertClause.from_dict(any_item_data)

                any_.append(any_item)

        alert_condition = cls(
            all_=all_,
            any_=any_,
        )

        return alert_condition
