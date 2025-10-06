from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.drs_dataset_write import DRSDatasetWrite
from ...types import Response


def _get_kwargs(
    ob_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v3/drsdatasets/{ob_id}/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DRSDatasetWrite]:
    if response.status_code == 200:
        response_200 = DRSDatasetWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DRSDatasetWrite]:
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
) -> Response[DRSDatasetWrite]:
    """Get a list of DRSDataset objects.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DRSDatasetWrite]
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
) -> Optional[DRSDatasetWrite]:
    """Get a list of DRSDataset objects.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DRSDatasetWrite
    """

    return sync_detailed(
        ob_id=ob_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ob_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[DRSDatasetWrite]:
    """Get a list of DRSDataset objects.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DRSDatasetWrite]
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
) -> Optional[DRSDatasetWrite]:
    """Get a list of DRSDataset objects.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DRSDatasetWrite
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
        )
    ).parsed
