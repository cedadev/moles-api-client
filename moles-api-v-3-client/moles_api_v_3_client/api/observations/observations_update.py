from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.observation_write import ObservationWrite
from ...models.observation_write_request import ObservationWriteRequest
from ...types import Response


def _get_kwargs(
    ob_id: int,
    *,
    body: ObservationWriteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v3/observations/{ob_id}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ObservationWrite]:
    if response.status_code == 200:
        response_200 = ObservationWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ObservationWrite]:
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
    body: ObservationWriteRequest,
) -> Response[ObservationWrite]:
    """Get a list of Observation objects.

    Args:
        ob_id (int):
        body (ObservationWriteRequest): A mixin that allows specifying which fields to include in
            the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObservationWrite]
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
    body: ObservationWriteRequest,
) -> Optional[ObservationWrite]:
    """Get a list of Observation objects.

    Args:
        ob_id (int):
        body (ObservationWriteRequest): A mixin that allows specifying which fields to include in
            the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObservationWrite
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
    body: ObservationWriteRequest,
) -> Response[ObservationWrite]:
    """Get a list of Observation objects.

    Args:
        ob_id (int):
        body (ObservationWriteRequest): A mixin that allows specifying which fields to include in
            the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObservationWrite]
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
    body: ObservationWriteRequest,
) -> Optional[ObservationWrite]:
    """Get a list of Observation objects.

    Args:
        ob_id (int):
        body (ObservationWriteRequest): A mixin that allows specifying which fields to include in
            the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObservationWrite
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
            body=body,
        )
    ).parsed
