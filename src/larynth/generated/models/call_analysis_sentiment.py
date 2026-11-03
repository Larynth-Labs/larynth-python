from typing import Literal

CallAnalysisSentiment = Literal["negative", "neutral", "positive"]

CALL_ANALYSIS_SENTIMENT_VALUES: set[CallAnalysisSentiment] = {
    "negative",
    "neutral",
    "positive",
}


def check_call_analysis_sentiment(value: str) -> CallAnalysisSentiment:
    if value in CALL_ANALYSIS_SENTIMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_ANALYSIS_SENTIMENT_VALUES!r}"
    )
