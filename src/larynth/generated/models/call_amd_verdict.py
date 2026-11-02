from typing import Literal

CallAmdVerdict = Literal[
    "carrier_vm", "fax", "human", "ivr", "screener", "sit", "unknown", "voicemail"
]

CALL_AMD_VERDICT_VALUES: set[CallAmdVerdict] = {
    "carrier_vm",
    "fax",
    "human",
    "ivr",
    "screener",
    "sit",
    "unknown",
    "voicemail",
}


def check_call_amd_verdict(value: str) -> CallAmdVerdict:
    if value in CALL_AMD_VERDICT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_AMD_VERDICT_VALUES!r}"
    )
