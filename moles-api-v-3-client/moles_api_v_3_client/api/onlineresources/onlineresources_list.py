from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.onlineresources_list_application_profile_file_format import (
    OnlineresourcesListApplicationProfileFileFormat,
)
from ...models.onlineresources_list_function import OnlineresourcesListFunction
from ...models.onlineresources_list_internal_resource_type import OnlineresourcesListInternalResourceType
from ...models.paginated_online_resource_read_list import PaginatedOnlineResourceReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    application_profile: OnlineresourcesListApplicationProfileFileFormat | Unset = UNSET,
    application_profile_contains: str | Unset = UNSET,
    application_profile_endswith: str | Unset = UNSET,
    application_profile_gt: str | Unset = UNSET,
    application_profile_gte: str | Unset = UNSET,
    application_profile_icontains: str | Unset = UNSET,
    application_profile_iendswith: str | Unset = UNSET,
    application_profile_iexact: str | Unset = UNSET,
    application_profile_in: list[str] | Unset = UNSET,
    application_profile_iregex: str | Unset = UNSET,
    application_profile_isnull: bool | Unset = UNSET,
    application_profile_istartswith: str | Unset = UNSET,
    application_profile_lt: str | Unset = UNSET,
    application_profile_lte: str | Unset = UNSET,
    application_profile_range: list[str] | Unset = UNSET,
    application_profile_regex: str | Unset = UNSET,
    application_profile_startswith: str | Unset = UNSET,
    description: str | Unset = UNSET,
    description_contains: str | Unset = UNSET,
    description_endswith: str | Unset = UNSET,
    description_gt: str | Unset = UNSET,
    description_gte: str | Unset = UNSET,
    description_icontains: str | Unset = UNSET,
    description_iendswith: str | Unset = UNSET,
    description_iexact: str | Unset = UNSET,
    description_in: list[str] | Unset = UNSET,
    description_iregex: str | Unset = UNSET,
    description_isnull: bool | Unset = UNSET,
    description_istartswith: str | Unset = UNSET,
    description_lt: str | Unset = UNSET,
    description_lte: str | Unset = UNSET,
    description_range: list[str] | Unset = UNSET,
    description_regex: str | Unset = UNSET,
    description_startswith: str | Unset = UNSET,
    function: OnlineresourcesListFunction | Unset = UNSET,
    function_contains: str | Unset = UNSET,
    function_endswith: str | Unset = UNSET,
    function_gt: str | Unset = UNSET,
    function_gte: str | Unset = UNSET,
    function_icontains: str | Unset = UNSET,
    function_iendswith: str | Unset = UNSET,
    function_iexact: str | Unset = UNSET,
    function_in: list[str] | Unset = UNSET,
    function_iregex: str | Unset = UNSET,
    function_isnull: bool | Unset = UNSET,
    function_istartswith: str | Unset = UNSET,
    function_lt: str | Unset = UNSET,
    function_lte: str | Unset = UNSET,
    function_range: list[str] | Unset = UNSET,
    function_regex: str | Unset = UNSET,
    function_startswith: str | Unset = UNSET,
    internal_resource_type: OnlineresourcesListInternalResourceType | Unset = UNSET,
    internal_resource_type_contains: str | Unset = UNSET,
    internal_resource_type_endswith: str | Unset = UNSET,
    internal_resource_type_gt: str | Unset = UNSET,
    internal_resource_type_gte: str | Unset = UNSET,
    internal_resource_type_icontains: str | Unset = UNSET,
    internal_resource_type_iendswith: str | Unset = UNSET,
    internal_resource_type_iexact: str | Unset = UNSET,
    internal_resource_type_in: list[str] | Unset = UNSET,
    internal_resource_type_iregex: str | Unset = UNSET,
    internal_resource_type_isnull: bool | Unset = UNSET,
    internal_resource_type_istartswith: str | Unset = UNSET,
    internal_resource_type_lt: str | Unset = UNSET,
    internal_resource_type_lte: str | Unset = UNSET,
    internal_resource_type_range: list[str] | Unset = UNSET,
    internal_resource_type_regex: str | Unset = UNSET,
    internal_resource_type_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    linkage: str | Unset = UNSET,
    linkage_contains: str | Unset = UNSET,
    linkage_endswith: str | Unset = UNSET,
    linkage_gt: str | Unset = UNSET,
    linkage_gte: str | Unset = UNSET,
    linkage_icontains: str | Unset = UNSET,
    linkage_iendswith: str | Unset = UNSET,
    linkage_iexact: str | Unset = UNSET,
    linkage_in: list[str] | Unset = UNSET,
    linkage_iregex: str | Unset = UNSET,
    linkage_isnull: bool | Unset = UNSET,
    linkage_istartswith: str | Unset = UNSET,
    linkage_lt: str | Unset = UNSET,
    linkage_lte: str | Unset = UNSET,
    linkage_range: list[str] | Unset = UNSET,
    linkage_regex: str | Unset = UNSET,
    linkage_startswith: str | Unset = UNSET,
    name: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    name_endswith: str | Unset = UNSET,
    name_gt: str | Unset = UNSET,
    name_gte: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_in: list[str] | Unset = UNSET,
    name_iregex: str | Unset = UNSET,
    name_isnull: bool | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    name_lt: str | Unset = UNSET,
    name_lte: str | Unset = UNSET,
    name_range: list[str] | Unset = UNSET,
    name_regex: str | Unset = UNSET,
    name_startswith: str | Unset = UNSET,
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
    related_to: int | Unset = UNSET,
    related_to_gt: int | Unset = UNSET,
    related_to_gte: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_lt: int | Unset = UNSET,
    related_to_lte: int | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_application_profile: str | Unset = UNSET
    if not isinstance(application_profile, Unset):
        json_application_profile = application_profile.value

    params["applicationProfile"] = json_application_profile

    params["applicationProfile__contains"] = application_profile_contains

    params["applicationProfile__endswith"] = application_profile_endswith

    params["applicationProfile__gt"] = application_profile_gt

    params["applicationProfile__gte"] = application_profile_gte

    params["applicationProfile__icontains"] = application_profile_icontains

    params["applicationProfile__iendswith"] = application_profile_iendswith

    params["applicationProfile__iexact"] = application_profile_iexact

    json_application_profile_in: list[str] | Unset = UNSET
    if not isinstance(application_profile_in, Unset):
        json_application_profile_in = ",".join(map(str, application_profile_in))

    params["applicationProfile__in"] = json_application_profile_in

    params["applicationProfile__iregex"] = application_profile_iregex

    params["applicationProfile__isnull"] = application_profile_isnull

    params["applicationProfile__istartswith"] = application_profile_istartswith

    params["applicationProfile__lt"] = application_profile_lt

    params["applicationProfile__lte"] = application_profile_lte

    json_application_profile_range: list[str] | Unset = UNSET
    if not isinstance(application_profile_range, Unset):
        json_application_profile_range = ",".join(map(str, application_profile_range))

    params["applicationProfile__range"] = json_application_profile_range

    params["applicationProfile__regex"] = application_profile_regex

    params["applicationProfile__startswith"] = application_profile_startswith

    params["description"] = description

    params["description__contains"] = description_contains

    params["description__endswith"] = description_endswith

    params["description__gt"] = description_gt

    params["description__gte"] = description_gte

    params["description__icontains"] = description_icontains

    params["description__iendswith"] = description_iendswith

    params["description__iexact"] = description_iexact

    json_description_in: list[str] | Unset = UNSET
    if not isinstance(description_in, Unset):
        json_description_in = ",".join(map(str, description_in))

    params["description__in"] = json_description_in

    params["description__iregex"] = description_iregex

    params["description__isnull"] = description_isnull

    params["description__istartswith"] = description_istartswith

    params["description__lt"] = description_lt

    params["description__lte"] = description_lte

    json_description_range: list[str] | Unset = UNSET
    if not isinstance(description_range, Unset):
        json_description_range = ",".join(map(str, description_range))

    params["description__range"] = json_description_range

    params["description__regex"] = description_regex

    params["description__startswith"] = description_startswith

    json_function: str | Unset = UNSET
    if not isinstance(function, Unset):
        json_function = function.value

    params["function"] = json_function

    params["function__contains"] = function_contains

    params["function__endswith"] = function_endswith

    params["function__gt"] = function_gt

    params["function__gte"] = function_gte

    params["function__icontains"] = function_icontains

    params["function__iendswith"] = function_iendswith

    params["function__iexact"] = function_iexact

    json_function_in: list[str] | Unset = UNSET
    if not isinstance(function_in, Unset):
        json_function_in = ",".join(map(str, function_in))

    params["function__in"] = json_function_in

    params["function__iregex"] = function_iregex

    params["function__isnull"] = function_isnull

    params["function__istartswith"] = function_istartswith

    params["function__lt"] = function_lt

    params["function__lte"] = function_lte

    json_function_range: list[str] | Unset = UNSET
    if not isinstance(function_range, Unset):
        json_function_range = ",".join(map(str, function_range))

    params["function__range"] = json_function_range

    params["function__regex"] = function_regex

    params["function__startswith"] = function_startswith

    json_internal_resource_type: str | Unset = UNSET
    if not isinstance(internal_resource_type, Unset):
        json_internal_resource_type = internal_resource_type.value

    params["internalResourceType"] = json_internal_resource_type

    params["internalResourceType__contains"] = internal_resource_type_contains

    params["internalResourceType__endswith"] = internal_resource_type_endswith

    params["internalResourceType__gt"] = internal_resource_type_gt

    params["internalResourceType__gte"] = internal_resource_type_gte

    params["internalResourceType__icontains"] = internal_resource_type_icontains

    params["internalResourceType__iendswith"] = internal_resource_type_iendswith

    params["internalResourceType__iexact"] = internal_resource_type_iexact

    json_internal_resource_type_in: list[str] | Unset = UNSET
    if not isinstance(internal_resource_type_in, Unset):
        json_internal_resource_type_in = ",".join(map(str, internal_resource_type_in))

    params["internalResourceType__in"] = json_internal_resource_type_in

    params["internalResourceType__iregex"] = internal_resource_type_iregex

    params["internalResourceType__isnull"] = internal_resource_type_isnull

    params["internalResourceType__istartswith"] = internal_resource_type_istartswith

    params["internalResourceType__lt"] = internal_resource_type_lt

    params["internalResourceType__lte"] = internal_resource_type_lte

    json_internal_resource_type_range: list[str] | Unset = UNSET
    if not isinstance(internal_resource_type_range, Unset):
        json_internal_resource_type_range = ",".join(map(str, internal_resource_type_range))

    params["internalResourceType__range"] = json_internal_resource_type_range

    params["internalResourceType__regex"] = internal_resource_type_regex

    params["internalResourceType__startswith"] = internal_resource_type_startswith

    params["limit"] = limit

    params["linkage"] = linkage

    params["linkage__contains"] = linkage_contains

    params["linkage__endswith"] = linkage_endswith

    params["linkage__gt"] = linkage_gt

    params["linkage__gte"] = linkage_gte

    params["linkage__icontains"] = linkage_icontains

    params["linkage__iendswith"] = linkage_iendswith

    params["linkage__iexact"] = linkage_iexact

    json_linkage_in: list[str] | Unset = UNSET
    if not isinstance(linkage_in, Unset):
        json_linkage_in = ",".join(map(str, linkage_in))

    params["linkage__in"] = json_linkage_in

    params["linkage__iregex"] = linkage_iregex

    params["linkage__isnull"] = linkage_isnull

    params["linkage__istartswith"] = linkage_istartswith

    params["linkage__lt"] = linkage_lt

    params["linkage__lte"] = linkage_lte

    json_linkage_range: list[str] | Unset = UNSET
    if not isinstance(linkage_range, Unset):
        json_linkage_range = ",".join(map(str, linkage_range))

    params["linkage__range"] = json_linkage_range

    params["linkage__regex"] = linkage_regex

    params["linkage__startswith"] = linkage_startswith

    params["name"] = name

    params["name__contains"] = name_contains

    params["name__endswith"] = name_endswith

    params["name__gt"] = name_gt

    params["name__gte"] = name_gte

    params["name__icontains"] = name_icontains

    params["name__iendswith"] = name_iendswith

    params["name__iexact"] = name_iexact

    json_name_in: list[str] | Unset = UNSET
    if not isinstance(name_in, Unset):
        json_name_in = ",".join(map(str, name_in))

    params["name__in"] = json_name_in

    params["name__iregex"] = name_iregex

    params["name__isnull"] = name_isnull

    params["name__istartswith"] = name_istartswith

    params["name__lt"] = name_lt

    params["name__lte"] = name_lte

    json_name_range: list[str] | Unset = UNSET
    if not isinstance(name_range, Unset):
        json_name_range = ",".join(map(str, name_range))

    params["name__range"] = json_name_range

    params["name__regex"] = name_regex

    params["name__startswith"] = name_startswith

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

    params["relatedTo"] = related_to

    params["relatedTo__gt"] = related_to_gt

    params["relatedTo__gte"] = related_to_gte

    json_related_to_in: list[int] | Unset = UNSET
    if not isinstance(related_to_in, Unset):
        json_related_to_in = ",".join(map(str, related_to_in))

    params["relatedTo__in"] = json_related_to_in

    params["relatedTo__isnull"] = related_to_isnull

    params["relatedTo__lt"] = related_to_lt

    params["relatedTo__lte"] = related_to_lte

    params["relatedTo__ob_id"] = related_to_ob_id

    json_related_to_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(related_to_ob_id_in, Unset):
        json_related_to_ob_id_in = ",".join(map(str, related_to_ob_id_in))

    params["relatedTo__ob_id__in"] = json_related_to_ob_id_in

    params["relatedTo__short_code"] = related_to_short_code

    json_related_to_short_code_in: list[str] | Unset = UNSET
    if not isinstance(related_to_short_code_in, Unset):
        json_related_to_short_code_in = ",".join(map(str, related_to_short_code_in))

    params["relatedTo__short_code__in"] = json_related_to_short_code_in

    params["relatedTo__uuid"] = related_to_uuid

    json_related_to_uuid_in: list[str] | Unset = UNSET
    if not isinstance(related_to_uuid_in, Unset):
        json_related_to_uuid_in = ",".join(map(str, related_to_uuid_in))

    params["relatedTo__uuid__in"] = json_related_to_uuid_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/onlineresources/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedOnlineResourceReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedOnlineResourceReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedOnlineResourceReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    application_profile: OnlineresourcesListApplicationProfileFileFormat | Unset = UNSET,
    application_profile_contains: str | Unset = UNSET,
    application_profile_endswith: str | Unset = UNSET,
    application_profile_gt: str | Unset = UNSET,
    application_profile_gte: str | Unset = UNSET,
    application_profile_icontains: str | Unset = UNSET,
    application_profile_iendswith: str | Unset = UNSET,
    application_profile_iexact: str | Unset = UNSET,
    application_profile_in: list[str] | Unset = UNSET,
    application_profile_iregex: str | Unset = UNSET,
    application_profile_isnull: bool | Unset = UNSET,
    application_profile_istartswith: str | Unset = UNSET,
    application_profile_lt: str | Unset = UNSET,
    application_profile_lte: str | Unset = UNSET,
    application_profile_range: list[str] | Unset = UNSET,
    application_profile_regex: str | Unset = UNSET,
    application_profile_startswith: str | Unset = UNSET,
    description: str | Unset = UNSET,
    description_contains: str | Unset = UNSET,
    description_endswith: str | Unset = UNSET,
    description_gt: str | Unset = UNSET,
    description_gte: str | Unset = UNSET,
    description_icontains: str | Unset = UNSET,
    description_iendswith: str | Unset = UNSET,
    description_iexact: str | Unset = UNSET,
    description_in: list[str] | Unset = UNSET,
    description_iregex: str | Unset = UNSET,
    description_isnull: bool | Unset = UNSET,
    description_istartswith: str | Unset = UNSET,
    description_lt: str | Unset = UNSET,
    description_lte: str | Unset = UNSET,
    description_range: list[str] | Unset = UNSET,
    description_regex: str | Unset = UNSET,
    description_startswith: str | Unset = UNSET,
    function: OnlineresourcesListFunction | Unset = UNSET,
    function_contains: str | Unset = UNSET,
    function_endswith: str | Unset = UNSET,
    function_gt: str | Unset = UNSET,
    function_gte: str | Unset = UNSET,
    function_icontains: str | Unset = UNSET,
    function_iendswith: str | Unset = UNSET,
    function_iexact: str | Unset = UNSET,
    function_in: list[str] | Unset = UNSET,
    function_iregex: str | Unset = UNSET,
    function_isnull: bool | Unset = UNSET,
    function_istartswith: str | Unset = UNSET,
    function_lt: str | Unset = UNSET,
    function_lte: str | Unset = UNSET,
    function_range: list[str] | Unset = UNSET,
    function_regex: str | Unset = UNSET,
    function_startswith: str | Unset = UNSET,
    internal_resource_type: OnlineresourcesListInternalResourceType | Unset = UNSET,
    internal_resource_type_contains: str | Unset = UNSET,
    internal_resource_type_endswith: str | Unset = UNSET,
    internal_resource_type_gt: str | Unset = UNSET,
    internal_resource_type_gte: str | Unset = UNSET,
    internal_resource_type_icontains: str | Unset = UNSET,
    internal_resource_type_iendswith: str | Unset = UNSET,
    internal_resource_type_iexact: str | Unset = UNSET,
    internal_resource_type_in: list[str] | Unset = UNSET,
    internal_resource_type_iregex: str | Unset = UNSET,
    internal_resource_type_isnull: bool | Unset = UNSET,
    internal_resource_type_istartswith: str | Unset = UNSET,
    internal_resource_type_lt: str | Unset = UNSET,
    internal_resource_type_lte: str | Unset = UNSET,
    internal_resource_type_range: list[str] | Unset = UNSET,
    internal_resource_type_regex: str | Unset = UNSET,
    internal_resource_type_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    linkage: str | Unset = UNSET,
    linkage_contains: str | Unset = UNSET,
    linkage_endswith: str | Unset = UNSET,
    linkage_gt: str | Unset = UNSET,
    linkage_gte: str | Unset = UNSET,
    linkage_icontains: str | Unset = UNSET,
    linkage_iendswith: str | Unset = UNSET,
    linkage_iexact: str | Unset = UNSET,
    linkage_in: list[str] | Unset = UNSET,
    linkage_iregex: str | Unset = UNSET,
    linkage_isnull: bool | Unset = UNSET,
    linkage_istartswith: str | Unset = UNSET,
    linkage_lt: str | Unset = UNSET,
    linkage_lte: str | Unset = UNSET,
    linkage_range: list[str] | Unset = UNSET,
    linkage_regex: str | Unset = UNSET,
    linkage_startswith: str | Unset = UNSET,
    name: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    name_endswith: str | Unset = UNSET,
    name_gt: str | Unset = UNSET,
    name_gte: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_in: list[str] | Unset = UNSET,
    name_iregex: str | Unset = UNSET,
    name_isnull: bool | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    name_lt: str | Unset = UNSET,
    name_lte: str | Unset = UNSET,
    name_range: list[str] | Unset = UNSET,
    name_regex: str | Unset = UNSET,
    name_startswith: str | Unset = UNSET,
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
    related_to: int | Unset = UNSET,
    related_to_gt: int | Unset = UNSET,
    related_to_gte: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_lt: int | Unset = UNSET,
    related_to_lte: int | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
) -> Response[PaginatedOnlineResourceReadList]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        application_profile (OnlineresourcesListApplicationProfileFileFormat | Unset):
        application_profile_contains (str | Unset):
        application_profile_endswith (str | Unset):
        application_profile_gt (str | Unset):
        application_profile_gte (str | Unset):
        application_profile_icontains (str | Unset):
        application_profile_iendswith (str | Unset):
        application_profile_iexact (str | Unset):
        application_profile_in (list[str] | Unset):
        application_profile_iregex (str | Unset):
        application_profile_isnull (bool | Unset):
        application_profile_istartswith (str | Unset):
        application_profile_lt (str | Unset):
        application_profile_lte (str | Unset):
        application_profile_range (list[str] | Unset):
        application_profile_regex (str | Unset):
        application_profile_startswith (str | Unset):
        description (str | Unset):
        description_contains (str | Unset):
        description_endswith (str | Unset):
        description_gt (str | Unset):
        description_gte (str | Unset):
        description_icontains (str | Unset):
        description_iendswith (str | Unset):
        description_iexact (str | Unset):
        description_in (list[str] | Unset):
        description_iregex (str | Unset):
        description_isnull (bool | Unset):
        description_istartswith (str | Unset):
        description_lt (str | Unset):
        description_lte (str | Unset):
        description_range (list[str] | Unset):
        description_regex (str | Unset):
        description_startswith (str | Unset):
        function (OnlineresourcesListFunction | Unset):
        function_contains (str | Unset):
        function_endswith (str | Unset):
        function_gt (str | Unset):
        function_gte (str | Unset):
        function_icontains (str | Unset):
        function_iendswith (str | Unset):
        function_iexact (str | Unset):
        function_in (list[str] | Unset):
        function_iregex (str | Unset):
        function_isnull (bool | Unset):
        function_istartswith (str | Unset):
        function_lt (str | Unset):
        function_lte (str | Unset):
        function_range (list[str] | Unset):
        function_regex (str | Unset):
        function_startswith (str | Unset):
        internal_resource_type (OnlineresourcesListInternalResourceType | Unset):
        internal_resource_type_contains (str | Unset):
        internal_resource_type_endswith (str | Unset):
        internal_resource_type_gt (str | Unset):
        internal_resource_type_gte (str | Unset):
        internal_resource_type_icontains (str | Unset):
        internal_resource_type_iendswith (str | Unset):
        internal_resource_type_iexact (str | Unset):
        internal_resource_type_in (list[str] | Unset):
        internal_resource_type_iregex (str | Unset):
        internal_resource_type_isnull (bool | Unset):
        internal_resource_type_istartswith (str | Unset):
        internal_resource_type_lt (str | Unset):
        internal_resource_type_lte (str | Unset):
        internal_resource_type_range (list[str] | Unset):
        internal_resource_type_regex (str | Unset):
        internal_resource_type_startswith (str | Unset):
        limit (int | Unset):
        linkage (str | Unset):
        linkage_contains (str | Unset):
        linkage_endswith (str | Unset):
        linkage_gt (str | Unset):
        linkage_gte (str | Unset):
        linkage_icontains (str | Unset):
        linkage_iendswith (str | Unset):
        linkage_iexact (str | Unset):
        linkage_in (list[str] | Unset):
        linkage_iregex (str | Unset):
        linkage_isnull (bool | Unset):
        linkage_istartswith (str | Unset):
        linkage_lt (str | Unset):
        linkage_lte (str | Unset):
        linkage_range (list[str] | Unset):
        linkage_regex (str | Unset):
        linkage_startswith (str | Unset):
        name (str | Unset):
        name_contains (str | Unset):
        name_endswith (str | Unset):
        name_gt (str | Unset):
        name_gte (str | Unset):
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_in (list[str] | Unset):
        name_iregex (str | Unset):
        name_isnull (bool | Unset):
        name_istartswith (str | Unset):
        name_lt (str | Unset):
        name_lte (str | Unset):
        name_range (list[str] | Unset):
        name_regex (str | Unset):
        name_startswith (str | Unset):
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
        related_to (int | Unset):
        related_to_gt (int | Unset):
        related_to_gte (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_lt (int | Unset):
        related_to_lte (int | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOnlineResourceReadList]
    """

    kwargs = _get_kwargs(
        application_profile=application_profile,
        application_profile_contains=application_profile_contains,
        application_profile_endswith=application_profile_endswith,
        application_profile_gt=application_profile_gt,
        application_profile_gte=application_profile_gte,
        application_profile_icontains=application_profile_icontains,
        application_profile_iendswith=application_profile_iendswith,
        application_profile_iexact=application_profile_iexact,
        application_profile_in=application_profile_in,
        application_profile_iregex=application_profile_iregex,
        application_profile_isnull=application_profile_isnull,
        application_profile_istartswith=application_profile_istartswith,
        application_profile_lt=application_profile_lt,
        application_profile_lte=application_profile_lte,
        application_profile_range=application_profile_range,
        application_profile_regex=application_profile_regex,
        application_profile_startswith=application_profile_startswith,
        description=description,
        description_contains=description_contains,
        description_endswith=description_endswith,
        description_gt=description_gt,
        description_gte=description_gte,
        description_icontains=description_icontains,
        description_iendswith=description_iendswith,
        description_iexact=description_iexact,
        description_in=description_in,
        description_iregex=description_iregex,
        description_isnull=description_isnull,
        description_istartswith=description_istartswith,
        description_lt=description_lt,
        description_lte=description_lte,
        description_range=description_range,
        description_regex=description_regex,
        description_startswith=description_startswith,
        function=function,
        function_contains=function_contains,
        function_endswith=function_endswith,
        function_gt=function_gt,
        function_gte=function_gte,
        function_icontains=function_icontains,
        function_iendswith=function_iendswith,
        function_iexact=function_iexact,
        function_in=function_in,
        function_iregex=function_iregex,
        function_isnull=function_isnull,
        function_istartswith=function_istartswith,
        function_lt=function_lt,
        function_lte=function_lte,
        function_range=function_range,
        function_regex=function_regex,
        function_startswith=function_startswith,
        internal_resource_type=internal_resource_type,
        internal_resource_type_contains=internal_resource_type_contains,
        internal_resource_type_endswith=internal_resource_type_endswith,
        internal_resource_type_gt=internal_resource_type_gt,
        internal_resource_type_gte=internal_resource_type_gte,
        internal_resource_type_icontains=internal_resource_type_icontains,
        internal_resource_type_iendswith=internal_resource_type_iendswith,
        internal_resource_type_iexact=internal_resource_type_iexact,
        internal_resource_type_in=internal_resource_type_in,
        internal_resource_type_iregex=internal_resource_type_iregex,
        internal_resource_type_isnull=internal_resource_type_isnull,
        internal_resource_type_istartswith=internal_resource_type_istartswith,
        internal_resource_type_lt=internal_resource_type_lt,
        internal_resource_type_lte=internal_resource_type_lte,
        internal_resource_type_range=internal_resource_type_range,
        internal_resource_type_regex=internal_resource_type_regex,
        internal_resource_type_startswith=internal_resource_type_startswith,
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
        name=name,
        name_contains=name_contains,
        name_endswith=name_endswith,
        name_gt=name_gt,
        name_gte=name_gte,
        name_icontains=name_icontains,
        name_iendswith=name_iendswith,
        name_iexact=name_iexact,
        name_in=name_in,
        name_iregex=name_iregex,
        name_isnull=name_isnull,
        name_istartswith=name_istartswith,
        name_lt=name_lt,
        name_lte=name_lte,
        name_range=name_range,
        name_regex=name_regex,
        name_startswith=name_startswith,
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
        related_to=related_to,
        related_to_gt=related_to_gt,
        related_to_gte=related_to_gte,
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
        related_to_lt=related_to_lt,
        related_to_lte=related_to_lte,
        related_to_ob_id=related_to_ob_id,
        related_to_ob_id_in=related_to_ob_id_in,
        related_to_short_code=related_to_short_code,
        related_to_short_code_in=related_to_short_code_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    application_profile: OnlineresourcesListApplicationProfileFileFormat | Unset = UNSET,
    application_profile_contains: str | Unset = UNSET,
    application_profile_endswith: str | Unset = UNSET,
    application_profile_gt: str | Unset = UNSET,
    application_profile_gte: str | Unset = UNSET,
    application_profile_icontains: str | Unset = UNSET,
    application_profile_iendswith: str | Unset = UNSET,
    application_profile_iexact: str | Unset = UNSET,
    application_profile_in: list[str] | Unset = UNSET,
    application_profile_iregex: str | Unset = UNSET,
    application_profile_isnull: bool | Unset = UNSET,
    application_profile_istartswith: str | Unset = UNSET,
    application_profile_lt: str | Unset = UNSET,
    application_profile_lte: str | Unset = UNSET,
    application_profile_range: list[str] | Unset = UNSET,
    application_profile_regex: str | Unset = UNSET,
    application_profile_startswith: str | Unset = UNSET,
    description: str | Unset = UNSET,
    description_contains: str | Unset = UNSET,
    description_endswith: str | Unset = UNSET,
    description_gt: str | Unset = UNSET,
    description_gte: str | Unset = UNSET,
    description_icontains: str | Unset = UNSET,
    description_iendswith: str | Unset = UNSET,
    description_iexact: str | Unset = UNSET,
    description_in: list[str] | Unset = UNSET,
    description_iregex: str | Unset = UNSET,
    description_isnull: bool | Unset = UNSET,
    description_istartswith: str | Unset = UNSET,
    description_lt: str | Unset = UNSET,
    description_lte: str | Unset = UNSET,
    description_range: list[str] | Unset = UNSET,
    description_regex: str | Unset = UNSET,
    description_startswith: str | Unset = UNSET,
    function: OnlineresourcesListFunction | Unset = UNSET,
    function_contains: str | Unset = UNSET,
    function_endswith: str | Unset = UNSET,
    function_gt: str | Unset = UNSET,
    function_gte: str | Unset = UNSET,
    function_icontains: str | Unset = UNSET,
    function_iendswith: str | Unset = UNSET,
    function_iexact: str | Unset = UNSET,
    function_in: list[str] | Unset = UNSET,
    function_iregex: str | Unset = UNSET,
    function_isnull: bool | Unset = UNSET,
    function_istartswith: str | Unset = UNSET,
    function_lt: str | Unset = UNSET,
    function_lte: str | Unset = UNSET,
    function_range: list[str] | Unset = UNSET,
    function_regex: str | Unset = UNSET,
    function_startswith: str | Unset = UNSET,
    internal_resource_type: OnlineresourcesListInternalResourceType | Unset = UNSET,
    internal_resource_type_contains: str | Unset = UNSET,
    internal_resource_type_endswith: str | Unset = UNSET,
    internal_resource_type_gt: str | Unset = UNSET,
    internal_resource_type_gte: str | Unset = UNSET,
    internal_resource_type_icontains: str | Unset = UNSET,
    internal_resource_type_iendswith: str | Unset = UNSET,
    internal_resource_type_iexact: str | Unset = UNSET,
    internal_resource_type_in: list[str] | Unset = UNSET,
    internal_resource_type_iregex: str | Unset = UNSET,
    internal_resource_type_isnull: bool | Unset = UNSET,
    internal_resource_type_istartswith: str | Unset = UNSET,
    internal_resource_type_lt: str | Unset = UNSET,
    internal_resource_type_lte: str | Unset = UNSET,
    internal_resource_type_range: list[str] | Unset = UNSET,
    internal_resource_type_regex: str | Unset = UNSET,
    internal_resource_type_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    linkage: str | Unset = UNSET,
    linkage_contains: str | Unset = UNSET,
    linkage_endswith: str | Unset = UNSET,
    linkage_gt: str | Unset = UNSET,
    linkage_gte: str | Unset = UNSET,
    linkage_icontains: str | Unset = UNSET,
    linkage_iendswith: str | Unset = UNSET,
    linkage_iexact: str | Unset = UNSET,
    linkage_in: list[str] | Unset = UNSET,
    linkage_iregex: str | Unset = UNSET,
    linkage_isnull: bool | Unset = UNSET,
    linkage_istartswith: str | Unset = UNSET,
    linkage_lt: str | Unset = UNSET,
    linkage_lte: str | Unset = UNSET,
    linkage_range: list[str] | Unset = UNSET,
    linkage_regex: str | Unset = UNSET,
    linkage_startswith: str | Unset = UNSET,
    name: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    name_endswith: str | Unset = UNSET,
    name_gt: str | Unset = UNSET,
    name_gte: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_in: list[str] | Unset = UNSET,
    name_iregex: str | Unset = UNSET,
    name_isnull: bool | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    name_lt: str | Unset = UNSET,
    name_lte: str | Unset = UNSET,
    name_range: list[str] | Unset = UNSET,
    name_regex: str | Unset = UNSET,
    name_startswith: str | Unset = UNSET,
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
    related_to: int | Unset = UNSET,
    related_to_gt: int | Unset = UNSET,
    related_to_gte: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_lt: int | Unset = UNSET,
    related_to_lte: int | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
) -> PaginatedOnlineResourceReadList | None:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        application_profile (OnlineresourcesListApplicationProfileFileFormat | Unset):
        application_profile_contains (str | Unset):
        application_profile_endswith (str | Unset):
        application_profile_gt (str | Unset):
        application_profile_gte (str | Unset):
        application_profile_icontains (str | Unset):
        application_profile_iendswith (str | Unset):
        application_profile_iexact (str | Unset):
        application_profile_in (list[str] | Unset):
        application_profile_iregex (str | Unset):
        application_profile_isnull (bool | Unset):
        application_profile_istartswith (str | Unset):
        application_profile_lt (str | Unset):
        application_profile_lte (str | Unset):
        application_profile_range (list[str] | Unset):
        application_profile_regex (str | Unset):
        application_profile_startswith (str | Unset):
        description (str | Unset):
        description_contains (str | Unset):
        description_endswith (str | Unset):
        description_gt (str | Unset):
        description_gte (str | Unset):
        description_icontains (str | Unset):
        description_iendswith (str | Unset):
        description_iexact (str | Unset):
        description_in (list[str] | Unset):
        description_iregex (str | Unset):
        description_isnull (bool | Unset):
        description_istartswith (str | Unset):
        description_lt (str | Unset):
        description_lte (str | Unset):
        description_range (list[str] | Unset):
        description_regex (str | Unset):
        description_startswith (str | Unset):
        function (OnlineresourcesListFunction | Unset):
        function_contains (str | Unset):
        function_endswith (str | Unset):
        function_gt (str | Unset):
        function_gte (str | Unset):
        function_icontains (str | Unset):
        function_iendswith (str | Unset):
        function_iexact (str | Unset):
        function_in (list[str] | Unset):
        function_iregex (str | Unset):
        function_isnull (bool | Unset):
        function_istartswith (str | Unset):
        function_lt (str | Unset):
        function_lte (str | Unset):
        function_range (list[str] | Unset):
        function_regex (str | Unset):
        function_startswith (str | Unset):
        internal_resource_type (OnlineresourcesListInternalResourceType | Unset):
        internal_resource_type_contains (str | Unset):
        internal_resource_type_endswith (str | Unset):
        internal_resource_type_gt (str | Unset):
        internal_resource_type_gte (str | Unset):
        internal_resource_type_icontains (str | Unset):
        internal_resource_type_iendswith (str | Unset):
        internal_resource_type_iexact (str | Unset):
        internal_resource_type_in (list[str] | Unset):
        internal_resource_type_iregex (str | Unset):
        internal_resource_type_isnull (bool | Unset):
        internal_resource_type_istartswith (str | Unset):
        internal_resource_type_lt (str | Unset):
        internal_resource_type_lte (str | Unset):
        internal_resource_type_range (list[str] | Unset):
        internal_resource_type_regex (str | Unset):
        internal_resource_type_startswith (str | Unset):
        limit (int | Unset):
        linkage (str | Unset):
        linkage_contains (str | Unset):
        linkage_endswith (str | Unset):
        linkage_gt (str | Unset):
        linkage_gte (str | Unset):
        linkage_icontains (str | Unset):
        linkage_iendswith (str | Unset):
        linkage_iexact (str | Unset):
        linkage_in (list[str] | Unset):
        linkage_iregex (str | Unset):
        linkage_isnull (bool | Unset):
        linkage_istartswith (str | Unset):
        linkage_lt (str | Unset):
        linkage_lte (str | Unset):
        linkage_range (list[str] | Unset):
        linkage_regex (str | Unset):
        linkage_startswith (str | Unset):
        name (str | Unset):
        name_contains (str | Unset):
        name_endswith (str | Unset):
        name_gt (str | Unset):
        name_gte (str | Unset):
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_in (list[str] | Unset):
        name_iregex (str | Unset):
        name_isnull (bool | Unset):
        name_istartswith (str | Unset):
        name_lt (str | Unset):
        name_lte (str | Unset):
        name_range (list[str] | Unset):
        name_regex (str | Unset):
        name_startswith (str | Unset):
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
        related_to (int | Unset):
        related_to_gt (int | Unset):
        related_to_gte (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_lt (int | Unset):
        related_to_lte (int | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOnlineResourceReadList
    """

    return sync_detailed(
        client=client,
        application_profile=application_profile,
        application_profile_contains=application_profile_contains,
        application_profile_endswith=application_profile_endswith,
        application_profile_gt=application_profile_gt,
        application_profile_gte=application_profile_gte,
        application_profile_icontains=application_profile_icontains,
        application_profile_iendswith=application_profile_iendswith,
        application_profile_iexact=application_profile_iexact,
        application_profile_in=application_profile_in,
        application_profile_iregex=application_profile_iregex,
        application_profile_isnull=application_profile_isnull,
        application_profile_istartswith=application_profile_istartswith,
        application_profile_lt=application_profile_lt,
        application_profile_lte=application_profile_lte,
        application_profile_range=application_profile_range,
        application_profile_regex=application_profile_regex,
        application_profile_startswith=application_profile_startswith,
        description=description,
        description_contains=description_contains,
        description_endswith=description_endswith,
        description_gt=description_gt,
        description_gte=description_gte,
        description_icontains=description_icontains,
        description_iendswith=description_iendswith,
        description_iexact=description_iexact,
        description_in=description_in,
        description_iregex=description_iregex,
        description_isnull=description_isnull,
        description_istartswith=description_istartswith,
        description_lt=description_lt,
        description_lte=description_lte,
        description_range=description_range,
        description_regex=description_regex,
        description_startswith=description_startswith,
        function=function,
        function_contains=function_contains,
        function_endswith=function_endswith,
        function_gt=function_gt,
        function_gte=function_gte,
        function_icontains=function_icontains,
        function_iendswith=function_iendswith,
        function_iexact=function_iexact,
        function_in=function_in,
        function_iregex=function_iregex,
        function_isnull=function_isnull,
        function_istartswith=function_istartswith,
        function_lt=function_lt,
        function_lte=function_lte,
        function_range=function_range,
        function_regex=function_regex,
        function_startswith=function_startswith,
        internal_resource_type=internal_resource_type,
        internal_resource_type_contains=internal_resource_type_contains,
        internal_resource_type_endswith=internal_resource_type_endswith,
        internal_resource_type_gt=internal_resource_type_gt,
        internal_resource_type_gte=internal_resource_type_gte,
        internal_resource_type_icontains=internal_resource_type_icontains,
        internal_resource_type_iendswith=internal_resource_type_iendswith,
        internal_resource_type_iexact=internal_resource_type_iexact,
        internal_resource_type_in=internal_resource_type_in,
        internal_resource_type_iregex=internal_resource_type_iregex,
        internal_resource_type_isnull=internal_resource_type_isnull,
        internal_resource_type_istartswith=internal_resource_type_istartswith,
        internal_resource_type_lt=internal_resource_type_lt,
        internal_resource_type_lte=internal_resource_type_lte,
        internal_resource_type_range=internal_resource_type_range,
        internal_resource_type_regex=internal_resource_type_regex,
        internal_resource_type_startswith=internal_resource_type_startswith,
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
        name=name,
        name_contains=name_contains,
        name_endswith=name_endswith,
        name_gt=name_gt,
        name_gte=name_gte,
        name_icontains=name_icontains,
        name_iendswith=name_iendswith,
        name_iexact=name_iexact,
        name_in=name_in,
        name_iregex=name_iregex,
        name_isnull=name_isnull,
        name_istartswith=name_istartswith,
        name_lt=name_lt,
        name_lte=name_lte,
        name_range=name_range,
        name_regex=name_regex,
        name_startswith=name_startswith,
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
        related_to=related_to,
        related_to_gt=related_to_gt,
        related_to_gte=related_to_gte,
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
        related_to_lt=related_to_lt,
        related_to_lte=related_to_lte,
        related_to_ob_id=related_to_ob_id,
        related_to_ob_id_in=related_to_ob_id_in,
        related_to_short_code=related_to_short_code,
        related_to_short_code_in=related_to_short_code_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    application_profile: OnlineresourcesListApplicationProfileFileFormat | Unset = UNSET,
    application_profile_contains: str | Unset = UNSET,
    application_profile_endswith: str | Unset = UNSET,
    application_profile_gt: str | Unset = UNSET,
    application_profile_gte: str | Unset = UNSET,
    application_profile_icontains: str | Unset = UNSET,
    application_profile_iendswith: str | Unset = UNSET,
    application_profile_iexact: str | Unset = UNSET,
    application_profile_in: list[str] | Unset = UNSET,
    application_profile_iregex: str | Unset = UNSET,
    application_profile_isnull: bool | Unset = UNSET,
    application_profile_istartswith: str | Unset = UNSET,
    application_profile_lt: str | Unset = UNSET,
    application_profile_lte: str | Unset = UNSET,
    application_profile_range: list[str] | Unset = UNSET,
    application_profile_regex: str | Unset = UNSET,
    application_profile_startswith: str | Unset = UNSET,
    description: str | Unset = UNSET,
    description_contains: str | Unset = UNSET,
    description_endswith: str | Unset = UNSET,
    description_gt: str | Unset = UNSET,
    description_gte: str | Unset = UNSET,
    description_icontains: str | Unset = UNSET,
    description_iendswith: str | Unset = UNSET,
    description_iexact: str | Unset = UNSET,
    description_in: list[str] | Unset = UNSET,
    description_iregex: str | Unset = UNSET,
    description_isnull: bool | Unset = UNSET,
    description_istartswith: str | Unset = UNSET,
    description_lt: str | Unset = UNSET,
    description_lte: str | Unset = UNSET,
    description_range: list[str] | Unset = UNSET,
    description_regex: str | Unset = UNSET,
    description_startswith: str | Unset = UNSET,
    function: OnlineresourcesListFunction | Unset = UNSET,
    function_contains: str | Unset = UNSET,
    function_endswith: str | Unset = UNSET,
    function_gt: str | Unset = UNSET,
    function_gte: str | Unset = UNSET,
    function_icontains: str | Unset = UNSET,
    function_iendswith: str | Unset = UNSET,
    function_iexact: str | Unset = UNSET,
    function_in: list[str] | Unset = UNSET,
    function_iregex: str | Unset = UNSET,
    function_isnull: bool | Unset = UNSET,
    function_istartswith: str | Unset = UNSET,
    function_lt: str | Unset = UNSET,
    function_lte: str | Unset = UNSET,
    function_range: list[str] | Unset = UNSET,
    function_regex: str | Unset = UNSET,
    function_startswith: str | Unset = UNSET,
    internal_resource_type: OnlineresourcesListInternalResourceType | Unset = UNSET,
    internal_resource_type_contains: str | Unset = UNSET,
    internal_resource_type_endswith: str | Unset = UNSET,
    internal_resource_type_gt: str | Unset = UNSET,
    internal_resource_type_gte: str | Unset = UNSET,
    internal_resource_type_icontains: str | Unset = UNSET,
    internal_resource_type_iendswith: str | Unset = UNSET,
    internal_resource_type_iexact: str | Unset = UNSET,
    internal_resource_type_in: list[str] | Unset = UNSET,
    internal_resource_type_iregex: str | Unset = UNSET,
    internal_resource_type_isnull: bool | Unset = UNSET,
    internal_resource_type_istartswith: str | Unset = UNSET,
    internal_resource_type_lt: str | Unset = UNSET,
    internal_resource_type_lte: str | Unset = UNSET,
    internal_resource_type_range: list[str] | Unset = UNSET,
    internal_resource_type_regex: str | Unset = UNSET,
    internal_resource_type_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    linkage: str | Unset = UNSET,
    linkage_contains: str | Unset = UNSET,
    linkage_endswith: str | Unset = UNSET,
    linkage_gt: str | Unset = UNSET,
    linkage_gte: str | Unset = UNSET,
    linkage_icontains: str | Unset = UNSET,
    linkage_iendswith: str | Unset = UNSET,
    linkage_iexact: str | Unset = UNSET,
    linkage_in: list[str] | Unset = UNSET,
    linkage_iregex: str | Unset = UNSET,
    linkage_isnull: bool | Unset = UNSET,
    linkage_istartswith: str | Unset = UNSET,
    linkage_lt: str | Unset = UNSET,
    linkage_lte: str | Unset = UNSET,
    linkage_range: list[str] | Unset = UNSET,
    linkage_regex: str | Unset = UNSET,
    linkage_startswith: str | Unset = UNSET,
    name: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    name_endswith: str | Unset = UNSET,
    name_gt: str | Unset = UNSET,
    name_gte: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_in: list[str] | Unset = UNSET,
    name_iregex: str | Unset = UNSET,
    name_isnull: bool | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    name_lt: str | Unset = UNSET,
    name_lte: str | Unset = UNSET,
    name_range: list[str] | Unset = UNSET,
    name_regex: str | Unset = UNSET,
    name_startswith: str | Unset = UNSET,
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
    related_to: int | Unset = UNSET,
    related_to_gt: int | Unset = UNSET,
    related_to_gte: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_lt: int | Unset = UNSET,
    related_to_lte: int | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
) -> Response[PaginatedOnlineResourceReadList]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        application_profile (OnlineresourcesListApplicationProfileFileFormat | Unset):
        application_profile_contains (str | Unset):
        application_profile_endswith (str | Unset):
        application_profile_gt (str | Unset):
        application_profile_gte (str | Unset):
        application_profile_icontains (str | Unset):
        application_profile_iendswith (str | Unset):
        application_profile_iexact (str | Unset):
        application_profile_in (list[str] | Unset):
        application_profile_iregex (str | Unset):
        application_profile_isnull (bool | Unset):
        application_profile_istartswith (str | Unset):
        application_profile_lt (str | Unset):
        application_profile_lte (str | Unset):
        application_profile_range (list[str] | Unset):
        application_profile_regex (str | Unset):
        application_profile_startswith (str | Unset):
        description (str | Unset):
        description_contains (str | Unset):
        description_endswith (str | Unset):
        description_gt (str | Unset):
        description_gte (str | Unset):
        description_icontains (str | Unset):
        description_iendswith (str | Unset):
        description_iexact (str | Unset):
        description_in (list[str] | Unset):
        description_iregex (str | Unset):
        description_isnull (bool | Unset):
        description_istartswith (str | Unset):
        description_lt (str | Unset):
        description_lte (str | Unset):
        description_range (list[str] | Unset):
        description_regex (str | Unset):
        description_startswith (str | Unset):
        function (OnlineresourcesListFunction | Unset):
        function_contains (str | Unset):
        function_endswith (str | Unset):
        function_gt (str | Unset):
        function_gte (str | Unset):
        function_icontains (str | Unset):
        function_iendswith (str | Unset):
        function_iexact (str | Unset):
        function_in (list[str] | Unset):
        function_iregex (str | Unset):
        function_isnull (bool | Unset):
        function_istartswith (str | Unset):
        function_lt (str | Unset):
        function_lte (str | Unset):
        function_range (list[str] | Unset):
        function_regex (str | Unset):
        function_startswith (str | Unset):
        internal_resource_type (OnlineresourcesListInternalResourceType | Unset):
        internal_resource_type_contains (str | Unset):
        internal_resource_type_endswith (str | Unset):
        internal_resource_type_gt (str | Unset):
        internal_resource_type_gte (str | Unset):
        internal_resource_type_icontains (str | Unset):
        internal_resource_type_iendswith (str | Unset):
        internal_resource_type_iexact (str | Unset):
        internal_resource_type_in (list[str] | Unset):
        internal_resource_type_iregex (str | Unset):
        internal_resource_type_isnull (bool | Unset):
        internal_resource_type_istartswith (str | Unset):
        internal_resource_type_lt (str | Unset):
        internal_resource_type_lte (str | Unset):
        internal_resource_type_range (list[str] | Unset):
        internal_resource_type_regex (str | Unset):
        internal_resource_type_startswith (str | Unset):
        limit (int | Unset):
        linkage (str | Unset):
        linkage_contains (str | Unset):
        linkage_endswith (str | Unset):
        linkage_gt (str | Unset):
        linkage_gte (str | Unset):
        linkage_icontains (str | Unset):
        linkage_iendswith (str | Unset):
        linkage_iexact (str | Unset):
        linkage_in (list[str] | Unset):
        linkage_iregex (str | Unset):
        linkage_isnull (bool | Unset):
        linkage_istartswith (str | Unset):
        linkage_lt (str | Unset):
        linkage_lte (str | Unset):
        linkage_range (list[str] | Unset):
        linkage_regex (str | Unset):
        linkage_startswith (str | Unset):
        name (str | Unset):
        name_contains (str | Unset):
        name_endswith (str | Unset):
        name_gt (str | Unset):
        name_gte (str | Unset):
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_in (list[str] | Unset):
        name_iregex (str | Unset):
        name_isnull (bool | Unset):
        name_istartswith (str | Unset):
        name_lt (str | Unset):
        name_lte (str | Unset):
        name_range (list[str] | Unset):
        name_regex (str | Unset):
        name_startswith (str | Unset):
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
        related_to (int | Unset):
        related_to_gt (int | Unset):
        related_to_gte (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_lt (int | Unset):
        related_to_lte (int | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedOnlineResourceReadList]
    """

    kwargs = _get_kwargs(
        application_profile=application_profile,
        application_profile_contains=application_profile_contains,
        application_profile_endswith=application_profile_endswith,
        application_profile_gt=application_profile_gt,
        application_profile_gte=application_profile_gte,
        application_profile_icontains=application_profile_icontains,
        application_profile_iendswith=application_profile_iendswith,
        application_profile_iexact=application_profile_iexact,
        application_profile_in=application_profile_in,
        application_profile_iregex=application_profile_iregex,
        application_profile_isnull=application_profile_isnull,
        application_profile_istartswith=application_profile_istartswith,
        application_profile_lt=application_profile_lt,
        application_profile_lte=application_profile_lte,
        application_profile_range=application_profile_range,
        application_profile_regex=application_profile_regex,
        application_profile_startswith=application_profile_startswith,
        description=description,
        description_contains=description_contains,
        description_endswith=description_endswith,
        description_gt=description_gt,
        description_gte=description_gte,
        description_icontains=description_icontains,
        description_iendswith=description_iendswith,
        description_iexact=description_iexact,
        description_in=description_in,
        description_iregex=description_iregex,
        description_isnull=description_isnull,
        description_istartswith=description_istartswith,
        description_lt=description_lt,
        description_lte=description_lte,
        description_range=description_range,
        description_regex=description_regex,
        description_startswith=description_startswith,
        function=function,
        function_contains=function_contains,
        function_endswith=function_endswith,
        function_gt=function_gt,
        function_gte=function_gte,
        function_icontains=function_icontains,
        function_iendswith=function_iendswith,
        function_iexact=function_iexact,
        function_in=function_in,
        function_iregex=function_iregex,
        function_isnull=function_isnull,
        function_istartswith=function_istartswith,
        function_lt=function_lt,
        function_lte=function_lte,
        function_range=function_range,
        function_regex=function_regex,
        function_startswith=function_startswith,
        internal_resource_type=internal_resource_type,
        internal_resource_type_contains=internal_resource_type_contains,
        internal_resource_type_endswith=internal_resource_type_endswith,
        internal_resource_type_gt=internal_resource_type_gt,
        internal_resource_type_gte=internal_resource_type_gte,
        internal_resource_type_icontains=internal_resource_type_icontains,
        internal_resource_type_iendswith=internal_resource_type_iendswith,
        internal_resource_type_iexact=internal_resource_type_iexact,
        internal_resource_type_in=internal_resource_type_in,
        internal_resource_type_iregex=internal_resource_type_iregex,
        internal_resource_type_isnull=internal_resource_type_isnull,
        internal_resource_type_istartswith=internal_resource_type_istartswith,
        internal_resource_type_lt=internal_resource_type_lt,
        internal_resource_type_lte=internal_resource_type_lte,
        internal_resource_type_range=internal_resource_type_range,
        internal_resource_type_regex=internal_resource_type_regex,
        internal_resource_type_startswith=internal_resource_type_startswith,
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
        name=name,
        name_contains=name_contains,
        name_endswith=name_endswith,
        name_gt=name_gt,
        name_gte=name_gte,
        name_icontains=name_icontains,
        name_iendswith=name_iendswith,
        name_iexact=name_iexact,
        name_in=name_in,
        name_iregex=name_iregex,
        name_isnull=name_isnull,
        name_istartswith=name_istartswith,
        name_lt=name_lt,
        name_lte=name_lte,
        name_range=name_range,
        name_regex=name_regex,
        name_startswith=name_startswith,
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
        related_to=related_to,
        related_to_gt=related_to_gt,
        related_to_gte=related_to_gte,
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
        related_to_lt=related_to_lt,
        related_to_lte=related_to_lte,
        related_to_ob_id=related_to_ob_id,
        related_to_ob_id_in=related_to_ob_id_in,
        related_to_short_code=related_to_short_code,
        related_to_short_code_in=related_to_short_code_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    application_profile: OnlineresourcesListApplicationProfileFileFormat | Unset = UNSET,
    application_profile_contains: str | Unset = UNSET,
    application_profile_endswith: str | Unset = UNSET,
    application_profile_gt: str | Unset = UNSET,
    application_profile_gte: str | Unset = UNSET,
    application_profile_icontains: str | Unset = UNSET,
    application_profile_iendswith: str | Unset = UNSET,
    application_profile_iexact: str | Unset = UNSET,
    application_profile_in: list[str] | Unset = UNSET,
    application_profile_iregex: str | Unset = UNSET,
    application_profile_isnull: bool | Unset = UNSET,
    application_profile_istartswith: str | Unset = UNSET,
    application_profile_lt: str | Unset = UNSET,
    application_profile_lte: str | Unset = UNSET,
    application_profile_range: list[str] | Unset = UNSET,
    application_profile_regex: str | Unset = UNSET,
    application_profile_startswith: str | Unset = UNSET,
    description: str | Unset = UNSET,
    description_contains: str | Unset = UNSET,
    description_endswith: str | Unset = UNSET,
    description_gt: str | Unset = UNSET,
    description_gte: str | Unset = UNSET,
    description_icontains: str | Unset = UNSET,
    description_iendswith: str | Unset = UNSET,
    description_iexact: str | Unset = UNSET,
    description_in: list[str] | Unset = UNSET,
    description_iregex: str | Unset = UNSET,
    description_isnull: bool | Unset = UNSET,
    description_istartswith: str | Unset = UNSET,
    description_lt: str | Unset = UNSET,
    description_lte: str | Unset = UNSET,
    description_range: list[str] | Unset = UNSET,
    description_regex: str | Unset = UNSET,
    description_startswith: str | Unset = UNSET,
    function: OnlineresourcesListFunction | Unset = UNSET,
    function_contains: str | Unset = UNSET,
    function_endswith: str | Unset = UNSET,
    function_gt: str | Unset = UNSET,
    function_gte: str | Unset = UNSET,
    function_icontains: str | Unset = UNSET,
    function_iendswith: str | Unset = UNSET,
    function_iexact: str | Unset = UNSET,
    function_in: list[str] | Unset = UNSET,
    function_iregex: str | Unset = UNSET,
    function_isnull: bool | Unset = UNSET,
    function_istartswith: str | Unset = UNSET,
    function_lt: str | Unset = UNSET,
    function_lte: str | Unset = UNSET,
    function_range: list[str] | Unset = UNSET,
    function_regex: str | Unset = UNSET,
    function_startswith: str | Unset = UNSET,
    internal_resource_type: OnlineresourcesListInternalResourceType | Unset = UNSET,
    internal_resource_type_contains: str | Unset = UNSET,
    internal_resource_type_endswith: str | Unset = UNSET,
    internal_resource_type_gt: str | Unset = UNSET,
    internal_resource_type_gte: str | Unset = UNSET,
    internal_resource_type_icontains: str | Unset = UNSET,
    internal_resource_type_iendswith: str | Unset = UNSET,
    internal_resource_type_iexact: str | Unset = UNSET,
    internal_resource_type_in: list[str] | Unset = UNSET,
    internal_resource_type_iregex: str | Unset = UNSET,
    internal_resource_type_isnull: bool | Unset = UNSET,
    internal_resource_type_istartswith: str | Unset = UNSET,
    internal_resource_type_lt: str | Unset = UNSET,
    internal_resource_type_lte: str | Unset = UNSET,
    internal_resource_type_range: list[str] | Unset = UNSET,
    internal_resource_type_regex: str | Unset = UNSET,
    internal_resource_type_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    linkage: str | Unset = UNSET,
    linkage_contains: str | Unset = UNSET,
    linkage_endswith: str | Unset = UNSET,
    linkage_gt: str | Unset = UNSET,
    linkage_gte: str | Unset = UNSET,
    linkage_icontains: str | Unset = UNSET,
    linkage_iendswith: str | Unset = UNSET,
    linkage_iexact: str | Unset = UNSET,
    linkage_in: list[str] | Unset = UNSET,
    linkage_iregex: str | Unset = UNSET,
    linkage_isnull: bool | Unset = UNSET,
    linkage_istartswith: str | Unset = UNSET,
    linkage_lt: str | Unset = UNSET,
    linkage_lte: str | Unset = UNSET,
    linkage_range: list[str] | Unset = UNSET,
    linkage_regex: str | Unset = UNSET,
    linkage_startswith: str | Unset = UNSET,
    name: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    name_endswith: str | Unset = UNSET,
    name_gt: str | Unset = UNSET,
    name_gte: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_in: list[str] | Unset = UNSET,
    name_iregex: str | Unset = UNSET,
    name_isnull: bool | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    name_lt: str | Unset = UNSET,
    name_lte: str | Unset = UNSET,
    name_range: list[str] | Unset = UNSET,
    name_regex: str | Unset = UNSET,
    name_startswith: str | Unset = UNSET,
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
    related_to: int | Unset = UNSET,
    related_to_gt: int | Unset = UNSET,
    related_to_gte: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_lt: int | Unset = UNSET,
    related_to_lte: int | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
) -> PaginatedOnlineResourceReadList | None:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        application_profile (OnlineresourcesListApplicationProfileFileFormat | Unset):
        application_profile_contains (str | Unset):
        application_profile_endswith (str | Unset):
        application_profile_gt (str | Unset):
        application_profile_gte (str | Unset):
        application_profile_icontains (str | Unset):
        application_profile_iendswith (str | Unset):
        application_profile_iexact (str | Unset):
        application_profile_in (list[str] | Unset):
        application_profile_iregex (str | Unset):
        application_profile_isnull (bool | Unset):
        application_profile_istartswith (str | Unset):
        application_profile_lt (str | Unset):
        application_profile_lte (str | Unset):
        application_profile_range (list[str] | Unset):
        application_profile_regex (str | Unset):
        application_profile_startswith (str | Unset):
        description (str | Unset):
        description_contains (str | Unset):
        description_endswith (str | Unset):
        description_gt (str | Unset):
        description_gte (str | Unset):
        description_icontains (str | Unset):
        description_iendswith (str | Unset):
        description_iexact (str | Unset):
        description_in (list[str] | Unset):
        description_iregex (str | Unset):
        description_isnull (bool | Unset):
        description_istartswith (str | Unset):
        description_lt (str | Unset):
        description_lte (str | Unset):
        description_range (list[str] | Unset):
        description_regex (str | Unset):
        description_startswith (str | Unset):
        function (OnlineresourcesListFunction | Unset):
        function_contains (str | Unset):
        function_endswith (str | Unset):
        function_gt (str | Unset):
        function_gte (str | Unset):
        function_icontains (str | Unset):
        function_iendswith (str | Unset):
        function_iexact (str | Unset):
        function_in (list[str] | Unset):
        function_iregex (str | Unset):
        function_isnull (bool | Unset):
        function_istartswith (str | Unset):
        function_lt (str | Unset):
        function_lte (str | Unset):
        function_range (list[str] | Unset):
        function_regex (str | Unset):
        function_startswith (str | Unset):
        internal_resource_type (OnlineresourcesListInternalResourceType | Unset):
        internal_resource_type_contains (str | Unset):
        internal_resource_type_endswith (str | Unset):
        internal_resource_type_gt (str | Unset):
        internal_resource_type_gte (str | Unset):
        internal_resource_type_icontains (str | Unset):
        internal_resource_type_iendswith (str | Unset):
        internal_resource_type_iexact (str | Unset):
        internal_resource_type_in (list[str] | Unset):
        internal_resource_type_iregex (str | Unset):
        internal_resource_type_isnull (bool | Unset):
        internal_resource_type_istartswith (str | Unset):
        internal_resource_type_lt (str | Unset):
        internal_resource_type_lte (str | Unset):
        internal_resource_type_range (list[str] | Unset):
        internal_resource_type_regex (str | Unset):
        internal_resource_type_startswith (str | Unset):
        limit (int | Unset):
        linkage (str | Unset):
        linkage_contains (str | Unset):
        linkage_endswith (str | Unset):
        linkage_gt (str | Unset):
        linkage_gte (str | Unset):
        linkage_icontains (str | Unset):
        linkage_iendswith (str | Unset):
        linkage_iexact (str | Unset):
        linkage_in (list[str] | Unset):
        linkage_iregex (str | Unset):
        linkage_isnull (bool | Unset):
        linkage_istartswith (str | Unset):
        linkage_lt (str | Unset):
        linkage_lte (str | Unset):
        linkage_range (list[str] | Unset):
        linkage_regex (str | Unset):
        linkage_startswith (str | Unset):
        name (str | Unset):
        name_contains (str | Unset):
        name_endswith (str | Unset):
        name_gt (str | Unset):
        name_gte (str | Unset):
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_in (list[str] | Unset):
        name_iregex (str | Unset):
        name_isnull (bool | Unset):
        name_istartswith (str | Unset):
        name_lt (str | Unset):
        name_lte (str | Unset):
        name_range (list[str] | Unset):
        name_regex (str | Unset):
        name_startswith (str | Unset):
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
        related_to (int | Unset):
        related_to_gt (int | Unset):
        related_to_gte (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_lt (int | Unset):
        related_to_lte (int | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedOnlineResourceReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            application_profile=application_profile,
            application_profile_contains=application_profile_contains,
            application_profile_endswith=application_profile_endswith,
            application_profile_gt=application_profile_gt,
            application_profile_gte=application_profile_gte,
            application_profile_icontains=application_profile_icontains,
            application_profile_iendswith=application_profile_iendswith,
            application_profile_iexact=application_profile_iexact,
            application_profile_in=application_profile_in,
            application_profile_iregex=application_profile_iregex,
            application_profile_isnull=application_profile_isnull,
            application_profile_istartswith=application_profile_istartswith,
            application_profile_lt=application_profile_lt,
            application_profile_lte=application_profile_lte,
            application_profile_range=application_profile_range,
            application_profile_regex=application_profile_regex,
            application_profile_startswith=application_profile_startswith,
            description=description,
            description_contains=description_contains,
            description_endswith=description_endswith,
            description_gt=description_gt,
            description_gte=description_gte,
            description_icontains=description_icontains,
            description_iendswith=description_iendswith,
            description_iexact=description_iexact,
            description_in=description_in,
            description_iregex=description_iregex,
            description_isnull=description_isnull,
            description_istartswith=description_istartswith,
            description_lt=description_lt,
            description_lte=description_lte,
            description_range=description_range,
            description_regex=description_regex,
            description_startswith=description_startswith,
            function=function,
            function_contains=function_contains,
            function_endswith=function_endswith,
            function_gt=function_gt,
            function_gte=function_gte,
            function_icontains=function_icontains,
            function_iendswith=function_iendswith,
            function_iexact=function_iexact,
            function_in=function_in,
            function_iregex=function_iregex,
            function_isnull=function_isnull,
            function_istartswith=function_istartswith,
            function_lt=function_lt,
            function_lte=function_lte,
            function_range=function_range,
            function_regex=function_regex,
            function_startswith=function_startswith,
            internal_resource_type=internal_resource_type,
            internal_resource_type_contains=internal_resource_type_contains,
            internal_resource_type_endswith=internal_resource_type_endswith,
            internal_resource_type_gt=internal_resource_type_gt,
            internal_resource_type_gte=internal_resource_type_gte,
            internal_resource_type_icontains=internal_resource_type_icontains,
            internal_resource_type_iendswith=internal_resource_type_iendswith,
            internal_resource_type_iexact=internal_resource_type_iexact,
            internal_resource_type_in=internal_resource_type_in,
            internal_resource_type_iregex=internal_resource_type_iregex,
            internal_resource_type_isnull=internal_resource_type_isnull,
            internal_resource_type_istartswith=internal_resource_type_istartswith,
            internal_resource_type_lt=internal_resource_type_lt,
            internal_resource_type_lte=internal_resource_type_lte,
            internal_resource_type_range=internal_resource_type_range,
            internal_resource_type_regex=internal_resource_type_regex,
            internal_resource_type_startswith=internal_resource_type_startswith,
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
            name=name,
            name_contains=name_contains,
            name_endswith=name_endswith,
            name_gt=name_gt,
            name_gte=name_gte,
            name_icontains=name_icontains,
            name_iendswith=name_iendswith,
            name_iexact=name_iexact,
            name_in=name_in,
            name_iregex=name_iregex,
            name_isnull=name_isnull,
            name_istartswith=name_istartswith,
            name_lt=name_lt,
            name_lte=name_lte,
            name_range=name_range,
            name_regex=name_regex,
            name_startswith=name_startswith,
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
            related_to=related_to,
            related_to_gt=related_to_gt,
            related_to_gte=related_to_gte,
            related_to_in=related_to_in,
            related_to_isnull=related_to_isnull,
            related_to_lt=related_to_lt,
            related_to_lte=related_to_lte,
            related_to_ob_id=related_to_ob_id,
            related_to_ob_id_in=related_to_ob_id_in,
            related_to_short_code=related_to_short_code,
            related_to_short_code_in=related_to_short_code_in,
            related_to_uuid=related_to_uuid,
            related_to_uuid_in=related_to_uuid_in,
        )
    ).parsed
