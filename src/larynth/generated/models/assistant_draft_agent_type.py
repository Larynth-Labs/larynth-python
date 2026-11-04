from typing import Literal

AssistantDraftAgentType = Literal["flow", "single_prompt"]

ASSISTANT_DRAFT_AGENT_TYPE_VALUES: set[AssistantDraftAgentType] = {
    "flow",
    "single_prompt",
}


def check_assistant_draft_agent_type(value: str) -> AssistantDraftAgentType:
    if value in ASSISTANT_DRAFT_AGENT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_DRAFT_AGENT_TYPE_VALUES!r}"
    )
