from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_blocked_caller import PageBlockedCaller
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    params["e164"] = e164

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/blocked-callers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageBlockedCaller | Problem | None:
    if response.status_code == 200:
        response_200 = PageBlockedCaller.from_dict(response.json())

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
) -> Response[PageBlockedCaller | Problem]:
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
) -> Response[PageBlockedCaller | Problem]:
    """Numbers this workspace does not answer; their calls are not billed

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageBlockedCaller | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        e164=e164,
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
) -> PageBlockedCaller | Problem | None:
    """Numbers this workspace does not answer; their calls are not billed

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageBlockedCaller | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        after=after,
        e164=e164,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
) -> Response[PageBlockedCaller | Problem]:
    """Numbers this workspace does not answer; their calls are not billed

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageBlockedCaller | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        e164=e164,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
) -> PageBlockedCaller | Problem | None:
    """Numbers this workspace does not answer; their calls are not billed

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageBlockedCaller | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            after=after,
            e164=e164,
        )
    ).parsed
