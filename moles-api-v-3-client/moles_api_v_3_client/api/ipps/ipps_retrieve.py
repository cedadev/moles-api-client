from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instrument_platform_pair_write import InstrumentPlatformPairWrite
from ...types import Response


def _get_kwargs(
    ob_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v3/ipps/{ob_id}/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[InstrumentPlatformPairWrite]:
    if response.status_code == 200:
        response_200 = InstrumentPlatformPairWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[InstrumentPlatformPairWrite]:
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
) -> Response[InstrumentPlatformPairWrite]:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstrumentPlatformPairWrite]
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
) -> Optional[InstrumentPlatformPairWrite]:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstrumentPlatformPairWrite
    """

    return sync_detailed(
        ob_id=ob_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ob_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[InstrumentPlatformPairWrite]:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InstrumentPlatformPairWrite]
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
) -> Optional[InstrumentPlatformPairWrite]:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InstrumentPlatformPairWrite
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
        )
    ).parsed
