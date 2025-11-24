from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_related_observation_info_read_list import PaginatedRelatedObservationInfoReadList
from ...models.relatedobservationinfos_list_relation_type_between_subject_and_object_obs import (
    RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs,
)
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
    object_observation: int | Unset = UNSET,
    object_observation_gt: int | Unset = UNSET,
    object_observation_gte: int | Unset = UNSET,
    object_observation_in: list[int] | Unset = UNSET,
    object_observation_isnull: bool | Unset = UNSET,
    object_observation_lt: int | Unset = UNSET,
    object_observation_lte: int | Unset = UNSET,
    object_observation_uuid: str | Unset = UNSET,
    object_observation_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    relation_type: RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs | Unset = UNSET,
    relation_type_contains: str | Unset = UNSET,
    relation_type_endswith: str | Unset = UNSET,
    relation_type_gt: str | Unset = UNSET,
    relation_type_gte: str | Unset = UNSET,
    relation_type_icontains: str | Unset = UNSET,
    relation_type_iendswith: str | Unset = UNSET,
    relation_type_iexact: str | Unset = UNSET,
    relation_type_in: list[str] | Unset = UNSET,
    relation_type_iregex: str | Unset = UNSET,
    relation_type_isnull: bool | Unset = UNSET,
    relation_type_istartswith: str | Unset = UNSET,
    relation_type_lt: str | Unset = UNSET,
    relation_type_lte: str | Unset = UNSET,
    relation_type_range: list[str] | Unset = UNSET,
    relation_type_regex: str | Unset = UNSET,
    relation_type_startswith: str | Unset = UNSET,
    subject_observation: int | Unset = UNSET,
    subject_observation_gt: int | Unset = UNSET,
    subject_observation_gte: int | Unset = UNSET,
    subject_observation_in: list[int] | Unset = UNSET,
    subject_observation_isnull: bool | Unset = UNSET,
    subject_observation_lt: int | Unset = UNSET,
    subject_observation_lte: int | Unset = UNSET,
    subject_observation_ob_id: int | Unset = UNSET,
    subject_observation_ob_id_in: list[int] | Unset = UNSET,
    subject_observation_uuid: str | Unset = UNSET,
    subject_observation_uuid_in: list[str] | Unset = UNSET,
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

    params["objectObservation"] = object_observation

    params["objectObservation__gt"] = object_observation_gt

    params["objectObservation__gte"] = object_observation_gte

    json_object_observation_in: list[int] | Unset = UNSET
    if not isinstance(object_observation_in, Unset):
        json_object_observation_in = ",".join(map(str, object_observation_in))

    params["objectObservation__in"] = json_object_observation_in

    params["objectObservation__isnull"] = object_observation_isnull

    params["objectObservation__lt"] = object_observation_lt

    params["objectObservation__lte"] = object_observation_lte

    params["objectObservation__uuid"] = object_observation_uuid

    json_object_observation_uuid_in: list[str] | Unset = UNSET
    if not isinstance(object_observation_uuid_in, Unset):
        json_object_observation_uuid_in = ",".join(map(str, object_observation_uuid_in))

    params["objectObservation__uuid__in"] = json_object_observation_uuid_in

    params["offset"] = offset

    params["ordering"] = ordering

    json_relation_type: str | Unset = UNSET
    if not isinstance(relation_type, Unset):
        json_relation_type = relation_type.value

    params["relationType"] = json_relation_type

    params["relationType__contains"] = relation_type_contains

    params["relationType__endswith"] = relation_type_endswith

    params["relationType__gt"] = relation_type_gt

    params["relationType__gte"] = relation_type_gte

    params["relationType__icontains"] = relation_type_icontains

    params["relationType__iendswith"] = relation_type_iendswith

    params["relationType__iexact"] = relation_type_iexact

    json_relation_type_in: list[str] | Unset = UNSET
    if not isinstance(relation_type_in, Unset):
        json_relation_type_in = ",".join(map(str, relation_type_in))

    params["relationType__in"] = json_relation_type_in

    params["relationType__iregex"] = relation_type_iregex

    params["relationType__isnull"] = relation_type_isnull

    params["relationType__istartswith"] = relation_type_istartswith

    params["relationType__lt"] = relation_type_lt

    params["relationType__lte"] = relation_type_lte

    json_relation_type_range: list[str] | Unset = UNSET
    if not isinstance(relation_type_range, Unset):
        json_relation_type_range = ",".join(map(str, relation_type_range))

    params["relationType__range"] = json_relation_type_range

    params["relationType__regex"] = relation_type_regex

    params["relationType__startswith"] = relation_type_startswith

    params["subjectObservation"] = subject_observation

    params["subjectObservation__gt"] = subject_observation_gt

    params["subjectObservation__gte"] = subject_observation_gte

    json_subject_observation_in: list[int] | Unset = UNSET
    if not isinstance(subject_observation_in, Unset):
        json_subject_observation_in = ",".join(map(str, subject_observation_in))

    params["subjectObservation__in"] = json_subject_observation_in

    params["subjectObservation__isnull"] = subject_observation_isnull

    params["subjectObservation__lt"] = subject_observation_lt

    params["subjectObservation__lte"] = subject_observation_lte

    params["subjectObservation__ob_id"] = subject_observation_ob_id

    json_subject_observation_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(subject_observation_ob_id_in, Unset):
        json_subject_observation_ob_id_in = ",".join(map(str, subject_observation_ob_id_in))

    params["subjectObservation__ob_id__in"] = json_subject_observation_ob_id_in

    params["subjectObservation__uuid"] = subject_observation_uuid

    json_subject_observation_uuid_in: list[str] | Unset = UNSET
    if not isinstance(subject_observation_uuid_in, Unset):
        json_subject_observation_uuid_in = ",".join(map(str, subject_observation_uuid_in))

    params["subjectObservation__uuid__in"] = json_subject_observation_uuid_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/relatedobservationinfos/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedRelatedObservationInfoReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedRelatedObservationInfoReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedRelatedObservationInfoReadList]:
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
    object_observation: int | Unset = UNSET,
    object_observation_gt: int | Unset = UNSET,
    object_observation_gte: int | Unset = UNSET,
    object_observation_in: list[int] | Unset = UNSET,
    object_observation_isnull: bool | Unset = UNSET,
    object_observation_lt: int | Unset = UNSET,
    object_observation_lte: int | Unset = UNSET,
    object_observation_uuid: str | Unset = UNSET,
    object_observation_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    relation_type: RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs | Unset = UNSET,
    relation_type_contains: str | Unset = UNSET,
    relation_type_endswith: str | Unset = UNSET,
    relation_type_gt: str | Unset = UNSET,
    relation_type_gte: str | Unset = UNSET,
    relation_type_icontains: str | Unset = UNSET,
    relation_type_iendswith: str | Unset = UNSET,
    relation_type_iexact: str | Unset = UNSET,
    relation_type_in: list[str] | Unset = UNSET,
    relation_type_iregex: str | Unset = UNSET,
    relation_type_isnull: bool | Unset = UNSET,
    relation_type_istartswith: str | Unset = UNSET,
    relation_type_lt: str | Unset = UNSET,
    relation_type_lte: str | Unset = UNSET,
    relation_type_range: list[str] | Unset = UNSET,
    relation_type_regex: str | Unset = UNSET,
    relation_type_startswith: str | Unset = UNSET,
    subject_observation: int | Unset = UNSET,
    subject_observation_gt: int | Unset = UNSET,
    subject_observation_gte: int | Unset = UNSET,
    subject_observation_in: list[int] | Unset = UNSET,
    subject_observation_isnull: bool | Unset = UNSET,
    subject_observation_lt: int | Unset = UNSET,
    subject_observation_lte: int | Unset = UNSET,
    subject_observation_ob_id: int | Unset = UNSET,
    subject_observation_ob_id_in: list[int] | Unset = UNSET,
    subject_observation_uuid: str | Unset = UNSET,
    subject_observation_uuid_in: list[str] | Unset = UNSET,
) -> Response[PaginatedRelatedObservationInfoReadList]:
    """Get a list of RelatedObservationInfo objects.

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
        object_observation (int | Unset):
        object_observation_gt (int | Unset):
        object_observation_gte (int | Unset):
        object_observation_in (list[int] | Unset):
        object_observation_isnull (bool | Unset):
        object_observation_lt (int | Unset):
        object_observation_lte (int | Unset):
        object_observation_uuid (str | Unset):
        object_observation_uuid_in (list[str] | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        relation_type (RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs | Unset):
        relation_type_contains (str | Unset):
        relation_type_endswith (str | Unset):
        relation_type_gt (str | Unset):
        relation_type_gte (str | Unset):
        relation_type_icontains (str | Unset):
        relation_type_iendswith (str | Unset):
        relation_type_iexact (str | Unset):
        relation_type_in (list[str] | Unset):
        relation_type_iregex (str | Unset):
        relation_type_isnull (bool | Unset):
        relation_type_istartswith (str | Unset):
        relation_type_lt (str | Unset):
        relation_type_lte (str | Unset):
        relation_type_range (list[str] | Unset):
        relation_type_regex (str | Unset):
        relation_type_startswith (str | Unset):
        subject_observation (int | Unset):
        subject_observation_gt (int | Unset):
        subject_observation_gte (int | Unset):
        subject_observation_in (list[int] | Unset):
        subject_observation_isnull (bool | Unset):
        subject_observation_lt (int | Unset):
        subject_observation_lte (int | Unset):
        subject_observation_ob_id (int | Unset):
        subject_observation_ob_id_in (list[int] | Unset):
        subject_observation_uuid (str | Unset):
        subject_observation_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRelatedObservationInfoReadList]
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
        object_observation=object_observation,
        object_observation_gt=object_observation_gt,
        object_observation_gte=object_observation_gte,
        object_observation_in=object_observation_in,
        object_observation_isnull=object_observation_isnull,
        object_observation_lt=object_observation_lt,
        object_observation_lte=object_observation_lte,
        object_observation_uuid=object_observation_uuid,
        object_observation_uuid_in=object_observation_uuid_in,
        offset=offset,
        ordering=ordering,
        relation_type=relation_type,
        relation_type_contains=relation_type_contains,
        relation_type_endswith=relation_type_endswith,
        relation_type_gt=relation_type_gt,
        relation_type_gte=relation_type_gte,
        relation_type_icontains=relation_type_icontains,
        relation_type_iendswith=relation_type_iendswith,
        relation_type_iexact=relation_type_iexact,
        relation_type_in=relation_type_in,
        relation_type_iregex=relation_type_iregex,
        relation_type_isnull=relation_type_isnull,
        relation_type_istartswith=relation_type_istartswith,
        relation_type_lt=relation_type_lt,
        relation_type_lte=relation_type_lte,
        relation_type_range=relation_type_range,
        relation_type_regex=relation_type_regex,
        relation_type_startswith=relation_type_startswith,
        subject_observation=subject_observation,
        subject_observation_gt=subject_observation_gt,
        subject_observation_gte=subject_observation_gte,
        subject_observation_in=subject_observation_in,
        subject_observation_isnull=subject_observation_isnull,
        subject_observation_lt=subject_observation_lt,
        subject_observation_lte=subject_observation_lte,
        subject_observation_ob_id=subject_observation_ob_id,
        subject_observation_ob_id_in=subject_observation_ob_id_in,
        subject_observation_uuid=subject_observation_uuid,
        subject_observation_uuid_in=subject_observation_uuid_in,
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
    object_observation: int | Unset = UNSET,
    object_observation_gt: int | Unset = UNSET,
    object_observation_gte: int | Unset = UNSET,
    object_observation_in: list[int] | Unset = UNSET,
    object_observation_isnull: bool | Unset = UNSET,
    object_observation_lt: int | Unset = UNSET,
    object_observation_lte: int | Unset = UNSET,
    object_observation_uuid: str | Unset = UNSET,
    object_observation_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    relation_type: RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs | Unset = UNSET,
    relation_type_contains: str | Unset = UNSET,
    relation_type_endswith: str | Unset = UNSET,
    relation_type_gt: str | Unset = UNSET,
    relation_type_gte: str | Unset = UNSET,
    relation_type_icontains: str | Unset = UNSET,
    relation_type_iendswith: str | Unset = UNSET,
    relation_type_iexact: str | Unset = UNSET,
    relation_type_in: list[str] | Unset = UNSET,
    relation_type_iregex: str | Unset = UNSET,
    relation_type_isnull: bool | Unset = UNSET,
    relation_type_istartswith: str | Unset = UNSET,
    relation_type_lt: str | Unset = UNSET,
    relation_type_lte: str | Unset = UNSET,
    relation_type_range: list[str] | Unset = UNSET,
    relation_type_regex: str | Unset = UNSET,
    relation_type_startswith: str | Unset = UNSET,
    subject_observation: int | Unset = UNSET,
    subject_observation_gt: int | Unset = UNSET,
    subject_observation_gte: int | Unset = UNSET,
    subject_observation_in: list[int] | Unset = UNSET,
    subject_observation_isnull: bool | Unset = UNSET,
    subject_observation_lt: int | Unset = UNSET,
    subject_observation_lte: int | Unset = UNSET,
    subject_observation_ob_id: int | Unset = UNSET,
    subject_observation_ob_id_in: list[int] | Unset = UNSET,
    subject_observation_uuid: str | Unset = UNSET,
    subject_observation_uuid_in: list[str] | Unset = UNSET,
) -> PaginatedRelatedObservationInfoReadList | None:
    """Get a list of RelatedObservationInfo objects.

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
        object_observation (int | Unset):
        object_observation_gt (int | Unset):
        object_observation_gte (int | Unset):
        object_observation_in (list[int] | Unset):
        object_observation_isnull (bool | Unset):
        object_observation_lt (int | Unset):
        object_observation_lte (int | Unset):
        object_observation_uuid (str | Unset):
        object_observation_uuid_in (list[str] | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        relation_type (RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs | Unset):
        relation_type_contains (str | Unset):
        relation_type_endswith (str | Unset):
        relation_type_gt (str | Unset):
        relation_type_gte (str | Unset):
        relation_type_icontains (str | Unset):
        relation_type_iendswith (str | Unset):
        relation_type_iexact (str | Unset):
        relation_type_in (list[str] | Unset):
        relation_type_iregex (str | Unset):
        relation_type_isnull (bool | Unset):
        relation_type_istartswith (str | Unset):
        relation_type_lt (str | Unset):
        relation_type_lte (str | Unset):
        relation_type_range (list[str] | Unset):
        relation_type_regex (str | Unset):
        relation_type_startswith (str | Unset):
        subject_observation (int | Unset):
        subject_observation_gt (int | Unset):
        subject_observation_gte (int | Unset):
        subject_observation_in (list[int] | Unset):
        subject_observation_isnull (bool | Unset):
        subject_observation_lt (int | Unset):
        subject_observation_lte (int | Unset):
        subject_observation_ob_id (int | Unset):
        subject_observation_ob_id_in (list[int] | Unset):
        subject_observation_uuid (str | Unset):
        subject_observation_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRelatedObservationInfoReadList
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
        object_observation=object_observation,
        object_observation_gt=object_observation_gt,
        object_observation_gte=object_observation_gte,
        object_observation_in=object_observation_in,
        object_observation_isnull=object_observation_isnull,
        object_observation_lt=object_observation_lt,
        object_observation_lte=object_observation_lte,
        object_observation_uuid=object_observation_uuid,
        object_observation_uuid_in=object_observation_uuid_in,
        offset=offset,
        ordering=ordering,
        relation_type=relation_type,
        relation_type_contains=relation_type_contains,
        relation_type_endswith=relation_type_endswith,
        relation_type_gt=relation_type_gt,
        relation_type_gte=relation_type_gte,
        relation_type_icontains=relation_type_icontains,
        relation_type_iendswith=relation_type_iendswith,
        relation_type_iexact=relation_type_iexact,
        relation_type_in=relation_type_in,
        relation_type_iregex=relation_type_iregex,
        relation_type_isnull=relation_type_isnull,
        relation_type_istartswith=relation_type_istartswith,
        relation_type_lt=relation_type_lt,
        relation_type_lte=relation_type_lte,
        relation_type_range=relation_type_range,
        relation_type_regex=relation_type_regex,
        relation_type_startswith=relation_type_startswith,
        subject_observation=subject_observation,
        subject_observation_gt=subject_observation_gt,
        subject_observation_gte=subject_observation_gte,
        subject_observation_in=subject_observation_in,
        subject_observation_isnull=subject_observation_isnull,
        subject_observation_lt=subject_observation_lt,
        subject_observation_lte=subject_observation_lte,
        subject_observation_ob_id=subject_observation_ob_id,
        subject_observation_ob_id_in=subject_observation_ob_id_in,
        subject_observation_uuid=subject_observation_uuid,
        subject_observation_uuid_in=subject_observation_uuid_in,
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
    object_observation: int | Unset = UNSET,
    object_observation_gt: int | Unset = UNSET,
    object_observation_gte: int | Unset = UNSET,
    object_observation_in: list[int] | Unset = UNSET,
    object_observation_isnull: bool | Unset = UNSET,
    object_observation_lt: int | Unset = UNSET,
    object_observation_lte: int | Unset = UNSET,
    object_observation_uuid: str | Unset = UNSET,
    object_observation_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    relation_type: RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs | Unset = UNSET,
    relation_type_contains: str | Unset = UNSET,
    relation_type_endswith: str | Unset = UNSET,
    relation_type_gt: str | Unset = UNSET,
    relation_type_gte: str | Unset = UNSET,
    relation_type_icontains: str | Unset = UNSET,
    relation_type_iendswith: str | Unset = UNSET,
    relation_type_iexact: str | Unset = UNSET,
    relation_type_in: list[str] | Unset = UNSET,
    relation_type_iregex: str | Unset = UNSET,
    relation_type_isnull: bool | Unset = UNSET,
    relation_type_istartswith: str | Unset = UNSET,
    relation_type_lt: str | Unset = UNSET,
    relation_type_lte: str | Unset = UNSET,
    relation_type_range: list[str] | Unset = UNSET,
    relation_type_regex: str | Unset = UNSET,
    relation_type_startswith: str | Unset = UNSET,
    subject_observation: int | Unset = UNSET,
    subject_observation_gt: int | Unset = UNSET,
    subject_observation_gte: int | Unset = UNSET,
    subject_observation_in: list[int] | Unset = UNSET,
    subject_observation_isnull: bool | Unset = UNSET,
    subject_observation_lt: int | Unset = UNSET,
    subject_observation_lte: int | Unset = UNSET,
    subject_observation_ob_id: int | Unset = UNSET,
    subject_observation_ob_id_in: list[int] | Unset = UNSET,
    subject_observation_uuid: str | Unset = UNSET,
    subject_observation_uuid_in: list[str] | Unset = UNSET,
) -> Response[PaginatedRelatedObservationInfoReadList]:
    """Get a list of RelatedObservationInfo objects.

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
        object_observation (int | Unset):
        object_observation_gt (int | Unset):
        object_observation_gte (int | Unset):
        object_observation_in (list[int] | Unset):
        object_observation_isnull (bool | Unset):
        object_observation_lt (int | Unset):
        object_observation_lte (int | Unset):
        object_observation_uuid (str | Unset):
        object_observation_uuid_in (list[str] | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        relation_type (RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs | Unset):
        relation_type_contains (str | Unset):
        relation_type_endswith (str | Unset):
        relation_type_gt (str | Unset):
        relation_type_gte (str | Unset):
        relation_type_icontains (str | Unset):
        relation_type_iendswith (str | Unset):
        relation_type_iexact (str | Unset):
        relation_type_in (list[str] | Unset):
        relation_type_iregex (str | Unset):
        relation_type_isnull (bool | Unset):
        relation_type_istartswith (str | Unset):
        relation_type_lt (str | Unset):
        relation_type_lte (str | Unset):
        relation_type_range (list[str] | Unset):
        relation_type_regex (str | Unset):
        relation_type_startswith (str | Unset):
        subject_observation (int | Unset):
        subject_observation_gt (int | Unset):
        subject_observation_gte (int | Unset):
        subject_observation_in (list[int] | Unset):
        subject_observation_isnull (bool | Unset):
        subject_observation_lt (int | Unset):
        subject_observation_lte (int | Unset):
        subject_observation_ob_id (int | Unset):
        subject_observation_ob_id_in (list[int] | Unset):
        subject_observation_uuid (str | Unset):
        subject_observation_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedRelatedObservationInfoReadList]
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
        object_observation=object_observation,
        object_observation_gt=object_observation_gt,
        object_observation_gte=object_observation_gte,
        object_observation_in=object_observation_in,
        object_observation_isnull=object_observation_isnull,
        object_observation_lt=object_observation_lt,
        object_observation_lte=object_observation_lte,
        object_observation_uuid=object_observation_uuid,
        object_observation_uuid_in=object_observation_uuid_in,
        offset=offset,
        ordering=ordering,
        relation_type=relation_type,
        relation_type_contains=relation_type_contains,
        relation_type_endswith=relation_type_endswith,
        relation_type_gt=relation_type_gt,
        relation_type_gte=relation_type_gte,
        relation_type_icontains=relation_type_icontains,
        relation_type_iendswith=relation_type_iendswith,
        relation_type_iexact=relation_type_iexact,
        relation_type_in=relation_type_in,
        relation_type_iregex=relation_type_iregex,
        relation_type_isnull=relation_type_isnull,
        relation_type_istartswith=relation_type_istartswith,
        relation_type_lt=relation_type_lt,
        relation_type_lte=relation_type_lte,
        relation_type_range=relation_type_range,
        relation_type_regex=relation_type_regex,
        relation_type_startswith=relation_type_startswith,
        subject_observation=subject_observation,
        subject_observation_gt=subject_observation_gt,
        subject_observation_gte=subject_observation_gte,
        subject_observation_in=subject_observation_in,
        subject_observation_isnull=subject_observation_isnull,
        subject_observation_lt=subject_observation_lt,
        subject_observation_lte=subject_observation_lte,
        subject_observation_ob_id=subject_observation_ob_id,
        subject_observation_ob_id_in=subject_observation_ob_id_in,
        subject_observation_uuid=subject_observation_uuid,
        subject_observation_uuid_in=subject_observation_uuid_in,
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
    object_observation: int | Unset = UNSET,
    object_observation_gt: int | Unset = UNSET,
    object_observation_gte: int | Unset = UNSET,
    object_observation_in: list[int] | Unset = UNSET,
    object_observation_isnull: bool | Unset = UNSET,
    object_observation_lt: int | Unset = UNSET,
    object_observation_lte: int | Unset = UNSET,
    object_observation_uuid: str | Unset = UNSET,
    object_observation_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    relation_type: RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs | Unset = UNSET,
    relation_type_contains: str | Unset = UNSET,
    relation_type_endswith: str | Unset = UNSET,
    relation_type_gt: str | Unset = UNSET,
    relation_type_gte: str | Unset = UNSET,
    relation_type_icontains: str | Unset = UNSET,
    relation_type_iendswith: str | Unset = UNSET,
    relation_type_iexact: str | Unset = UNSET,
    relation_type_in: list[str] | Unset = UNSET,
    relation_type_iregex: str | Unset = UNSET,
    relation_type_isnull: bool | Unset = UNSET,
    relation_type_istartswith: str | Unset = UNSET,
    relation_type_lt: str | Unset = UNSET,
    relation_type_lte: str | Unset = UNSET,
    relation_type_range: list[str] | Unset = UNSET,
    relation_type_regex: str | Unset = UNSET,
    relation_type_startswith: str | Unset = UNSET,
    subject_observation: int | Unset = UNSET,
    subject_observation_gt: int | Unset = UNSET,
    subject_observation_gte: int | Unset = UNSET,
    subject_observation_in: list[int] | Unset = UNSET,
    subject_observation_isnull: bool | Unset = UNSET,
    subject_observation_lt: int | Unset = UNSET,
    subject_observation_lte: int | Unset = UNSET,
    subject_observation_ob_id: int | Unset = UNSET,
    subject_observation_ob_id_in: list[int] | Unset = UNSET,
    subject_observation_uuid: str | Unset = UNSET,
    subject_observation_uuid_in: list[str] | Unset = UNSET,
) -> PaginatedRelatedObservationInfoReadList | None:
    """Get a list of RelatedObservationInfo objects.

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
        object_observation (int | Unset):
        object_observation_gt (int | Unset):
        object_observation_gte (int | Unset):
        object_observation_in (list[int] | Unset):
        object_observation_isnull (bool | Unset):
        object_observation_lt (int | Unset):
        object_observation_lte (int | Unset):
        object_observation_uuid (str | Unset):
        object_observation_uuid_in (list[str] | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        relation_type (RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs | Unset):
        relation_type_contains (str | Unset):
        relation_type_endswith (str | Unset):
        relation_type_gt (str | Unset):
        relation_type_gte (str | Unset):
        relation_type_icontains (str | Unset):
        relation_type_iendswith (str | Unset):
        relation_type_iexact (str | Unset):
        relation_type_in (list[str] | Unset):
        relation_type_iregex (str | Unset):
        relation_type_isnull (bool | Unset):
        relation_type_istartswith (str | Unset):
        relation_type_lt (str | Unset):
        relation_type_lte (str | Unset):
        relation_type_range (list[str] | Unset):
        relation_type_regex (str | Unset):
        relation_type_startswith (str | Unset):
        subject_observation (int | Unset):
        subject_observation_gt (int | Unset):
        subject_observation_gte (int | Unset):
        subject_observation_in (list[int] | Unset):
        subject_observation_isnull (bool | Unset):
        subject_observation_lt (int | Unset):
        subject_observation_lte (int | Unset):
        subject_observation_ob_id (int | Unset):
        subject_observation_ob_id_in (list[int] | Unset):
        subject_observation_uuid (str | Unset):
        subject_observation_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedRelatedObservationInfoReadList
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
            object_observation=object_observation,
            object_observation_gt=object_observation_gt,
            object_observation_gte=object_observation_gte,
            object_observation_in=object_observation_in,
            object_observation_isnull=object_observation_isnull,
            object_observation_lt=object_observation_lt,
            object_observation_lte=object_observation_lte,
            object_observation_uuid=object_observation_uuid,
            object_observation_uuid_in=object_observation_uuid_in,
            offset=offset,
            ordering=ordering,
            relation_type=relation_type,
            relation_type_contains=relation_type_contains,
            relation_type_endswith=relation_type_endswith,
            relation_type_gt=relation_type_gt,
            relation_type_gte=relation_type_gte,
            relation_type_icontains=relation_type_icontains,
            relation_type_iendswith=relation_type_iendswith,
            relation_type_iexact=relation_type_iexact,
            relation_type_in=relation_type_in,
            relation_type_iregex=relation_type_iregex,
            relation_type_isnull=relation_type_isnull,
            relation_type_istartswith=relation_type_istartswith,
            relation_type_lt=relation_type_lt,
            relation_type_lte=relation_type_lte,
            relation_type_range=relation_type_range,
            relation_type_regex=relation_type_regex,
            relation_type_startswith=relation_type_startswith,
            subject_observation=subject_observation,
            subject_observation_gt=subject_observation_gt,
            subject_observation_gte=subject_observation_gte,
            subject_observation_in=subject_observation_in,
            subject_observation_isnull=subject_observation_isnull,
            subject_observation_lt=subject_observation_lt,
            subject_observation_lte=subject_observation_lte,
            subject_observation_ob_id=subject_observation_ob_id,
            subject_observation_ob_id_in=subject_observation_ob_id_in,
            subject_observation_uuid=subject_observation_uuid,
            subject_observation_uuid_in=subject_observation_uuid_in,
        )
    ).parsed
