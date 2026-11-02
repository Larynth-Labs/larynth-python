from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_web_call_request import CreateWebCallRequest
from ...models.problem import Problem
from ...models.web_call import WebCall
from ...types import Response


def _get_kwargs(
    assistant_id: UUID,
    *,
    body: CreateWebCallRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assistants/{assistant_id}/web-calls".format(
            assistant_id=quote(str(assistant_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | WebCall | None:
    if response.status_code == 201:
        response_201 = WebCall.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = Problem.from_dict(response.json())

        return response_402

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

    if response.status_code == 502:
        response_502 = Problem.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | WebCall]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    assistant_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateWebCallRequest,
) -> Response[Problem | WebCall]:
    """Start a browser (WebRTC) test call to an assistant

    Args:
        assistant_id (UUID):
        body (CreateWebCallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebCall]
    """

    kwargs = _get_kwargs(
        assistant_id=assistant_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    assistant_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateWebCallRequest,
) -> Problem | WebCall | None:
    """Start a browser (WebRTC) test call to an assistant

    Args:
        assistant_id (UUID):
        body (CreateWebCallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebCall
    """

    return sync_detailed(
        assistant_id=assistant_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    assistant_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateWebCallRequest,
) -> Response[Problem | WebCall]:
    """Start a browser (WebRTC) test call to an assistant

    Args:
        assistant_id (UUID):
        body (CreateWebCallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | WebCall]
    """

    kwargs = _get_kwargs(
        assistant_id=assistant_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    assistant_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CreateWebCallRequest,
) -> Problem | WebCall | None:
    """Start a browser (WebRTC) test call to an assistant

    Args:
        assistant_id (UUID):
        body (CreateWebCallRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | WebCall
    """

    return (
        await asyncio_detailed(
            assistant_id=assistant_id,
            client=client,
            body=body,
        )
    ).parsed
