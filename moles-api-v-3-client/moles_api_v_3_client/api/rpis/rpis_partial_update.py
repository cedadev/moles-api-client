from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_responsible_party_info_write_request import PatchedResponsiblePartyInfoWriteRequest
from ...models.responsible_party_info_write import ResponsiblePartyInfoWrite
from ...types import Response


def _get_kwargs(
    ob_id: int,
    *,
    body: PatchedResponsiblePartyInfoWriteRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v3/rpis/{ob_id}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ResponsiblePartyInfoWrite | None:
    if response.status_code == 200:
        response_200 = ResponsiblePartyInfoWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ResponsiblePartyInfoWrite]:
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
    body: PatchedResponsiblePartyInfoWriteRequest,
) -> Response[ResponsiblePartyInfoWrite]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        ob_id (int):
        body (PatchedResponsiblePartyInfoWriteRequest): A mixin that allows specifying which
            fields to include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponsiblePartyInfoWrite]
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
    body: PatchedResponsiblePartyInfoWriteRequest,
) -> ResponsiblePartyInfoWrite | None:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        ob_id (int):
        body (PatchedResponsiblePartyInfoWriteRequest): A mixin that allows specifying which
            fields to include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponsiblePartyInfoWrite
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
    body: PatchedResponsiblePartyInfoWriteRequest,
) -> Response[ResponsiblePartyInfoWrite]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        ob_id (int):
        body (PatchedResponsiblePartyInfoWriteRequest): A mixin that allows specifying which
            fields to include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponsiblePartyInfoWrite]
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
    body: PatchedResponsiblePartyInfoWriteRequest,
) -> ResponsiblePartyInfoWrite | None:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        ob_id (int):
        body (PatchedResponsiblePartyInfoWriteRequest): A mixin that allows specifying which
            fields to include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponsiblePartyInfoWrite
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
            body=body,
        )
    ).parsed
