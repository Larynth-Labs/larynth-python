from typing import Literal

DiffLineOp = Literal["add", "del", "elided", "equal"]

DIFF_LINE_OP_VALUES: set[DiffLineOp] = {
    "add",
    "del",
    "elided",
    "equal",
}


def check_diff_line_op(value: str) -> DiffLineOp:
    if value in DIFF_LINE_OP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DIFF_LINE_OP_VALUES!r}"
    )
