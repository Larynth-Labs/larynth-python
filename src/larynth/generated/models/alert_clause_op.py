from typing import Literal

AlertClauseOp = Literal[
    "contains",
    "contains_any",
    "eq",
    "exists",
    "gt",
    "in",
    "lt",
    "ne",
    "not_exists",
    "not_in",
]

ALERT_CLAUSE_OP_VALUES: set[AlertClauseOp] = {
    "contains",
    "contains_any",
    "eq",
    "exists",
    "gt",
    "in",
    "lt",
    "ne",
    "not_exists",
    "not_in",
}


def check_alert_clause_op(value: str) -> AlertClauseOp:
    if value in ALERT_CLAUSE_OP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_CLAUSE_OP_VALUES!r}"
    )
