from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_procedure_acquisition_read_list import PaginatedProcedureAcquisitionReadList
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
    limit: Union[Unset, int] = UNSET,
    mobile_platform_operation_ob_id: Union[Unset, int] = UNSET,
    mobile_platform_operation_ob_id_in: Union[Unset, list[int]] = UNSET,
    mobile_platform_operation_uuid: Union[Unset, str] = UNSET,
    mobile_platform_operation_uuid_in: Union[Unset, list[str]] = UNSET,
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
    output_description: Union[Unset, int] = UNSET,
    output_description_gt: Union[Unset, int] = UNSET,
    output_description_gte: Union[Unset, int] = UNSET,
    output_description_in: Union[Unset, list[int]] = UNSET,
    output_description_isnull: Union[Unset, bool] = UNSET,
    output_description_lt: Union[Unset, int] = UNSET,
    output_description_lte: Union[Unset, int] = UNSET,
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

    params["limit"] = limit

    params["mobilePlatformOperation__ob_id"] = mobile_platform_operation_ob_id

    json_mobile_platform_operation_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(mobile_platform_operation_ob_id_in, Unset):
        json_mobile_platform_operation_ob_id_in = ",".join(map(str, mobile_platform_operation_ob_id_in))

    params["mobilePlatformOperation__ob_id__in"] = json_mobile_platform_operation_ob_id_in

    params["mobilePlatformOperation__uuid"] = mobile_platform_operation_uuid

    json_mobile_platform_operation_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(mobile_platform_operation_uuid_in, Unset):
        json_mobile_platform_operation_uuid_in = ",".join(map(str, mobile_platform_operation_uuid_in))

    params["mobilePlatformOperation__uuid__in"] = json_mobile_platform_operation_uuid_in

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

    params["outputDescription"] = output_description

    params["outputDescription__gt"] = output_description_gt

    params["outputDescription__gte"] = output_description_gte

    json_output_description_in: Union[Unset, list[int]] = UNSET
    if not isinstance(output_description_in, Unset):
        json_output_description_in = ",".join(map(str, output_description_in))

    params["outputDescription__in"] = json_output_description_in

    params["outputDescription__isnull"] = output_description_isnull

    params["outputDescription__lt"] = output_description_lt

    params["outputDescription__lte"] = output_description_lte

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
        "url": "/api/v3/acquisitions/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedProcedureAcquisitionReadList]:
    if response.status_code == 200:
        response_200 = PaginatedProcedureAcquisitionReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedProcedureAcquisitionReadList]:
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
    limit: Union[Unset, int] = UNSET,
    mobile_platform_operation_ob_id: Union[Unset, int] = UNSET,
    mobile_platform_operation_ob_id_in: Union[Unset, list[int]] = UNSET,
    mobile_platform_operation_uuid: Union[Unset, str] = UNSET,
    mobile_platform_operation_uuid_in: Union[Unset, list[str]] = UNSET,
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
    output_description: Union[Unset, int] = UNSET,
    output_description_gt: Union[Unset, int] = UNSET,
    output_description_gte: Union[Unset, int] = UNSET,
    output_description_in: Union[Unset, list[int]] = UNSET,
    output_description_isnull: Union[Unset, bool] = UNSET,
    output_description_lt: Union[Unset, int] = UNSET,
    output_description_lte: Union[Unset, int] = UNSET,
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
) -> Response[PaginatedProcedureAcquisitionReadList]:
    """Get a list of ProcedureAcquisition objects. ProcedureAcquisitions have a 1:1 mapping with
    Observations.

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
        limit (Union[Unset, int]):
        mobile_platform_operation_ob_id (Union[Unset, int]):
        mobile_platform_operation_ob_id_in (Union[Unset, list[int]]):
        mobile_platform_operation_uuid (Union[Unset, str]):
        mobile_platform_operation_uuid_in (Union[Unset, list[str]]):
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
        output_description (Union[Unset, int]):
        output_description_gt (Union[Unset, int]):
        output_description_gte (Union[Unset, int]):
        output_description_in (Union[Unset, list[int]]):
        output_description_isnull (Union[Unset, bool]):
        output_description_lt (Union[Unset, int]):
        output_description_lte (Union[Unset, int]):
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
        Response[PaginatedProcedureAcquisitionReadList]
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
        limit=limit,
        mobile_platform_operation_ob_id=mobile_platform_operation_ob_id,
        mobile_platform_operation_ob_id_in=mobile_platform_operation_ob_id_in,
        mobile_platform_operation_uuid=mobile_platform_operation_uuid,
        mobile_platform_operation_uuid_in=mobile_platform_operation_uuid_in,
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
        output_description=output_description,
        output_description_gt=output_description_gt,
        output_description_gte=output_description_gte,
        output_description_in=output_description_in,
        output_description_isnull=output_description_isnull,
        output_description_lt=output_description_lt,
        output_description_lte=output_description_lte,
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
    limit: Union[Unset, int] = UNSET,
    mobile_platform_operation_ob_id: Union[Unset, int] = UNSET,
    mobile_platform_operation_ob_id_in: Union[Unset, list[int]] = UNSET,
    mobile_platform_operation_uuid: Union[Unset, str] = UNSET,
    mobile_platform_operation_uuid_in: Union[Unset, list[str]] = UNSET,
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
    output_description: Union[Unset, int] = UNSET,
    output_description_gt: Union[Unset, int] = UNSET,
    output_description_gte: Union[Unset, int] = UNSET,
    output_description_in: Union[Unset, list[int]] = UNSET,
    output_description_isnull: Union[Unset, bool] = UNSET,
    output_description_lt: Union[Unset, int] = UNSET,
    output_description_lte: Union[Unset, int] = UNSET,
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
) -> Optional[PaginatedProcedureAcquisitionReadList]:
    """Get a list of ProcedureAcquisition objects. ProcedureAcquisitions have a 1:1 mapping with
    Observations.

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
        limit (Union[Unset, int]):
        mobile_platform_operation_ob_id (Union[Unset, int]):
        mobile_platform_operation_ob_id_in (Union[Unset, list[int]]):
        mobile_platform_operation_uuid (Union[Unset, str]):
        mobile_platform_operation_uuid_in (Union[Unset, list[str]]):
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
        output_description (Union[Unset, int]):
        output_description_gt (Union[Unset, int]):
        output_description_gte (Union[Unset, int]):
        output_description_in (Union[Unset, list[int]]):
        output_description_isnull (Union[Unset, bool]):
        output_description_lt (Union[Unset, int]):
        output_description_lte (Union[Unset, int]):
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
        PaginatedProcedureAcquisitionReadList
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
        limit=limit,
        mobile_platform_operation_ob_id=mobile_platform_operation_ob_id,
        mobile_platform_operation_ob_id_in=mobile_platform_operation_ob_id_in,
        mobile_platform_operation_uuid=mobile_platform_operation_uuid,
        mobile_platform_operation_uuid_in=mobile_platform_operation_uuid_in,
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
        output_description=output_description,
        output_description_gt=output_description_gt,
        output_description_gte=output_description_gte,
        output_description_in=output_description_in,
        output_description_isnull=output_description_isnull,
        output_description_lt=output_description_lt,
        output_description_lte=output_description_lte,
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
    limit: Union[Unset, int] = UNSET,
    mobile_platform_operation_ob_id: Union[Unset, int] = UNSET,
    mobile_platform_operation_ob_id_in: Union[Unset, list[int]] = UNSET,
    mobile_platform_operation_uuid: Union[Unset, str] = UNSET,
    mobile_platform_operation_uuid_in: Union[Unset, list[str]] = UNSET,
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
    output_description: Union[Unset, int] = UNSET,
    output_description_gt: Union[Unset, int] = UNSET,
    output_description_gte: Union[Unset, int] = UNSET,
    output_description_in: Union[Unset, list[int]] = UNSET,
    output_description_isnull: Union[Unset, bool] = UNSET,
    output_description_lt: Union[Unset, int] = UNSET,
    output_description_lte: Union[Unset, int] = UNSET,
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
) -> Response[PaginatedProcedureAcquisitionReadList]:
    """Get a list of ProcedureAcquisition objects. ProcedureAcquisitions have a 1:1 mapping with
    Observations.

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
        limit (Union[Unset, int]):
        mobile_platform_operation_ob_id (Union[Unset, int]):
        mobile_platform_operation_ob_id_in (Union[Unset, list[int]]):
        mobile_platform_operation_uuid (Union[Unset, str]):
        mobile_platform_operation_uuid_in (Union[Unset, list[str]]):
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
        output_description (Union[Unset, int]):
        output_description_gt (Union[Unset, int]):
        output_description_gte (Union[Unset, int]):
        output_description_in (Union[Unset, list[int]]):
        output_description_isnull (Union[Unset, bool]):
        output_description_lt (Union[Unset, int]):
        output_description_lte (Union[Unset, int]):
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
        Response[PaginatedProcedureAcquisitionReadList]
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
        limit=limit,
        mobile_platform_operation_ob_id=mobile_platform_operation_ob_id,
        mobile_platform_operation_ob_id_in=mobile_platform_operation_ob_id_in,
        mobile_platform_operation_uuid=mobile_platform_operation_uuid,
        mobile_platform_operation_uuid_in=mobile_platform_operation_uuid_in,
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
        output_description=output_description,
        output_description_gt=output_description_gt,
        output_description_gte=output_description_gte,
        output_description_in=output_description_in,
        output_description_isnull=output_description_isnull,
        output_description_lt=output_description_lt,
        output_description_lte=output_description_lte,
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
    limit: Union[Unset, int] = UNSET,
    mobile_platform_operation_ob_id: Union[Unset, int] = UNSET,
    mobile_platform_operation_ob_id_in: Union[Unset, list[int]] = UNSET,
    mobile_platform_operation_uuid: Union[Unset, str] = UNSET,
    mobile_platform_operation_uuid_in: Union[Unset, list[str]] = UNSET,
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
    output_description: Union[Unset, int] = UNSET,
    output_description_gt: Union[Unset, int] = UNSET,
    output_description_gte: Union[Unset, int] = UNSET,
    output_description_in: Union[Unset, list[int]] = UNSET,
    output_description_isnull: Union[Unset, bool] = UNSET,
    output_description_lt: Union[Unset, int] = UNSET,
    output_description_lte: Union[Unset, int] = UNSET,
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
) -> Optional[PaginatedProcedureAcquisitionReadList]:
    """Get a list of ProcedureAcquisition objects. ProcedureAcquisitions have a 1:1 mapping with
    Observations.

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
        limit (Union[Unset, int]):
        mobile_platform_operation_ob_id (Union[Unset, int]):
        mobile_platform_operation_ob_id_in (Union[Unset, list[int]]):
        mobile_platform_operation_uuid (Union[Unset, str]):
        mobile_platform_operation_uuid_in (Union[Unset, list[str]]):
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
        output_description (Union[Unset, int]):
        output_description_gt (Union[Unset, int]):
        output_description_gte (Union[Unset, int]):
        output_description_in (Union[Unset, list[int]]):
        output_description_isnull (Union[Unset, bool]):
        output_description_lt (Union[Unset, int]):
        output_description_lte (Union[Unset, int]):
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
        PaginatedProcedureAcquisitionReadList
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
            limit=limit,
            mobile_platform_operation_ob_id=mobile_platform_operation_ob_id,
            mobile_platform_operation_ob_id_in=mobile_platform_operation_ob_id_in,
            mobile_platform_operation_uuid=mobile_platform_operation_uuid,
            mobile_platform_operation_uuid_in=mobile_platform_operation_uuid_in,
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
            output_description=output_description,
            output_description_gt=output_description_gt,
            output_description_gte=output_description_gte,
            output_description_in=output_description_in,
            output_description_isnull=output_description_isnull,
            output_description_lt=output_description_lt,
            output_description_lte=output_description_lte,
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
