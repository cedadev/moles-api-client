from http import HTTPStatus
from typing import Any, Optional, Union

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
    object_observation: Union[Unset, int] = UNSET,
    object_observation_gt: Union[Unset, int] = UNSET,
    object_observation_gte: Union[Unset, int] = UNSET,
    object_observation_in: Union[Unset, list[int]] = UNSET,
    object_observation_isnull: Union[Unset, bool] = UNSET,
    object_observation_lt: Union[Unset, int] = UNSET,
    object_observation_lte: Union[Unset, int] = UNSET,
    object_observation_uuid: Union[Unset, str] = UNSET,
    object_observation_uuid_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    relation_type: Union[Unset, RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs] = UNSET,
    relation_type_contains: Union[Unset, str] = UNSET,
    relation_type_endswith: Union[Unset, str] = UNSET,
    relation_type_gt: Union[Unset, str] = UNSET,
    relation_type_gte: Union[Unset, str] = UNSET,
    relation_type_icontains: Union[Unset, str] = UNSET,
    relation_type_iendswith: Union[Unset, str] = UNSET,
    relation_type_iexact: Union[Unset, str] = UNSET,
    relation_type_in: Union[Unset, list[str]] = UNSET,
    relation_type_iregex: Union[Unset, str] = UNSET,
    relation_type_isnull: Union[Unset, bool] = UNSET,
    relation_type_istartswith: Union[Unset, str] = UNSET,
    relation_type_lt: Union[Unset, str] = UNSET,
    relation_type_lte: Union[Unset, str] = UNSET,
    relation_type_range: Union[Unset, list[str]] = UNSET,
    relation_type_regex: Union[Unset, str] = UNSET,
    relation_type_startswith: Union[Unset, str] = UNSET,
    subject_observation: Union[Unset, int] = UNSET,
    subject_observation_gt: Union[Unset, int] = UNSET,
    subject_observation_gte: Union[Unset, int] = UNSET,
    subject_observation_in: Union[Unset, list[int]] = UNSET,
    subject_observation_isnull: Union[Unset, bool] = UNSET,
    subject_observation_lt: Union[Unset, int] = UNSET,
    subject_observation_lte: Union[Unset, int] = UNSET,
    subject_observation_ob_id: Union[Unset, int] = UNSET,
    subject_observation_ob_id_in: Union[Unset, list[int]] = UNSET,
    subject_observation_uuid: Union[Unset, str] = UNSET,
    subject_observation_uuid_in: Union[Unset, list[str]] = UNSET,
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
        json_ob_id_in = ",".join(ob_id_in)

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ",".join(ob_id_range)

    params["ob_id__range"] = json_ob_id_range

    params["ob_id__regex"] = ob_id_regex

    params["ob_id__startswith"] = ob_id_startswith

    params["objectObservation"] = object_observation

    params["objectObservation__gt"] = object_observation_gt

    params["objectObservation__gte"] = object_observation_gte

    json_object_observation_in: Union[Unset, list[int]] = UNSET
    if not isinstance(object_observation_in, Unset):
        json_object_observation_in = ",".join(object_observation_in)

    params["objectObservation__in"] = json_object_observation_in

    params["objectObservation__isnull"] = object_observation_isnull

    params["objectObservation__lt"] = object_observation_lt

    params["objectObservation__lte"] = object_observation_lte

    params["objectObservation__uuid"] = object_observation_uuid

    json_object_observation_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(object_observation_uuid_in, Unset):
        json_object_observation_uuid_in = ",".join(object_observation_uuid_in)

    params["objectObservation__uuid__in"] = json_object_observation_uuid_in

    params["offset"] = offset

    params["ordering"] = ordering

    json_relation_type: Union[Unset, str] = UNSET
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

    json_relation_type_in: Union[Unset, list[str]] = UNSET
    if not isinstance(relation_type_in, Unset):
        json_relation_type_in = ",".join(relation_type_in)

    params["relationType__in"] = json_relation_type_in

    params["relationType__iregex"] = relation_type_iregex

    params["relationType__isnull"] = relation_type_isnull

    params["relationType__istartswith"] = relation_type_istartswith

    params["relationType__lt"] = relation_type_lt

    params["relationType__lte"] = relation_type_lte

    json_relation_type_range: Union[Unset, list[str]] = UNSET
    if not isinstance(relation_type_range, Unset):
        json_relation_type_range = ",".join(relation_type_range)

    params["relationType__range"] = json_relation_type_range

    params["relationType__regex"] = relation_type_regex

    params["relationType__startswith"] = relation_type_startswith

    params["subjectObservation"] = subject_observation

    params["subjectObservation__gt"] = subject_observation_gt

    params["subjectObservation__gte"] = subject_observation_gte

    json_subject_observation_in: Union[Unset, list[int]] = UNSET
    if not isinstance(subject_observation_in, Unset):
        json_subject_observation_in = ",".join(subject_observation_in)

    params["subjectObservation__in"] = json_subject_observation_in

    params["subjectObservation__isnull"] = subject_observation_isnull

    params["subjectObservation__lt"] = subject_observation_lt

    params["subjectObservation__lte"] = subject_observation_lte

    params["subjectObservation__ob_id"] = subject_observation_ob_id

    json_subject_observation_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(subject_observation_ob_id_in, Unset):
        json_subject_observation_ob_id_in = ",".join(subject_observation_ob_id_in)

    params["subjectObservation__ob_id__in"] = json_subject_observation_ob_id_in

    params["subjectObservation__uuid"] = subject_observation_uuid

    json_subject_observation_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(subject_observation_uuid_in, Unset):
        json_subject_observation_uuid_in = ",".join(subject_observation_uuid_in)

    params["subjectObservation__uuid__in"] = json_subject_observation_uuid_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/relatedobservationinfos/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedRelatedObservationInfoReadList]:
    if response.status_code == 200:
        response_200 = PaginatedRelatedObservationInfoReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
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
    object_observation: Union[Unset, int] = UNSET,
    object_observation_gt: Union[Unset, int] = UNSET,
    object_observation_gte: Union[Unset, int] = UNSET,
    object_observation_in: Union[Unset, list[int]] = UNSET,
    object_observation_isnull: Union[Unset, bool] = UNSET,
    object_observation_lt: Union[Unset, int] = UNSET,
    object_observation_lte: Union[Unset, int] = UNSET,
    object_observation_uuid: Union[Unset, str] = UNSET,
    object_observation_uuid_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    relation_type: Union[Unset, RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs] = UNSET,
    relation_type_contains: Union[Unset, str] = UNSET,
    relation_type_endswith: Union[Unset, str] = UNSET,
    relation_type_gt: Union[Unset, str] = UNSET,
    relation_type_gte: Union[Unset, str] = UNSET,
    relation_type_icontains: Union[Unset, str] = UNSET,
    relation_type_iendswith: Union[Unset, str] = UNSET,
    relation_type_iexact: Union[Unset, str] = UNSET,
    relation_type_in: Union[Unset, list[str]] = UNSET,
    relation_type_iregex: Union[Unset, str] = UNSET,
    relation_type_isnull: Union[Unset, bool] = UNSET,
    relation_type_istartswith: Union[Unset, str] = UNSET,
    relation_type_lt: Union[Unset, str] = UNSET,
    relation_type_lte: Union[Unset, str] = UNSET,
    relation_type_range: Union[Unset, list[str]] = UNSET,
    relation_type_regex: Union[Unset, str] = UNSET,
    relation_type_startswith: Union[Unset, str] = UNSET,
    subject_observation: Union[Unset, int] = UNSET,
    subject_observation_gt: Union[Unset, int] = UNSET,
    subject_observation_gte: Union[Unset, int] = UNSET,
    subject_observation_in: Union[Unset, list[int]] = UNSET,
    subject_observation_isnull: Union[Unset, bool] = UNSET,
    subject_observation_lt: Union[Unset, int] = UNSET,
    subject_observation_lte: Union[Unset, int] = UNSET,
    subject_observation_ob_id: Union[Unset, int] = UNSET,
    subject_observation_ob_id_in: Union[Unset, list[int]] = UNSET,
    subject_observation_uuid: Union[Unset, str] = UNSET,
    subject_observation_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedRelatedObservationInfoReadList]:
    """Get a list of RelatedObservationInfo objects.

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
        object_observation (Union[Unset, int]):
        object_observation_gt (Union[Unset, int]):
        object_observation_gte (Union[Unset, int]):
        object_observation_in (Union[Unset, list[int]]):
        object_observation_isnull (Union[Unset, bool]):
        object_observation_lt (Union[Unset, int]):
        object_observation_lte (Union[Unset, int]):
        object_observation_uuid (Union[Unset, str]):
        object_observation_uuid_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        relation_type (Union[Unset,
            RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs]):
        relation_type_contains (Union[Unset, str]):
        relation_type_endswith (Union[Unset, str]):
        relation_type_gt (Union[Unset, str]):
        relation_type_gte (Union[Unset, str]):
        relation_type_icontains (Union[Unset, str]):
        relation_type_iendswith (Union[Unset, str]):
        relation_type_iexact (Union[Unset, str]):
        relation_type_in (Union[Unset, list[str]]):
        relation_type_iregex (Union[Unset, str]):
        relation_type_isnull (Union[Unset, bool]):
        relation_type_istartswith (Union[Unset, str]):
        relation_type_lt (Union[Unset, str]):
        relation_type_lte (Union[Unset, str]):
        relation_type_range (Union[Unset, list[str]]):
        relation_type_regex (Union[Unset, str]):
        relation_type_startswith (Union[Unset, str]):
        subject_observation (Union[Unset, int]):
        subject_observation_gt (Union[Unset, int]):
        subject_observation_gte (Union[Unset, int]):
        subject_observation_in (Union[Unset, list[int]]):
        subject_observation_isnull (Union[Unset, bool]):
        subject_observation_lt (Union[Unset, int]):
        subject_observation_lte (Union[Unset, int]):
        subject_observation_ob_id (Union[Unset, int]):
        subject_observation_ob_id_in (Union[Unset, list[int]]):
        subject_observation_uuid (Union[Unset, str]):
        subject_observation_uuid_in (Union[Unset, list[str]]):

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
    object_observation: Union[Unset, int] = UNSET,
    object_observation_gt: Union[Unset, int] = UNSET,
    object_observation_gte: Union[Unset, int] = UNSET,
    object_observation_in: Union[Unset, list[int]] = UNSET,
    object_observation_isnull: Union[Unset, bool] = UNSET,
    object_observation_lt: Union[Unset, int] = UNSET,
    object_observation_lte: Union[Unset, int] = UNSET,
    object_observation_uuid: Union[Unset, str] = UNSET,
    object_observation_uuid_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    relation_type: Union[Unset, RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs] = UNSET,
    relation_type_contains: Union[Unset, str] = UNSET,
    relation_type_endswith: Union[Unset, str] = UNSET,
    relation_type_gt: Union[Unset, str] = UNSET,
    relation_type_gte: Union[Unset, str] = UNSET,
    relation_type_icontains: Union[Unset, str] = UNSET,
    relation_type_iendswith: Union[Unset, str] = UNSET,
    relation_type_iexact: Union[Unset, str] = UNSET,
    relation_type_in: Union[Unset, list[str]] = UNSET,
    relation_type_iregex: Union[Unset, str] = UNSET,
    relation_type_isnull: Union[Unset, bool] = UNSET,
    relation_type_istartswith: Union[Unset, str] = UNSET,
    relation_type_lt: Union[Unset, str] = UNSET,
    relation_type_lte: Union[Unset, str] = UNSET,
    relation_type_range: Union[Unset, list[str]] = UNSET,
    relation_type_regex: Union[Unset, str] = UNSET,
    relation_type_startswith: Union[Unset, str] = UNSET,
    subject_observation: Union[Unset, int] = UNSET,
    subject_observation_gt: Union[Unset, int] = UNSET,
    subject_observation_gte: Union[Unset, int] = UNSET,
    subject_observation_in: Union[Unset, list[int]] = UNSET,
    subject_observation_isnull: Union[Unset, bool] = UNSET,
    subject_observation_lt: Union[Unset, int] = UNSET,
    subject_observation_lte: Union[Unset, int] = UNSET,
    subject_observation_ob_id: Union[Unset, int] = UNSET,
    subject_observation_ob_id_in: Union[Unset, list[int]] = UNSET,
    subject_observation_uuid: Union[Unset, str] = UNSET,
    subject_observation_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedRelatedObservationInfoReadList]:
    """Get a list of RelatedObservationInfo objects.

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
        object_observation (Union[Unset, int]):
        object_observation_gt (Union[Unset, int]):
        object_observation_gte (Union[Unset, int]):
        object_observation_in (Union[Unset, list[int]]):
        object_observation_isnull (Union[Unset, bool]):
        object_observation_lt (Union[Unset, int]):
        object_observation_lte (Union[Unset, int]):
        object_observation_uuid (Union[Unset, str]):
        object_observation_uuid_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        relation_type (Union[Unset,
            RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs]):
        relation_type_contains (Union[Unset, str]):
        relation_type_endswith (Union[Unset, str]):
        relation_type_gt (Union[Unset, str]):
        relation_type_gte (Union[Unset, str]):
        relation_type_icontains (Union[Unset, str]):
        relation_type_iendswith (Union[Unset, str]):
        relation_type_iexact (Union[Unset, str]):
        relation_type_in (Union[Unset, list[str]]):
        relation_type_iregex (Union[Unset, str]):
        relation_type_isnull (Union[Unset, bool]):
        relation_type_istartswith (Union[Unset, str]):
        relation_type_lt (Union[Unset, str]):
        relation_type_lte (Union[Unset, str]):
        relation_type_range (Union[Unset, list[str]]):
        relation_type_regex (Union[Unset, str]):
        relation_type_startswith (Union[Unset, str]):
        subject_observation (Union[Unset, int]):
        subject_observation_gt (Union[Unset, int]):
        subject_observation_gte (Union[Unset, int]):
        subject_observation_in (Union[Unset, list[int]]):
        subject_observation_isnull (Union[Unset, bool]):
        subject_observation_lt (Union[Unset, int]):
        subject_observation_lte (Union[Unset, int]):
        subject_observation_ob_id (Union[Unset, int]):
        subject_observation_ob_id_in (Union[Unset, list[int]]):
        subject_observation_uuid (Union[Unset, str]):
        subject_observation_uuid_in (Union[Unset, list[str]]):

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
    object_observation: Union[Unset, int] = UNSET,
    object_observation_gt: Union[Unset, int] = UNSET,
    object_observation_gte: Union[Unset, int] = UNSET,
    object_observation_in: Union[Unset, list[int]] = UNSET,
    object_observation_isnull: Union[Unset, bool] = UNSET,
    object_observation_lt: Union[Unset, int] = UNSET,
    object_observation_lte: Union[Unset, int] = UNSET,
    object_observation_uuid: Union[Unset, str] = UNSET,
    object_observation_uuid_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    relation_type: Union[Unset, RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs] = UNSET,
    relation_type_contains: Union[Unset, str] = UNSET,
    relation_type_endswith: Union[Unset, str] = UNSET,
    relation_type_gt: Union[Unset, str] = UNSET,
    relation_type_gte: Union[Unset, str] = UNSET,
    relation_type_icontains: Union[Unset, str] = UNSET,
    relation_type_iendswith: Union[Unset, str] = UNSET,
    relation_type_iexact: Union[Unset, str] = UNSET,
    relation_type_in: Union[Unset, list[str]] = UNSET,
    relation_type_iregex: Union[Unset, str] = UNSET,
    relation_type_isnull: Union[Unset, bool] = UNSET,
    relation_type_istartswith: Union[Unset, str] = UNSET,
    relation_type_lt: Union[Unset, str] = UNSET,
    relation_type_lte: Union[Unset, str] = UNSET,
    relation_type_range: Union[Unset, list[str]] = UNSET,
    relation_type_regex: Union[Unset, str] = UNSET,
    relation_type_startswith: Union[Unset, str] = UNSET,
    subject_observation: Union[Unset, int] = UNSET,
    subject_observation_gt: Union[Unset, int] = UNSET,
    subject_observation_gte: Union[Unset, int] = UNSET,
    subject_observation_in: Union[Unset, list[int]] = UNSET,
    subject_observation_isnull: Union[Unset, bool] = UNSET,
    subject_observation_lt: Union[Unset, int] = UNSET,
    subject_observation_lte: Union[Unset, int] = UNSET,
    subject_observation_ob_id: Union[Unset, int] = UNSET,
    subject_observation_ob_id_in: Union[Unset, list[int]] = UNSET,
    subject_observation_uuid: Union[Unset, str] = UNSET,
    subject_observation_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedRelatedObservationInfoReadList]:
    """Get a list of RelatedObservationInfo objects.

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
        object_observation (Union[Unset, int]):
        object_observation_gt (Union[Unset, int]):
        object_observation_gte (Union[Unset, int]):
        object_observation_in (Union[Unset, list[int]]):
        object_observation_isnull (Union[Unset, bool]):
        object_observation_lt (Union[Unset, int]):
        object_observation_lte (Union[Unset, int]):
        object_observation_uuid (Union[Unset, str]):
        object_observation_uuid_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        relation_type (Union[Unset,
            RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs]):
        relation_type_contains (Union[Unset, str]):
        relation_type_endswith (Union[Unset, str]):
        relation_type_gt (Union[Unset, str]):
        relation_type_gte (Union[Unset, str]):
        relation_type_icontains (Union[Unset, str]):
        relation_type_iendswith (Union[Unset, str]):
        relation_type_iexact (Union[Unset, str]):
        relation_type_in (Union[Unset, list[str]]):
        relation_type_iregex (Union[Unset, str]):
        relation_type_isnull (Union[Unset, bool]):
        relation_type_istartswith (Union[Unset, str]):
        relation_type_lt (Union[Unset, str]):
        relation_type_lte (Union[Unset, str]):
        relation_type_range (Union[Unset, list[str]]):
        relation_type_regex (Union[Unset, str]):
        relation_type_startswith (Union[Unset, str]):
        subject_observation (Union[Unset, int]):
        subject_observation_gt (Union[Unset, int]):
        subject_observation_gte (Union[Unset, int]):
        subject_observation_in (Union[Unset, list[int]]):
        subject_observation_isnull (Union[Unset, bool]):
        subject_observation_lt (Union[Unset, int]):
        subject_observation_lte (Union[Unset, int]):
        subject_observation_ob_id (Union[Unset, int]):
        subject_observation_ob_id_in (Union[Unset, list[int]]):
        subject_observation_uuid (Union[Unset, str]):
        subject_observation_uuid_in (Union[Unset, list[str]]):

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
    object_observation: Union[Unset, int] = UNSET,
    object_observation_gt: Union[Unset, int] = UNSET,
    object_observation_gte: Union[Unset, int] = UNSET,
    object_observation_in: Union[Unset, list[int]] = UNSET,
    object_observation_isnull: Union[Unset, bool] = UNSET,
    object_observation_lt: Union[Unset, int] = UNSET,
    object_observation_lte: Union[Unset, int] = UNSET,
    object_observation_uuid: Union[Unset, str] = UNSET,
    object_observation_uuid_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    relation_type: Union[Unset, RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs] = UNSET,
    relation_type_contains: Union[Unset, str] = UNSET,
    relation_type_endswith: Union[Unset, str] = UNSET,
    relation_type_gt: Union[Unset, str] = UNSET,
    relation_type_gte: Union[Unset, str] = UNSET,
    relation_type_icontains: Union[Unset, str] = UNSET,
    relation_type_iendswith: Union[Unset, str] = UNSET,
    relation_type_iexact: Union[Unset, str] = UNSET,
    relation_type_in: Union[Unset, list[str]] = UNSET,
    relation_type_iregex: Union[Unset, str] = UNSET,
    relation_type_isnull: Union[Unset, bool] = UNSET,
    relation_type_istartswith: Union[Unset, str] = UNSET,
    relation_type_lt: Union[Unset, str] = UNSET,
    relation_type_lte: Union[Unset, str] = UNSET,
    relation_type_range: Union[Unset, list[str]] = UNSET,
    relation_type_regex: Union[Unset, str] = UNSET,
    relation_type_startswith: Union[Unset, str] = UNSET,
    subject_observation: Union[Unset, int] = UNSET,
    subject_observation_gt: Union[Unset, int] = UNSET,
    subject_observation_gte: Union[Unset, int] = UNSET,
    subject_observation_in: Union[Unset, list[int]] = UNSET,
    subject_observation_isnull: Union[Unset, bool] = UNSET,
    subject_observation_lt: Union[Unset, int] = UNSET,
    subject_observation_lte: Union[Unset, int] = UNSET,
    subject_observation_ob_id: Union[Unset, int] = UNSET,
    subject_observation_ob_id_in: Union[Unset, list[int]] = UNSET,
    subject_observation_uuid: Union[Unset, str] = UNSET,
    subject_observation_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedRelatedObservationInfoReadList]:
    """Get a list of RelatedObservationInfo objects.

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
        object_observation (Union[Unset, int]):
        object_observation_gt (Union[Unset, int]):
        object_observation_gte (Union[Unset, int]):
        object_observation_in (Union[Unset, list[int]]):
        object_observation_isnull (Union[Unset, bool]):
        object_observation_lt (Union[Unset, int]):
        object_observation_lte (Union[Unset, int]):
        object_observation_uuid (Union[Unset, str]):
        object_observation_uuid_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        relation_type (Union[Unset,
            RelatedobservationinfosListRelationTypeBetweenSubjectAndObjectObs]):
        relation_type_contains (Union[Unset, str]):
        relation_type_endswith (Union[Unset, str]):
        relation_type_gt (Union[Unset, str]):
        relation_type_gte (Union[Unset, str]):
        relation_type_icontains (Union[Unset, str]):
        relation_type_iendswith (Union[Unset, str]):
        relation_type_iexact (Union[Unset, str]):
        relation_type_in (Union[Unset, list[str]]):
        relation_type_iregex (Union[Unset, str]):
        relation_type_isnull (Union[Unset, bool]):
        relation_type_istartswith (Union[Unset, str]):
        relation_type_lt (Union[Unset, str]):
        relation_type_lte (Union[Unset, str]):
        relation_type_range (Union[Unset, list[str]]):
        relation_type_regex (Union[Unset, str]):
        relation_type_startswith (Union[Unset, str]):
        subject_observation (Union[Unset, int]):
        subject_observation_gt (Union[Unset, int]):
        subject_observation_gte (Union[Unset, int]):
        subject_observation_in (Union[Unset, list[int]]):
        subject_observation_isnull (Union[Unset, bool]):
        subject_observation_lt (Union[Unset, int]):
        subject_observation_lte (Union[Unset, int]):
        subject_observation_ob_id (Union[Unset, int]):
        subject_observation_ob_id_in (Union[Unset, list[int]]):
        subject_observation_uuid (Union[Unset, str]):
        subject_observation_uuid_in (Union[Unset, list[str]]):

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
