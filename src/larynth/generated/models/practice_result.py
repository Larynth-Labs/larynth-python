from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.practice_result_state import (
    PracticeResultState,
    check_practice_result_state,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.practice_check_result import PracticeCheckResult
    from ..models.practice_tool_call import PracticeToolCall
    from ..models.practice_turn import PracticeTurn


T = TypeVar("T", bound="PracticeResult")


@_attrs_define
class PracticeResult:
    """
    Attributes:
        attempt (int):
        checks (list[PracticeCheckResult]):
        created_at (datetime.datetime):
        id (UUID):
        run_id (UUID):
        state (PracticeResultState):
        test_name (str):
        tool_calls (list[PracticeToolCall]):
        transcript (list[PracticeTurn]):
        error (str | Unset):
        test_id (UUID | Unset):
    """

    attempt: int
    checks: list[PracticeCheckResult]
    created_at: datetime.datetime
    id: UUID
    run_id: UUID
    state: PracticeResultState
    test_name: str
    tool_calls: list[PracticeToolCall]
    transcript: list[PracticeTurn]
    error: str | Unset = UNSET
    test_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attempt = self.attempt

        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()
            checks.append(checks_item)

        created_at = self.created_at.isoformat()

        id = str(self.id)

        run_id = str(self.run_id)

        state: str = self.state

        test_name = self.test_name

        tool_calls = []
        for tool_calls_item_data in self.tool_calls:
            tool_calls_item = tool_calls_item_data.to_dict()
            tool_calls.append(tool_calls_item)

        transcript = []
        for transcript_item_data in self.transcript:
            transcript_item = transcript_item_data.to_dict()
            transcript.append(transcript_item)

        error = self.error

        test_id: str | Unset = UNSET
        if not isinstance(self.test_id, Unset):
            test_id = str(self.test_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempt": attempt,
                "checks": checks,
                "created_at": created_at,
                "id": id,
                "run_id": run_id,
                "state": state,
                "test_name": test_name,
                "tool_calls": tool_calls,
                "transcript": transcript,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if test_id is not UNSET:
            field_dict["test_id"] = test_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.practice_check_result import PracticeCheckResult
        from ..models.practice_tool_call import PracticeToolCall
        from ..models.practice_turn import PracticeTurn

        d = dict(src_dict)
        attempt = d.pop("attempt")

        checks = []
        _checks = d.pop("checks")
        for checks_item_data in _checks:
            checks_item = PracticeCheckResult.from_dict(checks_item_data)

            checks.append(checks_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        run_id = UUID(d.pop("run_id"))

        state = check_practice_result_state(d.pop("state"))

        test_name = d.pop("test_name")

        tool_calls = []
        _tool_calls = d.pop("tool_calls")
        for tool_calls_item_data in _tool_calls:
            tool_calls_item = PracticeToolCall.from_dict(tool_calls_item_data)

            tool_calls.append(tool_calls_item)

        transcript = []
        _transcript = d.pop("transcript")
        for transcript_item_data in _transcript:
            transcript_item = PracticeTurn.from_dict(transcript_item_data)

            transcript.append(transcript_item)

        error = d.pop("error", UNSET)

        _test_id = d.pop("test_id", UNSET)
        test_id: UUID | Unset
        if isinstance(_test_id, Unset):
            test_id = UNSET
        else:
            test_id = UUID(_test_id)

        practice_result = cls(
            attempt=attempt,
            checks=checks,
            created_at=created_at,
            id=id,
            run_id=run_id,
            state=state,
            test_name=test_name,
            tool_calls=tool_calls,
            transcript=transcript,
            error=error,
            test_id=test_id,
        )

        return practice_result
