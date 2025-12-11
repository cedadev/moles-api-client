import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_dq_conformance_result_read_list import PaginatedDQConformanceResultReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date | Unset = UNSET,
    date_contained_by: datetime.date | Unset = UNSET,
    date_contains: datetime.date | Unset = UNSET,
    date_day: float | Unset = UNSET,
    date_endswith: datetime.date | Unset = UNSET,
    date_gt: datetime.date | Unset = UNSET,
    date_gte: datetime.date | Unset = UNSET,
    date_icontains: datetime.date | Unset = UNSET,
    date_iendswith: datetime.date | Unset = UNSET,
    date_iexact: datetime.date | Unset = UNSET,
    date_in: list[datetime.date] | Unset = UNSET,
    date_iregex: datetime.date | Unset = UNSET,
    date_isnull: bool | Unset = UNSET,
    date_iso_week_day: float | Unset = UNSET,
    date_iso_year: float | Unset = UNSET,
    date_istartswith: datetime.date | Unset = UNSET,
    date_lt: datetime.date | Unset = UNSET,
    date_lte: datetime.date | Unset = UNSET,
    date_month: float | Unset = UNSET,
    date_quarter: float | Unset = UNSET,
    date_range: list[datetime.date] | Unset = UNSET,
    date_regex: datetime.date | Unset = UNSET,
    date_startswith: datetime.date | Unset = UNSET,
    date_week: float | Unset = UNSET,
    date_week_day: float | Unset = UNSET,
    date_year: float | Unset = UNSET,
    explanation: str | Unset = UNSET,
    explanation_contains: str | Unset = UNSET,
    explanation_endswith: str | Unset = UNSET,
    explanation_gt: str | Unset = UNSET,
    explanation_gte: str | Unset = UNSET,
    explanation_icontains: str | Unset = UNSET,
    explanation_iendswith: str | Unset = UNSET,
    explanation_iexact: str | Unset = UNSET,
    explanation_in: list[str] | Unset = UNSET,
    explanation_iregex: str | Unset = UNSET,
    explanation_isnull: bool | Unset = UNSET,
    explanation_istartswith: str | Unset = UNSET,
    explanation_lt: str | Unset = UNSET,
    explanation_lte: str | Unset = UNSET,
    explanation_range: list[str] | Unset = UNSET,
    explanation_regex: str | Unset = UNSET,
    explanation_startswith: str | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    passes_test: bool | Unset = UNSET,
    passes_test_contains: bool | Unset = UNSET,
    passes_test_endswith: bool | Unset = UNSET,
    passes_test_gt: bool | Unset = UNSET,
    passes_test_gte: bool | Unset = UNSET,
    passes_test_icontains: bool | Unset = UNSET,
    passes_test_iendswith: bool | Unset = UNSET,
    passes_test_iexact: bool | Unset = UNSET,
    passes_test_in: list[bool] | Unset = UNSET,
    passes_test_iregex: bool | Unset = UNSET,
    passes_test_isnull: bool | Unset = UNSET,
    passes_test_istartswith: bool | Unset = UNSET,
    passes_test_lt: bool | Unset = UNSET,
    passes_test_lte: bool | Unset = UNSET,
    passes_test_range: list[bool] | Unset = UNSET,
    passes_test_regex: bool | Unset = UNSET,
    passes_test_startswith: bool | Unset = UNSET,
    result_title: str | Unset = UNSET,
    result_title_contains: str | Unset = UNSET,
    result_title_endswith: str | Unset = UNSET,
    result_title_gt: str | Unset = UNSET,
    result_title_gte: str | Unset = UNSET,
    result_title_icontains: str | Unset = UNSET,
    result_title_iendswith: str | Unset = UNSET,
    result_title_iexact: str | Unset = UNSET,
    result_title_in: list[str] | Unset = UNSET,
    result_title_iregex: str | Unset = UNSET,
    result_title_isnull: bool | Unset = UNSET,
    result_title_istartswith: str | Unset = UNSET,
    result_title_lt: str | Unset = UNSET,
    result_title_lte: str | Unset = UNSET,
    result_title_range: list[str] | Unset = UNSET,
    result_title_regex: str | Unset = UNSET,
    result_title_startswith: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    json_date_contained_by: str | Unset = UNSET
    if not isinstance(date_contained_by, Unset):
        json_date_contained_by = date_contained_by.isoformat()
    params["date__contained_by"] = json_date_contained_by

    json_date_contains: str | Unset = UNSET
    if not isinstance(date_contains, Unset):
        json_date_contains = date_contains.isoformat()
    params["date__contains"] = json_date_contains

    params["date__day"] = date_day

    json_date_endswith: str | Unset = UNSET
    if not isinstance(date_endswith, Unset):
        json_date_endswith = date_endswith.isoformat()
    params["date__endswith"] = json_date_endswith

    json_date_gt: str | Unset = UNSET
    if not isinstance(date_gt, Unset):
        json_date_gt = date_gt.isoformat()
    params["date__gt"] = json_date_gt

    json_date_gte: str | Unset = UNSET
    if not isinstance(date_gte, Unset):
        json_date_gte = date_gte.isoformat()
    params["date__gte"] = json_date_gte

    json_date_icontains: str | Unset = UNSET
    if not isinstance(date_icontains, Unset):
        json_date_icontains = date_icontains.isoformat()
    params["date__icontains"] = json_date_icontains

    json_date_iendswith: str | Unset = UNSET
    if not isinstance(date_iendswith, Unset):
        json_date_iendswith = date_iendswith.isoformat()
    params["date__iendswith"] = json_date_iendswith

    json_date_iexact: str | Unset = UNSET
    if not isinstance(date_iexact, Unset):
        json_date_iexact = date_iexact.isoformat()
    params["date__iexact"] = json_date_iexact

    json_date_in: list[str] | Unset = UNSET
    if not isinstance(date_in, Unset):
        json_date_in = []
        for date_in_item_data in date_in:
            date_in_item = date_in_item_data.isoformat()
            json_date_in.append(date_in_item)

    params["date__in"] = json_date_in

    json_date_iregex: str | Unset = UNSET
    if not isinstance(date_iregex, Unset):
        json_date_iregex = date_iregex.isoformat()
    params["date__iregex"] = json_date_iregex

    params["date__isnull"] = date_isnull

    params["date__iso_week_day"] = date_iso_week_day

    params["date__iso_year"] = date_iso_year

    json_date_istartswith: str | Unset = UNSET
    if not isinstance(date_istartswith, Unset):
        json_date_istartswith = date_istartswith.isoformat()
    params["date__istartswith"] = json_date_istartswith

    json_date_lt: str | Unset = UNSET
    if not isinstance(date_lt, Unset):
        json_date_lt = date_lt.isoformat()
    params["date__lt"] = json_date_lt

    json_date_lte: str | Unset = UNSET
    if not isinstance(date_lte, Unset):
        json_date_lte = date_lte.isoformat()
    params["date__lte"] = json_date_lte

    params["date__month"] = date_month

    params["date__quarter"] = date_quarter

    json_date_range: list[str] | Unset = UNSET
    if not isinstance(date_range, Unset):
        json_date_range = []
        for date_range_item_data in date_range:
            date_range_item = date_range_item_data.isoformat()
            json_date_range.append(date_range_item)

    params["date__range"] = json_date_range

    json_date_regex: str | Unset = UNSET
    if not isinstance(date_regex, Unset):
        json_date_regex = date_regex.isoformat()
    params["date__regex"] = json_date_regex

    json_date_startswith: str | Unset = UNSET
    if not isinstance(date_startswith, Unset):
        json_date_startswith = date_startswith.isoformat()
    params["date__startswith"] = json_date_startswith

    params["date__week"] = date_week

    params["date__week_day"] = date_week_day

    params["date__year"] = date_year

    params["explanation"] = explanation

    params["explanation__contains"] = explanation_contains

    params["explanation__endswith"] = explanation_endswith

    params["explanation__gt"] = explanation_gt

    params["explanation__gte"] = explanation_gte

    params["explanation__icontains"] = explanation_icontains

    params["explanation__iendswith"] = explanation_iendswith

    params["explanation__iexact"] = explanation_iexact

    json_explanation_in: list[str] | Unset = UNSET
    if not isinstance(explanation_in, Unset):
        json_explanation_in = explanation_in

    params["explanation__in"] = json_explanation_in

    params["explanation__iregex"] = explanation_iregex

    params["explanation__isnull"] = explanation_isnull

    params["explanation__istartswith"] = explanation_istartswith

    params["explanation__lt"] = explanation_lt

    params["explanation__lte"] = explanation_lte

    json_explanation_range: list[str] | Unset = UNSET
    if not isinstance(explanation_range, Unset):
        json_explanation_range = explanation_range

    params["explanation__range"] = json_explanation_range

    params["explanation__regex"] = explanation_regex

    params["explanation__startswith"] = explanation_startswith

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
        json_ob_id_in = ob_id_in

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: list[int] | Unset = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ob_id_range

    params["ob_id__range"] = json_ob_id_range

    params["ob_id__regex"] = ob_id_regex

    params["ob_id__startswith"] = ob_id_startswith

    json_observation: list[int] | Unset = UNSET
    if not isinstance(observation, Unset):
        json_observation = observation

    params["observation"] = json_observation

    json_observation_in: list[int] | Unset = UNSET
    if not isinstance(observation_in, Unset):
        json_observation_in = observation_in

    params["observation__in"] = json_observation_in

    params["observation__isnull"] = observation_isnull

    params["offset"] = offset

    params["ordering"] = ordering

    params["passesTest"] = passes_test

    params["passesTest__contains"] = passes_test_contains

    params["passesTest__endswith"] = passes_test_endswith

    params["passesTest__gt"] = passes_test_gt

    params["passesTest__gte"] = passes_test_gte

    params["passesTest__icontains"] = passes_test_icontains

    params["passesTest__iendswith"] = passes_test_iendswith

    params["passesTest__iexact"] = passes_test_iexact

    json_passes_test_in: list[bool] | Unset = UNSET
    if not isinstance(passes_test_in, Unset):
        json_passes_test_in = passes_test_in

    params["passesTest__in"] = json_passes_test_in

    params["passesTest__iregex"] = passes_test_iregex

    params["passesTest__isnull"] = passes_test_isnull

    params["passesTest__istartswith"] = passes_test_istartswith

    params["passesTest__lt"] = passes_test_lt

    params["passesTest__lte"] = passes_test_lte

    json_passes_test_range: list[bool] | Unset = UNSET
    if not isinstance(passes_test_range, Unset):
        json_passes_test_range = passes_test_range

    params["passesTest__range"] = json_passes_test_range

    params["passesTest__regex"] = passes_test_regex

    params["passesTest__startswith"] = passes_test_startswith

    params["resultTitle"] = result_title

    params["resultTitle__contains"] = result_title_contains

    params["resultTitle__endswith"] = result_title_endswith

    params["resultTitle__gt"] = result_title_gt

    params["resultTitle__gte"] = result_title_gte

    params["resultTitle__icontains"] = result_title_icontains

    params["resultTitle__iendswith"] = result_title_iendswith

    params["resultTitle__iexact"] = result_title_iexact

    json_result_title_in: list[str] | Unset = UNSET
    if not isinstance(result_title_in, Unset):
        json_result_title_in = result_title_in

    params["resultTitle__in"] = json_result_title_in

    params["resultTitle__iregex"] = result_title_iregex

    params["resultTitle__isnull"] = result_title_isnull

    params["resultTitle__istartswith"] = result_title_istartswith

    params["resultTitle__lt"] = result_title_lt

    params["resultTitle__lte"] = result_title_lte

    json_result_title_range: list[str] | Unset = UNSET
    if not isinstance(result_title_range, Unset):
        json_result_title_range = result_title_range

    params["resultTitle__range"] = json_result_title_range

    params["resultTitle__regex"] = result_title_regex

    params["resultTitle__startswith"] = result_title_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/dqconformanceresults/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedDQConformanceResultReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedDQConformanceResultReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedDQConformanceResultReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    date_contained_by: datetime.date | Unset = UNSET,
    date_contains: datetime.date | Unset = UNSET,
    date_day: float | Unset = UNSET,
    date_endswith: datetime.date | Unset = UNSET,
    date_gt: datetime.date | Unset = UNSET,
    date_gte: datetime.date | Unset = UNSET,
    date_icontains: datetime.date | Unset = UNSET,
    date_iendswith: datetime.date | Unset = UNSET,
    date_iexact: datetime.date | Unset = UNSET,
    date_in: list[datetime.date] | Unset = UNSET,
    date_iregex: datetime.date | Unset = UNSET,
    date_isnull: bool | Unset = UNSET,
    date_iso_week_day: float | Unset = UNSET,
    date_iso_year: float | Unset = UNSET,
    date_istartswith: datetime.date | Unset = UNSET,
    date_lt: datetime.date | Unset = UNSET,
    date_lte: datetime.date | Unset = UNSET,
    date_month: float | Unset = UNSET,
    date_quarter: float | Unset = UNSET,
    date_range: list[datetime.date] | Unset = UNSET,
    date_regex: datetime.date | Unset = UNSET,
    date_startswith: datetime.date | Unset = UNSET,
    date_week: float | Unset = UNSET,
    date_week_day: float | Unset = UNSET,
    date_year: float | Unset = UNSET,
    explanation: str | Unset = UNSET,
    explanation_contains: str | Unset = UNSET,
    explanation_endswith: str | Unset = UNSET,
    explanation_gt: str | Unset = UNSET,
    explanation_gte: str | Unset = UNSET,
    explanation_icontains: str | Unset = UNSET,
    explanation_iendswith: str | Unset = UNSET,
    explanation_iexact: str | Unset = UNSET,
    explanation_in: list[str] | Unset = UNSET,
    explanation_iregex: str | Unset = UNSET,
    explanation_isnull: bool | Unset = UNSET,
    explanation_istartswith: str | Unset = UNSET,
    explanation_lt: str | Unset = UNSET,
    explanation_lte: str | Unset = UNSET,
    explanation_range: list[str] | Unset = UNSET,
    explanation_regex: str | Unset = UNSET,
    explanation_startswith: str | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    passes_test: bool | Unset = UNSET,
    passes_test_contains: bool | Unset = UNSET,
    passes_test_endswith: bool | Unset = UNSET,
    passes_test_gt: bool | Unset = UNSET,
    passes_test_gte: bool | Unset = UNSET,
    passes_test_icontains: bool | Unset = UNSET,
    passes_test_iendswith: bool | Unset = UNSET,
    passes_test_iexact: bool | Unset = UNSET,
    passes_test_in: list[bool] | Unset = UNSET,
    passes_test_iregex: bool | Unset = UNSET,
    passes_test_isnull: bool | Unset = UNSET,
    passes_test_istartswith: bool | Unset = UNSET,
    passes_test_lt: bool | Unset = UNSET,
    passes_test_lte: bool | Unset = UNSET,
    passes_test_range: list[bool] | Unset = UNSET,
    passes_test_regex: bool | Unset = UNSET,
    passes_test_startswith: bool | Unset = UNSET,
    result_title: str | Unset = UNSET,
    result_title_contains: str | Unset = UNSET,
    result_title_endswith: str | Unset = UNSET,
    result_title_gt: str | Unset = UNSET,
    result_title_gte: str | Unset = UNSET,
    result_title_icontains: str | Unset = UNSET,
    result_title_iendswith: str | Unset = UNSET,
    result_title_iexact: str | Unset = UNSET,
    result_title_in: list[str] | Unset = UNSET,
    result_title_iregex: str | Unset = UNSET,
    result_title_isnull: bool | Unset = UNSET,
    result_title_istartswith: str | Unset = UNSET,
    result_title_lt: str | Unset = UNSET,
    result_title_lte: str | Unset = UNSET,
    result_title_range: list[str] | Unset = UNSET,
    result_title_regex: str | Unset = UNSET,
    result_title_startswith: str | Unset = UNSET,
) -> Response[PaginatedDQConformanceResultReadList]:
    """Get a list of DQConformanceResult objects.

    Args:
        date (datetime.date | Unset):
        date_contained_by (datetime.date | Unset):
        date_contains (datetime.date | Unset):
        date_day (float | Unset):
        date_endswith (datetime.date | Unset):
        date_gt (datetime.date | Unset):
        date_gte (datetime.date | Unset):
        date_icontains (datetime.date | Unset):
        date_iendswith (datetime.date | Unset):
        date_iexact (datetime.date | Unset):
        date_in (list[datetime.date] | Unset):
        date_iregex (datetime.date | Unset):
        date_isnull (bool | Unset):
        date_iso_week_day (float | Unset):
        date_iso_year (float | Unset):
        date_istartswith (datetime.date | Unset):
        date_lt (datetime.date | Unset):
        date_lte (datetime.date | Unset):
        date_month (float | Unset):
        date_quarter (float | Unset):
        date_range (list[datetime.date] | Unset):
        date_regex (datetime.date | Unset):
        date_startswith (datetime.date | Unset):
        date_week (float | Unset):
        date_week_day (float | Unset):
        date_year (float | Unset):
        explanation (str | Unset):
        explanation_contains (str | Unset):
        explanation_endswith (str | Unset):
        explanation_gt (str | Unset):
        explanation_gte (str | Unset):
        explanation_icontains (str | Unset):
        explanation_iendswith (str | Unset):
        explanation_iexact (str | Unset):
        explanation_in (list[str] | Unset):
        explanation_iregex (str | Unset):
        explanation_isnull (bool | Unset):
        explanation_istartswith (str | Unset):
        explanation_lt (str | Unset):
        explanation_lte (str | Unset):
        explanation_range (list[str] | Unset):
        explanation_regex (str | Unset):
        explanation_startswith (str | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        passes_test (bool | Unset):
        passes_test_contains (bool | Unset):
        passes_test_endswith (bool | Unset):
        passes_test_gt (bool | Unset):
        passes_test_gte (bool | Unset):
        passes_test_icontains (bool | Unset):
        passes_test_iendswith (bool | Unset):
        passes_test_iexact (bool | Unset):
        passes_test_in (list[bool] | Unset):
        passes_test_iregex (bool | Unset):
        passes_test_isnull (bool | Unset):
        passes_test_istartswith (bool | Unset):
        passes_test_lt (bool | Unset):
        passes_test_lte (bool | Unset):
        passes_test_range (list[bool] | Unset):
        passes_test_regex (bool | Unset):
        passes_test_startswith (bool | Unset):
        result_title (str | Unset):
        result_title_contains (str | Unset):
        result_title_endswith (str | Unset):
        result_title_gt (str | Unset):
        result_title_gte (str | Unset):
        result_title_icontains (str | Unset):
        result_title_iendswith (str | Unset):
        result_title_iexact (str | Unset):
        result_title_in (list[str] | Unset):
        result_title_iregex (str | Unset):
        result_title_isnull (bool | Unset):
        result_title_istartswith (str | Unset):
        result_title_lt (str | Unset):
        result_title_lte (str | Unset):
        result_title_range (list[str] | Unset):
        result_title_regex (str | Unset):
        result_title_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDQConformanceResultReadList]
    """

    kwargs = _get_kwargs(
        date=date,
        date_contained_by=date_contained_by,
        date_contains=date_contains,
        date_day=date_day,
        date_endswith=date_endswith,
        date_gt=date_gt,
        date_gte=date_gte,
        date_icontains=date_icontains,
        date_iendswith=date_iendswith,
        date_iexact=date_iexact,
        date_in=date_in,
        date_iregex=date_iregex,
        date_isnull=date_isnull,
        date_iso_week_day=date_iso_week_day,
        date_iso_year=date_iso_year,
        date_istartswith=date_istartswith,
        date_lt=date_lt,
        date_lte=date_lte,
        date_month=date_month,
        date_quarter=date_quarter,
        date_range=date_range,
        date_regex=date_regex,
        date_startswith=date_startswith,
        date_week=date_week,
        date_week_day=date_week_day,
        date_year=date_year,
        explanation=explanation,
        explanation_contains=explanation_contains,
        explanation_endswith=explanation_endswith,
        explanation_gt=explanation_gt,
        explanation_gte=explanation_gte,
        explanation_icontains=explanation_icontains,
        explanation_iendswith=explanation_iendswith,
        explanation_iexact=explanation_iexact,
        explanation_in=explanation_in,
        explanation_iregex=explanation_iregex,
        explanation_isnull=explanation_isnull,
        explanation_istartswith=explanation_istartswith,
        explanation_lt=explanation_lt,
        explanation_lte=explanation_lte,
        explanation_range=explanation_range,
        explanation_regex=explanation_regex,
        explanation_startswith=explanation_startswith,
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
        offset=offset,
        ordering=ordering,
        passes_test=passes_test,
        passes_test_contains=passes_test_contains,
        passes_test_endswith=passes_test_endswith,
        passes_test_gt=passes_test_gt,
        passes_test_gte=passes_test_gte,
        passes_test_icontains=passes_test_icontains,
        passes_test_iendswith=passes_test_iendswith,
        passes_test_iexact=passes_test_iexact,
        passes_test_in=passes_test_in,
        passes_test_iregex=passes_test_iregex,
        passes_test_isnull=passes_test_isnull,
        passes_test_istartswith=passes_test_istartswith,
        passes_test_lt=passes_test_lt,
        passes_test_lte=passes_test_lte,
        passes_test_range=passes_test_range,
        passes_test_regex=passes_test_regex,
        passes_test_startswith=passes_test_startswith,
        result_title=result_title,
        result_title_contains=result_title_contains,
        result_title_endswith=result_title_endswith,
        result_title_gt=result_title_gt,
        result_title_gte=result_title_gte,
        result_title_icontains=result_title_icontains,
        result_title_iendswith=result_title_iendswith,
        result_title_iexact=result_title_iexact,
        result_title_in=result_title_in,
        result_title_iregex=result_title_iregex,
        result_title_isnull=result_title_isnull,
        result_title_istartswith=result_title_istartswith,
        result_title_lt=result_title_lt,
        result_title_lte=result_title_lte,
        result_title_range=result_title_range,
        result_title_regex=result_title_regex,
        result_title_startswith=result_title_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    date_contained_by: datetime.date | Unset = UNSET,
    date_contains: datetime.date | Unset = UNSET,
    date_day: float | Unset = UNSET,
    date_endswith: datetime.date | Unset = UNSET,
    date_gt: datetime.date | Unset = UNSET,
    date_gte: datetime.date | Unset = UNSET,
    date_icontains: datetime.date | Unset = UNSET,
    date_iendswith: datetime.date | Unset = UNSET,
    date_iexact: datetime.date | Unset = UNSET,
    date_in: list[datetime.date] | Unset = UNSET,
    date_iregex: datetime.date | Unset = UNSET,
    date_isnull: bool | Unset = UNSET,
    date_iso_week_day: float | Unset = UNSET,
    date_iso_year: float | Unset = UNSET,
    date_istartswith: datetime.date | Unset = UNSET,
    date_lt: datetime.date | Unset = UNSET,
    date_lte: datetime.date | Unset = UNSET,
    date_month: float | Unset = UNSET,
    date_quarter: float | Unset = UNSET,
    date_range: list[datetime.date] | Unset = UNSET,
    date_regex: datetime.date | Unset = UNSET,
    date_startswith: datetime.date | Unset = UNSET,
    date_week: float | Unset = UNSET,
    date_week_day: float | Unset = UNSET,
    date_year: float | Unset = UNSET,
    explanation: str | Unset = UNSET,
    explanation_contains: str | Unset = UNSET,
    explanation_endswith: str | Unset = UNSET,
    explanation_gt: str | Unset = UNSET,
    explanation_gte: str | Unset = UNSET,
    explanation_icontains: str | Unset = UNSET,
    explanation_iendswith: str | Unset = UNSET,
    explanation_iexact: str | Unset = UNSET,
    explanation_in: list[str] | Unset = UNSET,
    explanation_iregex: str | Unset = UNSET,
    explanation_isnull: bool | Unset = UNSET,
    explanation_istartswith: str | Unset = UNSET,
    explanation_lt: str | Unset = UNSET,
    explanation_lte: str | Unset = UNSET,
    explanation_range: list[str] | Unset = UNSET,
    explanation_regex: str | Unset = UNSET,
    explanation_startswith: str | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    passes_test: bool | Unset = UNSET,
    passes_test_contains: bool | Unset = UNSET,
    passes_test_endswith: bool | Unset = UNSET,
    passes_test_gt: bool | Unset = UNSET,
    passes_test_gte: bool | Unset = UNSET,
    passes_test_icontains: bool | Unset = UNSET,
    passes_test_iendswith: bool | Unset = UNSET,
    passes_test_iexact: bool | Unset = UNSET,
    passes_test_in: list[bool] | Unset = UNSET,
    passes_test_iregex: bool | Unset = UNSET,
    passes_test_isnull: bool | Unset = UNSET,
    passes_test_istartswith: bool | Unset = UNSET,
    passes_test_lt: bool | Unset = UNSET,
    passes_test_lte: bool | Unset = UNSET,
    passes_test_range: list[bool] | Unset = UNSET,
    passes_test_regex: bool | Unset = UNSET,
    passes_test_startswith: bool | Unset = UNSET,
    result_title: str | Unset = UNSET,
    result_title_contains: str | Unset = UNSET,
    result_title_endswith: str | Unset = UNSET,
    result_title_gt: str | Unset = UNSET,
    result_title_gte: str | Unset = UNSET,
    result_title_icontains: str | Unset = UNSET,
    result_title_iendswith: str | Unset = UNSET,
    result_title_iexact: str | Unset = UNSET,
    result_title_in: list[str] | Unset = UNSET,
    result_title_iregex: str | Unset = UNSET,
    result_title_isnull: bool | Unset = UNSET,
    result_title_istartswith: str | Unset = UNSET,
    result_title_lt: str | Unset = UNSET,
    result_title_lte: str | Unset = UNSET,
    result_title_range: list[str] | Unset = UNSET,
    result_title_regex: str | Unset = UNSET,
    result_title_startswith: str | Unset = UNSET,
) -> PaginatedDQConformanceResultReadList | None:
    """Get a list of DQConformanceResult objects.

    Args:
        date (datetime.date | Unset):
        date_contained_by (datetime.date | Unset):
        date_contains (datetime.date | Unset):
        date_day (float | Unset):
        date_endswith (datetime.date | Unset):
        date_gt (datetime.date | Unset):
        date_gte (datetime.date | Unset):
        date_icontains (datetime.date | Unset):
        date_iendswith (datetime.date | Unset):
        date_iexact (datetime.date | Unset):
        date_in (list[datetime.date] | Unset):
        date_iregex (datetime.date | Unset):
        date_isnull (bool | Unset):
        date_iso_week_day (float | Unset):
        date_iso_year (float | Unset):
        date_istartswith (datetime.date | Unset):
        date_lt (datetime.date | Unset):
        date_lte (datetime.date | Unset):
        date_month (float | Unset):
        date_quarter (float | Unset):
        date_range (list[datetime.date] | Unset):
        date_regex (datetime.date | Unset):
        date_startswith (datetime.date | Unset):
        date_week (float | Unset):
        date_week_day (float | Unset):
        date_year (float | Unset):
        explanation (str | Unset):
        explanation_contains (str | Unset):
        explanation_endswith (str | Unset):
        explanation_gt (str | Unset):
        explanation_gte (str | Unset):
        explanation_icontains (str | Unset):
        explanation_iendswith (str | Unset):
        explanation_iexact (str | Unset):
        explanation_in (list[str] | Unset):
        explanation_iregex (str | Unset):
        explanation_isnull (bool | Unset):
        explanation_istartswith (str | Unset):
        explanation_lt (str | Unset):
        explanation_lte (str | Unset):
        explanation_range (list[str] | Unset):
        explanation_regex (str | Unset):
        explanation_startswith (str | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        passes_test (bool | Unset):
        passes_test_contains (bool | Unset):
        passes_test_endswith (bool | Unset):
        passes_test_gt (bool | Unset):
        passes_test_gte (bool | Unset):
        passes_test_icontains (bool | Unset):
        passes_test_iendswith (bool | Unset):
        passes_test_iexact (bool | Unset):
        passes_test_in (list[bool] | Unset):
        passes_test_iregex (bool | Unset):
        passes_test_isnull (bool | Unset):
        passes_test_istartswith (bool | Unset):
        passes_test_lt (bool | Unset):
        passes_test_lte (bool | Unset):
        passes_test_range (list[bool] | Unset):
        passes_test_regex (bool | Unset):
        passes_test_startswith (bool | Unset):
        result_title (str | Unset):
        result_title_contains (str | Unset):
        result_title_endswith (str | Unset):
        result_title_gt (str | Unset):
        result_title_gte (str | Unset):
        result_title_icontains (str | Unset):
        result_title_iendswith (str | Unset):
        result_title_iexact (str | Unset):
        result_title_in (list[str] | Unset):
        result_title_iregex (str | Unset):
        result_title_isnull (bool | Unset):
        result_title_istartswith (str | Unset):
        result_title_lt (str | Unset):
        result_title_lte (str | Unset):
        result_title_range (list[str] | Unset):
        result_title_regex (str | Unset):
        result_title_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDQConformanceResultReadList
    """

    return sync_detailed(
        client=client,
        date=date,
        date_contained_by=date_contained_by,
        date_contains=date_contains,
        date_day=date_day,
        date_endswith=date_endswith,
        date_gt=date_gt,
        date_gte=date_gte,
        date_icontains=date_icontains,
        date_iendswith=date_iendswith,
        date_iexact=date_iexact,
        date_in=date_in,
        date_iregex=date_iregex,
        date_isnull=date_isnull,
        date_iso_week_day=date_iso_week_day,
        date_iso_year=date_iso_year,
        date_istartswith=date_istartswith,
        date_lt=date_lt,
        date_lte=date_lte,
        date_month=date_month,
        date_quarter=date_quarter,
        date_range=date_range,
        date_regex=date_regex,
        date_startswith=date_startswith,
        date_week=date_week,
        date_week_day=date_week_day,
        date_year=date_year,
        explanation=explanation,
        explanation_contains=explanation_contains,
        explanation_endswith=explanation_endswith,
        explanation_gt=explanation_gt,
        explanation_gte=explanation_gte,
        explanation_icontains=explanation_icontains,
        explanation_iendswith=explanation_iendswith,
        explanation_iexact=explanation_iexact,
        explanation_in=explanation_in,
        explanation_iregex=explanation_iregex,
        explanation_isnull=explanation_isnull,
        explanation_istartswith=explanation_istartswith,
        explanation_lt=explanation_lt,
        explanation_lte=explanation_lte,
        explanation_range=explanation_range,
        explanation_regex=explanation_regex,
        explanation_startswith=explanation_startswith,
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
        offset=offset,
        ordering=ordering,
        passes_test=passes_test,
        passes_test_contains=passes_test_contains,
        passes_test_endswith=passes_test_endswith,
        passes_test_gt=passes_test_gt,
        passes_test_gte=passes_test_gte,
        passes_test_icontains=passes_test_icontains,
        passes_test_iendswith=passes_test_iendswith,
        passes_test_iexact=passes_test_iexact,
        passes_test_in=passes_test_in,
        passes_test_iregex=passes_test_iregex,
        passes_test_isnull=passes_test_isnull,
        passes_test_istartswith=passes_test_istartswith,
        passes_test_lt=passes_test_lt,
        passes_test_lte=passes_test_lte,
        passes_test_range=passes_test_range,
        passes_test_regex=passes_test_regex,
        passes_test_startswith=passes_test_startswith,
        result_title=result_title,
        result_title_contains=result_title_contains,
        result_title_endswith=result_title_endswith,
        result_title_gt=result_title_gt,
        result_title_gte=result_title_gte,
        result_title_icontains=result_title_icontains,
        result_title_iendswith=result_title_iendswith,
        result_title_iexact=result_title_iexact,
        result_title_in=result_title_in,
        result_title_iregex=result_title_iregex,
        result_title_isnull=result_title_isnull,
        result_title_istartswith=result_title_istartswith,
        result_title_lt=result_title_lt,
        result_title_lte=result_title_lte,
        result_title_range=result_title_range,
        result_title_regex=result_title_regex,
        result_title_startswith=result_title_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    date_contained_by: datetime.date | Unset = UNSET,
    date_contains: datetime.date | Unset = UNSET,
    date_day: float | Unset = UNSET,
    date_endswith: datetime.date | Unset = UNSET,
    date_gt: datetime.date | Unset = UNSET,
    date_gte: datetime.date | Unset = UNSET,
    date_icontains: datetime.date | Unset = UNSET,
    date_iendswith: datetime.date | Unset = UNSET,
    date_iexact: datetime.date | Unset = UNSET,
    date_in: list[datetime.date] | Unset = UNSET,
    date_iregex: datetime.date | Unset = UNSET,
    date_isnull: bool | Unset = UNSET,
    date_iso_week_day: float | Unset = UNSET,
    date_iso_year: float | Unset = UNSET,
    date_istartswith: datetime.date | Unset = UNSET,
    date_lt: datetime.date | Unset = UNSET,
    date_lte: datetime.date | Unset = UNSET,
    date_month: float | Unset = UNSET,
    date_quarter: float | Unset = UNSET,
    date_range: list[datetime.date] | Unset = UNSET,
    date_regex: datetime.date | Unset = UNSET,
    date_startswith: datetime.date | Unset = UNSET,
    date_week: float | Unset = UNSET,
    date_week_day: float | Unset = UNSET,
    date_year: float | Unset = UNSET,
    explanation: str | Unset = UNSET,
    explanation_contains: str | Unset = UNSET,
    explanation_endswith: str | Unset = UNSET,
    explanation_gt: str | Unset = UNSET,
    explanation_gte: str | Unset = UNSET,
    explanation_icontains: str | Unset = UNSET,
    explanation_iendswith: str | Unset = UNSET,
    explanation_iexact: str | Unset = UNSET,
    explanation_in: list[str] | Unset = UNSET,
    explanation_iregex: str | Unset = UNSET,
    explanation_isnull: bool | Unset = UNSET,
    explanation_istartswith: str | Unset = UNSET,
    explanation_lt: str | Unset = UNSET,
    explanation_lte: str | Unset = UNSET,
    explanation_range: list[str] | Unset = UNSET,
    explanation_regex: str | Unset = UNSET,
    explanation_startswith: str | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    passes_test: bool | Unset = UNSET,
    passes_test_contains: bool | Unset = UNSET,
    passes_test_endswith: bool | Unset = UNSET,
    passes_test_gt: bool | Unset = UNSET,
    passes_test_gte: bool | Unset = UNSET,
    passes_test_icontains: bool | Unset = UNSET,
    passes_test_iendswith: bool | Unset = UNSET,
    passes_test_iexact: bool | Unset = UNSET,
    passes_test_in: list[bool] | Unset = UNSET,
    passes_test_iregex: bool | Unset = UNSET,
    passes_test_isnull: bool | Unset = UNSET,
    passes_test_istartswith: bool | Unset = UNSET,
    passes_test_lt: bool | Unset = UNSET,
    passes_test_lte: bool | Unset = UNSET,
    passes_test_range: list[bool] | Unset = UNSET,
    passes_test_regex: bool | Unset = UNSET,
    passes_test_startswith: bool | Unset = UNSET,
    result_title: str | Unset = UNSET,
    result_title_contains: str | Unset = UNSET,
    result_title_endswith: str | Unset = UNSET,
    result_title_gt: str | Unset = UNSET,
    result_title_gte: str | Unset = UNSET,
    result_title_icontains: str | Unset = UNSET,
    result_title_iendswith: str | Unset = UNSET,
    result_title_iexact: str | Unset = UNSET,
    result_title_in: list[str] | Unset = UNSET,
    result_title_iregex: str | Unset = UNSET,
    result_title_isnull: bool | Unset = UNSET,
    result_title_istartswith: str | Unset = UNSET,
    result_title_lt: str | Unset = UNSET,
    result_title_lte: str | Unset = UNSET,
    result_title_range: list[str] | Unset = UNSET,
    result_title_regex: str | Unset = UNSET,
    result_title_startswith: str | Unset = UNSET,
) -> Response[PaginatedDQConformanceResultReadList]:
    """Get a list of DQConformanceResult objects.

    Args:
        date (datetime.date | Unset):
        date_contained_by (datetime.date | Unset):
        date_contains (datetime.date | Unset):
        date_day (float | Unset):
        date_endswith (datetime.date | Unset):
        date_gt (datetime.date | Unset):
        date_gte (datetime.date | Unset):
        date_icontains (datetime.date | Unset):
        date_iendswith (datetime.date | Unset):
        date_iexact (datetime.date | Unset):
        date_in (list[datetime.date] | Unset):
        date_iregex (datetime.date | Unset):
        date_isnull (bool | Unset):
        date_iso_week_day (float | Unset):
        date_iso_year (float | Unset):
        date_istartswith (datetime.date | Unset):
        date_lt (datetime.date | Unset):
        date_lte (datetime.date | Unset):
        date_month (float | Unset):
        date_quarter (float | Unset):
        date_range (list[datetime.date] | Unset):
        date_regex (datetime.date | Unset):
        date_startswith (datetime.date | Unset):
        date_week (float | Unset):
        date_week_day (float | Unset):
        date_year (float | Unset):
        explanation (str | Unset):
        explanation_contains (str | Unset):
        explanation_endswith (str | Unset):
        explanation_gt (str | Unset):
        explanation_gte (str | Unset):
        explanation_icontains (str | Unset):
        explanation_iendswith (str | Unset):
        explanation_iexact (str | Unset):
        explanation_in (list[str] | Unset):
        explanation_iregex (str | Unset):
        explanation_isnull (bool | Unset):
        explanation_istartswith (str | Unset):
        explanation_lt (str | Unset):
        explanation_lte (str | Unset):
        explanation_range (list[str] | Unset):
        explanation_regex (str | Unset):
        explanation_startswith (str | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        passes_test (bool | Unset):
        passes_test_contains (bool | Unset):
        passes_test_endswith (bool | Unset):
        passes_test_gt (bool | Unset):
        passes_test_gte (bool | Unset):
        passes_test_icontains (bool | Unset):
        passes_test_iendswith (bool | Unset):
        passes_test_iexact (bool | Unset):
        passes_test_in (list[bool] | Unset):
        passes_test_iregex (bool | Unset):
        passes_test_isnull (bool | Unset):
        passes_test_istartswith (bool | Unset):
        passes_test_lt (bool | Unset):
        passes_test_lte (bool | Unset):
        passes_test_range (list[bool] | Unset):
        passes_test_regex (bool | Unset):
        passes_test_startswith (bool | Unset):
        result_title (str | Unset):
        result_title_contains (str | Unset):
        result_title_endswith (str | Unset):
        result_title_gt (str | Unset):
        result_title_gte (str | Unset):
        result_title_icontains (str | Unset):
        result_title_iendswith (str | Unset):
        result_title_iexact (str | Unset):
        result_title_in (list[str] | Unset):
        result_title_iregex (str | Unset):
        result_title_isnull (bool | Unset):
        result_title_istartswith (str | Unset):
        result_title_lt (str | Unset):
        result_title_lte (str | Unset):
        result_title_range (list[str] | Unset):
        result_title_regex (str | Unset):
        result_title_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDQConformanceResultReadList]
    """

    kwargs = _get_kwargs(
        date=date,
        date_contained_by=date_contained_by,
        date_contains=date_contains,
        date_day=date_day,
        date_endswith=date_endswith,
        date_gt=date_gt,
        date_gte=date_gte,
        date_icontains=date_icontains,
        date_iendswith=date_iendswith,
        date_iexact=date_iexact,
        date_in=date_in,
        date_iregex=date_iregex,
        date_isnull=date_isnull,
        date_iso_week_day=date_iso_week_day,
        date_iso_year=date_iso_year,
        date_istartswith=date_istartswith,
        date_lt=date_lt,
        date_lte=date_lte,
        date_month=date_month,
        date_quarter=date_quarter,
        date_range=date_range,
        date_regex=date_regex,
        date_startswith=date_startswith,
        date_week=date_week,
        date_week_day=date_week_day,
        date_year=date_year,
        explanation=explanation,
        explanation_contains=explanation_contains,
        explanation_endswith=explanation_endswith,
        explanation_gt=explanation_gt,
        explanation_gte=explanation_gte,
        explanation_icontains=explanation_icontains,
        explanation_iendswith=explanation_iendswith,
        explanation_iexact=explanation_iexact,
        explanation_in=explanation_in,
        explanation_iregex=explanation_iregex,
        explanation_isnull=explanation_isnull,
        explanation_istartswith=explanation_istartswith,
        explanation_lt=explanation_lt,
        explanation_lte=explanation_lte,
        explanation_range=explanation_range,
        explanation_regex=explanation_regex,
        explanation_startswith=explanation_startswith,
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
        offset=offset,
        ordering=ordering,
        passes_test=passes_test,
        passes_test_contains=passes_test_contains,
        passes_test_endswith=passes_test_endswith,
        passes_test_gt=passes_test_gt,
        passes_test_gte=passes_test_gte,
        passes_test_icontains=passes_test_icontains,
        passes_test_iendswith=passes_test_iendswith,
        passes_test_iexact=passes_test_iexact,
        passes_test_in=passes_test_in,
        passes_test_iregex=passes_test_iregex,
        passes_test_isnull=passes_test_isnull,
        passes_test_istartswith=passes_test_istartswith,
        passes_test_lt=passes_test_lt,
        passes_test_lte=passes_test_lte,
        passes_test_range=passes_test_range,
        passes_test_regex=passes_test_regex,
        passes_test_startswith=passes_test_startswith,
        result_title=result_title,
        result_title_contains=result_title_contains,
        result_title_endswith=result_title_endswith,
        result_title_gt=result_title_gt,
        result_title_gte=result_title_gte,
        result_title_icontains=result_title_icontains,
        result_title_iendswith=result_title_iendswith,
        result_title_iexact=result_title_iexact,
        result_title_in=result_title_in,
        result_title_iregex=result_title_iregex,
        result_title_isnull=result_title_isnull,
        result_title_istartswith=result_title_istartswith,
        result_title_lt=result_title_lt,
        result_title_lte=result_title_lte,
        result_title_range=result_title_range,
        result_title_regex=result_title_regex,
        result_title_startswith=result_title_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
    date_contained_by: datetime.date | Unset = UNSET,
    date_contains: datetime.date | Unset = UNSET,
    date_day: float | Unset = UNSET,
    date_endswith: datetime.date | Unset = UNSET,
    date_gt: datetime.date | Unset = UNSET,
    date_gte: datetime.date | Unset = UNSET,
    date_icontains: datetime.date | Unset = UNSET,
    date_iendswith: datetime.date | Unset = UNSET,
    date_iexact: datetime.date | Unset = UNSET,
    date_in: list[datetime.date] | Unset = UNSET,
    date_iregex: datetime.date | Unset = UNSET,
    date_isnull: bool | Unset = UNSET,
    date_iso_week_day: float | Unset = UNSET,
    date_iso_year: float | Unset = UNSET,
    date_istartswith: datetime.date | Unset = UNSET,
    date_lt: datetime.date | Unset = UNSET,
    date_lte: datetime.date | Unset = UNSET,
    date_month: float | Unset = UNSET,
    date_quarter: float | Unset = UNSET,
    date_range: list[datetime.date] | Unset = UNSET,
    date_regex: datetime.date | Unset = UNSET,
    date_startswith: datetime.date | Unset = UNSET,
    date_week: float | Unset = UNSET,
    date_week_day: float | Unset = UNSET,
    date_year: float | Unset = UNSET,
    explanation: str | Unset = UNSET,
    explanation_contains: str | Unset = UNSET,
    explanation_endswith: str | Unset = UNSET,
    explanation_gt: str | Unset = UNSET,
    explanation_gte: str | Unset = UNSET,
    explanation_icontains: str | Unset = UNSET,
    explanation_iendswith: str | Unset = UNSET,
    explanation_iexact: str | Unset = UNSET,
    explanation_in: list[str] | Unset = UNSET,
    explanation_iregex: str | Unset = UNSET,
    explanation_isnull: bool | Unset = UNSET,
    explanation_istartswith: str | Unset = UNSET,
    explanation_lt: str | Unset = UNSET,
    explanation_lte: str | Unset = UNSET,
    explanation_range: list[str] | Unset = UNSET,
    explanation_regex: str | Unset = UNSET,
    explanation_startswith: str | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    passes_test: bool | Unset = UNSET,
    passes_test_contains: bool | Unset = UNSET,
    passes_test_endswith: bool | Unset = UNSET,
    passes_test_gt: bool | Unset = UNSET,
    passes_test_gte: bool | Unset = UNSET,
    passes_test_icontains: bool | Unset = UNSET,
    passes_test_iendswith: bool | Unset = UNSET,
    passes_test_iexact: bool | Unset = UNSET,
    passes_test_in: list[bool] | Unset = UNSET,
    passes_test_iregex: bool | Unset = UNSET,
    passes_test_isnull: bool | Unset = UNSET,
    passes_test_istartswith: bool | Unset = UNSET,
    passes_test_lt: bool | Unset = UNSET,
    passes_test_lte: bool | Unset = UNSET,
    passes_test_range: list[bool] | Unset = UNSET,
    passes_test_regex: bool | Unset = UNSET,
    passes_test_startswith: bool | Unset = UNSET,
    result_title: str | Unset = UNSET,
    result_title_contains: str | Unset = UNSET,
    result_title_endswith: str | Unset = UNSET,
    result_title_gt: str | Unset = UNSET,
    result_title_gte: str | Unset = UNSET,
    result_title_icontains: str | Unset = UNSET,
    result_title_iendswith: str | Unset = UNSET,
    result_title_iexact: str | Unset = UNSET,
    result_title_in: list[str] | Unset = UNSET,
    result_title_iregex: str | Unset = UNSET,
    result_title_isnull: bool | Unset = UNSET,
    result_title_istartswith: str | Unset = UNSET,
    result_title_lt: str | Unset = UNSET,
    result_title_lte: str | Unset = UNSET,
    result_title_range: list[str] | Unset = UNSET,
    result_title_regex: str | Unset = UNSET,
    result_title_startswith: str | Unset = UNSET,
) -> PaginatedDQConformanceResultReadList | None:
    """Get a list of DQConformanceResult objects.

    Args:
        date (datetime.date | Unset):
        date_contained_by (datetime.date | Unset):
        date_contains (datetime.date | Unset):
        date_day (float | Unset):
        date_endswith (datetime.date | Unset):
        date_gt (datetime.date | Unset):
        date_gte (datetime.date | Unset):
        date_icontains (datetime.date | Unset):
        date_iendswith (datetime.date | Unset):
        date_iexact (datetime.date | Unset):
        date_in (list[datetime.date] | Unset):
        date_iregex (datetime.date | Unset):
        date_isnull (bool | Unset):
        date_iso_week_day (float | Unset):
        date_iso_year (float | Unset):
        date_istartswith (datetime.date | Unset):
        date_lt (datetime.date | Unset):
        date_lte (datetime.date | Unset):
        date_month (float | Unset):
        date_quarter (float | Unset):
        date_range (list[datetime.date] | Unset):
        date_regex (datetime.date | Unset):
        date_startswith (datetime.date | Unset):
        date_week (float | Unset):
        date_week_day (float | Unset):
        date_year (float | Unset):
        explanation (str | Unset):
        explanation_contains (str | Unset):
        explanation_endswith (str | Unset):
        explanation_gt (str | Unset):
        explanation_gte (str | Unset):
        explanation_icontains (str | Unset):
        explanation_iendswith (str | Unset):
        explanation_iexact (str | Unset):
        explanation_in (list[str] | Unset):
        explanation_iregex (str | Unset):
        explanation_isnull (bool | Unset):
        explanation_istartswith (str | Unset):
        explanation_lt (str | Unset):
        explanation_lte (str | Unset):
        explanation_range (list[str] | Unset):
        explanation_regex (str | Unset):
        explanation_startswith (str | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        passes_test (bool | Unset):
        passes_test_contains (bool | Unset):
        passes_test_endswith (bool | Unset):
        passes_test_gt (bool | Unset):
        passes_test_gte (bool | Unset):
        passes_test_icontains (bool | Unset):
        passes_test_iendswith (bool | Unset):
        passes_test_iexact (bool | Unset):
        passes_test_in (list[bool] | Unset):
        passes_test_iregex (bool | Unset):
        passes_test_isnull (bool | Unset):
        passes_test_istartswith (bool | Unset):
        passes_test_lt (bool | Unset):
        passes_test_lte (bool | Unset):
        passes_test_range (list[bool] | Unset):
        passes_test_regex (bool | Unset):
        passes_test_startswith (bool | Unset):
        result_title (str | Unset):
        result_title_contains (str | Unset):
        result_title_endswith (str | Unset):
        result_title_gt (str | Unset):
        result_title_gte (str | Unset):
        result_title_icontains (str | Unset):
        result_title_iendswith (str | Unset):
        result_title_iexact (str | Unset):
        result_title_in (list[str] | Unset):
        result_title_iregex (str | Unset):
        result_title_isnull (bool | Unset):
        result_title_istartswith (str | Unset):
        result_title_lt (str | Unset):
        result_title_lte (str | Unset):
        result_title_range (list[str] | Unset):
        result_title_regex (str | Unset):
        result_title_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDQConformanceResultReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            date_contained_by=date_contained_by,
            date_contains=date_contains,
            date_day=date_day,
            date_endswith=date_endswith,
            date_gt=date_gt,
            date_gte=date_gte,
            date_icontains=date_icontains,
            date_iendswith=date_iendswith,
            date_iexact=date_iexact,
            date_in=date_in,
            date_iregex=date_iregex,
            date_isnull=date_isnull,
            date_iso_week_day=date_iso_week_day,
            date_iso_year=date_iso_year,
            date_istartswith=date_istartswith,
            date_lt=date_lt,
            date_lte=date_lte,
            date_month=date_month,
            date_quarter=date_quarter,
            date_range=date_range,
            date_regex=date_regex,
            date_startswith=date_startswith,
            date_week=date_week,
            date_week_day=date_week_day,
            date_year=date_year,
            explanation=explanation,
            explanation_contains=explanation_contains,
            explanation_endswith=explanation_endswith,
            explanation_gt=explanation_gt,
            explanation_gte=explanation_gte,
            explanation_icontains=explanation_icontains,
            explanation_iendswith=explanation_iendswith,
            explanation_iexact=explanation_iexact,
            explanation_in=explanation_in,
            explanation_iregex=explanation_iregex,
            explanation_isnull=explanation_isnull,
            explanation_istartswith=explanation_istartswith,
            explanation_lt=explanation_lt,
            explanation_lte=explanation_lte,
            explanation_range=explanation_range,
            explanation_regex=explanation_regex,
            explanation_startswith=explanation_startswith,
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
            observation=observation,
            observation_in=observation_in,
            observation_isnull=observation_isnull,
            offset=offset,
            ordering=ordering,
            passes_test=passes_test,
            passes_test_contains=passes_test_contains,
            passes_test_endswith=passes_test_endswith,
            passes_test_gt=passes_test_gt,
            passes_test_gte=passes_test_gte,
            passes_test_icontains=passes_test_icontains,
            passes_test_iendswith=passes_test_iendswith,
            passes_test_iexact=passes_test_iexact,
            passes_test_in=passes_test_in,
            passes_test_iregex=passes_test_iregex,
            passes_test_isnull=passes_test_isnull,
            passes_test_istartswith=passes_test_istartswith,
            passes_test_lt=passes_test_lt,
            passes_test_lte=passes_test_lte,
            passes_test_range=passes_test_range,
            passes_test_regex=passes_test_regex,
            passes_test_startswith=passes_test_startswith,
            result_title=result_title,
            result_title_contains=result_title_contains,
            result_title_endswith=result_title_endswith,
            result_title_gt=result_title_gt,
            result_title_gte=result_title_gte,
            result_title_icontains=result_title_icontains,
            result_title_iendswith=result_title_iendswith,
            result_title_iexact=result_title_iexact,
            result_title_in=result_title_in,
            result_title_iregex=result_title_iregex,
            result_title_isnull=result_title_isnull,
            result_title_istartswith=result_title_istartswith,
            result_title_lt=result_title_lt,
            result_title_lte=result_title_lte,
            result_title_range=result_title_range,
            result_title_regex=result_title_regex,
            result_title_startswith=result_title_startswith,
        )
    ).parsed
