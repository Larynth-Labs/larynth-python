from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.call_analysis_outcome import (
    CallAnalysisOutcome,
    check_call_analysis_outcome,
)
from ..models.call_analysis_sentiment import (
    CallAnalysisSentiment,
    check_call_analysis_sentiment,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_analysis_data import CallAnalysisData
    from ..models.call_quality import CallQuality
    from ..models.inbox_snippet import InboxSnippet


T = TypeVar("T", bound="CallAnalysis")


@_attrs_define
class CallAnalysis:
    """
    Attributes:
        call_id (str):
        callback_requested (bool):
        cost_micro (int): Analysis cost in micro-USD
        created_at (datetime.datetime):
        data (CallAnalysisData):
        summary (str):
        tokens (int):
        callback_by (str | Unset): As the caller said it, for example "before 10"
        caller_name (str | Unset):
        key_moment (InboxSnippet | Unset):
        model_id (UUID | Unset):
        outcome (CallAnalysisOutcome | Unset):
        quality (CallQuality | Unset):
        reason (str | Unset):
        sentiment (CallAnalysisSentiment | Unset):
        successful (bool | Unset):
        unanswered_question (str | Unset):
    """

    call_id: str
    callback_requested: bool
    cost_micro: int
    created_at: datetime.datetime
    data: CallAnalysisData
    summary: str
    tokens: int
    callback_by: str | Unset = UNSET
    caller_name: str | Unset = UNSET
    key_moment: InboxSnippet | Unset = UNSET
    model_id: UUID | Unset = UNSET
    outcome: CallAnalysisOutcome | Unset = UNSET
    quality: CallQuality | Unset = UNSET
    reason: str | Unset = UNSET
    sentiment: CallAnalysisSentiment | Unset = UNSET
    successful: bool | Unset = UNSET
    unanswered_question: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        callback_requested = self.callback_requested

        cost_micro = self.cost_micro

        created_at = self.created_at.isoformat()

        data = self.data.to_dict()

        summary = self.summary

        tokens = self.tokens

        callback_by = self.callback_by

        caller_name = self.caller_name

        key_moment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key_moment, Unset):
            key_moment = self.key_moment.to_dict()

        model_id: str | Unset = UNSET
        if not isinstance(self.model_id, Unset):
            model_id = str(self.model_id)

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome

        quality: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        reason = self.reason

        sentiment: str | Unset = UNSET
        if not isinstance(self.sentiment, Unset):
            sentiment = self.sentiment

        successful = self.successful

        unanswered_question = self.unanswered_question

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "call_id": call_id,
                "callback_requested": callback_requested,
                "cost_micro": cost_micro,
                "created_at": created_at,
                "data": data,
                "summary": summary,
                "tokens": tokens,
            }
        )
        if callback_by is not UNSET:
            field_dict["callback_by"] = callback_by
        if caller_name is not UNSET:
            field_dict["caller_name"] = caller_name
        if key_moment is not UNSET:
            field_dict["key_moment"] = key_moment
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if quality is not UNSET:
            field_dict["quality"] = quality
        if reason is not UNSET:
            field_dict["reason"] = reason
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment
        if successful is not UNSET:
            field_dict["successful"] = successful
        if unanswered_question is not UNSET:
            field_dict["unanswered_question"] = unanswered_question

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_analysis_data import CallAnalysisData
        from ..models.call_quality import CallQuality
        from ..models.inbox_snippet import InboxSnippet

        d = dict(src_dict)
        call_id = d.pop("call_id")

        callback_requested = d.pop("callback_requested")

        cost_micro = d.pop("cost_micro")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        data = CallAnalysisData.from_dict(d.pop("data"))

        summary = d.pop("summary")

        tokens = d.pop("tokens")

        callback_by = d.pop("callback_by", UNSET)

        caller_name = d.pop("caller_name", UNSET)

        _key_moment = d.pop("key_moment", UNSET)
        key_moment: InboxSnippet | Unset
        if isinstance(_key_moment, Unset):
            key_moment = UNSET
        else:
            key_moment = InboxSnippet.from_dict(_key_moment)

        _model_id = d.pop("model_id", UNSET)
        model_id: UUID | Unset
        if isinstance(_model_id, Unset):
            model_id = UNSET
        else:
            model_id = UUID(_model_id)

        _outcome = d.pop("outcome", UNSET)
        outcome: CallAnalysisOutcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = check_call_analysis_outcome(_outcome)

        _quality = d.pop("quality", UNSET)
        quality: CallQuality | Unset
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = CallQuality.from_dict(_quality)

        reason = d.pop("reason", UNSET)

        _sentiment = d.pop("sentiment", UNSET)
        sentiment: CallAnalysisSentiment | Unset
        if isinstance(_sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = check_call_analysis_sentiment(_sentiment)

        successful = d.pop("successful", UNSET)

        unanswered_question = d.pop("unanswered_question", UNSET)

        call_analysis = cls(
            call_id=call_id,
            callback_requested=callback_requested,
            cost_micro=cost_micro,
            created_at=created_at,
            data=data,
            summary=summary,
            tokens=tokens,
            callback_by=callback_by,
            caller_name=caller_name,
            key_moment=key_moment,
            model_id=model_id,
            outcome=outcome,
            quality=quality,
            reason=reason,
            sentiment=sentiment,
            successful=successful,
            unanswered_question=unanswered_question,
        )

        return call_analysis
