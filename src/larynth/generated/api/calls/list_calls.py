import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.call_page import CallPage
from ...models.list_calls_billed import ListCallsBilled
from ...models.list_calls_direction import (
    ListCallsDirection,
)
from ...models.list_calls_order import ListCallsOrder
from ...models.list_calls_sentiment import (
    ListCallsSentiment,
)
from ...models.list_calls_status import ListCallsStatus
from ...models.list_calls_web_tests import ListCallsWebTests
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    order: ListCallsOrder | Unset = "-started",
    status: ListCallsStatus | Unset = UNSET,
    direction: ListCallsDirection | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    assistant_id: list[str] | Unset = UNSET,
    number_id: list[str] | Unset = UNSET,
    web_tests: ListCallsWebTests | Unset = UNSET,
    outcome: list[str] | Unset = UNSET,
    billed: ListCallsBilled | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    caller_e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    sentiment: ListCallsSentiment | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    params["before"] = before

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order

    params["order"] = json_order

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction

    params["direction"] = json_direction

    json_campaign_id: str | Unset = UNSET
    if not isinstance(campaign_id, Unset):
        json_campaign_id = str(campaign_id)
    params["campaign_id"] = json_campaign_id

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    json_until: str | Unset = UNSET
    if not isinstance(until, Unset):
        json_until = until.isoformat()
    params["until"] = json_until

    json_assistant_id: list[str] | Unset = UNSET
    if not isinstance(assistant_id, Unset):
        json_assistant_id = assistant_id

    params["assistant_id"] = json_assistant_id

    json_number_id: list[str] | Unset = UNSET
    if not isinstance(number_id, Unset):
        json_number_id = number_id

    params["number_id"] = json_number_id

    json_web_tests: str | Unset = UNSET
    if not isinstance(web_tests, Unset):
        json_web_tests = web_tests

    params["web_tests"] = json_web_tests

    json_outcome: list[str] | Unset = UNSET
    if not isinstance(outcome, Unset):
        json_outcome = outcome

    params["outcome"] = json_outcome

    json_billed: str | Unset = UNSET
    if not isinstance(billed, Unset):
        json_billed = billed

    params["billed"] = json_billed

    json_contact_id: str | Unset = UNSET
    if not isinstance(contact_id, Unset):
        json_contact_id = str(contact_id)
    params["contact_id"] = json_contact_id

    params["caller_e164"] = caller_e164

    params["q"] = q

    params["flagged"] = flagged

    params["tag"] = tag

    json_sentiment: str | Unset = UNSET
    if not isinstance(sentiment, Unset):
        json_sentiment = sentiment

    params["sentiment"] = json_sentiment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/calls",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CallPage | Problem | None:
    if response.status_code == 200:
        response_200 = CallPage.from_dict(response.json())

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
) -> Response[CallPage | Problem]:
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
    before: str | Unset = UNSET,
    order: ListCallsOrder | Unset = "-started",
    status: ListCallsStatus | Unset = UNSET,
    direction: ListCallsDirection | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    assistant_id: list[str] | Unset = UNSET,
    number_id: list[str] | Unset = UNSET,
    web_tests: ListCallsWebTests | Unset = UNSET,
    outcome: list[str] | Unset = UNSET,
    billed: ListCallsBilled | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    caller_e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    sentiment: ListCallsSentiment | Unset = UNSET,
) -> Response[CallPage | Problem]:
    """List calls with filters; newest first unless order says otherwise

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        before (str | Unset): Opaque cursor from prev_cursor, or a call's cursor, for the newer
            page
        order (ListCallsOrder | Unset): duration and price need a window of at most 90 days
            Default: '-started'.
        status (ListCallsStatus | Unset):
        direction (ListCallsDirection | Unset):
        campaign_id (UUID | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        assistant_id (list[str] | Unset): Repeat the key for several
        number_id (list[str] | Unset):
        web_tests (ListCallsWebTests | Unset): The Web test line
        outcome (list[str] | Unset):
        billed (ListCallsBilled | Unset):
        contact_id (UUID | Unset):
        caller_e164 (str | Unset): Calls from or to this number
        q (str | Unset): Caller name, number digits (3 or more), call id prefix and summary words
        flagged (bool | Unset): Only flagged calls
        tag (str | Unset):
        sentiment (ListCallsSentiment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallPage | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        before=before,
        order=order,
        status=status,
        direction=direction,
        campaign_id=campaign_id,
        since=since,
        until=until,
        assistant_id=assistant_id,
        number_id=number_id,
        web_tests=web_tests,
        outcome=outcome,
        billed=billed,
        contact_id=contact_id,
        caller_e164=caller_e164,
        q=q,
        flagged=flagged,
        tag=tag,
        sentiment=sentiment,
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
    before: str | Unset = UNSET,
    order: ListCallsOrder | Unset = "-started",
    status: ListCallsStatus | Unset = UNSET,
    direction: ListCallsDirection | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    assistant_id: list[str] | Unset = UNSET,
    number_id: list[str] | Unset = UNSET,
    web_tests: ListCallsWebTests | Unset = UNSET,
    outcome: list[str] | Unset = UNSET,
    billed: ListCallsBilled | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    caller_e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    sentiment: ListCallsSentiment | Unset = UNSET,
) -> CallPage | Problem | None:
    """List calls with filters; newest first unless order says otherwise

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        before (str | Unset): Opaque cursor from prev_cursor, or a call's cursor, for the newer
            page
        order (ListCallsOrder | Unset): duration and price need a window of at most 90 days
            Default: '-started'.
        status (ListCallsStatus | Unset):
        direction (ListCallsDirection | Unset):
        campaign_id (UUID | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        assistant_id (list[str] | Unset): Repeat the key for several
        number_id (list[str] | Unset):
        web_tests (ListCallsWebTests | Unset): The Web test line
        outcome (list[str] | Unset):
        billed (ListCallsBilled | Unset):
        contact_id (UUID | Unset):
        caller_e164 (str | Unset): Calls from or to this number
        q (str | Unset): Caller name, number digits (3 or more), call id prefix and summary words
        flagged (bool | Unset): Only flagged calls
        tag (str | Unset):
        sentiment (ListCallsSentiment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallPage | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        after=after,
        before=before,
        order=order,
        status=status,
        direction=direction,
        campaign_id=campaign_id,
        since=since,
        until=until,
        assistant_id=assistant_id,
        number_id=number_id,
        web_tests=web_tests,
        outcome=outcome,
        billed=billed,
        contact_id=contact_id,
        caller_e164=caller_e164,
        q=q,
        flagged=flagged,
        tag=tag,
        sentiment=sentiment,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    order: ListCallsOrder | Unset = "-started",
    status: ListCallsStatus | Unset = UNSET,
    direction: ListCallsDirection | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    assistant_id: list[str] | Unset = UNSET,
    number_id: list[str] | Unset = UNSET,
    web_tests: ListCallsWebTests | Unset = UNSET,
    outcome: list[str] | Unset = UNSET,
    billed: ListCallsBilled | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    caller_e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    sentiment: ListCallsSentiment | Unset = UNSET,
) -> Response[CallPage | Problem]:
    """List calls with filters; newest first unless order says otherwise

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        before (str | Unset): Opaque cursor from prev_cursor, or a call's cursor, for the newer
            page
        order (ListCallsOrder | Unset): duration and price need a window of at most 90 days
            Default: '-started'.
        status (ListCallsStatus | Unset):
        direction (ListCallsDirection | Unset):
        campaign_id (UUID | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        assistant_id (list[str] | Unset): Repeat the key for several
        number_id (list[str] | Unset):
        web_tests (ListCallsWebTests | Unset): The Web test line
        outcome (list[str] | Unset):
        billed (ListCallsBilled | Unset):
        contact_id (UUID | Unset):
        caller_e164 (str | Unset): Calls from or to this number
        q (str | Unset): Caller name, number digits (3 or more), call id prefix and summary words
        flagged (bool | Unset): Only flagged calls
        tag (str | Unset):
        sentiment (ListCallsSentiment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallPage | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        before=before,
        order=order,
        status=status,
        direction=direction,
        campaign_id=campaign_id,
        since=since,
        until=until,
        assistant_id=assistant_id,
        number_id=number_id,
        web_tests=web_tests,
        outcome=outcome,
        billed=billed,
        contact_id=contact_id,
        caller_e164=caller_e164,
        q=q,
        flagged=flagged,
        tag=tag,
        sentiment=sentiment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    order: ListCallsOrder | Unset = "-started",
    status: ListCallsStatus | Unset = UNSET,
    direction: ListCallsDirection | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    assistant_id: list[str] | Unset = UNSET,
    number_id: list[str] | Unset = UNSET,
    web_tests: ListCallsWebTests | Unset = UNSET,
    outcome: list[str] | Unset = UNSET,
    billed: ListCallsBilled | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    caller_e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    sentiment: ListCallsSentiment | Unset = UNSET,
) -> CallPage | Problem | None:
    """List calls with filters; newest first unless order says otherwise

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        before (str | Unset): Opaque cursor from prev_cursor, or a call's cursor, for the newer
            page
        order (ListCallsOrder | Unset): duration and price need a window of at most 90 days
            Default: '-started'.
        status (ListCallsStatus | Unset):
        direction (ListCallsDirection | Unset):
        campaign_id (UUID | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        assistant_id (list[str] | Unset): Repeat the key for several
        number_id (list[str] | Unset):
        web_tests (ListCallsWebTests | Unset): The Web test line
        outcome (list[str] | Unset):
        billed (ListCallsBilled | Unset):
        contact_id (UUID | Unset):
        caller_e164 (str | Unset): Calls from or to this number
        q (str | Unset): Caller name, number digits (3 or more), call id prefix and summary words
        flagged (bool | Unset): Only flagged calls
        tag (str | Unset):
        sentiment (ListCallsSentiment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallPage | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            after=after,
            before=before,
            order=order,
            status=status,
            direction=direction,
            campaign_id=campaign_id,
            since=since,
            until=until,
            assistant_id=assistant_id,
            number_id=number_id,
            web_tests=web_tests,
            outcome=outcome,
            billed=billed,
            contact_id=contact_id,
            caller_e164=caller_e164,
            q=q,
            flagged=flagged,
            tag=tag,
            sentiment=sentiment,
        )
    ).parsed
