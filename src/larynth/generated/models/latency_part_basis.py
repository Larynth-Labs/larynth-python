from typing import Literal

LatencyPartBasis = Literal["measured", "seeded"]

LATENCY_PART_BASIS_VALUES: set[LatencyPartBasis] = {
    "measured",
    "seeded",
}


def check_latency_part_basis(value: str) -> LatencyPartBasis:
    if value in LATENCY_PART_BASIS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LATENCY_PART_BASIS_VALUES!r}"
    )
