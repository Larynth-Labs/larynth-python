from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.knowledge_faq_source import KnowledgeFaqSource
from ...models.problem import Problem
from ...models.update_knowledge_faq_source_request import (
    UpdateKnowledgeFaqSourceRequest,
)
from ...types import Response


def _get_kwargs(
    id: UUID,
    source_id: UUID,
    *,
    body: UpdateKnowledgeFaqSourceRequest,
    if_match: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/knowledge-bases/{id}/sources/{source_id}/faq".format(
            id=quote(str(id), safe=""),
            source_id=quote(str(source_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KnowledgeFaqSource | Problem | None:
    if response.status_code == 200:
        response_200 = KnowledgeFaqSource.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = Problem.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = Problem.from_dict(response.json())

        return response_422

    if response.status_code == 428:
        response_428 = Problem.from_dict(response.json())

        return response_428

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
) -> Response[KnowledgeFaqSource | Problem]:
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
    body: UpdateKnowledgeFaqSourceRequest,
    if_match: str,
) -> Response[KnowledgeFaqSource | Problem]:
    """Replace the questions and answers of a FAQ source; the base rebuilds

    Args:
        id (UUID):
        source_id (UUID):
        if_match (str):
        body (UpdateKnowledgeFaqSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeFaqSource | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        source_id=source_id,
        body=body,
        if_match=if_match,
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
    body: UpdateKnowledgeFaqSourceRequest,
    if_match: str,
) -> KnowledgeFaqSource | Problem | None:
    """Replace the questions and answers of a FAQ source; the base rebuilds

    Args:
        id (UUID):
        source_id (UUID):
        if_match (str):
        body (UpdateKnowledgeFaqSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeFaqSource | Problem
    """

    return sync_detailed(
        id=id,
        source_id=source_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    source_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateKnowledgeFaqSourceRequest,
    if_match: str,
) -> Response[KnowledgeFaqSource | Problem]:
    """Replace the questions and answers of a FAQ source; the base rebuilds

    Args:
        id (UUID):
        source_id (UUID):
        if_match (str):
        body (UpdateKnowledgeFaqSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeFaqSource | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        source_id=source_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    source_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateKnowledgeFaqSourceRequest,
    if_match: str,
) -> KnowledgeFaqSource | Problem | None:
    """Replace the questions and answers of a FAQ source; the base rebuilds

    Args:
        id (UUID):
        source_id (UUID):
        if_match (str):
        body (UpdateKnowledgeFaqSourceRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeFaqSource | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            source_id=source_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
