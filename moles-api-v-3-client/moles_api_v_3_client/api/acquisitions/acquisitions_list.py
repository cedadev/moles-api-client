from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_procedure_acquisition_read_list import PaginatedProcedureAcquisitionReadList
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
    compositeprocess: list[int] | Unset = UNSET,
    compositeprocess_in: list[int] | Unset = UNSET,
    compositeprocess_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    image_details: list[int] | Unset = UNSET,
    image_details_in: list[int] | Unset = UNSET,
    image_details_isnull: bool | Unset = UNSET,
    independent_instrument: list[int] | Unset = UNSET,
    independent_instrument_in: list[int] | Unset = UNSET,
    independent_instrument_isnull: bool | Unset = UNSET,
    instrumentplatformpair: list[int] | Unset = UNSET,
    instrumentplatformpair_in: list[int] | Unset = UNSET,
    instrumentplatformpair_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobile_platform_operation: list[int] | Unset = UNSET,
    mobile_platform_operation_in: list[int] | Unset = UNSET,
    mobile_platform_operation_isnull: bool | Unset = UNSET,
    mobile_platform_operation_ob_id: int | Unset = UNSET,
    mobile_platform_operation_ob_id_in: list[int] | Unset = UNSET,
    mobile_platform_operation_uuid: str | Unset = UNSET,
    mobile_platform_operation_uuid_in: list[str] | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    output_description: int | Unset = UNSET,
    output_description_in: list[int] | Unset = UNSET,
    output_description_isnull: bool | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
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
        json_abstract_in = abstract_in

    params["abstract__in"] = json_abstract_in

    params["abstract__iregex"] = abstract_iregex

    params["abstract__isnull"] = abstract_isnull

    params["abstract__istartswith"] = abstract_istartswith

    params["abstract__lt"] = abstract_lt

    params["abstract__lte"] = abstract_lte

    json_abstract_range: list[str] | Unset = UNSET
    if not isinstance(abstract_range, Unset):
        json_abstract_range = abstract_range

    params["abstract__range"] = json_abstract_range

    params["abstract__regex"] = abstract_regex

    params["abstract__startswith"] = abstract_startswith

    json_compositeprocess: list[int] | Unset = UNSET
    if not isinstance(compositeprocess, Unset):
        json_compositeprocess = compositeprocess

    params["compositeprocess"] = json_compositeprocess

    json_compositeprocess_in: list[int] | Unset = UNSET
    if not isinstance(compositeprocess_in, Unset):
        json_compositeprocess_in = compositeprocess_in

    params["compositeprocess__in"] = json_compositeprocess_in

    params["compositeprocess__isnull"] = compositeprocess_isnull

    json_identifier: list[int] | Unset = UNSET
    if not isinstance(identifier, Unset):
        json_identifier = identifier

    params["identifier"] = json_identifier

    json_identifier_in: list[int] | Unset = UNSET
    if not isinstance(identifier_in, Unset):
        json_identifier_in = identifier_in

    params["identifier__in"] = json_identifier_in

    params["identifier__isnull"] = identifier_isnull

    json_image_details: list[int] | Unset = UNSET
    if not isinstance(image_details, Unset):
        json_image_details = image_details

    params["imageDetails"] = json_image_details

    json_image_details_in: list[int] | Unset = UNSET
    if not isinstance(image_details_in, Unset):
        json_image_details_in = image_details_in

    params["imageDetails__in"] = json_image_details_in

    params["imageDetails__isnull"] = image_details_isnull

    json_independent_instrument: list[int] | Unset = UNSET
    if not isinstance(independent_instrument, Unset):
        json_independent_instrument = independent_instrument

    params["independentInstrument"] = json_independent_instrument

    json_independent_instrument_in: list[int] | Unset = UNSET
    if not isinstance(independent_instrument_in, Unset):
        json_independent_instrument_in = independent_instrument_in

    params["independentInstrument__in"] = json_independent_instrument_in

    params["independentInstrument__isnull"] = independent_instrument_isnull

    json_instrumentplatformpair: list[int] | Unset = UNSET
    if not isinstance(instrumentplatformpair, Unset):
        json_instrumentplatformpair = instrumentplatformpair

    params["instrumentplatformpair"] = json_instrumentplatformpair

    json_instrumentplatformpair_in: list[int] | Unset = UNSET
    if not isinstance(instrumentplatformpair_in, Unset):
        json_instrumentplatformpair_in = instrumentplatformpair_in

    params["instrumentplatformpair__in"] = json_instrumentplatformpair_in

    params["instrumentplatformpair__isnull"] = instrumentplatformpair_isnull

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

    json_mobile_platform_operation: list[int] | Unset = UNSET
    if not isinstance(mobile_platform_operation, Unset):
        json_mobile_platform_operation = mobile_platform_operation

    params["mobilePlatformOperation"] = json_mobile_platform_operation

    json_mobile_platform_operation_in: list[int] | Unset = UNSET
    if not isinstance(mobile_platform_operation_in, Unset):
        json_mobile_platform_operation_in = mobile_platform_operation_in

    params["mobilePlatformOperation__in"] = json_mobile_platform_operation_in

    params["mobilePlatformOperation__isnull"] = mobile_platform_operation_isnull

    params["mobilePlatformOperation__ob_id"] = mobile_platform_operation_ob_id

    json_mobile_platform_operation_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(mobile_platform_operation_ob_id_in, Unset):
        json_mobile_platform_operation_ob_id_in = mobile_platform_operation_ob_id_in

    params["mobilePlatformOperation__ob_id__in"] = json_mobile_platform_operation_ob_id_in

    params["mobilePlatformOperation__uuid"] = mobile_platform_operation_uuid

    json_mobile_platform_operation_uuid_in: list[str] | Unset = UNSET
    if not isinstance(mobile_platform_operation_uuid_in, Unset):
        json_mobile_platform_operation_uuid_in = mobile_platform_operation_uuid_in

    params["mobilePlatformOperation__uuid__in"] = json_mobile_platform_operation_uuid_in

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

    json_observation: list[int] | Unset = UNSET
    if not isinstance(observation, Unset):
        json_observation = observation

    params["observation"] = json_observation

    json_observation_in: list[int] | Unset = UNSET
    if not isinstance(observation_in, Unset):
        json_observation_in = observation_in

    params["observation__in"] = json_observation_in

    params["observation__isnull"] = observation_isnull

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

    params["outputDescription"] = output_description

    json_output_description_in: list[int] | Unset = UNSET
    if not isinstance(output_description_in, Unset):
        json_output_description_in = output_description_in

    params["outputDescription__in"] = json_output_description_in

    params["outputDescription__isnull"] = output_description_isnull

    params["referenceable_ptr"] = referenceable_ptr

    json_referenceable_ptr_in: list[int] | Unset = UNSET
    if not isinstance(referenceable_ptr_in, Unset):
        json_referenceable_ptr_in = referenceable_ptr_in

    params["referenceable_ptr__in"] = json_referenceable_ptr_in

    params["referenceable_ptr__isnull"] = referenceable_ptr_isnull

    json_responsiblepartyinfo: list[int] | Unset = UNSET
    if not isinstance(responsiblepartyinfo, Unset):
        json_responsiblepartyinfo = responsiblepartyinfo

    params["responsiblepartyinfo"] = json_responsiblepartyinfo

    json_responsiblepartyinfo_in: list[int] | Unset = UNSET
    if not isinstance(responsiblepartyinfo_in, Unset):
        json_responsiblepartyinfo_in = responsiblepartyinfo_in

    params["responsiblepartyinfo__in"] = json_responsiblepartyinfo_in

    params["responsiblepartyinfo__isnull"] = responsiblepartyinfo_isnull

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
        json_title_in = title_in

    params["title__in"] = json_title_in

    params["title__iregex"] = title_iregex

    params["title__isnull"] = title_isnull

    params["title__istartswith"] = title_istartswith

    params["title__lt"] = title_lt

    params["title__lte"] = title_lte

    json_title_range: list[str] | Unset = UNSET
    if not isinstance(title_range, Unset):
        json_title_range = title_range

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
        "url": "/api/v3/acquisitions/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedProcedureAcquisitionReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedProcedureAcquisitionReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    compositeprocess: list[int] | Unset = UNSET,
    compositeprocess_in: list[int] | Unset = UNSET,
    compositeprocess_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    image_details: list[int] | Unset = UNSET,
    image_details_in: list[int] | Unset = UNSET,
    image_details_isnull: bool | Unset = UNSET,
    independent_instrument: list[int] | Unset = UNSET,
    independent_instrument_in: list[int] | Unset = UNSET,
    independent_instrument_isnull: bool | Unset = UNSET,
    instrumentplatformpair: list[int] | Unset = UNSET,
    instrumentplatformpair_in: list[int] | Unset = UNSET,
    instrumentplatformpair_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobile_platform_operation: list[int] | Unset = UNSET,
    mobile_platform_operation_in: list[int] | Unset = UNSET,
    mobile_platform_operation_isnull: bool | Unset = UNSET,
    mobile_platform_operation_ob_id: int | Unset = UNSET,
    mobile_platform_operation_ob_id_in: list[int] | Unset = UNSET,
    mobile_platform_operation_uuid: str | Unset = UNSET,
    mobile_platform_operation_uuid_in: list[str] | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    output_description: int | Unset = UNSET,
    output_description_in: list[int] | Unset = UNSET,
    output_description_isnull: bool | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
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
) -> Response[PaginatedProcedureAcquisitionReadList]:
    """Get a list of ProcedureAcquisition objects. ProcedureAcquisitions have a 1:1 mapping with
    Observations.

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
        compositeprocess (list[int] | Unset):
        compositeprocess_in (list[int] | Unset):
        compositeprocess_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        image_details (list[int] | Unset):
        image_details_in (list[int] | Unset):
        image_details_isnull (bool | Unset):
        independent_instrument (list[int] | Unset):
        independent_instrument_in (list[int] | Unset):
        independent_instrument_isnull (bool | Unset):
        instrumentplatformpair (list[int] | Unset):
        instrumentplatformpair_in (list[int] | Unset):
        instrumentplatformpair_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobile_platform_operation (list[int] | Unset):
        mobile_platform_operation_in (list[int] | Unset):
        mobile_platform_operation_isnull (bool | Unset):
        mobile_platform_operation_ob_id (int | Unset):
        mobile_platform_operation_ob_id_in (list[int] | Unset):
        mobile_platform_operation_uuid (str | Unset):
        mobile_platform_operation_uuid_in (list[str] | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
        output_description (int | Unset):
        output_description_in (list[int] | Unset):
        output_description_isnull (bool | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
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
        compositeprocess=compositeprocess,
        compositeprocess_in=compositeprocess_in,
        compositeprocess_isnull=compositeprocess_isnull,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        image_details=image_details,
        image_details_in=image_details_in,
        image_details_isnull=image_details_isnull,
        independent_instrument=independent_instrument,
        independent_instrument_in=independent_instrument_in,
        independent_instrument_isnull=independent_instrument_isnull,
        instrumentplatformpair=instrumentplatformpair,
        instrumentplatformpair_in=instrumentplatformpair_in,
        instrumentplatformpair_isnull=instrumentplatformpair_isnull,
        limit=limit,
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        mobile_platform_operation=mobile_platform_operation,
        mobile_platform_operation_in=mobile_platform_operation_in,
        mobile_platform_operation_isnull=mobile_platform_operation_isnull,
        mobile_platform_operation_ob_id=mobile_platform_operation_ob_id,
        mobile_platform_operation_ob_id_in=mobile_platform_operation_ob_id_in,
        mobile_platform_operation_uuid=mobile_platform_operation_uuid,
        mobile_platform_operation_uuid_in=mobile_platform_operation_uuid_in,
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
        offset=offset,
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        ordering=ordering,
        output_description=output_description,
        output_description_in=output_description_in,
        output_description_isnull=output_description_isnull,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
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
    compositeprocess: list[int] | Unset = UNSET,
    compositeprocess_in: list[int] | Unset = UNSET,
    compositeprocess_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    image_details: list[int] | Unset = UNSET,
    image_details_in: list[int] | Unset = UNSET,
    image_details_isnull: bool | Unset = UNSET,
    independent_instrument: list[int] | Unset = UNSET,
    independent_instrument_in: list[int] | Unset = UNSET,
    independent_instrument_isnull: bool | Unset = UNSET,
    instrumentplatformpair: list[int] | Unset = UNSET,
    instrumentplatformpair_in: list[int] | Unset = UNSET,
    instrumentplatformpair_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobile_platform_operation: list[int] | Unset = UNSET,
    mobile_platform_operation_in: list[int] | Unset = UNSET,
    mobile_platform_operation_isnull: bool | Unset = UNSET,
    mobile_platform_operation_ob_id: int | Unset = UNSET,
    mobile_platform_operation_ob_id_in: list[int] | Unset = UNSET,
    mobile_platform_operation_uuid: str | Unset = UNSET,
    mobile_platform_operation_uuid_in: list[str] | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    output_description: int | Unset = UNSET,
    output_description_in: list[int] | Unset = UNSET,
    output_description_isnull: bool | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
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
) -> PaginatedProcedureAcquisitionReadList | None:
    """Get a list of ProcedureAcquisition objects. ProcedureAcquisitions have a 1:1 mapping with
    Observations.

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
        compositeprocess (list[int] | Unset):
        compositeprocess_in (list[int] | Unset):
        compositeprocess_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        image_details (list[int] | Unset):
        image_details_in (list[int] | Unset):
        image_details_isnull (bool | Unset):
        independent_instrument (list[int] | Unset):
        independent_instrument_in (list[int] | Unset):
        independent_instrument_isnull (bool | Unset):
        instrumentplatformpair (list[int] | Unset):
        instrumentplatformpair_in (list[int] | Unset):
        instrumentplatformpair_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobile_platform_operation (list[int] | Unset):
        mobile_platform_operation_in (list[int] | Unset):
        mobile_platform_operation_isnull (bool | Unset):
        mobile_platform_operation_ob_id (int | Unset):
        mobile_platform_operation_ob_id_in (list[int] | Unset):
        mobile_platform_operation_uuid (str | Unset):
        mobile_platform_operation_uuid_in (list[str] | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
        output_description (int | Unset):
        output_description_in (list[int] | Unset):
        output_description_isnull (bool | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
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
        compositeprocess=compositeprocess,
        compositeprocess_in=compositeprocess_in,
        compositeprocess_isnull=compositeprocess_isnull,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        image_details=image_details,
        image_details_in=image_details_in,
        image_details_isnull=image_details_isnull,
        independent_instrument=independent_instrument,
        independent_instrument_in=independent_instrument_in,
        independent_instrument_isnull=independent_instrument_isnull,
        instrumentplatformpair=instrumentplatformpair,
        instrumentplatformpair_in=instrumentplatformpair_in,
        instrumentplatformpair_isnull=instrumentplatformpair_isnull,
        limit=limit,
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        mobile_platform_operation=mobile_platform_operation,
        mobile_platform_operation_in=mobile_platform_operation_in,
        mobile_platform_operation_isnull=mobile_platform_operation_isnull,
        mobile_platform_operation_ob_id=mobile_platform_operation_ob_id,
        mobile_platform_operation_ob_id_in=mobile_platform_operation_ob_id_in,
        mobile_platform_operation_uuid=mobile_platform_operation_uuid,
        mobile_platform_operation_uuid_in=mobile_platform_operation_uuid_in,
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
        offset=offset,
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        ordering=ordering,
        output_description=output_description,
        output_description_in=output_description_in,
        output_description_isnull=output_description_isnull,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
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
    compositeprocess: list[int] | Unset = UNSET,
    compositeprocess_in: list[int] | Unset = UNSET,
    compositeprocess_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    image_details: list[int] | Unset = UNSET,
    image_details_in: list[int] | Unset = UNSET,
    image_details_isnull: bool | Unset = UNSET,
    independent_instrument: list[int] | Unset = UNSET,
    independent_instrument_in: list[int] | Unset = UNSET,
    independent_instrument_isnull: bool | Unset = UNSET,
    instrumentplatformpair: list[int] | Unset = UNSET,
    instrumentplatformpair_in: list[int] | Unset = UNSET,
    instrumentplatformpair_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobile_platform_operation: list[int] | Unset = UNSET,
    mobile_platform_operation_in: list[int] | Unset = UNSET,
    mobile_platform_operation_isnull: bool | Unset = UNSET,
    mobile_platform_operation_ob_id: int | Unset = UNSET,
    mobile_platform_operation_ob_id_in: list[int] | Unset = UNSET,
    mobile_platform_operation_uuid: str | Unset = UNSET,
    mobile_platform_operation_uuid_in: list[str] | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    output_description: int | Unset = UNSET,
    output_description_in: list[int] | Unset = UNSET,
    output_description_isnull: bool | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
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
) -> Response[PaginatedProcedureAcquisitionReadList]:
    """Get a list of ProcedureAcquisition objects. ProcedureAcquisitions have a 1:1 mapping with
    Observations.

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
        compositeprocess (list[int] | Unset):
        compositeprocess_in (list[int] | Unset):
        compositeprocess_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        image_details (list[int] | Unset):
        image_details_in (list[int] | Unset):
        image_details_isnull (bool | Unset):
        independent_instrument (list[int] | Unset):
        independent_instrument_in (list[int] | Unset):
        independent_instrument_isnull (bool | Unset):
        instrumentplatformpair (list[int] | Unset):
        instrumentplatformpair_in (list[int] | Unset):
        instrumentplatformpair_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobile_platform_operation (list[int] | Unset):
        mobile_platform_operation_in (list[int] | Unset):
        mobile_platform_operation_isnull (bool | Unset):
        mobile_platform_operation_ob_id (int | Unset):
        mobile_platform_operation_ob_id_in (list[int] | Unset):
        mobile_platform_operation_uuid (str | Unset):
        mobile_platform_operation_uuid_in (list[str] | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
        output_description (int | Unset):
        output_description_in (list[int] | Unset):
        output_description_isnull (bool | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
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
        compositeprocess=compositeprocess,
        compositeprocess_in=compositeprocess_in,
        compositeprocess_isnull=compositeprocess_isnull,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        image_details=image_details,
        image_details_in=image_details_in,
        image_details_isnull=image_details_isnull,
        independent_instrument=independent_instrument,
        independent_instrument_in=independent_instrument_in,
        independent_instrument_isnull=independent_instrument_isnull,
        instrumentplatformpair=instrumentplatformpair,
        instrumentplatformpair_in=instrumentplatformpair_in,
        instrumentplatformpair_isnull=instrumentplatformpair_isnull,
        limit=limit,
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        mobile_platform_operation=mobile_platform_operation,
        mobile_platform_operation_in=mobile_platform_operation_in,
        mobile_platform_operation_isnull=mobile_platform_operation_isnull,
        mobile_platform_operation_ob_id=mobile_platform_operation_ob_id,
        mobile_platform_operation_ob_id_in=mobile_platform_operation_ob_id_in,
        mobile_platform_operation_uuid=mobile_platform_operation_uuid,
        mobile_platform_operation_uuid_in=mobile_platform_operation_uuid_in,
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
        offset=offset,
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        ordering=ordering,
        output_description=output_description,
        output_description_in=output_description_in,
        output_description_isnull=output_description_isnull,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
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
    compositeprocess: list[int] | Unset = UNSET,
    compositeprocess_in: list[int] | Unset = UNSET,
    compositeprocess_isnull: bool | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    image_details: list[int] | Unset = UNSET,
    image_details_in: list[int] | Unset = UNSET,
    image_details_isnull: bool | Unset = UNSET,
    independent_instrument: list[int] | Unset = UNSET,
    independent_instrument_in: list[int] | Unset = UNSET,
    independent_instrument_isnull: bool | Unset = UNSET,
    instrumentplatformpair: list[int] | Unset = UNSET,
    instrumentplatformpair_in: list[int] | Unset = UNSET,
    instrumentplatformpair_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    mobile_platform_operation: list[int] | Unset = UNSET,
    mobile_platform_operation_in: list[int] | Unset = UNSET,
    mobile_platform_operation_isnull: bool | Unset = UNSET,
    mobile_platform_operation_ob_id: int | Unset = UNSET,
    mobile_platform_operation_ob_id_in: list[int] | Unset = UNSET,
    mobile_platform_operation_uuid: str | Unset = UNSET,
    mobile_platform_operation_uuid_in: list[str] | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
    output_description: int | Unset = UNSET,
    output_description_in: list[int] | Unset = UNSET,
    output_description_isnull: bool | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
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
) -> PaginatedProcedureAcquisitionReadList | None:
    """Get a list of ProcedureAcquisition objects. ProcedureAcquisitions have a 1:1 mapping with
    Observations.

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
        compositeprocess (list[int] | Unset):
        compositeprocess_in (list[int] | Unset):
        compositeprocess_isnull (bool | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        image_details (list[int] | Unset):
        image_details_in (list[int] | Unset):
        image_details_isnull (bool | Unset):
        independent_instrument (list[int] | Unset):
        independent_instrument_in (list[int] | Unset):
        independent_instrument_isnull (bool | Unset):
        instrumentplatformpair (list[int] | Unset):
        instrumentplatformpair_in (list[int] | Unset):
        instrumentplatformpair_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        mobile_platform_operation (list[int] | Unset):
        mobile_platform_operation_in (list[int] | Unset):
        mobile_platform_operation_isnull (bool | Unset):
        mobile_platform_operation_ob_id (int | Unset):
        mobile_platform_operation_ob_id_in (list[int] | Unset):
        mobile_platform_operation_uuid (str | Unset):
        mobile_platform_operation_uuid_in (list[str] | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
        output_description (int | Unset):
        output_description_in (list[int] | Unset):
        output_description_isnull (bool | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
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
            compositeprocess=compositeprocess,
            compositeprocess_in=compositeprocess_in,
            compositeprocess_isnull=compositeprocess_isnull,
            identifier=identifier,
            identifier_in=identifier_in,
            identifier_isnull=identifier_isnull,
            image_details=image_details,
            image_details_in=image_details_in,
            image_details_isnull=image_details_isnull,
            independent_instrument=independent_instrument,
            independent_instrument_in=independent_instrument_in,
            independent_instrument_isnull=independent_instrument_isnull,
            instrumentplatformpair=instrumentplatformpair,
            instrumentplatformpair_in=instrumentplatformpair_in,
            instrumentplatformpair_isnull=instrumentplatformpair_isnull,
            limit=limit,
            migrationproperty=migrationproperty,
            migrationproperty_in=migrationproperty_in,
            migrationproperty_isnull=migrationproperty_isnull,
            mobile_platform_operation=mobile_platform_operation,
            mobile_platform_operation_in=mobile_platform_operation_in,
            mobile_platform_operation_isnull=mobile_platform_operation_isnull,
            mobile_platform_operation_ob_id=mobile_platform_operation_ob_id,
            mobile_platform_operation_ob_id_in=mobile_platform_operation_ob_id_in,
            mobile_platform_operation_uuid=mobile_platform_operation_uuid,
            mobile_platform_operation_uuid_in=mobile_platform_operation_uuid_in,
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
            offset=offset,
            onlineresource=onlineresource,
            onlineresource_in=onlineresource_in,
            onlineresource_isnull=onlineresource_isnull,
            ordering=ordering,
            output_description=output_description,
            output_description_in=output_description_in,
            output_description_isnull=output_description_isnull,
            referenceable_ptr=referenceable_ptr,
            referenceable_ptr_in=referenceable_ptr_in,
            referenceable_ptr_isnull=referenceable_ptr_isnull,
            responsiblepartyinfo=responsiblepartyinfo,
            responsiblepartyinfo_in=responsiblepartyinfo_in,
            responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
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
