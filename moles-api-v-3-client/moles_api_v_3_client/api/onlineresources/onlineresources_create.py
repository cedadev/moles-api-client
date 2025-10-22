from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.online_resource_write import OnlineResourceWrite
from ...models.online_resource_write_request import OnlineResourceWriteRequest
from ...types import Response


def _get_kwargs(
    *,
    body: OnlineResourceWriteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/onlineresources/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OnlineResourceWrite]:
    if response.status_code == 201:
        response_201 = OnlineResourceWrite.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OnlineResourceWrite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OnlineResourceWriteRequest,
) -> Response[OnlineResourceWrite]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        body (OnlineResourceWriteRequest): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OnlineResourceWrite]
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
    body: OnlineResourceWriteRequest,
) -> Optional[OnlineResourceWrite]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        body (OnlineResourceWriteRequest): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OnlineResourceWrite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OnlineResourceWriteRequest,
) -> Response[OnlineResourceWrite]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        body (OnlineResourceWriteRequest): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OnlineResourceWrite]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: OnlineResourceWriteRequest,
) -> Optional[OnlineResourceWrite]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        body (OnlineResourceWriteRequest): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OnlineResourceWrite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
