from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.procedure_computation_write import ProcedureComputationWrite
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        ProcedureComputationWrite,
        ProcedureComputationWrite,
        ProcedureComputationWrite,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/computations/",
    }

    if isinstance(body, ProcedureComputationWrite):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ProcedureComputationWrite):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ProcedureComputationWrite):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProcedureComputationWrite]:
    if response.status_code == 200:
        response_200 = ProcedureComputationWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProcedureComputationWrite]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ProcedureComputationWrite,
        ProcedureComputationWrite,
        ProcedureComputationWrite,
    ],
) -> Response[ProcedureComputationWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations.

    Args:
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcedureComputationWrite]
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
    body: Union[
        ProcedureComputationWrite,
        ProcedureComputationWrite,
        ProcedureComputationWrite,
    ],
) -> Optional[ProcedureComputationWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations.

    Args:
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcedureComputationWrite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ProcedureComputationWrite,
        ProcedureComputationWrite,
        ProcedureComputationWrite,
    ],
) -> Response[ProcedureComputationWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations.

    Args:
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcedureComputationWrite]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        ProcedureComputationWrite,
        ProcedureComputationWrite,
        ProcedureComputationWrite,
    ],
) -> Optional[ProcedureComputationWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations.

    Args:
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ProcedureComputationWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcedureComputationWrite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
