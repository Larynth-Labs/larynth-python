from typing import Literal

KnowledgeBaseStatus = Literal["building", "empty", "failed", "ready"]

KNOWLEDGE_BASE_STATUS_VALUES: set[KnowledgeBaseStatus] = {
    "building",
    "empty",
    "failed",
    "ready",
}


def check_knowledge_base_status(value: str) -> KnowledgeBaseStatus:
    if value in KNOWLEDGE_BASE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {KNOWLEDGE_BASE_STATUS_VALUES!r}"
    )
