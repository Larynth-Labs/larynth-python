from typing import Literal

CallAttestation = Literal["A", "B", "C"]

CALL_ATTESTATION_VALUES: set[CallAttestation] = {
    "A",
    "B",
    "C",
}


def check_call_attestation(value: str) -> CallAttestation:
    if value in CALL_ATTESTATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_ATTESTATION_VALUES!r}"
    )
