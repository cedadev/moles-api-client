from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_referenceable_list import PaginatedReferenceableList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    acquisition: int | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    compositeprocess: int | Unset = UNSET,
    compositeprocess_in: list[int] | Unset = UNSET,
    compositeprocess_isnull: bool | Unset = UNSET,
    computation: int | Unset = UNSET,
    computation_in: list[int] | Unset = UNSET,
    computation_isnull: bool | Unset = UNSET,
    externalcitation: int | Unset = UNSET,
    externalcitation_in: list[int] | Unset = UNSET,
    externalcitation_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    instrument: int | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobileplatformoperation: int | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    observation: int | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    observationcollection: int | Unset = UNSET,
    observationcollection_in: list[int] | Unset = UNSET,
    observationcollection_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform: int | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    project: int | Unset = UNSET,
    project_in: list[int] | Unset = UNSET,
    project_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    result: int | Unset = UNSET,
    result_in: list[int] | Unset = UNSET,
    result_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
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

    params["acquisition"] = acquisition

    json_acquisition_in: list[int] | Unset = UNSET
    if not isinstance(acquisition_in, Unset):
        json_acquisition_in = acquisition_in

    params["acquisition__in"] = json_acquisition_in

    params["acquisition__isnull"] = acquisition_isnull

    params["compositeprocess"] = compositeprocess

    json_compositeprocess_in: list[int] | Unset = UNSET
    if not isinstance(compositeprocess_in, Unset):
        json_compositeprocess_in = compositeprocess_in

    params["compositeprocess__in"] = json_compositeprocess_in

    params["compositeprocess__isnull"] = compositeprocess_isnull

    params["computation"] = computation

    json_computation_in: list[int] | Unset = UNSET
    if not isinstance(computation_in, Unset):
        json_computation_in = computation_in

    params["computation__in"] = json_computation_in

    params["computation__isnull"] = computation_isnull

    params["externalcitation"] = externalcitation

    json_externalcitation_in: list[int] | Unset = UNSET
    if not isinstance(externalcitation_in, Unset):
        json_externalcitation_in = externalcitation_in

    params["externalcitation__in"] = json_externalcitation_in

    params["externalcitation__isnull"] = externalcitation_isnull

    json_identifier: list[int] | Unset = UNSET
    if not isinstance(identifier, Unset):
        json_identifier = identifier

    params["identifier"] = json_identifier

    json_identifier_in: list[int] | Unset = UNSET
    if not isinstance(identifier_in, Unset):
        json_identifier_in = identifier_in

    params["identifier__in"] = json_identifier_in

    params["identifier__isnull"] = identifier_isnull

    params["instrument"] = instrument

    json_instrument_in: list[int] | Unset = UNSET
    if not isinstance(instrument_in, Unset):
        json_instrument_in = instrument_in

    params["instrument__in"] = json_instrument_in

    params["instrument__isnull"] = instrument_isnull

    params["limit"] = limit

    json_migrationproperty: list[int] | Unset = UNSET
    if not isinstance(migrationproperty, Unset):
        json_migrationproperty = migrationproperty

    params["migrationproperty"] = json_migrationproperty

    json_migrationproperty_in: list[int] | Unset = UNSET
    if not isinstance(migrationproperty_in, Unset):
        json_migrationproperty_in = migrationproperty_in

    params["migrationproperty__in"] = json_migrationproperty_in

    params["migrationproperty__isnull"] = migrationproperty_isnull

    params["mobileplatformoperation"] = mobileplatformoperation

    json_mobileplatformoperation_in: list[int] | Unset = UNSET
    if not isinstance(mobileplatformoperation_in, Unset):
        json_mobileplatformoperation_in = mobileplatformoperation_in

    params["mobileplatformoperation__in"] = json_mobileplatformoperation_in

    params["mobileplatformoperation__isnull"] = mobileplatformoperation_isnull

    json_note: list[int] | Unset = UNSET
    if not isinstance(note, Unset):
        json_note = note

    params["note"] = json_note

    json_note_in: list[int] | Unset = UNSET
    if not isinstance(note_in, Unset):
        json_note_in = note_in

    params["note__in"] = json_note_in

    params["note__isnull"] = note_isnull

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

    params["observation"] = observation

    json_observation_in: list[int] | Unset = UNSET
    if not isinstance(observation_in, Unset):
        json_observation_in = observation_in

    params["observation__in"] = json_observation_in

    params["observation__isnull"] = observation_isnull

    params["observationcollection"] = observationcollection

    json_observationcollection_in: list[int] | Unset = UNSET
    if not isinstance(observationcollection_in, Unset):
        json_observationcollection_in = observationcollection_in

    params["observationcollection__in"] = json_observationcollection_in

    params["observationcollection__isnull"] = observationcollection_isnull

    params["offset"] = offset

    json_onlineresource: list[int] | Unset = UNSET
    if not isinstance(onlineresource, Unset):
        json_onlineresource = onlineresource

    params["onlineresource"] = json_onlineresource

    json_onlineresource_in: list[int] | Unset = UNSET
    if not isinstance(onlineresource_in, Unset):
        json_onlineresource_in = onlineresource_in

    params["onlineresource__in"] = json_onlineresource_in

    params["onlineresource__isnull"] = onlineresource_isnull

    params["ordering"] = ordering

    params["platform"] = platform

    json_platform_in: list[int] | Unset = UNSET
    if not isinstance(platform_in, Unset):
        json_platform_in = platform_in

    params["platform__in"] = json_platform_in

    params["platform__isnull"] = platform_isnull

    params["project"] = project

    json_project_in: list[int] | Unset = UNSET
    if not isinstance(project_in, Unset):
        json_project_in = project_in

    params["project__in"] = json_project_in

    params["project__isnull"] = project_isnull

    json_responsiblepartyinfo: list[int] | Unset = UNSET
    if not isinstance(responsiblepartyinfo, Unset):
        json_responsiblepartyinfo = responsiblepartyinfo

    params["responsiblepartyinfo"] = json_responsiblepartyinfo

    json_responsiblepartyinfo_in: list[int] | Unset = UNSET
    if not isinstance(responsiblepartyinfo_in, Unset):
        json_responsiblepartyinfo_in = responsiblepartyinfo_in

    params["responsiblepartyinfo__in"] = json_responsiblepartyinfo_in

    params["responsiblepartyinfo__isnull"] = responsiblepartyinfo_isnull

    params["result"] = result

    json_result_in: list[int] | Unset = UNSET
    if not isinstance(result_in, Unset):
        json_result_in = result_in

    params["result__in"] = json_result_in

    params["result__isnull"] = result_isnull

    json_review: list[int] | Unset = UNSET
    if not isinstance(review, Unset):
        json_review = review

    params["review"] = json_review

    json_review_in: list[int] | Unset = UNSET
    if not isinstance(review_in, Unset):
        json_review_in = review_in

    params["review__in"] = json_review_in

    params["review__isnull"] = review_isnull

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
        json_short_code_in = short_code_in

    params["short_code__in"] = json_short_code_in

    params["short_code__iregex"] = short_code_iregex

    params["short_code__isnull"] = short_code_isnull

    params["short_code__istartswith"] = short_code_istartswith

    params["short_code__lt"] = short_code_lt

    params["short_code__lte"] = short_code_lte

    json_short_code_range: list[str] | Unset = UNSET
    if not isinstance(short_code_range, Unset):
        json_short_code_range = short_code_range

    params["short_code__range"] = json_short_code_range

    params["short_code__regex"] = short_code_regex

    params["short_code__startswith"] = short_code_startswith

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
        json_uuid_in = uuid_in

    params["uuid__in"] = json_uuid_in

    params["uuid__iregex"] = uuid_iregex

    params["uuid__isnull"] = uuid_isnull

    params["uuid__istartswith"] = uuid_istartswith

    params["uuid__lt"] = uuid_lt

    params["uuid__lte"] = uuid_lte

    json_uuid_range: list[str] | Unset = UNSET
    if not isinstance(uuid_range, Unset):
        json_uuid_range = uuid_range

    params["uuid__range"] = json_uuid_range

    params["uuid__regex"] = uuid_regex

    params["uuid__startswith"] = uuid_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/referenceables/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedReferenceableList | None:
    if response.status_code == 200:
        response_200 = PaginatedReferenceableList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedReferenceableList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    acquisition: int | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    compositeprocess: int | Unset = UNSET,
    compositeprocess_in: list[int] | Unset = UNSET,
    compositeprocess_isnull: bool | Unset = UNSET,
    computation: int | Unset = UNSET,
    computation_in: list[int] | Unset = UNSET,
    computation_isnull: bool | Unset = UNSET,
    externalcitation: int | Unset = UNSET,
    externalcitation_in: list[int] | Unset = UNSET,
    externalcitation_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    instrument: int | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobileplatformoperation: int | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    observation: int | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    observationcollection: int | Unset = UNSET,
    observationcollection_in: list[int] | Unset = UNSET,
    observationcollection_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform: int | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    project: int | Unset = UNSET,
    project_in: list[int] | Unset = UNSET,
    project_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    result: int | Unset = UNSET,
    result_in: list[int] | Unset = UNSET,
    result_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
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
) -> Response[PaginatedReferenceableList]:
    """Get a list of Referenceable objects. This is the base class for the main record types in the CEDA
    data catalogue.

    Args:
        acquisition (int | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        compositeprocess (int | Unset):
        compositeprocess_in (list[int] | Unset):
        compositeprocess_isnull (bool | Unset):
        computation (int | Unset):
        computation_in (list[int] | Unset):
        computation_isnull (bool | Unset):
        externalcitation (int | Unset):
        externalcitation_in (list[int] | Unset):
        externalcitation_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        instrument (int | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobileplatformoperation (int | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        observation (int | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        observationcollection (int | Unset):
        observationcollection_in (list[int] | Unset):
        observationcollection_isnull (bool | Unset):
        offset (int | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
        platform (int | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        project (int | Unset):
        project_in (list[int] | Unset):
        project_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        result (int | Unset):
        result_in (list[int] | Unset):
        result_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
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
        Response[PaginatedReferenceableList]
    """

    kwargs = _get_kwargs(
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        compositeprocess=compositeprocess,
        compositeprocess_in=compositeprocess_in,
        compositeprocess_isnull=compositeprocess_isnull,
        computation=computation,
        computation_in=computation_in,
        computation_isnull=computation_isnull,
        externalcitation=externalcitation,
        externalcitation_in=externalcitation_in,
        externalcitation_isnull=externalcitation_isnull,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        instrument=instrument,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        limit=limit,
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
        observationcollection=observationcollection,
        observationcollection_in=observationcollection_in,
        observationcollection_isnull=observationcollection_isnull,
        offset=offset,
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        ordering=ordering,
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        project=project,
        project_in=project_in,
        project_isnull=project_isnull,
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
        result=result,
        result_in=result_in,
        result_isnull=result_isnull,
        review=review,
        review_in=review_in,
        review_isnull=review_isnull,
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
    acquisition: int | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    compositeprocess: int | Unset = UNSET,
    compositeprocess_in: list[int] | Unset = UNSET,
    compositeprocess_isnull: bool | Unset = UNSET,
    computation: int | Unset = UNSET,
    computation_in: list[int] | Unset = UNSET,
    computation_isnull: bool | Unset = UNSET,
    externalcitation: int | Unset = UNSET,
    externalcitation_in: list[int] | Unset = UNSET,
    externalcitation_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    instrument: int | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobileplatformoperation: int | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    observation: int | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    observationcollection: int | Unset = UNSET,
    observationcollection_in: list[int] | Unset = UNSET,
    observationcollection_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform: int | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    project: int | Unset = UNSET,
    project_in: list[int] | Unset = UNSET,
    project_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    result: int | Unset = UNSET,
    result_in: list[int] | Unset = UNSET,
    result_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
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
) -> PaginatedReferenceableList | None:
    """Get a list of Referenceable objects. This is the base class for the main record types in the CEDA
    data catalogue.

    Args:
        acquisition (int | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        compositeprocess (int | Unset):
        compositeprocess_in (list[int] | Unset):
        compositeprocess_isnull (bool | Unset):
        computation (int | Unset):
        computation_in (list[int] | Unset):
        computation_isnull (bool | Unset):
        externalcitation (int | Unset):
        externalcitation_in (list[int] | Unset):
        externalcitation_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        instrument (int | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobileplatformoperation (int | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        observation (int | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        observationcollection (int | Unset):
        observationcollection_in (list[int] | Unset):
        observationcollection_isnull (bool | Unset):
        offset (int | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
        platform (int | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        project (int | Unset):
        project_in (list[int] | Unset):
        project_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        result (int | Unset):
        result_in (list[int] | Unset):
        result_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
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
        PaginatedReferenceableList
    """

    return sync_detailed(
        client=client,
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        compositeprocess=compositeprocess,
        compositeprocess_in=compositeprocess_in,
        compositeprocess_isnull=compositeprocess_isnull,
        computation=computation,
        computation_in=computation_in,
        computation_isnull=computation_isnull,
        externalcitation=externalcitation,
        externalcitation_in=externalcitation_in,
        externalcitation_isnull=externalcitation_isnull,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        instrument=instrument,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        limit=limit,
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
        observationcollection=observationcollection,
        observationcollection_in=observationcollection_in,
        observationcollection_isnull=observationcollection_isnull,
        offset=offset,
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        ordering=ordering,
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        project=project,
        project_in=project_in,
        project_isnull=project_isnull,
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
        result=result,
        result_in=result_in,
        result_isnull=result_isnull,
        review=review,
        review_in=review_in,
        review_isnull=review_isnull,
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
    acquisition: int | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    compositeprocess: int | Unset = UNSET,
    compositeprocess_in: list[int] | Unset = UNSET,
    compositeprocess_isnull: bool | Unset = UNSET,
    computation: int | Unset = UNSET,
    computation_in: list[int] | Unset = UNSET,
    computation_isnull: bool | Unset = UNSET,
    externalcitation: int | Unset = UNSET,
    externalcitation_in: list[int] | Unset = UNSET,
    externalcitation_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    instrument: int | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobileplatformoperation: int | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    observation: int | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    observationcollection: int | Unset = UNSET,
    observationcollection_in: list[int] | Unset = UNSET,
    observationcollection_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform: int | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    project: int | Unset = UNSET,
    project_in: list[int] | Unset = UNSET,
    project_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    result: int | Unset = UNSET,
    result_in: list[int] | Unset = UNSET,
    result_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
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
) -> Response[PaginatedReferenceableList]:
    """Get a list of Referenceable objects. This is the base class for the main record types in the CEDA
    data catalogue.

    Args:
        acquisition (int | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        compositeprocess (int | Unset):
        compositeprocess_in (list[int] | Unset):
        compositeprocess_isnull (bool | Unset):
        computation (int | Unset):
        computation_in (list[int] | Unset):
        computation_isnull (bool | Unset):
        externalcitation (int | Unset):
        externalcitation_in (list[int] | Unset):
        externalcitation_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        instrument (int | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobileplatformoperation (int | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        observation (int | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        observationcollection (int | Unset):
        observationcollection_in (list[int] | Unset):
        observationcollection_isnull (bool | Unset):
        offset (int | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
        platform (int | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        project (int | Unset):
        project_in (list[int] | Unset):
        project_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        result (int | Unset):
        result_in (list[int] | Unset):
        result_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
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
        Response[PaginatedReferenceableList]
    """

    kwargs = _get_kwargs(
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        compositeprocess=compositeprocess,
        compositeprocess_in=compositeprocess_in,
        compositeprocess_isnull=compositeprocess_isnull,
        computation=computation,
        computation_in=computation_in,
        computation_isnull=computation_isnull,
        externalcitation=externalcitation,
        externalcitation_in=externalcitation_in,
        externalcitation_isnull=externalcitation_isnull,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        instrument=instrument,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        limit=limit,
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        mobileplatformoperation=mobileplatformoperation,
        mobileplatformoperation_in=mobileplatformoperation_in,
        mobileplatformoperation_isnull=mobileplatformoperation_isnull,
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
        observationcollection=observationcollection,
        observationcollection_in=observationcollection_in,
        observationcollection_isnull=observationcollection_isnull,
        offset=offset,
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        ordering=ordering,
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        project=project,
        project_in=project_in,
        project_isnull=project_isnull,
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
        result=result,
        result_in=result_in,
        result_isnull=result_isnull,
        review=review,
        review_in=review_in,
        review_isnull=review_isnull,
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
    acquisition: int | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    compositeprocess: int | Unset = UNSET,
    compositeprocess_in: list[int] | Unset = UNSET,
    compositeprocess_isnull: bool | Unset = UNSET,
    computation: int | Unset = UNSET,
    computation_in: list[int] | Unset = UNSET,
    computation_isnull: bool | Unset = UNSET,
    externalcitation: int | Unset = UNSET,
    externalcitation_in: list[int] | Unset = UNSET,
    externalcitation_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    instrument: int | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobileplatformoperation: int | Unset = UNSET,
    mobileplatformoperation_in: list[int] | Unset = UNSET,
    mobileplatformoperation_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    observation: int | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    observationcollection: int | Unset = UNSET,
    observationcollection_in: list[int] | Unset = UNSET,
    observationcollection_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform: int | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    project: int | Unset = UNSET,
    project_in: list[int] | Unset = UNSET,
    project_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    result: int | Unset = UNSET,
    result_in: list[int] | Unset = UNSET,
    result_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
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
) -> PaginatedReferenceableList | None:
    """Get a list of Referenceable objects. This is the base class for the main record types in the CEDA
    data catalogue.

    Args:
        acquisition (int | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        compositeprocess (int | Unset):
        compositeprocess_in (list[int] | Unset):
        compositeprocess_isnull (bool | Unset):
        computation (int | Unset):
        computation_in (list[int] | Unset):
        computation_isnull (bool | Unset):
        externalcitation (int | Unset):
        externalcitation_in (list[int] | Unset):
        externalcitation_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        instrument (int | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobileplatformoperation (int | Unset):
        mobileplatformoperation_in (list[int] | Unset):
        mobileplatformoperation_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        observation (int | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        observationcollection (int | Unset):
        observationcollection_in (list[int] | Unset):
        observationcollection_isnull (bool | Unset):
        offset (int | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
        platform (int | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        project (int | Unset):
        project_in (list[int] | Unset):
        project_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        result (int | Unset):
        result_in (list[int] | Unset):
        result_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
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
        PaginatedReferenceableList
    """

    return (
        await asyncio_detailed(
            client=client,
            acquisition=acquisition,
            acquisition_in=acquisition_in,
            acquisition_isnull=acquisition_isnull,
            compositeprocess=compositeprocess,
            compositeprocess_in=compositeprocess_in,
            compositeprocess_isnull=compositeprocess_isnull,
            computation=computation,
            computation_in=computation_in,
            computation_isnull=computation_isnull,
            externalcitation=externalcitation,
            externalcitation_in=externalcitation_in,
            externalcitation_isnull=externalcitation_isnull,
            identifier=identifier,
            identifier_in=identifier_in,
            identifier_isnull=identifier_isnull,
            instrument=instrument,
            instrument_in=instrument_in,
            instrument_isnull=instrument_isnull,
            limit=limit,
            migrationproperty=migrationproperty,
            migrationproperty_in=migrationproperty_in,
            migrationproperty_isnull=migrationproperty_isnull,
            mobileplatformoperation=mobileplatformoperation,
            mobileplatformoperation_in=mobileplatformoperation_in,
            mobileplatformoperation_isnull=mobileplatformoperation_isnull,
            note=note,
            note_in=note_in,
            note_isnull=note_isnull,
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
            observation=observation,
            observation_in=observation_in,
            observation_isnull=observation_isnull,
            observationcollection=observationcollection,
            observationcollection_in=observationcollection_in,
            observationcollection_isnull=observationcollection_isnull,
            offset=offset,
            onlineresource=onlineresource,
            onlineresource_in=onlineresource_in,
            onlineresource_isnull=onlineresource_isnull,
            ordering=ordering,
            platform=platform,
            platform_in=platform_in,
            platform_isnull=platform_isnull,
            project=project,
            project_in=project_in,
            project_isnull=project_isnull,
            responsiblepartyinfo=responsiblepartyinfo,
            responsiblepartyinfo_in=responsiblepartyinfo_in,
            responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
            result=result,
            result_in=result_in,
            result_isnull=result_isnull,
            review=review,
            review_in=review_in,
            review_isnull=review_isnull,
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
