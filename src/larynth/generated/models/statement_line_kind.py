from typing import Literal

StatementLineKind = Literal[
    "adjustment",
    "auto_top_up",
    "branded_fee",
    "bundle_conversion",
    "bundle_purchase",
    "calls",
    "dispute",
    "free_credit",
    "number_rental",
    "refund",
    "top_up",
]

STATEMENT_LINE_KIND_VALUES: set[StatementLineKind] = {
    "adjustment",
    "auto_top_up",
    "branded_fee",
    "bundle_conversion",
    "bundle_purchase",
    "calls",
    "dispute",
    "free_credit",
    "number_rental",
    "refund",
    "top_up",
}


def check_statement_line_kind(value: str) -> StatementLineKind:
    if value in STATEMENT_LINE_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATEMENT_LINE_KIND_VALUES!r}"
    )
