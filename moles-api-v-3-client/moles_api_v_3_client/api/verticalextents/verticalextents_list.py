from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_vertical_extent_read_list import PaginatedVerticalExtentReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    highest_level_bound: Union[Unset, float] = UNSET,
    highest_level_bound_contained_by: Union[Unset, float] = UNSET,
    highest_level_bound_contains: Union[Unset, float] = UNSET,
    highest_level_bound_endswith: Union[Unset, float] = UNSET,
    highest_level_bound_gt: Union[Unset, float] = UNSET,
    highest_level_bound_gte: Union[Unset, float] = UNSET,
    highest_level_bound_icontains: Union[Unset, float] = UNSET,
    highest_level_bound_iendswith: Union[Unset, float] = UNSET,
    highest_level_bound_iexact: Union[Unset, float] = UNSET,
    highest_level_bound_in: Union[Unset, list[float]] = UNSET,
    highest_level_bound_iregex: Union[Unset, float] = UNSET,
    highest_level_bound_isnull: Union[Unset, bool] = UNSET,
    highest_level_bound_istartswith: Union[Unset, float] = UNSET,
    highest_level_bound_lt: Union[Unset, float] = UNSET,
    highest_level_bound_lte: Union[Unset, float] = UNSET,
    highest_level_bound_range: Union[Unset, list[float]] = UNSET,
    highest_level_bound_regex: Union[Unset, float] = UNSET,
    highest_level_bound_startswith: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    lowest_level_bound: Union[Unset, float] = UNSET,
    lowest_level_bound_contained_by: Union[Unset, float] = UNSET,
    lowest_level_bound_contains: Union[Unset, float] = UNSET,
    lowest_level_bound_endswith: Union[Unset, float] = UNSET,
    lowest_level_bound_gt: Union[Unset, float] = UNSET,
    lowest_level_bound_gte: Union[Unset, float] = UNSET,
    lowest_level_bound_icontains: Union[Unset, float] = UNSET,
    lowest_level_bound_iendswith: Union[Unset, float] = UNSET,
    lowest_level_bound_iexact: Union[Unset, float] = UNSET,
    lowest_level_bound_in: Union[Unset, list[float]] = UNSET,
    lowest_level_bound_iregex: Union[Unset, float] = UNSET,
    lowest_level_bound_isnull: Union[Unset, bool] = UNSET,
    lowest_level_bound_istartswith: Union[Unset, float] = UNSET,
    lowest_level_bound_lt: Union[Unset, float] = UNSET,
    lowest_level_bound_lte: Union[Unset, float] = UNSET,
    lowest_level_bound_range: Union[Unset, list[float]] = UNSET,
    lowest_level_bound_regex: Union[Unset, float] = UNSET,
    lowest_level_bound_startswith: Union[Unset, float] = UNSET,
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
    units: Union[Unset, str] = UNSET,
    units_contains: Union[Unset, str] = UNSET,
    units_endswith: Union[Unset, str] = UNSET,
    units_gt: Union[Unset, str] = UNSET,
    units_gte: Union[Unset, str] = UNSET,
    units_icontains: Union[Unset, str] = UNSET,
    units_iendswith: Union[Unset, str] = UNSET,
    units_iexact: Union[Unset, str] = UNSET,
    units_in: Union[Unset, list[str]] = UNSET,
    units_iregex: Union[Unset, str] = UNSET,
    units_isnull: Union[Unset, bool] = UNSET,
    units_istartswith: Union[Unset, str] = UNSET,
    units_lt: Union[Unset, str] = UNSET,
    units_lte: Union[Unset, str] = UNSET,
    units_range: Union[Unset, list[str]] = UNSET,
    units_regex: Union[Unset, str] = UNSET,
    units_startswith: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["highestLevelBound"] = highest_level_bound

    params["highestLevelBound__contained_by"] = highest_level_bound_contained_by

    params["highestLevelBound__contains"] = highest_level_bound_contains

    params["highestLevelBound__endswith"] = highest_level_bound_endswith

    params["highestLevelBound__gt"] = highest_level_bound_gt

    params["highestLevelBound__gte"] = highest_level_bound_gte

    params["highestLevelBound__icontains"] = highest_level_bound_icontains

    params["highestLevelBound__iendswith"] = highest_level_bound_iendswith

    params["highestLevelBound__iexact"] = highest_level_bound_iexact

    json_highest_level_bound_in: Union[Unset, list[float]] = UNSET
    if not isinstance(highest_level_bound_in, Unset):
        json_highest_level_bound_in = ",".join(map(str, highest_level_bound_in))

    params["highestLevelBound__in"] = json_highest_level_bound_in

    params["highestLevelBound__iregex"] = highest_level_bound_iregex

    params["highestLevelBound__isnull"] = highest_level_bound_isnull

    params["highestLevelBound__istartswith"] = highest_level_bound_istartswith

    params["highestLevelBound__lt"] = highest_level_bound_lt

    params["highestLevelBound__lte"] = highest_level_bound_lte

    json_highest_level_bound_range: Union[Unset, list[float]] = UNSET
    if not isinstance(highest_level_bound_range, Unset):
        json_highest_level_bound_range = ",".join(map(str, highest_level_bound_range))

    params["highestLevelBound__range"] = json_highest_level_bound_range

    params["highestLevelBound__regex"] = highest_level_bound_regex

    params["highestLevelBound__startswith"] = highest_level_bound_startswith

    params["limit"] = limit

    params["lowestLevelBound"] = lowest_level_bound

    params["lowestLevelBound__contained_by"] = lowest_level_bound_contained_by

    params["lowestLevelBound__contains"] = lowest_level_bound_contains

    params["lowestLevelBound__endswith"] = lowest_level_bound_endswith

    params["lowestLevelBound__gt"] = lowest_level_bound_gt

    params["lowestLevelBound__gte"] = lowest_level_bound_gte

    params["lowestLevelBound__icontains"] = lowest_level_bound_icontains

    params["lowestLevelBound__iendswith"] = lowest_level_bound_iendswith

    params["lowestLevelBound__iexact"] = lowest_level_bound_iexact

    json_lowest_level_bound_in: Union[Unset, list[float]] = UNSET
    if not isinstance(lowest_level_bound_in, Unset):
        json_lowest_level_bound_in = ",".join(map(str, lowest_level_bound_in))

    params["lowestLevelBound__in"] = json_lowest_level_bound_in

    params["lowestLevelBound__iregex"] = lowest_level_bound_iregex

    params["lowestLevelBound__isnull"] = lowest_level_bound_isnull

    params["lowestLevelBound__istartswith"] = lowest_level_bound_istartswith

    params["lowestLevelBound__lt"] = lowest_level_bound_lt

    params["lowestLevelBound__lte"] = lowest_level_bound_lte

    json_lowest_level_bound_range: Union[Unset, list[float]] = UNSET
    if not isinstance(lowest_level_bound_range, Unset):
        json_lowest_level_bound_range = ",".join(map(str, lowest_level_bound_range))

    params["lowestLevelBound__range"] = json_lowest_level_bound_range

    params["lowestLevelBound__regex"] = lowest_level_bound_regex

    params["lowestLevelBound__startswith"] = lowest_level_bound_startswith

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
        json_ob_id_in = ",".join(map(str, ob_id_in))

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ",".join(map(str, ob_id_range))

    params["ob_id__range"] = json_ob_id_range

    params["ob_id__regex"] = ob_id_regex

    params["ob_id__startswith"] = ob_id_startswith

    params["offset"] = offset

    params["ordering"] = ordering

    params["units"] = units

    params["units__contains"] = units_contains

    params["units__endswith"] = units_endswith

    params["units__gt"] = units_gt

    params["units__gte"] = units_gte

    params["units__icontains"] = units_icontains

    params["units__iendswith"] = units_iendswith

    params["units__iexact"] = units_iexact

    json_units_in: Union[Unset, list[str]] = UNSET
    if not isinstance(units_in, Unset):
        json_units_in = ",".join(map(str, units_in))

    params["units__in"] = json_units_in

    params["units__iregex"] = units_iregex

    params["units__isnull"] = units_isnull

    params["units__istartswith"] = units_istartswith

    params["units__lt"] = units_lt

    params["units__lte"] = units_lte

    json_units_range: Union[Unset, list[str]] = UNSET
    if not isinstance(units_range, Unset):
        json_units_range = ",".join(map(str, units_range))

    params["units__range"] = json_units_range

    params["units__regex"] = units_regex

    params["units__startswith"] = units_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/verticalextents/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedVerticalExtentReadList]:
    if response.status_code == 200:
        response_200 = PaginatedVerticalExtentReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedVerticalExtentReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    highest_level_bound: Union[Unset, float] = UNSET,
    highest_level_bound_contained_by: Union[Unset, float] = UNSET,
    highest_level_bound_contains: Union[Unset, float] = UNSET,
    highest_level_bound_endswith: Union[Unset, float] = UNSET,
    highest_level_bound_gt: Union[Unset, float] = UNSET,
    highest_level_bound_gte: Union[Unset, float] = UNSET,
    highest_level_bound_icontains: Union[Unset, float] = UNSET,
    highest_level_bound_iendswith: Union[Unset, float] = UNSET,
    highest_level_bound_iexact: Union[Unset, float] = UNSET,
    highest_level_bound_in: Union[Unset, list[float]] = UNSET,
    highest_level_bound_iregex: Union[Unset, float] = UNSET,
    highest_level_bound_isnull: Union[Unset, bool] = UNSET,
    highest_level_bound_istartswith: Union[Unset, float] = UNSET,
    highest_level_bound_lt: Union[Unset, float] = UNSET,
    highest_level_bound_lte: Union[Unset, float] = UNSET,
    highest_level_bound_range: Union[Unset, list[float]] = UNSET,
    highest_level_bound_regex: Union[Unset, float] = UNSET,
    highest_level_bound_startswith: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    lowest_level_bound: Union[Unset, float] = UNSET,
    lowest_level_bound_contained_by: Union[Unset, float] = UNSET,
    lowest_level_bound_contains: Union[Unset, float] = UNSET,
    lowest_level_bound_endswith: Union[Unset, float] = UNSET,
    lowest_level_bound_gt: Union[Unset, float] = UNSET,
    lowest_level_bound_gte: Union[Unset, float] = UNSET,
    lowest_level_bound_icontains: Union[Unset, float] = UNSET,
    lowest_level_bound_iendswith: Union[Unset, float] = UNSET,
    lowest_level_bound_iexact: Union[Unset, float] = UNSET,
    lowest_level_bound_in: Union[Unset, list[float]] = UNSET,
    lowest_level_bound_iregex: Union[Unset, float] = UNSET,
    lowest_level_bound_isnull: Union[Unset, bool] = UNSET,
    lowest_level_bound_istartswith: Union[Unset, float] = UNSET,
    lowest_level_bound_lt: Union[Unset, float] = UNSET,
    lowest_level_bound_lte: Union[Unset, float] = UNSET,
    lowest_level_bound_range: Union[Unset, list[float]] = UNSET,
    lowest_level_bound_regex: Union[Unset, float] = UNSET,
    lowest_level_bound_startswith: Union[Unset, float] = UNSET,
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
    units: Union[Unset, str] = UNSET,
    units_contains: Union[Unset, str] = UNSET,
    units_endswith: Union[Unset, str] = UNSET,
    units_gt: Union[Unset, str] = UNSET,
    units_gte: Union[Unset, str] = UNSET,
    units_icontains: Union[Unset, str] = UNSET,
    units_iendswith: Union[Unset, str] = UNSET,
    units_iexact: Union[Unset, str] = UNSET,
    units_in: Union[Unset, list[str]] = UNSET,
    units_iregex: Union[Unset, str] = UNSET,
    units_isnull: Union[Unset, bool] = UNSET,
    units_istartswith: Union[Unset, str] = UNSET,
    units_lt: Union[Unset, str] = UNSET,
    units_lte: Union[Unset, str] = UNSET,
    units_range: Union[Unset, list[str]] = UNSET,
    units_regex: Union[Unset, str] = UNSET,
    units_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedVerticalExtentReadList]:
    """Get a list of VerticalExtent objects.

    Args:
        highest_level_bound (Union[Unset, float]):
        highest_level_bound_contained_by (Union[Unset, float]):
        highest_level_bound_contains (Union[Unset, float]):
        highest_level_bound_endswith (Union[Unset, float]):
        highest_level_bound_gt (Union[Unset, float]):
        highest_level_bound_gte (Union[Unset, float]):
        highest_level_bound_icontains (Union[Unset, float]):
        highest_level_bound_iendswith (Union[Unset, float]):
        highest_level_bound_iexact (Union[Unset, float]):
        highest_level_bound_in (Union[Unset, list[float]]):
        highest_level_bound_iregex (Union[Unset, float]):
        highest_level_bound_isnull (Union[Unset, bool]):
        highest_level_bound_istartswith (Union[Unset, float]):
        highest_level_bound_lt (Union[Unset, float]):
        highest_level_bound_lte (Union[Unset, float]):
        highest_level_bound_range (Union[Unset, list[float]]):
        highest_level_bound_regex (Union[Unset, float]):
        highest_level_bound_startswith (Union[Unset, float]):
        limit (Union[Unset, int]):
        lowest_level_bound (Union[Unset, float]):
        lowest_level_bound_contained_by (Union[Unset, float]):
        lowest_level_bound_contains (Union[Unset, float]):
        lowest_level_bound_endswith (Union[Unset, float]):
        lowest_level_bound_gt (Union[Unset, float]):
        lowest_level_bound_gte (Union[Unset, float]):
        lowest_level_bound_icontains (Union[Unset, float]):
        lowest_level_bound_iendswith (Union[Unset, float]):
        lowest_level_bound_iexact (Union[Unset, float]):
        lowest_level_bound_in (Union[Unset, list[float]]):
        lowest_level_bound_iregex (Union[Unset, float]):
        lowest_level_bound_isnull (Union[Unset, bool]):
        lowest_level_bound_istartswith (Union[Unset, float]):
        lowest_level_bound_lt (Union[Unset, float]):
        lowest_level_bound_lte (Union[Unset, float]):
        lowest_level_bound_range (Union[Unset, list[float]]):
        lowest_level_bound_regex (Union[Unset, float]):
        lowest_level_bound_startswith (Union[Unset, float]):
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
        units (Union[Unset, str]):
        units_contains (Union[Unset, str]):
        units_endswith (Union[Unset, str]):
        units_gt (Union[Unset, str]):
        units_gte (Union[Unset, str]):
        units_icontains (Union[Unset, str]):
        units_iendswith (Union[Unset, str]):
        units_iexact (Union[Unset, str]):
        units_in (Union[Unset, list[str]]):
        units_iregex (Union[Unset, str]):
        units_isnull (Union[Unset, bool]):
        units_istartswith (Union[Unset, str]):
        units_lt (Union[Unset, str]):
        units_lte (Union[Unset, str]):
        units_range (Union[Unset, list[str]]):
        units_regex (Union[Unset, str]):
        units_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVerticalExtentReadList]
    """

    kwargs = _get_kwargs(
        highest_level_bound=highest_level_bound,
        highest_level_bound_contained_by=highest_level_bound_contained_by,
        highest_level_bound_contains=highest_level_bound_contains,
        highest_level_bound_endswith=highest_level_bound_endswith,
        highest_level_bound_gt=highest_level_bound_gt,
        highest_level_bound_gte=highest_level_bound_gte,
        highest_level_bound_icontains=highest_level_bound_icontains,
        highest_level_bound_iendswith=highest_level_bound_iendswith,
        highest_level_bound_iexact=highest_level_bound_iexact,
        highest_level_bound_in=highest_level_bound_in,
        highest_level_bound_iregex=highest_level_bound_iregex,
        highest_level_bound_isnull=highest_level_bound_isnull,
        highest_level_bound_istartswith=highest_level_bound_istartswith,
        highest_level_bound_lt=highest_level_bound_lt,
        highest_level_bound_lte=highest_level_bound_lte,
        highest_level_bound_range=highest_level_bound_range,
        highest_level_bound_regex=highest_level_bound_regex,
        highest_level_bound_startswith=highest_level_bound_startswith,
        limit=limit,
        lowest_level_bound=lowest_level_bound,
        lowest_level_bound_contained_by=lowest_level_bound_contained_by,
        lowest_level_bound_contains=lowest_level_bound_contains,
        lowest_level_bound_endswith=lowest_level_bound_endswith,
        lowest_level_bound_gt=lowest_level_bound_gt,
        lowest_level_bound_gte=lowest_level_bound_gte,
        lowest_level_bound_icontains=lowest_level_bound_icontains,
        lowest_level_bound_iendswith=lowest_level_bound_iendswith,
        lowest_level_bound_iexact=lowest_level_bound_iexact,
        lowest_level_bound_in=lowest_level_bound_in,
        lowest_level_bound_iregex=lowest_level_bound_iregex,
        lowest_level_bound_isnull=lowest_level_bound_isnull,
        lowest_level_bound_istartswith=lowest_level_bound_istartswith,
        lowest_level_bound_lt=lowest_level_bound_lt,
        lowest_level_bound_lte=lowest_level_bound_lte,
        lowest_level_bound_range=lowest_level_bound_range,
        lowest_level_bound_regex=lowest_level_bound_regex,
        lowest_level_bound_startswith=lowest_level_bound_startswith,
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
        units=units,
        units_contains=units_contains,
        units_endswith=units_endswith,
        units_gt=units_gt,
        units_gte=units_gte,
        units_icontains=units_icontains,
        units_iendswith=units_iendswith,
        units_iexact=units_iexact,
        units_in=units_in,
        units_iregex=units_iregex,
        units_isnull=units_isnull,
        units_istartswith=units_istartswith,
        units_lt=units_lt,
        units_lte=units_lte,
        units_range=units_range,
        units_regex=units_regex,
        units_startswith=units_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    highest_level_bound: Union[Unset, float] = UNSET,
    highest_level_bound_contained_by: Union[Unset, float] = UNSET,
    highest_level_bound_contains: Union[Unset, float] = UNSET,
    highest_level_bound_endswith: Union[Unset, float] = UNSET,
    highest_level_bound_gt: Union[Unset, float] = UNSET,
    highest_level_bound_gte: Union[Unset, float] = UNSET,
    highest_level_bound_icontains: Union[Unset, float] = UNSET,
    highest_level_bound_iendswith: Union[Unset, float] = UNSET,
    highest_level_bound_iexact: Union[Unset, float] = UNSET,
    highest_level_bound_in: Union[Unset, list[float]] = UNSET,
    highest_level_bound_iregex: Union[Unset, float] = UNSET,
    highest_level_bound_isnull: Union[Unset, bool] = UNSET,
    highest_level_bound_istartswith: Union[Unset, float] = UNSET,
    highest_level_bound_lt: Union[Unset, float] = UNSET,
    highest_level_bound_lte: Union[Unset, float] = UNSET,
    highest_level_bound_range: Union[Unset, list[float]] = UNSET,
    highest_level_bound_regex: Union[Unset, float] = UNSET,
    highest_level_bound_startswith: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    lowest_level_bound: Union[Unset, float] = UNSET,
    lowest_level_bound_contained_by: Union[Unset, float] = UNSET,
    lowest_level_bound_contains: Union[Unset, float] = UNSET,
    lowest_level_bound_endswith: Union[Unset, float] = UNSET,
    lowest_level_bound_gt: Union[Unset, float] = UNSET,
    lowest_level_bound_gte: Union[Unset, float] = UNSET,
    lowest_level_bound_icontains: Union[Unset, float] = UNSET,
    lowest_level_bound_iendswith: Union[Unset, float] = UNSET,
    lowest_level_bound_iexact: Union[Unset, float] = UNSET,
    lowest_level_bound_in: Union[Unset, list[float]] = UNSET,
    lowest_level_bound_iregex: Union[Unset, float] = UNSET,
    lowest_level_bound_isnull: Union[Unset, bool] = UNSET,
    lowest_level_bound_istartswith: Union[Unset, float] = UNSET,
    lowest_level_bound_lt: Union[Unset, float] = UNSET,
    lowest_level_bound_lte: Union[Unset, float] = UNSET,
    lowest_level_bound_range: Union[Unset, list[float]] = UNSET,
    lowest_level_bound_regex: Union[Unset, float] = UNSET,
    lowest_level_bound_startswith: Union[Unset, float] = UNSET,
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
    units: Union[Unset, str] = UNSET,
    units_contains: Union[Unset, str] = UNSET,
    units_endswith: Union[Unset, str] = UNSET,
    units_gt: Union[Unset, str] = UNSET,
    units_gte: Union[Unset, str] = UNSET,
    units_icontains: Union[Unset, str] = UNSET,
    units_iendswith: Union[Unset, str] = UNSET,
    units_iexact: Union[Unset, str] = UNSET,
    units_in: Union[Unset, list[str]] = UNSET,
    units_iregex: Union[Unset, str] = UNSET,
    units_isnull: Union[Unset, bool] = UNSET,
    units_istartswith: Union[Unset, str] = UNSET,
    units_lt: Union[Unset, str] = UNSET,
    units_lte: Union[Unset, str] = UNSET,
    units_range: Union[Unset, list[str]] = UNSET,
    units_regex: Union[Unset, str] = UNSET,
    units_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedVerticalExtentReadList]:
    """Get a list of VerticalExtent objects.

    Args:
        highest_level_bound (Union[Unset, float]):
        highest_level_bound_contained_by (Union[Unset, float]):
        highest_level_bound_contains (Union[Unset, float]):
        highest_level_bound_endswith (Union[Unset, float]):
        highest_level_bound_gt (Union[Unset, float]):
        highest_level_bound_gte (Union[Unset, float]):
        highest_level_bound_icontains (Union[Unset, float]):
        highest_level_bound_iendswith (Union[Unset, float]):
        highest_level_bound_iexact (Union[Unset, float]):
        highest_level_bound_in (Union[Unset, list[float]]):
        highest_level_bound_iregex (Union[Unset, float]):
        highest_level_bound_isnull (Union[Unset, bool]):
        highest_level_bound_istartswith (Union[Unset, float]):
        highest_level_bound_lt (Union[Unset, float]):
        highest_level_bound_lte (Union[Unset, float]):
        highest_level_bound_range (Union[Unset, list[float]]):
        highest_level_bound_regex (Union[Unset, float]):
        highest_level_bound_startswith (Union[Unset, float]):
        limit (Union[Unset, int]):
        lowest_level_bound (Union[Unset, float]):
        lowest_level_bound_contained_by (Union[Unset, float]):
        lowest_level_bound_contains (Union[Unset, float]):
        lowest_level_bound_endswith (Union[Unset, float]):
        lowest_level_bound_gt (Union[Unset, float]):
        lowest_level_bound_gte (Union[Unset, float]):
        lowest_level_bound_icontains (Union[Unset, float]):
        lowest_level_bound_iendswith (Union[Unset, float]):
        lowest_level_bound_iexact (Union[Unset, float]):
        lowest_level_bound_in (Union[Unset, list[float]]):
        lowest_level_bound_iregex (Union[Unset, float]):
        lowest_level_bound_isnull (Union[Unset, bool]):
        lowest_level_bound_istartswith (Union[Unset, float]):
        lowest_level_bound_lt (Union[Unset, float]):
        lowest_level_bound_lte (Union[Unset, float]):
        lowest_level_bound_range (Union[Unset, list[float]]):
        lowest_level_bound_regex (Union[Unset, float]):
        lowest_level_bound_startswith (Union[Unset, float]):
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
        units (Union[Unset, str]):
        units_contains (Union[Unset, str]):
        units_endswith (Union[Unset, str]):
        units_gt (Union[Unset, str]):
        units_gte (Union[Unset, str]):
        units_icontains (Union[Unset, str]):
        units_iendswith (Union[Unset, str]):
        units_iexact (Union[Unset, str]):
        units_in (Union[Unset, list[str]]):
        units_iregex (Union[Unset, str]):
        units_isnull (Union[Unset, bool]):
        units_istartswith (Union[Unset, str]):
        units_lt (Union[Unset, str]):
        units_lte (Union[Unset, str]):
        units_range (Union[Unset, list[str]]):
        units_regex (Union[Unset, str]):
        units_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVerticalExtentReadList
    """

    return sync_detailed(
        client=client,
        highest_level_bound=highest_level_bound,
        highest_level_bound_contained_by=highest_level_bound_contained_by,
        highest_level_bound_contains=highest_level_bound_contains,
        highest_level_bound_endswith=highest_level_bound_endswith,
        highest_level_bound_gt=highest_level_bound_gt,
        highest_level_bound_gte=highest_level_bound_gte,
        highest_level_bound_icontains=highest_level_bound_icontains,
        highest_level_bound_iendswith=highest_level_bound_iendswith,
        highest_level_bound_iexact=highest_level_bound_iexact,
        highest_level_bound_in=highest_level_bound_in,
        highest_level_bound_iregex=highest_level_bound_iregex,
        highest_level_bound_isnull=highest_level_bound_isnull,
        highest_level_bound_istartswith=highest_level_bound_istartswith,
        highest_level_bound_lt=highest_level_bound_lt,
        highest_level_bound_lte=highest_level_bound_lte,
        highest_level_bound_range=highest_level_bound_range,
        highest_level_bound_regex=highest_level_bound_regex,
        highest_level_bound_startswith=highest_level_bound_startswith,
        limit=limit,
        lowest_level_bound=lowest_level_bound,
        lowest_level_bound_contained_by=lowest_level_bound_contained_by,
        lowest_level_bound_contains=lowest_level_bound_contains,
        lowest_level_bound_endswith=lowest_level_bound_endswith,
        lowest_level_bound_gt=lowest_level_bound_gt,
        lowest_level_bound_gte=lowest_level_bound_gte,
        lowest_level_bound_icontains=lowest_level_bound_icontains,
        lowest_level_bound_iendswith=lowest_level_bound_iendswith,
        lowest_level_bound_iexact=lowest_level_bound_iexact,
        lowest_level_bound_in=lowest_level_bound_in,
        lowest_level_bound_iregex=lowest_level_bound_iregex,
        lowest_level_bound_isnull=lowest_level_bound_isnull,
        lowest_level_bound_istartswith=lowest_level_bound_istartswith,
        lowest_level_bound_lt=lowest_level_bound_lt,
        lowest_level_bound_lte=lowest_level_bound_lte,
        lowest_level_bound_range=lowest_level_bound_range,
        lowest_level_bound_regex=lowest_level_bound_regex,
        lowest_level_bound_startswith=lowest_level_bound_startswith,
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
        units=units,
        units_contains=units_contains,
        units_endswith=units_endswith,
        units_gt=units_gt,
        units_gte=units_gte,
        units_icontains=units_icontains,
        units_iendswith=units_iendswith,
        units_iexact=units_iexact,
        units_in=units_in,
        units_iregex=units_iregex,
        units_isnull=units_isnull,
        units_istartswith=units_istartswith,
        units_lt=units_lt,
        units_lte=units_lte,
        units_range=units_range,
        units_regex=units_regex,
        units_startswith=units_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    highest_level_bound: Union[Unset, float] = UNSET,
    highest_level_bound_contained_by: Union[Unset, float] = UNSET,
    highest_level_bound_contains: Union[Unset, float] = UNSET,
    highest_level_bound_endswith: Union[Unset, float] = UNSET,
    highest_level_bound_gt: Union[Unset, float] = UNSET,
    highest_level_bound_gte: Union[Unset, float] = UNSET,
    highest_level_bound_icontains: Union[Unset, float] = UNSET,
    highest_level_bound_iendswith: Union[Unset, float] = UNSET,
    highest_level_bound_iexact: Union[Unset, float] = UNSET,
    highest_level_bound_in: Union[Unset, list[float]] = UNSET,
    highest_level_bound_iregex: Union[Unset, float] = UNSET,
    highest_level_bound_isnull: Union[Unset, bool] = UNSET,
    highest_level_bound_istartswith: Union[Unset, float] = UNSET,
    highest_level_bound_lt: Union[Unset, float] = UNSET,
    highest_level_bound_lte: Union[Unset, float] = UNSET,
    highest_level_bound_range: Union[Unset, list[float]] = UNSET,
    highest_level_bound_regex: Union[Unset, float] = UNSET,
    highest_level_bound_startswith: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    lowest_level_bound: Union[Unset, float] = UNSET,
    lowest_level_bound_contained_by: Union[Unset, float] = UNSET,
    lowest_level_bound_contains: Union[Unset, float] = UNSET,
    lowest_level_bound_endswith: Union[Unset, float] = UNSET,
    lowest_level_bound_gt: Union[Unset, float] = UNSET,
    lowest_level_bound_gte: Union[Unset, float] = UNSET,
    lowest_level_bound_icontains: Union[Unset, float] = UNSET,
    lowest_level_bound_iendswith: Union[Unset, float] = UNSET,
    lowest_level_bound_iexact: Union[Unset, float] = UNSET,
    lowest_level_bound_in: Union[Unset, list[float]] = UNSET,
    lowest_level_bound_iregex: Union[Unset, float] = UNSET,
    lowest_level_bound_isnull: Union[Unset, bool] = UNSET,
    lowest_level_bound_istartswith: Union[Unset, float] = UNSET,
    lowest_level_bound_lt: Union[Unset, float] = UNSET,
    lowest_level_bound_lte: Union[Unset, float] = UNSET,
    lowest_level_bound_range: Union[Unset, list[float]] = UNSET,
    lowest_level_bound_regex: Union[Unset, float] = UNSET,
    lowest_level_bound_startswith: Union[Unset, float] = UNSET,
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
    units: Union[Unset, str] = UNSET,
    units_contains: Union[Unset, str] = UNSET,
    units_endswith: Union[Unset, str] = UNSET,
    units_gt: Union[Unset, str] = UNSET,
    units_gte: Union[Unset, str] = UNSET,
    units_icontains: Union[Unset, str] = UNSET,
    units_iendswith: Union[Unset, str] = UNSET,
    units_iexact: Union[Unset, str] = UNSET,
    units_in: Union[Unset, list[str]] = UNSET,
    units_iregex: Union[Unset, str] = UNSET,
    units_isnull: Union[Unset, bool] = UNSET,
    units_istartswith: Union[Unset, str] = UNSET,
    units_lt: Union[Unset, str] = UNSET,
    units_lte: Union[Unset, str] = UNSET,
    units_range: Union[Unset, list[str]] = UNSET,
    units_regex: Union[Unset, str] = UNSET,
    units_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedVerticalExtentReadList]:
    """Get a list of VerticalExtent objects.

    Args:
        highest_level_bound (Union[Unset, float]):
        highest_level_bound_contained_by (Union[Unset, float]):
        highest_level_bound_contains (Union[Unset, float]):
        highest_level_bound_endswith (Union[Unset, float]):
        highest_level_bound_gt (Union[Unset, float]):
        highest_level_bound_gte (Union[Unset, float]):
        highest_level_bound_icontains (Union[Unset, float]):
        highest_level_bound_iendswith (Union[Unset, float]):
        highest_level_bound_iexact (Union[Unset, float]):
        highest_level_bound_in (Union[Unset, list[float]]):
        highest_level_bound_iregex (Union[Unset, float]):
        highest_level_bound_isnull (Union[Unset, bool]):
        highest_level_bound_istartswith (Union[Unset, float]):
        highest_level_bound_lt (Union[Unset, float]):
        highest_level_bound_lte (Union[Unset, float]):
        highest_level_bound_range (Union[Unset, list[float]]):
        highest_level_bound_regex (Union[Unset, float]):
        highest_level_bound_startswith (Union[Unset, float]):
        limit (Union[Unset, int]):
        lowest_level_bound (Union[Unset, float]):
        lowest_level_bound_contained_by (Union[Unset, float]):
        lowest_level_bound_contains (Union[Unset, float]):
        lowest_level_bound_endswith (Union[Unset, float]):
        lowest_level_bound_gt (Union[Unset, float]):
        lowest_level_bound_gte (Union[Unset, float]):
        lowest_level_bound_icontains (Union[Unset, float]):
        lowest_level_bound_iendswith (Union[Unset, float]):
        lowest_level_bound_iexact (Union[Unset, float]):
        lowest_level_bound_in (Union[Unset, list[float]]):
        lowest_level_bound_iregex (Union[Unset, float]):
        lowest_level_bound_isnull (Union[Unset, bool]):
        lowest_level_bound_istartswith (Union[Unset, float]):
        lowest_level_bound_lt (Union[Unset, float]):
        lowest_level_bound_lte (Union[Unset, float]):
        lowest_level_bound_range (Union[Unset, list[float]]):
        lowest_level_bound_regex (Union[Unset, float]):
        lowest_level_bound_startswith (Union[Unset, float]):
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
        units (Union[Unset, str]):
        units_contains (Union[Unset, str]):
        units_endswith (Union[Unset, str]):
        units_gt (Union[Unset, str]):
        units_gte (Union[Unset, str]):
        units_icontains (Union[Unset, str]):
        units_iendswith (Union[Unset, str]):
        units_iexact (Union[Unset, str]):
        units_in (Union[Unset, list[str]]):
        units_iregex (Union[Unset, str]):
        units_isnull (Union[Unset, bool]):
        units_istartswith (Union[Unset, str]):
        units_lt (Union[Unset, str]):
        units_lte (Union[Unset, str]):
        units_range (Union[Unset, list[str]]):
        units_regex (Union[Unset, str]):
        units_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVerticalExtentReadList]
    """

    kwargs = _get_kwargs(
        highest_level_bound=highest_level_bound,
        highest_level_bound_contained_by=highest_level_bound_contained_by,
        highest_level_bound_contains=highest_level_bound_contains,
        highest_level_bound_endswith=highest_level_bound_endswith,
        highest_level_bound_gt=highest_level_bound_gt,
        highest_level_bound_gte=highest_level_bound_gte,
        highest_level_bound_icontains=highest_level_bound_icontains,
        highest_level_bound_iendswith=highest_level_bound_iendswith,
        highest_level_bound_iexact=highest_level_bound_iexact,
        highest_level_bound_in=highest_level_bound_in,
        highest_level_bound_iregex=highest_level_bound_iregex,
        highest_level_bound_isnull=highest_level_bound_isnull,
        highest_level_bound_istartswith=highest_level_bound_istartswith,
        highest_level_bound_lt=highest_level_bound_lt,
        highest_level_bound_lte=highest_level_bound_lte,
        highest_level_bound_range=highest_level_bound_range,
        highest_level_bound_regex=highest_level_bound_regex,
        highest_level_bound_startswith=highest_level_bound_startswith,
        limit=limit,
        lowest_level_bound=lowest_level_bound,
        lowest_level_bound_contained_by=lowest_level_bound_contained_by,
        lowest_level_bound_contains=lowest_level_bound_contains,
        lowest_level_bound_endswith=lowest_level_bound_endswith,
        lowest_level_bound_gt=lowest_level_bound_gt,
        lowest_level_bound_gte=lowest_level_bound_gte,
        lowest_level_bound_icontains=lowest_level_bound_icontains,
        lowest_level_bound_iendswith=lowest_level_bound_iendswith,
        lowest_level_bound_iexact=lowest_level_bound_iexact,
        lowest_level_bound_in=lowest_level_bound_in,
        lowest_level_bound_iregex=lowest_level_bound_iregex,
        lowest_level_bound_isnull=lowest_level_bound_isnull,
        lowest_level_bound_istartswith=lowest_level_bound_istartswith,
        lowest_level_bound_lt=lowest_level_bound_lt,
        lowest_level_bound_lte=lowest_level_bound_lte,
        lowest_level_bound_range=lowest_level_bound_range,
        lowest_level_bound_regex=lowest_level_bound_regex,
        lowest_level_bound_startswith=lowest_level_bound_startswith,
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
        units=units,
        units_contains=units_contains,
        units_endswith=units_endswith,
        units_gt=units_gt,
        units_gte=units_gte,
        units_icontains=units_icontains,
        units_iendswith=units_iendswith,
        units_iexact=units_iexact,
        units_in=units_in,
        units_iregex=units_iregex,
        units_isnull=units_isnull,
        units_istartswith=units_istartswith,
        units_lt=units_lt,
        units_lte=units_lte,
        units_range=units_range,
        units_regex=units_regex,
        units_startswith=units_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    highest_level_bound: Union[Unset, float] = UNSET,
    highest_level_bound_contained_by: Union[Unset, float] = UNSET,
    highest_level_bound_contains: Union[Unset, float] = UNSET,
    highest_level_bound_endswith: Union[Unset, float] = UNSET,
    highest_level_bound_gt: Union[Unset, float] = UNSET,
    highest_level_bound_gte: Union[Unset, float] = UNSET,
    highest_level_bound_icontains: Union[Unset, float] = UNSET,
    highest_level_bound_iendswith: Union[Unset, float] = UNSET,
    highest_level_bound_iexact: Union[Unset, float] = UNSET,
    highest_level_bound_in: Union[Unset, list[float]] = UNSET,
    highest_level_bound_iregex: Union[Unset, float] = UNSET,
    highest_level_bound_isnull: Union[Unset, bool] = UNSET,
    highest_level_bound_istartswith: Union[Unset, float] = UNSET,
    highest_level_bound_lt: Union[Unset, float] = UNSET,
    highest_level_bound_lte: Union[Unset, float] = UNSET,
    highest_level_bound_range: Union[Unset, list[float]] = UNSET,
    highest_level_bound_regex: Union[Unset, float] = UNSET,
    highest_level_bound_startswith: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    lowest_level_bound: Union[Unset, float] = UNSET,
    lowest_level_bound_contained_by: Union[Unset, float] = UNSET,
    lowest_level_bound_contains: Union[Unset, float] = UNSET,
    lowest_level_bound_endswith: Union[Unset, float] = UNSET,
    lowest_level_bound_gt: Union[Unset, float] = UNSET,
    lowest_level_bound_gte: Union[Unset, float] = UNSET,
    lowest_level_bound_icontains: Union[Unset, float] = UNSET,
    lowest_level_bound_iendswith: Union[Unset, float] = UNSET,
    lowest_level_bound_iexact: Union[Unset, float] = UNSET,
    lowest_level_bound_in: Union[Unset, list[float]] = UNSET,
    lowest_level_bound_iregex: Union[Unset, float] = UNSET,
    lowest_level_bound_isnull: Union[Unset, bool] = UNSET,
    lowest_level_bound_istartswith: Union[Unset, float] = UNSET,
    lowest_level_bound_lt: Union[Unset, float] = UNSET,
    lowest_level_bound_lte: Union[Unset, float] = UNSET,
    lowest_level_bound_range: Union[Unset, list[float]] = UNSET,
    lowest_level_bound_regex: Union[Unset, float] = UNSET,
    lowest_level_bound_startswith: Union[Unset, float] = UNSET,
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
    units: Union[Unset, str] = UNSET,
    units_contains: Union[Unset, str] = UNSET,
    units_endswith: Union[Unset, str] = UNSET,
    units_gt: Union[Unset, str] = UNSET,
    units_gte: Union[Unset, str] = UNSET,
    units_icontains: Union[Unset, str] = UNSET,
    units_iendswith: Union[Unset, str] = UNSET,
    units_iexact: Union[Unset, str] = UNSET,
    units_in: Union[Unset, list[str]] = UNSET,
    units_iregex: Union[Unset, str] = UNSET,
    units_isnull: Union[Unset, bool] = UNSET,
    units_istartswith: Union[Unset, str] = UNSET,
    units_lt: Union[Unset, str] = UNSET,
    units_lte: Union[Unset, str] = UNSET,
    units_range: Union[Unset, list[str]] = UNSET,
    units_regex: Union[Unset, str] = UNSET,
    units_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedVerticalExtentReadList]:
    """Get a list of VerticalExtent objects.

    Args:
        highest_level_bound (Union[Unset, float]):
        highest_level_bound_contained_by (Union[Unset, float]):
        highest_level_bound_contains (Union[Unset, float]):
        highest_level_bound_endswith (Union[Unset, float]):
        highest_level_bound_gt (Union[Unset, float]):
        highest_level_bound_gte (Union[Unset, float]):
        highest_level_bound_icontains (Union[Unset, float]):
        highest_level_bound_iendswith (Union[Unset, float]):
        highest_level_bound_iexact (Union[Unset, float]):
        highest_level_bound_in (Union[Unset, list[float]]):
        highest_level_bound_iregex (Union[Unset, float]):
        highest_level_bound_isnull (Union[Unset, bool]):
        highest_level_bound_istartswith (Union[Unset, float]):
        highest_level_bound_lt (Union[Unset, float]):
        highest_level_bound_lte (Union[Unset, float]):
        highest_level_bound_range (Union[Unset, list[float]]):
        highest_level_bound_regex (Union[Unset, float]):
        highest_level_bound_startswith (Union[Unset, float]):
        limit (Union[Unset, int]):
        lowest_level_bound (Union[Unset, float]):
        lowest_level_bound_contained_by (Union[Unset, float]):
        lowest_level_bound_contains (Union[Unset, float]):
        lowest_level_bound_endswith (Union[Unset, float]):
        lowest_level_bound_gt (Union[Unset, float]):
        lowest_level_bound_gte (Union[Unset, float]):
        lowest_level_bound_icontains (Union[Unset, float]):
        lowest_level_bound_iendswith (Union[Unset, float]):
        lowest_level_bound_iexact (Union[Unset, float]):
        lowest_level_bound_in (Union[Unset, list[float]]):
        lowest_level_bound_iregex (Union[Unset, float]):
        lowest_level_bound_isnull (Union[Unset, bool]):
        lowest_level_bound_istartswith (Union[Unset, float]):
        lowest_level_bound_lt (Union[Unset, float]):
        lowest_level_bound_lte (Union[Unset, float]):
        lowest_level_bound_range (Union[Unset, list[float]]):
        lowest_level_bound_regex (Union[Unset, float]):
        lowest_level_bound_startswith (Union[Unset, float]):
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
        units (Union[Unset, str]):
        units_contains (Union[Unset, str]):
        units_endswith (Union[Unset, str]):
        units_gt (Union[Unset, str]):
        units_gte (Union[Unset, str]):
        units_icontains (Union[Unset, str]):
        units_iendswith (Union[Unset, str]):
        units_iexact (Union[Unset, str]):
        units_in (Union[Unset, list[str]]):
        units_iregex (Union[Unset, str]):
        units_isnull (Union[Unset, bool]):
        units_istartswith (Union[Unset, str]):
        units_lt (Union[Unset, str]):
        units_lte (Union[Unset, str]):
        units_range (Union[Unset, list[str]]):
        units_regex (Union[Unset, str]):
        units_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVerticalExtentReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            highest_level_bound=highest_level_bound,
            highest_level_bound_contained_by=highest_level_bound_contained_by,
            highest_level_bound_contains=highest_level_bound_contains,
            highest_level_bound_endswith=highest_level_bound_endswith,
            highest_level_bound_gt=highest_level_bound_gt,
            highest_level_bound_gte=highest_level_bound_gte,
            highest_level_bound_icontains=highest_level_bound_icontains,
            highest_level_bound_iendswith=highest_level_bound_iendswith,
            highest_level_bound_iexact=highest_level_bound_iexact,
            highest_level_bound_in=highest_level_bound_in,
            highest_level_bound_iregex=highest_level_bound_iregex,
            highest_level_bound_isnull=highest_level_bound_isnull,
            highest_level_bound_istartswith=highest_level_bound_istartswith,
            highest_level_bound_lt=highest_level_bound_lt,
            highest_level_bound_lte=highest_level_bound_lte,
            highest_level_bound_range=highest_level_bound_range,
            highest_level_bound_regex=highest_level_bound_regex,
            highest_level_bound_startswith=highest_level_bound_startswith,
            limit=limit,
            lowest_level_bound=lowest_level_bound,
            lowest_level_bound_contained_by=lowest_level_bound_contained_by,
            lowest_level_bound_contains=lowest_level_bound_contains,
            lowest_level_bound_endswith=lowest_level_bound_endswith,
            lowest_level_bound_gt=lowest_level_bound_gt,
            lowest_level_bound_gte=lowest_level_bound_gte,
            lowest_level_bound_icontains=lowest_level_bound_icontains,
            lowest_level_bound_iendswith=lowest_level_bound_iendswith,
            lowest_level_bound_iexact=lowest_level_bound_iexact,
            lowest_level_bound_in=lowest_level_bound_in,
            lowest_level_bound_iregex=lowest_level_bound_iregex,
            lowest_level_bound_isnull=lowest_level_bound_isnull,
            lowest_level_bound_istartswith=lowest_level_bound_istartswith,
            lowest_level_bound_lt=lowest_level_bound_lt,
            lowest_level_bound_lte=lowest_level_bound_lte,
            lowest_level_bound_range=lowest_level_bound_range,
            lowest_level_bound_regex=lowest_level_bound_regex,
            lowest_level_bound_startswith=lowest_level_bound_startswith,
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
            units=units,
            units_contains=units_contains,
            units_endswith=units_endswith,
            units_gt=units_gt,
            units_gte=units_gte,
            units_icontains=units_icontains,
            units_iendswith=units_iendswith,
            units_iexact=units_iexact,
            units_in=units_in,
            units_iregex=units_iregex,
            units_isnull=units_isnull,
            units_istartswith=units_istartswith,
            units_lt=units_lt,
            units_lte=units_lte,
            units_range=units_range,
            units_regex=units_regex,
            units_startswith=units_startswith,
        )
    ).parsed
