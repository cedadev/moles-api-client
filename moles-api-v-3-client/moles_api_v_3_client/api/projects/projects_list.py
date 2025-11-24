from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_project_read_list import PaginatedProjectReadList
from ...models.projects_list_project_status import ProjectsListProjectStatus
from ...models.projects_list_publication_state import ProjectsListPublicationState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    keywords: str | Unset = UNSET,
    keywords_contains: str | Unset = UNSET,
    keywords_endswith: str | Unset = UNSET,
    keywords_gt: str | Unset = UNSET,
    keywords_gte: str | Unset = UNSET,
    keywords_icontains: str | Unset = UNSET,
    keywords_iendswith: str | Unset = UNSET,
    keywords_iexact: str | Unset = UNSET,
    keywords_in: list[str] | Unset = UNSET,
    keywords_iregex: str | Unset = UNSET,
    keywords_isnull: bool | Unset = UNSET,
    keywords_istartswith: str | Unset = UNSET,
    keywords_lt: str | Unset = UNSET,
    keywords_lte: str | Unset = UNSET,
    keywords_range: list[str] | Unset = UNSET,
    keywords_regex: str | Unset = UNSET,
    keywords_startswith: str | Unset = UNSET,
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
    observation_collection_ob_id: int | Unset = UNSET,
    observation_collection_ob_id_in: list[int] | Unset = UNSET,
    observation_collection_title: str | Unset = UNSET,
    observation_collection_title_contains: str | Unset = UNSET,
    observation_collection_uuid: str | Unset = UNSET,
    observation_collection_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    parent_project: int | Unset = UNSET,
    parent_project_gt: int | Unset = UNSET,
    parent_project_gte: int | Unset = UNSET,
    parent_project_in: list[int] | Unset = UNSET,
    parent_project_isnull: bool | Unset = UNSET,
    parent_project_lt: int | Unset = UNSET,
    parent_project_lte: int | Unset = UNSET,
    publication_state: ProjectsListPublicationState | Unset = UNSET,
    publication_state_contains: str | Unset = UNSET,
    publication_state_endswith: str | Unset = UNSET,
    publication_state_gt: str | Unset = UNSET,
    publication_state_gte: str | Unset = UNSET,
    publication_state_icontains: str | Unset = UNSET,
    publication_state_iendswith: str | Unset = UNSET,
    publication_state_iexact: str | Unset = UNSET,
    publication_state_in: list[str] | Unset = UNSET,
    publication_state_iregex: str | Unset = UNSET,
    publication_state_isnull: bool | Unset = UNSET,
    publication_state_istartswith: str | Unset = UNSET,
    publication_state_lt: str | Unset = UNSET,
    publication_state_lte: str | Unset = UNSET,
    publication_state_range: list[str] | Unset = UNSET,
    publication_state_regex: str | Unset = UNSET,
    publication_state_startswith: str | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_gt: int | Unset = UNSET,
    referenceable_ptr_gte: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    referenceable_ptr_lt: int | Unset = UNSET,
    referenceable_ptr_lte: int | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    status: ProjectsListProjectStatus | Unset = UNSET,
    status_contains: str | Unset = UNSET,
    status_endswith: str | Unset = UNSET,
    status_gt: str | Unset = UNSET,
    status_gte: str | Unset = UNSET,
    status_icontains: str | Unset = UNSET,
    status_iendswith: str | Unset = UNSET,
    status_iexact: str | Unset = UNSET,
    status_in: list[str] | Unset = UNSET,
    status_iregex: str | Unset = UNSET,
    status_isnull: bool | Unset = UNSET,
    status_istartswith: str | Unset = UNSET,
    status_lt: str | Unset = UNSET,
    status_lte: str | Unset = UNSET,
    status_range: list[str] | Unset = UNSET,
    status_regex: str | Unset = UNSET,
    status_startswith: str | Unset = UNSET,
    sub_project_ob_id: int | Unset = UNSET,
    sub_project_ob_id_in: list[int] | Unset = UNSET,
    sub_project_title: str | Unset = UNSET,
    sub_project_title_contains: str | Unset = UNSET,
    sub_project_title_in: list[str] | Unset = UNSET,
    sub_project_uuid: str | Unset = UNSET,
    sub_project_uuid_in: list[str] | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
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

    json_abstract_in: list[str] | Unset = UNSET
    if not isinstance(abstract_in, Unset):
        json_abstract_in = ",".join(map(str, abstract_in))

    params["abstract__in"] = json_abstract_in

    params["abstract__iregex"] = abstract_iregex

    params["abstract__isnull"] = abstract_isnull

    params["abstract__istartswith"] = abstract_istartswith

    params["abstract__lt"] = abstract_lt

    params["abstract__lte"] = abstract_lte

    json_abstract_range: list[str] | Unset = UNSET
    if not isinstance(abstract_range, Unset):
        json_abstract_range = ",".join(map(str, abstract_range))

    params["abstract__range"] = json_abstract_range

    params["abstract__regex"] = abstract_regex

    params["abstract__startswith"] = abstract_startswith

    params["keywords"] = keywords

    params["keywords__contains"] = keywords_contains

    params["keywords__endswith"] = keywords_endswith

    params["keywords__gt"] = keywords_gt

    params["keywords__gte"] = keywords_gte

    params["keywords__icontains"] = keywords_icontains

    params["keywords__iendswith"] = keywords_iendswith

    params["keywords__iexact"] = keywords_iexact

    json_keywords_in: list[str] | Unset = UNSET
    if not isinstance(keywords_in, Unset):
        json_keywords_in = ",".join(map(str, keywords_in))

    params["keywords__in"] = json_keywords_in

    params["keywords__iregex"] = keywords_iregex

    params["keywords__isnull"] = keywords_isnull

    params["keywords__istartswith"] = keywords_istartswith

    params["keywords__lt"] = keywords_lt

    params["keywords__lte"] = keywords_lte

    json_keywords_range: list[str] | Unset = UNSET
    if not isinstance(keywords_range, Unset):
        json_keywords_range = ",".join(map(str, keywords_range))

    params["keywords__range"] = json_keywords_range

    params["keywords__regex"] = keywords_regex

    params["keywords__startswith"] = keywords_startswith

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

    params["observationCollection__ob_id"] = observation_collection_ob_id

    json_observation_collection_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(observation_collection_ob_id_in, Unset):
        json_observation_collection_ob_id_in = ",".join(map(str, observation_collection_ob_id_in))

    params["observationCollection__ob_id__in"] = json_observation_collection_ob_id_in

    params["observationCollection__title"] = observation_collection_title

    params["observationCollection__title__contains"] = observation_collection_title_contains

    params["observationCollection__uuid"] = observation_collection_uuid

    json_observation_collection_uuid_in: list[str] | Unset = UNSET
    if not isinstance(observation_collection_uuid_in, Unset):
        json_observation_collection_uuid_in = ",".join(map(str, observation_collection_uuid_in))

    params["observationCollection__uuid__in"] = json_observation_collection_uuid_in

    params["offset"] = offset

    params["ordering"] = ordering

    params["parentProject"] = parent_project

    params["parentProject__gt"] = parent_project_gt

    params["parentProject__gte"] = parent_project_gte

    json_parent_project_in: list[int] | Unset = UNSET
    if not isinstance(parent_project_in, Unset):
        json_parent_project_in = ",".join(map(str, parent_project_in))

    params["parentProject__in"] = json_parent_project_in

    params["parentProject__isnull"] = parent_project_isnull

    params["parentProject__lt"] = parent_project_lt

    params["parentProject__lte"] = parent_project_lte

    json_publication_state: str | Unset = UNSET
    if not isinstance(publication_state, Unset):
        json_publication_state = publication_state.value

    params["publicationState"] = json_publication_state

    params["publicationState__contains"] = publication_state_contains

    params["publicationState__endswith"] = publication_state_endswith

    params["publicationState__gt"] = publication_state_gt

    params["publicationState__gte"] = publication_state_gte

    params["publicationState__icontains"] = publication_state_icontains

    params["publicationState__iendswith"] = publication_state_iendswith

    params["publicationState__iexact"] = publication_state_iexact

    json_publication_state_in: list[str] | Unset = UNSET
    if not isinstance(publication_state_in, Unset):
        json_publication_state_in = ",".join(map(str, publication_state_in))

    params["publicationState__in"] = json_publication_state_in

    params["publicationState__iregex"] = publication_state_iregex

    params["publicationState__isnull"] = publication_state_isnull

    params["publicationState__istartswith"] = publication_state_istartswith

    params["publicationState__lt"] = publication_state_lt

    params["publicationState__lte"] = publication_state_lte

    json_publication_state_range: list[str] | Unset = UNSET
    if not isinstance(publication_state_range, Unset):
        json_publication_state_range = ",".join(map(str, publication_state_range))

    params["publicationState__range"] = json_publication_state_range

    params["publicationState__regex"] = publication_state_regex

    params["publicationState__startswith"] = publication_state_startswith

    params["referenceable_ptr"] = referenceable_ptr

    params["referenceable_ptr__gt"] = referenceable_ptr_gt

    params["referenceable_ptr__gte"] = referenceable_ptr_gte

    json_referenceable_ptr_in: list[int] | Unset = UNSET
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

    json_short_code_in: list[str] | Unset = UNSET
    if not isinstance(short_code_in, Unset):
        json_short_code_in = ",".join(map(str, short_code_in))

    params["short_code__in"] = json_short_code_in

    params["short_code__iregex"] = short_code_iregex

    params["short_code__isnull"] = short_code_isnull

    params["short_code__istartswith"] = short_code_istartswith

    params["short_code__lt"] = short_code_lt

    params["short_code__lte"] = short_code_lte

    json_short_code_range: list[str] | Unset = UNSET
    if not isinstance(short_code_range, Unset):
        json_short_code_range = ",".join(map(str, short_code_range))

    params["short_code__range"] = json_short_code_range

    params["short_code__regex"] = short_code_regex

    params["short_code__startswith"] = short_code_startswith

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["status__contains"] = status_contains

    params["status__endswith"] = status_endswith

    params["status__gt"] = status_gt

    params["status__gte"] = status_gte

    params["status__icontains"] = status_icontains

    params["status__iendswith"] = status_iendswith

    params["status__iexact"] = status_iexact

    json_status_in: list[str] | Unset = UNSET
    if not isinstance(status_in, Unset):
        json_status_in = ",".join(map(str, status_in))

    params["status__in"] = json_status_in

    params["status__iregex"] = status_iregex

    params["status__isnull"] = status_isnull

    params["status__istartswith"] = status_istartswith

    params["status__lt"] = status_lt

    params["status__lte"] = status_lte

    json_status_range: list[str] | Unset = UNSET
    if not isinstance(status_range, Unset):
        json_status_range = ",".join(map(str, status_range))

    params["status__range"] = json_status_range

    params["status__regex"] = status_regex

    params["status__startswith"] = status_startswith

    params["subProject__ob_id"] = sub_project_ob_id

    json_sub_project_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(sub_project_ob_id_in, Unset):
        json_sub_project_ob_id_in = ",".join(map(str, sub_project_ob_id_in))

    params["subProject__ob_id__in"] = json_sub_project_ob_id_in

    params["subProject__title"] = sub_project_title

    params["subProject__title__contains"] = sub_project_title_contains

    json_sub_project_title_in: list[str] | Unset = UNSET
    if not isinstance(sub_project_title_in, Unset):
        json_sub_project_title_in = ",".join(map(str, sub_project_title_in))

    params["subProject__title__in"] = json_sub_project_title_in

    params["subProject__uuid"] = sub_project_uuid

    json_sub_project_uuid_in: list[str] | Unset = UNSET
    if not isinstance(sub_project_uuid_in, Unset):
        json_sub_project_uuid_in = ",".join(map(str, sub_project_uuid_in))

    params["subProject__uuid__in"] = json_sub_project_uuid_in

    params["title"] = title

    params["title__contains"] = title_contains

    params["title__endswith"] = title_endswith

    params["title__gt"] = title_gt

    params["title__gte"] = title_gte

    params["title__icontains"] = title_icontains

    params["title__iendswith"] = title_iendswith

    params["title__iexact"] = title_iexact

    json_title_in: list[str] | Unset = UNSET
    if not isinstance(title_in, Unset):
        json_title_in = ",".join(map(str, title_in))

    params["title__in"] = json_title_in

    params["title__iregex"] = title_iregex

    params["title__isnull"] = title_isnull

    params["title__istartswith"] = title_istartswith

    params["title__lt"] = title_lt

    params["title__lte"] = title_lte

    json_title_range: list[str] | Unset = UNSET
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

    json_uuid_in: list[str] | Unset = UNSET
    if not isinstance(uuid_in, Unset):
        json_uuid_in = ",".join(map(str, uuid_in))

    params["uuid__in"] = json_uuid_in

    params["uuid__iregex"] = uuid_iregex

    params["uuid__isnull"] = uuid_isnull

    params["uuid__istartswith"] = uuid_istartswith

    params["uuid__lt"] = uuid_lt

    params["uuid__lte"] = uuid_lte

    json_uuid_range: list[str] | Unset = UNSET
    if not isinstance(uuid_range, Unset):
        json_uuid_range = ",".join(map(str, uuid_range))

    params["uuid__range"] = json_uuid_range

    params["uuid__regex"] = uuid_regex

    params["uuid__startswith"] = uuid_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/projects/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedProjectReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedProjectReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedProjectReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    keywords: str | Unset = UNSET,
    keywords_contains: str | Unset = UNSET,
    keywords_endswith: str | Unset = UNSET,
    keywords_gt: str | Unset = UNSET,
    keywords_gte: str | Unset = UNSET,
    keywords_icontains: str | Unset = UNSET,
    keywords_iendswith: str | Unset = UNSET,
    keywords_iexact: str | Unset = UNSET,
    keywords_in: list[str] | Unset = UNSET,
    keywords_iregex: str | Unset = UNSET,
    keywords_isnull: bool | Unset = UNSET,
    keywords_istartswith: str | Unset = UNSET,
    keywords_lt: str | Unset = UNSET,
    keywords_lte: str | Unset = UNSET,
    keywords_range: list[str] | Unset = UNSET,
    keywords_regex: str | Unset = UNSET,
    keywords_startswith: str | Unset = UNSET,
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
    observation_collection_ob_id: int | Unset = UNSET,
    observation_collection_ob_id_in: list[int] | Unset = UNSET,
    observation_collection_title: str | Unset = UNSET,
    observation_collection_title_contains: str | Unset = UNSET,
    observation_collection_uuid: str | Unset = UNSET,
    observation_collection_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    parent_project: int | Unset = UNSET,
    parent_project_gt: int | Unset = UNSET,
    parent_project_gte: int | Unset = UNSET,
    parent_project_in: list[int] | Unset = UNSET,
    parent_project_isnull: bool | Unset = UNSET,
    parent_project_lt: int | Unset = UNSET,
    parent_project_lte: int | Unset = UNSET,
    publication_state: ProjectsListPublicationState | Unset = UNSET,
    publication_state_contains: str | Unset = UNSET,
    publication_state_endswith: str | Unset = UNSET,
    publication_state_gt: str | Unset = UNSET,
    publication_state_gte: str | Unset = UNSET,
    publication_state_icontains: str | Unset = UNSET,
    publication_state_iendswith: str | Unset = UNSET,
    publication_state_iexact: str | Unset = UNSET,
    publication_state_in: list[str] | Unset = UNSET,
    publication_state_iregex: str | Unset = UNSET,
    publication_state_isnull: bool | Unset = UNSET,
    publication_state_istartswith: str | Unset = UNSET,
    publication_state_lt: str | Unset = UNSET,
    publication_state_lte: str | Unset = UNSET,
    publication_state_range: list[str] | Unset = UNSET,
    publication_state_regex: str | Unset = UNSET,
    publication_state_startswith: str | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_gt: int | Unset = UNSET,
    referenceable_ptr_gte: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    referenceable_ptr_lt: int | Unset = UNSET,
    referenceable_ptr_lte: int | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    status: ProjectsListProjectStatus | Unset = UNSET,
    status_contains: str | Unset = UNSET,
    status_endswith: str | Unset = UNSET,
    status_gt: str | Unset = UNSET,
    status_gte: str | Unset = UNSET,
    status_icontains: str | Unset = UNSET,
    status_iendswith: str | Unset = UNSET,
    status_iexact: str | Unset = UNSET,
    status_in: list[str] | Unset = UNSET,
    status_iregex: str | Unset = UNSET,
    status_isnull: bool | Unset = UNSET,
    status_istartswith: str | Unset = UNSET,
    status_lt: str | Unset = UNSET,
    status_lte: str | Unset = UNSET,
    status_range: list[str] | Unset = UNSET,
    status_regex: str | Unset = UNSET,
    status_startswith: str | Unset = UNSET,
    sub_project_ob_id: int | Unset = UNSET,
    sub_project_ob_id_in: list[int] | Unset = UNSET,
    sub_project_title: str | Unset = UNSET,
    sub_project_title_contains: str | Unset = UNSET,
    sub_project_title_in: list[str] | Unset = UNSET,
    sub_project_uuid: str | Unset = UNSET,
    sub_project_uuid_in: list[str] | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> Response[PaginatedProjectReadList]:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        keywords (str | Unset):
        keywords_contains (str | Unset):
        keywords_endswith (str | Unset):
        keywords_gt (str | Unset):
        keywords_gte (str | Unset):
        keywords_icontains (str | Unset):
        keywords_iendswith (str | Unset):
        keywords_iexact (str | Unset):
        keywords_in (list[str] | Unset):
        keywords_iregex (str | Unset):
        keywords_isnull (bool | Unset):
        keywords_istartswith (str | Unset):
        keywords_lt (str | Unset):
        keywords_lte (str | Unset):
        keywords_range (list[str] | Unset):
        keywords_regex (str | Unset):
        keywords_startswith (str | Unset):
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
        observation_collection_ob_id (int | Unset):
        observation_collection_ob_id_in (list[int] | Unset):
        observation_collection_title (str | Unset):
        observation_collection_title_contains (str | Unset):
        observation_collection_uuid (str | Unset):
        observation_collection_uuid_in (list[str] | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        parent_project (int | Unset):
        parent_project_gt (int | Unset):
        parent_project_gte (int | Unset):
        parent_project_in (list[int] | Unset):
        parent_project_isnull (bool | Unset):
        parent_project_lt (int | Unset):
        parent_project_lte (int | Unset):
        publication_state (ProjectsListPublicationState | Unset):
        publication_state_contains (str | Unset):
        publication_state_endswith (str | Unset):
        publication_state_gt (str | Unset):
        publication_state_gte (str | Unset):
        publication_state_icontains (str | Unset):
        publication_state_iendswith (str | Unset):
        publication_state_iexact (str | Unset):
        publication_state_in (list[str] | Unset):
        publication_state_iregex (str | Unset):
        publication_state_isnull (bool | Unset):
        publication_state_istartswith (str | Unset):
        publication_state_lt (str | Unset):
        publication_state_lte (str | Unset):
        publication_state_range (list[str] | Unset):
        publication_state_regex (str | Unset):
        publication_state_startswith (str | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_gt (int | Unset):
        referenceable_ptr_gte (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        referenceable_ptr_lt (int | Unset):
        referenceable_ptr_lte (int | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        status (ProjectsListProjectStatus | Unset):
        status_contains (str | Unset):
        status_endswith (str | Unset):
        status_gt (str | Unset):
        status_gte (str | Unset):
        status_icontains (str | Unset):
        status_iendswith (str | Unset):
        status_iexact (str | Unset):
        status_in (list[str] | Unset):
        status_iregex (str | Unset):
        status_isnull (bool | Unset):
        status_istartswith (str | Unset):
        status_lt (str | Unset):
        status_lte (str | Unset):
        status_range (list[str] | Unset):
        status_regex (str | Unset):
        status_startswith (str | Unset):
        sub_project_ob_id (int | Unset):
        sub_project_ob_id_in (list[int] | Unset):
        sub_project_title (str | Unset):
        sub_project_title_contains (str | Unset):
        sub_project_title_in (list[str] | Unset):
        sub_project_uuid (str | Unset):
        sub_project_uuid_in (list[str] | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProjectReadList]
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
        keywords=keywords,
        keywords_contains=keywords_contains,
        keywords_endswith=keywords_endswith,
        keywords_gt=keywords_gt,
        keywords_gte=keywords_gte,
        keywords_icontains=keywords_icontains,
        keywords_iendswith=keywords_iendswith,
        keywords_iexact=keywords_iexact,
        keywords_in=keywords_in,
        keywords_iregex=keywords_iregex,
        keywords_isnull=keywords_isnull,
        keywords_istartswith=keywords_istartswith,
        keywords_lt=keywords_lt,
        keywords_lte=keywords_lte,
        keywords_range=keywords_range,
        keywords_regex=keywords_regex,
        keywords_startswith=keywords_startswith,
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
        observation_collection_ob_id=observation_collection_ob_id,
        observation_collection_ob_id_in=observation_collection_ob_id_in,
        observation_collection_title=observation_collection_title,
        observation_collection_title_contains=observation_collection_title_contains,
        observation_collection_uuid=observation_collection_uuid,
        observation_collection_uuid_in=observation_collection_uuid_in,
        offset=offset,
        ordering=ordering,
        parent_project=parent_project,
        parent_project_gt=parent_project_gt,
        parent_project_gte=parent_project_gte,
        parent_project_in=parent_project_in,
        parent_project_isnull=parent_project_isnull,
        parent_project_lt=parent_project_lt,
        parent_project_lte=parent_project_lte,
        publication_state=publication_state,
        publication_state_contains=publication_state_contains,
        publication_state_endswith=publication_state_endswith,
        publication_state_gt=publication_state_gt,
        publication_state_gte=publication_state_gte,
        publication_state_icontains=publication_state_icontains,
        publication_state_iendswith=publication_state_iendswith,
        publication_state_iexact=publication_state_iexact,
        publication_state_in=publication_state_in,
        publication_state_iregex=publication_state_iregex,
        publication_state_isnull=publication_state_isnull,
        publication_state_istartswith=publication_state_istartswith,
        publication_state_lt=publication_state_lt,
        publication_state_lte=publication_state_lte,
        publication_state_range=publication_state_range,
        publication_state_regex=publication_state_regex,
        publication_state_startswith=publication_state_startswith,
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
        status=status,
        status_contains=status_contains,
        status_endswith=status_endswith,
        status_gt=status_gt,
        status_gte=status_gte,
        status_icontains=status_icontains,
        status_iendswith=status_iendswith,
        status_iexact=status_iexact,
        status_in=status_in,
        status_iregex=status_iregex,
        status_isnull=status_isnull,
        status_istartswith=status_istartswith,
        status_lt=status_lt,
        status_lte=status_lte,
        status_range=status_range,
        status_regex=status_regex,
        status_startswith=status_startswith,
        sub_project_ob_id=sub_project_ob_id,
        sub_project_ob_id_in=sub_project_ob_id_in,
        sub_project_title=sub_project_title,
        sub_project_title_contains=sub_project_title_contains,
        sub_project_title_in=sub_project_title_in,
        sub_project_uuid=sub_project_uuid,
        sub_project_uuid_in=sub_project_uuid_in,
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
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    keywords: str | Unset = UNSET,
    keywords_contains: str | Unset = UNSET,
    keywords_endswith: str | Unset = UNSET,
    keywords_gt: str | Unset = UNSET,
    keywords_gte: str | Unset = UNSET,
    keywords_icontains: str | Unset = UNSET,
    keywords_iendswith: str | Unset = UNSET,
    keywords_iexact: str | Unset = UNSET,
    keywords_in: list[str] | Unset = UNSET,
    keywords_iregex: str | Unset = UNSET,
    keywords_isnull: bool | Unset = UNSET,
    keywords_istartswith: str | Unset = UNSET,
    keywords_lt: str | Unset = UNSET,
    keywords_lte: str | Unset = UNSET,
    keywords_range: list[str] | Unset = UNSET,
    keywords_regex: str | Unset = UNSET,
    keywords_startswith: str | Unset = UNSET,
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
    observation_collection_ob_id: int | Unset = UNSET,
    observation_collection_ob_id_in: list[int] | Unset = UNSET,
    observation_collection_title: str | Unset = UNSET,
    observation_collection_title_contains: str | Unset = UNSET,
    observation_collection_uuid: str | Unset = UNSET,
    observation_collection_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    parent_project: int | Unset = UNSET,
    parent_project_gt: int | Unset = UNSET,
    parent_project_gte: int | Unset = UNSET,
    parent_project_in: list[int] | Unset = UNSET,
    parent_project_isnull: bool | Unset = UNSET,
    parent_project_lt: int | Unset = UNSET,
    parent_project_lte: int | Unset = UNSET,
    publication_state: ProjectsListPublicationState | Unset = UNSET,
    publication_state_contains: str | Unset = UNSET,
    publication_state_endswith: str | Unset = UNSET,
    publication_state_gt: str | Unset = UNSET,
    publication_state_gte: str | Unset = UNSET,
    publication_state_icontains: str | Unset = UNSET,
    publication_state_iendswith: str | Unset = UNSET,
    publication_state_iexact: str | Unset = UNSET,
    publication_state_in: list[str] | Unset = UNSET,
    publication_state_iregex: str | Unset = UNSET,
    publication_state_isnull: bool | Unset = UNSET,
    publication_state_istartswith: str | Unset = UNSET,
    publication_state_lt: str | Unset = UNSET,
    publication_state_lte: str | Unset = UNSET,
    publication_state_range: list[str] | Unset = UNSET,
    publication_state_regex: str | Unset = UNSET,
    publication_state_startswith: str | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_gt: int | Unset = UNSET,
    referenceable_ptr_gte: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    referenceable_ptr_lt: int | Unset = UNSET,
    referenceable_ptr_lte: int | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    status: ProjectsListProjectStatus | Unset = UNSET,
    status_contains: str | Unset = UNSET,
    status_endswith: str | Unset = UNSET,
    status_gt: str | Unset = UNSET,
    status_gte: str | Unset = UNSET,
    status_icontains: str | Unset = UNSET,
    status_iendswith: str | Unset = UNSET,
    status_iexact: str | Unset = UNSET,
    status_in: list[str] | Unset = UNSET,
    status_iregex: str | Unset = UNSET,
    status_isnull: bool | Unset = UNSET,
    status_istartswith: str | Unset = UNSET,
    status_lt: str | Unset = UNSET,
    status_lte: str | Unset = UNSET,
    status_range: list[str] | Unset = UNSET,
    status_regex: str | Unset = UNSET,
    status_startswith: str | Unset = UNSET,
    sub_project_ob_id: int | Unset = UNSET,
    sub_project_ob_id_in: list[int] | Unset = UNSET,
    sub_project_title: str | Unset = UNSET,
    sub_project_title_contains: str | Unset = UNSET,
    sub_project_title_in: list[str] | Unset = UNSET,
    sub_project_uuid: str | Unset = UNSET,
    sub_project_uuid_in: list[str] | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> PaginatedProjectReadList | None:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        keywords (str | Unset):
        keywords_contains (str | Unset):
        keywords_endswith (str | Unset):
        keywords_gt (str | Unset):
        keywords_gte (str | Unset):
        keywords_icontains (str | Unset):
        keywords_iendswith (str | Unset):
        keywords_iexact (str | Unset):
        keywords_in (list[str] | Unset):
        keywords_iregex (str | Unset):
        keywords_isnull (bool | Unset):
        keywords_istartswith (str | Unset):
        keywords_lt (str | Unset):
        keywords_lte (str | Unset):
        keywords_range (list[str] | Unset):
        keywords_regex (str | Unset):
        keywords_startswith (str | Unset):
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
        observation_collection_ob_id (int | Unset):
        observation_collection_ob_id_in (list[int] | Unset):
        observation_collection_title (str | Unset):
        observation_collection_title_contains (str | Unset):
        observation_collection_uuid (str | Unset):
        observation_collection_uuid_in (list[str] | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        parent_project (int | Unset):
        parent_project_gt (int | Unset):
        parent_project_gte (int | Unset):
        parent_project_in (list[int] | Unset):
        parent_project_isnull (bool | Unset):
        parent_project_lt (int | Unset):
        parent_project_lte (int | Unset):
        publication_state (ProjectsListPublicationState | Unset):
        publication_state_contains (str | Unset):
        publication_state_endswith (str | Unset):
        publication_state_gt (str | Unset):
        publication_state_gte (str | Unset):
        publication_state_icontains (str | Unset):
        publication_state_iendswith (str | Unset):
        publication_state_iexact (str | Unset):
        publication_state_in (list[str] | Unset):
        publication_state_iregex (str | Unset):
        publication_state_isnull (bool | Unset):
        publication_state_istartswith (str | Unset):
        publication_state_lt (str | Unset):
        publication_state_lte (str | Unset):
        publication_state_range (list[str] | Unset):
        publication_state_regex (str | Unset):
        publication_state_startswith (str | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_gt (int | Unset):
        referenceable_ptr_gte (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        referenceable_ptr_lt (int | Unset):
        referenceable_ptr_lte (int | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        status (ProjectsListProjectStatus | Unset):
        status_contains (str | Unset):
        status_endswith (str | Unset):
        status_gt (str | Unset):
        status_gte (str | Unset):
        status_icontains (str | Unset):
        status_iendswith (str | Unset):
        status_iexact (str | Unset):
        status_in (list[str] | Unset):
        status_iregex (str | Unset):
        status_isnull (bool | Unset):
        status_istartswith (str | Unset):
        status_lt (str | Unset):
        status_lte (str | Unset):
        status_range (list[str] | Unset):
        status_regex (str | Unset):
        status_startswith (str | Unset):
        sub_project_ob_id (int | Unset):
        sub_project_ob_id_in (list[int] | Unset):
        sub_project_title (str | Unset):
        sub_project_title_contains (str | Unset):
        sub_project_title_in (list[str] | Unset):
        sub_project_uuid (str | Unset):
        sub_project_uuid_in (list[str] | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProjectReadList
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
        keywords=keywords,
        keywords_contains=keywords_contains,
        keywords_endswith=keywords_endswith,
        keywords_gt=keywords_gt,
        keywords_gte=keywords_gte,
        keywords_icontains=keywords_icontains,
        keywords_iendswith=keywords_iendswith,
        keywords_iexact=keywords_iexact,
        keywords_in=keywords_in,
        keywords_iregex=keywords_iregex,
        keywords_isnull=keywords_isnull,
        keywords_istartswith=keywords_istartswith,
        keywords_lt=keywords_lt,
        keywords_lte=keywords_lte,
        keywords_range=keywords_range,
        keywords_regex=keywords_regex,
        keywords_startswith=keywords_startswith,
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
        observation_collection_ob_id=observation_collection_ob_id,
        observation_collection_ob_id_in=observation_collection_ob_id_in,
        observation_collection_title=observation_collection_title,
        observation_collection_title_contains=observation_collection_title_contains,
        observation_collection_uuid=observation_collection_uuid,
        observation_collection_uuid_in=observation_collection_uuid_in,
        offset=offset,
        ordering=ordering,
        parent_project=parent_project,
        parent_project_gt=parent_project_gt,
        parent_project_gte=parent_project_gte,
        parent_project_in=parent_project_in,
        parent_project_isnull=parent_project_isnull,
        parent_project_lt=parent_project_lt,
        parent_project_lte=parent_project_lte,
        publication_state=publication_state,
        publication_state_contains=publication_state_contains,
        publication_state_endswith=publication_state_endswith,
        publication_state_gt=publication_state_gt,
        publication_state_gte=publication_state_gte,
        publication_state_icontains=publication_state_icontains,
        publication_state_iendswith=publication_state_iendswith,
        publication_state_iexact=publication_state_iexact,
        publication_state_in=publication_state_in,
        publication_state_iregex=publication_state_iregex,
        publication_state_isnull=publication_state_isnull,
        publication_state_istartswith=publication_state_istartswith,
        publication_state_lt=publication_state_lt,
        publication_state_lte=publication_state_lte,
        publication_state_range=publication_state_range,
        publication_state_regex=publication_state_regex,
        publication_state_startswith=publication_state_startswith,
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
        status=status,
        status_contains=status_contains,
        status_endswith=status_endswith,
        status_gt=status_gt,
        status_gte=status_gte,
        status_icontains=status_icontains,
        status_iendswith=status_iendswith,
        status_iexact=status_iexact,
        status_in=status_in,
        status_iregex=status_iregex,
        status_isnull=status_isnull,
        status_istartswith=status_istartswith,
        status_lt=status_lt,
        status_lte=status_lte,
        status_range=status_range,
        status_regex=status_regex,
        status_startswith=status_startswith,
        sub_project_ob_id=sub_project_ob_id,
        sub_project_ob_id_in=sub_project_ob_id_in,
        sub_project_title=sub_project_title,
        sub_project_title_contains=sub_project_title_contains,
        sub_project_title_in=sub_project_title_in,
        sub_project_uuid=sub_project_uuid,
        sub_project_uuid_in=sub_project_uuid_in,
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
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    keywords: str | Unset = UNSET,
    keywords_contains: str | Unset = UNSET,
    keywords_endswith: str | Unset = UNSET,
    keywords_gt: str | Unset = UNSET,
    keywords_gte: str | Unset = UNSET,
    keywords_icontains: str | Unset = UNSET,
    keywords_iendswith: str | Unset = UNSET,
    keywords_iexact: str | Unset = UNSET,
    keywords_in: list[str] | Unset = UNSET,
    keywords_iregex: str | Unset = UNSET,
    keywords_isnull: bool | Unset = UNSET,
    keywords_istartswith: str | Unset = UNSET,
    keywords_lt: str | Unset = UNSET,
    keywords_lte: str | Unset = UNSET,
    keywords_range: list[str] | Unset = UNSET,
    keywords_regex: str | Unset = UNSET,
    keywords_startswith: str | Unset = UNSET,
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
    observation_collection_ob_id: int | Unset = UNSET,
    observation_collection_ob_id_in: list[int] | Unset = UNSET,
    observation_collection_title: str | Unset = UNSET,
    observation_collection_title_contains: str | Unset = UNSET,
    observation_collection_uuid: str | Unset = UNSET,
    observation_collection_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    parent_project: int | Unset = UNSET,
    parent_project_gt: int | Unset = UNSET,
    parent_project_gte: int | Unset = UNSET,
    parent_project_in: list[int] | Unset = UNSET,
    parent_project_isnull: bool | Unset = UNSET,
    parent_project_lt: int | Unset = UNSET,
    parent_project_lte: int | Unset = UNSET,
    publication_state: ProjectsListPublicationState | Unset = UNSET,
    publication_state_contains: str | Unset = UNSET,
    publication_state_endswith: str | Unset = UNSET,
    publication_state_gt: str | Unset = UNSET,
    publication_state_gte: str | Unset = UNSET,
    publication_state_icontains: str | Unset = UNSET,
    publication_state_iendswith: str | Unset = UNSET,
    publication_state_iexact: str | Unset = UNSET,
    publication_state_in: list[str] | Unset = UNSET,
    publication_state_iregex: str | Unset = UNSET,
    publication_state_isnull: bool | Unset = UNSET,
    publication_state_istartswith: str | Unset = UNSET,
    publication_state_lt: str | Unset = UNSET,
    publication_state_lte: str | Unset = UNSET,
    publication_state_range: list[str] | Unset = UNSET,
    publication_state_regex: str | Unset = UNSET,
    publication_state_startswith: str | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_gt: int | Unset = UNSET,
    referenceable_ptr_gte: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    referenceable_ptr_lt: int | Unset = UNSET,
    referenceable_ptr_lte: int | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    status: ProjectsListProjectStatus | Unset = UNSET,
    status_contains: str | Unset = UNSET,
    status_endswith: str | Unset = UNSET,
    status_gt: str | Unset = UNSET,
    status_gte: str | Unset = UNSET,
    status_icontains: str | Unset = UNSET,
    status_iendswith: str | Unset = UNSET,
    status_iexact: str | Unset = UNSET,
    status_in: list[str] | Unset = UNSET,
    status_iregex: str | Unset = UNSET,
    status_isnull: bool | Unset = UNSET,
    status_istartswith: str | Unset = UNSET,
    status_lt: str | Unset = UNSET,
    status_lte: str | Unset = UNSET,
    status_range: list[str] | Unset = UNSET,
    status_regex: str | Unset = UNSET,
    status_startswith: str | Unset = UNSET,
    sub_project_ob_id: int | Unset = UNSET,
    sub_project_ob_id_in: list[int] | Unset = UNSET,
    sub_project_title: str | Unset = UNSET,
    sub_project_title_contains: str | Unset = UNSET,
    sub_project_title_in: list[str] | Unset = UNSET,
    sub_project_uuid: str | Unset = UNSET,
    sub_project_uuid_in: list[str] | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> Response[PaginatedProjectReadList]:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        keywords (str | Unset):
        keywords_contains (str | Unset):
        keywords_endswith (str | Unset):
        keywords_gt (str | Unset):
        keywords_gte (str | Unset):
        keywords_icontains (str | Unset):
        keywords_iendswith (str | Unset):
        keywords_iexact (str | Unset):
        keywords_in (list[str] | Unset):
        keywords_iregex (str | Unset):
        keywords_isnull (bool | Unset):
        keywords_istartswith (str | Unset):
        keywords_lt (str | Unset):
        keywords_lte (str | Unset):
        keywords_range (list[str] | Unset):
        keywords_regex (str | Unset):
        keywords_startswith (str | Unset):
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
        observation_collection_ob_id (int | Unset):
        observation_collection_ob_id_in (list[int] | Unset):
        observation_collection_title (str | Unset):
        observation_collection_title_contains (str | Unset):
        observation_collection_uuid (str | Unset):
        observation_collection_uuid_in (list[str] | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        parent_project (int | Unset):
        parent_project_gt (int | Unset):
        parent_project_gte (int | Unset):
        parent_project_in (list[int] | Unset):
        parent_project_isnull (bool | Unset):
        parent_project_lt (int | Unset):
        parent_project_lte (int | Unset):
        publication_state (ProjectsListPublicationState | Unset):
        publication_state_contains (str | Unset):
        publication_state_endswith (str | Unset):
        publication_state_gt (str | Unset):
        publication_state_gte (str | Unset):
        publication_state_icontains (str | Unset):
        publication_state_iendswith (str | Unset):
        publication_state_iexact (str | Unset):
        publication_state_in (list[str] | Unset):
        publication_state_iregex (str | Unset):
        publication_state_isnull (bool | Unset):
        publication_state_istartswith (str | Unset):
        publication_state_lt (str | Unset):
        publication_state_lte (str | Unset):
        publication_state_range (list[str] | Unset):
        publication_state_regex (str | Unset):
        publication_state_startswith (str | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_gt (int | Unset):
        referenceable_ptr_gte (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        referenceable_ptr_lt (int | Unset):
        referenceable_ptr_lte (int | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        status (ProjectsListProjectStatus | Unset):
        status_contains (str | Unset):
        status_endswith (str | Unset):
        status_gt (str | Unset):
        status_gte (str | Unset):
        status_icontains (str | Unset):
        status_iendswith (str | Unset):
        status_iexact (str | Unset):
        status_in (list[str] | Unset):
        status_iregex (str | Unset):
        status_isnull (bool | Unset):
        status_istartswith (str | Unset):
        status_lt (str | Unset):
        status_lte (str | Unset):
        status_range (list[str] | Unset):
        status_regex (str | Unset):
        status_startswith (str | Unset):
        sub_project_ob_id (int | Unset):
        sub_project_ob_id_in (list[int] | Unset):
        sub_project_title (str | Unset):
        sub_project_title_contains (str | Unset):
        sub_project_title_in (list[str] | Unset):
        sub_project_uuid (str | Unset):
        sub_project_uuid_in (list[str] | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedProjectReadList]
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
        keywords=keywords,
        keywords_contains=keywords_contains,
        keywords_endswith=keywords_endswith,
        keywords_gt=keywords_gt,
        keywords_gte=keywords_gte,
        keywords_icontains=keywords_icontains,
        keywords_iendswith=keywords_iendswith,
        keywords_iexact=keywords_iexact,
        keywords_in=keywords_in,
        keywords_iregex=keywords_iregex,
        keywords_isnull=keywords_isnull,
        keywords_istartswith=keywords_istartswith,
        keywords_lt=keywords_lt,
        keywords_lte=keywords_lte,
        keywords_range=keywords_range,
        keywords_regex=keywords_regex,
        keywords_startswith=keywords_startswith,
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
        observation_collection_ob_id=observation_collection_ob_id,
        observation_collection_ob_id_in=observation_collection_ob_id_in,
        observation_collection_title=observation_collection_title,
        observation_collection_title_contains=observation_collection_title_contains,
        observation_collection_uuid=observation_collection_uuid,
        observation_collection_uuid_in=observation_collection_uuid_in,
        offset=offset,
        ordering=ordering,
        parent_project=parent_project,
        parent_project_gt=parent_project_gt,
        parent_project_gte=parent_project_gte,
        parent_project_in=parent_project_in,
        parent_project_isnull=parent_project_isnull,
        parent_project_lt=parent_project_lt,
        parent_project_lte=parent_project_lte,
        publication_state=publication_state,
        publication_state_contains=publication_state_contains,
        publication_state_endswith=publication_state_endswith,
        publication_state_gt=publication_state_gt,
        publication_state_gte=publication_state_gte,
        publication_state_icontains=publication_state_icontains,
        publication_state_iendswith=publication_state_iendswith,
        publication_state_iexact=publication_state_iexact,
        publication_state_in=publication_state_in,
        publication_state_iregex=publication_state_iregex,
        publication_state_isnull=publication_state_isnull,
        publication_state_istartswith=publication_state_istartswith,
        publication_state_lt=publication_state_lt,
        publication_state_lte=publication_state_lte,
        publication_state_range=publication_state_range,
        publication_state_regex=publication_state_regex,
        publication_state_startswith=publication_state_startswith,
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
        status=status,
        status_contains=status_contains,
        status_endswith=status_endswith,
        status_gt=status_gt,
        status_gte=status_gte,
        status_icontains=status_icontains,
        status_iendswith=status_iendswith,
        status_iexact=status_iexact,
        status_in=status_in,
        status_iregex=status_iregex,
        status_isnull=status_isnull,
        status_istartswith=status_istartswith,
        status_lt=status_lt,
        status_lte=status_lte,
        status_range=status_range,
        status_regex=status_regex,
        status_startswith=status_startswith,
        sub_project_ob_id=sub_project_ob_id,
        sub_project_ob_id_in=sub_project_ob_id_in,
        sub_project_title=sub_project_title,
        sub_project_title_contains=sub_project_title_contains,
        sub_project_title_in=sub_project_title_in,
        sub_project_uuid=sub_project_uuid,
        sub_project_uuid_in=sub_project_uuid_in,
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
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    keywords: str | Unset = UNSET,
    keywords_contains: str | Unset = UNSET,
    keywords_endswith: str | Unset = UNSET,
    keywords_gt: str | Unset = UNSET,
    keywords_gte: str | Unset = UNSET,
    keywords_icontains: str | Unset = UNSET,
    keywords_iendswith: str | Unset = UNSET,
    keywords_iexact: str | Unset = UNSET,
    keywords_in: list[str] | Unset = UNSET,
    keywords_iregex: str | Unset = UNSET,
    keywords_isnull: bool | Unset = UNSET,
    keywords_istartswith: str | Unset = UNSET,
    keywords_lt: str | Unset = UNSET,
    keywords_lte: str | Unset = UNSET,
    keywords_range: list[str] | Unset = UNSET,
    keywords_regex: str | Unset = UNSET,
    keywords_startswith: str | Unset = UNSET,
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
    observation_collection_ob_id: int | Unset = UNSET,
    observation_collection_ob_id_in: list[int] | Unset = UNSET,
    observation_collection_title: str | Unset = UNSET,
    observation_collection_title_contains: str | Unset = UNSET,
    observation_collection_uuid: str | Unset = UNSET,
    observation_collection_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    parent_project: int | Unset = UNSET,
    parent_project_gt: int | Unset = UNSET,
    parent_project_gte: int | Unset = UNSET,
    parent_project_in: list[int] | Unset = UNSET,
    parent_project_isnull: bool | Unset = UNSET,
    parent_project_lt: int | Unset = UNSET,
    parent_project_lte: int | Unset = UNSET,
    publication_state: ProjectsListPublicationState | Unset = UNSET,
    publication_state_contains: str | Unset = UNSET,
    publication_state_endswith: str | Unset = UNSET,
    publication_state_gt: str | Unset = UNSET,
    publication_state_gte: str | Unset = UNSET,
    publication_state_icontains: str | Unset = UNSET,
    publication_state_iendswith: str | Unset = UNSET,
    publication_state_iexact: str | Unset = UNSET,
    publication_state_in: list[str] | Unset = UNSET,
    publication_state_iregex: str | Unset = UNSET,
    publication_state_isnull: bool | Unset = UNSET,
    publication_state_istartswith: str | Unset = UNSET,
    publication_state_lt: str | Unset = UNSET,
    publication_state_lte: str | Unset = UNSET,
    publication_state_range: list[str] | Unset = UNSET,
    publication_state_regex: str | Unset = UNSET,
    publication_state_startswith: str | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_gt: int | Unset = UNSET,
    referenceable_ptr_gte: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    referenceable_ptr_lt: int | Unset = UNSET,
    referenceable_ptr_lte: int | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    status: ProjectsListProjectStatus | Unset = UNSET,
    status_contains: str | Unset = UNSET,
    status_endswith: str | Unset = UNSET,
    status_gt: str | Unset = UNSET,
    status_gte: str | Unset = UNSET,
    status_icontains: str | Unset = UNSET,
    status_iendswith: str | Unset = UNSET,
    status_iexact: str | Unset = UNSET,
    status_in: list[str] | Unset = UNSET,
    status_iregex: str | Unset = UNSET,
    status_isnull: bool | Unset = UNSET,
    status_istartswith: str | Unset = UNSET,
    status_lt: str | Unset = UNSET,
    status_lte: str | Unset = UNSET,
    status_range: list[str] | Unset = UNSET,
    status_regex: str | Unset = UNSET,
    status_startswith: str | Unset = UNSET,
    sub_project_ob_id: int | Unset = UNSET,
    sub_project_ob_id_in: list[int] | Unset = UNSET,
    sub_project_title: str | Unset = UNSET,
    sub_project_title_contains: str | Unset = UNSET,
    sub_project_title_in: list[str] | Unset = UNSET,
    sub_project_uuid: str | Unset = UNSET,
    sub_project_uuid_in: list[str] | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> PaginatedProjectReadList | None:
    """Get a list of Project objects. Projects have a 1:1 mapping with Observations.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        keywords (str | Unset):
        keywords_contains (str | Unset):
        keywords_endswith (str | Unset):
        keywords_gt (str | Unset):
        keywords_gte (str | Unset):
        keywords_icontains (str | Unset):
        keywords_iendswith (str | Unset):
        keywords_iexact (str | Unset):
        keywords_in (list[str] | Unset):
        keywords_iregex (str | Unset):
        keywords_isnull (bool | Unset):
        keywords_istartswith (str | Unset):
        keywords_lt (str | Unset):
        keywords_lte (str | Unset):
        keywords_range (list[str] | Unset):
        keywords_regex (str | Unset):
        keywords_startswith (str | Unset):
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
        observation_collection_ob_id (int | Unset):
        observation_collection_ob_id_in (list[int] | Unset):
        observation_collection_title (str | Unset):
        observation_collection_title_contains (str | Unset):
        observation_collection_uuid (str | Unset):
        observation_collection_uuid_in (list[str] | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        parent_project (int | Unset):
        parent_project_gt (int | Unset):
        parent_project_gte (int | Unset):
        parent_project_in (list[int] | Unset):
        parent_project_isnull (bool | Unset):
        parent_project_lt (int | Unset):
        parent_project_lte (int | Unset):
        publication_state (ProjectsListPublicationState | Unset):
        publication_state_contains (str | Unset):
        publication_state_endswith (str | Unset):
        publication_state_gt (str | Unset):
        publication_state_gte (str | Unset):
        publication_state_icontains (str | Unset):
        publication_state_iendswith (str | Unset):
        publication_state_iexact (str | Unset):
        publication_state_in (list[str] | Unset):
        publication_state_iregex (str | Unset):
        publication_state_isnull (bool | Unset):
        publication_state_istartswith (str | Unset):
        publication_state_lt (str | Unset):
        publication_state_lte (str | Unset):
        publication_state_range (list[str] | Unset):
        publication_state_regex (str | Unset):
        publication_state_startswith (str | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_gt (int | Unset):
        referenceable_ptr_gte (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        referenceable_ptr_lt (int | Unset):
        referenceable_ptr_lte (int | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        status (ProjectsListProjectStatus | Unset):
        status_contains (str | Unset):
        status_endswith (str | Unset):
        status_gt (str | Unset):
        status_gte (str | Unset):
        status_icontains (str | Unset):
        status_iendswith (str | Unset):
        status_iexact (str | Unset):
        status_in (list[str] | Unset):
        status_iregex (str | Unset):
        status_isnull (bool | Unset):
        status_istartswith (str | Unset):
        status_lt (str | Unset):
        status_lte (str | Unset):
        status_range (list[str] | Unset):
        status_regex (str | Unset):
        status_startswith (str | Unset):
        sub_project_ob_id (int | Unset):
        sub_project_ob_id_in (list[int] | Unset):
        sub_project_title (str | Unset):
        sub_project_title_contains (str | Unset):
        sub_project_title_in (list[str] | Unset):
        sub_project_uuid (str | Unset):
        sub_project_uuid_in (list[str] | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedProjectReadList
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
            keywords=keywords,
            keywords_contains=keywords_contains,
            keywords_endswith=keywords_endswith,
            keywords_gt=keywords_gt,
            keywords_gte=keywords_gte,
            keywords_icontains=keywords_icontains,
            keywords_iendswith=keywords_iendswith,
            keywords_iexact=keywords_iexact,
            keywords_in=keywords_in,
            keywords_iregex=keywords_iregex,
            keywords_isnull=keywords_isnull,
            keywords_istartswith=keywords_istartswith,
            keywords_lt=keywords_lt,
            keywords_lte=keywords_lte,
            keywords_range=keywords_range,
            keywords_regex=keywords_regex,
            keywords_startswith=keywords_startswith,
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
            observation_collection_ob_id=observation_collection_ob_id,
            observation_collection_ob_id_in=observation_collection_ob_id_in,
            observation_collection_title=observation_collection_title,
            observation_collection_title_contains=observation_collection_title_contains,
            observation_collection_uuid=observation_collection_uuid,
            observation_collection_uuid_in=observation_collection_uuid_in,
            offset=offset,
            ordering=ordering,
            parent_project=parent_project,
            parent_project_gt=parent_project_gt,
            parent_project_gte=parent_project_gte,
            parent_project_in=parent_project_in,
            parent_project_isnull=parent_project_isnull,
            parent_project_lt=parent_project_lt,
            parent_project_lte=parent_project_lte,
            publication_state=publication_state,
            publication_state_contains=publication_state_contains,
            publication_state_endswith=publication_state_endswith,
            publication_state_gt=publication_state_gt,
            publication_state_gte=publication_state_gte,
            publication_state_icontains=publication_state_icontains,
            publication_state_iendswith=publication_state_iendswith,
            publication_state_iexact=publication_state_iexact,
            publication_state_in=publication_state_in,
            publication_state_iregex=publication_state_iregex,
            publication_state_isnull=publication_state_isnull,
            publication_state_istartswith=publication_state_istartswith,
            publication_state_lt=publication_state_lt,
            publication_state_lte=publication_state_lte,
            publication_state_range=publication_state_range,
            publication_state_regex=publication_state_regex,
            publication_state_startswith=publication_state_startswith,
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
            status=status,
            status_contains=status_contains,
            status_endswith=status_endswith,
            status_gt=status_gt,
            status_gte=status_gte,
            status_icontains=status_icontains,
            status_iendswith=status_iendswith,
            status_iexact=status_iexact,
            status_in=status_in,
            status_iregex=status_iregex,
            status_isnull=status_isnull,
            status_istartswith=status_istartswith,
            status_lt=status_lt,
            status_lte=status_lte,
            status_range=status_range,
            status_regex=status_regex,
            status_startswith=status_startswith,
            sub_project_ob_id=sub_project_ob_id,
            sub_project_ob_id_in=sub_project_ob_id_in,
            sub_project_title=sub_project_title,
            sub_project_title_contains=sub_project_title_contains,
            sub_project_title_in=sub_project_title_in,
            sub_project_uuid=sub_project_uuid,
            sub_project_uuid_in=sub_project_uuid_in,
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
