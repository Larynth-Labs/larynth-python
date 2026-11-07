from typing import Literal

KnowledgeFaqSourceStatus = Literal["failed", "pending", "processing", "ready"]

KNOWLEDGE_FAQ_SOURCE_STATUS_VALUES: set[KnowledgeFaqSourceStatus] = {
    "failed",
    "pending",
    "processing",
    "ready",
}


def check_knowledge_faq_source_status(value: str) -> KnowledgeFaqSourceStatus:
    if value in KNOWLEDGE_FAQ_SOURCE_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {KNOWLEDGE_FAQ_SOURCE_STATUS_VALUES!r}"
    )
