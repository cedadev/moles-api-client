import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mpos_list_status import MposListStatus
from ...models.paginated_mobile_platform_operation_read_list import PaginatedMobilePlatformOperationReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    child_operation: int | Unset = UNSET,
    child_operation_in: list[int] | Unset = UNSET,
    child_operation_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    location: int | Unset = UNSET,
    location_east_bound_longitude: float | Unset = UNSET,
    location_east_bound_longitude_gt: float | Unset = UNSET,
    location_east_bound_longitude_gte: float | Unset = UNSET,
    location_east_bound_longitude_lt: float | Unset = UNSET,
    location_east_bound_longitude_lte: float | Unset = UNSET,
    location_east_bound_longitude_range: list[float] | Unset = UNSET,
    location_in: list[int] | Unset = UNSET,
    location_isnull: bool | Unset = UNSET,
    location_north_bound_latitude: float | Unset = UNSET,
    location_north_bound_latitude_gt: float | Unset = UNSET,
    location_north_bound_latitude_gte: float | Unset = UNSET,
    location_north_bound_latitude_lt: float | Unset = UNSET,
    location_north_bound_latitude_lte: float | Unset = UNSET,
    location_north_bound_latitude_range: list[float] | Unset = UNSET,
    location_ob_id: int | Unset = UNSET,
    location_ob_id_in: list[int] | Unset = UNSET,
    location_south_bound_latitude: float | Unset = UNSET,
    location_south_bound_latitude_gt: float | Unset = UNSET,
    location_south_bound_latitude_gte: float | Unset = UNSET,
    location_south_bound_latitude_lt: float | Unset = UNSET,
    location_south_bound_latitude_lte: float | Unset = UNSET,
    location_south_bound_latitude_range: list[float] | Unset = UNSET,
    location_west_bound_longitude: float | Unset = UNSET,
    location_west_bound_longitude_gt: float | Unset = UNSET,
    location_west_bound_longitude_gte: float | Unset = UNSET,
    location_west_bound_longitude_lt: float | Unset = UNSET,
    location_west_bound_longitude_lte: float | Unset = UNSET,
    location_west_bound_longitude_range: list[float] | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    operation_time: int | Unset = UNSET,
    operation_time_end_time: datetime.datetime | Unset = UNSET,
    operation_time_end_time_gt: datetime.datetime | Unset = UNSET,
    operation_time_end_time_gte: datetime.datetime | Unset = UNSET,
    operation_time_end_time_lt: datetime.datetime | Unset = UNSET,
    operation_time_end_time_lte: datetime.datetime | Unset = UNSET,
    operation_time_end_time_range: list[datetime.datetime] | Unset = UNSET,
    operation_time_in: list[int] | Unset = UNSET,
    operation_time_isnull: bool | Unset = UNSET,
    operation_time_ob_id: int | Unset = UNSET,
    operation_time_ob_id_in: list[int] | Unset = UNSET,
    operation_time_start_time: datetime.datetime | Unset = UNSET,
    operation_time_start_time_gt: datetime.datetime | Unset = UNSET,
    operation_time_start_time_gte: datetime.datetime | Unset = UNSET,
    operation_time_start_time_lt: datetime.datetime | Unset = UNSET,
    operation_time_start_time_lte: datetime.datetime | Unset = UNSET,
    operation_time_start_time_range: list[datetime.datetime] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform_field: int | Unset = UNSET,
    platform_field_in: list[int] | Unset = UNSET,
    platform_field_isnull: bool | Unset = UNSET,
    platform_field_ob_id: int | Unset = UNSET,
    platform_field_ob_id_in: list[int] | Unset = UNSET,
    platform_field_uuid: str | Unset = UNSET,
    platform_field_uuid_in: list[str] | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    status: MposListStatus | Unset = UNSET,
    status_contains: str | Unset = UNSET,
    status_endswith: str | Unset = UNSET,
    status_gt: str | Unset = UNSET,
    status_gte: str | Unset = UNSET,
    status_icontains: str | Unset = UNSET,
    status_iendswith: str | Unset = UNSET,
    status_iexact: str | Unset = UNSET,
    status_in: list[str] | Unset = UNSET,
    status_iregex: str | Unset = UNSET,
    status_isnull: bool | Unset = UNSET,
    status_istartswith: str | Unset = UNSET,
    status_lt: str | Unset = UNSET,
    status_lte: str | Unset = UNSET,
    status_range: list[str] | Unset = UNSET,
    status_regex: str | Unset = UNSET,
    status_startswith: str | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
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

    json_abstract_in: list[str] | Unset = UNSET
    if not isinstance(abstract_in, Unset):
        json_abstract_in = abstract_in

    params["abstract__in"] = json_abstract_in

    params["abstract__iregex"] = abstract_iregex

    params["abstract__isnull"] = abstract_isnull

    params["abstract__istartswith"] = abstract_istartswith

    params["abstract__lt"] = abstract_lt

    params["abstract__lte"] = abstract_lte

    json_abstract_range: list[str] | Unset = UNSET
    if not isinstance(abstract_range, Unset):
        json_abstract_range = abstract_range

    params["abstract__range"] = json_abstract_range

    params["abstract__regex"] = abstract_regex

    params["abstract__startswith"] = abstract_startswith

    json_acquisition: list[int] | Unset = UNSET
    if not isinstance(acquisition, Unset):
        json_acquisition = acquisition

    params["acquisition"] = json_acquisition

    json_acquisition_in: list[int] | Unset = UNSET
    if not isinstance(acquisition_in, Unset):
        json_acquisition_in = acquisition_in

    params["acquisition__in"] = json_acquisition_in

    params["acquisition__isnull"] = acquisition_isnull

    params["childOperation"] = child_operation

    json_child_operation_in: list[int] | Unset = UNSET
    if not isinstance(child_operation_in, Unset):
        json_child_operation_in = child_operation_in

    params["childOperation__in"] = json_child_operation_in

    params["childOperation__isnull"] = child_operation_isnull

    json_identifier: list[int] | Unset = UNSET
    if not isinstance(identifier, Unset):
        json_identifier = identifier

    params["identifier"] = json_identifier

    json_identifier_in: list[int] | Unset = UNSET
    if not isinstance(identifier_in, Unset):
        json_identifier_in = identifier_in

    params["identifier__in"] = json_identifier_in

    params["identifier__isnull"] = identifier_isnull

    params["limit"] = limit

    params["location"] = location

    params["location__eastBoundLongitude"] = location_east_bound_longitude

    params["location__eastBoundLongitude__gt"] = location_east_bound_longitude_gt

    params["location__eastBoundLongitude__gte"] = location_east_bound_longitude_gte

    params["location__eastBoundLongitude__lt"] = location_east_bound_longitude_lt

    params["location__eastBoundLongitude__lte"] = location_east_bound_longitude_lte

    json_location_east_bound_longitude_range: list[float] | Unset = UNSET
    if not isinstance(location_east_bound_longitude_range, Unset):
        json_location_east_bound_longitude_range = location_east_bound_longitude_range

    params["location__eastBoundLongitude__range"] = json_location_east_bound_longitude_range

    json_location_in: list[int] | Unset = UNSET
    if not isinstance(location_in, Unset):
        json_location_in = location_in

    params["location__in"] = json_location_in

    params["location__isnull"] = location_isnull

    params["location__northBoundLatitude"] = location_north_bound_latitude

    params["location__northBoundLatitude__gt"] = location_north_bound_latitude_gt

    params["location__northBoundLatitude__gte"] = location_north_bound_latitude_gte

    params["location__northBoundLatitude__lt"] = location_north_bound_latitude_lt

    params["location__northBoundLatitude__lte"] = location_north_bound_latitude_lte

    json_location_north_bound_latitude_range: list[float] | Unset = UNSET
    if not isinstance(location_north_bound_latitude_range, Unset):
        json_location_north_bound_latitude_range = location_north_bound_latitude_range

    params["location__northBoundLatitude__range"] = json_location_north_bound_latitude_range

    params["location__ob_id"] = location_ob_id

    json_location_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(location_ob_id_in, Unset):
        json_location_ob_id_in = location_ob_id_in

    params["location__ob_id__in"] = json_location_ob_id_in

    params["location__southBoundLatitude"] = location_south_bound_latitude

    params["location__southBoundLatitude__gt"] = location_south_bound_latitude_gt

    params["location__southBoundLatitude__gte"] = location_south_bound_latitude_gte

    params["location__southBoundLatitude__lt"] = location_south_bound_latitude_lt

    params["location__southBoundLatitude__lte"] = location_south_bound_latitude_lte

    json_location_south_bound_latitude_range: list[float] | Unset = UNSET
    if not isinstance(location_south_bound_latitude_range, Unset):
        json_location_south_bound_latitude_range = location_south_bound_latitude_range

    params["location__southBoundLatitude__range"] = json_location_south_bound_latitude_range

    params["location__westBoundLongitude"] = location_west_bound_longitude

    params["location__westBoundLongitude__gt"] = location_west_bound_longitude_gt

    params["location__westBoundLongitude__gte"] = location_west_bound_longitude_gte

    params["location__westBoundLongitude__lt"] = location_west_bound_longitude_lt

    params["location__westBoundLongitude__lte"] = location_west_bound_longitude_lte

    json_location_west_bound_longitude_range: list[float] | Unset = UNSET
    if not isinstance(location_west_bound_longitude_range, Unset):
        json_location_west_bound_longitude_range = location_west_bound_longitude_range

    params["location__westBoundLongitude__range"] = json_location_west_bound_longitude_range

    json_migrationproperty: list[int] | Unset = UNSET
    if not isinstance(migrationproperty, Unset):
        json_migrationproperty = migrationproperty

    params["migrationproperty"] = json_migrationproperty

    json_migrationproperty_in: list[int] | Unset = UNSET
    if not isinstance(migrationproperty_in, Unset):
        json_migrationproperty_in = migrationproperty_in

    params["migrationproperty__in"] = json_migrationproperty_in

    params["migrationproperty__isnull"] = migrationproperty_isnull

    json_mobileplatformoperation: list[int] | Unset = UNSET
    if not isinstance(mobileplatformoperation, Unset):
        json_mobileplatformoperation = mobileplatformoperation

    params["mobileplatformoperation"] = json_mobileplatformoperation

    json_mobileplatformoperation_in: list[int] | Unset = UNSET
    if not isinstance(mobileplatformoperation_in, Unset):
        json_mobileplatformoperation_in = mobileplatformoperation_in

    params["mobileplatformoperation__in"] = json_mobileplatformoperation_in

    params["mobileplatformoperation__isnull"] = mobileplatformoperation_isnull

    json_note: list[int] | Unset = UNSET
    if not isinstance(note, Unset):
        json_note = note

    params["note"] = json_note

    json_note_in: list[int] | Unset = UNSET
    if not isinstance(note_in, Unset):
        json_note_in = note_in

    params["note__in"] = json_note_in

    params["note__isnull"] = note_isnull

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

    params["offset"] = offset

    json_onlineresource: list[int] | Unset = UNSET
    if not isinstance(onlineresource, Unset):
        json_onlineresource = onlineresource

    params["onlineresource"] = json_onlineresource

    json_onlineresource_in: list[int] | Unset = UNSET
    if not isinstance(onlineresource_in, Unset):
        json_onlineresource_in = onlineresource_in

    params["onlineresource__in"] = json_onlineresource_in

    params["onlineresource__isnull"] = onlineresource_isnull

    params["operationTime"] = operation_time

    json_operation_time_end_time: str | Unset = UNSET
    if not isinstance(operation_time_end_time, Unset):
        json_operation_time_end_time = operation_time_end_time.isoformat()
    params["operationTime__endTime"] = json_operation_time_end_time

    json_operation_time_end_time_gt: str | Unset = UNSET
    if not isinstance(operation_time_end_time_gt, Unset):
        json_operation_time_end_time_gt = operation_time_end_time_gt.isoformat()
    params["operationTime__endTime__gt"] = json_operation_time_end_time_gt

    json_operation_time_end_time_gte: str | Unset = UNSET
    if not isinstance(operation_time_end_time_gte, Unset):
        json_operation_time_end_time_gte = operation_time_end_time_gte.isoformat()
    params["operationTime__endTime__gte"] = json_operation_time_end_time_gte

    json_operation_time_end_time_lt: str | Unset = UNSET
    if not isinstance(operation_time_end_time_lt, Unset):
        json_operation_time_end_time_lt = operation_time_end_time_lt.isoformat()
    params["operationTime__endTime__lt"] = json_operation_time_end_time_lt

    json_operation_time_end_time_lte: str | Unset = UNSET
    if not isinstance(operation_time_end_time_lte, Unset):
        json_operation_time_end_time_lte = operation_time_end_time_lte.isoformat()
    params["operationTime__endTime__lte"] = json_operation_time_end_time_lte

    json_operation_time_end_time_range: list[str] | Unset = UNSET
    if not isinstance(operation_time_end_time_range, Unset):
        json_operation_time_end_time_range = []
        for operation_time_end_time_range_item_data in operation_time_end_time_range:
            operation_time_end_time_range_item = operation_time_end_time_range_item_data.isoformat()
            json_operation_time_end_time_range.append(operation_time_end_time_range_item)

    params["operationTime__endTime__range"] = json_operation_time_end_time_range

    json_operation_time_in: list[int] | Unset = UNSET
    if not isinstance(operation_time_in, Unset):
        json_operation_time_in = operation_time_in

    params["operationTime__in"] = json_operation_time_in

    params["operationTime__isnull"] = operation_time_isnull

    params["operationTime__ob_id"] = operation_time_ob_id

    json_operation_time_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(operation_time_ob_id_in, Unset):
        json_operation_time_ob_id_in = operation_time_ob_id_in

    params["operationTime__ob_id__in"] = json_operation_time_ob_id_in

    json_operation_time_start_time: str | Unset = UNSET
    if not isinstance(operation_time_start_time, Unset):
        json_operation_time_start_time = operation_time_start_time.isoformat()
    params["operationTime__startTime"] = json_operation_time_start_time

    json_operation_time_start_time_gt: str | Unset = UNSET
    if not isinstance(operation_time_start_time_gt, Unset):
        json_operation_time_start_time_gt = operation_time_start_time_gt.isoformat()
    params["operationTime__startTime__gt"] = json_operation_time_start_time_gt

    json_operation_time_start_time_gte: str | Unset = UNSET
    if not isinstance(operation_time_start_time_gte, Unset):
        json_operation_time_start_time_gte = operation_time_start_time_gte.isoformat()
    params["operationTime__startTime__gte"] = json_operation_time_start_time_gte

    json_operation_time_start_time_lt: str | Unset = UNSET
    if not isinstance(operation_time_start_time_lt, Unset):
        json_operation_time_start_time_lt = operation_time_start_time_lt.isoformat()
    params["operationTime__startTime__lt"] = json_operation_time_start_time_lt

    json_operation_time_start_time_lte: str | Unset = UNSET
    if not isinstance(operation_time_start_time_lte, Unset):
        json_operation_time_start_time_lte = operation_time_start_time_lte.isoformat()
    params["operationTime__startTime__lte"] = json_operation_time_start_time_lte

    json_operation_time_start_time_range: list[str] | Unset = UNSET
    if not isinstance(operation_time_start_time_range, Unset):
        json_operation_time_start_time_range = []
        for operation_time_start_time_range_item_data in operation_time_start_time_range:
            operation_time_start_time_range_item = operation_time_start_time_range_item_data.isoformat()
            json_operation_time_start_time_range.append(operation_time_start_time_range_item)

    params["operationTime__startTime__range"] = json_operation_time_start_time_range

    params["ordering"] = ordering

    params["platform_field"] = platform_field

    json_platform_field_in: list[int] | Unset = UNSET
    if not isinstance(platform_field_in, Unset):
        json_platform_field_in = platform_field_in

    params["platform_field__in"] = json_platform_field_in

    params["platform_field__isnull"] = platform_field_isnull

    params["platform_field__ob_id"] = platform_field_ob_id

    json_platform_field_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(platform_field_ob_id_in, Unset):
        json_platform_field_ob_id_in = platform_field_ob_id_in

    params["platform_field__ob_id__in"] = json_platform_field_ob_id_in

    params["platform_field__uuid"] = platform_field_uuid

    json_platform_field_uuid_in: list[str] | Unset = UNSET
    if not isinstance(platform_field_uuid_in, Unset):
        json_platform_field_uuid_in = platform_field_uuid_in

    params["platform_field__uuid__in"] = json_platform_field_uuid_in

    params["referenceable_ptr"] = referenceable_ptr

    json_referenceable_ptr_in: list[int] | Unset = UNSET
    if not isinstance(referenceable_ptr_in, Unset):
        json_referenceable_ptr_in = referenceable_ptr_in

    params["referenceable_ptr__in"] = json_referenceable_ptr_in

    params["referenceable_ptr__isnull"] = referenceable_ptr_isnull

    json_responsiblepartyinfo: list[int] | Unset = UNSET
    if not isinstance(responsiblepartyinfo, Unset):
        json_responsiblepartyinfo = responsiblepartyinfo

    params["responsiblepartyinfo"] = json_responsiblepartyinfo

    json_responsiblepartyinfo_in: list[int] | Unset = UNSET
    if not isinstance(responsiblepartyinfo_in, Unset):
        json_responsiblepartyinfo_in = responsiblepartyinfo_in

    params["responsiblepartyinfo__in"] = json_responsiblepartyinfo_in

    params["responsiblepartyinfo__isnull"] = responsiblepartyinfo_isnull

    json_review: list[int] | Unset = UNSET
    if not isinstance(review, Unset):
        json_review = review

    params["review"] = json_review

    json_review_in: list[int] | Unset = UNSET
    if not isinstance(review_in, Unset):
        json_review_in = review_in

    params["review__in"] = json_review_in

    params["review__isnull"] = review_isnull

    params["short_code"] = short_code

    params["short_code__contains"] = short_code_contains

    params["short_code__endswith"] = short_code_endswith

    params["short_code__gt"] = short_code_gt

    params["short_code__gte"] = short_code_gte

    params["short_code__icontains"] = short_code_icontains

    params["short_code__iendswith"] = short_code_iendswith

    params["short_code__iexact"] = short_code_iexact

    json_short_code_in: list[str] | Unset = UNSET
    if not isinstance(short_code_in, Unset):
        json_short_code_in = short_code_in

    params["short_code__in"] = json_short_code_in

    params["short_code__iregex"] = short_code_iregex

    params["short_code__isnull"] = short_code_isnull

    params["short_code__istartswith"] = short_code_istartswith

    params["short_code__lt"] = short_code_lt

    params["short_code__lte"] = short_code_lte

    json_short_code_range: list[str] | Unset = UNSET
    if not isinstance(short_code_range, Unset):
        json_short_code_range = short_code_range

    params["short_code__range"] = json_short_code_range

    params["short_code__regex"] = short_code_regex

    params["short_code__startswith"] = short_code_startswith

    json_status: str | Unset = UNSET
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

    json_status_in: list[str] | Unset = UNSET
    if not isinstance(status_in, Unset):
        json_status_in = status_in

    params["status__in"] = json_status_in

    params["status__iregex"] = status_iregex

    params["status__isnull"] = status_isnull

    params["status__istartswith"] = status_istartswith

    params["status__lt"] = status_lt

    params["status__lte"] = status_lte

    json_status_range: list[str] | Unset = UNSET
    if not isinstance(status_range, Unset):
        json_status_range = status_range

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

    json_title_in: list[str] | Unset = UNSET
    if not isinstance(title_in, Unset):
        json_title_in = title_in

    params["title__in"] = json_title_in

    params["title__iregex"] = title_iregex

    params["title__isnull"] = title_isnull

    params["title__istartswith"] = title_istartswith

    params["title__lt"] = title_lt

    params["title__lte"] = title_lte

    json_title_range: list[str] | Unset = UNSET
    if not isinstance(title_range, Unset):
        json_title_range = title_range

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

    json_uuid_in: list[str] | Unset = UNSET
    if not isinstance(uuid_in, Unset):
        json_uuid_in = uuid_in

    params["uuid__in"] = json_uuid_in

    params["uuid__iregex"] = uuid_iregex

    params["uuid__isnull"] = uuid_isnull

    params["uuid__istartswith"] = uuid_istartswith

    params["uuid__lt"] = uuid_lt

    params["uuid__lte"] = uuid_lte

    json_uuid_range: list[str] | Unset = UNSET
    if not isinstance(uuid_range, Unset):
        json_uuid_range = uuid_range

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedMobilePlatformOperationReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedMobilePlatformOperationReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    child_operation: int | Unset = UNSET,
    child_operation_in: list[int] | Unset = UNSET,
    child_operation_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    location: int | Unset = UNSET,
    location_east_bound_longitude: float | Unset = UNSET,
    location_east_bound_longitude_gt: float | Unset = UNSET,
    location_east_bound_longitude_gte: float | Unset = UNSET,
    location_east_bound_longitude_lt: float | Unset = UNSET,
    location_east_bound_longitude_lte: float | Unset = UNSET,
    location_east_bound_longitude_range: list[float] | Unset = UNSET,
    location_in: list[int] | Unset = UNSET,
    location_isnull: bool | Unset = UNSET,
    location_north_bound_latitude: float | Unset = UNSET,
    location_north_bound_latitude_gt: float | Unset = UNSET,
    location_north_bound_latitude_gte: float | Unset = UNSET,
    location_north_bound_latitude_lt: float | Unset = UNSET,
    location_north_bound_latitude_lte: float | Unset = UNSET,
    location_north_bound_latitude_range: list[float] | Unset = UNSET,
    location_ob_id: int | Unset = UNSET,
    location_ob_id_in: list[int] | Unset = UNSET,
    location_south_bound_latitude: float | Unset = UNSET,
    location_south_bound_latitude_gt: float | Unset = UNSET,
    location_south_bound_latitude_gte: float | Unset = UNSET,
    location_south_bound_latitude_lt: float | Unset = UNSET,
    location_south_bound_latitude_lte: float | Unset = UNSET,
    location_south_bound_latitude_range: list[float] | Unset = UNSET,
    location_west_bound_longitude: float | Unset = UNSET,
    location_west_bound_longitude_gt: float | Unset = UNSET,
    location_west_bound_longitude_gte: float | Unset = UNSET,
    location_west_bound_longitude_lt: float | Unset = UNSET,
    location_west_bound_longitude_lte: float | Unset = UNSET,
    location_west_bound_longitude_range: list[float] | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    operation_time: int | Unset = UNSET,
    operation_time_end_time: datetime.datetime | Unset = UNSET,
    operation_time_end_time_gt: datetime.datetime | Unset = UNSET,
    operation_time_end_time_gte: datetime.datetime | Unset = UNSET,
    operation_time_end_time_lt: datetime.datetime | Unset = UNSET,
    operation_time_end_time_lte: datetime.datetime | Unset = UNSET,
    operation_time_end_time_range: list[datetime.datetime] | Unset = UNSET,
    operation_time_in: list[int] | Unset = UNSET,
    operation_time_isnull: bool | Unset = UNSET,
    operation_time_ob_id: int | Unset = UNSET,
    operation_time_ob_id_in: list[int] | Unset = UNSET,
    operation_time_start_time: datetime.datetime | Unset = UNSET,
    operation_time_start_time_gt: datetime.datetime | Unset = UNSET,
    operation_time_start_time_gte: datetime.datetime | Unset = UNSET,
    operation_time_start_time_lt: datetime.datetime | Unset = UNSET,
    operation_time_start_time_lte: datetime.datetime | Unset = UNSET,
    operation_time_start_time_range: list[datetime.datetime] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform_field: int | Unset = UNSET,
    platform_field_in: list[int] | Unset = UNSET,
    platform_field_isnull: bool | Unset = UNSET,
    platform_field_ob_id: int | Unset = UNSET,
    platform_field_ob_id_in: list[int] | Unset = UNSET,
    platform_field_uuid: str | Unset = UNSET,
    platform_field_uuid_in: list[str] | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    status: MposListStatus | Unset = UNSET,
    status_contains: str | Unset = UNSET,
    status_endswith: str | Unset = UNSET,
    status_gt: str | Unset = UNSET,
    status_gte: str | Unset = UNSET,
    status_icontains: str | Unset = UNSET,
    status_iendswith: str | Unset = UNSET,
    status_iexact: str | Unset = UNSET,
    status_in: list[str] | Unset = UNSET,
    status_iregex: str | Unset = UNSET,
    status_isnull: bool | Unset = UNSET,
    status_istartswith: str | Unset = UNSET,
    status_lt: str | Unset = UNSET,
    status_lte: str | Unset = UNSET,
    status_range: list[str] | Unset = UNSET,
    status_regex: str | Unset = UNSET,
    status_startswith: str | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> Response[PaginatedMobilePlatformOperationReadList]:
    """Get a list of Mobile Platform Operation objects.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        child_operation (int | Unset):
        child_operation_in (list[int] | Unset):
        child_operation_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        limit (int | Unset):
        location (int | Unset):
        location_east_bound_longitude (float | Unset):
        location_east_bound_longitude_gt (float | Unset):
        location_east_bound_longitude_gte (float | Unset):
        location_east_bound_longitude_lt (float | Unset):
        location_east_bound_longitude_lte (float | Unset):
        location_east_bound_longitude_range (list[float] | Unset):
        location_in (list[int] | Unset):
        location_isnull (bool | Unset):
        location_north_bound_latitude (float | Unset):
        location_north_bound_latitude_gt (float | Unset):
        location_north_bound_latitude_gte (float | Unset):
        location_north_bound_latitude_lt (float | Unset):
        location_north_bound_latitude_lte (float | Unset):
        location_north_bound_latitude_range (list[float] | Unset):
        location_ob_id (int | Unset):
        location_ob_id_in (list[int] | Unset):
        location_south_bound_latitude (float | Unset):
        location_south_bound_latitude_gt (float | Unset):
        location_south_bound_latitude_gte (float | Unset):
        location_south_bound_latitude_lt (float | Unset):
        location_south_bound_latitude_lte (float | Unset):
        location_south_bound_latitude_range (list[float] | Unset):
        location_west_bound_longitude (float | Unset):
        location_west_bound_longitude_gt (float | Unset):
        location_west_bound_longitude_gte (float | Unset):
        location_west_bound_longitude_lt (float | Unset):
        location_west_bound_longitude_lte (float | Unset):
        location_west_bound_longitude_range (list[float] | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        operation_time (int | Unset):
        operation_time_end_time (datetime.datetime | Unset):
        operation_time_end_time_gt (datetime.datetime | Unset):
        operation_time_end_time_gte (datetime.datetime | Unset):
        operation_time_end_time_lt (datetime.datetime | Unset):
        operation_time_end_time_lte (datetime.datetime | Unset):
        operation_time_end_time_range (list[datetime.datetime] | Unset):
        operation_time_in (list[int] | Unset):
        operation_time_isnull (bool | Unset):
        operation_time_ob_id (int | Unset):
        operation_time_ob_id_in (list[int] | Unset):
        operation_time_start_time (datetime.datetime | Unset):
        operation_time_start_time_gt (datetime.datetime | Unset):
        operation_time_start_time_gte (datetime.datetime | Unset):
        operation_time_start_time_lt (datetime.datetime | Unset):
        operation_time_start_time_lte (datetime.datetime | Unset):
        operation_time_start_time_range (list[datetime.datetime] | Unset):
        ordering (str | Unset):
        platform_field (int | Unset):
        platform_field_in (list[int] | Unset):
        platform_field_isnull (bool | Unset):
        platform_field_ob_id (int | Unset):
        platform_field_ob_id_in (list[int] | Unset):
        platform_field_uuid (str | Unset):
        platform_field_uuid_in (list[str] | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        status (MposListStatus | Unset):
        status_contains (str | Unset):
        status_endswith (str | Unset):
        status_gt (str | Unset):
        status_gte (str | Unset):
        status_icontains (str | Unset):
        status_iendswith (str | Unset):
        status_iexact (str | Unset):
        status_in (list[str] | Unset):
        status_iregex (str | Unset):
        status_isnull (bool | Unset):
        status_istartswith (str | Unset):
        status_lt (str | Unset):
        status_lte (str | Unset):
        status_range (list[str] | Unset):
        status_regex (str | Unset):
        status_startswith (str | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

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
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        child_operation=child_operation,
        child_operation_in=child_operation_in,
        child_operation_isnull=child_operation_isnull,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        limit=limit,
        location=location,
        location_east_bound_longitude=location_east_bound_longitude,
        location_east_bound_longitude_gt=location_east_bound_longitude_gt,
        location_east_bound_longitude_gte=location_east_bound_longitude_gte,
        location_east_bound_longitude_lt=location_east_bound_longitude_lt,
        location_east_bound_longitude_lte=location_east_bound_longitude_lte,
        location_east_bound_longitude_range=location_east_bound_longitude_range,
        location_in=location_in,
        location_isnull=location_isnull,
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
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
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
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        operation_time=operation_time,
        operation_time_end_time=operation_time_end_time,
        operation_time_end_time_gt=operation_time_end_time_gt,
        operation_time_end_time_gte=operation_time_end_time_gte,
        operation_time_end_time_lt=operation_time_end_time_lt,
        operation_time_end_time_lte=operation_time_end_time_lte,
        operation_time_end_time_range=operation_time_end_time_range,
        operation_time_in=operation_time_in,
        operation_time_isnull=operation_time_isnull,
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
        platform_field_in=platform_field_in,
        platform_field_isnull=platform_field_isnull,
        platform_field_ob_id=platform_field_ob_id,
        platform_field_ob_id_in=platform_field_ob_id_in,
        platform_field_uuid=platform_field_uuid,
        platform_field_uuid_in=platform_field_uuid_in,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
        review=review,
        review_in=review_in,
        review_isnull=review_isnull,
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
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    child_operation: int | Unset = UNSET,
    child_operation_in: list[int] | Unset = UNSET,
    child_operation_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    location: int | Unset = UNSET,
    location_east_bound_longitude: float | Unset = UNSET,
    location_east_bound_longitude_gt: float | Unset = UNSET,
    location_east_bound_longitude_gte: float | Unset = UNSET,
    location_east_bound_longitude_lt: float | Unset = UNSET,
    location_east_bound_longitude_lte: float | Unset = UNSET,
    location_east_bound_longitude_range: list[float] | Unset = UNSET,
    location_in: list[int] | Unset = UNSET,
    location_isnull: bool | Unset = UNSET,
    location_north_bound_latitude: float | Unset = UNSET,
    location_north_bound_latitude_gt: float | Unset = UNSET,
    location_north_bound_latitude_gte: float | Unset = UNSET,
    location_north_bound_latitude_lt: float | Unset = UNSET,
    location_north_bound_latitude_lte: float | Unset = UNSET,
    location_north_bound_latitude_range: list[float] | Unset = UNSET,
    location_ob_id: int | Unset = UNSET,
    location_ob_id_in: list[int] | Unset = UNSET,
    location_south_bound_latitude: float | Unset = UNSET,
    location_south_bound_latitude_gt: float | Unset = UNSET,
    location_south_bound_latitude_gte: float | Unset = UNSET,
    location_south_bound_latitude_lt: float | Unset = UNSET,
    location_south_bound_latitude_lte: float | Unset = UNSET,
    location_south_bound_latitude_range: list[float] | Unset = UNSET,
    location_west_bound_longitude: float | Unset = UNSET,
    location_west_bound_longitude_gt: float | Unset = UNSET,
    location_west_bound_longitude_gte: float | Unset = UNSET,
    location_west_bound_longitude_lt: float | Unset = UNSET,
    location_west_bound_longitude_lte: float | Unset = UNSET,
    location_west_bound_longitude_range: list[float] | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    operation_time: int | Unset = UNSET,
    operation_time_end_time: datetime.datetime | Unset = UNSET,
    operation_time_end_time_gt: datetime.datetime | Unset = UNSET,
    operation_time_end_time_gte: datetime.datetime | Unset = UNSET,
    operation_time_end_time_lt: datetime.datetime | Unset = UNSET,
    operation_time_end_time_lte: datetime.datetime | Unset = UNSET,
    operation_time_end_time_range: list[datetime.datetime] | Unset = UNSET,
    operation_time_in: list[int] | Unset = UNSET,
    operation_time_isnull: bool | Unset = UNSET,
    operation_time_ob_id: int | Unset = UNSET,
    operation_time_ob_id_in: list[int] | Unset = UNSET,
    operation_time_start_time: datetime.datetime | Unset = UNSET,
    operation_time_start_time_gt: datetime.datetime | Unset = UNSET,
    operation_time_start_time_gte: datetime.datetime | Unset = UNSET,
    operation_time_start_time_lt: datetime.datetime | Unset = UNSET,
    operation_time_start_time_lte: datetime.datetime | Unset = UNSET,
    operation_time_start_time_range: list[datetime.datetime] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform_field: int | Unset = UNSET,
    platform_field_in: list[int] | Unset = UNSET,
    platform_field_isnull: bool | Unset = UNSET,
    platform_field_ob_id: int | Unset = UNSET,
    platform_field_ob_id_in: list[int] | Unset = UNSET,
    platform_field_uuid: str | Unset = UNSET,
    platform_field_uuid_in: list[str] | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    status: MposListStatus | Unset = UNSET,
    status_contains: str | Unset = UNSET,
    status_endswith: str | Unset = UNSET,
    status_gt: str | Unset = UNSET,
    status_gte: str | Unset = UNSET,
    status_icontains: str | Unset = UNSET,
    status_iendswith: str | Unset = UNSET,
    status_iexact: str | Unset = UNSET,
    status_in: list[str] | Unset = UNSET,
    status_iregex: str | Unset = UNSET,
    status_isnull: bool | Unset = UNSET,
    status_istartswith: str | Unset = UNSET,
    status_lt: str | Unset = UNSET,
    status_lte: str | Unset = UNSET,
    status_range: list[str] | Unset = UNSET,
    status_regex: str | Unset = UNSET,
    status_startswith: str | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> PaginatedMobilePlatformOperationReadList | None:
    """Get a list of Mobile Platform Operation objects.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        child_operation (int | Unset):
        child_operation_in (list[int] | Unset):
        child_operation_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        limit (int | Unset):
        location (int | Unset):
        location_east_bound_longitude (float | Unset):
        location_east_bound_longitude_gt (float | Unset):
        location_east_bound_longitude_gte (float | Unset):
        location_east_bound_longitude_lt (float | Unset):
        location_east_bound_longitude_lte (float | Unset):
        location_east_bound_longitude_range (list[float] | Unset):
        location_in (list[int] | Unset):
        location_isnull (bool | Unset):
        location_north_bound_latitude (float | Unset):
        location_north_bound_latitude_gt (float | Unset):
        location_north_bound_latitude_gte (float | Unset):
        location_north_bound_latitude_lt (float | Unset):
        location_north_bound_latitude_lte (float | Unset):
        location_north_bound_latitude_range (list[float] | Unset):
        location_ob_id (int | Unset):
        location_ob_id_in (list[int] | Unset):
        location_south_bound_latitude (float | Unset):
        location_south_bound_latitude_gt (float | Unset):
        location_south_bound_latitude_gte (float | Unset):
        location_south_bound_latitude_lt (float | Unset):
        location_south_bound_latitude_lte (float | Unset):
        location_south_bound_latitude_range (list[float] | Unset):
        location_west_bound_longitude (float | Unset):
        location_west_bound_longitude_gt (float | Unset):
        location_west_bound_longitude_gte (float | Unset):
        location_west_bound_longitude_lt (float | Unset):
        location_west_bound_longitude_lte (float | Unset):
        location_west_bound_longitude_range (list[float] | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        operation_time (int | Unset):
        operation_time_end_time (datetime.datetime | Unset):
        operation_time_end_time_gt (datetime.datetime | Unset):
        operation_time_end_time_gte (datetime.datetime | Unset):
        operation_time_end_time_lt (datetime.datetime | Unset):
        operation_time_end_time_lte (datetime.datetime | Unset):
        operation_time_end_time_range (list[datetime.datetime] | Unset):
        operation_time_in (list[int] | Unset):
        operation_time_isnull (bool | Unset):
        operation_time_ob_id (int | Unset):
        operation_time_ob_id_in (list[int] | Unset):
        operation_time_start_time (datetime.datetime | Unset):
        operation_time_start_time_gt (datetime.datetime | Unset):
        operation_time_start_time_gte (datetime.datetime | Unset):
        operation_time_start_time_lt (datetime.datetime | Unset):
        operation_time_start_time_lte (datetime.datetime | Unset):
        operation_time_start_time_range (list[datetime.datetime] | Unset):
        ordering (str | Unset):
        platform_field (int | Unset):
        platform_field_in (list[int] | Unset):
        platform_field_isnull (bool | Unset):
        platform_field_ob_id (int | Unset):
        platform_field_ob_id_in (list[int] | Unset):
        platform_field_uuid (str | Unset):
        platform_field_uuid_in (list[str] | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        status (MposListStatus | Unset):
        status_contains (str | Unset):
        status_endswith (str | Unset):
        status_gt (str | Unset):
        status_gte (str | Unset):
        status_icontains (str | Unset):
        status_iendswith (str | Unset):
        status_iexact (str | Unset):
        status_in (list[str] | Unset):
        status_iregex (str | Unset):
        status_isnull (bool | Unset):
        status_istartswith (str | Unset):
        status_lt (str | Unset):
        status_lte (str | Unset):
        status_range (list[str] | Unset):
        status_regex (str | Unset):
        status_startswith (str | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

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
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        child_operation=child_operation,
        child_operation_in=child_operation_in,
        child_operation_isnull=child_operation_isnull,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        limit=limit,
        location=location,
        location_east_bound_longitude=location_east_bound_longitude,
        location_east_bound_longitude_gt=location_east_bound_longitude_gt,
        location_east_bound_longitude_gte=location_east_bound_longitude_gte,
        location_east_bound_longitude_lt=location_east_bound_longitude_lt,
        location_east_bound_longitude_lte=location_east_bound_longitude_lte,
        location_east_bound_longitude_range=location_east_bound_longitude_range,
        location_in=location_in,
        location_isnull=location_isnull,
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
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
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
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        operation_time=operation_time,
        operation_time_end_time=operation_time_end_time,
        operation_time_end_time_gt=operation_time_end_time_gt,
        operation_time_end_time_gte=operation_time_end_time_gte,
        operation_time_end_time_lt=operation_time_end_time_lt,
        operation_time_end_time_lte=operation_time_end_time_lte,
        operation_time_end_time_range=operation_time_end_time_range,
        operation_time_in=operation_time_in,
        operation_time_isnull=operation_time_isnull,
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
        platform_field_in=platform_field_in,
        platform_field_isnull=platform_field_isnull,
        platform_field_ob_id=platform_field_ob_id,
        platform_field_ob_id_in=platform_field_ob_id_in,
        platform_field_uuid=platform_field_uuid,
        platform_field_uuid_in=platform_field_uuid_in,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
        review=review,
        review_in=review_in,
        review_isnull=review_isnull,
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
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    child_operation: int | Unset = UNSET,
    child_operation_in: list[int] | Unset = UNSET,
    child_operation_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    location: int | Unset = UNSET,
    location_east_bound_longitude: float | Unset = UNSET,
    location_east_bound_longitude_gt: float | Unset = UNSET,
    location_east_bound_longitude_gte: float | Unset = UNSET,
    location_east_bound_longitude_lt: float | Unset = UNSET,
    location_east_bound_longitude_lte: float | Unset = UNSET,
    location_east_bound_longitude_range: list[float] | Unset = UNSET,
    location_in: list[int] | Unset = UNSET,
    location_isnull: bool | Unset = UNSET,
    location_north_bound_latitude: float | Unset = UNSET,
    location_north_bound_latitude_gt: float | Unset = UNSET,
    location_north_bound_latitude_gte: float | Unset = UNSET,
    location_north_bound_latitude_lt: float | Unset = UNSET,
    location_north_bound_latitude_lte: float | Unset = UNSET,
    location_north_bound_latitude_range: list[float] | Unset = UNSET,
    location_ob_id: int | Unset = UNSET,
    location_ob_id_in: list[int] | Unset = UNSET,
    location_south_bound_latitude: float | Unset = UNSET,
    location_south_bound_latitude_gt: float | Unset = UNSET,
    location_south_bound_latitude_gte: float | Unset = UNSET,
    location_south_bound_latitude_lt: float | Unset = UNSET,
    location_south_bound_latitude_lte: float | Unset = UNSET,
    location_south_bound_latitude_range: list[float] | Unset = UNSET,
    location_west_bound_longitude: float | Unset = UNSET,
    location_west_bound_longitude_gt: float | Unset = UNSET,
    location_west_bound_longitude_gte: float | Unset = UNSET,
    location_west_bound_longitude_lt: float | Unset = UNSET,
    location_west_bound_longitude_lte: float | Unset = UNSET,
    location_west_bound_longitude_range: list[float] | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    operation_time: int | Unset = UNSET,
    operation_time_end_time: datetime.datetime | Unset = UNSET,
    operation_time_end_time_gt: datetime.datetime | Unset = UNSET,
    operation_time_end_time_gte: datetime.datetime | Unset = UNSET,
    operation_time_end_time_lt: datetime.datetime | Unset = UNSET,
    operation_time_end_time_lte: datetime.datetime | Unset = UNSET,
    operation_time_end_time_range: list[datetime.datetime] | Unset = UNSET,
    operation_time_in: list[int] | Unset = UNSET,
    operation_time_isnull: bool | Unset = UNSET,
    operation_time_ob_id: int | Unset = UNSET,
    operation_time_ob_id_in: list[int] | Unset = UNSET,
    operation_time_start_time: datetime.datetime | Unset = UNSET,
    operation_time_start_time_gt: datetime.datetime | Unset = UNSET,
    operation_time_start_time_gte: datetime.datetime | Unset = UNSET,
    operation_time_start_time_lt: datetime.datetime | Unset = UNSET,
    operation_time_start_time_lte: datetime.datetime | Unset = UNSET,
    operation_time_start_time_range: list[datetime.datetime] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform_field: int | Unset = UNSET,
    platform_field_in: list[int] | Unset = UNSET,
    platform_field_isnull: bool | Unset = UNSET,
    platform_field_ob_id: int | Unset = UNSET,
    platform_field_ob_id_in: list[int] | Unset = UNSET,
    platform_field_uuid: str | Unset = UNSET,
    platform_field_uuid_in: list[str] | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    status: MposListStatus | Unset = UNSET,
    status_contains: str | Unset = UNSET,
    status_endswith: str | Unset = UNSET,
    status_gt: str | Unset = UNSET,
    status_gte: str | Unset = UNSET,
    status_icontains: str | Unset = UNSET,
    status_iendswith: str | Unset = UNSET,
    status_iexact: str | Unset = UNSET,
    status_in: list[str] | Unset = UNSET,
    status_iregex: str | Unset = UNSET,
    status_isnull: bool | Unset = UNSET,
    status_istartswith: str | Unset = UNSET,
    status_lt: str | Unset = UNSET,
    status_lte: str | Unset = UNSET,
    status_range: list[str] | Unset = UNSET,
    status_regex: str | Unset = UNSET,
    status_startswith: str | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> Response[PaginatedMobilePlatformOperationReadList]:
    """Get a list of Mobile Platform Operation objects.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        child_operation (int | Unset):
        child_operation_in (list[int] | Unset):
        child_operation_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        limit (int | Unset):
        location (int | Unset):
        location_east_bound_longitude (float | Unset):
        location_east_bound_longitude_gt (float | Unset):
        location_east_bound_longitude_gte (float | Unset):
        location_east_bound_longitude_lt (float | Unset):
        location_east_bound_longitude_lte (float | Unset):
        location_east_bound_longitude_range (list[float] | Unset):
        location_in (list[int] | Unset):
        location_isnull (bool | Unset):
        location_north_bound_latitude (float | Unset):
        location_north_bound_latitude_gt (float | Unset):
        location_north_bound_latitude_gte (float | Unset):
        location_north_bound_latitude_lt (float | Unset):
        location_north_bound_latitude_lte (float | Unset):
        location_north_bound_latitude_range (list[float] | Unset):
        location_ob_id (int | Unset):
        location_ob_id_in (list[int] | Unset):
        location_south_bound_latitude (float | Unset):
        location_south_bound_latitude_gt (float | Unset):
        location_south_bound_latitude_gte (float | Unset):
        location_south_bound_latitude_lt (float | Unset):
        location_south_bound_latitude_lte (float | Unset):
        location_south_bound_latitude_range (list[float] | Unset):
        location_west_bound_longitude (float | Unset):
        location_west_bound_longitude_gt (float | Unset):
        location_west_bound_longitude_gte (float | Unset):
        location_west_bound_longitude_lt (float | Unset):
        location_west_bound_longitude_lte (float | Unset):
        location_west_bound_longitude_range (list[float] | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        operation_time (int | Unset):
        operation_time_end_time (datetime.datetime | Unset):
        operation_time_end_time_gt (datetime.datetime | Unset):
        operation_time_end_time_gte (datetime.datetime | Unset):
        operation_time_end_time_lt (datetime.datetime | Unset):
        operation_time_end_time_lte (datetime.datetime | Unset):
        operation_time_end_time_range (list[datetime.datetime] | Unset):
        operation_time_in (list[int] | Unset):
        operation_time_isnull (bool | Unset):
        operation_time_ob_id (int | Unset):
        operation_time_ob_id_in (list[int] | Unset):
        operation_time_start_time (datetime.datetime | Unset):
        operation_time_start_time_gt (datetime.datetime | Unset):
        operation_time_start_time_gte (datetime.datetime | Unset):
        operation_time_start_time_lt (datetime.datetime | Unset):
        operation_time_start_time_lte (datetime.datetime | Unset):
        operation_time_start_time_range (list[datetime.datetime] | Unset):
        ordering (str | Unset):
        platform_field (int | Unset):
        platform_field_in (list[int] | Unset):
        platform_field_isnull (bool | Unset):
        platform_field_ob_id (int | Unset):
        platform_field_ob_id_in (list[int] | Unset):
        platform_field_uuid (str | Unset):
        platform_field_uuid_in (list[str] | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        status (MposListStatus | Unset):
        status_contains (str | Unset):
        status_endswith (str | Unset):
        status_gt (str | Unset):
        status_gte (str | Unset):
        status_icontains (str | Unset):
        status_iendswith (str | Unset):
        status_iexact (str | Unset):
        status_in (list[str] | Unset):
        status_iregex (str | Unset):
        status_isnull (bool | Unset):
        status_istartswith (str | Unset):
        status_lt (str | Unset):
        status_lte (str | Unset):
        status_range (list[str] | Unset):
        status_regex (str | Unset):
        status_startswith (str | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

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
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        child_operation=child_operation,
        child_operation_in=child_operation_in,
        child_operation_isnull=child_operation_isnull,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        limit=limit,
        location=location,
        location_east_bound_longitude=location_east_bound_longitude,
        location_east_bound_longitude_gt=location_east_bound_longitude_gt,
        location_east_bound_longitude_gte=location_east_bound_longitude_gte,
        location_east_bound_longitude_lt=location_east_bound_longitude_lt,
        location_east_bound_longitude_lte=location_east_bound_longitude_lte,
        location_east_bound_longitude_range=location_east_bound_longitude_range,
        location_in=location_in,
        location_isnull=location_isnull,
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
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
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
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        operation_time=operation_time,
        operation_time_end_time=operation_time_end_time,
        operation_time_end_time_gt=operation_time_end_time_gt,
        operation_time_end_time_gte=operation_time_end_time_gte,
        operation_time_end_time_lt=operation_time_end_time_lt,
        operation_time_end_time_lte=operation_time_end_time_lte,
        operation_time_end_time_range=operation_time_end_time_range,
        operation_time_in=operation_time_in,
        operation_time_isnull=operation_time_isnull,
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
        platform_field_in=platform_field_in,
        platform_field_isnull=platform_field_isnull,
        platform_field_ob_id=platform_field_ob_id,
        platform_field_ob_id_in=platform_field_ob_id_in,
        platform_field_uuid=platform_field_uuid,
        platform_field_uuid_in=platform_field_uuid_in,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
        review=review,
        review_in=review_in,
        review_isnull=review_isnull,
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
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    child_operation: int | Unset = UNSET,
    child_operation_in: list[int] | Unset = UNSET,
    child_operation_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    location: int | Unset = UNSET,
    location_east_bound_longitude: float | Unset = UNSET,
    location_east_bound_longitude_gt: float | Unset = UNSET,
    location_east_bound_longitude_gte: float | Unset = UNSET,
    location_east_bound_longitude_lt: float | Unset = UNSET,
    location_east_bound_longitude_lte: float | Unset = UNSET,
    location_east_bound_longitude_range: list[float] | Unset = UNSET,
    location_in: list[int] | Unset = UNSET,
    location_isnull: bool | Unset = UNSET,
    location_north_bound_latitude: float | Unset = UNSET,
    location_north_bound_latitude_gt: float | Unset = UNSET,
    location_north_bound_latitude_gte: float | Unset = UNSET,
    location_north_bound_latitude_lt: float | Unset = UNSET,
    location_north_bound_latitude_lte: float | Unset = UNSET,
    location_north_bound_latitude_range: list[float] | Unset = UNSET,
    location_ob_id: int | Unset = UNSET,
    location_ob_id_in: list[int] | Unset = UNSET,
    location_south_bound_latitude: float | Unset = UNSET,
    location_south_bound_latitude_gt: float | Unset = UNSET,
    location_south_bound_latitude_gte: float | Unset = UNSET,
    location_south_bound_latitude_lt: float | Unset = UNSET,
    location_south_bound_latitude_lte: float | Unset = UNSET,
    location_south_bound_latitude_range: list[float] | Unset = UNSET,
    location_west_bound_longitude: float | Unset = UNSET,
    location_west_bound_longitude_gt: float | Unset = UNSET,
    location_west_bound_longitude_gte: float | Unset = UNSET,
    location_west_bound_longitude_lt: float | Unset = UNSET,
    location_west_bound_longitude_lte: float | Unset = UNSET,
    location_west_bound_longitude_range: list[float] | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    operation_time: int | Unset = UNSET,
    operation_time_end_time: datetime.datetime | Unset = UNSET,
    operation_time_end_time_gt: datetime.datetime | Unset = UNSET,
    operation_time_end_time_gte: datetime.datetime | Unset = UNSET,
    operation_time_end_time_lt: datetime.datetime | Unset = UNSET,
    operation_time_end_time_lte: datetime.datetime | Unset = UNSET,
    operation_time_end_time_range: list[datetime.datetime] | Unset = UNSET,
    operation_time_in: list[int] | Unset = UNSET,
    operation_time_isnull: bool | Unset = UNSET,
    operation_time_ob_id: int | Unset = UNSET,
    operation_time_ob_id_in: list[int] | Unset = UNSET,
    operation_time_start_time: datetime.datetime | Unset = UNSET,
    operation_time_start_time_gt: datetime.datetime | Unset = UNSET,
    operation_time_start_time_gte: datetime.datetime | Unset = UNSET,
    operation_time_start_time_lt: datetime.datetime | Unset = UNSET,
    operation_time_start_time_lte: datetime.datetime | Unset = UNSET,
    operation_time_start_time_range: list[datetime.datetime] | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform_field: int | Unset = UNSET,
    platform_field_in: list[int] | Unset = UNSET,
    platform_field_isnull: bool | Unset = UNSET,
    platform_field_ob_id: int | Unset = UNSET,
    platform_field_ob_id_in: list[int] | Unset = UNSET,
    platform_field_uuid: str | Unset = UNSET,
    platform_field_uuid_in: list[str] | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    status: MposListStatus | Unset = UNSET,
    status_contains: str | Unset = UNSET,
    status_endswith: str | Unset = UNSET,
    status_gt: str | Unset = UNSET,
    status_gte: str | Unset = UNSET,
    status_icontains: str | Unset = UNSET,
    status_iendswith: str | Unset = UNSET,
    status_iexact: str | Unset = UNSET,
    status_in: list[str] | Unset = UNSET,
    status_iregex: str | Unset = UNSET,
    status_isnull: bool | Unset = UNSET,
    status_istartswith: str | Unset = UNSET,
    status_lt: str | Unset = UNSET,
    status_lte: str | Unset = UNSET,
    status_range: list[str] | Unset = UNSET,
    status_regex: str | Unset = UNSET,
    status_startswith: str | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> PaginatedMobilePlatformOperationReadList | None:
    """Get a list of Mobile Platform Operation objects.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        child_operation (int | Unset):
        child_operation_in (list[int] | Unset):
        child_operation_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        limit (int | Unset):
        location (int | Unset):
        location_east_bound_longitude (float | Unset):
        location_east_bound_longitude_gt (float | Unset):
        location_east_bound_longitude_gte (float | Unset):
        location_east_bound_longitude_lt (float | Unset):
        location_east_bound_longitude_lte (float | Unset):
        location_east_bound_longitude_range (list[float] | Unset):
        location_in (list[int] | Unset):
        location_isnull (bool | Unset):
        location_north_bound_latitude (float | Unset):
        location_north_bound_latitude_gt (float | Unset):
        location_north_bound_latitude_gte (float | Unset):
        location_north_bound_latitude_lt (float | Unset):
        location_north_bound_latitude_lte (float | Unset):
        location_north_bound_latitude_range (list[float] | Unset):
        location_ob_id (int | Unset):
        location_ob_id_in (list[int] | Unset):
        location_south_bound_latitude (float | Unset):
        location_south_bound_latitude_gt (float | Unset):
        location_south_bound_latitude_gte (float | Unset):
        location_south_bound_latitude_lt (float | Unset):
        location_south_bound_latitude_lte (float | Unset):
        location_south_bound_latitude_range (list[float] | Unset):
        location_west_bound_longitude (float | Unset):
        location_west_bound_longitude_gt (float | Unset):
        location_west_bound_longitude_gte (float | Unset):
        location_west_bound_longitude_lt (float | Unset):
        location_west_bound_longitude_lte (float | Unset):
        location_west_bound_longitude_range (list[float] | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        operation_time (int | Unset):
        operation_time_end_time (datetime.datetime | Unset):
        operation_time_end_time_gt (datetime.datetime | Unset):
        operation_time_end_time_gte (datetime.datetime | Unset):
        operation_time_end_time_lt (datetime.datetime | Unset):
        operation_time_end_time_lte (datetime.datetime | Unset):
        operation_time_end_time_range (list[datetime.datetime] | Unset):
        operation_time_in (list[int] | Unset):
        operation_time_isnull (bool | Unset):
        operation_time_ob_id (int | Unset):
        operation_time_ob_id_in (list[int] | Unset):
        operation_time_start_time (datetime.datetime | Unset):
        operation_time_start_time_gt (datetime.datetime | Unset):
        operation_time_start_time_gte (datetime.datetime | Unset):
        operation_time_start_time_lt (datetime.datetime | Unset):
        operation_time_start_time_lte (datetime.datetime | Unset):
        operation_time_start_time_range (list[datetime.datetime] | Unset):
        ordering (str | Unset):
        platform_field (int | Unset):
        platform_field_in (list[int] | Unset):
        platform_field_isnull (bool | Unset):
        platform_field_ob_id (int | Unset):
        platform_field_ob_id_in (list[int] | Unset):
        platform_field_uuid (str | Unset):
        platform_field_uuid_in (list[str] | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        status (MposListStatus | Unset):
        status_contains (str | Unset):
        status_endswith (str | Unset):
        status_gt (str | Unset):
        status_gte (str | Unset):
        status_icontains (str | Unset):
        status_iendswith (str | Unset):
        status_iexact (str | Unset):
        status_in (list[str] | Unset):
        status_iregex (str | Unset):
        status_isnull (bool | Unset):
        status_istartswith (str | Unset):
        status_lt (str | Unset):
        status_lte (str | Unset):
        status_range (list[str] | Unset):
        status_regex (str | Unset):
        status_startswith (str | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

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
            acquisition=acquisition,
            acquisition_in=acquisition_in,
            acquisition_isnull=acquisition_isnull,
            child_operation=child_operation,
            child_operation_in=child_operation_in,
            child_operation_isnull=child_operation_isnull,
            identifier=identifier,
            identifier_in=identifier_in,
            identifier_isnull=identifier_isnull,
            limit=limit,
            location=location,
            location_east_bound_longitude=location_east_bound_longitude,
            location_east_bound_longitude_gt=location_east_bound_longitude_gt,
            location_east_bound_longitude_gte=location_east_bound_longitude_gte,
            location_east_bound_longitude_lt=location_east_bound_longitude_lt,
            location_east_bound_longitude_lte=location_east_bound_longitude_lte,
            location_east_bound_longitude_range=location_east_bound_longitude_range,
            location_in=location_in,
            location_isnull=location_isnull,
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
            migrationproperty=migrationproperty,
            migrationproperty_in=migrationproperty_in,
            migrationproperty_isnull=migrationproperty_isnull,
            mobileplatformoperation=mobileplatformoperation,
            mobileplatformoperation_in=mobileplatformoperation_in,
            mobileplatformoperation_isnull=mobileplatformoperation_isnull,
            note=note,
            note_in=note_in,
            note_isnull=note_isnull,
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
            onlineresource=onlineresource,
            onlineresource_in=onlineresource_in,
            onlineresource_isnull=onlineresource_isnull,
            operation_time=operation_time,
            operation_time_end_time=operation_time_end_time,
            operation_time_end_time_gt=operation_time_end_time_gt,
            operation_time_end_time_gte=operation_time_end_time_gte,
            operation_time_end_time_lt=operation_time_end_time_lt,
            operation_time_end_time_lte=operation_time_end_time_lte,
            operation_time_end_time_range=operation_time_end_time_range,
            operation_time_in=operation_time_in,
            operation_time_isnull=operation_time_isnull,
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
            platform_field_in=platform_field_in,
            platform_field_isnull=platform_field_isnull,
            platform_field_ob_id=platform_field_ob_id,
            platform_field_ob_id_in=platform_field_ob_id_in,
            platform_field_uuid=platform_field_uuid,
            platform_field_uuid_in=platform_field_uuid_in,
            referenceable_ptr=referenceable_ptr,
            referenceable_ptr_in=referenceable_ptr_in,
            referenceable_ptr_isnull=referenceable_ptr_isnull,
            responsiblepartyinfo=responsiblepartyinfo,
            responsiblepartyinfo_in=responsiblepartyinfo_in,
            responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
            review=review,
            review_in=review_in,
            review_isnull=review_isnull,
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
