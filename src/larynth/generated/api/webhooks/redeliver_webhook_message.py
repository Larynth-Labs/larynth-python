from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.webhook_message import WebhookMessage
from ...types import Response


def _get_kwargs(
    id: UUID,
    event_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/{id}/messages/{event_id}/redeliver".format(
            id=quote(str(id), safe=""),
            event_id=quote(str(event_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | WebhookMessage | None:
    if response.status_code == 202:
        response_202 = WebhookMessage.from_dict(response.json())

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
) -> Response[Problem | WebhookMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | WebhookMessage]:
    """Send the same event again as a new attempt series signed with the current secret

    Args:
        id (UUID):
        event_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookMessage]
    """

    kwargs = _get_kwargs(
        id=id,
        event_id=event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Problem | WebhookMessage | None:
    """Send the same event again as a new attempt series signed with the current secret

    Args:
        id (UUID):
        event_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookMessage
    """

    return sync_detailed(
        id=id,
        event_id=event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Problem | WebhookMessage]:
    """Send the same event again as a new attempt series signed with the current secret

    Args:
        id (UUID):
        event_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebhookMessage]
    """

    kwargs = _get_kwargs(
        id=id,
        event_id=event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    event_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Problem | WebhookMessage | None:
    """Send the same event again as a new attempt series signed with the current secret

    Args:
        id (UUID):
        event_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebhookMessage
    """

    return (
        await asyncio_detailed(
            id=id,
            event_id=event_id,
            client=client,
        )
    ).parsed
