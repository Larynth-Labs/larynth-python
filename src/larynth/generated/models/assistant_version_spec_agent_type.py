from typing import Literal

AssistantVersionSpecAgentType = Literal["flow", "single_prompt"]

ASSISTANT_VERSION_SPEC_AGENT_TYPE_VALUES: set[AssistantVersionSpecAgentType] = {
    "flow",
    "single_prompt",
}


def check_assistant_version_spec_agent_type(
    value: str,
) -> AssistantVersionSpecAgentType:
    if value in ASSISTANT_VERSION_SPEC_AGENT_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_VERSION_SPEC_AGENT_TYPE_VALUES!r}"
    )
