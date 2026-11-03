from typing import Literal

HolidayCalendarKey = Literal["us_federal"]

HOLIDAY_CALENDAR_KEY_VALUES: set[HolidayCalendarKey] = {
    "us_federal",
}


def check_holiday_calendar_key(value: str) -> HolidayCalendarKey:
    if value in HOLIDAY_CALENDAR_KEY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {HOLIDAY_CALENDAR_KEY_VALUES!r}"
    )
