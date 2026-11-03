from typing import Literal

ImportProblemKind = Literal["dnc", "duplicate", "existing", "invalid", "non_us"]

IMPORT_PROBLEM_KIND_VALUES: set[ImportProblemKind] = {
    "dnc",
    "duplicate",
    "existing",
    "invalid",
    "non_us",
}


def check_import_problem_kind(value: str) -> ImportProblemKind:
    if value in IMPORT_PROBLEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IMPORT_PROBLEM_KIND_VALUES!r}"
    )
