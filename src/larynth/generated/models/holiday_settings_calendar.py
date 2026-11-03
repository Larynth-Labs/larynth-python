from typing import Literal

HolidaySettingsCalendar = Literal["us_federal"]

HOLIDAY_SETTINGS_CALENDAR_VALUES: set[HolidaySettingsCalendar] = {
    "us_federal",
}


def check_holiday_settings_calendar(value: str) -> HolidaySettingsCalendar:
    if value in HOLIDAY_SETTINGS_CALENDAR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {HOLIDAY_SETTINGS_CALENDAR_VALUES!r}"
    )
