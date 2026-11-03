from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.left_out_contact import LeftOutContact
    from ..models.state_audience import StateAudience
    from ..models.timezone_share import TimezoneShare


T = TypeVar("T", bound="AudiencePreview")


@_attrs_define
class AudiencePreview:
    """
    Attributes:
        by_state (list[StateAudience]):
        by_timezone (list[TimezoneShare]):
        callable_ (int):
        dnc (int):
        no_consent (int):
        sample_left_out (list[LeftOutContact]):
        total (int):
    """

    by_state: list[StateAudience]
    by_timezone: list[TimezoneShare]
    callable_: int
    dnc: int
    no_consent: int
    sample_left_out: list[LeftOutContact]
    total: int

    def to_dict(self) -> dict[str, Any]:
        by_state = []
        for by_state_item_data in self.by_state:
            by_state_item = by_state_item_data.to_dict()
            by_state.append(by_state_item)

        by_timezone = []
        for by_timezone_item_data in self.by_timezone:
            by_timezone_item = by_timezone_item_data.to_dict()
            by_timezone.append(by_timezone_item)

        callable_ = self.callable_

        dnc = self.dnc

        no_consent = self.no_consent

        sample_left_out = []
        for sample_left_out_item_data in self.sample_left_out:
            sample_left_out_item = sample_left_out_item_data.to_dict()
            sample_left_out.append(sample_left_out_item)

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "by_state": by_state,
                "by_timezone": by_timezone,
                "callable": callable_,
                "dnc": dnc,
                "no_consent": no_consent,
                "sample_left_out": sample_left_out,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.left_out_contact import LeftOutContact
        from ..models.state_audience import StateAudience
        from ..models.timezone_share import TimezoneShare

        d = dict(src_dict)
        by_state = []
        _by_state = d.pop("by_state")
        for by_state_item_data in _by_state:
            by_state_item = StateAudience.from_dict(by_state_item_data)

            by_state.append(by_state_item)

        by_timezone = []
        _by_timezone = d.pop("by_timezone")
        for by_timezone_item_data in _by_timezone:
            by_timezone_item = TimezoneShare.from_dict(by_timezone_item_data)

            by_timezone.append(by_timezone_item)

        callable_ = d.pop("callable")

        dnc = d.pop("dnc")

        no_consent = d.pop("no_consent")

        sample_left_out = []
        _sample_left_out = d.pop("sample_left_out")
        for sample_left_out_item_data in _sample_left_out:
            sample_left_out_item = LeftOutContact.from_dict(sample_left_out_item_data)

            sample_left_out.append(sample_left_out_item)

        total = d.pop("total")

        audience_preview = cls(
            by_state=by_state,
            by_timezone=by_timezone,
            callable_=callable_,
            dnc=dnc,
            no_consent=no_consent,
            sample_left_out=sample_left_out,
            total=total,
        )

        return audience_preview
