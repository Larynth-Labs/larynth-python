from typing import Literal

ProblemPeriod = Literal["daily", "monthly"]

PROBLEM_PERIOD_VALUES: set[ProblemPeriod] = {
    "daily",
    "monthly",
}


def check_problem_period(value: str) -> ProblemPeriod:
    if value in PROBLEM_PERIOD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROBLEM_PERIOD_VALUES!r}"
    )
