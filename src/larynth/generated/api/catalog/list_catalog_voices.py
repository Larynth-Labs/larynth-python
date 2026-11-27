from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_catalog_voices_gender import (
    ListCatalogVoicesGender,
)
from ...models.problem import Problem
from ...models.voice_page import VoicePage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    provider_key: str | Unset = UNSET,
    model_id: UUID | Unset = UNSET,
    q: str | Unset = UNSET,
    language: str | Unset = UNSET,
    gender: ListCatalogVoicesGender | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["provider_key"] = provider_key

    json_model_id: str | Unset = UNSET
    if not isinstance(model_id, Unset):
        json_model_id = str(model_id)
    params["model_id"] = json_model_id

    params["q"] = q

    params["language"] = language

    json_gender: str | Unset = UNSET
    if not isinstance(gender, Unset):
        json_gender = gender

    params["gender"] = json_gender

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/voices",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | VoicePage | None:
    if response.status_code == 200:
        response_200 = VoicePage.from_dict(response.json())

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
) -> Response[Problem | VoicePage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    provider_key: str | Unset = UNSET,
    model_id: UUID | Unset = UNSET,
    q: str | Unset = UNSET,
    language: str | Unset = UNSET,
    gender: ListCatalogVoicesGender | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[Problem | VoicePage]:
    """List enabled voices

    Args:
        provider_key (str | Unset): Only voices of this provider
        model_id (UUID | Unset): Only voices usable with this TTS model
        q (str | Unset): Case-insensitive search over name, description and tags
        language (str | Unset): Voices that speak this language; a region suffix is ignored
        gender (ListCatalogVoicesGender | Unset):
        limit (int | Unset): Page size Default: 50.
        cursor (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | VoicePage]
    """

    kwargs = _get_kwargs(
        provider_key=provider_key,
        model_id=model_id,
        q=q,
        language=language,
        gender=gender,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    provider_key: str | Unset = UNSET,
    model_id: UUID | Unset = UNSET,
    q: str | Unset = UNSET,
    language: str | Unset = UNSET,
    gender: ListCatalogVoicesGender | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Problem | VoicePage | None:
    """List enabled voices

    Args:
        provider_key (str | Unset): Only voices of this provider
        model_id (UUID | Unset): Only voices usable with this TTS model
        q (str | Unset): Case-insensitive search over name, description and tags
        language (str | Unset): Voices that speak this language; a region suffix is ignored
        gender (ListCatalogVoicesGender | Unset):
        limit (int | Unset): Page size Default: 50.
        cursor (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | VoicePage
    """

    return sync_detailed(
        client=client,
        provider_key=provider_key,
        model_id=model_id,
        q=q,
        language=language,
        gender=gender,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    provider_key: str | Unset = UNSET,
    model_id: UUID | Unset = UNSET,
    q: str | Unset = UNSET,
    language: str | Unset = UNSET,
    gender: ListCatalogVoicesGender | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Response[Problem | VoicePage]:
    """List enabled voices

    Args:
        provider_key (str | Unset): Only voices of this provider
        model_id (UUID | Unset): Only voices usable with this TTS model
        q (str | Unset): Case-insensitive search over name, description and tags
        language (str | Unset): Voices that speak this language; a region suffix is ignored
        gender (ListCatalogVoicesGender | Unset):
        limit (int | Unset): Page size Default: 50.
        cursor (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | VoicePage]
    """

    kwargs = _get_kwargs(
        provider_key=provider_key,
        model_id=model_id,
        q=q,
        language=language,
        gender=gender,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    provider_key: str | Unset = UNSET,
    model_id: UUID | Unset = UNSET,
    q: str | Unset = UNSET,
    language: str | Unset = UNSET,
    gender: ListCatalogVoicesGender | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
) -> Problem | VoicePage | None:
    """List enabled voices

    Args:
        provider_key (str | Unset): Only voices of this provider
        model_id (UUID | Unset): Only voices usable with this TTS model
        q (str | Unset): Case-insensitive search over name, description and tags
        language (str | Unset): Voices that speak this language; a region suffix is ignored
        gender (ListCatalogVoicesGender | Unset):
        limit (int | Unset): Page size Default: 50.
        cursor (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | VoicePage
    """

    return (
        await asyncio_detailed(
            client=client,
            provider_key=provider_key,
            model_id=model_id,
            q=q,
            language=language,
            gender=gender,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
