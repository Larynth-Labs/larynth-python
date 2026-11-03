from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conversation import Conversation
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    call_id: str,
    *,
    limit: int | Unset = 500,
    after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/calls/{call_id}/conversation".format(
            call_id=quote(str(call_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Conversation | Problem | None:
    if response.status_code == 200:
        response_200 = Conversation.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

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
) -> Response[Conversation | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    call_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 500,
    after: str | Unset = UNSET,
) -> Response[Conversation | Problem]:
    """Turns, tools, transfers and markers with offsets and reply latency

    Args:
        call_id (str): <cell>_<ULID>
        limit (int | Unset):  Default: 500.
        after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Conversation | Problem]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
        limit=limit,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    call_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 500,
    after: str | Unset = UNSET,
) -> Conversation | Problem | None:
    """Turns, tools, transfers and markers with offsets and reply latency

    Args:
        call_id (str): <cell>_<ULID>
        limit (int | Unset):  Default: 500.
        after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Conversation | Problem
    """

    return sync_detailed(
        call_id=call_id,
        client=client,
        limit=limit,
        after=after,
    ).parsed


async def asyncio_detailed(
    call_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 500,
    after: str | Unset = UNSET,
) -> Response[Conversation | Problem]:
    """Turns, tools, transfers and markers with offsets and reply latency

    Args:
        call_id (str): <cell>_<ULID>
        limit (int | Unset):  Default: 500.
        after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Conversation | Problem]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
        limit=limit,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    call_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 500,
    after: str | Unset = UNSET,
) -> Conversation | Problem | None:
    """Turns, tools, transfers and markers with offsets and reply latency

    Args:
        call_id (str): <cell>_<ULID>
        limit (int | Unset):  Default: 500.
        after (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Conversation | Problem
    """

    return (
        await asyncio_detailed(
            call_id=call_id,
            client=client,
            limit=limit,
            after=after,
        )
    ).parsed
