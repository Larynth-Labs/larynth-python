from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    call_id: str,
    *,
    range_: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(range_, Unset):
        headers["Range"] = range_

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/calls/{call_id}/recording/audio".format(
            call_id=quote(str(call_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | None:
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

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = Problem.from_dict(response.json())

        return response_410

    if response.status_code == 416:
        response_416 = Problem.from_dict(response.json())

        return response_416

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
) -> Response[Problem]:
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
    range_: str | Unset = UNSET,
) -> Response[Problem]:
    """Stream both parties of a call as one mixed WAV, with byte ranges; each playback is logged

    Args:
        call_id (str): <cell>_<ULID>
        range_ (str | Unset): bytes=<start>-[<end>]; recordings over 60 minutes answer 200 only

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
        range_=range_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    call_id: str,
    *,
    client: AuthenticatedClient,
    range_: str | Unset = UNSET,
) -> Problem | None:
    """Stream both parties of a call as one mixed WAV, with byte ranges; each playback is logged

    Args:
        call_id (str): <cell>_<ULID>
        range_ (str | Unset): bytes=<start>-[<end>]; recordings over 60 minutes answer 200 only

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem
    """

    return sync_detailed(
        call_id=call_id,
        client=client,
        range_=range_,
    ).parsed


async def asyncio_detailed(
    call_id: str,
    *,
    client: AuthenticatedClient,
    range_: str | Unset = UNSET,
) -> Response[Problem]:
    """Stream both parties of a call as one mixed WAV, with byte ranges; each playback is logged

    Args:
        call_id (str): <cell>_<ULID>
        range_ (str | Unset): bytes=<start>-[<end>]; recordings over 60 minutes answer 200 only

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
        range_=range_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    call_id: str,
    *,
    client: AuthenticatedClient,
    range_: str | Unset = UNSET,
) -> Problem | None:
    """Stream both parties of a call as one mixed WAV, with byte ranges; each playback is logged

    Args:
        call_id (str): <cell>_<ULID>
        range_ (str | Unset): bytes=<start>-[<end>]; recordings over 60 minutes answer 200 only

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem
    """

    return (
        await asyncio_detailed(
            call_id=call_id,
            client=client,
            range_=range_,
        )
    ).parsed
