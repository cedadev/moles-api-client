import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.observationcollections_list_publication_state import ObservationcollectionsListPublicationState
from ...models.paginated_observation_collection_read_list import PaginatedObservationCollectionReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    abstract: Union[Unset, str] = UNSET,
    abstract_contains: Union[Unset, str] = UNSET,
    abstract_endswith: Union[Unset, str] = UNSET,
    abstract_gt: Union[Unset, str] = UNSET,
    abstract_gte: Union[Unset, str] = UNSET,
    abstract_icontains: Union[Unset, str] = UNSET,
    abstract_iendswith: Union[Unset, str] = UNSET,
    abstract_iexact: Union[Unset, str] = UNSET,
    abstract_in: Union[Unset, list[str]] = UNSET,
    abstract_iregex: Union[Unset, str] = UNSET,
    abstract_isnull: Union[Unset, bool] = UNSET,
    abstract_istartswith: Union[Unset, str] = UNSET,
    abstract_lt: Union[Unset, str] = UNSET,
    abstract_lte: Union[Unset, str] = UNSET,
    abstract_range: Union[Unset, list[str]] = UNSET,
    abstract_regex: Union[Unset, str] = UNSET,
    abstract_startswith: Union[Unset, str] = UNSET,
    data_published_time: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_contains: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_date: Union[Unset, datetime.date] = UNSET,
    data_published_time_day: Union[Unset, float] = UNSET,
    data_published_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_gt: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_gte: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_hour: Union[Unset, float] = UNSET,
    data_published_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    data_published_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_isnull: Union[Unset, bool] = UNSET,
    data_published_time_iso_week_day: Union[Unset, float] = UNSET,
    data_published_time_iso_year: Union[Unset, float] = UNSET,
    data_published_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_lt: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_lte: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_minute: Union[Unset, float] = UNSET,
    data_published_time_month: Union[Unset, float] = UNSET,
    data_published_time_quarter: Union[Unset, float] = UNSET,
    data_published_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    data_published_time_regex: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_second: Union[Unset, float] = UNSET,
    data_published_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_time: Union[Unset, str] = UNSET,
    data_published_time_week: Union[Unset, float] = UNSET,
    data_published_time_week_day: Union[Unset, float] = UNSET,
    data_published_time_year: Union[Unset, float] = UNSET,
    discovery_keywords_name: Union[Unset, str] = UNSET,
    discovery_keywords_name_contains: Union[Unset, str] = UNSET,
    doi_published_time: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_contains: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_date: Union[Unset, datetime.date] = UNSET,
    doi_published_time_day: Union[Unset, float] = UNSET,
    doi_published_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_gt: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_gte: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_hour: Union[Unset, float] = UNSET,
    doi_published_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    doi_published_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_isnull: Union[Unset, bool] = UNSET,
    doi_published_time_iso_week_day: Union[Unset, float] = UNSET,
    doi_published_time_iso_year: Union[Unset, float] = UNSET,
    doi_published_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_lt: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_lte: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_minute: Union[Unset, float] = UNSET,
    doi_published_time_month: Union[Unset, float] = UNSET,
    doi_published_time_quarter: Union[Unset, float] = UNSET,
    doi_published_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    doi_published_time_regex: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_second: Union[Unset, float] = UNSET,
    doi_published_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_time: Union[Unset, str] = UNSET,
    doi_published_time_week: Union[Unset, float] = UNSET,
    doi_published_time_week_day: Union[Unset, float] = UNSET,
    doi_published_time_year: Union[Unset, float] = UNSET,
    dont_harvest_from_projects: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_contains: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_endswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_gt: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_gte: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_icontains: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_iendswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_iexact: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_in: Union[Unset, list[bool]] = UNSET,
    dont_harvest_from_projects_iregex: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_isnull: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_istartswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_lt: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_lte: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_range: Union[Unset, list[bool]] = UNSET,
    dont_harvest_from_projects_regex: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_startswith: Union[Unset, bool] = UNSET,
    keywords: Union[Unset, str] = UNSET,
    keywords_contains: Union[Unset, str] = UNSET,
    keywords_endswith: Union[Unset, str] = UNSET,
    keywords_gt: Union[Unset, str] = UNSET,
    keywords_gte: Union[Unset, str] = UNSET,
    keywords_icontains: Union[Unset, str] = UNSET,
    keywords_iendswith: Union[Unset, str] = UNSET,
    keywords_iexact: Union[Unset, str] = UNSET,
    keywords_in: Union[Unset, list[str]] = UNSET,
    keywords_iregex: Union[Unset, str] = UNSET,
    keywords_isnull: Union[Unset, bool] = UNSET,
    keywords_istartswith: Union[Unset, str] = UNSET,
    keywords_lt: Union[Unset, str] = UNSET,
    keywords_lte: Union[Unset, str] = UNSET,
    keywords_range: Union[Unset, list[str]] = UNSET,
    keywords_regex: Union[Unset, str] = UNSET,
    keywords_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    member_ob_id: Union[Unset, int] = UNSET,
    member_ob_id_in: Union[Unset, list[int]] = UNSET,
    member_uuid: Union[Unset, str] = UNSET,
    member_uuid_in: Union[Unset, list[str]] = UNSET,
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
    publication_state: Union[Unset, ObservationcollectionsListPublicationState] = UNSET,
    publication_state_contains: Union[Unset, str] = UNSET,
    publication_state_endswith: Union[Unset, str] = UNSET,
    publication_state_gt: Union[Unset, str] = UNSET,
    publication_state_gte: Union[Unset, str] = UNSET,
    publication_state_icontains: Union[Unset, str] = UNSET,
    publication_state_iendswith: Union[Unset, str] = UNSET,
    publication_state_iexact: Union[Unset, str] = UNSET,
    publication_state_in: Union[Unset, list[str]] = UNSET,
    publication_state_iregex: Union[Unset, str] = UNSET,
    publication_state_isnull: Union[Unset, bool] = UNSET,
    publication_state_istartswith: Union[Unset, str] = UNSET,
    publication_state_lt: Union[Unset, str] = UNSET,
    publication_state_lte: Union[Unset, str] = UNSET,
    publication_state_range: Union[Unset, list[str]] = UNSET,
    publication_state_regex: Union[Unset, str] = UNSET,
    publication_state_startswith: Union[Unset, str] = UNSET,
    referenceable_ptr: Union[Unset, int] = UNSET,
    referenceable_ptr_gt: Union[Unset, int] = UNSET,
    referenceable_ptr_gte: Union[Unset, int] = UNSET,
    referenceable_ptr_in: Union[Unset, list[int]] = UNSET,
    referenceable_ptr_isnull: Union[Unset, bool] = UNSET,
    referenceable_ptr_lt: Union[Unset, int] = UNSET,
    referenceable_ptr_lte: Union[Unset, int] = UNSET,
    short_code: Union[Unset, str] = UNSET,
    short_code_contains: Union[Unset, str] = UNSET,
    short_code_endswith: Union[Unset, str] = UNSET,
    short_code_gt: Union[Unset, str] = UNSET,
    short_code_gte: Union[Unset, str] = UNSET,
    short_code_icontains: Union[Unset, str] = UNSET,
    short_code_iendswith: Union[Unset, str] = UNSET,
    short_code_iexact: Union[Unset, str] = UNSET,
    short_code_in: Union[Unset, list[str]] = UNSET,
    short_code_iregex: Union[Unset, str] = UNSET,
    short_code_isnull: Union[Unset, bool] = UNSET,
    short_code_istartswith: Union[Unset, str] = UNSET,
    short_code_lt: Union[Unset, str] = UNSET,
    short_code_lte: Union[Unset, str] = UNSET,
    short_code_range: Union[Unset, list[str]] = UNSET,
    short_code_regex: Union[Unset, str] = UNSET,
    short_code_startswith: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    title_contains: Union[Unset, str] = UNSET,
    title_endswith: Union[Unset, str] = UNSET,
    title_gt: Union[Unset, str] = UNSET,
    title_gte: Union[Unset, str] = UNSET,
    title_icontains: Union[Unset, str] = UNSET,
    title_iendswith: Union[Unset, str] = UNSET,
    title_iexact: Union[Unset, str] = UNSET,
    title_in: Union[Unset, list[str]] = UNSET,
    title_iregex: Union[Unset, str] = UNSET,
    title_isnull: Union[Unset, bool] = UNSET,
    title_istartswith: Union[Unset, str] = UNSET,
    title_lt: Union[Unset, str] = UNSET,
    title_lte: Union[Unset, str] = UNSET,
    title_range: Union[Unset, list[str]] = UNSET,
    title_regex: Union[Unset, str] = UNSET,
    title_startswith: Union[Unset, str] = UNSET,
    uuid: Union[Unset, str] = UNSET,
    uuid_contains: Union[Unset, str] = UNSET,
    uuid_endswith: Union[Unset, str] = UNSET,
    uuid_gt: Union[Unset, str] = UNSET,
    uuid_gte: Union[Unset, str] = UNSET,
    uuid_icontains: Union[Unset, str] = UNSET,
    uuid_iendswith: Union[Unset, str] = UNSET,
    uuid_iexact: Union[Unset, str] = UNSET,
    uuid_in: Union[Unset, list[str]] = UNSET,
    uuid_iregex: Union[Unset, str] = UNSET,
    uuid_isnull: Union[Unset, bool] = UNSET,
    uuid_istartswith: Union[Unset, str] = UNSET,
    uuid_lt: Union[Unset, str] = UNSET,
    uuid_lte: Union[Unset, str] = UNSET,
    uuid_range: Union[Unset, list[str]] = UNSET,
    uuid_regex: Union[Unset, str] = UNSET,
    uuid_startswith: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["abstract"] = abstract

    params["abstract__contains"] = abstract_contains

    params["abstract__endswith"] = abstract_endswith

    params["abstract__gt"] = abstract_gt

    params["abstract__gte"] = abstract_gte

    params["abstract__icontains"] = abstract_icontains

    params["abstract__iendswith"] = abstract_iendswith

    params["abstract__iexact"] = abstract_iexact

    json_abstract_in: Union[Unset, list[str]] = UNSET
    if not isinstance(abstract_in, Unset):
        json_abstract_in = ",".join(map(str, abstract_in))

    params["abstract__in"] = json_abstract_in

    params["abstract__iregex"] = abstract_iregex

    params["abstract__isnull"] = abstract_isnull

    params["abstract__istartswith"] = abstract_istartswith

    params["abstract__lt"] = abstract_lt

    params["abstract__lte"] = abstract_lte

    json_abstract_range: Union[Unset, list[str]] = UNSET
    if not isinstance(abstract_range, Unset):
        json_abstract_range = ",".join(map(str, abstract_range))

    params["abstract__range"] = json_abstract_range

    params["abstract__regex"] = abstract_regex

    params["abstract__startswith"] = abstract_startswith

    json_data_published_time: Union[Unset, str] = UNSET
    if not isinstance(data_published_time, Unset):
        json_data_published_time = data_published_time.isoformat()
    params["dataPublishedTime"] = json_data_published_time

    json_data_published_time_contained_by: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_contained_by, Unset):
        json_data_published_time_contained_by = data_published_time_contained_by.isoformat()
    params["dataPublishedTime__contained_by"] = json_data_published_time_contained_by

    json_data_published_time_contains: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_contains, Unset):
        json_data_published_time_contains = data_published_time_contains.isoformat()
    params["dataPublishedTime__contains"] = json_data_published_time_contains

    json_data_published_time_date: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_date, Unset):
        json_data_published_time_date = data_published_time_date.isoformat()
    params["dataPublishedTime__date"] = json_data_published_time_date

    params["dataPublishedTime__day"] = data_published_time_day

    json_data_published_time_endswith: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_endswith, Unset):
        json_data_published_time_endswith = data_published_time_endswith.isoformat()
    params["dataPublishedTime__endswith"] = json_data_published_time_endswith

    json_data_published_time_gt: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_gt, Unset):
        json_data_published_time_gt = data_published_time_gt.isoformat()
    params["dataPublishedTime__gt"] = json_data_published_time_gt

    json_data_published_time_gte: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_gte, Unset):
        json_data_published_time_gte = data_published_time_gte.isoformat()
    params["dataPublishedTime__gte"] = json_data_published_time_gte

    params["dataPublishedTime__hour"] = data_published_time_hour

    json_data_published_time_icontains: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_icontains, Unset):
        json_data_published_time_icontains = data_published_time_icontains.isoformat()
    params["dataPublishedTime__icontains"] = json_data_published_time_icontains

    json_data_published_time_iendswith: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_iendswith, Unset):
        json_data_published_time_iendswith = data_published_time_iendswith.isoformat()
    params["dataPublishedTime__iendswith"] = json_data_published_time_iendswith

    json_data_published_time_iexact: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_iexact, Unset):
        json_data_published_time_iexact = data_published_time_iexact.isoformat()
    params["dataPublishedTime__iexact"] = json_data_published_time_iexact

    json_data_published_time_in: Union[Unset, list[str]] = UNSET
    if not isinstance(data_published_time_in, Unset):
        json_data_published_time_in = []
        for data_published_time_in_item_data in data_published_time_in:
            data_published_time_in_item = data_published_time_in_item_data.isoformat()
            json_data_published_time_in.append(data_published_time_in_item)

    params["dataPublishedTime__in"] = json_data_published_time_in

    json_data_published_time_iregex: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_iregex, Unset):
        json_data_published_time_iregex = data_published_time_iregex.isoformat()
    params["dataPublishedTime__iregex"] = json_data_published_time_iregex

    params["dataPublishedTime__isnull"] = data_published_time_isnull

    params["dataPublishedTime__iso_week_day"] = data_published_time_iso_week_day

    params["dataPublishedTime__iso_year"] = data_published_time_iso_year

    json_data_published_time_istartswith: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_istartswith, Unset):
        json_data_published_time_istartswith = data_published_time_istartswith.isoformat()
    params["dataPublishedTime__istartswith"] = json_data_published_time_istartswith

    json_data_published_time_lt: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_lt, Unset):
        json_data_published_time_lt = data_published_time_lt.isoformat()
    params["dataPublishedTime__lt"] = json_data_published_time_lt

    json_data_published_time_lte: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_lte, Unset):
        json_data_published_time_lte = data_published_time_lte.isoformat()
    params["dataPublishedTime__lte"] = json_data_published_time_lte

    params["dataPublishedTime__minute"] = data_published_time_minute

    params["dataPublishedTime__month"] = data_published_time_month

    params["dataPublishedTime__quarter"] = data_published_time_quarter

    json_data_published_time_range: Union[Unset, list[str]] = UNSET
    if not isinstance(data_published_time_range, Unset):
        json_data_published_time_range = []
        for data_published_time_range_item_data in data_published_time_range:
            data_published_time_range_item = data_published_time_range_item_data.isoformat()
            json_data_published_time_range.append(data_published_time_range_item)

    params["dataPublishedTime__range"] = json_data_published_time_range

    json_data_published_time_regex: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_regex, Unset):
        json_data_published_time_regex = data_published_time_regex.isoformat()
    params["dataPublishedTime__regex"] = json_data_published_time_regex

    params["dataPublishedTime__second"] = data_published_time_second

    json_data_published_time_startswith: Union[Unset, str] = UNSET
    if not isinstance(data_published_time_startswith, Unset):
        json_data_published_time_startswith = data_published_time_startswith.isoformat()
    params["dataPublishedTime__startswith"] = json_data_published_time_startswith

    params["dataPublishedTime__time"] = data_published_time_time

    params["dataPublishedTime__week"] = data_published_time_week

    params["dataPublishedTime__week_day"] = data_published_time_week_day

    params["dataPublishedTime__year"] = data_published_time_year

    params["discoveryKeywords__name"] = discovery_keywords_name

    params["discoveryKeywords__name__contains"] = discovery_keywords_name_contains

    json_doi_published_time: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time, Unset):
        json_doi_published_time = doi_published_time.isoformat()
    params["doiPublishedTime"] = json_doi_published_time

    json_doi_published_time_contained_by: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_contained_by, Unset):
        json_doi_published_time_contained_by = doi_published_time_contained_by.isoformat()
    params["doiPublishedTime__contained_by"] = json_doi_published_time_contained_by

    json_doi_published_time_contains: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_contains, Unset):
        json_doi_published_time_contains = doi_published_time_contains.isoformat()
    params["doiPublishedTime__contains"] = json_doi_published_time_contains

    json_doi_published_time_date: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_date, Unset):
        json_doi_published_time_date = doi_published_time_date.isoformat()
    params["doiPublishedTime__date"] = json_doi_published_time_date

    params["doiPublishedTime__day"] = doi_published_time_day

    json_doi_published_time_endswith: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_endswith, Unset):
        json_doi_published_time_endswith = doi_published_time_endswith.isoformat()
    params["doiPublishedTime__endswith"] = json_doi_published_time_endswith

    json_doi_published_time_gt: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_gt, Unset):
        json_doi_published_time_gt = doi_published_time_gt.isoformat()
    params["doiPublishedTime__gt"] = json_doi_published_time_gt

    json_doi_published_time_gte: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_gte, Unset):
        json_doi_published_time_gte = doi_published_time_gte.isoformat()
    params["doiPublishedTime__gte"] = json_doi_published_time_gte

    params["doiPublishedTime__hour"] = doi_published_time_hour

    json_doi_published_time_icontains: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_icontains, Unset):
        json_doi_published_time_icontains = doi_published_time_icontains.isoformat()
    params["doiPublishedTime__icontains"] = json_doi_published_time_icontains

    json_doi_published_time_iendswith: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_iendswith, Unset):
        json_doi_published_time_iendswith = doi_published_time_iendswith.isoformat()
    params["doiPublishedTime__iendswith"] = json_doi_published_time_iendswith

    json_doi_published_time_iexact: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_iexact, Unset):
        json_doi_published_time_iexact = doi_published_time_iexact.isoformat()
    params["doiPublishedTime__iexact"] = json_doi_published_time_iexact

    json_doi_published_time_in: Union[Unset, list[str]] = UNSET
    if not isinstance(doi_published_time_in, Unset):
        json_doi_published_time_in = []
        for doi_published_time_in_item_data in doi_published_time_in:
            doi_published_time_in_item = doi_published_time_in_item_data.isoformat()
            json_doi_published_time_in.append(doi_published_time_in_item)

    params["doiPublishedTime__in"] = json_doi_published_time_in

    json_doi_published_time_iregex: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_iregex, Unset):
        json_doi_published_time_iregex = doi_published_time_iregex.isoformat()
    params["doiPublishedTime__iregex"] = json_doi_published_time_iregex

    params["doiPublishedTime__isnull"] = doi_published_time_isnull

    params["doiPublishedTime__iso_week_day"] = doi_published_time_iso_week_day

    params["doiPublishedTime__iso_year"] = doi_published_time_iso_year

    json_doi_published_time_istartswith: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_istartswith, Unset):
        json_doi_published_time_istartswith = doi_published_time_istartswith.isoformat()
    params["doiPublishedTime__istartswith"] = json_doi_published_time_istartswith

    json_doi_published_time_lt: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_lt, Unset):
        json_doi_published_time_lt = doi_published_time_lt.isoformat()
    params["doiPublishedTime__lt"] = json_doi_published_time_lt

    json_doi_published_time_lte: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_lte, Unset):
        json_doi_published_time_lte = doi_published_time_lte.isoformat()
    params["doiPublishedTime__lte"] = json_doi_published_time_lte

    params["doiPublishedTime__minute"] = doi_published_time_minute

    params["doiPublishedTime__month"] = doi_published_time_month

    params["doiPublishedTime__quarter"] = doi_published_time_quarter

    json_doi_published_time_range: Union[Unset, list[str]] = UNSET
    if not isinstance(doi_published_time_range, Unset):
        json_doi_published_time_range = []
        for doi_published_time_range_item_data in doi_published_time_range:
            doi_published_time_range_item = doi_published_time_range_item_data.isoformat()
            json_doi_published_time_range.append(doi_published_time_range_item)

    params["doiPublishedTime__range"] = json_doi_published_time_range

    json_doi_published_time_regex: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_regex, Unset):
        json_doi_published_time_regex = doi_published_time_regex.isoformat()
    params["doiPublishedTime__regex"] = json_doi_published_time_regex

    params["doiPublishedTime__second"] = doi_published_time_second

    json_doi_published_time_startswith: Union[Unset, str] = UNSET
    if not isinstance(doi_published_time_startswith, Unset):
        json_doi_published_time_startswith = doi_published_time_startswith.isoformat()
    params["doiPublishedTime__startswith"] = json_doi_published_time_startswith

    params["doiPublishedTime__time"] = doi_published_time_time

    params["doiPublishedTime__week"] = doi_published_time_week

    params["doiPublishedTime__week_day"] = doi_published_time_week_day

    params["doiPublishedTime__year"] = doi_published_time_year

    params["dontHarvestFromProjects"] = dont_harvest_from_projects

    params["dontHarvestFromProjects__contains"] = dont_harvest_from_projects_contains

    params["dontHarvestFromProjects__endswith"] = dont_harvest_from_projects_endswith

    params["dontHarvestFromProjects__gt"] = dont_harvest_from_projects_gt

    params["dontHarvestFromProjects__gte"] = dont_harvest_from_projects_gte

    params["dontHarvestFromProjects__icontains"] = dont_harvest_from_projects_icontains

    params["dontHarvestFromProjects__iendswith"] = dont_harvest_from_projects_iendswith

    params["dontHarvestFromProjects__iexact"] = dont_harvest_from_projects_iexact

    json_dont_harvest_from_projects_in: Union[Unset, list[bool]] = UNSET
    if not isinstance(dont_harvest_from_projects_in, Unset):
        json_dont_harvest_from_projects_in = ",".join(map(str, dont_harvest_from_projects_in))

    params["dontHarvestFromProjects__in"] = json_dont_harvest_from_projects_in

    params["dontHarvestFromProjects__iregex"] = dont_harvest_from_projects_iregex

    params["dontHarvestFromProjects__isnull"] = dont_harvest_from_projects_isnull

    params["dontHarvestFromProjects__istartswith"] = dont_harvest_from_projects_istartswith

    params["dontHarvestFromProjects__lt"] = dont_harvest_from_projects_lt

    params["dontHarvestFromProjects__lte"] = dont_harvest_from_projects_lte

    json_dont_harvest_from_projects_range: Union[Unset, list[bool]] = UNSET
    if not isinstance(dont_harvest_from_projects_range, Unset):
        json_dont_harvest_from_projects_range = ",".join(map(str, dont_harvest_from_projects_range))

    params["dontHarvestFromProjects__range"] = json_dont_harvest_from_projects_range

    params["dontHarvestFromProjects__regex"] = dont_harvest_from_projects_regex

    params["dontHarvestFromProjects__startswith"] = dont_harvest_from_projects_startswith

    params["keywords"] = keywords

    params["keywords__contains"] = keywords_contains

    params["keywords__endswith"] = keywords_endswith

    params["keywords__gt"] = keywords_gt

    params["keywords__gte"] = keywords_gte

    params["keywords__icontains"] = keywords_icontains

    params["keywords__iendswith"] = keywords_iendswith

    params["keywords__iexact"] = keywords_iexact

    json_keywords_in: Union[Unset, list[str]] = UNSET
    if not isinstance(keywords_in, Unset):
        json_keywords_in = ",".join(map(str, keywords_in))

    params["keywords__in"] = json_keywords_in

    params["keywords__iregex"] = keywords_iregex

    params["keywords__isnull"] = keywords_isnull

    params["keywords__istartswith"] = keywords_istartswith

    params["keywords__lt"] = keywords_lt

    params["keywords__lte"] = keywords_lte

    json_keywords_range: Union[Unset, list[str]] = UNSET
    if not isinstance(keywords_range, Unset):
        json_keywords_range = ",".join(map(str, keywords_range))

    params["keywords__range"] = json_keywords_range

    params["keywords__regex"] = keywords_regex

    params["keywords__startswith"] = keywords_startswith

    params["limit"] = limit

    params["member__ob_id"] = member_ob_id

    json_member_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(member_ob_id_in, Unset):
        json_member_ob_id_in = ",".join(map(str, member_ob_id_in))

    params["member__ob_id__in"] = json_member_ob_id_in

    params["member__uuid"] = member_uuid

    json_member_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(member_uuid_in, Unset):
        json_member_uuid_in = ",".join(map(str, member_uuid_in))

    params["member__uuid__in"] = json_member_uuid_in

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

    json_publication_state: Union[Unset, str] = UNSET
    if not isinstance(publication_state, Unset):
        json_publication_state = publication_state.value

    params["publicationState"] = json_publication_state

    params["publicationState__contains"] = publication_state_contains

    params["publicationState__endswith"] = publication_state_endswith

    params["publicationState__gt"] = publication_state_gt

    params["publicationState__gte"] = publication_state_gte

    params["publicationState__icontains"] = publication_state_icontains

    params["publicationState__iendswith"] = publication_state_iendswith

    params["publicationState__iexact"] = publication_state_iexact

    json_publication_state_in: Union[Unset, list[str]] = UNSET
    if not isinstance(publication_state_in, Unset):
        json_publication_state_in = ",".join(map(str, publication_state_in))

    params["publicationState__in"] = json_publication_state_in

    params["publicationState__iregex"] = publication_state_iregex

    params["publicationState__isnull"] = publication_state_isnull

    params["publicationState__istartswith"] = publication_state_istartswith

    params["publicationState__lt"] = publication_state_lt

    params["publicationState__lte"] = publication_state_lte

    json_publication_state_range: Union[Unset, list[str]] = UNSET
    if not isinstance(publication_state_range, Unset):
        json_publication_state_range = ",".join(map(str, publication_state_range))

    params["publicationState__range"] = json_publication_state_range

    params["publicationState__regex"] = publication_state_regex

    params["publicationState__startswith"] = publication_state_startswith

    params["referenceable_ptr"] = referenceable_ptr

    params["referenceable_ptr__gt"] = referenceable_ptr_gt

    params["referenceable_ptr__gte"] = referenceable_ptr_gte

    json_referenceable_ptr_in: Union[Unset, list[int]] = UNSET
    if not isinstance(referenceable_ptr_in, Unset):
        json_referenceable_ptr_in = ",".join(map(str, referenceable_ptr_in))

    params["referenceable_ptr__in"] = json_referenceable_ptr_in

    params["referenceable_ptr__isnull"] = referenceable_ptr_isnull

    params["referenceable_ptr__lt"] = referenceable_ptr_lt

    params["referenceable_ptr__lte"] = referenceable_ptr_lte

    params["short_code"] = short_code

    params["short_code__contains"] = short_code_contains

    params["short_code__endswith"] = short_code_endswith

    params["short_code__gt"] = short_code_gt

    params["short_code__gte"] = short_code_gte

    params["short_code__icontains"] = short_code_icontains

    params["short_code__iendswith"] = short_code_iendswith

    params["short_code__iexact"] = short_code_iexact

    json_short_code_in: Union[Unset, list[str]] = UNSET
    if not isinstance(short_code_in, Unset):
        json_short_code_in = ",".join(map(str, short_code_in))

    params["short_code__in"] = json_short_code_in

    params["short_code__iregex"] = short_code_iregex

    params["short_code__isnull"] = short_code_isnull

    params["short_code__istartswith"] = short_code_istartswith

    params["short_code__lt"] = short_code_lt

    params["short_code__lte"] = short_code_lte

    json_short_code_range: Union[Unset, list[str]] = UNSET
    if not isinstance(short_code_range, Unset):
        json_short_code_range = ",".join(map(str, short_code_range))

    params["short_code__range"] = json_short_code_range

    params["short_code__regex"] = short_code_regex

    params["short_code__startswith"] = short_code_startswith

    params["title"] = title

    params["title__contains"] = title_contains

    params["title__endswith"] = title_endswith

    params["title__gt"] = title_gt

    params["title__gte"] = title_gte

    params["title__icontains"] = title_icontains

    params["title__iendswith"] = title_iendswith

    params["title__iexact"] = title_iexact

    json_title_in: Union[Unset, list[str]] = UNSET
    if not isinstance(title_in, Unset):
        json_title_in = ",".join(map(str, title_in))

    params["title__in"] = json_title_in

    params["title__iregex"] = title_iregex

    params["title__isnull"] = title_isnull

    params["title__istartswith"] = title_istartswith

    params["title__lt"] = title_lt

    params["title__lte"] = title_lte

    json_title_range: Union[Unset, list[str]] = UNSET
    if not isinstance(title_range, Unset):
        json_title_range = ",".join(map(str, title_range))

    params["title__range"] = json_title_range

    params["title__regex"] = title_regex

    params["title__startswith"] = title_startswith

    params["uuid"] = uuid

    params["uuid__contains"] = uuid_contains

    params["uuid__endswith"] = uuid_endswith

    params["uuid__gt"] = uuid_gt

    params["uuid__gte"] = uuid_gte

    params["uuid__icontains"] = uuid_icontains

    params["uuid__iendswith"] = uuid_iendswith

    params["uuid__iexact"] = uuid_iexact

    json_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(uuid_in, Unset):
        json_uuid_in = ",".join(map(str, uuid_in))

    params["uuid__in"] = json_uuid_in

    params["uuid__iregex"] = uuid_iregex

    params["uuid__isnull"] = uuid_isnull

    params["uuid__istartswith"] = uuid_istartswith

    params["uuid__lt"] = uuid_lt

    params["uuid__lte"] = uuid_lte

    json_uuid_range: Union[Unset, list[str]] = UNSET
    if not isinstance(uuid_range, Unset):
        json_uuid_range = ",".join(map(str, uuid_range))

    params["uuid__range"] = json_uuid_range

    params["uuid__regex"] = uuid_regex

    params["uuid__startswith"] = uuid_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/observationcollections/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedObservationCollectionReadList]:
    if response.status_code == 200:
        response_200 = PaginatedObservationCollectionReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedObservationCollectionReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    abstract: Union[Unset, str] = UNSET,
    abstract_contains: Union[Unset, str] = UNSET,
    abstract_endswith: Union[Unset, str] = UNSET,
    abstract_gt: Union[Unset, str] = UNSET,
    abstract_gte: Union[Unset, str] = UNSET,
    abstract_icontains: Union[Unset, str] = UNSET,
    abstract_iendswith: Union[Unset, str] = UNSET,
    abstract_iexact: Union[Unset, str] = UNSET,
    abstract_in: Union[Unset, list[str]] = UNSET,
    abstract_iregex: Union[Unset, str] = UNSET,
    abstract_isnull: Union[Unset, bool] = UNSET,
    abstract_istartswith: Union[Unset, str] = UNSET,
    abstract_lt: Union[Unset, str] = UNSET,
    abstract_lte: Union[Unset, str] = UNSET,
    abstract_range: Union[Unset, list[str]] = UNSET,
    abstract_regex: Union[Unset, str] = UNSET,
    abstract_startswith: Union[Unset, str] = UNSET,
    data_published_time: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_contains: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_date: Union[Unset, datetime.date] = UNSET,
    data_published_time_day: Union[Unset, float] = UNSET,
    data_published_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_gt: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_gte: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_hour: Union[Unset, float] = UNSET,
    data_published_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    data_published_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_isnull: Union[Unset, bool] = UNSET,
    data_published_time_iso_week_day: Union[Unset, float] = UNSET,
    data_published_time_iso_year: Union[Unset, float] = UNSET,
    data_published_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_lt: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_lte: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_minute: Union[Unset, float] = UNSET,
    data_published_time_month: Union[Unset, float] = UNSET,
    data_published_time_quarter: Union[Unset, float] = UNSET,
    data_published_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    data_published_time_regex: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_second: Union[Unset, float] = UNSET,
    data_published_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_time: Union[Unset, str] = UNSET,
    data_published_time_week: Union[Unset, float] = UNSET,
    data_published_time_week_day: Union[Unset, float] = UNSET,
    data_published_time_year: Union[Unset, float] = UNSET,
    discovery_keywords_name: Union[Unset, str] = UNSET,
    discovery_keywords_name_contains: Union[Unset, str] = UNSET,
    doi_published_time: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_contains: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_date: Union[Unset, datetime.date] = UNSET,
    doi_published_time_day: Union[Unset, float] = UNSET,
    doi_published_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_gt: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_gte: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_hour: Union[Unset, float] = UNSET,
    doi_published_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    doi_published_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_isnull: Union[Unset, bool] = UNSET,
    doi_published_time_iso_week_day: Union[Unset, float] = UNSET,
    doi_published_time_iso_year: Union[Unset, float] = UNSET,
    doi_published_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_lt: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_lte: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_minute: Union[Unset, float] = UNSET,
    doi_published_time_month: Union[Unset, float] = UNSET,
    doi_published_time_quarter: Union[Unset, float] = UNSET,
    doi_published_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    doi_published_time_regex: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_second: Union[Unset, float] = UNSET,
    doi_published_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_time: Union[Unset, str] = UNSET,
    doi_published_time_week: Union[Unset, float] = UNSET,
    doi_published_time_week_day: Union[Unset, float] = UNSET,
    doi_published_time_year: Union[Unset, float] = UNSET,
    dont_harvest_from_projects: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_contains: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_endswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_gt: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_gte: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_icontains: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_iendswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_iexact: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_in: Union[Unset, list[bool]] = UNSET,
    dont_harvest_from_projects_iregex: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_isnull: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_istartswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_lt: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_lte: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_range: Union[Unset, list[bool]] = UNSET,
    dont_harvest_from_projects_regex: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_startswith: Union[Unset, bool] = UNSET,
    keywords: Union[Unset, str] = UNSET,
    keywords_contains: Union[Unset, str] = UNSET,
    keywords_endswith: Union[Unset, str] = UNSET,
    keywords_gt: Union[Unset, str] = UNSET,
    keywords_gte: Union[Unset, str] = UNSET,
    keywords_icontains: Union[Unset, str] = UNSET,
    keywords_iendswith: Union[Unset, str] = UNSET,
    keywords_iexact: Union[Unset, str] = UNSET,
    keywords_in: Union[Unset, list[str]] = UNSET,
    keywords_iregex: Union[Unset, str] = UNSET,
    keywords_isnull: Union[Unset, bool] = UNSET,
    keywords_istartswith: Union[Unset, str] = UNSET,
    keywords_lt: Union[Unset, str] = UNSET,
    keywords_lte: Union[Unset, str] = UNSET,
    keywords_range: Union[Unset, list[str]] = UNSET,
    keywords_regex: Union[Unset, str] = UNSET,
    keywords_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    member_ob_id: Union[Unset, int] = UNSET,
    member_ob_id_in: Union[Unset, list[int]] = UNSET,
    member_uuid: Union[Unset, str] = UNSET,
    member_uuid_in: Union[Unset, list[str]] = UNSET,
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
    publication_state: Union[Unset, ObservationcollectionsListPublicationState] = UNSET,
    publication_state_contains: Union[Unset, str] = UNSET,
    publication_state_endswith: Union[Unset, str] = UNSET,
    publication_state_gt: Union[Unset, str] = UNSET,
    publication_state_gte: Union[Unset, str] = UNSET,
    publication_state_icontains: Union[Unset, str] = UNSET,
    publication_state_iendswith: Union[Unset, str] = UNSET,
    publication_state_iexact: Union[Unset, str] = UNSET,
    publication_state_in: Union[Unset, list[str]] = UNSET,
    publication_state_iregex: Union[Unset, str] = UNSET,
    publication_state_isnull: Union[Unset, bool] = UNSET,
    publication_state_istartswith: Union[Unset, str] = UNSET,
    publication_state_lt: Union[Unset, str] = UNSET,
    publication_state_lte: Union[Unset, str] = UNSET,
    publication_state_range: Union[Unset, list[str]] = UNSET,
    publication_state_regex: Union[Unset, str] = UNSET,
    publication_state_startswith: Union[Unset, str] = UNSET,
    referenceable_ptr: Union[Unset, int] = UNSET,
    referenceable_ptr_gt: Union[Unset, int] = UNSET,
    referenceable_ptr_gte: Union[Unset, int] = UNSET,
    referenceable_ptr_in: Union[Unset, list[int]] = UNSET,
    referenceable_ptr_isnull: Union[Unset, bool] = UNSET,
    referenceable_ptr_lt: Union[Unset, int] = UNSET,
    referenceable_ptr_lte: Union[Unset, int] = UNSET,
    short_code: Union[Unset, str] = UNSET,
    short_code_contains: Union[Unset, str] = UNSET,
    short_code_endswith: Union[Unset, str] = UNSET,
    short_code_gt: Union[Unset, str] = UNSET,
    short_code_gte: Union[Unset, str] = UNSET,
    short_code_icontains: Union[Unset, str] = UNSET,
    short_code_iendswith: Union[Unset, str] = UNSET,
    short_code_iexact: Union[Unset, str] = UNSET,
    short_code_in: Union[Unset, list[str]] = UNSET,
    short_code_iregex: Union[Unset, str] = UNSET,
    short_code_isnull: Union[Unset, bool] = UNSET,
    short_code_istartswith: Union[Unset, str] = UNSET,
    short_code_lt: Union[Unset, str] = UNSET,
    short_code_lte: Union[Unset, str] = UNSET,
    short_code_range: Union[Unset, list[str]] = UNSET,
    short_code_regex: Union[Unset, str] = UNSET,
    short_code_startswith: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    title_contains: Union[Unset, str] = UNSET,
    title_endswith: Union[Unset, str] = UNSET,
    title_gt: Union[Unset, str] = UNSET,
    title_gte: Union[Unset, str] = UNSET,
    title_icontains: Union[Unset, str] = UNSET,
    title_iendswith: Union[Unset, str] = UNSET,
    title_iexact: Union[Unset, str] = UNSET,
    title_in: Union[Unset, list[str]] = UNSET,
    title_iregex: Union[Unset, str] = UNSET,
    title_isnull: Union[Unset, bool] = UNSET,
    title_istartswith: Union[Unset, str] = UNSET,
    title_lt: Union[Unset, str] = UNSET,
    title_lte: Union[Unset, str] = UNSET,
    title_range: Union[Unset, list[str]] = UNSET,
    title_regex: Union[Unset, str] = UNSET,
    title_startswith: Union[Unset, str] = UNSET,
    uuid: Union[Unset, str] = UNSET,
    uuid_contains: Union[Unset, str] = UNSET,
    uuid_endswith: Union[Unset, str] = UNSET,
    uuid_gt: Union[Unset, str] = UNSET,
    uuid_gte: Union[Unset, str] = UNSET,
    uuid_icontains: Union[Unset, str] = UNSET,
    uuid_iendswith: Union[Unset, str] = UNSET,
    uuid_iexact: Union[Unset, str] = UNSET,
    uuid_in: Union[Unset, list[str]] = UNSET,
    uuid_iregex: Union[Unset, str] = UNSET,
    uuid_isnull: Union[Unset, bool] = UNSET,
    uuid_istartswith: Union[Unset, str] = UNSET,
    uuid_lt: Union[Unset, str] = UNSET,
    uuid_lte: Union[Unset, str] = UNSET,
    uuid_range: Union[Unset, list[str]] = UNSET,
    uuid_regex: Union[Unset, str] = UNSET,
    uuid_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedObservationCollectionReadList]:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        abstract (Union[Unset, str]):
        abstract_contains (Union[Unset, str]):
        abstract_endswith (Union[Unset, str]):
        abstract_gt (Union[Unset, str]):
        abstract_gte (Union[Unset, str]):
        abstract_icontains (Union[Unset, str]):
        abstract_iendswith (Union[Unset, str]):
        abstract_iexact (Union[Unset, str]):
        abstract_in (Union[Unset, list[str]]):
        abstract_iregex (Union[Unset, str]):
        abstract_isnull (Union[Unset, bool]):
        abstract_istartswith (Union[Unset, str]):
        abstract_lt (Union[Unset, str]):
        abstract_lte (Union[Unset, str]):
        abstract_range (Union[Unset, list[str]]):
        abstract_regex (Union[Unset, str]):
        abstract_startswith (Union[Unset, str]):
        data_published_time (Union[Unset, datetime.datetime]):
        data_published_time_contained_by (Union[Unset, datetime.datetime]):
        data_published_time_contains (Union[Unset, datetime.datetime]):
        data_published_time_date (Union[Unset, datetime.date]):
        data_published_time_day (Union[Unset, float]):
        data_published_time_endswith (Union[Unset, datetime.datetime]):
        data_published_time_gt (Union[Unset, datetime.datetime]):
        data_published_time_gte (Union[Unset, datetime.datetime]):
        data_published_time_hour (Union[Unset, float]):
        data_published_time_icontains (Union[Unset, datetime.datetime]):
        data_published_time_iendswith (Union[Unset, datetime.datetime]):
        data_published_time_iexact (Union[Unset, datetime.datetime]):
        data_published_time_in (Union[Unset, list[datetime.datetime]]):
        data_published_time_iregex (Union[Unset, datetime.datetime]):
        data_published_time_isnull (Union[Unset, bool]):
        data_published_time_iso_week_day (Union[Unset, float]):
        data_published_time_iso_year (Union[Unset, float]):
        data_published_time_istartswith (Union[Unset, datetime.datetime]):
        data_published_time_lt (Union[Unset, datetime.datetime]):
        data_published_time_lte (Union[Unset, datetime.datetime]):
        data_published_time_minute (Union[Unset, float]):
        data_published_time_month (Union[Unset, float]):
        data_published_time_quarter (Union[Unset, float]):
        data_published_time_range (Union[Unset, list[datetime.datetime]]):
        data_published_time_regex (Union[Unset, datetime.datetime]):
        data_published_time_second (Union[Unset, float]):
        data_published_time_startswith (Union[Unset, datetime.datetime]):
        data_published_time_time (Union[Unset, str]):
        data_published_time_week (Union[Unset, float]):
        data_published_time_week_day (Union[Unset, float]):
        data_published_time_year (Union[Unset, float]):
        discovery_keywords_name (Union[Unset, str]):
        discovery_keywords_name_contains (Union[Unset, str]):
        doi_published_time (Union[Unset, datetime.datetime]):
        doi_published_time_contained_by (Union[Unset, datetime.datetime]):
        doi_published_time_contains (Union[Unset, datetime.datetime]):
        doi_published_time_date (Union[Unset, datetime.date]):
        doi_published_time_day (Union[Unset, float]):
        doi_published_time_endswith (Union[Unset, datetime.datetime]):
        doi_published_time_gt (Union[Unset, datetime.datetime]):
        doi_published_time_gte (Union[Unset, datetime.datetime]):
        doi_published_time_hour (Union[Unset, float]):
        doi_published_time_icontains (Union[Unset, datetime.datetime]):
        doi_published_time_iendswith (Union[Unset, datetime.datetime]):
        doi_published_time_iexact (Union[Unset, datetime.datetime]):
        doi_published_time_in (Union[Unset, list[datetime.datetime]]):
        doi_published_time_iregex (Union[Unset, datetime.datetime]):
        doi_published_time_isnull (Union[Unset, bool]):
        doi_published_time_iso_week_day (Union[Unset, float]):
        doi_published_time_iso_year (Union[Unset, float]):
        doi_published_time_istartswith (Union[Unset, datetime.datetime]):
        doi_published_time_lt (Union[Unset, datetime.datetime]):
        doi_published_time_lte (Union[Unset, datetime.datetime]):
        doi_published_time_minute (Union[Unset, float]):
        doi_published_time_month (Union[Unset, float]):
        doi_published_time_quarter (Union[Unset, float]):
        doi_published_time_range (Union[Unset, list[datetime.datetime]]):
        doi_published_time_regex (Union[Unset, datetime.datetime]):
        doi_published_time_second (Union[Unset, float]):
        doi_published_time_startswith (Union[Unset, datetime.datetime]):
        doi_published_time_time (Union[Unset, str]):
        doi_published_time_week (Union[Unset, float]):
        doi_published_time_week_day (Union[Unset, float]):
        doi_published_time_year (Union[Unset, float]):
        dont_harvest_from_projects (Union[Unset, bool]):
        dont_harvest_from_projects_contains (Union[Unset, bool]):
        dont_harvest_from_projects_endswith (Union[Unset, bool]):
        dont_harvest_from_projects_gt (Union[Unset, bool]):
        dont_harvest_from_projects_gte (Union[Unset, bool]):
        dont_harvest_from_projects_icontains (Union[Unset, bool]):
        dont_harvest_from_projects_iendswith (Union[Unset, bool]):
        dont_harvest_from_projects_iexact (Union[Unset, bool]):
        dont_harvest_from_projects_in (Union[Unset, list[bool]]):
        dont_harvest_from_projects_iregex (Union[Unset, bool]):
        dont_harvest_from_projects_isnull (Union[Unset, bool]):
        dont_harvest_from_projects_istartswith (Union[Unset, bool]):
        dont_harvest_from_projects_lt (Union[Unset, bool]):
        dont_harvest_from_projects_lte (Union[Unset, bool]):
        dont_harvest_from_projects_range (Union[Unset, list[bool]]):
        dont_harvest_from_projects_regex (Union[Unset, bool]):
        dont_harvest_from_projects_startswith (Union[Unset, bool]):
        keywords (Union[Unset, str]):
        keywords_contains (Union[Unset, str]):
        keywords_endswith (Union[Unset, str]):
        keywords_gt (Union[Unset, str]):
        keywords_gte (Union[Unset, str]):
        keywords_icontains (Union[Unset, str]):
        keywords_iendswith (Union[Unset, str]):
        keywords_iexact (Union[Unset, str]):
        keywords_in (Union[Unset, list[str]]):
        keywords_iregex (Union[Unset, str]):
        keywords_isnull (Union[Unset, bool]):
        keywords_istartswith (Union[Unset, str]):
        keywords_lt (Union[Unset, str]):
        keywords_lte (Union[Unset, str]):
        keywords_range (Union[Unset, list[str]]):
        keywords_regex (Union[Unset, str]):
        keywords_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        member_ob_id (Union[Unset, int]):
        member_ob_id_in (Union[Unset, list[int]]):
        member_uuid (Union[Unset, str]):
        member_uuid_in (Union[Unset, list[str]]):
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
        publication_state (Union[Unset, ObservationcollectionsListPublicationState]):
        publication_state_contains (Union[Unset, str]):
        publication_state_endswith (Union[Unset, str]):
        publication_state_gt (Union[Unset, str]):
        publication_state_gte (Union[Unset, str]):
        publication_state_icontains (Union[Unset, str]):
        publication_state_iendswith (Union[Unset, str]):
        publication_state_iexact (Union[Unset, str]):
        publication_state_in (Union[Unset, list[str]]):
        publication_state_iregex (Union[Unset, str]):
        publication_state_isnull (Union[Unset, bool]):
        publication_state_istartswith (Union[Unset, str]):
        publication_state_lt (Union[Unset, str]):
        publication_state_lte (Union[Unset, str]):
        publication_state_range (Union[Unset, list[str]]):
        publication_state_regex (Union[Unset, str]):
        publication_state_startswith (Union[Unset, str]):
        referenceable_ptr (Union[Unset, int]):
        referenceable_ptr_gt (Union[Unset, int]):
        referenceable_ptr_gte (Union[Unset, int]):
        referenceable_ptr_in (Union[Unset, list[int]]):
        referenceable_ptr_isnull (Union[Unset, bool]):
        referenceable_ptr_lt (Union[Unset, int]):
        referenceable_ptr_lte (Union[Unset, int]):
        short_code (Union[Unset, str]):
        short_code_contains (Union[Unset, str]):
        short_code_endswith (Union[Unset, str]):
        short_code_gt (Union[Unset, str]):
        short_code_gte (Union[Unset, str]):
        short_code_icontains (Union[Unset, str]):
        short_code_iendswith (Union[Unset, str]):
        short_code_iexact (Union[Unset, str]):
        short_code_in (Union[Unset, list[str]]):
        short_code_iregex (Union[Unset, str]):
        short_code_isnull (Union[Unset, bool]):
        short_code_istartswith (Union[Unset, str]):
        short_code_lt (Union[Unset, str]):
        short_code_lte (Union[Unset, str]):
        short_code_range (Union[Unset, list[str]]):
        short_code_regex (Union[Unset, str]):
        short_code_startswith (Union[Unset, str]):
        title (Union[Unset, str]):
        title_contains (Union[Unset, str]):
        title_endswith (Union[Unset, str]):
        title_gt (Union[Unset, str]):
        title_gte (Union[Unset, str]):
        title_icontains (Union[Unset, str]):
        title_iendswith (Union[Unset, str]):
        title_iexact (Union[Unset, str]):
        title_in (Union[Unset, list[str]]):
        title_iregex (Union[Unset, str]):
        title_isnull (Union[Unset, bool]):
        title_istartswith (Union[Unset, str]):
        title_lt (Union[Unset, str]):
        title_lte (Union[Unset, str]):
        title_range (Union[Unset, list[str]]):
        title_regex (Union[Unset, str]):
        title_startswith (Union[Unset, str]):
        uuid (Union[Unset, str]):
        uuid_contains (Union[Unset, str]):
        uuid_endswith (Union[Unset, str]):
        uuid_gt (Union[Unset, str]):
        uuid_gte (Union[Unset, str]):
        uuid_icontains (Union[Unset, str]):
        uuid_iendswith (Union[Unset, str]):
        uuid_iexact (Union[Unset, str]):
        uuid_in (Union[Unset, list[str]]):
        uuid_iregex (Union[Unset, str]):
        uuid_isnull (Union[Unset, bool]):
        uuid_istartswith (Union[Unset, str]):
        uuid_lt (Union[Unset, str]):
        uuid_lte (Union[Unset, str]):
        uuid_range (Union[Unset, list[str]]):
        uuid_regex (Union[Unset, str]):
        uuid_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedObservationCollectionReadList]
    """

    kwargs = _get_kwargs(
        abstract=abstract,
        abstract_contains=abstract_contains,
        abstract_endswith=abstract_endswith,
        abstract_gt=abstract_gt,
        abstract_gte=abstract_gte,
        abstract_icontains=abstract_icontains,
        abstract_iendswith=abstract_iendswith,
        abstract_iexact=abstract_iexact,
        abstract_in=abstract_in,
        abstract_iregex=abstract_iregex,
        abstract_isnull=abstract_isnull,
        abstract_istartswith=abstract_istartswith,
        abstract_lt=abstract_lt,
        abstract_lte=abstract_lte,
        abstract_range=abstract_range,
        abstract_regex=abstract_regex,
        abstract_startswith=abstract_startswith,
        data_published_time=data_published_time,
        data_published_time_contained_by=data_published_time_contained_by,
        data_published_time_contains=data_published_time_contains,
        data_published_time_date=data_published_time_date,
        data_published_time_day=data_published_time_day,
        data_published_time_endswith=data_published_time_endswith,
        data_published_time_gt=data_published_time_gt,
        data_published_time_gte=data_published_time_gte,
        data_published_time_hour=data_published_time_hour,
        data_published_time_icontains=data_published_time_icontains,
        data_published_time_iendswith=data_published_time_iendswith,
        data_published_time_iexact=data_published_time_iexact,
        data_published_time_in=data_published_time_in,
        data_published_time_iregex=data_published_time_iregex,
        data_published_time_isnull=data_published_time_isnull,
        data_published_time_iso_week_day=data_published_time_iso_week_day,
        data_published_time_iso_year=data_published_time_iso_year,
        data_published_time_istartswith=data_published_time_istartswith,
        data_published_time_lt=data_published_time_lt,
        data_published_time_lte=data_published_time_lte,
        data_published_time_minute=data_published_time_minute,
        data_published_time_month=data_published_time_month,
        data_published_time_quarter=data_published_time_quarter,
        data_published_time_range=data_published_time_range,
        data_published_time_regex=data_published_time_regex,
        data_published_time_second=data_published_time_second,
        data_published_time_startswith=data_published_time_startswith,
        data_published_time_time=data_published_time_time,
        data_published_time_week=data_published_time_week,
        data_published_time_week_day=data_published_time_week_day,
        data_published_time_year=data_published_time_year,
        discovery_keywords_name=discovery_keywords_name,
        discovery_keywords_name_contains=discovery_keywords_name_contains,
        doi_published_time=doi_published_time,
        doi_published_time_contained_by=doi_published_time_contained_by,
        doi_published_time_contains=doi_published_time_contains,
        doi_published_time_date=doi_published_time_date,
        doi_published_time_day=doi_published_time_day,
        doi_published_time_endswith=doi_published_time_endswith,
        doi_published_time_gt=doi_published_time_gt,
        doi_published_time_gte=doi_published_time_gte,
        doi_published_time_hour=doi_published_time_hour,
        doi_published_time_icontains=doi_published_time_icontains,
        doi_published_time_iendswith=doi_published_time_iendswith,
        doi_published_time_iexact=doi_published_time_iexact,
        doi_published_time_in=doi_published_time_in,
        doi_published_time_iregex=doi_published_time_iregex,
        doi_published_time_isnull=doi_published_time_isnull,
        doi_published_time_iso_week_day=doi_published_time_iso_week_day,
        doi_published_time_iso_year=doi_published_time_iso_year,
        doi_published_time_istartswith=doi_published_time_istartswith,
        doi_published_time_lt=doi_published_time_lt,
        doi_published_time_lte=doi_published_time_lte,
        doi_published_time_minute=doi_published_time_minute,
        doi_published_time_month=doi_published_time_month,
        doi_published_time_quarter=doi_published_time_quarter,
        doi_published_time_range=doi_published_time_range,
        doi_published_time_regex=doi_published_time_regex,
        doi_published_time_second=doi_published_time_second,
        doi_published_time_startswith=doi_published_time_startswith,
        doi_published_time_time=doi_published_time_time,
        doi_published_time_week=doi_published_time_week,
        doi_published_time_week_day=doi_published_time_week_day,
        doi_published_time_year=doi_published_time_year,
        dont_harvest_from_projects=dont_harvest_from_projects,
        dont_harvest_from_projects_contains=dont_harvest_from_projects_contains,
        dont_harvest_from_projects_endswith=dont_harvest_from_projects_endswith,
        dont_harvest_from_projects_gt=dont_harvest_from_projects_gt,
        dont_harvest_from_projects_gte=dont_harvest_from_projects_gte,
        dont_harvest_from_projects_icontains=dont_harvest_from_projects_icontains,
        dont_harvest_from_projects_iendswith=dont_harvest_from_projects_iendswith,
        dont_harvest_from_projects_iexact=dont_harvest_from_projects_iexact,
        dont_harvest_from_projects_in=dont_harvest_from_projects_in,
        dont_harvest_from_projects_iregex=dont_harvest_from_projects_iregex,
        dont_harvest_from_projects_isnull=dont_harvest_from_projects_isnull,
        dont_harvest_from_projects_istartswith=dont_harvest_from_projects_istartswith,
        dont_harvest_from_projects_lt=dont_harvest_from_projects_lt,
        dont_harvest_from_projects_lte=dont_harvest_from_projects_lte,
        dont_harvest_from_projects_range=dont_harvest_from_projects_range,
        dont_harvest_from_projects_regex=dont_harvest_from_projects_regex,
        dont_harvest_from_projects_startswith=dont_harvest_from_projects_startswith,
        keywords=keywords,
        keywords_contains=keywords_contains,
        keywords_endswith=keywords_endswith,
        keywords_gt=keywords_gt,
        keywords_gte=keywords_gte,
        keywords_icontains=keywords_icontains,
        keywords_iendswith=keywords_iendswith,
        keywords_iexact=keywords_iexact,
        keywords_in=keywords_in,
        keywords_iregex=keywords_iregex,
        keywords_isnull=keywords_isnull,
        keywords_istartswith=keywords_istartswith,
        keywords_lt=keywords_lt,
        keywords_lte=keywords_lte,
        keywords_range=keywords_range,
        keywords_regex=keywords_regex,
        keywords_startswith=keywords_startswith,
        limit=limit,
        member_ob_id=member_ob_id,
        member_ob_id_in=member_ob_id_in,
        member_uuid=member_uuid,
        member_uuid_in=member_uuid_in,
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
        publication_state=publication_state,
        publication_state_contains=publication_state_contains,
        publication_state_endswith=publication_state_endswith,
        publication_state_gt=publication_state_gt,
        publication_state_gte=publication_state_gte,
        publication_state_icontains=publication_state_icontains,
        publication_state_iendswith=publication_state_iendswith,
        publication_state_iexact=publication_state_iexact,
        publication_state_in=publication_state_in,
        publication_state_iregex=publication_state_iregex,
        publication_state_isnull=publication_state_isnull,
        publication_state_istartswith=publication_state_istartswith,
        publication_state_lt=publication_state_lt,
        publication_state_lte=publication_state_lte,
        publication_state_range=publication_state_range,
        publication_state_regex=publication_state_regex,
        publication_state_startswith=publication_state_startswith,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_gt=referenceable_ptr_gt,
        referenceable_ptr_gte=referenceable_ptr_gte,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        referenceable_ptr_lt=referenceable_ptr_lt,
        referenceable_ptr_lte=referenceable_ptr_lte,
        short_code=short_code,
        short_code_contains=short_code_contains,
        short_code_endswith=short_code_endswith,
        short_code_gt=short_code_gt,
        short_code_gte=short_code_gte,
        short_code_icontains=short_code_icontains,
        short_code_iendswith=short_code_iendswith,
        short_code_iexact=short_code_iexact,
        short_code_in=short_code_in,
        short_code_iregex=short_code_iregex,
        short_code_isnull=short_code_isnull,
        short_code_istartswith=short_code_istartswith,
        short_code_lt=short_code_lt,
        short_code_lte=short_code_lte,
        short_code_range=short_code_range,
        short_code_regex=short_code_regex,
        short_code_startswith=short_code_startswith,
        title=title,
        title_contains=title_contains,
        title_endswith=title_endswith,
        title_gt=title_gt,
        title_gte=title_gte,
        title_icontains=title_icontains,
        title_iendswith=title_iendswith,
        title_iexact=title_iexact,
        title_in=title_in,
        title_iregex=title_iregex,
        title_isnull=title_isnull,
        title_istartswith=title_istartswith,
        title_lt=title_lt,
        title_lte=title_lte,
        title_range=title_range,
        title_regex=title_regex,
        title_startswith=title_startswith,
        uuid=uuid,
        uuid_contains=uuid_contains,
        uuid_endswith=uuid_endswith,
        uuid_gt=uuid_gt,
        uuid_gte=uuid_gte,
        uuid_icontains=uuid_icontains,
        uuid_iendswith=uuid_iendswith,
        uuid_iexact=uuid_iexact,
        uuid_in=uuid_in,
        uuid_iregex=uuid_iregex,
        uuid_isnull=uuid_isnull,
        uuid_istartswith=uuid_istartswith,
        uuid_lt=uuid_lt,
        uuid_lte=uuid_lte,
        uuid_range=uuid_range,
        uuid_regex=uuid_regex,
        uuid_startswith=uuid_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    abstract: Union[Unset, str] = UNSET,
    abstract_contains: Union[Unset, str] = UNSET,
    abstract_endswith: Union[Unset, str] = UNSET,
    abstract_gt: Union[Unset, str] = UNSET,
    abstract_gte: Union[Unset, str] = UNSET,
    abstract_icontains: Union[Unset, str] = UNSET,
    abstract_iendswith: Union[Unset, str] = UNSET,
    abstract_iexact: Union[Unset, str] = UNSET,
    abstract_in: Union[Unset, list[str]] = UNSET,
    abstract_iregex: Union[Unset, str] = UNSET,
    abstract_isnull: Union[Unset, bool] = UNSET,
    abstract_istartswith: Union[Unset, str] = UNSET,
    abstract_lt: Union[Unset, str] = UNSET,
    abstract_lte: Union[Unset, str] = UNSET,
    abstract_range: Union[Unset, list[str]] = UNSET,
    abstract_regex: Union[Unset, str] = UNSET,
    abstract_startswith: Union[Unset, str] = UNSET,
    data_published_time: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_contains: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_date: Union[Unset, datetime.date] = UNSET,
    data_published_time_day: Union[Unset, float] = UNSET,
    data_published_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_gt: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_gte: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_hour: Union[Unset, float] = UNSET,
    data_published_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    data_published_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_isnull: Union[Unset, bool] = UNSET,
    data_published_time_iso_week_day: Union[Unset, float] = UNSET,
    data_published_time_iso_year: Union[Unset, float] = UNSET,
    data_published_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_lt: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_lte: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_minute: Union[Unset, float] = UNSET,
    data_published_time_month: Union[Unset, float] = UNSET,
    data_published_time_quarter: Union[Unset, float] = UNSET,
    data_published_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    data_published_time_regex: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_second: Union[Unset, float] = UNSET,
    data_published_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_time: Union[Unset, str] = UNSET,
    data_published_time_week: Union[Unset, float] = UNSET,
    data_published_time_week_day: Union[Unset, float] = UNSET,
    data_published_time_year: Union[Unset, float] = UNSET,
    discovery_keywords_name: Union[Unset, str] = UNSET,
    discovery_keywords_name_contains: Union[Unset, str] = UNSET,
    doi_published_time: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_contains: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_date: Union[Unset, datetime.date] = UNSET,
    doi_published_time_day: Union[Unset, float] = UNSET,
    doi_published_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_gt: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_gte: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_hour: Union[Unset, float] = UNSET,
    doi_published_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    doi_published_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_isnull: Union[Unset, bool] = UNSET,
    doi_published_time_iso_week_day: Union[Unset, float] = UNSET,
    doi_published_time_iso_year: Union[Unset, float] = UNSET,
    doi_published_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_lt: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_lte: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_minute: Union[Unset, float] = UNSET,
    doi_published_time_month: Union[Unset, float] = UNSET,
    doi_published_time_quarter: Union[Unset, float] = UNSET,
    doi_published_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    doi_published_time_regex: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_second: Union[Unset, float] = UNSET,
    doi_published_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_time: Union[Unset, str] = UNSET,
    doi_published_time_week: Union[Unset, float] = UNSET,
    doi_published_time_week_day: Union[Unset, float] = UNSET,
    doi_published_time_year: Union[Unset, float] = UNSET,
    dont_harvest_from_projects: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_contains: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_endswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_gt: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_gte: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_icontains: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_iendswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_iexact: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_in: Union[Unset, list[bool]] = UNSET,
    dont_harvest_from_projects_iregex: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_isnull: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_istartswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_lt: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_lte: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_range: Union[Unset, list[bool]] = UNSET,
    dont_harvest_from_projects_regex: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_startswith: Union[Unset, bool] = UNSET,
    keywords: Union[Unset, str] = UNSET,
    keywords_contains: Union[Unset, str] = UNSET,
    keywords_endswith: Union[Unset, str] = UNSET,
    keywords_gt: Union[Unset, str] = UNSET,
    keywords_gte: Union[Unset, str] = UNSET,
    keywords_icontains: Union[Unset, str] = UNSET,
    keywords_iendswith: Union[Unset, str] = UNSET,
    keywords_iexact: Union[Unset, str] = UNSET,
    keywords_in: Union[Unset, list[str]] = UNSET,
    keywords_iregex: Union[Unset, str] = UNSET,
    keywords_isnull: Union[Unset, bool] = UNSET,
    keywords_istartswith: Union[Unset, str] = UNSET,
    keywords_lt: Union[Unset, str] = UNSET,
    keywords_lte: Union[Unset, str] = UNSET,
    keywords_range: Union[Unset, list[str]] = UNSET,
    keywords_regex: Union[Unset, str] = UNSET,
    keywords_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    member_ob_id: Union[Unset, int] = UNSET,
    member_ob_id_in: Union[Unset, list[int]] = UNSET,
    member_uuid: Union[Unset, str] = UNSET,
    member_uuid_in: Union[Unset, list[str]] = UNSET,
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
    publication_state: Union[Unset, ObservationcollectionsListPublicationState] = UNSET,
    publication_state_contains: Union[Unset, str] = UNSET,
    publication_state_endswith: Union[Unset, str] = UNSET,
    publication_state_gt: Union[Unset, str] = UNSET,
    publication_state_gte: Union[Unset, str] = UNSET,
    publication_state_icontains: Union[Unset, str] = UNSET,
    publication_state_iendswith: Union[Unset, str] = UNSET,
    publication_state_iexact: Union[Unset, str] = UNSET,
    publication_state_in: Union[Unset, list[str]] = UNSET,
    publication_state_iregex: Union[Unset, str] = UNSET,
    publication_state_isnull: Union[Unset, bool] = UNSET,
    publication_state_istartswith: Union[Unset, str] = UNSET,
    publication_state_lt: Union[Unset, str] = UNSET,
    publication_state_lte: Union[Unset, str] = UNSET,
    publication_state_range: Union[Unset, list[str]] = UNSET,
    publication_state_regex: Union[Unset, str] = UNSET,
    publication_state_startswith: Union[Unset, str] = UNSET,
    referenceable_ptr: Union[Unset, int] = UNSET,
    referenceable_ptr_gt: Union[Unset, int] = UNSET,
    referenceable_ptr_gte: Union[Unset, int] = UNSET,
    referenceable_ptr_in: Union[Unset, list[int]] = UNSET,
    referenceable_ptr_isnull: Union[Unset, bool] = UNSET,
    referenceable_ptr_lt: Union[Unset, int] = UNSET,
    referenceable_ptr_lte: Union[Unset, int] = UNSET,
    short_code: Union[Unset, str] = UNSET,
    short_code_contains: Union[Unset, str] = UNSET,
    short_code_endswith: Union[Unset, str] = UNSET,
    short_code_gt: Union[Unset, str] = UNSET,
    short_code_gte: Union[Unset, str] = UNSET,
    short_code_icontains: Union[Unset, str] = UNSET,
    short_code_iendswith: Union[Unset, str] = UNSET,
    short_code_iexact: Union[Unset, str] = UNSET,
    short_code_in: Union[Unset, list[str]] = UNSET,
    short_code_iregex: Union[Unset, str] = UNSET,
    short_code_isnull: Union[Unset, bool] = UNSET,
    short_code_istartswith: Union[Unset, str] = UNSET,
    short_code_lt: Union[Unset, str] = UNSET,
    short_code_lte: Union[Unset, str] = UNSET,
    short_code_range: Union[Unset, list[str]] = UNSET,
    short_code_regex: Union[Unset, str] = UNSET,
    short_code_startswith: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    title_contains: Union[Unset, str] = UNSET,
    title_endswith: Union[Unset, str] = UNSET,
    title_gt: Union[Unset, str] = UNSET,
    title_gte: Union[Unset, str] = UNSET,
    title_icontains: Union[Unset, str] = UNSET,
    title_iendswith: Union[Unset, str] = UNSET,
    title_iexact: Union[Unset, str] = UNSET,
    title_in: Union[Unset, list[str]] = UNSET,
    title_iregex: Union[Unset, str] = UNSET,
    title_isnull: Union[Unset, bool] = UNSET,
    title_istartswith: Union[Unset, str] = UNSET,
    title_lt: Union[Unset, str] = UNSET,
    title_lte: Union[Unset, str] = UNSET,
    title_range: Union[Unset, list[str]] = UNSET,
    title_regex: Union[Unset, str] = UNSET,
    title_startswith: Union[Unset, str] = UNSET,
    uuid: Union[Unset, str] = UNSET,
    uuid_contains: Union[Unset, str] = UNSET,
    uuid_endswith: Union[Unset, str] = UNSET,
    uuid_gt: Union[Unset, str] = UNSET,
    uuid_gte: Union[Unset, str] = UNSET,
    uuid_icontains: Union[Unset, str] = UNSET,
    uuid_iendswith: Union[Unset, str] = UNSET,
    uuid_iexact: Union[Unset, str] = UNSET,
    uuid_in: Union[Unset, list[str]] = UNSET,
    uuid_iregex: Union[Unset, str] = UNSET,
    uuid_isnull: Union[Unset, bool] = UNSET,
    uuid_istartswith: Union[Unset, str] = UNSET,
    uuid_lt: Union[Unset, str] = UNSET,
    uuid_lte: Union[Unset, str] = UNSET,
    uuid_range: Union[Unset, list[str]] = UNSET,
    uuid_regex: Union[Unset, str] = UNSET,
    uuid_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedObservationCollectionReadList]:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        abstract (Union[Unset, str]):
        abstract_contains (Union[Unset, str]):
        abstract_endswith (Union[Unset, str]):
        abstract_gt (Union[Unset, str]):
        abstract_gte (Union[Unset, str]):
        abstract_icontains (Union[Unset, str]):
        abstract_iendswith (Union[Unset, str]):
        abstract_iexact (Union[Unset, str]):
        abstract_in (Union[Unset, list[str]]):
        abstract_iregex (Union[Unset, str]):
        abstract_isnull (Union[Unset, bool]):
        abstract_istartswith (Union[Unset, str]):
        abstract_lt (Union[Unset, str]):
        abstract_lte (Union[Unset, str]):
        abstract_range (Union[Unset, list[str]]):
        abstract_regex (Union[Unset, str]):
        abstract_startswith (Union[Unset, str]):
        data_published_time (Union[Unset, datetime.datetime]):
        data_published_time_contained_by (Union[Unset, datetime.datetime]):
        data_published_time_contains (Union[Unset, datetime.datetime]):
        data_published_time_date (Union[Unset, datetime.date]):
        data_published_time_day (Union[Unset, float]):
        data_published_time_endswith (Union[Unset, datetime.datetime]):
        data_published_time_gt (Union[Unset, datetime.datetime]):
        data_published_time_gte (Union[Unset, datetime.datetime]):
        data_published_time_hour (Union[Unset, float]):
        data_published_time_icontains (Union[Unset, datetime.datetime]):
        data_published_time_iendswith (Union[Unset, datetime.datetime]):
        data_published_time_iexact (Union[Unset, datetime.datetime]):
        data_published_time_in (Union[Unset, list[datetime.datetime]]):
        data_published_time_iregex (Union[Unset, datetime.datetime]):
        data_published_time_isnull (Union[Unset, bool]):
        data_published_time_iso_week_day (Union[Unset, float]):
        data_published_time_iso_year (Union[Unset, float]):
        data_published_time_istartswith (Union[Unset, datetime.datetime]):
        data_published_time_lt (Union[Unset, datetime.datetime]):
        data_published_time_lte (Union[Unset, datetime.datetime]):
        data_published_time_minute (Union[Unset, float]):
        data_published_time_month (Union[Unset, float]):
        data_published_time_quarter (Union[Unset, float]):
        data_published_time_range (Union[Unset, list[datetime.datetime]]):
        data_published_time_regex (Union[Unset, datetime.datetime]):
        data_published_time_second (Union[Unset, float]):
        data_published_time_startswith (Union[Unset, datetime.datetime]):
        data_published_time_time (Union[Unset, str]):
        data_published_time_week (Union[Unset, float]):
        data_published_time_week_day (Union[Unset, float]):
        data_published_time_year (Union[Unset, float]):
        discovery_keywords_name (Union[Unset, str]):
        discovery_keywords_name_contains (Union[Unset, str]):
        doi_published_time (Union[Unset, datetime.datetime]):
        doi_published_time_contained_by (Union[Unset, datetime.datetime]):
        doi_published_time_contains (Union[Unset, datetime.datetime]):
        doi_published_time_date (Union[Unset, datetime.date]):
        doi_published_time_day (Union[Unset, float]):
        doi_published_time_endswith (Union[Unset, datetime.datetime]):
        doi_published_time_gt (Union[Unset, datetime.datetime]):
        doi_published_time_gte (Union[Unset, datetime.datetime]):
        doi_published_time_hour (Union[Unset, float]):
        doi_published_time_icontains (Union[Unset, datetime.datetime]):
        doi_published_time_iendswith (Union[Unset, datetime.datetime]):
        doi_published_time_iexact (Union[Unset, datetime.datetime]):
        doi_published_time_in (Union[Unset, list[datetime.datetime]]):
        doi_published_time_iregex (Union[Unset, datetime.datetime]):
        doi_published_time_isnull (Union[Unset, bool]):
        doi_published_time_iso_week_day (Union[Unset, float]):
        doi_published_time_iso_year (Union[Unset, float]):
        doi_published_time_istartswith (Union[Unset, datetime.datetime]):
        doi_published_time_lt (Union[Unset, datetime.datetime]):
        doi_published_time_lte (Union[Unset, datetime.datetime]):
        doi_published_time_minute (Union[Unset, float]):
        doi_published_time_month (Union[Unset, float]):
        doi_published_time_quarter (Union[Unset, float]):
        doi_published_time_range (Union[Unset, list[datetime.datetime]]):
        doi_published_time_regex (Union[Unset, datetime.datetime]):
        doi_published_time_second (Union[Unset, float]):
        doi_published_time_startswith (Union[Unset, datetime.datetime]):
        doi_published_time_time (Union[Unset, str]):
        doi_published_time_week (Union[Unset, float]):
        doi_published_time_week_day (Union[Unset, float]):
        doi_published_time_year (Union[Unset, float]):
        dont_harvest_from_projects (Union[Unset, bool]):
        dont_harvest_from_projects_contains (Union[Unset, bool]):
        dont_harvest_from_projects_endswith (Union[Unset, bool]):
        dont_harvest_from_projects_gt (Union[Unset, bool]):
        dont_harvest_from_projects_gte (Union[Unset, bool]):
        dont_harvest_from_projects_icontains (Union[Unset, bool]):
        dont_harvest_from_projects_iendswith (Union[Unset, bool]):
        dont_harvest_from_projects_iexact (Union[Unset, bool]):
        dont_harvest_from_projects_in (Union[Unset, list[bool]]):
        dont_harvest_from_projects_iregex (Union[Unset, bool]):
        dont_harvest_from_projects_isnull (Union[Unset, bool]):
        dont_harvest_from_projects_istartswith (Union[Unset, bool]):
        dont_harvest_from_projects_lt (Union[Unset, bool]):
        dont_harvest_from_projects_lte (Union[Unset, bool]):
        dont_harvest_from_projects_range (Union[Unset, list[bool]]):
        dont_harvest_from_projects_regex (Union[Unset, bool]):
        dont_harvest_from_projects_startswith (Union[Unset, bool]):
        keywords (Union[Unset, str]):
        keywords_contains (Union[Unset, str]):
        keywords_endswith (Union[Unset, str]):
        keywords_gt (Union[Unset, str]):
        keywords_gte (Union[Unset, str]):
        keywords_icontains (Union[Unset, str]):
        keywords_iendswith (Union[Unset, str]):
        keywords_iexact (Union[Unset, str]):
        keywords_in (Union[Unset, list[str]]):
        keywords_iregex (Union[Unset, str]):
        keywords_isnull (Union[Unset, bool]):
        keywords_istartswith (Union[Unset, str]):
        keywords_lt (Union[Unset, str]):
        keywords_lte (Union[Unset, str]):
        keywords_range (Union[Unset, list[str]]):
        keywords_regex (Union[Unset, str]):
        keywords_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        member_ob_id (Union[Unset, int]):
        member_ob_id_in (Union[Unset, list[int]]):
        member_uuid (Union[Unset, str]):
        member_uuid_in (Union[Unset, list[str]]):
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
        publication_state (Union[Unset, ObservationcollectionsListPublicationState]):
        publication_state_contains (Union[Unset, str]):
        publication_state_endswith (Union[Unset, str]):
        publication_state_gt (Union[Unset, str]):
        publication_state_gte (Union[Unset, str]):
        publication_state_icontains (Union[Unset, str]):
        publication_state_iendswith (Union[Unset, str]):
        publication_state_iexact (Union[Unset, str]):
        publication_state_in (Union[Unset, list[str]]):
        publication_state_iregex (Union[Unset, str]):
        publication_state_isnull (Union[Unset, bool]):
        publication_state_istartswith (Union[Unset, str]):
        publication_state_lt (Union[Unset, str]):
        publication_state_lte (Union[Unset, str]):
        publication_state_range (Union[Unset, list[str]]):
        publication_state_regex (Union[Unset, str]):
        publication_state_startswith (Union[Unset, str]):
        referenceable_ptr (Union[Unset, int]):
        referenceable_ptr_gt (Union[Unset, int]):
        referenceable_ptr_gte (Union[Unset, int]):
        referenceable_ptr_in (Union[Unset, list[int]]):
        referenceable_ptr_isnull (Union[Unset, bool]):
        referenceable_ptr_lt (Union[Unset, int]):
        referenceable_ptr_lte (Union[Unset, int]):
        short_code (Union[Unset, str]):
        short_code_contains (Union[Unset, str]):
        short_code_endswith (Union[Unset, str]):
        short_code_gt (Union[Unset, str]):
        short_code_gte (Union[Unset, str]):
        short_code_icontains (Union[Unset, str]):
        short_code_iendswith (Union[Unset, str]):
        short_code_iexact (Union[Unset, str]):
        short_code_in (Union[Unset, list[str]]):
        short_code_iregex (Union[Unset, str]):
        short_code_isnull (Union[Unset, bool]):
        short_code_istartswith (Union[Unset, str]):
        short_code_lt (Union[Unset, str]):
        short_code_lte (Union[Unset, str]):
        short_code_range (Union[Unset, list[str]]):
        short_code_regex (Union[Unset, str]):
        short_code_startswith (Union[Unset, str]):
        title (Union[Unset, str]):
        title_contains (Union[Unset, str]):
        title_endswith (Union[Unset, str]):
        title_gt (Union[Unset, str]):
        title_gte (Union[Unset, str]):
        title_icontains (Union[Unset, str]):
        title_iendswith (Union[Unset, str]):
        title_iexact (Union[Unset, str]):
        title_in (Union[Unset, list[str]]):
        title_iregex (Union[Unset, str]):
        title_isnull (Union[Unset, bool]):
        title_istartswith (Union[Unset, str]):
        title_lt (Union[Unset, str]):
        title_lte (Union[Unset, str]):
        title_range (Union[Unset, list[str]]):
        title_regex (Union[Unset, str]):
        title_startswith (Union[Unset, str]):
        uuid (Union[Unset, str]):
        uuid_contains (Union[Unset, str]):
        uuid_endswith (Union[Unset, str]):
        uuid_gt (Union[Unset, str]):
        uuid_gte (Union[Unset, str]):
        uuid_icontains (Union[Unset, str]):
        uuid_iendswith (Union[Unset, str]):
        uuid_iexact (Union[Unset, str]):
        uuid_in (Union[Unset, list[str]]):
        uuid_iregex (Union[Unset, str]):
        uuid_isnull (Union[Unset, bool]):
        uuid_istartswith (Union[Unset, str]):
        uuid_lt (Union[Unset, str]):
        uuid_lte (Union[Unset, str]):
        uuid_range (Union[Unset, list[str]]):
        uuid_regex (Union[Unset, str]):
        uuid_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedObservationCollectionReadList
    """

    return sync_detailed(
        client=client,
        abstract=abstract,
        abstract_contains=abstract_contains,
        abstract_endswith=abstract_endswith,
        abstract_gt=abstract_gt,
        abstract_gte=abstract_gte,
        abstract_icontains=abstract_icontains,
        abstract_iendswith=abstract_iendswith,
        abstract_iexact=abstract_iexact,
        abstract_in=abstract_in,
        abstract_iregex=abstract_iregex,
        abstract_isnull=abstract_isnull,
        abstract_istartswith=abstract_istartswith,
        abstract_lt=abstract_lt,
        abstract_lte=abstract_lte,
        abstract_range=abstract_range,
        abstract_regex=abstract_regex,
        abstract_startswith=abstract_startswith,
        data_published_time=data_published_time,
        data_published_time_contained_by=data_published_time_contained_by,
        data_published_time_contains=data_published_time_contains,
        data_published_time_date=data_published_time_date,
        data_published_time_day=data_published_time_day,
        data_published_time_endswith=data_published_time_endswith,
        data_published_time_gt=data_published_time_gt,
        data_published_time_gte=data_published_time_gte,
        data_published_time_hour=data_published_time_hour,
        data_published_time_icontains=data_published_time_icontains,
        data_published_time_iendswith=data_published_time_iendswith,
        data_published_time_iexact=data_published_time_iexact,
        data_published_time_in=data_published_time_in,
        data_published_time_iregex=data_published_time_iregex,
        data_published_time_isnull=data_published_time_isnull,
        data_published_time_iso_week_day=data_published_time_iso_week_day,
        data_published_time_iso_year=data_published_time_iso_year,
        data_published_time_istartswith=data_published_time_istartswith,
        data_published_time_lt=data_published_time_lt,
        data_published_time_lte=data_published_time_lte,
        data_published_time_minute=data_published_time_minute,
        data_published_time_month=data_published_time_month,
        data_published_time_quarter=data_published_time_quarter,
        data_published_time_range=data_published_time_range,
        data_published_time_regex=data_published_time_regex,
        data_published_time_second=data_published_time_second,
        data_published_time_startswith=data_published_time_startswith,
        data_published_time_time=data_published_time_time,
        data_published_time_week=data_published_time_week,
        data_published_time_week_day=data_published_time_week_day,
        data_published_time_year=data_published_time_year,
        discovery_keywords_name=discovery_keywords_name,
        discovery_keywords_name_contains=discovery_keywords_name_contains,
        doi_published_time=doi_published_time,
        doi_published_time_contained_by=doi_published_time_contained_by,
        doi_published_time_contains=doi_published_time_contains,
        doi_published_time_date=doi_published_time_date,
        doi_published_time_day=doi_published_time_day,
        doi_published_time_endswith=doi_published_time_endswith,
        doi_published_time_gt=doi_published_time_gt,
        doi_published_time_gte=doi_published_time_gte,
        doi_published_time_hour=doi_published_time_hour,
        doi_published_time_icontains=doi_published_time_icontains,
        doi_published_time_iendswith=doi_published_time_iendswith,
        doi_published_time_iexact=doi_published_time_iexact,
        doi_published_time_in=doi_published_time_in,
        doi_published_time_iregex=doi_published_time_iregex,
        doi_published_time_isnull=doi_published_time_isnull,
        doi_published_time_iso_week_day=doi_published_time_iso_week_day,
        doi_published_time_iso_year=doi_published_time_iso_year,
        doi_published_time_istartswith=doi_published_time_istartswith,
        doi_published_time_lt=doi_published_time_lt,
        doi_published_time_lte=doi_published_time_lte,
        doi_published_time_minute=doi_published_time_minute,
        doi_published_time_month=doi_published_time_month,
        doi_published_time_quarter=doi_published_time_quarter,
        doi_published_time_range=doi_published_time_range,
        doi_published_time_regex=doi_published_time_regex,
        doi_published_time_second=doi_published_time_second,
        doi_published_time_startswith=doi_published_time_startswith,
        doi_published_time_time=doi_published_time_time,
        doi_published_time_week=doi_published_time_week,
        doi_published_time_week_day=doi_published_time_week_day,
        doi_published_time_year=doi_published_time_year,
        dont_harvest_from_projects=dont_harvest_from_projects,
        dont_harvest_from_projects_contains=dont_harvest_from_projects_contains,
        dont_harvest_from_projects_endswith=dont_harvest_from_projects_endswith,
        dont_harvest_from_projects_gt=dont_harvest_from_projects_gt,
        dont_harvest_from_projects_gte=dont_harvest_from_projects_gte,
        dont_harvest_from_projects_icontains=dont_harvest_from_projects_icontains,
        dont_harvest_from_projects_iendswith=dont_harvest_from_projects_iendswith,
        dont_harvest_from_projects_iexact=dont_harvest_from_projects_iexact,
        dont_harvest_from_projects_in=dont_harvest_from_projects_in,
        dont_harvest_from_projects_iregex=dont_harvest_from_projects_iregex,
        dont_harvest_from_projects_isnull=dont_harvest_from_projects_isnull,
        dont_harvest_from_projects_istartswith=dont_harvest_from_projects_istartswith,
        dont_harvest_from_projects_lt=dont_harvest_from_projects_lt,
        dont_harvest_from_projects_lte=dont_harvest_from_projects_lte,
        dont_harvest_from_projects_range=dont_harvest_from_projects_range,
        dont_harvest_from_projects_regex=dont_harvest_from_projects_regex,
        dont_harvest_from_projects_startswith=dont_harvest_from_projects_startswith,
        keywords=keywords,
        keywords_contains=keywords_contains,
        keywords_endswith=keywords_endswith,
        keywords_gt=keywords_gt,
        keywords_gte=keywords_gte,
        keywords_icontains=keywords_icontains,
        keywords_iendswith=keywords_iendswith,
        keywords_iexact=keywords_iexact,
        keywords_in=keywords_in,
        keywords_iregex=keywords_iregex,
        keywords_isnull=keywords_isnull,
        keywords_istartswith=keywords_istartswith,
        keywords_lt=keywords_lt,
        keywords_lte=keywords_lte,
        keywords_range=keywords_range,
        keywords_regex=keywords_regex,
        keywords_startswith=keywords_startswith,
        limit=limit,
        member_ob_id=member_ob_id,
        member_ob_id_in=member_ob_id_in,
        member_uuid=member_uuid,
        member_uuid_in=member_uuid_in,
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
        publication_state=publication_state,
        publication_state_contains=publication_state_contains,
        publication_state_endswith=publication_state_endswith,
        publication_state_gt=publication_state_gt,
        publication_state_gte=publication_state_gte,
        publication_state_icontains=publication_state_icontains,
        publication_state_iendswith=publication_state_iendswith,
        publication_state_iexact=publication_state_iexact,
        publication_state_in=publication_state_in,
        publication_state_iregex=publication_state_iregex,
        publication_state_isnull=publication_state_isnull,
        publication_state_istartswith=publication_state_istartswith,
        publication_state_lt=publication_state_lt,
        publication_state_lte=publication_state_lte,
        publication_state_range=publication_state_range,
        publication_state_regex=publication_state_regex,
        publication_state_startswith=publication_state_startswith,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_gt=referenceable_ptr_gt,
        referenceable_ptr_gte=referenceable_ptr_gte,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        referenceable_ptr_lt=referenceable_ptr_lt,
        referenceable_ptr_lte=referenceable_ptr_lte,
        short_code=short_code,
        short_code_contains=short_code_contains,
        short_code_endswith=short_code_endswith,
        short_code_gt=short_code_gt,
        short_code_gte=short_code_gte,
        short_code_icontains=short_code_icontains,
        short_code_iendswith=short_code_iendswith,
        short_code_iexact=short_code_iexact,
        short_code_in=short_code_in,
        short_code_iregex=short_code_iregex,
        short_code_isnull=short_code_isnull,
        short_code_istartswith=short_code_istartswith,
        short_code_lt=short_code_lt,
        short_code_lte=short_code_lte,
        short_code_range=short_code_range,
        short_code_regex=short_code_regex,
        short_code_startswith=short_code_startswith,
        title=title,
        title_contains=title_contains,
        title_endswith=title_endswith,
        title_gt=title_gt,
        title_gte=title_gte,
        title_icontains=title_icontains,
        title_iendswith=title_iendswith,
        title_iexact=title_iexact,
        title_in=title_in,
        title_iregex=title_iregex,
        title_isnull=title_isnull,
        title_istartswith=title_istartswith,
        title_lt=title_lt,
        title_lte=title_lte,
        title_range=title_range,
        title_regex=title_regex,
        title_startswith=title_startswith,
        uuid=uuid,
        uuid_contains=uuid_contains,
        uuid_endswith=uuid_endswith,
        uuid_gt=uuid_gt,
        uuid_gte=uuid_gte,
        uuid_icontains=uuid_icontains,
        uuid_iendswith=uuid_iendswith,
        uuid_iexact=uuid_iexact,
        uuid_in=uuid_in,
        uuid_iregex=uuid_iregex,
        uuid_isnull=uuid_isnull,
        uuid_istartswith=uuid_istartswith,
        uuid_lt=uuid_lt,
        uuid_lte=uuid_lte,
        uuid_range=uuid_range,
        uuid_regex=uuid_regex,
        uuid_startswith=uuid_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    abstract: Union[Unset, str] = UNSET,
    abstract_contains: Union[Unset, str] = UNSET,
    abstract_endswith: Union[Unset, str] = UNSET,
    abstract_gt: Union[Unset, str] = UNSET,
    abstract_gte: Union[Unset, str] = UNSET,
    abstract_icontains: Union[Unset, str] = UNSET,
    abstract_iendswith: Union[Unset, str] = UNSET,
    abstract_iexact: Union[Unset, str] = UNSET,
    abstract_in: Union[Unset, list[str]] = UNSET,
    abstract_iregex: Union[Unset, str] = UNSET,
    abstract_isnull: Union[Unset, bool] = UNSET,
    abstract_istartswith: Union[Unset, str] = UNSET,
    abstract_lt: Union[Unset, str] = UNSET,
    abstract_lte: Union[Unset, str] = UNSET,
    abstract_range: Union[Unset, list[str]] = UNSET,
    abstract_regex: Union[Unset, str] = UNSET,
    abstract_startswith: Union[Unset, str] = UNSET,
    data_published_time: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_contains: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_date: Union[Unset, datetime.date] = UNSET,
    data_published_time_day: Union[Unset, float] = UNSET,
    data_published_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_gt: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_gte: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_hour: Union[Unset, float] = UNSET,
    data_published_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    data_published_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_isnull: Union[Unset, bool] = UNSET,
    data_published_time_iso_week_day: Union[Unset, float] = UNSET,
    data_published_time_iso_year: Union[Unset, float] = UNSET,
    data_published_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_lt: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_lte: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_minute: Union[Unset, float] = UNSET,
    data_published_time_month: Union[Unset, float] = UNSET,
    data_published_time_quarter: Union[Unset, float] = UNSET,
    data_published_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    data_published_time_regex: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_second: Union[Unset, float] = UNSET,
    data_published_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_time: Union[Unset, str] = UNSET,
    data_published_time_week: Union[Unset, float] = UNSET,
    data_published_time_week_day: Union[Unset, float] = UNSET,
    data_published_time_year: Union[Unset, float] = UNSET,
    discovery_keywords_name: Union[Unset, str] = UNSET,
    discovery_keywords_name_contains: Union[Unset, str] = UNSET,
    doi_published_time: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_contains: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_date: Union[Unset, datetime.date] = UNSET,
    doi_published_time_day: Union[Unset, float] = UNSET,
    doi_published_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_gt: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_gte: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_hour: Union[Unset, float] = UNSET,
    doi_published_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    doi_published_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_isnull: Union[Unset, bool] = UNSET,
    doi_published_time_iso_week_day: Union[Unset, float] = UNSET,
    doi_published_time_iso_year: Union[Unset, float] = UNSET,
    doi_published_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_lt: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_lte: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_minute: Union[Unset, float] = UNSET,
    doi_published_time_month: Union[Unset, float] = UNSET,
    doi_published_time_quarter: Union[Unset, float] = UNSET,
    doi_published_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    doi_published_time_regex: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_second: Union[Unset, float] = UNSET,
    doi_published_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_time: Union[Unset, str] = UNSET,
    doi_published_time_week: Union[Unset, float] = UNSET,
    doi_published_time_week_day: Union[Unset, float] = UNSET,
    doi_published_time_year: Union[Unset, float] = UNSET,
    dont_harvest_from_projects: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_contains: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_endswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_gt: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_gte: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_icontains: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_iendswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_iexact: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_in: Union[Unset, list[bool]] = UNSET,
    dont_harvest_from_projects_iregex: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_isnull: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_istartswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_lt: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_lte: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_range: Union[Unset, list[bool]] = UNSET,
    dont_harvest_from_projects_regex: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_startswith: Union[Unset, bool] = UNSET,
    keywords: Union[Unset, str] = UNSET,
    keywords_contains: Union[Unset, str] = UNSET,
    keywords_endswith: Union[Unset, str] = UNSET,
    keywords_gt: Union[Unset, str] = UNSET,
    keywords_gte: Union[Unset, str] = UNSET,
    keywords_icontains: Union[Unset, str] = UNSET,
    keywords_iendswith: Union[Unset, str] = UNSET,
    keywords_iexact: Union[Unset, str] = UNSET,
    keywords_in: Union[Unset, list[str]] = UNSET,
    keywords_iregex: Union[Unset, str] = UNSET,
    keywords_isnull: Union[Unset, bool] = UNSET,
    keywords_istartswith: Union[Unset, str] = UNSET,
    keywords_lt: Union[Unset, str] = UNSET,
    keywords_lte: Union[Unset, str] = UNSET,
    keywords_range: Union[Unset, list[str]] = UNSET,
    keywords_regex: Union[Unset, str] = UNSET,
    keywords_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    member_ob_id: Union[Unset, int] = UNSET,
    member_ob_id_in: Union[Unset, list[int]] = UNSET,
    member_uuid: Union[Unset, str] = UNSET,
    member_uuid_in: Union[Unset, list[str]] = UNSET,
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
    publication_state: Union[Unset, ObservationcollectionsListPublicationState] = UNSET,
    publication_state_contains: Union[Unset, str] = UNSET,
    publication_state_endswith: Union[Unset, str] = UNSET,
    publication_state_gt: Union[Unset, str] = UNSET,
    publication_state_gte: Union[Unset, str] = UNSET,
    publication_state_icontains: Union[Unset, str] = UNSET,
    publication_state_iendswith: Union[Unset, str] = UNSET,
    publication_state_iexact: Union[Unset, str] = UNSET,
    publication_state_in: Union[Unset, list[str]] = UNSET,
    publication_state_iregex: Union[Unset, str] = UNSET,
    publication_state_isnull: Union[Unset, bool] = UNSET,
    publication_state_istartswith: Union[Unset, str] = UNSET,
    publication_state_lt: Union[Unset, str] = UNSET,
    publication_state_lte: Union[Unset, str] = UNSET,
    publication_state_range: Union[Unset, list[str]] = UNSET,
    publication_state_regex: Union[Unset, str] = UNSET,
    publication_state_startswith: Union[Unset, str] = UNSET,
    referenceable_ptr: Union[Unset, int] = UNSET,
    referenceable_ptr_gt: Union[Unset, int] = UNSET,
    referenceable_ptr_gte: Union[Unset, int] = UNSET,
    referenceable_ptr_in: Union[Unset, list[int]] = UNSET,
    referenceable_ptr_isnull: Union[Unset, bool] = UNSET,
    referenceable_ptr_lt: Union[Unset, int] = UNSET,
    referenceable_ptr_lte: Union[Unset, int] = UNSET,
    short_code: Union[Unset, str] = UNSET,
    short_code_contains: Union[Unset, str] = UNSET,
    short_code_endswith: Union[Unset, str] = UNSET,
    short_code_gt: Union[Unset, str] = UNSET,
    short_code_gte: Union[Unset, str] = UNSET,
    short_code_icontains: Union[Unset, str] = UNSET,
    short_code_iendswith: Union[Unset, str] = UNSET,
    short_code_iexact: Union[Unset, str] = UNSET,
    short_code_in: Union[Unset, list[str]] = UNSET,
    short_code_iregex: Union[Unset, str] = UNSET,
    short_code_isnull: Union[Unset, bool] = UNSET,
    short_code_istartswith: Union[Unset, str] = UNSET,
    short_code_lt: Union[Unset, str] = UNSET,
    short_code_lte: Union[Unset, str] = UNSET,
    short_code_range: Union[Unset, list[str]] = UNSET,
    short_code_regex: Union[Unset, str] = UNSET,
    short_code_startswith: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    title_contains: Union[Unset, str] = UNSET,
    title_endswith: Union[Unset, str] = UNSET,
    title_gt: Union[Unset, str] = UNSET,
    title_gte: Union[Unset, str] = UNSET,
    title_icontains: Union[Unset, str] = UNSET,
    title_iendswith: Union[Unset, str] = UNSET,
    title_iexact: Union[Unset, str] = UNSET,
    title_in: Union[Unset, list[str]] = UNSET,
    title_iregex: Union[Unset, str] = UNSET,
    title_isnull: Union[Unset, bool] = UNSET,
    title_istartswith: Union[Unset, str] = UNSET,
    title_lt: Union[Unset, str] = UNSET,
    title_lte: Union[Unset, str] = UNSET,
    title_range: Union[Unset, list[str]] = UNSET,
    title_regex: Union[Unset, str] = UNSET,
    title_startswith: Union[Unset, str] = UNSET,
    uuid: Union[Unset, str] = UNSET,
    uuid_contains: Union[Unset, str] = UNSET,
    uuid_endswith: Union[Unset, str] = UNSET,
    uuid_gt: Union[Unset, str] = UNSET,
    uuid_gte: Union[Unset, str] = UNSET,
    uuid_icontains: Union[Unset, str] = UNSET,
    uuid_iendswith: Union[Unset, str] = UNSET,
    uuid_iexact: Union[Unset, str] = UNSET,
    uuid_in: Union[Unset, list[str]] = UNSET,
    uuid_iregex: Union[Unset, str] = UNSET,
    uuid_isnull: Union[Unset, bool] = UNSET,
    uuid_istartswith: Union[Unset, str] = UNSET,
    uuid_lt: Union[Unset, str] = UNSET,
    uuid_lte: Union[Unset, str] = UNSET,
    uuid_range: Union[Unset, list[str]] = UNSET,
    uuid_regex: Union[Unset, str] = UNSET,
    uuid_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedObservationCollectionReadList]:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        abstract (Union[Unset, str]):
        abstract_contains (Union[Unset, str]):
        abstract_endswith (Union[Unset, str]):
        abstract_gt (Union[Unset, str]):
        abstract_gte (Union[Unset, str]):
        abstract_icontains (Union[Unset, str]):
        abstract_iendswith (Union[Unset, str]):
        abstract_iexact (Union[Unset, str]):
        abstract_in (Union[Unset, list[str]]):
        abstract_iregex (Union[Unset, str]):
        abstract_isnull (Union[Unset, bool]):
        abstract_istartswith (Union[Unset, str]):
        abstract_lt (Union[Unset, str]):
        abstract_lte (Union[Unset, str]):
        abstract_range (Union[Unset, list[str]]):
        abstract_regex (Union[Unset, str]):
        abstract_startswith (Union[Unset, str]):
        data_published_time (Union[Unset, datetime.datetime]):
        data_published_time_contained_by (Union[Unset, datetime.datetime]):
        data_published_time_contains (Union[Unset, datetime.datetime]):
        data_published_time_date (Union[Unset, datetime.date]):
        data_published_time_day (Union[Unset, float]):
        data_published_time_endswith (Union[Unset, datetime.datetime]):
        data_published_time_gt (Union[Unset, datetime.datetime]):
        data_published_time_gte (Union[Unset, datetime.datetime]):
        data_published_time_hour (Union[Unset, float]):
        data_published_time_icontains (Union[Unset, datetime.datetime]):
        data_published_time_iendswith (Union[Unset, datetime.datetime]):
        data_published_time_iexact (Union[Unset, datetime.datetime]):
        data_published_time_in (Union[Unset, list[datetime.datetime]]):
        data_published_time_iregex (Union[Unset, datetime.datetime]):
        data_published_time_isnull (Union[Unset, bool]):
        data_published_time_iso_week_day (Union[Unset, float]):
        data_published_time_iso_year (Union[Unset, float]):
        data_published_time_istartswith (Union[Unset, datetime.datetime]):
        data_published_time_lt (Union[Unset, datetime.datetime]):
        data_published_time_lte (Union[Unset, datetime.datetime]):
        data_published_time_minute (Union[Unset, float]):
        data_published_time_month (Union[Unset, float]):
        data_published_time_quarter (Union[Unset, float]):
        data_published_time_range (Union[Unset, list[datetime.datetime]]):
        data_published_time_regex (Union[Unset, datetime.datetime]):
        data_published_time_second (Union[Unset, float]):
        data_published_time_startswith (Union[Unset, datetime.datetime]):
        data_published_time_time (Union[Unset, str]):
        data_published_time_week (Union[Unset, float]):
        data_published_time_week_day (Union[Unset, float]):
        data_published_time_year (Union[Unset, float]):
        discovery_keywords_name (Union[Unset, str]):
        discovery_keywords_name_contains (Union[Unset, str]):
        doi_published_time (Union[Unset, datetime.datetime]):
        doi_published_time_contained_by (Union[Unset, datetime.datetime]):
        doi_published_time_contains (Union[Unset, datetime.datetime]):
        doi_published_time_date (Union[Unset, datetime.date]):
        doi_published_time_day (Union[Unset, float]):
        doi_published_time_endswith (Union[Unset, datetime.datetime]):
        doi_published_time_gt (Union[Unset, datetime.datetime]):
        doi_published_time_gte (Union[Unset, datetime.datetime]):
        doi_published_time_hour (Union[Unset, float]):
        doi_published_time_icontains (Union[Unset, datetime.datetime]):
        doi_published_time_iendswith (Union[Unset, datetime.datetime]):
        doi_published_time_iexact (Union[Unset, datetime.datetime]):
        doi_published_time_in (Union[Unset, list[datetime.datetime]]):
        doi_published_time_iregex (Union[Unset, datetime.datetime]):
        doi_published_time_isnull (Union[Unset, bool]):
        doi_published_time_iso_week_day (Union[Unset, float]):
        doi_published_time_iso_year (Union[Unset, float]):
        doi_published_time_istartswith (Union[Unset, datetime.datetime]):
        doi_published_time_lt (Union[Unset, datetime.datetime]):
        doi_published_time_lte (Union[Unset, datetime.datetime]):
        doi_published_time_minute (Union[Unset, float]):
        doi_published_time_month (Union[Unset, float]):
        doi_published_time_quarter (Union[Unset, float]):
        doi_published_time_range (Union[Unset, list[datetime.datetime]]):
        doi_published_time_regex (Union[Unset, datetime.datetime]):
        doi_published_time_second (Union[Unset, float]):
        doi_published_time_startswith (Union[Unset, datetime.datetime]):
        doi_published_time_time (Union[Unset, str]):
        doi_published_time_week (Union[Unset, float]):
        doi_published_time_week_day (Union[Unset, float]):
        doi_published_time_year (Union[Unset, float]):
        dont_harvest_from_projects (Union[Unset, bool]):
        dont_harvest_from_projects_contains (Union[Unset, bool]):
        dont_harvest_from_projects_endswith (Union[Unset, bool]):
        dont_harvest_from_projects_gt (Union[Unset, bool]):
        dont_harvest_from_projects_gte (Union[Unset, bool]):
        dont_harvest_from_projects_icontains (Union[Unset, bool]):
        dont_harvest_from_projects_iendswith (Union[Unset, bool]):
        dont_harvest_from_projects_iexact (Union[Unset, bool]):
        dont_harvest_from_projects_in (Union[Unset, list[bool]]):
        dont_harvest_from_projects_iregex (Union[Unset, bool]):
        dont_harvest_from_projects_isnull (Union[Unset, bool]):
        dont_harvest_from_projects_istartswith (Union[Unset, bool]):
        dont_harvest_from_projects_lt (Union[Unset, bool]):
        dont_harvest_from_projects_lte (Union[Unset, bool]):
        dont_harvest_from_projects_range (Union[Unset, list[bool]]):
        dont_harvest_from_projects_regex (Union[Unset, bool]):
        dont_harvest_from_projects_startswith (Union[Unset, bool]):
        keywords (Union[Unset, str]):
        keywords_contains (Union[Unset, str]):
        keywords_endswith (Union[Unset, str]):
        keywords_gt (Union[Unset, str]):
        keywords_gte (Union[Unset, str]):
        keywords_icontains (Union[Unset, str]):
        keywords_iendswith (Union[Unset, str]):
        keywords_iexact (Union[Unset, str]):
        keywords_in (Union[Unset, list[str]]):
        keywords_iregex (Union[Unset, str]):
        keywords_isnull (Union[Unset, bool]):
        keywords_istartswith (Union[Unset, str]):
        keywords_lt (Union[Unset, str]):
        keywords_lte (Union[Unset, str]):
        keywords_range (Union[Unset, list[str]]):
        keywords_regex (Union[Unset, str]):
        keywords_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        member_ob_id (Union[Unset, int]):
        member_ob_id_in (Union[Unset, list[int]]):
        member_uuid (Union[Unset, str]):
        member_uuid_in (Union[Unset, list[str]]):
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
        publication_state (Union[Unset, ObservationcollectionsListPublicationState]):
        publication_state_contains (Union[Unset, str]):
        publication_state_endswith (Union[Unset, str]):
        publication_state_gt (Union[Unset, str]):
        publication_state_gte (Union[Unset, str]):
        publication_state_icontains (Union[Unset, str]):
        publication_state_iendswith (Union[Unset, str]):
        publication_state_iexact (Union[Unset, str]):
        publication_state_in (Union[Unset, list[str]]):
        publication_state_iregex (Union[Unset, str]):
        publication_state_isnull (Union[Unset, bool]):
        publication_state_istartswith (Union[Unset, str]):
        publication_state_lt (Union[Unset, str]):
        publication_state_lte (Union[Unset, str]):
        publication_state_range (Union[Unset, list[str]]):
        publication_state_regex (Union[Unset, str]):
        publication_state_startswith (Union[Unset, str]):
        referenceable_ptr (Union[Unset, int]):
        referenceable_ptr_gt (Union[Unset, int]):
        referenceable_ptr_gte (Union[Unset, int]):
        referenceable_ptr_in (Union[Unset, list[int]]):
        referenceable_ptr_isnull (Union[Unset, bool]):
        referenceable_ptr_lt (Union[Unset, int]):
        referenceable_ptr_lte (Union[Unset, int]):
        short_code (Union[Unset, str]):
        short_code_contains (Union[Unset, str]):
        short_code_endswith (Union[Unset, str]):
        short_code_gt (Union[Unset, str]):
        short_code_gte (Union[Unset, str]):
        short_code_icontains (Union[Unset, str]):
        short_code_iendswith (Union[Unset, str]):
        short_code_iexact (Union[Unset, str]):
        short_code_in (Union[Unset, list[str]]):
        short_code_iregex (Union[Unset, str]):
        short_code_isnull (Union[Unset, bool]):
        short_code_istartswith (Union[Unset, str]):
        short_code_lt (Union[Unset, str]):
        short_code_lte (Union[Unset, str]):
        short_code_range (Union[Unset, list[str]]):
        short_code_regex (Union[Unset, str]):
        short_code_startswith (Union[Unset, str]):
        title (Union[Unset, str]):
        title_contains (Union[Unset, str]):
        title_endswith (Union[Unset, str]):
        title_gt (Union[Unset, str]):
        title_gte (Union[Unset, str]):
        title_icontains (Union[Unset, str]):
        title_iendswith (Union[Unset, str]):
        title_iexact (Union[Unset, str]):
        title_in (Union[Unset, list[str]]):
        title_iregex (Union[Unset, str]):
        title_isnull (Union[Unset, bool]):
        title_istartswith (Union[Unset, str]):
        title_lt (Union[Unset, str]):
        title_lte (Union[Unset, str]):
        title_range (Union[Unset, list[str]]):
        title_regex (Union[Unset, str]):
        title_startswith (Union[Unset, str]):
        uuid (Union[Unset, str]):
        uuid_contains (Union[Unset, str]):
        uuid_endswith (Union[Unset, str]):
        uuid_gt (Union[Unset, str]):
        uuid_gte (Union[Unset, str]):
        uuid_icontains (Union[Unset, str]):
        uuid_iendswith (Union[Unset, str]):
        uuid_iexact (Union[Unset, str]):
        uuid_in (Union[Unset, list[str]]):
        uuid_iregex (Union[Unset, str]):
        uuid_isnull (Union[Unset, bool]):
        uuid_istartswith (Union[Unset, str]):
        uuid_lt (Union[Unset, str]):
        uuid_lte (Union[Unset, str]):
        uuid_range (Union[Unset, list[str]]):
        uuid_regex (Union[Unset, str]):
        uuid_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedObservationCollectionReadList]
    """

    kwargs = _get_kwargs(
        abstract=abstract,
        abstract_contains=abstract_contains,
        abstract_endswith=abstract_endswith,
        abstract_gt=abstract_gt,
        abstract_gte=abstract_gte,
        abstract_icontains=abstract_icontains,
        abstract_iendswith=abstract_iendswith,
        abstract_iexact=abstract_iexact,
        abstract_in=abstract_in,
        abstract_iregex=abstract_iregex,
        abstract_isnull=abstract_isnull,
        abstract_istartswith=abstract_istartswith,
        abstract_lt=abstract_lt,
        abstract_lte=abstract_lte,
        abstract_range=abstract_range,
        abstract_regex=abstract_regex,
        abstract_startswith=abstract_startswith,
        data_published_time=data_published_time,
        data_published_time_contained_by=data_published_time_contained_by,
        data_published_time_contains=data_published_time_contains,
        data_published_time_date=data_published_time_date,
        data_published_time_day=data_published_time_day,
        data_published_time_endswith=data_published_time_endswith,
        data_published_time_gt=data_published_time_gt,
        data_published_time_gte=data_published_time_gte,
        data_published_time_hour=data_published_time_hour,
        data_published_time_icontains=data_published_time_icontains,
        data_published_time_iendswith=data_published_time_iendswith,
        data_published_time_iexact=data_published_time_iexact,
        data_published_time_in=data_published_time_in,
        data_published_time_iregex=data_published_time_iregex,
        data_published_time_isnull=data_published_time_isnull,
        data_published_time_iso_week_day=data_published_time_iso_week_day,
        data_published_time_iso_year=data_published_time_iso_year,
        data_published_time_istartswith=data_published_time_istartswith,
        data_published_time_lt=data_published_time_lt,
        data_published_time_lte=data_published_time_lte,
        data_published_time_minute=data_published_time_minute,
        data_published_time_month=data_published_time_month,
        data_published_time_quarter=data_published_time_quarter,
        data_published_time_range=data_published_time_range,
        data_published_time_regex=data_published_time_regex,
        data_published_time_second=data_published_time_second,
        data_published_time_startswith=data_published_time_startswith,
        data_published_time_time=data_published_time_time,
        data_published_time_week=data_published_time_week,
        data_published_time_week_day=data_published_time_week_day,
        data_published_time_year=data_published_time_year,
        discovery_keywords_name=discovery_keywords_name,
        discovery_keywords_name_contains=discovery_keywords_name_contains,
        doi_published_time=doi_published_time,
        doi_published_time_contained_by=doi_published_time_contained_by,
        doi_published_time_contains=doi_published_time_contains,
        doi_published_time_date=doi_published_time_date,
        doi_published_time_day=doi_published_time_day,
        doi_published_time_endswith=doi_published_time_endswith,
        doi_published_time_gt=doi_published_time_gt,
        doi_published_time_gte=doi_published_time_gte,
        doi_published_time_hour=doi_published_time_hour,
        doi_published_time_icontains=doi_published_time_icontains,
        doi_published_time_iendswith=doi_published_time_iendswith,
        doi_published_time_iexact=doi_published_time_iexact,
        doi_published_time_in=doi_published_time_in,
        doi_published_time_iregex=doi_published_time_iregex,
        doi_published_time_isnull=doi_published_time_isnull,
        doi_published_time_iso_week_day=doi_published_time_iso_week_day,
        doi_published_time_iso_year=doi_published_time_iso_year,
        doi_published_time_istartswith=doi_published_time_istartswith,
        doi_published_time_lt=doi_published_time_lt,
        doi_published_time_lte=doi_published_time_lte,
        doi_published_time_minute=doi_published_time_minute,
        doi_published_time_month=doi_published_time_month,
        doi_published_time_quarter=doi_published_time_quarter,
        doi_published_time_range=doi_published_time_range,
        doi_published_time_regex=doi_published_time_regex,
        doi_published_time_second=doi_published_time_second,
        doi_published_time_startswith=doi_published_time_startswith,
        doi_published_time_time=doi_published_time_time,
        doi_published_time_week=doi_published_time_week,
        doi_published_time_week_day=doi_published_time_week_day,
        doi_published_time_year=doi_published_time_year,
        dont_harvest_from_projects=dont_harvest_from_projects,
        dont_harvest_from_projects_contains=dont_harvest_from_projects_contains,
        dont_harvest_from_projects_endswith=dont_harvest_from_projects_endswith,
        dont_harvest_from_projects_gt=dont_harvest_from_projects_gt,
        dont_harvest_from_projects_gte=dont_harvest_from_projects_gte,
        dont_harvest_from_projects_icontains=dont_harvest_from_projects_icontains,
        dont_harvest_from_projects_iendswith=dont_harvest_from_projects_iendswith,
        dont_harvest_from_projects_iexact=dont_harvest_from_projects_iexact,
        dont_harvest_from_projects_in=dont_harvest_from_projects_in,
        dont_harvest_from_projects_iregex=dont_harvest_from_projects_iregex,
        dont_harvest_from_projects_isnull=dont_harvest_from_projects_isnull,
        dont_harvest_from_projects_istartswith=dont_harvest_from_projects_istartswith,
        dont_harvest_from_projects_lt=dont_harvest_from_projects_lt,
        dont_harvest_from_projects_lte=dont_harvest_from_projects_lte,
        dont_harvest_from_projects_range=dont_harvest_from_projects_range,
        dont_harvest_from_projects_regex=dont_harvest_from_projects_regex,
        dont_harvest_from_projects_startswith=dont_harvest_from_projects_startswith,
        keywords=keywords,
        keywords_contains=keywords_contains,
        keywords_endswith=keywords_endswith,
        keywords_gt=keywords_gt,
        keywords_gte=keywords_gte,
        keywords_icontains=keywords_icontains,
        keywords_iendswith=keywords_iendswith,
        keywords_iexact=keywords_iexact,
        keywords_in=keywords_in,
        keywords_iregex=keywords_iregex,
        keywords_isnull=keywords_isnull,
        keywords_istartswith=keywords_istartswith,
        keywords_lt=keywords_lt,
        keywords_lte=keywords_lte,
        keywords_range=keywords_range,
        keywords_regex=keywords_regex,
        keywords_startswith=keywords_startswith,
        limit=limit,
        member_ob_id=member_ob_id,
        member_ob_id_in=member_ob_id_in,
        member_uuid=member_uuid,
        member_uuid_in=member_uuid_in,
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
        publication_state=publication_state,
        publication_state_contains=publication_state_contains,
        publication_state_endswith=publication_state_endswith,
        publication_state_gt=publication_state_gt,
        publication_state_gte=publication_state_gte,
        publication_state_icontains=publication_state_icontains,
        publication_state_iendswith=publication_state_iendswith,
        publication_state_iexact=publication_state_iexact,
        publication_state_in=publication_state_in,
        publication_state_iregex=publication_state_iregex,
        publication_state_isnull=publication_state_isnull,
        publication_state_istartswith=publication_state_istartswith,
        publication_state_lt=publication_state_lt,
        publication_state_lte=publication_state_lte,
        publication_state_range=publication_state_range,
        publication_state_regex=publication_state_regex,
        publication_state_startswith=publication_state_startswith,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_gt=referenceable_ptr_gt,
        referenceable_ptr_gte=referenceable_ptr_gte,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        referenceable_ptr_lt=referenceable_ptr_lt,
        referenceable_ptr_lte=referenceable_ptr_lte,
        short_code=short_code,
        short_code_contains=short_code_contains,
        short_code_endswith=short_code_endswith,
        short_code_gt=short_code_gt,
        short_code_gte=short_code_gte,
        short_code_icontains=short_code_icontains,
        short_code_iendswith=short_code_iendswith,
        short_code_iexact=short_code_iexact,
        short_code_in=short_code_in,
        short_code_iregex=short_code_iregex,
        short_code_isnull=short_code_isnull,
        short_code_istartswith=short_code_istartswith,
        short_code_lt=short_code_lt,
        short_code_lte=short_code_lte,
        short_code_range=short_code_range,
        short_code_regex=short_code_regex,
        short_code_startswith=short_code_startswith,
        title=title,
        title_contains=title_contains,
        title_endswith=title_endswith,
        title_gt=title_gt,
        title_gte=title_gte,
        title_icontains=title_icontains,
        title_iendswith=title_iendswith,
        title_iexact=title_iexact,
        title_in=title_in,
        title_iregex=title_iregex,
        title_isnull=title_isnull,
        title_istartswith=title_istartswith,
        title_lt=title_lt,
        title_lte=title_lte,
        title_range=title_range,
        title_regex=title_regex,
        title_startswith=title_startswith,
        uuid=uuid,
        uuid_contains=uuid_contains,
        uuid_endswith=uuid_endswith,
        uuid_gt=uuid_gt,
        uuid_gte=uuid_gte,
        uuid_icontains=uuid_icontains,
        uuid_iendswith=uuid_iendswith,
        uuid_iexact=uuid_iexact,
        uuid_in=uuid_in,
        uuid_iregex=uuid_iregex,
        uuid_isnull=uuid_isnull,
        uuid_istartswith=uuid_istartswith,
        uuid_lt=uuid_lt,
        uuid_lte=uuid_lte,
        uuid_range=uuid_range,
        uuid_regex=uuid_regex,
        uuid_startswith=uuid_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    abstract: Union[Unset, str] = UNSET,
    abstract_contains: Union[Unset, str] = UNSET,
    abstract_endswith: Union[Unset, str] = UNSET,
    abstract_gt: Union[Unset, str] = UNSET,
    abstract_gte: Union[Unset, str] = UNSET,
    abstract_icontains: Union[Unset, str] = UNSET,
    abstract_iendswith: Union[Unset, str] = UNSET,
    abstract_iexact: Union[Unset, str] = UNSET,
    abstract_in: Union[Unset, list[str]] = UNSET,
    abstract_iregex: Union[Unset, str] = UNSET,
    abstract_isnull: Union[Unset, bool] = UNSET,
    abstract_istartswith: Union[Unset, str] = UNSET,
    abstract_lt: Union[Unset, str] = UNSET,
    abstract_lte: Union[Unset, str] = UNSET,
    abstract_range: Union[Unset, list[str]] = UNSET,
    abstract_regex: Union[Unset, str] = UNSET,
    abstract_startswith: Union[Unset, str] = UNSET,
    data_published_time: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_contains: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_date: Union[Unset, datetime.date] = UNSET,
    data_published_time_day: Union[Unset, float] = UNSET,
    data_published_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_gt: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_gte: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_hour: Union[Unset, float] = UNSET,
    data_published_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    data_published_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_isnull: Union[Unset, bool] = UNSET,
    data_published_time_iso_week_day: Union[Unset, float] = UNSET,
    data_published_time_iso_year: Union[Unset, float] = UNSET,
    data_published_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_lt: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_lte: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_minute: Union[Unset, float] = UNSET,
    data_published_time_month: Union[Unset, float] = UNSET,
    data_published_time_quarter: Union[Unset, float] = UNSET,
    data_published_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    data_published_time_regex: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_second: Union[Unset, float] = UNSET,
    data_published_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    data_published_time_time: Union[Unset, str] = UNSET,
    data_published_time_week: Union[Unset, float] = UNSET,
    data_published_time_week_day: Union[Unset, float] = UNSET,
    data_published_time_year: Union[Unset, float] = UNSET,
    discovery_keywords_name: Union[Unset, str] = UNSET,
    discovery_keywords_name_contains: Union[Unset, str] = UNSET,
    doi_published_time: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_contained_by: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_contains: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_date: Union[Unset, datetime.date] = UNSET,
    doi_published_time_day: Union[Unset, float] = UNSET,
    doi_published_time_endswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_gt: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_gte: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_hour: Union[Unset, float] = UNSET,
    doi_published_time_icontains: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_iendswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_iexact: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_in: Union[Unset, list[datetime.datetime]] = UNSET,
    doi_published_time_iregex: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_isnull: Union[Unset, bool] = UNSET,
    doi_published_time_iso_week_day: Union[Unset, float] = UNSET,
    doi_published_time_iso_year: Union[Unset, float] = UNSET,
    doi_published_time_istartswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_lt: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_lte: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_minute: Union[Unset, float] = UNSET,
    doi_published_time_month: Union[Unset, float] = UNSET,
    doi_published_time_quarter: Union[Unset, float] = UNSET,
    doi_published_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    doi_published_time_regex: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_second: Union[Unset, float] = UNSET,
    doi_published_time_startswith: Union[Unset, datetime.datetime] = UNSET,
    doi_published_time_time: Union[Unset, str] = UNSET,
    doi_published_time_week: Union[Unset, float] = UNSET,
    doi_published_time_week_day: Union[Unset, float] = UNSET,
    doi_published_time_year: Union[Unset, float] = UNSET,
    dont_harvest_from_projects: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_contains: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_endswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_gt: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_gte: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_icontains: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_iendswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_iexact: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_in: Union[Unset, list[bool]] = UNSET,
    dont_harvest_from_projects_iregex: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_isnull: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_istartswith: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_lt: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_lte: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_range: Union[Unset, list[bool]] = UNSET,
    dont_harvest_from_projects_regex: Union[Unset, bool] = UNSET,
    dont_harvest_from_projects_startswith: Union[Unset, bool] = UNSET,
    keywords: Union[Unset, str] = UNSET,
    keywords_contains: Union[Unset, str] = UNSET,
    keywords_endswith: Union[Unset, str] = UNSET,
    keywords_gt: Union[Unset, str] = UNSET,
    keywords_gte: Union[Unset, str] = UNSET,
    keywords_icontains: Union[Unset, str] = UNSET,
    keywords_iendswith: Union[Unset, str] = UNSET,
    keywords_iexact: Union[Unset, str] = UNSET,
    keywords_in: Union[Unset, list[str]] = UNSET,
    keywords_iregex: Union[Unset, str] = UNSET,
    keywords_isnull: Union[Unset, bool] = UNSET,
    keywords_istartswith: Union[Unset, str] = UNSET,
    keywords_lt: Union[Unset, str] = UNSET,
    keywords_lte: Union[Unset, str] = UNSET,
    keywords_range: Union[Unset, list[str]] = UNSET,
    keywords_regex: Union[Unset, str] = UNSET,
    keywords_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    member_ob_id: Union[Unset, int] = UNSET,
    member_ob_id_in: Union[Unset, list[int]] = UNSET,
    member_uuid: Union[Unset, str] = UNSET,
    member_uuid_in: Union[Unset, list[str]] = UNSET,
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
    publication_state: Union[Unset, ObservationcollectionsListPublicationState] = UNSET,
    publication_state_contains: Union[Unset, str] = UNSET,
    publication_state_endswith: Union[Unset, str] = UNSET,
    publication_state_gt: Union[Unset, str] = UNSET,
    publication_state_gte: Union[Unset, str] = UNSET,
    publication_state_icontains: Union[Unset, str] = UNSET,
    publication_state_iendswith: Union[Unset, str] = UNSET,
    publication_state_iexact: Union[Unset, str] = UNSET,
    publication_state_in: Union[Unset, list[str]] = UNSET,
    publication_state_iregex: Union[Unset, str] = UNSET,
    publication_state_isnull: Union[Unset, bool] = UNSET,
    publication_state_istartswith: Union[Unset, str] = UNSET,
    publication_state_lt: Union[Unset, str] = UNSET,
    publication_state_lte: Union[Unset, str] = UNSET,
    publication_state_range: Union[Unset, list[str]] = UNSET,
    publication_state_regex: Union[Unset, str] = UNSET,
    publication_state_startswith: Union[Unset, str] = UNSET,
    referenceable_ptr: Union[Unset, int] = UNSET,
    referenceable_ptr_gt: Union[Unset, int] = UNSET,
    referenceable_ptr_gte: Union[Unset, int] = UNSET,
    referenceable_ptr_in: Union[Unset, list[int]] = UNSET,
    referenceable_ptr_isnull: Union[Unset, bool] = UNSET,
    referenceable_ptr_lt: Union[Unset, int] = UNSET,
    referenceable_ptr_lte: Union[Unset, int] = UNSET,
    short_code: Union[Unset, str] = UNSET,
    short_code_contains: Union[Unset, str] = UNSET,
    short_code_endswith: Union[Unset, str] = UNSET,
    short_code_gt: Union[Unset, str] = UNSET,
    short_code_gte: Union[Unset, str] = UNSET,
    short_code_icontains: Union[Unset, str] = UNSET,
    short_code_iendswith: Union[Unset, str] = UNSET,
    short_code_iexact: Union[Unset, str] = UNSET,
    short_code_in: Union[Unset, list[str]] = UNSET,
    short_code_iregex: Union[Unset, str] = UNSET,
    short_code_isnull: Union[Unset, bool] = UNSET,
    short_code_istartswith: Union[Unset, str] = UNSET,
    short_code_lt: Union[Unset, str] = UNSET,
    short_code_lte: Union[Unset, str] = UNSET,
    short_code_range: Union[Unset, list[str]] = UNSET,
    short_code_regex: Union[Unset, str] = UNSET,
    short_code_startswith: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    title_contains: Union[Unset, str] = UNSET,
    title_endswith: Union[Unset, str] = UNSET,
    title_gt: Union[Unset, str] = UNSET,
    title_gte: Union[Unset, str] = UNSET,
    title_icontains: Union[Unset, str] = UNSET,
    title_iendswith: Union[Unset, str] = UNSET,
    title_iexact: Union[Unset, str] = UNSET,
    title_in: Union[Unset, list[str]] = UNSET,
    title_iregex: Union[Unset, str] = UNSET,
    title_isnull: Union[Unset, bool] = UNSET,
    title_istartswith: Union[Unset, str] = UNSET,
    title_lt: Union[Unset, str] = UNSET,
    title_lte: Union[Unset, str] = UNSET,
    title_range: Union[Unset, list[str]] = UNSET,
    title_regex: Union[Unset, str] = UNSET,
    title_startswith: Union[Unset, str] = UNSET,
    uuid: Union[Unset, str] = UNSET,
    uuid_contains: Union[Unset, str] = UNSET,
    uuid_endswith: Union[Unset, str] = UNSET,
    uuid_gt: Union[Unset, str] = UNSET,
    uuid_gte: Union[Unset, str] = UNSET,
    uuid_icontains: Union[Unset, str] = UNSET,
    uuid_iendswith: Union[Unset, str] = UNSET,
    uuid_iexact: Union[Unset, str] = UNSET,
    uuid_in: Union[Unset, list[str]] = UNSET,
    uuid_iregex: Union[Unset, str] = UNSET,
    uuid_isnull: Union[Unset, bool] = UNSET,
    uuid_istartswith: Union[Unset, str] = UNSET,
    uuid_lt: Union[Unset, str] = UNSET,
    uuid_lte: Union[Unset, str] = UNSET,
    uuid_range: Union[Unset, list[str]] = UNSET,
    uuid_regex: Union[Unset, str] = UNSET,
    uuid_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedObservationCollectionReadList]:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        abstract (Union[Unset, str]):
        abstract_contains (Union[Unset, str]):
        abstract_endswith (Union[Unset, str]):
        abstract_gt (Union[Unset, str]):
        abstract_gte (Union[Unset, str]):
        abstract_icontains (Union[Unset, str]):
        abstract_iendswith (Union[Unset, str]):
        abstract_iexact (Union[Unset, str]):
        abstract_in (Union[Unset, list[str]]):
        abstract_iregex (Union[Unset, str]):
        abstract_isnull (Union[Unset, bool]):
        abstract_istartswith (Union[Unset, str]):
        abstract_lt (Union[Unset, str]):
        abstract_lte (Union[Unset, str]):
        abstract_range (Union[Unset, list[str]]):
        abstract_regex (Union[Unset, str]):
        abstract_startswith (Union[Unset, str]):
        data_published_time (Union[Unset, datetime.datetime]):
        data_published_time_contained_by (Union[Unset, datetime.datetime]):
        data_published_time_contains (Union[Unset, datetime.datetime]):
        data_published_time_date (Union[Unset, datetime.date]):
        data_published_time_day (Union[Unset, float]):
        data_published_time_endswith (Union[Unset, datetime.datetime]):
        data_published_time_gt (Union[Unset, datetime.datetime]):
        data_published_time_gte (Union[Unset, datetime.datetime]):
        data_published_time_hour (Union[Unset, float]):
        data_published_time_icontains (Union[Unset, datetime.datetime]):
        data_published_time_iendswith (Union[Unset, datetime.datetime]):
        data_published_time_iexact (Union[Unset, datetime.datetime]):
        data_published_time_in (Union[Unset, list[datetime.datetime]]):
        data_published_time_iregex (Union[Unset, datetime.datetime]):
        data_published_time_isnull (Union[Unset, bool]):
        data_published_time_iso_week_day (Union[Unset, float]):
        data_published_time_iso_year (Union[Unset, float]):
        data_published_time_istartswith (Union[Unset, datetime.datetime]):
        data_published_time_lt (Union[Unset, datetime.datetime]):
        data_published_time_lte (Union[Unset, datetime.datetime]):
        data_published_time_minute (Union[Unset, float]):
        data_published_time_month (Union[Unset, float]):
        data_published_time_quarter (Union[Unset, float]):
        data_published_time_range (Union[Unset, list[datetime.datetime]]):
        data_published_time_regex (Union[Unset, datetime.datetime]):
        data_published_time_second (Union[Unset, float]):
        data_published_time_startswith (Union[Unset, datetime.datetime]):
        data_published_time_time (Union[Unset, str]):
        data_published_time_week (Union[Unset, float]):
        data_published_time_week_day (Union[Unset, float]):
        data_published_time_year (Union[Unset, float]):
        discovery_keywords_name (Union[Unset, str]):
        discovery_keywords_name_contains (Union[Unset, str]):
        doi_published_time (Union[Unset, datetime.datetime]):
        doi_published_time_contained_by (Union[Unset, datetime.datetime]):
        doi_published_time_contains (Union[Unset, datetime.datetime]):
        doi_published_time_date (Union[Unset, datetime.date]):
        doi_published_time_day (Union[Unset, float]):
        doi_published_time_endswith (Union[Unset, datetime.datetime]):
        doi_published_time_gt (Union[Unset, datetime.datetime]):
        doi_published_time_gte (Union[Unset, datetime.datetime]):
        doi_published_time_hour (Union[Unset, float]):
        doi_published_time_icontains (Union[Unset, datetime.datetime]):
        doi_published_time_iendswith (Union[Unset, datetime.datetime]):
        doi_published_time_iexact (Union[Unset, datetime.datetime]):
        doi_published_time_in (Union[Unset, list[datetime.datetime]]):
        doi_published_time_iregex (Union[Unset, datetime.datetime]):
        doi_published_time_isnull (Union[Unset, bool]):
        doi_published_time_iso_week_day (Union[Unset, float]):
        doi_published_time_iso_year (Union[Unset, float]):
        doi_published_time_istartswith (Union[Unset, datetime.datetime]):
        doi_published_time_lt (Union[Unset, datetime.datetime]):
        doi_published_time_lte (Union[Unset, datetime.datetime]):
        doi_published_time_minute (Union[Unset, float]):
        doi_published_time_month (Union[Unset, float]):
        doi_published_time_quarter (Union[Unset, float]):
        doi_published_time_range (Union[Unset, list[datetime.datetime]]):
        doi_published_time_regex (Union[Unset, datetime.datetime]):
        doi_published_time_second (Union[Unset, float]):
        doi_published_time_startswith (Union[Unset, datetime.datetime]):
        doi_published_time_time (Union[Unset, str]):
        doi_published_time_week (Union[Unset, float]):
        doi_published_time_week_day (Union[Unset, float]):
        doi_published_time_year (Union[Unset, float]):
        dont_harvest_from_projects (Union[Unset, bool]):
        dont_harvest_from_projects_contains (Union[Unset, bool]):
        dont_harvest_from_projects_endswith (Union[Unset, bool]):
        dont_harvest_from_projects_gt (Union[Unset, bool]):
        dont_harvest_from_projects_gte (Union[Unset, bool]):
        dont_harvest_from_projects_icontains (Union[Unset, bool]):
        dont_harvest_from_projects_iendswith (Union[Unset, bool]):
        dont_harvest_from_projects_iexact (Union[Unset, bool]):
        dont_harvest_from_projects_in (Union[Unset, list[bool]]):
        dont_harvest_from_projects_iregex (Union[Unset, bool]):
        dont_harvest_from_projects_isnull (Union[Unset, bool]):
        dont_harvest_from_projects_istartswith (Union[Unset, bool]):
        dont_harvest_from_projects_lt (Union[Unset, bool]):
        dont_harvest_from_projects_lte (Union[Unset, bool]):
        dont_harvest_from_projects_range (Union[Unset, list[bool]]):
        dont_harvest_from_projects_regex (Union[Unset, bool]):
        dont_harvest_from_projects_startswith (Union[Unset, bool]):
        keywords (Union[Unset, str]):
        keywords_contains (Union[Unset, str]):
        keywords_endswith (Union[Unset, str]):
        keywords_gt (Union[Unset, str]):
        keywords_gte (Union[Unset, str]):
        keywords_icontains (Union[Unset, str]):
        keywords_iendswith (Union[Unset, str]):
        keywords_iexact (Union[Unset, str]):
        keywords_in (Union[Unset, list[str]]):
        keywords_iregex (Union[Unset, str]):
        keywords_isnull (Union[Unset, bool]):
        keywords_istartswith (Union[Unset, str]):
        keywords_lt (Union[Unset, str]):
        keywords_lte (Union[Unset, str]):
        keywords_range (Union[Unset, list[str]]):
        keywords_regex (Union[Unset, str]):
        keywords_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        member_ob_id (Union[Unset, int]):
        member_ob_id_in (Union[Unset, list[int]]):
        member_uuid (Union[Unset, str]):
        member_uuid_in (Union[Unset, list[str]]):
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
        publication_state (Union[Unset, ObservationcollectionsListPublicationState]):
        publication_state_contains (Union[Unset, str]):
        publication_state_endswith (Union[Unset, str]):
        publication_state_gt (Union[Unset, str]):
        publication_state_gte (Union[Unset, str]):
        publication_state_icontains (Union[Unset, str]):
        publication_state_iendswith (Union[Unset, str]):
        publication_state_iexact (Union[Unset, str]):
        publication_state_in (Union[Unset, list[str]]):
        publication_state_iregex (Union[Unset, str]):
        publication_state_isnull (Union[Unset, bool]):
        publication_state_istartswith (Union[Unset, str]):
        publication_state_lt (Union[Unset, str]):
        publication_state_lte (Union[Unset, str]):
        publication_state_range (Union[Unset, list[str]]):
        publication_state_regex (Union[Unset, str]):
        publication_state_startswith (Union[Unset, str]):
        referenceable_ptr (Union[Unset, int]):
        referenceable_ptr_gt (Union[Unset, int]):
        referenceable_ptr_gte (Union[Unset, int]):
        referenceable_ptr_in (Union[Unset, list[int]]):
        referenceable_ptr_isnull (Union[Unset, bool]):
        referenceable_ptr_lt (Union[Unset, int]):
        referenceable_ptr_lte (Union[Unset, int]):
        short_code (Union[Unset, str]):
        short_code_contains (Union[Unset, str]):
        short_code_endswith (Union[Unset, str]):
        short_code_gt (Union[Unset, str]):
        short_code_gte (Union[Unset, str]):
        short_code_icontains (Union[Unset, str]):
        short_code_iendswith (Union[Unset, str]):
        short_code_iexact (Union[Unset, str]):
        short_code_in (Union[Unset, list[str]]):
        short_code_iregex (Union[Unset, str]):
        short_code_isnull (Union[Unset, bool]):
        short_code_istartswith (Union[Unset, str]):
        short_code_lt (Union[Unset, str]):
        short_code_lte (Union[Unset, str]):
        short_code_range (Union[Unset, list[str]]):
        short_code_regex (Union[Unset, str]):
        short_code_startswith (Union[Unset, str]):
        title (Union[Unset, str]):
        title_contains (Union[Unset, str]):
        title_endswith (Union[Unset, str]):
        title_gt (Union[Unset, str]):
        title_gte (Union[Unset, str]):
        title_icontains (Union[Unset, str]):
        title_iendswith (Union[Unset, str]):
        title_iexact (Union[Unset, str]):
        title_in (Union[Unset, list[str]]):
        title_iregex (Union[Unset, str]):
        title_isnull (Union[Unset, bool]):
        title_istartswith (Union[Unset, str]):
        title_lt (Union[Unset, str]):
        title_lte (Union[Unset, str]):
        title_range (Union[Unset, list[str]]):
        title_regex (Union[Unset, str]):
        title_startswith (Union[Unset, str]):
        uuid (Union[Unset, str]):
        uuid_contains (Union[Unset, str]):
        uuid_endswith (Union[Unset, str]):
        uuid_gt (Union[Unset, str]):
        uuid_gte (Union[Unset, str]):
        uuid_icontains (Union[Unset, str]):
        uuid_iendswith (Union[Unset, str]):
        uuid_iexact (Union[Unset, str]):
        uuid_in (Union[Unset, list[str]]):
        uuid_iregex (Union[Unset, str]):
        uuid_isnull (Union[Unset, bool]):
        uuid_istartswith (Union[Unset, str]):
        uuid_lt (Union[Unset, str]):
        uuid_lte (Union[Unset, str]):
        uuid_range (Union[Unset, list[str]]):
        uuid_regex (Union[Unset, str]):
        uuid_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedObservationCollectionReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            abstract=abstract,
            abstract_contains=abstract_contains,
            abstract_endswith=abstract_endswith,
            abstract_gt=abstract_gt,
            abstract_gte=abstract_gte,
            abstract_icontains=abstract_icontains,
            abstract_iendswith=abstract_iendswith,
            abstract_iexact=abstract_iexact,
            abstract_in=abstract_in,
            abstract_iregex=abstract_iregex,
            abstract_isnull=abstract_isnull,
            abstract_istartswith=abstract_istartswith,
            abstract_lt=abstract_lt,
            abstract_lte=abstract_lte,
            abstract_range=abstract_range,
            abstract_regex=abstract_regex,
            abstract_startswith=abstract_startswith,
            data_published_time=data_published_time,
            data_published_time_contained_by=data_published_time_contained_by,
            data_published_time_contains=data_published_time_contains,
            data_published_time_date=data_published_time_date,
            data_published_time_day=data_published_time_day,
            data_published_time_endswith=data_published_time_endswith,
            data_published_time_gt=data_published_time_gt,
            data_published_time_gte=data_published_time_gte,
            data_published_time_hour=data_published_time_hour,
            data_published_time_icontains=data_published_time_icontains,
            data_published_time_iendswith=data_published_time_iendswith,
            data_published_time_iexact=data_published_time_iexact,
            data_published_time_in=data_published_time_in,
            data_published_time_iregex=data_published_time_iregex,
            data_published_time_isnull=data_published_time_isnull,
            data_published_time_iso_week_day=data_published_time_iso_week_day,
            data_published_time_iso_year=data_published_time_iso_year,
            data_published_time_istartswith=data_published_time_istartswith,
            data_published_time_lt=data_published_time_lt,
            data_published_time_lte=data_published_time_lte,
            data_published_time_minute=data_published_time_minute,
            data_published_time_month=data_published_time_month,
            data_published_time_quarter=data_published_time_quarter,
            data_published_time_range=data_published_time_range,
            data_published_time_regex=data_published_time_regex,
            data_published_time_second=data_published_time_second,
            data_published_time_startswith=data_published_time_startswith,
            data_published_time_time=data_published_time_time,
            data_published_time_week=data_published_time_week,
            data_published_time_week_day=data_published_time_week_day,
            data_published_time_year=data_published_time_year,
            discovery_keywords_name=discovery_keywords_name,
            discovery_keywords_name_contains=discovery_keywords_name_contains,
            doi_published_time=doi_published_time,
            doi_published_time_contained_by=doi_published_time_contained_by,
            doi_published_time_contains=doi_published_time_contains,
            doi_published_time_date=doi_published_time_date,
            doi_published_time_day=doi_published_time_day,
            doi_published_time_endswith=doi_published_time_endswith,
            doi_published_time_gt=doi_published_time_gt,
            doi_published_time_gte=doi_published_time_gte,
            doi_published_time_hour=doi_published_time_hour,
            doi_published_time_icontains=doi_published_time_icontains,
            doi_published_time_iendswith=doi_published_time_iendswith,
            doi_published_time_iexact=doi_published_time_iexact,
            doi_published_time_in=doi_published_time_in,
            doi_published_time_iregex=doi_published_time_iregex,
            doi_published_time_isnull=doi_published_time_isnull,
            doi_published_time_iso_week_day=doi_published_time_iso_week_day,
            doi_published_time_iso_year=doi_published_time_iso_year,
            doi_published_time_istartswith=doi_published_time_istartswith,
            doi_published_time_lt=doi_published_time_lt,
            doi_published_time_lte=doi_published_time_lte,
            doi_published_time_minute=doi_published_time_minute,
            doi_published_time_month=doi_published_time_month,
            doi_published_time_quarter=doi_published_time_quarter,
            doi_published_time_range=doi_published_time_range,
            doi_published_time_regex=doi_published_time_regex,
            doi_published_time_second=doi_published_time_second,
            doi_published_time_startswith=doi_published_time_startswith,
            doi_published_time_time=doi_published_time_time,
            doi_published_time_week=doi_published_time_week,
            doi_published_time_week_day=doi_published_time_week_day,
            doi_published_time_year=doi_published_time_year,
            dont_harvest_from_projects=dont_harvest_from_projects,
            dont_harvest_from_projects_contains=dont_harvest_from_projects_contains,
            dont_harvest_from_projects_endswith=dont_harvest_from_projects_endswith,
            dont_harvest_from_projects_gt=dont_harvest_from_projects_gt,
            dont_harvest_from_projects_gte=dont_harvest_from_projects_gte,
            dont_harvest_from_projects_icontains=dont_harvest_from_projects_icontains,
            dont_harvest_from_projects_iendswith=dont_harvest_from_projects_iendswith,
            dont_harvest_from_projects_iexact=dont_harvest_from_projects_iexact,
            dont_harvest_from_projects_in=dont_harvest_from_projects_in,
            dont_harvest_from_projects_iregex=dont_harvest_from_projects_iregex,
            dont_harvest_from_projects_isnull=dont_harvest_from_projects_isnull,
            dont_harvest_from_projects_istartswith=dont_harvest_from_projects_istartswith,
            dont_harvest_from_projects_lt=dont_harvest_from_projects_lt,
            dont_harvest_from_projects_lte=dont_harvest_from_projects_lte,
            dont_harvest_from_projects_range=dont_harvest_from_projects_range,
            dont_harvest_from_projects_regex=dont_harvest_from_projects_regex,
            dont_harvest_from_projects_startswith=dont_harvest_from_projects_startswith,
            keywords=keywords,
            keywords_contains=keywords_contains,
            keywords_endswith=keywords_endswith,
            keywords_gt=keywords_gt,
            keywords_gte=keywords_gte,
            keywords_icontains=keywords_icontains,
            keywords_iendswith=keywords_iendswith,
            keywords_iexact=keywords_iexact,
            keywords_in=keywords_in,
            keywords_iregex=keywords_iregex,
            keywords_isnull=keywords_isnull,
            keywords_istartswith=keywords_istartswith,
            keywords_lt=keywords_lt,
            keywords_lte=keywords_lte,
            keywords_range=keywords_range,
            keywords_regex=keywords_regex,
            keywords_startswith=keywords_startswith,
            limit=limit,
            member_ob_id=member_ob_id,
            member_ob_id_in=member_ob_id_in,
            member_uuid=member_uuid,
            member_uuid_in=member_uuid_in,
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
            publication_state=publication_state,
            publication_state_contains=publication_state_contains,
            publication_state_endswith=publication_state_endswith,
            publication_state_gt=publication_state_gt,
            publication_state_gte=publication_state_gte,
            publication_state_icontains=publication_state_icontains,
            publication_state_iendswith=publication_state_iendswith,
            publication_state_iexact=publication_state_iexact,
            publication_state_in=publication_state_in,
            publication_state_iregex=publication_state_iregex,
            publication_state_isnull=publication_state_isnull,
            publication_state_istartswith=publication_state_istartswith,
            publication_state_lt=publication_state_lt,
            publication_state_lte=publication_state_lte,
            publication_state_range=publication_state_range,
            publication_state_regex=publication_state_regex,
            publication_state_startswith=publication_state_startswith,
            referenceable_ptr=referenceable_ptr,
            referenceable_ptr_gt=referenceable_ptr_gt,
            referenceable_ptr_gte=referenceable_ptr_gte,
            referenceable_ptr_in=referenceable_ptr_in,
            referenceable_ptr_isnull=referenceable_ptr_isnull,
            referenceable_ptr_lt=referenceable_ptr_lt,
            referenceable_ptr_lte=referenceable_ptr_lte,
            short_code=short_code,
            short_code_contains=short_code_contains,
            short_code_endswith=short_code_endswith,
            short_code_gt=short_code_gt,
            short_code_gte=short_code_gte,
            short_code_icontains=short_code_icontains,
            short_code_iendswith=short_code_iendswith,
            short_code_iexact=short_code_iexact,
            short_code_in=short_code_in,
            short_code_iregex=short_code_iregex,
            short_code_isnull=short_code_isnull,
            short_code_istartswith=short_code_istartswith,
            short_code_lt=short_code_lt,
            short_code_lte=short_code_lte,
            short_code_range=short_code_range,
            short_code_regex=short_code_regex,
            short_code_startswith=short_code_startswith,
            title=title,
            title_contains=title_contains,
            title_endswith=title_endswith,
            title_gt=title_gt,
            title_gte=title_gte,
            title_icontains=title_icontains,
            title_iendswith=title_iendswith,
            title_iexact=title_iexact,
            title_in=title_in,
            title_iregex=title_iregex,
            title_isnull=title_isnull,
            title_istartswith=title_istartswith,
            title_lt=title_lt,
            title_lte=title_lte,
            title_range=title_range,
            title_regex=title_regex,
            title_startswith=title_startswith,
            uuid=uuid,
            uuid_contains=uuid_contains,
            uuid_endswith=uuid_endswith,
            uuid_gt=uuid_gt,
            uuid_gte=uuid_gte,
            uuid_icontains=uuid_icontains,
            uuid_iendswith=uuid_iendswith,
            uuid_iexact=uuid_iexact,
            uuid_in=uuid_in,
            uuid_iregex=uuid_iregex,
            uuid_isnull=uuid_isnull,
            uuid_istartswith=uuid_istartswith,
            uuid_lt=uuid_lt,
            uuid_lte=uuid_lte,
            uuid_range=uuid_range,
            uuid_regex=uuid_regex,
            uuid_startswith=uuid_startswith,
        )
    ).parsed
