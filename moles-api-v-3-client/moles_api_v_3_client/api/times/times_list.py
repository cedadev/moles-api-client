import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_time_period_list import PaginatedTimePeriodList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    end_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    end_time_contains: Union[Unset, datetime.datetime] = UNSET,
    end_time_date: Union[Unset, datetime.date] = UNSET,
    end_time_day: Union[Unset, float] = UNSET,
    end_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_gt: Union[Unset, datetime.datetime] = UNSET,
    end_time_gte: Union[Unset, datetime.datetime] = UNSET,
    end_time_hour: Union[Unset, float] = UNSET,
    end_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    end_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    end_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    end_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    end_time_isnull: Union[Unset, bool] = UNSET,
    end_time_iso_week_day: Union[Unset, float] = UNSET,
    end_time_iso_year: Union[Unset, float] = UNSET,
    end_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_lt: Union[Unset, datetime.datetime] = UNSET,
    end_time_lte: Union[Unset, datetime.datetime] = UNSET,
    end_time_minute: Union[Unset, float] = UNSET,
    end_time_month: Union[Unset, float] = UNSET,
    end_time_quarter: Union[Unset, float] = UNSET,
    end_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    end_time_regex: Union[Unset, datetime.datetime] = UNSET,
    end_time_second: Union[Unset, float] = UNSET,
    end_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_time: Union[Unset, str] = UNSET,
    end_time_week: Union[Unset, float] = UNSET,
    end_time_week_day: Union[Unset, float] = UNSET,
    end_time_year: Union[Unset, float] = UNSET,
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
    start_time: Union[Unset, datetime.datetime] = UNSET,
    start_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    start_time_contains: Union[Unset, datetime.datetime] = UNSET,
    start_time_date: Union[Unset, datetime.date] = UNSET,
    start_time_day: Union[Unset, float] = UNSET,
    start_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_gt: Union[Unset, datetime.datetime] = UNSET,
    start_time_gte: Union[Unset, datetime.datetime] = UNSET,
    start_time_hour: Union[Unset, float] = UNSET,
    start_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    start_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    start_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    start_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    start_time_isnull: Union[Unset, bool] = UNSET,
    start_time_iso_week_day: Union[Unset, float] = UNSET,
    start_time_iso_year: Union[Unset, float] = UNSET,
    start_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_lt: Union[Unset, datetime.datetime] = UNSET,
    start_time_lte: Union[Unset, datetime.datetime] = UNSET,
    start_time_minute: Union[Unset, float] = UNSET,
    start_time_month: Union[Unset, float] = UNSET,
    start_time_quarter: Union[Unset, float] = UNSET,
    start_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    start_time_regex: Union[Unset, datetime.datetime] = UNSET,
    start_time_second: Union[Unset, float] = UNSET,
    start_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_time: Union[Unset, str] = UNSET,
    start_time_week: Union[Unset, float] = UNSET,
    start_time_week_day: Union[Unset, float] = UNSET,
    start_time_year: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    json_end_time_contained_by: Union[Unset, str] = UNSET
    if not isinstance(end_time_contained_by, Unset):
        json_end_time_contained_by = end_time_contained_by.isoformat()
    params["endTime__contained_by"] = json_end_time_contained_by

    json_end_time_contains: Union[Unset, str] = UNSET
    if not isinstance(end_time_contains, Unset):
        json_end_time_contains = end_time_contains.isoformat()
    params["endTime__contains"] = json_end_time_contains

    json_end_time_date: Union[Unset, str] = UNSET
    if not isinstance(end_time_date, Unset):
        json_end_time_date = end_time_date.isoformat()
    params["endTime__date"] = json_end_time_date

    params["endTime__day"] = end_time_day

    json_end_time_endswith: Union[Unset, str] = UNSET
    if not isinstance(end_time_endswith, Unset):
        json_end_time_endswith = end_time_endswith.isoformat()
    params["endTime__endswith"] = json_end_time_endswith

    json_end_time_gt: Union[Unset, str] = UNSET
    if not isinstance(end_time_gt, Unset):
        json_end_time_gt = end_time_gt.isoformat()
    params["endTime__gt"] = json_end_time_gt

    json_end_time_gte: Union[Unset, str] = UNSET
    if not isinstance(end_time_gte, Unset):
        json_end_time_gte = end_time_gte.isoformat()
    params["endTime__gte"] = json_end_time_gte

    params["endTime__hour"] = end_time_hour

    json_end_time_icontains: Union[Unset, str] = UNSET
    if not isinstance(end_time_icontains, Unset):
        json_end_time_icontains = end_time_icontains.isoformat()
    params["endTime__icontains"] = json_end_time_icontains

    json_end_time_iendswith: Union[Unset, str] = UNSET
    if not isinstance(end_time_iendswith, Unset):
        json_end_time_iendswith = end_time_iendswith.isoformat()
    params["endTime__iendswith"] = json_end_time_iendswith

    json_end_time_iexact: Union[Unset, str] = UNSET
    if not isinstance(end_time_iexact, Unset):
        json_end_time_iexact = end_time_iexact.isoformat()
    params["endTime__iexact"] = json_end_time_iexact

    json_end_time_in: Union[Unset, list[str]] = UNSET
    if not isinstance(end_time_in, Unset):
        json_end_time_in = []
        for end_time_in_item_data in end_time_in:
            end_time_in_item = end_time_in_item_data.isoformat()
            json_end_time_in.append(end_time_in_item)

    params["endTime__in"] = json_end_time_in

    json_end_time_iregex: Union[Unset, str] = UNSET
    if not isinstance(end_time_iregex, Unset):
        json_end_time_iregex = end_time_iregex.isoformat()
    params["endTime__iregex"] = json_end_time_iregex

    params["endTime__isnull"] = end_time_isnull

    params["endTime__iso_week_day"] = end_time_iso_week_day

    params["endTime__iso_year"] = end_time_iso_year

    json_end_time_istartswith: Union[Unset, str] = UNSET
    if not isinstance(end_time_istartswith, Unset):
        json_end_time_istartswith = end_time_istartswith.isoformat()
    params["endTime__istartswith"] = json_end_time_istartswith

    json_end_time_lt: Union[Unset, str] = UNSET
    if not isinstance(end_time_lt, Unset):
        json_end_time_lt = end_time_lt.isoformat()
    params["endTime__lt"] = json_end_time_lt

    json_end_time_lte: Union[Unset, str] = UNSET
    if not isinstance(end_time_lte, Unset):
        json_end_time_lte = end_time_lte.isoformat()
    params["endTime__lte"] = json_end_time_lte

    params["endTime__minute"] = end_time_minute

    params["endTime__month"] = end_time_month

    params["endTime__quarter"] = end_time_quarter

    json_end_time_range: Union[Unset, list[str]] = UNSET
    if not isinstance(end_time_range, Unset):
        json_end_time_range = []
        for end_time_range_item_data in end_time_range:
            end_time_range_item = end_time_range_item_data.isoformat()
            json_end_time_range.append(end_time_range_item)

    params["endTime__range"] = json_end_time_range

    json_end_time_regex: Union[Unset, str] = UNSET
    if not isinstance(end_time_regex, Unset):
        json_end_time_regex = end_time_regex.isoformat()
    params["endTime__regex"] = json_end_time_regex

    params["endTime__second"] = end_time_second

    json_end_time_startswith: Union[Unset, str] = UNSET
    if not isinstance(end_time_startswith, Unset):
        json_end_time_startswith = end_time_startswith.isoformat()
    params["endTime__startswith"] = json_end_time_startswith

    params["endTime__time"] = end_time_time

    params["endTime__week"] = end_time_week

    params["endTime__week_day"] = end_time_week_day

    params["endTime__year"] = end_time_year

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

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_start_time_contained_by: Union[Unset, str] = UNSET
    if not isinstance(start_time_contained_by, Unset):
        json_start_time_contained_by = start_time_contained_by.isoformat()
    params["startTime__contained_by"] = json_start_time_contained_by

    json_start_time_contains: Union[Unset, str] = UNSET
    if not isinstance(start_time_contains, Unset):
        json_start_time_contains = start_time_contains.isoformat()
    params["startTime__contains"] = json_start_time_contains

    json_start_time_date: Union[Unset, str] = UNSET
    if not isinstance(start_time_date, Unset):
        json_start_time_date = start_time_date.isoformat()
    params["startTime__date"] = json_start_time_date

    params["startTime__day"] = start_time_day

    json_start_time_endswith: Union[Unset, str] = UNSET
    if not isinstance(start_time_endswith, Unset):
        json_start_time_endswith = start_time_endswith.isoformat()
    params["startTime__endswith"] = json_start_time_endswith

    json_start_time_gt: Union[Unset, str] = UNSET
    if not isinstance(start_time_gt, Unset):
        json_start_time_gt = start_time_gt.isoformat()
    params["startTime__gt"] = json_start_time_gt

    json_start_time_gte: Union[Unset, str] = UNSET
    if not isinstance(start_time_gte, Unset):
        json_start_time_gte = start_time_gte.isoformat()
    params["startTime__gte"] = json_start_time_gte

    params["startTime__hour"] = start_time_hour

    json_start_time_icontains: Union[Unset, str] = UNSET
    if not isinstance(start_time_icontains, Unset):
        json_start_time_icontains = start_time_icontains.isoformat()
    params["startTime__icontains"] = json_start_time_icontains

    json_start_time_iendswith: Union[Unset, str] = UNSET
    if not isinstance(start_time_iendswith, Unset):
        json_start_time_iendswith = start_time_iendswith.isoformat()
    params["startTime__iendswith"] = json_start_time_iendswith

    json_start_time_iexact: Union[Unset, str] = UNSET
    if not isinstance(start_time_iexact, Unset):
        json_start_time_iexact = start_time_iexact.isoformat()
    params["startTime__iexact"] = json_start_time_iexact

    json_start_time_in: Union[Unset, list[str]] = UNSET
    if not isinstance(start_time_in, Unset):
        json_start_time_in = []
        for start_time_in_item_data in start_time_in:
            start_time_in_item = start_time_in_item_data.isoformat()
            json_start_time_in.append(start_time_in_item)

    params["startTime__in"] = json_start_time_in

    json_start_time_iregex: Union[Unset, str] = UNSET
    if not isinstance(start_time_iregex, Unset):
        json_start_time_iregex = start_time_iregex.isoformat()
    params["startTime__iregex"] = json_start_time_iregex

    params["startTime__isnull"] = start_time_isnull

    params["startTime__iso_week_day"] = start_time_iso_week_day

    params["startTime__iso_year"] = start_time_iso_year

    json_start_time_istartswith: Union[Unset, str] = UNSET
    if not isinstance(start_time_istartswith, Unset):
        json_start_time_istartswith = start_time_istartswith.isoformat()
    params["startTime__istartswith"] = json_start_time_istartswith

    json_start_time_lt: Union[Unset, str] = UNSET
    if not isinstance(start_time_lt, Unset):
        json_start_time_lt = start_time_lt.isoformat()
    params["startTime__lt"] = json_start_time_lt

    json_start_time_lte: Union[Unset, str] = UNSET
    if not isinstance(start_time_lte, Unset):
        json_start_time_lte = start_time_lte.isoformat()
    params["startTime__lte"] = json_start_time_lte

    params["startTime__minute"] = start_time_minute

    params["startTime__month"] = start_time_month

    params["startTime__quarter"] = start_time_quarter

    json_start_time_range: Union[Unset, list[str]] = UNSET
    if not isinstance(start_time_range, Unset):
        json_start_time_range = []
        for start_time_range_item_data in start_time_range:
            start_time_range_item = start_time_range_item_data.isoformat()
            json_start_time_range.append(start_time_range_item)

    params["startTime__range"] = json_start_time_range

    json_start_time_regex: Union[Unset, str] = UNSET
    if not isinstance(start_time_regex, Unset):
        json_start_time_regex = start_time_regex.isoformat()
    params["startTime__regex"] = json_start_time_regex

    params["startTime__second"] = start_time_second

    json_start_time_startswith: Union[Unset, str] = UNSET
    if not isinstance(start_time_startswith, Unset):
        json_start_time_startswith = start_time_startswith.isoformat()
    params["startTime__startswith"] = json_start_time_startswith

    params["startTime__time"] = start_time_time

    params["startTime__week"] = start_time_week

    params["startTime__week_day"] = start_time_week_day

    params["startTime__year"] = start_time_year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/times/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedTimePeriodList]:
    if response.status_code == 200:
        response_200 = PaginatedTimePeriodList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedTimePeriodList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    end_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    end_time_contains: Union[Unset, datetime.datetime] = UNSET,
    end_time_date: Union[Unset, datetime.date] = UNSET,
    end_time_day: Union[Unset, float] = UNSET,
    end_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_gt: Union[Unset, datetime.datetime] = UNSET,
    end_time_gte: Union[Unset, datetime.datetime] = UNSET,
    end_time_hour: Union[Unset, float] = UNSET,
    end_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    end_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    end_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    end_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    end_time_isnull: Union[Unset, bool] = UNSET,
    end_time_iso_week_day: Union[Unset, float] = UNSET,
    end_time_iso_year: Union[Unset, float] = UNSET,
    end_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_lt: Union[Unset, datetime.datetime] = UNSET,
    end_time_lte: Union[Unset, datetime.datetime] = UNSET,
    end_time_minute: Union[Unset, float] = UNSET,
    end_time_month: Union[Unset, float] = UNSET,
    end_time_quarter: Union[Unset, float] = UNSET,
    end_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    end_time_regex: Union[Unset, datetime.datetime] = UNSET,
    end_time_second: Union[Unset, float] = UNSET,
    end_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_time: Union[Unset, str] = UNSET,
    end_time_week: Union[Unset, float] = UNSET,
    end_time_week_day: Union[Unset, float] = UNSET,
    end_time_year: Union[Unset, float] = UNSET,
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
    start_time: Union[Unset, datetime.datetime] = UNSET,
    start_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    start_time_contains: Union[Unset, datetime.datetime] = UNSET,
    start_time_date: Union[Unset, datetime.date] = UNSET,
    start_time_day: Union[Unset, float] = UNSET,
    start_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_gt: Union[Unset, datetime.datetime] = UNSET,
    start_time_gte: Union[Unset, datetime.datetime] = UNSET,
    start_time_hour: Union[Unset, float] = UNSET,
    start_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    start_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    start_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    start_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    start_time_isnull: Union[Unset, bool] = UNSET,
    start_time_iso_week_day: Union[Unset, float] = UNSET,
    start_time_iso_year: Union[Unset, float] = UNSET,
    start_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_lt: Union[Unset, datetime.datetime] = UNSET,
    start_time_lte: Union[Unset, datetime.datetime] = UNSET,
    start_time_minute: Union[Unset, float] = UNSET,
    start_time_month: Union[Unset, float] = UNSET,
    start_time_quarter: Union[Unset, float] = UNSET,
    start_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    start_time_regex: Union[Unset, datetime.datetime] = UNSET,
    start_time_second: Union[Unset, float] = UNSET,
    start_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_time: Union[Unset, str] = UNSET,
    start_time_week: Union[Unset, float] = UNSET,
    start_time_week_day: Union[Unset, float] = UNSET,
    start_time_year: Union[Unset, float] = UNSET,
) -> Response[PaginatedTimePeriodList]:
    """Get a list of TimePeriod objects. TimePeriods have a 1:1 use with many types of principal record
    types.

    Args:
        end_time (Union[Unset, datetime.datetime]):
        end_time_contained_by (Union[Unset, datetime.datetime]):
        end_time_contains (Union[Unset, datetime.datetime]):
        end_time_date (Union[Unset, datetime.date]):
        end_time_day (Union[Unset, float]):
        end_time_endswith (Union[Unset, datetime.datetime]):
        end_time_gt (Union[Unset, datetime.datetime]):
        end_time_gte (Union[Unset, datetime.datetime]):
        end_time_hour (Union[Unset, float]):
        end_time_icontains (Union[Unset, datetime.datetime]):
        end_time_iendswith (Union[Unset, datetime.datetime]):
        end_time_iexact (Union[Unset, datetime.datetime]):
        end_time_in (Union[Unset, list[datetime.datetime]]):
        end_time_iregex (Union[Unset, datetime.datetime]):
        end_time_isnull (Union[Unset, bool]):
        end_time_iso_week_day (Union[Unset, float]):
        end_time_iso_year (Union[Unset, float]):
        end_time_istartswith (Union[Unset, datetime.datetime]):
        end_time_lt (Union[Unset, datetime.datetime]):
        end_time_lte (Union[Unset, datetime.datetime]):
        end_time_minute (Union[Unset, float]):
        end_time_month (Union[Unset, float]):
        end_time_quarter (Union[Unset, float]):
        end_time_range (Union[Unset, list[datetime.datetime]]):
        end_time_regex (Union[Unset, datetime.datetime]):
        end_time_second (Union[Unset, float]):
        end_time_startswith (Union[Unset, datetime.datetime]):
        end_time_time (Union[Unset, str]):
        end_time_week (Union[Unset, float]):
        end_time_week_day (Union[Unset, float]):
        end_time_year (Union[Unset, float]):
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
        start_time (Union[Unset, datetime.datetime]):
        start_time_contained_by (Union[Unset, datetime.datetime]):
        start_time_contains (Union[Unset, datetime.datetime]):
        start_time_date (Union[Unset, datetime.date]):
        start_time_day (Union[Unset, float]):
        start_time_endswith (Union[Unset, datetime.datetime]):
        start_time_gt (Union[Unset, datetime.datetime]):
        start_time_gte (Union[Unset, datetime.datetime]):
        start_time_hour (Union[Unset, float]):
        start_time_icontains (Union[Unset, datetime.datetime]):
        start_time_iendswith (Union[Unset, datetime.datetime]):
        start_time_iexact (Union[Unset, datetime.datetime]):
        start_time_in (Union[Unset, list[datetime.datetime]]):
        start_time_iregex (Union[Unset, datetime.datetime]):
        start_time_isnull (Union[Unset, bool]):
        start_time_iso_week_day (Union[Unset, float]):
        start_time_iso_year (Union[Unset, float]):
        start_time_istartswith (Union[Unset, datetime.datetime]):
        start_time_lt (Union[Unset, datetime.datetime]):
        start_time_lte (Union[Unset, datetime.datetime]):
        start_time_minute (Union[Unset, float]):
        start_time_month (Union[Unset, float]):
        start_time_quarter (Union[Unset, float]):
        start_time_range (Union[Unset, list[datetime.datetime]]):
        start_time_regex (Union[Unset, datetime.datetime]):
        start_time_second (Union[Unset, float]):
        start_time_startswith (Union[Unset, datetime.datetime]):
        start_time_time (Union[Unset, str]):
        start_time_week (Union[Unset, float]):
        start_time_week_day (Union[Unset, float]):
        start_time_year (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTimePeriodList]
    """

    kwargs = _get_kwargs(
        end_time=end_time,
        end_time_contained_by=end_time_contained_by,
        end_time_contains=end_time_contains,
        end_time_date=end_time_date,
        end_time_day=end_time_day,
        end_time_endswith=end_time_endswith,
        end_time_gt=end_time_gt,
        end_time_gte=end_time_gte,
        end_time_hour=end_time_hour,
        end_time_icontains=end_time_icontains,
        end_time_iendswith=end_time_iendswith,
        end_time_iexact=end_time_iexact,
        end_time_in=end_time_in,
        end_time_iregex=end_time_iregex,
        end_time_isnull=end_time_isnull,
        end_time_iso_week_day=end_time_iso_week_day,
        end_time_iso_year=end_time_iso_year,
        end_time_istartswith=end_time_istartswith,
        end_time_lt=end_time_lt,
        end_time_lte=end_time_lte,
        end_time_minute=end_time_minute,
        end_time_month=end_time_month,
        end_time_quarter=end_time_quarter,
        end_time_range=end_time_range,
        end_time_regex=end_time_regex,
        end_time_second=end_time_second,
        end_time_startswith=end_time_startswith,
        end_time_time=end_time_time,
        end_time_week=end_time_week,
        end_time_week_day=end_time_week_day,
        end_time_year=end_time_year,
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
        start_time=start_time,
        start_time_contained_by=start_time_contained_by,
        start_time_contains=start_time_contains,
        start_time_date=start_time_date,
        start_time_day=start_time_day,
        start_time_endswith=start_time_endswith,
        start_time_gt=start_time_gt,
        start_time_gte=start_time_gte,
        start_time_hour=start_time_hour,
        start_time_icontains=start_time_icontains,
        start_time_iendswith=start_time_iendswith,
        start_time_iexact=start_time_iexact,
        start_time_in=start_time_in,
        start_time_iregex=start_time_iregex,
        start_time_isnull=start_time_isnull,
        start_time_iso_week_day=start_time_iso_week_day,
        start_time_iso_year=start_time_iso_year,
        start_time_istartswith=start_time_istartswith,
        start_time_lt=start_time_lt,
        start_time_lte=start_time_lte,
        start_time_minute=start_time_minute,
        start_time_month=start_time_month,
        start_time_quarter=start_time_quarter,
        start_time_range=start_time_range,
        start_time_regex=start_time_regex,
        start_time_second=start_time_second,
        start_time_startswith=start_time_startswith,
        start_time_time=start_time_time,
        start_time_week=start_time_week,
        start_time_week_day=start_time_week_day,
        start_time_year=start_time_year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    end_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    end_time_contains: Union[Unset, datetime.datetime] = UNSET,
    end_time_date: Union[Unset, datetime.date] = UNSET,
    end_time_day: Union[Unset, float] = UNSET,
    end_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_gt: Union[Unset, datetime.datetime] = UNSET,
    end_time_gte: Union[Unset, datetime.datetime] = UNSET,
    end_time_hour: Union[Unset, float] = UNSET,
    end_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    end_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    end_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    end_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    end_time_isnull: Union[Unset, bool] = UNSET,
    end_time_iso_week_day: Union[Unset, float] = UNSET,
    end_time_iso_year: Union[Unset, float] = UNSET,
    end_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_lt: Union[Unset, datetime.datetime] = UNSET,
    end_time_lte: Union[Unset, datetime.datetime] = UNSET,
    end_time_minute: Union[Unset, float] = UNSET,
    end_time_month: Union[Unset, float] = UNSET,
    end_time_quarter: Union[Unset, float] = UNSET,
    end_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    end_time_regex: Union[Unset, datetime.datetime] = UNSET,
    end_time_second: Union[Unset, float] = UNSET,
    end_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_time: Union[Unset, str] = UNSET,
    end_time_week: Union[Unset, float] = UNSET,
    end_time_week_day: Union[Unset, float] = UNSET,
    end_time_year: Union[Unset, float] = UNSET,
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
    start_time: Union[Unset, datetime.datetime] = UNSET,
    start_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    start_time_contains: Union[Unset, datetime.datetime] = UNSET,
    start_time_date: Union[Unset, datetime.date] = UNSET,
    start_time_day: Union[Unset, float] = UNSET,
    start_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_gt: Union[Unset, datetime.datetime] = UNSET,
    start_time_gte: Union[Unset, datetime.datetime] = UNSET,
    start_time_hour: Union[Unset, float] = UNSET,
    start_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    start_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    start_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    start_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    start_time_isnull: Union[Unset, bool] = UNSET,
    start_time_iso_week_day: Union[Unset, float] = UNSET,
    start_time_iso_year: Union[Unset, float] = UNSET,
    start_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_lt: Union[Unset, datetime.datetime] = UNSET,
    start_time_lte: Union[Unset, datetime.datetime] = UNSET,
    start_time_minute: Union[Unset, float] = UNSET,
    start_time_month: Union[Unset, float] = UNSET,
    start_time_quarter: Union[Unset, float] = UNSET,
    start_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    start_time_regex: Union[Unset, datetime.datetime] = UNSET,
    start_time_second: Union[Unset, float] = UNSET,
    start_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_time: Union[Unset, str] = UNSET,
    start_time_week: Union[Unset, float] = UNSET,
    start_time_week_day: Union[Unset, float] = UNSET,
    start_time_year: Union[Unset, float] = UNSET,
) -> Optional[PaginatedTimePeriodList]:
    """Get a list of TimePeriod objects. TimePeriods have a 1:1 use with many types of principal record
    types.

    Args:
        end_time (Union[Unset, datetime.datetime]):
        end_time_contained_by (Union[Unset, datetime.datetime]):
        end_time_contains (Union[Unset, datetime.datetime]):
        end_time_date (Union[Unset, datetime.date]):
        end_time_day (Union[Unset, float]):
        end_time_endswith (Union[Unset, datetime.datetime]):
        end_time_gt (Union[Unset, datetime.datetime]):
        end_time_gte (Union[Unset, datetime.datetime]):
        end_time_hour (Union[Unset, float]):
        end_time_icontains (Union[Unset, datetime.datetime]):
        end_time_iendswith (Union[Unset, datetime.datetime]):
        end_time_iexact (Union[Unset, datetime.datetime]):
        end_time_in (Union[Unset, list[datetime.datetime]]):
        end_time_iregex (Union[Unset, datetime.datetime]):
        end_time_isnull (Union[Unset, bool]):
        end_time_iso_week_day (Union[Unset, float]):
        end_time_iso_year (Union[Unset, float]):
        end_time_istartswith (Union[Unset, datetime.datetime]):
        end_time_lt (Union[Unset, datetime.datetime]):
        end_time_lte (Union[Unset, datetime.datetime]):
        end_time_minute (Union[Unset, float]):
        end_time_month (Union[Unset, float]):
        end_time_quarter (Union[Unset, float]):
        end_time_range (Union[Unset, list[datetime.datetime]]):
        end_time_regex (Union[Unset, datetime.datetime]):
        end_time_second (Union[Unset, float]):
        end_time_startswith (Union[Unset, datetime.datetime]):
        end_time_time (Union[Unset, str]):
        end_time_week (Union[Unset, float]):
        end_time_week_day (Union[Unset, float]):
        end_time_year (Union[Unset, float]):
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
        start_time (Union[Unset, datetime.datetime]):
        start_time_contained_by (Union[Unset, datetime.datetime]):
        start_time_contains (Union[Unset, datetime.datetime]):
        start_time_date (Union[Unset, datetime.date]):
        start_time_day (Union[Unset, float]):
        start_time_endswith (Union[Unset, datetime.datetime]):
        start_time_gt (Union[Unset, datetime.datetime]):
        start_time_gte (Union[Unset, datetime.datetime]):
        start_time_hour (Union[Unset, float]):
        start_time_icontains (Union[Unset, datetime.datetime]):
        start_time_iendswith (Union[Unset, datetime.datetime]):
        start_time_iexact (Union[Unset, datetime.datetime]):
        start_time_in (Union[Unset, list[datetime.datetime]]):
        start_time_iregex (Union[Unset, datetime.datetime]):
        start_time_isnull (Union[Unset, bool]):
        start_time_iso_week_day (Union[Unset, float]):
        start_time_iso_year (Union[Unset, float]):
        start_time_istartswith (Union[Unset, datetime.datetime]):
        start_time_lt (Union[Unset, datetime.datetime]):
        start_time_lte (Union[Unset, datetime.datetime]):
        start_time_minute (Union[Unset, float]):
        start_time_month (Union[Unset, float]):
        start_time_quarter (Union[Unset, float]):
        start_time_range (Union[Unset, list[datetime.datetime]]):
        start_time_regex (Union[Unset, datetime.datetime]):
        start_time_second (Union[Unset, float]):
        start_time_startswith (Union[Unset, datetime.datetime]):
        start_time_time (Union[Unset, str]):
        start_time_week (Union[Unset, float]):
        start_time_week_day (Union[Unset, float]):
        start_time_year (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTimePeriodList
    """

    return sync_detailed(
        client=client,
        end_time=end_time,
        end_time_contained_by=end_time_contained_by,
        end_time_contains=end_time_contains,
        end_time_date=end_time_date,
        end_time_day=end_time_day,
        end_time_endswith=end_time_endswith,
        end_time_gt=end_time_gt,
        end_time_gte=end_time_gte,
        end_time_hour=end_time_hour,
        end_time_icontains=end_time_icontains,
        end_time_iendswith=end_time_iendswith,
        end_time_iexact=end_time_iexact,
        end_time_in=end_time_in,
        end_time_iregex=end_time_iregex,
        end_time_isnull=end_time_isnull,
        end_time_iso_week_day=end_time_iso_week_day,
        end_time_iso_year=end_time_iso_year,
        end_time_istartswith=end_time_istartswith,
        end_time_lt=end_time_lt,
        end_time_lte=end_time_lte,
        end_time_minute=end_time_minute,
        end_time_month=end_time_month,
        end_time_quarter=end_time_quarter,
        end_time_range=end_time_range,
        end_time_regex=end_time_regex,
        end_time_second=end_time_second,
        end_time_startswith=end_time_startswith,
        end_time_time=end_time_time,
        end_time_week=end_time_week,
        end_time_week_day=end_time_week_day,
        end_time_year=end_time_year,
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
        start_time=start_time,
        start_time_contained_by=start_time_contained_by,
        start_time_contains=start_time_contains,
        start_time_date=start_time_date,
        start_time_day=start_time_day,
        start_time_endswith=start_time_endswith,
        start_time_gt=start_time_gt,
        start_time_gte=start_time_gte,
        start_time_hour=start_time_hour,
        start_time_icontains=start_time_icontains,
        start_time_iendswith=start_time_iendswith,
        start_time_iexact=start_time_iexact,
        start_time_in=start_time_in,
        start_time_iregex=start_time_iregex,
        start_time_isnull=start_time_isnull,
        start_time_iso_week_day=start_time_iso_week_day,
        start_time_iso_year=start_time_iso_year,
        start_time_istartswith=start_time_istartswith,
        start_time_lt=start_time_lt,
        start_time_lte=start_time_lte,
        start_time_minute=start_time_minute,
        start_time_month=start_time_month,
        start_time_quarter=start_time_quarter,
        start_time_range=start_time_range,
        start_time_regex=start_time_regex,
        start_time_second=start_time_second,
        start_time_startswith=start_time_startswith,
        start_time_time=start_time_time,
        start_time_week=start_time_week,
        start_time_week_day=start_time_week_day,
        start_time_year=start_time_year,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    end_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    end_time_contains: Union[Unset, datetime.datetime] = UNSET,
    end_time_date: Union[Unset, datetime.date] = UNSET,
    end_time_day: Union[Unset, float] = UNSET,
    end_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_gt: Union[Unset, datetime.datetime] = UNSET,
    end_time_gte: Union[Unset, datetime.datetime] = UNSET,
    end_time_hour: Union[Unset, float] = UNSET,
    end_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    end_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    end_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    end_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    end_time_isnull: Union[Unset, bool] = UNSET,
    end_time_iso_week_day: Union[Unset, float] = UNSET,
    end_time_iso_year: Union[Unset, float] = UNSET,
    end_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_lt: Union[Unset, datetime.datetime] = UNSET,
    end_time_lte: Union[Unset, datetime.datetime] = UNSET,
    end_time_minute: Union[Unset, float] = UNSET,
    end_time_month: Union[Unset, float] = UNSET,
    end_time_quarter: Union[Unset, float] = UNSET,
    end_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    end_time_regex: Union[Unset, datetime.datetime] = UNSET,
    end_time_second: Union[Unset, float] = UNSET,
    end_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_time: Union[Unset, str] = UNSET,
    end_time_week: Union[Unset, float] = UNSET,
    end_time_week_day: Union[Unset, float] = UNSET,
    end_time_year: Union[Unset, float] = UNSET,
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
    start_time: Union[Unset, datetime.datetime] = UNSET,
    start_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    start_time_contains: Union[Unset, datetime.datetime] = UNSET,
    start_time_date: Union[Unset, datetime.date] = UNSET,
    start_time_day: Union[Unset, float] = UNSET,
    start_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_gt: Union[Unset, datetime.datetime] = UNSET,
    start_time_gte: Union[Unset, datetime.datetime] = UNSET,
    start_time_hour: Union[Unset, float] = UNSET,
    start_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    start_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    start_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    start_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    start_time_isnull: Union[Unset, bool] = UNSET,
    start_time_iso_week_day: Union[Unset, float] = UNSET,
    start_time_iso_year: Union[Unset, float] = UNSET,
    start_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_lt: Union[Unset, datetime.datetime] = UNSET,
    start_time_lte: Union[Unset, datetime.datetime] = UNSET,
    start_time_minute: Union[Unset, float] = UNSET,
    start_time_month: Union[Unset, float] = UNSET,
    start_time_quarter: Union[Unset, float] = UNSET,
    start_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    start_time_regex: Union[Unset, datetime.datetime] = UNSET,
    start_time_second: Union[Unset, float] = UNSET,
    start_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_time: Union[Unset, str] = UNSET,
    start_time_week: Union[Unset, float] = UNSET,
    start_time_week_day: Union[Unset, float] = UNSET,
    start_time_year: Union[Unset, float] = UNSET,
) -> Response[PaginatedTimePeriodList]:
    """Get a list of TimePeriod objects. TimePeriods have a 1:1 use with many types of principal record
    types.

    Args:
        end_time (Union[Unset, datetime.datetime]):
        end_time_contained_by (Union[Unset, datetime.datetime]):
        end_time_contains (Union[Unset, datetime.datetime]):
        end_time_date (Union[Unset, datetime.date]):
        end_time_day (Union[Unset, float]):
        end_time_endswith (Union[Unset, datetime.datetime]):
        end_time_gt (Union[Unset, datetime.datetime]):
        end_time_gte (Union[Unset, datetime.datetime]):
        end_time_hour (Union[Unset, float]):
        end_time_icontains (Union[Unset, datetime.datetime]):
        end_time_iendswith (Union[Unset, datetime.datetime]):
        end_time_iexact (Union[Unset, datetime.datetime]):
        end_time_in (Union[Unset, list[datetime.datetime]]):
        end_time_iregex (Union[Unset, datetime.datetime]):
        end_time_isnull (Union[Unset, bool]):
        end_time_iso_week_day (Union[Unset, float]):
        end_time_iso_year (Union[Unset, float]):
        end_time_istartswith (Union[Unset, datetime.datetime]):
        end_time_lt (Union[Unset, datetime.datetime]):
        end_time_lte (Union[Unset, datetime.datetime]):
        end_time_minute (Union[Unset, float]):
        end_time_month (Union[Unset, float]):
        end_time_quarter (Union[Unset, float]):
        end_time_range (Union[Unset, list[datetime.datetime]]):
        end_time_regex (Union[Unset, datetime.datetime]):
        end_time_second (Union[Unset, float]):
        end_time_startswith (Union[Unset, datetime.datetime]):
        end_time_time (Union[Unset, str]):
        end_time_week (Union[Unset, float]):
        end_time_week_day (Union[Unset, float]):
        end_time_year (Union[Unset, float]):
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
        start_time (Union[Unset, datetime.datetime]):
        start_time_contained_by (Union[Unset, datetime.datetime]):
        start_time_contains (Union[Unset, datetime.datetime]):
        start_time_date (Union[Unset, datetime.date]):
        start_time_day (Union[Unset, float]):
        start_time_endswith (Union[Unset, datetime.datetime]):
        start_time_gt (Union[Unset, datetime.datetime]):
        start_time_gte (Union[Unset, datetime.datetime]):
        start_time_hour (Union[Unset, float]):
        start_time_icontains (Union[Unset, datetime.datetime]):
        start_time_iendswith (Union[Unset, datetime.datetime]):
        start_time_iexact (Union[Unset, datetime.datetime]):
        start_time_in (Union[Unset, list[datetime.datetime]]):
        start_time_iregex (Union[Unset, datetime.datetime]):
        start_time_isnull (Union[Unset, bool]):
        start_time_iso_week_day (Union[Unset, float]):
        start_time_iso_year (Union[Unset, float]):
        start_time_istartswith (Union[Unset, datetime.datetime]):
        start_time_lt (Union[Unset, datetime.datetime]):
        start_time_lte (Union[Unset, datetime.datetime]):
        start_time_minute (Union[Unset, float]):
        start_time_month (Union[Unset, float]):
        start_time_quarter (Union[Unset, float]):
        start_time_range (Union[Unset, list[datetime.datetime]]):
        start_time_regex (Union[Unset, datetime.datetime]):
        start_time_second (Union[Unset, float]):
        start_time_startswith (Union[Unset, datetime.datetime]):
        start_time_time (Union[Unset, str]):
        start_time_week (Union[Unset, float]):
        start_time_week_day (Union[Unset, float]):
        start_time_year (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTimePeriodList]
    """

    kwargs = _get_kwargs(
        end_time=end_time,
        end_time_contained_by=end_time_contained_by,
        end_time_contains=end_time_contains,
        end_time_date=end_time_date,
        end_time_day=end_time_day,
        end_time_endswith=end_time_endswith,
        end_time_gt=end_time_gt,
        end_time_gte=end_time_gte,
        end_time_hour=end_time_hour,
        end_time_icontains=end_time_icontains,
        end_time_iendswith=end_time_iendswith,
        end_time_iexact=end_time_iexact,
        end_time_in=end_time_in,
        end_time_iregex=end_time_iregex,
        end_time_isnull=end_time_isnull,
        end_time_iso_week_day=end_time_iso_week_day,
        end_time_iso_year=end_time_iso_year,
        end_time_istartswith=end_time_istartswith,
        end_time_lt=end_time_lt,
        end_time_lte=end_time_lte,
        end_time_minute=end_time_minute,
        end_time_month=end_time_month,
        end_time_quarter=end_time_quarter,
        end_time_range=end_time_range,
        end_time_regex=end_time_regex,
        end_time_second=end_time_second,
        end_time_startswith=end_time_startswith,
        end_time_time=end_time_time,
        end_time_week=end_time_week,
        end_time_week_day=end_time_week_day,
        end_time_year=end_time_year,
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
        start_time=start_time,
        start_time_contained_by=start_time_contained_by,
        start_time_contains=start_time_contains,
        start_time_date=start_time_date,
        start_time_day=start_time_day,
        start_time_endswith=start_time_endswith,
        start_time_gt=start_time_gt,
        start_time_gte=start_time_gte,
        start_time_hour=start_time_hour,
        start_time_icontains=start_time_icontains,
        start_time_iendswith=start_time_iendswith,
        start_time_iexact=start_time_iexact,
        start_time_in=start_time_in,
        start_time_iregex=start_time_iregex,
        start_time_isnull=start_time_isnull,
        start_time_iso_week_day=start_time_iso_week_day,
        start_time_iso_year=start_time_iso_year,
        start_time_istartswith=start_time_istartswith,
        start_time_lt=start_time_lt,
        start_time_lte=start_time_lte,
        start_time_minute=start_time_minute,
        start_time_month=start_time_month,
        start_time_quarter=start_time_quarter,
        start_time_range=start_time_range,
        start_time_regex=start_time_regex,
        start_time_second=start_time_second,
        start_time_startswith=start_time_startswith,
        start_time_time=start_time_time,
        start_time_week=start_time_week,
        start_time_week_day=start_time_week_day,
        start_time_year=start_time_year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    end_time: Union[Unset, datetime.datetime] = UNSET,
    end_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    end_time_contains: Union[Unset, datetime.datetime] = UNSET,
    end_time_date: Union[Unset, datetime.date] = UNSET,
    end_time_day: Union[Unset, float] = UNSET,
    end_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_gt: Union[Unset, datetime.datetime] = UNSET,
    end_time_gte: Union[Unset, datetime.datetime] = UNSET,
    end_time_hour: Union[Unset, float] = UNSET,
    end_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    end_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    end_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    end_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    end_time_isnull: Union[Unset, bool] = UNSET,
    end_time_iso_week_day: Union[Unset, float] = UNSET,
    end_time_iso_year: Union[Unset, float] = UNSET,
    end_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_lt: Union[Unset, datetime.datetime] = UNSET,
    end_time_lte: Union[Unset, datetime.datetime] = UNSET,
    end_time_minute: Union[Unset, float] = UNSET,
    end_time_month: Union[Unset, float] = UNSET,
    end_time_quarter: Union[Unset, float] = UNSET,
    end_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    end_time_regex: Union[Unset, datetime.datetime] = UNSET,
    end_time_second: Union[Unset, float] = UNSET,
    end_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    end_time_time: Union[Unset, str] = UNSET,
    end_time_week: Union[Unset, float] = UNSET,
    end_time_week_day: Union[Unset, float] = UNSET,
    end_time_year: Union[Unset, float] = UNSET,
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
    start_time: Union[Unset, datetime.datetime] = UNSET,
    start_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    start_time_contains: Union[Unset, datetime.datetime] = UNSET,
    start_time_date: Union[Unset, datetime.date] = UNSET,
    start_time_day: Union[Unset, float] = UNSET,
    start_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_gt: Union[Unset, datetime.datetime] = UNSET,
    start_time_gte: Union[Unset, datetime.datetime] = UNSET,
    start_time_hour: Union[Unset, float] = UNSET,
    start_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    start_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    start_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    start_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    start_time_isnull: Union[Unset, bool] = UNSET,
    start_time_iso_week_day: Union[Unset, float] = UNSET,
    start_time_iso_year: Union[Unset, float] = UNSET,
    start_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_lt: Union[Unset, datetime.datetime] = UNSET,
    start_time_lte: Union[Unset, datetime.datetime] = UNSET,
    start_time_minute: Union[Unset, float] = UNSET,
    start_time_month: Union[Unset, float] = UNSET,
    start_time_quarter: Union[Unset, float] = UNSET,
    start_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    start_time_regex: Union[Unset, datetime.datetime] = UNSET,
    start_time_second: Union[Unset, float] = UNSET,
    start_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    start_time_time: Union[Unset, str] = UNSET,
    start_time_week: Union[Unset, float] = UNSET,
    start_time_week_day: Union[Unset, float] = UNSET,
    start_time_year: Union[Unset, float] = UNSET,
) -> Optional[PaginatedTimePeriodList]:
    """Get a list of TimePeriod objects. TimePeriods have a 1:1 use with many types of principal record
    types.

    Args:
        end_time (Union[Unset, datetime.datetime]):
        end_time_contained_by (Union[Unset, datetime.datetime]):
        end_time_contains (Union[Unset, datetime.datetime]):
        end_time_date (Union[Unset, datetime.date]):
        end_time_day (Union[Unset, float]):
        end_time_endswith (Union[Unset, datetime.datetime]):
        end_time_gt (Union[Unset, datetime.datetime]):
        end_time_gte (Union[Unset, datetime.datetime]):
        end_time_hour (Union[Unset, float]):
        end_time_icontains (Union[Unset, datetime.datetime]):
        end_time_iendswith (Union[Unset, datetime.datetime]):
        end_time_iexact (Union[Unset, datetime.datetime]):
        end_time_in (Union[Unset, list[datetime.datetime]]):
        end_time_iregex (Union[Unset, datetime.datetime]):
        end_time_isnull (Union[Unset, bool]):
        end_time_iso_week_day (Union[Unset, float]):
        end_time_iso_year (Union[Unset, float]):
        end_time_istartswith (Union[Unset, datetime.datetime]):
        end_time_lt (Union[Unset, datetime.datetime]):
        end_time_lte (Union[Unset, datetime.datetime]):
        end_time_minute (Union[Unset, float]):
        end_time_month (Union[Unset, float]):
        end_time_quarter (Union[Unset, float]):
        end_time_range (Union[Unset, list[datetime.datetime]]):
        end_time_regex (Union[Unset, datetime.datetime]):
        end_time_second (Union[Unset, float]):
        end_time_startswith (Union[Unset, datetime.datetime]):
        end_time_time (Union[Unset, str]):
        end_time_week (Union[Unset, float]):
        end_time_week_day (Union[Unset, float]):
        end_time_year (Union[Unset, float]):
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
        start_time (Union[Unset, datetime.datetime]):
        start_time_contained_by (Union[Unset, datetime.datetime]):
        start_time_contains (Union[Unset, datetime.datetime]):
        start_time_date (Union[Unset, datetime.date]):
        start_time_day (Union[Unset, float]):
        start_time_endswith (Union[Unset, datetime.datetime]):
        start_time_gt (Union[Unset, datetime.datetime]):
        start_time_gte (Union[Unset, datetime.datetime]):
        start_time_hour (Union[Unset, float]):
        start_time_icontains (Union[Unset, datetime.datetime]):
        start_time_iendswith (Union[Unset, datetime.datetime]):
        start_time_iexact (Union[Unset, datetime.datetime]):
        start_time_in (Union[Unset, list[datetime.datetime]]):
        start_time_iregex (Union[Unset, datetime.datetime]):
        start_time_isnull (Union[Unset, bool]):
        start_time_iso_week_day (Union[Unset, float]):
        start_time_iso_year (Union[Unset, float]):
        start_time_istartswith (Union[Unset, datetime.datetime]):
        start_time_lt (Union[Unset, datetime.datetime]):
        start_time_lte (Union[Unset, datetime.datetime]):
        start_time_minute (Union[Unset, float]):
        start_time_month (Union[Unset, float]):
        start_time_quarter (Union[Unset, float]):
        start_time_range (Union[Unset, list[datetime.datetime]]):
        start_time_regex (Union[Unset, datetime.datetime]):
        start_time_second (Union[Unset, float]):
        start_time_startswith (Union[Unset, datetime.datetime]):
        start_time_time (Union[Unset, str]):
        start_time_week (Union[Unset, float]):
        start_time_week_day (Union[Unset, float]):
        start_time_year (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTimePeriodList
    """

    return (
        await asyncio_detailed(
            client=client,
            end_time=end_time,
            end_time_contained_by=end_time_contained_by,
            end_time_contains=end_time_contains,
            end_time_date=end_time_date,
            end_time_day=end_time_day,
            end_time_endswith=end_time_endswith,
            end_time_gt=end_time_gt,
            end_time_gte=end_time_gte,
            end_time_hour=end_time_hour,
            end_time_icontains=end_time_icontains,
            end_time_iendswith=end_time_iendswith,
            end_time_iexact=end_time_iexact,
            end_time_in=end_time_in,
            end_time_iregex=end_time_iregex,
            end_time_isnull=end_time_isnull,
            end_time_iso_week_day=end_time_iso_week_day,
            end_time_iso_year=end_time_iso_year,
            end_time_istartswith=end_time_istartswith,
            end_time_lt=end_time_lt,
            end_time_lte=end_time_lte,
            end_time_minute=end_time_minute,
            end_time_month=end_time_month,
            end_time_quarter=end_time_quarter,
            end_time_range=end_time_range,
            end_time_regex=end_time_regex,
            end_time_second=end_time_second,
            end_time_startswith=end_time_startswith,
            end_time_time=end_time_time,
            end_time_week=end_time_week,
            end_time_week_day=end_time_week_day,
            end_time_year=end_time_year,
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
            start_time=start_time,
            start_time_contained_by=start_time_contained_by,
            start_time_contains=start_time_contains,
            start_time_date=start_time_date,
            start_time_day=start_time_day,
            start_time_endswith=start_time_endswith,
            start_time_gt=start_time_gt,
            start_time_gte=start_time_gte,
            start_time_hour=start_time_hour,
            start_time_icontains=start_time_icontains,
            start_time_iendswith=start_time_iendswith,
            start_time_iexact=start_time_iexact,
            start_time_in=start_time_in,
            start_time_iregex=start_time_iregex,
            start_time_isnull=start_time_isnull,
            start_time_iso_week_day=start_time_iso_week_day,
            start_time_iso_year=start_time_iso_year,
            start_time_istartswith=start_time_istartswith,
            start_time_lt=start_time_lt,
            start_time_lte=start_time_lte,
            start_time_minute=start_time_minute,
            start_time_month=start_time_month,
            start_time_quarter=start_time_quarter,
            start_time_range=start_time_range,
            start_time_regex=start_time_regex,
            start_time_second=start_time_second,
            start_time_startswith=start_time_startswith,
            start_time_time=start_time_time,
            start_time_week=start_time_week,
            start_time_week_day=start_time_week_day,
            start_time_year=start_time_year,
        )
    ).parsed
