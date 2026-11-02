from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_available_number import PageAvailableNumber
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    country: str | Unset = "US",
    area_code: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["country"] = country

    params["area_code"] = area_code

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/numbers/available",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageAvailableNumber | Problem | None:
    if response.status_code == 200:
        response_200 = PageAvailableNumber.from_dict(response.json())

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
) -> Response[PageAvailableNumber | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    country: str | Unset = "US",
    area_code: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[PageAvailableNumber | Problem]:
    """Search numbers available to order

    Args:
        country (str | Unset):  Default: 'US'.
        area_code (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageAvailableNumber | Problem]
    """

    kwargs = _get_kwargs(
        country=country,
        area_code=area_code,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    country: str | Unset = "US",
    area_code: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> PageAvailableNumber | Problem | None:
    """Search numbers available to order

    Args:
        country (str | Unset):  Default: 'US'.
        area_code (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageAvailableNumber | Problem
    """

    return sync_detailed(
        client=client,
        country=country,
        area_code=area_code,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    country: str | Unset = "US",
    area_code: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> Response[PageAvailableNumber | Problem]:
    """Search numbers available to order

    Args:
        country (str | Unset):  Default: 'US'.
        area_code (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageAvailableNumber | Problem]
    """

    kwargs = _get_kwargs(
        country=country,
        area_code=area_code,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    country: str | Unset = "US",
    area_code: str | Unset = UNSET,
    limit: int | Unset = 20,
) -> PageAvailableNumber | Problem | None:
    """Search numbers available to order

    Args:
        country (str | Unset):  Default: 'US'.
        area_code (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageAvailableNumber | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            country=country,
            area_code=area_code,
            limit=limit,
        )
    ).parsed
