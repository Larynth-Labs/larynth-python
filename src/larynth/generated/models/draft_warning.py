from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.draft_warning_code import DraftWarningCode, check_draft_warning_code
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.draft_warning_params import DraftWarningParams


T = TypeVar("T", bound="DraftWarning")


@_attrs_define
class DraftWarning:
    """
    Attributes:
        code (DraftWarningCode):
        field (str): Spec path, for example system_prompt
        params (DraftWarningParams | Unset):
    """

    code: DraftWarningCode
    field: str
    params: DraftWarningParams | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code: str = self.code

        field = self.field

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "field": field,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.draft_warning_params import DraftWarningParams

        d = dict(src_dict)
        code = check_draft_warning_code(d.pop("code"))

        field = d.pop("field")

        _params = d.pop("params", UNSET)
        params: DraftWarningParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = DraftWarningParams.from_dict(_params)

        draft_warning = cls(
            code=code,
            field=field,
            params=params,
        )

        return draft_warning
