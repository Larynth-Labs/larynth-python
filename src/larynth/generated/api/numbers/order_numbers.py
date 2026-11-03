from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.order_numbers_request import OrderNumbersRequest
from ...models.order_numbers_result import OrderNumbersResult
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    *,
    body: OrderNumbersRequest,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/numbers/orders",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OrderNumbersResult | Problem | None:
    if response.status_code == 202:
        response_202 = OrderNumbersResult.from_dict(response.json())

        return response_202

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OrderNumbersResult | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OrderNumbersRequest,
    idempotency_key: str,
) -> Response[OrderNumbersResult | Problem]:
    """Order 1 to 3 numbers with one spend decision; provisioning is asynchronous

    Args:
        idempotency_key (str): Replays within 24 h return the stored response; the same key with a
            different body returns 409
        body (OrderNumbersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderNumbersResult | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: OrderNumbersRequest,
    idempotency_key: str,
) -> OrderNumbersResult | Problem | None:
    """Order 1 to 3 numbers with one spend decision; provisioning is asynchronous

    Args:
        idempotency_key (str): Replays within 24 h return the stored response; the same key with a
            different body returns 409
        body (OrderNumbersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderNumbersResult | Problem
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OrderNumbersRequest,
    idempotency_key: str,
) -> Response[OrderNumbersResult | Problem]:
    """Order 1 to 3 numbers with one spend decision; provisioning is asynchronous

    Args:
        idempotency_key (str): Replays within 24 h return the stored response; the same key with a
            different body returns 409
        body (OrderNumbersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrderNumbersResult | Problem]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: OrderNumbersRequest,
    idempotency_key: str,
) -> OrderNumbersResult | Problem | None:
    """Order 1 to 3 numbers with one spend decision; provisioning is asynchronous

    Args:
        idempotency_key (str): Replays within 24 h return the stored response; the same key with a
            different body returns 409
        body (OrderNumbersRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrderNumbersResult | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
