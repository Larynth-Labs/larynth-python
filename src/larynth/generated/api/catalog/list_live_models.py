from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_live_model import ListLiveModel
from ...models.list_live_models_direction import (
    ListLiveModelsDirection,
)
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    direction: ListLiveModelsDirection | Unset = "inbound",
    language: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction

    params["direction"] = json_direction

    params["language"] = language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/live-models",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListLiveModel | Problem | None:
    if response.status_code == 200:
        response_200 = ListLiveModel.from_dict(response.json())

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
) -> Response[ListLiveModel | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    direction: ListLiveModelsDirection | Unset = "inbound",
    language: str | Unset = UNSET,
) -> Response[ListLiveModel | Problem]:
    """Live (speech-to-speech) models this workspace can pick, with their price per minute

    Args:
        direction (ListLiveModelsDirection | Unset): Call direction the prices are for Default:
            'inbound'.
        language (str | Unset): Only models that speak this language

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListLiveModel | Problem]
    """

    kwargs = _get_kwargs(
        direction=direction,
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    direction: ListLiveModelsDirection | Unset = "inbound",
    language: str | Unset = UNSET,
) -> ListLiveModel | Problem | None:
    """Live (speech-to-speech) models this workspace can pick, with their price per minute

    Args:
        direction (ListLiveModelsDirection | Unset): Call direction the prices are for Default:
            'inbound'.
        language (str | Unset): Only models that speak this language

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListLiveModel | Problem
    """

    return sync_detailed(
        client=client,
        direction=direction,
        language=language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    direction: ListLiveModelsDirection | Unset = "inbound",
    language: str | Unset = UNSET,
) -> Response[ListLiveModel | Problem]:
    """Live (speech-to-speech) models this workspace can pick, with their price per minute

    Args:
        direction (ListLiveModelsDirection | Unset): Call direction the prices are for Default:
            'inbound'.
        language (str | Unset): Only models that speak this language

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListLiveModel | Problem]
    """

    kwargs = _get_kwargs(
        direction=direction,
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    direction: ListLiveModelsDirection | Unset = "inbound",
    language: str | Unset = UNSET,
) -> ListLiveModel | Problem | None:
    """Live (speech-to-speech) models this workspace can pick, with their price per minute

    Args:
        direction (ListLiveModelsDirection | Unset): Call direction the prices are for Default:
            'inbound'.
        language (str | Unset): Only models that speak this language

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListLiveModel | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            direction=direction,
            language=language,
        )
    ).parsed
