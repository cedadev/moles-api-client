from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.responsible_party_info_write import ResponsiblePartyInfoWrite
from ...types import Response


def _get_kwargs(
    ob_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v3/rpis/{ob_id}/",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ResponsiblePartyInfoWrite]:
    if response.status_code == 200:
        response_200 = ResponsiblePartyInfoWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
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
) -> Response[ResponsiblePartyInfoWrite]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponsiblePartyInfoWrite]
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
) -> Optional[ResponsiblePartyInfoWrite]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponsiblePartyInfoWrite
    """

    return sync_detailed(
        ob_id=ob_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    ob_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ResponsiblePartyInfoWrite]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        ob_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponsiblePartyInfoWrite]
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
) -> Optional[ResponsiblePartyInfoWrite]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        ob_id (int):

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
        )
    ).parsed
