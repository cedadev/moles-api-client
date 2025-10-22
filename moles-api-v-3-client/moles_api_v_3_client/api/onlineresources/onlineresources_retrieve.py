from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.online_resource_read import OnlineResourceRead
from ...types import Response


def _get_kwargs(
    ob_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v3/onlineresources/{ob_id}/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[OnlineResourceRead]:
    if response.status_code == 200:
        response_200 = OnlineResourceRead.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[OnlineResourceRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ob_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[OnlineResourceRead]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OnlineResourceRead]
    """

    kwargs = _get_kwargs(
        ob_id=ob_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ob_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[OnlineResourceRead]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OnlineResourceRead
    """

    return sync_detailed(
        ob_id=ob_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ob_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[OnlineResourceRead]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OnlineResourceRead]
    """

    kwargs = _get_kwargs(
        ob_id=ob_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ob_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[OnlineResourceRead]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OnlineResourceRead
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
        )
    ).parsed
