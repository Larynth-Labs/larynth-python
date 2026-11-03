from typing import Literal

AssistantPublishKind = Literal["publish", "rollback"]

ASSISTANT_PUBLISH_KIND_VALUES: set[AssistantPublishKind] = {
    "publish",
    "rollback",
}


def check_assistant_publish_kind(value: str) -> AssistantPublishKind:
    if value in ASSISTANT_PUBLISH_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_PUBLISH_KIND_VALUES!r}"
    )
