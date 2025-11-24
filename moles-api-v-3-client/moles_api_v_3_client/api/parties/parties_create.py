from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.party_write import PartyWrite
from ...models.party_write_request import PartyWriteRequest
from ...types import Response


def _get_kwargs(
    *,
    body: PartyWriteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/parties/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PartyWrite | None:
    if response.status_code == 201:
        response_201 = PartyWrite.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PartyWrite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PartyWriteRequest,
) -> Response[PartyWrite]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        body (PartyWriteRequest): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartyWrite]
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
    body: PartyWriteRequest,
) -> PartyWrite | None:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        body (PartyWriteRequest): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartyWrite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PartyWriteRequest,
) -> Response[PartyWrite]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        body (PartyWriteRequest): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartyWrite]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PartyWriteRequest,
) -> PartyWrite | None:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        body (PartyWriteRequest): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartyWrite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
