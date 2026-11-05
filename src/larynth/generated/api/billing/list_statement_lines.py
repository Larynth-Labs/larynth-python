import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_statement_lines_group import (
    ListStatementLinesGroup,
)
from ...models.problem import Problem
from ...models.statement_line_page import StatementLinePage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group: ListStatementLinesGroup | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_group: str | Unset = UNSET
    if not isinstance(group, Unset):
        json_group = group

    params["group"] = json_group

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["limit"] = limit

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/billing/statement-lines",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | StatementLinePage | None:
    if response.status_code == 200:
        response_200 = StatementLinePage.from_dict(response.json())

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
) -> Response[Problem | StatementLinePage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group: ListStatementLinesGroup | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
) -> Response[Problem | StatementLinePage]:
    """Statement lines, newest first: calls rolled up per local day, every other ledger transaction one
    line, holds hidden

    Args:
        group (ListStatementLinesGroup | Unset):
        from_ (datetime.date | Unset): First local day
        to (datetime.date | Unset): Last local day
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | StatementLinePage]
    """

    kwargs = _get_kwargs(
        group=group,
        from_=from_,
        to=to,
        limit=limit,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group: ListStatementLinesGroup | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
) -> Problem | StatementLinePage | None:
    """Statement lines, newest first: calls rolled up per local day, every other ledger transaction one
    line, holds hidden

    Args:
        group (ListStatementLinesGroup | Unset):
        from_ (datetime.date | Unset): First local day
        to (datetime.date | Unset): Last local day
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | StatementLinePage
    """

    return sync_detailed(
        client=client,
        group=group,
        from_=from_,
        to=to,
        limit=limit,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group: ListStatementLinesGroup | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
) -> Response[Problem | StatementLinePage]:
    """Statement lines, newest first: calls rolled up per local day, every other ledger transaction one
    line, holds hidden

    Args:
        group (ListStatementLinesGroup | Unset):
        from_ (datetime.date | Unset): First local day
        to (datetime.date | Unset): Last local day
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | StatementLinePage]
    """

    kwargs = _get_kwargs(
        group=group,
        from_=from_,
        to=to,
        limit=limit,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group: ListStatementLinesGroup | Unset = UNSET,
    from_: datetime.date | Unset = UNSET,
    to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
) -> Problem | StatementLinePage | None:
    """Statement lines, newest first: calls rolled up per local day, every other ledger transaction one
    line, holds hidden

    Args:
        group (ListStatementLinesGroup | Unset):
        from_ (datetime.date | Unset): First local day
        to (datetime.date | Unset): Last local day
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | StatementLinePage
    """

    return (
        await asyncio_detailed(
            client=client,
            group=group,
            from_=from_,
            to=to,
            limit=limit,
            after=after,
        )
    ).parsed
