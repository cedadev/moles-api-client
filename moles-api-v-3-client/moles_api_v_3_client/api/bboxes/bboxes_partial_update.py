from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.geographic_bounding_box_write import GeographicBoundingBoxWrite
from ...models.patched_geographic_bounding_box_write_request import PatchedGeographicBoundingBoxWriteRequest
from ...types import Response


def _get_kwargs(
    ob_id: int,
    *,
    body: PatchedGeographicBoundingBoxWriteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v3/bboxes/{ob_id}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GeographicBoundingBoxWrite | None:
    if response.status_code == 200:
        response_200 = GeographicBoundingBoxWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GeographicBoundingBoxWrite]:
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
    body: PatchedGeographicBoundingBoxWriteRequest,
) -> Response[GeographicBoundingBoxWrite]:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        ob_id (int):
        body (PatchedGeographicBoundingBoxWriteRequest): A mixin that allows specifying which
            fields to include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeographicBoundingBoxWrite]
    """

    kwargs = _get_kwargs(
        ob_id=ob_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ob_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedGeographicBoundingBoxWriteRequest,
) -> GeographicBoundingBoxWrite | None:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        ob_id (int):
        body (PatchedGeographicBoundingBoxWriteRequest): A mixin that allows specifying which
            fields to include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeographicBoundingBoxWrite
    """

    return sync_detailed(
        ob_id=ob_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    ob_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedGeographicBoundingBoxWriteRequest,
) -> Response[GeographicBoundingBoxWrite]:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        ob_id (int):
        body (PatchedGeographicBoundingBoxWriteRequest): A mixin that allows specifying which
            fields to include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GeographicBoundingBoxWrite]
    """

    kwargs = _get_kwargs(
        ob_id=ob_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ob_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedGeographicBoundingBoxWriteRequest,
) -> GeographicBoundingBoxWrite | None:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        ob_id (int):
        body (PatchedGeographicBoundingBoxWriteRequest): A mixin that allows specifying which
            fields to include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GeographicBoundingBoxWrite
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
            body=body,
        )
    ).parsed
