from typing import Literal

AssistantVersionAgentType = Literal["flow", "single_prompt"]

ASSISTANT_VERSION_AGENT_TYPE_VALUES: set[AssistantVersionAgentType] = {
    "flow",
    "single_prompt",
}


def check_assistant_version_agent_type(value: str) -> AssistantVersionAgentType:
    if value in ASSISTANT_VERSION_AGENT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_VERSION_AGENT_TYPE_VALUES!r}"
    )
