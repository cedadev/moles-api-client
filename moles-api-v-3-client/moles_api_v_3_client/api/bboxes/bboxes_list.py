from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_geographic_bounding_box_read_list import PaginatedGeographicBoundingBoxReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bbox_name: str | Unset = UNSET,
    bbox_name_contains: str | Unset = UNSET,
    bbox_name_endswith: str | Unset = UNSET,
    bbox_name_gt: str | Unset = UNSET,
    bbox_name_gte: str | Unset = UNSET,
    bbox_name_icontains: str | Unset = UNSET,
    bbox_name_iendswith: str | Unset = UNSET,
    bbox_name_iexact: str | Unset = UNSET,
    bbox_name_in: list[str] | Unset = UNSET,
    bbox_name_iregex: str | Unset = UNSET,
    bbox_name_isnull: bool | Unset = UNSET,
    bbox_name_istartswith: str | Unset = UNSET,
    bbox_name_lt: str | Unset = UNSET,
    bbox_name_lte: str | Unset = UNSET,
    bbox_name_range: list[str] | Unset = UNSET,
    bbox_name_regex: str | Unset = UNSET,
    bbox_name_startswith: str | Unset = UNSET,
    east_bound_longitude: float | Unset = UNSET,
    east_bound_longitude_contained_by: float | Unset = UNSET,
    east_bound_longitude_contains: float | Unset = UNSET,
    east_bound_longitude_endswith: float | Unset = UNSET,
    east_bound_longitude_gt: float | Unset = UNSET,
    east_bound_longitude_gte: float | Unset = UNSET,
    east_bound_longitude_icontains: float | Unset = UNSET,
    east_bound_longitude_iendswith: float | Unset = UNSET,
    east_bound_longitude_iexact: float | Unset = UNSET,
    east_bound_longitude_in: list[float] | Unset = UNSET,
    east_bound_longitude_iregex: float | Unset = UNSET,
    east_bound_longitude_isnull: bool | Unset = UNSET,
    east_bound_longitude_istartswith: float | Unset = UNSET,
    east_bound_longitude_lt: float | Unset = UNSET,
    east_bound_longitude_lte: float | Unset = UNSET,
    east_bound_longitude_range: list[float] | Unset = UNSET,
    east_bound_longitude_regex: float | Unset = UNSET,
    east_bound_longitude_startswith: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    north_bound_latitude: float | Unset = UNSET,
    north_bound_latitude_contained_by: float | Unset = UNSET,
    north_bound_latitude_contains: float | Unset = UNSET,
    north_bound_latitude_endswith: float | Unset = UNSET,
    north_bound_latitude_gt: float | Unset = UNSET,
    north_bound_latitude_gte: float | Unset = UNSET,
    north_bound_latitude_icontains: float | Unset = UNSET,
    north_bound_latitude_iendswith: float | Unset = UNSET,
    north_bound_latitude_iexact: float | Unset = UNSET,
    north_bound_latitude_in: list[float] | Unset = UNSET,
    north_bound_latitude_iregex: float | Unset = UNSET,
    north_bound_latitude_isnull: bool | Unset = UNSET,
    north_bound_latitude_istartswith: float | Unset = UNSET,
    north_bound_latitude_lt: float | Unset = UNSET,
    north_bound_latitude_lte: float | Unset = UNSET,
    north_bound_latitude_range: list[float] | Unset = UNSET,
    north_bound_latitude_regex: float | Unset = UNSET,
    north_bound_latitude_startswith: float | Unset = UNSET,
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
    platform: list[int] | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    south_bound_latitude: float | Unset = UNSET,
    south_bound_latitude_contained_by: float | Unset = UNSET,
    south_bound_latitude_contains: float | Unset = UNSET,
    south_bound_latitude_endswith: float | Unset = UNSET,
    south_bound_latitude_gt: float | Unset = UNSET,
    south_bound_latitude_gte: float | Unset = UNSET,
    south_bound_latitude_icontains: float | Unset = UNSET,
    south_bound_latitude_iendswith: float | Unset = UNSET,
    south_bound_latitude_iexact: float | Unset = UNSET,
    south_bound_latitude_in: list[float] | Unset = UNSET,
    south_bound_latitude_iregex: float | Unset = UNSET,
    south_bound_latitude_isnull: bool | Unset = UNSET,
    south_bound_latitude_istartswith: float | Unset = UNSET,
    south_bound_latitude_lt: float | Unset = UNSET,
    south_bound_latitude_lte: float | Unset = UNSET,
    south_bound_latitude_range: list[float] | Unset = UNSET,
    south_bound_latitude_regex: float | Unset = UNSET,
    south_bound_latitude_startswith: float | Unset = UNSET,
    west_bound_longitude: float | Unset = UNSET,
    west_bound_longitude_contained_by: float | Unset = UNSET,
    west_bound_longitude_contains: float | Unset = UNSET,
    west_bound_longitude_endswith: float | Unset = UNSET,
    west_bound_longitude_gt: float | Unset = UNSET,
    west_bound_longitude_gte: float | Unset = UNSET,
    west_bound_longitude_icontains: float | Unset = UNSET,
    west_bound_longitude_iendswith: float | Unset = UNSET,
    west_bound_longitude_iexact: float | Unset = UNSET,
    west_bound_longitude_in: list[float] | Unset = UNSET,
    west_bound_longitude_iregex: float | Unset = UNSET,
    west_bound_longitude_isnull: bool | Unset = UNSET,
    west_bound_longitude_istartswith: float | Unset = UNSET,
    west_bound_longitude_lt: float | Unset = UNSET,
    west_bound_longitude_lte: float | Unset = UNSET,
    west_bound_longitude_range: list[float] | Unset = UNSET,
    west_bound_longitude_regex: float | Unset = UNSET,
    west_bound_longitude_startswith: float | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["bboxName"] = bbox_name

    params["bboxName__contains"] = bbox_name_contains

    params["bboxName__endswith"] = bbox_name_endswith

    params["bboxName__gt"] = bbox_name_gt

    params["bboxName__gte"] = bbox_name_gte

    params["bboxName__icontains"] = bbox_name_icontains

    params["bboxName__iendswith"] = bbox_name_iendswith

    params["bboxName__iexact"] = bbox_name_iexact

    json_bbox_name_in: list[str] | Unset = UNSET
    if not isinstance(bbox_name_in, Unset):
        json_bbox_name_in = bbox_name_in

    params["bboxName__in"] = json_bbox_name_in

    params["bboxName__iregex"] = bbox_name_iregex

    params["bboxName__isnull"] = bbox_name_isnull

    params["bboxName__istartswith"] = bbox_name_istartswith

    params["bboxName__lt"] = bbox_name_lt

    params["bboxName__lte"] = bbox_name_lte

    json_bbox_name_range: list[str] | Unset = UNSET
    if not isinstance(bbox_name_range, Unset):
        json_bbox_name_range = bbox_name_range

    params["bboxName__range"] = json_bbox_name_range

    params["bboxName__regex"] = bbox_name_regex

    params["bboxName__startswith"] = bbox_name_startswith

    params["eastBoundLongitude"] = east_bound_longitude

    params["eastBoundLongitude__contained_by"] = east_bound_longitude_contained_by

    params["eastBoundLongitude__contains"] = east_bound_longitude_contains

    params["eastBoundLongitude__endswith"] = east_bound_longitude_endswith

    params["eastBoundLongitude__gt"] = east_bound_longitude_gt

    params["eastBoundLongitude__gte"] = east_bound_longitude_gte

    params["eastBoundLongitude__icontains"] = east_bound_longitude_icontains

    params["eastBoundLongitude__iendswith"] = east_bound_longitude_iendswith

    params["eastBoundLongitude__iexact"] = east_bound_longitude_iexact

    json_east_bound_longitude_in: list[float] | Unset = UNSET
    if not isinstance(east_bound_longitude_in, Unset):
        json_east_bound_longitude_in = east_bound_longitude_in

    params["eastBoundLongitude__in"] = json_east_bound_longitude_in

    params["eastBoundLongitude__iregex"] = east_bound_longitude_iregex

    params["eastBoundLongitude__isnull"] = east_bound_longitude_isnull

    params["eastBoundLongitude__istartswith"] = east_bound_longitude_istartswith

    params["eastBoundLongitude__lt"] = east_bound_longitude_lt

    params["eastBoundLongitude__lte"] = east_bound_longitude_lte

    json_east_bound_longitude_range: list[float] | Unset = UNSET
    if not isinstance(east_bound_longitude_range, Unset):
        json_east_bound_longitude_range = east_bound_longitude_range

    params["eastBoundLongitude__range"] = json_east_bound_longitude_range

    params["eastBoundLongitude__regex"] = east_bound_longitude_regex

    params["eastBoundLongitude__startswith"] = east_bound_longitude_startswith

    params["limit"] = limit

    json_mobileplatformoperation: list[int] | Unset = UNSET
    if not isinstance(mobileplatformoperation, Unset):
        json_mobileplatformoperation = mobileplatformoperation

    params["mobileplatformoperation"] = json_mobileplatformoperation

    json_mobileplatformoperation_in: list[int] | Unset = UNSET
    if not isinstance(mobileplatformoperation_in, Unset):
        json_mobileplatformoperation_in = mobileplatformoperation_in

    params["mobileplatformoperation__in"] = json_mobileplatformoperation_in

    params["mobileplatformoperation__isnull"] = mobileplatformoperation_isnull

    params["northBoundLatitude"] = north_bound_latitude

    params["northBoundLatitude__contained_by"] = north_bound_latitude_contained_by

    params["northBoundLatitude__contains"] = north_bound_latitude_contains

    params["northBoundLatitude__endswith"] = north_bound_latitude_endswith

    params["northBoundLatitude__gt"] = north_bound_latitude_gt

    params["northBoundLatitude__gte"] = north_bound_latitude_gte

    params["northBoundLatitude__icontains"] = north_bound_latitude_icontains

    params["northBoundLatitude__iendswith"] = north_bound_latitude_iendswith

    params["northBoundLatitude__iexact"] = north_bound_latitude_iexact

    json_north_bound_latitude_in: list[float] | Unset = UNSET
    if not isinstance(north_bound_latitude_in, Unset):
        json_north_bound_latitude_in = north_bound_latitude_in

    params["northBoundLatitude__in"] = json_north_bound_latitude_in

    params["northBoundLatitude__iregex"] = north_bound_latitude_iregex

    params["northBoundLatitude__isnull"] = north_bound_latitude_isnull

    params["northBoundLatitude__istartswith"] = north_bound_latitude_istartswith

    params["northBoundLatitude__lt"] = north_bound_latitude_lt

    params["northBoundLatitude__lte"] = north_bound_latitude_lte

    json_north_bound_latitude_range: list[float] | Unset = UNSET
    if not isinstance(north_bound_latitude_range, Unset):
        json_north_bound_latitude_range = north_bound_latitude_range

    params["northBoundLatitude__range"] = json_north_bound_latitude_range

    params["northBoundLatitude__regex"] = north_bound_latitude_regex

    params["northBoundLatitude__startswith"] = north_bound_latitude_startswith

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

    json_platform: list[int] | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform

    params["platform"] = json_platform

    json_platform_in: list[int] | Unset = UNSET
    if not isinstance(platform_in, Unset):
        json_platform_in = platform_in

    params["platform__in"] = json_platform_in

    params["platform__isnull"] = platform_isnull

    params["southBoundLatitude"] = south_bound_latitude

    params["southBoundLatitude__contained_by"] = south_bound_latitude_contained_by

    params["southBoundLatitude__contains"] = south_bound_latitude_contains

    params["southBoundLatitude__endswith"] = south_bound_latitude_endswith

    params["southBoundLatitude__gt"] = south_bound_latitude_gt

    params["southBoundLatitude__gte"] = south_bound_latitude_gte

    params["southBoundLatitude__icontains"] = south_bound_latitude_icontains

    params["southBoundLatitude__iendswith"] = south_bound_latitude_iendswith

    params["southBoundLatitude__iexact"] = south_bound_latitude_iexact

    json_south_bound_latitude_in: list[float] | Unset = UNSET
    if not isinstance(south_bound_latitude_in, Unset):
        json_south_bound_latitude_in = south_bound_latitude_in

    params["southBoundLatitude__in"] = json_south_bound_latitude_in

    params["southBoundLatitude__iregex"] = south_bound_latitude_iregex

    params["southBoundLatitude__isnull"] = south_bound_latitude_isnull

    params["southBoundLatitude__istartswith"] = south_bound_latitude_istartswith

    params["southBoundLatitude__lt"] = south_bound_latitude_lt

    params["southBoundLatitude__lte"] = south_bound_latitude_lte

    json_south_bound_latitude_range: list[float] | Unset = UNSET
    if not isinstance(south_bound_latitude_range, Unset):
        json_south_bound_latitude_range = south_bound_latitude_range

    params["southBoundLatitude__range"] = json_south_bound_latitude_range

    params["southBoundLatitude__regex"] = south_bound_latitude_regex

    params["southBoundLatitude__startswith"] = south_bound_latitude_startswith

    params["westBoundLongitude"] = west_bound_longitude

    params["westBoundLongitude__contained_by"] = west_bound_longitude_contained_by

    params["westBoundLongitude__contains"] = west_bound_longitude_contains

    params["westBoundLongitude__endswith"] = west_bound_longitude_endswith

    params["westBoundLongitude__gt"] = west_bound_longitude_gt

    params["westBoundLongitude__gte"] = west_bound_longitude_gte

    params["westBoundLongitude__icontains"] = west_bound_longitude_icontains

    params["westBoundLongitude__iendswith"] = west_bound_longitude_iendswith

    params["westBoundLongitude__iexact"] = west_bound_longitude_iexact

    json_west_bound_longitude_in: list[float] | Unset = UNSET
    if not isinstance(west_bound_longitude_in, Unset):
        json_west_bound_longitude_in = west_bound_longitude_in

    params["westBoundLongitude__in"] = json_west_bound_longitude_in

    params["westBoundLongitude__iregex"] = west_bound_longitude_iregex

    params["westBoundLongitude__isnull"] = west_bound_longitude_isnull

    params["westBoundLongitude__istartswith"] = west_bound_longitude_istartswith

    params["westBoundLongitude__lt"] = west_bound_longitude_lt

    params["westBoundLongitude__lte"] = west_bound_longitude_lte

    json_west_bound_longitude_range: list[float] | Unset = UNSET
    if not isinstance(west_bound_longitude_range, Unset):
        json_west_bound_longitude_range = west_bound_longitude_range

    params["westBoundLongitude__range"] = json_west_bound_longitude_range

    params["westBoundLongitude__regex"] = west_bound_longitude_regex

    params["westBoundLongitude__startswith"] = west_bound_longitude_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/bboxes/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedGeographicBoundingBoxReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedGeographicBoundingBoxReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedGeographicBoundingBoxReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    bbox_name: str | Unset = UNSET,
    bbox_name_contains: str | Unset = UNSET,
    bbox_name_endswith: str | Unset = UNSET,
    bbox_name_gt: str | Unset = UNSET,
    bbox_name_gte: str | Unset = UNSET,
    bbox_name_icontains: str | Unset = UNSET,
    bbox_name_iendswith: str | Unset = UNSET,
    bbox_name_iexact: str | Unset = UNSET,
    bbox_name_in: list[str] | Unset = UNSET,
    bbox_name_iregex: str | Unset = UNSET,
    bbox_name_isnull: bool | Unset = UNSET,
    bbox_name_istartswith: str | Unset = UNSET,
    bbox_name_lt: str | Unset = UNSET,
    bbox_name_lte: str | Unset = UNSET,
    bbox_name_range: list[str] | Unset = UNSET,
    bbox_name_regex: str | Unset = UNSET,
    bbox_name_startswith: str | Unset = UNSET,
    east_bound_longitude: float | Unset = UNSET,
    east_bound_longitude_contained_by: float | Unset = UNSET,
    east_bound_longitude_contains: float | Unset = UNSET,
    east_bound_longitude_endswith: float | Unset = UNSET,
    east_bound_longitude_gt: float | Unset = UNSET,
    east_bound_longitude_gte: float | Unset = UNSET,
    east_bound_longitude_icontains: float | Unset = UNSET,
    east_bound_longitude_iendswith: float | Unset = UNSET,
    east_bound_longitude_iexact: float | Unset = UNSET,
    east_bound_longitude_in: list[float] | Unset = UNSET,
    east_bound_longitude_iregex: float | Unset = UNSET,
    east_bound_longitude_isnull: bool | Unset = UNSET,
    east_bound_longitude_istartswith: float | Unset = UNSET,
    east_bound_longitude_lt: float | Unset = UNSET,
    east_bound_longitude_lte: float | Unset = UNSET,
    east_bound_longitude_range: list[float] | Unset = UNSET,
    east_bound_longitude_regex: float | Unset = UNSET,
    east_bound_longitude_startswith: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    north_bound_latitude: float | Unset = UNSET,
    north_bound_latitude_contained_by: float | Unset = UNSET,
    north_bound_latitude_contains: float | Unset = UNSET,
    north_bound_latitude_endswith: float | Unset = UNSET,
    north_bound_latitude_gt: float | Unset = UNSET,
    north_bound_latitude_gte: float | Unset = UNSET,
    north_bound_latitude_icontains: float | Unset = UNSET,
    north_bound_latitude_iendswith: float | Unset = UNSET,
    north_bound_latitude_iexact: float | Unset = UNSET,
    north_bound_latitude_in: list[float] | Unset = UNSET,
    north_bound_latitude_iregex: float | Unset = UNSET,
    north_bound_latitude_isnull: bool | Unset = UNSET,
    north_bound_latitude_istartswith: float | Unset = UNSET,
    north_bound_latitude_lt: float | Unset = UNSET,
    north_bound_latitude_lte: float | Unset = UNSET,
    north_bound_latitude_range: list[float] | Unset = UNSET,
    north_bound_latitude_regex: float | Unset = UNSET,
    north_bound_latitude_startswith: float | Unset = UNSET,
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
    platform: list[int] | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    south_bound_latitude: float | Unset = UNSET,
    south_bound_latitude_contained_by: float | Unset = UNSET,
    south_bound_latitude_contains: float | Unset = UNSET,
    south_bound_latitude_endswith: float | Unset = UNSET,
    south_bound_latitude_gt: float | Unset = UNSET,
    south_bound_latitude_gte: float | Unset = UNSET,
    south_bound_latitude_icontains: float | Unset = UNSET,
    south_bound_latitude_iendswith: float | Unset = UNSET,
    south_bound_latitude_iexact: float | Unset = UNSET,
    south_bound_latitude_in: list[float] | Unset = UNSET,
    south_bound_latitude_iregex: float | Unset = UNSET,
    south_bound_latitude_isnull: bool | Unset = UNSET,
    south_bound_latitude_istartswith: float | Unset = UNSET,
    south_bound_latitude_lt: float | Unset = UNSET,
    south_bound_latitude_lte: float | Unset = UNSET,
    south_bound_latitude_range: list[float] | Unset = UNSET,
    south_bound_latitude_regex: float | Unset = UNSET,
    south_bound_latitude_startswith: float | Unset = UNSET,
    west_bound_longitude: float | Unset = UNSET,
    west_bound_longitude_contained_by: float | Unset = UNSET,
    west_bound_longitude_contains: float | Unset = UNSET,
    west_bound_longitude_endswith: float | Unset = UNSET,
    west_bound_longitude_gt: float | Unset = UNSET,
    west_bound_longitude_gte: float | Unset = UNSET,
    west_bound_longitude_icontains: float | Unset = UNSET,
    west_bound_longitude_iendswith: float | Unset = UNSET,
    west_bound_longitude_iexact: float | Unset = UNSET,
    west_bound_longitude_in: list[float] | Unset = UNSET,
    west_bound_longitude_iregex: float | Unset = UNSET,
    west_bound_longitude_isnull: bool | Unset = UNSET,
    west_bound_longitude_istartswith: float | Unset = UNSET,
    west_bound_longitude_lt: float | Unset = UNSET,
    west_bound_longitude_lte: float | Unset = UNSET,
    west_bound_longitude_range: list[float] | Unset = UNSET,
    west_bound_longitude_regex: float | Unset = UNSET,
    west_bound_longitude_startswith: float | Unset = UNSET,
) -> Response[PaginatedGeographicBoundingBoxReadList]:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        bbox_name (str | Unset):
        bbox_name_contains (str | Unset):
        bbox_name_endswith (str | Unset):
        bbox_name_gt (str | Unset):
        bbox_name_gte (str | Unset):
        bbox_name_icontains (str | Unset):
        bbox_name_iendswith (str | Unset):
        bbox_name_iexact (str | Unset):
        bbox_name_in (list[str] | Unset):
        bbox_name_iregex (str | Unset):
        bbox_name_isnull (bool | Unset):
        bbox_name_istartswith (str | Unset):
        bbox_name_lt (str | Unset):
        bbox_name_lte (str | Unset):
        bbox_name_range (list[str] | Unset):
        bbox_name_regex (str | Unset):
        bbox_name_startswith (str | Unset):
        east_bound_longitude (float | Unset):
        east_bound_longitude_contained_by (float | Unset):
        east_bound_longitude_contains (float | Unset):
        east_bound_longitude_endswith (float | Unset):
        east_bound_longitude_gt (float | Unset):
        east_bound_longitude_gte (float | Unset):
        east_bound_longitude_icontains (float | Unset):
        east_bound_longitude_iendswith (float | Unset):
        east_bound_longitude_iexact (float | Unset):
        east_bound_longitude_in (list[float] | Unset):
        east_bound_longitude_iregex (float | Unset):
        east_bound_longitude_isnull (bool | Unset):
        east_bound_longitude_istartswith (float | Unset):
        east_bound_longitude_lt (float | Unset):
        east_bound_longitude_lte (float | Unset):
        east_bound_longitude_range (list[float] | Unset):
        east_bound_longitude_regex (float | Unset):
        east_bound_longitude_startswith (float | Unset):
        limit (int | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        north_bound_latitude (float | Unset):
        north_bound_latitude_contained_by (float | Unset):
        north_bound_latitude_contains (float | Unset):
        north_bound_latitude_endswith (float | Unset):
        north_bound_latitude_gt (float | Unset):
        north_bound_latitude_gte (float | Unset):
        north_bound_latitude_icontains (float | Unset):
        north_bound_latitude_iendswith (float | Unset):
        north_bound_latitude_iexact (float | Unset):
        north_bound_latitude_in (list[float] | Unset):
        north_bound_latitude_iregex (float | Unset):
        north_bound_latitude_isnull (bool | Unset):
        north_bound_latitude_istartswith (float | Unset):
        north_bound_latitude_lt (float | Unset):
        north_bound_latitude_lte (float | Unset):
        north_bound_latitude_range (list[float] | Unset):
        north_bound_latitude_regex (float | Unset):
        north_bound_latitude_startswith (float | Unset):
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
        platform (list[int] | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        south_bound_latitude (float | Unset):
        south_bound_latitude_contained_by (float | Unset):
        south_bound_latitude_contains (float | Unset):
        south_bound_latitude_endswith (float | Unset):
        south_bound_latitude_gt (float | Unset):
        south_bound_latitude_gte (float | Unset):
        south_bound_latitude_icontains (float | Unset):
        south_bound_latitude_iendswith (float | Unset):
        south_bound_latitude_iexact (float | Unset):
        south_bound_latitude_in (list[float] | Unset):
        south_bound_latitude_iregex (float | Unset):
        south_bound_latitude_isnull (bool | Unset):
        south_bound_latitude_istartswith (float | Unset):
        south_bound_latitude_lt (float | Unset):
        south_bound_latitude_lte (float | Unset):
        south_bound_latitude_range (list[float] | Unset):
        south_bound_latitude_regex (float | Unset):
        south_bound_latitude_startswith (float | Unset):
        west_bound_longitude (float | Unset):
        west_bound_longitude_contained_by (float | Unset):
        west_bound_longitude_contains (float | Unset):
        west_bound_longitude_endswith (float | Unset):
        west_bound_longitude_gt (float | Unset):
        west_bound_longitude_gte (float | Unset):
        west_bound_longitude_icontains (float | Unset):
        west_bound_longitude_iendswith (float | Unset):
        west_bound_longitude_iexact (float | Unset):
        west_bound_longitude_in (list[float] | Unset):
        west_bound_longitude_iregex (float | Unset):
        west_bound_longitude_isnull (bool | Unset):
        west_bound_longitude_istartswith (float | Unset):
        west_bound_longitude_lt (float | Unset):
        west_bound_longitude_lte (float | Unset):
        west_bound_longitude_range (list[float] | Unset):
        west_bound_longitude_regex (float | Unset):
        west_bound_longitude_startswith (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedGeographicBoundingBoxReadList]
    """

    kwargs = _get_kwargs(
        bbox_name=bbox_name,
        bbox_name_contains=bbox_name_contains,
        bbox_name_endswith=bbox_name_endswith,
        bbox_name_gt=bbox_name_gt,
        bbox_name_gte=bbox_name_gte,
        bbox_name_icontains=bbox_name_icontains,
        bbox_name_iendswith=bbox_name_iendswith,
        bbox_name_iexact=bbox_name_iexact,
        bbox_name_in=bbox_name_in,
        bbox_name_iregex=bbox_name_iregex,
        bbox_name_isnull=bbox_name_isnull,
        bbox_name_istartswith=bbox_name_istartswith,
        bbox_name_lt=bbox_name_lt,
        bbox_name_lte=bbox_name_lte,
        bbox_name_range=bbox_name_range,
        bbox_name_regex=bbox_name_regex,
        bbox_name_startswith=bbox_name_startswith,
        east_bound_longitude=east_bound_longitude,
        east_bound_longitude_contained_by=east_bound_longitude_contained_by,
        east_bound_longitude_contains=east_bound_longitude_contains,
        east_bound_longitude_endswith=east_bound_longitude_endswith,
        east_bound_longitude_gt=east_bound_longitude_gt,
        east_bound_longitude_gte=east_bound_longitude_gte,
        east_bound_longitude_icontains=east_bound_longitude_icontains,
        east_bound_longitude_iendswith=east_bound_longitude_iendswith,
        east_bound_longitude_iexact=east_bound_longitude_iexact,
        east_bound_longitude_in=east_bound_longitude_in,
        east_bound_longitude_iregex=east_bound_longitude_iregex,
        east_bound_longitude_isnull=east_bound_longitude_isnull,
        east_bound_longitude_istartswith=east_bound_longitude_istartswith,
        east_bound_longitude_lt=east_bound_longitude_lt,
        east_bound_longitude_lte=east_bound_longitude_lte,
        east_bound_longitude_range=east_bound_longitude_range,
        east_bound_longitude_regex=east_bound_longitude_regex,
        east_bound_longitude_startswith=east_bound_longitude_startswith,
        limit=limit,
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
        north_bound_latitude=north_bound_latitude,
        north_bound_latitude_contained_by=north_bound_latitude_contained_by,
        north_bound_latitude_contains=north_bound_latitude_contains,
        north_bound_latitude_endswith=north_bound_latitude_endswith,
        north_bound_latitude_gt=north_bound_latitude_gt,
        north_bound_latitude_gte=north_bound_latitude_gte,
        north_bound_latitude_icontains=north_bound_latitude_icontains,
        north_bound_latitude_iendswith=north_bound_latitude_iendswith,
        north_bound_latitude_iexact=north_bound_latitude_iexact,
        north_bound_latitude_in=north_bound_latitude_in,
        north_bound_latitude_iregex=north_bound_latitude_iregex,
        north_bound_latitude_isnull=north_bound_latitude_isnull,
        north_bound_latitude_istartswith=north_bound_latitude_istartswith,
        north_bound_latitude_lt=north_bound_latitude_lt,
        north_bound_latitude_lte=north_bound_latitude_lte,
        north_bound_latitude_range=north_bound_latitude_range,
        north_bound_latitude_regex=north_bound_latitude_regex,
        north_bound_latitude_startswith=north_bound_latitude_startswith,
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
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        south_bound_latitude=south_bound_latitude,
        south_bound_latitude_contained_by=south_bound_latitude_contained_by,
        south_bound_latitude_contains=south_bound_latitude_contains,
        south_bound_latitude_endswith=south_bound_latitude_endswith,
        south_bound_latitude_gt=south_bound_latitude_gt,
        south_bound_latitude_gte=south_bound_latitude_gte,
        south_bound_latitude_icontains=south_bound_latitude_icontains,
        south_bound_latitude_iendswith=south_bound_latitude_iendswith,
        south_bound_latitude_iexact=south_bound_latitude_iexact,
        south_bound_latitude_in=south_bound_latitude_in,
        south_bound_latitude_iregex=south_bound_latitude_iregex,
        south_bound_latitude_isnull=south_bound_latitude_isnull,
        south_bound_latitude_istartswith=south_bound_latitude_istartswith,
        south_bound_latitude_lt=south_bound_latitude_lt,
        south_bound_latitude_lte=south_bound_latitude_lte,
        south_bound_latitude_range=south_bound_latitude_range,
        south_bound_latitude_regex=south_bound_latitude_regex,
        south_bound_latitude_startswith=south_bound_latitude_startswith,
        west_bound_longitude=west_bound_longitude,
        west_bound_longitude_contained_by=west_bound_longitude_contained_by,
        west_bound_longitude_contains=west_bound_longitude_contains,
        west_bound_longitude_endswith=west_bound_longitude_endswith,
        west_bound_longitude_gt=west_bound_longitude_gt,
        west_bound_longitude_gte=west_bound_longitude_gte,
        west_bound_longitude_icontains=west_bound_longitude_icontains,
        west_bound_longitude_iendswith=west_bound_longitude_iendswith,
        west_bound_longitude_iexact=west_bound_longitude_iexact,
        west_bound_longitude_in=west_bound_longitude_in,
        west_bound_longitude_iregex=west_bound_longitude_iregex,
        west_bound_longitude_isnull=west_bound_longitude_isnull,
        west_bound_longitude_istartswith=west_bound_longitude_istartswith,
        west_bound_longitude_lt=west_bound_longitude_lt,
        west_bound_longitude_lte=west_bound_longitude_lte,
        west_bound_longitude_range=west_bound_longitude_range,
        west_bound_longitude_regex=west_bound_longitude_regex,
        west_bound_longitude_startswith=west_bound_longitude_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    bbox_name: str | Unset = UNSET,
    bbox_name_contains: str | Unset = UNSET,
    bbox_name_endswith: str | Unset = UNSET,
    bbox_name_gt: str | Unset = UNSET,
    bbox_name_gte: str | Unset = UNSET,
    bbox_name_icontains: str | Unset = UNSET,
    bbox_name_iendswith: str | Unset = UNSET,
    bbox_name_iexact: str | Unset = UNSET,
    bbox_name_in: list[str] | Unset = UNSET,
    bbox_name_iregex: str | Unset = UNSET,
    bbox_name_isnull: bool | Unset = UNSET,
    bbox_name_istartswith: str | Unset = UNSET,
    bbox_name_lt: str | Unset = UNSET,
    bbox_name_lte: str | Unset = UNSET,
    bbox_name_range: list[str] | Unset = UNSET,
    bbox_name_regex: str | Unset = UNSET,
    bbox_name_startswith: str | Unset = UNSET,
    east_bound_longitude: float | Unset = UNSET,
    east_bound_longitude_contained_by: float | Unset = UNSET,
    east_bound_longitude_contains: float | Unset = UNSET,
    east_bound_longitude_endswith: float | Unset = UNSET,
    east_bound_longitude_gt: float | Unset = UNSET,
    east_bound_longitude_gte: float | Unset = UNSET,
    east_bound_longitude_icontains: float | Unset = UNSET,
    east_bound_longitude_iendswith: float | Unset = UNSET,
    east_bound_longitude_iexact: float | Unset = UNSET,
    east_bound_longitude_in: list[float] | Unset = UNSET,
    east_bound_longitude_iregex: float | Unset = UNSET,
    east_bound_longitude_isnull: bool | Unset = UNSET,
    east_bound_longitude_istartswith: float | Unset = UNSET,
    east_bound_longitude_lt: float | Unset = UNSET,
    east_bound_longitude_lte: float | Unset = UNSET,
    east_bound_longitude_range: list[float] | Unset = UNSET,
    east_bound_longitude_regex: float | Unset = UNSET,
    east_bound_longitude_startswith: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    north_bound_latitude: float | Unset = UNSET,
    north_bound_latitude_contained_by: float | Unset = UNSET,
    north_bound_latitude_contains: float | Unset = UNSET,
    north_bound_latitude_endswith: float | Unset = UNSET,
    north_bound_latitude_gt: float | Unset = UNSET,
    north_bound_latitude_gte: float | Unset = UNSET,
    north_bound_latitude_icontains: float | Unset = UNSET,
    north_bound_latitude_iendswith: float | Unset = UNSET,
    north_bound_latitude_iexact: float | Unset = UNSET,
    north_bound_latitude_in: list[float] | Unset = UNSET,
    north_bound_latitude_iregex: float | Unset = UNSET,
    north_bound_latitude_isnull: bool | Unset = UNSET,
    north_bound_latitude_istartswith: float | Unset = UNSET,
    north_bound_latitude_lt: float | Unset = UNSET,
    north_bound_latitude_lte: float | Unset = UNSET,
    north_bound_latitude_range: list[float] | Unset = UNSET,
    north_bound_latitude_regex: float | Unset = UNSET,
    north_bound_latitude_startswith: float | Unset = UNSET,
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
    platform: list[int] | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    south_bound_latitude: float | Unset = UNSET,
    south_bound_latitude_contained_by: float | Unset = UNSET,
    south_bound_latitude_contains: float | Unset = UNSET,
    south_bound_latitude_endswith: float | Unset = UNSET,
    south_bound_latitude_gt: float | Unset = UNSET,
    south_bound_latitude_gte: float | Unset = UNSET,
    south_bound_latitude_icontains: float | Unset = UNSET,
    south_bound_latitude_iendswith: float | Unset = UNSET,
    south_bound_latitude_iexact: float | Unset = UNSET,
    south_bound_latitude_in: list[float] | Unset = UNSET,
    south_bound_latitude_iregex: float | Unset = UNSET,
    south_bound_latitude_isnull: bool | Unset = UNSET,
    south_bound_latitude_istartswith: float | Unset = UNSET,
    south_bound_latitude_lt: float | Unset = UNSET,
    south_bound_latitude_lte: float | Unset = UNSET,
    south_bound_latitude_range: list[float] | Unset = UNSET,
    south_bound_latitude_regex: float | Unset = UNSET,
    south_bound_latitude_startswith: float | Unset = UNSET,
    west_bound_longitude: float | Unset = UNSET,
    west_bound_longitude_contained_by: float | Unset = UNSET,
    west_bound_longitude_contains: float | Unset = UNSET,
    west_bound_longitude_endswith: float | Unset = UNSET,
    west_bound_longitude_gt: float | Unset = UNSET,
    west_bound_longitude_gte: float | Unset = UNSET,
    west_bound_longitude_icontains: float | Unset = UNSET,
    west_bound_longitude_iendswith: float | Unset = UNSET,
    west_bound_longitude_iexact: float | Unset = UNSET,
    west_bound_longitude_in: list[float] | Unset = UNSET,
    west_bound_longitude_iregex: float | Unset = UNSET,
    west_bound_longitude_isnull: bool | Unset = UNSET,
    west_bound_longitude_istartswith: float | Unset = UNSET,
    west_bound_longitude_lt: float | Unset = UNSET,
    west_bound_longitude_lte: float | Unset = UNSET,
    west_bound_longitude_range: list[float] | Unset = UNSET,
    west_bound_longitude_regex: float | Unset = UNSET,
    west_bound_longitude_startswith: float | Unset = UNSET,
) -> PaginatedGeographicBoundingBoxReadList | None:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        bbox_name (str | Unset):
        bbox_name_contains (str | Unset):
        bbox_name_endswith (str | Unset):
        bbox_name_gt (str | Unset):
        bbox_name_gte (str | Unset):
        bbox_name_icontains (str | Unset):
        bbox_name_iendswith (str | Unset):
        bbox_name_iexact (str | Unset):
        bbox_name_in (list[str] | Unset):
        bbox_name_iregex (str | Unset):
        bbox_name_isnull (bool | Unset):
        bbox_name_istartswith (str | Unset):
        bbox_name_lt (str | Unset):
        bbox_name_lte (str | Unset):
        bbox_name_range (list[str] | Unset):
        bbox_name_regex (str | Unset):
        bbox_name_startswith (str | Unset):
        east_bound_longitude (float | Unset):
        east_bound_longitude_contained_by (float | Unset):
        east_bound_longitude_contains (float | Unset):
        east_bound_longitude_endswith (float | Unset):
        east_bound_longitude_gt (float | Unset):
        east_bound_longitude_gte (float | Unset):
        east_bound_longitude_icontains (float | Unset):
        east_bound_longitude_iendswith (float | Unset):
        east_bound_longitude_iexact (float | Unset):
        east_bound_longitude_in (list[float] | Unset):
        east_bound_longitude_iregex (float | Unset):
        east_bound_longitude_isnull (bool | Unset):
        east_bound_longitude_istartswith (float | Unset):
        east_bound_longitude_lt (float | Unset):
        east_bound_longitude_lte (float | Unset):
        east_bound_longitude_range (list[float] | Unset):
        east_bound_longitude_regex (float | Unset):
        east_bound_longitude_startswith (float | Unset):
        limit (int | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        north_bound_latitude (float | Unset):
        north_bound_latitude_contained_by (float | Unset):
        north_bound_latitude_contains (float | Unset):
        north_bound_latitude_endswith (float | Unset):
        north_bound_latitude_gt (float | Unset):
        north_bound_latitude_gte (float | Unset):
        north_bound_latitude_icontains (float | Unset):
        north_bound_latitude_iendswith (float | Unset):
        north_bound_latitude_iexact (float | Unset):
        north_bound_latitude_in (list[float] | Unset):
        north_bound_latitude_iregex (float | Unset):
        north_bound_latitude_isnull (bool | Unset):
        north_bound_latitude_istartswith (float | Unset):
        north_bound_latitude_lt (float | Unset):
        north_bound_latitude_lte (float | Unset):
        north_bound_latitude_range (list[float] | Unset):
        north_bound_latitude_regex (float | Unset):
        north_bound_latitude_startswith (float | Unset):
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
        platform (list[int] | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        south_bound_latitude (float | Unset):
        south_bound_latitude_contained_by (float | Unset):
        south_bound_latitude_contains (float | Unset):
        south_bound_latitude_endswith (float | Unset):
        south_bound_latitude_gt (float | Unset):
        south_bound_latitude_gte (float | Unset):
        south_bound_latitude_icontains (float | Unset):
        south_bound_latitude_iendswith (float | Unset):
        south_bound_latitude_iexact (float | Unset):
        south_bound_latitude_in (list[float] | Unset):
        south_bound_latitude_iregex (float | Unset):
        south_bound_latitude_isnull (bool | Unset):
        south_bound_latitude_istartswith (float | Unset):
        south_bound_latitude_lt (float | Unset):
        south_bound_latitude_lte (float | Unset):
        south_bound_latitude_range (list[float] | Unset):
        south_bound_latitude_regex (float | Unset):
        south_bound_latitude_startswith (float | Unset):
        west_bound_longitude (float | Unset):
        west_bound_longitude_contained_by (float | Unset):
        west_bound_longitude_contains (float | Unset):
        west_bound_longitude_endswith (float | Unset):
        west_bound_longitude_gt (float | Unset):
        west_bound_longitude_gte (float | Unset):
        west_bound_longitude_icontains (float | Unset):
        west_bound_longitude_iendswith (float | Unset):
        west_bound_longitude_iexact (float | Unset):
        west_bound_longitude_in (list[float] | Unset):
        west_bound_longitude_iregex (float | Unset):
        west_bound_longitude_isnull (bool | Unset):
        west_bound_longitude_istartswith (float | Unset):
        west_bound_longitude_lt (float | Unset):
        west_bound_longitude_lte (float | Unset):
        west_bound_longitude_range (list[float] | Unset):
        west_bound_longitude_regex (float | Unset):
        west_bound_longitude_startswith (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedGeographicBoundingBoxReadList
    """

    return sync_detailed(
        client=client,
        bbox_name=bbox_name,
        bbox_name_contains=bbox_name_contains,
        bbox_name_endswith=bbox_name_endswith,
        bbox_name_gt=bbox_name_gt,
        bbox_name_gte=bbox_name_gte,
        bbox_name_icontains=bbox_name_icontains,
        bbox_name_iendswith=bbox_name_iendswith,
        bbox_name_iexact=bbox_name_iexact,
        bbox_name_in=bbox_name_in,
        bbox_name_iregex=bbox_name_iregex,
        bbox_name_isnull=bbox_name_isnull,
        bbox_name_istartswith=bbox_name_istartswith,
        bbox_name_lt=bbox_name_lt,
        bbox_name_lte=bbox_name_lte,
        bbox_name_range=bbox_name_range,
        bbox_name_regex=bbox_name_regex,
        bbox_name_startswith=bbox_name_startswith,
        east_bound_longitude=east_bound_longitude,
        east_bound_longitude_contained_by=east_bound_longitude_contained_by,
        east_bound_longitude_contains=east_bound_longitude_contains,
        east_bound_longitude_endswith=east_bound_longitude_endswith,
        east_bound_longitude_gt=east_bound_longitude_gt,
        east_bound_longitude_gte=east_bound_longitude_gte,
        east_bound_longitude_icontains=east_bound_longitude_icontains,
        east_bound_longitude_iendswith=east_bound_longitude_iendswith,
        east_bound_longitude_iexact=east_bound_longitude_iexact,
        east_bound_longitude_in=east_bound_longitude_in,
        east_bound_longitude_iregex=east_bound_longitude_iregex,
        east_bound_longitude_isnull=east_bound_longitude_isnull,
        east_bound_longitude_istartswith=east_bound_longitude_istartswith,
        east_bound_longitude_lt=east_bound_longitude_lt,
        east_bound_longitude_lte=east_bound_longitude_lte,
        east_bound_longitude_range=east_bound_longitude_range,
        east_bound_longitude_regex=east_bound_longitude_regex,
        east_bound_longitude_startswith=east_bound_longitude_startswith,
        limit=limit,
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
        north_bound_latitude=north_bound_latitude,
        north_bound_latitude_contained_by=north_bound_latitude_contained_by,
        north_bound_latitude_contains=north_bound_latitude_contains,
        north_bound_latitude_endswith=north_bound_latitude_endswith,
        north_bound_latitude_gt=north_bound_latitude_gt,
        north_bound_latitude_gte=north_bound_latitude_gte,
        north_bound_latitude_icontains=north_bound_latitude_icontains,
        north_bound_latitude_iendswith=north_bound_latitude_iendswith,
        north_bound_latitude_iexact=north_bound_latitude_iexact,
        north_bound_latitude_in=north_bound_latitude_in,
        north_bound_latitude_iregex=north_bound_latitude_iregex,
        north_bound_latitude_isnull=north_bound_latitude_isnull,
        north_bound_latitude_istartswith=north_bound_latitude_istartswith,
        north_bound_latitude_lt=north_bound_latitude_lt,
        north_bound_latitude_lte=north_bound_latitude_lte,
        north_bound_latitude_range=north_bound_latitude_range,
        north_bound_latitude_regex=north_bound_latitude_regex,
        north_bound_latitude_startswith=north_bound_latitude_startswith,
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
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        south_bound_latitude=south_bound_latitude,
        south_bound_latitude_contained_by=south_bound_latitude_contained_by,
        south_bound_latitude_contains=south_bound_latitude_contains,
        south_bound_latitude_endswith=south_bound_latitude_endswith,
        south_bound_latitude_gt=south_bound_latitude_gt,
        south_bound_latitude_gte=south_bound_latitude_gte,
        south_bound_latitude_icontains=south_bound_latitude_icontains,
        south_bound_latitude_iendswith=south_bound_latitude_iendswith,
        south_bound_latitude_iexact=south_bound_latitude_iexact,
        south_bound_latitude_in=south_bound_latitude_in,
        south_bound_latitude_iregex=south_bound_latitude_iregex,
        south_bound_latitude_isnull=south_bound_latitude_isnull,
        south_bound_latitude_istartswith=south_bound_latitude_istartswith,
        south_bound_latitude_lt=south_bound_latitude_lt,
        south_bound_latitude_lte=south_bound_latitude_lte,
        south_bound_latitude_range=south_bound_latitude_range,
        south_bound_latitude_regex=south_bound_latitude_regex,
        south_bound_latitude_startswith=south_bound_latitude_startswith,
        west_bound_longitude=west_bound_longitude,
        west_bound_longitude_contained_by=west_bound_longitude_contained_by,
        west_bound_longitude_contains=west_bound_longitude_contains,
        west_bound_longitude_endswith=west_bound_longitude_endswith,
        west_bound_longitude_gt=west_bound_longitude_gt,
        west_bound_longitude_gte=west_bound_longitude_gte,
        west_bound_longitude_icontains=west_bound_longitude_icontains,
        west_bound_longitude_iendswith=west_bound_longitude_iendswith,
        west_bound_longitude_iexact=west_bound_longitude_iexact,
        west_bound_longitude_in=west_bound_longitude_in,
        west_bound_longitude_iregex=west_bound_longitude_iregex,
        west_bound_longitude_isnull=west_bound_longitude_isnull,
        west_bound_longitude_istartswith=west_bound_longitude_istartswith,
        west_bound_longitude_lt=west_bound_longitude_lt,
        west_bound_longitude_lte=west_bound_longitude_lte,
        west_bound_longitude_range=west_bound_longitude_range,
        west_bound_longitude_regex=west_bound_longitude_regex,
        west_bound_longitude_startswith=west_bound_longitude_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    bbox_name: str | Unset = UNSET,
    bbox_name_contains: str | Unset = UNSET,
    bbox_name_endswith: str | Unset = UNSET,
    bbox_name_gt: str | Unset = UNSET,
    bbox_name_gte: str | Unset = UNSET,
    bbox_name_icontains: str | Unset = UNSET,
    bbox_name_iendswith: str | Unset = UNSET,
    bbox_name_iexact: str | Unset = UNSET,
    bbox_name_in: list[str] | Unset = UNSET,
    bbox_name_iregex: str | Unset = UNSET,
    bbox_name_isnull: bool | Unset = UNSET,
    bbox_name_istartswith: str | Unset = UNSET,
    bbox_name_lt: str | Unset = UNSET,
    bbox_name_lte: str | Unset = UNSET,
    bbox_name_range: list[str] | Unset = UNSET,
    bbox_name_regex: str | Unset = UNSET,
    bbox_name_startswith: str | Unset = UNSET,
    east_bound_longitude: float | Unset = UNSET,
    east_bound_longitude_contained_by: float | Unset = UNSET,
    east_bound_longitude_contains: float | Unset = UNSET,
    east_bound_longitude_endswith: float | Unset = UNSET,
    east_bound_longitude_gt: float | Unset = UNSET,
    east_bound_longitude_gte: float | Unset = UNSET,
    east_bound_longitude_icontains: float | Unset = UNSET,
    east_bound_longitude_iendswith: float | Unset = UNSET,
    east_bound_longitude_iexact: float | Unset = UNSET,
    east_bound_longitude_in: list[float] | Unset = UNSET,
    east_bound_longitude_iregex: float | Unset = UNSET,
    east_bound_longitude_isnull: bool | Unset = UNSET,
    east_bound_longitude_istartswith: float | Unset = UNSET,
    east_bound_longitude_lt: float | Unset = UNSET,
    east_bound_longitude_lte: float | Unset = UNSET,
    east_bound_longitude_range: list[float] | Unset = UNSET,
    east_bound_longitude_regex: float | Unset = UNSET,
    east_bound_longitude_startswith: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    north_bound_latitude: float | Unset = UNSET,
    north_bound_latitude_contained_by: float | Unset = UNSET,
    north_bound_latitude_contains: float | Unset = UNSET,
    north_bound_latitude_endswith: float | Unset = UNSET,
    north_bound_latitude_gt: float | Unset = UNSET,
    north_bound_latitude_gte: float | Unset = UNSET,
    north_bound_latitude_icontains: float | Unset = UNSET,
    north_bound_latitude_iendswith: float | Unset = UNSET,
    north_bound_latitude_iexact: float | Unset = UNSET,
    north_bound_latitude_in: list[float] | Unset = UNSET,
    north_bound_latitude_iregex: float | Unset = UNSET,
    north_bound_latitude_isnull: bool | Unset = UNSET,
    north_bound_latitude_istartswith: float | Unset = UNSET,
    north_bound_latitude_lt: float | Unset = UNSET,
    north_bound_latitude_lte: float | Unset = UNSET,
    north_bound_latitude_range: list[float] | Unset = UNSET,
    north_bound_latitude_regex: float | Unset = UNSET,
    north_bound_latitude_startswith: float | Unset = UNSET,
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
    platform: list[int] | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    south_bound_latitude: float | Unset = UNSET,
    south_bound_latitude_contained_by: float | Unset = UNSET,
    south_bound_latitude_contains: float | Unset = UNSET,
    south_bound_latitude_endswith: float | Unset = UNSET,
    south_bound_latitude_gt: float | Unset = UNSET,
    south_bound_latitude_gte: float | Unset = UNSET,
    south_bound_latitude_icontains: float | Unset = UNSET,
    south_bound_latitude_iendswith: float | Unset = UNSET,
    south_bound_latitude_iexact: float | Unset = UNSET,
    south_bound_latitude_in: list[float] | Unset = UNSET,
    south_bound_latitude_iregex: float | Unset = UNSET,
    south_bound_latitude_isnull: bool | Unset = UNSET,
    south_bound_latitude_istartswith: float | Unset = UNSET,
    south_bound_latitude_lt: float | Unset = UNSET,
    south_bound_latitude_lte: float | Unset = UNSET,
    south_bound_latitude_range: list[float] | Unset = UNSET,
    south_bound_latitude_regex: float | Unset = UNSET,
    south_bound_latitude_startswith: float | Unset = UNSET,
    west_bound_longitude: float | Unset = UNSET,
    west_bound_longitude_contained_by: float | Unset = UNSET,
    west_bound_longitude_contains: float | Unset = UNSET,
    west_bound_longitude_endswith: float | Unset = UNSET,
    west_bound_longitude_gt: float | Unset = UNSET,
    west_bound_longitude_gte: float | Unset = UNSET,
    west_bound_longitude_icontains: float | Unset = UNSET,
    west_bound_longitude_iendswith: float | Unset = UNSET,
    west_bound_longitude_iexact: float | Unset = UNSET,
    west_bound_longitude_in: list[float] | Unset = UNSET,
    west_bound_longitude_iregex: float | Unset = UNSET,
    west_bound_longitude_isnull: bool | Unset = UNSET,
    west_bound_longitude_istartswith: float | Unset = UNSET,
    west_bound_longitude_lt: float | Unset = UNSET,
    west_bound_longitude_lte: float | Unset = UNSET,
    west_bound_longitude_range: list[float] | Unset = UNSET,
    west_bound_longitude_regex: float | Unset = UNSET,
    west_bound_longitude_startswith: float | Unset = UNSET,
) -> Response[PaginatedGeographicBoundingBoxReadList]:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        bbox_name (str | Unset):
        bbox_name_contains (str | Unset):
        bbox_name_endswith (str | Unset):
        bbox_name_gt (str | Unset):
        bbox_name_gte (str | Unset):
        bbox_name_icontains (str | Unset):
        bbox_name_iendswith (str | Unset):
        bbox_name_iexact (str | Unset):
        bbox_name_in (list[str] | Unset):
        bbox_name_iregex (str | Unset):
        bbox_name_isnull (bool | Unset):
        bbox_name_istartswith (str | Unset):
        bbox_name_lt (str | Unset):
        bbox_name_lte (str | Unset):
        bbox_name_range (list[str] | Unset):
        bbox_name_regex (str | Unset):
        bbox_name_startswith (str | Unset):
        east_bound_longitude (float | Unset):
        east_bound_longitude_contained_by (float | Unset):
        east_bound_longitude_contains (float | Unset):
        east_bound_longitude_endswith (float | Unset):
        east_bound_longitude_gt (float | Unset):
        east_bound_longitude_gte (float | Unset):
        east_bound_longitude_icontains (float | Unset):
        east_bound_longitude_iendswith (float | Unset):
        east_bound_longitude_iexact (float | Unset):
        east_bound_longitude_in (list[float] | Unset):
        east_bound_longitude_iregex (float | Unset):
        east_bound_longitude_isnull (bool | Unset):
        east_bound_longitude_istartswith (float | Unset):
        east_bound_longitude_lt (float | Unset):
        east_bound_longitude_lte (float | Unset):
        east_bound_longitude_range (list[float] | Unset):
        east_bound_longitude_regex (float | Unset):
        east_bound_longitude_startswith (float | Unset):
        limit (int | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        north_bound_latitude (float | Unset):
        north_bound_latitude_contained_by (float | Unset):
        north_bound_latitude_contains (float | Unset):
        north_bound_latitude_endswith (float | Unset):
        north_bound_latitude_gt (float | Unset):
        north_bound_latitude_gte (float | Unset):
        north_bound_latitude_icontains (float | Unset):
        north_bound_latitude_iendswith (float | Unset):
        north_bound_latitude_iexact (float | Unset):
        north_bound_latitude_in (list[float] | Unset):
        north_bound_latitude_iregex (float | Unset):
        north_bound_latitude_isnull (bool | Unset):
        north_bound_latitude_istartswith (float | Unset):
        north_bound_latitude_lt (float | Unset):
        north_bound_latitude_lte (float | Unset):
        north_bound_latitude_range (list[float] | Unset):
        north_bound_latitude_regex (float | Unset):
        north_bound_latitude_startswith (float | Unset):
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
        platform (list[int] | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        south_bound_latitude (float | Unset):
        south_bound_latitude_contained_by (float | Unset):
        south_bound_latitude_contains (float | Unset):
        south_bound_latitude_endswith (float | Unset):
        south_bound_latitude_gt (float | Unset):
        south_bound_latitude_gte (float | Unset):
        south_bound_latitude_icontains (float | Unset):
        south_bound_latitude_iendswith (float | Unset):
        south_bound_latitude_iexact (float | Unset):
        south_bound_latitude_in (list[float] | Unset):
        south_bound_latitude_iregex (float | Unset):
        south_bound_latitude_isnull (bool | Unset):
        south_bound_latitude_istartswith (float | Unset):
        south_bound_latitude_lt (float | Unset):
        south_bound_latitude_lte (float | Unset):
        south_bound_latitude_range (list[float] | Unset):
        south_bound_latitude_regex (float | Unset):
        south_bound_latitude_startswith (float | Unset):
        west_bound_longitude (float | Unset):
        west_bound_longitude_contained_by (float | Unset):
        west_bound_longitude_contains (float | Unset):
        west_bound_longitude_endswith (float | Unset):
        west_bound_longitude_gt (float | Unset):
        west_bound_longitude_gte (float | Unset):
        west_bound_longitude_icontains (float | Unset):
        west_bound_longitude_iendswith (float | Unset):
        west_bound_longitude_iexact (float | Unset):
        west_bound_longitude_in (list[float] | Unset):
        west_bound_longitude_iregex (float | Unset):
        west_bound_longitude_isnull (bool | Unset):
        west_bound_longitude_istartswith (float | Unset):
        west_bound_longitude_lt (float | Unset):
        west_bound_longitude_lte (float | Unset):
        west_bound_longitude_range (list[float] | Unset):
        west_bound_longitude_regex (float | Unset):
        west_bound_longitude_startswith (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedGeographicBoundingBoxReadList]
    """

    kwargs = _get_kwargs(
        bbox_name=bbox_name,
        bbox_name_contains=bbox_name_contains,
        bbox_name_endswith=bbox_name_endswith,
        bbox_name_gt=bbox_name_gt,
        bbox_name_gte=bbox_name_gte,
        bbox_name_icontains=bbox_name_icontains,
        bbox_name_iendswith=bbox_name_iendswith,
        bbox_name_iexact=bbox_name_iexact,
        bbox_name_in=bbox_name_in,
        bbox_name_iregex=bbox_name_iregex,
        bbox_name_isnull=bbox_name_isnull,
        bbox_name_istartswith=bbox_name_istartswith,
        bbox_name_lt=bbox_name_lt,
        bbox_name_lte=bbox_name_lte,
        bbox_name_range=bbox_name_range,
        bbox_name_regex=bbox_name_regex,
        bbox_name_startswith=bbox_name_startswith,
        east_bound_longitude=east_bound_longitude,
        east_bound_longitude_contained_by=east_bound_longitude_contained_by,
        east_bound_longitude_contains=east_bound_longitude_contains,
        east_bound_longitude_endswith=east_bound_longitude_endswith,
        east_bound_longitude_gt=east_bound_longitude_gt,
        east_bound_longitude_gte=east_bound_longitude_gte,
        east_bound_longitude_icontains=east_bound_longitude_icontains,
        east_bound_longitude_iendswith=east_bound_longitude_iendswith,
        east_bound_longitude_iexact=east_bound_longitude_iexact,
        east_bound_longitude_in=east_bound_longitude_in,
        east_bound_longitude_iregex=east_bound_longitude_iregex,
        east_bound_longitude_isnull=east_bound_longitude_isnull,
        east_bound_longitude_istartswith=east_bound_longitude_istartswith,
        east_bound_longitude_lt=east_bound_longitude_lt,
        east_bound_longitude_lte=east_bound_longitude_lte,
        east_bound_longitude_range=east_bound_longitude_range,
        east_bound_longitude_regex=east_bound_longitude_regex,
        east_bound_longitude_startswith=east_bound_longitude_startswith,
        limit=limit,
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
        north_bound_latitude=north_bound_latitude,
        north_bound_latitude_contained_by=north_bound_latitude_contained_by,
        north_bound_latitude_contains=north_bound_latitude_contains,
        north_bound_latitude_endswith=north_bound_latitude_endswith,
        north_bound_latitude_gt=north_bound_latitude_gt,
        north_bound_latitude_gte=north_bound_latitude_gte,
        north_bound_latitude_icontains=north_bound_latitude_icontains,
        north_bound_latitude_iendswith=north_bound_latitude_iendswith,
        north_bound_latitude_iexact=north_bound_latitude_iexact,
        north_bound_latitude_in=north_bound_latitude_in,
        north_bound_latitude_iregex=north_bound_latitude_iregex,
        north_bound_latitude_isnull=north_bound_latitude_isnull,
        north_bound_latitude_istartswith=north_bound_latitude_istartswith,
        north_bound_latitude_lt=north_bound_latitude_lt,
        north_bound_latitude_lte=north_bound_latitude_lte,
        north_bound_latitude_range=north_bound_latitude_range,
        north_bound_latitude_regex=north_bound_latitude_regex,
        north_bound_latitude_startswith=north_bound_latitude_startswith,
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
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        south_bound_latitude=south_bound_latitude,
        south_bound_latitude_contained_by=south_bound_latitude_contained_by,
        south_bound_latitude_contains=south_bound_latitude_contains,
        south_bound_latitude_endswith=south_bound_latitude_endswith,
        south_bound_latitude_gt=south_bound_latitude_gt,
        south_bound_latitude_gte=south_bound_latitude_gte,
        south_bound_latitude_icontains=south_bound_latitude_icontains,
        south_bound_latitude_iendswith=south_bound_latitude_iendswith,
        south_bound_latitude_iexact=south_bound_latitude_iexact,
        south_bound_latitude_in=south_bound_latitude_in,
        south_bound_latitude_iregex=south_bound_latitude_iregex,
        south_bound_latitude_isnull=south_bound_latitude_isnull,
        south_bound_latitude_istartswith=south_bound_latitude_istartswith,
        south_bound_latitude_lt=south_bound_latitude_lt,
        south_bound_latitude_lte=south_bound_latitude_lte,
        south_bound_latitude_range=south_bound_latitude_range,
        south_bound_latitude_regex=south_bound_latitude_regex,
        south_bound_latitude_startswith=south_bound_latitude_startswith,
        west_bound_longitude=west_bound_longitude,
        west_bound_longitude_contained_by=west_bound_longitude_contained_by,
        west_bound_longitude_contains=west_bound_longitude_contains,
        west_bound_longitude_endswith=west_bound_longitude_endswith,
        west_bound_longitude_gt=west_bound_longitude_gt,
        west_bound_longitude_gte=west_bound_longitude_gte,
        west_bound_longitude_icontains=west_bound_longitude_icontains,
        west_bound_longitude_iendswith=west_bound_longitude_iendswith,
        west_bound_longitude_iexact=west_bound_longitude_iexact,
        west_bound_longitude_in=west_bound_longitude_in,
        west_bound_longitude_iregex=west_bound_longitude_iregex,
        west_bound_longitude_isnull=west_bound_longitude_isnull,
        west_bound_longitude_istartswith=west_bound_longitude_istartswith,
        west_bound_longitude_lt=west_bound_longitude_lt,
        west_bound_longitude_lte=west_bound_longitude_lte,
        west_bound_longitude_range=west_bound_longitude_range,
        west_bound_longitude_regex=west_bound_longitude_regex,
        west_bound_longitude_startswith=west_bound_longitude_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    bbox_name: str | Unset = UNSET,
    bbox_name_contains: str | Unset = UNSET,
    bbox_name_endswith: str | Unset = UNSET,
    bbox_name_gt: str | Unset = UNSET,
    bbox_name_gte: str | Unset = UNSET,
    bbox_name_icontains: str | Unset = UNSET,
    bbox_name_iendswith: str | Unset = UNSET,
    bbox_name_iexact: str | Unset = UNSET,
    bbox_name_in: list[str] | Unset = UNSET,
    bbox_name_iregex: str | Unset = UNSET,
    bbox_name_isnull: bool | Unset = UNSET,
    bbox_name_istartswith: str | Unset = UNSET,
    bbox_name_lt: str | Unset = UNSET,
    bbox_name_lte: str | Unset = UNSET,
    bbox_name_range: list[str] | Unset = UNSET,
    bbox_name_regex: str | Unset = UNSET,
    bbox_name_startswith: str | Unset = UNSET,
    east_bound_longitude: float | Unset = UNSET,
    east_bound_longitude_contained_by: float | Unset = UNSET,
    east_bound_longitude_contains: float | Unset = UNSET,
    east_bound_longitude_endswith: float | Unset = UNSET,
    east_bound_longitude_gt: float | Unset = UNSET,
    east_bound_longitude_gte: float | Unset = UNSET,
    east_bound_longitude_icontains: float | Unset = UNSET,
    east_bound_longitude_iendswith: float | Unset = UNSET,
    east_bound_longitude_iexact: float | Unset = UNSET,
    east_bound_longitude_in: list[float] | Unset = UNSET,
    east_bound_longitude_iregex: float | Unset = UNSET,
    east_bound_longitude_isnull: bool | Unset = UNSET,
    east_bound_longitude_istartswith: float | Unset = UNSET,
    east_bound_longitude_lt: float | Unset = UNSET,
    east_bound_longitude_lte: float | Unset = UNSET,
    east_bound_longitude_range: list[float] | Unset = UNSET,
    east_bound_longitude_regex: float | Unset = UNSET,
    east_bound_longitude_startswith: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    mobileplatformoperation: list[int] | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    north_bound_latitude: float | Unset = UNSET,
    north_bound_latitude_contained_by: float | Unset = UNSET,
    north_bound_latitude_contains: float | Unset = UNSET,
    north_bound_latitude_endswith: float | Unset = UNSET,
    north_bound_latitude_gt: float | Unset = UNSET,
    north_bound_latitude_gte: float | Unset = UNSET,
    north_bound_latitude_icontains: float | Unset = UNSET,
    north_bound_latitude_iendswith: float | Unset = UNSET,
    north_bound_latitude_iexact: float | Unset = UNSET,
    north_bound_latitude_in: list[float] | Unset = UNSET,
    north_bound_latitude_iregex: float | Unset = UNSET,
    north_bound_latitude_isnull: bool | Unset = UNSET,
    north_bound_latitude_istartswith: float | Unset = UNSET,
    north_bound_latitude_lt: float | Unset = UNSET,
    north_bound_latitude_lte: float | Unset = UNSET,
    north_bound_latitude_range: list[float] | Unset = UNSET,
    north_bound_latitude_regex: float | Unset = UNSET,
    north_bound_latitude_startswith: float | Unset = UNSET,
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
    platform: list[int] | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    south_bound_latitude: float | Unset = UNSET,
    south_bound_latitude_contained_by: float | Unset = UNSET,
    south_bound_latitude_contains: float | Unset = UNSET,
    south_bound_latitude_endswith: float | Unset = UNSET,
    south_bound_latitude_gt: float | Unset = UNSET,
    south_bound_latitude_gte: float | Unset = UNSET,
    south_bound_latitude_icontains: float | Unset = UNSET,
    south_bound_latitude_iendswith: float | Unset = UNSET,
    south_bound_latitude_iexact: float | Unset = UNSET,
    south_bound_latitude_in: list[float] | Unset = UNSET,
    south_bound_latitude_iregex: float | Unset = UNSET,
    south_bound_latitude_isnull: bool | Unset = UNSET,
    south_bound_latitude_istartswith: float | Unset = UNSET,
    south_bound_latitude_lt: float | Unset = UNSET,
    south_bound_latitude_lte: float | Unset = UNSET,
    south_bound_latitude_range: list[float] | Unset = UNSET,
    south_bound_latitude_regex: float | Unset = UNSET,
    south_bound_latitude_startswith: float | Unset = UNSET,
    west_bound_longitude: float | Unset = UNSET,
    west_bound_longitude_contained_by: float | Unset = UNSET,
    west_bound_longitude_contains: float | Unset = UNSET,
    west_bound_longitude_endswith: float | Unset = UNSET,
    west_bound_longitude_gt: float | Unset = UNSET,
    west_bound_longitude_gte: float | Unset = UNSET,
    west_bound_longitude_icontains: float | Unset = UNSET,
    west_bound_longitude_iendswith: float | Unset = UNSET,
    west_bound_longitude_iexact: float | Unset = UNSET,
    west_bound_longitude_in: list[float] | Unset = UNSET,
    west_bound_longitude_iregex: float | Unset = UNSET,
    west_bound_longitude_isnull: bool | Unset = UNSET,
    west_bound_longitude_istartswith: float | Unset = UNSET,
    west_bound_longitude_lt: float | Unset = UNSET,
    west_bound_longitude_lte: float | Unset = UNSET,
    west_bound_longitude_range: list[float] | Unset = UNSET,
    west_bound_longitude_regex: float | Unset = UNSET,
    west_bound_longitude_startswith: float | Unset = UNSET,
) -> PaginatedGeographicBoundingBoxReadList | None:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        bbox_name (str | Unset):
        bbox_name_contains (str | Unset):
        bbox_name_endswith (str | Unset):
        bbox_name_gt (str | Unset):
        bbox_name_gte (str | Unset):
        bbox_name_icontains (str | Unset):
        bbox_name_iendswith (str | Unset):
        bbox_name_iexact (str | Unset):
        bbox_name_in (list[str] | Unset):
        bbox_name_iregex (str | Unset):
        bbox_name_isnull (bool | Unset):
        bbox_name_istartswith (str | Unset):
        bbox_name_lt (str | Unset):
        bbox_name_lte (str | Unset):
        bbox_name_range (list[str] | Unset):
        bbox_name_regex (str | Unset):
        bbox_name_startswith (str | Unset):
        east_bound_longitude (float | Unset):
        east_bound_longitude_contained_by (float | Unset):
        east_bound_longitude_contains (float | Unset):
        east_bound_longitude_endswith (float | Unset):
        east_bound_longitude_gt (float | Unset):
        east_bound_longitude_gte (float | Unset):
        east_bound_longitude_icontains (float | Unset):
        east_bound_longitude_iendswith (float | Unset):
        east_bound_longitude_iexact (float | Unset):
        east_bound_longitude_in (list[float] | Unset):
        east_bound_longitude_iregex (float | Unset):
        east_bound_longitude_isnull (bool | Unset):
        east_bound_longitude_istartswith (float | Unset):
        east_bound_longitude_lt (float | Unset):
        east_bound_longitude_lte (float | Unset):
        east_bound_longitude_range (list[float] | Unset):
        east_bound_longitude_regex (float | Unset):
        east_bound_longitude_startswith (float | Unset):
        limit (int | Unset):
        mobileplatformoperation (list[int] | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        north_bound_latitude (float | Unset):
        north_bound_latitude_contained_by (float | Unset):
        north_bound_latitude_contains (float | Unset):
        north_bound_latitude_endswith (float | Unset):
        north_bound_latitude_gt (float | Unset):
        north_bound_latitude_gte (float | Unset):
        north_bound_latitude_icontains (float | Unset):
        north_bound_latitude_iendswith (float | Unset):
        north_bound_latitude_iexact (float | Unset):
        north_bound_latitude_in (list[float] | Unset):
        north_bound_latitude_iregex (float | Unset):
        north_bound_latitude_isnull (bool | Unset):
        north_bound_latitude_istartswith (float | Unset):
        north_bound_latitude_lt (float | Unset):
        north_bound_latitude_lte (float | Unset):
        north_bound_latitude_range (list[float] | Unset):
        north_bound_latitude_regex (float | Unset):
        north_bound_latitude_startswith (float | Unset):
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
        platform (list[int] | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        south_bound_latitude (float | Unset):
        south_bound_latitude_contained_by (float | Unset):
        south_bound_latitude_contains (float | Unset):
        south_bound_latitude_endswith (float | Unset):
        south_bound_latitude_gt (float | Unset):
        south_bound_latitude_gte (float | Unset):
        south_bound_latitude_icontains (float | Unset):
        south_bound_latitude_iendswith (float | Unset):
        south_bound_latitude_iexact (float | Unset):
        south_bound_latitude_in (list[float] | Unset):
        south_bound_latitude_iregex (float | Unset):
        south_bound_latitude_isnull (bool | Unset):
        south_bound_latitude_istartswith (float | Unset):
        south_bound_latitude_lt (float | Unset):
        south_bound_latitude_lte (float | Unset):
        south_bound_latitude_range (list[float] | Unset):
        south_bound_latitude_regex (float | Unset):
        south_bound_latitude_startswith (float | Unset):
        west_bound_longitude (float | Unset):
        west_bound_longitude_contained_by (float | Unset):
        west_bound_longitude_contains (float | Unset):
        west_bound_longitude_endswith (float | Unset):
        west_bound_longitude_gt (float | Unset):
        west_bound_longitude_gte (float | Unset):
        west_bound_longitude_icontains (float | Unset):
        west_bound_longitude_iendswith (float | Unset):
        west_bound_longitude_iexact (float | Unset):
        west_bound_longitude_in (list[float] | Unset):
        west_bound_longitude_iregex (float | Unset):
        west_bound_longitude_isnull (bool | Unset):
        west_bound_longitude_istartswith (float | Unset):
        west_bound_longitude_lt (float | Unset):
        west_bound_longitude_lte (float | Unset):
        west_bound_longitude_range (list[float] | Unset):
        west_bound_longitude_regex (float | Unset):
        west_bound_longitude_startswith (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedGeographicBoundingBoxReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            bbox_name=bbox_name,
            bbox_name_contains=bbox_name_contains,
            bbox_name_endswith=bbox_name_endswith,
            bbox_name_gt=bbox_name_gt,
            bbox_name_gte=bbox_name_gte,
            bbox_name_icontains=bbox_name_icontains,
            bbox_name_iendswith=bbox_name_iendswith,
            bbox_name_iexact=bbox_name_iexact,
            bbox_name_in=bbox_name_in,
            bbox_name_iregex=bbox_name_iregex,
            bbox_name_isnull=bbox_name_isnull,
            bbox_name_istartswith=bbox_name_istartswith,
            bbox_name_lt=bbox_name_lt,
            bbox_name_lte=bbox_name_lte,
            bbox_name_range=bbox_name_range,
            bbox_name_regex=bbox_name_regex,
            bbox_name_startswith=bbox_name_startswith,
            east_bound_longitude=east_bound_longitude,
            east_bound_longitude_contained_by=east_bound_longitude_contained_by,
            east_bound_longitude_contains=east_bound_longitude_contains,
            east_bound_longitude_endswith=east_bound_longitude_endswith,
            east_bound_longitude_gt=east_bound_longitude_gt,
            east_bound_longitude_gte=east_bound_longitude_gte,
            east_bound_longitude_icontains=east_bound_longitude_icontains,
            east_bound_longitude_iendswith=east_bound_longitude_iendswith,
            east_bound_longitude_iexact=east_bound_longitude_iexact,
            east_bound_longitude_in=east_bound_longitude_in,
            east_bound_longitude_iregex=east_bound_longitude_iregex,
            east_bound_longitude_isnull=east_bound_longitude_isnull,
            east_bound_longitude_istartswith=east_bound_longitude_istartswith,
            east_bound_longitude_lt=east_bound_longitude_lt,
            east_bound_longitude_lte=east_bound_longitude_lte,
            east_bound_longitude_range=east_bound_longitude_range,
            east_bound_longitude_regex=east_bound_longitude_regex,
            east_bound_longitude_startswith=east_bound_longitude_startswith,
            limit=limit,
            mobileplatformoperation=mobileplatformoperation,
            mobileplatformoperation_in=mobileplatformoperation_in,
            mobileplatformoperation_isnull=mobileplatformoperation_isnull,
            north_bound_latitude=north_bound_latitude,
            north_bound_latitude_contained_by=north_bound_latitude_contained_by,
            north_bound_latitude_contains=north_bound_latitude_contains,
            north_bound_latitude_endswith=north_bound_latitude_endswith,
            north_bound_latitude_gt=north_bound_latitude_gt,
            north_bound_latitude_gte=north_bound_latitude_gte,
            north_bound_latitude_icontains=north_bound_latitude_icontains,
            north_bound_latitude_iendswith=north_bound_latitude_iendswith,
            north_bound_latitude_iexact=north_bound_latitude_iexact,
            north_bound_latitude_in=north_bound_latitude_in,
            north_bound_latitude_iregex=north_bound_latitude_iregex,
            north_bound_latitude_isnull=north_bound_latitude_isnull,
            north_bound_latitude_istartswith=north_bound_latitude_istartswith,
            north_bound_latitude_lt=north_bound_latitude_lt,
            north_bound_latitude_lte=north_bound_latitude_lte,
            north_bound_latitude_range=north_bound_latitude_range,
            north_bound_latitude_regex=north_bound_latitude_regex,
            north_bound_latitude_startswith=north_bound_latitude_startswith,
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
            platform=platform,
            platform_in=platform_in,
            platform_isnull=platform_isnull,
            south_bound_latitude=south_bound_latitude,
            south_bound_latitude_contained_by=south_bound_latitude_contained_by,
            south_bound_latitude_contains=south_bound_latitude_contains,
            south_bound_latitude_endswith=south_bound_latitude_endswith,
            south_bound_latitude_gt=south_bound_latitude_gt,
            south_bound_latitude_gte=south_bound_latitude_gte,
            south_bound_latitude_icontains=south_bound_latitude_icontains,
            south_bound_latitude_iendswith=south_bound_latitude_iendswith,
            south_bound_latitude_iexact=south_bound_latitude_iexact,
            south_bound_latitude_in=south_bound_latitude_in,
            south_bound_latitude_iregex=south_bound_latitude_iregex,
            south_bound_latitude_isnull=south_bound_latitude_isnull,
            south_bound_latitude_istartswith=south_bound_latitude_istartswith,
            south_bound_latitude_lt=south_bound_latitude_lt,
            south_bound_latitude_lte=south_bound_latitude_lte,
            south_bound_latitude_range=south_bound_latitude_range,
            south_bound_latitude_regex=south_bound_latitude_regex,
            south_bound_latitude_startswith=south_bound_latitude_startswith,
            west_bound_longitude=west_bound_longitude,
            west_bound_longitude_contained_by=west_bound_longitude_contained_by,
            west_bound_longitude_contains=west_bound_longitude_contains,
            west_bound_longitude_endswith=west_bound_longitude_endswith,
            west_bound_longitude_gt=west_bound_longitude_gt,
            west_bound_longitude_gte=west_bound_longitude_gte,
            west_bound_longitude_icontains=west_bound_longitude_icontains,
            west_bound_longitude_iendswith=west_bound_longitude_iendswith,
            west_bound_longitude_iexact=west_bound_longitude_iexact,
            west_bound_longitude_in=west_bound_longitude_in,
            west_bound_longitude_iregex=west_bound_longitude_iregex,
            west_bound_longitude_isnull=west_bound_longitude_isnull,
            west_bound_longitude_istartswith=west_bound_longitude_istartswith,
            west_bound_longitude_lt=west_bound_longitude_lt,
            west_bound_longitude_lte=west_bound_longitude_lte,
            west_bound_longitude_range=west_bound_longitude_range,
            west_bound_longitude_regex=west_bound_longitude_regex,
            west_bound_longitude_startswith=west_bound_longitude_startswith,
        )
    ).parsed
