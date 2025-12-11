from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.note_write import NoteWrite
from ...models.note_write_request import NoteWriteRequest
from ...types import Response


def _get_kwargs(
    *,
    body: NoteWriteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/notes/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> NoteWrite | None:
    if response.status_code == 201:
        response_201 = NoteWrite.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[NoteWrite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NoteWriteRequest,
) -> Response[NoteWrite]:
    """Get a list of Note objects.

    Args:
        body (NoteWriteRequest): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NoteWrite]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: NoteWriteRequest,
) -> NoteWrite | None:
    """Get a list of Note objects.

    Args:
        body (NoteWriteRequest): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NoteWrite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NoteWriteRequest,
) -> Response[NoteWrite]:
    """Get a list of Note objects.

    Args:
        body (NoteWriteRequest): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[NoteWrite]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NoteWriteRequest,
) -> NoteWrite | None:
    """Get a list of Note objects.

    Args:
        body (NoteWriteRequest): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        NoteWrite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
