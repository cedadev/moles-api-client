from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identifier_write import IdentifierWrite
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        IdentifierWrite,
        IdentifierWrite,
        IdentifierWrite,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/identifiers/",
    }

    if isinstance(body, IdentifierWrite):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, IdentifierWrite):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, IdentifierWrite):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[IdentifierWrite]:
    if response.status_code == 200:
        response_200 = IdentifierWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[IdentifierWrite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        IdentifierWrite,
        IdentifierWrite,
        IdentifierWrite,
    ],
) -> Response[IdentifierWrite]:
    """Get a list of Identifier objects. Idenfifiers have a 1..*:1 mapping with Observations.

    Args:
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentifierWrite]
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
    body: Union[
        IdentifierWrite,
        IdentifierWrite,
        IdentifierWrite,
    ],
) -> Optional[IdentifierWrite]:
    """Get a list of Identifier objects. Idenfifiers have a 1..*:1 mapping with Observations.

    Args:
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentifierWrite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        IdentifierWrite,
        IdentifierWrite,
        IdentifierWrite,
    ],
) -> Response[IdentifierWrite]:
    """Get a list of Identifier objects. Idenfifiers have a 1..*:1 mapping with Observations.

    Args:
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdentifierWrite]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        IdentifierWrite,
        IdentifierWrite,
        IdentifierWrite,
    ],
) -> Optional[IdentifierWrite]:
    """Get a list of Identifier objects. Idenfifiers have a 1..*:1 mapping with Observations.

    Args:
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (IdentifierWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdentifierWrite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
