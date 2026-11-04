import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_billing_usage_group_by import (
    GetBillingUsageGroupBy,
)
from ...models.problem import Problem
from ...models.usage import Usage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    period: str | Unset = UNSET,
    group_by: GetBillingUsageGroupBy | Unset = "category",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["period"] = period

    json_group_by: str | Unset = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = group_by

    params["group_by"] = json_group_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing/usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | Usage | None:
    if response.status_code == 200:
        response_200 = Usage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Problem.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Problem.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Problem.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | Usage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    period: str | Unset = UNSET,
    group_by: GetBillingUsageGroupBy | Unset = "category",
) -> Response[Problem | Usage]:
    """Spend by category, agent, day or number from the ledger-written usage lines

    Args:
        from_ (datetime.date | Unset): First local day; at most 366 days before to
        to (datetime.date | Unset): Last local day
        period (str | Unset): Instead of from and to: this_month, last_30_days or month:YYYY-MM
        group_by (GetBillingUsageGroupBy | Unset):  Default: 'category'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Usage]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        period=period,
        group_by=group_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    period: str | Unset = UNSET,
    group_by: GetBillingUsageGroupBy | Unset = "category",
) -> Problem | Usage | None:
    """Spend by category, agent, day or number from the ledger-written usage lines

    Args:
        from_ (datetime.date | Unset): First local day; at most 366 days before to
        to (datetime.date | Unset): Last local day
        period (str | Unset): Instead of from and to: this_month, last_30_days or month:YYYY-MM
        group_by (GetBillingUsageGroupBy | Unset):  Default: 'category'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Usage
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        period=period,
        group_by=group_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    period: str | Unset = UNSET,
    group_by: GetBillingUsageGroupBy | Unset = "category",
) -> Response[Problem | Usage]:
    """Spend by category, agent, day or number from the ledger-written usage lines

    Args:
        from_ (datetime.date | Unset): First local day; at most 366 days before to
        to (datetime.date | Unset): Last local day
        period (str | Unset): Instead of from and to: this_month, last_30_days or month:YYYY-MM
        group_by (GetBillingUsageGroupBy | Unset):  Default: 'category'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Usage]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        period=period,
        group_by=group_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    period: str | Unset = UNSET,
    group_by: GetBillingUsageGroupBy | Unset = "category",
) -> Problem | Usage | None:
    """Spend by category, agent, day or number from the ledger-written usage lines

    Args:
        from_ (datetime.date | Unset): First local day; at most 366 days before to
        to (datetime.date | Unset): Last local day
        period (str | Unset): Instead of from and to: this_month, last_30_days or month:YYYY-MM
        group_by (GetBillingUsageGroupBy | Unset):  Default: 'category'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Usage
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            period=period,
            group_by=group_by,
        )
    ).parsed
