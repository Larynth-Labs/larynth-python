from typing import Literal

ListComplianceTextsKind = Literal[
    "disclosure_inbound",
    "disclosure_outbound",
    "goodbye",
    "inbound_ai_attestation",
    "optout_ack",
    "optout_instruction",
    "recording_notice",
    "screener_line",
    "unavailable",
    "voicemail_intro",
    "voicemail_optout",
]

LIST_COMPLIANCE_TEXTS_KIND_VALUES: set[ListComplianceTextsKind] = {
    "disclosure_inbound",
    "disclosure_outbound",
    "goodbye",
    "inbound_ai_attestation",
    "optout_ack",
    "optout_instruction",
    "recording_notice",
    "screener_line",
    "unavailable",
    "voicemail_intro",
    "voicemail_optout",
}


def check_list_compliance_texts_kind(value: str) -> ListComplianceTextsKind:
    if value in LIST_COMPLIANCE_TEXTS_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_COMPLIANCE_TEXTS_KIND_VALUES!r}"
    )
