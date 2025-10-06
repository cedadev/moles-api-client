from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.licence_classification_write import LicenceClassificationWrite
from ...models.patched_licence_classification_write import PatchedLicenceClassificationWrite
from ...types import Response


def _get_kwargs(
    ob_id: int,
    *,
    body: Union[
        PatchedLicenceClassificationWrite,
        PatchedLicenceClassificationWrite,
        PatchedLicenceClassificationWrite,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/v3/licenceclassifications/{ob_id}/",
    }

    if isinstance(body, PatchedLicenceClassificationWrite):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PatchedLicenceClassificationWrite):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PatchedLicenceClassificationWrite):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[LicenceClassificationWrite]:
    if response.status_code == 200:
        response_200 = LicenceClassificationWrite.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[LicenceClassificationWrite]:
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
        PatchedLicenceClassificationWrite,
        PatchedLicenceClassificationWrite,
        PatchedLicenceClassificationWrite,
    ],
) -> Response[LicenceClassificationWrite]:
    """Get a list of LicenceClassification objects.

    Args:
        ob_id (int):
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LicenceClassificationWrite]
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
        PatchedLicenceClassificationWrite,
        PatchedLicenceClassificationWrite,
        PatchedLicenceClassificationWrite,
    ],
) -> Optional[LicenceClassificationWrite]:
    """Get a list of LicenceClassification objects.

    Args:
        ob_id (int):
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LicenceClassificationWrite
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
        PatchedLicenceClassificationWrite,
        PatchedLicenceClassificationWrite,
        PatchedLicenceClassificationWrite,
    ],
) -> Response[LicenceClassificationWrite]:
    """Get a list of LicenceClassification objects.

    Args:
        ob_id (int):
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LicenceClassificationWrite]
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
        PatchedLicenceClassificationWrite,
        PatchedLicenceClassificationWrite,
        PatchedLicenceClassificationWrite,
    ],
) -> Optional[LicenceClassificationWrite]:
    """Get a list of LicenceClassification objects.

    Args:
        ob_id (int):
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.
        body (PatchedLicenceClassificationWrite): A mixin that allows specifying which fields to
            include in the serializer
            via the 'fields' keyword argument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LicenceClassificationWrite
    """

    return (
        await asyncio_detailed(
            ob_id=ob_id,
            client=client,
            body=body,
        )
    ).parsed
