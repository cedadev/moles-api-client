from http import HTTPStatus
from typing import Any, Optional, Union

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
    application_profile: Union[Unset, OnlineresourcesListApplicationProfileFileFormat] = UNSET,
    application_profile_contains: Union[Unset, str] = UNSET,
    application_profile_endswith: Union[Unset, str] = UNSET,
    application_profile_gt: Union[Unset, str] = UNSET,
    application_profile_gte: Union[Unset, str] = UNSET,
    application_profile_icontains: Union[Unset, str] = UNSET,
    application_profile_iendswith: Union[Unset, str] = UNSET,
    application_profile_iexact: Union[Unset, str] = UNSET,
    application_profile_in: Union[Unset, list[str]] = UNSET,
    application_profile_iregex: Union[Unset, str] = UNSET,
    application_profile_isnull: Union[Unset, bool] = UNSET,
    application_profile_istartswith: Union[Unset, str] = UNSET,
    application_profile_lt: Union[Unset, str] = UNSET,
    application_profile_lte: Union[Unset, str] = UNSET,
    application_profile_range: Union[Unset, list[str]] = UNSET,
    application_profile_regex: Union[Unset, str] = UNSET,
    application_profile_startswith: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    description_contains: Union[Unset, str] = UNSET,
    description_endswith: Union[Unset, str] = UNSET,
    description_gt: Union[Unset, str] = UNSET,
    description_gte: Union[Unset, str] = UNSET,
    description_icontains: Union[Unset, str] = UNSET,
    description_iendswith: Union[Unset, str] = UNSET,
    description_iexact: Union[Unset, str] = UNSET,
    description_in: Union[Unset, list[str]] = UNSET,
    description_iregex: Union[Unset, str] = UNSET,
    description_isnull: Union[Unset, bool] = UNSET,
    description_istartswith: Union[Unset, str] = UNSET,
    description_lt: Union[Unset, str] = UNSET,
    description_lte: Union[Unset, str] = UNSET,
    description_range: Union[Unset, list[str]] = UNSET,
    description_regex: Union[Unset, str] = UNSET,
    description_startswith: Union[Unset, str] = UNSET,
    function: Union[Unset, OnlineresourcesListFunction] = UNSET,
    function_contains: Union[Unset, str] = UNSET,
    function_endswith: Union[Unset, str] = UNSET,
    function_gt: Union[Unset, str] = UNSET,
    function_gte: Union[Unset, str] = UNSET,
    function_icontains: Union[Unset, str] = UNSET,
    function_iendswith: Union[Unset, str] = UNSET,
    function_iexact: Union[Unset, str] = UNSET,
    function_in: Union[Unset, list[str]] = UNSET,
    function_iregex: Union[Unset, str] = UNSET,
    function_isnull: Union[Unset, bool] = UNSET,
    function_istartswith: Union[Unset, str] = UNSET,
    function_lt: Union[Unset, str] = UNSET,
    function_lte: Union[Unset, str] = UNSET,
    function_range: Union[Unset, list[str]] = UNSET,
    function_regex: Union[Unset, str] = UNSET,
    function_startswith: Union[Unset, str] = UNSET,
    internal_resource_type: Union[Unset, OnlineresourcesListInternalResourceType] = UNSET,
    internal_resource_type_contains: Union[Unset, str] = UNSET,
    internal_resource_type_endswith: Union[Unset, str] = UNSET,
    internal_resource_type_gt: Union[Unset, str] = UNSET,
    internal_resource_type_gte: Union[Unset, str] = UNSET,
    internal_resource_type_icontains: Union[Unset, str] = UNSET,
    internal_resource_type_iendswith: Union[Unset, str] = UNSET,
    internal_resource_type_iexact: Union[Unset, str] = UNSET,
    internal_resource_type_in: Union[Unset, list[str]] = UNSET,
    internal_resource_type_iregex: Union[Unset, str] = UNSET,
    internal_resource_type_isnull: Union[Unset, bool] = UNSET,
    internal_resource_type_istartswith: Union[Unset, str] = UNSET,
    internal_resource_type_lt: Union[Unset, str] = UNSET,
    internal_resource_type_lte: Union[Unset, str] = UNSET,
    internal_resource_type_range: Union[Unset, list[str]] = UNSET,
    internal_resource_type_regex: Union[Unset, str] = UNSET,
    internal_resource_type_startswith: Union[Unset, str] = UNSET,
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
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    name_endswith: Union[Unset, str] = UNSET,
    name_gt: Union[Unset, str] = UNSET,
    name_gte: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    name_iendswith: Union[Unset, str] = UNSET,
    name_iexact: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    name_iregex: Union[Unset, str] = UNSET,
    name_isnull: Union[Unset, bool] = UNSET,
    name_istartswith: Union[Unset, str] = UNSET,
    name_lt: Union[Unset, str] = UNSET,
    name_lte: Union[Unset, str] = UNSET,
    name_range: Union[Unset, list[str]] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    name_startswith: Union[Unset, str] = UNSET,
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
    related_to: Union[Unset, int] = UNSET,
    related_to_gt: Union[Unset, int] = UNSET,
    related_to_gte: Union[Unset, int] = UNSET,
    related_to_in: Union[Unset, list[int]] = UNSET,
    related_to_isnull: Union[Unset, bool] = UNSET,
    related_to_lt: Union[Unset, int] = UNSET,
    related_to_lte: Union[Unset, int] = UNSET,
    related_to_ob_id: Union[Unset, int] = UNSET,
    related_to_ob_id_in: Union[Unset, list[int]] = UNSET,
    related_to_short_code: Union[Unset, str] = UNSET,
    related_to_short_code_in: Union[Unset, list[str]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_application_profile: Union[Unset, str] = UNSET
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

    json_application_profile_in: Union[Unset, list[str]] = UNSET
    if not isinstance(application_profile_in, Unset):
        json_application_profile_in = ",".join(map(str, application_profile_in))

    params["applicationProfile__in"] = json_application_profile_in

    params["applicationProfile__iregex"] = application_profile_iregex

    params["applicationProfile__isnull"] = application_profile_isnull

    params["applicationProfile__istartswith"] = application_profile_istartswith

    params["applicationProfile__lt"] = application_profile_lt

    params["applicationProfile__lte"] = application_profile_lte

    json_application_profile_range: Union[Unset, list[str]] = UNSET
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

    json_description_in: Union[Unset, list[str]] = UNSET
    if not isinstance(description_in, Unset):
        json_description_in = ",".join(map(str, description_in))

    params["description__in"] = json_description_in

    params["description__iregex"] = description_iregex

    params["description__isnull"] = description_isnull

    params["description__istartswith"] = description_istartswith

    params["description__lt"] = description_lt

    params["description__lte"] = description_lte

    json_description_range: Union[Unset, list[str]] = UNSET
    if not isinstance(description_range, Unset):
        json_description_range = ",".join(map(str, description_range))

    params["description__range"] = json_description_range

    params["description__regex"] = description_regex

    params["description__startswith"] = description_startswith

    json_function: Union[Unset, str] = UNSET
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

    json_function_in: Union[Unset, list[str]] = UNSET
    if not isinstance(function_in, Unset):
        json_function_in = ",".join(map(str, function_in))

    params["function__in"] = json_function_in

    params["function__iregex"] = function_iregex

    params["function__isnull"] = function_isnull

    params["function__istartswith"] = function_istartswith

    params["function__lt"] = function_lt

    params["function__lte"] = function_lte

    json_function_range: Union[Unset, list[str]] = UNSET
    if not isinstance(function_range, Unset):
        json_function_range = ",".join(map(str, function_range))

    params["function__range"] = json_function_range

    params["function__regex"] = function_regex

    params["function__startswith"] = function_startswith

    json_internal_resource_type: Union[Unset, str] = UNSET
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

    json_internal_resource_type_in: Union[Unset, list[str]] = UNSET
    if not isinstance(internal_resource_type_in, Unset):
        json_internal_resource_type_in = ",".join(map(str, internal_resource_type_in))

    params["internalResourceType__in"] = json_internal_resource_type_in

    params["internalResourceType__iregex"] = internal_resource_type_iregex

    params["internalResourceType__isnull"] = internal_resource_type_isnull

    params["internalResourceType__istartswith"] = internal_resource_type_istartswith

    params["internalResourceType__lt"] = internal_resource_type_lt

    params["internalResourceType__lte"] = internal_resource_type_lte

    json_internal_resource_type_range: Union[Unset, list[str]] = UNSET
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

    json_linkage_in: Union[Unset, list[str]] = UNSET
    if not isinstance(linkage_in, Unset):
        json_linkage_in = ",".join(map(str, linkage_in))

    params["linkage__in"] = json_linkage_in

    params["linkage__iregex"] = linkage_iregex

    params["linkage__isnull"] = linkage_isnull

    params["linkage__istartswith"] = linkage_istartswith

    params["linkage__lt"] = linkage_lt

    params["linkage__lte"] = linkage_lte

    json_linkage_range: Union[Unset, list[str]] = UNSET
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

    json_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(name_in, Unset):
        json_name_in = ",".join(map(str, name_in))

    params["name__in"] = json_name_in

    params["name__iregex"] = name_iregex

    params["name__isnull"] = name_isnull

    params["name__istartswith"] = name_istartswith

    params["name__lt"] = name_lt

    params["name__lte"] = name_lte

    json_name_range: Union[Unset, list[str]] = UNSET
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

    params["relatedTo"] = related_to

    params["relatedTo__gt"] = related_to_gt

    params["relatedTo__gte"] = related_to_gte

    json_related_to_in: Union[Unset, list[int]] = UNSET
    if not isinstance(related_to_in, Unset):
        json_related_to_in = ",".join(map(str, related_to_in))

    params["relatedTo__in"] = json_related_to_in

    params["relatedTo__isnull"] = related_to_isnull

    params["relatedTo__lt"] = related_to_lt

    params["relatedTo__lte"] = related_to_lte

    params["relatedTo__ob_id"] = related_to_ob_id

    json_related_to_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(related_to_ob_id_in, Unset):
        json_related_to_ob_id_in = ",".join(map(str, related_to_ob_id_in))

    params["relatedTo__ob_id__in"] = json_related_to_ob_id_in

    params["relatedTo__short_code"] = related_to_short_code

    json_related_to_short_code_in: Union[Unset, list[str]] = UNSET
    if not isinstance(related_to_short_code_in, Unset):
        json_related_to_short_code_in = ",".join(map(str, related_to_short_code_in))

    params["relatedTo__short_code__in"] = json_related_to_short_code_in

    params["relatedTo__uuid"] = related_to_uuid

    json_related_to_uuid_in: Union[Unset, list[str]] = UNSET
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedOnlineResourceReadList]:
    if response.status_code == 200:
        response_200 = PaginatedOnlineResourceReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
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
    application_profile: Union[Unset, OnlineresourcesListApplicationProfileFileFormat] = UNSET,
    application_profile_contains: Union[Unset, str] = UNSET,
    application_profile_endswith: Union[Unset, str] = UNSET,
    application_profile_gt: Union[Unset, str] = UNSET,
    application_profile_gte: Union[Unset, str] = UNSET,
    application_profile_icontains: Union[Unset, str] = UNSET,
    application_profile_iendswith: Union[Unset, str] = UNSET,
    application_profile_iexact: Union[Unset, str] = UNSET,
    application_profile_in: Union[Unset, list[str]] = UNSET,
    application_profile_iregex: Union[Unset, str] = UNSET,
    application_profile_isnull: Union[Unset, bool] = UNSET,
    application_profile_istartswith: Union[Unset, str] = UNSET,
    application_profile_lt: Union[Unset, str] = UNSET,
    application_profile_lte: Union[Unset, str] = UNSET,
    application_profile_range: Union[Unset, list[str]] = UNSET,
    application_profile_regex: Union[Unset, str] = UNSET,
    application_profile_startswith: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    description_contains: Union[Unset, str] = UNSET,
    description_endswith: Union[Unset, str] = UNSET,
    description_gt: Union[Unset, str] = UNSET,
    description_gte: Union[Unset, str] = UNSET,
    description_icontains: Union[Unset, str] = UNSET,
    description_iendswith: Union[Unset, str] = UNSET,
    description_iexact: Union[Unset, str] = UNSET,
    description_in: Union[Unset, list[str]] = UNSET,
    description_iregex: Union[Unset, str] = UNSET,
    description_isnull: Union[Unset, bool] = UNSET,
    description_istartswith: Union[Unset, str] = UNSET,
    description_lt: Union[Unset, str] = UNSET,
    description_lte: Union[Unset, str] = UNSET,
    description_range: Union[Unset, list[str]] = UNSET,
    description_regex: Union[Unset, str] = UNSET,
    description_startswith: Union[Unset, str] = UNSET,
    function: Union[Unset, OnlineresourcesListFunction] = UNSET,
    function_contains: Union[Unset, str] = UNSET,
    function_endswith: Union[Unset, str] = UNSET,
    function_gt: Union[Unset, str] = UNSET,
    function_gte: Union[Unset, str] = UNSET,
    function_icontains: Union[Unset, str] = UNSET,
    function_iendswith: Union[Unset, str] = UNSET,
    function_iexact: Union[Unset, str] = UNSET,
    function_in: Union[Unset, list[str]] = UNSET,
    function_iregex: Union[Unset, str] = UNSET,
    function_isnull: Union[Unset, bool] = UNSET,
    function_istartswith: Union[Unset, str] = UNSET,
    function_lt: Union[Unset, str] = UNSET,
    function_lte: Union[Unset, str] = UNSET,
    function_range: Union[Unset, list[str]] = UNSET,
    function_regex: Union[Unset, str] = UNSET,
    function_startswith: Union[Unset, str] = UNSET,
    internal_resource_type: Union[Unset, OnlineresourcesListInternalResourceType] = UNSET,
    internal_resource_type_contains: Union[Unset, str] = UNSET,
    internal_resource_type_endswith: Union[Unset, str] = UNSET,
    internal_resource_type_gt: Union[Unset, str] = UNSET,
    internal_resource_type_gte: Union[Unset, str] = UNSET,
    internal_resource_type_icontains: Union[Unset, str] = UNSET,
    internal_resource_type_iendswith: Union[Unset, str] = UNSET,
    internal_resource_type_iexact: Union[Unset, str] = UNSET,
    internal_resource_type_in: Union[Unset, list[str]] = UNSET,
    internal_resource_type_iregex: Union[Unset, str] = UNSET,
    internal_resource_type_isnull: Union[Unset, bool] = UNSET,
    internal_resource_type_istartswith: Union[Unset, str] = UNSET,
    internal_resource_type_lt: Union[Unset, str] = UNSET,
    internal_resource_type_lte: Union[Unset, str] = UNSET,
    internal_resource_type_range: Union[Unset, list[str]] = UNSET,
    internal_resource_type_regex: Union[Unset, str] = UNSET,
    internal_resource_type_startswith: Union[Unset, str] = UNSET,
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
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    name_endswith: Union[Unset, str] = UNSET,
    name_gt: Union[Unset, str] = UNSET,
    name_gte: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    name_iendswith: Union[Unset, str] = UNSET,
    name_iexact: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    name_iregex: Union[Unset, str] = UNSET,
    name_isnull: Union[Unset, bool] = UNSET,
    name_istartswith: Union[Unset, str] = UNSET,
    name_lt: Union[Unset, str] = UNSET,
    name_lte: Union[Unset, str] = UNSET,
    name_range: Union[Unset, list[str]] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    name_startswith: Union[Unset, str] = UNSET,
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
    related_to: Union[Unset, int] = UNSET,
    related_to_gt: Union[Unset, int] = UNSET,
    related_to_gte: Union[Unset, int] = UNSET,
    related_to_in: Union[Unset, list[int]] = UNSET,
    related_to_isnull: Union[Unset, bool] = UNSET,
    related_to_lt: Union[Unset, int] = UNSET,
    related_to_lte: Union[Unset, int] = UNSET,
    related_to_ob_id: Union[Unset, int] = UNSET,
    related_to_ob_id_in: Union[Unset, list[int]] = UNSET,
    related_to_short_code: Union[Unset, str] = UNSET,
    related_to_short_code_in: Union[Unset, list[str]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedOnlineResourceReadList]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        application_profile (Union[Unset, OnlineresourcesListApplicationProfileFileFormat]):
        application_profile_contains (Union[Unset, str]):
        application_profile_endswith (Union[Unset, str]):
        application_profile_gt (Union[Unset, str]):
        application_profile_gte (Union[Unset, str]):
        application_profile_icontains (Union[Unset, str]):
        application_profile_iendswith (Union[Unset, str]):
        application_profile_iexact (Union[Unset, str]):
        application_profile_in (Union[Unset, list[str]]):
        application_profile_iregex (Union[Unset, str]):
        application_profile_isnull (Union[Unset, bool]):
        application_profile_istartswith (Union[Unset, str]):
        application_profile_lt (Union[Unset, str]):
        application_profile_lte (Union[Unset, str]):
        application_profile_range (Union[Unset, list[str]]):
        application_profile_regex (Union[Unset, str]):
        application_profile_startswith (Union[Unset, str]):
        description (Union[Unset, str]):
        description_contains (Union[Unset, str]):
        description_endswith (Union[Unset, str]):
        description_gt (Union[Unset, str]):
        description_gte (Union[Unset, str]):
        description_icontains (Union[Unset, str]):
        description_iendswith (Union[Unset, str]):
        description_iexact (Union[Unset, str]):
        description_in (Union[Unset, list[str]]):
        description_iregex (Union[Unset, str]):
        description_isnull (Union[Unset, bool]):
        description_istartswith (Union[Unset, str]):
        description_lt (Union[Unset, str]):
        description_lte (Union[Unset, str]):
        description_range (Union[Unset, list[str]]):
        description_regex (Union[Unset, str]):
        description_startswith (Union[Unset, str]):
        function (Union[Unset, OnlineresourcesListFunction]):
        function_contains (Union[Unset, str]):
        function_endswith (Union[Unset, str]):
        function_gt (Union[Unset, str]):
        function_gte (Union[Unset, str]):
        function_icontains (Union[Unset, str]):
        function_iendswith (Union[Unset, str]):
        function_iexact (Union[Unset, str]):
        function_in (Union[Unset, list[str]]):
        function_iregex (Union[Unset, str]):
        function_isnull (Union[Unset, bool]):
        function_istartswith (Union[Unset, str]):
        function_lt (Union[Unset, str]):
        function_lte (Union[Unset, str]):
        function_range (Union[Unset, list[str]]):
        function_regex (Union[Unset, str]):
        function_startswith (Union[Unset, str]):
        internal_resource_type (Union[Unset, OnlineresourcesListInternalResourceType]):
        internal_resource_type_contains (Union[Unset, str]):
        internal_resource_type_endswith (Union[Unset, str]):
        internal_resource_type_gt (Union[Unset, str]):
        internal_resource_type_gte (Union[Unset, str]):
        internal_resource_type_icontains (Union[Unset, str]):
        internal_resource_type_iendswith (Union[Unset, str]):
        internal_resource_type_iexact (Union[Unset, str]):
        internal_resource_type_in (Union[Unset, list[str]]):
        internal_resource_type_iregex (Union[Unset, str]):
        internal_resource_type_isnull (Union[Unset, bool]):
        internal_resource_type_istartswith (Union[Unset, str]):
        internal_resource_type_lt (Union[Unset, str]):
        internal_resource_type_lte (Union[Unset, str]):
        internal_resource_type_range (Union[Unset, list[str]]):
        internal_resource_type_regex (Union[Unset, str]):
        internal_resource_type_startswith (Union[Unset, str]):
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
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):
        name_endswith (Union[Unset, str]):
        name_gt (Union[Unset, str]):
        name_gte (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        name_iendswith (Union[Unset, str]):
        name_iexact (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        name_iregex (Union[Unset, str]):
        name_isnull (Union[Unset, bool]):
        name_istartswith (Union[Unset, str]):
        name_lt (Union[Unset, str]):
        name_lte (Union[Unset, str]):
        name_range (Union[Unset, list[str]]):
        name_regex (Union[Unset, str]):
        name_startswith (Union[Unset, str]):
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
        related_to (Union[Unset, int]):
        related_to_gt (Union[Unset, int]):
        related_to_gte (Union[Unset, int]):
        related_to_in (Union[Unset, list[int]]):
        related_to_isnull (Union[Unset, bool]):
        related_to_lt (Union[Unset, int]):
        related_to_lte (Union[Unset, int]):
        related_to_ob_id (Union[Unset, int]):
        related_to_ob_id_in (Union[Unset, list[int]]):
        related_to_short_code (Union[Unset, str]):
        related_to_short_code_in (Union[Unset, list[str]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):

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
    application_profile: Union[Unset, OnlineresourcesListApplicationProfileFileFormat] = UNSET,
    application_profile_contains: Union[Unset, str] = UNSET,
    application_profile_endswith: Union[Unset, str] = UNSET,
    application_profile_gt: Union[Unset, str] = UNSET,
    application_profile_gte: Union[Unset, str] = UNSET,
    application_profile_icontains: Union[Unset, str] = UNSET,
    application_profile_iendswith: Union[Unset, str] = UNSET,
    application_profile_iexact: Union[Unset, str] = UNSET,
    application_profile_in: Union[Unset, list[str]] = UNSET,
    application_profile_iregex: Union[Unset, str] = UNSET,
    application_profile_isnull: Union[Unset, bool] = UNSET,
    application_profile_istartswith: Union[Unset, str] = UNSET,
    application_profile_lt: Union[Unset, str] = UNSET,
    application_profile_lte: Union[Unset, str] = UNSET,
    application_profile_range: Union[Unset, list[str]] = UNSET,
    application_profile_regex: Union[Unset, str] = UNSET,
    application_profile_startswith: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    description_contains: Union[Unset, str] = UNSET,
    description_endswith: Union[Unset, str] = UNSET,
    description_gt: Union[Unset, str] = UNSET,
    description_gte: Union[Unset, str] = UNSET,
    description_icontains: Union[Unset, str] = UNSET,
    description_iendswith: Union[Unset, str] = UNSET,
    description_iexact: Union[Unset, str] = UNSET,
    description_in: Union[Unset, list[str]] = UNSET,
    description_iregex: Union[Unset, str] = UNSET,
    description_isnull: Union[Unset, bool] = UNSET,
    description_istartswith: Union[Unset, str] = UNSET,
    description_lt: Union[Unset, str] = UNSET,
    description_lte: Union[Unset, str] = UNSET,
    description_range: Union[Unset, list[str]] = UNSET,
    description_regex: Union[Unset, str] = UNSET,
    description_startswith: Union[Unset, str] = UNSET,
    function: Union[Unset, OnlineresourcesListFunction] = UNSET,
    function_contains: Union[Unset, str] = UNSET,
    function_endswith: Union[Unset, str] = UNSET,
    function_gt: Union[Unset, str] = UNSET,
    function_gte: Union[Unset, str] = UNSET,
    function_icontains: Union[Unset, str] = UNSET,
    function_iendswith: Union[Unset, str] = UNSET,
    function_iexact: Union[Unset, str] = UNSET,
    function_in: Union[Unset, list[str]] = UNSET,
    function_iregex: Union[Unset, str] = UNSET,
    function_isnull: Union[Unset, bool] = UNSET,
    function_istartswith: Union[Unset, str] = UNSET,
    function_lt: Union[Unset, str] = UNSET,
    function_lte: Union[Unset, str] = UNSET,
    function_range: Union[Unset, list[str]] = UNSET,
    function_regex: Union[Unset, str] = UNSET,
    function_startswith: Union[Unset, str] = UNSET,
    internal_resource_type: Union[Unset, OnlineresourcesListInternalResourceType] = UNSET,
    internal_resource_type_contains: Union[Unset, str] = UNSET,
    internal_resource_type_endswith: Union[Unset, str] = UNSET,
    internal_resource_type_gt: Union[Unset, str] = UNSET,
    internal_resource_type_gte: Union[Unset, str] = UNSET,
    internal_resource_type_icontains: Union[Unset, str] = UNSET,
    internal_resource_type_iendswith: Union[Unset, str] = UNSET,
    internal_resource_type_iexact: Union[Unset, str] = UNSET,
    internal_resource_type_in: Union[Unset, list[str]] = UNSET,
    internal_resource_type_iregex: Union[Unset, str] = UNSET,
    internal_resource_type_isnull: Union[Unset, bool] = UNSET,
    internal_resource_type_istartswith: Union[Unset, str] = UNSET,
    internal_resource_type_lt: Union[Unset, str] = UNSET,
    internal_resource_type_lte: Union[Unset, str] = UNSET,
    internal_resource_type_range: Union[Unset, list[str]] = UNSET,
    internal_resource_type_regex: Union[Unset, str] = UNSET,
    internal_resource_type_startswith: Union[Unset, str] = UNSET,
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
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    name_endswith: Union[Unset, str] = UNSET,
    name_gt: Union[Unset, str] = UNSET,
    name_gte: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    name_iendswith: Union[Unset, str] = UNSET,
    name_iexact: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    name_iregex: Union[Unset, str] = UNSET,
    name_isnull: Union[Unset, bool] = UNSET,
    name_istartswith: Union[Unset, str] = UNSET,
    name_lt: Union[Unset, str] = UNSET,
    name_lte: Union[Unset, str] = UNSET,
    name_range: Union[Unset, list[str]] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    name_startswith: Union[Unset, str] = UNSET,
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
    related_to: Union[Unset, int] = UNSET,
    related_to_gt: Union[Unset, int] = UNSET,
    related_to_gte: Union[Unset, int] = UNSET,
    related_to_in: Union[Unset, list[int]] = UNSET,
    related_to_isnull: Union[Unset, bool] = UNSET,
    related_to_lt: Union[Unset, int] = UNSET,
    related_to_lte: Union[Unset, int] = UNSET,
    related_to_ob_id: Union[Unset, int] = UNSET,
    related_to_ob_id_in: Union[Unset, list[int]] = UNSET,
    related_to_short_code: Union[Unset, str] = UNSET,
    related_to_short_code_in: Union[Unset, list[str]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedOnlineResourceReadList]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        application_profile (Union[Unset, OnlineresourcesListApplicationProfileFileFormat]):
        application_profile_contains (Union[Unset, str]):
        application_profile_endswith (Union[Unset, str]):
        application_profile_gt (Union[Unset, str]):
        application_profile_gte (Union[Unset, str]):
        application_profile_icontains (Union[Unset, str]):
        application_profile_iendswith (Union[Unset, str]):
        application_profile_iexact (Union[Unset, str]):
        application_profile_in (Union[Unset, list[str]]):
        application_profile_iregex (Union[Unset, str]):
        application_profile_isnull (Union[Unset, bool]):
        application_profile_istartswith (Union[Unset, str]):
        application_profile_lt (Union[Unset, str]):
        application_profile_lte (Union[Unset, str]):
        application_profile_range (Union[Unset, list[str]]):
        application_profile_regex (Union[Unset, str]):
        application_profile_startswith (Union[Unset, str]):
        description (Union[Unset, str]):
        description_contains (Union[Unset, str]):
        description_endswith (Union[Unset, str]):
        description_gt (Union[Unset, str]):
        description_gte (Union[Unset, str]):
        description_icontains (Union[Unset, str]):
        description_iendswith (Union[Unset, str]):
        description_iexact (Union[Unset, str]):
        description_in (Union[Unset, list[str]]):
        description_iregex (Union[Unset, str]):
        description_isnull (Union[Unset, bool]):
        description_istartswith (Union[Unset, str]):
        description_lt (Union[Unset, str]):
        description_lte (Union[Unset, str]):
        description_range (Union[Unset, list[str]]):
        description_regex (Union[Unset, str]):
        description_startswith (Union[Unset, str]):
        function (Union[Unset, OnlineresourcesListFunction]):
        function_contains (Union[Unset, str]):
        function_endswith (Union[Unset, str]):
        function_gt (Union[Unset, str]):
        function_gte (Union[Unset, str]):
        function_icontains (Union[Unset, str]):
        function_iendswith (Union[Unset, str]):
        function_iexact (Union[Unset, str]):
        function_in (Union[Unset, list[str]]):
        function_iregex (Union[Unset, str]):
        function_isnull (Union[Unset, bool]):
        function_istartswith (Union[Unset, str]):
        function_lt (Union[Unset, str]):
        function_lte (Union[Unset, str]):
        function_range (Union[Unset, list[str]]):
        function_regex (Union[Unset, str]):
        function_startswith (Union[Unset, str]):
        internal_resource_type (Union[Unset, OnlineresourcesListInternalResourceType]):
        internal_resource_type_contains (Union[Unset, str]):
        internal_resource_type_endswith (Union[Unset, str]):
        internal_resource_type_gt (Union[Unset, str]):
        internal_resource_type_gte (Union[Unset, str]):
        internal_resource_type_icontains (Union[Unset, str]):
        internal_resource_type_iendswith (Union[Unset, str]):
        internal_resource_type_iexact (Union[Unset, str]):
        internal_resource_type_in (Union[Unset, list[str]]):
        internal_resource_type_iregex (Union[Unset, str]):
        internal_resource_type_isnull (Union[Unset, bool]):
        internal_resource_type_istartswith (Union[Unset, str]):
        internal_resource_type_lt (Union[Unset, str]):
        internal_resource_type_lte (Union[Unset, str]):
        internal_resource_type_range (Union[Unset, list[str]]):
        internal_resource_type_regex (Union[Unset, str]):
        internal_resource_type_startswith (Union[Unset, str]):
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
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):
        name_endswith (Union[Unset, str]):
        name_gt (Union[Unset, str]):
        name_gte (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        name_iendswith (Union[Unset, str]):
        name_iexact (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        name_iregex (Union[Unset, str]):
        name_isnull (Union[Unset, bool]):
        name_istartswith (Union[Unset, str]):
        name_lt (Union[Unset, str]):
        name_lte (Union[Unset, str]):
        name_range (Union[Unset, list[str]]):
        name_regex (Union[Unset, str]):
        name_startswith (Union[Unset, str]):
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
        related_to (Union[Unset, int]):
        related_to_gt (Union[Unset, int]):
        related_to_gte (Union[Unset, int]):
        related_to_in (Union[Unset, list[int]]):
        related_to_isnull (Union[Unset, bool]):
        related_to_lt (Union[Unset, int]):
        related_to_lte (Union[Unset, int]):
        related_to_ob_id (Union[Unset, int]):
        related_to_ob_id_in (Union[Unset, list[int]]):
        related_to_short_code (Union[Unset, str]):
        related_to_short_code_in (Union[Unset, list[str]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):

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
    application_profile: Union[Unset, OnlineresourcesListApplicationProfileFileFormat] = UNSET,
    application_profile_contains: Union[Unset, str] = UNSET,
    application_profile_endswith: Union[Unset, str] = UNSET,
    application_profile_gt: Union[Unset, str] = UNSET,
    application_profile_gte: Union[Unset, str] = UNSET,
    application_profile_icontains: Union[Unset, str] = UNSET,
    application_profile_iendswith: Union[Unset, str] = UNSET,
    application_profile_iexact: Union[Unset, str] = UNSET,
    application_profile_in: Union[Unset, list[str]] = UNSET,
    application_profile_iregex: Union[Unset, str] = UNSET,
    application_profile_isnull: Union[Unset, bool] = UNSET,
    application_profile_istartswith: Union[Unset, str] = UNSET,
    application_profile_lt: Union[Unset, str] = UNSET,
    application_profile_lte: Union[Unset, str] = UNSET,
    application_profile_range: Union[Unset, list[str]] = UNSET,
    application_profile_regex: Union[Unset, str] = UNSET,
    application_profile_startswith: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    description_contains: Union[Unset, str] = UNSET,
    description_endswith: Union[Unset, str] = UNSET,
    description_gt: Union[Unset, str] = UNSET,
    description_gte: Union[Unset, str] = UNSET,
    description_icontains: Union[Unset, str] = UNSET,
    description_iendswith: Union[Unset, str] = UNSET,
    description_iexact: Union[Unset, str] = UNSET,
    description_in: Union[Unset, list[str]] = UNSET,
    description_iregex: Union[Unset, str] = UNSET,
    description_isnull: Union[Unset, bool] = UNSET,
    description_istartswith: Union[Unset, str] = UNSET,
    description_lt: Union[Unset, str] = UNSET,
    description_lte: Union[Unset, str] = UNSET,
    description_range: Union[Unset, list[str]] = UNSET,
    description_regex: Union[Unset, str] = UNSET,
    description_startswith: Union[Unset, str] = UNSET,
    function: Union[Unset, OnlineresourcesListFunction] = UNSET,
    function_contains: Union[Unset, str] = UNSET,
    function_endswith: Union[Unset, str] = UNSET,
    function_gt: Union[Unset, str] = UNSET,
    function_gte: Union[Unset, str] = UNSET,
    function_icontains: Union[Unset, str] = UNSET,
    function_iendswith: Union[Unset, str] = UNSET,
    function_iexact: Union[Unset, str] = UNSET,
    function_in: Union[Unset, list[str]] = UNSET,
    function_iregex: Union[Unset, str] = UNSET,
    function_isnull: Union[Unset, bool] = UNSET,
    function_istartswith: Union[Unset, str] = UNSET,
    function_lt: Union[Unset, str] = UNSET,
    function_lte: Union[Unset, str] = UNSET,
    function_range: Union[Unset, list[str]] = UNSET,
    function_regex: Union[Unset, str] = UNSET,
    function_startswith: Union[Unset, str] = UNSET,
    internal_resource_type: Union[Unset, OnlineresourcesListInternalResourceType] = UNSET,
    internal_resource_type_contains: Union[Unset, str] = UNSET,
    internal_resource_type_endswith: Union[Unset, str] = UNSET,
    internal_resource_type_gt: Union[Unset, str] = UNSET,
    internal_resource_type_gte: Union[Unset, str] = UNSET,
    internal_resource_type_icontains: Union[Unset, str] = UNSET,
    internal_resource_type_iendswith: Union[Unset, str] = UNSET,
    internal_resource_type_iexact: Union[Unset, str] = UNSET,
    internal_resource_type_in: Union[Unset, list[str]] = UNSET,
    internal_resource_type_iregex: Union[Unset, str] = UNSET,
    internal_resource_type_isnull: Union[Unset, bool] = UNSET,
    internal_resource_type_istartswith: Union[Unset, str] = UNSET,
    internal_resource_type_lt: Union[Unset, str] = UNSET,
    internal_resource_type_lte: Union[Unset, str] = UNSET,
    internal_resource_type_range: Union[Unset, list[str]] = UNSET,
    internal_resource_type_regex: Union[Unset, str] = UNSET,
    internal_resource_type_startswith: Union[Unset, str] = UNSET,
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
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    name_endswith: Union[Unset, str] = UNSET,
    name_gt: Union[Unset, str] = UNSET,
    name_gte: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    name_iendswith: Union[Unset, str] = UNSET,
    name_iexact: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    name_iregex: Union[Unset, str] = UNSET,
    name_isnull: Union[Unset, bool] = UNSET,
    name_istartswith: Union[Unset, str] = UNSET,
    name_lt: Union[Unset, str] = UNSET,
    name_lte: Union[Unset, str] = UNSET,
    name_range: Union[Unset, list[str]] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    name_startswith: Union[Unset, str] = UNSET,
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
    related_to: Union[Unset, int] = UNSET,
    related_to_gt: Union[Unset, int] = UNSET,
    related_to_gte: Union[Unset, int] = UNSET,
    related_to_in: Union[Unset, list[int]] = UNSET,
    related_to_isnull: Union[Unset, bool] = UNSET,
    related_to_lt: Union[Unset, int] = UNSET,
    related_to_lte: Union[Unset, int] = UNSET,
    related_to_ob_id: Union[Unset, int] = UNSET,
    related_to_ob_id_in: Union[Unset, list[int]] = UNSET,
    related_to_short_code: Union[Unset, str] = UNSET,
    related_to_short_code_in: Union[Unset, list[str]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedOnlineResourceReadList]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        application_profile (Union[Unset, OnlineresourcesListApplicationProfileFileFormat]):
        application_profile_contains (Union[Unset, str]):
        application_profile_endswith (Union[Unset, str]):
        application_profile_gt (Union[Unset, str]):
        application_profile_gte (Union[Unset, str]):
        application_profile_icontains (Union[Unset, str]):
        application_profile_iendswith (Union[Unset, str]):
        application_profile_iexact (Union[Unset, str]):
        application_profile_in (Union[Unset, list[str]]):
        application_profile_iregex (Union[Unset, str]):
        application_profile_isnull (Union[Unset, bool]):
        application_profile_istartswith (Union[Unset, str]):
        application_profile_lt (Union[Unset, str]):
        application_profile_lte (Union[Unset, str]):
        application_profile_range (Union[Unset, list[str]]):
        application_profile_regex (Union[Unset, str]):
        application_profile_startswith (Union[Unset, str]):
        description (Union[Unset, str]):
        description_contains (Union[Unset, str]):
        description_endswith (Union[Unset, str]):
        description_gt (Union[Unset, str]):
        description_gte (Union[Unset, str]):
        description_icontains (Union[Unset, str]):
        description_iendswith (Union[Unset, str]):
        description_iexact (Union[Unset, str]):
        description_in (Union[Unset, list[str]]):
        description_iregex (Union[Unset, str]):
        description_isnull (Union[Unset, bool]):
        description_istartswith (Union[Unset, str]):
        description_lt (Union[Unset, str]):
        description_lte (Union[Unset, str]):
        description_range (Union[Unset, list[str]]):
        description_regex (Union[Unset, str]):
        description_startswith (Union[Unset, str]):
        function (Union[Unset, OnlineresourcesListFunction]):
        function_contains (Union[Unset, str]):
        function_endswith (Union[Unset, str]):
        function_gt (Union[Unset, str]):
        function_gte (Union[Unset, str]):
        function_icontains (Union[Unset, str]):
        function_iendswith (Union[Unset, str]):
        function_iexact (Union[Unset, str]):
        function_in (Union[Unset, list[str]]):
        function_iregex (Union[Unset, str]):
        function_isnull (Union[Unset, bool]):
        function_istartswith (Union[Unset, str]):
        function_lt (Union[Unset, str]):
        function_lte (Union[Unset, str]):
        function_range (Union[Unset, list[str]]):
        function_regex (Union[Unset, str]):
        function_startswith (Union[Unset, str]):
        internal_resource_type (Union[Unset, OnlineresourcesListInternalResourceType]):
        internal_resource_type_contains (Union[Unset, str]):
        internal_resource_type_endswith (Union[Unset, str]):
        internal_resource_type_gt (Union[Unset, str]):
        internal_resource_type_gte (Union[Unset, str]):
        internal_resource_type_icontains (Union[Unset, str]):
        internal_resource_type_iendswith (Union[Unset, str]):
        internal_resource_type_iexact (Union[Unset, str]):
        internal_resource_type_in (Union[Unset, list[str]]):
        internal_resource_type_iregex (Union[Unset, str]):
        internal_resource_type_isnull (Union[Unset, bool]):
        internal_resource_type_istartswith (Union[Unset, str]):
        internal_resource_type_lt (Union[Unset, str]):
        internal_resource_type_lte (Union[Unset, str]):
        internal_resource_type_range (Union[Unset, list[str]]):
        internal_resource_type_regex (Union[Unset, str]):
        internal_resource_type_startswith (Union[Unset, str]):
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
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):
        name_endswith (Union[Unset, str]):
        name_gt (Union[Unset, str]):
        name_gte (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        name_iendswith (Union[Unset, str]):
        name_iexact (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        name_iregex (Union[Unset, str]):
        name_isnull (Union[Unset, bool]):
        name_istartswith (Union[Unset, str]):
        name_lt (Union[Unset, str]):
        name_lte (Union[Unset, str]):
        name_range (Union[Unset, list[str]]):
        name_regex (Union[Unset, str]):
        name_startswith (Union[Unset, str]):
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
        related_to (Union[Unset, int]):
        related_to_gt (Union[Unset, int]):
        related_to_gte (Union[Unset, int]):
        related_to_in (Union[Unset, list[int]]):
        related_to_isnull (Union[Unset, bool]):
        related_to_lt (Union[Unset, int]):
        related_to_lte (Union[Unset, int]):
        related_to_ob_id (Union[Unset, int]):
        related_to_ob_id_in (Union[Unset, list[int]]):
        related_to_short_code (Union[Unset, str]):
        related_to_short_code_in (Union[Unset, list[str]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):

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
    application_profile: Union[Unset, OnlineresourcesListApplicationProfileFileFormat] = UNSET,
    application_profile_contains: Union[Unset, str] = UNSET,
    application_profile_endswith: Union[Unset, str] = UNSET,
    application_profile_gt: Union[Unset, str] = UNSET,
    application_profile_gte: Union[Unset, str] = UNSET,
    application_profile_icontains: Union[Unset, str] = UNSET,
    application_profile_iendswith: Union[Unset, str] = UNSET,
    application_profile_iexact: Union[Unset, str] = UNSET,
    application_profile_in: Union[Unset, list[str]] = UNSET,
    application_profile_iregex: Union[Unset, str] = UNSET,
    application_profile_isnull: Union[Unset, bool] = UNSET,
    application_profile_istartswith: Union[Unset, str] = UNSET,
    application_profile_lt: Union[Unset, str] = UNSET,
    application_profile_lte: Union[Unset, str] = UNSET,
    application_profile_range: Union[Unset, list[str]] = UNSET,
    application_profile_regex: Union[Unset, str] = UNSET,
    application_profile_startswith: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    description_contains: Union[Unset, str] = UNSET,
    description_endswith: Union[Unset, str] = UNSET,
    description_gt: Union[Unset, str] = UNSET,
    description_gte: Union[Unset, str] = UNSET,
    description_icontains: Union[Unset, str] = UNSET,
    description_iendswith: Union[Unset, str] = UNSET,
    description_iexact: Union[Unset, str] = UNSET,
    description_in: Union[Unset, list[str]] = UNSET,
    description_iregex: Union[Unset, str] = UNSET,
    description_isnull: Union[Unset, bool] = UNSET,
    description_istartswith: Union[Unset, str] = UNSET,
    description_lt: Union[Unset, str] = UNSET,
    description_lte: Union[Unset, str] = UNSET,
    description_range: Union[Unset, list[str]] = UNSET,
    description_regex: Union[Unset, str] = UNSET,
    description_startswith: Union[Unset, str] = UNSET,
    function: Union[Unset, OnlineresourcesListFunction] = UNSET,
    function_contains: Union[Unset, str] = UNSET,
    function_endswith: Union[Unset, str] = UNSET,
    function_gt: Union[Unset, str] = UNSET,
    function_gte: Union[Unset, str] = UNSET,
    function_icontains: Union[Unset, str] = UNSET,
    function_iendswith: Union[Unset, str] = UNSET,
    function_iexact: Union[Unset, str] = UNSET,
    function_in: Union[Unset, list[str]] = UNSET,
    function_iregex: Union[Unset, str] = UNSET,
    function_isnull: Union[Unset, bool] = UNSET,
    function_istartswith: Union[Unset, str] = UNSET,
    function_lt: Union[Unset, str] = UNSET,
    function_lte: Union[Unset, str] = UNSET,
    function_range: Union[Unset, list[str]] = UNSET,
    function_regex: Union[Unset, str] = UNSET,
    function_startswith: Union[Unset, str] = UNSET,
    internal_resource_type: Union[Unset, OnlineresourcesListInternalResourceType] = UNSET,
    internal_resource_type_contains: Union[Unset, str] = UNSET,
    internal_resource_type_endswith: Union[Unset, str] = UNSET,
    internal_resource_type_gt: Union[Unset, str] = UNSET,
    internal_resource_type_gte: Union[Unset, str] = UNSET,
    internal_resource_type_icontains: Union[Unset, str] = UNSET,
    internal_resource_type_iendswith: Union[Unset, str] = UNSET,
    internal_resource_type_iexact: Union[Unset, str] = UNSET,
    internal_resource_type_in: Union[Unset, list[str]] = UNSET,
    internal_resource_type_iregex: Union[Unset, str] = UNSET,
    internal_resource_type_isnull: Union[Unset, bool] = UNSET,
    internal_resource_type_istartswith: Union[Unset, str] = UNSET,
    internal_resource_type_lt: Union[Unset, str] = UNSET,
    internal_resource_type_lte: Union[Unset, str] = UNSET,
    internal_resource_type_range: Union[Unset, list[str]] = UNSET,
    internal_resource_type_regex: Union[Unset, str] = UNSET,
    internal_resource_type_startswith: Union[Unset, str] = UNSET,
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
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    name_endswith: Union[Unset, str] = UNSET,
    name_gt: Union[Unset, str] = UNSET,
    name_gte: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    name_iendswith: Union[Unset, str] = UNSET,
    name_iexact: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    name_iregex: Union[Unset, str] = UNSET,
    name_isnull: Union[Unset, bool] = UNSET,
    name_istartswith: Union[Unset, str] = UNSET,
    name_lt: Union[Unset, str] = UNSET,
    name_lte: Union[Unset, str] = UNSET,
    name_range: Union[Unset, list[str]] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    name_startswith: Union[Unset, str] = UNSET,
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
    related_to: Union[Unset, int] = UNSET,
    related_to_gt: Union[Unset, int] = UNSET,
    related_to_gte: Union[Unset, int] = UNSET,
    related_to_in: Union[Unset, list[int]] = UNSET,
    related_to_isnull: Union[Unset, bool] = UNSET,
    related_to_lt: Union[Unset, int] = UNSET,
    related_to_lte: Union[Unset, int] = UNSET,
    related_to_ob_id: Union[Unset, int] = UNSET,
    related_to_ob_id_in: Union[Unset, list[int]] = UNSET,
    related_to_short_code: Union[Unset, str] = UNSET,
    related_to_short_code_in: Union[Unset, list[str]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedOnlineResourceReadList]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        application_profile (Union[Unset, OnlineresourcesListApplicationProfileFileFormat]):
        application_profile_contains (Union[Unset, str]):
        application_profile_endswith (Union[Unset, str]):
        application_profile_gt (Union[Unset, str]):
        application_profile_gte (Union[Unset, str]):
        application_profile_icontains (Union[Unset, str]):
        application_profile_iendswith (Union[Unset, str]):
        application_profile_iexact (Union[Unset, str]):
        application_profile_in (Union[Unset, list[str]]):
        application_profile_iregex (Union[Unset, str]):
        application_profile_isnull (Union[Unset, bool]):
        application_profile_istartswith (Union[Unset, str]):
        application_profile_lt (Union[Unset, str]):
        application_profile_lte (Union[Unset, str]):
        application_profile_range (Union[Unset, list[str]]):
        application_profile_regex (Union[Unset, str]):
        application_profile_startswith (Union[Unset, str]):
        description (Union[Unset, str]):
        description_contains (Union[Unset, str]):
        description_endswith (Union[Unset, str]):
        description_gt (Union[Unset, str]):
        description_gte (Union[Unset, str]):
        description_icontains (Union[Unset, str]):
        description_iendswith (Union[Unset, str]):
        description_iexact (Union[Unset, str]):
        description_in (Union[Unset, list[str]]):
        description_iregex (Union[Unset, str]):
        description_isnull (Union[Unset, bool]):
        description_istartswith (Union[Unset, str]):
        description_lt (Union[Unset, str]):
        description_lte (Union[Unset, str]):
        description_range (Union[Unset, list[str]]):
        description_regex (Union[Unset, str]):
        description_startswith (Union[Unset, str]):
        function (Union[Unset, OnlineresourcesListFunction]):
        function_contains (Union[Unset, str]):
        function_endswith (Union[Unset, str]):
        function_gt (Union[Unset, str]):
        function_gte (Union[Unset, str]):
        function_icontains (Union[Unset, str]):
        function_iendswith (Union[Unset, str]):
        function_iexact (Union[Unset, str]):
        function_in (Union[Unset, list[str]]):
        function_iregex (Union[Unset, str]):
        function_isnull (Union[Unset, bool]):
        function_istartswith (Union[Unset, str]):
        function_lt (Union[Unset, str]):
        function_lte (Union[Unset, str]):
        function_range (Union[Unset, list[str]]):
        function_regex (Union[Unset, str]):
        function_startswith (Union[Unset, str]):
        internal_resource_type (Union[Unset, OnlineresourcesListInternalResourceType]):
        internal_resource_type_contains (Union[Unset, str]):
        internal_resource_type_endswith (Union[Unset, str]):
        internal_resource_type_gt (Union[Unset, str]):
        internal_resource_type_gte (Union[Unset, str]):
        internal_resource_type_icontains (Union[Unset, str]):
        internal_resource_type_iendswith (Union[Unset, str]):
        internal_resource_type_iexact (Union[Unset, str]):
        internal_resource_type_in (Union[Unset, list[str]]):
        internal_resource_type_iregex (Union[Unset, str]):
        internal_resource_type_isnull (Union[Unset, bool]):
        internal_resource_type_istartswith (Union[Unset, str]):
        internal_resource_type_lt (Union[Unset, str]):
        internal_resource_type_lte (Union[Unset, str]):
        internal_resource_type_range (Union[Unset, list[str]]):
        internal_resource_type_regex (Union[Unset, str]):
        internal_resource_type_startswith (Union[Unset, str]):
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
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):
        name_endswith (Union[Unset, str]):
        name_gt (Union[Unset, str]):
        name_gte (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        name_iendswith (Union[Unset, str]):
        name_iexact (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        name_iregex (Union[Unset, str]):
        name_isnull (Union[Unset, bool]):
        name_istartswith (Union[Unset, str]):
        name_lt (Union[Unset, str]):
        name_lte (Union[Unset, str]):
        name_range (Union[Unset, list[str]]):
        name_regex (Union[Unset, str]):
        name_startswith (Union[Unset, str]):
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
        related_to (Union[Unset, int]):
        related_to_gt (Union[Unset, int]):
        related_to_gte (Union[Unset, int]):
        related_to_in (Union[Unset, list[int]]):
        related_to_isnull (Union[Unset, bool]):
        related_to_lt (Union[Unset, int]):
        related_to_lte (Union[Unset, int]):
        related_to_ob_id (Union[Unset, int]):
        related_to_ob_id_in (Union[Unset, list[int]]):
        related_to_short_code (Union[Unset, str]):
        related_to_short_code_in (Union[Unset, list[str]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):

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
