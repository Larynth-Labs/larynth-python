from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.calling_rule_sunday import CallingRuleSunday, check_calling_rule_sunday

if TYPE_CHECKING:
    from ..models.holiday_calendar_date import HolidayCalendarDate
    from ..models.rule_window import RuleWindow


T = TypeVar("T", bound="CallingRule")


@_attrs_define
class CallingRule:
    """
    Attributes:
        ca_preamble (bool):
        counsel_reviewed (bool):
        freq_cap_24h (int):
        holidays_next_90d (list[HolidayCalendarDate]):
        registration_required (bool):
        state (str):
        sunday (CallingRuleSunday):
        windows (list[RuleWindow]):
    """

    ca_preamble: bool
    counsel_reviewed: bool
    freq_cap_24h: int
    holidays_next_90d: list[HolidayCalendarDate]
    registration_required: bool
    state: str
    sunday: CallingRuleSunday
    windows: list[RuleWindow]

    def to_dict(self) -> dict[str, Any]:
        ca_preamble = self.ca_preamble

        counsel_reviewed = self.counsel_reviewed

        freq_cap_24h = self.freq_cap_24h

        holidays_next_90d = []
        for holidays_next_90d_item_data in self.holidays_next_90d:
            holidays_next_90d_item = holidays_next_90d_item_data.to_dict()
            holidays_next_90d.append(holidays_next_90d_item)

        registration_required = self.registration_required

        state = self.state

        sunday: str = self.sunday

        windows = []
        for windows_item_data in self.windows:
            windows_item = windows_item_data.to_dict()
            windows.append(windows_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ca_preamble": ca_preamble,
                "counsel_reviewed": counsel_reviewed,
                "freq_cap_24h": freq_cap_24h,
                "holidays_next_90d": holidays_next_90d,
                "registration_required": registration_required,
                "state": state,
                "sunday": sunday,
                "windows": windows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.holiday_calendar_date import HolidayCalendarDate
        from ..models.rule_window import RuleWindow

        d = dict(src_dict)
        ca_preamble = d.pop("ca_preamble")

        counsel_reviewed = d.pop("counsel_reviewed")

        freq_cap_24h = d.pop("freq_cap_24h")

        holidays_next_90d = []
        _holidays_next_90d = d.pop("holidays_next_90d")
        for holidays_next_90d_item_data in _holidays_next_90d:
            holidays_next_90d_item = HolidayCalendarDate.from_dict(
                holidays_next_90d_item_data
            )

            holidays_next_90d.append(holidays_next_90d_item)

        registration_required = d.pop("registration_required")

        state = d.pop("state")

        sunday = check_calling_rule_sunday(d.pop("sunday"))

        windows = []
        _windows = d.pop("windows")
        for windows_item_data in _windows:
            windows_item = RuleWindow.from_dict(windows_item_data)

            windows.append(windows_item)

        calling_rule = cls(
            ca_preamble=ca_preamble,
            counsel_reviewed=counsel_reviewed,
            freq_cap_24h=freq_cap_24h,
            holidays_next_90d=holidays_next_90d,
            registration_required=registration_required,
            state=state,
            sunday=sunday,
            windows=windows,
        )

        return calling_rule
