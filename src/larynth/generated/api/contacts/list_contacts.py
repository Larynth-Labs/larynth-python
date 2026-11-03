from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact_page import ContactPage
from ...models.list_contacts_order import ListContactsOrder
from ...models.list_contacts_purpose import (
    ListContactsPurpose,
)
from ...models.list_contacts_view import ListContactsView
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    view: ListContactsView | Unset = "all",
    purpose: ListContactsPurpose | Unset = "informational",
    tag: list[str] | Unset = UNSET,
    import_id: UUID | Unset = UNSET,
    order: ListContactsOrder | Unset = "name",
    before: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    params["e164"] = e164

    params["q"] = q

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view

    params["view"] = json_view

    json_purpose: str | Unset = UNSET
    if not isinstance(purpose, Unset):
        json_purpose = purpose

    params["purpose"] = json_purpose

    json_tag: list[str] | Unset = UNSET
    if not isinstance(tag, Unset):
        json_tag = tag

    params["tag"] = json_tag

    json_import_id: str | Unset = UNSET
    if not isinstance(import_id, Unset):
        json_import_id = str(import_id)
    params["import_id"] = json_import_id

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order

    params["order"] = json_order

    params["before"] = before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/contacts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContactPage | Problem | None:
    if response.status_code == 200:
        response_200 = ContactPage.from_dict(response.json())

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
) -> Response[ContactPage | Problem]:
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
    e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    view: ListContactsView | Unset = "all",
    purpose: ListContactsPurpose | Unset = "informational",
    tag: list[str] | Unset = UNSET,
    import_id: UUID | Unset = UNSET,
    order: ListContactsOrder | Unset = "name",
    before: str | Unset = UNSET,
) -> Response[ContactPage | Problem]:
    """List contacts

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):
        q (str | Unset): Name, at least 3 digits of the number, or a tag
        view (ListContactsView | Unset):  Default: 'all'.
        purpose (ListContactsPurpose | Unset): Which callability view=callable uses Default:
            'informational'.
        tag (list[str] | Unset):
        import_id (UUID | Unset):
        order (ListContactsOrder | Unset):  Default: 'name'.
        before (str | Unset): Opaque cursor from prev_cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactPage | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        e164=e164,
        q=q,
        view=view,
        purpose=purpose,
        tag=tag,
        import_id=import_id,
        order=order,
        before=before,
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
    e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    view: ListContactsView | Unset = "all",
    purpose: ListContactsPurpose | Unset = "informational",
    tag: list[str] | Unset = UNSET,
    import_id: UUID | Unset = UNSET,
    order: ListContactsOrder | Unset = "name",
    before: str | Unset = UNSET,
) -> ContactPage | Problem | None:
    """List contacts

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):
        q (str | Unset): Name, at least 3 digits of the number, or a tag
        view (ListContactsView | Unset):  Default: 'all'.
        purpose (ListContactsPurpose | Unset): Which callability view=callable uses Default:
            'informational'.
        tag (list[str] | Unset):
        import_id (UUID | Unset):
        order (ListContactsOrder | Unset):  Default: 'name'.
        before (str | Unset): Opaque cursor from prev_cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactPage | Problem
    """

    return sync_detailed(
        client=client,
        limit=limit,
        after=after,
        e164=e164,
        q=q,
        view=view,
        purpose=purpose,
        tag=tag,
        import_id=import_id,
        order=order,
        before=before,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    view: ListContactsView | Unset = "all",
    purpose: ListContactsPurpose | Unset = "informational",
    tag: list[str] | Unset = UNSET,
    import_id: UUID | Unset = UNSET,
    order: ListContactsOrder | Unset = "name",
    before: str | Unset = UNSET,
) -> Response[ContactPage | Problem]:
    """List contacts

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):
        q (str | Unset): Name, at least 3 digits of the number, or a tag
        view (ListContactsView | Unset):  Default: 'all'.
        purpose (ListContactsPurpose | Unset): Which callability view=callable uses Default:
            'informational'.
        tag (list[str] | Unset):
        import_id (UUID | Unset):
        order (ListContactsOrder | Unset):  Default: 'name'.
        before (str | Unset): Opaque cursor from prev_cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactPage | Problem]
    """

    kwargs = _get_kwargs(
        limit=limit,
        after=after,
        e164=e164,
        q=q,
        view=view,
        purpose=purpose,
        tag=tag,
        import_id=import_id,
        order=order,
        before=before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 50,
    after: str | Unset = UNSET,
    e164: str | Unset = UNSET,
    q: str | Unset = UNSET,
    view: ListContactsView | Unset = "all",
    purpose: ListContactsPurpose | Unset = "informational",
    tag: list[str] | Unset = UNSET,
    import_id: UUID | Unset = UNSET,
    order: ListContactsOrder | Unset = "name",
    before: str | Unset = UNSET,
) -> ContactPage | Problem | None:
    """List contacts

    Args:
        limit (int | Unset): Page size Default: 50.
        after (str | Unset): Opaque cursor from next_cursor of the previous page
        e164 (str | Unset):
        q (str | Unset): Name, at least 3 digits of the number, or a tag
        view (ListContactsView | Unset):  Default: 'all'.
        purpose (ListContactsPurpose | Unset): Which callability view=callable uses Default:
            'informational'.
        tag (list[str] | Unset):
        import_id (UUID | Unset):
        order (ListContactsOrder | Unset):  Default: 'name'.
        before (str | Unset): Opaque cursor from prev_cursor

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactPage | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            after=after,
            e164=e164,
            q=q,
            view=view,
            purpose=purpose,
            tag=tag,
            import_id=import_id,
            order=order,
            before=before,
        )
    ).parsed
