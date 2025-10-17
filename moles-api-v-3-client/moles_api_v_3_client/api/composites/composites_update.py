from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.procedure_composite_process_write import ProcedureCompositeProcessWrite
from ...types import Response


def _get_kwargs(
    ob_id: int,
    *,
    body: ProcedureCompositeProcessWrite,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v3/composites/{ob_id}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ProcedureCompositeProcessWrite]:
    if response.status_code == 200:
        response_200 = ProcedureCompositeProcessWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ProcedureCompositeProcessWrite]:
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
    body: ProcedureCompositeProcessWrite,
) -> Response[ProcedureCompositeProcessWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations where used.
    These may have a number of 2 or more components made up of combinations of Computation and
    Acquisition records.
    The details of the underlying records have been serialised.

    Args:
        ob_id (int):
        body (ProcedureCompositeProcessWrite): A mixin that adds 'simple_fields' as ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcedureCompositeProcessWrite]
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
    body: ProcedureCompositeProcessWrite,
) -> Optional[ProcedureCompositeProcessWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations where used.
    These may have a number of 2 or more components made up of combinations of Computation and
    Acquisition records.
    The details of the underlying records have been serialised.

    Args:
        ob_id (int):
        body (ProcedureCompositeProcessWrite): A mixin that adds 'simple_fields' as ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcedureCompositeProcessWrite
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
    body: ProcedureCompositeProcessWrite,
) -> Response[ProcedureCompositeProcessWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations where used.
    These may have a number of 2 or more components made up of combinations of Computation and
    Acquisition records.
    The details of the underlying records have been serialised.

    Args:
        ob_id (int):
        body (ProcedureCompositeProcessWrite): A mixin that adds 'simple_fields' as ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcedureCompositeProcessWrite]
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
    body: ProcedureCompositeProcessWrite,
) -> Optional[ProcedureCompositeProcessWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations where used.
    These may have a number of 2 or more components made up of combinations of Computation and
    Acquisition records.
    The details of the underlying records have been serialised.

    Args:
        ob_id (int):
        body (ProcedureCompositeProcessWrite): A mixin that adds 'simple_fields' as ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcedureCompositeProcessWrite
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
            body=body,
        )
    ).parsed
