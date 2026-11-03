from typing import Literal

ListCallsWebTests = Literal["exclude", "include", "only"]

LIST_CALLS_WEB_TESTS_VALUES: set[ListCallsWebTests] = {
    "exclude",
    "include",
    "only",
}


def check_list_calls_web_tests(value: str) -> ListCallsWebTests:
    if value in LIST_CALLS_WEB_TESTS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CALLS_WEB_TESTS_VALUES!r}"
    )
