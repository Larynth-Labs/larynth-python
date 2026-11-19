from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_catalog_price_estimate_direction import (
    GetCatalogPriceEstimateDirection,
)
from ...models.price_estimate import PriceEstimate
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    stt: UUID,
    llm: UUID,
    tts: UUID,
    voice: UUID | Unset = UNSET,
    direction: GetCatalogPriceEstimateDirection | Unset = "inbound",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_stt = str(stt)
    params["stt"] = json_stt

    json_llm = str(llm)
    params["llm"] = json_llm

    json_tts = str(tts)
    params["tts"] = json_tts

    json_voice: str | Unset = UNSET
    if not isinstance(voice, Unset):
        json_voice = str(voice)
    params["voice"] = json_voice

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction

    params["direction"] = json_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/price-estimate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PriceEstimate | Problem | None:
    if response.status_code == 200:
        response_200 = PriceEstimate.from_dict(response.json())

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
) -> Response[PriceEstimate | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    stt: UUID,
    llm: UUID,
    tts: UUID,
    voice: UUID | Unset = UNSET,
    direction: GetCatalogPriceEstimateDirection | Unset = "inbound",
) -> Response[PriceEstimate | Problem]:
    """Price per minute and expected latency of a model selection

    Args:
        stt (UUID): An enabled stt model id
        llm (UUID): An enabled llm model id
        tts (UUID): An enabled tts model id
        voice (UUID | Unset): An enabled voice of the tts model
        direction (GetCatalogPriceEstimateDirection | Unset):  Default: 'inbound'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PriceEstimate | Problem]
    """

    kwargs = _get_kwargs(
        stt=stt,
        llm=llm,
        tts=tts,
        voice=voice,
        direction=direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    stt: UUID,
    llm: UUID,
    tts: UUID,
    voice: UUID | Unset = UNSET,
    direction: GetCatalogPriceEstimateDirection | Unset = "inbound",
) -> PriceEstimate | Problem | None:
    """Price per minute and expected latency of a model selection

    Args:
        stt (UUID): An enabled stt model id
        llm (UUID): An enabled llm model id
        tts (UUID): An enabled tts model id
        voice (UUID | Unset): An enabled voice of the tts model
        direction (GetCatalogPriceEstimateDirection | Unset):  Default: 'inbound'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PriceEstimate | Problem
    """

    return sync_detailed(
        client=client,
        stt=stt,
        llm=llm,
        tts=tts,
        voice=voice,
        direction=direction,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    stt: UUID,
    llm: UUID,
    tts: UUID,
    voice: UUID | Unset = UNSET,
    direction: GetCatalogPriceEstimateDirection | Unset = "inbound",
) -> Response[PriceEstimate | Problem]:
    """Price per minute and expected latency of a model selection

    Args:
        stt (UUID): An enabled stt model id
        llm (UUID): An enabled llm model id
        tts (UUID): An enabled tts model id
        voice (UUID | Unset): An enabled voice of the tts model
        direction (GetCatalogPriceEstimateDirection | Unset):  Default: 'inbound'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PriceEstimate | Problem]
    """

    kwargs = _get_kwargs(
        stt=stt,
        llm=llm,
        tts=tts,
        voice=voice,
        direction=direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    stt: UUID,
    llm: UUID,
    tts: UUID,
    voice: UUID | Unset = UNSET,
    direction: GetCatalogPriceEstimateDirection | Unset = "inbound",
) -> PriceEstimate | Problem | None:
    """Price per minute and expected latency of a model selection

    Args:
        stt (UUID): An enabled stt model id
        llm (UUID): An enabled llm model id
        tts (UUID): An enabled tts model id
        voice (UUID | Unset): An enabled voice of the tts model
        direction (GetCatalogPriceEstimateDirection | Unset):  Default: 'inbound'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PriceEstimate | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            stt=stt,
            llm=llm,
            tts=tts,
            voice=voice,
            direction=direction,
        )
    ).parsed
