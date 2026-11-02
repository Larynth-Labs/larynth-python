from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.knowledge_search_result import KnowledgeSearchResult
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    query: str,
    k: int | Unset = 3,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    params["k"] = k

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/knowledge-bases/{id}/search".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KnowledgeSearchResult | Problem | None:
    if response.status_code == 200:
        response_200 = KnowledgeSearchResult.from_dict(response.json())

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
) -> Response[KnowledgeSearchResult | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    query: str,
    k: int | Unset = 3,
) -> Response[KnowledgeSearchResult | Problem]:
    """Run a retrieval query against a knowledge base

    Args:
        id (UUID):
        query (str):
        k (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeSearchResult | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        query=query,
        k=k,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    query: str,
    k: int | Unset = 3,
) -> KnowledgeSearchResult | Problem | None:
    """Run a retrieval query against a knowledge base

    Args:
        id (UUID):
        query (str):
        k (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeSearchResult | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        query=query,
        k=k,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    query: str,
    k: int | Unset = 3,
) -> Response[KnowledgeSearchResult | Problem]:
    """Run a retrieval query against a knowledge base

    Args:
        id (UUID):
        query (str):
        k (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeSearchResult | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        query=query,
        k=k,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    query: str,
    k: int | Unset = 3,
) -> KnowledgeSearchResult | Problem | None:
    """Run a retrieval query against a knowledge base

    Args:
        id (UUID):
        query (str):
        k (int | Unset):  Default: 3.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeSearchResult | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            query=query,
            k=k,
        )
    ).parsed
