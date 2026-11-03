import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_revocations_channel import (
    ListRevocationsChannel,
)
from ...models.page_revocation import PageRevocation
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
    channel: ListRevocationsChannel | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    params["e164"] = e164

    json_channel: str | Unset = UNSET
    if not isinstance(channel, Unset):
        json_channel = channel

    params["channel"] = json_channel

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/compliance/revocations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageRevocation | Problem | None:
    if response.status_code == 200:
        response_200 = PageRevocation.from_dict(response.json())

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
) -> Response[PageRevocation | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
    channel: ListRevocationsChannel | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
) -> Response[PageRevocation | Problem]:
    """Opt-outs, newest first

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):
        channel (ListRevocationsChannel | Unset):
        since (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageRevocation | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        e164=e164,
        channel=channel,
        since=since,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
    channel: ListRevocationsChannel | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
) -> PageRevocation | Problem | None:
    """Opt-outs, newest first

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):
        channel (ListRevocationsChannel | Unset):
        since (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageRevocation | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        after=after,
        e164=e164,
        channel=channel,
        since=since,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
    channel: ListRevocationsChannel | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
) -> Response[PageRevocation | Problem]:
    """Opt-outs, newest first

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):
        channel (ListRevocationsChannel | Unset):
        since (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageRevocation | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        e164=e164,
        channel=channel,
        since=since,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
    channel: ListRevocationsChannel | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
) -> PageRevocation | Problem | None:
    """Opt-outs, newest first

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):
        channel (ListRevocationsChannel | Unset):
        since (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageRevocation | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            after=after,
            e164=e164,
            channel=channel,
            since=since,
        )
    ).parsed
