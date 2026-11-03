from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.campaign_page import CampaignPage
from ...models.list_campaigns_display_status import (
    ListCampaignsDisplayStatus,
)
from ...models.list_campaigns_status import (
    ListCampaignsStatus,
)
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    status: ListCampaignsStatus | Unset = UNSET,
    display_status: ListCampaignsDisplayStatus | Unset = UNSET,
    number_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_display_status: str | Unset = UNSET
    if not isinstance(display_status, Unset):
        json_display_status = display_status

    params["display_status"] = json_display_status

    json_number_id: str | Unset = UNSET
    if not isinstance(number_id, Unset):
        json_number_id = str(number_id)
    params["number_id"] = json_number_id

    json_assistant_id: str | Unset = UNSET
    if not isinstance(assistant_id, Unset):
        json_assistant_id = str(assistant_id)
    params["assistant_id"] = json_assistant_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/campaigns",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CampaignPage | Problem | None:
    if response.status_code == 200:
        response_200 = CampaignPage.from_dict(response.json())

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
) -> Response[CampaignPage | Problem]:
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
    status: ListCampaignsStatus | Unset = UNSET,
    display_status: ListCampaignsDisplayStatus | Unset = UNSET,
    number_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
) -> Response[CampaignPage | Problem]:
    """List campaigns

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        status (ListCampaignsStatus | Unset):
        display_status (ListCampaignsDisplayStatus | Unset):
        number_id (UUID | Unset):
        assistant_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignPage | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        status=status,
        display_status=display_status,
        number_id=number_id,
        assistant_id=assistant_id,
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
    status: ListCampaignsStatus | Unset = UNSET,
    display_status: ListCampaignsDisplayStatus | Unset = UNSET,
    number_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
) -> CampaignPage | Problem | None:
    """List campaigns

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        status (ListCampaignsStatus | Unset):
        display_status (ListCampaignsDisplayStatus | Unset):
        number_id (UUID | Unset):
        assistant_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignPage | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        after=after,
        status=status,
        display_status=display_status,
        number_id=number_id,
        assistant_id=assistant_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    status: ListCampaignsStatus | Unset = UNSET,
    display_status: ListCampaignsDisplayStatus | Unset = UNSET,
    number_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
) -> Response[CampaignPage | Problem]:
    """List campaigns

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        status (ListCampaignsStatus | Unset):
        display_status (ListCampaignsDisplayStatus | Unset):
        number_id (UUID | Unset):
        assistant_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CampaignPage | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        status=status,
        display_status=display_status,
        number_id=number_id,
        assistant_id=assistant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    status: ListCampaignsStatus | Unset = UNSET,
    display_status: ListCampaignsDisplayStatus | Unset = UNSET,
    number_id: UUID | Unset = UNSET,
    assistant_id: UUID | Unset = UNSET,
) -> CampaignPage | Problem | None:
    """List campaigns

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        status (ListCampaignsStatus | Unset):
        display_status (ListCampaignsDisplayStatus | Unset):
        number_id (UUID | Unset):
        assistant_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CampaignPage | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            after=after,
            status=status,
            display_status=display_status,
            number_id=number_id,
            assistant_id=assistant_id,
        )
    ).parsed
