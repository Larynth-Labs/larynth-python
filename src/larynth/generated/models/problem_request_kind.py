from typing import Literal

ProblemRequestKind = Literal["campaign_launch", "number_purchase"]

PROBLEM_REQUEST_KIND_VALUES: set[ProblemRequestKind] = {
    "campaign_launch",
    "number_purchase",
}


def check_problem_request_kind(value: str) -> ProblemRequestKind:
    if value in PROBLEM_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROBLEM_REQUEST_KIND_VALUES!r}"
    )
