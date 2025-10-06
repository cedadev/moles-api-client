from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.party_write import PartyWrite
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        PartyWrite,
        PartyWrite,
        PartyWrite,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/parties/",
    }

    if isinstance(body, PartyWrite):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PartyWrite):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PartyWrite):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PartyWrite]:
    if response.status_code == 200:
        response_200 = PartyWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PartyWrite]:
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
        PartyWrite,
        PartyWrite,
        PartyWrite,
    ],
) -> Response[PartyWrite]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartyWrite]
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
        PartyWrite,
        PartyWrite,
        PartyWrite,
    ],
) -> Optional[PartyWrite]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartyWrite
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        PartyWrite,
        PartyWrite,
        PartyWrite,
    ],
) -> Response[PartyWrite]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PartyWrite]
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
        PartyWrite,
        PartyWrite,
        PartyWrite,
    ],
) -> Optional[PartyWrite]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (PartyWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PartyWrite
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
