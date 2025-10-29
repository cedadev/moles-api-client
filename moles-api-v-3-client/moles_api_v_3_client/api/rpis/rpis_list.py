from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_responsible_party_info_read_list import PaginatedResponsiblePartyInfoReadList
from ...models.rpis_list_role import RpisListRole
from ...models.rpis_list_type import RpisListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
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
    party: Union[Unset, int] = UNSET,
    party_first_name: Union[Unset, str] = UNSET,
    party_first_name_in: Union[Unset, list[str]] = UNSET,
    party_gt: Union[Unset, int] = UNSET,
    party_gte: Union[Unset, int] = UNSET,
    party_in: Union[Unset, list[int]] = UNSET,
    party_isnull: Union[Unset, bool] = UNSET,
    party_last_name: Union[Unset, str] = UNSET,
    party_last_name_in: Union[Unset, list[str]] = UNSET,
    party_lt: Union[Unset, int] = UNSET,
    party_lte: Union[Unset, int] = UNSET,
    party_ob_id: Union[Unset, int] = UNSET,
    party_ob_id_in: Union[Unset, list[int]] = UNSET,
    party_party_type: Union[Unset, RpisListType] = UNSET,
    party_party_type_in: Union[Unset, list[str]] = UNSET,
    priority: Union[Unset, int] = UNSET,
    priority_contained_by: Union[Unset, int] = UNSET,
    priority_contains: Union[Unset, int] = UNSET,
    priority_endswith: Union[Unset, int] = UNSET,
    priority_gt: Union[Unset, int] = UNSET,
    priority_gte: Union[Unset, int] = UNSET,
    priority_icontains: Union[Unset, int] = UNSET,
    priority_iendswith: Union[Unset, int] = UNSET,
    priority_iexact: Union[Unset, int] = UNSET,
    priority_in: Union[Unset, list[int]] = UNSET,
    priority_iregex: Union[Unset, int] = UNSET,
    priority_isnull: Union[Unset, bool] = UNSET,
    priority_istartswith: Union[Unset, int] = UNSET,
    priority_lt: Union[Unset, int] = UNSET,
    priority_lte: Union[Unset, int] = UNSET,
    priority_range: Union[Unset, list[int]] = UNSET,
    priority_regex: Union[Unset, int] = UNSET,
    priority_startswith: Union[Unset, int] = UNSET,
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
    role: Union[Unset, RpisListRole] = UNSET,
    role_contains: Union[Unset, str] = UNSET,
    role_endswith: Union[Unset, str] = UNSET,
    role_gt: Union[Unset, str] = UNSET,
    role_gte: Union[Unset, str] = UNSET,
    role_icontains: Union[Unset, str] = UNSET,
    role_iendswith: Union[Unset, str] = UNSET,
    role_iexact: Union[Unset, str] = UNSET,
    role_in: Union[Unset, list[str]] = UNSET,
    role_iregex: Union[Unset, str] = UNSET,
    role_isnull: Union[Unset, bool] = UNSET,
    role_istartswith: Union[Unset, str] = UNSET,
    role_lt: Union[Unset, str] = UNSET,
    role_lte: Union[Unset, str] = UNSET,
    role_range: Union[Unset, list[str]] = UNSET,
    role_regex: Union[Unset, str] = UNSET,
    role_startswith: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    params["party"] = party

    params["party__firstName"] = party_first_name

    json_party_first_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(party_first_name_in, Unset):
        json_party_first_name_in = ",".join(map(str, party_first_name_in))

    params["party__firstName__in"] = json_party_first_name_in

    params["party__gt"] = party_gt

    params["party__gte"] = party_gte

    json_party_in: Union[Unset, list[int]] = UNSET
    if not isinstance(party_in, Unset):
        json_party_in = ",".join(map(str, party_in))

    params["party__in"] = json_party_in

    params["party__isnull"] = party_isnull

    params["party__lastName"] = party_last_name

    json_party_last_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(party_last_name_in, Unset):
        json_party_last_name_in = ",".join(map(str, party_last_name_in))

    params["party__lastName__in"] = json_party_last_name_in

    params["party__lt"] = party_lt

    params["party__lte"] = party_lte

    params["party__ob_id"] = party_ob_id

    json_party_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(party_ob_id_in, Unset):
        json_party_ob_id_in = ",".join(map(str, party_ob_id_in))

    params["party__ob_id__in"] = json_party_ob_id_in

    json_party_party_type: Union[Unset, str] = UNSET
    if not isinstance(party_party_type, Unset):
        json_party_party_type = party_party_type.value

    params["party__partyType"] = json_party_party_type

    json_party_party_type_in: Union[Unset, list[str]] = UNSET
    if not isinstance(party_party_type_in, Unset):
        json_party_party_type_in = ",".join(map(str, party_party_type_in))

    params["party__partyType__in"] = json_party_party_type_in

    params["priority"] = priority

    params["priority__contained_by"] = priority_contained_by

    params["priority__contains"] = priority_contains

    params["priority__endswith"] = priority_endswith

    params["priority__gt"] = priority_gt

    params["priority__gte"] = priority_gte

    params["priority__icontains"] = priority_icontains

    params["priority__iendswith"] = priority_iendswith

    params["priority__iexact"] = priority_iexact

    json_priority_in: Union[Unset, list[int]] = UNSET
    if not isinstance(priority_in, Unset):
        json_priority_in = ",".join(map(str, priority_in))

    params["priority__in"] = json_priority_in

    params["priority__iregex"] = priority_iregex

    params["priority__isnull"] = priority_isnull

    params["priority__istartswith"] = priority_istartswith

    params["priority__lt"] = priority_lt

    params["priority__lte"] = priority_lte

    json_priority_range: Union[Unset, list[int]] = UNSET
    if not isinstance(priority_range, Unset):
        json_priority_range = ",".join(map(str, priority_range))

    params["priority__range"] = json_priority_range

    params["priority__regex"] = priority_regex

    params["priority__startswith"] = priority_startswith

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

    json_role: Union[Unset, str] = UNSET
    if not isinstance(role, Unset):
        json_role = role.value

    params["role"] = json_role

    params["role__contains"] = role_contains

    params["role__endswith"] = role_endswith

    params["role__gt"] = role_gt

    params["role__gte"] = role_gte

    params["role__icontains"] = role_icontains

    params["role__iendswith"] = role_iendswith

    params["role__iexact"] = role_iexact

    json_role_in: Union[Unset, list[str]] = UNSET
    if not isinstance(role_in, Unset):
        json_role_in = ",".join(map(str, role_in))

    params["role__in"] = json_role_in

    params["role__iregex"] = role_iregex

    params["role__isnull"] = role_isnull

    params["role__istartswith"] = role_istartswith

    params["role__lt"] = role_lt

    params["role__lte"] = role_lte

    json_role_range: Union[Unset, list[str]] = UNSET
    if not isinstance(role_range, Unset):
        json_role_range = ",".join(map(str, role_range))

    params["role__range"] = json_role_range

    params["role__regex"] = role_regex

    params["role__startswith"] = role_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/rpis/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedResponsiblePartyInfoReadList]:
    if response.status_code == 200:
        response_200 = PaginatedResponsiblePartyInfoReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedResponsiblePartyInfoReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
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
    party: Union[Unset, int] = UNSET,
    party_first_name: Union[Unset, str] = UNSET,
    party_first_name_in: Union[Unset, list[str]] = UNSET,
    party_gt: Union[Unset, int] = UNSET,
    party_gte: Union[Unset, int] = UNSET,
    party_in: Union[Unset, list[int]] = UNSET,
    party_isnull: Union[Unset, bool] = UNSET,
    party_last_name: Union[Unset, str] = UNSET,
    party_last_name_in: Union[Unset, list[str]] = UNSET,
    party_lt: Union[Unset, int] = UNSET,
    party_lte: Union[Unset, int] = UNSET,
    party_ob_id: Union[Unset, int] = UNSET,
    party_ob_id_in: Union[Unset, list[int]] = UNSET,
    party_party_type: Union[Unset, RpisListType] = UNSET,
    party_party_type_in: Union[Unset, list[str]] = UNSET,
    priority: Union[Unset, int] = UNSET,
    priority_contained_by: Union[Unset, int] = UNSET,
    priority_contains: Union[Unset, int] = UNSET,
    priority_endswith: Union[Unset, int] = UNSET,
    priority_gt: Union[Unset, int] = UNSET,
    priority_gte: Union[Unset, int] = UNSET,
    priority_icontains: Union[Unset, int] = UNSET,
    priority_iendswith: Union[Unset, int] = UNSET,
    priority_iexact: Union[Unset, int] = UNSET,
    priority_in: Union[Unset, list[int]] = UNSET,
    priority_iregex: Union[Unset, int] = UNSET,
    priority_isnull: Union[Unset, bool] = UNSET,
    priority_istartswith: Union[Unset, int] = UNSET,
    priority_lt: Union[Unset, int] = UNSET,
    priority_lte: Union[Unset, int] = UNSET,
    priority_range: Union[Unset, list[int]] = UNSET,
    priority_regex: Union[Unset, int] = UNSET,
    priority_startswith: Union[Unset, int] = UNSET,
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
    role: Union[Unset, RpisListRole] = UNSET,
    role_contains: Union[Unset, str] = UNSET,
    role_endswith: Union[Unset, str] = UNSET,
    role_gt: Union[Unset, str] = UNSET,
    role_gte: Union[Unset, str] = UNSET,
    role_icontains: Union[Unset, str] = UNSET,
    role_iendswith: Union[Unset, str] = UNSET,
    role_iexact: Union[Unset, str] = UNSET,
    role_in: Union[Unset, list[str]] = UNSET,
    role_iregex: Union[Unset, str] = UNSET,
    role_isnull: Union[Unset, bool] = UNSET,
    role_istartswith: Union[Unset, str] = UNSET,
    role_lt: Union[Unset, str] = UNSET,
    role_lte: Union[Unset, str] = UNSET,
    role_range: Union[Unset, list[str]] = UNSET,
    role_regex: Union[Unset, str] = UNSET,
    role_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedResponsiblePartyInfoReadList]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        limit (Union[Unset, int]):
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
        party (Union[Unset, int]):
        party_first_name (Union[Unset, str]):
        party_first_name_in (Union[Unset, list[str]]):
        party_gt (Union[Unset, int]):
        party_gte (Union[Unset, int]):
        party_in (Union[Unset, list[int]]):
        party_isnull (Union[Unset, bool]):
        party_last_name (Union[Unset, str]):
        party_last_name_in (Union[Unset, list[str]]):
        party_lt (Union[Unset, int]):
        party_lte (Union[Unset, int]):
        party_ob_id (Union[Unset, int]):
        party_ob_id_in (Union[Unset, list[int]]):
        party_party_type (Union[Unset, RpisListType]):
        party_party_type_in (Union[Unset, list[str]]):
        priority (Union[Unset, int]):
        priority_contained_by (Union[Unset, int]):
        priority_contains (Union[Unset, int]):
        priority_endswith (Union[Unset, int]):
        priority_gt (Union[Unset, int]):
        priority_gte (Union[Unset, int]):
        priority_icontains (Union[Unset, int]):
        priority_iendswith (Union[Unset, int]):
        priority_iexact (Union[Unset, int]):
        priority_in (Union[Unset, list[int]]):
        priority_iregex (Union[Unset, int]):
        priority_isnull (Union[Unset, bool]):
        priority_istartswith (Union[Unset, int]):
        priority_lt (Union[Unset, int]):
        priority_lte (Union[Unset, int]):
        priority_range (Union[Unset, list[int]]):
        priority_regex (Union[Unset, int]):
        priority_startswith (Union[Unset, int]):
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
        role (Union[Unset, RpisListRole]):
        role_contains (Union[Unset, str]):
        role_endswith (Union[Unset, str]):
        role_gt (Union[Unset, str]):
        role_gte (Union[Unset, str]):
        role_icontains (Union[Unset, str]):
        role_iendswith (Union[Unset, str]):
        role_iexact (Union[Unset, str]):
        role_in (Union[Unset, list[str]]):
        role_iregex (Union[Unset, str]):
        role_isnull (Union[Unset, bool]):
        role_istartswith (Union[Unset, str]):
        role_lt (Union[Unset, str]):
        role_lte (Union[Unset, str]):
        role_range (Union[Unset, list[str]]):
        role_regex (Union[Unset, str]):
        role_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponsiblePartyInfoReadList]
    """

    kwargs = _get_kwargs(
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
        party=party,
        party_first_name=party_first_name,
        party_first_name_in=party_first_name_in,
        party_gt=party_gt,
        party_gte=party_gte,
        party_in=party_in,
        party_isnull=party_isnull,
        party_last_name=party_last_name,
        party_last_name_in=party_last_name_in,
        party_lt=party_lt,
        party_lte=party_lte,
        party_ob_id=party_ob_id,
        party_ob_id_in=party_ob_id_in,
        party_party_type=party_party_type,
        party_party_type_in=party_party_type_in,
        priority=priority,
        priority_contained_by=priority_contained_by,
        priority_contains=priority_contains,
        priority_endswith=priority_endswith,
        priority_gt=priority_gt,
        priority_gte=priority_gte,
        priority_icontains=priority_icontains,
        priority_iendswith=priority_iendswith,
        priority_iexact=priority_iexact,
        priority_in=priority_in,
        priority_iregex=priority_iregex,
        priority_isnull=priority_isnull,
        priority_istartswith=priority_istartswith,
        priority_lt=priority_lt,
        priority_lte=priority_lte,
        priority_range=priority_range,
        priority_regex=priority_regex,
        priority_startswith=priority_startswith,
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
        role=role,
        role_contains=role_contains,
        role_endswith=role_endswith,
        role_gt=role_gt,
        role_gte=role_gte,
        role_icontains=role_icontains,
        role_iendswith=role_iendswith,
        role_iexact=role_iexact,
        role_in=role_in,
        role_iregex=role_iregex,
        role_isnull=role_isnull,
        role_istartswith=role_istartswith,
        role_lt=role_lt,
        role_lte=role_lte,
        role_range=role_range,
        role_regex=role_regex,
        role_startswith=role_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
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
    party: Union[Unset, int] = UNSET,
    party_first_name: Union[Unset, str] = UNSET,
    party_first_name_in: Union[Unset, list[str]] = UNSET,
    party_gt: Union[Unset, int] = UNSET,
    party_gte: Union[Unset, int] = UNSET,
    party_in: Union[Unset, list[int]] = UNSET,
    party_isnull: Union[Unset, bool] = UNSET,
    party_last_name: Union[Unset, str] = UNSET,
    party_last_name_in: Union[Unset, list[str]] = UNSET,
    party_lt: Union[Unset, int] = UNSET,
    party_lte: Union[Unset, int] = UNSET,
    party_ob_id: Union[Unset, int] = UNSET,
    party_ob_id_in: Union[Unset, list[int]] = UNSET,
    party_party_type: Union[Unset, RpisListType] = UNSET,
    party_party_type_in: Union[Unset, list[str]] = UNSET,
    priority: Union[Unset, int] = UNSET,
    priority_contained_by: Union[Unset, int] = UNSET,
    priority_contains: Union[Unset, int] = UNSET,
    priority_endswith: Union[Unset, int] = UNSET,
    priority_gt: Union[Unset, int] = UNSET,
    priority_gte: Union[Unset, int] = UNSET,
    priority_icontains: Union[Unset, int] = UNSET,
    priority_iendswith: Union[Unset, int] = UNSET,
    priority_iexact: Union[Unset, int] = UNSET,
    priority_in: Union[Unset, list[int]] = UNSET,
    priority_iregex: Union[Unset, int] = UNSET,
    priority_isnull: Union[Unset, bool] = UNSET,
    priority_istartswith: Union[Unset, int] = UNSET,
    priority_lt: Union[Unset, int] = UNSET,
    priority_lte: Union[Unset, int] = UNSET,
    priority_range: Union[Unset, list[int]] = UNSET,
    priority_regex: Union[Unset, int] = UNSET,
    priority_startswith: Union[Unset, int] = UNSET,
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
    role: Union[Unset, RpisListRole] = UNSET,
    role_contains: Union[Unset, str] = UNSET,
    role_endswith: Union[Unset, str] = UNSET,
    role_gt: Union[Unset, str] = UNSET,
    role_gte: Union[Unset, str] = UNSET,
    role_icontains: Union[Unset, str] = UNSET,
    role_iendswith: Union[Unset, str] = UNSET,
    role_iexact: Union[Unset, str] = UNSET,
    role_in: Union[Unset, list[str]] = UNSET,
    role_iregex: Union[Unset, str] = UNSET,
    role_isnull: Union[Unset, bool] = UNSET,
    role_istartswith: Union[Unset, str] = UNSET,
    role_lt: Union[Unset, str] = UNSET,
    role_lte: Union[Unset, str] = UNSET,
    role_range: Union[Unset, list[str]] = UNSET,
    role_regex: Union[Unset, str] = UNSET,
    role_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedResponsiblePartyInfoReadList]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        limit (Union[Unset, int]):
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
        party (Union[Unset, int]):
        party_first_name (Union[Unset, str]):
        party_first_name_in (Union[Unset, list[str]]):
        party_gt (Union[Unset, int]):
        party_gte (Union[Unset, int]):
        party_in (Union[Unset, list[int]]):
        party_isnull (Union[Unset, bool]):
        party_last_name (Union[Unset, str]):
        party_last_name_in (Union[Unset, list[str]]):
        party_lt (Union[Unset, int]):
        party_lte (Union[Unset, int]):
        party_ob_id (Union[Unset, int]):
        party_ob_id_in (Union[Unset, list[int]]):
        party_party_type (Union[Unset, RpisListType]):
        party_party_type_in (Union[Unset, list[str]]):
        priority (Union[Unset, int]):
        priority_contained_by (Union[Unset, int]):
        priority_contains (Union[Unset, int]):
        priority_endswith (Union[Unset, int]):
        priority_gt (Union[Unset, int]):
        priority_gte (Union[Unset, int]):
        priority_icontains (Union[Unset, int]):
        priority_iendswith (Union[Unset, int]):
        priority_iexact (Union[Unset, int]):
        priority_in (Union[Unset, list[int]]):
        priority_iregex (Union[Unset, int]):
        priority_isnull (Union[Unset, bool]):
        priority_istartswith (Union[Unset, int]):
        priority_lt (Union[Unset, int]):
        priority_lte (Union[Unset, int]):
        priority_range (Union[Unset, list[int]]):
        priority_regex (Union[Unset, int]):
        priority_startswith (Union[Unset, int]):
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
        role (Union[Unset, RpisListRole]):
        role_contains (Union[Unset, str]):
        role_endswith (Union[Unset, str]):
        role_gt (Union[Unset, str]):
        role_gte (Union[Unset, str]):
        role_icontains (Union[Unset, str]):
        role_iendswith (Union[Unset, str]):
        role_iexact (Union[Unset, str]):
        role_in (Union[Unset, list[str]]):
        role_iregex (Union[Unset, str]):
        role_isnull (Union[Unset, bool]):
        role_istartswith (Union[Unset, str]):
        role_lt (Union[Unset, str]):
        role_lte (Union[Unset, str]):
        role_range (Union[Unset, list[str]]):
        role_regex (Union[Unset, str]):
        role_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponsiblePartyInfoReadList
    """

    return sync_detailed(
        client=client,
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
        party=party,
        party_first_name=party_first_name,
        party_first_name_in=party_first_name_in,
        party_gt=party_gt,
        party_gte=party_gte,
        party_in=party_in,
        party_isnull=party_isnull,
        party_last_name=party_last_name,
        party_last_name_in=party_last_name_in,
        party_lt=party_lt,
        party_lte=party_lte,
        party_ob_id=party_ob_id,
        party_ob_id_in=party_ob_id_in,
        party_party_type=party_party_type,
        party_party_type_in=party_party_type_in,
        priority=priority,
        priority_contained_by=priority_contained_by,
        priority_contains=priority_contains,
        priority_endswith=priority_endswith,
        priority_gt=priority_gt,
        priority_gte=priority_gte,
        priority_icontains=priority_icontains,
        priority_iendswith=priority_iendswith,
        priority_iexact=priority_iexact,
        priority_in=priority_in,
        priority_iregex=priority_iregex,
        priority_isnull=priority_isnull,
        priority_istartswith=priority_istartswith,
        priority_lt=priority_lt,
        priority_lte=priority_lte,
        priority_range=priority_range,
        priority_regex=priority_regex,
        priority_startswith=priority_startswith,
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
        role=role,
        role_contains=role_contains,
        role_endswith=role_endswith,
        role_gt=role_gt,
        role_gte=role_gte,
        role_icontains=role_icontains,
        role_iendswith=role_iendswith,
        role_iexact=role_iexact,
        role_in=role_in,
        role_iregex=role_iregex,
        role_isnull=role_isnull,
        role_istartswith=role_istartswith,
        role_lt=role_lt,
        role_lte=role_lte,
        role_range=role_range,
        role_regex=role_regex,
        role_startswith=role_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
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
    party: Union[Unset, int] = UNSET,
    party_first_name: Union[Unset, str] = UNSET,
    party_first_name_in: Union[Unset, list[str]] = UNSET,
    party_gt: Union[Unset, int] = UNSET,
    party_gte: Union[Unset, int] = UNSET,
    party_in: Union[Unset, list[int]] = UNSET,
    party_isnull: Union[Unset, bool] = UNSET,
    party_last_name: Union[Unset, str] = UNSET,
    party_last_name_in: Union[Unset, list[str]] = UNSET,
    party_lt: Union[Unset, int] = UNSET,
    party_lte: Union[Unset, int] = UNSET,
    party_ob_id: Union[Unset, int] = UNSET,
    party_ob_id_in: Union[Unset, list[int]] = UNSET,
    party_party_type: Union[Unset, RpisListType] = UNSET,
    party_party_type_in: Union[Unset, list[str]] = UNSET,
    priority: Union[Unset, int] = UNSET,
    priority_contained_by: Union[Unset, int] = UNSET,
    priority_contains: Union[Unset, int] = UNSET,
    priority_endswith: Union[Unset, int] = UNSET,
    priority_gt: Union[Unset, int] = UNSET,
    priority_gte: Union[Unset, int] = UNSET,
    priority_icontains: Union[Unset, int] = UNSET,
    priority_iendswith: Union[Unset, int] = UNSET,
    priority_iexact: Union[Unset, int] = UNSET,
    priority_in: Union[Unset, list[int]] = UNSET,
    priority_iregex: Union[Unset, int] = UNSET,
    priority_isnull: Union[Unset, bool] = UNSET,
    priority_istartswith: Union[Unset, int] = UNSET,
    priority_lt: Union[Unset, int] = UNSET,
    priority_lte: Union[Unset, int] = UNSET,
    priority_range: Union[Unset, list[int]] = UNSET,
    priority_regex: Union[Unset, int] = UNSET,
    priority_startswith: Union[Unset, int] = UNSET,
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
    role: Union[Unset, RpisListRole] = UNSET,
    role_contains: Union[Unset, str] = UNSET,
    role_endswith: Union[Unset, str] = UNSET,
    role_gt: Union[Unset, str] = UNSET,
    role_gte: Union[Unset, str] = UNSET,
    role_icontains: Union[Unset, str] = UNSET,
    role_iendswith: Union[Unset, str] = UNSET,
    role_iexact: Union[Unset, str] = UNSET,
    role_in: Union[Unset, list[str]] = UNSET,
    role_iregex: Union[Unset, str] = UNSET,
    role_isnull: Union[Unset, bool] = UNSET,
    role_istartswith: Union[Unset, str] = UNSET,
    role_lt: Union[Unset, str] = UNSET,
    role_lte: Union[Unset, str] = UNSET,
    role_range: Union[Unset, list[str]] = UNSET,
    role_regex: Union[Unset, str] = UNSET,
    role_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedResponsiblePartyInfoReadList]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        limit (Union[Unset, int]):
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
        party (Union[Unset, int]):
        party_first_name (Union[Unset, str]):
        party_first_name_in (Union[Unset, list[str]]):
        party_gt (Union[Unset, int]):
        party_gte (Union[Unset, int]):
        party_in (Union[Unset, list[int]]):
        party_isnull (Union[Unset, bool]):
        party_last_name (Union[Unset, str]):
        party_last_name_in (Union[Unset, list[str]]):
        party_lt (Union[Unset, int]):
        party_lte (Union[Unset, int]):
        party_ob_id (Union[Unset, int]):
        party_ob_id_in (Union[Unset, list[int]]):
        party_party_type (Union[Unset, RpisListType]):
        party_party_type_in (Union[Unset, list[str]]):
        priority (Union[Unset, int]):
        priority_contained_by (Union[Unset, int]):
        priority_contains (Union[Unset, int]):
        priority_endswith (Union[Unset, int]):
        priority_gt (Union[Unset, int]):
        priority_gte (Union[Unset, int]):
        priority_icontains (Union[Unset, int]):
        priority_iendswith (Union[Unset, int]):
        priority_iexact (Union[Unset, int]):
        priority_in (Union[Unset, list[int]]):
        priority_iregex (Union[Unset, int]):
        priority_isnull (Union[Unset, bool]):
        priority_istartswith (Union[Unset, int]):
        priority_lt (Union[Unset, int]):
        priority_lte (Union[Unset, int]):
        priority_range (Union[Unset, list[int]]):
        priority_regex (Union[Unset, int]):
        priority_startswith (Union[Unset, int]):
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
        role (Union[Unset, RpisListRole]):
        role_contains (Union[Unset, str]):
        role_endswith (Union[Unset, str]):
        role_gt (Union[Unset, str]):
        role_gte (Union[Unset, str]):
        role_icontains (Union[Unset, str]):
        role_iendswith (Union[Unset, str]):
        role_iexact (Union[Unset, str]):
        role_in (Union[Unset, list[str]]):
        role_iregex (Union[Unset, str]):
        role_isnull (Union[Unset, bool]):
        role_istartswith (Union[Unset, str]):
        role_lt (Union[Unset, str]):
        role_lte (Union[Unset, str]):
        role_range (Union[Unset, list[str]]):
        role_regex (Union[Unset, str]):
        role_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResponsiblePartyInfoReadList]
    """

    kwargs = _get_kwargs(
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
        party=party,
        party_first_name=party_first_name,
        party_first_name_in=party_first_name_in,
        party_gt=party_gt,
        party_gte=party_gte,
        party_in=party_in,
        party_isnull=party_isnull,
        party_last_name=party_last_name,
        party_last_name_in=party_last_name_in,
        party_lt=party_lt,
        party_lte=party_lte,
        party_ob_id=party_ob_id,
        party_ob_id_in=party_ob_id_in,
        party_party_type=party_party_type,
        party_party_type_in=party_party_type_in,
        priority=priority,
        priority_contained_by=priority_contained_by,
        priority_contains=priority_contains,
        priority_endswith=priority_endswith,
        priority_gt=priority_gt,
        priority_gte=priority_gte,
        priority_icontains=priority_icontains,
        priority_iendswith=priority_iendswith,
        priority_iexact=priority_iexact,
        priority_in=priority_in,
        priority_iregex=priority_iregex,
        priority_isnull=priority_isnull,
        priority_istartswith=priority_istartswith,
        priority_lt=priority_lt,
        priority_lte=priority_lte,
        priority_range=priority_range,
        priority_regex=priority_regex,
        priority_startswith=priority_startswith,
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
        role=role,
        role_contains=role_contains,
        role_endswith=role_endswith,
        role_gt=role_gt,
        role_gte=role_gte,
        role_icontains=role_icontains,
        role_iendswith=role_iendswith,
        role_iexact=role_iexact,
        role_in=role_in,
        role_iregex=role_iregex,
        role_isnull=role_isnull,
        role_istartswith=role_istartswith,
        role_lt=role_lt,
        role_lte=role_lte,
        role_range=role_range,
        role_regex=role_regex,
        role_startswith=role_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
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
    party: Union[Unset, int] = UNSET,
    party_first_name: Union[Unset, str] = UNSET,
    party_first_name_in: Union[Unset, list[str]] = UNSET,
    party_gt: Union[Unset, int] = UNSET,
    party_gte: Union[Unset, int] = UNSET,
    party_in: Union[Unset, list[int]] = UNSET,
    party_isnull: Union[Unset, bool] = UNSET,
    party_last_name: Union[Unset, str] = UNSET,
    party_last_name_in: Union[Unset, list[str]] = UNSET,
    party_lt: Union[Unset, int] = UNSET,
    party_lte: Union[Unset, int] = UNSET,
    party_ob_id: Union[Unset, int] = UNSET,
    party_ob_id_in: Union[Unset, list[int]] = UNSET,
    party_party_type: Union[Unset, RpisListType] = UNSET,
    party_party_type_in: Union[Unset, list[str]] = UNSET,
    priority: Union[Unset, int] = UNSET,
    priority_contained_by: Union[Unset, int] = UNSET,
    priority_contains: Union[Unset, int] = UNSET,
    priority_endswith: Union[Unset, int] = UNSET,
    priority_gt: Union[Unset, int] = UNSET,
    priority_gte: Union[Unset, int] = UNSET,
    priority_icontains: Union[Unset, int] = UNSET,
    priority_iendswith: Union[Unset, int] = UNSET,
    priority_iexact: Union[Unset, int] = UNSET,
    priority_in: Union[Unset, list[int]] = UNSET,
    priority_iregex: Union[Unset, int] = UNSET,
    priority_isnull: Union[Unset, bool] = UNSET,
    priority_istartswith: Union[Unset, int] = UNSET,
    priority_lt: Union[Unset, int] = UNSET,
    priority_lte: Union[Unset, int] = UNSET,
    priority_range: Union[Unset, list[int]] = UNSET,
    priority_regex: Union[Unset, int] = UNSET,
    priority_startswith: Union[Unset, int] = UNSET,
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
    role: Union[Unset, RpisListRole] = UNSET,
    role_contains: Union[Unset, str] = UNSET,
    role_endswith: Union[Unset, str] = UNSET,
    role_gt: Union[Unset, str] = UNSET,
    role_gte: Union[Unset, str] = UNSET,
    role_icontains: Union[Unset, str] = UNSET,
    role_iendswith: Union[Unset, str] = UNSET,
    role_iexact: Union[Unset, str] = UNSET,
    role_in: Union[Unset, list[str]] = UNSET,
    role_iregex: Union[Unset, str] = UNSET,
    role_isnull: Union[Unset, bool] = UNSET,
    role_istartswith: Union[Unset, str] = UNSET,
    role_lt: Union[Unset, str] = UNSET,
    role_lte: Union[Unset, str] = UNSET,
    role_range: Union[Unset, list[str]] = UNSET,
    role_regex: Union[Unset, str] = UNSET,
    role_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedResponsiblePartyInfoReadList]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        limit (Union[Unset, int]):
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
        party (Union[Unset, int]):
        party_first_name (Union[Unset, str]):
        party_first_name_in (Union[Unset, list[str]]):
        party_gt (Union[Unset, int]):
        party_gte (Union[Unset, int]):
        party_in (Union[Unset, list[int]]):
        party_isnull (Union[Unset, bool]):
        party_last_name (Union[Unset, str]):
        party_last_name_in (Union[Unset, list[str]]):
        party_lt (Union[Unset, int]):
        party_lte (Union[Unset, int]):
        party_ob_id (Union[Unset, int]):
        party_ob_id_in (Union[Unset, list[int]]):
        party_party_type (Union[Unset, RpisListType]):
        party_party_type_in (Union[Unset, list[str]]):
        priority (Union[Unset, int]):
        priority_contained_by (Union[Unset, int]):
        priority_contains (Union[Unset, int]):
        priority_endswith (Union[Unset, int]):
        priority_gt (Union[Unset, int]):
        priority_gte (Union[Unset, int]):
        priority_icontains (Union[Unset, int]):
        priority_iendswith (Union[Unset, int]):
        priority_iexact (Union[Unset, int]):
        priority_in (Union[Unset, list[int]]):
        priority_iregex (Union[Unset, int]):
        priority_isnull (Union[Unset, bool]):
        priority_istartswith (Union[Unset, int]):
        priority_lt (Union[Unset, int]):
        priority_lte (Union[Unset, int]):
        priority_range (Union[Unset, list[int]]):
        priority_regex (Union[Unset, int]):
        priority_startswith (Union[Unset, int]):
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
        role (Union[Unset, RpisListRole]):
        role_contains (Union[Unset, str]):
        role_endswith (Union[Unset, str]):
        role_gt (Union[Unset, str]):
        role_gte (Union[Unset, str]):
        role_icontains (Union[Unset, str]):
        role_iendswith (Union[Unset, str]):
        role_iexact (Union[Unset, str]):
        role_in (Union[Unset, list[str]]):
        role_iregex (Union[Unset, str]):
        role_isnull (Union[Unset, bool]):
        role_istartswith (Union[Unset, str]):
        role_lt (Union[Unset, str]):
        role_lte (Union[Unset, str]):
        role_range (Union[Unset, list[str]]):
        role_regex (Union[Unset, str]):
        role_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResponsiblePartyInfoReadList
    """

    return (
        await asyncio_detailed(
            client=client,
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
            party=party,
            party_first_name=party_first_name,
            party_first_name_in=party_first_name_in,
            party_gt=party_gt,
            party_gte=party_gte,
            party_in=party_in,
            party_isnull=party_isnull,
            party_last_name=party_last_name,
            party_last_name_in=party_last_name_in,
            party_lt=party_lt,
            party_lte=party_lte,
            party_ob_id=party_ob_id,
            party_ob_id_in=party_ob_id_in,
            party_party_type=party_party_type,
            party_party_type_in=party_party_type_in,
            priority=priority,
            priority_contained_by=priority_contained_by,
            priority_contains=priority_contains,
            priority_endswith=priority_endswith,
            priority_gt=priority_gt,
            priority_gte=priority_gte,
            priority_icontains=priority_icontains,
            priority_iendswith=priority_iendswith,
            priority_iexact=priority_iexact,
            priority_in=priority_in,
            priority_iregex=priority_iregex,
            priority_isnull=priority_isnull,
            priority_istartswith=priority_istartswith,
            priority_lt=priority_lt,
            priority_lte=priority_lte,
            priority_range=priority_range,
            priority_regex=priority_regex,
            priority_startswith=priority_startswith,
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
            role=role,
            role_contains=role_contains,
            role_endswith=role_endswith,
            role_gt=role_gt,
            role_gte=role_gte,
            role_icontains=role_icontains,
            role_iendswith=role_iendswith,
            role_iexact=role_iexact,
            role_in=role_in,
            role_iregex=role_iregex,
            role_isnull=role_isnull,
            role_istartswith=role_istartswith,
            role_lt=role_lt,
            role_lte=role_lte,
            role_range=role_range,
            role_regex=role_regex,
            role_startswith=role_startswith,
        )
    ).parsed
