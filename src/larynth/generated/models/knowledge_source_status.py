from typing import Literal

KnowledgeSourceStatus = Literal["failed", "pending", "processing", "ready"]

KNOWLEDGE_SOURCE_STATUS_VALUES: set[KnowledgeSourceStatus] = {
    "failed",
    "pending",
    "processing",
    "ready",
}


def check_knowledge_source_status(value: str) -> KnowledgeSourceStatus:
    if value in KNOWLEDGE_SOURCE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {KNOWLEDGE_SOURCE_STATUS_VALUES!r}"
    )
