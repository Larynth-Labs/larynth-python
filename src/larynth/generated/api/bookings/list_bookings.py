import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_bookings_status_item import (
    ListBookingsStatusItem,
)
from ...models.list_bookings_when import ListBookingsWhen
from ...models.page_booking import PageBooking
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    when: ListBookingsWhen | Unset = "upcoming",
    connection_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    call_id: str | Unset = UNSET,
    status: list[ListBookingsStatusItem] | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    json_when: str | Unset = UNSET
    if not isinstance(when, Unset):
        json_when = when

    params["when"] = json_when

    json_connection_id: str | Unset = UNSET
    if not isinstance(connection_id, Unset):
        json_connection_id = str(connection_id)
    params["connection_id"] = json_connection_id

    json_assistant_id: str | Unset = UNSET
    if not isinstance(assistant_id, Unset):
        json_assistant_id = str(assistant_id)
    params["assistant_id"] = json_assistant_id

    params["call_id"] = call_id

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item: str = status_item_data
            json_status.append(status_item)

    params["status"] = json_status

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/bookings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageBooking | Problem | None:
    if response.status_code == 200:
        response_200 = PageBooking.from_dict(response.json())

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
) -> Response[PageBooking | Problem]:
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
    when: ListBookingsWhen | Unset = "upcoming",
    connection_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    call_id: str | Unset = UNSET,
    status: list[ListBookingsStatusItem] | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[PageBooking | Problem]:
    """List bookings agents made

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        when (ListBookingsWhen | Unset): upcoming sorts by start time ascending, past descending
            Default: 'upcoming'.
        connection_id (UUID | Unset):
        assistant_id (UUID | Unset):
        call_id (str | Unset):
        status (list[ListBookingsStatusItem] | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageBooking | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        when=when,
        connection_id=connection_id,
        assistant_id=assistant_id,
        call_id=call_id,
        status=status,
        from_=from_,
        to=to,
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
    when: ListBookingsWhen | Unset = "upcoming",
    connection_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    call_id: str | Unset = UNSET,
    status: list[ListBookingsStatusItem] | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> PageBooking | Problem | None:
    """List bookings agents made

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        when (ListBookingsWhen | Unset): upcoming sorts by start time ascending, past descending
            Default: 'upcoming'.
        connection_id (UUID | Unset):
        assistant_id (UUID | Unset):
        call_id (str | Unset):
        status (list[ListBookingsStatusItem] | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageBooking | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        after=after,
        when=when,
        connection_id=connection_id,
        assistant_id=assistant_id,
        call_id=call_id,
        status=status,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    when: ListBookingsWhen | Unset = "upcoming",
    connection_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    call_id: str | Unset = UNSET,
    status: list[ListBookingsStatusItem] | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> Response[PageBooking | Problem]:
    """List bookings agents made

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        when (ListBookingsWhen | Unset): upcoming sorts by start time ascending, past descending
            Default: 'upcoming'.
        connection_id (UUID | Unset):
        assistant_id (UUID | Unset):
        call_id (str | Unset):
        status (list[ListBookingsStatusItem] | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageBooking | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        when=when,
        connection_id=connection_id,
        assistant_id=assistant_id,
        call_id=call_id,
        status=status,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    when: ListBookingsWhen | Unset = "upcoming",
    connection_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
    call_id: str | Unset = UNSET,
    status: list[ListBookingsStatusItem] | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
) -> PageBooking | Problem | None:
    """List bookings agents made

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        when (ListBookingsWhen | Unset): upcoming sorts by start time ascending, past descending
            Default: 'upcoming'.
        connection_id (UUID | Unset):
        assistant_id (UUID | Unset):
        call_id (str | Unset):
        status (list[ListBookingsStatusItem] | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageBooking | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            after=after,
            when=when,
            connection_id=connection_id,
            assistant_id=assistant_id,
            call_id=call_id,
            status=status,
            from_=from_,
            to=to,
        )
    ).parsed
