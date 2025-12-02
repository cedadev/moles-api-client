import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_time_period_list import PaginatedTimePeriodList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    end_time: datetime.datetime | Unset = UNSET,
    end_time_contained_by: datetime.datetime | Unset = UNSET,
    end_time_contains: datetime.datetime | Unset = UNSET,
    end_time_date: datetime.date | Unset = UNSET,
    end_time_day: float | Unset = UNSET,
    end_time_endswith: datetime.datetime | Unset = UNSET,
    end_time_gt: datetime.datetime | Unset = UNSET,
    end_time_gte: datetime.datetime | Unset = UNSET,
    end_time_hour: float | Unset = UNSET,
    end_time_icontains: datetime.datetime | Unset = UNSET,
    end_time_iendswith: datetime.datetime | Unset = UNSET,
    end_time_iexact: datetime.datetime | Unset = UNSET,
    end_time_in: list[datetime.datetime] | Unset = UNSET,
    end_time_iregex: datetime.datetime | Unset = UNSET,
    end_time_isnull: bool | Unset = UNSET,
    end_time_iso_week_day: float | Unset = UNSET,
    end_time_iso_year: float | Unset = UNSET,
    end_time_istartswith: datetime.datetime | Unset = UNSET,
    end_time_lt: datetime.datetime | Unset = UNSET,
    end_time_lte: datetime.datetime | Unset = UNSET,
    end_time_minute: float | Unset = UNSET,
    end_time_month: float | Unset = UNSET,
    end_time_quarter: float | Unset = UNSET,
    end_time_range: list[datetime.datetime] | Unset = UNSET,
    end_time_regex: datetime.datetime | Unset = UNSET,
    end_time_second: float | Unset = UNSET,
    end_time_startswith: datetime.datetime | Unset = UNSET,
    end_time_time: str | Unset = UNSET,
    end_time_week: float | Unset = UNSET,
    end_time_week_day: float | Unset = UNSET,
    end_time_year: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_phenomenon_time: list[int] | Unset = UNSET,
    observation_phenomenon_time_in: list[int] | Unset = UNSET,
    observation_phenomenon_time_isnull: bool | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    start_time_contained_by: datetime.datetime | Unset = UNSET,
    start_time_contains: datetime.datetime | Unset = UNSET,
    start_time_date: datetime.date | Unset = UNSET,
    start_time_day: float | Unset = UNSET,
    start_time_endswith: datetime.datetime | Unset = UNSET,
    start_time_gt: datetime.datetime | Unset = UNSET,
    start_time_gte: datetime.datetime | Unset = UNSET,
    start_time_hour: float | Unset = UNSET,
    start_time_icontains: datetime.datetime | Unset = UNSET,
    start_time_iendswith: datetime.datetime | Unset = UNSET,
    start_time_iexact: datetime.datetime | Unset = UNSET,
    start_time_in: list[datetime.datetime] | Unset = UNSET,
    start_time_iregex: datetime.datetime | Unset = UNSET,
    start_time_isnull: bool | Unset = UNSET,
    start_time_iso_week_day: float | Unset = UNSET,
    start_time_iso_year: float | Unset = UNSET,
    start_time_istartswith: datetime.datetime | Unset = UNSET,
    start_time_lt: datetime.datetime | Unset = UNSET,
    start_time_lte: datetime.datetime | Unset = UNSET,
    start_time_minute: float | Unset = UNSET,
    start_time_month: float | Unset = UNSET,
    start_time_quarter: float | Unset = UNSET,
    start_time_range: list[datetime.datetime] | Unset = UNSET,
    start_time_regex: datetime.datetime | Unset = UNSET,
    start_time_second: float | Unset = UNSET,
    start_time_startswith: datetime.datetime | Unset = UNSET,
    start_time_time: str | Unset = UNSET,
    start_time_week: float | Unset = UNSET,
    start_time_week_day: float | Unset = UNSET,
    start_time_year: float | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_end_time: str | Unset = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    json_end_time_contained_by: str | Unset = UNSET
    if not isinstance(end_time_contained_by, Unset):
        json_end_time_contained_by = end_time_contained_by.isoformat()
    params["endTime__contained_by"] = json_end_time_contained_by

    json_end_time_contains: str | Unset = UNSET
    if not isinstance(end_time_contains, Unset):
        json_end_time_contains = end_time_contains.isoformat()
    params["endTime__contains"] = json_end_time_contains

    json_end_time_date: str | Unset = UNSET
    if not isinstance(end_time_date, Unset):
        json_end_time_date = end_time_date.isoformat()
    params["endTime__date"] = json_end_time_date

    params["endTime__day"] = end_time_day

    json_end_time_endswith: str | Unset = UNSET
    if not isinstance(end_time_endswith, Unset):
        json_end_time_endswith = end_time_endswith.isoformat()
    params["endTime__endswith"] = json_end_time_endswith

    json_end_time_gt: str | Unset = UNSET
    if not isinstance(end_time_gt, Unset):
        json_end_time_gt = end_time_gt.isoformat()
    params["endTime__gt"] = json_end_time_gt

    json_end_time_gte: str | Unset = UNSET
    if not isinstance(end_time_gte, Unset):
        json_end_time_gte = end_time_gte.isoformat()
    params["endTime__gte"] = json_end_time_gte

    params["endTime__hour"] = end_time_hour

    json_end_time_icontains: str | Unset = UNSET
    if not isinstance(end_time_icontains, Unset):
        json_end_time_icontains = end_time_icontains.isoformat()
    params["endTime__icontains"] = json_end_time_icontains

    json_end_time_iendswith: str | Unset = UNSET
    if not isinstance(end_time_iendswith, Unset):
        json_end_time_iendswith = end_time_iendswith.isoformat()
    params["endTime__iendswith"] = json_end_time_iendswith

    json_end_time_iexact: str | Unset = UNSET
    if not isinstance(end_time_iexact, Unset):
        json_end_time_iexact = end_time_iexact.isoformat()
    params["endTime__iexact"] = json_end_time_iexact

    json_end_time_in: list[str] | Unset = UNSET
    if not isinstance(end_time_in, Unset):
        json_end_time_in = []
        for end_time_in_item_data in end_time_in:
            end_time_in_item = end_time_in_item_data.isoformat()
            json_end_time_in.append(end_time_in_item)

    params["endTime__in"] = json_end_time_in

    json_end_time_iregex: str | Unset = UNSET
    if not isinstance(end_time_iregex, Unset):
        json_end_time_iregex = end_time_iregex.isoformat()
    params["endTime__iregex"] = json_end_time_iregex

    params["endTime__isnull"] = end_time_isnull

    params["endTime__iso_week_day"] = end_time_iso_week_day

    params["endTime__iso_year"] = end_time_iso_year

    json_end_time_istartswith: str | Unset = UNSET
    if not isinstance(end_time_istartswith, Unset):
        json_end_time_istartswith = end_time_istartswith.isoformat()
    params["endTime__istartswith"] = json_end_time_istartswith

    json_end_time_lt: str | Unset = UNSET
    if not isinstance(end_time_lt, Unset):
        json_end_time_lt = end_time_lt.isoformat()
    params["endTime__lt"] = json_end_time_lt

    json_end_time_lte: str | Unset = UNSET
    if not isinstance(end_time_lte, Unset):
        json_end_time_lte = end_time_lte.isoformat()
    params["endTime__lte"] = json_end_time_lte

    params["endTime__minute"] = end_time_minute

    params["endTime__month"] = end_time_month

    params["endTime__quarter"] = end_time_quarter

    json_end_time_range: list[str] | Unset = UNSET
    if not isinstance(end_time_range, Unset):
        json_end_time_range = []
        for end_time_range_item_data in end_time_range:
            end_time_range_item = end_time_range_item_data.isoformat()
            json_end_time_range.append(end_time_range_item)

    params["endTime__range"] = json_end_time_range

    json_end_time_regex: str | Unset = UNSET
    if not isinstance(end_time_regex, Unset):
        json_end_time_regex = end_time_regex.isoformat()
    params["endTime__regex"] = json_end_time_regex

    params["endTime__second"] = end_time_second

    json_end_time_startswith: str | Unset = UNSET
    if not isinstance(end_time_startswith, Unset):
        json_end_time_startswith = end_time_startswith.isoformat()
    params["endTime__startswith"] = json_end_time_startswith

    params["endTime__time"] = end_time_time

    params["endTime__week"] = end_time_week

    params["endTime__week_day"] = end_time_week_day

    params["endTime__year"] = end_time_year

    params["limit"] = limit

    json_mobileplatformoperation: list[int] | Unset = UNSET
    if not isinstance(mobileplatformoperation, Unset):
        json_mobileplatformoperation = ",".join(map(str, mobileplatformoperation))

    params["mobileplatformoperation"] = json_mobileplatformoperation

    json_mobileplatformoperation_in: list[int] | Unset = UNSET
    if not isinstance(mobileplatformoperation_in, Unset):
        json_mobileplatformoperation_in = ",".join(map(str, mobileplatformoperation_in))

    params["mobileplatformoperation__in"] = json_mobileplatformoperation_in

    params["mobileplatformoperation__isnull"] = mobileplatformoperation_isnull

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

    json_observation: list[int] | Unset = UNSET
    if not isinstance(observation, Unset):
        json_observation = ",".join(map(str, observation))

    params["observation"] = json_observation

    json_observation_phenomenon_time: list[int] | Unset = UNSET
    if not isinstance(observation_phenomenon_time, Unset):
        json_observation_phenomenon_time = ",".join(map(str, observation_phenomenon_time))

    params["observationPhenomenonTime"] = json_observation_phenomenon_time

    json_observation_phenomenon_time_in: list[int] | Unset = UNSET
    if not isinstance(observation_phenomenon_time_in, Unset):
        json_observation_phenomenon_time_in = ",".join(map(str, observation_phenomenon_time_in))

    params["observationPhenomenonTime__in"] = json_observation_phenomenon_time_in

    params["observationPhenomenonTime__isnull"] = observation_phenomenon_time_isnull

    json_observation_in: list[int] | Unset = UNSET
    if not isinstance(observation_in, Unset):
        json_observation_in = ",".join(map(str, observation_in))

    params["observation__in"] = json_observation_in

    params["observation__isnull"] = observation_isnull

    params["offset"] = offset

    params["ordering"] = ordering

    json_start_time: str | Unset = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_start_time_contained_by: str | Unset = UNSET
    if not isinstance(start_time_contained_by, Unset):
        json_start_time_contained_by = start_time_contained_by.isoformat()
    params["startTime__contained_by"] = json_start_time_contained_by

    json_start_time_contains: str | Unset = UNSET
    if not isinstance(start_time_contains, Unset):
        json_start_time_contains = start_time_contains.isoformat()
    params["startTime__contains"] = json_start_time_contains

    json_start_time_date: str | Unset = UNSET
    if not isinstance(start_time_date, Unset):
        json_start_time_date = start_time_date.isoformat()
    params["startTime__date"] = json_start_time_date

    params["startTime__day"] = start_time_day

    json_start_time_endswith: str | Unset = UNSET
    if not isinstance(start_time_endswith, Unset):
        json_start_time_endswith = start_time_endswith.isoformat()
    params["startTime__endswith"] = json_start_time_endswith

    json_start_time_gt: str | Unset = UNSET
    if not isinstance(start_time_gt, Unset):
        json_start_time_gt = start_time_gt.isoformat()
    params["startTime__gt"] = json_start_time_gt

    json_start_time_gte: str | Unset = UNSET
    if not isinstance(start_time_gte, Unset):
        json_start_time_gte = start_time_gte.isoformat()
    params["startTime__gte"] = json_start_time_gte

    params["startTime__hour"] = start_time_hour

    json_start_time_icontains: str | Unset = UNSET
    if not isinstance(start_time_icontains, Unset):
        json_start_time_icontains = start_time_icontains.isoformat()
    params["startTime__icontains"] = json_start_time_icontains

    json_start_time_iendswith: str | Unset = UNSET
    if not isinstance(start_time_iendswith, Unset):
        json_start_time_iendswith = start_time_iendswith.isoformat()
    params["startTime__iendswith"] = json_start_time_iendswith

    json_start_time_iexact: str | Unset = UNSET
    if not isinstance(start_time_iexact, Unset):
        json_start_time_iexact = start_time_iexact.isoformat()
    params["startTime__iexact"] = json_start_time_iexact

    json_start_time_in: list[str] | Unset = UNSET
    if not isinstance(start_time_in, Unset):
        json_start_time_in = []
        for start_time_in_item_data in start_time_in:
            start_time_in_item = start_time_in_item_data.isoformat()
            json_start_time_in.append(start_time_in_item)

    params["startTime__in"] = json_start_time_in

    json_start_time_iregex: str | Unset = UNSET
    if not isinstance(start_time_iregex, Unset):
        json_start_time_iregex = start_time_iregex.isoformat()
    params["startTime__iregex"] = json_start_time_iregex

    params["startTime__isnull"] = start_time_isnull

    params["startTime__iso_week_day"] = start_time_iso_week_day

    params["startTime__iso_year"] = start_time_iso_year

    json_start_time_istartswith: str | Unset = UNSET
    if not isinstance(start_time_istartswith, Unset):
        json_start_time_istartswith = start_time_istartswith.isoformat()
    params["startTime__istartswith"] = json_start_time_istartswith

    json_start_time_lt: str | Unset = UNSET
    if not isinstance(start_time_lt, Unset):
        json_start_time_lt = start_time_lt.isoformat()
    params["startTime__lt"] = json_start_time_lt

    json_start_time_lte: str | Unset = UNSET
    if not isinstance(start_time_lte, Unset):
        json_start_time_lte = start_time_lte.isoformat()
    params["startTime__lte"] = json_start_time_lte

    params["startTime__minute"] = start_time_minute

    params["startTime__month"] = start_time_month

    params["startTime__quarter"] = start_time_quarter

    json_start_time_range: list[str] | Unset = UNSET
    if not isinstance(start_time_range, Unset):
        json_start_time_range = []
        for start_time_range_item_data in start_time_range:
            start_time_range_item = start_time_range_item_data.isoformat()
            json_start_time_range.append(start_time_range_item)

    params["startTime__range"] = json_start_time_range

    json_start_time_regex: str | Unset = UNSET
    if not isinstance(start_time_regex, Unset):
        json_start_time_regex = start_time_regex.isoformat()
    params["startTime__regex"] = json_start_time_regex

    params["startTime__second"] = start_time_second

    json_start_time_startswith: str | Unset = UNSET
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedTimePeriodList | None:
    if response.status_code == 200:
        response_200 = PaginatedTimePeriodList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    end_time: datetime.datetime | Unset = UNSET,
    end_time_contained_by: datetime.datetime | Unset = UNSET,
    end_time_contains: datetime.datetime | Unset = UNSET,
    end_time_date: datetime.date | Unset = UNSET,
    end_time_day: float | Unset = UNSET,
    end_time_endswith: datetime.datetime | Unset = UNSET,
    end_time_gt: datetime.datetime | Unset = UNSET,
    end_time_gte: datetime.datetime | Unset = UNSET,
    end_time_hour: float | Unset = UNSET,
    end_time_icontains: datetime.datetime | Unset = UNSET,
    end_time_iendswith: datetime.datetime | Unset = UNSET,
    end_time_iexact: datetime.datetime | Unset = UNSET,
    end_time_in: list[datetime.datetime] | Unset = UNSET,
    end_time_iregex: datetime.datetime | Unset = UNSET,
    end_time_isnull: bool | Unset = UNSET,
    end_time_iso_week_day: float | Unset = UNSET,
    end_time_iso_year: float | Unset = UNSET,
    end_time_istartswith: datetime.datetime | Unset = UNSET,
    end_time_lt: datetime.datetime | Unset = UNSET,
    end_time_lte: datetime.datetime | Unset = UNSET,
    end_time_minute: float | Unset = UNSET,
    end_time_month: float | Unset = UNSET,
    end_time_quarter: float | Unset = UNSET,
    end_time_range: list[datetime.datetime] | Unset = UNSET,
    end_time_regex: datetime.datetime | Unset = UNSET,
    end_time_second: float | Unset = UNSET,
    end_time_startswith: datetime.datetime | Unset = UNSET,
    end_time_time: str | Unset = UNSET,
    end_time_week: float | Unset = UNSET,
    end_time_week_day: float | Unset = UNSET,
    end_time_year: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_phenomenon_time: list[int] | Unset = UNSET,
    observation_phenomenon_time_in: list[int] | Unset = UNSET,
    observation_phenomenon_time_isnull: bool | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    start_time_contained_by: datetime.datetime | Unset = UNSET,
    start_time_contains: datetime.datetime | Unset = UNSET,
    start_time_date: datetime.date | Unset = UNSET,
    start_time_day: float | Unset = UNSET,
    start_time_endswith: datetime.datetime | Unset = UNSET,
    start_time_gt: datetime.datetime | Unset = UNSET,
    start_time_gte: datetime.datetime | Unset = UNSET,
    start_time_hour: float | Unset = UNSET,
    start_time_icontains: datetime.datetime | Unset = UNSET,
    start_time_iendswith: datetime.datetime | Unset = UNSET,
    start_time_iexact: datetime.datetime | Unset = UNSET,
    start_time_in: list[datetime.datetime] | Unset = UNSET,
    start_time_iregex: datetime.datetime | Unset = UNSET,
    start_time_isnull: bool | Unset = UNSET,
    start_time_iso_week_day: float | Unset = UNSET,
    start_time_iso_year: float | Unset = UNSET,
    start_time_istartswith: datetime.datetime | Unset = UNSET,
    start_time_lt: datetime.datetime | Unset = UNSET,
    start_time_lte: datetime.datetime | Unset = UNSET,
    start_time_minute: float | Unset = UNSET,
    start_time_month: float | Unset = UNSET,
    start_time_quarter: float | Unset = UNSET,
    start_time_range: list[datetime.datetime] | Unset = UNSET,
    start_time_regex: datetime.datetime | Unset = UNSET,
    start_time_second: float | Unset = UNSET,
    start_time_startswith: datetime.datetime | Unset = UNSET,
    start_time_time: str | Unset = UNSET,
    start_time_week: float | Unset = UNSET,
    start_time_week_day: float | Unset = UNSET,
    start_time_year: float | Unset = UNSET,
) -> Response[PaginatedTimePeriodList]:
    """Get a list of TimePeriod objects. TimePeriods have a 1:1 use with many types of principal record
    types.

    Args:
        end_time (datetime.datetime | Unset):
        end_time_contained_by (datetime.datetime | Unset):
        end_time_contains (datetime.datetime | Unset):
        end_time_date (datetime.date | Unset):
        end_time_day (float | Unset):
        end_time_endswith (datetime.datetime | Unset):
        end_time_gt (datetime.datetime | Unset):
        end_time_gte (datetime.datetime | Unset):
        end_time_hour (float | Unset):
        end_time_icontains (datetime.datetime | Unset):
        end_time_iendswith (datetime.datetime | Unset):
        end_time_iexact (datetime.datetime | Unset):
        end_time_in (list[datetime.datetime] | Unset):
        end_time_iregex (datetime.datetime | Unset):
        end_time_isnull (bool | Unset):
        end_time_iso_week_day (float | Unset):
        end_time_iso_year (float | Unset):
        end_time_istartswith (datetime.datetime | Unset):
        end_time_lt (datetime.datetime | Unset):
        end_time_lte (datetime.datetime | Unset):
        end_time_minute (float | Unset):
        end_time_month (float | Unset):
        end_time_quarter (float | Unset):
        end_time_range (list[datetime.datetime] | Unset):
        end_time_regex (datetime.datetime | Unset):
        end_time_second (float | Unset):
        end_time_startswith (datetime.datetime | Unset):
        end_time_time (str | Unset):
        end_time_week (float | Unset):
        end_time_week_day (float | Unset):
        end_time_year (float | Unset):
        limit (int | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
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
        observation (list[int] | Unset):
        observation_phenomenon_time (list[int] | Unset):
        observation_phenomenon_time_in (list[int] | Unset):
        observation_phenomenon_time_isnull (bool | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        start_time (datetime.datetime | Unset):
        start_time_contained_by (datetime.datetime | Unset):
        start_time_contains (datetime.datetime | Unset):
        start_time_date (datetime.date | Unset):
        start_time_day (float | Unset):
        start_time_endswith (datetime.datetime | Unset):
        start_time_gt (datetime.datetime | Unset):
        start_time_gte (datetime.datetime | Unset):
        start_time_hour (float | Unset):
        start_time_icontains (datetime.datetime | Unset):
        start_time_iendswith (datetime.datetime | Unset):
        start_time_iexact (datetime.datetime | Unset):
        start_time_in (list[datetime.datetime] | Unset):
        start_time_iregex (datetime.datetime | Unset):
        start_time_isnull (bool | Unset):
        start_time_iso_week_day (float | Unset):
        start_time_iso_year (float | Unset):
        start_time_istartswith (datetime.datetime | Unset):
        start_time_lt (datetime.datetime | Unset):
        start_time_lte (datetime.datetime | Unset):
        start_time_minute (float | Unset):
        start_time_month (float | Unset):
        start_time_quarter (float | Unset):
        start_time_range (list[datetime.datetime] | Unset):
        start_time_regex (datetime.datetime | Unset):
        start_time_second (float | Unset):
        start_time_startswith (datetime.datetime | Unset):
        start_time_time (str | Unset):
        start_time_week (float | Unset):
        start_time_week_day (float | Unset):
        start_time_year (float | Unset):

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
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
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
        observation=observation,
        observation_phenomenon_time=observation_phenomenon_time,
        observation_phenomenon_time_in=observation_phenomenon_time_in,
        observation_phenomenon_time_isnull=observation_phenomenon_time_isnull,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
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
    end_time: datetime.datetime | Unset = UNSET,
    end_time_contained_by: datetime.datetime | Unset = UNSET,
    end_time_contains: datetime.datetime | Unset = UNSET,
    end_time_date: datetime.date | Unset = UNSET,
    end_time_day: float | Unset = UNSET,
    end_time_endswith: datetime.datetime | Unset = UNSET,
    end_time_gt: datetime.datetime | Unset = UNSET,
    end_time_gte: datetime.datetime | Unset = UNSET,
    end_time_hour: float | Unset = UNSET,
    end_time_icontains: datetime.datetime | Unset = UNSET,
    end_time_iendswith: datetime.datetime | Unset = UNSET,
    end_time_iexact: datetime.datetime | Unset = UNSET,
    end_time_in: list[datetime.datetime] | Unset = UNSET,
    end_time_iregex: datetime.datetime | Unset = UNSET,
    end_time_isnull: bool | Unset = UNSET,
    end_time_iso_week_day: float | Unset = UNSET,
    end_time_iso_year: float | Unset = UNSET,
    end_time_istartswith: datetime.datetime | Unset = UNSET,
    end_time_lt: datetime.datetime | Unset = UNSET,
    end_time_lte: datetime.datetime | Unset = UNSET,
    end_time_minute: float | Unset = UNSET,
    end_time_month: float | Unset = UNSET,
    end_time_quarter: float | Unset = UNSET,
    end_time_range: list[datetime.datetime] | Unset = UNSET,
    end_time_regex: datetime.datetime | Unset = UNSET,
    end_time_second: float | Unset = UNSET,
    end_time_startswith: datetime.datetime | Unset = UNSET,
    end_time_time: str | Unset = UNSET,
    end_time_week: float | Unset = UNSET,
    end_time_week_day: float | Unset = UNSET,
    end_time_year: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_phenomenon_time: list[int] | Unset = UNSET,
    observation_phenomenon_time_in: list[int] | Unset = UNSET,
    observation_phenomenon_time_isnull: bool | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    start_time_contained_by: datetime.datetime | Unset = UNSET,
    start_time_contains: datetime.datetime | Unset = UNSET,
    start_time_date: datetime.date | Unset = UNSET,
    start_time_day: float | Unset = UNSET,
    start_time_endswith: datetime.datetime | Unset = UNSET,
    start_time_gt: datetime.datetime | Unset = UNSET,
    start_time_gte: datetime.datetime | Unset = UNSET,
    start_time_hour: float | Unset = UNSET,
    start_time_icontains: datetime.datetime | Unset = UNSET,
    start_time_iendswith: datetime.datetime | Unset = UNSET,
    start_time_iexact: datetime.datetime | Unset = UNSET,
    start_time_in: list[datetime.datetime] | Unset = UNSET,
    start_time_iregex: datetime.datetime | Unset = UNSET,
    start_time_isnull: bool | Unset = UNSET,
    start_time_iso_week_day: float | Unset = UNSET,
    start_time_iso_year: float | Unset = UNSET,
    start_time_istartswith: datetime.datetime | Unset = UNSET,
    start_time_lt: datetime.datetime | Unset = UNSET,
    start_time_lte: datetime.datetime | Unset = UNSET,
    start_time_minute: float | Unset = UNSET,
    start_time_month: float | Unset = UNSET,
    start_time_quarter: float | Unset = UNSET,
    start_time_range: list[datetime.datetime] | Unset = UNSET,
    start_time_regex: datetime.datetime | Unset = UNSET,
    start_time_second: float | Unset = UNSET,
    start_time_startswith: datetime.datetime | Unset = UNSET,
    start_time_time: str | Unset = UNSET,
    start_time_week: float | Unset = UNSET,
    start_time_week_day: float | Unset = UNSET,
    start_time_year: float | Unset = UNSET,
) -> PaginatedTimePeriodList | None:
    """Get a list of TimePeriod objects. TimePeriods have a 1:1 use with many types of principal record
    types.

    Args:
        end_time (datetime.datetime | Unset):
        end_time_contained_by (datetime.datetime | Unset):
        end_time_contains (datetime.datetime | Unset):
        end_time_date (datetime.date | Unset):
        end_time_day (float | Unset):
        end_time_endswith (datetime.datetime | Unset):
        end_time_gt (datetime.datetime | Unset):
        end_time_gte (datetime.datetime | Unset):
        end_time_hour (float | Unset):
        end_time_icontains (datetime.datetime | Unset):
        end_time_iendswith (datetime.datetime | Unset):
        end_time_iexact (datetime.datetime | Unset):
        end_time_in (list[datetime.datetime] | Unset):
        end_time_iregex (datetime.datetime | Unset):
        end_time_isnull (bool | Unset):
        end_time_iso_week_day (float | Unset):
        end_time_iso_year (float | Unset):
        end_time_istartswith (datetime.datetime | Unset):
        end_time_lt (datetime.datetime | Unset):
        end_time_lte (datetime.datetime | Unset):
        end_time_minute (float | Unset):
        end_time_month (float | Unset):
        end_time_quarter (float | Unset):
        end_time_range (list[datetime.datetime] | Unset):
        end_time_regex (datetime.datetime | Unset):
        end_time_second (float | Unset):
        end_time_startswith (datetime.datetime | Unset):
        end_time_time (str | Unset):
        end_time_week (float | Unset):
        end_time_week_day (float | Unset):
        end_time_year (float | Unset):
        limit (int | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
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
        observation (list[int] | Unset):
        observation_phenomenon_time (list[int] | Unset):
        observation_phenomenon_time_in (list[int] | Unset):
        observation_phenomenon_time_isnull (bool | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        start_time (datetime.datetime | Unset):
        start_time_contained_by (datetime.datetime | Unset):
        start_time_contains (datetime.datetime | Unset):
        start_time_date (datetime.date | Unset):
        start_time_day (float | Unset):
        start_time_endswith (datetime.datetime | Unset):
        start_time_gt (datetime.datetime | Unset):
        start_time_gte (datetime.datetime | Unset):
        start_time_hour (float | Unset):
        start_time_icontains (datetime.datetime | Unset):
        start_time_iendswith (datetime.datetime | Unset):
        start_time_iexact (datetime.datetime | Unset):
        start_time_in (list[datetime.datetime] | Unset):
        start_time_iregex (datetime.datetime | Unset):
        start_time_isnull (bool | Unset):
        start_time_iso_week_day (float | Unset):
        start_time_iso_year (float | Unset):
        start_time_istartswith (datetime.datetime | Unset):
        start_time_lt (datetime.datetime | Unset):
        start_time_lte (datetime.datetime | Unset):
        start_time_minute (float | Unset):
        start_time_month (float | Unset):
        start_time_quarter (float | Unset):
        start_time_range (list[datetime.datetime] | Unset):
        start_time_regex (datetime.datetime | Unset):
        start_time_second (float | Unset):
        start_time_startswith (datetime.datetime | Unset):
        start_time_time (str | Unset):
        start_time_week (float | Unset):
        start_time_week_day (float | Unset):
        start_time_year (float | Unset):

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
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
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
        observation=observation,
        observation_phenomenon_time=observation_phenomenon_time,
        observation_phenomenon_time_in=observation_phenomenon_time_in,
        observation_phenomenon_time_isnull=observation_phenomenon_time_isnull,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
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
    end_time: datetime.datetime | Unset = UNSET,
    end_time_contained_by: datetime.datetime | Unset = UNSET,
    end_time_contains: datetime.datetime | Unset = UNSET,
    end_time_date: datetime.date | Unset = UNSET,
    end_time_day: float | Unset = UNSET,
    end_time_endswith: datetime.datetime | Unset = UNSET,
    end_time_gt: datetime.datetime | Unset = UNSET,
    end_time_gte: datetime.datetime | Unset = UNSET,
    end_time_hour: float | Unset = UNSET,
    end_time_icontains: datetime.datetime | Unset = UNSET,
    end_time_iendswith: datetime.datetime | Unset = UNSET,
    end_time_iexact: datetime.datetime | Unset = UNSET,
    end_time_in: list[datetime.datetime] | Unset = UNSET,
    end_time_iregex: datetime.datetime | Unset = UNSET,
    end_time_isnull: bool | Unset = UNSET,
    end_time_iso_week_day: float | Unset = UNSET,
    end_time_iso_year: float | Unset = UNSET,
    end_time_istartswith: datetime.datetime | Unset = UNSET,
    end_time_lt: datetime.datetime | Unset = UNSET,
    end_time_lte: datetime.datetime | Unset = UNSET,
    end_time_minute: float | Unset = UNSET,
    end_time_month: float | Unset = UNSET,
    end_time_quarter: float | Unset = UNSET,
    end_time_range: list[datetime.datetime] | Unset = UNSET,
    end_time_regex: datetime.datetime | Unset = UNSET,
    end_time_second: float | Unset = UNSET,
    end_time_startswith: datetime.datetime | Unset = UNSET,
    end_time_time: str | Unset = UNSET,
    end_time_week: float | Unset = UNSET,
    end_time_week_day: float | Unset = UNSET,
    end_time_year: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_phenomenon_time: list[int] | Unset = UNSET,
    observation_phenomenon_time_in: list[int] | Unset = UNSET,
    observation_phenomenon_time_isnull: bool | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    start_time_contained_by: datetime.datetime | Unset = UNSET,
    start_time_contains: datetime.datetime | Unset = UNSET,
    start_time_date: datetime.date | Unset = UNSET,
    start_time_day: float | Unset = UNSET,
    start_time_endswith: datetime.datetime | Unset = UNSET,
    start_time_gt: datetime.datetime | Unset = UNSET,
    start_time_gte: datetime.datetime | Unset = UNSET,
    start_time_hour: float | Unset = UNSET,
    start_time_icontains: datetime.datetime | Unset = UNSET,
    start_time_iendswith: datetime.datetime | Unset = UNSET,
    start_time_iexact: datetime.datetime | Unset = UNSET,
    start_time_in: list[datetime.datetime] | Unset = UNSET,
    start_time_iregex: datetime.datetime | Unset = UNSET,
    start_time_isnull: bool | Unset = UNSET,
    start_time_iso_week_day: float | Unset = UNSET,
    start_time_iso_year: float | Unset = UNSET,
    start_time_istartswith: datetime.datetime | Unset = UNSET,
    start_time_lt: datetime.datetime | Unset = UNSET,
    start_time_lte: datetime.datetime | Unset = UNSET,
    start_time_minute: float | Unset = UNSET,
    start_time_month: float | Unset = UNSET,
    start_time_quarter: float | Unset = UNSET,
    start_time_range: list[datetime.datetime] | Unset = UNSET,
    start_time_regex: datetime.datetime | Unset = UNSET,
    start_time_second: float | Unset = UNSET,
    start_time_startswith: datetime.datetime | Unset = UNSET,
    start_time_time: str | Unset = UNSET,
    start_time_week: float | Unset = UNSET,
    start_time_week_day: float | Unset = UNSET,
    start_time_year: float | Unset = UNSET,
) -> Response[PaginatedTimePeriodList]:
    """Get a list of TimePeriod objects. TimePeriods have a 1:1 use with many types of principal record
    types.

    Args:
        end_time (datetime.datetime | Unset):
        end_time_contained_by (datetime.datetime | Unset):
        end_time_contains (datetime.datetime | Unset):
        end_time_date (datetime.date | Unset):
        end_time_day (float | Unset):
        end_time_endswith (datetime.datetime | Unset):
        end_time_gt (datetime.datetime | Unset):
        end_time_gte (datetime.datetime | Unset):
        end_time_hour (float | Unset):
        end_time_icontains (datetime.datetime | Unset):
        end_time_iendswith (datetime.datetime | Unset):
        end_time_iexact (datetime.datetime | Unset):
        end_time_in (list[datetime.datetime] | Unset):
        end_time_iregex (datetime.datetime | Unset):
        end_time_isnull (bool | Unset):
        end_time_iso_week_day (float | Unset):
        end_time_iso_year (float | Unset):
        end_time_istartswith (datetime.datetime | Unset):
        end_time_lt (datetime.datetime | Unset):
        end_time_lte (datetime.datetime | Unset):
        end_time_minute (float | Unset):
        end_time_month (float | Unset):
        end_time_quarter (float | Unset):
        end_time_range (list[datetime.datetime] | Unset):
        end_time_regex (datetime.datetime | Unset):
        end_time_second (float | Unset):
        end_time_startswith (datetime.datetime | Unset):
        end_time_time (str | Unset):
        end_time_week (float | Unset):
        end_time_week_day (float | Unset):
        end_time_year (float | Unset):
        limit (int | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
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
        observation (list[int] | Unset):
        observation_phenomenon_time (list[int] | Unset):
        observation_phenomenon_time_in (list[int] | Unset):
        observation_phenomenon_time_isnull (bool | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        start_time (datetime.datetime | Unset):
        start_time_contained_by (datetime.datetime | Unset):
        start_time_contains (datetime.datetime | Unset):
        start_time_date (datetime.date | Unset):
        start_time_day (float | Unset):
        start_time_endswith (datetime.datetime | Unset):
        start_time_gt (datetime.datetime | Unset):
        start_time_gte (datetime.datetime | Unset):
        start_time_hour (float | Unset):
        start_time_icontains (datetime.datetime | Unset):
        start_time_iendswith (datetime.datetime | Unset):
        start_time_iexact (datetime.datetime | Unset):
        start_time_in (list[datetime.datetime] | Unset):
        start_time_iregex (datetime.datetime | Unset):
        start_time_isnull (bool | Unset):
        start_time_iso_week_day (float | Unset):
        start_time_iso_year (float | Unset):
        start_time_istartswith (datetime.datetime | Unset):
        start_time_lt (datetime.datetime | Unset):
        start_time_lte (datetime.datetime | Unset):
        start_time_minute (float | Unset):
        start_time_month (float | Unset):
        start_time_quarter (float | Unset):
        start_time_range (list[datetime.datetime] | Unset):
        start_time_regex (datetime.datetime | Unset):
        start_time_second (float | Unset):
        start_time_startswith (datetime.datetime | Unset):
        start_time_time (str | Unset):
        start_time_week (float | Unset):
        start_time_week_day (float | Unset):
        start_time_year (float | Unset):

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
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
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
        observation=observation,
        observation_phenomenon_time=observation_phenomenon_time,
        observation_phenomenon_time_in=observation_phenomenon_time_in,
        observation_phenomenon_time_isnull=observation_phenomenon_time_isnull,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
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
    end_time: datetime.datetime | Unset = UNSET,
    end_time_contained_by: datetime.datetime | Unset = UNSET,
    end_time_contains: datetime.datetime | Unset = UNSET,
    end_time_date: datetime.date | Unset = UNSET,
    end_time_day: float | Unset = UNSET,
    end_time_endswith: datetime.datetime | Unset = UNSET,
    end_time_gt: datetime.datetime | Unset = UNSET,
    end_time_gte: datetime.datetime | Unset = UNSET,
    end_time_hour: float | Unset = UNSET,
    end_time_icontains: datetime.datetime | Unset = UNSET,
    end_time_iendswith: datetime.datetime | Unset = UNSET,
    end_time_iexact: datetime.datetime | Unset = UNSET,
    end_time_in: list[datetime.datetime] | Unset = UNSET,
    end_time_iregex: datetime.datetime | Unset = UNSET,
    end_time_isnull: bool | Unset = UNSET,
    end_time_iso_week_day: float | Unset = UNSET,
    end_time_iso_year: float | Unset = UNSET,
    end_time_istartswith: datetime.datetime | Unset = UNSET,
    end_time_lt: datetime.datetime | Unset = UNSET,
    end_time_lte: datetime.datetime | Unset = UNSET,
    end_time_minute: float | Unset = UNSET,
    end_time_month: float | Unset = UNSET,
    end_time_quarter: float | Unset = UNSET,
    end_time_range: list[datetime.datetime] | Unset = UNSET,
    end_time_regex: datetime.datetime | Unset = UNSET,
    end_time_second: float | Unset = UNSET,
    end_time_startswith: datetime.datetime | Unset = UNSET,
    end_time_time: str | Unset = UNSET,
    end_time_week: float | Unset = UNSET,
    end_time_week_day: float | Unset = UNSET,
    end_time_year: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_phenomenon_time: list[int] | Unset = UNSET,
    observation_phenomenon_time_in: list[int] | Unset = UNSET,
    observation_phenomenon_time_isnull: bool | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    start_time: datetime.datetime | Unset = UNSET,
    start_time_contained_by: datetime.datetime | Unset = UNSET,
    start_time_contains: datetime.datetime | Unset = UNSET,
    start_time_date: datetime.date | Unset = UNSET,
    start_time_day: float | Unset = UNSET,
    start_time_endswith: datetime.datetime | Unset = UNSET,
    start_time_gt: datetime.datetime | Unset = UNSET,
    start_time_gte: datetime.datetime | Unset = UNSET,
    start_time_hour: float | Unset = UNSET,
    start_time_icontains: datetime.datetime | Unset = UNSET,
    start_time_iendswith: datetime.datetime | Unset = UNSET,
    start_time_iexact: datetime.datetime | Unset = UNSET,
    start_time_in: list[datetime.datetime] | Unset = UNSET,
    start_time_iregex: datetime.datetime | Unset = UNSET,
    start_time_isnull: bool | Unset = UNSET,
    start_time_iso_week_day: float | Unset = UNSET,
    start_time_iso_year: float | Unset = UNSET,
    start_time_istartswith: datetime.datetime | Unset = UNSET,
    start_time_lt: datetime.datetime | Unset = UNSET,
    start_time_lte: datetime.datetime | Unset = UNSET,
    start_time_minute: float | Unset = UNSET,
    start_time_month: float | Unset = UNSET,
    start_time_quarter: float | Unset = UNSET,
    start_time_range: list[datetime.datetime] | Unset = UNSET,
    start_time_regex: datetime.datetime | Unset = UNSET,
    start_time_second: float | Unset = UNSET,
    start_time_startswith: datetime.datetime | Unset = UNSET,
    start_time_time: str | Unset = UNSET,
    start_time_week: float | Unset = UNSET,
    start_time_week_day: float | Unset = UNSET,
    start_time_year: float | Unset = UNSET,
) -> PaginatedTimePeriodList | None:
    """Get a list of TimePeriod objects. TimePeriods have a 1:1 use with many types of principal record
    types.

    Args:
        end_time (datetime.datetime | Unset):
        end_time_contained_by (datetime.datetime | Unset):
        end_time_contains (datetime.datetime | Unset):
        end_time_date (datetime.date | Unset):
        end_time_day (float | Unset):
        end_time_endswith (datetime.datetime | Unset):
        end_time_gt (datetime.datetime | Unset):
        end_time_gte (datetime.datetime | Unset):
        end_time_hour (float | Unset):
        end_time_icontains (datetime.datetime | Unset):
        end_time_iendswith (datetime.datetime | Unset):
        end_time_iexact (datetime.datetime | Unset):
        end_time_in (list[datetime.datetime] | Unset):
        end_time_iregex (datetime.datetime | Unset):
        end_time_isnull (bool | Unset):
        end_time_iso_week_day (float | Unset):
        end_time_iso_year (float | Unset):
        end_time_istartswith (datetime.datetime | Unset):
        end_time_lt (datetime.datetime | Unset):
        end_time_lte (datetime.datetime | Unset):
        end_time_minute (float | Unset):
        end_time_month (float | Unset):
        end_time_quarter (float | Unset):
        end_time_range (list[datetime.datetime] | Unset):
        end_time_regex (datetime.datetime | Unset):
        end_time_second (float | Unset):
        end_time_startswith (datetime.datetime | Unset):
        end_time_time (str | Unset):
        end_time_week (float | Unset):
        end_time_week_day (float | Unset):
        end_time_year (float | Unset):
        limit (int | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
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
        observation (list[int] | Unset):
        observation_phenomenon_time (list[int] | Unset):
        observation_phenomenon_time_in (list[int] | Unset):
        observation_phenomenon_time_isnull (bool | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        start_time (datetime.datetime | Unset):
        start_time_contained_by (datetime.datetime | Unset):
        start_time_contains (datetime.datetime | Unset):
        start_time_date (datetime.date | Unset):
        start_time_day (float | Unset):
        start_time_endswith (datetime.datetime | Unset):
        start_time_gt (datetime.datetime | Unset):
        start_time_gte (datetime.datetime | Unset):
        start_time_hour (float | Unset):
        start_time_icontains (datetime.datetime | Unset):
        start_time_iendswith (datetime.datetime | Unset):
        start_time_iexact (datetime.datetime | Unset):
        start_time_in (list[datetime.datetime] | Unset):
        start_time_iregex (datetime.datetime | Unset):
        start_time_isnull (bool | Unset):
        start_time_iso_week_day (float | Unset):
        start_time_iso_year (float | Unset):
        start_time_istartswith (datetime.datetime | Unset):
        start_time_lt (datetime.datetime | Unset):
        start_time_lte (datetime.datetime | Unset):
        start_time_minute (float | Unset):
        start_time_month (float | Unset):
        start_time_quarter (float | Unset):
        start_time_range (list[datetime.datetime] | Unset):
        start_time_regex (datetime.datetime | Unset):
        start_time_second (float | Unset):
        start_time_startswith (datetime.datetime | Unset):
        start_time_time (str | Unset):
        start_time_week (float | Unset):
        start_time_week_day (float | Unset):
        start_time_year (float | Unset):

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
            mobileplatformoperation=mobileplatformoperation,
            mobileplatformoperation_in=mobileplatformoperation_in,
            mobileplatformoperation_isnull=mobileplatformoperation_isnull,
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
            observation=observation,
            observation_phenomenon_time=observation_phenomenon_time,
            observation_phenomenon_time_in=observation_phenomenon_time_in,
            observation_phenomenon_time_isnull=observation_phenomenon_time_isnull,
            observation_in=observation_in,
            observation_isnull=observation_isnull,
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
