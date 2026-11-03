from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.compare_result import CompareResult
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    v: int,
    *,
    against: str | Unset = "published",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["against"] = against

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assistants/{id}/versions/{v}/compare".format(
            id=quote(str(id), safe=""),
            v=quote(str(v), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CompareResult | Problem | None:
    if response.status_code == 200:
        response_200 = CompareResult.from_dict(response.json())

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
) -> Response[CompareResult | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    v: int,
    *,
    client: AuthenticatedClient,
    against: str | Unset = "published",
) -> Response[CompareResult | Problem]:
    """Field and instruction differences between two versions, with price and numbers affected

    Args:
        id (UUID):
        v (int):
        against (str | Unset): published, or a version number Default: 'published'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompareResult | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        v=v,
        against=against,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    v: int,
    *,
    client: AuthenticatedClient,
    against: str | Unset = "published",
) -> CompareResult | Problem | None:
    """Field and instruction differences between two versions, with price and numbers affected

    Args:
        id (UUID):
        v (int):
        against (str | Unset): published, or a version number Default: 'published'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompareResult | Problem
    """

    return sync_detailed(
        id=id,
        v=v,
        client=client,
        against=against,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    v: int,
    *,
    client: AuthenticatedClient,
    against: str | Unset = "published",
) -> Response[CompareResult | Problem]:
    """Field and instruction differences between two versions, with price and numbers affected

    Args:
        id (UUID):
        v (int):
        against (str | Unset): published, or a version number Default: 'published'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompareResult | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        v=v,
        against=against,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    v: int,
    *,
    client: AuthenticatedClient,
    against: str | Unset = "published",
) -> CompareResult | Problem | None:
    """Field and instruction differences between two versions, with price and numbers affected

    Args:
        id (UUID):
        v (int):
        against (str | Unset): published, or a version number Default: 'published'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompareResult | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            v=v,
            client=client,
            against=against,
        )
    ).parsed
