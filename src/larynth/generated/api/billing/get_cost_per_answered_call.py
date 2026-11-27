import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cost_per_answered_call import CostPerAnsweredCall
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    period: str | Unset = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing/cost-per-answered-call",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CostPerAnsweredCall | Problem | None:
    if response.status_code == 200:
        response_200 = CostPerAnsweredCall.from_dict(response.json())

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
) -> Response[CostPerAnsweredCall | Problem]:
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
) -> Response[CostPerAnsweredCall | Problem]:
    """Settled call charges divided by answered calls, overall and per agent; read from the usage lines,
    never charges anything

    Args:
        from_ (datetime.date | Unset): First local day; at most 366 days before to
        to (datetime.date | Unset): Last local day
        period (str | Unset): Instead of from and to: this_month, last_7_days, last_30_days or
            month:YYYY-MM

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostPerAnsweredCall | Problem]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        period=period,
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
) -> CostPerAnsweredCall | Problem | None:
    """Settled call charges divided by answered calls, overall and per agent; read from the usage lines,
    never charges anything

    Args:
        from_ (datetime.date | Unset): First local day; at most 366 days before to
        to (datetime.date | Unset): Last local day
        period (str | Unset): Instead of from and to: this_month, last_7_days, last_30_days or
            month:YYYY-MM

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostPerAnsweredCall | Problem
    """

    return sync_detailed(
        client=client,
        from_=from_,
        to=to,
        period=period,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    period: str | Unset = UNSET,
) -> Response[CostPerAnsweredCall | Problem]:
    """Settled call charges divided by answered calls, overall and per agent; read from the usage lines,
    never charges anything

    Args:
        from_ (datetime.date | Unset): First local day; at most 366 days before to
        to (datetime.date | Unset): Last local day
        period (str | Unset): Instead of from and to: this_month, last_7_days, last_30_days or
            month:YYYY-MM

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CostPerAnsweredCall | Problem]
    """

    kwargs = _get_kwargs(
        from_=from_,
        to=to,
        period=period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    period: str | Unset = UNSET,
) -> CostPerAnsweredCall | Problem | None:
    """Settled call charges divided by answered calls, overall and per agent; read from the usage lines,
    never charges anything

    Args:
        from_ (datetime.date | Unset): First local day; at most 366 days before to
        to (datetime.date | Unset): Last local day
        period (str | Unset): Instead of from and to: this_month, last_7_days, last_30_days or
            month:YYYY-MM

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CostPerAnsweredCall | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            from_=from_,
            to=to,
            period=period,
        )
    ).parsed
