from typing import Literal

PreflightCheckCode = Literal[
    "agent_published",
    "audience",
    "balance",
    "ca_preamble",
    "caller_id",
    "calling_hours",
    "consent_coverage",
    "daily_spend_cap",
    "dnc_internal",
    "dnc_national",
    "frequency_cap",
    "holidays_sundays",
    "outbound_terms",
    "paid_top_up",
    "platform_outbound_open",
    "recheck_due",
    "script_check",
    "state_registrations",
    "telemarketing_approved",
    "verification",
    "voicemail_optout_line",
]

PREFLIGHT_CHECK_CODE_VALUES: set[PreflightCheckCode] = {
    "agent_published",
    "audience",
    "balance",
    "ca_preamble",
    "caller_id",
    "calling_hours",
    "consent_coverage",
    "daily_spend_cap",
    "dnc_internal",
    "dnc_national",
    "frequency_cap",
    "holidays_sundays",
    "outbound_terms",
    "paid_top_up",
    "platform_outbound_open",
    "recheck_due",
    "script_check",
    "state_registrations",
    "telemarketing_approved",
    "verification",
    "voicemail_optout_line",
}


def check_preflight_check_code(value: str) -> PreflightCheckCode:
    if value in PREFLIGHT_CHECK_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PREFLIGHT_CHECK_CODE_VALUES!r}"
    )
