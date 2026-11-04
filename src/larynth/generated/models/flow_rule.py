from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlowRule")


@_attrs_define
class FlowRule:
    """
    Attributes:
        all_ (list[FlowRule] | Unset):
        any_ (list[FlowRule] | Unset):
        not_ (FlowRule | Unset):
        op (str | Unset):
        value (Any | Unset):
        var (str | Unset):
    """

    all_: list[FlowRule] | Unset = UNSET
    any_: list[FlowRule] | Unset = UNSET
    not_: FlowRule | Unset = UNSET
    op: str | Unset = UNSET
    value: Any | Unset = UNSET
    var: str | Unset = UNSET

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

        not_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.not_, Unset):
            not_ = self.not_.to_dict()

        op = self.op

        value = self.value

        var = self.var

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if any_ is not UNSET:
            field_dict["any"] = any_
        if not_ is not UNSET:
            field_dict["not"] = not_
        if op is not UNSET:
            field_dict["op"] = op
        if value is not UNSET:
            field_dict["value"] = value
        if var is not UNSET:
            field_dict["var"] = var

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _all_ = d.pop("all", UNSET)
        all_: list[FlowRule] | Unset = UNSET
        if _all_ is not UNSET:
            all_ = []
            for all_item_data in _all_:
                all_item = FlowRule.from_dict(all_item_data)

                all_.append(all_item)

        _any_ = d.pop("any", UNSET)
        any_: list[FlowRule] | Unset = UNSET
        if _any_ is not UNSET:
            any_ = []
            for any_item_data in _any_:
                any_item = FlowRule.from_dict(any_item_data)

                any_.append(any_item)

        _not_ = d.pop("not", UNSET)
        not_: FlowRule | Unset
        if isinstance(_not_, Unset):
            not_ = UNSET
        else:
            not_ = FlowRule.from_dict(_not_)

        op = d.pop("op", UNSET)

        value = d.pop("value", UNSET)

        var = d.pop("var", UNSET)

        flow_rule = cls(
            all_=all_,
            any_=any_,
            not_=not_,
            op=op,
            value=value,
            var=var,
        )

        return flow_rule
