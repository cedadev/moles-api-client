import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_migration_property_read_list import PaginatedMigrationPropertyReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: Union[Unset, int] = UNSET,
    id_contained_by: Union[Unset, int] = UNSET,
    id_contains: Union[Unset, int] = UNSET,
    id_endswith: Union[Unset, int] = UNSET,
    id_gt: Union[Unset, int] = UNSET,
    id_gte: Union[Unset, int] = UNSET,
    id_icontains: Union[Unset, int] = UNSET,
    id_iendswith: Union[Unset, int] = UNSET,
    id_iexact: Union[Unset, int] = UNSET,
    id_in: Union[Unset, list[int]] = UNSET,
    id_iregex: Union[Unset, int] = UNSET,
    id_isnull: Union[Unset, bool] = UNSET,
    id_istartswith: Union[Unset, int] = UNSET,
    id_lt: Union[Unset, int] = UNSET,
    id_lte: Union[Unset, int] = UNSET,
    id_range: Union[Unset, list[int]] = UNSET,
    id_regex: Union[Unset, int] = UNSET,
    id_startswith: Union[Unset, int] = UNSET,
    key: Union[Unset, str] = UNSET,
    key_contains: Union[Unset, str] = UNSET,
    key_endswith: Union[Unset, str] = UNSET,
    key_gt: Union[Unset, str] = UNSET,
    key_gte: Union[Unset, str] = UNSET,
    key_icontains: Union[Unset, str] = UNSET,
    key_iendswith: Union[Unset, str] = UNSET,
    key_iexact: Union[Unset, str] = UNSET,
    key_in: Union[Unset, list[str]] = UNSET,
    key_iregex: Union[Unset, str] = UNSET,
    key_isnull: Union[Unset, bool] = UNSET,
    key_istartswith: Union[Unset, str] = UNSET,
    key_lt: Union[Unset, str] = UNSET,
    key_lte: Union[Unset, str] = UNSET,
    key_range: Union[Unset, list[str]] = UNSET,
    key_regex: Union[Unset, str] = UNSET,
    key_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified: Union[Unset, datetime.date] = UNSET,
    modified_contained_by: Union[Unset, datetime.date] = UNSET,
    modified_contains: Union[Unset, datetime.date] = UNSET,
    modified_day: Union[Unset, float] = UNSET,
    modified_endswith: Union[Unset, datetime.date] = UNSET,
    modified_gt: Union[Unset, datetime.date] = UNSET,
    modified_gte: Union[Unset, datetime.date] = UNSET,
    modified_icontains: Union[Unset, datetime.date] = UNSET,
    modified_iendswith: Union[Unset, datetime.date] = UNSET,
    modified_iexact: Union[Unset, datetime.date] = UNSET,
    modified_in: Union[Unset, list[datetime.date]] = UNSET,
    modified_iregex: Union[Unset, datetime.date] = UNSET,
    modified_isnull: Union[Unset, bool] = UNSET,
    modified_iso_week_day: Union[Unset, float] = UNSET,
    modified_iso_year: Union[Unset, float] = UNSET,
    modified_istartswith: Union[Unset, datetime.date] = UNSET,
    modified_lt: Union[Unset, datetime.date] = UNSET,
    modified_lte: Union[Unset, datetime.date] = UNSET,
    modified_month: Union[Unset, float] = UNSET,
    modified_quarter: Union[Unset, float] = UNSET,
    modified_range: Union[Unset, list[datetime.date]] = UNSET,
    modified_regex: Union[Unset, datetime.date] = UNSET,
    modified_startswith: Union[Unset, datetime.date] = UNSET,
    modified_week: Union[Unset, float] = UNSET,
    modified_week_day: Union[Unset, float] = UNSET,
    modified_year: Union[Unset, float] = UNSET,
    ob_ref: Union[Unset, int] = UNSET,
    ob_ref_gt: Union[Unset, int] = UNSET,
    ob_ref_gte: Union[Unset, int] = UNSET,
    ob_ref_in: Union[Unset, list[int]] = UNSET,
    ob_ref_isnull: Union[Unset, bool] = UNSET,
    ob_ref_lt: Union[Unset, int] = UNSET,
    ob_ref_lte: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
    value_contains: Union[Unset, str] = UNSET,
    value_endswith: Union[Unset, str] = UNSET,
    value_gt: Union[Unset, str] = UNSET,
    value_gte: Union[Unset, str] = UNSET,
    value_icontains: Union[Unset, str] = UNSET,
    value_iendswith: Union[Unset, str] = UNSET,
    value_iexact: Union[Unset, str] = UNSET,
    value_in: Union[Unset, list[str]] = UNSET,
    value_iregex: Union[Unset, str] = UNSET,
    value_isnull: Union[Unset, bool] = UNSET,
    value_istartswith: Union[Unset, str] = UNSET,
    value_lt: Union[Unset, str] = UNSET,
    value_lte: Union[Unset, str] = UNSET,
    value_range: Union[Unset, list[str]] = UNSET,
    value_regex: Union[Unset, str] = UNSET,
    value_startswith: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["id"] = id

    params["id__contained_by"] = id_contained_by

    params["id__contains"] = id_contains

    params["id__endswith"] = id_endswith

    params["id__gt"] = id_gt

    params["id__gte"] = id_gte

    params["id__icontains"] = id_icontains

    params["id__iendswith"] = id_iendswith

    params["id__iexact"] = id_iexact

    json_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(id_in, Unset):
        json_id_in = ",".join(id_in)

    params["id__in"] = json_id_in

    params["id__iregex"] = id_iregex

    params["id__isnull"] = id_isnull

    params["id__istartswith"] = id_istartswith

    params["id__lt"] = id_lt

    params["id__lte"] = id_lte

    json_id_range: Union[Unset, list[int]] = UNSET
    if not isinstance(id_range, Unset):
        json_id_range = ",".join(id_range)

    params["id__range"] = json_id_range

    params["id__regex"] = id_regex

    params["id__startswith"] = id_startswith

    params["key"] = key

    params["key__contains"] = key_contains

    params["key__endswith"] = key_endswith

    params["key__gt"] = key_gt

    params["key__gte"] = key_gte

    params["key__icontains"] = key_icontains

    params["key__iendswith"] = key_iendswith

    params["key__iexact"] = key_iexact

    json_key_in: Union[Unset, list[str]] = UNSET
    if not isinstance(key_in, Unset):
        json_key_in = ",".join(key_in)

    params["key__in"] = json_key_in

    params["key__iregex"] = key_iregex

    params["key__isnull"] = key_isnull

    params["key__istartswith"] = key_istartswith

    params["key__lt"] = key_lt

    params["key__lte"] = key_lte

    json_key_range: Union[Unset, list[str]] = UNSET
    if not isinstance(key_range, Unset):
        json_key_range = ",".join(key_range)

    params["key__range"] = json_key_range

    params["key__regex"] = key_regex

    params["key__startswith"] = key_startswith

    params["limit"] = limit

    json_modified: Union[Unset, str] = UNSET
    if not isinstance(modified, Unset):
        json_modified = modified.isoformat()
    params["modified"] = json_modified

    json_modified_contained_by: Union[Unset, str] = UNSET
    if not isinstance(modified_contained_by, Unset):
        json_modified_contained_by = modified_contained_by.isoformat()
    params["modified__contained_by"] = json_modified_contained_by

    json_modified_contains: Union[Unset, str] = UNSET
    if not isinstance(modified_contains, Unset):
        json_modified_contains = modified_contains.isoformat()
    params["modified__contains"] = json_modified_contains

    params["modified__day"] = modified_day

    json_modified_endswith: Union[Unset, str] = UNSET
    if not isinstance(modified_endswith, Unset):
        json_modified_endswith = modified_endswith.isoformat()
    params["modified__endswith"] = json_modified_endswith

    json_modified_gt: Union[Unset, str] = UNSET
    if not isinstance(modified_gt, Unset):
        json_modified_gt = modified_gt.isoformat()
    params["modified__gt"] = json_modified_gt

    json_modified_gte: Union[Unset, str] = UNSET
    if not isinstance(modified_gte, Unset):
        json_modified_gte = modified_gte.isoformat()
    params["modified__gte"] = json_modified_gte

    json_modified_icontains: Union[Unset, str] = UNSET
    if not isinstance(modified_icontains, Unset):
        json_modified_icontains = modified_icontains.isoformat()
    params["modified__icontains"] = json_modified_icontains

    json_modified_iendswith: Union[Unset, str] = UNSET
    if not isinstance(modified_iendswith, Unset):
        json_modified_iendswith = modified_iendswith.isoformat()
    params["modified__iendswith"] = json_modified_iendswith

    json_modified_iexact: Union[Unset, str] = UNSET
    if not isinstance(modified_iexact, Unset):
        json_modified_iexact = modified_iexact.isoformat()
    params["modified__iexact"] = json_modified_iexact

    json_modified_in: Union[Unset, list[str]] = UNSET
    if not isinstance(modified_in, Unset):
        json_modified_in = []
        for modified_in_item_data in modified_in:
            modified_in_item = modified_in_item_data.isoformat()
            json_modified_in.append(modified_in_item)

    params["modified__in"] = json_modified_in

    json_modified_iregex: Union[Unset, str] = UNSET
    if not isinstance(modified_iregex, Unset):
        json_modified_iregex = modified_iregex.isoformat()
    params["modified__iregex"] = json_modified_iregex

    params["modified__isnull"] = modified_isnull

    params["modified__iso_week_day"] = modified_iso_week_day

    params["modified__iso_year"] = modified_iso_year

    json_modified_istartswith: Union[Unset, str] = UNSET
    if not isinstance(modified_istartswith, Unset):
        json_modified_istartswith = modified_istartswith.isoformat()
    params["modified__istartswith"] = json_modified_istartswith

    json_modified_lt: Union[Unset, str] = UNSET
    if not isinstance(modified_lt, Unset):
        json_modified_lt = modified_lt.isoformat()
    params["modified__lt"] = json_modified_lt

    json_modified_lte: Union[Unset, str] = UNSET
    if not isinstance(modified_lte, Unset):
        json_modified_lte = modified_lte.isoformat()
    params["modified__lte"] = json_modified_lte

    params["modified__month"] = modified_month

    params["modified__quarter"] = modified_quarter

    json_modified_range: Union[Unset, list[str]] = UNSET
    if not isinstance(modified_range, Unset):
        json_modified_range = []
        for modified_range_item_data in modified_range:
            modified_range_item = modified_range_item_data.isoformat()
            json_modified_range.append(modified_range_item)

    params["modified__range"] = json_modified_range

    json_modified_regex: Union[Unset, str] = UNSET
    if not isinstance(modified_regex, Unset):
        json_modified_regex = modified_regex.isoformat()
    params["modified__regex"] = json_modified_regex

    json_modified_startswith: Union[Unset, str] = UNSET
    if not isinstance(modified_startswith, Unset):
        json_modified_startswith = modified_startswith.isoformat()
    params["modified__startswith"] = json_modified_startswith

    params["modified__week"] = modified_week

    params["modified__week_day"] = modified_week_day

    params["modified__year"] = modified_year

    params["ob_ref"] = ob_ref

    params["ob_ref__gt"] = ob_ref_gt

    params["ob_ref__gte"] = ob_ref_gte

    json_ob_ref_in: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_ref_in, Unset):
        json_ob_ref_in = ",".join(ob_ref_in)

    params["ob_ref__in"] = json_ob_ref_in

    params["ob_ref__isnull"] = ob_ref_isnull

    params["ob_ref__lt"] = ob_ref_lt

    params["ob_ref__lte"] = ob_ref_lte

    params["offset"] = offset

    params["ordering"] = ordering

    params["value"] = value

    params["value__contains"] = value_contains

    params["value__endswith"] = value_endswith

    params["value__gt"] = value_gt

    params["value__gte"] = value_gte

    params["value__icontains"] = value_icontains

    params["value__iendswith"] = value_iendswith

    params["value__iexact"] = value_iexact

    json_value_in: Union[Unset, list[str]] = UNSET
    if not isinstance(value_in, Unset):
        json_value_in = ",".join(value_in)

    params["value__in"] = json_value_in

    params["value__iregex"] = value_iregex

    params["value__isnull"] = value_isnull

    params["value__istartswith"] = value_istartswith

    params["value__lt"] = value_lt

    params["value__lte"] = value_lte

    json_value_range: Union[Unset, list[str]] = UNSET
    if not isinstance(value_range, Unset):
        json_value_range = ",".join(value_range)

    params["value__range"] = json_value_range

    params["value__regex"] = value_regex

    params["value__startswith"] = value_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/migrationproperties/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedMigrationPropertyReadList]:
    if response.status_code == 200:
        response_200 = PaginatedMigrationPropertyReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedMigrationPropertyReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, int] = UNSET,
    id_contained_by: Union[Unset, int] = UNSET,
    id_contains: Union[Unset, int] = UNSET,
    id_endswith: Union[Unset, int] = UNSET,
    id_gt: Union[Unset, int] = UNSET,
    id_gte: Union[Unset, int] = UNSET,
    id_icontains: Union[Unset, int] = UNSET,
    id_iendswith: Union[Unset, int] = UNSET,
    id_iexact: Union[Unset, int] = UNSET,
    id_in: Union[Unset, list[int]] = UNSET,
    id_iregex: Union[Unset, int] = UNSET,
    id_isnull: Union[Unset, bool] = UNSET,
    id_istartswith: Union[Unset, int] = UNSET,
    id_lt: Union[Unset, int] = UNSET,
    id_lte: Union[Unset, int] = UNSET,
    id_range: Union[Unset, list[int]] = UNSET,
    id_regex: Union[Unset, int] = UNSET,
    id_startswith: Union[Unset, int] = UNSET,
    key: Union[Unset, str] = UNSET,
    key_contains: Union[Unset, str] = UNSET,
    key_endswith: Union[Unset, str] = UNSET,
    key_gt: Union[Unset, str] = UNSET,
    key_gte: Union[Unset, str] = UNSET,
    key_icontains: Union[Unset, str] = UNSET,
    key_iendswith: Union[Unset, str] = UNSET,
    key_iexact: Union[Unset, str] = UNSET,
    key_in: Union[Unset, list[str]] = UNSET,
    key_iregex: Union[Unset, str] = UNSET,
    key_isnull: Union[Unset, bool] = UNSET,
    key_istartswith: Union[Unset, str] = UNSET,
    key_lt: Union[Unset, str] = UNSET,
    key_lte: Union[Unset, str] = UNSET,
    key_range: Union[Unset, list[str]] = UNSET,
    key_regex: Union[Unset, str] = UNSET,
    key_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified: Union[Unset, datetime.date] = UNSET,
    modified_contained_by: Union[Unset, datetime.date] = UNSET,
    modified_contains: Union[Unset, datetime.date] = UNSET,
    modified_day: Union[Unset, float] = UNSET,
    modified_endswith: Union[Unset, datetime.date] = UNSET,
    modified_gt: Union[Unset, datetime.date] = UNSET,
    modified_gte: Union[Unset, datetime.date] = UNSET,
    modified_icontains: Union[Unset, datetime.date] = UNSET,
    modified_iendswith: Union[Unset, datetime.date] = UNSET,
    modified_iexact: Union[Unset, datetime.date] = UNSET,
    modified_in: Union[Unset, list[datetime.date]] = UNSET,
    modified_iregex: Union[Unset, datetime.date] = UNSET,
    modified_isnull: Union[Unset, bool] = UNSET,
    modified_iso_week_day: Union[Unset, float] = UNSET,
    modified_iso_year: Union[Unset, float] = UNSET,
    modified_istartswith: Union[Unset, datetime.date] = UNSET,
    modified_lt: Union[Unset, datetime.date] = UNSET,
    modified_lte: Union[Unset, datetime.date] = UNSET,
    modified_month: Union[Unset, float] = UNSET,
    modified_quarter: Union[Unset, float] = UNSET,
    modified_range: Union[Unset, list[datetime.date]] = UNSET,
    modified_regex: Union[Unset, datetime.date] = UNSET,
    modified_startswith: Union[Unset, datetime.date] = UNSET,
    modified_week: Union[Unset, float] = UNSET,
    modified_week_day: Union[Unset, float] = UNSET,
    modified_year: Union[Unset, float] = UNSET,
    ob_ref: Union[Unset, int] = UNSET,
    ob_ref_gt: Union[Unset, int] = UNSET,
    ob_ref_gte: Union[Unset, int] = UNSET,
    ob_ref_in: Union[Unset, list[int]] = UNSET,
    ob_ref_isnull: Union[Unset, bool] = UNSET,
    ob_ref_lt: Union[Unset, int] = UNSET,
    ob_ref_lte: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
    value_contains: Union[Unset, str] = UNSET,
    value_endswith: Union[Unset, str] = UNSET,
    value_gt: Union[Unset, str] = UNSET,
    value_gte: Union[Unset, str] = UNSET,
    value_icontains: Union[Unset, str] = UNSET,
    value_iendswith: Union[Unset, str] = UNSET,
    value_iexact: Union[Unset, str] = UNSET,
    value_in: Union[Unset, list[str]] = UNSET,
    value_iregex: Union[Unset, str] = UNSET,
    value_isnull: Union[Unset, bool] = UNSET,
    value_istartswith: Union[Unset, str] = UNSET,
    value_lt: Union[Unset, str] = UNSET,
    value_lte: Union[Unset, str] = UNSET,
    value_range: Union[Unset, list[str]] = UNSET,
    value_regex: Union[Unset, str] = UNSET,
    value_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedMigrationPropertyReadList]:
    """Get a list of MigrationProperty objects.

    Args:
        id (Union[Unset, int]):
        id_contained_by (Union[Unset, int]):
        id_contains (Union[Unset, int]):
        id_endswith (Union[Unset, int]):
        id_gt (Union[Unset, int]):
        id_gte (Union[Unset, int]):
        id_icontains (Union[Unset, int]):
        id_iendswith (Union[Unset, int]):
        id_iexact (Union[Unset, int]):
        id_in (Union[Unset, list[int]]):
        id_iregex (Union[Unset, int]):
        id_isnull (Union[Unset, bool]):
        id_istartswith (Union[Unset, int]):
        id_lt (Union[Unset, int]):
        id_lte (Union[Unset, int]):
        id_range (Union[Unset, list[int]]):
        id_regex (Union[Unset, int]):
        id_startswith (Union[Unset, int]):
        key (Union[Unset, str]):
        key_contains (Union[Unset, str]):
        key_endswith (Union[Unset, str]):
        key_gt (Union[Unset, str]):
        key_gte (Union[Unset, str]):
        key_icontains (Union[Unset, str]):
        key_iendswith (Union[Unset, str]):
        key_iexact (Union[Unset, str]):
        key_in (Union[Unset, list[str]]):
        key_iregex (Union[Unset, str]):
        key_isnull (Union[Unset, bool]):
        key_istartswith (Union[Unset, str]):
        key_lt (Union[Unset, str]):
        key_lte (Union[Unset, str]):
        key_range (Union[Unset, list[str]]):
        key_regex (Union[Unset, str]):
        key_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        modified (Union[Unset, datetime.date]):
        modified_contained_by (Union[Unset, datetime.date]):
        modified_contains (Union[Unset, datetime.date]):
        modified_day (Union[Unset, float]):
        modified_endswith (Union[Unset, datetime.date]):
        modified_gt (Union[Unset, datetime.date]):
        modified_gte (Union[Unset, datetime.date]):
        modified_icontains (Union[Unset, datetime.date]):
        modified_iendswith (Union[Unset, datetime.date]):
        modified_iexact (Union[Unset, datetime.date]):
        modified_in (Union[Unset, list[datetime.date]]):
        modified_iregex (Union[Unset, datetime.date]):
        modified_isnull (Union[Unset, bool]):
        modified_iso_week_day (Union[Unset, float]):
        modified_iso_year (Union[Unset, float]):
        modified_istartswith (Union[Unset, datetime.date]):
        modified_lt (Union[Unset, datetime.date]):
        modified_lte (Union[Unset, datetime.date]):
        modified_month (Union[Unset, float]):
        modified_quarter (Union[Unset, float]):
        modified_range (Union[Unset, list[datetime.date]]):
        modified_regex (Union[Unset, datetime.date]):
        modified_startswith (Union[Unset, datetime.date]):
        modified_week (Union[Unset, float]):
        modified_week_day (Union[Unset, float]):
        modified_year (Union[Unset, float]):
        ob_ref (Union[Unset, int]):
        ob_ref_gt (Union[Unset, int]):
        ob_ref_gte (Union[Unset, int]):
        ob_ref_in (Union[Unset, list[int]]):
        ob_ref_isnull (Union[Unset, bool]):
        ob_ref_lt (Union[Unset, int]):
        ob_ref_lte (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        value (Union[Unset, str]):
        value_contains (Union[Unset, str]):
        value_endswith (Union[Unset, str]):
        value_gt (Union[Unset, str]):
        value_gte (Union[Unset, str]):
        value_icontains (Union[Unset, str]):
        value_iendswith (Union[Unset, str]):
        value_iexact (Union[Unset, str]):
        value_in (Union[Unset, list[str]]):
        value_iregex (Union[Unset, str]):
        value_isnull (Union[Unset, bool]):
        value_istartswith (Union[Unset, str]):
        value_lt (Union[Unset, str]):
        value_lte (Union[Unset, str]):
        value_range (Union[Unset, list[str]]):
        value_regex (Union[Unset, str]):
        value_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMigrationPropertyReadList]
    """

    kwargs = _get_kwargs(
        id=id,
        id_contained_by=id_contained_by,
        id_contains=id_contains,
        id_endswith=id_endswith,
        id_gt=id_gt,
        id_gte=id_gte,
        id_icontains=id_icontains,
        id_iendswith=id_iendswith,
        id_iexact=id_iexact,
        id_in=id_in,
        id_iregex=id_iregex,
        id_isnull=id_isnull,
        id_istartswith=id_istartswith,
        id_lt=id_lt,
        id_lte=id_lte,
        id_range=id_range,
        id_regex=id_regex,
        id_startswith=id_startswith,
        key=key,
        key_contains=key_contains,
        key_endswith=key_endswith,
        key_gt=key_gt,
        key_gte=key_gte,
        key_icontains=key_icontains,
        key_iendswith=key_iendswith,
        key_iexact=key_iexact,
        key_in=key_in,
        key_iregex=key_iregex,
        key_isnull=key_isnull,
        key_istartswith=key_istartswith,
        key_lt=key_lt,
        key_lte=key_lte,
        key_range=key_range,
        key_regex=key_regex,
        key_startswith=key_startswith,
        limit=limit,
        modified=modified,
        modified_contained_by=modified_contained_by,
        modified_contains=modified_contains,
        modified_day=modified_day,
        modified_endswith=modified_endswith,
        modified_gt=modified_gt,
        modified_gte=modified_gte,
        modified_icontains=modified_icontains,
        modified_iendswith=modified_iendswith,
        modified_iexact=modified_iexact,
        modified_in=modified_in,
        modified_iregex=modified_iregex,
        modified_isnull=modified_isnull,
        modified_iso_week_day=modified_iso_week_day,
        modified_iso_year=modified_iso_year,
        modified_istartswith=modified_istartswith,
        modified_lt=modified_lt,
        modified_lte=modified_lte,
        modified_month=modified_month,
        modified_quarter=modified_quarter,
        modified_range=modified_range,
        modified_regex=modified_regex,
        modified_startswith=modified_startswith,
        modified_week=modified_week,
        modified_week_day=modified_week_day,
        modified_year=modified_year,
        ob_ref=ob_ref,
        ob_ref_gt=ob_ref_gt,
        ob_ref_gte=ob_ref_gte,
        ob_ref_in=ob_ref_in,
        ob_ref_isnull=ob_ref_isnull,
        ob_ref_lt=ob_ref_lt,
        ob_ref_lte=ob_ref_lte,
        offset=offset,
        ordering=ordering,
        value=value,
        value_contains=value_contains,
        value_endswith=value_endswith,
        value_gt=value_gt,
        value_gte=value_gte,
        value_icontains=value_icontains,
        value_iendswith=value_iendswith,
        value_iexact=value_iexact,
        value_in=value_in,
        value_iregex=value_iregex,
        value_isnull=value_isnull,
        value_istartswith=value_istartswith,
        value_lt=value_lt,
        value_lte=value_lte,
        value_range=value_range,
        value_regex=value_regex,
        value_startswith=value_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, int] = UNSET,
    id_contained_by: Union[Unset, int] = UNSET,
    id_contains: Union[Unset, int] = UNSET,
    id_endswith: Union[Unset, int] = UNSET,
    id_gt: Union[Unset, int] = UNSET,
    id_gte: Union[Unset, int] = UNSET,
    id_icontains: Union[Unset, int] = UNSET,
    id_iendswith: Union[Unset, int] = UNSET,
    id_iexact: Union[Unset, int] = UNSET,
    id_in: Union[Unset, list[int]] = UNSET,
    id_iregex: Union[Unset, int] = UNSET,
    id_isnull: Union[Unset, bool] = UNSET,
    id_istartswith: Union[Unset, int] = UNSET,
    id_lt: Union[Unset, int] = UNSET,
    id_lte: Union[Unset, int] = UNSET,
    id_range: Union[Unset, list[int]] = UNSET,
    id_regex: Union[Unset, int] = UNSET,
    id_startswith: Union[Unset, int] = UNSET,
    key: Union[Unset, str] = UNSET,
    key_contains: Union[Unset, str] = UNSET,
    key_endswith: Union[Unset, str] = UNSET,
    key_gt: Union[Unset, str] = UNSET,
    key_gte: Union[Unset, str] = UNSET,
    key_icontains: Union[Unset, str] = UNSET,
    key_iendswith: Union[Unset, str] = UNSET,
    key_iexact: Union[Unset, str] = UNSET,
    key_in: Union[Unset, list[str]] = UNSET,
    key_iregex: Union[Unset, str] = UNSET,
    key_isnull: Union[Unset, bool] = UNSET,
    key_istartswith: Union[Unset, str] = UNSET,
    key_lt: Union[Unset, str] = UNSET,
    key_lte: Union[Unset, str] = UNSET,
    key_range: Union[Unset, list[str]] = UNSET,
    key_regex: Union[Unset, str] = UNSET,
    key_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified: Union[Unset, datetime.date] = UNSET,
    modified_contained_by: Union[Unset, datetime.date] = UNSET,
    modified_contains: Union[Unset, datetime.date] = UNSET,
    modified_day: Union[Unset, float] = UNSET,
    modified_endswith: Union[Unset, datetime.date] = UNSET,
    modified_gt: Union[Unset, datetime.date] = UNSET,
    modified_gte: Union[Unset, datetime.date] = UNSET,
    modified_icontains: Union[Unset, datetime.date] = UNSET,
    modified_iendswith: Union[Unset, datetime.date] = UNSET,
    modified_iexact: Union[Unset, datetime.date] = UNSET,
    modified_in: Union[Unset, list[datetime.date]] = UNSET,
    modified_iregex: Union[Unset, datetime.date] = UNSET,
    modified_isnull: Union[Unset, bool] = UNSET,
    modified_iso_week_day: Union[Unset, float] = UNSET,
    modified_iso_year: Union[Unset, float] = UNSET,
    modified_istartswith: Union[Unset, datetime.date] = UNSET,
    modified_lt: Union[Unset, datetime.date] = UNSET,
    modified_lte: Union[Unset, datetime.date] = UNSET,
    modified_month: Union[Unset, float] = UNSET,
    modified_quarter: Union[Unset, float] = UNSET,
    modified_range: Union[Unset, list[datetime.date]] = UNSET,
    modified_regex: Union[Unset, datetime.date] = UNSET,
    modified_startswith: Union[Unset, datetime.date] = UNSET,
    modified_week: Union[Unset, float] = UNSET,
    modified_week_day: Union[Unset, float] = UNSET,
    modified_year: Union[Unset, float] = UNSET,
    ob_ref: Union[Unset, int] = UNSET,
    ob_ref_gt: Union[Unset, int] = UNSET,
    ob_ref_gte: Union[Unset, int] = UNSET,
    ob_ref_in: Union[Unset, list[int]] = UNSET,
    ob_ref_isnull: Union[Unset, bool] = UNSET,
    ob_ref_lt: Union[Unset, int] = UNSET,
    ob_ref_lte: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
    value_contains: Union[Unset, str] = UNSET,
    value_endswith: Union[Unset, str] = UNSET,
    value_gt: Union[Unset, str] = UNSET,
    value_gte: Union[Unset, str] = UNSET,
    value_icontains: Union[Unset, str] = UNSET,
    value_iendswith: Union[Unset, str] = UNSET,
    value_iexact: Union[Unset, str] = UNSET,
    value_in: Union[Unset, list[str]] = UNSET,
    value_iregex: Union[Unset, str] = UNSET,
    value_isnull: Union[Unset, bool] = UNSET,
    value_istartswith: Union[Unset, str] = UNSET,
    value_lt: Union[Unset, str] = UNSET,
    value_lte: Union[Unset, str] = UNSET,
    value_range: Union[Unset, list[str]] = UNSET,
    value_regex: Union[Unset, str] = UNSET,
    value_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedMigrationPropertyReadList]:
    """Get a list of MigrationProperty objects.

    Args:
        id (Union[Unset, int]):
        id_contained_by (Union[Unset, int]):
        id_contains (Union[Unset, int]):
        id_endswith (Union[Unset, int]):
        id_gt (Union[Unset, int]):
        id_gte (Union[Unset, int]):
        id_icontains (Union[Unset, int]):
        id_iendswith (Union[Unset, int]):
        id_iexact (Union[Unset, int]):
        id_in (Union[Unset, list[int]]):
        id_iregex (Union[Unset, int]):
        id_isnull (Union[Unset, bool]):
        id_istartswith (Union[Unset, int]):
        id_lt (Union[Unset, int]):
        id_lte (Union[Unset, int]):
        id_range (Union[Unset, list[int]]):
        id_regex (Union[Unset, int]):
        id_startswith (Union[Unset, int]):
        key (Union[Unset, str]):
        key_contains (Union[Unset, str]):
        key_endswith (Union[Unset, str]):
        key_gt (Union[Unset, str]):
        key_gte (Union[Unset, str]):
        key_icontains (Union[Unset, str]):
        key_iendswith (Union[Unset, str]):
        key_iexact (Union[Unset, str]):
        key_in (Union[Unset, list[str]]):
        key_iregex (Union[Unset, str]):
        key_isnull (Union[Unset, bool]):
        key_istartswith (Union[Unset, str]):
        key_lt (Union[Unset, str]):
        key_lte (Union[Unset, str]):
        key_range (Union[Unset, list[str]]):
        key_regex (Union[Unset, str]):
        key_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        modified (Union[Unset, datetime.date]):
        modified_contained_by (Union[Unset, datetime.date]):
        modified_contains (Union[Unset, datetime.date]):
        modified_day (Union[Unset, float]):
        modified_endswith (Union[Unset, datetime.date]):
        modified_gt (Union[Unset, datetime.date]):
        modified_gte (Union[Unset, datetime.date]):
        modified_icontains (Union[Unset, datetime.date]):
        modified_iendswith (Union[Unset, datetime.date]):
        modified_iexact (Union[Unset, datetime.date]):
        modified_in (Union[Unset, list[datetime.date]]):
        modified_iregex (Union[Unset, datetime.date]):
        modified_isnull (Union[Unset, bool]):
        modified_iso_week_day (Union[Unset, float]):
        modified_iso_year (Union[Unset, float]):
        modified_istartswith (Union[Unset, datetime.date]):
        modified_lt (Union[Unset, datetime.date]):
        modified_lte (Union[Unset, datetime.date]):
        modified_month (Union[Unset, float]):
        modified_quarter (Union[Unset, float]):
        modified_range (Union[Unset, list[datetime.date]]):
        modified_regex (Union[Unset, datetime.date]):
        modified_startswith (Union[Unset, datetime.date]):
        modified_week (Union[Unset, float]):
        modified_week_day (Union[Unset, float]):
        modified_year (Union[Unset, float]):
        ob_ref (Union[Unset, int]):
        ob_ref_gt (Union[Unset, int]):
        ob_ref_gte (Union[Unset, int]):
        ob_ref_in (Union[Unset, list[int]]):
        ob_ref_isnull (Union[Unset, bool]):
        ob_ref_lt (Union[Unset, int]):
        ob_ref_lte (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        value (Union[Unset, str]):
        value_contains (Union[Unset, str]):
        value_endswith (Union[Unset, str]):
        value_gt (Union[Unset, str]):
        value_gte (Union[Unset, str]):
        value_icontains (Union[Unset, str]):
        value_iendswith (Union[Unset, str]):
        value_iexact (Union[Unset, str]):
        value_in (Union[Unset, list[str]]):
        value_iregex (Union[Unset, str]):
        value_isnull (Union[Unset, bool]):
        value_istartswith (Union[Unset, str]):
        value_lt (Union[Unset, str]):
        value_lte (Union[Unset, str]):
        value_range (Union[Unset, list[str]]):
        value_regex (Union[Unset, str]):
        value_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMigrationPropertyReadList
    """

    return sync_detailed(
        client=client,
        id=id,
        id_contained_by=id_contained_by,
        id_contains=id_contains,
        id_endswith=id_endswith,
        id_gt=id_gt,
        id_gte=id_gte,
        id_icontains=id_icontains,
        id_iendswith=id_iendswith,
        id_iexact=id_iexact,
        id_in=id_in,
        id_iregex=id_iregex,
        id_isnull=id_isnull,
        id_istartswith=id_istartswith,
        id_lt=id_lt,
        id_lte=id_lte,
        id_range=id_range,
        id_regex=id_regex,
        id_startswith=id_startswith,
        key=key,
        key_contains=key_contains,
        key_endswith=key_endswith,
        key_gt=key_gt,
        key_gte=key_gte,
        key_icontains=key_icontains,
        key_iendswith=key_iendswith,
        key_iexact=key_iexact,
        key_in=key_in,
        key_iregex=key_iregex,
        key_isnull=key_isnull,
        key_istartswith=key_istartswith,
        key_lt=key_lt,
        key_lte=key_lte,
        key_range=key_range,
        key_regex=key_regex,
        key_startswith=key_startswith,
        limit=limit,
        modified=modified,
        modified_contained_by=modified_contained_by,
        modified_contains=modified_contains,
        modified_day=modified_day,
        modified_endswith=modified_endswith,
        modified_gt=modified_gt,
        modified_gte=modified_gte,
        modified_icontains=modified_icontains,
        modified_iendswith=modified_iendswith,
        modified_iexact=modified_iexact,
        modified_in=modified_in,
        modified_iregex=modified_iregex,
        modified_isnull=modified_isnull,
        modified_iso_week_day=modified_iso_week_day,
        modified_iso_year=modified_iso_year,
        modified_istartswith=modified_istartswith,
        modified_lt=modified_lt,
        modified_lte=modified_lte,
        modified_month=modified_month,
        modified_quarter=modified_quarter,
        modified_range=modified_range,
        modified_regex=modified_regex,
        modified_startswith=modified_startswith,
        modified_week=modified_week,
        modified_week_day=modified_week_day,
        modified_year=modified_year,
        ob_ref=ob_ref,
        ob_ref_gt=ob_ref_gt,
        ob_ref_gte=ob_ref_gte,
        ob_ref_in=ob_ref_in,
        ob_ref_isnull=ob_ref_isnull,
        ob_ref_lt=ob_ref_lt,
        ob_ref_lte=ob_ref_lte,
        offset=offset,
        ordering=ordering,
        value=value,
        value_contains=value_contains,
        value_endswith=value_endswith,
        value_gt=value_gt,
        value_gte=value_gte,
        value_icontains=value_icontains,
        value_iendswith=value_iendswith,
        value_iexact=value_iexact,
        value_in=value_in,
        value_iregex=value_iregex,
        value_isnull=value_isnull,
        value_istartswith=value_istartswith,
        value_lt=value_lt,
        value_lte=value_lte,
        value_range=value_range,
        value_regex=value_regex,
        value_startswith=value_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, int] = UNSET,
    id_contained_by: Union[Unset, int] = UNSET,
    id_contains: Union[Unset, int] = UNSET,
    id_endswith: Union[Unset, int] = UNSET,
    id_gt: Union[Unset, int] = UNSET,
    id_gte: Union[Unset, int] = UNSET,
    id_icontains: Union[Unset, int] = UNSET,
    id_iendswith: Union[Unset, int] = UNSET,
    id_iexact: Union[Unset, int] = UNSET,
    id_in: Union[Unset, list[int]] = UNSET,
    id_iregex: Union[Unset, int] = UNSET,
    id_isnull: Union[Unset, bool] = UNSET,
    id_istartswith: Union[Unset, int] = UNSET,
    id_lt: Union[Unset, int] = UNSET,
    id_lte: Union[Unset, int] = UNSET,
    id_range: Union[Unset, list[int]] = UNSET,
    id_regex: Union[Unset, int] = UNSET,
    id_startswith: Union[Unset, int] = UNSET,
    key: Union[Unset, str] = UNSET,
    key_contains: Union[Unset, str] = UNSET,
    key_endswith: Union[Unset, str] = UNSET,
    key_gt: Union[Unset, str] = UNSET,
    key_gte: Union[Unset, str] = UNSET,
    key_icontains: Union[Unset, str] = UNSET,
    key_iendswith: Union[Unset, str] = UNSET,
    key_iexact: Union[Unset, str] = UNSET,
    key_in: Union[Unset, list[str]] = UNSET,
    key_iregex: Union[Unset, str] = UNSET,
    key_isnull: Union[Unset, bool] = UNSET,
    key_istartswith: Union[Unset, str] = UNSET,
    key_lt: Union[Unset, str] = UNSET,
    key_lte: Union[Unset, str] = UNSET,
    key_range: Union[Unset, list[str]] = UNSET,
    key_regex: Union[Unset, str] = UNSET,
    key_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified: Union[Unset, datetime.date] = UNSET,
    modified_contained_by: Union[Unset, datetime.date] = UNSET,
    modified_contains: Union[Unset, datetime.date] = UNSET,
    modified_day: Union[Unset, float] = UNSET,
    modified_endswith: Union[Unset, datetime.date] = UNSET,
    modified_gt: Union[Unset, datetime.date] = UNSET,
    modified_gte: Union[Unset, datetime.date] = UNSET,
    modified_icontains: Union[Unset, datetime.date] = UNSET,
    modified_iendswith: Union[Unset, datetime.date] = UNSET,
    modified_iexact: Union[Unset, datetime.date] = UNSET,
    modified_in: Union[Unset, list[datetime.date]] = UNSET,
    modified_iregex: Union[Unset, datetime.date] = UNSET,
    modified_isnull: Union[Unset, bool] = UNSET,
    modified_iso_week_day: Union[Unset, float] = UNSET,
    modified_iso_year: Union[Unset, float] = UNSET,
    modified_istartswith: Union[Unset, datetime.date] = UNSET,
    modified_lt: Union[Unset, datetime.date] = UNSET,
    modified_lte: Union[Unset, datetime.date] = UNSET,
    modified_month: Union[Unset, float] = UNSET,
    modified_quarter: Union[Unset, float] = UNSET,
    modified_range: Union[Unset, list[datetime.date]] = UNSET,
    modified_regex: Union[Unset, datetime.date] = UNSET,
    modified_startswith: Union[Unset, datetime.date] = UNSET,
    modified_week: Union[Unset, float] = UNSET,
    modified_week_day: Union[Unset, float] = UNSET,
    modified_year: Union[Unset, float] = UNSET,
    ob_ref: Union[Unset, int] = UNSET,
    ob_ref_gt: Union[Unset, int] = UNSET,
    ob_ref_gte: Union[Unset, int] = UNSET,
    ob_ref_in: Union[Unset, list[int]] = UNSET,
    ob_ref_isnull: Union[Unset, bool] = UNSET,
    ob_ref_lt: Union[Unset, int] = UNSET,
    ob_ref_lte: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
    value_contains: Union[Unset, str] = UNSET,
    value_endswith: Union[Unset, str] = UNSET,
    value_gt: Union[Unset, str] = UNSET,
    value_gte: Union[Unset, str] = UNSET,
    value_icontains: Union[Unset, str] = UNSET,
    value_iendswith: Union[Unset, str] = UNSET,
    value_iexact: Union[Unset, str] = UNSET,
    value_in: Union[Unset, list[str]] = UNSET,
    value_iregex: Union[Unset, str] = UNSET,
    value_isnull: Union[Unset, bool] = UNSET,
    value_istartswith: Union[Unset, str] = UNSET,
    value_lt: Union[Unset, str] = UNSET,
    value_lte: Union[Unset, str] = UNSET,
    value_range: Union[Unset, list[str]] = UNSET,
    value_regex: Union[Unset, str] = UNSET,
    value_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedMigrationPropertyReadList]:
    """Get a list of MigrationProperty objects.

    Args:
        id (Union[Unset, int]):
        id_contained_by (Union[Unset, int]):
        id_contains (Union[Unset, int]):
        id_endswith (Union[Unset, int]):
        id_gt (Union[Unset, int]):
        id_gte (Union[Unset, int]):
        id_icontains (Union[Unset, int]):
        id_iendswith (Union[Unset, int]):
        id_iexact (Union[Unset, int]):
        id_in (Union[Unset, list[int]]):
        id_iregex (Union[Unset, int]):
        id_isnull (Union[Unset, bool]):
        id_istartswith (Union[Unset, int]):
        id_lt (Union[Unset, int]):
        id_lte (Union[Unset, int]):
        id_range (Union[Unset, list[int]]):
        id_regex (Union[Unset, int]):
        id_startswith (Union[Unset, int]):
        key (Union[Unset, str]):
        key_contains (Union[Unset, str]):
        key_endswith (Union[Unset, str]):
        key_gt (Union[Unset, str]):
        key_gte (Union[Unset, str]):
        key_icontains (Union[Unset, str]):
        key_iendswith (Union[Unset, str]):
        key_iexact (Union[Unset, str]):
        key_in (Union[Unset, list[str]]):
        key_iregex (Union[Unset, str]):
        key_isnull (Union[Unset, bool]):
        key_istartswith (Union[Unset, str]):
        key_lt (Union[Unset, str]):
        key_lte (Union[Unset, str]):
        key_range (Union[Unset, list[str]]):
        key_regex (Union[Unset, str]):
        key_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        modified (Union[Unset, datetime.date]):
        modified_contained_by (Union[Unset, datetime.date]):
        modified_contains (Union[Unset, datetime.date]):
        modified_day (Union[Unset, float]):
        modified_endswith (Union[Unset, datetime.date]):
        modified_gt (Union[Unset, datetime.date]):
        modified_gte (Union[Unset, datetime.date]):
        modified_icontains (Union[Unset, datetime.date]):
        modified_iendswith (Union[Unset, datetime.date]):
        modified_iexact (Union[Unset, datetime.date]):
        modified_in (Union[Unset, list[datetime.date]]):
        modified_iregex (Union[Unset, datetime.date]):
        modified_isnull (Union[Unset, bool]):
        modified_iso_week_day (Union[Unset, float]):
        modified_iso_year (Union[Unset, float]):
        modified_istartswith (Union[Unset, datetime.date]):
        modified_lt (Union[Unset, datetime.date]):
        modified_lte (Union[Unset, datetime.date]):
        modified_month (Union[Unset, float]):
        modified_quarter (Union[Unset, float]):
        modified_range (Union[Unset, list[datetime.date]]):
        modified_regex (Union[Unset, datetime.date]):
        modified_startswith (Union[Unset, datetime.date]):
        modified_week (Union[Unset, float]):
        modified_week_day (Union[Unset, float]):
        modified_year (Union[Unset, float]):
        ob_ref (Union[Unset, int]):
        ob_ref_gt (Union[Unset, int]):
        ob_ref_gte (Union[Unset, int]):
        ob_ref_in (Union[Unset, list[int]]):
        ob_ref_isnull (Union[Unset, bool]):
        ob_ref_lt (Union[Unset, int]):
        ob_ref_lte (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        value (Union[Unset, str]):
        value_contains (Union[Unset, str]):
        value_endswith (Union[Unset, str]):
        value_gt (Union[Unset, str]):
        value_gte (Union[Unset, str]):
        value_icontains (Union[Unset, str]):
        value_iendswith (Union[Unset, str]):
        value_iexact (Union[Unset, str]):
        value_in (Union[Unset, list[str]]):
        value_iregex (Union[Unset, str]):
        value_isnull (Union[Unset, bool]):
        value_istartswith (Union[Unset, str]):
        value_lt (Union[Unset, str]):
        value_lte (Union[Unset, str]):
        value_range (Union[Unset, list[str]]):
        value_regex (Union[Unset, str]):
        value_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedMigrationPropertyReadList]
    """

    kwargs = _get_kwargs(
        id=id,
        id_contained_by=id_contained_by,
        id_contains=id_contains,
        id_endswith=id_endswith,
        id_gt=id_gt,
        id_gte=id_gte,
        id_icontains=id_icontains,
        id_iendswith=id_iendswith,
        id_iexact=id_iexact,
        id_in=id_in,
        id_iregex=id_iregex,
        id_isnull=id_isnull,
        id_istartswith=id_istartswith,
        id_lt=id_lt,
        id_lte=id_lte,
        id_range=id_range,
        id_regex=id_regex,
        id_startswith=id_startswith,
        key=key,
        key_contains=key_contains,
        key_endswith=key_endswith,
        key_gt=key_gt,
        key_gte=key_gte,
        key_icontains=key_icontains,
        key_iendswith=key_iendswith,
        key_iexact=key_iexact,
        key_in=key_in,
        key_iregex=key_iregex,
        key_isnull=key_isnull,
        key_istartswith=key_istartswith,
        key_lt=key_lt,
        key_lte=key_lte,
        key_range=key_range,
        key_regex=key_regex,
        key_startswith=key_startswith,
        limit=limit,
        modified=modified,
        modified_contained_by=modified_contained_by,
        modified_contains=modified_contains,
        modified_day=modified_day,
        modified_endswith=modified_endswith,
        modified_gt=modified_gt,
        modified_gte=modified_gte,
        modified_icontains=modified_icontains,
        modified_iendswith=modified_iendswith,
        modified_iexact=modified_iexact,
        modified_in=modified_in,
        modified_iregex=modified_iregex,
        modified_isnull=modified_isnull,
        modified_iso_week_day=modified_iso_week_day,
        modified_iso_year=modified_iso_year,
        modified_istartswith=modified_istartswith,
        modified_lt=modified_lt,
        modified_lte=modified_lte,
        modified_month=modified_month,
        modified_quarter=modified_quarter,
        modified_range=modified_range,
        modified_regex=modified_regex,
        modified_startswith=modified_startswith,
        modified_week=modified_week,
        modified_week_day=modified_week_day,
        modified_year=modified_year,
        ob_ref=ob_ref,
        ob_ref_gt=ob_ref_gt,
        ob_ref_gte=ob_ref_gte,
        ob_ref_in=ob_ref_in,
        ob_ref_isnull=ob_ref_isnull,
        ob_ref_lt=ob_ref_lt,
        ob_ref_lte=ob_ref_lte,
        offset=offset,
        ordering=ordering,
        value=value,
        value_contains=value_contains,
        value_endswith=value_endswith,
        value_gt=value_gt,
        value_gte=value_gte,
        value_icontains=value_icontains,
        value_iendswith=value_iendswith,
        value_iexact=value_iexact,
        value_in=value_in,
        value_iregex=value_iregex,
        value_isnull=value_isnull,
        value_istartswith=value_istartswith,
        value_lt=value_lt,
        value_lte=value_lte,
        value_range=value_range,
        value_regex=value_regex,
        value_startswith=value_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: Union[Unset, int] = UNSET,
    id_contained_by: Union[Unset, int] = UNSET,
    id_contains: Union[Unset, int] = UNSET,
    id_endswith: Union[Unset, int] = UNSET,
    id_gt: Union[Unset, int] = UNSET,
    id_gte: Union[Unset, int] = UNSET,
    id_icontains: Union[Unset, int] = UNSET,
    id_iendswith: Union[Unset, int] = UNSET,
    id_iexact: Union[Unset, int] = UNSET,
    id_in: Union[Unset, list[int]] = UNSET,
    id_iregex: Union[Unset, int] = UNSET,
    id_isnull: Union[Unset, bool] = UNSET,
    id_istartswith: Union[Unset, int] = UNSET,
    id_lt: Union[Unset, int] = UNSET,
    id_lte: Union[Unset, int] = UNSET,
    id_range: Union[Unset, list[int]] = UNSET,
    id_regex: Union[Unset, int] = UNSET,
    id_startswith: Union[Unset, int] = UNSET,
    key: Union[Unset, str] = UNSET,
    key_contains: Union[Unset, str] = UNSET,
    key_endswith: Union[Unset, str] = UNSET,
    key_gt: Union[Unset, str] = UNSET,
    key_gte: Union[Unset, str] = UNSET,
    key_icontains: Union[Unset, str] = UNSET,
    key_iendswith: Union[Unset, str] = UNSET,
    key_iexact: Union[Unset, str] = UNSET,
    key_in: Union[Unset, list[str]] = UNSET,
    key_iregex: Union[Unset, str] = UNSET,
    key_isnull: Union[Unset, bool] = UNSET,
    key_istartswith: Union[Unset, str] = UNSET,
    key_lt: Union[Unset, str] = UNSET,
    key_lte: Union[Unset, str] = UNSET,
    key_range: Union[Unset, list[str]] = UNSET,
    key_regex: Union[Unset, str] = UNSET,
    key_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    modified: Union[Unset, datetime.date] = UNSET,
    modified_contained_by: Union[Unset, datetime.date] = UNSET,
    modified_contains: Union[Unset, datetime.date] = UNSET,
    modified_day: Union[Unset, float] = UNSET,
    modified_endswith: Union[Unset, datetime.date] = UNSET,
    modified_gt: Union[Unset, datetime.date] = UNSET,
    modified_gte: Union[Unset, datetime.date] = UNSET,
    modified_icontains: Union[Unset, datetime.date] = UNSET,
    modified_iendswith: Union[Unset, datetime.date] = UNSET,
    modified_iexact: Union[Unset, datetime.date] = UNSET,
    modified_in: Union[Unset, list[datetime.date]] = UNSET,
    modified_iregex: Union[Unset, datetime.date] = UNSET,
    modified_isnull: Union[Unset, bool] = UNSET,
    modified_iso_week_day: Union[Unset, float] = UNSET,
    modified_iso_year: Union[Unset, float] = UNSET,
    modified_istartswith: Union[Unset, datetime.date] = UNSET,
    modified_lt: Union[Unset, datetime.date] = UNSET,
    modified_lte: Union[Unset, datetime.date] = UNSET,
    modified_month: Union[Unset, float] = UNSET,
    modified_quarter: Union[Unset, float] = UNSET,
    modified_range: Union[Unset, list[datetime.date]] = UNSET,
    modified_regex: Union[Unset, datetime.date] = UNSET,
    modified_startswith: Union[Unset, datetime.date] = UNSET,
    modified_week: Union[Unset, float] = UNSET,
    modified_week_day: Union[Unset, float] = UNSET,
    modified_year: Union[Unset, float] = UNSET,
    ob_ref: Union[Unset, int] = UNSET,
    ob_ref_gt: Union[Unset, int] = UNSET,
    ob_ref_gte: Union[Unset, int] = UNSET,
    ob_ref_in: Union[Unset, list[int]] = UNSET,
    ob_ref_isnull: Union[Unset, bool] = UNSET,
    ob_ref_lt: Union[Unset, int] = UNSET,
    ob_ref_lte: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    value: Union[Unset, str] = UNSET,
    value_contains: Union[Unset, str] = UNSET,
    value_endswith: Union[Unset, str] = UNSET,
    value_gt: Union[Unset, str] = UNSET,
    value_gte: Union[Unset, str] = UNSET,
    value_icontains: Union[Unset, str] = UNSET,
    value_iendswith: Union[Unset, str] = UNSET,
    value_iexact: Union[Unset, str] = UNSET,
    value_in: Union[Unset, list[str]] = UNSET,
    value_iregex: Union[Unset, str] = UNSET,
    value_isnull: Union[Unset, bool] = UNSET,
    value_istartswith: Union[Unset, str] = UNSET,
    value_lt: Union[Unset, str] = UNSET,
    value_lte: Union[Unset, str] = UNSET,
    value_range: Union[Unset, list[str]] = UNSET,
    value_regex: Union[Unset, str] = UNSET,
    value_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedMigrationPropertyReadList]:
    """Get a list of MigrationProperty objects.

    Args:
        id (Union[Unset, int]):
        id_contained_by (Union[Unset, int]):
        id_contains (Union[Unset, int]):
        id_endswith (Union[Unset, int]):
        id_gt (Union[Unset, int]):
        id_gte (Union[Unset, int]):
        id_icontains (Union[Unset, int]):
        id_iendswith (Union[Unset, int]):
        id_iexact (Union[Unset, int]):
        id_in (Union[Unset, list[int]]):
        id_iregex (Union[Unset, int]):
        id_isnull (Union[Unset, bool]):
        id_istartswith (Union[Unset, int]):
        id_lt (Union[Unset, int]):
        id_lte (Union[Unset, int]):
        id_range (Union[Unset, list[int]]):
        id_regex (Union[Unset, int]):
        id_startswith (Union[Unset, int]):
        key (Union[Unset, str]):
        key_contains (Union[Unset, str]):
        key_endswith (Union[Unset, str]):
        key_gt (Union[Unset, str]):
        key_gte (Union[Unset, str]):
        key_icontains (Union[Unset, str]):
        key_iendswith (Union[Unset, str]):
        key_iexact (Union[Unset, str]):
        key_in (Union[Unset, list[str]]):
        key_iregex (Union[Unset, str]):
        key_isnull (Union[Unset, bool]):
        key_istartswith (Union[Unset, str]):
        key_lt (Union[Unset, str]):
        key_lte (Union[Unset, str]):
        key_range (Union[Unset, list[str]]):
        key_regex (Union[Unset, str]):
        key_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        modified (Union[Unset, datetime.date]):
        modified_contained_by (Union[Unset, datetime.date]):
        modified_contains (Union[Unset, datetime.date]):
        modified_day (Union[Unset, float]):
        modified_endswith (Union[Unset, datetime.date]):
        modified_gt (Union[Unset, datetime.date]):
        modified_gte (Union[Unset, datetime.date]):
        modified_icontains (Union[Unset, datetime.date]):
        modified_iendswith (Union[Unset, datetime.date]):
        modified_iexact (Union[Unset, datetime.date]):
        modified_in (Union[Unset, list[datetime.date]]):
        modified_iregex (Union[Unset, datetime.date]):
        modified_isnull (Union[Unset, bool]):
        modified_iso_week_day (Union[Unset, float]):
        modified_iso_year (Union[Unset, float]):
        modified_istartswith (Union[Unset, datetime.date]):
        modified_lt (Union[Unset, datetime.date]):
        modified_lte (Union[Unset, datetime.date]):
        modified_month (Union[Unset, float]):
        modified_quarter (Union[Unset, float]):
        modified_range (Union[Unset, list[datetime.date]]):
        modified_regex (Union[Unset, datetime.date]):
        modified_startswith (Union[Unset, datetime.date]):
        modified_week (Union[Unset, float]):
        modified_week_day (Union[Unset, float]):
        modified_year (Union[Unset, float]):
        ob_ref (Union[Unset, int]):
        ob_ref_gt (Union[Unset, int]):
        ob_ref_gte (Union[Unset, int]):
        ob_ref_in (Union[Unset, list[int]]):
        ob_ref_isnull (Union[Unset, bool]):
        ob_ref_lt (Union[Unset, int]):
        ob_ref_lte (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        value (Union[Unset, str]):
        value_contains (Union[Unset, str]):
        value_endswith (Union[Unset, str]):
        value_gt (Union[Unset, str]):
        value_gte (Union[Unset, str]):
        value_icontains (Union[Unset, str]):
        value_iendswith (Union[Unset, str]):
        value_iexact (Union[Unset, str]):
        value_in (Union[Unset, list[str]]):
        value_iregex (Union[Unset, str]):
        value_isnull (Union[Unset, bool]):
        value_istartswith (Union[Unset, str]):
        value_lt (Union[Unset, str]):
        value_lte (Union[Unset, str]):
        value_range (Union[Unset, list[str]]):
        value_regex (Union[Unset, str]):
        value_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedMigrationPropertyReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            id_contained_by=id_contained_by,
            id_contains=id_contains,
            id_endswith=id_endswith,
            id_gt=id_gt,
            id_gte=id_gte,
            id_icontains=id_icontains,
            id_iendswith=id_iendswith,
            id_iexact=id_iexact,
            id_in=id_in,
            id_iregex=id_iregex,
            id_isnull=id_isnull,
            id_istartswith=id_istartswith,
            id_lt=id_lt,
            id_lte=id_lte,
            id_range=id_range,
            id_regex=id_regex,
            id_startswith=id_startswith,
            key=key,
            key_contains=key_contains,
            key_endswith=key_endswith,
            key_gt=key_gt,
            key_gte=key_gte,
            key_icontains=key_icontains,
            key_iendswith=key_iendswith,
            key_iexact=key_iexact,
            key_in=key_in,
            key_iregex=key_iregex,
            key_isnull=key_isnull,
            key_istartswith=key_istartswith,
            key_lt=key_lt,
            key_lte=key_lte,
            key_range=key_range,
            key_regex=key_regex,
            key_startswith=key_startswith,
            limit=limit,
            modified=modified,
            modified_contained_by=modified_contained_by,
            modified_contains=modified_contains,
            modified_day=modified_day,
            modified_endswith=modified_endswith,
            modified_gt=modified_gt,
            modified_gte=modified_gte,
            modified_icontains=modified_icontains,
            modified_iendswith=modified_iendswith,
            modified_iexact=modified_iexact,
            modified_in=modified_in,
            modified_iregex=modified_iregex,
            modified_isnull=modified_isnull,
            modified_iso_week_day=modified_iso_week_day,
            modified_iso_year=modified_iso_year,
            modified_istartswith=modified_istartswith,
            modified_lt=modified_lt,
            modified_lte=modified_lte,
            modified_month=modified_month,
            modified_quarter=modified_quarter,
            modified_range=modified_range,
            modified_regex=modified_regex,
            modified_startswith=modified_startswith,
            modified_week=modified_week,
            modified_week_day=modified_week_day,
            modified_year=modified_year,
            ob_ref=ob_ref,
            ob_ref_gt=ob_ref_gt,
            ob_ref_gte=ob_ref_gte,
            ob_ref_in=ob_ref_in,
            ob_ref_isnull=ob_ref_isnull,
            ob_ref_lt=ob_ref_lt,
            ob_ref_lte=ob_ref_lte,
            offset=offset,
            ordering=ordering,
            value=value,
            value_contains=value_contains,
            value_endswith=value_endswith,
            value_gt=value_gt,
            value_gte=value_gte,
            value_icontains=value_icontains,
            value_iendswith=value_iendswith,
            value_iexact=value_iexact,
            value_in=value_in,
            value_iregex=value_iregex,
            value_isnull=value_isnull,
            value_istartswith=value_istartswith,
            value_lt=value_lt,
            value_lte=value_lte,
            value_range=value_range,
            value_regex=value_regex,
            value_startswith=value_startswith,
        )
    ).parsed
