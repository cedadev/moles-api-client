from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.inspire_theme_write import InspireThemeWrite
from ...types import Response


def _get_kwargs(
    ob_id: int,
    *,
    body: Union[
        InspireThemeWrite,
        InspireThemeWrite,
        InspireThemeWrite,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/v3/inspirethemes/{ob_id}/",
    }

    if isinstance(body, InspireThemeWrite):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, InspireThemeWrite):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, InspireThemeWrite):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[InspireThemeWrite]:
    if response.status_code == 200:
        response_200 = InspireThemeWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[InspireThemeWrite]:
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
        InspireThemeWrite,
        InspireThemeWrite,
        InspireThemeWrite,
    ],
) -> Response[InspireThemeWrite]:
    """Get a list of InspireTheme objects.

    Args:
        ob_id (int):
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InspireThemeWrite]
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
        InspireThemeWrite,
        InspireThemeWrite,
        InspireThemeWrite,
    ],
) -> Optional[InspireThemeWrite]:
    """Get a list of InspireTheme objects.

    Args:
        ob_id (int):
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InspireThemeWrite
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
        InspireThemeWrite,
        InspireThemeWrite,
        InspireThemeWrite,
    ],
) -> Response[InspireThemeWrite]:
    """Get a list of InspireTheme objects.

    Args:
        ob_id (int):
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InspireThemeWrite]
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
        InspireThemeWrite,
        InspireThemeWrite,
        InspireThemeWrite,
    ],
) -> Optional[InspireThemeWrite]:
    """Get a list of InspireTheme objects.

    Args:
        ob_id (int):
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.
        body (InspireThemeWrite): A mixin that allows specifying which fields to include in the
            serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InspireThemeWrite
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
            body=body,
        )
    ).parsed
