from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.observation_collection_write import ObservationCollectionWrite
from ...models.patched_observation_collection_write import PatchedObservationCollectionWrite
from ...types import Response


def _get_kwargs(
    ob_id: int,
    *,
    body: Union[
        PatchedObservationCollectionWrite,
        PatchedObservationCollectionWrite,
        PatchedObservationCollectionWrite,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/v3/observationcollections/{ob_id}/",
    }

    if isinstance(body, PatchedObservationCollectionWrite):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedObservationCollectionWrite):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedObservationCollectionWrite):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ObservationCollectionWrite]:
    if response.status_code == 200:
        response_200 = ObservationCollectionWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ObservationCollectionWrite]:
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
    body: Union[
        PatchedObservationCollectionWrite,
        PatchedObservationCollectionWrite,
        PatchedObservationCollectionWrite,
    ],
) -> Response[ObservationCollectionWrite]:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        ob_id (int):
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObservationCollectionWrite]
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
    body: Union[
        PatchedObservationCollectionWrite,
        PatchedObservationCollectionWrite,
        PatchedObservationCollectionWrite,
    ],
) -> Optional[ObservationCollectionWrite]:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        ob_id (int):
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObservationCollectionWrite
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
    body: Union[
        PatchedObservationCollectionWrite,
        PatchedObservationCollectionWrite,
        PatchedObservationCollectionWrite,
    ],
) -> Response[ObservationCollectionWrite]:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        ob_id (int):
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObservationCollectionWrite]
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
    body: Union[
        PatchedObservationCollectionWrite,
        PatchedObservationCollectionWrite,
        PatchedObservationCollectionWrite,
    ],
) -> Optional[ObservationCollectionWrite]:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        ob_id (int):
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedObservationCollectionWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObservationCollectionWrite
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
            body=body,
        )
    ).parsed
