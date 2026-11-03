from typing import Literal

ComplianceTextViewKind = Literal[
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

COMPLIANCE_TEXT_VIEW_KIND_VALUES: set[ComplianceTextViewKind] = {
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


def check_compliance_text_view_kind(value: str) -> ComplianceTextViewKind:
    if value in COMPLIANCE_TEXT_VIEW_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMPLIANCE_TEXT_VIEW_KIND_VALUES!r}"
    )
