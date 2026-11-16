from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_practice_results_state import (
    ListPracticeResultsState,
)
from ...models.page_practice_result import PagePracticeResult
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    run_id: UUID,
    *,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    test_id: UUID | Unset = UNSET,
    state: ListPracticeResultsState | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    json_test_id: str | Unset = UNSET
    if not isinstance(test_id, Unset):
        json_test_id = str(test_id)
    params["test_id"] = json_test_id

    json_state: str | Unset = UNSET
    if not isinstance(state, Unset):
        json_state = state

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/practice-runs/{run_id}/results".format(
            run_id=quote(str(run_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PagePracticeResult | Problem | None:
    if response.status_code == 200:
        response_200 = PagePracticeResult.from_dict(response.json())

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
) -> Response[PagePracticeResult | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    test_id: UUID | Unset = UNSET,
    state: ListPracticeResultsState | Unset = UNSET,
) -> Response[PagePracticeResult | Problem]:
    """List the attempts of a practice run with transcript and checks

    Args:
        run_id (UUID):
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        test_id (UUID | Unset):
        state (ListPracticeResultsState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagePracticeResult | Problem]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        limit=limit,
        after=after,
        test_id=test_id,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    test_id: UUID | Unset = UNSET,
    state: ListPracticeResultsState | Unset = UNSET,
) -> PagePracticeResult | Problem | None:
    """List the attempts of a practice run with transcript and checks

    Args:
        run_id (UUID):
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        test_id (UUID | Unset):
        state (ListPracticeResultsState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagePracticeResult | Problem
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        limit=limit,
        after=after,
        test_id=test_id,
        state=state,
    ).parsed


async def asyncio_detailed(
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    test_id: UUID | Unset = UNSET,
    state: ListPracticeResultsState | Unset = UNSET,
) -> Response[PagePracticeResult | Problem]:
    """List the attempts of a practice run with transcript and checks

    Args:
        run_id (UUID):
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        test_id (UUID | Unset):
        state (ListPracticeResultsState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagePracticeResult | Problem]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        limit=limit,
        after=after,
        test_id=test_id,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    test_id: UUID | Unset = UNSET,
    state: ListPracticeResultsState | Unset = UNSET,
) -> PagePracticeResult | Problem | None:
    """List the attempts of a practice run with transcript and checks

    Args:
        run_id (UUID):
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        test_id (UUID | Unset):
        state (ListPracticeResultsState | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagePracticeResult | Problem
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            limit=limit,
            after=after,
            test_id=test_id,
            state=state,
        )
    ).parsed
