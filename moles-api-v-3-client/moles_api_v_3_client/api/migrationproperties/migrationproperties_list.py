import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_migration_property_read_list import PaginatedMigrationPropertyReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: int | Unset = UNSET,
    id_contained_by: int | Unset = UNSET,
    id_contains: int | Unset = UNSET,
    id_endswith: int | Unset = UNSET,
    id_gt: int | Unset = UNSET,
    id_gte: int | Unset = UNSET,
    id_icontains: int | Unset = UNSET,
    id_iendswith: int | Unset = UNSET,
    id_iexact: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    id_iregex: int | Unset = UNSET,
    id_isnull: bool | Unset = UNSET,
    id_istartswith: int | Unset = UNSET,
    id_lt: int | Unset = UNSET,
    id_lte: int | Unset = UNSET,
    id_range: list[int] | Unset = UNSET,
    id_regex: int | Unset = UNSET,
    id_startswith: int | Unset = UNSET,
    key: str | Unset = UNSET,
    key_contains: str | Unset = UNSET,
    key_endswith: str | Unset = UNSET,
    key_gt: str | Unset = UNSET,
    key_gte: str | Unset = UNSET,
    key_icontains: str | Unset = UNSET,
    key_iendswith: str | Unset = UNSET,
    key_iexact: str | Unset = UNSET,
    key_in: list[str] | Unset = UNSET,
    key_iregex: str | Unset = UNSET,
    key_isnull: bool | Unset = UNSET,
    key_istartswith: str | Unset = UNSET,
    key_lt: str | Unset = UNSET,
    key_lte: str | Unset = UNSET,
    key_range: list[str] | Unset = UNSET,
    key_regex: str | Unset = UNSET,
    key_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    modified: datetime.date | Unset = UNSET,
    modified_contained_by: datetime.date | Unset = UNSET,
    modified_contains: datetime.date | Unset = UNSET,
    modified_day: float | Unset = UNSET,
    modified_endswith: datetime.date | Unset = UNSET,
    modified_gt: datetime.date | Unset = UNSET,
    modified_gte: datetime.date | Unset = UNSET,
    modified_icontains: datetime.date | Unset = UNSET,
    modified_iendswith: datetime.date | Unset = UNSET,
    modified_iexact: datetime.date | Unset = UNSET,
    modified_in: list[datetime.date] | Unset = UNSET,
    modified_iregex: datetime.date | Unset = UNSET,
    modified_isnull: bool | Unset = UNSET,
    modified_iso_week_day: float | Unset = UNSET,
    modified_iso_year: float | Unset = UNSET,
    modified_istartswith: datetime.date | Unset = UNSET,
    modified_lt: datetime.date | Unset = UNSET,
    modified_lte: datetime.date | Unset = UNSET,
    modified_month: float | Unset = UNSET,
    modified_quarter: float | Unset = UNSET,
    modified_range: list[datetime.date] | Unset = UNSET,
    modified_regex: datetime.date | Unset = UNSET,
    modified_startswith: datetime.date | Unset = UNSET,
    modified_week: float | Unset = UNSET,
    modified_week_day: float | Unset = UNSET,
    modified_year: float | Unset = UNSET,
    ob_ref: int | Unset = UNSET,
    ob_ref_in: list[int] | Unset = UNSET,
    ob_ref_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    value: str | Unset = UNSET,
    value_contains: str | Unset = UNSET,
    value_endswith: str | Unset = UNSET,
    value_gt: str | Unset = UNSET,
    value_gte: str | Unset = UNSET,
    value_icontains: str | Unset = UNSET,
    value_iendswith: str | Unset = UNSET,
    value_iexact: str | Unset = UNSET,
    value_in: list[str] | Unset = UNSET,
    value_iregex: str | Unset = UNSET,
    value_isnull: bool | Unset = UNSET,
    value_istartswith: str | Unset = UNSET,
    value_lt: str | Unset = UNSET,
    value_lte: str | Unset = UNSET,
    value_range: list[str] | Unset = UNSET,
    value_regex: str | Unset = UNSET,
    value_startswith: str | Unset = UNSET,
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

    json_id_in: list[int] | Unset = UNSET
    if not isinstance(id_in, Unset):
        json_id_in = id_in

    params["id__in"] = json_id_in

    params["id__iregex"] = id_iregex

    params["id__isnull"] = id_isnull

    params["id__istartswith"] = id_istartswith

    params["id__lt"] = id_lt

    params["id__lte"] = id_lte

    json_id_range: list[int] | Unset = UNSET
    if not isinstance(id_range, Unset):
        json_id_range = id_range

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

    json_key_in: list[str] | Unset = UNSET
    if not isinstance(key_in, Unset):
        json_key_in = key_in

    params["key__in"] = json_key_in

    params["key__iregex"] = key_iregex

    params["key__isnull"] = key_isnull

    params["key__istartswith"] = key_istartswith

    params["key__lt"] = key_lt

    params["key__lte"] = key_lte

    json_key_range: list[str] | Unset = UNSET
    if not isinstance(key_range, Unset):
        json_key_range = key_range

    params["key__range"] = json_key_range

    params["key__regex"] = key_regex

    params["key__startswith"] = key_startswith

    params["limit"] = limit

    json_modified: str | Unset = UNSET
    if not isinstance(modified, Unset):
        json_modified = modified.isoformat()
    params["modified"] = json_modified

    json_modified_contained_by: str | Unset = UNSET
    if not isinstance(modified_contained_by, Unset):
        json_modified_contained_by = modified_contained_by.isoformat()
    params["modified__contained_by"] = json_modified_contained_by

    json_modified_contains: str | Unset = UNSET
    if not isinstance(modified_contains, Unset):
        json_modified_contains = modified_contains.isoformat()
    params["modified__contains"] = json_modified_contains

    params["modified__day"] = modified_day

    json_modified_endswith: str | Unset = UNSET
    if not isinstance(modified_endswith, Unset):
        json_modified_endswith = modified_endswith.isoformat()
    params["modified__endswith"] = json_modified_endswith

    json_modified_gt: str | Unset = UNSET
    if not isinstance(modified_gt, Unset):
        json_modified_gt = modified_gt.isoformat()
    params["modified__gt"] = json_modified_gt

    json_modified_gte: str | Unset = UNSET
    if not isinstance(modified_gte, Unset):
        json_modified_gte = modified_gte.isoformat()
    params["modified__gte"] = json_modified_gte

    json_modified_icontains: str | Unset = UNSET
    if not isinstance(modified_icontains, Unset):
        json_modified_icontains = modified_icontains.isoformat()
    params["modified__icontains"] = json_modified_icontains

    json_modified_iendswith: str | Unset = UNSET
    if not isinstance(modified_iendswith, Unset):
        json_modified_iendswith = modified_iendswith.isoformat()
    params["modified__iendswith"] = json_modified_iendswith

    json_modified_iexact: str | Unset = UNSET
    if not isinstance(modified_iexact, Unset):
        json_modified_iexact = modified_iexact.isoformat()
    params["modified__iexact"] = json_modified_iexact

    json_modified_in: list[str] | Unset = UNSET
    if not isinstance(modified_in, Unset):
        json_modified_in = []
        for modified_in_item_data in modified_in:
            modified_in_item = modified_in_item_data.isoformat()
            json_modified_in.append(modified_in_item)

    params["modified__in"] = json_modified_in

    json_modified_iregex: str | Unset = UNSET
    if not isinstance(modified_iregex, Unset):
        json_modified_iregex = modified_iregex.isoformat()
    params["modified__iregex"] = json_modified_iregex

    params["modified__isnull"] = modified_isnull

    params["modified__iso_week_day"] = modified_iso_week_day

    params["modified__iso_year"] = modified_iso_year

    json_modified_istartswith: str | Unset = UNSET
    if not isinstance(modified_istartswith, Unset):
        json_modified_istartswith = modified_istartswith.isoformat()
    params["modified__istartswith"] = json_modified_istartswith

    json_modified_lt: str | Unset = UNSET
    if not isinstance(modified_lt, Unset):
        json_modified_lt = modified_lt.isoformat()
    params["modified__lt"] = json_modified_lt

    json_modified_lte: str | Unset = UNSET
    if not isinstance(modified_lte, Unset):
        json_modified_lte = modified_lte.isoformat()
    params["modified__lte"] = json_modified_lte

    params["modified__month"] = modified_month

    params["modified__quarter"] = modified_quarter

    json_modified_range: list[str] | Unset = UNSET
    if not isinstance(modified_range, Unset):
        json_modified_range = []
        for modified_range_item_data in modified_range:
            modified_range_item = modified_range_item_data.isoformat()
            json_modified_range.append(modified_range_item)

    params["modified__range"] = json_modified_range

    json_modified_regex: str | Unset = UNSET
    if not isinstance(modified_regex, Unset):
        json_modified_regex = modified_regex.isoformat()
    params["modified__regex"] = json_modified_regex

    json_modified_startswith: str | Unset = UNSET
    if not isinstance(modified_startswith, Unset):
        json_modified_startswith = modified_startswith.isoformat()
    params["modified__startswith"] = json_modified_startswith

    params["modified__week"] = modified_week

    params["modified__week_day"] = modified_week_day

    params["modified__year"] = modified_year

    params["ob_ref"] = ob_ref

    json_ob_ref_in: list[int] | Unset = UNSET
    if not isinstance(ob_ref_in, Unset):
        json_ob_ref_in = ob_ref_in

    params["ob_ref__in"] = json_ob_ref_in

    params["ob_ref__isnull"] = ob_ref_isnull

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

    json_value_in: list[str] | Unset = UNSET
    if not isinstance(value_in, Unset):
        json_value_in = value_in

    params["value__in"] = json_value_in

    params["value__iregex"] = value_iregex

    params["value__isnull"] = value_isnull

    params["value__istartswith"] = value_istartswith

    params["value__lt"] = value_lt

    params["value__lte"] = value_lte

    json_value_range: list[str] | Unset = UNSET
    if not isinstance(value_range, Unset):
        json_value_range = value_range

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedMigrationPropertyReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedMigrationPropertyReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    id: int | Unset = UNSET,
    id_contained_by: int | Unset = UNSET,
    id_contains: int | Unset = UNSET,
    id_endswith: int | Unset = UNSET,
    id_gt: int | Unset = UNSET,
    id_gte: int | Unset = UNSET,
    id_icontains: int | Unset = UNSET,
    id_iendswith: int | Unset = UNSET,
    id_iexact: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    id_iregex: int | Unset = UNSET,
    id_isnull: bool | Unset = UNSET,
    id_istartswith: int | Unset = UNSET,
    id_lt: int | Unset = UNSET,
    id_lte: int | Unset = UNSET,
    id_range: list[int] | Unset = UNSET,
    id_regex: int | Unset = UNSET,
    id_startswith: int | Unset = UNSET,
    key: str | Unset = UNSET,
    key_contains: str | Unset = UNSET,
    key_endswith: str | Unset = UNSET,
    key_gt: str | Unset = UNSET,
    key_gte: str | Unset = UNSET,
    key_icontains: str | Unset = UNSET,
    key_iendswith: str | Unset = UNSET,
    key_iexact: str | Unset = UNSET,
    key_in: list[str] | Unset = UNSET,
    key_iregex: str | Unset = UNSET,
    key_isnull: bool | Unset = UNSET,
    key_istartswith: str | Unset = UNSET,
    key_lt: str | Unset = UNSET,
    key_lte: str | Unset = UNSET,
    key_range: list[str] | Unset = UNSET,
    key_regex: str | Unset = UNSET,
    key_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    modified: datetime.date | Unset = UNSET,
    modified_contained_by: datetime.date | Unset = UNSET,
    modified_contains: datetime.date | Unset = UNSET,
    modified_day: float | Unset = UNSET,
    modified_endswith: datetime.date | Unset = UNSET,
    modified_gt: datetime.date | Unset = UNSET,
    modified_gte: datetime.date | Unset = UNSET,
    modified_icontains: datetime.date | Unset = UNSET,
    modified_iendswith: datetime.date | Unset = UNSET,
    modified_iexact: datetime.date | Unset = UNSET,
    modified_in: list[datetime.date] | Unset = UNSET,
    modified_iregex: datetime.date | Unset = UNSET,
    modified_isnull: bool | Unset = UNSET,
    modified_iso_week_day: float | Unset = UNSET,
    modified_iso_year: float | Unset = UNSET,
    modified_istartswith: datetime.date | Unset = UNSET,
    modified_lt: datetime.date | Unset = UNSET,
    modified_lte: datetime.date | Unset = UNSET,
    modified_month: float | Unset = UNSET,
    modified_quarter: float | Unset = UNSET,
    modified_range: list[datetime.date] | Unset = UNSET,
    modified_regex: datetime.date | Unset = UNSET,
    modified_startswith: datetime.date | Unset = UNSET,
    modified_week: float | Unset = UNSET,
    modified_week_day: float | Unset = UNSET,
    modified_year: float | Unset = UNSET,
    ob_ref: int | Unset = UNSET,
    ob_ref_in: list[int] | Unset = UNSET,
    ob_ref_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    value: str | Unset = UNSET,
    value_contains: str | Unset = UNSET,
    value_endswith: str | Unset = UNSET,
    value_gt: str | Unset = UNSET,
    value_gte: str | Unset = UNSET,
    value_icontains: str | Unset = UNSET,
    value_iendswith: str | Unset = UNSET,
    value_iexact: str | Unset = UNSET,
    value_in: list[str] | Unset = UNSET,
    value_iregex: str | Unset = UNSET,
    value_isnull: bool | Unset = UNSET,
    value_istartswith: str | Unset = UNSET,
    value_lt: str | Unset = UNSET,
    value_lte: str | Unset = UNSET,
    value_range: list[str] | Unset = UNSET,
    value_regex: str | Unset = UNSET,
    value_startswith: str | Unset = UNSET,
) -> Response[PaginatedMigrationPropertyReadList]:
    """Get a list of MigrationProperty objects.

    Args:
        id (int | Unset):
        id_contained_by (int | Unset):
        id_contains (int | Unset):
        id_endswith (int | Unset):
        id_gt (int | Unset):
        id_gte (int | Unset):
        id_icontains (int | Unset):
        id_iendswith (int | Unset):
        id_iexact (int | Unset):
        id_in (list[int] | Unset):
        id_iregex (int | Unset):
        id_isnull (bool | Unset):
        id_istartswith (int | Unset):
        id_lt (int | Unset):
        id_lte (int | Unset):
        id_range (list[int] | Unset):
        id_regex (int | Unset):
        id_startswith (int | Unset):
        key (str | Unset):
        key_contains (str | Unset):
        key_endswith (str | Unset):
        key_gt (str | Unset):
        key_gte (str | Unset):
        key_icontains (str | Unset):
        key_iendswith (str | Unset):
        key_iexact (str | Unset):
        key_in (list[str] | Unset):
        key_iregex (str | Unset):
        key_isnull (bool | Unset):
        key_istartswith (str | Unset):
        key_lt (str | Unset):
        key_lte (str | Unset):
        key_range (list[str] | Unset):
        key_regex (str | Unset):
        key_startswith (str | Unset):
        limit (int | Unset):
        modified (datetime.date | Unset):
        modified_contained_by (datetime.date | Unset):
        modified_contains (datetime.date | Unset):
        modified_day (float | Unset):
        modified_endswith (datetime.date | Unset):
        modified_gt (datetime.date | Unset):
        modified_gte (datetime.date | Unset):
        modified_icontains (datetime.date | Unset):
        modified_iendswith (datetime.date | Unset):
        modified_iexact (datetime.date | Unset):
        modified_in (list[datetime.date] | Unset):
        modified_iregex (datetime.date | Unset):
        modified_isnull (bool | Unset):
        modified_iso_week_day (float | Unset):
        modified_iso_year (float | Unset):
        modified_istartswith (datetime.date | Unset):
        modified_lt (datetime.date | Unset):
        modified_lte (datetime.date | Unset):
        modified_month (float | Unset):
        modified_quarter (float | Unset):
        modified_range (list[datetime.date] | Unset):
        modified_regex (datetime.date | Unset):
        modified_startswith (datetime.date | Unset):
        modified_week (float | Unset):
        modified_week_day (float | Unset):
        modified_year (float | Unset):
        ob_ref (int | Unset):
        ob_ref_in (list[int] | Unset):
        ob_ref_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        value (str | Unset):
        value_contains (str | Unset):
        value_endswith (str | Unset):
        value_gt (str | Unset):
        value_gte (str | Unset):
        value_icontains (str | Unset):
        value_iendswith (str | Unset):
        value_iexact (str | Unset):
        value_in (list[str] | Unset):
        value_iregex (str | Unset):
        value_isnull (bool | Unset):
        value_istartswith (str | Unset):
        value_lt (str | Unset):
        value_lte (str | Unset):
        value_range (list[str] | Unset):
        value_regex (str | Unset):
        value_startswith (str | Unset):

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
        ob_ref_in=ob_ref_in,
        ob_ref_isnull=ob_ref_isnull,
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
    id: int | Unset = UNSET,
    id_contained_by: int | Unset = UNSET,
    id_contains: int | Unset = UNSET,
    id_endswith: int | Unset = UNSET,
    id_gt: int | Unset = UNSET,
    id_gte: int | Unset = UNSET,
    id_icontains: int | Unset = UNSET,
    id_iendswith: int | Unset = UNSET,
    id_iexact: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    id_iregex: int | Unset = UNSET,
    id_isnull: bool | Unset = UNSET,
    id_istartswith: int | Unset = UNSET,
    id_lt: int | Unset = UNSET,
    id_lte: int | Unset = UNSET,
    id_range: list[int] | Unset = UNSET,
    id_regex: int | Unset = UNSET,
    id_startswith: int | Unset = UNSET,
    key: str | Unset = UNSET,
    key_contains: str | Unset = UNSET,
    key_endswith: str | Unset = UNSET,
    key_gt: str | Unset = UNSET,
    key_gte: str | Unset = UNSET,
    key_icontains: str | Unset = UNSET,
    key_iendswith: str | Unset = UNSET,
    key_iexact: str | Unset = UNSET,
    key_in: list[str] | Unset = UNSET,
    key_iregex: str | Unset = UNSET,
    key_isnull: bool | Unset = UNSET,
    key_istartswith: str | Unset = UNSET,
    key_lt: str | Unset = UNSET,
    key_lte: str | Unset = UNSET,
    key_range: list[str] | Unset = UNSET,
    key_regex: str | Unset = UNSET,
    key_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    modified: datetime.date | Unset = UNSET,
    modified_contained_by: datetime.date | Unset = UNSET,
    modified_contains: datetime.date | Unset = UNSET,
    modified_day: float | Unset = UNSET,
    modified_endswith: datetime.date | Unset = UNSET,
    modified_gt: datetime.date | Unset = UNSET,
    modified_gte: datetime.date | Unset = UNSET,
    modified_icontains: datetime.date | Unset = UNSET,
    modified_iendswith: datetime.date | Unset = UNSET,
    modified_iexact: datetime.date | Unset = UNSET,
    modified_in: list[datetime.date] | Unset = UNSET,
    modified_iregex: datetime.date | Unset = UNSET,
    modified_isnull: bool | Unset = UNSET,
    modified_iso_week_day: float | Unset = UNSET,
    modified_iso_year: float | Unset = UNSET,
    modified_istartswith: datetime.date | Unset = UNSET,
    modified_lt: datetime.date | Unset = UNSET,
    modified_lte: datetime.date | Unset = UNSET,
    modified_month: float | Unset = UNSET,
    modified_quarter: float | Unset = UNSET,
    modified_range: list[datetime.date] | Unset = UNSET,
    modified_regex: datetime.date | Unset = UNSET,
    modified_startswith: datetime.date | Unset = UNSET,
    modified_week: float | Unset = UNSET,
    modified_week_day: float | Unset = UNSET,
    modified_year: float | Unset = UNSET,
    ob_ref: int | Unset = UNSET,
    ob_ref_in: list[int] | Unset = UNSET,
    ob_ref_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    value: str | Unset = UNSET,
    value_contains: str | Unset = UNSET,
    value_endswith: str | Unset = UNSET,
    value_gt: str | Unset = UNSET,
    value_gte: str | Unset = UNSET,
    value_icontains: str | Unset = UNSET,
    value_iendswith: str | Unset = UNSET,
    value_iexact: str | Unset = UNSET,
    value_in: list[str] | Unset = UNSET,
    value_iregex: str | Unset = UNSET,
    value_isnull: bool | Unset = UNSET,
    value_istartswith: str | Unset = UNSET,
    value_lt: str | Unset = UNSET,
    value_lte: str | Unset = UNSET,
    value_range: list[str] | Unset = UNSET,
    value_regex: str | Unset = UNSET,
    value_startswith: str | Unset = UNSET,
) -> PaginatedMigrationPropertyReadList | None:
    """Get a list of MigrationProperty objects.

    Args:
        id (int | Unset):
        id_contained_by (int | Unset):
        id_contains (int | Unset):
        id_endswith (int | Unset):
        id_gt (int | Unset):
        id_gte (int | Unset):
        id_icontains (int | Unset):
        id_iendswith (int | Unset):
        id_iexact (int | Unset):
        id_in (list[int] | Unset):
        id_iregex (int | Unset):
        id_isnull (bool | Unset):
        id_istartswith (int | Unset):
        id_lt (int | Unset):
        id_lte (int | Unset):
        id_range (list[int] | Unset):
        id_regex (int | Unset):
        id_startswith (int | Unset):
        key (str | Unset):
        key_contains (str | Unset):
        key_endswith (str | Unset):
        key_gt (str | Unset):
        key_gte (str | Unset):
        key_icontains (str | Unset):
        key_iendswith (str | Unset):
        key_iexact (str | Unset):
        key_in (list[str] | Unset):
        key_iregex (str | Unset):
        key_isnull (bool | Unset):
        key_istartswith (str | Unset):
        key_lt (str | Unset):
        key_lte (str | Unset):
        key_range (list[str] | Unset):
        key_regex (str | Unset):
        key_startswith (str | Unset):
        limit (int | Unset):
        modified (datetime.date | Unset):
        modified_contained_by (datetime.date | Unset):
        modified_contains (datetime.date | Unset):
        modified_day (float | Unset):
        modified_endswith (datetime.date | Unset):
        modified_gt (datetime.date | Unset):
        modified_gte (datetime.date | Unset):
        modified_icontains (datetime.date | Unset):
        modified_iendswith (datetime.date | Unset):
        modified_iexact (datetime.date | Unset):
        modified_in (list[datetime.date] | Unset):
        modified_iregex (datetime.date | Unset):
        modified_isnull (bool | Unset):
        modified_iso_week_day (float | Unset):
        modified_iso_year (float | Unset):
        modified_istartswith (datetime.date | Unset):
        modified_lt (datetime.date | Unset):
        modified_lte (datetime.date | Unset):
        modified_month (float | Unset):
        modified_quarter (float | Unset):
        modified_range (list[datetime.date] | Unset):
        modified_regex (datetime.date | Unset):
        modified_startswith (datetime.date | Unset):
        modified_week (float | Unset):
        modified_week_day (float | Unset):
        modified_year (float | Unset):
        ob_ref (int | Unset):
        ob_ref_in (list[int] | Unset):
        ob_ref_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        value (str | Unset):
        value_contains (str | Unset):
        value_endswith (str | Unset):
        value_gt (str | Unset):
        value_gte (str | Unset):
        value_icontains (str | Unset):
        value_iendswith (str | Unset):
        value_iexact (str | Unset):
        value_in (list[str] | Unset):
        value_iregex (str | Unset):
        value_isnull (bool | Unset):
        value_istartswith (str | Unset):
        value_lt (str | Unset):
        value_lte (str | Unset):
        value_range (list[str] | Unset):
        value_regex (str | Unset):
        value_startswith (str | Unset):

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
        ob_ref_in=ob_ref_in,
        ob_ref_isnull=ob_ref_isnull,
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
    id: int | Unset = UNSET,
    id_contained_by: int | Unset = UNSET,
    id_contains: int | Unset = UNSET,
    id_endswith: int | Unset = UNSET,
    id_gt: int | Unset = UNSET,
    id_gte: int | Unset = UNSET,
    id_icontains: int | Unset = UNSET,
    id_iendswith: int | Unset = UNSET,
    id_iexact: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    id_iregex: int | Unset = UNSET,
    id_isnull: bool | Unset = UNSET,
    id_istartswith: int | Unset = UNSET,
    id_lt: int | Unset = UNSET,
    id_lte: int | Unset = UNSET,
    id_range: list[int] | Unset = UNSET,
    id_regex: int | Unset = UNSET,
    id_startswith: int | Unset = UNSET,
    key: str | Unset = UNSET,
    key_contains: str | Unset = UNSET,
    key_endswith: str | Unset = UNSET,
    key_gt: str | Unset = UNSET,
    key_gte: str | Unset = UNSET,
    key_icontains: str | Unset = UNSET,
    key_iendswith: str | Unset = UNSET,
    key_iexact: str | Unset = UNSET,
    key_in: list[str] | Unset = UNSET,
    key_iregex: str | Unset = UNSET,
    key_isnull: bool | Unset = UNSET,
    key_istartswith: str | Unset = UNSET,
    key_lt: str | Unset = UNSET,
    key_lte: str | Unset = UNSET,
    key_range: list[str] | Unset = UNSET,
    key_regex: str | Unset = UNSET,
    key_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    modified: datetime.date | Unset = UNSET,
    modified_contained_by: datetime.date | Unset = UNSET,
    modified_contains: datetime.date | Unset = UNSET,
    modified_day: float | Unset = UNSET,
    modified_endswith: datetime.date | Unset = UNSET,
    modified_gt: datetime.date | Unset = UNSET,
    modified_gte: datetime.date | Unset = UNSET,
    modified_icontains: datetime.date | Unset = UNSET,
    modified_iendswith: datetime.date | Unset = UNSET,
    modified_iexact: datetime.date | Unset = UNSET,
    modified_in: list[datetime.date] | Unset = UNSET,
    modified_iregex: datetime.date | Unset = UNSET,
    modified_isnull: bool | Unset = UNSET,
    modified_iso_week_day: float | Unset = UNSET,
    modified_iso_year: float | Unset = UNSET,
    modified_istartswith: datetime.date | Unset = UNSET,
    modified_lt: datetime.date | Unset = UNSET,
    modified_lte: datetime.date | Unset = UNSET,
    modified_month: float | Unset = UNSET,
    modified_quarter: float | Unset = UNSET,
    modified_range: list[datetime.date] | Unset = UNSET,
    modified_regex: datetime.date | Unset = UNSET,
    modified_startswith: datetime.date | Unset = UNSET,
    modified_week: float | Unset = UNSET,
    modified_week_day: float | Unset = UNSET,
    modified_year: float | Unset = UNSET,
    ob_ref: int | Unset = UNSET,
    ob_ref_in: list[int] | Unset = UNSET,
    ob_ref_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    value: str | Unset = UNSET,
    value_contains: str | Unset = UNSET,
    value_endswith: str | Unset = UNSET,
    value_gt: str | Unset = UNSET,
    value_gte: str | Unset = UNSET,
    value_icontains: str | Unset = UNSET,
    value_iendswith: str | Unset = UNSET,
    value_iexact: str | Unset = UNSET,
    value_in: list[str] | Unset = UNSET,
    value_iregex: str | Unset = UNSET,
    value_isnull: bool | Unset = UNSET,
    value_istartswith: str | Unset = UNSET,
    value_lt: str | Unset = UNSET,
    value_lte: str | Unset = UNSET,
    value_range: list[str] | Unset = UNSET,
    value_regex: str | Unset = UNSET,
    value_startswith: str | Unset = UNSET,
) -> Response[PaginatedMigrationPropertyReadList]:
    """Get a list of MigrationProperty objects.

    Args:
        id (int | Unset):
        id_contained_by (int | Unset):
        id_contains (int | Unset):
        id_endswith (int | Unset):
        id_gt (int | Unset):
        id_gte (int | Unset):
        id_icontains (int | Unset):
        id_iendswith (int | Unset):
        id_iexact (int | Unset):
        id_in (list[int] | Unset):
        id_iregex (int | Unset):
        id_isnull (bool | Unset):
        id_istartswith (int | Unset):
        id_lt (int | Unset):
        id_lte (int | Unset):
        id_range (list[int] | Unset):
        id_regex (int | Unset):
        id_startswith (int | Unset):
        key (str | Unset):
        key_contains (str | Unset):
        key_endswith (str | Unset):
        key_gt (str | Unset):
        key_gte (str | Unset):
        key_icontains (str | Unset):
        key_iendswith (str | Unset):
        key_iexact (str | Unset):
        key_in (list[str] | Unset):
        key_iregex (str | Unset):
        key_isnull (bool | Unset):
        key_istartswith (str | Unset):
        key_lt (str | Unset):
        key_lte (str | Unset):
        key_range (list[str] | Unset):
        key_regex (str | Unset):
        key_startswith (str | Unset):
        limit (int | Unset):
        modified (datetime.date | Unset):
        modified_contained_by (datetime.date | Unset):
        modified_contains (datetime.date | Unset):
        modified_day (float | Unset):
        modified_endswith (datetime.date | Unset):
        modified_gt (datetime.date | Unset):
        modified_gte (datetime.date | Unset):
        modified_icontains (datetime.date | Unset):
        modified_iendswith (datetime.date | Unset):
        modified_iexact (datetime.date | Unset):
        modified_in (list[datetime.date] | Unset):
        modified_iregex (datetime.date | Unset):
        modified_isnull (bool | Unset):
        modified_iso_week_day (float | Unset):
        modified_iso_year (float | Unset):
        modified_istartswith (datetime.date | Unset):
        modified_lt (datetime.date | Unset):
        modified_lte (datetime.date | Unset):
        modified_month (float | Unset):
        modified_quarter (float | Unset):
        modified_range (list[datetime.date] | Unset):
        modified_regex (datetime.date | Unset):
        modified_startswith (datetime.date | Unset):
        modified_week (float | Unset):
        modified_week_day (float | Unset):
        modified_year (float | Unset):
        ob_ref (int | Unset):
        ob_ref_in (list[int] | Unset):
        ob_ref_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        value (str | Unset):
        value_contains (str | Unset):
        value_endswith (str | Unset):
        value_gt (str | Unset):
        value_gte (str | Unset):
        value_icontains (str | Unset):
        value_iendswith (str | Unset):
        value_iexact (str | Unset):
        value_in (list[str] | Unset):
        value_iregex (str | Unset):
        value_isnull (bool | Unset):
        value_istartswith (str | Unset):
        value_lt (str | Unset):
        value_lte (str | Unset):
        value_range (list[str] | Unset):
        value_regex (str | Unset):
        value_startswith (str | Unset):

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
        ob_ref_in=ob_ref_in,
        ob_ref_isnull=ob_ref_isnull,
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
    id: int | Unset = UNSET,
    id_contained_by: int | Unset = UNSET,
    id_contains: int | Unset = UNSET,
    id_endswith: int | Unset = UNSET,
    id_gt: int | Unset = UNSET,
    id_gte: int | Unset = UNSET,
    id_icontains: int | Unset = UNSET,
    id_iendswith: int | Unset = UNSET,
    id_iexact: int | Unset = UNSET,
    id_in: list[int] | Unset = UNSET,
    id_iregex: int | Unset = UNSET,
    id_isnull: bool | Unset = UNSET,
    id_istartswith: int | Unset = UNSET,
    id_lt: int | Unset = UNSET,
    id_lte: int | Unset = UNSET,
    id_range: list[int] | Unset = UNSET,
    id_regex: int | Unset = UNSET,
    id_startswith: int | Unset = UNSET,
    key: str | Unset = UNSET,
    key_contains: str | Unset = UNSET,
    key_endswith: str | Unset = UNSET,
    key_gt: str | Unset = UNSET,
    key_gte: str | Unset = UNSET,
    key_icontains: str | Unset = UNSET,
    key_iendswith: str | Unset = UNSET,
    key_iexact: str | Unset = UNSET,
    key_in: list[str] | Unset = UNSET,
    key_iregex: str | Unset = UNSET,
    key_isnull: bool | Unset = UNSET,
    key_istartswith: str | Unset = UNSET,
    key_lt: str | Unset = UNSET,
    key_lte: str | Unset = UNSET,
    key_range: list[str] | Unset = UNSET,
    key_regex: str | Unset = UNSET,
    key_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    modified: datetime.date | Unset = UNSET,
    modified_contained_by: datetime.date | Unset = UNSET,
    modified_contains: datetime.date | Unset = UNSET,
    modified_day: float | Unset = UNSET,
    modified_endswith: datetime.date | Unset = UNSET,
    modified_gt: datetime.date | Unset = UNSET,
    modified_gte: datetime.date | Unset = UNSET,
    modified_icontains: datetime.date | Unset = UNSET,
    modified_iendswith: datetime.date | Unset = UNSET,
    modified_iexact: datetime.date | Unset = UNSET,
    modified_in: list[datetime.date] | Unset = UNSET,
    modified_iregex: datetime.date | Unset = UNSET,
    modified_isnull: bool | Unset = UNSET,
    modified_iso_week_day: float | Unset = UNSET,
    modified_iso_year: float | Unset = UNSET,
    modified_istartswith: datetime.date | Unset = UNSET,
    modified_lt: datetime.date | Unset = UNSET,
    modified_lte: datetime.date | Unset = UNSET,
    modified_month: float | Unset = UNSET,
    modified_quarter: float | Unset = UNSET,
    modified_range: list[datetime.date] | Unset = UNSET,
    modified_regex: datetime.date | Unset = UNSET,
    modified_startswith: datetime.date | Unset = UNSET,
    modified_week: float | Unset = UNSET,
    modified_week_day: float | Unset = UNSET,
    modified_year: float | Unset = UNSET,
    ob_ref: int | Unset = UNSET,
    ob_ref_in: list[int] | Unset = UNSET,
    ob_ref_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    value: str | Unset = UNSET,
    value_contains: str | Unset = UNSET,
    value_endswith: str | Unset = UNSET,
    value_gt: str | Unset = UNSET,
    value_gte: str | Unset = UNSET,
    value_icontains: str | Unset = UNSET,
    value_iendswith: str | Unset = UNSET,
    value_iexact: str | Unset = UNSET,
    value_in: list[str] | Unset = UNSET,
    value_iregex: str | Unset = UNSET,
    value_isnull: bool | Unset = UNSET,
    value_istartswith: str | Unset = UNSET,
    value_lt: str | Unset = UNSET,
    value_lte: str | Unset = UNSET,
    value_range: list[str] | Unset = UNSET,
    value_regex: str | Unset = UNSET,
    value_startswith: str | Unset = UNSET,
) -> PaginatedMigrationPropertyReadList | None:
    """Get a list of MigrationProperty objects.

    Args:
        id (int | Unset):
        id_contained_by (int | Unset):
        id_contains (int | Unset):
        id_endswith (int | Unset):
        id_gt (int | Unset):
        id_gte (int | Unset):
        id_icontains (int | Unset):
        id_iendswith (int | Unset):
        id_iexact (int | Unset):
        id_in (list[int] | Unset):
        id_iregex (int | Unset):
        id_isnull (bool | Unset):
        id_istartswith (int | Unset):
        id_lt (int | Unset):
        id_lte (int | Unset):
        id_range (list[int] | Unset):
        id_regex (int | Unset):
        id_startswith (int | Unset):
        key (str | Unset):
        key_contains (str | Unset):
        key_endswith (str | Unset):
        key_gt (str | Unset):
        key_gte (str | Unset):
        key_icontains (str | Unset):
        key_iendswith (str | Unset):
        key_iexact (str | Unset):
        key_in (list[str] | Unset):
        key_iregex (str | Unset):
        key_isnull (bool | Unset):
        key_istartswith (str | Unset):
        key_lt (str | Unset):
        key_lte (str | Unset):
        key_range (list[str] | Unset):
        key_regex (str | Unset):
        key_startswith (str | Unset):
        limit (int | Unset):
        modified (datetime.date | Unset):
        modified_contained_by (datetime.date | Unset):
        modified_contains (datetime.date | Unset):
        modified_day (float | Unset):
        modified_endswith (datetime.date | Unset):
        modified_gt (datetime.date | Unset):
        modified_gte (datetime.date | Unset):
        modified_icontains (datetime.date | Unset):
        modified_iendswith (datetime.date | Unset):
        modified_iexact (datetime.date | Unset):
        modified_in (list[datetime.date] | Unset):
        modified_iregex (datetime.date | Unset):
        modified_isnull (bool | Unset):
        modified_iso_week_day (float | Unset):
        modified_iso_year (float | Unset):
        modified_istartswith (datetime.date | Unset):
        modified_lt (datetime.date | Unset):
        modified_lte (datetime.date | Unset):
        modified_month (float | Unset):
        modified_quarter (float | Unset):
        modified_range (list[datetime.date] | Unset):
        modified_regex (datetime.date | Unset):
        modified_startswith (datetime.date | Unset):
        modified_week (float | Unset):
        modified_week_day (float | Unset):
        modified_year (float | Unset):
        ob_ref (int | Unset):
        ob_ref_in (list[int] | Unset):
        ob_ref_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        value (str | Unset):
        value_contains (str | Unset):
        value_endswith (str | Unset):
        value_gt (str | Unset):
        value_gte (str | Unset):
        value_icontains (str | Unset):
        value_iendswith (str | Unset):
        value_iexact (str | Unset):
        value_in (list[str] | Unset):
        value_iregex (str | Unset):
        value_isnull (bool | Unset):
        value_istartswith (str | Unset):
        value_lt (str | Unset):
        value_lte (str | Unset):
        value_range (list[str] | Unset):
        value_regex (str | Unset):
        value_startswith (str | Unset):

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
            ob_ref_in=ob_ref_in,
            ob_ref_isnull=ob_ref_isnull,
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
