from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.preflight_check_code import PreflightCheckCode, check_preflight_check_code
from ..models.preflight_check_state import (
    PreflightCheckState,
    check_preflight_check_state,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_fix import CheckFix
    from ..models.preflight_check_params import PreflightCheckParams


T = TypeVar("T", bound="PreflightCheck")


@_attrs_define
class PreflightCheck:
    """
    Attributes:
        code (PreflightCheckCode):
        state (PreflightCheckState):
        fix (CheckFix | Unset):
        params (PreflightCheckParams | Unset):
    """

    code: PreflightCheckCode
    state: PreflightCheckState
    fix: CheckFix | Unset = UNSET
    params: PreflightCheckParams | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code: str = self.code

        state: str = self.state

        fix: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fix, Unset):
            fix = self.fix.to_dict()

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "state": state,
            }
        )
        if fix is not UNSET:
            field_dict["fix"] = fix
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.check_fix import CheckFix
        from ..models.preflight_check_params import PreflightCheckParams

        d = dict(src_dict)
        code = check_preflight_check_code(d.pop("code"))

        state = check_preflight_check_state(d.pop("state"))

        _fix = d.pop("fix", UNSET)
        fix: CheckFix | Unset
        if isinstance(_fix, Unset):
            fix = UNSET
        else:
            fix = CheckFix.from_dict(_fix)

        _params = d.pop("params", UNSET)
        params: PreflightCheckParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = PreflightCheckParams.from_dict(_params)

        preflight_check = cls(
            code=code,
            state=state,
            fix=fix,
            params=params,
        )

        return preflight_check
