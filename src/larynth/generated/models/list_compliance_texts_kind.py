from typing import Literal

ListComplianceTextsKind = Literal[
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

LIST_COMPLIANCE_TEXTS_KIND_VALUES: set[ListComplianceTextsKind] = {
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


def check_list_compliance_texts_kind(value: str) -> ListComplianceTextsKind:
    if value in LIST_COMPLIANCE_TEXTS_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_COMPLIANCE_TEXTS_KIND_VALUES!r}"
    )
