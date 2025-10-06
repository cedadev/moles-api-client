from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.responsible_party_info_write import ResponsiblePartyInfoWrite
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        ResponsiblePartyInfoWrite,
        ResponsiblePartyInfoWrite,
        ResponsiblePartyInfoWrite,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/rpis/",
    }

    if isinstance(body, ResponsiblePartyInfoWrite):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, ResponsiblePartyInfoWrite):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, ResponsiblePartyInfoWrite):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: Union[
        ResponsiblePartyInfoWrite,
        ResponsiblePartyInfoWrite,
        ResponsiblePartyInfoWrite,
    ],
) -> Response[ResponsiblePartyInfoWrite]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponsiblePartyInfoWrite]
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
        ResponsiblePartyInfoWrite,
        ResponsiblePartyInfoWrite,
        ResponsiblePartyInfoWrite,
    ],
) -> Optional[ResponsiblePartyInfoWrite]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponsiblePartyInfoWrite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ResponsiblePartyInfoWrite,
        ResponsiblePartyInfoWrite,
        ResponsiblePartyInfoWrite,
    ],
) -> Response[ResponsiblePartyInfoWrite]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResponsiblePartyInfoWrite]
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
        ResponsiblePartyInfoWrite,
        ResponsiblePartyInfoWrite,
        ResponsiblePartyInfoWrite,
    ],
) -> Optional[ResponsiblePartyInfoWrite]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.
        body (ResponsiblePartyInfoWrite): A mixin that allows specifying which fields to include
            in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResponsiblePartyInfoWrite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
