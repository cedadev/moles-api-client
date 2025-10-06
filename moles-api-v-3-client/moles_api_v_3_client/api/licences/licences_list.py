from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_licence_write_list import PaginatedLicenceWriteList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    licence_classifications_classification: Union[Unset, str] = UNSET,
    licence_classifications_classification_in: Union[Unset, list[str]] = UNSET,
    licence_classifications_ob_id: Union[Unset, int] = UNSET,
    licence_classifications_ob_id_in: Union[Unset, list[int]] = UNSET,
    licence_url: Union[Unset, str] = UNSET,
    licence_url_contains: Union[Unset, str] = UNSET,
    licence_url_endswith: Union[Unset, str] = UNSET,
    licence_url_gt: Union[Unset, str] = UNSET,
    licence_url_gte: Union[Unset, str] = UNSET,
    licence_url_icontains: Union[Unset, str] = UNSET,
    licence_url_iendswith: Union[Unset, str] = UNSET,
    licence_url_iexact: Union[Unset, str] = UNSET,
    licence_url_in: Union[Unset, list[str]] = UNSET,
    licence_url_iregex: Union[Unset, str] = UNSET,
    licence_url_isnull: Union[Unset, bool] = UNSET,
    licence_url_istartswith: Union[Unset, str] = UNSET,
    licence_url_lt: Union[Unset, str] = UNSET,
    licence_url_lte: Union[Unset, str] = UNSET,
    licence_url_range: Union[Unset, list[str]] = UNSET,
    licence_url_regex: Union[Unset, str] = UNSET,
    licence_url_startswith: Union[Unset, str] = UNSET,
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

    params["licenceClassifications__classification"] = licence_classifications_classification

    json_licence_classifications_classification_in: Union[Unset, list[str]] = UNSET
    if not isinstance(licence_classifications_classification_in, Unset):
        json_licence_classifications_classification_in = licence_classifications_classification_in

    params["licenceClassifications__classification__in"] = json_licence_classifications_classification_in

    params["licenceClassifications__ob_id"] = licence_classifications_ob_id

    json_licence_classifications_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(licence_classifications_ob_id_in, Unset):
        json_licence_classifications_ob_id_in = licence_classifications_ob_id_in

    params["licenceClassifications__ob_id__in"] = json_licence_classifications_ob_id_in

    params["licenceURL"] = licence_url

    params["licenceURL__contains"] = licence_url_contains

    params["licenceURL__endswith"] = licence_url_endswith

    params["licenceURL__gt"] = licence_url_gt

    params["licenceURL__gte"] = licence_url_gte

    params["licenceURL__icontains"] = licence_url_icontains

    params["licenceURL__iendswith"] = licence_url_iendswith

    params["licenceURL__iexact"] = licence_url_iexact

    json_licence_url_in: Union[Unset, list[str]] = UNSET
    if not isinstance(licence_url_in, Unset):
        json_licence_url_in = licence_url_in

    params["licenceURL__in"] = json_licence_url_in

    params["licenceURL__iregex"] = licence_url_iregex

    params["licenceURL__isnull"] = licence_url_isnull

    params["licenceURL__istartswith"] = licence_url_istartswith

    params["licenceURL__lt"] = licence_url_lt

    params["licenceURL__lte"] = licence_url_lte

    json_licence_url_range: Union[Unset, list[str]] = UNSET
    if not isinstance(licence_url_range, Unset):
        json_licence_url_range = licence_url_range

    params["licenceURL__range"] = json_licence_url_range

    params["licenceURL__regex"] = licence_url_regex

    params["licenceURL__startswith"] = licence_url_startswith

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
        "url": "/v3/licences/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedLicenceWriteList]:
    if response.status_code == 200:
        response_200 = PaginatedLicenceWriteList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedLicenceWriteList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    licence_classifications_classification: Union[Unset, str] = UNSET,
    licence_classifications_classification_in: Union[Unset, list[str]] = UNSET,
    licence_classifications_ob_id: Union[Unset, int] = UNSET,
    licence_classifications_ob_id_in: Union[Unset, list[int]] = UNSET,
    licence_url: Union[Unset, str] = UNSET,
    licence_url_contains: Union[Unset, str] = UNSET,
    licence_url_endswith: Union[Unset, str] = UNSET,
    licence_url_gt: Union[Unset, str] = UNSET,
    licence_url_gte: Union[Unset, str] = UNSET,
    licence_url_icontains: Union[Unset, str] = UNSET,
    licence_url_iendswith: Union[Unset, str] = UNSET,
    licence_url_iexact: Union[Unset, str] = UNSET,
    licence_url_in: Union[Unset, list[str]] = UNSET,
    licence_url_iregex: Union[Unset, str] = UNSET,
    licence_url_isnull: Union[Unset, bool] = UNSET,
    licence_url_istartswith: Union[Unset, str] = UNSET,
    licence_url_lt: Union[Unset, str] = UNSET,
    licence_url_lte: Union[Unset, str] = UNSET,
    licence_url_range: Union[Unset, list[str]] = UNSET,
    licence_url_regex: Union[Unset, str] = UNSET,
    licence_url_startswith: Union[Unset, str] = UNSET,
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
) -> Response[PaginatedLicenceWriteList]:
    """Get a list of Licence objects.

    Args:
        licence_classifications_classification (Union[Unset, str]):
        licence_classifications_classification_in (Union[Unset, list[str]]):
        licence_classifications_ob_id (Union[Unset, int]):
        licence_classifications_ob_id_in (Union[Unset, list[int]]):
        licence_url (Union[Unset, str]):
        licence_url_contains (Union[Unset, str]):
        licence_url_endswith (Union[Unset, str]):
        licence_url_gt (Union[Unset, str]):
        licence_url_gte (Union[Unset, str]):
        licence_url_icontains (Union[Unset, str]):
        licence_url_iendswith (Union[Unset, str]):
        licence_url_iexact (Union[Unset, str]):
        licence_url_in (Union[Unset, list[str]]):
        licence_url_iregex (Union[Unset, str]):
        licence_url_isnull (Union[Unset, bool]):
        licence_url_istartswith (Union[Unset, str]):
        licence_url_lt (Union[Unset, str]):
        licence_url_lte (Union[Unset, str]):
        licence_url_range (Union[Unset, list[str]]):
        licence_url_regex (Union[Unset, str]):
        licence_url_startswith (Union[Unset, str]):
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
        Response[PaginatedLicenceWriteList]
    """

    kwargs = _get_kwargs(
        licence_classifications_classification=licence_classifications_classification,
        licence_classifications_classification_in=licence_classifications_classification_in,
        licence_classifications_ob_id=licence_classifications_ob_id,
        licence_classifications_ob_id_in=licence_classifications_ob_id_in,
        licence_url=licence_url,
        licence_url_contains=licence_url_contains,
        licence_url_endswith=licence_url_endswith,
        licence_url_gt=licence_url_gt,
        licence_url_gte=licence_url_gte,
        licence_url_icontains=licence_url_icontains,
        licence_url_iendswith=licence_url_iendswith,
        licence_url_iexact=licence_url_iexact,
        licence_url_in=licence_url_in,
        licence_url_iregex=licence_url_iregex,
        licence_url_isnull=licence_url_isnull,
        licence_url_istartswith=licence_url_istartswith,
        licence_url_lt=licence_url_lt,
        licence_url_lte=licence_url_lte,
        licence_url_range=licence_url_range,
        licence_url_regex=licence_url_regex,
        licence_url_startswith=licence_url_startswith,
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
    licence_classifications_classification: Union[Unset, str] = UNSET,
    licence_classifications_classification_in: Union[Unset, list[str]] = UNSET,
    licence_classifications_ob_id: Union[Unset, int] = UNSET,
    licence_classifications_ob_id_in: Union[Unset, list[int]] = UNSET,
    licence_url: Union[Unset, str] = UNSET,
    licence_url_contains: Union[Unset, str] = UNSET,
    licence_url_endswith: Union[Unset, str] = UNSET,
    licence_url_gt: Union[Unset, str] = UNSET,
    licence_url_gte: Union[Unset, str] = UNSET,
    licence_url_icontains: Union[Unset, str] = UNSET,
    licence_url_iendswith: Union[Unset, str] = UNSET,
    licence_url_iexact: Union[Unset, str] = UNSET,
    licence_url_in: Union[Unset, list[str]] = UNSET,
    licence_url_iregex: Union[Unset, str] = UNSET,
    licence_url_isnull: Union[Unset, bool] = UNSET,
    licence_url_istartswith: Union[Unset, str] = UNSET,
    licence_url_lt: Union[Unset, str] = UNSET,
    licence_url_lte: Union[Unset, str] = UNSET,
    licence_url_range: Union[Unset, list[str]] = UNSET,
    licence_url_regex: Union[Unset, str] = UNSET,
    licence_url_startswith: Union[Unset, str] = UNSET,
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
) -> Optional[PaginatedLicenceWriteList]:
    """Get a list of Licence objects.

    Args:
        licence_classifications_classification (Union[Unset, str]):
        licence_classifications_classification_in (Union[Unset, list[str]]):
        licence_classifications_ob_id (Union[Unset, int]):
        licence_classifications_ob_id_in (Union[Unset, list[int]]):
        licence_url (Union[Unset, str]):
        licence_url_contains (Union[Unset, str]):
        licence_url_endswith (Union[Unset, str]):
        licence_url_gt (Union[Unset, str]):
        licence_url_gte (Union[Unset, str]):
        licence_url_icontains (Union[Unset, str]):
        licence_url_iendswith (Union[Unset, str]):
        licence_url_iexact (Union[Unset, str]):
        licence_url_in (Union[Unset, list[str]]):
        licence_url_iregex (Union[Unset, str]):
        licence_url_isnull (Union[Unset, bool]):
        licence_url_istartswith (Union[Unset, str]):
        licence_url_lt (Union[Unset, str]):
        licence_url_lte (Union[Unset, str]):
        licence_url_range (Union[Unset, list[str]]):
        licence_url_regex (Union[Unset, str]):
        licence_url_startswith (Union[Unset, str]):
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
        PaginatedLicenceWriteList
    """

    return sync_detailed(
        client=client,
        licence_classifications_classification=licence_classifications_classification,
        licence_classifications_classification_in=licence_classifications_classification_in,
        licence_classifications_ob_id=licence_classifications_ob_id,
        licence_classifications_ob_id_in=licence_classifications_ob_id_in,
        licence_url=licence_url,
        licence_url_contains=licence_url_contains,
        licence_url_endswith=licence_url_endswith,
        licence_url_gt=licence_url_gt,
        licence_url_gte=licence_url_gte,
        licence_url_icontains=licence_url_icontains,
        licence_url_iendswith=licence_url_iendswith,
        licence_url_iexact=licence_url_iexact,
        licence_url_in=licence_url_in,
        licence_url_iregex=licence_url_iregex,
        licence_url_isnull=licence_url_isnull,
        licence_url_istartswith=licence_url_istartswith,
        licence_url_lt=licence_url_lt,
        licence_url_lte=licence_url_lte,
        licence_url_range=licence_url_range,
        licence_url_regex=licence_url_regex,
        licence_url_startswith=licence_url_startswith,
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
    licence_classifications_classification: Union[Unset, str] = UNSET,
    licence_classifications_classification_in: Union[Unset, list[str]] = UNSET,
    licence_classifications_ob_id: Union[Unset, int] = UNSET,
    licence_classifications_ob_id_in: Union[Unset, list[int]] = UNSET,
    licence_url: Union[Unset, str] = UNSET,
    licence_url_contains: Union[Unset, str] = UNSET,
    licence_url_endswith: Union[Unset, str] = UNSET,
    licence_url_gt: Union[Unset, str] = UNSET,
    licence_url_gte: Union[Unset, str] = UNSET,
    licence_url_icontains: Union[Unset, str] = UNSET,
    licence_url_iendswith: Union[Unset, str] = UNSET,
    licence_url_iexact: Union[Unset, str] = UNSET,
    licence_url_in: Union[Unset, list[str]] = UNSET,
    licence_url_iregex: Union[Unset, str] = UNSET,
    licence_url_isnull: Union[Unset, bool] = UNSET,
    licence_url_istartswith: Union[Unset, str] = UNSET,
    licence_url_lt: Union[Unset, str] = UNSET,
    licence_url_lte: Union[Unset, str] = UNSET,
    licence_url_range: Union[Unset, list[str]] = UNSET,
    licence_url_regex: Union[Unset, str] = UNSET,
    licence_url_startswith: Union[Unset, str] = UNSET,
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
) -> Response[PaginatedLicenceWriteList]:
    """Get a list of Licence objects.

    Args:
        licence_classifications_classification (Union[Unset, str]):
        licence_classifications_classification_in (Union[Unset, list[str]]):
        licence_classifications_ob_id (Union[Unset, int]):
        licence_classifications_ob_id_in (Union[Unset, list[int]]):
        licence_url (Union[Unset, str]):
        licence_url_contains (Union[Unset, str]):
        licence_url_endswith (Union[Unset, str]):
        licence_url_gt (Union[Unset, str]):
        licence_url_gte (Union[Unset, str]):
        licence_url_icontains (Union[Unset, str]):
        licence_url_iendswith (Union[Unset, str]):
        licence_url_iexact (Union[Unset, str]):
        licence_url_in (Union[Unset, list[str]]):
        licence_url_iregex (Union[Unset, str]):
        licence_url_isnull (Union[Unset, bool]):
        licence_url_istartswith (Union[Unset, str]):
        licence_url_lt (Union[Unset, str]):
        licence_url_lte (Union[Unset, str]):
        licence_url_range (Union[Unset, list[str]]):
        licence_url_regex (Union[Unset, str]):
        licence_url_startswith (Union[Unset, str]):
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
        Response[PaginatedLicenceWriteList]
    """

    kwargs = _get_kwargs(
        licence_classifications_classification=licence_classifications_classification,
        licence_classifications_classification_in=licence_classifications_classification_in,
        licence_classifications_ob_id=licence_classifications_ob_id,
        licence_classifications_ob_id_in=licence_classifications_ob_id_in,
        licence_url=licence_url,
        licence_url_contains=licence_url_contains,
        licence_url_endswith=licence_url_endswith,
        licence_url_gt=licence_url_gt,
        licence_url_gte=licence_url_gte,
        licence_url_icontains=licence_url_icontains,
        licence_url_iendswith=licence_url_iendswith,
        licence_url_iexact=licence_url_iexact,
        licence_url_in=licence_url_in,
        licence_url_iregex=licence_url_iregex,
        licence_url_isnull=licence_url_isnull,
        licence_url_istartswith=licence_url_istartswith,
        licence_url_lt=licence_url_lt,
        licence_url_lte=licence_url_lte,
        licence_url_range=licence_url_range,
        licence_url_regex=licence_url_regex,
        licence_url_startswith=licence_url_startswith,
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
    licence_classifications_classification: Union[Unset, str] = UNSET,
    licence_classifications_classification_in: Union[Unset, list[str]] = UNSET,
    licence_classifications_ob_id: Union[Unset, int] = UNSET,
    licence_classifications_ob_id_in: Union[Unset, list[int]] = UNSET,
    licence_url: Union[Unset, str] = UNSET,
    licence_url_contains: Union[Unset, str] = UNSET,
    licence_url_endswith: Union[Unset, str] = UNSET,
    licence_url_gt: Union[Unset, str] = UNSET,
    licence_url_gte: Union[Unset, str] = UNSET,
    licence_url_icontains: Union[Unset, str] = UNSET,
    licence_url_iendswith: Union[Unset, str] = UNSET,
    licence_url_iexact: Union[Unset, str] = UNSET,
    licence_url_in: Union[Unset, list[str]] = UNSET,
    licence_url_iregex: Union[Unset, str] = UNSET,
    licence_url_isnull: Union[Unset, bool] = UNSET,
    licence_url_istartswith: Union[Unset, str] = UNSET,
    licence_url_lt: Union[Unset, str] = UNSET,
    licence_url_lte: Union[Unset, str] = UNSET,
    licence_url_range: Union[Unset, list[str]] = UNSET,
    licence_url_regex: Union[Unset, str] = UNSET,
    licence_url_startswith: Union[Unset, str] = UNSET,
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
) -> Optional[PaginatedLicenceWriteList]:
    """Get a list of Licence objects.

    Args:
        licence_classifications_classification (Union[Unset, str]):
        licence_classifications_classification_in (Union[Unset, list[str]]):
        licence_classifications_ob_id (Union[Unset, int]):
        licence_classifications_ob_id_in (Union[Unset, list[int]]):
        licence_url (Union[Unset, str]):
        licence_url_contains (Union[Unset, str]):
        licence_url_endswith (Union[Unset, str]):
        licence_url_gt (Union[Unset, str]):
        licence_url_gte (Union[Unset, str]):
        licence_url_icontains (Union[Unset, str]):
        licence_url_iendswith (Union[Unset, str]):
        licence_url_iexact (Union[Unset, str]):
        licence_url_in (Union[Unset, list[str]]):
        licence_url_iregex (Union[Unset, str]):
        licence_url_isnull (Union[Unset, bool]):
        licence_url_istartswith (Union[Unset, str]):
        licence_url_lt (Union[Unset, str]):
        licence_url_lte (Union[Unset, str]):
        licence_url_range (Union[Unset, list[str]]):
        licence_url_regex (Union[Unset, str]):
        licence_url_startswith (Union[Unset, str]):
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
        PaginatedLicenceWriteList
    """

    return (
        await asyncio_detailed(
            client=client,
            licence_classifications_classification=licence_classifications_classification,
            licence_classifications_classification_in=licence_classifications_classification_in,
            licence_classifications_ob_id=licence_classifications_ob_id,
            licence_classifications_ob_id_in=licence_classifications_ob_id_in,
            licence_url=licence_url,
            licence_url_contains=licence_url_contains,
            licence_url_endswith=licence_url_endswith,
            licence_url_gt=licence_url_gt,
            licence_url_gte=licence_url_gte,
            licence_url_icontains=licence_url_icontains,
            licence_url_iendswith=licence_url_iendswith,
            licence_url_iexact=licence_url_iexact,
            licence_url_in=licence_url_in,
            licence_url_iregex=licence_url_iregex,
            licence_url_isnull=licence_url_isnull,
            licence_url_istartswith=licence_url_istartswith,
            licence_url_lt=licence_url_lt,
            licence_url_lte=licence_url_lte,
            licence_url_range=licence_url_range,
            licence_url_regex=licence_url_regex,
            licence_url_startswith=licence_url_startswith,
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
