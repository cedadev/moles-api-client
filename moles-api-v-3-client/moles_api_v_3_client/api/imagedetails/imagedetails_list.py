from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_image_details_read_list import PaginatedImageDetailsReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    file_description: Union[Unset, str] = UNSET,
    file_description_contains: Union[Unset, str] = UNSET,
    file_description_endswith: Union[Unset, str] = UNSET,
    file_description_gt: Union[Unset, str] = UNSET,
    file_description_gte: Union[Unset, str] = UNSET,
    file_description_icontains: Union[Unset, str] = UNSET,
    file_description_iendswith: Union[Unset, str] = UNSET,
    file_description_iexact: Union[Unset, str] = UNSET,
    file_description_in: Union[Unset, list[str]] = UNSET,
    file_description_iregex: Union[Unset, str] = UNSET,
    file_description_isnull: Union[Unset, bool] = UNSET,
    file_description_istartswith: Union[Unset, str] = UNSET,
    file_description_lt: Union[Unset, str] = UNSET,
    file_description_lte: Union[Unset, str] = UNSET,
    file_description_range: Union[Unset, list[str]] = UNSET,
    file_description_regex: Union[Unset, str] = UNSET,
    file_description_startswith: Union[Unset, str] = UNSET,
    file_name: Union[Unset, str] = UNSET,
    file_name_contains: Union[Unset, str] = UNSET,
    file_name_endswith: Union[Unset, str] = UNSET,
    file_name_gt: Union[Unset, str] = UNSET,
    file_name_gte: Union[Unset, str] = UNSET,
    file_name_icontains: Union[Unset, str] = UNSET,
    file_name_iendswith: Union[Unset, str] = UNSET,
    file_name_iexact: Union[Unset, str] = UNSET,
    file_name_in: Union[Unset, list[str]] = UNSET,
    file_name_iregex: Union[Unset, str] = UNSET,
    file_name_isnull: Union[Unset, bool] = UNSET,
    file_name_istartswith: Union[Unset, str] = UNSET,
    file_name_lt: Union[Unset, str] = UNSET,
    file_name_lte: Union[Unset, str] = UNSET,
    file_name_range: Union[Unset, list[str]] = UNSET,
    file_name_regex: Union[Unset, str] = UNSET,
    file_name_startswith: Union[Unset, str] = UNSET,
    image_constraints: Union[Unset, int] = UNSET,
    image_constraints_gt: Union[Unset, int] = UNSET,
    image_constraints_gte: Union[Unset, int] = UNSET,
    image_constraints_in: Union[Unset, list[int]] = UNSET,
    image_constraints_isnull: Union[Unset, bool] = UNSET,
    image_constraints_lt: Union[Unset, int] = UNSET,
    image_constraints_lte: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    linkage: Union[Unset, str] = UNSET,
    linkage_contains: Union[Unset, str] = UNSET,
    linkage_endswith: Union[Unset, str] = UNSET,
    linkage_gt: Union[Unset, str] = UNSET,
    linkage_gte: Union[Unset, str] = UNSET,
    linkage_icontains: Union[Unset, str] = UNSET,
    linkage_iendswith: Union[Unset, str] = UNSET,
    linkage_iexact: Union[Unset, str] = UNSET,
    linkage_in: Union[Unset, list[str]] = UNSET,
    linkage_iregex: Union[Unset, str] = UNSET,
    linkage_isnull: Union[Unset, bool] = UNSET,
    linkage_istartswith: Union[Unset, str] = UNSET,
    linkage_lt: Union[Unset, str] = UNSET,
    linkage_lte: Union[Unset, str] = UNSET,
    linkage_range: Union[Unset, list[str]] = UNSET,
    linkage_regex: Union[Unset, str] = UNSET,
    linkage_startswith: Union[Unset, str] = UNSET,
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
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["fileDescription"] = file_description

    params["fileDescription__contains"] = file_description_contains

    params["fileDescription__endswith"] = file_description_endswith

    params["fileDescription__gt"] = file_description_gt

    params["fileDescription__gte"] = file_description_gte

    params["fileDescription__icontains"] = file_description_icontains

    params["fileDescription__iendswith"] = file_description_iendswith

    params["fileDescription__iexact"] = file_description_iexact

    json_file_description_in: Union[Unset, list[str]] = UNSET
    if not isinstance(file_description_in, Unset):
        json_file_description_in = file_description_in

    params["fileDescription__in"] = json_file_description_in

    params["fileDescription__iregex"] = file_description_iregex

    params["fileDescription__isnull"] = file_description_isnull

    params["fileDescription__istartswith"] = file_description_istartswith

    params["fileDescription__lt"] = file_description_lt

    params["fileDescription__lte"] = file_description_lte

    json_file_description_range: Union[Unset, list[str]] = UNSET
    if not isinstance(file_description_range, Unset):
        json_file_description_range = file_description_range

    params["fileDescription__range"] = json_file_description_range

    params["fileDescription__regex"] = file_description_regex

    params["fileDescription__startswith"] = file_description_startswith

    params["fileName"] = file_name

    params["fileName__contains"] = file_name_contains

    params["fileName__endswith"] = file_name_endswith

    params["fileName__gt"] = file_name_gt

    params["fileName__gte"] = file_name_gte

    params["fileName__icontains"] = file_name_icontains

    params["fileName__iendswith"] = file_name_iendswith

    params["fileName__iexact"] = file_name_iexact

    json_file_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_in, Unset):
        json_file_name_in = file_name_in

    params["fileName__in"] = json_file_name_in

    params["fileName__iregex"] = file_name_iregex

    params["fileName__isnull"] = file_name_isnull

    params["fileName__istartswith"] = file_name_istartswith

    params["fileName__lt"] = file_name_lt

    params["fileName__lte"] = file_name_lte

    json_file_name_range: Union[Unset, list[str]] = UNSET
    if not isinstance(file_name_range, Unset):
        json_file_name_range = file_name_range

    params["fileName__range"] = json_file_name_range

    params["fileName__regex"] = file_name_regex

    params["fileName__startswith"] = file_name_startswith

    params["imageConstraints"] = image_constraints

    params["imageConstraints__gt"] = image_constraints_gt

    params["imageConstraints__gte"] = image_constraints_gte

    json_image_constraints_in: Union[Unset, list[int]] = UNSET
    if not isinstance(image_constraints_in, Unset):
        json_image_constraints_in = image_constraints_in

    params["imageConstraints__in"] = json_image_constraints_in

    params["imageConstraints__isnull"] = image_constraints_isnull

    params["imageConstraints__lt"] = image_constraints_lt

    params["imageConstraints__lte"] = image_constraints_lte

    params["limit"] = limit

    params["linkage"] = linkage

    params["linkage__contains"] = linkage_contains

    params["linkage__endswith"] = linkage_endswith

    params["linkage__gt"] = linkage_gt

    params["linkage__gte"] = linkage_gte

    params["linkage__icontains"] = linkage_icontains

    params["linkage__iendswith"] = linkage_iendswith

    params["linkage__iexact"] = linkage_iexact

    json_linkage_in: Union[Unset, list[str]] = UNSET
    if not isinstance(linkage_in, Unset):
        json_linkage_in = linkage_in

    params["linkage__in"] = json_linkage_in

    params["linkage__iregex"] = linkage_iregex

    params["linkage__isnull"] = linkage_isnull

    params["linkage__istartswith"] = linkage_istartswith

    params["linkage__lt"] = linkage_lt

    params["linkage__lte"] = linkage_lte

    json_linkage_range: Union[Unset, list[str]] = UNSET
    if not isinstance(linkage_range, Unset):
        json_linkage_range = linkage_range

    params["linkage__range"] = json_linkage_range

    params["linkage__regex"] = linkage_regex

    params["linkage__startswith"] = linkage_startswith

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/imagedetails/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedImageDetailsReadList]:
    if response.status_code == 200:
        response_200 = PaginatedImageDetailsReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedImageDetailsReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    file_description: Union[Unset, str] = UNSET,
    file_description_contains: Union[Unset, str] = UNSET,
    file_description_endswith: Union[Unset, str] = UNSET,
    file_description_gt: Union[Unset, str] = UNSET,
    file_description_gte: Union[Unset, str] = UNSET,
    file_description_icontains: Union[Unset, str] = UNSET,
    file_description_iendswith: Union[Unset, str] = UNSET,
    file_description_iexact: Union[Unset, str] = UNSET,
    file_description_in: Union[Unset, list[str]] = UNSET,
    file_description_iregex: Union[Unset, str] = UNSET,
    file_description_isnull: Union[Unset, bool] = UNSET,
    file_description_istartswith: Union[Unset, str] = UNSET,
    file_description_lt: Union[Unset, str] = UNSET,
    file_description_lte: Union[Unset, str] = UNSET,
    file_description_range: Union[Unset, list[str]] = UNSET,
    file_description_regex: Union[Unset, str] = UNSET,
    file_description_startswith: Union[Unset, str] = UNSET,
    file_name: Union[Unset, str] = UNSET,
    file_name_contains: Union[Unset, str] = UNSET,
    file_name_endswith: Union[Unset, str] = UNSET,
    file_name_gt: Union[Unset, str] = UNSET,
    file_name_gte: Union[Unset, str] = UNSET,
    file_name_icontains: Union[Unset, str] = UNSET,
    file_name_iendswith: Union[Unset, str] = UNSET,
    file_name_iexact: Union[Unset, str] = UNSET,
    file_name_in: Union[Unset, list[str]] = UNSET,
    file_name_iregex: Union[Unset, str] = UNSET,
    file_name_isnull: Union[Unset, bool] = UNSET,
    file_name_istartswith: Union[Unset, str] = UNSET,
    file_name_lt: Union[Unset, str] = UNSET,
    file_name_lte: Union[Unset, str] = UNSET,
    file_name_range: Union[Unset, list[str]] = UNSET,
    file_name_regex: Union[Unset, str] = UNSET,
    file_name_startswith: Union[Unset, str] = UNSET,
    image_constraints: Union[Unset, int] = UNSET,
    image_constraints_gt: Union[Unset, int] = UNSET,
    image_constraints_gte: Union[Unset, int] = UNSET,
    image_constraints_in: Union[Unset, list[int]] = UNSET,
    image_constraints_isnull: Union[Unset, bool] = UNSET,
    image_constraints_lt: Union[Unset, int] = UNSET,
    image_constraints_lte: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    linkage: Union[Unset, str] = UNSET,
    linkage_contains: Union[Unset, str] = UNSET,
    linkage_endswith: Union[Unset, str] = UNSET,
    linkage_gt: Union[Unset, str] = UNSET,
    linkage_gte: Union[Unset, str] = UNSET,
    linkage_icontains: Union[Unset, str] = UNSET,
    linkage_iendswith: Union[Unset, str] = UNSET,
    linkage_iexact: Union[Unset, str] = UNSET,
    linkage_in: Union[Unset, list[str]] = UNSET,
    linkage_iregex: Union[Unset, str] = UNSET,
    linkage_isnull: Union[Unset, bool] = UNSET,
    linkage_istartswith: Union[Unset, str] = UNSET,
    linkage_lt: Union[Unset, str] = UNSET,
    linkage_lte: Union[Unset, str] = UNSET,
    linkage_range: Union[Unset, list[str]] = UNSET,
    linkage_regex: Union[Unset, str] = UNSET,
    linkage_startswith: Union[Unset, str] = UNSET,
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
) -> Response[PaginatedImageDetailsReadList]:
    """Get a list of ImageDetails objects.

    Args:
        file_description (Union[Unset, str]):
        file_description_contains (Union[Unset, str]):
        file_description_endswith (Union[Unset, str]):
        file_description_gt (Union[Unset, str]):
        file_description_gte (Union[Unset, str]):
        file_description_icontains (Union[Unset, str]):
        file_description_iendswith (Union[Unset, str]):
        file_description_iexact (Union[Unset, str]):
        file_description_in (Union[Unset, list[str]]):
        file_description_iregex (Union[Unset, str]):
        file_description_isnull (Union[Unset, bool]):
        file_description_istartswith (Union[Unset, str]):
        file_description_lt (Union[Unset, str]):
        file_description_lte (Union[Unset, str]):
        file_description_range (Union[Unset, list[str]]):
        file_description_regex (Union[Unset, str]):
        file_description_startswith (Union[Unset, str]):
        file_name (Union[Unset, str]):
        file_name_contains (Union[Unset, str]):
        file_name_endswith (Union[Unset, str]):
        file_name_gt (Union[Unset, str]):
        file_name_gte (Union[Unset, str]):
        file_name_icontains (Union[Unset, str]):
        file_name_iendswith (Union[Unset, str]):
        file_name_iexact (Union[Unset, str]):
        file_name_in (Union[Unset, list[str]]):
        file_name_iregex (Union[Unset, str]):
        file_name_isnull (Union[Unset, bool]):
        file_name_istartswith (Union[Unset, str]):
        file_name_lt (Union[Unset, str]):
        file_name_lte (Union[Unset, str]):
        file_name_range (Union[Unset, list[str]]):
        file_name_regex (Union[Unset, str]):
        file_name_startswith (Union[Unset, str]):
        image_constraints (Union[Unset, int]):
        image_constraints_gt (Union[Unset, int]):
        image_constraints_gte (Union[Unset, int]):
        image_constraints_in (Union[Unset, list[int]]):
        image_constraints_isnull (Union[Unset, bool]):
        image_constraints_lt (Union[Unset, int]):
        image_constraints_lte (Union[Unset, int]):
        limit (Union[Unset, int]):
        linkage (Union[Unset, str]):
        linkage_contains (Union[Unset, str]):
        linkage_endswith (Union[Unset, str]):
        linkage_gt (Union[Unset, str]):
        linkage_gte (Union[Unset, str]):
        linkage_icontains (Union[Unset, str]):
        linkage_iendswith (Union[Unset, str]):
        linkage_iexact (Union[Unset, str]):
        linkage_in (Union[Unset, list[str]]):
        linkage_iregex (Union[Unset, str]):
        linkage_isnull (Union[Unset, bool]):
        linkage_istartswith (Union[Unset, str]):
        linkage_lt (Union[Unset, str]):
        linkage_lte (Union[Unset, str]):
        linkage_range (Union[Unset, list[str]]):
        linkage_regex (Union[Unset, str]):
        linkage_startswith (Union[Unset, str]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedImageDetailsReadList]
    """

    kwargs = _get_kwargs(
        file_description=file_description,
        file_description_contains=file_description_contains,
        file_description_endswith=file_description_endswith,
        file_description_gt=file_description_gt,
        file_description_gte=file_description_gte,
        file_description_icontains=file_description_icontains,
        file_description_iendswith=file_description_iendswith,
        file_description_iexact=file_description_iexact,
        file_description_in=file_description_in,
        file_description_iregex=file_description_iregex,
        file_description_isnull=file_description_isnull,
        file_description_istartswith=file_description_istartswith,
        file_description_lt=file_description_lt,
        file_description_lte=file_description_lte,
        file_description_range=file_description_range,
        file_description_regex=file_description_regex,
        file_description_startswith=file_description_startswith,
        file_name=file_name,
        file_name_contains=file_name_contains,
        file_name_endswith=file_name_endswith,
        file_name_gt=file_name_gt,
        file_name_gte=file_name_gte,
        file_name_icontains=file_name_icontains,
        file_name_iendswith=file_name_iendswith,
        file_name_iexact=file_name_iexact,
        file_name_in=file_name_in,
        file_name_iregex=file_name_iregex,
        file_name_isnull=file_name_isnull,
        file_name_istartswith=file_name_istartswith,
        file_name_lt=file_name_lt,
        file_name_lte=file_name_lte,
        file_name_range=file_name_range,
        file_name_regex=file_name_regex,
        file_name_startswith=file_name_startswith,
        image_constraints=image_constraints,
        image_constraints_gt=image_constraints_gt,
        image_constraints_gte=image_constraints_gte,
        image_constraints_in=image_constraints_in,
        image_constraints_isnull=image_constraints_isnull,
        image_constraints_lt=image_constraints_lt,
        image_constraints_lte=image_constraints_lte,
        limit=limit,
        linkage=linkage,
        linkage_contains=linkage_contains,
        linkage_endswith=linkage_endswith,
        linkage_gt=linkage_gt,
        linkage_gte=linkage_gte,
        linkage_icontains=linkage_icontains,
        linkage_iendswith=linkage_iendswith,
        linkage_iexact=linkage_iexact,
        linkage_in=linkage_in,
        linkage_iregex=linkage_iregex,
        linkage_isnull=linkage_isnull,
        linkage_istartswith=linkage_istartswith,
        linkage_lt=linkage_lt,
        linkage_lte=linkage_lte,
        linkage_range=linkage_range,
        linkage_regex=linkage_regex,
        linkage_startswith=linkage_startswith,
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    file_description: Union[Unset, str] = UNSET,
    file_description_contains: Union[Unset, str] = UNSET,
    file_description_endswith: Union[Unset, str] = UNSET,
    file_description_gt: Union[Unset, str] = UNSET,
    file_description_gte: Union[Unset, str] = UNSET,
    file_description_icontains: Union[Unset, str] = UNSET,
    file_description_iendswith: Union[Unset, str] = UNSET,
    file_description_iexact: Union[Unset, str] = UNSET,
    file_description_in: Union[Unset, list[str]] = UNSET,
    file_description_iregex: Union[Unset, str] = UNSET,
    file_description_isnull: Union[Unset, bool] = UNSET,
    file_description_istartswith: Union[Unset, str] = UNSET,
    file_description_lt: Union[Unset, str] = UNSET,
    file_description_lte: Union[Unset, str] = UNSET,
    file_description_range: Union[Unset, list[str]] = UNSET,
    file_description_regex: Union[Unset, str] = UNSET,
    file_description_startswith: Union[Unset, str] = UNSET,
    file_name: Union[Unset, str] = UNSET,
    file_name_contains: Union[Unset, str] = UNSET,
    file_name_endswith: Union[Unset, str] = UNSET,
    file_name_gt: Union[Unset, str] = UNSET,
    file_name_gte: Union[Unset, str] = UNSET,
    file_name_icontains: Union[Unset, str] = UNSET,
    file_name_iendswith: Union[Unset, str] = UNSET,
    file_name_iexact: Union[Unset, str] = UNSET,
    file_name_in: Union[Unset, list[str]] = UNSET,
    file_name_iregex: Union[Unset, str] = UNSET,
    file_name_isnull: Union[Unset, bool] = UNSET,
    file_name_istartswith: Union[Unset, str] = UNSET,
    file_name_lt: Union[Unset, str] = UNSET,
    file_name_lte: Union[Unset, str] = UNSET,
    file_name_range: Union[Unset, list[str]] = UNSET,
    file_name_regex: Union[Unset, str] = UNSET,
    file_name_startswith: Union[Unset, str] = UNSET,
    image_constraints: Union[Unset, int] = UNSET,
    image_constraints_gt: Union[Unset, int] = UNSET,
    image_constraints_gte: Union[Unset, int] = UNSET,
    image_constraints_in: Union[Unset, list[int]] = UNSET,
    image_constraints_isnull: Union[Unset, bool] = UNSET,
    image_constraints_lt: Union[Unset, int] = UNSET,
    image_constraints_lte: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    linkage: Union[Unset, str] = UNSET,
    linkage_contains: Union[Unset, str] = UNSET,
    linkage_endswith: Union[Unset, str] = UNSET,
    linkage_gt: Union[Unset, str] = UNSET,
    linkage_gte: Union[Unset, str] = UNSET,
    linkage_icontains: Union[Unset, str] = UNSET,
    linkage_iendswith: Union[Unset, str] = UNSET,
    linkage_iexact: Union[Unset, str] = UNSET,
    linkage_in: Union[Unset, list[str]] = UNSET,
    linkage_iregex: Union[Unset, str] = UNSET,
    linkage_isnull: Union[Unset, bool] = UNSET,
    linkage_istartswith: Union[Unset, str] = UNSET,
    linkage_lt: Union[Unset, str] = UNSET,
    linkage_lte: Union[Unset, str] = UNSET,
    linkage_range: Union[Unset, list[str]] = UNSET,
    linkage_regex: Union[Unset, str] = UNSET,
    linkage_startswith: Union[Unset, str] = UNSET,
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
) -> Optional[PaginatedImageDetailsReadList]:
    """Get a list of ImageDetails objects.

    Args:
        file_description (Union[Unset, str]):
        file_description_contains (Union[Unset, str]):
        file_description_endswith (Union[Unset, str]):
        file_description_gt (Union[Unset, str]):
        file_description_gte (Union[Unset, str]):
        file_description_icontains (Union[Unset, str]):
        file_description_iendswith (Union[Unset, str]):
        file_description_iexact (Union[Unset, str]):
        file_description_in (Union[Unset, list[str]]):
        file_description_iregex (Union[Unset, str]):
        file_description_isnull (Union[Unset, bool]):
        file_description_istartswith (Union[Unset, str]):
        file_description_lt (Union[Unset, str]):
        file_description_lte (Union[Unset, str]):
        file_description_range (Union[Unset, list[str]]):
        file_description_regex (Union[Unset, str]):
        file_description_startswith (Union[Unset, str]):
        file_name (Union[Unset, str]):
        file_name_contains (Union[Unset, str]):
        file_name_endswith (Union[Unset, str]):
        file_name_gt (Union[Unset, str]):
        file_name_gte (Union[Unset, str]):
        file_name_icontains (Union[Unset, str]):
        file_name_iendswith (Union[Unset, str]):
        file_name_iexact (Union[Unset, str]):
        file_name_in (Union[Unset, list[str]]):
        file_name_iregex (Union[Unset, str]):
        file_name_isnull (Union[Unset, bool]):
        file_name_istartswith (Union[Unset, str]):
        file_name_lt (Union[Unset, str]):
        file_name_lte (Union[Unset, str]):
        file_name_range (Union[Unset, list[str]]):
        file_name_regex (Union[Unset, str]):
        file_name_startswith (Union[Unset, str]):
        image_constraints (Union[Unset, int]):
        image_constraints_gt (Union[Unset, int]):
        image_constraints_gte (Union[Unset, int]):
        image_constraints_in (Union[Unset, list[int]]):
        image_constraints_isnull (Union[Unset, bool]):
        image_constraints_lt (Union[Unset, int]):
        image_constraints_lte (Union[Unset, int]):
        limit (Union[Unset, int]):
        linkage (Union[Unset, str]):
        linkage_contains (Union[Unset, str]):
        linkage_endswith (Union[Unset, str]):
        linkage_gt (Union[Unset, str]):
        linkage_gte (Union[Unset, str]):
        linkage_icontains (Union[Unset, str]):
        linkage_iendswith (Union[Unset, str]):
        linkage_iexact (Union[Unset, str]):
        linkage_in (Union[Unset, list[str]]):
        linkage_iregex (Union[Unset, str]):
        linkage_isnull (Union[Unset, bool]):
        linkage_istartswith (Union[Unset, str]):
        linkage_lt (Union[Unset, str]):
        linkage_lte (Union[Unset, str]):
        linkage_range (Union[Unset, list[str]]):
        linkage_regex (Union[Unset, str]):
        linkage_startswith (Union[Unset, str]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedImageDetailsReadList
    """

    return sync_detailed(
        client=client,
        file_description=file_description,
        file_description_contains=file_description_contains,
        file_description_endswith=file_description_endswith,
        file_description_gt=file_description_gt,
        file_description_gte=file_description_gte,
        file_description_icontains=file_description_icontains,
        file_description_iendswith=file_description_iendswith,
        file_description_iexact=file_description_iexact,
        file_description_in=file_description_in,
        file_description_iregex=file_description_iregex,
        file_description_isnull=file_description_isnull,
        file_description_istartswith=file_description_istartswith,
        file_description_lt=file_description_lt,
        file_description_lte=file_description_lte,
        file_description_range=file_description_range,
        file_description_regex=file_description_regex,
        file_description_startswith=file_description_startswith,
        file_name=file_name,
        file_name_contains=file_name_contains,
        file_name_endswith=file_name_endswith,
        file_name_gt=file_name_gt,
        file_name_gte=file_name_gte,
        file_name_icontains=file_name_icontains,
        file_name_iendswith=file_name_iendswith,
        file_name_iexact=file_name_iexact,
        file_name_in=file_name_in,
        file_name_iregex=file_name_iregex,
        file_name_isnull=file_name_isnull,
        file_name_istartswith=file_name_istartswith,
        file_name_lt=file_name_lt,
        file_name_lte=file_name_lte,
        file_name_range=file_name_range,
        file_name_regex=file_name_regex,
        file_name_startswith=file_name_startswith,
        image_constraints=image_constraints,
        image_constraints_gt=image_constraints_gt,
        image_constraints_gte=image_constraints_gte,
        image_constraints_in=image_constraints_in,
        image_constraints_isnull=image_constraints_isnull,
        image_constraints_lt=image_constraints_lt,
        image_constraints_lte=image_constraints_lte,
        limit=limit,
        linkage=linkage,
        linkage_contains=linkage_contains,
        linkage_endswith=linkage_endswith,
        linkage_gt=linkage_gt,
        linkage_gte=linkage_gte,
        linkage_icontains=linkage_icontains,
        linkage_iendswith=linkage_iendswith,
        linkage_iexact=linkage_iexact,
        linkage_in=linkage_in,
        linkage_iregex=linkage_iregex,
        linkage_isnull=linkage_isnull,
        linkage_istartswith=linkage_istartswith,
        linkage_lt=linkage_lt,
        linkage_lte=linkage_lte,
        linkage_range=linkage_range,
        linkage_regex=linkage_regex,
        linkage_startswith=linkage_startswith,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    file_description: Union[Unset, str] = UNSET,
    file_description_contains: Union[Unset, str] = UNSET,
    file_description_endswith: Union[Unset, str] = UNSET,
    file_description_gt: Union[Unset, str] = UNSET,
    file_description_gte: Union[Unset, str] = UNSET,
    file_description_icontains: Union[Unset, str] = UNSET,
    file_description_iendswith: Union[Unset, str] = UNSET,
    file_description_iexact: Union[Unset, str] = UNSET,
    file_description_in: Union[Unset, list[str]] = UNSET,
    file_description_iregex: Union[Unset, str] = UNSET,
    file_description_isnull: Union[Unset, bool] = UNSET,
    file_description_istartswith: Union[Unset, str] = UNSET,
    file_description_lt: Union[Unset, str] = UNSET,
    file_description_lte: Union[Unset, str] = UNSET,
    file_description_range: Union[Unset, list[str]] = UNSET,
    file_description_regex: Union[Unset, str] = UNSET,
    file_description_startswith: Union[Unset, str] = UNSET,
    file_name: Union[Unset, str] = UNSET,
    file_name_contains: Union[Unset, str] = UNSET,
    file_name_endswith: Union[Unset, str] = UNSET,
    file_name_gt: Union[Unset, str] = UNSET,
    file_name_gte: Union[Unset, str] = UNSET,
    file_name_icontains: Union[Unset, str] = UNSET,
    file_name_iendswith: Union[Unset, str] = UNSET,
    file_name_iexact: Union[Unset, str] = UNSET,
    file_name_in: Union[Unset, list[str]] = UNSET,
    file_name_iregex: Union[Unset, str] = UNSET,
    file_name_isnull: Union[Unset, bool] = UNSET,
    file_name_istartswith: Union[Unset, str] = UNSET,
    file_name_lt: Union[Unset, str] = UNSET,
    file_name_lte: Union[Unset, str] = UNSET,
    file_name_range: Union[Unset, list[str]] = UNSET,
    file_name_regex: Union[Unset, str] = UNSET,
    file_name_startswith: Union[Unset, str] = UNSET,
    image_constraints: Union[Unset, int] = UNSET,
    image_constraints_gt: Union[Unset, int] = UNSET,
    image_constraints_gte: Union[Unset, int] = UNSET,
    image_constraints_in: Union[Unset, list[int]] = UNSET,
    image_constraints_isnull: Union[Unset, bool] = UNSET,
    image_constraints_lt: Union[Unset, int] = UNSET,
    image_constraints_lte: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    linkage: Union[Unset, str] = UNSET,
    linkage_contains: Union[Unset, str] = UNSET,
    linkage_endswith: Union[Unset, str] = UNSET,
    linkage_gt: Union[Unset, str] = UNSET,
    linkage_gte: Union[Unset, str] = UNSET,
    linkage_icontains: Union[Unset, str] = UNSET,
    linkage_iendswith: Union[Unset, str] = UNSET,
    linkage_iexact: Union[Unset, str] = UNSET,
    linkage_in: Union[Unset, list[str]] = UNSET,
    linkage_iregex: Union[Unset, str] = UNSET,
    linkage_isnull: Union[Unset, bool] = UNSET,
    linkage_istartswith: Union[Unset, str] = UNSET,
    linkage_lt: Union[Unset, str] = UNSET,
    linkage_lte: Union[Unset, str] = UNSET,
    linkage_range: Union[Unset, list[str]] = UNSET,
    linkage_regex: Union[Unset, str] = UNSET,
    linkage_startswith: Union[Unset, str] = UNSET,
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
) -> Response[PaginatedImageDetailsReadList]:
    """Get a list of ImageDetails objects.

    Args:
        file_description (Union[Unset, str]):
        file_description_contains (Union[Unset, str]):
        file_description_endswith (Union[Unset, str]):
        file_description_gt (Union[Unset, str]):
        file_description_gte (Union[Unset, str]):
        file_description_icontains (Union[Unset, str]):
        file_description_iendswith (Union[Unset, str]):
        file_description_iexact (Union[Unset, str]):
        file_description_in (Union[Unset, list[str]]):
        file_description_iregex (Union[Unset, str]):
        file_description_isnull (Union[Unset, bool]):
        file_description_istartswith (Union[Unset, str]):
        file_description_lt (Union[Unset, str]):
        file_description_lte (Union[Unset, str]):
        file_description_range (Union[Unset, list[str]]):
        file_description_regex (Union[Unset, str]):
        file_description_startswith (Union[Unset, str]):
        file_name (Union[Unset, str]):
        file_name_contains (Union[Unset, str]):
        file_name_endswith (Union[Unset, str]):
        file_name_gt (Union[Unset, str]):
        file_name_gte (Union[Unset, str]):
        file_name_icontains (Union[Unset, str]):
        file_name_iendswith (Union[Unset, str]):
        file_name_iexact (Union[Unset, str]):
        file_name_in (Union[Unset, list[str]]):
        file_name_iregex (Union[Unset, str]):
        file_name_isnull (Union[Unset, bool]):
        file_name_istartswith (Union[Unset, str]):
        file_name_lt (Union[Unset, str]):
        file_name_lte (Union[Unset, str]):
        file_name_range (Union[Unset, list[str]]):
        file_name_regex (Union[Unset, str]):
        file_name_startswith (Union[Unset, str]):
        image_constraints (Union[Unset, int]):
        image_constraints_gt (Union[Unset, int]):
        image_constraints_gte (Union[Unset, int]):
        image_constraints_in (Union[Unset, list[int]]):
        image_constraints_isnull (Union[Unset, bool]):
        image_constraints_lt (Union[Unset, int]):
        image_constraints_lte (Union[Unset, int]):
        limit (Union[Unset, int]):
        linkage (Union[Unset, str]):
        linkage_contains (Union[Unset, str]):
        linkage_endswith (Union[Unset, str]):
        linkage_gt (Union[Unset, str]):
        linkage_gte (Union[Unset, str]):
        linkage_icontains (Union[Unset, str]):
        linkage_iendswith (Union[Unset, str]):
        linkage_iexact (Union[Unset, str]):
        linkage_in (Union[Unset, list[str]]):
        linkage_iregex (Union[Unset, str]):
        linkage_isnull (Union[Unset, bool]):
        linkage_istartswith (Union[Unset, str]):
        linkage_lt (Union[Unset, str]):
        linkage_lte (Union[Unset, str]):
        linkage_range (Union[Unset, list[str]]):
        linkage_regex (Union[Unset, str]):
        linkage_startswith (Union[Unset, str]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedImageDetailsReadList]
    """

    kwargs = _get_kwargs(
        file_description=file_description,
        file_description_contains=file_description_contains,
        file_description_endswith=file_description_endswith,
        file_description_gt=file_description_gt,
        file_description_gte=file_description_gte,
        file_description_icontains=file_description_icontains,
        file_description_iendswith=file_description_iendswith,
        file_description_iexact=file_description_iexact,
        file_description_in=file_description_in,
        file_description_iregex=file_description_iregex,
        file_description_isnull=file_description_isnull,
        file_description_istartswith=file_description_istartswith,
        file_description_lt=file_description_lt,
        file_description_lte=file_description_lte,
        file_description_range=file_description_range,
        file_description_regex=file_description_regex,
        file_description_startswith=file_description_startswith,
        file_name=file_name,
        file_name_contains=file_name_contains,
        file_name_endswith=file_name_endswith,
        file_name_gt=file_name_gt,
        file_name_gte=file_name_gte,
        file_name_icontains=file_name_icontains,
        file_name_iendswith=file_name_iendswith,
        file_name_iexact=file_name_iexact,
        file_name_in=file_name_in,
        file_name_iregex=file_name_iregex,
        file_name_isnull=file_name_isnull,
        file_name_istartswith=file_name_istartswith,
        file_name_lt=file_name_lt,
        file_name_lte=file_name_lte,
        file_name_range=file_name_range,
        file_name_regex=file_name_regex,
        file_name_startswith=file_name_startswith,
        image_constraints=image_constraints,
        image_constraints_gt=image_constraints_gt,
        image_constraints_gte=image_constraints_gte,
        image_constraints_in=image_constraints_in,
        image_constraints_isnull=image_constraints_isnull,
        image_constraints_lt=image_constraints_lt,
        image_constraints_lte=image_constraints_lte,
        limit=limit,
        linkage=linkage,
        linkage_contains=linkage_contains,
        linkage_endswith=linkage_endswith,
        linkage_gt=linkage_gt,
        linkage_gte=linkage_gte,
        linkage_icontains=linkage_icontains,
        linkage_iendswith=linkage_iendswith,
        linkage_iexact=linkage_iexact,
        linkage_in=linkage_in,
        linkage_iregex=linkage_iregex,
        linkage_isnull=linkage_isnull,
        linkage_istartswith=linkage_istartswith,
        linkage_lt=linkage_lt,
        linkage_lte=linkage_lte,
        linkage_range=linkage_range,
        linkage_regex=linkage_regex,
        linkage_startswith=linkage_startswith,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    file_description: Union[Unset, str] = UNSET,
    file_description_contains: Union[Unset, str] = UNSET,
    file_description_endswith: Union[Unset, str] = UNSET,
    file_description_gt: Union[Unset, str] = UNSET,
    file_description_gte: Union[Unset, str] = UNSET,
    file_description_icontains: Union[Unset, str] = UNSET,
    file_description_iendswith: Union[Unset, str] = UNSET,
    file_description_iexact: Union[Unset, str] = UNSET,
    file_description_in: Union[Unset, list[str]] = UNSET,
    file_description_iregex: Union[Unset, str] = UNSET,
    file_description_isnull: Union[Unset, bool] = UNSET,
    file_description_istartswith: Union[Unset, str] = UNSET,
    file_description_lt: Union[Unset, str] = UNSET,
    file_description_lte: Union[Unset, str] = UNSET,
    file_description_range: Union[Unset, list[str]] = UNSET,
    file_description_regex: Union[Unset, str] = UNSET,
    file_description_startswith: Union[Unset, str] = UNSET,
    file_name: Union[Unset, str] = UNSET,
    file_name_contains: Union[Unset, str] = UNSET,
    file_name_endswith: Union[Unset, str] = UNSET,
    file_name_gt: Union[Unset, str] = UNSET,
    file_name_gte: Union[Unset, str] = UNSET,
    file_name_icontains: Union[Unset, str] = UNSET,
    file_name_iendswith: Union[Unset, str] = UNSET,
    file_name_iexact: Union[Unset, str] = UNSET,
    file_name_in: Union[Unset, list[str]] = UNSET,
    file_name_iregex: Union[Unset, str] = UNSET,
    file_name_isnull: Union[Unset, bool] = UNSET,
    file_name_istartswith: Union[Unset, str] = UNSET,
    file_name_lt: Union[Unset, str] = UNSET,
    file_name_lte: Union[Unset, str] = UNSET,
    file_name_range: Union[Unset, list[str]] = UNSET,
    file_name_regex: Union[Unset, str] = UNSET,
    file_name_startswith: Union[Unset, str] = UNSET,
    image_constraints: Union[Unset, int] = UNSET,
    image_constraints_gt: Union[Unset, int] = UNSET,
    image_constraints_gte: Union[Unset, int] = UNSET,
    image_constraints_in: Union[Unset, list[int]] = UNSET,
    image_constraints_isnull: Union[Unset, bool] = UNSET,
    image_constraints_lt: Union[Unset, int] = UNSET,
    image_constraints_lte: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    linkage: Union[Unset, str] = UNSET,
    linkage_contains: Union[Unset, str] = UNSET,
    linkage_endswith: Union[Unset, str] = UNSET,
    linkage_gt: Union[Unset, str] = UNSET,
    linkage_gte: Union[Unset, str] = UNSET,
    linkage_icontains: Union[Unset, str] = UNSET,
    linkage_iendswith: Union[Unset, str] = UNSET,
    linkage_iexact: Union[Unset, str] = UNSET,
    linkage_in: Union[Unset, list[str]] = UNSET,
    linkage_iregex: Union[Unset, str] = UNSET,
    linkage_isnull: Union[Unset, bool] = UNSET,
    linkage_istartswith: Union[Unset, str] = UNSET,
    linkage_lt: Union[Unset, str] = UNSET,
    linkage_lte: Union[Unset, str] = UNSET,
    linkage_range: Union[Unset, list[str]] = UNSET,
    linkage_regex: Union[Unset, str] = UNSET,
    linkage_startswith: Union[Unset, str] = UNSET,
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
) -> Optional[PaginatedImageDetailsReadList]:
    """Get a list of ImageDetails objects.

    Args:
        file_description (Union[Unset, str]):
        file_description_contains (Union[Unset, str]):
        file_description_endswith (Union[Unset, str]):
        file_description_gt (Union[Unset, str]):
        file_description_gte (Union[Unset, str]):
        file_description_icontains (Union[Unset, str]):
        file_description_iendswith (Union[Unset, str]):
        file_description_iexact (Union[Unset, str]):
        file_description_in (Union[Unset, list[str]]):
        file_description_iregex (Union[Unset, str]):
        file_description_isnull (Union[Unset, bool]):
        file_description_istartswith (Union[Unset, str]):
        file_description_lt (Union[Unset, str]):
        file_description_lte (Union[Unset, str]):
        file_description_range (Union[Unset, list[str]]):
        file_description_regex (Union[Unset, str]):
        file_description_startswith (Union[Unset, str]):
        file_name (Union[Unset, str]):
        file_name_contains (Union[Unset, str]):
        file_name_endswith (Union[Unset, str]):
        file_name_gt (Union[Unset, str]):
        file_name_gte (Union[Unset, str]):
        file_name_icontains (Union[Unset, str]):
        file_name_iendswith (Union[Unset, str]):
        file_name_iexact (Union[Unset, str]):
        file_name_in (Union[Unset, list[str]]):
        file_name_iregex (Union[Unset, str]):
        file_name_isnull (Union[Unset, bool]):
        file_name_istartswith (Union[Unset, str]):
        file_name_lt (Union[Unset, str]):
        file_name_lte (Union[Unset, str]):
        file_name_range (Union[Unset, list[str]]):
        file_name_regex (Union[Unset, str]):
        file_name_startswith (Union[Unset, str]):
        image_constraints (Union[Unset, int]):
        image_constraints_gt (Union[Unset, int]):
        image_constraints_gte (Union[Unset, int]):
        image_constraints_in (Union[Unset, list[int]]):
        image_constraints_isnull (Union[Unset, bool]):
        image_constraints_lt (Union[Unset, int]):
        image_constraints_lte (Union[Unset, int]):
        limit (Union[Unset, int]):
        linkage (Union[Unset, str]):
        linkage_contains (Union[Unset, str]):
        linkage_endswith (Union[Unset, str]):
        linkage_gt (Union[Unset, str]):
        linkage_gte (Union[Unset, str]):
        linkage_icontains (Union[Unset, str]):
        linkage_iendswith (Union[Unset, str]):
        linkage_iexact (Union[Unset, str]):
        linkage_in (Union[Unset, list[str]]):
        linkage_iregex (Union[Unset, str]):
        linkage_isnull (Union[Unset, bool]):
        linkage_istartswith (Union[Unset, str]):
        linkage_lt (Union[Unset, str]):
        linkage_lte (Union[Unset, str]):
        linkage_range (Union[Unset, list[str]]):
        linkage_regex (Union[Unset, str]):
        linkage_startswith (Union[Unset, str]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedImageDetailsReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            file_description=file_description,
            file_description_contains=file_description_contains,
            file_description_endswith=file_description_endswith,
            file_description_gt=file_description_gt,
            file_description_gte=file_description_gte,
            file_description_icontains=file_description_icontains,
            file_description_iendswith=file_description_iendswith,
            file_description_iexact=file_description_iexact,
            file_description_in=file_description_in,
            file_description_iregex=file_description_iregex,
            file_description_isnull=file_description_isnull,
            file_description_istartswith=file_description_istartswith,
            file_description_lt=file_description_lt,
            file_description_lte=file_description_lte,
            file_description_range=file_description_range,
            file_description_regex=file_description_regex,
            file_description_startswith=file_description_startswith,
            file_name=file_name,
            file_name_contains=file_name_contains,
            file_name_endswith=file_name_endswith,
            file_name_gt=file_name_gt,
            file_name_gte=file_name_gte,
            file_name_icontains=file_name_icontains,
            file_name_iendswith=file_name_iendswith,
            file_name_iexact=file_name_iexact,
            file_name_in=file_name_in,
            file_name_iregex=file_name_iregex,
            file_name_isnull=file_name_isnull,
            file_name_istartswith=file_name_istartswith,
            file_name_lt=file_name_lt,
            file_name_lte=file_name_lte,
            file_name_range=file_name_range,
            file_name_regex=file_name_regex,
            file_name_startswith=file_name_startswith,
            image_constraints=image_constraints,
            image_constraints_gt=image_constraints_gt,
            image_constraints_gte=image_constraints_gte,
            image_constraints_in=image_constraints_in,
            image_constraints_isnull=image_constraints_isnull,
            image_constraints_lt=image_constraints_lt,
            image_constraints_lte=image_constraints_lte,
            limit=limit,
            linkage=linkage,
            linkage_contains=linkage_contains,
            linkage_endswith=linkage_endswith,
            linkage_gt=linkage_gt,
            linkage_gte=linkage_gte,
            linkage_icontains=linkage_icontains,
            linkage_iendswith=linkage_iendswith,
            linkage_iexact=linkage_iexact,
            linkage_in=linkage_in,
            linkage_iregex=linkage_iregex,
            linkage_isnull=linkage_isnull,
            linkage_istartswith=linkage_istartswith,
            linkage_lt=linkage_lt,
            linkage_lte=linkage_lte,
            linkage_range=linkage_range,
            linkage_regex=linkage_regex,
            linkage_startswith=linkage_startswith,
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
        )
    ).parsed
