from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.free_rule_params import FreeRuleParams


T = TypeVar("T", bound="FreeRule")


@_attrs_define
class FreeRule:
    """
    Attributes:
        key (str):
        params (FreeRuleParams | Unset):
    """

    key: str
    params: FreeRuleParams | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.free_rule_params import FreeRuleParams

        d = dict(src_dict)
        key = d.pop("key")

        _params = d.pop("params", UNSET)
        params: FreeRuleParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = FreeRuleParams.from_dict(_params)

        free_rule = cls(
            key=key,
            params=params,
        )

        return free_rule
