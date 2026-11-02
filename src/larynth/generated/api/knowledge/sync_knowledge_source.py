from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.knowledge_source import KnowledgeSource
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    id: UUID,
    source_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/knowledge-bases/{id}/sources/{source_id}/sync".format(
            id=quote(str(id), safe=""),
            source_id=quote(str(source_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KnowledgeSource | Problem | None:
    if response.status_code == 202:
        response_202 = KnowledgeSource.from_dict(response.json())

        return response_202

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
) -> Response[KnowledgeSource | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    source_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[KnowledgeSource | Problem]:
    """Re-fetch a website or re-read a file

    Args:
        id (UUID):
        source_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeSource | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        source_id=source_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    source_id: UUID,
    *,
    client: AuthenticatedClient,
) -> KnowledgeSource | Problem | None:
    """Re-fetch a website or re-read a file

    Args:
        id (UUID):
        source_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeSource | Problem
    """

    return sync_detailed(
        id=id,
        source_id=source_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    source_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[KnowledgeSource | Problem]:
    """Re-fetch a website or re-read a file

    Args:
        id (UUID):
        source_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeSource | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        source_id=source_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    source_id: UUID,
    *,
    client: AuthenticatedClient,
) -> KnowledgeSource | Problem | None:
    """Re-fetch a website or re-read a file

    Args:
        id (UUID):
        source_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeSource | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            source_id=source_id,
            client=client,
        )
    ).parsed
