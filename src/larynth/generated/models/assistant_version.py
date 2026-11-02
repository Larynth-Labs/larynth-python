from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.assistant_version_mode import (
    AssistantVersionMode,
    check_assistant_version_mode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_tool import AssistantTool
    from ..models.assistant_version_llm_params import AssistantVersionLlmParams
    from ..models.assistant_version_s2s_params import AssistantVersionS2SParams
    from ..models.assistant_version_stt_params import AssistantVersionSttParams
    from ..models.assistant_version_tts_params import AssistantVersionTtsParams
    from ..models.interruption_profile import InterruptionProfile
    from ..models.latency_settings import LatencySettings
    from ..models.post_call_settings import PostCallSettings
    from ..models.turn_profile import TurnProfile


T = TypeVar("T", bound="AssistantVersion")


@_attrs_define
class AssistantVersion:
    """
    Attributes:
        assistant_id (UUID):
        created_at (datetime.datetime):
        created_by (str):
        greeting_text (str):
        id (UUID):
        language (str):
        mode (AssistantVersionMode):
        system_prompt (str):
        version (int):
        denoise (bool | Unset):
        fillers (list[str] | Unset):
        interruption_profile (InterruptionProfile | Unset):
        knowledge_base_ids (list[str] | Unset): Knowledge bases the assistant can search with the search_knowledge tool;
            each must be ready when the version is published
        latency (LatencySettings | Unset):
        llm_fallback_model_ids (list[str] | Unset):
        llm_model_id (UUID | Unset): Required for cascade
        llm_params (AssistantVersionLlmParams | Unset):
        max_call_seconds (int | Unset):  Default: 1800.
        post_call (PostCallSettings | Unset):
        published_at (datetime.datetime | Unset):
        s2s_model_id (UUID | Unset): Required for s2s
        s2s_params (AssistantVersionS2SParams | Unset):
        stt_model_id (UUID | Unset): Required for cascade
        stt_params (AssistantVersionSttParams | Unset):
        tools (list[AssistantTool] | Unset):
        tts_model_id (UUID | Unset): Required for cascade
        tts_params (AssistantVersionTtsParams | Unset):
        tts_voice_id (UUID | Unset): Required for cascade
        turn_profile (TurnProfile | Unset):
    """

    assistant_id: UUID
    created_at: datetime.datetime
    created_by: str
    greeting_text: str
    id: UUID
    language: str
    mode: AssistantVersionMode
    system_prompt: str
    version: int
    denoise: bool | Unset = UNSET
    fillers: list[str] | Unset = UNSET
    interruption_profile: InterruptionProfile | Unset = UNSET
    knowledge_base_ids: list[str] | Unset = UNSET
    latency: LatencySettings | Unset = UNSET
    llm_fallback_model_ids: list[str] | Unset = UNSET
    llm_model_id: UUID | Unset = UNSET
    llm_params: AssistantVersionLlmParams | Unset = UNSET
    max_call_seconds: int | Unset = 1800
    post_call: PostCallSettings | Unset = UNSET
    published_at: datetime.datetime | Unset = UNSET
    s2s_model_id: UUID | Unset = UNSET
    s2s_params: AssistantVersionS2SParams | Unset = UNSET
    stt_model_id: UUID | Unset = UNSET
    stt_params: AssistantVersionSttParams | Unset = UNSET
    tools: list[AssistantTool] | Unset = UNSET
    tts_model_id: UUID | Unset = UNSET
    tts_params: AssistantVersionTtsParams | Unset = UNSET
    tts_voice_id: UUID | Unset = UNSET
    turn_profile: TurnProfile | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        greeting_text = self.greeting_text

        id = str(self.id)

        language = self.language

        mode: str = self.mode

        system_prompt = self.system_prompt

        version = self.version

        denoise = self.denoise

        fillers: list[str] | Unset = UNSET
        if not isinstance(self.fillers, Unset):
            fillers = self.fillers

        interruption_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interruption_profile, Unset):
            interruption_profile = self.interruption_profile.to_dict()

        knowledge_base_ids: list[str] | Unset = UNSET
        if not isinstance(self.knowledge_base_ids, Unset):
            knowledge_base_ids = self.knowledge_base_ids

        latency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latency, Unset):
            latency = self.latency.to_dict()

        llm_fallback_model_ids: list[str] | Unset = UNSET
        if not isinstance(self.llm_fallback_model_ids, Unset):
            llm_fallback_model_ids = self.llm_fallback_model_ids

        llm_model_id: str | Unset = UNSET
        if not isinstance(self.llm_model_id, Unset):
            llm_model_id = str(self.llm_model_id)

        llm_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.llm_params, Unset):
            llm_params = self.llm_params.to_dict()

        max_call_seconds = self.max_call_seconds

        post_call: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post_call, Unset):
            post_call = self.post_call.to_dict()

        published_at: str | Unset = UNSET
        if not isinstance(self.published_at, Unset):
            published_at = self.published_at.isoformat()

        s2s_model_id: str | Unset = UNSET
        if not isinstance(self.s2s_model_id, Unset):
            s2s_model_id = str(self.s2s_model_id)

        s2s_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.s2s_params, Unset):
            s2s_params = self.s2s_params.to_dict()

        stt_model_id: str | Unset = UNSET
        if not isinstance(self.stt_model_id, Unset):
            stt_model_id = str(self.stt_model_id)

        stt_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stt_params, Unset):
            stt_params = self.stt_params.to_dict()

        tools: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tools, Unset):
            tools = []
            for tools_item_data in self.tools:
                tools_item = tools_item_data.to_dict()
                tools.append(tools_item)

        tts_model_id: str | Unset = UNSET
        if not isinstance(self.tts_model_id, Unset):
            tts_model_id = str(self.tts_model_id)

        tts_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tts_params, Unset):
            tts_params = self.tts_params.to_dict()

        tts_voice_id: str | Unset = UNSET
        if not isinstance(self.tts_voice_id, Unset):
            tts_voice_id = str(self.tts_voice_id)

        turn_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.turn_profile, Unset):
            turn_profile = self.turn_profile.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "created_at": created_at,
                "created_by": created_by,
                "greeting_text": greeting_text,
                "id": id,
                "language": language,
                "mode": mode,
                "system_prompt": system_prompt,
                "version": version,
            }
        )
        if denoise is not UNSET:
            field_dict["denoise"] = denoise
        if fillers is not UNSET:
            field_dict["fillers"] = fillers
        if interruption_profile is not UNSET:
            field_dict["interruption_profile"] = interruption_profile
        if knowledge_base_ids is not UNSET:
            field_dict["knowledge_base_ids"] = knowledge_base_ids
        if latency is not UNSET:
            field_dict["latency"] = latency
        if llm_fallback_model_ids is not UNSET:
            field_dict["llm_fallback_model_ids"] = llm_fallback_model_ids
        if llm_model_id is not UNSET:
            field_dict["llm_model_id"] = llm_model_id
        if llm_params is not UNSET:
            field_dict["llm_params"] = llm_params
        if max_call_seconds is not UNSET:
            field_dict["max_call_seconds"] = max_call_seconds
        if post_call is not UNSET:
            field_dict["post_call"] = post_call
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if s2s_model_id is not UNSET:
            field_dict["s2s_model_id"] = s2s_model_id
        if s2s_params is not UNSET:
            field_dict["s2s_params"] = s2s_params
        if stt_model_id is not UNSET:
            field_dict["stt_model_id"] = stt_model_id
        if stt_params is not UNSET:
            field_dict["stt_params"] = stt_params
        if tools is not UNSET:
            field_dict["tools"] = tools
        if tts_model_id is not UNSET:
            field_dict["tts_model_id"] = tts_model_id
        if tts_params is not UNSET:
            field_dict["tts_params"] = tts_params
        if tts_voice_id is not UNSET:
            field_dict["tts_voice_id"] = tts_voice_id
        if turn_profile is not UNSET:
            field_dict["turn_profile"] = turn_profile

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assistant_tool import AssistantTool
        from ..models.assistant_version_llm_params import AssistantVersionLlmParams
        from ..models.assistant_version_s2s_params import AssistantVersionS2SParams
        from ..models.assistant_version_stt_params import AssistantVersionSttParams
        from ..models.assistant_version_tts_params import AssistantVersionTtsParams
        from ..models.interruption_profile import InterruptionProfile
        from ..models.latency_settings import LatencySettings
        from ..models.post_call_settings import PostCallSettings
        from ..models.turn_profile import TurnProfile

        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by = d.pop("created_by")

        greeting_text = d.pop("greeting_text")

        id = UUID(d.pop("id"))

        language = d.pop("language")

        mode = check_assistant_version_mode(d.pop("mode"))

        system_prompt = d.pop("system_prompt")

        version = d.pop("version")

        denoise = d.pop("denoise", UNSET)

        fillers = cast(list[str], d.pop("fillers", UNSET))

        _interruption_profile = d.pop("interruption_profile", UNSET)
        interruption_profile: InterruptionProfile | Unset
        if isinstance(_interruption_profile, Unset):
            interruption_profile = UNSET
        else:
            interruption_profile = InterruptionProfile.from_dict(_interruption_profile)

        knowledge_base_ids = cast(list[str], d.pop("knowledge_base_ids", UNSET))

        _latency = d.pop("latency", UNSET)
        latency: LatencySettings | Unset
        if isinstance(_latency, Unset):
            latency = UNSET
        else:
            latency = LatencySettings.from_dict(_latency)

        llm_fallback_model_ids = cast(list[str], d.pop("llm_fallback_model_ids", UNSET))

        _llm_model_id = d.pop("llm_model_id", UNSET)
        llm_model_id: UUID | Unset
        if isinstance(_llm_model_id, Unset):
            llm_model_id = UNSET
        else:
            llm_model_id = UUID(_llm_model_id)

        _llm_params = d.pop("llm_params", UNSET)
        llm_params: AssistantVersionLlmParams | Unset
        if isinstance(_llm_params, Unset):
            llm_params = UNSET
        else:
            llm_params = AssistantVersionLlmParams.from_dict(_llm_params)

        max_call_seconds = d.pop("max_call_seconds", UNSET)

        _post_call = d.pop("post_call", UNSET)
        post_call: PostCallSettings | Unset
        if isinstance(_post_call, Unset):
            post_call = UNSET
        else:
            post_call = PostCallSettings.from_dict(_post_call)

        _published_at = d.pop("published_at", UNSET)
        published_at: datetime.datetime | Unset
        if isinstance(_published_at, Unset):
            published_at = UNSET
        else:
            published_at = datetime.datetime.fromisoformat(_published_at)

        _s2s_model_id = d.pop("s2s_model_id", UNSET)
        s2s_model_id: UUID | Unset
        if isinstance(_s2s_model_id, Unset):
            s2s_model_id = UNSET
        else:
            s2s_model_id = UUID(_s2s_model_id)

        _s2s_params = d.pop("s2s_params", UNSET)
        s2s_params: AssistantVersionS2SParams | Unset
        if isinstance(_s2s_params, Unset):
            s2s_params = UNSET
        else:
            s2s_params = AssistantVersionS2SParams.from_dict(_s2s_params)

        _stt_model_id = d.pop("stt_model_id", UNSET)
        stt_model_id: UUID | Unset
        if isinstance(_stt_model_id, Unset):
            stt_model_id = UNSET
        else:
            stt_model_id = UUID(_stt_model_id)

        _stt_params = d.pop("stt_params", UNSET)
        stt_params: AssistantVersionSttParams | Unset
        if isinstance(_stt_params, Unset):
            stt_params = UNSET
        else:
            stt_params = AssistantVersionSttParams.from_dict(_stt_params)

        _tools = d.pop("tools", UNSET)
        tools: list[AssistantTool] | Unset = UNSET
        if _tools is not UNSET:
            tools = []
            for tools_item_data in _tools:
                tools_item = AssistantTool.from_dict(tools_item_data)

                tools.append(tools_item)

        _tts_model_id = d.pop("tts_model_id", UNSET)
        tts_model_id: UUID | Unset
        if isinstance(_tts_model_id, Unset):
            tts_model_id = UNSET
        else:
            tts_model_id = UUID(_tts_model_id)

        _tts_params = d.pop("tts_params", UNSET)
        tts_params: AssistantVersionTtsParams | Unset
        if isinstance(_tts_params, Unset):
            tts_params = UNSET
        else:
            tts_params = AssistantVersionTtsParams.from_dict(_tts_params)

        _tts_voice_id = d.pop("tts_voice_id", UNSET)
        tts_voice_id: UUID | Unset
        if isinstance(_tts_voice_id, Unset):
            tts_voice_id = UNSET
        else:
            tts_voice_id = UUID(_tts_voice_id)

        _turn_profile = d.pop("turn_profile", UNSET)
        turn_profile: TurnProfile | Unset
        if isinstance(_turn_profile, Unset):
            turn_profile = UNSET
        else:
            turn_profile = TurnProfile.from_dict(_turn_profile)

        assistant_version = cls(
            assistant_id=assistant_id,
            created_at=created_at,
            created_by=created_by,
            greeting_text=greeting_text,
            id=id,
            language=language,
            mode=mode,
            system_prompt=system_prompt,
            version=version,
            denoise=denoise,
            fillers=fillers,
            interruption_profile=interruption_profile,
            knowledge_base_ids=knowledge_base_ids,
            latency=latency,
            llm_fallback_model_ids=llm_fallback_model_ids,
            llm_model_id=llm_model_id,
            llm_params=llm_params,
            max_call_seconds=max_call_seconds,
            post_call=post_call,
            published_at=published_at,
            s2s_model_id=s2s_model_id,
            s2s_params=s2s_params,
            stt_model_id=stt_model_id,
            stt_params=stt_params,
            tools=tools,
            tts_model_id=tts_model_id,
            tts_params=tts_params,
            tts_voice_id=tts_voice_id,
            turn_profile=turn_profile,
        )

        return assistant_version
