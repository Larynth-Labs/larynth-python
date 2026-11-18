from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_issues_sort import ListIssuesSort
from ...models.list_issues_status import ListIssuesStatus
from ...models.page_issue import PageIssue
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: ListIssuesStatus | Unset = "open",
    kind: list[str] | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    assignee: str | Unset = UNSET,
    call_id: str | Unset = UNSET,
    sort: ListIssuesSort | Unset = "impact",
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_kind: list[str] | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind

    params["kind"] = json_kind

    json_assistant_id: str | Unset = UNSET
    if not isinstance(assistant_id, Unset):
        json_assistant_id = str(assistant_id)
    params["assistant_id"] = json_assistant_id

    params["assignee"] = assignee

    params["call_id"] = call_id

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["limit"] = limit

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/issues",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageIssue | Problem | None:
    if response.status_code == 200:
        response_200 = PageIssue.from_dict(response.json())

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
) -> Response[PageIssue | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: ListIssuesStatus | Unset = "open",
    kind: list[str] | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    assignee: str | Unset = UNSET,
    call_id: str | Unset = UNSET,
    sort: ListIssuesSort | Unset = "impact",
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
) -> Response[PageIssue | Problem]:
    """List the problems found with your agents, worst first

    Args:
        status (ListIssuesStatus | Unset):  Default: 'open'.
        kind (list[str] | Unset): Comma-separated kinds
        assistant_id (UUID | Unset):
        assignee (str | Unset): me, none or a user id
        call_id (str | Unset): Only issues that happened on this call
        sort (ListIssuesSort | Unset):  Default: 'impact'.
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageIssue | Problem]
    """

    kwargs = _get_kwargs(
        status=status,
        kind=kind,
        assistant_id=assistant_id,
        assignee=assignee,
        call_id=call_id,
        sort=sort,
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
    status: ListIssuesStatus | Unset = "open",
    kind: list[str] | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    assignee: str | Unset = UNSET,
    call_id: str | Unset = UNSET,
    sort: ListIssuesSort | Unset = "impact",
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
) -> PageIssue | Problem | None:
    """List the problems found with your agents, worst first

    Args:
        status (ListIssuesStatus | Unset):  Default: 'open'.
        kind (list[str] | Unset): Comma-separated kinds
        assistant_id (UUID | Unset):
        assignee (str | Unset): me, none or a user id
        call_id (str | Unset): Only issues that happened on this call
        sort (ListIssuesSort | Unset):  Default: 'impact'.
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageIssue | Problem
    """

    return sync_detailed(
        client=client,
        status=status,
        kind=kind,
        assistant_id=assistant_id,
        assignee=assignee,
        call_id=call_id,
        sort=sort,
        limit=limit,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: ListIssuesStatus | Unset = "open",
    kind: list[str] | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    assignee: str | Unset = UNSET,
    call_id: str | Unset = UNSET,
    sort: ListIssuesSort | Unset = "impact",
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
) -> Response[PageIssue | Problem]:
    """List the problems found with your agents, worst first

    Args:
        status (ListIssuesStatus | Unset):  Default: 'open'.
        kind (list[str] | Unset): Comma-separated kinds
        assistant_id (UUID | Unset):
        assignee (str | Unset): me, none or a user id
        call_id (str | Unset): Only issues that happened on this call
        sort (ListIssuesSort | Unset):  Default: 'impact'.
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageIssue | Problem]
    """

    kwargs = _get_kwargs(
        status=status,
        kind=kind,
        assistant_id=assistant_id,
        assignee=assignee,
        call_id=call_id,
        sort=sort,
        limit=limit,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: ListIssuesStatus | Unset = "open",
    kind: list[str] | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    assignee: str | Unset = UNSET,
    call_id: str | Unset = UNSET,
    sort: ListIssuesSort | Unset = "impact",
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
) -> PageIssue | Problem | None:
    """List the problems found with your agents, worst first

    Args:
        status (ListIssuesStatus | Unset):  Default: 'open'.
        kind (list[str] | Unset): Comma-separated kinds
        assistant_id (UUID | Unset):
        assignee (str | Unset): me, none or a user id
        call_id (str | Unset): Only issues that happened on this call
        sort (ListIssuesSort | Unset):  Default: 'impact'.
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageIssue | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            kind=kind,
            assistant_id=assistant_id,
            assignee=assignee,
            call_id=call_id,
            sort=sort,
            limit=limit,
            after=after,
        )
    ).parsed
