from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_webhook_messages_status import (
    ListWebhookMessagesStatus,
)
from ...models.page_webhook_message import PageWebhookMessage
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    status: ListWebhookMessagesStatus | Unset = UNSET,
    event_type: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params["event_type"] = event_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/webhooks/{id}/messages".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageWebhookMessage | Problem | None:
    if response.status_code == 200:
        response_200 = PageWebhookMessage.from_dict(response.json())

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
) -> Response[PageWebhookMessage | Problem]:
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
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    status: ListWebhookMessagesStatus | Unset = UNSET,
    event_type: str | Unset = UNSET,
) -> Response[PageWebhookMessage | Problem]:
    """One row per event sent to this endpoint, newest first (30 days)

    Args:
        id (UUID):
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        status (ListWebhookMessagesStatus | Unset):
        event_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageWebhookMessage | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        after=after,
        status=status,
        event_type=event_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    status: ListWebhookMessagesStatus | Unset = UNSET,
    event_type: str | Unset = UNSET,
) -> PageWebhookMessage | Problem | None:
    """One row per event sent to this endpoint, newest first (30 days)

    Args:
        id (UUID):
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        status (ListWebhookMessagesStatus | Unset):
        event_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageWebhookMessage | Problem
    """

    return sync_detailed(
        id=id,
        client=client,
        limit=limit,
        after=after,
        status=status,
        event_type=event_type,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    status: ListWebhookMessagesStatus | Unset = UNSET,
    event_type: str | Unset = UNSET,
) -> Response[PageWebhookMessage | Problem]:
    """One row per event sent to this endpoint, newest first (30 days)

    Args:
        id (UUID):
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        status (ListWebhookMessagesStatus | Unset):
        event_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageWebhookMessage | Problem]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        after=after,
        status=status,
        event_type=event_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    status: ListWebhookMessagesStatus | Unset = UNSET,
    event_type: str | Unset = UNSET,
) -> PageWebhookMessage | Problem | None:
    """One row per event sent to this endpoint, newest first (30 days)

    Args:
        id (UUID):
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        status (ListWebhookMessagesStatus | Unset):
        event_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageWebhookMessage | Problem
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            limit=limit,
            after=after,
            status=status,
            event_type=event_type,
        )
    ).parsed
