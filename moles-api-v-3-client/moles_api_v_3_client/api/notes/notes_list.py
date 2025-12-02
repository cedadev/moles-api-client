import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_note_read_list import PaginatedNoteReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    commentator: int | Unset = UNSET,
    commentator_in: list[int] | Unset = UNSET,
    commentator_isnull: bool | Unset = UNSET,
    comments: str | Unset = UNSET,
    comments_contains: str | Unset = UNSET,
    comments_endswith: str | Unset = UNSET,
    comments_gt: str | Unset = UNSET,
    comments_gte: str | Unset = UNSET,
    comments_icontains: str | Unset = UNSET,
    comments_iendswith: str | Unset = UNSET,
    comments_iexact: str | Unset = UNSET,
    comments_in: list[str] | Unset = UNSET,
    comments_iregex: str | Unset = UNSET,
    comments_isnull: bool | Unset = UNSET,
    comments_istartswith: str | Unset = UNSET,
    comments_lt: str | Unset = UNSET,
    comments_lte: str | Unset = UNSET,
    comments_range: list[str] | Unset = UNSET,
    comments_regex: str | Unset = UNSET,
    comments_startswith: str | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_contained_by: datetime.datetime | Unset = UNSET,
    date_contains: datetime.datetime | Unset = UNSET,
    date_date: datetime.date | Unset = UNSET,
    date_day: float | Unset = UNSET,
    date_endswith: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_hour: float | Unset = UNSET,
    date_icontains: datetime.datetime | Unset = UNSET,
    date_iendswith: datetime.datetime | Unset = UNSET,
    date_iexact: datetime.datetime | Unset = UNSET,
    date_in: list[datetime.datetime] | Unset = UNSET,
    date_iregex: datetime.datetime | Unset = UNSET,
    date_isnull: bool | Unset = UNSET,
    date_iso_week_day: float | Unset = UNSET,
    date_iso_year: float | Unset = UNSET,
    date_istartswith: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    date_minute: float | Unset = UNSET,
    date_month: float | Unset = UNSET,
    date_quarter: float | Unset = UNSET,
    date_range: list[datetime.datetime] | Unset = UNSET,
    date_regex: datetime.datetime | Unset = UNSET,
    date_second: float | Unset = UNSET,
    date_startswith: datetime.datetime | Unset = UNSET,
    date_time: str | Unset = UNSET,
    date_week: float | Unset = UNSET,
    date_week_day: float | Unset = UNSET,
    date_year: float | Unset = UNSET,
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
    related_record: int | Unset = UNSET,
    related_record_in: list[int] | Unset = UNSET,
    related_record_isnull: bool | Unset = UNSET,
    related_record_ob_id: int | Unset = UNSET,
    related_record_ob_id_in: list[int] | Unset = UNSET,
    related_record_short_code: str | Unset = UNSET,
    related_record_short_code_in: list[str] | Unset = UNSET,
    related_record_uuid: str | Unset = UNSET,
    related_record_uuid_in: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["commentator"] = commentator

    json_commentator_in: list[int] | Unset = UNSET
    if not isinstance(commentator_in, Unset):
        json_commentator_in = ",".join(map(str, commentator_in))

    params["commentator__in"] = json_commentator_in

    params["commentator__isnull"] = commentator_isnull

    params["comments"] = comments

    params["comments__contains"] = comments_contains

    params["comments__endswith"] = comments_endswith

    params["comments__gt"] = comments_gt

    params["comments__gte"] = comments_gte

    params["comments__icontains"] = comments_icontains

    params["comments__iendswith"] = comments_iendswith

    params["comments__iexact"] = comments_iexact

    json_comments_in: list[str] | Unset = UNSET
    if not isinstance(comments_in, Unset):
        json_comments_in = ",".join(map(str, comments_in))

    params["comments__in"] = json_comments_in

    params["comments__iregex"] = comments_iregex

    params["comments__isnull"] = comments_isnull

    params["comments__istartswith"] = comments_istartswith

    params["comments__lt"] = comments_lt

    params["comments__lte"] = comments_lte

    json_comments_range: list[str] | Unset = UNSET
    if not isinstance(comments_range, Unset):
        json_comments_range = ",".join(map(str, comments_range))

    params["comments__range"] = json_comments_range

    params["comments__regex"] = comments_regex

    params["comments__startswith"] = comments_startswith

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

    json_date_date: str | Unset = UNSET
    if not isinstance(date_date, Unset):
        json_date_date = date_date.isoformat()
    params["date__date"] = json_date_date

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

    params["date__hour"] = date_hour

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

    params["date__minute"] = date_minute

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

    params["date__second"] = date_second

    json_date_startswith: str | Unset = UNSET
    if not isinstance(date_startswith, Unset):
        json_date_startswith = date_startswith.isoformat()
    params["date__startswith"] = json_date_startswith

    params["date__time"] = date_time

    params["date__week"] = date_week

    params["date__week_day"] = date_week_day

    params["date__year"] = date_year

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

    params["relatedRecord"] = related_record

    json_related_record_in: list[int] | Unset = UNSET
    if not isinstance(related_record_in, Unset):
        json_related_record_in = ",".join(map(str, related_record_in))

    params["relatedRecord__in"] = json_related_record_in

    params["relatedRecord__isnull"] = related_record_isnull

    params["relatedRecord__ob_id"] = related_record_ob_id

    json_related_record_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(related_record_ob_id_in, Unset):
        json_related_record_ob_id_in = ",".join(map(str, related_record_ob_id_in))

    params["relatedRecord__ob_id__in"] = json_related_record_ob_id_in

    params["relatedRecord__short_code"] = related_record_short_code

    json_related_record_short_code_in: list[str] | Unset = UNSET
    if not isinstance(related_record_short_code_in, Unset):
        json_related_record_short_code_in = ",".join(map(str, related_record_short_code_in))

    params["relatedRecord__short_code__in"] = json_related_record_short_code_in

    params["relatedRecord__uuid"] = related_record_uuid

    json_related_record_uuid_in: list[str] | Unset = UNSET
    if not isinstance(related_record_uuid_in, Unset):
        json_related_record_uuid_in = ",".join(map(str, related_record_uuid_in))

    params["relatedRecord__uuid__in"] = json_related_record_uuid_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/notes/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedNoteReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedNoteReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedNoteReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    commentator: int | Unset = UNSET,
    commentator_in: list[int] | Unset = UNSET,
    commentator_isnull: bool | Unset = UNSET,
    comments: str | Unset = UNSET,
    comments_contains: str | Unset = UNSET,
    comments_endswith: str | Unset = UNSET,
    comments_gt: str | Unset = UNSET,
    comments_gte: str | Unset = UNSET,
    comments_icontains: str | Unset = UNSET,
    comments_iendswith: str | Unset = UNSET,
    comments_iexact: str | Unset = UNSET,
    comments_in: list[str] | Unset = UNSET,
    comments_iregex: str | Unset = UNSET,
    comments_isnull: bool | Unset = UNSET,
    comments_istartswith: str | Unset = UNSET,
    comments_lt: str | Unset = UNSET,
    comments_lte: str | Unset = UNSET,
    comments_range: list[str] | Unset = UNSET,
    comments_regex: str | Unset = UNSET,
    comments_startswith: str | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_contained_by: datetime.datetime | Unset = UNSET,
    date_contains: datetime.datetime | Unset = UNSET,
    date_date: datetime.date | Unset = UNSET,
    date_day: float | Unset = UNSET,
    date_endswith: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_hour: float | Unset = UNSET,
    date_icontains: datetime.datetime | Unset = UNSET,
    date_iendswith: datetime.datetime | Unset = UNSET,
    date_iexact: datetime.datetime | Unset = UNSET,
    date_in: list[datetime.datetime] | Unset = UNSET,
    date_iregex: datetime.datetime | Unset = UNSET,
    date_isnull: bool | Unset = UNSET,
    date_iso_week_day: float | Unset = UNSET,
    date_iso_year: float | Unset = UNSET,
    date_istartswith: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    date_minute: float | Unset = UNSET,
    date_month: float | Unset = UNSET,
    date_quarter: float | Unset = UNSET,
    date_range: list[datetime.datetime] | Unset = UNSET,
    date_regex: datetime.datetime | Unset = UNSET,
    date_second: float | Unset = UNSET,
    date_startswith: datetime.datetime | Unset = UNSET,
    date_time: str | Unset = UNSET,
    date_week: float | Unset = UNSET,
    date_week_day: float | Unset = UNSET,
    date_year: float | Unset = UNSET,
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
    related_record: int | Unset = UNSET,
    related_record_in: list[int] | Unset = UNSET,
    related_record_isnull: bool | Unset = UNSET,
    related_record_ob_id: int | Unset = UNSET,
    related_record_ob_id_in: list[int] | Unset = UNSET,
    related_record_short_code: str | Unset = UNSET,
    related_record_short_code_in: list[str] | Unset = UNSET,
    related_record_uuid: str | Unset = UNSET,
    related_record_uuid_in: list[str] | Unset = UNSET,
) -> Response[PaginatedNoteReadList]:
    """Get a list of Note objects.

    Args:
        commentator (int | Unset):
        commentator_in (list[int] | Unset):
        commentator_isnull (bool | Unset):
        comments (str | Unset):
        comments_contains (str | Unset):
        comments_endswith (str | Unset):
        comments_gt (str | Unset):
        comments_gte (str | Unset):
        comments_icontains (str | Unset):
        comments_iendswith (str | Unset):
        comments_iexact (str | Unset):
        comments_in (list[str] | Unset):
        comments_iregex (str | Unset):
        comments_isnull (bool | Unset):
        comments_istartswith (str | Unset):
        comments_lt (str | Unset):
        comments_lte (str | Unset):
        comments_range (list[str] | Unset):
        comments_regex (str | Unset):
        comments_startswith (str | Unset):
        date (datetime.datetime | Unset):
        date_contained_by (datetime.datetime | Unset):
        date_contains (datetime.datetime | Unset):
        date_date (datetime.date | Unset):
        date_day (float | Unset):
        date_endswith (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_hour (float | Unset):
        date_icontains (datetime.datetime | Unset):
        date_iendswith (datetime.datetime | Unset):
        date_iexact (datetime.datetime | Unset):
        date_in (list[datetime.datetime] | Unset):
        date_iregex (datetime.datetime | Unset):
        date_isnull (bool | Unset):
        date_iso_week_day (float | Unset):
        date_iso_year (float | Unset):
        date_istartswith (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        date_minute (float | Unset):
        date_month (float | Unset):
        date_quarter (float | Unset):
        date_range (list[datetime.datetime] | Unset):
        date_regex (datetime.datetime | Unset):
        date_second (float | Unset):
        date_startswith (datetime.datetime | Unset):
        date_time (str | Unset):
        date_week (float | Unset):
        date_week_day (float | Unset):
        date_year (float | Unset):
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
        related_record (int | Unset):
        related_record_in (list[int] | Unset):
        related_record_isnull (bool | Unset):
        related_record_ob_id (int | Unset):
        related_record_ob_id_in (list[int] | Unset):
        related_record_short_code (str | Unset):
        related_record_short_code_in (list[str] | Unset):
        related_record_uuid (str | Unset):
        related_record_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNoteReadList]
    """

    kwargs = _get_kwargs(
        commentator=commentator,
        commentator_in=commentator_in,
        commentator_isnull=commentator_isnull,
        comments=comments,
        comments_contains=comments_contains,
        comments_endswith=comments_endswith,
        comments_gt=comments_gt,
        comments_gte=comments_gte,
        comments_icontains=comments_icontains,
        comments_iendswith=comments_iendswith,
        comments_iexact=comments_iexact,
        comments_in=comments_in,
        comments_iregex=comments_iregex,
        comments_isnull=comments_isnull,
        comments_istartswith=comments_istartswith,
        comments_lt=comments_lt,
        comments_lte=comments_lte,
        comments_range=comments_range,
        comments_regex=comments_regex,
        comments_startswith=comments_startswith,
        date=date,
        date_contained_by=date_contained_by,
        date_contains=date_contains,
        date_date=date_date,
        date_day=date_day,
        date_endswith=date_endswith,
        date_gt=date_gt,
        date_gte=date_gte,
        date_hour=date_hour,
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
        date_minute=date_minute,
        date_month=date_month,
        date_quarter=date_quarter,
        date_range=date_range,
        date_regex=date_regex,
        date_second=date_second,
        date_startswith=date_startswith,
        date_time=date_time,
        date_week=date_week,
        date_week_day=date_week_day,
        date_year=date_year,
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
        related_record=related_record,
        related_record_in=related_record_in,
        related_record_isnull=related_record_isnull,
        related_record_ob_id=related_record_ob_id,
        related_record_ob_id_in=related_record_ob_id_in,
        related_record_short_code=related_record_short_code,
        related_record_short_code_in=related_record_short_code_in,
        related_record_uuid=related_record_uuid,
        related_record_uuid_in=related_record_uuid_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    commentator: int | Unset = UNSET,
    commentator_in: list[int] | Unset = UNSET,
    commentator_isnull: bool | Unset = UNSET,
    comments: str | Unset = UNSET,
    comments_contains: str | Unset = UNSET,
    comments_endswith: str | Unset = UNSET,
    comments_gt: str | Unset = UNSET,
    comments_gte: str | Unset = UNSET,
    comments_icontains: str | Unset = UNSET,
    comments_iendswith: str | Unset = UNSET,
    comments_iexact: str | Unset = UNSET,
    comments_in: list[str] | Unset = UNSET,
    comments_iregex: str | Unset = UNSET,
    comments_isnull: bool | Unset = UNSET,
    comments_istartswith: str | Unset = UNSET,
    comments_lt: str | Unset = UNSET,
    comments_lte: str | Unset = UNSET,
    comments_range: list[str] | Unset = UNSET,
    comments_regex: str | Unset = UNSET,
    comments_startswith: str | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_contained_by: datetime.datetime | Unset = UNSET,
    date_contains: datetime.datetime | Unset = UNSET,
    date_date: datetime.date | Unset = UNSET,
    date_day: float | Unset = UNSET,
    date_endswith: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_hour: float | Unset = UNSET,
    date_icontains: datetime.datetime | Unset = UNSET,
    date_iendswith: datetime.datetime | Unset = UNSET,
    date_iexact: datetime.datetime | Unset = UNSET,
    date_in: list[datetime.datetime] | Unset = UNSET,
    date_iregex: datetime.datetime | Unset = UNSET,
    date_isnull: bool | Unset = UNSET,
    date_iso_week_day: float | Unset = UNSET,
    date_iso_year: float | Unset = UNSET,
    date_istartswith: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    date_minute: float | Unset = UNSET,
    date_month: float | Unset = UNSET,
    date_quarter: float | Unset = UNSET,
    date_range: list[datetime.datetime] | Unset = UNSET,
    date_regex: datetime.datetime | Unset = UNSET,
    date_second: float | Unset = UNSET,
    date_startswith: datetime.datetime | Unset = UNSET,
    date_time: str | Unset = UNSET,
    date_week: float | Unset = UNSET,
    date_week_day: float | Unset = UNSET,
    date_year: float | Unset = UNSET,
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
    related_record: int | Unset = UNSET,
    related_record_in: list[int] | Unset = UNSET,
    related_record_isnull: bool | Unset = UNSET,
    related_record_ob_id: int | Unset = UNSET,
    related_record_ob_id_in: list[int] | Unset = UNSET,
    related_record_short_code: str | Unset = UNSET,
    related_record_short_code_in: list[str] | Unset = UNSET,
    related_record_uuid: str | Unset = UNSET,
    related_record_uuid_in: list[str] | Unset = UNSET,
) -> PaginatedNoteReadList | None:
    """Get a list of Note objects.

    Args:
        commentator (int | Unset):
        commentator_in (list[int] | Unset):
        commentator_isnull (bool | Unset):
        comments (str | Unset):
        comments_contains (str | Unset):
        comments_endswith (str | Unset):
        comments_gt (str | Unset):
        comments_gte (str | Unset):
        comments_icontains (str | Unset):
        comments_iendswith (str | Unset):
        comments_iexact (str | Unset):
        comments_in (list[str] | Unset):
        comments_iregex (str | Unset):
        comments_isnull (bool | Unset):
        comments_istartswith (str | Unset):
        comments_lt (str | Unset):
        comments_lte (str | Unset):
        comments_range (list[str] | Unset):
        comments_regex (str | Unset):
        comments_startswith (str | Unset):
        date (datetime.datetime | Unset):
        date_contained_by (datetime.datetime | Unset):
        date_contains (datetime.datetime | Unset):
        date_date (datetime.date | Unset):
        date_day (float | Unset):
        date_endswith (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_hour (float | Unset):
        date_icontains (datetime.datetime | Unset):
        date_iendswith (datetime.datetime | Unset):
        date_iexact (datetime.datetime | Unset):
        date_in (list[datetime.datetime] | Unset):
        date_iregex (datetime.datetime | Unset):
        date_isnull (bool | Unset):
        date_iso_week_day (float | Unset):
        date_iso_year (float | Unset):
        date_istartswith (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        date_minute (float | Unset):
        date_month (float | Unset):
        date_quarter (float | Unset):
        date_range (list[datetime.datetime] | Unset):
        date_regex (datetime.datetime | Unset):
        date_second (float | Unset):
        date_startswith (datetime.datetime | Unset):
        date_time (str | Unset):
        date_week (float | Unset):
        date_week_day (float | Unset):
        date_year (float | Unset):
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
        related_record (int | Unset):
        related_record_in (list[int] | Unset):
        related_record_isnull (bool | Unset):
        related_record_ob_id (int | Unset):
        related_record_ob_id_in (list[int] | Unset):
        related_record_short_code (str | Unset):
        related_record_short_code_in (list[str] | Unset):
        related_record_uuid (str | Unset):
        related_record_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNoteReadList
    """

    return sync_detailed(
        client=client,
        commentator=commentator,
        commentator_in=commentator_in,
        commentator_isnull=commentator_isnull,
        comments=comments,
        comments_contains=comments_contains,
        comments_endswith=comments_endswith,
        comments_gt=comments_gt,
        comments_gte=comments_gte,
        comments_icontains=comments_icontains,
        comments_iendswith=comments_iendswith,
        comments_iexact=comments_iexact,
        comments_in=comments_in,
        comments_iregex=comments_iregex,
        comments_isnull=comments_isnull,
        comments_istartswith=comments_istartswith,
        comments_lt=comments_lt,
        comments_lte=comments_lte,
        comments_range=comments_range,
        comments_regex=comments_regex,
        comments_startswith=comments_startswith,
        date=date,
        date_contained_by=date_contained_by,
        date_contains=date_contains,
        date_date=date_date,
        date_day=date_day,
        date_endswith=date_endswith,
        date_gt=date_gt,
        date_gte=date_gte,
        date_hour=date_hour,
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
        date_minute=date_minute,
        date_month=date_month,
        date_quarter=date_quarter,
        date_range=date_range,
        date_regex=date_regex,
        date_second=date_second,
        date_startswith=date_startswith,
        date_time=date_time,
        date_week=date_week,
        date_week_day=date_week_day,
        date_year=date_year,
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
        related_record=related_record,
        related_record_in=related_record_in,
        related_record_isnull=related_record_isnull,
        related_record_ob_id=related_record_ob_id,
        related_record_ob_id_in=related_record_ob_id_in,
        related_record_short_code=related_record_short_code,
        related_record_short_code_in=related_record_short_code_in,
        related_record_uuid=related_record_uuid,
        related_record_uuid_in=related_record_uuid_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    commentator: int | Unset = UNSET,
    commentator_in: list[int] | Unset = UNSET,
    commentator_isnull: bool | Unset = UNSET,
    comments: str | Unset = UNSET,
    comments_contains: str | Unset = UNSET,
    comments_endswith: str | Unset = UNSET,
    comments_gt: str | Unset = UNSET,
    comments_gte: str | Unset = UNSET,
    comments_icontains: str | Unset = UNSET,
    comments_iendswith: str | Unset = UNSET,
    comments_iexact: str | Unset = UNSET,
    comments_in: list[str] | Unset = UNSET,
    comments_iregex: str | Unset = UNSET,
    comments_isnull: bool | Unset = UNSET,
    comments_istartswith: str | Unset = UNSET,
    comments_lt: str | Unset = UNSET,
    comments_lte: str | Unset = UNSET,
    comments_range: list[str] | Unset = UNSET,
    comments_regex: str | Unset = UNSET,
    comments_startswith: str | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_contained_by: datetime.datetime | Unset = UNSET,
    date_contains: datetime.datetime | Unset = UNSET,
    date_date: datetime.date | Unset = UNSET,
    date_day: float | Unset = UNSET,
    date_endswith: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_hour: float | Unset = UNSET,
    date_icontains: datetime.datetime | Unset = UNSET,
    date_iendswith: datetime.datetime | Unset = UNSET,
    date_iexact: datetime.datetime | Unset = UNSET,
    date_in: list[datetime.datetime] | Unset = UNSET,
    date_iregex: datetime.datetime | Unset = UNSET,
    date_isnull: bool | Unset = UNSET,
    date_iso_week_day: float | Unset = UNSET,
    date_iso_year: float | Unset = UNSET,
    date_istartswith: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    date_minute: float | Unset = UNSET,
    date_month: float | Unset = UNSET,
    date_quarter: float | Unset = UNSET,
    date_range: list[datetime.datetime] | Unset = UNSET,
    date_regex: datetime.datetime | Unset = UNSET,
    date_second: float | Unset = UNSET,
    date_startswith: datetime.datetime | Unset = UNSET,
    date_time: str | Unset = UNSET,
    date_week: float | Unset = UNSET,
    date_week_day: float | Unset = UNSET,
    date_year: float | Unset = UNSET,
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
    related_record: int | Unset = UNSET,
    related_record_in: list[int] | Unset = UNSET,
    related_record_isnull: bool | Unset = UNSET,
    related_record_ob_id: int | Unset = UNSET,
    related_record_ob_id_in: list[int] | Unset = UNSET,
    related_record_short_code: str | Unset = UNSET,
    related_record_short_code_in: list[str] | Unset = UNSET,
    related_record_uuid: str | Unset = UNSET,
    related_record_uuid_in: list[str] | Unset = UNSET,
) -> Response[PaginatedNoteReadList]:
    """Get a list of Note objects.

    Args:
        commentator (int | Unset):
        commentator_in (list[int] | Unset):
        commentator_isnull (bool | Unset):
        comments (str | Unset):
        comments_contains (str | Unset):
        comments_endswith (str | Unset):
        comments_gt (str | Unset):
        comments_gte (str | Unset):
        comments_icontains (str | Unset):
        comments_iendswith (str | Unset):
        comments_iexact (str | Unset):
        comments_in (list[str] | Unset):
        comments_iregex (str | Unset):
        comments_isnull (bool | Unset):
        comments_istartswith (str | Unset):
        comments_lt (str | Unset):
        comments_lte (str | Unset):
        comments_range (list[str] | Unset):
        comments_regex (str | Unset):
        comments_startswith (str | Unset):
        date (datetime.datetime | Unset):
        date_contained_by (datetime.datetime | Unset):
        date_contains (datetime.datetime | Unset):
        date_date (datetime.date | Unset):
        date_day (float | Unset):
        date_endswith (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_hour (float | Unset):
        date_icontains (datetime.datetime | Unset):
        date_iendswith (datetime.datetime | Unset):
        date_iexact (datetime.datetime | Unset):
        date_in (list[datetime.datetime] | Unset):
        date_iregex (datetime.datetime | Unset):
        date_isnull (bool | Unset):
        date_iso_week_day (float | Unset):
        date_iso_year (float | Unset):
        date_istartswith (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        date_minute (float | Unset):
        date_month (float | Unset):
        date_quarter (float | Unset):
        date_range (list[datetime.datetime] | Unset):
        date_regex (datetime.datetime | Unset):
        date_second (float | Unset):
        date_startswith (datetime.datetime | Unset):
        date_time (str | Unset):
        date_week (float | Unset):
        date_week_day (float | Unset):
        date_year (float | Unset):
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
        related_record (int | Unset):
        related_record_in (list[int] | Unset):
        related_record_isnull (bool | Unset):
        related_record_ob_id (int | Unset):
        related_record_ob_id_in (list[int] | Unset):
        related_record_short_code (str | Unset):
        related_record_short_code_in (list[str] | Unset):
        related_record_uuid (str | Unset):
        related_record_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedNoteReadList]
    """

    kwargs = _get_kwargs(
        commentator=commentator,
        commentator_in=commentator_in,
        commentator_isnull=commentator_isnull,
        comments=comments,
        comments_contains=comments_contains,
        comments_endswith=comments_endswith,
        comments_gt=comments_gt,
        comments_gte=comments_gte,
        comments_icontains=comments_icontains,
        comments_iendswith=comments_iendswith,
        comments_iexact=comments_iexact,
        comments_in=comments_in,
        comments_iregex=comments_iregex,
        comments_isnull=comments_isnull,
        comments_istartswith=comments_istartswith,
        comments_lt=comments_lt,
        comments_lte=comments_lte,
        comments_range=comments_range,
        comments_regex=comments_regex,
        comments_startswith=comments_startswith,
        date=date,
        date_contained_by=date_contained_by,
        date_contains=date_contains,
        date_date=date_date,
        date_day=date_day,
        date_endswith=date_endswith,
        date_gt=date_gt,
        date_gte=date_gte,
        date_hour=date_hour,
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
        date_minute=date_minute,
        date_month=date_month,
        date_quarter=date_quarter,
        date_range=date_range,
        date_regex=date_regex,
        date_second=date_second,
        date_startswith=date_startswith,
        date_time=date_time,
        date_week=date_week,
        date_week_day=date_week_day,
        date_year=date_year,
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
        related_record=related_record,
        related_record_in=related_record_in,
        related_record_isnull=related_record_isnull,
        related_record_ob_id=related_record_ob_id,
        related_record_ob_id_in=related_record_ob_id_in,
        related_record_short_code=related_record_short_code,
        related_record_short_code_in=related_record_short_code_in,
        related_record_uuid=related_record_uuid,
        related_record_uuid_in=related_record_uuid_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    commentator: int | Unset = UNSET,
    commentator_in: list[int] | Unset = UNSET,
    commentator_isnull: bool | Unset = UNSET,
    comments: str | Unset = UNSET,
    comments_contains: str | Unset = UNSET,
    comments_endswith: str | Unset = UNSET,
    comments_gt: str | Unset = UNSET,
    comments_gte: str | Unset = UNSET,
    comments_icontains: str | Unset = UNSET,
    comments_iendswith: str | Unset = UNSET,
    comments_iexact: str | Unset = UNSET,
    comments_in: list[str] | Unset = UNSET,
    comments_iregex: str | Unset = UNSET,
    comments_isnull: bool | Unset = UNSET,
    comments_istartswith: str | Unset = UNSET,
    comments_lt: str | Unset = UNSET,
    comments_lte: str | Unset = UNSET,
    comments_range: list[str] | Unset = UNSET,
    comments_regex: str | Unset = UNSET,
    comments_startswith: str | Unset = UNSET,
    date: datetime.datetime | Unset = UNSET,
    date_contained_by: datetime.datetime | Unset = UNSET,
    date_contains: datetime.datetime | Unset = UNSET,
    date_date: datetime.date | Unset = UNSET,
    date_day: float | Unset = UNSET,
    date_endswith: datetime.datetime | Unset = UNSET,
    date_gt: datetime.datetime | Unset = UNSET,
    date_gte: datetime.datetime | Unset = UNSET,
    date_hour: float | Unset = UNSET,
    date_icontains: datetime.datetime | Unset = UNSET,
    date_iendswith: datetime.datetime | Unset = UNSET,
    date_iexact: datetime.datetime | Unset = UNSET,
    date_in: list[datetime.datetime] | Unset = UNSET,
    date_iregex: datetime.datetime | Unset = UNSET,
    date_isnull: bool | Unset = UNSET,
    date_iso_week_day: float | Unset = UNSET,
    date_iso_year: float | Unset = UNSET,
    date_istartswith: datetime.datetime | Unset = UNSET,
    date_lt: datetime.datetime | Unset = UNSET,
    date_lte: datetime.datetime | Unset = UNSET,
    date_minute: float | Unset = UNSET,
    date_month: float | Unset = UNSET,
    date_quarter: float | Unset = UNSET,
    date_range: list[datetime.datetime] | Unset = UNSET,
    date_regex: datetime.datetime | Unset = UNSET,
    date_second: float | Unset = UNSET,
    date_startswith: datetime.datetime | Unset = UNSET,
    date_time: str | Unset = UNSET,
    date_week: float | Unset = UNSET,
    date_week_day: float | Unset = UNSET,
    date_year: float | Unset = UNSET,
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
    related_record: int | Unset = UNSET,
    related_record_in: list[int] | Unset = UNSET,
    related_record_isnull: bool | Unset = UNSET,
    related_record_ob_id: int | Unset = UNSET,
    related_record_ob_id_in: list[int] | Unset = UNSET,
    related_record_short_code: str | Unset = UNSET,
    related_record_short_code_in: list[str] | Unset = UNSET,
    related_record_uuid: str | Unset = UNSET,
    related_record_uuid_in: list[str] | Unset = UNSET,
) -> PaginatedNoteReadList | None:
    """Get a list of Note objects.

    Args:
        commentator (int | Unset):
        commentator_in (list[int] | Unset):
        commentator_isnull (bool | Unset):
        comments (str | Unset):
        comments_contains (str | Unset):
        comments_endswith (str | Unset):
        comments_gt (str | Unset):
        comments_gte (str | Unset):
        comments_icontains (str | Unset):
        comments_iendswith (str | Unset):
        comments_iexact (str | Unset):
        comments_in (list[str] | Unset):
        comments_iregex (str | Unset):
        comments_isnull (bool | Unset):
        comments_istartswith (str | Unset):
        comments_lt (str | Unset):
        comments_lte (str | Unset):
        comments_range (list[str] | Unset):
        comments_regex (str | Unset):
        comments_startswith (str | Unset):
        date (datetime.datetime | Unset):
        date_contained_by (datetime.datetime | Unset):
        date_contains (datetime.datetime | Unset):
        date_date (datetime.date | Unset):
        date_day (float | Unset):
        date_endswith (datetime.datetime | Unset):
        date_gt (datetime.datetime | Unset):
        date_gte (datetime.datetime | Unset):
        date_hour (float | Unset):
        date_icontains (datetime.datetime | Unset):
        date_iendswith (datetime.datetime | Unset):
        date_iexact (datetime.datetime | Unset):
        date_in (list[datetime.datetime] | Unset):
        date_iregex (datetime.datetime | Unset):
        date_isnull (bool | Unset):
        date_iso_week_day (float | Unset):
        date_iso_year (float | Unset):
        date_istartswith (datetime.datetime | Unset):
        date_lt (datetime.datetime | Unset):
        date_lte (datetime.datetime | Unset):
        date_minute (float | Unset):
        date_month (float | Unset):
        date_quarter (float | Unset):
        date_range (list[datetime.datetime] | Unset):
        date_regex (datetime.datetime | Unset):
        date_second (float | Unset):
        date_startswith (datetime.datetime | Unset):
        date_time (str | Unset):
        date_week (float | Unset):
        date_week_day (float | Unset):
        date_year (float | Unset):
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
        related_record (int | Unset):
        related_record_in (list[int] | Unset):
        related_record_isnull (bool | Unset):
        related_record_ob_id (int | Unset):
        related_record_ob_id_in (list[int] | Unset):
        related_record_short_code (str | Unset):
        related_record_short_code_in (list[str] | Unset):
        related_record_uuid (str | Unset):
        related_record_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedNoteReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            commentator=commentator,
            commentator_in=commentator_in,
            commentator_isnull=commentator_isnull,
            comments=comments,
            comments_contains=comments_contains,
            comments_endswith=comments_endswith,
            comments_gt=comments_gt,
            comments_gte=comments_gte,
            comments_icontains=comments_icontains,
            comments_iendswith=comments_iendswith,
            comments_iexact=comments_iexact,
            comments_in=comments_in,
            comments_iregex=comments_iregex,
            comments_isnull=comments_isnull,
            comments_istartswith=comments_istartswith,
            comments_lt=comments_lt,
            comments_lte=comments_lte,
            comments_range=comments_range,
            comments_regex=comments_regex,
            comments_startswith=comments_startswith,
            date=date,
            date_contained_by=date_contained_by,
            date_contains=date_contains,
            date_date=date_date,
            date_day=date_day,
            date_endswith=date_endswith,
            date_gt=date_gt,
            date_gte=date_gte,
            date_hour=date_hour,
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
            date_minute=date_minute,
            date_month=date_month,
            date_quarter=date_quarter,
            date_range=date_range,
            date_regex=date_regex,
            date_second=date_second,
            date_startswith=date_startswith,
            date_time=date_time,
            date_week=date_week,
            date_week_day=date_week_day,
            date_year=date_year,
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
            related_record=related_record,
            related_record_in=related_record_in,
            related_record_isnull=related_record_isnull,
            related_record_ob_id=related_record_ob_id,
            related_record_ob_id_in=related_record_ob_id_in,
            related_record_short_code=related_record_short_code,
            related_record_short_code_in=related_record_short_code_in,
            related_record_uuid=related_record_uuid,
            related_record_uuid_in=related_record_uuid_in,
        )
    ).parsed
