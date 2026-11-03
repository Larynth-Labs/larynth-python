from typing import Literal

GetCallsSummaryWebTests = Literal["exclude", "include", "only"]

GET_CALLS_SUMMARY_WEB_TESTS_VALUES: set[GetCallsSummaryWebTests] = {
    "exclude",
    "include",
    "only",
}


def check_get_calls_summary_web_tests(value: str) -> GetCallsSummaryWebTests:
    if value in GET_CALLS_SUMMARY_WEB_TESTS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CALLS_SUMMARY_WEB_TESTS_VALUES!r}"
    )
