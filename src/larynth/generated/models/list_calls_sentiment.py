from typing import Literal

ListCallsSentiment = Literal["negative", "neutral", "positive"]

LIST_CALLS_SENTIMENT_VALUES: set[ListCallsSentiment] = {
    "negative",
    "neutral",
    "positive",
}


def check_list_calls_sentiment(value: str) -> ListCallsSentiment:
    if value in LIST_CALLS_SENTIMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CALLS_SENTIMENT_VALUES!r}"
    )
