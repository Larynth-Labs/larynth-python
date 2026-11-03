from typing import Literal

CallSentiment = Literal["negative", "neutral", "positive"]

CALL_SENTIMENT_VALUES: set[CallSentiment] = {
    "negative",
    "neutral",
    "positive",
}


def check_call_sentiment(value: str) -> CallSentiment:
    if value in CALL_SENTIMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_SENTIMENT_VALUES!r}"
    )
