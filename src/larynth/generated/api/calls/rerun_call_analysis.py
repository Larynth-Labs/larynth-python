from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_analysis_rerun import CallAnalysisRerun
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    call_id: str,
    *,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/calls/{call_id}/analysis/rerun".format(
            call_id=quote(str(call_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CallAnalysisRerun | Problem | None:
    if response.status_code == 202:
        response_202 = CallAnalysisRerun.from_dict(response.json())

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
) -> Response[CallAnalysisRerun | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    call_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> Response[CallAnalysisRerun | Problem]:
    """Make the call's summary and extracted data again; once per call per 10 minutes

    Args:
        call_id (str): <cell>_<ULID>
        idempotency_key (str): Replays within 24 h return the stored response; the same key with a
            different body returns 409

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallAnalysisRerun | Problem]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    call_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> CallAnalysisRerun | Problem | None:
    """Make the call's summary and extracted data again; once per call per 10 minutes

    Args:
        call_id (str): <cell>_<ULID>
        idempotency_key (str): Replays within 24 h return the stored response; the same key with a
            different body returns 409

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallAnalysisRerun | Problem
    """

    return sync_detailed(
        call_id=call_id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    call_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> Response[CallAnalysisRerun | Problem]:
    """Make the call's summary and extracted data again; once per call per 10 minutes

    Args:
        call_id (str): <cell>_<ULID>
        idempotency_key (str): Replays within 24 h return the stored response; the same key with a
            different body returns 409

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallAnalysisRerun | Problem]
    """

    kwargs = _get_kwargs(
        call_id=call_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    call_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str,
) -> CallAnalysisRerun | Problem | None:
    """Make the call's summary and extracted data again; once per call per 10 minutes

    Args:
        call_id (str): <cell>_<ULID>
        idempotency_key (str): Replays within 24 h return the stored response; the same key with a
            different body returns 409

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallAnalysisRerun | Problem
    """

    return (
        await asyncio_detailed(
            call_id=call_id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
