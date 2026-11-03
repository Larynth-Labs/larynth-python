from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.dnc_check_list import DncCheckList, check_dnc_check_list
from ..models.dnc_check_result import DncCheckResult, check_dnc_check_result
from ..types import UNSET, Unset

T = TypeVar("T", bound="DncCheck")


@_attrs_define
class DncCheck:
    """
    Attributes:
        at (datetime.datetime):
        list_ (DncCheckList):
        reason_code (str):
        result (DncCheckResult):
        campaign_id (UUID | Unset):
    """

    at: datetime.datetime
    list_: DncCheckList
    reason_code: str
    result: DncCheckResult
    campaign_id: UUID | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        list_: str = self.list_

        reason_code = self.reason_code

        result: str = self.result

        campaign_id: str | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = str(self.campaign_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "list": list_,
                "reason_code": reason_code,
                "result": result,
            }
        )
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        list_ = check_dnc_check_list(d.pop("list"))

        reason_code = d.pop("reason_code")

        result = check_dnc_check_result(d.pop("result"))

        _campaign_id = d.pop("campaign_id", UNSET)
        campaign_id: UUID | Unset
        if isinstance(_campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = UUID(_campaign_id)

        dnc_check = cls(
            at=at,
            list_=list_,
            reason_code=reason_code,
            result=result,
            campaign_id=campaign_id,
        )

        return dnc_check
