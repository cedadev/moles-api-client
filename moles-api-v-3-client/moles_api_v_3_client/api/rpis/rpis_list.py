from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_responsible_party_info_read_list import PaginatedResponsiblePartyInfoReadList
from ...models.rpis_list_role import RpisListRole
from ...models.rpis_list_type import RpisListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = UNSET,
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
    party: int | Unset = UNSET,
    party_first_name: str | Unset = UNSET,
    party_first_name_in: list[str] | Unset = UNSET,
    party_in: list[int] | Unset = UNSET,
    party_isnull: bool | Unset = UNSET,
    party_last_name: str | Unset = UNSET,
    party_last_name_in: list[str] | Unset = UNSET,
    party_ob_id: int | Unset = UNSET,
    party_ob_id_in: list[int] | Unset = UNSET,
    party_party_type: RpisListType | Unset = UNSET,
    party_party_type_in: list[str] | Unset = UNSET,
    priority: int | Unset = UNSET,
    priority_contained_by: int | Unset = UNSET,
    priority_contains: int | Unset = UNSET,
    priority_endswith: int | Unset = UNSET,
    priority_gt: int | Unset = UNSET,
    priority_gte: int | Unset = UNSET,
    priority_icontains: int | Unset = UNSET,
    priority_iendswith: int | Unset = UNSET,
    priority_iexact: int | Unset = UNSET,
    priority_in: list[int] | Unset = UNSET,
    priority_iregex: int | Unset = UNSET,
    priority_isnull: bool | Unset = UNSET,
    priority_istartswith: int | Unset = UNSET,
    priority_lt: int | Unset = UNSET,
    priority_lte: int | Unset = UNSET,
    priority_range: list[int] | Unset = UNSET,
    priority_regex: int | Unset = UNSET,
    priority_startswith: int | Unset = UNSET,
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
    role: RpisListRole | Unset = UNSET,
    role_contains: str | Unset = UNSET,
    role_endswith: str | Unset = UNSET,
    role_gt: str | Unset = UNSET,
    role_gte: str | Unset = UNSET,
    role_icontains: str | Unset = UNSET,
    role_iendswith: str | Unset = UNSET,
    role_iexact: str | Unset = UNSET,
    role_in: list[str] | Unset = UNSET,
    role_iregex: str | Unset = UNSET,
    role_isnull: bool | Unset = UNSET,
    role_istartswith: str | Unset = UNSET,
    role_lt: str | Unset = UNSET,
    role_lte: str | Unset = UNSET,
    role_range: list[str] | Unset = UNSET,
    role_regex: str | Unset = UNSET,
    role_startswith: str | Unset = UNSET,
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

    params["ordering"] = ordering

    params["party"] = party

    params["party__firstName"] = party_first_name

    json_party_first_name_in: list[str] | Unset = UNSET
    if not isinstance(party_first_name_in, Unset):
        json_party_first_name_in = party_first_name_in

    params["party__firstName__in"] = json_party_first_name_in

    json_party_in: list[int] | Unset = UNSET
    if not isinstance(party_in, Unset):
        json_party_in = party_in

    params["party__in"] = json_party_in

    params["party__isnull"] = party_isnull

    params["party__lastName"] = party_last_name

    json_party_last_name_in: list[str] | Unset = UNSET
    if not isinstance(party_last_name_in, Unset):
        json_party_last_name_in = party_last_name_in

    params["party__lastName__in"] = json_party_last_name_in

    params["party__ob_id"] = party_ob_id

    json_party_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(party_ob_id_in, Unset):
        json_party_ob_id_in = party_ob_id_in

    params["party__ob_id__in"] = json_party_ob_id_in

    json_party_party_type: str | Unset = UNSET
    if not isinstance(party_party_type, Unset):
        json_party_party_type = party_party_type.value

    params["party__partyType"] = json_party_party_type

    json_party_party_type_in: list[str] | Unset = UNSET
    if not isinstance(party_party_type_in, Unset):
        json_party_party_type_in = party_party_type_in

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

    json_priority_in: list[int] | Unset = UNSET
    if not isinstance(priority_in, Unset):
        json_priority_in = priority_in

    params["priority__in"] = json_priority_in

    params["priority__iregex"] = priority_iregex

    params["priority__isnull"] = priority_isnull

    params["priority__istartswith"] = priority_istartswith

    params["priority__lt"] = priority_lt

    params["priority__lte"] = priority_lte

    json_priority_range: list[int] | Unset = UNSET
    if not isinstance(priority_range, Unset):
        json_priority_range = priority_range

    params["priority__range"] = json_priority_range

    params["priority__regex"] = priority_regex

    params["priority__startswith"] = priority_startswith

    params["relatedTo"] = related_to

    json_related_to_in: list[int] | Unset = UNSET
    if not isinstance(related_to_in, Unset):
        json_related_to_in = related_to_in

    params["relatedTo__in"] = json_related_to_in

    params["relatedTo__isnull"] = related_to_isnull

    params["relatedTo__ob_id"] = related_to_ob_id

    json_related_to_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(related_to_ob_id_in, Unset):
        json_related_to_ob_id_in = related_to_ob_id_in

    params["relatedTo__ob_id__in"] = json_related_to_ob_id_in

    params["relatedTo__short_code"] = related_to_short_code

    json_related_to_short_code_in: list[str] | Unset = UNSET
    if not isinstance(related_to_short_code_in, Unset):
        json_related_to_short_code_in = related_to_short_code_in

    params["relatedTo__short_code__in"] = json_related_to_short_code_in

    params["relatedTo__uuid"] = related_to_uuid

    json_related_to_uuid_in: list[str] | Unset = UNSET
    if not isinstance(related_to_uuid_in, Unset):
        json_related_to_uuid_in = related_to_uuid_in

    params["relatedTo__uuid__in"] = json_related_to_uuid_in

    json_role: str | Unset = UNSET
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

    json_role_in: list[str] | Unset = UNSET
    if not isinstance(role_in, Unset):
        json_role_in = role_in

    params["role__in"] = json_role_in

    params["role__iregex"] = role_iregex

    params["role__isnull"] = role_isnull

    params["role__istartswith"] = role_istartswith

    params["role__lt"] = role_lt

    params["role__lte"] = role_lte

    json_role_range: list[str] | Unset = UNSET
    if not isinstance(role_range, Unset):
        json_role_range = role_range

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResponsiblePartyInfoReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedResponsiblePartyInfoReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    limit: int | Unset = UNSET,
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
    party: int | Unset = UNSET,
    party_first_name: str | Unset = UNSET,
    party_first_name_in: list[str] | Unset = UNSET,
    party_in: list[int] | Unset = UNSET,
    party_isnull: bool | Unset = UNSET,
    party_last_name: str | Unset = UNSET,
    party_last_name_in: list[str] | Unset = UNSET,
    party_ob_id: int | Unset = UNSET,
    party_ob_id_in: list[int] | Unset = UNSET,
    party_party_type: RpisListType | Unset = UNSET,
    party_party_type_in: list[str] | Unset = UNSET,
    priority: int | Unset = UNSET,
    priority_contained_by: int | Unset = UNSET,
    priority_contains: int | Unset = UNSET,
    priority_endswith: int | Unset = UNSET,
    priority_gt: int | Unset = UNSET,
    priority_gte: int | Unset = UNSET,
    priority_icontains: int | Unset = UNSET,
    priority_iendswith: int | Unset = UNSET,
    priority_iexact: int | Unset = UNSET,
    priority_in: list[int] | Unset = UNSET,
    priority_iregex: int | Unset = UNSET,
    priority_isnull: bool | Unset = UNSET,
    priority_istartswith: int | Unset = UNSET,
    priority_lt: int | Unset = UNSET,
    priority_lte: int | Unset = UNSET,
    priority_range: list[int] | Unset = UNSET,
    priority_regex: int | Unset = UNSET,
    priority_startswith: int | Unset = UNSET,
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
    role: RpisListRole | Unset = UNSET,
    role_contains: str | Unset = UNSET,
    role_endswith: str | Unset = UNSET,
    role_gt: str | Unset = UNSET,
    role_gte: str | Unset = UNSET,
    role_icontains: str | Unset = UNSET,
    role_iendswith: str | Unset = UNSET,
    role_iexact: str | Unset = UNSET,
    role_in: list[str] | Unset = UNSET,
    role_iregex: str | Unset = UNSET,
    role_isnull: bool | Unset = UNSET,
    role_istartswith: str | Unset = UNSET,
    role_lt: str | Unset = UNSET,
    role_lte: str | Unset = UNSET,
    role_range: list[str] | Unset = UNSET,
    role_regex: str | Unset = UNSET,
    role_startswith: str | Unset = UNSET,
) -> Response[PaginatedResponsiblePartyInfoReadList]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        limit (int | Unset):
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
        party (int | Unset):
        party_first_name (str | Unset):
        party_first_name_in (list[str] | Unset):
        party_in (list[int] | Unset):
        party_isnull (bool | Unset):
        party_last_name (str | Unset):
        party_last_name_in (list[str] | Unset):
        party_ob_id (int | Unset):
        party_ob_id_in (list[int] | Unset):
        party_party_type (RpisListType | Unset):
        party_party_type_in (list[str] | Unset):
        priority (int | Unset):
        priority_contained_by (int | Unset):
        priority_contains (int | Unset):
        priority_endswith (int | Unset):
        priority_gt (int | Unset):
        priority_gte (int | Unset):
        priority_icontains (int | Unset):
        priority_iendswith (int | Unset):
        priority_iexact (int | Unset):
        priority_in (list[int] | Unset):
        priority_iregex (int | Unset):
        priority_isnull (bool | Unset):
        priority_istartswith (int | Unset):
        priority_lt (int | Unset):
        priority_lte (int | Unset):
        priority_range (list[int] | Unset):
        priority_regex (int | Unset):
        priority_startswith (int | Unset):
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):
        role (RpisListRole | Unset):
        role_contains (str | Unset):
        role_endswith (str | Unset):
        role_gt (str | Unset):
        role_gte (str | Unset):
        role_icontains (str | Unset):
        role_iendswith (str | Unset):
        role_iexact (str | Unset):
        role_in (list[str] | Unset):
        role_iregex (str | Unset):
        role_isnull (bool | Unset):
        role_istartswith (str | Unset):
        role_lt (str | Unset):
        role_lte (str | Unset):
        role_range (list[str] | Unset):
        role_regex (str | Unset):
        role_startswith (str | Unset):

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
        party_in=party_in,
        party_isnull=party_isnull,
        party_last_name=party_last_name,
        party_last_name_in=party_last_name_in,
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
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
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
    limit: int | Unset = UNSET,
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
    party: int | Unset = UNSET,
    party_first_name: str | Unset = UNSET,
    party_first_name_in: list[str] | Unset = UNSET,
    party_in: list[int] | Unset = UNSET,
    party_isnull: bool | Unset = UNSET,
    party_last_name: str | Unset = UNSET,
    party_last_name_in: list[str] | Unset = UNSET,
    party_ob_id: int | Unset = UNSET,
    party_ob_id_in: list[int] | Unset = UNSET,
    party_party_type: RpisListType | Unset = UNSET,
    party_party_type_in: list[str] | Unset = UNSET,
    priority: int | Unset = UNSET,
    priority_contained_by: int | Unset = UNSET,
    priority_contains: int | Unset = UNSET,
    priority_endswith: int | Unset = UNSET,
    priority_gt: int | Unset = UNSET,
    priority_gte: int | Unset = UNSET,
    priority_icontains: int | Unset = UNSET,
    priority_iendswith: int | Unset = UNSET,
    priority_iexact: int | Unset = UNSET,
    priority_in: list[int] | Unset = UNSET,
    priority_iregex: int | Unset = UNSET,
    priority_isnull: bool | Unset = UNSET,
    priority_istartswith: int | Unset = UNSET,
    priority_lt: int | Unset = UNSET,
    priority_lte: int | Unset = UNSET,
    priority_range: list[int] | Unset = UNSET,
    priority_regex: int | Unset = UNSET,
    priority_startswith: int | Unset = UNSET,
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
    role: RpisListRole | Unset = UNSET,
    role_contains: str | Unset = UNSET,
    role_endswith: str | Unset = UNSET,
    role_gt: str | Unset = UNSET,
    role_gte: str | Unset = UNSET,
    role_icontains: str | Unset = UNSET,
    role_iendswith: str | Unset = UNSET,
    role_iexact: str | Unset = UNSET,
    role_in: list[str] | Unset = UNSET,
    role_iregex: str | Unset = UNSET,
    role_isnull: bool | Unset = UNSET,
    role_istartswith: str | Unset = UNSET,
    role_lt: str | Unset = UNSET,
    role_lte: str | Unset = UNSET,
    role_range: list[str] | Unset = UNSET,
    role_regex: str | Unset = UNSET,
    role_startswith: str | Unset = UNSET,
) -> PaginatedResponsiblePartyInfoReadList | None:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        limit (int | Unset):
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
        party (int | Unset):
        party_first_name (str | Unset):
        party_first_name_in (list[str] | Unset):
        party_in (list[int] | Unset):
        party_isnull (bool | Unset):
        party_last_name (str | Unset):
        party_last_name_in (list[str] | Unset):
        party_ob_id (int | Unset):
        party_ob_id_in (list[int] | Unset):
        party_party_type (RpisListType | Unset):
        party_party_type_in (list[str] | Unset):
        priority (int | Unset):
        priority_contained_by (int | Unset):
        priority_contains (int | Unset):
        priority_endswith (int | Unset):
        priority_gt (int | Unset):
        priority_gte (int | Unset):
        priority_icontains (int | Unset):
        priority_iendswith (int | Unset):
        priority_iexact (int | Unset):
        priority_in (list[int] | Unset):
        priority_iregex (int | Unset):
        priority_isnull (bool | Unset):
        priority_istartswith (int | Unset):
        priority_lt (int | Unset):
        priority_lte (int | Unset):
        priority_range (list[int] | Unset):
        priority_regex (int | Unset):
        priority_startswith (int | Unset):
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):
        role (RpisListRole | Unset):
        role_contains (str | Unset):
        role_endswith (str | Unset):
        role_gt (str | Unset):
        role_gte (str | Unset):
        role_icontains (str | Unset):
        role_iendswith (str | Unset):
        role_iexact (str | Unset):
        role_in (list[str] | Unset):
        role_iregex (str | Unset):
        role_isnull (bool | Unset):
        role_istartswith (str | Unset):
        role_lt (str | Unset):
        role_lte (str | Unset):
        role_range (list[str] | Unset):
        role_regex (str | Unset):
        role_startswith (str | Unset):

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
        party_in=party_in,
        party_isnull=party_isnull,
        party_last_name=party_last_name,
        party_last_name_in=party_last_name_in,
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
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
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
    limit: int | Unset = UNSET,
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
    party: int | Unset = UNSET,
    party_first_name: str | Unset = UNSET,
    party_first_name_in: list[str] | Unset = UNSET,
    party_in: list[int] | Unset = UNSET,
    party_isnull: bool | Unset = UNSET,
    party_last_name: str | Unset = UNSET,
    party_last_name_in: list[str] | Unset = UNSET,
    party_ob_id: int | Unset = UNSET,
    party_ob_id_in: list[int] | Unset = UNSET,
    party_party_type: RpisListType | Unset = UNSET,
    party_party_type_in: list[str] | Unset = UNSET,
    priority: int | Unset = UNSET,
    priority_contained_by: int | Unset = UNSET,
    priority_contains: int | Unset = UNSET,
    priority_endswith: int | Unset = UNSET,
    priority_gt: int | Unset = UNSET,
    priority_gte: int | Unset = UNSET,
    priority_icontains: int | Unset = UNSET,
    priority_iendswith: int | Unset = UNSET,
    priority_iexact: int | Unset = UNSET,
    priority_in: list[int] | Unset = UNSET,
    priority_iregex: int | Unset = UNSET,
    priority_isnull: bool | Unset = UNSET,
    priority_istartswith: int | Unset = UNSET,
    priority_lt: int | Unset = UNSET,
    priority_lte: int | Unset = UNSET,
    priority_range: list[int] | Unset = UNSET,
    priority_regex: int | Unset = UNSET,
    priority_startswith: int | Unset = UNSET,
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
    role: RpisListRole | Unset = UNSET,
    role_contains: str | Unset = UNSET,
    role_endswith: str | Unset = UNSET,
    role_gt: str | Unset = UNSET,
    role_gte: str | Unset = UNSET,
    role_icontains: str | Unset = UNSET,
    role_iendswith: str | Unset = UNSET,
    role_iexact: str | Unset = UNSET,
    role_in: list[str] | Unset = UNSET,
    role_iregex: str | Unset = UNSET,
    role_isnull: bool | Unset = UNSET,
    role_istartswith: str | Unset = UNSET,
    role_lt: str | Unset = UNSET,
    role_lte: str | Unset = UNSET,
    role_range: list[str] | Unset = UNSET,
    role_regex: str | Unset = UNSET,
    role_startswith: str | Unset = UNSET,
) -> Response[PaginatedResponsiblePartyInfoReadList]:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        limit (int | Unset):
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
        party (int | Unset):
        party_first_name (str | Unset):
        party_first_name_in (list[str] | Unset):
        party_in (list[int] | Unset):
        party_isnull (bool | Unset):
        party_last_name (str | Unset):
        party_last_name_in (list[str] | Unset):
        party_ob_id (int | Unset):
        party_ob_id_in (list[int] | Unset):
        party_party_type (RpisListType | Unset):
        party_party_type_in (list[str] | Unset):
        priority (int | Unset):
        priority_contained_by (int | Unset):
        priority_contains (int | Unset):
        priority_endswith (int | Unset):
        priority_gt (int | Unset):
        priority_gte (int | Unset):
        priority_icontains (int | Unset):
        priority_iendswith (int | Unset):
        priority_iexact (int | Unset):
        priority_in (list[int] | Unset):
        priority_iregex (int | Unset):
        priority_isnull (bool | Unset):
        priority_istartswith (int | Unset):
        priority_lt (int | Unset):
        priority_lte (int | Unset):
        priority_range (list[int] | Unset):
        priority_regex (int | Unset):
        priority_startswith (int | Unset):
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):
        role (RpisListRole | Unset):
        role_contains (str | Unset):
        role_endswith (str | Unset):
        role_gt (str | Unset):
        role_gte (str | Unset):
        role_icontains (str | Unset):
        role_iendswith (str | Unset):
        role_iexact (str | Unset):
        role_in (list[str] | Unset):
        role_iregex (str | Unset):
        role_isnull (bool | Unset):
        role_istartswith (str | Unset):
        role_lt (str | Unset):
        role_lte (str | Unset):
        role_range (list[str] | Unset):
        role_regex (str | Unset):
        role_startswith (str | Unset):

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
        party_in=party_in,
        party_isnull=party_isnull,
        party_last_name=party_last_name,
        party_last_name_in=party_last_name_in,
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
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
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
    limit: int | Unset = UNSET,
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
    party: int | Unset = UNSET,
    party_first_name: str | Unset = UNSET,
    party_first_name_in: list[str] | Unset = UNSET,
    party_in: list[int] | Unset = UNSET,
    party_isnull: bool | Unset = UNSET,
    party_last_name: str | Unset = UNSET,
    party_last_name_in: list[str] | Unset = UNSET,
    party_ob_id: int | Unset = UNSET,
    party_ob_id_in: list[int] | Unset = UNSET,
    party_party_type: RpisListType | Unset = UNSET,
    party_party_type_in: list[str] | Unset = UNSET,
    priority: int | Unset = UNSET,
    priority_contained_by: int | Unset = UNSET,
    priority_contains: int | Unset = UNSET,
    priority_endswith: int | Unset = UNSET,
    priority_gt: int | Unset = UNSET,
    priority_gte: int | Unset = UNSET,
    priority_icontains: int | Unset = UNSET,
    priority_iendswith: int | Unset = UNSET,
    priority_iexact: int | Unset = UNSET,
    priority_in: list[int] | Unset = UNSET,
    priority_iregex: int | Unset = UNSET,
    priority_isnull: bool | Unset = UNSET,
    priority_istartswith: int | Unset = UNSET,
    priority_lt: int | Unset = UNSET,
    priority_lte: int | Unset = UNSET,
    priority_range: list[int] | Unset = UNSET,
    priority_regex: int | Unset = UNSET,
    priority_startswith: int | Unset = UNSET,
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
    role: RpisListRole | Unset = UNSET,
    role_contains: str | Unset = UNSET,
    role_endswith: str | Unset = UNSET,
    role_gt: str | Unset = UNSET,
    role_gte: str | Unset = UNSET,
    role_icontains: str | Unset = UNSET,
    role_iendswith: str | Unset = UNSET,
    role_iexact: str | Unset = UNSET,
    role_in: list[str] | Unset = UNSET,
    role_iregex: str | Unset = UNSET,
    role_isnull: bool | Unset = UNSET,
    role_istartswith: str | Unset = UNSET,
    role_lt: str | Unset = UNSET,
    role_lte: str | Unset = UNSET,
    role_range: list[str] | Unset = UNSET,
    role_regex: str | Unset = UNSET,
    role_startswith: str | Unset = UNSET,
) -> PaginatedResponsiblePartyInfoReadList | None:
    """Get a list of ResponsiblePartyInfo objects. These link a Party (individual or organisation) to
    a principal record type (e.g. Observation, Instrument, Project) and the role which the Party was
    undertaking. Additionally, the priority value indicates an ordering that may be present for
    that given role for the relatedTo object.

    Args:
        limit (int | Unset):
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
        party (int | Unset):
        party_first_name (str | Unset):
        party_first_name_in (list[str] | Unset):
        party_in (list[int] | Unset):
        party_isnull (bool | Unset):
        party_last_name (str | Unset):
        party_last_name_in (list[str] | Unset):
        party_ob_id (int | Unset):
        party_ob_id_in (list[int] | Unset):
        party_party_type (RpisListType | Unset):
        party_party_type_in (list[str] | Unset):
        priority (int | Unset):
        priority_contained_by (int | Unset):
        priority_contains (int | Unset):
        priority_endswith (int | Unset):
        priority_gt (int | Unset):
        priority_gte (int | Unset):
        priority_icontains (int | Unset):
        priority_iendswith (int | Unset):
        priority_iexact (int | Unset):
        priority_in (list[int] | Unset):
        priority_iregex (int | Unset):
        priority_isnull (bool | Unset):
        priority_istartswith (int | Unset):
        priority_lt (int | Unset):
        priority_lte (int | Unset):
        priority_range (list[int] | Unset):
        priority_regex (int | Unset):
        priority_startswith (int | Unset):
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):
        role (RpisListRole | Unset):
        role_contains (str | Unset):
        role_endswith (str | Unset):
        role_gt (str | Unset):
        role_gte (str | Unset):
        role_icontains (str | Unset):
        role_iendswith (str | Unset):
        role_iexact (str | Unset):
        role_in (list[str] | Unset):
        role_iregex (str | Unset):
        role_isnull (bool | Unset):
        role_istartswith (str | Unset):
        role_lt (str | Unset):
        role_lte (str | Unset):
        role_range (list[str] | Unset):
        role_regex (str | Unset):
        role_startswith (str | Unset):

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
            party_in=party_in,
            party_isnull=party_isnull,
            party_last_name=party_last_name,
            party_last_name_in=party_last_name_in,
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
            related_to_in=related_to_in,
            related_to_isnull=related_to_isnull,
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
