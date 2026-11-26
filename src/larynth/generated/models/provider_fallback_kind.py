from typing import Literal

ProviderFallbackKind = Literal["llm", "stt", "tts"]

PROVIDER_FALLBACK_KIND_VALUES: set[ProviderFallbackKind] = {
    "llm",
    "stt",
    "tts",
}


def check_provider_fallback_kind(value: str) -> ProviderFallbackKind:
    if value in PROVIDER_FALLBACK_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_FALLBACK_KIND_VALUES!r}"
    )
