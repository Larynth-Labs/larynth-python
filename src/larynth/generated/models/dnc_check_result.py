from typing import Literal

DncCheckResult = Literal["clear", "listed", "not_configured"]

DNC_CHECK_RESULT_VALUES: set[DncCheckResult] = {
    "clear",
    "listed",
    "not_configured",
}


def check_dnc_check_result(value: str) -> DncCheckResult:
    if value in DNC_CHECK_RESULT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DNC_CHECK_RESULT_VALUES!r}"
    )
