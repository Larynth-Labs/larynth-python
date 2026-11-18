import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.analytics_usage import AnalyticsUsage
from ...models.get_analytics_usage_direction import (
    GetAnalyticsUsageDirection,
)
from ...models.get_analytics_usage_group_by import (
    GetAnalyticsUsageGroupBy,
)
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    direction: GetAnalyticsUsageDirection | Unset = UNSET,
    group_by: GetAnalyticsUsageGroupBy | Unset = "none",
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

    json_assistant_id: str | Unset = UNSET
    if not isinstance(assistant_id, Unset):
        json_assistant_id = str(assistant_id)
    params["assistant_id"] = json_assistant_id

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction

    params["direction"] = json_direction

    json_group_by: str | Unset = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = group_by

    params["group_by"] = json_group_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AnalyticsUsage | Problem | None:
    if response.status_code == 200:
        response_200 = AnalyticsUsage.from_dict(response.json())

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
) -> Response[AnalyticsUsage | Problem]:
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
    assistant_id: UUID | Unset = UNSET,
    direction: GetAnalyticsUsageDirection | Unset = UNSET,
    group_by: GetAnalyticsUsageGroupBy | Unset = "none",
) -> Response[AnalyticsUsage | Problem]:
    """Calls, billed minutes and spend from the ledger-written usage lines, optionally per day

    Args:
        from_ (datetime.date | Unset): First local day; defaults to 29 days before to
        to (datetime.date | Unset): Last local day, inclusive; defaults to today in the workspace
            time zone. At most 366 days after from
        assistant_id (UUID | Unset): Only this agent
        direction (GetAnalyticsUsageDirection | Unset): Only this call direction
        group_by (GetAnalyticsUsageGroupBy | Unset): day adds one row per local day, zero-filled
            Default: 'none'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsUsage | Problem]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        assistant_id=assistant_id,
        direction=direction,
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
    assistant_id: UUID | Unset = UNSET,
    direction: GetAnalyticsUsageDirection | Unset = UNSET,
    group_by: GetAnalyticsUsageGroupBy | Unset = "none",
) -> AnalyticsUsage | Problem | None:
    """Calls, billed minutes and spend from the ledger-written usage lines, optionally per day

    Args:
        from_ (datetime.date | Unset): First local day; defaults to 29 days before to
        to (datetime.date | Unset): Last local day, inclusive; defaults to today in the workspace
            time zone. At most 366 days after from
        assistant_id (UUID | Unset): Only this agent
        direction (GetAnalyticsUsageDirection | Unset): Only this call direction
        group_by (GetAnalyticsUsageGroupBy | Unset): day adds one row per local day, zero-filled
            Default: 'none'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsUsage | Problem
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        assistant_id=assistant_id,
        direction=direction,
        group_by=group_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    direction: GetAnalyticsUsageDirection | Unset = UNSET,
    group_by: GetAnalyticsUsageGroupBy | Unset = "none",
) -> Response[AnalyticsUsage | Problem]:
    """Calls, billed minutes and spend from the ledger-written usage lines, optionally per day

    Args:
        from_ (datetime.date | Unset): First local day; defaults to 29 days before to
        to (datetime.date | Unset): Last local day, inclusive; defaults to today in the workspace
            time zone. At most 366 days after from
        assistant_id (UUID | Unset): Only this agent
        direction (GetAnalyticsUsageDirection | Unset): Only this call direction
        group_by (GetAnalyticsUsageGroupBy | Unset): day adds one row per local day, zero-filled
            Default: 'none'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AnalyticsUsage | Problem]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        assistant_id=assistant_id,
        direction=direction,
        group_by=group_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    direction: GetAnalyticsUsageDirection | Unset = UNSET,
    group_by: GetAnalyticsUsageGroupBy | Unset = "none",
) -> AnalyticsUsage | Problem | None:
    """Calls, billed minutes and spend from the ledger-written usage lines, optionally per day

    Args:
        from_ (datetime.date | Unset): First local day; defaults to 29 days before to
        to (datetime.date | Unset): Last local day, inclusive; defaults to today in the workspace
            time zone. At most 366 days after from
        assistant_id (UUID | Unset): Only this agent
        direction (GetAnalyticsUsageDirection | Unset): Only this call direction
        group_by (GetAnalyticsUsageGroupBy | Unset): day adds one row per local day, zero-filled
            Default: 'none'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AnalyticsUsage | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            assistant_id=assistant_id,
            direction=direction,
            group_by=group_by,
        )
    ).parsed
