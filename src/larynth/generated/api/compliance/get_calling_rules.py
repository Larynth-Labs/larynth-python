from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_calling_rules_purpose import (
    GetCallingRulesPurpose,
)
from ...models.list_calling_rule import ListCallingRule
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    purpose: GetCallingRulesPurpose | Unset = "informational",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_purpose: str | Unset = UNSET
    if not isinstance(purpose, Unset):
        json_purpose = purpose

    params["purpose"] = json_purpose

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/compliance/calling-rules",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListCallingRule | Problem | None:
    if response.status_code == 200:
        response_200 = ListCallingRule.from_dict(response.json())

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
) -> Response[ListCallingRule | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    purpose: GetCallingRulesPurpose | Unset = "informational",
) -> Response[ListCallingRule | Problem]:
    """Calling rules applied at dial time, per US state

    Args:
        purpose (GetCallingRulesPurpose | Unset):  Default: 'informational'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCallingRule | Problem]
    """

    kwargs = _get_kwargs(
        purpose=purpose,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    purpose: GetCallingRulesPurpose | Unset = "informational",
) -> ListCallingRule | Problem | None:
    """Calling rules applied at dial time, per US state

    Args:
        purpose (GetCallingRulesPurpose | Unset):  Default: 'informational'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCallingRule | Problem
    """

    return sync_detailed(
        client=client,
        purpose=purpose,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    purpose: GetCallingRulesPurpose | Unset = "informational",
) -> Response[ListCallingRule | Problem]:
    """Calling rules applied at dial time, per US state

    Args:
        purpose (GetCallingRulesPurpose | Unset):  Default: 'informational'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListCallingRule | Problem]
    """

    kwargs = _get_kwargs(
        purpose=purpose,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    purpose: GetCallingRulesPurpose | Unset = "informational",
) -> ListCallingRule | Problem | None:
    """Calling rules applied at dial time, per US state

    Args:
        purpose (GetCallingRulesPurpose | Unset):  Default: 'informational'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListCallingRule | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            purpose=purpose,
        )
    ).parsed
