from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_licence_classification_write_list import PaginatedLicenceClassificationWriteList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    classification: Union[Unset, str] = UNSET,
    classification_contains: Union[Unset, str] = UNSET,
    classification_endswith: Union[Unset, str] = UNSET,
    classification_gt: Union[Unset, str] = UNSET,
    classification_gte: Union[Unset, str] = UNSET,
    classification_icontains: Union[Unset, str] = UNSET,
    classification_iendswith: Union[Unset, str] = UNSET,
    classification_iexact: Union[Unset, str] = UNSET,
    classification_in: Union[Unset, list[str]] = UNSET,
    classification_iregex: Union[Unset, str] = UNSET,
    classification_isnull: Union[Unset, bool] = UNSET,
    classification_istartswith: Union[Unset, str] = UNSET,
    classification_lt: Union[Unset, str] = UNSET,
    classification_lte: Union[Unset, str] = UNSET,
    classification_range: Union[Unset, list[str]] = UNSET,
    classification_regex: Union[Unset, str] = UNSET,
    classification_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    ob_id: Union[Unset, int] = UNSET,
    ob_id_contained_by: Union[Unset, int] = UNSET,
    ob_id_contains: Union[Unset, int] = UNSET,
    ob_id_endswith: Union[Unset, int] = UNSET,
    ob_id_gt: Union[Unset, int] = UNSET,
    ob_id_gte: Union[Unset, int] = UNSET,
    ob_id_icontains: Union[Unset, int] = UNSET,
    ob_id_iendswith: Union[Unset, int] = UNSET,
    ob_id_iexact: Union[Unset, int] = UNSET,
    ob_id_in: Union[Unset, list[int]] = UNSET,
    ob_id_iregex: Union[Unset, int] = UNSET,
    ob_id_isnull: Union[Unset, bool] = UNSET,
    ob_id_istartswith: Union[Unset, int] = UNSET,
    ob_id_lt: Union[Unset, int] = UNSET,
    ob_id_lte: Union[Unset, int] = UNSET,
    ob_id_range: Union[Unset, list[int]] = UNSET,
    ob_id_regex: Union[Unset, int] = UNSET,
    ob_id_startswith: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
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

    json_classification_in: Union[Unset, list[str]] = UNSET
    if not isinstance(classification_in, Unset):
        json_classification_in = classification_in

    params["classification__in"] = json_classification_in

    params["classification__iregex"] = classification_iregex

    params["classification__isnull"] = classification_isnull

    params["classification__istartswith"] = classification_istartswith

    params["classification__lt"] = classification_lt

    params["classification__lte"] = classification_lte

    json_classification_range: Union[Unset, list[str]] = UNSET
    if not isinstance(classification_range, Unset):
        json_classification_range = classification_range

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

    json_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_in, Unset):
        json_ob_id_in = ob_id_in

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ob_id_range

    params["ob_id__range"] = json_ob_id_range

    params["ob_id__regex"] = ob_id_regex

    params["ob_id__startswith"] = ob_id_startswith

    params["offset"] = offset

    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/licenceclassifications/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedLicenceClassificationWriteList]:
    if response.status_code == 200:
        response_200 = PaginatedLicenceClassificationWriteList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedLicenceClassificationWriteList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    classification: Union[Unset, str] = UNSET,
    classification_contains: Union[Unset, str] = UNSET,
    classification_endswith: Union[Unset, str] = UNSET,
    classification_gt: Union[Unset, str] = UNSET,
    classification_gte: Union[Unset, str] = UNSET,
    classification_icontains: Union[Unset, str] = UNSET,
    classification_iendswith: Union[Unset, str] = UNSET,
    classification_iexact: Union[Unset, str] = UNSET,
    classification_in: Union[Unset, list[str]] = UNSET,
    classification_iregex: Union[Unset, str] = UNSET,
    classification_isnull: Union[Unset, bool] = UNSET,
    classification_istartswith: Union[Unset, str] = UNSET,
    classification_lt: Union[Unset, str] = UNSET,
    classification_lte: Union[Unset, str] = UNSET,
    classification_range: Union[Unset, list[str]] = UNSET,
    classification_regex: Union[Unset, str] = UNSET,
    classification_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    ob_id: Union[Unset, int] = UNSET,
    ob_id_contained_by: Union[Unset, int] = UNSET,
    ob_id_contains: Union[Unset, int] = UNSET,
    ob_id_endswith: Union[Unset, int] = UNSET,
    ob_id_gt: Union[Unset, int] = UNSET,
    ob_id_gte: Union[Unset, int] = UNSET,
    ob_id_icontains: Union[Unset, int] = UNSET,
    ob_id_iendswith: Union[Unset, int] = UNSET,
    ob_id_iexact: Union[Unset, int] = UNSET,
    ob_id_in: Union[Unset, list[int]] = UNSET,
    ob_id_iregex: Union[Unset, int] = UNSET,
    ob_id_isnull: Union[Unset, bool] = UNSET,
    ob_id_istartswith: Union[Unset, int] = UNSET,
    ob_id_lt: Union[Unset, int] = UNSET,
    ob_id_lte: Union[Unset, int] = UNSET,
    ob_id_range: Union[Unset, list[int]] = UNSET,
    ob_id_regex: Union[Unset, int] = UNSET,
    ob_id_startswith: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
) -> Response[PaginatedLicenceClassificationWriteList]:
    """Get a list of LicenceClassification objects.

    Args:
        classification (Union[Unset, str]):
        classification_contains (Union[Unset, str]):
        classification_endswith (Union[Unset, str]):
        classification_gt (Union[Unset, str]):
        classification_gte (Union[Unset, str]):
        classification_icontains (Union[Unset, str]):
        classification_iendswith (Union[Unset, str]):
        classification_iexact (Union[Unset, str]):
        classification_in (Union[Unset, list[str]]):
        classification_iregex (Union[Unset, str]):
        classification_isnull (Union[Unset, bool]):
        classification_istartswith (Union[Unset, str]):
        classification_lt (Union[Unset, str]):
        classification_lte (Union[Unset, str]):
        classification_range (Union[Unset, list[str]]):
        classification_regex (Union[Unset, str]):
        classification_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        ob_id (Union[Unset, int]):
        ob_id_contained_by (Union[Unset, int]):
        ob_id_contains (Union[Unset, int]):
        ob_id_endswith (Union[Unset, int]):
        ob_id_gt (Union[Unset, int]):
        ob_id_gte (Union[Unset, int]):
        ob_id_icontains (Union[Unset, int]):
        ob_id_iendswith (Union[Unset, int]):
        ob_id_iexact (Union[Unset, int]):
        ob_id_in (Union[Unset, list[int]]):
        ob_id_iregex (Union[Unset, int]):
        ob_id_isnull (Union[Unset, bool]):
        ob_id_istartswith (Union[Unset, int]):
        ob_id_lt (Union[Unset, int]):
        ob_id_lte (Union[Unset, int]):
        ob_id_range (Union[Unset, list[int]]):
        ob_id_regex (Union[Unset, int]):
        ob_id_startswith (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLicenceClassificationWriteList]
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
    classification: Union[Unset, str] = UNSET,
    classification_contains: Union[Unset, str] = UNSET,
    classification_endswith: Union[Unset, str] = UNSET,
    classification_gt: Union[Unset, str] = UNSET,
    classification_gte: Union[Unset, str] = UNSET,
    classification_icontains: Union[Unset, str] = UNSET,
    classification_iendswith: Union[Unset, str] = UNSET,
    classification_iexact: Union[Unset, str] = UNSET,
    classification_in: Union[Unset, list[str]] = UNSET,
    classification_iregex: Union[Unset, str] = UNSET,
    classification_isnull: Union[Unset, bool] = UNSET,
    classification_istartswith: Union[Unset, str] = UNSET,
    classification_lt: Union[Unset, str] = UNSET,
    classification_lte: Union[Unset, str] = UNSET,
    classification_range: Union[Unset, list[str]] = UNSET,
    classification_regex: Union[Unset, str] = UNSET,
    classification_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    ob_id: Union[Unset, int] = UNSET,
    ob_id_contained_by: Union[Unset, int] = UNSET,
    ob_id_contains: Union[Unset, int] = UNSET,
    ob_id_endswith: Union[Unset, int] = UNSET,
    ob_id_gt: Union[Unset, int] = UNSET,
    ob_id_gte: Union[Unset, int] = UNSET,
    ob_id_icontains: Union[Unset, int] = UNSET,
    ob_id_iendswith: Union[Unset, int] = UNSET,
    ob_id_iexact: Union[Unset, int] = UNSET,
    ob_id_in: Union[Unset, list[int]] = UNSET,
    ob_id_iregex: Union[Unset, int] = UNSET,
    ob_id_isnull: Union[Unset, bool] = UNSET,
    ob_id_istartswith: Union[Unset, int] = UNSET,
    ob_id_lt: Union[Unset, int] = UNSET,
    ob_id_lte: Union[Unset, int] = UNSET,
    ob_id_range: Union[Unset, list[int]] = UNSET,
    ob_id_regex: Union[Unset, int] = UNSET,
    ob_id_startswith: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
) -> Optional[PaginatedLicenceClassificationWriteList]:
    """Get a list of LicenceClassification objects.

    Args:
        classification (Union[Unset, str]):
        classification_contains (Union[Unset, str]):
        classification_endswith (Union[Unset, str]):
        classification_gt (Union[Unset, str]):
        classification_gte (Union[Unset, str]):
        classification_icontains (Union[Unset, str]):
        classification_iendswith (Union[Unset, str]):
        classification_iexact (Union[Unset, str]):
        classification_in (Union[Unset, list[str]]):
        classification_iregex (Union[Unset, str]):
        classification_isnull (Union[Unset, bool]):
        classification_istartswith (Union[Unset, str]):
        classification_lt (Union[Unset, str]):
        classification_lte (Union[Unset, str]):
        classification_range (Union[Unset, list[str]]):
        classification_regex (Union[Unset, str]):
        classification_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        ob_id (Union[Unset, int]):
        ob_id_contained_by (Union[Unset, int]):
        ob_id_contains (Union[Unset, int]):
        ob_id_endswith (Union[Unset, int]):
        ob_id_gt (Union[Unset, int]):
        ob_id_gte (Union[Unset, int]):
        ob_id_icontains (Union[Unset, int]):
        ob_id_iendswith (Union[Unset, int]):
        ob_id_iexact (Union[Unset, int]):
        ob_id_in (Union[Unset, list[int]]):
        ob_id_iregex (Union[Unset, int]):
        ob_id_isnull (Union[Unset, bool]):
        ob_id_istartswith (Union[Unset, int]):
        ob_id_lt (Union[Unset, int]):
        ob_id_lte (Union[Unset, int]):
        ob_id_range (Union[Unset, list[int]]):
        ob_id_regex (Union[Unset, int]):
        ob_id_startswith (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLicenceClassificationWriteList
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
    classification: Union[Unset, str] = UNSET,
    classification_contains: Union[Unset, str] = UNSET,
    classification_endswith: Union[Unset, str] = UNSET,
    classification_gt: Union[Unset, str] = UNSET,
    classification_gte: Union[Unset, str] = UNSET,
    classification_icontains: Union[Unset, str] = UNSET,
    classification_iendswith: Union[Unset, str] = UNSET,
    classification_iexact: Union[Unset, str] = UNSET,
    classification_in: Union[Unset, list[str]] = UNSET,
    classification_iregex: Union[Unset, str] = UNSET,
    classification_isnull: Union[Unset, bool] = UNSET,
    classification_istartswith: Union[Unset, str] = UNSET,
    classification_lt: Union[Unset, str] = UNSET,
    classification_lte: Union[Unset, str] = UNSET,
    classification_range: Union[Unset, list[str]] = UNSET,
    classification_regex: Union[Unset, str] = UNSET,
    classification_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    ob_id: Union[Unset, int] = UNSET,
    ob_id_contained_by: Union[Unset, int] = UNSET,
    ob_id_contains: Union[Unset, int] = UNSET,
    ob_id_endswith: Union[Unset, int] = UNSET,
    ob_id_gt: Union[Unset, int] = UNSET,
    ob_id_gte: Union[Unset, int] = UNSET,
    ob_id_icontains: Union[Unset, int] = UNSET,
    ob_id_iendswith: Union[Unset, int] = UNSET,
    ob_id_iexact: Union[Unset, int] = UNSET,
    ob_id_in: Union[Unset, list[int]] = UNSET,
    ob_id_iregex: Union[Unset, int] = UNSET,
    ob_id_isnull: Union[Unset, bool] = UNSET,
    ob_id_istartswith: Union[Unset, int] = UNSET,
    ob_id_lt: Union[Unset, int] = UNSET,
    ob_id_lte: Union[Unset, int] = UNSET,
    ob_id_range: Union[Unset, list[int]] = UNSET,
    ob_id_regex: Union[Unset, int] = UNSET,
    ob_id_startswith: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
) -> Response[PaginatedLicenceClassificationWriteList]:
    """Get a list of LicenceClassification objects.

    Args:
        classification (Union[Unset, str]):
        classification_contains (Union[Unset, str]):
        classification_endswith (Union[Unset, str]):
        classification_gt (Union[Unset, str]):
        classification_gte (Union[Unset, str]):
        classification_icontains (Union[Unset, str]):
        classification_iendswith (Union[Unset, str]):
        classification_iexact (Union[Unset, str]):
        classification_in (Union[Unset, list[str]]):
        classification_iregex (Union[Unset, str]):
        classification_isnull (Union[Unset, bool]):
        classification_istartswith (Union[Unset, str]):
        classification_lt (Union[Unset, str]):
        classification_lte (Union[Unset, str]):
        classification_range (Union[Unset, list[str]]):
        classification_regex (Union[Unset, str]):
        classification_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        ob_id (Union[Unset, int]):
        ob_id_contained_by (Union[Unset, int]):
        ob_id_contains (Union[Unset, int]):
        ob_id_endswith (Union[Unset, int]):
        ob_id_gt (Union[Unset, int]):
        ob_id_gte (Union[Unset, int]):
        ob_id_icontains (Union[Unset, int]):
        ob_id_iendswith (Union[Unset, int]):
        ob_id_iexact (Union[Unset, int]):
        ob_id_in (Union[Unset, list[int]]):
        ob_id_iregex (Union[Unset, int]):
        ob_id_isnull (Union[Unset, bool]):
        ob_id_istartswith (Union[Unset, int]):
        ob_id_lt (Union[Unset, int]):
        ob_id_lte (Union[Unset, int]):
        ob_id_range (Union[Unset, list[int]]):
        ob_id_regex (Union[Unset, int]):
        ob_id_startswith (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLicenceClassificationWriteList]
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
    classification: Union[Unset, str] = UNSET,
    classification_contains: Union[Unset, str] = UNSET,
    classification_endswith: Union[Unset, str] = UNSET,
    classification_gt: Union[Unset, str] = UNSET,
    classification_gte: Union[Unset, str] = UNSET,
    classification_icontains: Union[Unset, str] = UNSET,
    classification_iendswith: Union[Unset, str] = UNSET,
    classification_iexact: Union[Unset, str] = UNSET,
    classification_in: Union[Unset, list[str]] = UNSET,
    classification_iregex: Union[Unset, str] = UNSET,
    classification_isnull: Union[Unset, bool] = UNSET,
    classification_istartswith: Union[Unset, str] = UNSET,
    classification_lt: Union[Unset, str] = UNSET,
    classification_lte: Union[Unset, str] = UNSET,
    classification_range: Union[Unset, list[str]] = UNSET,
    classification_regex: Union[Unset, str] = UNSET,
    classification_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    ob_id: Union[Unset, int] = UNSET,
    ob_id_contained_by: Union[Unset, int] = UNSET,
    ob_id_contains: Union[Unset, int] = UNSET,
    ob_id_endswith: Union[Unset, int] = UNSET,
    ob_id_gt: Union[Unset, int] = UNSET,
    ob_id_gte: Union[Unset, int] = UNSET,
    ob_id_icontains: Union[Unset, int] = UNSET,
    ob_id_iendswith: Union[Unset, int] = UNSET,
    ob_id_iexact: Union[Unset, int] = UNSET,
    ob_id_in: Union[Unset, list[int]] = UNSET,
    ob_id_iregex: Union[Unset, int] = UNSET,
    ob_id_isnull: Union[Unset, bool] = UNSET,
    ob_id_istartswith: Union[Unset, int] = UNSET,
    ob_id_lt: Union[Unset, int] = UNSET,
    ob_id_lte: Union[Unset, int] = UNSET,
    ob_id_range: Union[Unset, list[int]] = UNSET,
    ob_id_regex: Union[Unset, int] = UNSET,
    ob_id_startswith: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
) -> Optional[PaginatedLicenceClassificationWriteList]:
    """Get a list of LicenceClassification objects.

    Args:
        classification (Union[Unset, str]):
        classification_contains (Union[Unset, str]):
        classification_endswith (Union[Unset, str]):
        classification_gt (Union[Unset, str]):
        classification_gte (Union[Unset, str]):
        classification_icontains (Union[Unset, str]):
        classification_iendswith (Union[Unset, str]):
        classification_iexact (Union[Unset, str]):
        classification_in (Union[Unset, list[str]]):
        classification_iregex (Union[Unset, str]):
        classification_isnull (Union[Unset, bool]):
        classification_istartswith (Union[Unset, str]):
        classification_lt (Union[Unset, str]):
        classification_lte (Union[Unset, str]):
        classification_range (Union[Unset, list[str]]):
        classification_regex (Union[Unset, str]):
        classification_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        ob_id (Union[Unset, int]):
        ob_id_contained_by (Union[Unset, int]):
        ob_id_contains (Union[Unset, int]):
        ob_id_endswith (Union[Unset, int]):
        ob_id_gt (Union[Unset, int]):
        ob_id_gte (Union[Unset, int]):
        ob_id_icontains (Union[Unset, int]):
        ob_id_iendswith (Union[Unset, int]):
        ob_id_iexact (Union[Unset, int]):
        ob_id_in (Union[Unset, list[int]]):
        ob_id_iregex (Union[Unset, int]):
        ob_id_isnull (Union[Unset, bool]):
        ob_id_istartswith (Union[Unset, int]):
        ob_id_lt (Union[Unset, int]):
        ob_id_lte (Union[Unset, int]):
        ob_id_range (Union[Unset, list[int]]):
        ob_id_regex (Union[Unset, int]):
        ob_id_startswith (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLicenceClassificationWriteList
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
