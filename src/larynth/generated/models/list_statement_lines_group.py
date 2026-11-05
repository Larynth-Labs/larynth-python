from typing import Literal

ListStatementLinesGroup = Literal[
    "adjustments", "bundles", "calls", "free_credit", "numbers", "top_ups"
]

LIST_STATEMENT_LINES_GROUP_VALUES: set[ListStatementLinesGroup] = {
    "adjustments",
    "bundles",
    "calls",
    "free_credit",
    "numbers",
    "top_ups",
}


def check_list_statement_lines_group(value: str) -> ListStatementLinesGroup:
    if value in LIST_STATEMENT_LINES_GROUP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_STATEMENT_LINES_GROUP_VALUES!r}"
    )
