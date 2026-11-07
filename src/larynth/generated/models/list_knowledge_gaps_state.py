from typing import Literal

ListKnowledgeGapsState = Literal["answered", "dismissed", "open"]

LIST_KNOWLEDGE_GAPS_STATE_VALUES: set[ListKnowledgeGapsState] = {
    "answered",
    "dismissed",
    "open",
}


def check_list_knowledge_gaps_state(value: str) -> ListKnowledgeGapsState:
    if value in LIST_KNOWLEDGE_GAPS_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_KNOWLEDGE_GAPS_STATE_VALUES!r}"
    )
