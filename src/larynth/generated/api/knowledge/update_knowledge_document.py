from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.knowledge_document import KnowledgeDocument
from ...models.problem import Problem
from ...models.update_knowledge_document_request import UpdateKnowledgeDocumentRequest
from ...types import Response


def _get_kwargs(
    id: UUID,
    document_id: UUID,
    *,
    body: UpdateKnowledgeDocumentRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/knowledge-bases/{id}/documents/{document_id}".format(
            id=quote(str(id), safe=""),
            document_id=quote(str(document_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> KnowledgeDocument | Problem | None:
    if response.status_code == 200:
        response_200 = KnowledgeDocument.from_dict(response.json())

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
) -> Response[KnowledgeDocument | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    document_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateKnowledgeDocumentRequest,
) -> Response[KnowledgeDocument | Problem]:
    """Leave a page or file out of the next build, or include it again

    Args:
        id (UUID):
        document_id (UUID):
        body (UpdateKnowledgeDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeDocument | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        document_id=document_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    document_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateKnowledgeDocumentRequest,
) -> KnowledgeDocument | Problem | None:
    """Leave a page or file out of the next build, or include it again

    Args:
        id (UUID):
        document_id (UUID):
        body (UpdateKnowledgeDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeDocument | Problem
    """

    return sync_detailed(
        id=id,
        document_id=document_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    document_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateKnowledgeDocumentRequest,
) -> Response[KnowledgeDocument | Problem]:
    """Leave a page or file out of the next build, or include it again

    Args:
        id (UUID):
        document_id (UUID):
        body (UpdateKnowledgeDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[KnowledgeDocument | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        document_id=document_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    document_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateKnowledgeDocumentRequest,
) -> KnowledgeDocument | Problem | None:
    """Leave a page or file out of the next build, or include it again

    Args:
        id (UUID):
        document_id (UUID):
        body (UpdateKnowledgeDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        KnowledgeDocument | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            document_id=document_id,
            client=client,
            body=body,
        )
    ).parsed
