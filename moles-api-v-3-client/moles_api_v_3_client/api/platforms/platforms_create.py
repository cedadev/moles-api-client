from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.platform_write import PlatformWrite
from ...types import Response


def _get_kwargs(
    *,
    body: PlatformWrite,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v3/platforms/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PlatformWrite]:
    if response.status_code == 200:
        response_200 = PlatformWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PlatformWrite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PlatformWrite,
) -> Response[PlatformWrite]:
    """Get a list of Platform objects. Platforms have a 1:1 mapping with Observations.

    Args:
        body (PlatformWrite): A mixin that adds 'simple_fields' as ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlatformWrite]
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
    body: PlatformWrite,
) -> Optional[PlatformWrite]:
    """Get a list of Platform objects. Platforms have a 1:1 mapping with Observations.

    Args:
        body (PlatformWrite): A mixin that adds 'simple_fields' as ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlatformWrite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PlatformWrite,
) -> Response[PlatformWrite]:
    """Get a list of Platform objects. Platforms have a 1:1 mapping with Observations.

    Args:
        body (PlatformWrite): A mixin that adds 'simple_fields' as ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlatformWrite]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PlatformWrite,
) -> Optional[PlatformWrite]:
    """Get a list of Platform objects. Platforms have a 1:1 mapping with Observations.

    Args:
        body (PlatformWrite): A mixin that adds 'simple_fields' as ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlatformWrite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
