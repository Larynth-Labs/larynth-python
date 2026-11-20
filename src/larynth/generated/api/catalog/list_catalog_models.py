from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_catalog_models_kind import (
    ListCatalogModelsKind,
)
from ...models.list_catalog_models_sort import (
    ListCatalogModelsSort,
)
from ...models.page_catalog_model import PageCatalogModel
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    kind: ListCatalogModelsKind | Unset = UNSET,
    language: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    sort: ListCatalogModelsSort | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind

    params["kind"] = json_kind

    params["language"] = language

    params["provider"] = provider

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/catalog/models",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PageCatalogModel | Problem | None:
    if response.status_code == 200:
        response_200 = PageCatalogModel.from_dict(response.json())

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
) -> Response[PageCatalogModel | Problem]:
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
    kind: ListCatalogModelsKind | Unset = UNSET,
    language: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    sort: ListCatalogModelsSort | Unset = UNSET,
) -> Response[PageCatalogModel | Problem]:
    """List enabled models

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        kind (ListCatalogModelsKind | Unset):
        language (str | Unset):
        provider (str | Unset): Only models of this provider key
        sort (ListCatalogModelsSort | Unset): latency: lowest typical_latency_ms first; quality:
            highest quality_score first; price: lowest premium first. Unknown values sort last; ties
            break on id. The cursor carries the sort key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageCatalogModel | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        kind=kind,
        language=language,
        provider=provider,
        sort=sort,
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
    kind: ListCatalogModelsKind | Unset = UNSET,
    language: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    sort: ListCatalogModelsSort | Unset = UNSET,
) -> PageCatalogModel | Problem | None:
    """List enabled models

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        kind (ListCatalogModelsKind | Unset):
        language (str | Unset):
        provider (str | Unset): Only models of this provider key
        sort (ListCatalogModelsSort | Unset): latency: lowest typical_latency_ms first; quality:
            highest quality_score first; price: lowest premium first. Unknown values sort last; ties
            break on id. The cursor carries the sort key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageCatalogModel | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        after=after,
        kind=kind,
        language=language,
        provider=provider,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    kind: ListCatalogModelsKind | Unset = UNSET,
    language: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    sort: ListCatalogModelsSort | Unset = UNSET,
) -> Response[PageCatalogModel | Problem]:
    """List enabled models

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        kind (ListCatalogModelsKind | Unset):
        language (str | Unset):
        provider (str | Unset): Only models of this provider key
        sort (ListCatalogModelsSort | Unset): latency: lowest typical_latency_ms first; quality:
            highest quality_score first; price: lowest premium first. Unknown values sort last; ties
            break on id. The cursor carries the sort key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageCatalogModel | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        kind=kind,
        language=language,
        provider=provider,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    kind: ListCatalogModelsKind | Unset = UNSET,
    language: str | Unset = UNSET,
    provider: str | Unset = UNSET,
    sort: ListCatalogModelsSort | Unset = UNSET,
) -> PageCatalogModel | Problem | None:
    """List enabled models

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        kind (ListCatalogModelsKind | Unset):
        language (str | Unset):
        provider (str | Unset): Only models of this provider key
        sort (ListCatalogModelsSort | Unset): latency: lowest typical_latency_ms first; quality:
            highest quality_score first; price: lowest premium first. Unknown values sort last; ties
            break on id. The cursor carries the sort key

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageCatalogModel | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            after=after,
            kind=kind,
            language=language,
            provider=provider,
            sort=sort,
        )
    ).parsed
