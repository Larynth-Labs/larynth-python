from typing import Literal

KnowledgeFaqSourceKind = Literal["faq", "file", "website"]

KNOWLEDGE_FAQ_SOURCE_KIND_VALUES: set[KnowledgeFaqSourceKind] = {
    "faq",
    "file",
    "website",
}


def check_knowledge_faq_source_kind(value: str) -> KnowledgeFaqSourceKind:
    if value in KNOWLEDGE_FAQ_SOURCE_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {KNOWLEDGE_FAQ_SOURCE_KIND_VALUES!r}"
    )
