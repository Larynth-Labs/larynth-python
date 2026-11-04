from typing import Literal

ProblemUsedByItem = Literal["auto_top_up", "bundle"]

PROBLEM_USED_BY_ITEM_VALUES: set[ProblemUsedByItem] = {
    "auto_top_up",
    "bundle",
}


def check_problem_used_by_item(value: str) -> ProblemUsedByItem:
    if value in PROBLEM_USED_BY_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROBLEM_USED_BY_ITEM_VALUES!r}"
    )
