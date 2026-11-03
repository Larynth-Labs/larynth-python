from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_guardrail_built_in import ListGuardrailBuiltIn
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    language: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["language"] = language

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/guardrails",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListGuardrailBuiltIn | Problem | None:
    if response.status_code == 200:
        response_200 = ListGuardrailBuiltIn.from_dict(response.json())

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
) -> Response[ListGuardrailBuiltIn | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    language: str | Unset = UNSET,
) -> Response[ListGuardrailBuiltIn | Problem]:
    """Built-in guardrail rules every agent follows; they cannot be switched off

    Args:
        language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListGuardrailBuiltIn | Problem]
    """

    kwargs = _get_kwargs(
        language=language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    language: str | Unset = UNSET,
) -> ListGuardrailBuiltIn | Problem | None:
    """Built-in guardrail rules every agent follows; they cannot be switched off

    Args:
        language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListGuardrailBuiltIn | Problem
    """

    return sync_detailed(
        client=client,
        language=language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    language: str | Unset = UNSET,
) -> Response[ListGuardrailBuiltIn | Problem]:
    """Built-in guardrail rules every agent follows; they cannot be switched off

    Args:
        language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListGuardrailBuiltIn | Problem]
    """

    kwargs = _get_kwargs(
        language=language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    language: str | Unset = UNSET,
) -> ListGuardrailBuiltIn | Problem | None:
    """Built-in guardrail rules every agent follows; they cannot be switched off

    Args:
        language (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListGuardrailBuiltIn | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            language=language,
        )
    ).parsed
