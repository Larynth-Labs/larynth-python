import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.calls_summary import CallsSummary
from ...models.get_calls_summary_billed import (
    GetCallsSummaryBilled,
)
from ...models.get_calls_summary_direction import (
    GetCallsSummaryDirection,
)
from ...models.get_calls_summary_group_by import (
    GetCallsSummaryGroupBy,
)
from ...models.get_calls_summary_sentiment import (
    GetCallsSummarySentiment,
)
from ...models.get_calls_summary_status import (
    GetCallsSummaryStatus,
)
from ...models.get_calls_summary_web_tests import (
    GetCallsSummaryWebTests,
)
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: GetCallsSummaryStatus | Unset = UNSET,
    direction: GetCallsSummaryDirection | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    group_by: GetCallsSummaryGroupBy | Unset = "none",
    assistant_id: list[str] | Unset = UNSET,
    number_id: list[str] | Unset = UNSET,
    web_tests: GetCallsSummaryWebTests | Unset = UNSET,
    outcome: list[str] | Unset = UNSET,
    billed: GetCallsSummaryBilled | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    caller_e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    sentiment: GetCallsSummarySentiment | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

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

    json_group_by: str | Unset = UNSET
    if not isinstance(group_by, Unset):
        json_group_by = group_by

    params["group_by"] = json_group_by

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
        "url": "/v1/calls/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CallsSummary | Problem | None:
    if response.status_code == 200:
        response_200 = CallsSummary.from_dict(response.json())

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
) -> Response[CallsSummary | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: GetCallsSummaryStatus | Unset = UNSET,
    direction: GetCallsSummaryDirection | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    group_by: GetCallsSummaryGroupBy | Unset = "none",
    assistant_id: list[str] | Unset = UNSET,
    number_id: list[str] | Unset = UNSET,
    web_tests: GetCallsSummaryWebTests | Unset = UNSET,
    outcome: list[str] | Unset = UNSET,
    billed: GetCallsSummaryBilled | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    caller_e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    sentiment: GetCallsSummarySentiment | Unset = UNSET,
) -> Response[CallsSummary | Problem]:
    """Totals for a call filter: counts, billed time, spend and not-billed split

    Args:
        status (GetCallsSummaryStatus | Unset):
        direction (GetCallsSummaryDirection | Unset):
        campaign_id (UUID | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        group_by (GetCallsSummaryGroupBy | Unset):  Default: 'none'.
        assistant_id (list[str] | Unset): Repeat the key for several
        number_id (list[str] | Unset):
        web_tests (GetCallsSummaryWebTests | Unset): The Web test line
        outcome (list[str] | Unset):
        billed (GetCallsSummaryBilled | Unset):
        contact_id (UUID | Unset):
        caller_e164 (str | Unset): Calls from or to this number
        q (str | Unset): Caller name, number digits (3 or more), call id prefix and summary words
        flagged (bool | Unset): Only flagged calls
        tag (str | Unset):
        sentiment (GetCallsSummarySentiment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallsSummary | Problem]
    """

    kwargs = _get_kwargs(
        status=status,
        direction=direction,
        campaign_id=campaign_id,
        since=since,
        until=until,
        group_by=group_by,
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
    status: GetCallsSummaryStatus | Unset = UNSET,
    direction: GetCallsSummaryDirection | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    group_by: GetCallsSummaryGroupBy | Unset = "none",
    assistant_id: list[str] | Unset = UNSET,
    number_id: list[str] | Unset = UNSET,
    web_tests: GetCallsSummaryWebTests | Unset = UNSET,
    outcome: list[str] | Unset = UNSET,
    billed: GetCallsSummaryBilled | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    caller_e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    sentiment: GetCallsSummarySentiment | Unset = UNSET,
) -> CallsSummary | Problem | None:
    """Totals for a call filter: counts, billed time, spend and not-billed split

    Args:
        status (GetCallsSummaryStatus | Unset):
        direction (GetCallsSummaryDirection | Unset):
        campaign_id (UUID | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        group_by (GetCallsSummaryGroupBy | Unset):  Default: 'none'.
        assistant_id (list[str] | Unset): Repeat the key for several
        number_id (list[str] | Unset):
        web_tests (GetCallsSummaryWebTests | Unset): The Web test line
        outcome (list[str] | Unset):
        billed (GetCallsSummaryBilled | Unset):
        contact_id (UUID | Unset):
        caller_e164 (str | Unset): Calls from or to this number
        q (str | Unset): Caller name, number digits (3 or more), call id prefix and summary words
        flagged (bool | Unset): Only flagged calls
        tag (str | Unset):
        sentiment (GetCallsSummarySentiment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallsSummary | Problem
    """

    return sync_detailed(
        client=client,
        status=status,
        direction=direction,
        campaign_id=campaign_id,
        since=since,
        until=until,
        group_by=group_by,
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
    status: GetCallsSummaryStatus | Unset = UNSET,
    direction: GetCallsSummaryDirection | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    group_by: GetCallsSummaryGroupBy | Unset = "none",
    assistant_id: list[str] | Unset = UNSET,
    number_id: list[str] | Unset = UNSET,
    web_tests: GetCallsSummaryWebTests | Unset = UNSET,
    outcome: list[str] | Unset = UNSET,
    billed: GetCallsSummaryBilled | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    caller_e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    sentiment: GetCallsSummarySentiment | Unset = UNSET,
) -> Response[CallsSummary | Problem]:
    """Totals for a call filter: counts, billed time, spend and not-billed split

    Args:
        status (GetCallsSummaryStatus | Unset):
        direction (GetCallsSummaryDirection | Unset):
        campaign_id (UUID | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        group_by (GetCallsSummaryGroupBy | Unset):  Default: 'none'.
        assistant_id (list[str] | Unset): Repeat the key for several
        number_id (list[str] | Unset):
        web_tests (GetCallsSummaryWebTests | Unset): The Web test line
        outcome (list[str] | Unset):
        billed (GetCallsSummaryBilled | Unset):
        contact_id (UUID | Unset):
        caller_e164 (str | Unset): Calls from or to this number
        q (str | Unset): Caller name, number digits (3 or more), call id prefix and summary words
        flagged (bool | Unset): Only flagged calls
        tag (str | Unset):
        sentiment (GetCallsSummarySentiment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CallsSummary | Problem]
    """

    kwargs = _get_kwargs(
        status=status,
        direction=direction,
        campaign_id=campaign_id,
        since=since,
        until=until,
        group_by=group_by,
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
    status: GetCallsSummaryStatus | Unset = UNSET,
    direction: GetCallsSummaryDirection | Unset = UNSET,
    campaign_id: UUID | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    group_by: GetCallsSummaryGroupBy | Unset = "none",
    assistant_id: list[str] | Unset = UNSET,
    number_id: list[str] | Unset = UNSET,
    web_tests: GetCallsSummaryWebTests | Unset = UNSET,
    outcome: list[str] | Unset = UNSET,
    billed: GetCallsSummaryBilled | Unset = UNSET,
    contact_id: UUID | Unset = UNSET,
    caller_e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    tag: str | Unset = UNSET,
    sentiment: GetCallsSummarySentiment | Unset = UNSET,
) -> CallsSummary | Problem | None:
    """Totals for a call filter: counts, billed time, spend and not-billed split

    Args:
        status (GetCallsSummaryStatus | Unset):
        direction (GetCallsSummaryDirection | Unset):
        campaign_id (UUID | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        group_by (GetCallsSummaryGroupBy | Unset):  Default: 'none'.
        assistant_id (list[str] | Unset): Repeat the key for several
        number_id (list[str] | Unset):
        web_tests (GetCallsSummaryWebTests | Unset): The Web test line
        outcome (list[str] | Unset):
        billed (GetCallsSummaryBilled | Unset):
        contact_id (UUID | Unset):
        caller_e164 (str | Unset): Calls from or to this number
        q (str | Unset): Caller name, number digits (3 or more), call id prefix and summary words
        flagged (bool | Unset): Only flagged calls
        tag (str | Unset):
        sentiment (GetCallsSummarySentiment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CallsSummary | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            direction=direction,
            campaign_id=campaign_id,
            since=since,
            until=until,
            group_by=group_by,
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
