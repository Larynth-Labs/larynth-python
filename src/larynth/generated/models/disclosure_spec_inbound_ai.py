from typing import Literal

DisclosureSpecInboundAi = Literal["off", "on"]

DISCLOSURE_SPEC_INBOUND_AI_VALUES: set[DisclosureSpecInboundAi] = {
    "off",
    "on",
}


def check_disclosure_spec_inbound_ai(value: str) -> DisclosureSpecInboundAi:
    if value in DISCLOSURE_SPEC_INBOUND_AI_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DISCLOSURE_SPEC_INBOUND_AI_VALUES!r}"
    )
