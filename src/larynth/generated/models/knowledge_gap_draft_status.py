from typing import Literal

KnowledgeGapDraftStatus = Literal[
    "blocked_clinical", "blocked_unverified", "drafted", "none"
]

KNOWLEDGE_GAP_DRAFT_STATUS_VALUES: set[KnowledgeGapDraftStatus] = {
    "blocked_clinical",
    "blocked_unverified",
    "drafted",
    "none",
}


def check_knowledge_gap_draft_status(value: str) -> KnowledgeGapDraftStatus:
    if value in KNOWLEDGE_GAP_DRAFT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {KNOWLEDGE_GAP_DRAFT_STATUS_VALUES!r}"
    )
