from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_geographic_bounding_box_read_list import PaginatedGeographicBoundingBoxReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    bbox_name: Union[Unset, str] = UNSET,
    bbox_name_contains: Union[Unset, str] = UNSET,
    bbox_name_endswith: Union[Unset, str] = UNSET,
    bbox_name_gt: Union[Unset, str] = UNSET,
    bbox_name_gte: Union[Unset, str] = UNSET,
    bbox_name_icontains: Union[Unset, str] = UNSET,
    bbox_name_iendswith: Union[Unset, str] = UNSET,
    bbox_name_iexact: Union[Unset, str] = UNSET,
    bbox_name_in: Union[Unset, list[str]] = UNSET,
    bbox_name_iregex: Union[Unset, str] = UNSET,
    bbox_name_isnull: Union[Unset, bool] = UNSET,
    bbox_name_istartswith: Union[Unset, str] = UNSET,
    bbox_name_lt: Union[Unset, str] = UNSET,
    bbox_name_lte: Union[Unset, str] = UNSET,
    bbox_name_range: Union[Unset, list[str]] = UNSET,
    bbox_name_regex: Union[Unset, str] = UNSET,
    bbox_name_startswith: Union[Unset, str] = UNSET,
    east_bound_longitude: Union[Unset, float] = UNSET,
    east_bound_longitude_contained_by: Union[Unset, float] = UNSET,
    east_bound_longitude_contains: Union[Unset, float] = UNSET,
    east_bound_longitude_endswith: Union[Unset, float] = UNSET,
    east_bound_longitude_gt: Union[Unset, float] = UNSET,
    east_bound_longitude_gte: Union[Unset, float] = UNSET,
    east_bound_longitude_icontains: Union[Unset, float] = UNSET,
    east_bound_longitude_iendswith: Union[Unset, float] = UNSET,
    east_bound_longitude_iexact: Union[Unset, float] = UNSET,
    east_bound_longitude_in: Union[Unset, list[float]] = UNSET,
    east_bound_longitude_iregex: Union[Unset, float] = UNSET,
    east_bound_longitude_isnull: Union[Unset, bool] = UNSET,
    east_bound_longitude_istartswith: Union[Unset, float] = UNSET,
    east_bound_longitude_lt: Union[Unset, float] = UNSET,
    east_bound_longitude_lte: Union[Unset, float] = UNSET,
    east_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    east_bound_longitude_regex: Union[Unset, float] = UNSET,
    east_bound_longitude_startswith: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    north_bound_latitude: Union[Unset, float] = UNSET,
    north_bound_latitude_contained_by: Union[Unset, float] = UNSET,
    north_bound_latitude_contains: Union[Unset, float] = UNSET,
    north_bound_latitude_endswith: Union[Unset, float] = UNSET,
    north_bound_latitude_gt: Union[Unset, float] = UNSET,
    north_bound_latitude_gte: Union[Unset, float] = UNSET,
    north_bound_latitude_icontains: Union[Unset, float] = UNSET,
    north_bound_latitude_iendswith: Union[Unset, float] = UNSET,
    north_bound_latitude_iexact: Union[Unset, float] = UNSET,
    north_bound_latitude_in: Union[Unset, list[float]] = UNSET,
    north_bound_latitude_iregex: Union[Unset, float] = UNSET,
    north_bound_latitude_isnull: Union[Unset, bool] = UNSET,
    north_bound_latitude_istartswith: Union[Unset, float] = UNSET,
    north_bound_latitude_lt: Union[Unset, float] = UNSET,
    north_bound_latitude_lte: Union[Unset, float] = UNSET,
    north_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    north_bound_latitude_regex: Union[Unset, float] = UNSET,
    north_bound_latitude_startswith: Union[Unset, float] = UNSET,
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
    south_bound_latitude: Union[Unset, float] = UNSET,
    south_bound_latitude_contained_by: Union[Unset, float] = UNSET,
    south_bound_latitude_contains: Union[Unset, float] = UNSET,
    south_bound_latitude_endswith: Union[Unset, float] = UNSET,
    south_bound_latitude_gt: Union[Unset, float] = UNSET,
    south_bound_latitude_gte: Union[Unset, float] = UNSET,
    south_bound_latitude_icontains: Union[Unset, float] = UNSET,
    south_bound_latitude_iendswith: Union[Unset, float] = UNSET,
    south_bound_latitude_iexact: Union[Unset, float] = UNSET,
    south_bound_latitude_in: Union[Unset, list[float]] = UNSET,
    south_bound_latitude_iregex: Union[Unset, float] = UNSET,
    south_bound_latitude_isnull: Union[Unset, bool] = UNSET,
    south_bound_latitude_istartswith: Union[Unset, float] = UNSET,
    south_bound_latitude_lt: Union[Unset, float] = UNSET,
    south_bound_latitude_lte: Union[Unset, float] = UNSET,
    south_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    south_bound_latitude_regex: Union[Unset, float] = UNSET,
    south_bound_latitude_startswith: Union[Unset, float] = UNSET,
    west_bound_longitude: Union[Unset, float] = UNSET,
    west_bound_longitude_contained_by: Union[Unset, float] = UNSET,
    west_bound_longitude_contains: Union[Unset, float] = UNSET,
    west_bound_longitude_endswith: Union[Unset, float] = UNSET,
    west_bound_longitude_gt: Union[Unset, float] = UNSET,
    west_bound_longitude_gte: Union[Unset, float] = UNSET,
    west_bound_longitude_icontains: Union[Unset, float] = UNSET,
    west_bound_longitude_iendswith: Union[Unset, float] = UNSET,
    west_bound_longitude_iexact: Union[Unset, float] = UNSET,
    west_bound_longitude_in: Union[Unset, list[float]] = UNSET,
    west_bound_longitude_iregex: Union[Unset, float] = UNSET,
    west_bound_longitude_isnull: Union[Unset, bool] = UNSET,
    west_bound_longitude_istartswith: Union[Unset, float] = UNSET,
    west_bound_longitude_lt: Union[Unset, float] = UNSET,
    west_bound_longitude_lte: Union[Unset, float] = UNSET,
    west_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    west_bound_longitude_regex: Union[Unset, float] = UNSET,
    west_bound_longitude_startswith: Union[Unset, float] = UNSET,
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

    json_bbox_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(bbox_name_in, Unset):
        json_bbox_name_in = bbox_name_in

    params["bboxName__in"] = json_bbox_name_in

    params["bboxName__iregex"] = bbox_name_iregex

    params["bboxName__isnull"] = bbox_name_isnull

    params["bboxName__istartswith"] = bbox_name_istartswith

    params["bboxName__lt"] = bbox_name_lt

    params["bboxName__lte"] = bbox_name_lte

    json_bbox_name_range: Union[Unset, list[str]] = UNSET
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

    json_east_bound_longitude_in: Union[Unset, list[float]] = UNSET
    if not isinstance(east_bound_longitude_in, Unset):
        json_east_bound_longitude_in = east_bound_longitude_in

    params["eastBoundLongitude__in"] = json_east_bound_longitude_in

    params["eastBoundLongitude__iregex"] = east_bound_longitude_iregex

    params["eastBoundLongitude__isnull"] = east_bound_longitude_isnull

    params["eastBoundLongitude__istartswith"] = east_bound_longitude_istartswith

    params["eastBoundLongitude__lt"] = east_bound_longitude_lt

    params["eastBoundLongitude__lte"] = east_bound_longitude_lte

    json_east_bound_longitude_range: Union[Unset, list[float]] = UNSET
    if not isinstance(east_bound_longitude_range, Unset):
        json_east_bound_longitude_range = east_bound_longitude_range

    params["eastBoundLongitude__range"] = json_east_bound_longitude_range

    params["eastBoundLongitude__regex"] = east_bound_longitude_regex

    params["eastBoundLongitude__startswith"] = east_bound_longitude_startswith

    params["limit"] = limit

    params["northBoundLatitude"] = north_bound_latitude

    params["northBoundLatitude__contained_by"] = north_bound_latitude_contained_by

    params["northBoundLatitude__contains"] = north_bound_latitude_contains

    params["northBoundLatitude__endswith"] = north_bound_latitude_endswith

    params["northBoundLatitude__gt"] = north_bound_latitude_gt

    params["northBoundLatitude__gte"] = north_bound_latitude_gte

    params["northBoundLatitude__icontains"] = north_bound_latitude_icontains

    params["northBoundLatitude__iendswith"] = north_bound_latitude_iendswith

    params["northBoundLatitude__iexact"] = north_bound_latitude_iexact

    json_north_bound_latitude_in: Union[Unset, list[float]] = UNSET
    if not isinstance(north_bound_latitude_in, Unset):
        json_north_bound_latitude_in = north_bound_latitude_in

    params["northBoundLatitude__in"] = json_north_bound_latitude_in

    params["northBoundLatitude__iregex"] = north_bound_latitude_iregex

    params["northBoundLatitude__isnull"] = north_bound_latitude_isnull

    params["northBoundLatitude__istartswith"] = north_bound_latitude_istartswith

    params["northBoundLatitude__lt"] = north_bound_latitude_lt

    params["northBoundLatitude__lte"] = north_bound_latitude_lte

    json_north_bound_latitude_range: Union[Unset, list[float]] = UNSET
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

    json_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_in, Unset):
        json_ob_id_in = ob_id_in

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ob_id_range

    params["ob_id__range"] = json_ob_id_range

    params["ob_id__regex"] = ob_id_regex

    params["ob_id__startswith"] = ob_id_startswith

    params["offset"] = offset

    params["ordering"] = ordering

    params["southBoundLatitude"] = south_bound_latitude

    params["southBoundLatitude__contained_by"] = south_bound_latitude_contained_by

    params["southBoundLatitude__contains"] = south_bound_latitude_contains

    params["southBoundLatitude__endswith"] = south_bound_latitude_endswith

    params["southBoundLatitude__gt"] = south_bound_latitude_gt

    params["southBoundLatitude__gte"] = south_bound_latitude_gte

    params["southBoundLatitude__icontains"] = south_bound_latitude_icontains

    params["southBoundLatitude__iendswith"] = south_bound_latitude_iendswith

    params["southBoundLatitude__iexact"] = south_bound_latitude_iexact

    json_south_bound_latitude_in: Union[Unset, list[float]] = UNSET
    if not isinstance(south_bound_latitude_in, Unset):
        json_south_bound_latitude_in = south_bound_latitude_in

    params["southBoundLatitude__in"] = json_south_bound_latitude_in

    params["southBoundLatitude__iregex"] = south_bound_latitude_iregex

    params["southBoundLatitude__isnull"] = south_bound_latitude_isnull

    params["southBoundLatitude__istartswith"] = south_bound_latitude_istartswith

    params["southBoundLatitude__lt"] = south_bound_latitude_lt

    params["southBoundLatitude__lte"] = south_bound_latitude_lte

    json_south_bound_latitude_range: Union[Unset, list[float]] = UNSET
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

    json_west_bound_longitude_in: Union[Unset, list[float]] = UNSET
    if not isinstance(west_bound_longitude_in, Unset):
        json_west_bound_longitude_in = west_bound_longitude_in

    params["westBoundLongitude__in"] = json_west_bound_longitude_in

    params["westBoundLongitude__iregex"] = west_bound_longitude_iregex

    params["westBoundLongitude__isnull"] = west_bound_longitude_isnull

    params["westBoundLongitude__istartswith"] = west_bound_longitude_istartswith

    params["westBoundLongitude__lt"] = west_bound_longitude_lt

    params["westBoundLongitude__lte"] = west_bound_longitude_lte

    json_west_bound_longitude_range: Union[Unset, list[float]] = UNSET
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedGeographicBoundingBoxReadList]:
    if response.status_code == 200:
        response_200 = PaginatedGeographicBoundingBoxReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
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
    bbox_name: Union[Unset, str] = UNSET,
    bbox_name_contains: Union[Unset, str] = UNSET,
    bbox_name_endswith: Union[Unset, str] = UNSET,
    bbox_name_gt: Union[Unset, str] = UNSET,
    bbox_name_gte: Union[Unset, str] = UNSET,
    bbox_name_icontains: Union[Unset, str] = UNSET,
    bbox_name_iendswith: Union[Unset, str] = UNSET,
    bbox_name_iexact: Union[Unset, str] = UNSET,
    bbox_name_in: Union[Unset, list[str]] = UNSET,
    bbox_name_iregex: Union[Unset, str] = UNSET,
    bbox_name_isnull: Union[Unset, bool] = UNSET,
    bbox_name_istartswith: Union[Unset, str] = UNSET,
    bbox_name_lt: Union[Unset, str] = UNSET,
    bbox_name_lte: Union[Unset, str] = UNSET,
    bbox_name_range: Union[Unset, list[str]] = UNSET,
    bbox_name_regex: Union[Unset, str] = UNSET,
    bbox_name_startswith: Union[Unset, str] = UNSET,
    east_bound_longitude: Union[Unset, float] = UNSET,
    east_bound_longitude_contained_by: Union[Unset, float] = UNSET,
    east_bound_longitude_contains: Union[Unset, float] = UNSET,
    east_bound_longitude_endswith: Union[Unset, float] = UNSET,
    east_bound_longitude_gt: Union[Unset, float] = UNSET,
    east_bound_longitude_gte: Union[Unset, float] = UNSET,
    east_bound_longitude_icontains: Union[Unset, float] = UNSET,
    east_bound_longitude_iendswith: Union[Unset, float] = UNSET,
    east_bound_longitude_iexact: Union[Unset, float] = UNSET,
    east_bound_longitude_in: Union[Unset, list[float]] = UNSET,
    east_bound_longitude_iregex: Union[Unset, float] = UNSET,
    east_bound_longitude_isnull: Union[Unset, bool] = UNSET,
    east_bound_longitude_istartswith: Union[Unset, float] = UNSET,
    east_bound_longitude_lt: Union[Unset, float] = UNSET,
    east_bound_longitude_lte: Union[Unset, float] = UNSET,
    east_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    east_bound_longitude_regex: Union[Unset, float] = UNSET,
    east_bound_longitude_startswith: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    north_bound_latitude: Union[Unset, float] = UNSET,
    north_bound_latitude_contained_by: Union[Unset, float] = UNSET,
    north_bound_latitude_contains: Union[Unset, float] = UNSET,
    north_bound_latitude_endswith: Union[Unset, float] = UNSET,
    north_bound_latitude_gt: Union[Unset, float] = UNSET,
    north_bound_latitude_gte: Union[Unset, float] = UNSET,
    north_bound_latitude_icontains: Union[Unset, float] = UNSET,
    north_bound_latitude_iendswith: Union[Unset, float] = UNSET,
    north_bound_latitude_iexact: Union[Unset, float] = UNSET,
    north_bound_latitude_in: Union[Unset, list[float]] = UNSET,
    north_bound_latitude_iregex: Union[Unset, float] = UNSET,
    north_bound_latitude_isnull: Union[Unset, bool] = UNSET,
    north_bound_latitude_istartswith: Union[Unset, float] = UNSET,
    north_bound_latitude_lt: Union[Unset, float] = UNSET,
    north_bound_latitude_lte: Union[Unset, float] = UNSET,
    north_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    north_bound_latitude_regex: Union[Unset, float] = UNSET,
    north_bound_latitude_startswith: Union[Unset, float] = UNSET,
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
    south_bound_latitude: Union[Unset, float] = UNSET,
    south_bound_latitude_contained_by: Union[Unset, float] = UNSET,
    south_bound_latitude_contains: Union[Unset, float] = UNSET,
    south_bound_latitude_endswith: Union[Unset, float] = UNSET,
    south_bound_latitude_gt: Union[Unset, float] = UNSET,
    south_bound_latitude_gte: Union[Unset, float] = UNSET,
    south_bound_latitude_icontains: Union[Unset, float] = UNSET,
    south_bound_latitude_iendswith: Union[Unset, float] = UNSET,
    south_bound_latitude_iexact: Union[Unset, float] = UNSET,
    south_bound_latitude_in: Union[Unset, list[float]] = UNSET,
    south_bound_latitude_iregex: Union[Unset, float] = UNSET,
    south_bound_latitude_isnull: Union[Unset, bool] = UNSET,
    south_bound_latitude_istartswith: Union[Unset, float] = UNSET,
    south_bound_latitude_lt: Union[Unset, float] = UNSET,
    south_bound_latitude_lte: Union[Unset, float] = UNSET,
    south_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    south_bound_latitude_regex: Union[Unset, float] = UNSET,
    south_bound_latitude_startswith: Union[Unset, float] = UNSET,
    west_bound_longitude: Union[Unset, float] = UNSET,
    west_bound_longitude_contained_by: Union[Unset, float] = UNSET,
    west_bound_longitude_contains: Union[Unset, float] = UNSET,
    west_bound_longitude_endswith: Union[Unset, float] = UNSET,
    west_bound_longitude_gt: Union[Unset, float] = UNSET,
    west_bound_longitude_gte: Union[Unset, float] = UNSET,
    west_bound_longitude_icontains: Union[Unset, float] = UNSET,
    west_bound_longitude_iendswith: Union[Unset, float] = UNSET,
    west_bound_longitude_iexact: Union[Unset, float] = UNSET,
    west_bound_longitude_in: Union[Unset, list[float]] = UNSET,
    west_bound_longitude_iregex: Union[Unset, float] = UNSET,
    west_bound_longitude_isnull: Union[Unset, bool] = UNSET,
    west_bound_longitude_istartswith: Union[Unset, float] = UNSET,
    west_bound_longitude_lt: Union[Unset, float] = UNSET,
    west_bound_longitude_lte: Union[Unset, float] = UNSET,
    west_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    west_bound_longitude_regex: Union[Unset, float] = UNSET,
    west_bound_longitude_startswith: Union[Unset, float] = UNSET,
) -> Response[PaginatedGeographicBoundingBoxReadList]:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        bbox_name (Union[Unset, str]):
        bbox_name_contains (Union[Unset, str]):
        bbox_name_endswith (Union[Unset, str]):
        bbox_name_gt (Union[Unset, str]):
        bbox_name_gte (Union[Unset, str]):
        bbox_name_icontains (Union[Unset, str]):
        bbox_name_iendswith (Union[Unset, str]):
        bbox_name_iexact (Union[Unset, str]):
        bbox_name_in (Union[Unset, list[str]]):
        bbox_name_iregex (Union[Unset, str]):
        bbox_name_isnull (Union[Unset, bool]):
        bbox_name_istartswith (Union[Unset, str]):
        bbox_name_lt (Union[Unset, str]):
        bbox_name_lte (Union[Unset, str]):
        bbox_name_range (Union[Unset, list[str]]):
        bbox_name_regex (Union[Unset, str]):
        bbox_name_startswith (Union[Unset, str]):
        east_bound_longitude (Union[Unset, float]):
        east_bound_longitude_contained_by (Union[Unset, float]):
        east_bound_longitude_contains (Union[Unset, float]):
        east_bound_longitude_endswith (Union[Unset, float]):
        east_bound_longitude_gt (Union[Unset, float]):
        east_bound_longitude_gte (Union[Unset, float]):
        east_bound_longitude_icontains (Union[Unset, float]):
        east_bound_longitude_iendswith (Union[Unset, float]):
        east_bound_longitude_iexact (Union[Unset, float]):
        east_bound_longitude_in (Union[Unset, list[float]]):
        east_bound_longitude_iregex (Union[Unset, float]):
        east_bound_longitude_isnull (Union[Unset, bool]):
        east_bound_longitude_istartswith (Union[Unset, float]):
        east_bound_longitude_lt (Union[Unset, float]):
        east_bound_longitude_lte (Union[Unset, float]):
        east_bound_longitude_range (Union[Unset, list[float]]):
        east_bound_longitude_regex (Union[Unset, float]):
        east_bound_longitude_startswith (Union[Unset, float]):
        limit (Union[Unset, int]):
        north_bound_latitude (Union[Unset, float]):
        north_bound_latitude_contained_by (Union[Unset, float]):
        north_bound_latitude_contains (Union[Unset, float]):
        north_bound_latitude_endswith (Union[Unset, float]):
        north_bound_latitude_gt (Union[Unset, float]):
        north_bound_latitude_gte (Union[Unset, float]):
        north_bound_latitude_icontains (Union[Unset, float]):
        north_bound_latitude_iendswith (Union[Unset, float]):
        north_bound_latitude_iexact (Union[Unset, float]):
        north_bound_latitude_in (Union[Unset, list[float]]):
        north_bound_latitude_iregex (Union[Unset, float]):
        north_bound_latitude_isnull (Union[Unset, bool]):
        north_bound_latitude_istartswith (Union[Unset, float]):
        north_bound_latitude_lt (Union[Unset, float]):
        north_bound_latitude_lte (Union[Unset, float]):
        north_bound_latitude_range (Union[Unset, list[float]]):
        north_bound_latitude_regex (Union[Unset, float]):
        north_bound_latitude_startswith (Union[Unset, float]):
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
        south_bound_latitude (Union[Unset, float]):
        south_bound_latitude_contained_by (Union[Unset, float]):
        south_bound_latitude_contains (Union[Unset, float]):
        south_bound_latitude_endswith (Union[Unset, float]):
        south_bound_latitude_gt (Union[Unset, float]):
        south_bound_latitude_gte (Union[Unset, float]):
        south_bound_latitude_icontains (Union[Unset, float]):
        south_bound_latitude_iendswith (Union[Unset, float]):
        south_bound_latitude_iexact (Union[Unset, float]):
        south_bound_latitude_in (Union[Unset, list[float]]):
        south_bound_latitude_iregex (Union[Unset, float]):
        south_bound_latitude_isnull (Union[Unset, bool]):
        south_bound_latitude_istartswith (Union[Unset, float]):
        south_bound_latitude_lt (Union[Unset, float]):
        south_bound_latitude_lte (Union[Unset, float]):
        south_bound_latitude_range (Union[Unset, list[float]]):
        south_bound_latitude_regex (Union[Unset, float]):
        south_bound_latitude_startswith (Union[Unset, float]):
        west_bound_longitude (Union[Unset, float]):
        west_bound_longitude_contained_by (Union[Unset, float]):
        west_bound_longitude_contains (Union[Unset, float]):
        west_bound_longitude_endswith (Union[Unset, float]):
        west_bound_longitude_gt (Union[Unset, float]):
        west_bound_longitude_gte (Union[Unset, float]):
        west_bound_longitude_icontains (Union[Unset, float]):
        west_bound_longitude_iendswith (Union[Unset, float]):
        west_bound_longitude_iexact (Union[Unset, float]):
        west_bound_longitude_in (Union[Unset, list[float]]):
        west_bound_longitude_iregex (Union[Unset, float]):
        west_bound_longitude_isnull (Union[Unset, bool]):
        west_bound_longitude_istartswith (Union[Unset, float]):
        west_bound_longitude_lt (Union[Unset, float]):
        west_bound_longitude_lte (Union[Unset, float]):
        west_bound_longitude_range (Union[Unset, list[float]]):
        west_bound_longitude_regex (Union[Unset, float]):
        west_bound_longitude_startswith (Union[Unset, float]):

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
        offset=offset,
        ordering=ordering,
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
    bbox_name: Union[Unset, str] = UNSET,
    bbox_name_contains: Union[Unset, str] = UNSET,
    bbox_name_endswith: Union[Unset, str] = UNSET,
    bbox_name_gt: Union[Unset, str] = UNSET,
    bbox_name_gte: Union[Unset, str] = UNSET,
    bbox_name_icontains: Union[Unset, str] = UNSET,
    bbox_name_iendswith: Union[Unset, str] = UNSET,
    bbox_name_iexact: Union[Unset, str] = UNSET,
    bbox_name_in: Union[Unset, list[str]] = UNSET,
    bbox_name_iregex: Union[Unset, str] = UNSET,
    bbox_name_isnull: Union[Unset, bool] = UNSET,
    bbox_name_istartswith: Union[Unset, str] = UNSET,
    bbox_name_lt: Union[Unset, str] = UNSET,
    bbox_name_lte: Union[Unset, str] = UNSET,
    bbox_name_range: Union[Unset, list[str]] = UNSET,
    bbox_name_regex: Union[Unset, str] = UNSET,
    bbox_name_startswith: Union[Unset, str] = UNSET,
    east_bound_longitude: Union[Unset, float] = UNSET,
    east_bound_longitude_contained_by: Union[Unset, float] = UNSET,
    east_bound_longitude_contains: Union[Unset, float] = UNSET,
    east_bound_longitude_endswith: Union[Unset, float] = UNSET,
    east_bound_longitude_gt: Union[Unset, float] = UNSET,
    east_bound_longitude_gte: Union[Unset, float] = UNSET,
    east_bound_longitude_icontains: Union[Unset, float] = UNSET,
    east_bound_longitude_iendswith: Union[Unset, float] = UNSET,
    east_bound_longitude_iexact: Union[Unset, float] = UNSET,
    east_bound_longitude_in: Union[Unset, list[float]] = UNSET,
    east_bound_longitude_iregex: Union[Unset, float] = UNSET,
    east_bound_longitude_isnull: Union[Unset, bool] = UNSET,
    east_bound_longitude_istartswith: Union[Unset, float] = UNSET,
    east_bound_longitude_lt: Union[Unset, float] = UNSET,
    east_bound_longitude_lte: Union[Unset, float] = UNSET,
    east_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    east_bound_longitude_regex: Union[Unset, float] = UNSET,
    east_bound_longitude_startswith: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    north_bound_latitude: Union[Unset, float] = UNSET,
    north_bound_latitude_contained_by: Union[Unset, float] = UNSET,
    north_bound_latitude_contains: Union[Unset, float] = UNSET,
    north_bound_latitude_endswith: Union[Unset, float] = UNSET,
    north_bound_latitude_gt: Union[Unset, float] = UNSET,
    north_bound_latitude_gte: Union[Unset, float] = UNSET,
    north_bound_latitude_icontains: Union[Unset, float] = UNSET,
    north_bound_latitude_iendswith: Union[Unset, float] = UNSET,
    north_bound_latitude_iexact: Union[Unset, float] = UNSET,
    north_bound_latitude_in: Union[Unset, list[float]] = UNSET,
    north_bound_latitude_iregex: Union[Unset, float] = UNSET,
    north_bound_latitude_isnull: Union[Unset, bool] = UNSET,
    north_bound_latitude_istartswith: Union[Unset, float] = UNSET,
    north_bound_latitude_lt: Union[Unset, float] = UNSET,
    north_bound_latitude_lte: Union[Unset, float] = UNSET,
    north_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    north_bound_latitude_regex: Union[Unset, float] = UNSET,
    north_bound_latitude_startswith: Union[Unset, float] = UNSET,
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
    south_bound_latitude: Union[Unset, float] = UNSET,
    south_bound_latitude_contained_by: Union[Unset, float] = UNSET,
    south_bound_latitude_contains: Union[Unset, float] = UNSET,
    south_bound_latitude_endswith: Union[Unset, float] = UNSET,
    south_bound_latitude_gt: Union[Unset, float] = UNSET,
    south_bound_latitude_gte: Union[Unset, float] = UNSET,
    south_bound_latitude_icontains: Union[Unset, float] = UNSET,
    south_bound_latitude_iendswith: Union[Unset, float] = UNSET,
    south_bound_latitude_iexact: Union[Unset, float] = UNSET,
    south_bound_latitude_in: Union[Unset, list[float]] = UNSET,
    south_bound_latitude_iregex: Union[Unset, float] = UNSET,
    south_bound_latitude_isnull: Union[Unset, bool] = UNSET,
    south_bound_latitude_istartswith: Union[Unset, float] = UNSET,
    south_bound_latitude_lt: Union[Unset, float] = UNSET,
    south_bound_latitude_lte: Union[Unset, float] = UNSET,
    south_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    south_bound_latitude_regex: Union[Unset, float] = UNSET,
    south_bound_latitude_startswith: Union[Unset, float] = UNSET,
    west_bound_longitude: Union[Unset, float] = UNSET,
    west_bound_longitude_contained_by: Union[Unset, float] = UNSET,
    west_bound_longitude_contains: Union[Unset, float] = UNSET,
    west_bound_longitude_endswith: Union[Unset, float] = UNSET,
    west_bound_longitude_gt: Union[Unset, float] = UNSET,
    west_bound_longitude_gte: Union[Unset, float] = UNSET,
    west_bound_longitude_icontains: Union[Unset, float] = UNSET,
    west_bound_longitude_iendswith: Union[Unset, float] = UNSET,
    west_bound_longitude_iexact: Union[Unset, float] = UNSET,
    west_bound_longitude_in: Union[Unset, list[float]] = UNSET,
    west_bound_longitude_iregex: Union[Unset, float] = UNSET,
    west_bound_longitude_isnull: Union[Unset, bool] = UNSET,
    west_bound_longitude_istartswith: Union[Unset, float] = UNSET,
    west_bound_longitude_lt: Union[Unset, float] = UNSET,
    west_bound_longitude_lte: Union[Unset, float] = UNSET,
    west_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    west_bound_longitude_regex: Union[Unset, float] = UNSET,
    west_bound_longitude_startswith: Union[Unset, float] = UNSET,
) -> Optional[PaginatedGeographicBoundingBoxReadList]:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        bbox_name (Union[Unset, str]):
        bbox_name_contains (Union[Unset, str]):
        bbox_name_endswith (Union[Unset, str]):
        bbox_name_gt (Union[Unset, str]):
        bbox_name_gte (Union[Unset, str]):
        bbox_name_icontains (Union[Unset, str]):
        bbox_name_iendswith (Union[Unset, str]):
        bbox_name_iexact (Union[Unset, str]):
        bbox_name_in (Union[Unset, list[str]]):
        bbox_name_iregex (Union[Unset, str]):
        bbox_name_isnull (Union[Unset, bool]):
        bbox_name_istartswith (Union[Unset, str]):
        bbox_name_lt (Union[Unset, str]):
        bbox_name_lte (Union[Unset, str]):
        bbox_name_range (Union[Unset, list[str]]):
        bbox_name_regex (Union[Unset, str]):
        bbox_name_startswith (Union[Unset, str]):
        east_bound_longitude (Union[Unset, float]):
        east_bound_longitude_contained_by (Union[Unset, float]):
        east_bound_longitude_contains (Union[Unset, float]):
        east_bound_longitude_endswith (Union[Unset, float]):
        east_bound_longitude_gt (Union[Unset, float]):
        east_bound_longitude_gte (Union[Unset, float]):
        east_bound_longitude_icontains (Union[Unset, float]):
        east_bound_longitude_iendswith (Union[Unset, float]):
        east_bound_longitude_iexact (Union[Unset, float]):
        east_bound_longitude_in (Union[Unset, list[float]]):
        east_bound_longitude_iregex (Union[Unset, float]):
        east_bound_longitude_isnull (Union[Unset, bool]):
        east_bound_longitude_istartswith (Union[Unset, float]):
        east_bound_longitude_lt (Union[Unset, float]):
        east_bound_longitude_lte (Union[Unset, float]):
        east_bound_longitude_range (Union[Unset, list[float]]):
        east_bound_longitude_regex (Union[Unset, float]):
        east_bound_longitude_startswith (Union[Unset, float]):
        limit (Union[Unset, int]):
        north_bound_latitude (Union[Unset, float]):
        north_bound_latitude_contained_by (Union[Unset, float]):
        north_bound_latitude_contains (Union[Unset, float]):
        north_bound_latitude_endswith (Union[Unset, float]):
        north_bound_latitude_gt (Union[Unset, float]):
        north_bound_latitude_gte (Union[Unset, float]):
        north_bound_latitude_icontains (Union[Unset, float]):
        north_bound_latitude_iendswith (Union[Unset, float]):
        north_bound_latitude_iexact (Union[Unset, float]):
        north_bound_latitude_in (Union[Unset, list[float]]):
        north_bound_latitude_iregex (Union[Unset, float]):
        north_bound_latitude_isnull (Union[Unset, bool]):
        north_bound_latitude_istartswith (Union[Unset, float]):
        north_bound_latitude_lt (Union[Unset, float]):
        north_bound_latitude_lte (Union[Unset, float]):
        north_bound_latitude_range (Union[Unset, list[float]]):
        north_bound_latitude_regex (Union[Unset, float]):
        north_bound_latitude_startswith (Union[Unset, float]):
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
        south_bound_latitude (Union[Unset, float]):
        south_bound_latitude_contained_by (Union[Unset, float]):
        south_bound_latitude_contains (Union[Unset, float]):
        south_bound_latitude_endswith (Union[Unset, float]):
        south_bound_latitude_gt (Union[Unset, float]):
        south_bound_latitude_gte (Union[Unset, float]):
        south_bound_latitude_icontains (Union[Unset, float]):
        south_bound_latitude_iendswith (Union[Unset, float]):
        south_bound_latitude_iexact (Union[Unset, float]):
        south_bound_latitude_in (Union[Unset, list[float]]):
        south_bound_latitude_iregex (Union[Unset, float]):
        south_bound_latitude_isnull (Union[Unset, bool]):
        south_bound_latitude_istartswith (Union[Unset, float]):
        south_bound_latitude_lt (Union[Unset, float]):
        south_bound_latitude_lte (Union[Unset, float]):
        south_bound_latitude_range (Union[Unset, list[float]]):
        south_bound_latitude_regex (Union[Unset, float]):
        south_bound_latitude_startswith (Union[Unset, float]):
        west_bound_longitude (Union[Unset, float]):
        west_bound_longitude_contained_by (Union[Unset, float]):
        west_bound_longitude_contains (Union[Unset, float]):
        west_bound_longitude_endswith (Union[Unset, float]):
        west_bound_longitude_gt (Union[Unset, float]):
        west_bound_longitude_gte (Union[Unset, float]):
        west_bound_longitude_icontains (Union[Unset, float]):
        west_bound_longitude_iendswith (Union[Unset, float]):
        west_bound_longitude_iexact (Union[Unset, float]):
        west_bound_longitude_in (Union[Unset, list[float]]):
        west_bound_longitude_iregex (Union[Unset, float]):
        west_bound_longitude_isnull (Union[Unset, bool]):
        west_bound_longitude_istartswith (Union[Unset, float]):
        west_bound_longitude_lt (Union[Unset, float]):
        west_bound_longitude_lte (Union[Unset, float]):
        west_bound_longitude_range (Union[Unset, list[float]]):
        west_bound_longitude_regex (Union[Unset, float]):
        west_bound_longitude_startswith (Union[Unset, float]):

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
        offset=offset,
        ordering=ordering,
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
    bbox_name: Union[Unset, str] = UNSET,
    bbox_name_contains: Union[Unset, str] = UNSET,
    bbox_name_endswith: Union[Unset, str] = UNSET,
    bbox_name_gt: Union[Unset, str] = UNSET,
    bbox_name_gte: Union[Unset, str] = UNSET,
    bbox_name_icontains: Union[Unset, str] = UNSET,
    bbox_name_iendswith: Union[Unset, str] = UNSET,
    bbox_name_iexact: Union[Unset, str] = UNSET,
    bbox_name_in: Union[Unset, list[str]] = UNSET,
    bbox_name_iregex: Union[Unset, str] = UNSET,
    bbox_name_isnull: Union[Unset, bool] = UNSET,
    bbox_name_istartswith: Union[Unset, str] = UNSET,
    bbox_name_lt: Union[Unset, str] = UNSET,
    bbox_name_lte: Union[Unset, str] = UNSET,
    bbox_name_range: Union[Unset, list[str]] = UNSET,
    bbox_name_regex: Union[Unset, str] = UNSET,
    bbox_name_startswith: Union[Unset, str] = UNSET,
    east_bound_longitude: Union[Unset, float] = UNSET,
    east_bound_longitude_contained_by: Union[Unset, float] = UNSET,
    east_bound_longitude_contains: Union[Unset, float] = UNSET,
    east_bound_longitude_endswith: Union[Unset, float] = UNSET,
    east_bound_longitude_gt: Union[Unset, float] = UNSET,
    east_bound_longitude_gte: Union[Unset, float] = UNSET,
    east_bound_longitude_icontains: Union[Unset, float] = UNSET,
    east_bound_longitude_iendswith: Union[Unset, float] = UNSET,
    east_bound_longitude_iexact: Union[Unset, float] = UNSET,
    east_bound_longitude_in: Union[Unset, list[float]] = UNSET,
    east_bound_longitude_iregex: Union[Unset, float] = UNSET,
    east_bound_longitude_isnull: Union[Unset, bool] = UNSET,
    east_bound_longitude_istartswith: Union[Unset, float] = UNSET,
    east_bound_longitude_lt: Union[Unset, float] = UNSET,
    east_bound_longitude_lte: Union[Unset, float] = UNSET,
    east_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    east_bound_longitude_regex: Union[Unset, float] = UNSET,
    east_bound_longitude_startswith: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    north_bound_latitude: Union[Unset, float] = UNSET,
    north_bound_latitude_contained_by: Union[Unset, float] = UNSET,
    north_bound_latitude_contains: Union[Unset, float] = UNSET,
    north_bound_latitude_endswith: Union[Unset, float] = UNSET,
    north_bound_latitude_gt: Union[Unset, float] = UNSET,
    north_bound_latitude_gte: Union[Unset, float] = UNSET,
    north_bound_latitude_icontains: Union[Unset, float] = UNSET,
    north_bound_latitude_iendswith: Union[Unset, float] = UNSET,
    north_bound_latitude_iexact: Union[Unset, float] = UNSET,
    north_bound_latitude_in: Union[Unset, list[float]] = UNSET,
    north_bound_latitude_iregex: Union[Unset, float] = UNSET,
    north_bound_latitude_isnull: Union[Unset, bool] = UNSET,
    north_bound_latitude_istartswith: Union[Unset, float] = UNSET,
    north_bound_latitude_lt: Union[Unset, float] = UNSET,
    north_bound_latitude_lte: Union[Unset, float] = UNSET,
    north_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    north_bound_latitude_regex: Union[Unset, float] = UNSET,
    north_bound_latitude_startswith: Union[Unset, float] = UNSET,
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
    south_bound_latitude: Union[Unset, float] = UNSET,
    south_bound_latitude_contained_by: Union[Unset, float] = UNSET,
    south_bound_latitude_contains: Union[Unset, float] = UNSET,
    south_bound_latitude_endswith: Union[Unset, float] = UNSET,
    south_bound_latitude_gt: Union[Unset, float] = UNSET,
    south_bound_latitude_gte: Union[Unset, float] = UNSET,
    south_bound_latitude_icontains: Union[Unset, float] = UNSET,
    south_bound_latitude_iendswith: Union[Unset, float] = UNSET,
    south_bound_latitude_iexact: Union[Unset, float] = UNSET,
    south_bound_latitude_in: Union[Unset, list[float]] = UNSET,
    south_bound_latitude_iregex: Union[Unset, float] = UNSET,
    south_bound_latitude_isnull: Union[Unset, bool] = UNSET,
    south_bound_latitude_istartswith: Union[Unset, float] = UNSET,
    south_bound_latitude_lt: Union[Unset, float] = UNSET,
    south_bound_latitude_lte: Union[Unset, float] = UNSET,
    south_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    south_bound_latitude_regex: Union[Unset, float] = UNSET,
    south_bound_latitude_startswith: Union[Unset, float] = UNSET,
    west_bound_longitude: Union[Unset, float] = UNSET,
    west_bound_longitude_contained_by: Union[Unset, float] = UNSET,
    west_bound_longitude_contains: Union[Unset, float] = UNSET,
    west_bound_longitude_endswith: Union[Unset, float] = UNSET,
    west_bound_longitude_gt: Union[Unset, float] = UNSET,
    west_bound_longitude_gte: Union[Unset, float] = UNSET,
    west_bound_longitude_icontains: Union[Unset, float] = UNSET,
    west_bound_longitude_iendswith: Union[Unset, float] = UNSET,
    west_bound_longitude_iexact: Union[Unset, float] = UNSET,
    west_bound_longitude_in: Union[Unset, list[float]] = UNSET,
    west_bound_longitude_iregex: Union[Unset, float] = UNSET,
    west_bound_longitude_isnull: Union[Unset, bool] = UNSET,
    west_bound_longitude_istartswith: Union[Unset, float] = UNSET,
    west_bound_longitude_lt: Union[Unset, float] = UNSET,
    west_bound_longitude_lte: Union[Unset, float] = UNSET,
    west_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    west_bound_longitude_regex: Union[Unset, float] = UNSET,
    west_bound_longitude_startswith: Union[Unset, float] = UNSET,
) -> Response[PaginatedGeographicBoundingBoxReadList]:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        bbox_name (Union[Unset, str]):
        bbox_name_contains (Union[Unset, str]):
        bbox_name_endswith (Union[Unset, str]):
        bbox_name_gt (Union[Unset, str]):
        bbox_name_gte (Union[Unset, str]):
        bbox_name_icontains (Union[Unset, str]):
        bbox_name_iendswith (Union[Unset, str]):
        bbox_name_iexact (Union[Unset, str]):
        bbox_name_in (Union[Unset, list[str]]):
        bbox_name_iregex (Union[Unset, str]):
        bbox_name_isnull (Union[Unset, bool]):
        bbox_name_istartswith (Union[Unset, str]):
        bbox_name_lt (Union[Unset, str]):
        bbox_name_lte (Union[Unset, str]):
        bbox_name_range (Union[Unset, list[str]]):
        bbox_name_regex (Union[Unset, str]):
        bbox_name_startswith (Union[Unset, str]):
        east_bound_longitude (Union[Unset, float]):
        east_bound_longitude_contained_by (Union[Unset, float]):
        east_bound_longitude_contains (Union[Unset, float]):
        east_bound_longitude_endswith (Union[Unset, float]):
        east_bound_longitude_gt (Union[Unset, float]):
        east_bound_longitude_gte (Union[Unset, float]):
        east_bound_longitude_icontains (Union[Unset, float]):
        east_bound_longitude_iendswith (Union[Unset, float]):
        east_bound_longitude_iexact (Union[Unset, float]):
        east_bound_longitude_in (Union[Unset, list[float]]):
        east_bound_longitude_iregex (Union[Unset, float]):
        east_bound_longitude_isnull (Union[Unset, bool]):
        east_bound_longitude_istartswith (Union[Unset, float]):
        east_bound_longitude_lt (Union[Unset, float]):
        east_bound_longitude_lte (Union[Unset, float]):
        east_bound_longitude_range (Union[Unset, list[float]]):
        east_bound_longitude_regex (Union[Unset, float]):
        east_bound_longitude_startswith (Union[Unset, float]):
        limit (Union[Unset, int]):
        north_bound_latitude (Union[Unset, float]):
        north_bound_latitude_contained_by (Union[Unset, float]):
        north_bound_latitude_contains (Union[Unset, float]):
        north_bound_latitude_endswith (Union[Unset, float]):
        north_bound_latitude_gt (Union[Unset, float]):
        north_bound_latitude_gte (Union[Unset, float]):
        north_bound_latitude_icontains (Union[Unset, float]):
        north_bound_latitude_iendswith (Union[Unset, float]):
        north_bound_latitude_iexact (Union[Unset, float]):
        north_bound_latitude_in (Union[Unset, list[float]]):
        north_bound_latitude_iregex (Union[Unset, float]):
        north_bound_latitude_isnull (Union[Unset, bool]):
        north_bound_latitude_istartswith (Union[Unset, float]):
        north_bound_latitude_lt (Union[Unset, float]):
        north_bound_latitude_lte (Union[Unset, float]):
        north_bound_latitude_range (Union[Unset, list[float]]):
        north_bound_latitude_regex (Union[Unset, float]):
        north_bound_latitude_startswith (Union[Unset, float]):
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
        south_bound_latitude (Union[Unset, float]):
        south_bound_latitude_contained_by (Union[Unset, float]):
        south_bound_latitude_contains (Union[Unset, float]):
        south_bound_latitude_endswith (Union[Unset, float]):
        south_bound_latitude_gt (Union[Unset, float]):
        south_bound_latitude_gte (Union[Unset, float]):
        south_bound_latitude_icontains (Union[Unset, float]):
        south_bound_latitude_iendswith (Union[Unset, float]):
        south_bound_latitude_iexact (Union[Unset, float]):
        south_bound_latitude_in (Union[Unset, list[float]]):
        south_bound_latitude_iregex (Union[Unset, float]):
        south_bound_latitude_isnull (Union[Unset, bool]):
        south_bound_latitude_istartswith (Union[Unset, float]):
        south_bound_latitude_lt (Union[Unset, float]):
        south_bound_latitude_lte (Union[Unset, float]):
        south_bound_latitude_range (Union[Unset, list[float]]):
        south_bound_latitude_regex (Union[Unset, float]):
        south_bound_latitude_startswith (Union[Unset, float]):
        west_bound_longitude (Union[Unset, float]):
        west_bound_longitude_contained_by (Union[Unset, float]):
        west_bound_longitude_contains (Union[Unset, float]):
        west_bound_longitude_endswith (Union[Unset, float]):
        west_bound_longitude_gt (Union[Unset, float]):
        west_bound_longitude_gte (Union[Unset, float]):
        west_bound_longitude_icontains (Union[Unset, float]):
        west_bound_longitude_iendswith (Union[Unset, float]):
        west_bound_longitude_iexact (Union[Unset, float]):
        west_bound_longitude_in (Union[Unset, list[float]]):
        west_bound_longitude_iregex (Union[Unset, float]):
        west_bound_longitude_isnull (Union[Unset, bool]):
        west_bound_longitude_istartswith (Union[Unset, float]):
        west_bound_longitude_lt (Union[Unset, float]):
        west_bound_longitude_lte (Union[Unset, float]):
        west_bound_longitude_range (Union[Unset, list[float]]):
        west_bound_longitude_regex (Union[Unset, float]):
        west_bound_longitude_startswith (Union[Unset, float]):

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
        offset=offset,
        ordering=ordering,
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
    bbox_name: Union[Unset, str] = UNSET,
    bbox_name_contains: Union[Unset, str] = UNSET,
    bbox_name_endswith: Union[Unset, str] = UNSET,
    bbox_name_gt: Union[Unset, str] = UNSET,
    bbox_name_gte: Union[Unset, str] = UNSET,
    bbox_name_icontains: Union[Unset, str] = UNSET,
    bbox_name_iendswith: Union[Unset, str] = UNSET,
    bbox_name_iexact: Union[Unset, str] = UNSET,
    bbox_name_in: Union[Unset, list[str]] = UNSET,
    bbox_name_iregex: Union[Unset, str] = UNSET,
    bbox_name_isnull: Union[Unset, bool] = UNSET,
    bbox_name_istartswith: Union[Unset, str] = UNSET,
    bbox_name_lt: Union[Unset, str] = UNSET,
    bbox_name_lte: Union[Unset, str] = UNSET,
    bbox_name_range: Union[Unset, list[str]] = UNSET,
    bbox_name_regex: Union[Unset, str] = UNSET,
    bbox_name_startswith: Union[Unset, str] = UNSET,
    east_bound_longitude: Union[Unset, float] = UNSET,
    east_bound_longitude_contained_by: Union[Unset, float] = UNSET,
    east_bound_longitude_contains: Union[Unset, float] = UNSET,
    east_bound_longitude_endswith: Union[Unset, float] = UNSET,
    east_bound_longitude_gt: Union[Unset, float] = UNSET,
    east_bound_longitude_gte: Union[Unset, float] = UNSET,
    east_bound_longitude_icontains: Union[Unset, float] = UNSET,
    east_bound_longitude_iendswith: Union[Unset, float] = UNSET,
    east_bound_longitude_iexact: Union[Unset, float] = UNSET,
    east_bound_longitude_in: Union[Unset, list[float]] = UNSET,
    east_bound_longitude_iregex: Union[Unset, float] = UNSET,
    east_bound_longitude_isnull: Union[Unset, bool] = UNSET,
    east_bound_longitude_istartswith: Union[Unset, float] = UNSET,
    east_bound_longitude_lt: Union[Unset, float] = UNSET,
    east_bound_longitude_lte: Union[Unset, float] = UNSET,
    east_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    east_bound_longitude_regex: Union[Unset, float] = UNSET,
    east_bound_longitude_startswith: Union[Unset, float] = UNSET,
    limit: Union[Unset, int] = UNSET,
    north_bound_latitude: Union[Unset, float] = UNSET,
    north_bound_latitude_contained_by: Union[Unset, float] = UNSET,
    north_bound_latitude_contains: Union[Unset, float] = UNSET,
    north_bound_latitude_endswith: Union[Unset, float] = UNSET,
    north_bound_latitude_gt: Union[Unset, float] = UNSET,
    north_bound_latitude_gte: Union[Unset, float] = UNSET,
    north_bound_latitude_icontains: Union[Unset, float] = UNSET,
    north_bound_latitude_iendswith: Union[Unset, float] = UNSET,
    north_bound_latitude_iexact: Union[Unset, float] = UNSET,
    north_bound_latitude_in: Union[Unset, list[float]] = UNSET,
    north_bound_latitude_iregex: Union[Unset, float] = UNSET,
    north_bound_latitude_isnull: Union[Unset, bool] = UNSET,
    north_bound_latitude_istartswith: Union[Unset, float] = UNSET,
    north_bound_latitude_lt: Union[Unset, float] = UNSET,
    north_bound_latitude_lte: Union[Unset, float] = UNSET,
    north_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    north_bound_latitude_regex: Union[Unset, float] = UNSET,
    north_bound_latitude_startswith: Union[Unset, float] = UNSET,
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
    south_bound_latitude: Union[Unset, float] = UNSET,
    south_bound_latitude_contained_by: Union[Unset, float] = UNSET,
    south_bound_latitude_contains: Union[Unset, float] = UNSET,
    south_bound_latitude_endswith: Union[Unset, float] = UNSET,
    south_bound_latitude_gt: Union[Unset, float] = UNSET,
    south_bound_latitude_gte: Union[Unset, float] = UNSET,
    south_bound_latitude_icontains: Union[Unset, float] = UNSET,
    south_bound_latitude_iendswith: Union[Unset, float] = UNSET,
    south_bound_latitude_iexact: Union[Unset, float] = UNSET,
    south_bound_latitude_in: Union[Unset, list[float]] = UNSET,
    south_bound_latitude_iregex: Union[Unset, float] = UNSET,
    south_bound_latitude_isnull: Union[Unset, bool] = UNSET,
    south_bound_latitude_istartswith: Union[Unset, float] = UNSET,
    south_bound_latitude_lt: Union[Unset, float] = UNSET,
    south_bound_latitude_lte: Union[Unset, float] = UNSET,
    south_bound_latitude_range: Union[Unset, list[float]] = UNSET,
    south_bound_latitude_regex: Union[Unset, float] = UNSET,
    south_bound_latitude_startswith: Union[Unset, float] = UNSET,
    west_bound_longitude: Union[Unset, float] = UNSET,
    west_bound_longitude_contained_by: Union[Unset, float] = UNSET,
    west_bound_longitude_contains: Union[Unset, float] = UNSET,
    west_bound_longitude_endswith: Union[Unset, float] = UNSET,
    west_bound_longitude_gt: Union[Unset, float] = UNSET,
    west_bound_longitude_gte: Union[Unset, float] = UNSET,
    west_bound_longitude_icontains: Union[Unset, float] = UNSET,
    west_bound_longitude_iendswith: Union[Unset, float] = UNSET,
    west_bound_longitude_iexact: Union[Unset, float] = UNSET,
    west_bound_longitude_in: Union[Unset, list[float]] = UNSET,
    west_bound_longitude_iregex: Union[Unset, float] = UNSET,
    west_bound_longitude_isnull: Union[Unset, bool] = UNSET,
    west_bound_longitude_istartswith: Union[Unset, float] = UNSET,
    west_bound_longitude_lt: Union[Unset, float] = UNSET,
    west_bound_longitude_lte: Union[Unset, float] = UNSET,
    west_bound_longitude_range: Union[Unset, list[float]] = UNSET,
    west_bound_longitude_regex: Union[Unset, float] = UNSET,
    west_bound_longitude_startswith: Union[Unset, float] = UNSET,
) -> Optional[PaginatedGeographicBoundingBoxReadList]:
    """Get a list of geographic bounding box objects. GeographicBoundingBoxes have a 1:many mapping with
    Observations.

    Args:
        bbox_name (Union[Unset, str]):
        bbox_name_contains (Union[Unset, str]):
        bbox_name_endswith (Union[Unset, str]):
        bbox_name_gt (Union[Unset, str]):
        bbox_name_gte (Union[Unset, str]):
        bbox_name_icontains (Union[Unset, str]):
        bbox_name_iendswith (Union[Unset, str]):
        bbox_name_iexact (Union[Unset, str]):
        bbox_name_in (Union[Unset, list[str]]):
        bbox_name_iregex (Union[Unset, str]):
        bbox_name_isnull (Union[Unset, bool]):
        bbox_name_istartswith (Union[Unset, str]):
        bbox_name_lt (Union[Unset, str]):
        bbox_name_lte (Union[Unset, str]):
        bbox_name_range (Union[Unset, list[str]]):
        bbox_name_regex (Union[Unset, str]):
        bbox_name_startswith (Union[Unset, str]):
        east_bound_longitude (Union[Unset, float]):
        east_bound_longitude_contained_by (Union[Unset, float]):
        east_bound_longitude_contains (Union[Unset, float]):
        east_bound_longitude_endswith (Union[Unset, float]):
        east_bound_longitude_gt (Union[Unset, float]):
        east_bound_longitude_gte (Union[Unset, float]):
        east_bound_longitude_icontains (Union[Unset, float]):
        east_bound_longitude_iendswith (Union[Unset, float]):
        east_bound_longitude_iexact (Union[Unset, float]):
        east_bound_longitude_in (Union[Unset, list[float]]):
        east_bound_longitude_iregex (Union[Unset, float]):
        east_bound_longitude_isnull (Union[Unset, bool]):
        east_bound_longitude_istartswith (Union[Unset, float]):
        east_bound_longitude_lt (Union[Unset, float]):
        east_bound_longitude_lte (Union[Unset, float]):
        east_bound_longitude_range (Union[Unset, list[float]]):
        east_bound_longitude_regex (Union[Unset, float]):
        east_bound_longitude_startswith (Union[Unset, float]):
        limit (Union[Unset, int]):
        north_bound_latitude (Union[Unset, float]):
        north_bound_latitude_contained_by (Union[Unset, float]):
        north_bound_latitude_contains (Union[Unset, float]):
        north_bound_latitude_endswith (Union[Unset, float]):
        north_bound_latitude_gt (Union[Unset, float]):
        north_bound_latitude_gte (Union[Unset, float]):
        north_bound_latitude_icontains (Union[Unset, float]):
        north_bound_latitude_iendswith (Union[Unset, float]):
        north_bound_latitude_iexact (Union[Unset, float]):
        north_bound_latitude_in (Union[Unset, list[float]]):
        north_bound_latitude_iregex (Union[Unset, float]):
        north_bound_latitude_isnull (Union[Unset, bool]):
        north_bound_latitude_istartswith (Union[Unset, float]):
        north_bound_latitude_lt (Union[Unset, float]):
        north_bound_latitude_lte (Union[Unset, float]):
        north_bound_latitude_range (Union[Unset, list[float]]):
        north_bound_latitude_regex (Union[Unset, float]):
        north_bound_latitude_startswith (Union[Unset, float]):
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
        south_bound_latitude (Union[Unset, float]):
        south_bound_latitude_contained_by (Union[Unset, float]):
        south_bound_latitude_contains (Union[Unset, float]):
        south_bound_latitude_endswith (Union[Unset, float]):
        south_bound_latitude_gt (Union[Unset, float]):
        south_bound_latitude_gte (Union[Unset, float]):
        south_bound_latitude_icontains (Union[Unset, float]):
        south_bound_latitude_iendswith (Union[Unset, float]):
        south_bound_latitude_iexact (Union[Unset, float]):
        south_bound_latitude_in (Union[Unset, list[float]]):
        south_bound_latitude_iregex (Union[Unset, float]):
        south_bound_latitude_isnull (Union[Unset, bool]):
        south_bound_latitude_istartswith (Union[Unset, float]):
        south_bound_latitude_lt (Union[Unset, float]):
        south_bound_latitude_lte (Union[Unset, float]):
        south_bound_latitude_range (Union[Unset, list[float]]):
        south_bound_latitude_regex (Union[Unset, float]):
        south_bound_latitude_startswith (Union[Unset, float]):
        west_bound_longitude (Union[Unset, float]):
        west_bound_longitude_contained_by (Union[Unset, float]):
        west_bound_longitude_contains (Union[Unset, float]):
        west_bound_longitude_endswith (Union[Unset, float]):
        west_bound_longitude_gt (Union[Unset, float]):
        west_bound_longitude_gte (Union[Unset, float]):
        west_bound_longitude_icontains (Union[Unset, float]):
        west_bound_longitude_iendswith (Union[Unset, float]):
        west_bound_longitude_iexact (Union[Unset, float]):
        west_bound_longitude_in (Union[Unset, list[float]]):
        west_bound_longitude_iregex (Union[Unset, float]):
        west_bound_longitude_isnull (Union[Unset, bool]):
        west_bound_longitude_istartswith (Union[Unset, float]):
        west_bound_longitude_lt (Union[Unset, float]):
        west_bound_longitude_lte (Union[Unset, float]):
        west_bound_longitude_range (Union[Unset, list[float]]):
        west_bound_longitude_regex (Union[Unset, float]):
        west_bound_longitude_startswith (Union[Unset, float]):

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
            offset=offset,
            ordering=ordering,
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
