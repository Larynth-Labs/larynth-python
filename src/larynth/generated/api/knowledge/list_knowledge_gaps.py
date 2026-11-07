from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_knowledge_gaps_state import (
    ListKnowledgeGapsState,
)
from ...models.page_knowledge_gap import PageKnowledgeGap
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    knowledge_base_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    state: ListKnowledgeGapsState | Unset = "open",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    json_knowledge_base_id: str | Unset = UNSET
    if not isinstance(knowledge_base_id, Unset):
        json_knowledge_base_id = str(knowledge_base_id)
    params["knowledge_base_id"] = json_knowledge_base_id

    json_assistant_id: str | Unset = UNSET
    if not isinstance(assistant_id, Unset):
        json_assistant_id = str(assistant_id)
    params["assistant_id"] = json_assistant_id

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/knowledge-gaps",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageKnowledgeGap | Problem | None:
    if response.status_code == 200:
        response_200 = PageKnowledgeGap.from_dict(response.json())

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
) -> Response[PageKnowledgeGap | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    knowledge_base_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    state: ListKnowledgeGapsState | Unset = "open",
) -> Response[PageKnowledgeGap | Problem]:
    """Questions callers asked that agents could not answer, grouped by similar wording

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        knowledge_base_id (UUID | Unset): Only questions asked of agents that had this base
            attached
        assistant_id (UUID | Unset):
        state (ListKnowledgeGapsState | Unset):  Default: 'open'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageKnowledgeGap | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        knowledge_base_id=knowledge_base_id,
        assistant_id=assistant_id,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    knowledge_base_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    state: ListKnowledgeGapsState | Unset = "open",
) -> PageKnowledgeGap | Problem | None:
    """Questions callers asked that agents could not answer, grouped by similar wording

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        knowledge_base_id (UUID | Unset): Only questions asked of agents that had this base
            attached
        assistant_id (UUID | Unset):
        state (ListKnowledgeGapsState | Unset):  Default: 'open'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageKnowledgeGap | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        after=after,
        knowledge_base_id=knowledge_base_id,
        assistant_id=assistant_id,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    knowledge_base_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    state: ListKnowledgeGapsState | Unset = "open",
) -> Response[PageKnowledgeGap | Problem]:
    """Questions callers asked that agents could not answer, grouped by similar wording

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        knowledge_base_id (UUID | Unset): Only questions asked of agents that had this base
            attached
        assistant_id (UUID | Unset):
        state (ListKnowledgeGapsState | Unset):  Default: 'open'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageKnowledgeGap | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        knowledge_base_id=knowledge_base_id,
        assistant_id=assistant_id,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    knowledge_base_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    state: ListKnowledgeGapsState | Unset = "open",
) -> PageKnowledgeGap | Problem | None:
    """Questions callers asked that agents could not answer, grouped by similar wording

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        knowledge_base_id (UUID | Unset): Only questions asked of agents that had this base
            attached
        assistant_id (UUID | Unset):
        state (ListKnowledgeGapsState | Unset):  Default: 'open'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageKnowledgeGap | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            after=after,
            knowledge_base_id=knowledge_base_id,
            assistant_id=assistant_id,
            state=state,
        )
    ).parsed
