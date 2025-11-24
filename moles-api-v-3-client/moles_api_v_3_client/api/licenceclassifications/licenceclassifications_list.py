from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_licence_classification_read_list import PaginatedLicenceClassificationReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    classification: str | Unset = UNSET,
    classification_contains: str | Unset = UNSET,
    classification_endswith: str | Unset = UNSET,
    classification_gt: str | Unset = UNSET,
    classification_gte: str | Unset = UNSET,
    classification_icontains: str | Unset = UNSET,
    classification_iendswith: str | Unset = UNSET,
    classification_iexact: str | Unset = UNSET,
    classification_in: list[str] | Unset = UNSET,
    classification_iregex: str | Unset = UNSET,
    classification_isnull: bool | Unset = UNSET,
    classification_istartswith: str | Unset = UNSET,
    classification_lt: str | Unset = UNSET,
    classification_lte: str | Unset = UNSET,
    classification_range: list[str] | Unset = UNSET,
    classification_regex: str | Unset = UNSET,
    classification_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ob_id: int | Unset = UNSET,
    ob_id_contained_by: int | Unset = UNSET,
    ob_id_contains: int | Unset = UNSET,
    ob_id_endswith: int | Unset = UNSET,
    ob_id_gt: int | Unset = UNSET,
    ob_id_gte: int | Unset = UNSET,
    ob_id_icontains: int | Unset = UNSET,
    ob_id_iendswith: int | Unset = UNSET,
    ob_id_iexact: int | Unset = UNSET,
    ob_id_in: list[int] | Unset = UNSET,
    ob_id_iregex: int | Unset = UNSET,
    ob_id_isnull: bool | Unset = UNSET,
    ob_id_istartswith: int | Unset = UNSET,
    ob_id_lt: int | Unset = UNSET,
    ob_id_lte: int | Unset = UNSET,
    ob_id_range: list[int] | Unset = UNSET,
    ob_id_regex: int | Unset = UNSET,
    ob_id_startswith: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["classification"] = classification

    params["classification__contains"] = classification_contains

    params["classification__endswith"] = classification_endswith

    params["classification__gt"] = classification_gt

    params["classification__gte"] = classification_gte

    params["classification__icontains"] = classification_icontains

    params["classification__iendswith"] = classification_iendswith

    params["classification__iexact"] = classification_iexact

    json_classification_in: list[str] | Unset = UNSET
    if not isinstance(classification_in, Unset):
        json_classification_in = ",".join(map(str, classification_in))

    params["classification__in"] = json_classification_in

    params["classification__iregex"] = classification_iregex

    params["classification__isnull"] = classification_isnull

    params["classification__istartswith"] = classification_istartswith

    params["classification__lt"] = classification_lt

    params["classification__lte"] = classification_lte

    json_classification_range: list[str] | Unset = UNSET
    if not isinstance(classification_range, Unset):
        json_classification_range = ",".join(map(str, classification_range))

    params["classification__range"] = json_classification_range

    params["classification__regex"] = classification_regex

    params["classification__startswith"] = classification_startswith

    params["limit"] = limit

    params["ob_id"] = ob_id

    params["ob_id__contained_by"] = ob_id_contained_by

    params["ob_id__contains"] = ob_id_contains

    params["ob_id__endswith"] = ob_id_endswith

    params["ob_id__gt"] = ob_id_gt

    params["ob_id__gte"] = ob_id_gte

    params["ob_id__icontains"] = ob_id_icontains

    params["ob_id__iendswith"] = ob_id_iendswith

    params["ob_id__iexact"] = ob_id_iexact

    json_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(ob_id_in, Unset):
        json_ob_id_in = ",".join(map(str, ob_id_in))

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: list[int] | Unset = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ",".join(map(str, ob_id_range))

    params["ob_id__range"] = json_ob_id_range

    params["ob_id__regex"] = ob_id_regex

    params["ob_id__startswith"] = ob_id_startswith

    params["offset"] = offset

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/licenceclassifications/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedLicenceClassificationReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedLicenceClassificationReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedLicenceClassificationReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    classification: str | Unset = UNSET,
    classification_contains: str | Unset = UNSET,
    classification_endswith: str | Unset = UNSET,
    classification_gt: str | Unset = UNSET,
    classification_gte: str | Unset = UNSET,
    classification_icontains: str | Unset = UNSET,
    classification_iendswith: str | Unset = UNSET,
    classification_iexact: str | Unset = UNSET,
    classification_in: list[str] | Unset = UNSET,
    classification_iregex: str | Unset = UNSET,
    classification_isnull: bool | Unset = UNSET,
    classification_istartswith: str | Unset = UNSET,
    classification_lt: str | Unset = UNSET,
    classification_lte: str | Unset = UNSET,
    classification_range: list[str] | Unset = UNSET,
    classification_regex: str | Unset = UNSET,
    classification_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ob_id: int | Unset = UNSET,
    ob_id_contained_by: int | Unset = UNSET,
    ob_id_contains: int | Unset = UNSET,
    ob_id_endswith: int | Unset = UNSET,
    ob_id_gt: int | Unset = UNSET,
    ob_id_gte: int | Unset = UNSET,
    ob_id_icontains: int | Unset = UNSET,
    ob_id_iendswith: int | Unset = UNSET,
    ob_id_iexact: int | Unset = UNSET,
    ob_id_in: list[int] | Unset = UNSET,
    ob_id_iregex: int | Unset = UNSET,
    ob_id_isnull: bool | Unset = UNSET,
    ob_id_istartswith: int | Unset = UNSET,
    ob_id_lt: int | Unset = UNSET,
    ob_id_lte: int | Unset = UNSET,
    ob_id_range: list[int] | Unset = UNSET,
    ob_id_regex: int | Unset = UNSET,
    ob_id_startswith: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedLicenceClassificationReadList]:
    """Get a list of LicenceClassification objects.

    Args:
        classification (str | Unset):
        classification_contains (str | Unset):
        classification_endswith (str | Unset):
        classification_gt (str | Unset):
        classification_gte (str | Unset):
        classification_icontains (str | Unset):
        classification_iendswith (str | Unset):
        classification_iexact (str | Unset):
        classification_in (list[str] | Unset):
        classification_iregex (str | Unset):
        classification_isnull (bool | Unset):
        classification_istartswith (str | Unset):
        classification_lt (str | Unset):
        classification_lte (str | Unset):
        classification_range (list[str] | Unset):
        classification_regex (str | Unset):
        classification_startswith (str | Unset):
        limit (int | Unset):
        ob_id (int | Unset):
        ob_id_contained_by (int | Unset):
        ob_id_contains (int | Unset):
        ob_id_endswith (int | Unset):
        ob_id_gt (int | Unset):
        ob_id_gte (int | Unset):
        ob_id_icontains (int | Unset):
        ob_id_iendswith (int | Unset):
        ob_id_iexact (int | Unset):
        ob_id_in (list[int] | Unset):
        ob_id_iregex (int | Unset):
        ob_id_isnull (bool | Unset):
        ob_id_istartswith (int | Unset):
        ob_id_lt (int | Unset):
        ob_id_lte (int | Unset):
        ob_id_range (list[int] | Unset):
        ob_id_regex (int | Unset):
        ob_id_startswith (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLicenceClassificationReadList]
    """

    kwargs = _get_kwargs(
        classification=classification,
        classification_contains=classification_contains,
        classification_endswith=classification_endswith,
        classification_gt=classification_gt,
        classification_gte=classification_gte,
        classification_icontains=classification_icontains,
        classification_iendswith=classification_iendswith,
        classification_iexact=classification_iexact,
        classification_in=classification_in,
        classification_iregex=classification_iregex,
        classification_isnull=classification_isnull,
        classification_istartswith=classification_istartswith,
        classification_lt=classification_lt,
        classification_lte=classification_lte,
        classification_range=classification_range,
        classification_regex=classification_regex,
        classification_startswith=classification_startswith,
        limit=limit,
        ob_id=ob_id,
        ob_id_contained_by=ob_id_contained_by,
        ob_id_contains=ob_id_contains,
        ob_id_endswith=ob_id_endswith,
        ob_id_gt=ob_id_gt,
        ob_id_gte=ob_id_gte,
        ob_id_icontains=ob_id_icontains,
        ob_id_iendswith=ob_id_iendswith,
        ob_id_iexact=ob_id_iexact,
        ob_id_in=ob_id_in,
        ob_id_iregex=ob_id_iregex,
        ob_id_isnull=ob_id_isnull,
        ob_id_istartswith=ob_id_istartswith,
        ob_id_lt=ob_id_lt,
        ob_id_lte=ob_id_lte,
        ob_id_range=ob_id_range,
        ob_id_regex=ob_id_regex,
        ob_id_startswith=ob_id_startswith,
        offset=offset,
        ordering=ordering,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    classification: str | Unset = UNSET,
    classification_contains: str | Unset = UNSET,
    classification_endswith: str | Unset = UNSET,
    classification_gt: str | Unset = UNSET,
    classification_gte: str | Unset = UNSET,
    classification_icontains: str | Unset = UNSET,
    classification_iendswith: str | Unset = UNSET,
    classification_iexact: str | Unset = UNSET,
    classification_in: list[str] | Unset = UNSET,
    classification_iregex: str | Unset = UNSET,
    classification_isnull: bool | Unset = UNSET,
    classification_istartswith: str | Unset = UNSET,
    classification_lt: str | Unset = UNSET,
    classification_lte: str | Unset = UNSET,
    classification_range: list[str] | Unset = UNSET,
    classification_regex: str | Unset = UNSET,
    classification_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ob_id: int | Unset = UNSET,
    ob_id_contained_by: int | Unset = UNSET,
    ob_id_contains: int | Unset = UNSET,
    ob_id_endswith: int | Unset = UNSET,
    ob_id_gt: int | Unset = UNSET,
    ob_id_gte: int | Unset = UNSET,
    ob_id_icontains: int | Unset = UNSET,
    ob_id_iendswith: int | Unset = UNSET,
    ob_id_iexact: int | Unset = UNSET,
    ob_id_in: list[int] | Unset = UNSET,
    ob_id_iregex: int | Unset = UNSET,
    ob_id_isnull: bool | Unset = UNSET,
    ob_id_istartswith: int | Unset = UNSET,
    ob_id_lt: int | Unset = UNSET,
    ob_id_lte: int | Unset = UNSET,
    ob_id_range: list[int] | Unset = UNSET,
    ob_id_regex: int | Unset = UNSET,
    ob_id_startswith: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedLicenceClassificationReadList | None:
    """Get a list of LicenceClassification objects.

    Args:
        classification (str | Unset):
        classification_contains (str | Unset):
        classification_endswith (str | Unset):
        classification_gt (str | Unset):
        classification_gte (str | Unset):
        classification_icontains (str | Unset):
        classification_iendswith (str | Unset):
        classification_iexact (str | Unset):
        classification_in (list[str] | Unset):
        classification_iregex (str | Unset):
        classification_isnull (bool | Unset):
        classification_istartswith (str | Unset):
        classification_lt (str | Unset):
        classification_lte (str | Unset):
        classification_range (list[str] | Unset):
        classification_regex (str | Unset):
        classification_startswith (str | Unset):
        limit (int | Unset):
        ob_id (int | Unset):
        ob_id_contained_by (int | Unset):
        ob_id_contains (int | Unset):
        ob_id_endswith (int | Unset):
        ob_id_gt (int | Unset):
        ob_id_gte (int | Unset):
        ob_id_icontains (int | Unset):
        ob_id_iendswith (int | Unset):
        ob_id_iexact (int | Unset):
        ob_id_in (list[int] | Unset):
        ob_id_iregex (int | Unset):
        ob_id_isnull (bool | Unset):
        ob_id_istartswith (int | Unset):
        ob_id_lt (int | Unset):
        ob_id_lte (int | Unset):
        ob_id_range (list[int] | Unset):
        ob_id_regex (int | Unset):
        ob_id_startswith (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLicenceClassificationReadList
    """

    return sync_detailed(
        client=client,
        classification=classification,
        classification_contains=classification_contains,
        classification_endswith=classification_endswith,
        classification_gt=classification_gt,
        classification_gte=classification_gte,
        classification_icontains=classification_icontains,
        classification_iendswith=classification_iendswith,
        classification_iexact=classification_iexact,
        classification_in=classification_in,
        classification_iregex=classification_iregex,
        classification_isnull=classification_isnull,
        classification_istartswith=classification_istartswith,
        classification_lt=classification_lt,
        classification_lte=classification_lte,
        classification_range=classification_range,
        classification_regex=classification_regex,
        classification_startswith=classification_startswith,
        limit=limit,
        ob_id=ob_id,
        ob_id_contained_by=ob_id_contained_by,
        ob_id_contains=ob_id_contains,
        ob_id_endswith=ob_id_endswith,
        ob_id_gt=ob_id_gt,
        ob_id_gte=ob_id_gte,
        ob_id_icontains=ob_id_icontains,
        ob_id_iendswith=ob_id_iendswith,
        ob_id_iexact=ob_id_iexact,
        ob_id_in=ob_id_in,
        ob_id_iregex=ob_id_iregex,
        ob_id_isnull=ob_id_isnull,
        ob_id_istartswith=ob_id_istartswith,
        ob_id_lt=ob_id_lt,
        ob_id_lte=ob_id_lte,
        ob_id_range=ob_id_range,
        ob_id_regex=ob_id_regex,
        ob_id_startswith=ob_id_startswith,
        offset=offset,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    classification: str | Unset = UNSET,
    classification_contains: str | Unset = UNSET,
    classification_endswith: str | Unset = UNSET,
    classification_gt: str | Unset = UNSET,
    classification_gte: str | Unset = UNSET,
    classification_icontains: str | Unset = UNSET,
    classification_iendswith: str | Unset = UNSET,
    classification_iexact: str | Unset = UNSET,
    classification_in: list[str] | Unset = UNSET,
    classification_iregex: str | Unset = UNSET,
    classification_isnull: bool | Unset = UNSET,
    classification_istartswith: str | Unset = UNSET,
    classification_lt: str | Unset = UNSET,
    classification_lte: str | Unset = UNSET,
    classification_range: list[str] | Unset = UNSET,
    classification_regex: str | Unset = UNSET,
    classification_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ob_id: int | Unset = UNSET,
    ob_id_contained_by: int | Unset = UNSET,
    ob_id_contains: int | Unset = UNSET,
    ob_id_endswith: int | Unset = UNSET,
    ob_id_gt: int | Unset = UNSET,
    ob_id_gte: int | Unset = UNSET,
    ob_id_icontains: int | Unset = UNSET,
    ob_id_iendswith: int | Unset = UNSET,
    ob_id_iexact: int | Unset = UNSET,
    ob_id_in: list[int] | Unset = UNSET,
    ob_id_iregex: int | Unset = UNSET,
    ob_id_isnull: bool | Unset = UNSET,
    ob_id_istartswith: int | Unset = UNSET,
    ob_id_lt: int | Unset = UNSET,
    ob_id_lte: int | Unset = UNSET,
    ob_id_range: list[int] | Unset = UNSET,
    ob_id_regex: int | Unset = UNSET,
    ob_id_startswith: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> Response[PaginatedLicenceClassificationReadList]:
    """Get a list of LicenceClassification objects.

    Args:
        classification (str | Unset):
        classification_contains (str | Unset):
        classification_endswith (str | Unset):
        classification_gt (str | Unset):
        classification_gte (str | Unset):
        classification_icontains (str | Unset):
        classification_iendswith (str | Unset):
        classification_iexact (str | Unset):
        classification_in (list[str] | Unset):
        classification_iregex (str | Unset):
        classification_isnull (bool | Unset):
        classification_istartswith (str | Unset):
        classification_lt (str | Unset):
        classification_lte (str | Unset):
        classification_range (list[str] | Unset):
        classification_regex (str | Unset):
        classification_startswith (str | Unset):
        limit (int | Unset):
        ob_id (int | Unset):
        ob_id_contained_by (int | Unset):
        ob_id_contains (int | Unset):
        ob_id_endswith (int | Unset):
        ob_id_gt (int | Unset):
        ob_id_gte (int | Unset):
        ob_id_icontains (int | Unset):
        ob_id_iendswith (int | Unset):
        ob_id_iexact (int | Unset):
        ob_id_in (list[int] | Unset):
        ob_id_iregex (int | Unset):
        ob_id_isnull (bool | Unset):
        ob_id_istartswith (int | Unset):
        ob_id_lt (int | Unset):
        ob_id_lte (int | Unset):
        ob_id_range (list[int] | Unset):
        ob_id_regex (int | Unset):
        ob_id_startswith (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLicenceClassificationReadList]
    """

    kwargs = _get_kwargs(
        classification=classification,
        classification_contains=classification_contains,
        classification_endswith=classification_endswith,
        classification_gt=classification_gt,
        classification_gte=classification_gte,
        classification_icontains=classification_icontains,
        classification_iendswith=classification_iendswith,
        classification_iexact=classification_iexact,
        classification_in=classification_in,
        classification_iregex=classification_iregex,
        classification_isnull=classification_isnull,
        classification_istartswith=classification_istartswith,
        classification_lt=classification_lt,
        classification_lte=classification_lte,
        classification_range=classification_range,
        classification_regex=classification_regex,
        classification_startswith=classification_startswith,
        limit=limit,
        ob_id=ob_id,
        ob_id_contained_by=ob_id_contained_by,
        ob_id_contains=ob_id_contains,
        ob_id_endswith=ob_id_endswith,
        ob_id_gt=ob_id_gt,
        ob_id_gte=ob_id_gte,
        ob_id_icontains=ob_id_icontains,
        ob_id_iendswith=ob_id_iendswith,
        ob_id_iexact=ob_id_iexact,
        ob_id_in=ob_id_in,
        ob_id_iregex=ob_id_iregex,
        ob_id_isnull=ob_id_isnull,
        ob_id_istartswith=ob_id_istartswith,
        ob_id_lt=ob_id_lt,
        ob_id_lte=ob_id_lte,
        ob_id_range=ob_id_range,
        ob_id_regex=ob_id_regex,
        ob_id_startswith=ob_id_startswith,
        offset=offset,
        ordering=ordering,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    classification: str | Unset = UNSET,
    classification_contains: str | Unset = UNSET,
    classification_endswith: str | Unset = UNSET,
    classification_gt: str | Unset = UNSET,
    classification_gte: str | Unset = UNSET,
    classification_icontains: str | Unset = UNSET,
    classification_iendswith: str | Unset = UNSET,
    classification_iexact: str | Unset = UNSET,
    classification_in: list[str] | Unset = UNSET,
    classification_iregex: str | Unset = UNSET,
    classification_isnull: bool | Unset = UNSET,
    classification_istartswith: str | Unset = UNSET,
    classification_lt: str | Unset = UNSET,
    classification_lte: str | Unset = UNSET,
    classification_range: list[str] | Unset = UNSET,
    classification_regex: str | Unset = UNSET,
    classification_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ob_id: int | Unset = UNSET,
    ob_id_contained_by: int | Unset = UNSET,
    ob_id_contains: int | Unset = UNSET,
    ob_id_endswith: int | Unset = UNSET,
    ob_id_gt: int | Unset = UNSET,
    ob_id_gte: int | Unset = UNSET,
    ob_id_icontains: int | Unset = UNSET,
    ob_id_iendswith: int | Unset = UNSET,
    ob_id_iexact: int | Unset = UNSET,
    ob_id_in: list[int] | Unset = UNSET,
    ob_id_iregex: int | Unset = UNSET,
    ob_id_isnull: bool | Unset = UNSET,
    ob_id_istartswith: int | Unset = UNSET,
    ob_id_lt: int | Unset = UNSET,
    ob_id_lte: int | Unset = UNSET,
    ob_id_range: list[int] | Unset = UNSET,
    ob_id_regex: int | Unset = UNSET,
    ob_id_startswith: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
) -> PaginatedLicenceClassificationReadList | None:
    """Get a list of LicenceClassification objects.

    Args:
        classification (str | Unset):
        classification_contains (str | Unset):
        classification_endswith (str | Unset):
        classification_gt (str | Unset):
        classification_gte (str | Unset):
        classification_icontains (str | Unset):
        classification_iendswith (str | Unset):
        classification_iexact (str | Unset):
        classification_in (list[str] | Unset):
        classification_iregex (str | Unset):
        classification_isnull (bool | Unset):
        classification_istartswith (str | Unset):
        classification_lt (str | Unset):
        classification_lte (str | Unset):
        classification_range (list[str] | Unset):
        classification_regex (str | Unset):
        classification_startswith (str | Unset):
        limit (int | Unset):
        ob_id (int | Unset):
        ob_id_contained_by (int | Unset):
        ob_id_contains (int | Unset):
        ob_id_endswith (int | Unset):
        ob_id_gt (int | Unset):
        ob_id_gte (int | Unset):
        ob_id_icontains (int | Unset):
        ob_id_iendswith (int | Unset):
        ob_id_iexact (int | Unset):
        ob_id_in (list[int] | Unset):
        ob_id_iregex (int | Unset):
        ob_id_isnull (bool | Unset):
        ob_id_istartswith (int | Unset):
        ob_id_lt (int | Unset):
        ob_id_lte (int | Unset):
        ob_id_range (list[int] | Unset):
        ob_id_regex (int | Unset):
        ob_id_startswith (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLicenceClassificationReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            classification=classification,
            classification_contains=classification_contains,
            classification_endswith=classification_endswith,
            classification_gt=classification_gt,
            classification_gte=classification_gte,
            classification_icontains=classification_icontains,
            classification_iendswith=classification_iendswith,
            classification_iexact=classification_iexact,
            classification_in=classification_in,
            classification_iregex=classification_iregex,
            classification_isnull=classification_isnull,
            classification_istartswith=classification_istartswith,
            classification_lt=classification_lt,
            classification_lte=classification_lte,
            classification_range=classification_range,
            classification_regex=classification_regex,
            classification_startswith=classification_startswith,
            limit=limit,
            ob_id=ob_id,
            ob_id_contained_by=ob_id_contained_by,
            ob_id_contains=ob_id_contains,
            ob_id_endswith=ob_id_endswith,
            ob_id_gt=ob_id_gt,
            ob_id_gte=ob_id_gte,
            ob_id_icontains=ob_id_icontains,
            ob_id_iendswith=ob_id_iendswith,
            ob_id_iexact=ob_id_iexact,
            ob_id_in=ob_id_in,
            ob_id_iregex=ob_id_iregex,
            ob_id_isnull=ob_id_isnull,
            ob_id_istartswith=ob_id_istartswith,
            ob_id_lt=ob_id_lt,
            ob_id_lte=ob_id_lte,
            ob_id_range=ob_id_range,
            ob_id_regex=ob_id_regex,
            ob_id_startswith=ob_id_startswith,
            offset=offset,
            ordering=ordering,
        )
    ).parsed
