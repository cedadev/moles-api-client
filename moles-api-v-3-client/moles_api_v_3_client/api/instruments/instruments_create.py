from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instrument_write import InstrumentWrite
from ...models.instrument_write_request import InstrumentWriteRequest
from ...types import Response


def _get_kwargs(
    *,
    body: InstrumentWriteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/instruments/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InstrumentWrite | None:
    if response.status_code == 201:
        response_201 = InstrumentWrite.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InstrumentWrite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: InstrumentWriteRequest,
) -> Response[InstrumentWrite]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        body (InstrumentWriteRequest): A mixin that allows specifying which fields to include in
            the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstrumentWrite]
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
    body: InstrumentWriteRequest,
) -> InstrumentWrite | None:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        body (InstrumentWriteRequest): A mixin that allows specifying which fields to include in
            the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstrumentWrite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: InstrumentWriteRequest,
) -> Response[InstrumentWrite]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        body (InstrumentWriteRequest): A mixin that allows specifying which fields to include in
            the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstrumentWrite]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: InstrumentWriteRequest,
) -> InstrumentWrite | None:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        body (InstrumentWriteRequest): A mixin that allows specifying which fields to include in
            the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstrumentWrite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
