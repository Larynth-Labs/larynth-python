from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.assistant_draft_mode import AssistantDraftMode, check_assistant_draft_mode
from ..models.assistant_draft_transfer_fallback import (
    AssistantDraftTransferFallback,
    check_assistant_draft_transfer_fallback,
)
from ..models.assistant_draft_turn_preset import (
    AssistantDraftTurnPreset,
    check_assistant_draft_turn_preset,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_draft_language_voices import AssistantDraftLanguageVoices
    from ..models.assistant_draft_llm_params import AssistantDraftLlmParams
    from ..models.assistant_draft_s2s_params import AssistantDraftS2SParams
    from ..models.assistant_draft_stt_params import AssistantDraftSttParams
    from ..models.assistant_draft_tts_params import AssistantDraftTtsParams
    from ..models.assistant_tool import AssistantTool
    from ..models.call_handling import CallHandling
    from ..models.call_limits import CallLimits
    from ..models.disclosure_spec import DisclosureSpec
    from ..models.draft_warning import DraftWarning
    from ..models.guardrails_spec import GuardrailsSpec
    from ..models.interruption_profile import InterruptionProfile
    from ..models.latency_settings import LatencySettings
    from ..models.post_call_settings import PostCallSettings
    from ..models.turn_profile import TurnProfile
    from ..models.vocabulary import Vocabulary


T = TypeVar("T", bound="AssistantDraft")


@_attrs_define
class AssistantDraft:
    """
    Attributes:
        assistant_id (UUID):
        changed_sections (list[str]): basics, instructions, voice, model, knowledge, tools, call_handling, disclosures,
            guardrails, post_call, advanced
        created_at (datetime.datetime):
        created_by (str):
        greeting_text (str):
        id (UUID):
        language (str):
        mode (AssistantDraftMode):
        revision (int):
        system_prompt (str):
        updated_at (datetime.datetime):
        version (int):
        warnings (list[DraftWarning]):
        call_handling (CallHandling | Unset):
        call_limits (CallLimits | Unset):
        denoise (bool | Unset):
        disclosure (DisclosureSpec | Unset):
        fillers (list[str] | Unset):
        guardrails (GuardrailsSpec | Unset):
        interruption_profile (InterruptionProfile | Unset):
        knowledge_base_ids (list[str] | Unset): Knowledge bases the assistant can search with the search_knowledge tool;
            each must be ready when the version is published
        language_voices (AssistantDraftLanguageVoices | Unset): Voice id per languages_extra entry, on the same tts
            model; unset uses the main voice when it speaks the language
        languages_extra (list[str] | Unset): Languages the agent switches to when the caller speaks them; only languages
            the catalog marks switchable
        latency (LatencySettings | Unset):
        llm_fallback_model_ids (list[str] | Unset):
        llm_model_id (UUID | Unset): Required for cascade
        llm_params (AssistantDraftLlmParams | Unset):
        max_call_seconds (int | Unset):  Default: 1800.
        post_call (PostCallSettings | Unset):
        published_at (datetime.datetime | Unset):
        s2s_model_id (UUID | Unset): Required for s2s
        s2s_params (AssistantDraftS2SParams | Unset):
        stt_model_id (UUID | Unset): Required for cascade
        stt_params (AssistantDraftSttParams | Unset):
        tools (list[AssistantTool] | Unset):
        transfer_fallback (AssistantDraftTransferFallback | Unset): What happens when nobody picks up a transfer
        tts_model_id (UUID | Unset): Required for cascade
        tts_params (AssistantDraftTtsParams | Unset):
        tts_voice_id (UUID | Unset): Required for cascade
        turn_preset (AssistantDraftTurnPreset | Unset): Turn-taking preset from listTurnPresets; custom means
            turn_profile and interruption_profile hold the advanced values. Unset is balanced
        turn_profile (TurnProfile | Unset):
        updated_by_name (str | Unset):
        vocabulary (Vocabulary | Unset):
    """

    assistant_id: UUID
    changed_sections: list[str]
    created_at: datetime.datetime
    created_by: str
    greeting_text: str
    id: UUID
    language: str
    mode: AssistantDraftMode
    revision: int
    system_prompt: str
    updated_at: datetime.datetime
    version: int
    warnings: list[DraftWarning]
    call_handling: CallHandling | Unset = UNSET
    call_limits: CallLimits | Unset = UNSET
    denoise: bool | Unset = UNSET
    disclosure: DisclosureSpec | Unset = UNSET
    fillers: list[str] | Unset = UNSET
    guardrails: GuardrailsSpec | Unset = UNSET
    interruption_profile: InterruptionProfile | Unset = UNSET
    knowledge_base_ids: list[str] | Unset = UNSET
    language_voices: AssistantDraftLanguageVoices | Unset = UNSET
    languages_extra: list[str] | Unset = UNSET
    latency: LatencySettings | Unset = UNSET
    llm_fallback_model_ids: list[str] | Unset = UNSET
    llm_model_id: UUID | Unset = UNSET
    llm_params: AssistantDraftLlmParams | Unset = UNSET
    max_call_seconds: int | Unset = 1800
    post_call: PostCallSettings | Unset = UNSET
    published_at: datetime.datetime | Unset = UNSET
    s2s_model_id: UUID | Unset = UNSET
    s2s_params: AssistantDraftS2SParams | Unset = UNSET
    stt_model_id: UUID | Unset = UNSET
    stt_params: AssistantDraftSttParams | Unset = UNSET
    tools: list[AssistantTool] | Unset = UNSET
    transfer_fallback: AssistantDraftTransferFallback | Unset = UNSET
    tts_model_id: UUID | Unset = UNSET
    tts_params: AssistantDraftTtsParams | Unset = UNSET
    tts_voice_id: UUID | Unset = UNSET
    turn_preset: AssistantDraftTurnPreset | Unset = UNSET
    turn_profile: TurnProfile | Unset = UNSET
    updated_by_name: str | Unset = UNSET
    vocabulary: Vocabulary | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        changed_sections = self.changed_sections

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        greeting_text = self.greeting_text

        id = str(self.id)

        language = self.language

        mode: str = self.mode

        revision = self.revision

        system_prompt = self.system_prompt

        updated_at = self.updated_at.isoformat()

        version = self.version

        warnings = []
        for warnings_item_data in self.warnings:
            warnings_item = warnings_item_data.to_dict()
            warnings.append(warnings_item)

        call_handling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.call_handling, Unset):
            call_handling = self.call_handling.to_dict()

        call_limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.call_limits, Unset):
            call_limits = self.call_limits.to_dict()

        denoise = self.denoise

        disclosure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disclosure, Unset):
            disclosure = self.disclosure.to_dict()

        fillers: list[str] | Unset = UNSET
        if not isinstance(self.fillers, Unset):
            fillers = self.fillers

        guardrails: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guardrails, Unset):
            guardrails = self.guardrails.to_dict()

        interruption_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interruption_profile, Unset):
            interruption_profile = self.interruption_profile.to_dict()

        knowledge_base_ids: list[str] | Unset = UNSET
        if not isinstance(self.knowledge_base_ids, Unset):
            knowledge_base_ids = self.knowledge_base_ids

        language_voices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.language_voices, Unset):
            language_voices = self.language_voices.to_dict()

        languages_extra: list[str] | Unset = UNSET
        if not isinstance(self.languages_extra, Unset):
            languages_extra = self.languages_extra

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

        transfer_fallback: str | Unset = UNSET
        if not isinstance(self.transfer_fallback, Unset):
            transfer_fallback = self.transfer_fallback

        tts_model_id: str | Unset = UNSET
        if not isinstance(self.tts_model_id, Unset):
            tts_model_id = str(self.tts_model_id)

        tts_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tts_params, Unset):
            tts_params = self.tts_params.to_dict()

        tts_voice_id: str | Unset = UNSET
        if not isinstance(self.tts_voice_id, Unset):
            tts_voice_id = str(self.tts_voice_id)

        turn_preset: str | Unset = UNSET
        if not isinstance(self.turn_preset, Unset):
            turn_preset = self.turn_preset

        turn_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.turn_profile, Unset):
            turn_profile = self.turn_profile.to_dict()

        updated_by_name = self.updated_by_name

        vocabulary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vocabulary, Unset):
            vocabulary = self.vocabulary.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "changed_sections": changed_sections,
                "created_at": created_at,
                "created_by": created_by,
                "greeting_text": greeting_text,
                "id": id,
                "language": language,
                "mode": mode,
                "revision": revision,
                "system_prompt": system_prompt,
                "updated_at": updated_at,
                "version": version,
                "warnings": warnings,
            }
        )
        if call_handling is not UNSET:
            field_dict["call_handling"] = call_handling
        if call_limits is not UNSET:
            field_dict["call_limits"] = call_limits
        if denoise is not UNSET:
            field_dict["denoise"] = denoise
        if disclosure is not UNSET:
            field_dict["disclosure"] = disclosure
        if fillers is not UNSET:
            field_dict["fillers"] = fillers
        if guardrails is not UNSET:
            field_dict["guardrails"] = guardrails
        if interruption_profile is not UNSET:
            field_dict["interruption_profile"] = interruption_profile
        if knowledge_base_ids is not UNSET:
            field_dict["knowledge_base_ids"] = knowledge_base_ids
        if language_voices is not UNSET:
            field_dict["language_voices"] = language_voices
        if languages_extra is not UNSET:
            field_dict["languages_extra"] = languages_extra
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
        if transfer_fallback is not UNSET:
            field_dict["transfer_fallback"] = transfer_fallback
        if tts_model_id is not UNSET:
            field_dict["tts_model_id"] = tts_model_id
        if tts_params is not UNSET:
            field_dict["tts_params"] = tts_params
        if tts_voice_id is not UNSET:
            field_dict["tts_voice_id"] = tts_voice_id
        if turn_preset is not UNSET:
            field_dict["turn_preset"] = turn_preset
        if turn_profile is not UNSET:
            field_dict["turn_profile"] = turn_profile
        if updated_by_name is not UNSET:
            field_dict["updated_by_name"] = updated_by_name
        if vocabulary is not UNSET:
            field_dict["vocabulary"] = vocabulary

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assistant_draft_language_voices import (
            AssistantDraftLanguageVoices,
        )
        from ..models.assistant_draft_llm_params import AssistantDraftLlmParams
        from ..models.assistant_draft_s2s_params import AssistantDraftS2SParams
        from ..models.assistant_draft_stt_params import AssistantDraftSttParams
        from ..models.assistant_draft_tts_params import AssistantDraftTtsParams
        from ..models.assistant_tool import AssistantTool
        from ..models.call_handling import CallHandling
        from ..models.call_limits import CallLimits
        from ..models.disclosure_spec import DisclosureSpec
        from ..models.draft_warning import DraftWarning
        from ..models.guardrails_spec import GuardrailsSpec
        from ..models.interruption_profile import InterruptionProfile
        from ..models.latency_settings import LatencySettings
        from ..models.post_call_settings import PostCallSettings
        from ..models.turn_profile import TurnProfile
        from ..models.vocabulary import Vocabulary

        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        changed_sections = cast(list[str], d.pop("changed_sections"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by = d.pop("created_by")

        greeting_text = d.pop("greeting_text")

        id = UUID(d.pop("id"))

        language = d.pop("language")

        mode = check_assistant_draft_mode(d.pop("mode"))

        revision = d.pop("revision")

        system_prompt = d.pop("system_prompt")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        warnings = []
        _warnings = d.pop("warnings")
        for warnings_item_data in _warnings:
            warnings_item = DraftWarning.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        _call_handling = d.pop("call_handling", UNSET)
        call_handling: CallHandling | Unset
        if isinstance(_call_handling, Unset):
            call_handling = UNSET
        else:
            call_handling = CallHandling.from_dict(_call_handling)

        _call_limits = d.pop("call_limits", UNSET)
        call_limits: CallLimits | Unset
        if isinstance(_call_limits, Unset):
            call_limits = UNSET
        else:
            call_limits = CallLimits.from_dict(_call_limits)

        denoise = d.pop("denoise", UNSET)

        _disclosure = d.pop("disclosure", UNSET)
        disclosure: DisclosureSpec | Unset
        if isinstance(_disclosure, Unset):
            disclosure = UNSET
        else:
            disclosure = DisclosureSpec.from_dict(_disclosure)

        fillers = cast(list[str], d.pop("fillers", UNSET))

        _guardrails = d.pop("guardrails", UNSET)
        guardrails: GuardrailsSpec | Unset
        if isinstance(_guardrails, Unset):
            guardrails = UNSET
        else:
            guardrails = GuardrailsSpec.from_dict(_guardrails)

        _interruption_profile = d.pop("interruption_profile", UNSET)
        interruption_profile: InterruptionProfile | Unset
        if isinstance(_interruption_profile, Unset):
            interruption_profile = UNSET
        else:
            interruption_profile = InterruptionProfile.from_dict(_interruption_profile)

        knowledge_base_ids = cast(list[str], d.pop("knowledge_base_ids", UNSET))

        _language_voices = d.pop("language_voices", UNSET)
        language_voices: AssistantDraftLanguageVoices | Unset
        if isinstance(_language_voices, Unset):
            language_voices = UNSET
        else:
            language_voices = AssistantDraftLanguageVoices.from_dict(_language_voices)

        languages_extra = cast(list[str], d.pop("languages_extra", UNSET))

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
        llm_params: AssistantDraftLlmParams | Unset
        if isinstance(_llm_params, Unset):
            llm_params = UNSET
        else:
            llm_params = AssistantDraftLlmParams.from_dict(_llm_params)

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
        s2s_params: AssistantDraftS2SParams | Unset
        if isinstance(_s2s_params, Unset):
            s2s_params = UNSET
        else:
            s2s_params = AssistantDraftS2SParams.from_dict(_s2s_params)

        _stt_model_id = d.pop("stt_model_id", UNSET)
        stt_model_id: UUID | Unset
        if isinstance(_stt_model_id, Unset):
            stt_model_id = UNSET
        else:
            stt_model_id = UUID(_stt_model_id)

        _stt_params = d.pop("stt_params", UNSET)
        stt_params: AssistantDraftSttParams | Unset
        if isinstance(_stt_params, Unset):
            stt_params = UNSET
        else:
            stt_params = AssistantDraftSttParams.from_dict(_stt_params)

        _tools = d.pop("tools", UNSET)
        tools: list[AssistantTool] | Unset = UNSET
        if _tools is not UNSET:
            tools = []
            for tools_item_data in _tools:
                tools_item = AssistantTool.from_dict(tools_item_data)

                tools.append(tools_item)

        _transfer_fallback = d.pop("transfer_fallback", UNSET)
        transfer_fallback: AssistantDraftTransferFallback | Unset
        if isinstance(_transfer_fallback, Unset):
            transfer_fallback = UNSET
        else:
            transfer_fallback = check_assistant_draft_transfer_fallback(
                _transfer_fallback
            )

        _tts_model_id = d.pop("tts_model_id", UNSET)
        tts_model_id: UUID | Unset
        if isinstance(_tts_model_id, Unset):
            tts_model_id = UNSET
        else:
            tts_model_id = UUID(_tts_model_id)

        _tts_params = d.pop("tts_params", UNSET)
        tts_params: AssistantDraftTtsParams | Unset
        if isinstance(_tts_params, Unset):
            tts_params = UNSET
        else:
            tts_params = AssistantDraftTtsParams.from_dict(_tts_params)

        _tts_voice_id = d.pop("tts_voice_id", UNSET)
        tts_voice_id: UUID | Unset
        if isinstance(_tts_voice_id, Unset):
            tts_voice_id = UNSET
        else:
            tts_voice_id = UUID(_tts_voice_id)

        _turn_preset = d.pop("turn_preset", UNSET)
        turn_preset: AssistantDraftTurnPreset | Unset
        if isinstance(_turn_preset, Unset):
            turn_preset = UNSET
        else:
            turn_preset = check_assistant_draft_turn_preset(_turn_preset)

        _turn_profile = d.pop("turn_profile", UNSET)
        turn_profile: TurnProfile | Unset
        if isinstance(_turn_profile, Unset):
            turn_profile = UNSET
        else:
            turn_profile = TurnProfile.from_dict(_turn_profile)

        updated_by_name = d.pop("updated_by_name", UNSET)

        _vocabulary = d.pop("vocabulary", UNSET)
        vocabulary: Vocabulary | Unset
        if isinstance(_vocabulary, Unset):
            vocabulary = UNSET
        else:
            vocabulary = Vocabulary.from_dict(_vocabulary)

        assistant_draft = cls(
            assistant_id=assistant_id,
            changed_sections=changed_sections,
            created_at=created_at,
            created_by=created_by,
            greeting_text=greeting_text,
            id=id,
            language=language,
            mode=mode,
            revision=revision,
            system_prompt=system_prompt,
            updated_at=updated_at,
            version=version,
            warnings=warnings,
            call_handling=call_handling,
            call_limits=call_limits,
            denoise=denoise,
            disclosure=disclosure,
            fillers=fillers,
            guardrails=guardrails,
            interruption_profile=interruption_profile,
            knowledge_base_ids=knowledge_base_ids,
            language_voices=language_voices,
            languages_extra=languages_extra,
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
            transfer_fallback=transfer_fallback,
            tts_model_id=tts_model_id,
            tts_params=tts_params,
            tts_voice_id=tts_voice_id,
            turn_preset=turn_preset,
            turn_profile=turn_profile,
            updated_by_name=updated_by_name,
            vocabulary=vocabulary,
        )

        return assistant_draft
