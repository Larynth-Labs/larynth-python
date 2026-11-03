from typing import Literal

GetCallsSummarySentiment = Literal["negative", "neutral", "positive"]

GET_CALLS_SUMMARY_SENTIMENT_VALUES: set[GetCallsSummarySentiment] = {
    "negative",
    "neutral",
    "positive",
}


def check_get_calls_summary_sentiment(value: str) -> GetCallsSummarySentiment:
    if value in GET_CALLS_SUMMARY_SENTIMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CALLS_SUMMARY_SENTIMENT_VALUES!r}"
    )
