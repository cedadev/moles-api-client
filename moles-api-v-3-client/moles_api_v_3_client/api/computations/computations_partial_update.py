from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_procedure_computation_write import PatchedProcedureComputationWrite
from ...models.procedure_computation_write import ProcedureComputationWrite
from ...types import Response


def _get_kwargs(
    ob_id: int,
    *,
    body: PatchedProcedureComputationWrite,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v3/computations/{ob_id}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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
    ob_id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedProcedureComputationWrite,
) -> Response[ProcedureComputationWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations.

    Args:
        ob_id (int):
        body (PatchedProcedureComputationWrite): A mixin that adds 'simple_fields' as
            ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcedureComputationWrite]
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
    body: PatchedProcedureComputationWrite,
) -> Optional[ProcedureComputationWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations.

    Args:
        ob_id (int):
        body (PatchedProcedureComputationWrite): A mixin that adds 'simple_fields' as
            ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcedureComputationWrite
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
    body: PatchedProcedureComputationWrite,
) -> Response[ProcedureComputationWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations.

    Args:
        ob_id (int):
        body (PatchedProcedureComputationWrite): A mixin that adds 'simple_fields' as
            ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProcedureComputationWrite]
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
    body: PatchedProcedureComputationWrite,
) -> Optional[ProcedureComputationWrite]:
    """Get a list of ProcedureComputation objects. ProcedureComputations have a 1:1 mapping with
    Observations.

    Args:
        ob_id (int):
        body (PatchedProcedureComputationWrite): A mixin that adds 'simple_fields' as
            ReadOnlyFields
            and reorders them to the top.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProcedureComputationWrite
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
            body=body,
        )
    ).parsed
