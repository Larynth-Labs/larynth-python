from typing import Literal

KnowledgeGapState = Literal["answered", "dismissed", "open"]

KNOWLEDGE_GAP_STATE_VALUES: set[KnowledgeGapState] = {
    "answered",
    "dismissed",
    "open",
}


def check_knowledge_gap_state(value: str) -> KnowledgeGapState:
    if value in KNOWLEDGE_GAP_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {KNOWLEDGE_GAP_STATE_VALUES!r}"
    )
