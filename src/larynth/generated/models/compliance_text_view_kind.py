from typing import Literal

ComplianceTextViewKind = Literal[
    "after_hours_message_mode",
    "biometric_consent",
    "ca_preamble",
    "ca_preamble_decline_ack",
    "callback_check_code",
    "campaign_launch_attestation",
    "consent_attestation",
    "disclosure_inbound",
    "disclosure_outbound",
    "goodbye",
    "inbound_ai_attestation",
    "optout_ack",
    "optout_instruction",
    "optout_line_ack",
    "optout_line_greeting",
    "recording_notice",
    "screener_line",
    "transcript_notice",
    "unavailable",
    "voicemail_callback",
    "voicemail_intro",
    "voicemail_optout",
]

COMPLIANCE_TEXT_VIEW_KIND_VALUES: set[ComplianceTextViewKind] = {
    "after_hours_message_mode",
    "biometric_consent",
    "ca_preamble",
    "ca_preamble_decline_ack",
    "callback_check_code",
    "campaign_launch_attestation",
    "consent_attestation",
    "disclosure_inbound",
    "disclosure_outbound",
    "goodbye",
    "inbound_ai_attestation",
    "optout_ack",
    "optout_instruction",
    "optout_line_ack",
    "optout_line_greeting",
    "recording_notice",
    "screener_line",
    "transcript_notice",
    "unavailable",
    "voicemail_callback",
    "voicemail_intro",
    "voicemail_optout",
}


def check_compliance_text_view_kind(value: str) -> ComplianceTextViewKind:
    if value in COMPLIANCE_TEXT_VIEW_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMPLIANCE_TEXT_VIEW_KIND_VALUES!r}"
    )
