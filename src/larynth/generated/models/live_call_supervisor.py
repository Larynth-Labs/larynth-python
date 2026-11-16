from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.live_call_supervisor_mode import (
    LiveCallSupervisorMode,
    check_live_call_supervisor_mode,
)
from ..models.live_call_supervisor_phase import (
    LiveCallSupervisorPhase,
    check_live_call_supervisor_phase,
)

T = TypeVar("T", bound="LiveCallSupervisor")


@_attrs_define
class LiveCallSupervisor:
    """
    Attributes:
        mode (LiveCallSupervisorMode):
        phase (LiveCallSupervisorPhase):
        user_id (UUID):
    """

    mode: LiveCallSupervisorMode
    phase: LiveCallSupervisorPhase
    user_id: UUID

    def to_dict(self) -> dict[str, Any]:
        mode: str = self.mode

        phase: str = self.phase

        user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
                "phase": phase,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = check_live_call_supervisor_mode(d.pop("mode"))

        phase = check_live_call_supervisor_phase(d.pop("phase"))

        user_id = UUID(d.pop("user_id"))

        live_call_supervisor = cls(
            mode=mode,
            phase=phase,
            user_id=user_id,
        )

        return live_call_supervisor
