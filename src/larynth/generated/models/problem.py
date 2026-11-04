from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.problem_period import ProblemPeriod, check_problem_period
from ..models.problem_request_kind import ProblemRequestKind, check_problem_request_kind
from ..models.problem_used_by_item import ProblemUsedByItem, check_problem_used_by_item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_detail import ErrorDetail
    from ..models.preflight_check import PreflightCheck


T = TypeVar("T", bound="Problem")


@_attrs_define
class Problem:
    """
    Attributes:
        code (str): Stable machine-readable error code; compliance denials carry the dial.* rule id
        status (int):
        title (str):
        type_ (str): Stable URI identifying the error code
        api_base (str | Unset): API base URL of the workspace's home region (workspace.other_region)
        attempts_left (int | Unset): Code attempts left in this sign-in step
        campaign_ids (list[str] | Unset): Campaigns that use the number (numbers.in_use)
        cap_micro (int | Unset): Cap of that limit (billing.spend_limit_reached)
        checks (list[PreflightCheck] | Unset): Failed launch checks (campaign.preflight_failed)
        contact_id (str | Unset): Existing contact (contacts.exists)
        detail (str | Unset):
        errors (list[ErrorDetail] | Unset):
        instance (str | Unset):
        max_micro (int | Unset): Maximum top-up (billing.top_up_above_maximum)
        min_micro (int | Unset): Minimum top-up (billing.top_up_below_minimum)
        optout_line (bool | Unset): The number is the opt-out line (numbers.in_use)
        period (ProblemPeriod | Unset): Limit that was reached (billing.spend_limit_reached)
        reauth_methods (list[str] | Unset): Ways to re-authenticate, in preference order (auth.reauth_required)
        request_kind (ProblemRequestKind | Unset): Spending request kind to file instead (spending.approval_required)
        retry_at (datetime.datetime | Unset): Next moment the request may succeed (calling windows)
        revision (int | Unset): Current revision (numbers.routing_conflict, campaign.revision_conflict)
        updated_by_name (str | Unset):
        used_by (list[ProblemUsedByItem] | Unset): What uses the card (billing.payment_method_in_use)
        used_micro (int | Unset): Spend counted against it (billing.spend_limit_reached)
    """

    code: str
    status: int
    title: str
    type_: str
    api_base: str | Unset = UNSET
    attempts_left: int | Unset = UNSET
    campaign_ids: list[str] | Unset = UNSET
    cap_micro: int | Unset = UNSET
    checks: list[PreflightCheck] | Unset = UNSET
    contact_id: str | Unset = UNSET
    detail: str | Unset = UNSET
    errors: list[ErrorDetail] | Unset = UNSET
    instance: str | Unset = UNSET
    max_micro: int | Unset = UNSET
    min_micro: int | Unset = UNSET
    optout_line: bool | Unset = UNSET
    period: ProblemPeriod | Unset = UNSET
    reauth_methods: list[str] | Unset = UNSET
    request_kind: ProblemRequestKind | Unset = UNSET
    retry_at: datetime.datetime | Unset = UNSET
    revision: int | Unset = UNSET
    updated_by_name: str | Unset = UNSET
    used_by: list[ProblemUsedByItem] | Unset = UNSET
    used_micro: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        status = self.status

        title = self.title

        type_ = self.type_

        api_base = self.api_base

        attempts_left = self.attempts_left

        campaign_ids: list[str] | Unset = UNSET
        if not isinstance(self.campaign_ids, Unset):
            campaign_ids = self.campaign_ids

        cap_micro = self.cap_micro

        checks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.checks, Unset):
            checks = []
            for checks_item_data in self.checks:
                checks_item = checks_item_data.to_dict()
                checks.append(checks_item)

        contact_id = self.contact_id

        detail = self.detail

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        instance = self.instance

        max_micro = self.max_micro

        min_micro = self.min_micro

        optout_line = self.optout_line

        period: str | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period

        reauth_methods: list[str] | Unset = UNSET
        if not isinstance(self.reauth_methods, Unset):
            reauth_methods = self.reauth_methods

        request_kind: str | Unset = UNSET
        if not isinstance(self.request_kind, Unset):
            request_kind = self.request_kind

        retry_at: str | Unset = UNSET
        if not isinstance(self.retry_at, Unset):
            retry_at = self.retry_at.isoformat()

        revision = self.revision

        updated_by_name = self.updated_by_name

        used_by: list[str] | Unset = UNSET
        if not isinstance(self.used_by, Unset):
            used_by = []
            for used_by_item_data in self.used_by:
                used_by_item: str = used_by_item_data
                used_by.append(used_by_item)

        used_micro = self.used_micro

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "status": status,
                "title": title,
                "type": type_,
            }
        )
        if api_base is not UNSET:
            field_dict["api_base"] = api_base
        if attempts_left is not UNSET:
            field_dict["attempts_left"] = attempts_left
        if campaign_ids is not UNSET:
            field_dict["campaign_ids"] = campaign_ids
        if cap_micro is not UNSET:
            field_dict["cap_micro"] = cap_micro
        if checks is not UNSET:
            field_dict["checks"] = checks
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if detail is not UNSET:
            field_dict["detail"] = detail
        if errors is not UNSET:
            field_dict["errors"] = errors
        if instance is not UNSET:
            field_dict["instance"] = instance
        if max_micro is not UNSET:
            field_dict["max_micro"] = max_micro
        if min_micro is not UNSET:
            field_dict["min_micro"] = min_micro
        if optout_line is not UNSET:
            field_dict["optout_line"] = optout_line
        if period is not UNSET:
            field_dict["period"] = period
        if reauth_methods is not UNSET:
            field_dict["reauth_methods"] = reauth_methods
        if request_kind is not UNSET:
            field_dict["request_kind"] = request_kind
        if retry_at is not UNSET:
            field_dict["retry_at"] = retry_at
        if revision is not UNSET:
            field_dict["revision"] = revision
        if updated_by_name is not UNSET:
            field_dict["updated_by_name"] = updated_by_name
        if used_by is not UNSET:
            field_dict["used_by"] = used_by
        if used_micro is not UNSET:
            field_dict["used_micro"] = used_micro

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.error_detail import ErrorDetail
        from ..models.preflight_check import PreflightCheck

        d = dict(src_dict)
        code = d.pop("code")

        status = d.pop("status")

        title = d.pop("title")

        type_ = d.pop("type")

        api_base = d.pop("api_base", UNSET)

        attempts_left = d.pop("attempts_left", UNSET)

        campaign_ids = cast(list[str], d.pop("campaign_ids", UNSET))

        cap_micro = d.pop("cap_micro", UNSET)

        _checks = d.pop("checks", UNSET)
        checks: list[PreflightCheck] | Unset = UNSET
        if _checks is not UNSET:
            checks = []
            for checks_item_data in _checks:
                checks_item = PreflightCheck.from_dict(checks_item_data)

                checks.append(checks_item)

        contact_id = d.pop("contact_id", UNSET)

        detail = d.pop("detail", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[ErrorDetail] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ErrorDetail.from_dict(errors_item_data)

                errors.append(errors_item)

        instance = d.pop("instance", UNSET)

        max_micro = d.pop("max_micro", UNSET)

        min_micro = d.pop("min_micro", UNSET)

        optout_line = d.pop("optout_line", UNSET)

        _period = d.pop("period", UNSET)
        period: ProblemPeriod | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = check_problem_period(_period)

        reauth_methods = cast(list[str], d.pop("reauth_methods", UNSET))

        _request_kind = d.pop("request_kind", UNSET)
        request_kind: ProblemRequestKind | Unset
        if isinstance(_request_kind, Unset):
            request_kind = UNSET
        else:
            request_kind = check_problem_request_kind(_request_kind)

        _retry_at = d.pop("retry_at", UNSET)
        retry_at: datetime.datetime | Unset
        if isinstance(_retry_at, Unset):
            retry_at = UNSET
        else:
            retry_at = datetime.datetime.fromisoformat(_retry_at)

        revision = d.pop("revision", UNSET)

        updated_by_name = d.pop("updated_by_name", UNSET)

        _used_by = d.pop("used_by", UNSET)
        used_by: list[ProblemUsedByItem] | Unset = UNSET
        if _used_by is not UNSET:
            used_by = []
            for used_by_item_data in _used_by:
                used_by_item = check_problem_used_by_item(used_by_item_data)

                used_by.append(used_by_item)

        used_micro = d.pop("used_micro", UNSET)

        problem = cls(
            code=code,
            status=status,
            title=title,
            type_=type_,
            api_base=api_base,
            attempts_left=attempts_left,
            campaign_ids=campaign_ids,
            cap_micro=cap_micro,
            checks=checks,
            contact_id=contact_id,
            detail=detail,
            errors=errors,
            instance=instance,
            max_micro=max_micro,
            min_micro=min_micro,
            optout_line=optout_line,
            period=period,
            reauth_methods=reauth_methods,
            request_kind=request_kind,
            retry_at=retry_at,
            revision=revision,
            updated_by_name=updated_by_name,
            used_by=used_by,
            used_micro=used_micro,
        )

        problem.additional_properties = d
        return problem

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
