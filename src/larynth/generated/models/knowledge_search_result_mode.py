from typing import Literal

KnowledgeSearchResultMode = Literal["hybrid", "lexical"]

KNOWLEDGE_SEARCH_RESULT_MODE_VALUES: set[KnowledgeSearchResultMode] = {
    "hybrid",
    "lexical",
}


def check_knowledge_search_result_mode(value: str) -> KnowledgeSearchResultMode:
    if value in KNOWLEDGE_SEARCH_RESULT_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {KNOWLEDGE_SEARCH_RESULT_MODE_VALUES!r}"
    )
