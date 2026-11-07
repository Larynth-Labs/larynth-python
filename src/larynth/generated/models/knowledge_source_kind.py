from typing import Literal

KnowledgeSourceKind = Literal["faq", "file", "website"]

KNOWLEDGE_SOURCE_KIND_VALUES: set[KnowledgeSourceKind] = {
    "faq",
    "file",
    "website",
}


def check_knowledge_source_kind(value: str) -> KnowledgeSourceKind:
    if value in KNOWLEDGE_SOURCE_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {KNOWLEDGE_SOURCE_KIND_VALUES!r}"
    )
