import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mpos_list_status import MposListStatus
from ...models.paginated_mobile_platform_operation_read_list import PaginatedMobilePlatformOperationReadList
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
    child_operation: Union[Unset, int] = UNSET,
    child_operation_gt: Union[Unset, int] = UNSET,
    child_operation_gte: Union[Unset, int] = UNSET,
    child_operation_in: Union[Unset, list[int]] = UNSET,
    child_operation_isnull: Union[Unset, bool] = UNSET,
    child_operation_lt: Union[Unset, int] = UNSET,
    child_operation_lte: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, int] = UNSET,
    location_east_bound_longitude: Union[Unset, float] = UNSET,
    location_east_bound_longitude_gt: Union[Unset, float] = UNSET,
    location_east_bound_longitude_gte: Union[Unset, float] = UNSET,
    location_east_bound_longitude_lt: Union[Unset, float] = UNSET,
    location_east_bound_longitude_lte: Union[Unset, float] = UNSET,
    location_east_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    location_gt: Union[Unset, int] = UNSET,
    location_gte: Union[Unset, int] = UNSET,
    location_in: Union[Unset, list[int]] = UNSET,
    location_isnull: Union[Unset, bool] = UNSET,
    location_lt: Union[Unset, int] = UNSET,
    location_lte: Union[Unset, int] = UNSET,
    location_north_bound_latitude: Union[Unset, float] = UNSET,
    location_north_bound_latitude_gt: Union[Unset, float] = UNSET,
    location_north_bound_latitude_gte: Union[Unset, float] = UNSET,
    location_north_bound_latitude_lt: Union[Unset, float] = UNSET,
    location_north_bound_latitude_lte: Union[Unset, float] = UNSET,
    location_north_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    location_ob_id: Union[Unset, int] = UNSET,
    location_ob_id_in: Union[Unset, list[int]] = UNSET,
    location_south_bound_latitude: Union[Unset, float] = UNSET,
    location_south_bound_latitude_gt: Union[Unset, float] = UNSET,
    location_south_bound_latitude_gte: Union[Unset, float] = UNSET,
    location_south_bound_latitude_lt: Union[Unset, float] = UNSET,
    location_south_bound_latitude_lte: Union[Unset, float] = UNSET,
    location_south_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    location_west_bound_longitude: Union[Unset, float] = UNSET,
    location_west_bound_longitude_gt: Union[Unset, float] = UNSET,
    location_west_bound_longitude_gte: Union[Unset, float] = UNSET,
    location_west_bound_longitude_lt: Union[Unset, float] = UNSET,
    location_west_bound_longitude_lte: Union[Unset, float] = UNSET,
    location_west_bound_longitude_range: Union[Unset, list[float]] = UNSET,
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
    operation_time: Union[Unset, int] = UNSET,
    operation_time_end_time: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_gt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_gte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_lt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_lte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    operation_time_gt: Union[Unset, int] = UNSET,
    operation_time_gte: Union[Unset, int] = UNSET,
    operation_time_in: Union[Unset, list[int]] = UNSET,
    operation_time_isnull: Union[Unset, bool] = UNSET,
    operation_time_lt: Union[Unset, int] = UNSET,
    operation_time_lte: Union[Unset, int] = UNSET,
    operation_time_ob_id: Union[Unset, int] = UNSET,
    operation_time_ob_id_in: Union[Unset, list[int]] = UNSET,
    operation_time_start_time: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_gt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_gte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_lt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_lte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    platform_field: Union[Unset, int] = UNSET,
    platform_field_gt: Union[Unset, int] = UNSET,
    platform_field_gte: Union[Unset, int] = UNSET,
    platform_field_in: Union[Unset, list[int]] = UNSET,
    platform_field_isnull: Union[Unset, bool] = UNSET,
    platform_field_lt: Union[Unset, int] = UNSET,
    platform_field_lte: Union[Unset, int] = UNSET,
    platform_field_ob_id: Union[Unset, int] = UNSET,
    platform_field_ob_id_in: Union[Unset, list[int]] = UNSET,
    platform_field_uuid: Union[Unset, str] = UNSET,
    platform_field_uuid_in: Union[Unset, list[str]] = UNSET,
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
    status: Union[Unset, MposListStatus] = UNSET,
    status_contains: Union[Unset, str] = UNSET,
    status_endswith: Union[Unset, str] = UNSET,
    status_gt: Union[Unset, str] = UNSET,
    status_gte: Union[Unset, str] = UNSET,
    status_icontains: Union[Unset, str] = UNSET,
    status_iendswith: Union[Unset, str] = UNSET,
    status_iexact: Union[Unset, str] = UNSET,
    status_in: Union[Unset, list[str]] = UNSET,
    status_iregex: Union[Unset, str] = UNSET,
    status_isnull: Union[Unset, bool] = UNSET,
    status_istartswith: Union[Unset, str] = UNSET,
    status_lt: Union[Unset, str] = UNSET,
    status_lte: Union[Unset, str] = UNSET,
    status_range: Union[Unset, list[str]] = UNSET,
    status_regex: Union[Unset, str] = UNSET,
    status_startswith: Union[Unset, str] = UNSET,
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

    params["childOperation"] = child_operation

    params["childOperation__gt"] = child_operation_gt

    params["childOperation__gte"] = child_operation_gte

    json_child_operation_in: Union[Unset, list[int]] = UNSET
    if not isinstance(child_operation_in, Unset):
        json_child_operation_in = ",".join(map(str, child_operation_in))

    params["childOperation__in"] = json_child_operation_in

    params["childOperation__isnull"] = child_operation_isnull

    params["childOperation__lt"] = child_operation_lt

    params["childOperation__lte"] = child_operation_lte

    params["limit"] = limit

    params["location"] = location

    params["location__eastBoundLongitude"] = location_east_bound_longitude

    params["location__eastBoundLongitude__gt"] = location_east_bound_longitude_gt

    params["location__eastBoundLongitude__gte"] = location_east_bound_longitude_gte

    params["location__eastBoundLongitude__lt"] = location_east_bound_longitude_lt

    params["location__eastBoundLongitude__lte"] = location_east_bound_longitude_lte

    json_location_east_bound_longitude_range: Union[Unset, list[float]] = UNSET
    if not isinstance(location_east_bound_longitude_range, Unset):
        json_location_east_bound_longitude_range = ",".join(map(str, location_east_bound_longitude_range))

    params["location__eastBoundLongitude__range"] = json_location_east_bound_longitude_range

    params["location__gt"] = location_gt

    params["location__gte"] = location_gte

    json_location_in: Union[Unset, list[int]] = UNSET
    if not isinstance(location_in, Unset):
        json_location_in = ",".join(map(str, location_in))

    params["location__in"] = json_location_in

    params["location__isnull"] = location_isnull

    params["location__lt"] = location_lt

    params["location__lte"] = location_lte

    params["location__northBoundLatitude"] = location_north_bound_latitude

    params["location__northBoundLatitude__gt"] = location_north_bound_latitude_gt

    params["location__northBoundLatitude__gte"] = location_north_bound_latitude_gte

    params["location__northBoundLatitude__lt"] = location_north_bound_latitude_lt

    params["location__northBoundLatitude__lte"] = location_north_bound_latitude_lte

    json_location_north_bound_latitude_range: Union[Unset, list[float]] = UNSET
    if not isinstance(location_north_bound_latitude_range, Unset):
        json_location_north_bound_latitude_range = ",".join(map(str, location_north_bound_latitude_range))

    params["location__northBoundLatitude__range"] = json_location_north_bound_latitude_range

    params["location__ob_id"] = location_ob_id

    json_location_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(location_ob_id_in, Unset):
        json_location_ob_id_in = ",".join(map(str, location_ob_id_in))

    params["location__ob_id__in"] = json_location_ob_id_in

    params["location__southBoundLatitude"] = location_south_bound_latitude

    params["location__southBoundLatitude__gt"] = location_south_bound_latitude_gt

    params["location__southBoundLatitude__gte"] = location_south_bound_latitude_gte

    params["location__southBoundLatitude__lt"] = location_south_bound_latitude_lt

    params["location__southBoundLatitude__lte"] = location_south_bound_latitude_lte

    json_location_south_bound_latitude_range: Union[Unset, list[float]] = UNSET
    if not isinstance(location_south_bound_latitude_range, Unset):
        json_location_south_bound_latitude_range = ",".join(map(str, location_south_bound_latitude_range))

    params["location__southBoundLatitude__range"] = json_location_south_bound_latitude_range

    params["location__westBoundLongitude"] = location_west_bound_longitude

    params["location__westBoundLongitude__gt"] = location_west_bound_longitude_gt

    params["location__westBoundLongitude__gte"] = location_west_bound_longitude_gte

    params["location__westBoundLongitude__lt"] = location_west_bound_longitude_lt

    params["location__westBoundLongitude__lte"] = location_west_bound_longitude_lte

    json_location_west_bound_longitude_range: Union[Unset, list[float]] = UNSET
    if not isinstance(location_west_bound_longitude_range, Unset):
        json_location_west_bound_longitude_range = ",".join(map(str, location_west_bound_longitude_range))

    params["location__westBoundLongitude__range"] = json_location_west_bound_longitude_range

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

    params["operationTime"] = operation_time

    json_operation_time_end_time: Union[Unset, str] = UNSET
    if not isinstance(operation_time_end_time, Unset):
        json_operation_time_end_time = operation_time_end_time.isoformat()
    params["operationTime__endTime"] = json_operation_time_end_time

    json_operation_time_end_time_gt: Union[Unset, str] = UNSET
    if not isinstance(operation_time_end_time_gt, Unset):
        json_operation_time_end_time_gt = operation_time_end_time_gt.isoformat()
    params["operationTime__endTime__gt"] = json_operation_time_end_time_gt

    json_operation_time_end_time_gte: Union[Unset, str] = UNSET
    if not isinstance(operation_time_end_time_gte, Unset):
        json_operation_time_end_time_gte = operation_time_end_time_gte.isoformat()
    params["operationTime__endTime__gte"] = json_operation_time_end_time_gte

    json_operation_time_end_time_lt: Union[Unset, str] = UNSET
    if not isinstance(operation_time_end_time_lt, Unset):
        json_operation_time_end_time_lt = operation_time_end_time_lt.isoformat()
    params["operationTime__endTime__lt"] = json_operation_time_end_time_lt

    json_operation_time_end_time_lte: Union[Unset, str] = UNSET
    if not isinstance(operation_time_end_time_lte, Unset):
        json_operation_time_end_time_lte = operation_time_end_time_lte.isoformat()
    params["operationTime__endTime__lte"] = json_operation_time_end_time_lte

    json_operation_time_end_time_range: Union[Unset, list[str]] = UNSET
    if not isinstance(operation_time_end_time_range, Unset):
        json_operation_time_end_time_range = []
        for operation_time_end_time_range_item_data in operation_time_end_time_range:
            operation_time_end_time_range_item = operation_time_end_time_range_item_data.isoformat()
            json_operation_time_end_time_range.append(operation_time_end_time_range_item)

    params["operationTime__endTime__range"] = json_operation_time_end_time_range

    params["operationTime__gt"] = operation_time_gt

    params["operationTime__gte"] = operation_time_gte

    json_operation_time_in: Union[Unset, list[int]] = UNSET
    if not isinstance(operation_time_in, Unset):
        json_operation_time_in = ",".join(map(str, operation_time_in))

    params["operationTime__in"] = json_operation_time_in

    params["operationTime__isnull"] = operation_time_isnull

    params["operationTime__lt"] = operation_time_lt

    params["operationTime__lte"] = operation_time_lte

    params["operationTime__ob_id"] = operation_time_ob_id

    json_operation_time_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(operation_time_ob_id_in, Unset):
        json_operation_time_ob_id_in = ",".join(map(str, operation_time_ob_id_in))

    params["operationTime__ob_id__in"] = json_operation_time_ob_id_in

    json_operation_time_start_time: Union[Unset, str] = UNSET
    if not isinstance(operation_time_start_time, Unset):
        json_operation_time_start_time = operation_time_start_time.isoformat()
    params["operationTime__startTime"] = json_operation_time_start_time

    json_operation_time_start_time_gt: Union[Unset, str] = UNSET
    if not isinstance(operation_time_start_time_gt, Unset):
        json_operation_time_start_time_gt = operation_time_start_time_gt.isoformat()
    params["operationTime__startTime__gt"] = json_operation_time_start_time_gt

    json_operation_time_start_time_gte: Union[Unset, str] = UNSET
    if not isinstance(operation_time_start_time_gte, Unset):
        json_operation_time_start_time_gte = operation_time_start_time_gte.isoformat()
    params["operationTime__startTime__gte"] = json_operation_time_start_time_gte

    json_operation_time_start_time_lt: Union[Unset, str] = UNSET
    if not isinstance(operation_time_start_time_lt, Unset):
        json_operation_time_start_time_lt = operation_time_start_time_lt.isoformat()
    params["operationTime__startTime__lt"] = json_operation_time_start_time_lt

    json_operation_time_start_time_lte: Union[Unset, str] = UNSET
    if not isinstance(operation_time_start_time_lte, Unset):
        json_operation_time_start_time_lte = operation_time_start_time_lte.isoformat()
    params["operationTime__startTime__lte"] = json_operation_time_start_time_lte

    json_operation_time_start_time_range: Union[Unset, list[str]] = UNSET
    if not isinstance(operation_time_start_time_range, Unset):
        json_operation_time_start_time_range = []
        for operation_time_start_time_range_item_data in operation_time_start_time_range:
            operation_time_start_time_range_item = operation_time_start_time_range_item_data.isoformat()
            json_operation_time_start_time_range.append(operation_time_start_time_range_item)

    params["operationTime__startTime__range"] = json_operation_time_start_time_range

    params["ordering"] = ordering

    params["platform_field"] = platform_field

    params["platform_field__gt"] = platform_field_gt

    params["platform_field__gte"] = platform_field_gte

    json_platform_field_in: Union[Unset, list[int]] = UNSET
    if not isinstance(platform_field_in, Unset):
        json_platform_field_in = ",".join(map(str, platform_field_in))

    params["platform_field__in"] = json_platform_field_in

    params["platform_field__isnull"] = platform_field_isnull

    params["platform_field__lt"] = platform_field_lt

    params["platform_field__lte"] = platform_field_lte

    params["platform_field__ob_id"] = platform_field_ob_id

    json_platform_field_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(platform_field_ob_id_in, Unset):
        json_platform_field_ob_id_in = ",".join(map(str, platform_field_ob_id_in))

    params["platform_field__ob_id__in"] = json_platform_field_ob_id_in

    params["platform_field__uuid"] = platform_field_uuid

    json_platform_field_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(platform_field_uuid_in, Unset):
        json_platform_field_uuid_in = ",".join(map(str, platform_field_uuid_in))

    params["platform_field__uuid__in"] = json_platform_field_uuid_in

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

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["status__contains"] = status_contains

    params["status__endswith"] = status_endswith

    params["status__gt"] = status_gt

    params["status__gte"] = status_gte

    params["status__icontains"] = status_icontains

    params["status__iendswith"] = status_iendswith

    params["status__iexact"] = status_iexact

    json_status_in: Union[Unset, list[str]] = UNSET
    if not isinstance(status_in, Unset):
        json_status_in = ",".join(map(str, status_in))

    params["status__in"] = json_status_in

    params["status__iregex"] = status_iregex

    params["status__isnull"] = status_isnull

    params["status__istartswith"] = status_istartswith

    params["status__lt"] = status_lt

    params["status__lte"] = status_lte

    json_status_range: Union[Unset, list[str]] = UNSET
    if not isinstance(status_range, Unset):
        json_status_range = ",".join(map(str, status_range))

    params["status__range"] = json_status_range

    params["status__regex"] = status_regex

    params["status__startswith"] = status_startswith

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
        "url": "/api/v3/mpos/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedMobilePlatformOperationReadList]:
    if response.status_code == 200:
        response_200 = PaginatedMobilePlatformOperationReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedMobilePlatformOperationReadList]:
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
    child_operation: Union[Unset, int] = UNSET,
    child_operation_gt: Union[Unset, int] = UNSET,
    child_operation_gte: Union[Unset, int] = UNSET,
    child_operation_in: Union[Unset, list[int]] = UNSET,
    child_operation_isnull: Union[Unset, bool] = UNSET,
    child_operation_lt: Union[Unset, int] = UNSET,
    child_operation_lte: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, int] = UNSET,
    location_east_bound_longitude: Union[Unset, float] = UNSET,
    location_east_bound_longitude_gt: Union[Unset, float] = UNSET,
    location_east_bound_longitude_gte: Union[Unset, float] = UNSET,
    location_east_bound_longitude_lt: Union[Unset, float] = UNSET,
    location_east_bound_longitude_lte: Union[Unset, float] = UNSET,
    location_east_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    location_gt: Union[Unset, int] = UNSET,
    location_gte: Union[Unset, int] = UNSET,
    location_in: Union[Unset, list[int]] = UNSET,
    location_isnull: Union[Unset, bool] = UNSET,
    location_lt: Union[Unset, int] = UNSET,
    location_lte: Union[Unset, int] = UNSET,
    location_north_bound_latitude: Union[Unset, float] = UNSET,
    location_north_bound_latitude_gt: Union[Unset, float] = UNSET,
    location_north_bound_latitude_gte: Union[Unset, float] = UNSET,
    location_north_bound_latitude_lt: Union[Unset, float] = UNSET,
    location_north_bound_latitude_lte: Union[Unset, float] = UNSET,
    location_north_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    location_ob_id: Union[Unset, int] = UNSET,
    location_ob_id_in: Union[Unset, list[int]] = UNSET,
    location_south_bound_latitude: Union[Unset, float] = UNSET,
    location_south_bound_latitude_gt: Union[Unset, float] = UNSET,
    location_south_bound_latitude_gte: Union[Unset, float] = UNSET,
    location_south_bound_latitude_lt: Union[Unset, float] = UNSET,
    location_south_bound_latitude_lte: Union[Unset, float] = UNSET,
    location_south_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    location_west_bound_longitude: Union[Unset, float] = UNSET,
    location_west_bound_longitude_gt: Union[Unset, float] = UNSET,
    location_west_bound_longitude_gte: Union[Unset, float] = UNSET,
    location_west_bound_longitude_lt: Union[Unset, float] = UNSET,
    location_west_bound_longitude_lte: Union[Unset, float] = UNSET,
    location_west_bound_longitude_range: Union[Unset, list[float]] = UNSET,
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
    operation_time: Union[Unset, int] = UNSET,
    operation_time_end_time: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_gt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_gte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_lt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_lte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    operation_time_gt: Union[Unset, int] = UNSET,
    operation_time_gte: Union[Unset, int] = UNSET,
    operation_time_in: Union[Unset, list[int]] = UNSET,
    operation_time_isnull: Union[Unset, bool] = UNSET,
    operation_time_lt: Union[Unset, int] = UNSET,
    operation_time_lte: Union[Unset, int] = UNSET,
    operation_time_ob_id: Union[Unset, int] = UNSET,
    operation_time_ob_id_in: Union[Unset, list[int]] = UNSET,
    operation_time_start_time: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_gt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_gte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_lt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_lte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    platform_field: Union[Unset, int] = UNSET,
    platform_field_gt: Union[Unset, int] = UNSET,
    platform_field_gte: Union[Unset, int] = UNSET,
    platform_field_in: Union[Unset, list[int]] = UNSET,
    platform_field_isnull: Union[Unset, bool] = UNSET,
    platform_field_lt: Union[Unset, int] = UNSET,
    platform_field_lte: Union[Unset, int] = UNSET,
    platform_field_ob_id: Union[Unset, int] = UNSET,
    platform_field_ob_id_in: Union[Unset, list[int]] = UNSET,
    platform_field_uuid: Union[Unset, str] = UNSET,
    platform_field_uuid_in: Union[Unset, list[str]] = UNSET,
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
    status: Union[Unset, MposListStatus] = UNSET,
    status_contains: Union[Unset, str] = UNSET,
    status_endswith: Union[Unset, str] = UNSET,
    status_gt: Union[Unset, str] = UNSET,
    status_gte: Union[Unset, str] = UNSET,
    status_icontains: Union[Unset, str] = UNSET,
    status_iendswith: Union[Unset, str] = UNSET,
    status_iexact: Union[Unset, str] = UNSET,
    status_in: Union[Unset, list[str]] = UNSET,
    status_iregex: Union[Unset, str] = UNSET,
    status_isnull: Union[Unset, bool] = UNSET,
    status_istartswith: Union[Unset, str] = UNSET,
    status_lt: Union[Unset, str] = UNSET,
    status_lte: Union[Unset, str] = UNSET,
    status_range: Union[Unset, list[str]] = UNSET,
    status_regex: Union[Unset, str] = UNSET,
    status_startswith: Union[Unset, str] = UNSET,
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
) -> Response[PaginatedMobilePlatformOperationReadList]:
    """Get a list of Mobile Platform Operation objects.

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
        child_operation (Union[Unset, int]):
        child_operation_gt (Union[Unset, int]):
        child_operation_gte (Union[Unset, int]):
        child_operation_in (Union[Unset, list[int]]):
        child_operation_isnull (Union[Unset, bool]):
        child_operation_lt (Union[Unset, int]):
        child_operation_lte (Union[Unset, int]):
        limit (Union[Unset, int]):
        location (Union[Unset, int]):
        location_east_bound_longitude (Union[Unset, float]):
        location_east_bound_longitude_gt (Union[Unset, float]):
        location_east_bound_longitude_gte (Union[Unset, float]):
        location_east_bound_longitude_lt (Union[Unset, float]):
        location_east_bound_longitude_lte (Union[Unset, float]):
        location_east_bound_longitude_range (Union[Unset, list[float]]):
        location_gt (Union[Unset, int]):
        location_gte (Union[Unset, int]):
        location_in (Union[Unset, list[int]]):
        location_isnull (Union[Unset, bool]):
        location_lt (Union[Unset, int]):
        location_lte (Union[Unset, int]):
        location_north_bound_latitude (Union[Unset, float]):
        location_north_bound_latitude_gt (Union[Unset, float]):
        location_north_bound_latitude_gte (Union[Unset, float]):
        location_north_bound_latitude_lt (Union[Unset, float]):
        location_north_bound_latitude_lte (Union[Unset, float]):
        location_north_bound_latitude_range (Union[Unset, list[float]]):
        location_ob_id (Union[Unset, int]):
        location_ob_id_in (Union[Unset, list[int]]):
        location_south_bound_latitude (Union[Unset, float]):
        location_south_bound_latitude_gt (Union[Unset, float]):
        location_south_bound_latitude_gte (Union[Unset, float]):
        location_south_bound_latitude_lt (Union[Unset, float]):
        location_south_bound_latitude_lte (Union[Unset, float]):
        location_south_bound_latitude_range (Union[Unset, list[float]]):
        location_west_bound_longitude (Union[Unset, float]):
        location_west_bound_longitude_gt (Union[Unset, float]):
        location_west_bound_longitude_gte (Union[Unset, float]):
        location_west_bound_longitude_lt (Union[Unset, float]):
        location_west_bound_longitude_lte (Union[Unset, float]):
        location_west_bound_longitude_range (Union[Unset, list[float]]):
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
        operation_time (Union[Unset, int]):
        operation_time_end_time (Union[Unset, datetime.datetime]):
        operation_time_end_time_gt (Union[Unset, datetime.datetime]):
        operation_time_end_time_gte (Union[Unset, datetime.datetime]):
        operation_time_end_time_lt (Union[Unset, datetime.datetime]):
        operation_time_end_time_lte (Union[Unset, datetime.datetime]):
        operation_time_end_time_range (Union[Unset, list[datetime.datetime]]):
        operation_time_gt (Union[Unset, int]):
        operation_time_gte (Union[Unset, int]):
        operation_time_in (Union[Unset, list[int]]):
        operation_time_isnull (Union[Unset, bool]):
        operation_time_lt (Union[Unset, int]):
        operation_time_lte (Union[Unset, int]):
        operation_time_ob_id (Union[Unset, int]):
        operation_time_ob_id_in (Union[Unset, list[int]]):
        operation_time_start_time (Union[Unset, datetime.datetime]):
        operation_time_start_time_gt (Union[Unset, datetime.datetime]):
        operation_time_start_time_gte (Union[Unset, datetime.datetime]):
        operation_time_start_time_lt (Union[Unset, datetime.datetime]):
        operation_time_start_time_lte (Union[Unset, datetime.datetime]):
        operation_time_start_time_range (Union[Unset, list[datetime.datetime]]):
        ordering (Union[Unset, str]):
        platform_field (Union[Unset, int]):
        platform_field_gt (Union[Unset, int]):
        platform_field_gte (Union[Unset, int]):
        platform_field_in (Union[Unset, list[int]]):
        platform_field_isnull (Union[Unset, bool]):
        platform_field_lt (Union[Unset, int]):
        platform_field_lte (Union[Unset, int]):
        platform_field_ob_id (Union[Unset, int]):
        platform_field_ob_id_in (Union[Unset, list[int]]):
        platform_field_uuid (Union[Unset, str]):
        platform_field_uuid_in (Union[Unset, list[str]]):
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
        status (Union[Unset, MposListStatus]):
        status_contains (Union[Unset, str]):
        status_endswith (Union[Unset, str]):
        status_gt (Union[Unset, str]):
        status_gte (Union[Unset, str]):
        status_icontains (Union[Unset, str]):
        status_iendswith (Union[Unset, str]):
        status_iexact (Union[Unset, str]):
        status_in (Union[Unset, list[str]]):
        status_iregex (Union[Unset, str]):
        status_isnull (Union[Unset, bool]):
        status_istartswith (Union[Unset, str]):
        status_lt (Union[Unset, str]):
        status_lte (Union[Unset, str]):
        status_range (Union[Unset, list[str]]):
        status_regex (Union[Unset, str]):
        status_startswith (Union[Unset, str]):
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
        Response[PaginatedMobilePlatformOperationReadList]
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
        child_operation=child_operation,
        child_operation_gt=child_operation_gt,
        child_operation_gte=child_operation_gte,
        child_operation_in=child_operation_in,
        child_operation_isnull=child_operation_isnull,
        child_operation_lt=child_operation_lt,
        child_operation_lte=child_operation_lte,
        limit=limit,
        location=location,
        location_east_bound_longitude=location_east_bound_longitude,
        location_east_bound_longitude_gt=location_east_bound_longitude_gt,
        location_east_bound_longitude_gte=location_east_bound_longitude_gte,
        location_east_bound_longitude_lt=location_east_bound_longitude_lt,
        location_east_bound_longitude_lte=location_east_bound_longitude_lte,
        location_east_bound_longitude_range=location_east_bound_longitude_range,
        location_gt=location_gt,
        location_gte=location_gte,
        location_in=location_in,
        location_isnull=location_isnull,
        location_lt=location_lt,
        location_lte=location_lte,
        location_north_bound_latitude=location_north_bound_latitude,
        location_north_bound_latitude_gt=location_north_bound_latitude_gt,
        location_north_bound_latitude_gte=location_north_bound_latitude_gte,
        location_north_bound_latitude_lt=location_north_bound_latitude_lt,
        location_north_bound_latitude_lte=location_north_bound_latitude_lte,
        location_north_bound_latitude_range=location_north_bound_latitude_range,
        location_ob_id=location_ob_id,
        location_ob_id_in=location_ob_id_in,
        location_south_bound_latitude=location_south_bound_latitude,
        location_south_bound_latitude_gt=location_south_bound_latitude_gt,
        location_south_bound_latitude_gte=location_south_bound_latitude_gte,
        location_south_bound_latitude_lt=location_south_bound_latitude_lt,
        location_south_bound_latitude_lte=location_south_bound_latitude_lte,
        location_south_bound_latitude_range=location_south_bound_latitude_range,
        location_west_bound_longitude=location_west_bound_longitude,
        location_west_bound_longitude_gt=location_west_bound_longitude_gt,
        location_west_bound_longitude_gte=location_west_bound_longitude_gte,
        location_west_bound_longitude_lt=location_west_bound_longitude_lt,
        location_west_bound_longitude_lte=location_west_bound_longitude_lte,
        location_west_bound_longitude_range=location_west_bound_longitude_range,
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
        operation_time=operation_time,
        operation_time_end_time=operation_time_end_time,
        operation_time_end_time_gt=operation_time_end_time_gt,
        operation_time_end_time_gte=operation_time_end_time_gte,
        operation_time_end_time_lt=operation_time_end_time_lt,
        operation_time_end_time_lte=operation_time_end_time_lte,
        operation_time_end_time_range=operation_time_end_time_range,
        operation_time_gt=operation_time_gt,
        operation_time_gte=operation_time_gte,
        operation_time_in=operation_time_in,
        operation_time_isnull=operation_time_isnull,
        operation_time_lt=operation_time_lt,
        operation_time_lte=operation_time_lte,
        operation_time_ob_id=operation_time_ob_id,
        operation_time_ob_id_in=operation_time_ob_id_in,
        operation_time_start_time=operation_time_start_time,
        operation_time_start_time_gt=operation_time_start_time_gt,
        operation_time_start_time_gte=operation_time_start_time_gte,
        operation_time_start_time_lt=operation_time_start_time_lt,
        operation_time_start_time_lte=operation_time_start_time_lte,
        operation_time_start_time_range=operation_time_start_time_range,
        ordering=ordering,
        platform_field=platform_field,
        platform_field_gt=platform_field_gt,
        platform_field_gte=platform_field_gte,
        platform_field_in=platform_field_in,
        platform_field_isnull=platform_field_isnull,
        platform_field_lt=platform_field_lt,
        platform_field_lte=platform_field_lte,
        platform_field_ob_id=platform_field_ob_id,
        platform_field_ob_id_in=platform_field_ob_id_in,
        platform_field_uuid=platform_field_uuid,
        platform_field_uuid_in=platform_field_uuid_in,
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
        status=status,
        status_contains=status_contains,
        status_endswith=status_endswith,
        status_gt=status_gt,
        status_gte=status_gte,
        status_icontains=status_icontains,
        status_iendswith=status_iendswith,
        status_iexact=status_iexact,
        status_in=status_in,
        status_iregex=status_iregex,
        status_isnull=status_isnull,
        status_istartswith=status_istartswith,
        status_lt=status_lt,
        status_lte=status_lte,
        status_range=status_range,
        status_regex=status_regex,
        status_startswith=status_startswith,
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
    child_operation: Union[Unset, int] = UNSET,
    child_operation_gt: Union[Unset, int] = UNSET,
    child_operation_gte: Union[Unset, int] = UNSET,
    child_operation_in: Union[Unset, list[int]] = UNSET,
    child_operation_isnull: Union[Unset, bool] = UNSET,
    child_operation_lt: Union[Unset, int] = UNSET,
    child_operation_lte: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, int] = UNSET,
    location_east_bound_longitude: Union[Unset, float] = UNSET,
    location_east_bound_longitude_gt: Union[Unset, float] = UNSET,
    location_east_bound_longitude_gte: Union[Unset, float] = UNSET,
    location_east_bound_longitude_lt: Union[Unset, float] = UNSET,
    location_east_bound_longitude_lte: Union[Unset, float] = UNSET,
    location_east_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    location_gt: Union[Unset, int] = UNSET,
    location_gte: Union[Unset, int] = UNSET,
    location_in: Union[Unset, list[int]] = UNSET,
    location_isnull: Union[Unset, bool] = UNSET,
    location_lt: Union[Unset, int] = UNSET,
    location_lte: Union[Unset, int] = UNSET,
    location_north_bound_latitude: Union[Unset, float] = UNSET,
    location_north_bound_latitude_gt: Union[Unset, float] = UNSET,
    location_north_bound_latitude_gte: Union[Unset, float] = UNSET,
    location_north_bound_latitude_lt: Union[Unset, float] = UNSET,
    location_north_bound_latitude_lte: Union[Unset, float] = UNSET,
    location_north_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    location_ob_id: Union[Unset, int] = UNSET,
    location_ob_id_in: Union[Unset, list[int]] = UNSET,
    location_south_bound_latitude: Union[Unset, float] = UNSET,
    location_south_bound_latitude_gt: Union[Unset, float] = UNSET,
    location_south_bound_latitude_gte: Union[Unset, float] = UNSET,
    location_south_bound_latitude_lt: Union[Unset, float] = UNSET,
    location_south_bound_latitude_lte: Union[Unset, float] = UNSET,
    location_south_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    location_west_bound_longitude: Union[Unset, float] = UNSET,
    location_west_bound_longitude_gt: Union[Unset, float] = UNSET,
    location_west_bound_longitude_gte: Union[Unset, float] = UNSET,
    location_west_bound_longitude_lt: Union[Unset, float] = UNSET,
    location_west_bound_longitude_lte: Union[Unset, float] = UNSET,
    location_west_bound_longitude_range: Union[Unset, list[float]] = UNSET,
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
    operation_time: Union[Unset, int] = UNSET,
    operation_time_end_time: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_gt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_gte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_lt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_lte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    operation_time_gt: Union[Unset, int] = UNSET,
    operation_time_gte: Union[Unset, int] = UNSET,
    operation_time_in: Union[Unset, list[int]] = UNSET,
    operation_time_isnull: Union[Unset, bool] = UNSET,
    operation_time_lt: Union[Unset, int] = UNSET,
    operation_time_lte: Union[Unset, int] = UNSET,
    operation_time_ob_id: Union[Unset, int] = UNSET,
    operation_time_ob_id_in: Union[Unset, list[int]] = UNSET,
    operation_time_start_time: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_gt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_gte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_lt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_lte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    platform_field: Union[Unset, int] = UNSET,
    platform_field_gt: Union[Unset, int] = UNSET,
    platform_field_gte: Union[Unset, int] = UNSET,
    platform_field_in: Union[Unset, list[int]] = UNSET,
    platform_field_isnull: Union[Unset, bool] = UNSET,
    platform_field_lt: Union[Unset, int] = UNSET,
    platform_field_lte: Union[Unset, int] = UNSET,
    platform_field_ob_id: Union[Unset, int] = UNSET,
    platform_field_ob_id_in: Union[Unset, list[int]] = UNSET,
    platform_field_uuid: Union[Unset, str] = UNSET,
    platform_field_uuid_in: Union[Unset, list[str]] = UNSET,
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
    status: Union[Unset, MposListStatus] = UNSET,
    status_contains: Union[Unset, str] = UNSET,
    status_endswith: Union[Unset, str] = UNSET,
    status_gt: Union[Unset, str] = UNSET,
    status_gte: Union[Unset, str] = UNSET,
    status_icontains: Union[Unset, str] = UNSET,
    status_iendswith: Union[Unset, str] = UNSET,
    status_iexact: Union[Unset, str] = UNSET,
    status_in: Union[Unset, list[str]] = UNSET,
    status_iregex: Union[Unset, str] = UNSET,
    status_isnull: Union[Unset, bool] = UNSET,
    status_istartswith: Union[Unset, str] = UNSET,
    status_lt: Union[Unset, str] = UNSET,
    status_lte: Union[Unset, str] = UNSET,
    status_range: Union[Unset, list[str]] = UNSET,
    status_regex: Union[Unset, str] = UNSET,
    status_startswith: Union[Unset, str] = UNSET,
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
) -> Optional[PaginatedMobilePlatformOperationReadList]:
    """Get a list of Mobile Platform Operation objects.

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
        child_operation (Union[Unset, int]):
        child_operation_gt (Union[Unset, int]):
        child_operation_gte (Union[Unset, int]):
        child_operation_in (Union[Unset, list[int]]):
        child_operation_isnull (Union[Unset, bool]):
        child_operation_lt (Union[Unset, int]):
        child_operation_lte (Union[Unset, int]):
        limit (Union[Unset, int]):
        location (Union[Unset, int]):
        location_east_bound_longitude (Union[Unset, float]):
        location_east_bound_longitude_gt (Union[Unset, float]):
        location_east_bound_longitude_gte (Union[Unset, float]):
        location_east_bound_longitude_lt (Union[Unset, float]):
        location_east_bound_longitude_lte (Union[Unset, float]):
        location_east_bound_longitude_range (Union[Unset, list[float]]):
        location_gt (Union[Unset, int]):
        location_gte (Union[Unset, int]):
        location_in (Union[Unset, list[int]]):
        location_isnull (Union[Unset, bool]):
        location_lt (Union[Unset, int]):
        location_lte (Union[Unset, int]):
        location_north_bound_latitude (Union[Unset, float]):
        location_north_bound_latitude_gt (Union[Unset, float]):
        location_north_bound_latitude_gte (Union[Unset, float]):
        location_north_bound_latitude_lt (Union[Unset, float]):
        location_north_bound_latitude_lte (Union[Unset, float]):
        location_north_bound_latitude_range (Union[Unset, list[float]]):
        location_ob_id (Union[Unset, int]):
        location_ob_id_in (Union[Unset, list[int]]):
        location_south_bound_latitude (Union[Unset, float]):
        location_south_bound_latitude_gt (Union[Unset, float]):
        location_south_bound_latitude_gte (Union[Unset, float]):
        location_south_bound_latitude_lt (Union[Unset, float]):
        location_south_bound_latitude_lte (Union[Unset, float]):
        location_south_bound_latitude_range (Union[Unset, list[float]]):
        location_west_bound_longitude (Union[Unset, float]):
        location_west_bound_longitude_gt (Union[Unset, float]):
        location_west_bound_longitude_gte (Union[Unset, float]):
        location_west_bound_longitude_lt (Union[Unset, float]):
        location_west_bound_longitude_lte (Union[Unset, float]):
        location_west_bound_longitude_range (Union[Unset, list[float]]):
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
        operation_time (Union[Unset, int]):
        operation_time_end_time (Union[Unset, datetime.datetime]):
        operation_time_end_time_gt (Union[Unset, datetime.datetime]):
        operation_time_end_time_gte (Union[Unset, datetime.datetime]):
        operation_time_end_time_lt (Union[Unset, datetime.datetime]):
        operation_time_end_time_lte (Union[Unset, datetime.datetime]):
        operation_time_end_time_range (Union[Unset, list[datetime.datetime]]):
        operation_time_gt (Union[Unset, int]):
        operation_time_gte (Union[Unset, int]):
        operation_time_in (Union[Unset, list[int]]):
        operation_time_isnull (Union[Unset, bool]):
        operation_time_lt (Union[Unset, int]):
        operation_time_lte (Union[Unset, int]):
        operation_time_ob_id (Union[Unset, int]):
        operation_time_ob_id_in (Union[Unset, list[int]]):
        operation_time_start_time (Union[Unset, datetime.datetime]):
        operation_time_start_time_gt (Union[Unset, datetime.datetime]):
        operation_time_start_time_gte (Union[Unset, datetime.datetime]):
        operation_time_start_time_lt (Union[Unset, datetime.datetime]):
        operation_time_start_time_lte (Union[Unset, datetime.datetime]):
        operation_time_start_time_range (Union[Unset, list[datetime.datetime]]):
        ordering (Union[Unset, str]):
        platform_field (Union[Unset, int]):
        platform_field_gt (Union[Unset, int]):
        platform_field_gte (Union[Unset, int]):
        platform_field_in (Union[Unset, list[int]]):
        platform_field_isnull (Union[Unset, bool]):
        platform_field_lt (Union[Unset, int]):
        platform_field_lte (Union[Unset, int]):
        platform_field_ob_id (Union[Unset, int]):
        platform_field_ob_id_in (Union[Unset, list[int]]):
        platform_field_uuid (Union[Unset, str]):
        platform_field_uuid_in (Union[Unset, list[str]]):
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
        status (Union[Unset, MposListStatus]):
        status_contains (Union[Unset, str]):
        status_endswith (Union[Unset, str]):
        status_gt (Union[Unset, str]):
        status_gte (Union[Unset, str]):
        status_icontains (Union[Unset, str]):
        status_iendswith (Union[Unset, str]):
        status_iexact (Union[Unset, str]):
        status_in (Union[Unset, list[str]]):
        status_iregex (Union[Unset, str]):
        status_isnull (Union[Unset, bool]):
        status_istartswith (Union[Unset, str]):
        status_lt (Union[Unset, str]):
        status_lte (Union[Unset, str]):
        status_range (Union[Unset, list[str]]):
        status_regex (Union[Unset, str]):
        status_startswith (Union[Unset, str]):
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
        PaginatedMobilePlatformOperationReadList
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
        child_operation=child_operation,
        child_operation_gt=child_operation_gt,
        child_operation_gte=child_operation_gte,
        child_operation_in=child_operation_in,
        child_operation_isnull=child_operation_isnull,
        child_operation_lt=child_operation_lt,
        child_operation_lte=child_operation_lte,
        limit=limit,
        location=location,
        location_east_bound_longitude=location_east_bound_longitude,
        location_east_bound_longitude_gt=location_east_bound_longitude_gt,
        location_east_bound_longitude_gte=location_east_bound_longitude_gte,
        location_east_bound_longitude_lt=location_east_bound_longitude_lt,
        location_east_bound_longitude_lte=location_east_bound_longitude_lte,
        location_east_bound_longitude_range=location_east_bound_longitude_range,
        location_gt=location_gt,
        location_gte=location_gte,
        location_in=location_in,
        location_isnull=location_isnull,
        location_lt=location_lt,
        location_lte=location_lte,
        location_north_bound_latitude=location_north_bound_latitude,
        location_north_bound_latitude_gt=location_north_bound_latitude_gt,
        location_north_bound_latitude_gte=location_north_bound_latitude_gte,
        location_north_bound_latitude_lt=location_north_bound_latitude_lt,
        location_north_bound_latitude_lte=location_north_bound_latitude_lte,
        location_north_bound_latitude_range=location_north_bound_latitude_range,
        location_ob_id=location_ob_id,
        location_ob_id_in=location_ob_id_in,
        location_south_bound_latitude=location_south_bound_latitude,
        location_south_bound_latitude_gt=location_south_bound_latitude_gt,
        location_south_bound_latitude_gte=location_south_bound_latitude_gte,
        location_south_bound_latitude_lt=location_south_bound_latitude_lt,
        location_south_bound_latitude_lte=location_south_bound_latitude_lte,
        location_south_bound_latitude_range=location_south_bound_latitude_range,
        location_west_bound_longitude=location_west_bound_longitude,
        location_west_bound_longitude_gt=location_west_bound_longitude_gt,
        location_west_bound_longitude_gte=location_west_bound_longitude_gte,
        location_west_bound_longitude_lt=location_west_bound_longitude_lt,
        location_west_bound_longitude_lte=location_west_bound_longitude_lte,
        location_west_bound_longitude_range=location_west_bound_longitude_range,
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
        operation_time=operation_time,
        operation_time_end_time=operation_time_end_time,
        operation_time_end_time_gt=operation_time_end_time_gt,
        operation_time_end_time_gte=operation_time_end_time_gte,
        operation_time_end_time_lt=operation_time_end_time_lt,
        operation_time_end_time_lte=operation_time_end_time_lte,
        operation_time_end_time_range=operation_time_end_time_range,
        operation_time_gt=operation_time_gt,
        operation_time_gte=operation_time_gte,
        operation_time_in=operation_time_in,
        operation_time_isnull=operation_time_isnull,
        operation_time_lt=operation_time_lt,
        operation_time_lte=operation_time_lte,
        operation_time_ob_id=operation_time_ob_id,
        operation_time_ob_id_in=operation_time_ob_id_in,
        operation_time_start_time=operation_time_start_time,
        operation_time_start_time_gt=operation_time_start_time_gt,
        operation_time_start_time_gte=operation_time_start_time_gte,
        operation_time_start_time_lt=operation_time_start_time_lt,
        operation_time_start_time_lte=operation_time_start_time_lte,
        operation_time_start_time_range=operation_time_start_time_range,
        ordering=ordering,
        platform_field=platform_field,
        platform_field_gt=platform_field_gt,
        platform_field_gte=platform_field_gte,
        platform_field_in=platform_field_in,
        platform_field_isnull=platform_field_isnull,
        platform_field_lt=platform_field_lt,
        platform_field_lte=platform_field_lte,
        platform_field_ob_id=platform_field_ob_id,
        platform_field_ob_id_in=platform_field_ob_id_in,
        platform_field_uuid=platform_field_uuid,
        platform_field_uuid_in=platform_field_uuid_in,
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
        status=status,
        status_contains=status_contains,
        status_endswith=status_endswith,
        status_gt=status_gt,
        status_gte=status_gte,
        status_icontains=status_icontains,
        status_iendswith=status_iendswith,
        status_iexact=status_iexact,
        status_in=status_in,
        status_iregex=status_iregex,
        status_isnull=status_isnull,
        status_istartswith=status_istartswith,
        status_lt=status_lt,
        status_lte=status_lte,
        status_range=status_range,
        status_regex=status_regex,
        status_startswith=status_startswith,
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
    child_operation: Union[Unset, int] = UNSET,
    child_operation_gt: Union[Unset, int] = UNSET,
    child_operation_gte: Union[Unset, int] = UNSET,
    child_operation_in: Union[Unset, list[int]] = UNSET,
    child_operation_isnull: Union[Unset, bool] = UNSET,
    child_operation_lt: Union[Unset, int] = UNSET,
    child_operation_lte: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, int] = UNSET,
    location_east_bound_longitude: Union[Unset, float] = UNSET,
    location_east_bound_longitude_gt: Union[Unset, float] = UNSET,
    location_east_bound_longitude_gte: Union[Unset, float] = UNSET,
    location_east_bound_longitude_lt: Union[Unset, float] = UNSET,
    location_east_bound_longitude_lte: Union[Unset, float] = UNSET,
    location_east_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    location_gt: Union[Unset, int] = UNSET,
    location_gte: Union[Unset, int] = UNSET,
    location_in: Union[Unset, list[int]] = UNSET,
    location_isnull: Union[Unset, bool] = UNSET,
    location_lt: Union[Unset, int] = UNSET,
    location_lte: Union[Unset, int] = UNSET,
    location_north_bound_latitude: Union[Unset, float] = UNSET,
    location_north_bound_latitude_gt: Union[Unset, float] = UNSET,
    location_north_bound_latitude_gte: Union[Unset, float] = UNSET,
    location_north_bound_latitude_lt: Union[Unset, float] = UNSET,
    location_north_bound_latitude_lte: Union[Unset, float] = UNSET,
    location_north_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    location_ob_id: Union[Unset, int] = UNSET,
    location_ob_id_in: Union[Unset, list[int]] = UNSET,
    location_south_bound_latitude: Union[Unset, float] = UNSET,
    location_south_bound_latitude_gt: Union[Unset, float] = UNSET,
    location_south_bound_latitude_gte: Union[Unset, float] = UNSET,
    location_south_bound_latitude_lt: Union[Unset, float] = UNSET,
    location_south_bound_latitude_lte: Union[Unset, float] = UNSET,
    location_south_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    location_west_bound_longitude: Union[Unset, float] = UNSET,
    location_west_bound_longitude_gt: Union[Unset, float] = UNSET,
    location_west_bound_longitude_gte: Union[Unset, float] = UNSET,
    location_west_bound_longitude_lt: Union[Unset, float] = UNSET,
    location_west_bound_longitude_lte: Union[Unset, float] = UNSET,
    location_west_bound_longitude_range: Union[Unset, list[float]] = UNSET,
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
    operation_time: Union[Unset, int] = UNSET,
    operation_time_end_time: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_gt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_gte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_lt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_lte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    operation_time_gt: Union[Unset, int] = UNSET,
    operation_time_gte: Union[Unset, int] = UNSET,
    operation_time_in: Union[Unset, list[int]] = UNSET,
    operation_time_isnull: Union[Unset, bool] = UNSET,
    operation_time_lt: Union[Unset, int] = UNSET,
    operation_time_lte: Union[Unset, int] = UNSET,
    operation_time_ob_id: Union[Unset, int] = UNSET,
    operation_time_ob_id_in: Union[Unset, list[int]] = UNSET,
    operation_time_start_time: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_gt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_gte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_lt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_lte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    platform_field: Union[Unset, int] = UNSET,
    platform_field_gt: Union[Unset, int] = UNSET,
    platform_field_gte: Union[Unset, int] = UNSET,
    platform_field_in: Union[Unset, list[int]] = UNSET,
    platform_field_isnull: Union[Unset, bool] = UNSET,
    platform_field_lt: Union[Unset, int] = UNSET,
    platform_field_lte: Union[Unset, int] = UNSET,
    platform_field_ob_id: Union[Unset, int] = UNSET,
    platform_field_ob_id_in: Union[Unset, list[int]] = UNSET,
    platform_field_uuid: Union[Unset, str] = UNSET,
    platform_field_uuid_in: Union[Unset, list[str]] = UNSET,
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
    status: Union[Unset, MposListStatus] = UNSET,
    status_contains: Union[Unset, str] = UNSET,
    status_endswith: Union[Unset, str] = UNSET,
    status_gt: Union[Unset, str] = UNSET,
    status_gte: Union[Unset, str] = UNSET,
    status_icontains: Union[Unset, str] = UNSET,
    status_iendswith: Union[Unset, str] = UNSET,
    status_iexact: Union[Unset, str] = UNSET,
    status_in: Union[Unset, list[str]] = UNSET,
    status_iregex: Union[Unset, str] = UNSET,
    status_isnull: Union[Unset, bool] = UNSET,
    status_istartswith: Union[Unset, str] = UNSET,
    status_lt: Union[Unset, str] = UNSET,
    status_lte: Union[Unset, str] = UNSET,
    status_range: Union[Unset, list[str]] = UNSET,
    status_regex: Union[Unset, str] = UNSET,
    status_startswith: Union[Unset, str] = UNSET,
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
) -> Response[PaginatedMobilePlatformOperationReadList]:
    """Get a list of Mobile Platform Operation objects.

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
        child_operation (Union[Unset, int]):
        child_operation_gt (Union[Unset, int]):
        child_operation_gte (Union[Unset, int]):
        child_operation_in (Union[Unset, list[int]]):
        child_operation_isnull (Union[Unset, bool]):
        child_operation_lt (Union[Unset, int]):
        child_operation_lte (Union[Unset, int]):
        limit (Union[Unset, int]):
        location (Union[Unset, int]):
        location_east_bound_longitude (Union[Unset, float]):
        location_east_bound_longitude_gt (Union[Unset, float]):
        location_east_bound_longitude_gte (Union[Unset, float]):
        location_east_bound_longitude_lt (Union[Unset, float]):
        location_east_bound_longitude_lte (Union[Unset, float]):
        location_east_bound_longitude_range (Union[Unset, list[float]]):
        location_gt (Union[Unset, int]):
        location_gte (Union[Unset, int]):
        location_in (Union[Unset, list[int]]):
        location_isnull (Union[Unset, bool]):
        location_lt (Union[Unset, int]):
        location_lte (Union[Unset, int]):
        location_north_bound_latitude (Union[Unset, float]):
        location_north_bound_latitude_gt (Union[Unset, float]):
        location_north_bound_latitude_gte (Union[Unset, float]):
        location_north_bound_latitude_lt (Union[Unset, float]):
        location_north_bound_latitude_lte (Union[Unset, float]):
        location_north_bound_latitude_range (Union[Unset, list[float]]):
        location_ob_id (Union[Unset, int]):
        location_ob_id_in (Union[Unset, list[int]]):
        location_south_bound_latitude (Union[Unset, float]):
        location_south_bound_latitude_gt (Union[Unset, float]):
        location_south_bound_latitude_gte (Union[Unset, float]):
        location_south_bound_latitude_lt (Union[Unset, float]):
        location_south_bound_latitude_lte (Union[Unset, float]):
        location_south_bound_latitude_range (Union[Unset, list[float]]):
        location_west_bound_longitude (Union[Unset, float]):
        location_west_bound_longitude_gt (Union[Unset, float]):
        location_west_bound_longitude_gte (Union[Unset, float]):
        location_west_bound_longitude_lt (Union[Unset, float]):
        location_west_bound_longitude_lte (Union[Unset, float]):
        location_west_bound_longitude_range (Union[Unset, list[float]]):
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
        operation_time (Union[Unset, int]):
        operation_time_end_time (Union[Unset, datetime.datetime]):
        operation_time_end_time_gt (Union[Unset, datetime.datetime]):
        operation_time_end_time_gte (Union[Unset, datetime.datetime]):
        operation_time_end_time_lt (Union[Unset, datetime.datetime]):
        operation_time_end_time_lte (Union[Unset, datetime.datetime]):
        operation_time_end_time_range (Union[Unset, list[datetime.datetime]]):
        operation_time_gt (Union[Unset, int]):
        operation_time_gte (Union[Unset, int]):
        operation_time_in (Union[Unset, list[int]]):
        operation_time_isnull (Union[Unset, bool]):
        operation_time_lt (Union[Unset, int]):
        operation_time_lte (Union[Unset, int]):
        operation_time_ob_id (Union[Unset, int]):
        operation_time_ob_id_in (Union[Unset, list[int]]):
        operation_time_start_time (Union[Unset, datetime.datetime]):
        operation_time_start_time_gt (Union[Unset, datetime.datetime]):
        operation_time_start_time_gte (Union[Unset, datetime.datetime]):
        operation_time_start_time_lt (Union[Unset, datetime.datetime]):
        operation_time_start_time_lte (Union[Unset, datetime.datetime]):
        operation_time_start_time_range (Union[Unset, list[datetime.datetime]]):
        ordering (Union[Unset, str]):
        platform_field (Union[Unset, int]):
        platform_field_gt (Union[Unset, int]):
        platform_field_gte (Union[Unset, int]):
        platform_field_in (Union[Unset, list[int]]):
        platform_field_isnull (Union[Unset, bool]):
        platform_field_lt (Union[Unset, int]):
        platform_field_lte (Union[Unset, int]):
        platform_field_ob_id (Union[Unset, int]):
        platform_field_ob_id_in (Union[Unset, list[int]]):
        platform_field_uuid (Union[Unset, str]):
        platform_field_uuid_in (Union[Unset, list[str]]):
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
        status (Union[Unset, MposListStatus]):
        status_contains (Union[Unset, str]):
        status_endswith (Union[Unset, str]):
        status_gt (Union[Unset, str]):
        status_gte (Union[Unset, str]):
        status_icontains (Union[Unset, str]):
        status_iendswith (Union[Unset, str]):
        status_iexact (Union[Unset, str]):
        status_in (Union[Unset, list[str]]):
        status_iregex (Union[Unset, str]):
        status_isnull (Union[Unset, bool]):
        status_istartswith (Union[Unset, str]):
        status_lt (Union[Unset, str]):
        status_lte (Union[Unset, str]):
        status_range (Union[Unset, list[str]]):
        status_regex (Union[Unset, str]):
        status_startswith (Union[Unset, str]):
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
        Response[PaginatedMobilePlatformOperationReadList]
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
        child_operation=child_operation,
        child_operation_gt=child_operation_gt,
        child_operation_gte=child_operation_gte,
        child_operation_in=child_operation_in,
        child_operation_isnull=child_operation_isnull,
        child_operation_lt=child_operation_lt,
        child_operation_lte=child_operation_lte,
        limit=limit,
        location=location,
        location_east_bound_longitude=location_east_bound_longitude,
        location_east_bound_longitude_gt=location_east_bound_longitude_gt,
        location_east_bound_longitude_gte=location_east_bound_longitude_gte,
        location_east_bound_longitude_lt=location_east_bound_longitude_lt,
        location_east_bound_longitude_lte=location_east_bound_longitude_lte,
        location_east_bound_longitude_range=location_east_bound_longitude_range,
        location_gt=location_gt,
        location_gte=location_gte,
        location_in=location_in,
        location_isnull=location_isnull,
        location_lt=location_lt,
        location_lte=location_lte,
        location_north_bound_latitude=location_north_bound_latitude,
        location_north_bound_latitude_gt=location_north_bound_latitude_gt,
        location_north_bound_latitude_gte=location_north_bound_latitude_gte,
        location_north_bound_latitude_lt=location_north_bound_latitude_lt,
        location_north_bound_latitude_lte=location_north_bound_latitude_lte,
        location_north_bound_latitude_range=location_north_bound_latitude_range,
        location_ob_id=location_ob_id,
        location_ob_id_in=location_ob_id_in,
        location_south_bound_latitude=location_south_bound_latitude,
        location_south_bound_latitude_gt=location_south_bound_latitude_gt,
        location_south_bound_latitude_gte=location_south_bound_latitude_gte,
        location_south_bound_latitude_lt=location_south_bound_latitude_lt,
        location_south_bound_latitude_lte=location_south_bound_latitude_lte,
        location_south_bound_latitude_range=location_south_bound_latitude_range,
        location_west_bound_longitude=location_west_bound_longitude,
        location_west_bound_longitude_gt=location_west_bound_longitude_gt,
        location_west_bound_longitude_gte=location_west_bound_longitude_gte,
        location_west_bound_longitude_lt=location_west_bound_longitude_lt,
        location_west_bound_longitude_lte=location_west_bound_longitude_lte,
        location_west_bound_longitude_range=location_west_bound_longitude_range,
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
        operation_time=operation_time,
        operation_time_end_time=operation_time_end_time,
        operation_time_end_time_gt=operation_time_end_time_gt,
        operation_time_end_time_gte=operation_time_end_time_gte,
        operation_time_end_time_lt=operation_time_end_time_lt,
        operation_time_end_time_lte=operation_time_end_time_lte,
        operation_time_end_time_range=operation_time_end_time_range,
        operation_time_gt=operation_time_gt,
        operation_time_gte=operation_time_gte,
        operation_time_in=operation_time_in,
        operation_time_isnull=operation_time_isnull,
        operation_time_lt=operation_time_lt,
        operation_time_lte=operation_time_lte,
        operation_time_ob_id=operation_time_ob_id,
        operation_time_ob_id_in=operation_time_ob_id_in,
        operation_time_start_time=operation_time_start_time,
        operation_time_start_time_gt=operation_time_start_time_gt,
        operation_time_start_time_gte=operation_time_start_time_gte,
        operation_time_start_time_lt=operation_time_start_time_lt,
        operation_time_start_time_lte=operation_time_start_time_lte,
        operation_time_start_time_range=operation_time_start_time_range,
        ordering=ordering,
        platform_field=platform_field,
        platform_field_gt=platform_field_gt,
        platform_field_gte=platform_field_gte,
        platform_field_in=platform_field_in,
        platform_field_isnull=platform_field_isnull,
        platform_field_lt=platform_field_lt,
        platform_field_lte=platform_field_lte,
        platform_field_ob_id=platform_field_ob_id,
        platform_field_ob_id_in=platform_field_ob_id_in,
        platform_field_uuid=platform_field_uuid,
        platform_field_uuid_in=platform_field_uuid_in,
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
        status=status,
        status_contains=status_contains,
        status_endswith=status_endswith,
        status_gt=status_gt,
        status_gte=status_gte,
        status_icontains=status_icontains,
        status_iendswith=status_iendswith,
        status_iexact=status_iexact,
        status_in=status_in,
        status_iregex=status_iregex,
        status_isnull=status_isnull,
        status_istartswith=status_istartswith,
        status_lt=status_lt,
        status_lte=status_lte,
        status_range=status_range,
        status_regex=status_regex,
        status_startswith=status_startswith,
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
    child_operation: Union[Unset, int] = UNSET,
    child_operation_gt: Union[Unset, int] = UNSET,
    child_operation_gte: Union[Unset, int] = UNSET,
    child_operation_in: Union[Unset, list[int]] = UNSET,
    child_operation_isnull: Union[Unset, bool] = UNSET,
    child_operation_lt: Union[Unset, int] = UNSET,
    child_operation_lte: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    location: Union[Unset, int] = UNSET,
    location_east_bound_longitude: Union[Unset, float] = UNSET,
    location_east_bound_longitude_gt: Union[Unset, float] = UNSET,
    location_east_bound_longitude_gte: Union[Unset, float] = UNSET,
    location_east_bound_longitude_lt: Union[Unset, float] = UNSET,
    location_east_bound_longitude_lte: Union[Unset, float] = UNSET,
    location_east_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    location_gt: Union[Unset, int] = UNSET,
    location_gte: Union[Unset, int] = UNSET,
    location_in: Union[Unset, list[int]] = UNSET,
    location_isnull: Union[Unset, bool] = UNSET,
    location_lt: Union[Unset, int] = UNSET,
    location_lte: Union[Unset, int] = UNSET,
    location_north_bound_latitude: Union[Unset, float] = UNSET,
    location_north_bound_latitude_gt: Union[Unset, float] = UNSET,
    location_north_bound_latitude_gte: Union[Unset, float] = UNSET,
    location_north_bound_latitude_lt: Union[Unset, float] = UNSET,
    location_north_bound_latitude_lte: Union[Unset, float] = UNSET,
    location_north_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    location_ob_id: Union[Unset, int] = UNSET,
    location_ob_id_in: Union[Unset, list[int]] = UNSET,
    location_south_bound_latitude: Union[Unset, float] = UNSET,
    location_south_bound_latitude_gt: Union[Unset, float] = UNSET,
    location_south_bound_latitude_gte: Union[Unset, float] = UNSET,
    location_south_bound_latitude_lt: Union[Unset, float] = UNSET,
    location_south_bound_latitude_lte: Union[Unset, float] = UNSET,
    location_south_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    location_west_bound_longitude: Union[Unset, float] = UNSET,
    location_west_bound_longitude_gt: Union[Unset, float] = UNSET,
    location_west_bound_longitude_gte: Union[Unset, float] = UNSET,
    location_west_bound_longitude_lt: Union[Unset, float] = UNSET,
    location_west_bound_longitude_lte: Union[Unset, float] = UNSET,
    location_west_bound_longitude_range: Union[Unset, list[float]] = UNSET,
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
    operation_time: Union[Unset, int] = UNSET,
    operation_time_end_time: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_gt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_gte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_lt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_lte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_end_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    operation_time_gt: Union[Unset, int] = UNSET,
    operation_time_gte: Union[Unset, int] = UNSET,
    operation_time_in: Union[Unset, list[int]] = UNSET,
    operation_time_isnull: Union[Unset, bool] = UNSET,
    operation_time_lt: Union[Unset, int] = UNSET,
    operation_time_lte: Union[Unset, int] = UNSET,
    operation_time_ob_id: Union[Unset, int] = UNSET,
    operation_time_ob_id_in: Union[Unset, list[int]] = UNSET,
    operation_time_start_time: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_gt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_gte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_lt: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_lte: Union[Unset, datetime.datetime] = UNSET,
    operation_time_start_time_range: Union[Unset, list[datetime.datetime]] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    platform_field: Union[Unset, int] = UNSET,
    platform_field_gt: Union[Unset, int] = UNSET,
    platform_field_gte: Union[Unset, int] = UNSET,
    platform_field_in: Union[Unset, list[int]] = UNSET,
    platform_field_isnull: Union[Unset, bool] = UNSET,
    platform_field_lt: Union[Unset, int] = UNSET,
    platform_field_lte: Union[Unset, int] = UNSET,
    platform_field_ob_id: Union[Unset, int] = UNSET,
    platform_field_ob_id_in: Union[Unset, list[int]] = UNSET,
    platform_field_uuid: Union[Unset, str] = UNSET,
    platform_field_uuid_in: Union[Unset, list[str]] = UNSET,
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
    status: Union[Unset, MposListStatus] = UNSET,
    status_contains: Union[Unset, str] = UNSET,
    status_endswith: Union[Unset, str] = UNSET,
    status_gt: Union[Unset, str] = UNSET,
    status_gte: Union[Unset, str] = UNSET,
    status_icontains: Union[Unset, str] = UNSET,
    status_iendswith: Union[Unset, str] = UNSET,
    status_iexact: Union[Unset, str] = UNSET,
    status_in: Union[Unset, list[str]] = UNSET,
    status_iregex: Union[Unset, str] = UNSET,
    status_isnull: Union[Unset, bool] = UNSET,
    status_istartswith: Union[Unset, str] = UNSET,
    status_lt: Union[Unset, str] = UNSET,
    status_lte: Union[Unset, str] = UNSET,
    status_range: Union[Unset, list[str]] = UNSET,
    status_regex: Union[Unset, str] = UNSET,
    status_startswith: Union[Unset, str] = UNSET,
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
) -> Optional[PaginatedMobilePlatformOperationReadList]:
    """Get a list of Mobile Platform Operation objects.

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
        child_operation (Union[Unset, int]):
        child_operation_gt (Union[Unset, int]):
        child_operation_gte (Union[Unset, int]):
        child_operation_in (Union[Unset, list[int]]):
        child_operation_isnull (Union[Unset, bool]):
        child_operation_lt (Union[Unset, int]):
        child_operation_lte (Union[Unset, int]):
        limit (Union[Unset, int]):
        location (Union[Unset, int]):
        location_east_bound_longitude (Union[Unset, float]):
        location_east_bound_longitude_gt (Union[Unset, float]):
        location_east_bound_longitude_gte (Union[Unset, float]):
        location_east_bound_longitude_lt (Union[Unset, float]):
        location_east_bound_longitude_lte (Union[Unset, float]):
        location_east_bound_longitude_range (Union[Unset, list[float]]):
        location_gt (Union[Unset, int]):
        location_gte (Union[Unset, int]):
        location_in (Union[Unset, list[int]]):
        location_isnull (Union[Unset, bool]):
        location_lt (Union[Unset, int]):
        location_lte (Union[Unset, int]):
        location_north_bound_latitude (Union[Unset, float]):
        location_north_bound_latitude_gt (Union[Unset, float]):
        location_north_bound_latitude_gte (Union[Unset, float]):
        location_north_bound_latitude_lt (Union[Unset, float]):
        location_north_bound_latitude_lte (Union[Unset, float]):
        location_north_bound_latitude_range (Union[Unset, list[float]]):
        location_ob_id (Union[Unset, int]):
        location_ob_id_in (Union[Unset, list[int]]):
        location_south_bound_latitude (Union[Unset, float]):
        location_south_bound_latitude_gt (Union[Unset, float]):
        location_south_bound_latitude_gte (Union[Unset, float]):
        location_south_bound_latitude_lt (Union[Unset, float]):
        location_south_bound_latitude_lte (Union[Unset, float]):
        location_south_bound_latitude_range (Union[Unset, list[float]]):
        location_west_bound_longitude (Union[Unset, float]):
        location_west_bound_longitude_gt (Union[Unset, float]):
        location_west_bound_longitude_gte (Union[Unset, float]):
        location_west_bound_longitude_lt (Union[Unset, float]):
        location_west_bound_longitude_lte (Union[Unset, float]):
        location_west_bound_longitude_range (Union[Unset, list[float]]):
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
        operation_time (Union[Unset, int]):
        operation_time_end_time (Union[Unset, datetime.datetime]):
        operation_time_end_time_gt (Union[Unset, datetime.datetime]):
        operation_time_end_time_gte (Union[Unset, datetime.datetime]):
        operation_time_end_time_lt (Union[Unset, datetime.datetime]):
        operation_time_end_time_lte (Union[Unset, datetime.datetime]):
        operation_time_end_time_range (Union[Unset, list[datetime.datetime]]):
        operation_time_gt (Union[Unset, int]):
        operation_time_gte (Union[Unset, int]):
        operation_time_in (Union[Unset, list[int]]):
        operation_time_isnull (Union[Unset, bool]):
        operation_time_lt (Union[Unset, int]):
        operation_time_lte (Union[Unset, int]):
        operation_time_ob_id (Union[Unset, int]):
        operation_time_ob_id_in (Union[Unset, list[int]]):
        operation_time_start_time (Union[Unset, datetime.datetime]):
        operation_time_start_time_gt (Union[Unset, datetime.datetime]):
        operation_time_start_time_gte (Union[Unset, datetime.datetime]):
        operation_time_start_time_lt (Union[Unset, datetime.datetime]):
        operation_time_start_time_lte (Union[Unset, datetime.datetime]):
        operation_time_start_time_range (Union[Unset, list[datetime.datetime]]):
        ordering (Union[Unset, str]):
        platform_field (Union[Unset, int]):
        platform_field_gt (Union[Unset, int]):
        platform_field_gte (Union[Unset, int]):
        platform_field_in (Union[Unset, list[int]]):
        platform_field_isnull (Union[Unset, bool]):
        platform_field_lt (Union[Unset, int]):
        platform_field_lte (Union[Unset, int]):
        platform_field_ob_id (Union[Unset, int]):
        platform_field_ob_id_in (Union[Unset, list[int]]):
        platform_field_uuid (Union[Unset, str]):
        platform_field_uuid_in (Union[Unset, list[str]]):
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
        status (Union[Unset, MposListStatus]):
        status_contains (Union[Unset, str]):
        status_endswith (Union[Unset, str]):
        status_gt (Union[Unset, str]):
        status_gte (Union[Unset, str]):
        status_icontains (Union[Unset, str]):
        status_iendswith (Union[Unset, str]):
        status_iexact (Union[Unset, str]):
        status_in (Union[Unset, list[str]]):
        status_iregex (Union[Unset, str]):
        status_isnull (Union[Unset, bool]):
        status_istartswith (Union[Unset, str]):
        status_lt (Union[Unset, str]):
        status_lte (Union[Unset, str]):
        status_range (Union[Unset, list[str]]):
        status_regex (Union[Unset, str]):
        status_startswith (Union[Unset, str]):
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
        PaginatedMobilePlatformOperationReadList
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
            child_operation=child_operation,
            child_operation_gt=child_operation_gt,
            child_operation_gte=child_operation_gte,
            child_operation_in=child_operation_in,
            child_operation_isnull=child_operation_isnull,
            child_operation_lt=child_operation_lt,
            child_operation_lte=child_operation_lte,
            limit=limit,
            location=location,
            location_east_bound_longitude=location_east_bound_longitude,
            location_east_bound_longitude_gt=location_east_bound_longitude_gt,
            location_east_bound_longitude_gte=location_east_bound_longitude_gte,
            location_east_bound_longitude_lt=location_east_bound_longitude_lt,
            location_east_bound_longitude_lte=location_east_bound_longitude_lte,
            location_east_bound_longitude_range=location_east_bound_longitude_range,
            location_gt=location_gt,
            location_gte=location_gte,
            location_in=location_in,
            location_isnull=location_isnull,
            location_lt=location_lt,
            location_lte=location_lte,
            location_north_bound_latitude=location_north_bound_latitude,
            location_north_bound_latitude_gt=location_north_bound_latitude_gt,
            location_north_bound_latitude_gte=location_north_bound_latitude_gte,
            location_north_bound_latitude_lt=location_north_bound_latitude_lt,
            location_north_bound_latitude_lte=location_north_bound_latitude_lte,
            location_north_bound_latitude_range=location_north_bound_latitude_range,
            location_ob_id=location_ob_id,
            location_ob_id_in=location_ob_id_in,
            location_south_bound_latitude=location_south_bound_latitude,
            location_south_bound_latitude_gt=location_south_bound_latitude_gt,
            location_south_bound_latitude_gte=location_south_bound_latitude_gte,
            location_south_bound_latitude_lt=location_south_bound_latitude_lt,
            location_south_bound_latitude_lte=location_south_bound_latitude_lte,
            location_south_bound_latitude_range=location_south_bound_latitude_range,
            location_west_bound_longitude=location_west_bound_longitude,
            location_west_bound_longitude_gt=location_west_bound_longitude_gt,
            location_west_bound_longitude_gte=location_west_bound_longitude_gte,
            location_west_bound_longitude_lt=location_west_bound_longitude_lt,
            location_west_bound_longitude_lte=location_west_bound_longitude_lte,
            location_west_bound_longitude_range=location_west_bound_longitude_range,
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
            operation_time=operation_time,
            operation_time_end_time=operation_time_end_time,
            operation_time_end_time_gt=operation_time_end_time_gt,
            operation_time_end_time_gte=operation_time_end_time_gte,
            operation_time_end_time_lt=operation_time_end_time_lt,
            operation_time_end_time_lte=operation_time_end_time_lte,
            operation_time_end_time_range=operation_time_end_time_range,
            operation_time_gt=operation_time_gt,
            operation_time_gte=operation_time_gte,
            operation_time_in=operation_time_in,
            operation_time_isnull=operation_time_isnull,
            operation_time_lt=operation_time_lt,
            operation_time_lte=operation_time_lte,
            operation_time_ob_id=operation_time_ob_id,
            operation_time_ob_id_in=operation_time_ob_id_in,
            operation_time_start_time=operation_time_start_time,
            operation_time_start_time_gt=operation_time_start_time_gt,
            operation_time_start_time_gte=operation_time_start_time_gte,
            operation_time_start_time_lt=operation_time_start_time_lt,
            operation_time_start_time_lte=operation_time_start_time_lte,
            operation_time_start_time_range=operation_time_start_time_range,
            ordering=ordering,
            platform_field=platform_field,
            platform_field_gt=platform_field_gt,
            platform_field_gte=platform_field_gte,
            platform_field_in=platform_field_in,
            platform_field_isnull=platform_field_isnull,
            platform_field_lt=platform_field_lt,
            platform_field_lte=platform_field_lte,
            platform_field_ob_id=platform_field_ob_id,
            platform_field_ob_id_in=platform_field_ob_id_in,
            platform_field_uuid=platform_field_uuid,
            platform_field_uuid_in=platform_field_uuid_in,
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
            status=status,
            status_contains=status_contains,
            status_endswith=status_endswith,
            status_gt=status_gt,
            status_gte=status_gte,
            status_icontains=status_icontains,
            status_iendswith=status_iendswith,
            status_iexact=status_iexact,
            status_in=status_in,
            status_iregex=status_iregex,
            status_isnull=status_isnull,
            status_istartswith=status_istartswith,
            status_lt=status_lt,
            status_lte=status_lte,
            status_range=status_range,
            status_regex=status_regex,
            status_startswith=status_startswith,
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
