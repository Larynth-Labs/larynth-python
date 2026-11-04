from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.same_caller_calls import SameCallerCalls
from ...types import UNSET, Response, Unset


def _get_kwargs(
    call_id: str,
    *,
    limit: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/calls/{call_id}/same-caller".format(
            call_id=quote(str(call_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | SameCallerCalls | None:
    if response.status_code == 200:
        response_200 = SameCallerCalls.from_dict(response.json())

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
) -> Response[Problem | SameCallerCalls]:
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
    limit: int | Unset = 10,
) -> Response[Problem | SameCallerCalls]:
    """Earlier calls from the same caller, newest first

    Args:
        call_id (str): <cell>_<ULID>
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SameCallerCalls]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    call_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
) -> Problem | SameCallerCalls | None:
    """Earlier calls from the same caller, newest first

    Args:
        call_id (str): <cell>_<ULID>
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SameCallerCalls
    """

    return sync_detailed(
        call_id=call_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    call_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
) -> Response[Problem | SameCallerCalls]:
    """Earlier calls from the same caller, newest first

    Args:
        call_id (str): <cell>_<ULID>
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SameCallerCalls]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    call_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 10,
) -> Problem | SameCallerCalls | None:
    """Earlier calls from the same caller, newest first

    Args:
        call_id (str): <cell>_<ULID>
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SameCallerCalls
    """

    return (
        await asyncio_detailed(
            call_id=call_id,
            client=client,
            limit=limit,
        )
    ).parsed
