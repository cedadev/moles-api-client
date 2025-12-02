from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_result_read_list import PaginatedResultReadList
from ...models.results_list_ceda_curation_category import ResultsListCEDACurationCategory
from ...models.results_list_storage_location import ResultsListStorageLocation
from ...models.results_list_storage_status import ResultsListStorageStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    curation_category: ResultsListCEDACurationCategory | Unset = UNSET,
    curation_category_contains: str | Unset = UNSET,
    curation_category_endswith: str | Unset = UNSET,
    curation_category_gt: str | Unset = UNSET,
    curation_category_gte: str | Unset = UNSET,
    curation_category_icontains: str | Unset = UNSET,
    curation_category_iendswith: str | Unset = UNSET,
    curation_category_iexact: str | Unset = UNSET,
    curation_category_in: list[str] | Unset = UNSET,
    curation_category_iregex: str | Unset = UNSET,
    curation_category_isnull: bool | Unset = UNSET,
    curation_category_istartswith: str | Unset = UNSET,
    curation_category_lt: str | Unset = UNSET,
    curation_category_lte: str | Unset = UNSET,
    curation_category_range: list[str] | Unset = UNSET,
    curation_category_regex: str | Unset = UNSET,
    curation_category_startswith: str | Unset = UNSET,
    current_data_path: list[int] | Unset = UNSET,
    current_data_path_in: list[int] | Unset = UNSET,
    current_data_path_isnull: bool | Unset = UNSET,
    data_path: str | Unset = UNSET,
    data_path_contains: str | Unset = UNSET,
    data_path_endswith: str | Unset = UNSET,
    data_path_gt: str | Unset = UNSET,
    data_path_gte: str | Unset = UNSET,
    data_path_icontains: str | Unset = UNSET,
    data_path_iendswith: str | Unset = UNSET,
    data_path_iexact: str | Unset = UNSET,
    data_path_in: list[str] | Unset = UNSET,
    data_path_iregex: str | Unset = UNSET,
    data_path_isnull: bool | Unset = UNSET,
    data_path_istartswith: str | Unset = UNSET,
    data_path_lt: str | Unset = UNSET,
    data_path_lte: str | Unset = UNSET,
    data_path_range: list[str] | Unset = UNSET,
    data_path_regex: str | Unset = UNSET,
    data_path_startswith: str | Unset = UNSET,
    file_format: str | Unset = UNSET,
    file_format_contains: str | Unset = UNSET,
    file_format_endswith: str | Unset = UNSET,
    file_format_gt: str | Unset = UNSET,
    file_format_gte: str | Unset = UNSET,
    file_format_icontains: str | Unset = UNSET,
    file_format_iendswith: str | Unset = UNSET,
    file_format_iexact: str | Unset = UNSET,
    file_format_in: list[str] | Unset = UNSET,
    file_format_iregex: str | Unset = UNSET,
    file_format_isnull: bool | Unset = UNSET,
    file_format_istartswith: str | Unset = UNSET,
    file_format_lt: str | Unset = UNSET,
    file_format_lte: str | Unset = UNSET,
    file_format_range: list[str] | Unset = UNSET,
    file_format_regex: str | Unset = UNSET,
    file_format_startswith: str | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
    number_of_files: int | Unset = UNSET,
    number_of_files_contained_by: int | Unset = UNSET,
    number_of_files_contains: int | Unset = UNSET,
    number_of_files_endswith: int | Unset = UNSET,
    number_of_files_gt: int | Unset = UNSET,
    number_of_files_gte: int | Unset = UNSET,
    number_of_files_icontains: int | Unset = UNSET,
    number_of_files_iendswith: int | Unset = UNSET,
    number_of_files_iexact: int | Unset = UNSET,
    number_of_files_in: list[int] | Unset = UNSET,
    number_of_files_iregex: int | Unset = UNSET,
    number_of_files_isnull: bool | Unset = UNSET,
    number_of_files_istartswith: int | Unset = UNSET,
    number_of_files_lt: int | Unset = UNSET,
    number_of_files_lte: int | Unset = UNSET,
    number_of_files_range: list[int] | Unset = UNSET,
    number_of_files_regex: int | Unset = UNSET,
    number_of_files_startswith: int | Unset = UNSET,
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
    observation_ob_id: int | Unset = UNSET,
    observation_ob_id_in: list[int] | Unset = UNSET,
    observation_uuid: str | Unset = UNSET,
    observation_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    old_data_path: list[int] | Unset = UNSET,
    old_data_path_in: list[int] | Unset = UNSET,
    old_data_path_isnull: bool | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
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
    storage_location: ResultsListStorageLocation | Unset = UNSET,
    storage_location_contains: str | Unset = UNSET,
    storage_location_endswith: str | Unset = UNSET,
    storage_location_gt: str | Unset = UNSET,
    storage_location_gte: str | Unset = UNSET,
    storage_location_icontains: str | Unset = UNSET,
    storage_location_iendswith: str | Unset = UNSET,
    storage_location_iexact: str | Unset = UNSET,
    storage_location_in: list[str] | Unset = UNSET,
    storage_location_iregex: str | Unset = UNSET,
    storage_location_isnull: bool | Unset = UNSET,
    storage_location_istartswith: str | Unset = UNSET,
    storage_location_lt: str | Unset = UNSET,
    storage_location_lte: str | Unset = UNSET,
    storage_location_range: list[str] | Unset = UNSET,
    storage_location_regex: str | Unset = UNSET,
    storage_location_startswith: str | Unset = UNSET,
    storage_status: ResultsListStorageStatus | Unset = UNSET,
    storage_status_contains: str | Unset = UNSET,
    storage_status_endswith: str | Unset = UNSET,
    storage_status_gt: str | Unset = UNSET,
    storage_status_gte: str | Unset = UNSET,
    storage_status_icontains: str | Unset = UNSET,
    storage_status_iendswith: str | Unset = UNSET,
    storage_status_iexact: str | Unset = UNSET,
    storage_status_in: list[str] | Unset = UNSET,
    storage_status_iregex: str | Unset = UNSET,
    storage_status_isnull: bool | Unset = UNSET,
    storage_status_istartswith: str | Unset = UNSET,
    storage_status_lt: str | Unset = UNSET,
    storage_status_lte: str | Unset = UNSET,
    storage_status_range: list[str] | Unset = UNSET,
    storage_status_regex: str | Unset = UNSET,
    storage_status_startswith: str | Unset = UNSET,
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
    volume: int | Unset = UNSET,
    volume_contained_by: int | Unset = UNSET,
    volume_contains: int | Unset = UNSET,
    volume_endswith: int | Unset = UNSET,
    volume_gt: int | Unset = UNSET,
    volume_gte: int | Unset = UNSET,
    volume_icontains: int | Unset = UNSET,
    volume_iendswith: int | Unset = UNSET,
    volume_iexact: int | Unset = UNSET,
    volume_in: list[int] | Unset = UNSET,
    volume_iregex: int | Unset = UNSET,
    volume_isnull: bool | Unset = UNSET,
    volume_istartswith: int | Unset = UNSET,
    volume_lt: int | Unset = UNSET,
    volume_lte: int | Unset = UNSET,
    volume_range: list[int] | Unset = UNSET,
    volume_regex: int | Unset = UNSET,
    volume_startswith: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_curation_category: str | Unset = UNSET
    if not isinstance(curation_category, Unset):
        json_curation_category = curation_category.value

    params["curationCategory"] = json_curation_category

    params["curationCategory__contains"] = curation_category_contains

    params["curationCategory__endswith"] = curation_category_endswith

    params["curationCategory__gt"] = curation_category_gt

    params["curationCategory__gte"] = curation_category_gte

    params["curationCategory__icontains"] = curation_category_icontains

    params["curationCategory__iendswith"] = curation_category_iendswith

    params["curationCategory__iexact"] = curation_category_iexact

    json_curation_category_in: list[str] | Unset = UNSET
    if not isinstance(curation_category_in, Unset):
        json_curation_category_in = ",".join(map(str, curation_category_in))

    params["curationCategory__in"] = json_curation_category_in

    params["curationCategory__iregex"] = curation_category_iregex

    params["curationCategory__isnull"] = curation_category_isnull

    params["curationCategory__istartswith"] = curation_category_istartswith

    params["curationCategory__lt"] = curation_category_lt

    params["curationCategory__lte"] = curation_category_lte

    json_curation_category_range: list[str] | Unset = UNSET
    if not isinstance(curation_category_range, Unset):
        json_curation_category_range = ",".join(map(str, curation_category_range))

    params["curationCategory__range"] = json_curation_category_range

    params["curationCategory__regex"] = curation_category_regex

    params["curationCategory__startswith"] = curation_category_startswith

    json_current_data_path: list[int] | Unset = UNSET
    if not isinstance(current_data_path, Unset):
        json_current_data_path = ",".join(map(str, current_data_path))

    params["currentDataPath"] = json_current_data_path

    json_current_data_path_in: list[int] | Unset = UNSET
    if not isinstance(current_data_path_in, Unset):
        json_current_data_path_in = ",".join(map(str, current_data_path_in))

    params["currentDataPath__in"] = json_current_data_path_in

    params["currentDataPath__isnull"] = current_data_path_isnull

    params["dataPath"] = data_path

    params["dataPath__contains"] = data_path_contains

    params["dataPath__endswith"] = data_path_endswith

    params["dataPath__gt"] = data_path_gt

    params["dataPath__gte"] = data_path_gte

    params["dataPath__icontains"] = data_path_icontains

    params["dataPath__iendswith"] = data_path_iendswith

    params["dataPath__iexact"] = data_path_iexact

    json_data_path_in: list[str] | Unset = UNSET
    if not isinstance(data_path_in, Unset):
        json_data_path_in = ",".join(map(str, data_path_in))

    params["dataPath__in"] = json_data_path_in

    params["dataPath__iregex"] = data_path_iregex

    params["dataPath__isnull"] = data_path_isnull

    params["dataPath__istartswith"] = data_path_istartswith

    params["dataPath__lt"] = data_path_lt

    params["dataPath__lte"] = data_path_lte

    json_data_path_range: list[str] | Unset = UNSET
    if not isinstance(data_path_range, Unset):
        json_data_path_range = ",".join(map(str, data_path_range))

    params["dataPath__range"] = json_data_path_range

    params["dataPath__regex"] = data_path_regex

    params["dataPath__startswith"] = data_path_startswith

    params["fileFormat"] = file_format

    params["fileFormat__contains"] = file_format_contains

    params["fileFormat__endswith"] = file_format_endswith

    params["fileFormat__gt"] = file_format_gt

    params["fileFormat__gte"] = file_format_gte

    params["fileFormat__icontains"] = file_format_icontains

    params["fileFormat__iendswith"] = file_format_iendswith

    params["fileFormat__iexact"] = file_format_iexact

    json_file_format_in: list[str] | Unset = UNSET
    if not isinstance(file_format_in, Unset):
        json_file_format_in = ",".join(map(str, file_format_in))

    params["fileFormat__in"] = json_file_format_in

    params["fileFormat__iregex"] = file_format_iregex

    params["fileFormat__isnull"] = file_format_isnull

    params["fileFormat__istartswith"] = file_format_istartswith

    params["fileFormat__lt"] = file_format_lt

    params["fileFormat__lte"] = file_format_lte

    json_file_format_range: list[str] | Unset = UNSET
    if not isinstance(file_format_range, Unset):
        json_file_format_range = ",".join(map(str, file_format_range))

    params["fileFormat__range"] = json_file_format_range

    params["fileFormat__regex"] = file_format_regex

    params["fileFormat__startswith"] = file_format_startswith

    json_identifier: list[int] | Unset = UNSET
    if not isinstance(identifier, Unset):
        json_identifier = ",".join(map(str, identifier))

    params["identifier"] = json_identifier

    json_identifier_in: list[int] | Unset = UNSET
    if not isinstance(identifier_in, Unset):
        json_identifier_in = ",".join(map(str, identifier_in))

    params["identifier__in"] = json_identifier_in

    params["identifier__isnull"] = identifier_isnull

    params["limit"] = limit

    json_migrationproperty: list[int] | Unset = UNSET
    if not isinstance(migrationproperty, Unset):
        json_migrationproperty = ",".join(map(str, migrationproperty))

    params["migrationproperty"] = json_migrationproperty

    json_migrationproperty_in: list[int] | Unset = UNSET
    if not isinstance(migrationproperty_in, Unset):
        json_migrationproperty_in = ",".join(map(str, migrationproperty_in))

    params["migrationproperty__in"] = json_migrationproperty_in

    params["migrationproperty__isnull"] = migrationproperty_isnull

    json_note: list[int] | Unset = UNSET
    if not isinstance(note, Unset):
        json_note = ",".join(map(str, note))

    params["note"] = json_note

    json_note_in: list[int] | Unset = UNSET
    if not isinstance(note_in, Unset):
        json_note_in = ",".join(map(str, note_in))

    params["note__in"] = json_note_in

    params["note__isnull"] = note_isnull

    params["numberOfFiles"] = number_of_files

    params["numberOfFiles__contained_by"] = number_of_files_contained_by

    params["numberOfFiles__contains"] = number_of_files_contains

    params["numberOfFiles__endswith"] = number_of_files_endswith

    params["numberOfFiles__gt"] = number_of_files_gt

    params["numberOfFiles__gte"] = number_of_files_gte

    params["numberOfFiles__icontains"] = number_of_files_icontains

    params["numberOfFiles__iendswith"] = number_of_files_iendswith

    params["numberOfFiles__iexact"] = number_of_files_iexact

    json_number_of_files_in: list[int] | Unset = UNSET
    if not isinstance(number_of_files_in, Unset):
        json_number_of_files_in = ",".join(map(str, number_of_files_in))

    params["numberOfFiles__in"] = json_number_of_files_in

    params["numberOfFiles__iregex"] = number_of_files_iregex

    params["numberOfFiles__isnull"] = number_of_files_isnull

    params["numberOfFiles__istartswith"] = number_of_files_istartswith

    params["numberOfFiles__lt"] = number_of_files_lt

    params["numberOfFiles__lte"] = number_of_files_lte

    json_number_of_files_range: list[int] | Unset = UNSET
    if not isinstance(number_of_files_range, Unset):
        json_number_of_files_range = ",".join(map(str, number_of_files_range))

    params["numberOfFiles__range"] = json_number_of_files_range

    params["numberOfFiles__regex"] = number_of_files_regex

    params["numberOfFiles__startswith"] = number_of_files_startswith

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

    params["observation"] = observation

    json_observation_in: list[int] | Unset = UNSET
    if not isinstance(observation_in, Unset):
        json_observation_in = ",".join(map(str, observation_in))

    params["observation__in"] = json_observation_in

    params["observation__isnull"] = observation_isnull

    params["observation__ob_id"] = observation_ob_id

    json_observation_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(observation_ob_id_in, Unset):
        json_observation_ob_id_in = ",".join(map(str, observation_ob_id_in))

    params["observation__ob_id__in"] = json_observation_ob_id_in

    params["observation__uuid"] = observation_uuid

    json_observation_uuid_in: list[str] | Unset = UNSET
    if not isinstance(observation_uuid_in, Unset):
        json_observation_uuid_in = ",".join(map(str, observation_uuid_in))

    params["observation__uuid__in"] = json_observation_uuid_in

    params["offset"] = offset

    json_old_data_path: list[int] | Unset = UNSET
    if not isinstance(old_data_path, Unset):
        json_old_data_path = ",".join(map(str, old_data_path))

    params["oldDataPath"] = json_old_data_path

    json_old_data_path_in: list[int] | Unset = UNSET
    if not isinstance(old_data_path_in, Unset):
        json_old_data_path_in = ",".join(map(str, old_data_path_in))

    params["oldDataPath__in"] = json_old_data_path_in

    params["oldDataPath__isnull"] = old_data_path_isnull

    json_onlineresource: list[int] | Unset = UNSET
    if not isinstance(onlineresource, Unset):
        json_onlineresource = ",".join(map(str, onlineresource))

    params["onlineresource"] = json_onlineresource

    json_onlineresource_in: list[int] | Unset = UNSET
    if not isinstance(onlineresource_in, Unset):
        json_onlineresource_in = ",".join(map(str, onlineresource_in))

    params["onlineresource__in"] = json_onlineresource_in

    params["onlineresource__isnull"] = onlineresource_isnull

    params["ordering"] = ordering

    params["referenceable_ptr"] = referenceable_ptr

    json_referenceable_ptr_in: list[int] | Unset = UNSET
    if not isinstance(referenceable_ptr_in, Unset):
        json_referenceable_ptr_in = ",".join(map(str, referenceable_ptr_in))

    params["referenceable_ptr__in"] = json_referenceable_ptr_in

    params["referenceable_ptr__isnull"] = referenceable_ptr_isnull

    json_responsiblepartyinfo: list[int] | Unset = UNSET
    if not isinstance(responsiblepartyinfo, Unset):
        json_responsiblepartyinfo = ",".join(map(str, responsiblepartyinfo))

    params["responsiblepartyinfo"] = json_responsiblepartyinfo

    json_responsiblepartyinfo_in: list[int] | Unset = UNSET
    if not isinstance(responsiblepartyinfo_in, Unset):
        json_responsiblepartyinfo_in = ",".join(map(str, responsiblepartyinfo_in))

    params["responsiblepartyinfo__in"] = json_responsiblepartyinfo_in

    params["responsiblepartyinfo__isnull"] = responsiblepartyinfo_isnull

    json_review: list[int] | Unset = UNSET
    if not isinstance(review, Unset):
        json_review = ",".join(map(str, review))

    params["review"] = json_review

    json_review_in: list[int] | Unset = UNSET
    if not isinstance(review_in, Unset):
        json_review_in = ",".join(map(str, review_in))

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

    json_storage_location: str | Unset = UNSET
    if not isinstance(storage_location, Unset):
        json_storage_location = storage_location.value

    params["storageLocation"] = json_storage_location

    params["storageLocation__contains"] = storage_location_contains

    params["storageLocation__endswith"] = storage_location_endswith

    params["storageLocation__gt"] = storage_location_gt

    params["storageLocation__gte"] = storage_location_gte

    params["storageLocation__icontains"] = storage_location_icontains

    params["storageLocation__iendswith"] = storage_location_iendswith

    params["storageLocation__iexact"] = storage_location_iexact

    json_storage_location_in: list[str] | Unset = UNSET
    if not isinstance(storage_location_in, Unset):
        json_storage_location_in = ",".join(map(str, storage_location_in))

    params["storageLocation__in"] = json_storage_location_in

    params["storageLocation__iregex"] = storage_location_iregex

    params["storageLocation__isnull"] = storage_location_isnull

    params["storageLocation__istartswith"] = storage_location_istartswith

    params["storageLocation__lt"] = storage_location_lt

    params["storageLocation__lte"] = storage_location_lte

    json_storage_location_range: list[str] | Unset = UNSET
    if not isinstance(storage_location_range, Unset):
        json_storage_location_range = ",".join(map(str, storage_location_range))

    params["storageLocation__range"] = json_storage_location_range

    params["storageLocation__regex"] = storage_location_regex

    params["storageLocation__startswith"] = storage_location_startswith

    json_storage_status: str | Unset = UNSET
    if not isinstance(storage_status, Unset):
        json_storage_status = storage_status.value

    params["storageStatus"] = json_storage_status

    params["storageStatus__contains"] = storage_status_contains

    params["storageStatus__endswith"] = storage_status_endswith

    params["storageStatus__gt"] = storage_status_gt

    params["storageStatus__gte"] = storage_status_gte

    params["storageStatus__icontains"] = storage_status_icontains

    params["storageStatus__iendswith"] = storage_status_iendswith

    params["storageStatus__iexact"] = storage_status_iexact

    json_storage_status_in: list[str] | Unset = UNSET
    if not isinstance(storage_status_in, Unset):
        json_storage_status_in = ",".join(map(str, storage_status_in))

    params["storageStatus__in"] = json_storage_status_in

    params["storageStatus__iregex"] = storage_status_iregex

    params["storageStatus__isnull"] = storage_status_isnull

    params["storageStatus__istartswith"] = storage_status_istartswith

    params["storageStatus__lt"] = storage_status_lt

    params["storageStatus__lte"] = storage_status_lte

    json_storage_status_range: list[str] | Unset = UNSET
    if not isinstance(storage_status_range, Unset):
        json_storage_status_range = ",".join(map(str, storage_status_range))

    params["storageStatus__range"] = json_storage_status_range

    params["storageStatus__regex"] = storage_status_regex

    params["storageStatus__startswith"] = storage_status_startswith

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

    params["volume"] = volume

    params["volume__contained_by"] = volume_contained_by

    params["volume__contains"] = volume_contains

    params["volume__endswith"] = volume_endswith

    params["volume__gt"] = volume_gt

    params["volume__gte"] = volume_gte

    params["volume__icontains"] = volume_icontains

    params["volume__iendswith"] = volume_iendswith

    params["volume__iexact"] = volume_iexact

    json_volume_in: list[int] | Unset = UNSET
    if not isinstance(volume_in, Unset):
        json_volume_in = ",".join(map(str, volume_in))

    params["volume__in"] = json_volume_in

    params["volume__iregex"] = volume_iregex

    params["volume__isnull"] = volume_isnull

    params["volume__istartswith"] = volume_istartswith

    params["volume__lt"] = volume_lt

    params["volume__lte"] = volume_lte

    json_volume_range: list[int] | Unset = UNSET
    if not isinstance(volume_range, Unset):
        json_volume_range = ",".join(map(str, volume_range))

    params["volume__range"] = json_volume_range

    params["volume__regex"] = volume_regex

    params["volume__startswith"] = volume_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/results/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedResultReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedResultReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedResultReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    curation_category: ResultsListCEDACurationCategory | Unset = UNSET,
    curation_category_contains: str | Unset = UNSET,
    curation_category_endswith: str | Unset = UNSET,
    curation_category_gt: str | Unset = UNSET,
    curation_category_gte: str | Unset = UNSET,
    curation_category_icontains: str | Unset = UNSET,
    curation_category_iendswith: str | Unset = UNSET,
    curation_category_iexact: str | Unset = UNSET,
    curation_category_in: list[str] | Unset = UNSET,
    curation_category_iregex: str | Unset = UNSET,
    curation_category_isnull: bool | Unset = UNSET,
    curation_category_istartswith: str | Unset = UNSET,
    curation_category_lt: str | Unset = UNSET,
    curation_category_lte: str | Unset = UNSET,
    curation_category_range: list[str] | Unset = UNSET,
    curation_category_regex: str | Unset = UNSET,
    curation_category_startswith: str | Unset = UNSET,
    current_data_path: list[int] | Unset = UNSET,
    current_data_path_in: list[int] | Unset = UNSET,
    current_data_path_isnull: bool | Unset = UNSET,
    data_path: str | Unset = UNSET,
    data_path_contains: str | Unset = UNSET,
    data_path_endswith: str | Unset = UNSET,
    data_path_gt: str | Unset = UNSET,
    data_path_gte: str | Unset = UNSET,
    data_path_icontains: str | Unset = UNSET,
    data_path_iendswith: str | Unset = UNSET,
    data_path_iexact: str | Unset = UNSET,
    data_path_in: list[str] | Unset = UNSET,
    data_path_iregex: str | Unset = UNSET,
    data_path_isnull: bool | Unset = UNSET,
    data_path_istartswith: str | Unset = UNSET,
    data_path_lt: str | Unset = UNSET,
    data_path_lte: str | Unset = UNSET,
    data_path_range: list[str] | Unset = UNSET,
    data_path_regex: str | Unset = UNSET,
    data_path_startswith: str | Unset = UNSET,
    file_format: str | Unset = UNSET,
    file_format_contains: str | Unset = UNSET,
    file_format_endswith: str | Unset = UNSET,
    file_format_gt: str | Unset = UNSET,
    file_format_gte: str | Unset = UNSET,
    file_format_icontains: str | Unset = UNSET,
    file_format_iendswith: str | Unset = UNSET,
    file_format_iexact: str | Unset = UNSET,
    file_format_in: list[str] | Unset = UNSET,
    file_format_iregex: str | Unset = UNSET,
    file_format_isnull: bool | Unset = UNSET,
    file_format_istartswith: str | Unset = UNSET,
    file_format_lt: str | Unset = UNSET,
    file_format_lte: str | Unset = UNSET,
    file_format_range: list[str] | Unset = UNSET,
    file_format_regex: str | Unset = UNSET,
    file_format_startswith: str | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
    number_of_files: int | Unset = UNSET,
    number_of_files_contained_by: int | Unset = UNSET,
    number_of_files_contains: int | Unset = UNSET,
    number_of_files_endswith: int | Unset = UNSET,
    number_of_files_gt: int | Unset = UNSET,
    number_of_files_gte: int | Unset = UNSET,
    number_of_files_icontains: int | Unset = UNSET,
    number_of_files_iendswith: int | Unset = UNSET,
    number_of_files_iexact: int | Unset = UNSET,
    number_of_files_in: list[int] | Unset = UNSET,
    number_of_files_iregex: int | Unset = UNSET,
    number_of_files_isnull: bool | Unset = UNSET,
    number_of_files_istartswith: int | Unset = UNSET,
    number_of_files_lt: int | Unset = UNSET,
    number_of_files_lte: int | Unset = UNSET,
    number_of_files_range: list[int] | Unset = UNSET,
    number_of_files_regex: int | Unset = UNSET,
    number_of_files_startswith: int | Unset = UNSET,
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
    observation_ob_id: int | Unset = UNSET,
    observation_ob_id_in: list[int] | Unset = UNSET,
    observation_uuid: str | Unset = UNSET,
    observation_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    old_data_path: list[int] | Unset = UNSET,
    old_data_path_in: list[int] | Unset = UNSET,
    old_data_path_isnull: bool | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
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
    storage_location: ResultsListStorageLocation | Unset = UNSET,
    storage_location_contains: str | Unset = UNSET,
    storage_location_endswith: str | Unset = UNSET,
    storage_location_gt: str | Unset = UNSET,
    storage_location_gte: str | Unset = UNSET,
    storage_location_icontains: str | Unset = UNSET,
    storage_location_iendswith: str | Unset = UNSET,
    storage_location_iexact: str | Unset = UNSET,
    storage_location_in: list[str] | Unset = UNSET,
    storage_location_iregex: str | Unset = UNSET,
    storage_location_isnull: bool | Unset = UNSET,
    storage_location_istartswith: str | Unset = UNSET,
    storage_location_lt: str | Unset = UNSET,
    storage_location_lte: str | Unset = UNSET,
    storage_location_range: list[str] | Unset = UNSET,
    storage_location_regex: str | Unset = UNSET,
    storage_location_startswith: str | Unset = UNSET,
    storage_status: ResultsListStorageStatus | Unset = UNSET,
    storage_status_contains: str | Unset = UNSET,
    storage_status_endswith: str | Unset = UNSET,
    storage_status_gt: str | Unset = UNSET,
    storage_status_gte: str | Unset = UNSET,
    storage_status_icontains: str | Unset = UNSET,
    storage_status_iendswith: str | Unset = UNSET,
    storage_status_iexact: str | Unset = UNSET,
    storage_status_in: list[str] | Unset = UNSET,
    storage_status_iregex: str | Unset = UNSET,
    storage_status_isnull: bool | Unset = UNSET,
    storage_status_istartswith: str | Unset = UNSET,
    storage_status_lt: str | Unset = UNSET,
    storage_status_lte: str | Unset = UNSET,
    storage_status_range: list[str] | Unset = UNSET,
    storage_status_regex: str | Unset = UNSET,
    storage_status_startswith: str | Unset = UNSET,
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
    volume: int | Unset = UNSET,
    volume_contained_by: int | Unset = UNSET,
    volume_contains: int | Unset = UNSET,
    volume_endswith: int | Unset = UNSET,
    volume_gt: int | Unset = UNSET,
    volume_gte: int | Unset = UNSET,
    volume_icontains: int | Unset = UNSET,
    volume_iendswith: int | Unset = UNSET,
    volume_iexact: int | Unset = UNSET,
    volume_in: list[int] | Unset = UNSET,
    volume_iregex: int | Unset = UNSET,
    volume_isnull: bool | Unset = UNSET,
    volume_istartswith: int | Unset = UNSET,
    volume_lt: int | Unset = UNSET,
    volume_lte: int | Unset = UNSET,
    volume_range: list[int] | Unset = UNSET,
    volume_regex: int | Unset = UNSET,
    volume_startswith: int | Unset = UNSET,
) -> Response[PaginatedResultReadList]:
    """Get a list of Result objects. Results have a 1:1 mapping with Observations.

    Args:
        curation_category (ResultsListCEDACurationCategory | Unset):
        curation_category_contains (str | Unset):
        curation_category_endswith (str | Unset):
        curation_category_gt (str | Unset):
        curation_category_gte (str | Unset):
        curation_category_icontains (str | Unset):
        curation_category_iendswith (str | Unset):
        curation_category_iexact (str | Unset):
        curation_category_in (list[str] | Unset):
        curation_category_iregex (str | Unset):
        curation_category_isnull (bool | Unset):
        curation_category_istartswith (str | Unset):
        curation_category_lt (str | Unset):
        curation_category_lte (str | Unset):
        curation_category_range (list[str] | Unset):
        curation_category_regex (str | Unset):
        curation_category_startswith (str | Unset):
        current_data_path (list[int] | Unset):
        current_data_path_in (list[int] | Unset):
        current_data_path_isnull (bool | Unset):
        data_path (str | Unset):
        data_path_contains (str | Unset):
        data_path_endswith (str | Unset):
        data_path_gt (str | Unset):
        data_path_gte (str | Unset):
        data_path_icontains (str | Unset):
        data_path_iendswith (str | Unset):
        data_path_iexact (str | Unset):
        data_path_in (list[str] | Unset):
        data_path_iregex (str | Unset):
        data_path_isnull (bool | Unset):
        data_path_istartswith (str | Unset):
        data_path_lt (str | Unset):
        data_path_lte (str | Unset):
        data_path_range (list[str] | Unset):
        data_path_regex (str | Unset):
        data_path_startswith (str | Unset):
        file_format (str | Unset):
        file_format_contains (str | Unset):
        file_format_endswith (str | Unset):
        file_format_gt (str | Unset):
        file_format_gte (str | Unset):
        file_format_icontains (str | Unset):
        file_format_iendswith (str | Unset):
        file_format_iexact (str | Unset):
        file_format_in (list[str] | Unset):
        file_format_iregex (str | Unset):
        file_format_isnull (bool | Unset):
        file_format_istartswith (str | Unset):
        file_format_lt (str | Unset):
        file_format_lte (str | Unset):
        file_format_range (list[str] | Unset):
        file_format_regex (str | Unset):
        file_format_startswith (str | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
        number_of_files (int | Unset):
        number_of_files_contained_by (int | Unset):
        number_of_files_contains (int | Unset):
        number_of_files_endswith (int | Unset):
        number_of_files_gt (int | Unset):
        number_of_files_gte (int | Unset):
        number_of_files_icontains (int | Unset):
        number_of_files_iendswith (int | Unset):
        number_of_files_iexact (int | Unset):
        number_of_files_in (list[int] | Unset):
        number_of_files_iregex (int | Unset):
        number_of_files_isnull (bool | Unset):
        number_of_files_istartswith (int | Unset):
        number_of_files_lt (int | Unset):
        number_of_files_lte (int | Unset):
        number_of_files_range (list[int] | Unset):
        number_of_files_regex (int | Unset):
        number_of_files_startswith (int | Unset):
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
        observation_ob_id (int | Unset):
        observation_ob_id_in (list[int] | Unset):
        observation_uuid (str | Unset):
        observation_uuid_in (list[str] | Unset):
        offset (int | Unset):
        old_data_path (list[int] | Unset):
        old_data_path_in (list[int] | Unset):
        old_data_path_isnull (bool | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
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
        storage_location (ResultsListStorageLocation | Unset):
        storage_location_contains (str | Unset):
        storage_location_endswith (str | Unset):
        storage_location_gt (str | Unset):
        storage_location_gte (str | Unset):
        storage_location_icontains (str | Unset):
        storage_location_iendswith (str | Unset):
        storage_location_iexact (str | Unset):
        storage_location_in (list[str] | Unset):
        storage_location_iregex (str | Unset):
        storage_location_isnull (bool | Unset):
        storage_location_istartswith (str | Unset):
        storage_location_lt (str | Unset):
        storage_location_lte (str | Unset):
        storage_location_range (list[str] | Unset):
        storage_location_regex (str | Unset):
        storage_location_startswith (str | Unset):
        storage_status (ResultsListStorageStatus | Unset):
        storage_status_contains (str | Unset):
        storage_status_endswith (str | Unset):
        storage_status_gt (str | Unset):
        storage_status_gte (str | Unset):
        storage_status_icontains (str | Unset):
        storage_status_iendswith (str | Unset):
        storage_status_iexact (str | Unset):
        storage_status_in (list[str] | Unset):
        storage_status_iregex (str | Unset):
        storage_status_isnull (bool | Unset):
        storage_status_istartswith (str | Unset):
        storage_status_lt (str | Unset):
        storage_status_lte (str | Unset):
        storage_status_range (list[str] | Unset):
        storage_status_regex (str | Unset):
        storage_status_startswith (str | Unset):
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
        volume (int | Unset):
        volume_contained_by (int | Unset):
        volume_contains (int | Unset):
        volume_endswith (int | Unset):
        volume_gt (int | Unset):
        volume_gte (int | Unset):
        volume_icontains (int | Unset):
        volume_iendswith (int | Unset):
        volume_iexact (int | Unset):
        volume_in (list[int] | Unset):
        volume_iregex (int | Unset):
        volume_isnull (bool | Unset):
        volume_istartswith (int | Unset):
        volume_lt (int | Unset):
        volume_lte (int | Unset):
        volume_range (list[int] | Unset):
        volume_regex (int | Unset):
        volume_startswith (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResultReadList]
    """

    kwargs = _get_kwargs(
        curation_category=curation_category,
        curation_category_contains=curation_category_contains,
        curation_category_endswith=curation_category_endswith,
        curation_category_gt=curation_category_gt,
        curation_category_gte=curation_category_gte,
        curation_category_icontains=curation_category_icontains,
        curation_category_iendswith=curation_category_iendswith,
        curation_category_iexact=curation_category_iexact,
        curation_category_in=curation_category_in,
        curation_category_iregex=curation_category_iregex,
        curation_category_isnull=curation_category_isnull,
        curation_category_istartswith=curation_category_istartswith,
        curation_category_lt=curation_category_lt,
        curation_category_lte=curation_category_lte,
        curation_category_range=curation_category_range,
        curation_category_regex=curation_category_regex,
        curation_category_startswith=curation_category_startswith,
        current_data_path=current_data_path,
        current_data_path_in=current_data_path_in,
        current_data_path_isnull=current_data_path_isnull,
        data_path=data_path,
        data_path_contains=data_path_contains,
        data_path_endswith=data_path_endswith,
        data_path_gt=data_path_gt,
        data_path_gte=data_path_gte,
        data_path_icontains=data_path_icontains,
        data_path_iendswith=data_path_iendswith,
        data_path_iexact=data_path_iexact,
        data_path_in=data_path_in,
        data_path_iregex=data_path_iregex,
        data_path_isnull=data_path_isnull,
        data_path_istartswith=data_path_istartswith,
        data_path_lt=data_path_lt,
        data_path_lte=data_path_lte,
        data_path_range=data_path_range,
        data_path_regex=data_path_regex,
        data_path_startswith=data_path_startswith,
        file_format=file_format,
        file_format_contains=file_format_contains,
        file_format_endswith=file_format_endswith,
        file_format_gt=file_format_gt,
        file_format_gte=file_format_gte,
        file_format_icontains=file_format_icontains,
        file_format_iendswith=file_format_iendswith,
        file_format_iexact=file_format_iexact,
        file_format_in=file_format_in,
        file_format_iregex=file_format_iregex,
        file_format_isnull=file_format_isnull,
        file_format_istartswith=file_format_istartswith,
        file_format_lt=file_format_lt,
        file_format_lte=file_format_lte,
        file_format_range=file_format_range,
        file_format_regex=file_format_regex,
        file_format_startswith=file_format_startswith,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        limit=limit,
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
        number_of_files=number_of_files,
        number_of_files_contained_by=number_of_files_contained_by,
        number_of_files_contains=number_of_files_contains,
        number_of_files_endswith=number_of_files_endswith,
        number_of_files_gt=number_of_files_gt,
        number_of_files_gte=number_of_files_gte,
        number_of_files_icontains=number_of_files_icontains,
        number_of_files_iendswith=number_of_files_iendswith,
        number_of_files_iexact=number_of_files_iexact,
        number_of_files_in=number_of_files_in,
        number_of_files_iregex=number_of_files_iregex,
        number_of_files_isnull=number_of_files_isnull,
        number_of_files_istartswith=number_of_files_istartswith,
        number_of_files_lt=number_of_files_lt,
        number_of_files_lte=number_of_files_lte,
        number_of_files_range=number_of_files_range,
        number_of_files_regex=number_of_files_regex,
        number_of_files_startswith=number_of_files_startswith,
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
        observation_ob_id=observation_ob_id,
        observation_ob_id_in=observation_ob_id_in,
        observation_uuid=observation_uuid,
        observation_uuid_in=observation_uuid_in,
        offset=offset,
        old_data_path=old_data_path,
        old_data_path_in=old_data_path_in,
        old_data_path_isnull=old_data_path_isnull,
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        ordering=ordering,
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
        storage_location=storage_location,
        storage_location_contains=storage_location_contains,
        storage_location_endswith=storage_location_endswith,
        storage_location_gt=storage_location_gt,
        storage_location_gte=storage_location_gte,
        storage_location_icontains=storage_location_icontains,
        storage_location_iendswith=storage_location_iendswith,
        storage_location_iexact=storage_location_iexact,
        storage_location_in=storage_location_in,
        storage_location_iregex=storage_location_iregex,
        storage_location_isnull=storage_location_isnull,
        storage_location_istartswith=storage_location_istartswith,
        storage_location_lt=storage_location_lt,
        storage_location_lte=storage_location_lte,
        storage_location_range=storage_location_range,
        storage_location_regex=storage_location_regex,
        storage_location_startswith=storage_location_startswith,
        storage_status=storage_status,
        storage_status_contains=storage_status_contains,
        storage_status_endswith=storage_status_endswith,
        storage_status_gt=storage_status_gt,
        storage_status_gte=storage_status_gte,
        storage_status_icontains=storage_status_icontains,
        storage_status_iendswith=storage_status_iendswith,
        storage_status_iexact=storage_status_iexact,
        storage_status_in=storage_status_in,
        storage_status_iregex=storage_status_iregex,
        storage_status_isnull=storage_status_isnull,
        storage_status_istartswith=storage_status_istartswith,
        storage_status_lt=storage_status_lt,
        storage_status_lte=storage_status_lte,
        storage_status_range=storage_status_range,
        storage_status_regex=storage_status_regex,
        storage_status_startswith=storage_status_startswith,
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
        volume=volume,
        volume_contained_by=volume_contained_by,
        volume_contains=volume_contains,
        volume_endswith=volume_endswith,
        volume_gt=volume_gt,
        volume_gte=volume_gte,
        volume_icontains=volume_icontains,
        volume_iendswith=volume_iendswith,
        volume_iexact=volume_iexact,
        volume_in=volume_in,
        volume_iregex=volume_iregex,
        volume_isnull=volume_isnull,
        volume_istartswith=volume_istartswith,
        volume_lt=volume_lt,
        volume_lte=volume_lte,
        volume_range=volume_range,
        volume_regex=volume_regex,
        volume_startswith=volume_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    curation_category: ResultsListCEDACurationCategory | Unset = UNSET,
    curation_category_contains: str | Unset = UNSET,
    curation_category_endswith: str | Unset = UNSET,
    curation_category_gt: str | Unset = UNSET,
    curation_category_gte: str | Unset = UNSET,
    curation_category_icontains: str | Unset = UNSET,
    curation_category_iendswith: str | Unset = UNSET,
    curation_category_iexact: str | Unset = UNSET,
    curation_category_in: list[str] | Unset = UNSET,
    curation_category_iregex: str | Unset = UNSET,
    curation_category_isnull: bool | Unset = UNSET,
    curation_category_istartswith: str | Unset = UNSET,
    curation_category_lt: str | Unset = UNSET,
    curation_category_lte: str | Unset = UNSET,
    curation_category_range: list[str] | Unset = UNSET,
    curation_category_regex: str | Unset = UNSET,
    curation_category_startswith: str | Unset = UNSET,
    current_data_path: list[int] | Unset = UNSET,
    current_data_path_in: list[int] | Unset = UNSET,
    current_data_path_isnull: bool | Unset = UNSET,
    data_path: str | Unset = UNSET,
    data_path_contains: str | Unset = UNSET,
    data_path_endswith: str | Unset = UNSET,
    data_path_gt: str | Unset = UNSET,
    data_path_gte: str | Unset = UNSET,
    data_path_icontains: str | Unset = UNSET,
    data_path_iendswith: str | Unset = UNSET,
    data_path_iexact: str | Unset = UNSET,
    data_path_in: list[str] | Unset = UNSET,
    data_path_iregex: str | Unset = UNSET,
    data_path_isnull: bool | Unset = UNSET,
    data_path_istartswith: str | Unset = UNSET,
    data_path_lt: str | Unset = UNSET,
    data_path_lte: str | Unset = UNSET,
    data_path_range: list[str] | Unset = UNSET,
    data_path_regex: str | Unset = UNSET,
    data_path_startswith: str | Unset = UNSET,
    file_format: str | Unset = UNSET,
    file_format_contains: str | Unset = UNSET,
    file_format_endswith: str | Unset = UNSET,
    file_format_gt: str | Unset = UNSET,
    file_format_gte: str | Unset = UNSET,
    file_format_icontains: str | Unset = UNSET,
    file_format_iendswith: str | Unset = UNSET,
    file_format_iexact: str | Unset = UNSET,
    file_format_in: list[str] | Unset = UNSET,
    file_format_iregex: str | Unset = UNSET,
    file_format_isnull: bool | Unset = UNSET,
    file_format_istartswith: str | Unset = UNSET,
    file_format_lt: str | Unset = UNSET,
    file_format_lte: str | Unset = UNSET,
    file_format_range: list[str] | Unset = UNSET,
    file_format_regex: str | Unset = UNSET,
    file_format_startswith: str | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
    number_of_files: int | Unset = UNSET,
    number_of_files_contained_by: int | Unset = UNSET,
    number_of_files_contains: int | Unset = UNSET,
    number_of_files_endswith: int | Unset = UNSET,
    number_of_files_gt: int | Unset = UNSET,
    number_of_files_gte: int | Unset = UNSET,
    number_of_files_icontains: int | Unset = UNSET,
    number_of_files_iendswith: int | Unset = UNSET,
    number_of_files_iexact: int | Unset = UNSET,
    number_of_files_in: list[int] | Unset = UNSET,
    number_of_files_iregex: int | Unset = UNSET,
    number_of_files_isnull: bool | Unset = UNSET,
    number_of_files_istartswith: int | Unset = UNSET,
    number_of_files_lt: int | Unset = UNSET,
    number_of_files_lte: int | Unset = UNSET,
    number_of_files_range: list[int] | Unset = UNSET,
    number_of_files_regex: int | Unset = UNSET,
    number_of_files_startswith: int | Unset = UNSET,
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
    observation_ob_id: int | Unset = UNSET,
    observation_ob_id_in: list[int] | Unset = UNSET,
    observation_uuid: str | Unset = UNSET,
    observation_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    old_data_path: list[int] | Unset = UNSET,
    old_data_path_in: list[int] | Unset = UNSET,
    old_data_path_isnull: bool | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
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
    storage_location: ResultsListStorageLocation | Unset = UNSET,
    storage_location_contains: str | Unset = UNSET,
    storage_location_endswith: str | Unset = UNSET,
    storage_location_gt: str | Unset = UNSET,
    storage_location_gte: str | Unset = UNSET,
    storage_location_icontains: str | Unset = UNSET,
    storage_location_iendswith: str | Unset = UNSET,
    storage_location_iexact: str | Unset = UNSET,
    storage_location_in: list[str] | Unset = UNSET,
    storage_location_iregex: str | Unset = UNSET,
    storage_location_isnull: bool | Unset = UNSET,
    storage_location_istartswith: str | Unset = UNSET,
    storage_location_lt: str | Unset = UNSET,
    storage_location_lte: str | Unset = UNSET,
    storage_location_range: list[str] | Unset = UNSET,
    storage_location_regex: str | Unset = UNSET,
    storage_location_startswith: str | Unset = UNSET,
    storage_status: ResultsListStorageStatus | Unset = UNSET,
    storage_status_contains: str | Unset = UNSET,
    storage_status_endswith: str | Unset = UNSET,
    storage_status_gt: str | Unset = UNSET,
    storage_status_gte: str | Unset = UNSET,
    storage_status_icontains: str | Unset = UNSET,
    storage_status_iendswith: str | Unset = UNSET,
    storage_status_iexact: str | Unset = UNSET,
    storage_status_in: list[str] | Unset = UNSET,
    storage_status_iregex: str | Unset = UNSET,
    storage_status_isnull: bool | Unset = UNSET,
    storage_status_istartswith: str | Unset = UNSET,
    storage_status_lt: str | Unset = UNSET,
    storage_status_lte: str | Unset = UNSET,
    storage_status_range: list[str] | Unset = UNSET,
    storage_status_regex: str | Unset = UNSET,
    storage_status_startswith: str | Unset = UNSET,
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
    volume: int | Unset = UNSET,
    volume_contained_by: int | Unset = UNSET,
    volume_contains: int | Unset = UNSET,
    volume_endswith: int | Unset = UNSET,
    volume_gt: int | Unset = UNSET,
    volume_gte: int | Unset = UNSET,
    volume_icontains: int | Unset = UNSET,
    volume_iendswith: int | Unset = UNSET,
    volume_iexact: int | Unset = UNSET,
    volume_in: list[int] | Unset = UNSET,
    volume_iregex: int | Unset = UNSET,
    volume_isnull: bool | Unset = UNSET,
    volume_istartswith: int | Unset = UNSET,
    volume_lt: int | Unset = UNSET,
    volume_lte: int | Unset = UNSET,
    volume_range: list[int] | Unset = UNSET,
    volume_regex: int | Unset = UNSET,
    volume_startswith: int | Unset = UNSET,
) -> PaginatedResultReadList | None:
    """Get a list of Result objects. Results have a 1:1 mapping with Observations.

    Args:
        curation_category (ResultsListCEDACurationCategory | Unset):
        curation_category_contains (str | Unset):
        curation_category_endswith (str | Unset):
        curation_category_gt (str | Unset):
        curation_category_gte (str | Unset):
        curation_category_icontains (str | Unset):
        curation_category_iendswith (str | Unset):
        curation_category_iexact (str | Unset):
        curation_category_in (list[str] | Unset):
        curation_category_iregex (str | Unset):
        curation_category_isnull (bool | Unset):
        curation_category_istartswith (str | Unset):
        curation_category_lt (str | Unset):
        curation_category_lte (str | Unset):
        curation_category_range (list[str] | Unset):
        curation_category_regex (str | Unset):
        curation_category_startswith (str | Unset):
        current_data_path (list[int] | Unset):
        current_data_path_in (list[int] | Unset):
        current_data_path_isnull (bool | Unset):
        data_path (str | Unset):
        data_path_contains (str | Unset):
        data_path_endswith (str | Unset):
        data_path_gt (str | Unset):
        data_path_gte (str | Unset):
        data_path_icontains (str | Unset):
        data_path_iendswith (str | Unset):
        data_path_iexact (str | Unset):
        data_path_in (list[str] | Unset):
        data_path_iregex (str | Unset):
        data_path_isnull (bool | Unset):
        data_path_istartswith (str | Unset):
        data_path_lt (str | Unset):
        data_path_lte (str | Unset):
        data_path_range (list[str] | Unset):
        data_path_regex (str | Unset):
        data_path_startswith (str | Unset):
        file_format (str | Unset):
        file_format_contains (str | Unset):
        file_format_endswith (str | Unset):
        file_format_gt (str | Unset):
        file_format_gte (str | Unset):
        file_format_icontains (str | Unset):
        file_format_iendswith (str | Unset):
        file_format_iexact (str | Unset):
        file_format_in (list[str] | Unset):
        file_format_iregex (str | Unset):
        file_format_isnull (bool | Unset):
        file_format_istartswith (str | Unset):
        file_format_lt (str | Unset):
        file_format_lte (str | Unset):
        file_format_range (list[str] | Unset):
        file_format_regex (str | Unset):
        file_format_startswith (str | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
        number_of_files (int | Unset):
        number_of_files_contained_by (int | Unset):
        number_of_files_contains (int | Unset):
        number_of_files_endswith (int | Unset):
        number_of_files_gt (int | Unset):
        number_of_files_gte (int | Unset):
        number_of_files_icontains (int | Unset):
        number_of_files_iendswith (int | Unset):
        number_of_files_iexact (int | Unset):
        number_of_files_in (list[int] | Unset):
        number_of_files_iregex (int | Unset):
        number_of_files_isnull (bool | Unset):
        number_of_files_istartswith (int | Unset):
        number_of_files_lt (int | Unset):
        number_of_files_lte (int | Unset):
        number_of_files_range (list[int] | Unset):
        number_of_files_regex (int | Unset):
        number_of_files_startswith (int | Unset):
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
        observation_ob_id (int | Unset):
        observation_ob_id_in (list[int] | Unset):
        observation_uuid (str | Unset):
        observation_uuid_in (list[str] | Unset):
        offset (int | Unset):
        old_data_path (list[int] | Unset):
        old_data_path_in (list[int] | Unset):
        old_data_path_isnull (bool | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
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
        storage_location (ResultsListStorageLocation | Unset):
        storage_location_contains (str | Unset):
        storage_location_endswith (str | Unset):
        storage_location_gt (str | Unset):
        storage_location_gte (str | Unset):
        storage_location_icontains (str | Unset):
        storage_location_iendswith (str | Unset):
        storage_location_iexact (str | Unset):
        storage_location_in (list[str] | Unset):
        storage_location_iregex (str | Unset):
        storage_location_isnull (bool | Unset):
        storage_location_istartswith (str | Unset):
        storage_location_lt (str | Unset):
        storage_location_lte (str | Unset):
        storage_location_range (list[str] | Unset):
        storage_location_regex (str | Unset):
        storage_location_startswith (str | Unset):
        storage_status (ResultsListStorageStatus | Unset):
        storage_status_contains (str | Unset):
        storage_status_endswith (str | Unset):
        storage_status_gt (str | Unset):
        storage_status_gte (str | Unset):
        storage_status_icontains (str | Unset):
        storage_status_iendswith (str | Unset):
        storage_status_iexact (str | Unset):
        storage_status_in (list[str] | Unset):
        storage_status_iregex (str | Unset):
        storage_status_isnull (bool | Unset):
        storage_status_istartswith (str | Unset):
        storage_status_lt (str | Unset):
        storage_status_lte (str | Unset):
        storage_status_range (list[str] | Unset):
        storage_status_regex (str | Unset):
        storage_status_startswith (str | Unset):
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
        volume (int | Unset):
        volume_contained_by (int | Unset):
        volume_contains (int | Unset):
        volume_endswith (int | Unset):
        volume_gt (int | Unset):
        volume_gte (int | Unset):
        volume_icontains (int | Unset):
        volume_iendswith (int | Unset):
        volume_iexact (int | Unset):
        volume_in (list[int] | Unset):
        volume_iregex (int | Unset):
        volume_isnull (bool | Unset):
        volume_istartswith (int | Unset):
        volume_lt (int | Unset):
        volume_lte (int | Unset):
        volume_range (list[int] | Unset):
        volume_regex (int | Unset):
        volume_startswith (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResultReadList
    """

    return sync_detailed(
        client=client,
        curation_category=curation_category,
        curation_category_contains=curation_category_contains,
        curation_category_endswith=curation_category_endswith,
        curation_category_gt=curation_category_gt,
        curation_category_gte=curation_category_gte,
        curation_category_icontains=curation_category_icontains,
        curation_category_iendswith=curation_category_iendswith,
        curation_category_iexact=curation_category_iexact,
        curation_category_in=curation_category_in,
        curation_category_iregex=curation_category_iregex,
        curation_category_isnull=curation_category_isnull,
        curation_category_istartswith=curation_category_istartswith,
        curation_category_lt=curation_category_lt,
        curation_category_lte=curation_category_lte,
        curation_category_range=curation_category_range,
        curation_category_regex=curation_category_regex,
        curation_category_startswith=curation_category_startswith,
        current_data_path=current_data_path,
        current_data_path_in=current_data_path_in,
        current_data_path_isnull=current_data_path_isnull,
        data_path=data_path,
        data_path_contains=data_path_contains,
        data_path_endswith=data_path_endswith,
        data_path_gt=data_path_gt,
        data_path_gte=data_path_gte,
        data_path_icontains=data_path_icontains,
        data_path_iendswith=data_path_iendswith,
        data_path_iexact=data_path_iexact,
        data_path_in=data_path_in,
        data_path_iregex=data_path_iregex,
        data_path_isnull=data_path_isnull,
        data_path_istartswith=data_path_istartswith,
        data_path_lt=data_path_lt,
        data_path_lte=data_path_lte,
        data_path_range=data_path_range,
        data_path_regex=data_path_regex,
        data_path_startswith=data_path_startswith,
        file_format=file_format,
        file_format_contains=file_format_contains,
        file_format_endswith=file_format_endswith,
        file_format_gt=file_format_gt,
        file_format_gte=file_format_gte,
        file_format_icontains=file_format_icontains,
        file_format_iendswith=file_format_iendswith,
        file_format_iexact=file_format_iexact,
        file_format_in=file_format_in,
        file_format_iregex=file_format_iregex,
        file_format_isnull=file_format_isnull,
        file_format_istartswith=file_format_istartswith,
        file_format_lt=file_format_lt,
        file_format_lte=file_format_lte,
        file_format_range=file_format_range,
        file_format_regex=file_format_regex,
        file_format_startswith=file_format_startswith,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        limit=limit,
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
        number_of_files=number_of_files,
        number_of_files_contained_by=number_of_files_contained_by,
        number_of_files_contains=number_of_files_contains,
        number_of_files_endswith=number_of_files_endswith,
        number_of_files_gt=number_of_files_gt,
        number_of_files_gte=number_of_files_gte,
        number_of_files_icontains=number_of_files_icontains,
        number_of_files_iendswith=number_of_files_iendswith,
        number_of_files_iexact=number_of_files_iexact,
        number_of_files_in=number_of_files_in,
        number_of_files_iregex=number_of_files_iregex,
        number_of_files_isnull=number_of_files_isnull,
        number_of_files_istartswith=number_of_files_istartswith,
        number_of_files_lt=number_of_files_lt,
        number_of_files_lte=number_of_files_lte,
        number_of_files_range=number_of_files_range,
        number_of_files_regex=number_of_files_regex,
        number_of_files_startswith=number_of_files_startswith,
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
        observation_ob_id=observation_ob_id,
        observation_ob_id_in=observation_ob_id_in,
        observation_uuid=observation_uuid,
        observation_uuid_in=observation_uuid_in,
        offset=offset,
        old_data_path=old_data_path,
        old_data_path_in=old_data_path_in,
        old_data_path_isnull=old_data_path_isnull,
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        ordering=ordering,
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
        storage_location=storage_location,
        storage_location_contains=storage_location_contains,
        storage_location_endswith=storage_location_endswith,
        storage_location_gt=storage_location_gt,
        storage_location_gte=storage_location_gte,
        storage_location_icontains=storage_location_icontains,
        storage_location_iendswith=storage_location_iendswith,
        storage_location_iexact=storage_location_iexact,
        storage_location_in=storage_location_in,
        storage_location_iregex=storage_location_iregex,
        storage_location_isnull=storage_location_isnull,
        storage_location_istartswith=storage_location_istartswith,
        storage_location_lt=storage_location_lt,
        storage_location_lte=storage_location_lte,
        storage_location_range=storage_location_range,
        storage_location_regex=storage_location_regex,
        storage_location_startswith=storage_location_startswith,
        storage_status=storage_status,
        storage_status_contains=storage_status_contains,
        storage_status_endswith=storage_status_endswith,
        storage_status_gt=storage_status_gt,
        storage_status_gte=storage_status_gte,
        storage_status_icontains=storage_status_icontains,
        storage_status_iendswith=storage_status_iendswith,
        storage_status_iexact=storage_status_iexact,
        storage_status_in=storage_status_in,
        storage_status_iregex=storage_status_iregex,
        storage_status_isnull=storage_status_isnull,
        storage_status_istartswith=storage_status_istartswith,
        storage_status_lt=storage_status_lt,
        storage_status_lte=storage_status_lte,
        storage_status_range=storage_status_range,
        storage_status_regex=storage_status_regex,
        storage_status_startswith=storage_status_startswith,
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
        volume=volume,
        volume_contained_by=volume_contained_by,
        volume_contains=volume_contains,
        volume_endswith=volume_endswith,
        volume_gt=volume_gt,
        volume_gte=volume_gte,
        volume_icontains=volume_icontains,
        volume_iendswith=volume_iendswith,
        volume_iexact=volume_iexact,
        volume_in=volume_in,
        volume_iregex=volume_iregex,
        volume_isnull=volume_isnull,
        volume_istartswith=volume_istartswith,
        volume_lt=volume_lt,
        volume_lte=volume_lte,
        volume_range=volume_range,
        volume_regex=volume_regex,
        volume_startswith=volume_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    curation_category: ResultsListCEDACurationCategory | Unset = UNSET,
    curation_category_contains: str | Unset = UNSET,
    curation_category_endswith: str | Unset = UNSET,
    curation_category_gt: str | Unset = UNSET,
    curation_category_gte: str | Unset = UNSET,
    curation_category_icontains: str | Unset = UNSET,
    curation_category_iendswith: str | Unset = UNSET,
    curation_category_iexact: str | Unset = UNSET,
    curation_category_in: list[str] | Unset = UNSET,
    curation_category_iregex: str | Unset = UNSET,
    curation_category_isnull: bool | Unset = UNSET,
    curation_category_istartswith: str | Unset = UNSET,
    curation_category_lt: str | Unset = UNSET,
    curation_category_lte: str | Unset = UNSET,
    curation_category_range: list[str] | Unset = UNSET,
    curation_category_regex: str | Unset = UNSET,
    curation_category_startswith: str | Unset = UNSET,
    current_data_path: list[int] | Unset = UNSET,
    current_data_path_in: list[int] | Unset = UNSET,
    current_data_path_isnull: bool | Unset = UNSET,
    data_path: str | Unset = UNSET,
    data_path_contains: str | Unset = UNSET,
    data_path_endswith: str | Unset = UNSET,
    data_path_gt: str | Unset = UNSET,
    data_path_gte: str | Unset = UNSET,
    data_path_icontains: str | Unset = UNSET,
    data_path_iendswith: str | Unset = UNSET,
    data_path_iexact: str | Unset = UNSET,
    data_path_in: list[str] | Unset = UNSET,
    data_path_iregex: str | Unset = UNSET,
    data_path_isnull: bool | Unset = UNSET,
    data_path_istartswith: str | Unset = UNSET,
    data_path_lt: str | Unset = UNSET,
    data_path_lte: str | Unset = UNSET,
    data_path_range: list[str] | Unset = UNSET,
    data_path_regex: str | Unset = UNSET,
    data_path_startswith: str | Unset = UNSET,
    file_format: str | Unset = UNSET,
    file_format_contains: str | Unset = UNSET,
    file_format_endswith: str | Unset = UNSET,
    file_format_gt: str | Unset = UNSET,
    file_format_gte: str | Unset = UNSET,
    file_format_icontains: str | Unset = UNSET,
    file_format_iendswith: str | Unset = UNSET,
    file_format_iexact: str | Unset = UNSET,
    file_format_in: list[str] | Unset = UNSET,
    file_format_iregex: str | Unset = UNSET,
    file_format_isnull: bool | Unset = UNSET,
    file_format_istartswith: str | Unset = UNSET,
    file_format_lt: str | Unset = UNSET,
    file_format_lte: str | Unset = UNSET,
    file_format_range: list[str] | Unset = UNSET,
    file_format_regex: str | Unset = UNSET,
    file_format_startswith: str | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
    number_of_files: int | Unset = UNSET,
    number_of_files_contained_by: int | Unset = UNSET,
    number_of_files_contains: int | Unset = UNSET,
    number_of_files_endswith: int | Unset = UNSET,
    number_of_files_gt: int | Unset = UNSET,
    number_of_files_gte: int | Unset = UNSET,
    number_of_files_icontains: int | Unset = UNSET,
    number_of_files_iendswith: int | Unset = UNSET,
    number_of_files_iexact: int | Unset = UNSET,
    number_of_files_in: list[int] | Unset = UNSET,
    number_of_files_iregex: int | Unset = UNSET,
    number_of_files_isnull: bool | Unset = UNSET,
    number_of_files_istartswith: int | Unset = UNSET,
    number_of_files_lt: int | Unset = UNSET,
    number_of_files_lte: int | Unset = UNSET,
    number_of_files_range: list[int] | Unset = UNSET,
    number_of_files_regex: int | Unset = UNSET,
    number_of_files_startswith: int | Unset = UNSET,
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
    observation_ob_id: int | Unset = UNSET,
    observation_ob_id_in: list[int] | Unset = UNSET,
    observation_uuid: str | Unset = UNSET,
    observation_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    old_data_path: list[int] | Unset = UNSET,
    old_data_path_in: list[int] | Unset = UNSET,
    old_data_path_isnull: bool | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
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
    storage_location: ResultsListStorageLocation | Unset = UNSET,
    storage_location_contains: str | Unset = UNSET,
    storage_location_endswith: str | Unset = UNSET,
    storage_location_gt: str | Unset = UNSET,
    storage_location_gte: str | Unset = UNSET,
    storage_location_icontains: str | Unset = UNSET,
    storage_location_iendswith: str | Unset = UNSET,
    storage_location_iexact: str | Unset = UNSET,
    storage_location_in: list[str] | Unset = UNSET,
    storage_location_iregex: str | Unset = UNSET,
    storage_location_isnull: bool | Unset = UNSET,
    storage_location_istartswith: str | Unset = UNSET,
    storage_location_lt: str | Unset = UNSET,
    storage_location_lte: str | Unset = UNSET,
    storage_location_range: list[str] | Unset = UNSET,
    storage_location_regex: str | Unset = UNSET,
    storage_location_startswith: str | Unset = UNSET,
    storage_status: ResultsListStorageStatus | Unset = UNSET,
    storage_status_contains: str | Unset = UNSET,
    storage_status_endswith: str | Unset = UNSET,
    storage_status_gt: str | Unset = UNSET,
    storage_status_gte: str | Unset = UNSET,
    storage_status_icontains: str | Unset = UNSET,
    storage_status_iendswith: str | Unset = UNSET,
    storage_status_iexact: str | Unset = UNSET,
    storage_status_in: list[str] | Unset = UNSET,
    storage_status_iregex: str | Unset = UNSET,
    storage_status_isnull: bool | Unset = UNSET,
    storage_status_istartswith: str | Unset = UNSET,
    storage_status_lt: str | Unset = UNSET,
    storage_status_lte: str | Unset = UNSET,
    storage_status_range: list[str] | Unset = UNSET,
    storage_status_regex: str | Unset = UNSET,
    storage_status_startswith: str | Unset = UNSET,
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
    volume: int | Unset = UNSET,
    volume_contained_by: int | Unset = UNSET,
    volume_contains: int | Unset = UNSET,
    volume_endswith: int | Unset = UNSET,
    volume_gt: int | Unset = UNSET,
    volume_gte: int | Unset = UNSET,
    volume_icontains: int | Unset = UNSET,
    volume_iendswith: int | Unset = UNSET,
    volume_iexact: int | Unset = UNSET,
    volume_in: list[int] | Unset = UNSET,
    volume_iregex: int | Unset = UNSET,
    volume_isnull: bool | Unset = UNSET,
    volume_istartswith: int | Unset = UNSET,
    volume_lt: int | Unset = UNSET,
    volume_lte: int | Unset = UNSET,
    volume_range: list[int] | Unset = UNSET,
    volume_regex: int | Unset = UNSET,
    volume_startswith: int | Unset = UNSET,
) -> Response[PaginatedResultReadList]:
    """Get a list of Result objects. Results have a 1:1 mapping with Observations.

    Args:
        curation_category (ResultsListCEDACurationCategory | Unset):
        curation_category_contains (str | Unset):
        curation_category_endswith (str | Unset):
        curation_category_gt (str | Unset):
        curation_category_gte (str | Unset):
        curation_category_icontains (str | Unset):
        curation_category_iendswith (str | Unset):
        curation_category_iexact (str | Unset):
        curation_category_in (list[str] | Unset):
        curation_category_iregex (str | Unset):
        curation_category_isnull (bool | Unset):
        curation_category_istartswith (str | Unset):
        curation_category_lt (str | Unset):
        curation_category_lte (str | Unset):
        curation_category_range (list[str] | Unset):
        curation_category_regex (str | Unset):
        curation_category_startswith (str | Unset):
        current_data_path (list[int] | Unset):
        current_data_path_in (list[int] | Unset):
        current_data_path_isnull (bool | Unset):
        data_path (str | Unset):
        data_path_contains (str | Unset):
        data_path_endswith (str | Unset):
        data_path_gt (str | Unset):
        data_path_gte (str | Unset):
        data_path_icontains (str | Unset):
        data_path_iendswith (str | Unset):
        data_path_iexact (str | Unset):
        data_path_in (list[str] | Unset):
        data_path_iregex (str | Unset):
        data_path_isnull (bool | Unset):
        data_path_istartswith (str | Unset):
        data_path_lt (str | Unset):
        data_path_lte (str | Unset):
        data_path_range (list[str] | Unset):
        data_path_regex (str | Unset):
        data_path_startswith (str | Unset):
        file_format (str | Unset):
        file_format_contains (str | Unset):
        file_format_endswith (str | Unset):
        file_format_gt (str | Unset):
        file_format_gte (str | Unset):
        file_format_icontains (str | Unset):
        file_format_iendswith (str | Unset):
        file_format_iexact (str | Unset):
        file_format_in (list[str] | Unset):
        file_format_iregex (str | Unset):
        file_format_isnull (bool | Unset):
        file_format_istartswith (str | Unset):
        file_format_lt (str | Unset):
        file_format_lte (str | Unset):
        file_format_range (list[str] | Unset):
        file_format_regex (str | Unset):
        file_format_startswith (str | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
        number_of_files (int | Unset):
        number_of_files_contained_by (int | Unset):
        number_of_files_contains (int | Unset):
        number_of_files_endswith (int | Unset):
        number_of_files_gt (int | Unset):
        number_of_files_gte (int | Unset):
        number_of_files_icontains (int | Unset):
        number_of_files_iendswith (int | Unset):
        number_of_files_iexact (int | Unset):
        number_of_files_in (list[int] | Unset):
        number_of_files_iregex (int | Unset):
        number_of_files_isnull (bool | Unset):
        number_of_files_istartswith (int | Unset):
        number_of_files_lt (int | Unset):
        number_of_files_lte (int | Unset):
        number_of_files_range (list[int] | Unset):
        number_of_files_regex (int | Unset):
        number_of_files_startswith (int | Unset):
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
        observation_ob_id (int | Unset):
        observation_ob_id_in (list[int] | Unset):
        observation_uuid (str | Unset):
        observation_uuid_in (list[str] | Unset):
        offset (int | Unset):
        old_data_path (list[int] | Unset):
        old_data_path_in (list[int] | Unset):
        old_data_path_isnull (bool | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
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
        storage_location (ResultsListStorageLocation | Unset):
        storage_location_contains (str | Unset):
        storage_location_endswith (str | Unset):
        storage_location_gt (str | Unset):
        storage_location_gte (str | Unset):
        storage_location_icontains (str | Unset):
        storage_location_iendswith (str | Unset):
        storage_location_iexact (str | Unset):
        storage_location_in (list[str] | Unset):
        storage_location_iregex (str | Unset):
        storage_location_isnull (bool | Unset):
        storage_location_istartswith (str | Unset):
        storage_location_lt (str | Unset):
        storage_location_lte (str | Unset):
        storage_location_range (list[str] | Unset):
        storage_location_regex (str | Unset):
        storage_location_startswith (str | Unset):
        storage_status (ResultsListStorageStatus | Unset):
        storage_status_contains (str | Unset):
        storage_status_endswith (str | Unset):
        storage_status_gt (str | Unset):
        storage_status_gte (str | Unset):
        storage_status_icontains (str | Unset):
        storage_status_iendswith (str | Unset):
        storage_status_iexact (str | Unset):
        storage_status_in (list[str] | Unset):
        storage_status_iregex (str | Unset):
        storage_status_isnull (bool | Unset):
        storage_status_istartswith (str | Unset):
        storage_status_lt (str | Unset):
        storage_status_lte (str | Unset):
        storage_status_range (list[str] | Unset):
        storage_status_regex (str | Unset):
        storage_status_startswith (str | Unset):
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
        volume (int | Unset):
        volume_contained_by (int | Unset):
        volume_contains (int | Unset):
        volume_endswith (int | Unset):
        volume_gt (int | Unset):
        volume_gte (int | Unset):
        volume_icontains (int | Unset):
        volume_iendswith (int | Unset):
        volume_iexact (int | Unset):
        volume_in (list[int] | Unset):
        volume_iregex (int | Unset):
        volume_isnull (bool | Unset):
        volume_istartswith (int | Unset):
        volume_lt (int | Unset):
        volume_lte (int | Unset):
        volume_range (list[int] | Unset):
        volume_regex (int | Unset):
        volume_startswith (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResultReadList]
    """

    kwargs = _get_kwargs(
        curation_category=curation_category,
        curation_category_contains=curation_category_contains,
        curation_category_endswith=curation_category_endswith,
        curation_category_gt=curation_category_gt,
        curation_category_gte=curation_category_gte,
        curation_category_icontains=curation_category_icontains,
        curation_category_iendswith=curation_category_iendswith,
        curation_category_iexact=curation_category_iexact,
        curation_category_in=curation_category_in,
        curation_category_iregex=curation_category_iregex,
        curation_category_isnull=curation_category_isnull,
        curation_category_istartswith=curation_category_istartswith,
        curation_category_lt=curation_category_lt,
        curation_category_lte=curation_category_lte,
        curation_category_range=curation_category_range,
        curation_category_regex=curation_category_regex,
        curation_category_startswith=curation_category_startswith,
        current_data_path=current_data_path,
        current_data_path_in=current_data_path_in,
        current_data_path_isnull=current_data_path_isnull,
        data_path=data_path,
        data_path_contains=data_path_contains,
        data_path_endswith=data_path_endswith,
        data_path_gt=data_path_gt,
        data_path_gte=data_path_gte,
        data_path_icontains=data_path_icontains,
        data_path_iendswith=data_path_iendswith,
        data_path_iexact=data_path_iexact,
        data_path_in=data_path_in,
        data_path_iregex=data_path_iregex,
        data_path_isnull=data_path_isnull,
        data_path_istartswith=data_path_istartswith,
        data_path_lt=data_path_lt,
        data_path_lte=data_path_lte,
        data_path_range=data_path_range,
        data_path_regex=data_path_regex,
        data_path_startswith=data_path_startswith,
        file_format=file_format,
        file_format_contains=file_format_contains,
        file_format_endswith=file_format_endswith,
        file_format_gt=file_format_gt,
        file_format_gte=file_format_gte,
        file_format_icontains=file_format_icontains,
        file_format_iendswith=file_format_iendswith,
        file_format_iexact=file_format_iexact,
        file_format_in=file_format_in,
        file_format_iregex=file_format_iregex,
        file_format_isnull=file_format_isnull,
        file_format_istartswith=file_format_istartswith,
        file_format_lt=file_format_lt,
        file_format_lte=file_format_lte,
        file_format_range=file_format_range,
        file_format_regex=file_format_regex,
        file_format_startswith=file_format_startswith,
        identifier=identifier,
        identifier_in=identifier_in,
        identifier_isnull=identifier_isnull,
        limit=limit,
        migrationproperty=migrationproperty,
        migrationproperty_in=migrationproperty_in,
        migrationproperty_isnull=migrationproperty_isnull,
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
        number_of_files=number_of_files,
        number_of_files_contained_by=number_of_files_contained_by,
        number_of_files_contains=number_of_files_contains,
        number_of_files_endswith=number_of_files_endswith,
        number_of_files_gt=number_of_files_gt,
        number_of_files_gte=number_of_files_gte,
        number_of_files_icontains=number_of_files_icontains,
        number_of_files_iendswith=number_of_files_iendswith,
        number_of_files_iexact=number_of_files_iexact,
        number_of_files_in=number_of_files_in,
        number_of_files_iregex=number_of_files_iregex,
        number_of_files_isnull=number_of_files_isnull,
        number_of_files_istartswith=number_of_files_istartswith,
        number_of_files_lt=number_of_files_lt,
        number_of_files_lte=number_of_files_lte,
        number_of_files_range=number_of_files_range,
        number_of_files_regex=number_of_files_regex,
        number_of_files_startswith=number_of_files_startswith,
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
        observation_ob_id=observation_ob_id,
        observation_ob_id_in=observation_ob_id_in,
        observation_uuid=observation_uuid,
        observation_uuid_in=observation_uuid_in,
        offset=offset,
        old_data_path=old_data_path,
        old_data_path_in=old_data_path_in,
        old_data_path_isnull=old_data_path_isnull,
        onlineresource=onlineresource,
        onlineresource_in=onlineresource_in,
        onlineresource_isnull=onlineresource_isnull,
        ordering=ordering,
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
        storage_location=storage_location,
        storage_location_contains=storage_location_contains,
        storage_location_endswith=storage_location_endswith,
        storage_location_gt=storage_location_gt,
        storage_location_gte=storage_location_gte,
        storage_location_icontains=storage_location_icontains,
        storage_location_iendswith=storage_location_iendswith,
        storage_location_iexact=storage_location_iexact,
        storage_location_in=storage_location_in,
        storage_location_iregex=storage_location_iregex,
        storage_location_isnull=storage_location_isnull,
        storage_location_istartswith=storage_location_istartswith,
        storage_location_lt=storage_location_lt,
        storage_location_lte=storage_location_lte,
        storage_location_range=storage_location_range,
        storage_location_regex=storage_location_regex,
        storage_location_startswith=storage_location_startswith,
        storage_status=storage_status,
        storage_status_contains=storage_status_contains,
        storage_status_endswith=storage_status_endswith,
        storage_status_gt=storage_status_gt,
        storage_status_gte=storage_status_gte,
        storage_status_icontains=storage_status_icontains,
        storage_status_iendswith=storage_status_iendswith,
        storage_status_iexact=storage_status_iexact,
        storage_status_in=storage_status_in,
        storage_status_iregex=storage_status_iregex,
        storage_status_isnull=storage_status_isnull,
        storage_status_istartswith=storage_status_istartswith,
        storage_status_lt=storage_status_lt,
        storage_status_lte=storage_status_lte,
        storage_status_range=storage_status_range,
        storage_status_regex=storage_status_regex,
        storage_status_startswith=storage_status_startswith,
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
        volume=volume,
        volume_contained_by=volume_contained_by,
        volume_contains=volume_contains,
        volume_endswith=volume_endswith,
        volume_gt=volume_gt,
        volume_gte=volume_gte,
        volume_icontains=volume_icontains,
        volume_iendswith=volume_iendswith,
        volume_iexact=volume_iexact,
        volume_in=volume_in,
        volume_iregex=volume_iregex,
        volume_isnull=volume_isnull,
        volume_istartswith=volume_istartswith,
        volume_lt=volume_lt,
        volume_lte=volume_lte,
        volume_range=volume_range,
        volume_regex=volume_regex,
        volume_startswith=volume_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    curation_category: ResultsListCEDACurationCategory | Unset = UNSET,
    curation_category_contains: str | Unset = UNSET,
    curation_category_endswith: str | Unset = UNSET,
    curation_category_gt: str | Unset = UNSET,
    curation_category_gte: str | Unset = UNSET,
    curation_category_icontains: str | Unset = UNSET,
    curation_category_iendswith: str | Unset = UNSET,
    curation_category_iexact: str | Unset = UNSET,
    curation_category_in: list[str] | Unset = UNSET,
    curation_category_iregex: str | Unset = UNSET,
    curation_category_isnull: bool | Unset = UNSET,
    curation_category_istartswith: str | Unset = UNSET,
    curation_category_lt: str | Unset = UNSET,
    curation_category_lte: str | Unset = UNSET,
    curation_category_range: list[str] | Unset = UNSET,
    curation_category_regex: str | Unset = UNSET,
    curation_category_startswith: str | Unset = UNSET,
    current_data_path: list[int] | Unset = UNSET,
    current_data_path_in: list[int] | Unset = UNSET,
    current_data_path_isnull: bool | Unset = UNSET,
    data_path: str | Unset = UNSET,
    data_path_contains: str | Unset = UNSET,
    data_path_endswith: str | Unset = UNSET,
    data_path_gt: str | Unset = UNSET,
    data_path_gte: str | Unset = UNSET,
    data_path_icontains: str | Unset = UNSET,
    data_path_iendswith: str | Unset = UNSET,
    data_path_iexact: str | Unset = UNSET,
    data_path_in: list[str] | Unset = UNSET,
    data_path_iregex: str | Unset = UNSET,
    data_path_isnull: bool | Unset = UNSET,
    data_path_istartswith: str | Unset = UNSET,
    data_path_lt: str | Unset = UNSET,
    data_path_lte: str | Unset = UNSET,
    data_path_range: list[str] | Unset = UNSET,
    data_path_regex: str | Unset = UNSET,
    data_path_startswith: str | Unset = UNSET,
    file_format: str | Unset = UNSET,
    file_format_contains: str | Unset = UNSET,
    file_format_endswith: str | Unset = UNSET,
    file_format_gt: str | Unset = UNSET,
    file_format_gte: str | Unset = UNSET,
    file_format_icontains: str | Unset = UNSET,
    file_format_iendswith: str | Unset = UNSET,
    file_format_iexact: str | Unset = UNSET,
    file_format_in: list[str] | Unset = UNSET,
    file_format_iregex: str | Unset = UNSET,
    file_format_isnull: bool | Unset = UNSET,
    file_format_istartswith: str | Unset = UNSET,
    file_format_lt: str | Unset = UNSET,
    file_format_lte: str | Unset = UNSET,
    file_format_range: list[str] | Unset = UNSET,
    file_format_regex: str | Unset = UNSET,
    file_format_startswith: str | Unset = UNSET,
    identifier: list[int] | Unset = UNSET,
    identifier_in: list[int] | Unset = UNSET,
    identifier_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    migrationproperty: list[int] | Unset = UNSET,
    migrationproperty_in: list[int] | Unset = UNSET,
    migrationproperty_isnull: bool | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
    number_of_files: int | Unset = UNSET,
    number_of_files_contained_by: int | Unset = UNSET,
    number_of_files_contains: int | Unset = UNSET,
    number_of_files_endswith: int | Unset = UNSET,
    number_of_files_gt: int | Unset = UNSET,
    number_of_files_gte: int | Unset = UNSET,
    number_of_files_icontains: int | Unset = UNSET,
    number_of_files_iendswith: int | Unset = UNSET,
    number_of_files_iexact: int | Unset = UNSET,
    number_of_files_in: list[int] | Unset = UNSET,
    number_of_files_iregex: int | Unset = UNSET,
    number_of_files_isnull: bool | Unset = UNSET,
    number_of_files_istartswith: int | Unset = UNSET,
    number_of_files_lt: int | Unset = UNSET,
    number_of_files_lte: int | Unset = UNSET,
    number_of_files_range: list[int] | Unset = UNSET,
    number_of_files_regex: int | Unset = UNSET,
    number_of_files_startswith: int | Unset = UNSET,
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
    observation_ob_id: int | Unset = UNSET,
    observation_ob_id_in: list[int] | Unset = UNSET,
    observation_uuid: str | Unset = UNSET,
    observation_uuid_in: list[str] | Unset = UNSET,
    offset: int | Unset = UNSET,
    old_data_path: list[int] | Unset = UNSET,
    old_data_path_in: list[int] | Unset = UNSET,
    old_data_path_isnull: bool | Unset = UNSET,
    onlineresource: list[int] | Unset = UNSET,
    onlineresource_in: list[int] | Unset = UNSET,
    onlineresource_isnull: bool | Unset = UNSET,
    ordering: str | Unset = UNSET,
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
    storage_location: ResultsListStorageLocation | Unset = UNSET,
    storage_location_contains: str | Unset = UNSET,
    storage_location_endswith: str | Unset = UNSET,
    storage_location_gt: str | Unset = UNSET,
    storage_location_gte: str | Unset = UNSET,
    storage_location_icontains: str | Unset = UNSET,
    storage_location_iendswith: str | Unset = UNSET,
    storage_location_iexact: str | Unset = UNSET,
    storage_location_in: list[str] | Unset = UNSET,
    storage_location_iregex: str | Unset = UNSET,
    storage_location_isnull: bool | Unset = UNSET,
    storage_location_istartswith: str | Unset = UNSET,
    storage_location_lt: str | Unset = UNSET,
    storage_location_lte: str | Unset = UNSET,
    storage_location_range: list[str] | Unset = UNSET,
    storage_location_regex: str | Unset = UNSET,
    storage_location_startswith: str | Unset = UNSET,
    storage_status: ResultsListStorageStatus | Unset = UNSET,
    storage_status_contains: str | Unset = UNSET,
    storage_status_endswith: str | Unset = UNSET,
    storage_status_gt: str | Unset = UNSET,
    storage_status_gte: str | Unset = UNSET,
    storage_status_icontains: str | Unset = UNSET,
    storage_status_iendswith: str | Unset = UNSET,
    storage_status_iexact: str | Unset = UNSET,
    storage_status_in: list[str] | Unset = UNSET,
    storage_status_iregex: str | Unset = UNSET,
    storage_status_isnull: bool | Unset = UNSET,
    storage_status_istartswith: str | Unset = UNSET,
    storage_status_lt: str | Unset = UNSET,
    storage_status_lte: str | Unset = UNSET,
    storage_status_range: list[str] | Unset = UNSET,
    storage_status_regex: str | Unset = UNSET,
    storage_status_startswith: str | Unset = UNSET,
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
    volume: int | Unset = UNSET,
    volume_contained_by: int | Unset = UNSET,
    volume_contains: int | Unset = UNSET,
    volume_endswith: int | Unset = UNSET,
    volume_gt: int | Unset = UNSET,
    volume_gte: int | Unset = UNSET,
    volume_icontains: int | Unset = UNSET,
    volume_iendswith: int | Unset = UNSET,
    volume_iexact: int | Unset = UNSET,
    volume_in: list[int] | Unset = UNSET,
    volume_iregex: int | Unset = UNSET,
    volume_isnull: bool | Unset = UNSET,
    volume_istartswith: int | Unset = UNSET,
    volume_lt: int | Unset = UNSET,
    volume_lte: int | Unset = UNSET,
    volume_range: list[int] | Unset = UNSET,
    volume_regex: int | Unset = UNSET,
    volume_startswith: int | Unset = UNSET,
) -> PaginatedResultReadList | None:
    """Get a list of Result objects. Results have a 1:1 mapping with Observations.

    Args:
        curation_category (ResultsListCEDACurationCategory | Unset):
        curation_category_contains (str | Unset):
        curation_category_endswith (str | Unset):
        curation_category_gt (str | Unset):
        curation_category_gte (str | Unset):
        curation_category_icontains (str | Unset):
        curation_category_iendswith (str | Unset):
        curation_category_iexact (str | Unset):
        curation_category_in (list[str] | Unset):
        curation_category_iregex (str | Unset):
        curation_category_isnull (bool | Unset):
        curation_category_istartswith (str | Unset):
        curation_category_lt (str | Unset):
        curation_category_lte (str | Unset):
        curation_category_range (list[str] | Unset):
        curation_category_regex (str | Unset):
        curation_category_startswith (str | Unset):
        current_data_path (list[int] | Unset):
        current_data_path_in (list[int] | Unset):
        current_data_path_isnull (bool | Unset):
        data_path (str | Unset):
        data_path_contains (str | Unset):
        data_path_endswith (str | Unset):
        data_path_gt (str | Unset):
        data_path_gte (str | Unset):
        data_path_icontains (str | Unset):
        data_path_iendswith (str | Unset):
        data_path_iexact (str | Unset):
        data_path_in (list[str] | Unset):
        data_path_iregex (str | Unset):
        data_path_isnull (bool | Unset):
        data_path_istartswith (str | Unset):
        data_path_lt (str | Unset):
        data_path_lte (str | Unset):
        data_path_range (list[str] | Unset):
        data_path_regex (str | Unset):
        data_path_startswith (str | Unset):
        file_format (str | Unset):
        file_format_contains (str | Unset):
        file_format_endswith (str | Unset):
        file_format_gt (str | Unset):
        file_format_gte (str | Unset):
        file_format_icontains (str | Unset):
        file_format_iendswith (str | Unset):
        file_format_iexact (str | Unset):
        file_format_in (list[str] | Unset):
        file_format_iregex (str | Unset):
        file_format_isnull (bool | Unset):
        file_format_istartswith (str | Unset):
        file_format_lt (str | Unset):
        file_format_lte (str | Unset):
        file_format_range (list[str] | Unset):
        file_format_regex (str | Unset):
        file_format_startswith (str | Unset):
        identifier (list[int] | Unset):
        identifier_in (list[int] | Unset):
        identifier_isnull (bool | Unset):
        limit (int | Unset):
        migrationproperty (list[int] | Unset):
        migrationproperty_in (list[int] | Unset):
        migrationproperty_isnull (bool | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
        number_of_files (int | Unset):
        number_of_files_contained_by (int | Unset):
        number_of_files_contains (int | Unset):
        number_of_files_endswith (int | Unset):
        number_of_files_gt (int | Unset):
        number_of_files_gte (int | Unset):
        number_of_files_icontains (int | Unset):
        number_of_files_iendswith (int | Unset):
        number_of_files_iexact (int | Unset):
        number_of_files_in (list[int] | Unset):
        number_of_files_iregex (int | Unset):
        number_of_files_isnull (bool | Unset):
        number_of_files_istartswith (int | Unset):
        number_of_files_lt (int | Unset):
        number_of_files_lte (int | Unset):
        number_of_files_range (list[int] | Unset):
        number_of_files_regex (int | Unset):
        number_of_files_startswith (int | Unset):
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
        observation_ob_id (int | Unset):
        observation_ob_id_in (list[int] | Unset):
        observation_uuid (str | Unset):
        observation_uuid_in (list[str] | Unset):
        offset (int | Unset):
        old_data_path (list[int] | Unset):
        old_data_path_in (list[int] | Unset):
        old_data_path_isnull (bool | Unset):
        onlineresource (list[int] | Unset):
        onlineresource_in (list[int] | Unset):
        onlineresource_isnull (bool | Unset):
        ordering (str | Unset):
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
        storage_location (ResultsListStorageLocation | Unset):
        storage_location_contains (str | Unset):
        storage_location_endswith (str | Unset):
        storage_location_gt (str | Unset):
        storage_location_gte (str | Unset):
        storage_location_icontains (str | Unset):
        storage_location_iendswith (str | Unset):
        storage_location_iexact (str | Unset):
        storage_location_in (list[str] | Unset):
        storage_location_iregex (str | Unset):
        storage_location_isnull (bool | Unset):
        storage_location_istartswith (str | Unset):
        storage_location_lt (str | Unset):
        storage_location_lte (str | Unset):
        storage_location_range (list[str] | Unset):
        storage_location_regex (str | Unset):
        storage_location_startswith (str | Unset):
        storage_status (ResultsListStorageStatus | Unset):
        storage_status_contains (str | Unset):
        storage_status_endswith (str | Unset):
        storage_status_gt (str | Unset):
        storage_status_gte (str | Unset):
        storage_status_icontains (str | Unset):
        storage_status_iendswith (str | Unset):
        storage_status_iexact (str | Unset):
        storage_status_in (list[str] | Unset):
        storage_status_iregex (str | Unset):
        storage_status_isnull (bool | Unset):
        storage_status_istartswith (str | Unset):
        storage_status_lt (str | Unset):
        storage_status_lte (str | Unset):
        storage_status_range (list[str] | Unset):
        storage_status_regex (str | Unset):
        storage_status_startswith (str | Unset):
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
        volume (int | Unset):
        volume_contained_by (int | Unset):
        volume_contains (int | Unset):
        volume_endswith (int | Unset):
        volume_gt (int | Unset):
        volume_gte (int | Unset):
        volume_icontains (int | Unset):
        volume_iendswith (int | Unset):
        volume_iexact (int | Unset):
        volume_in (list[int] | Unset):
        volume_iregex (int | Unset):
        volume_isnull (bool | Unset):
        volume_istartswith (int | Unset):
        volume_lt (int | Unset):
        volume_lte (int | Unset):
        volume_range (list[int] | Unset):
        volume_regex (int | Unset):
        volume_startswith (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResultReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            curation_category=curation_category,
            curation_category_contains=curation_category_contains,
            curation_category_endswith=curation_category_endswith,
            curation_category_gt=curation_category_gt,
            curation_category_gte=curation_category_gte,
            curation_category_icontains=curation_category_icontains,
            curation_category_iendswith=curation_category_iendswith,
            curation_category_iexact=curation_category_iexact,
            curation_category_in=curation_category_in,
            curation_category_iregex=curation_category_iregex,
            curation_category_isnull=curation_category_isnull,
            curation_category_istartswith=curation_category_istartswith,
            curation_category_lt=curation_category_lt,
            curation_category_lte=curation_category_lte,
            curation_category_range=curation_category_range,
            curation_category_regex=curation_category_regex,
            curation_category_startswith=curation_category_startswith,
            current_data_path=current_data_path,
            current_data_path_in=current_data_path_in,
            current_data_path_isnull=current_data_path_isnull,
            data_path=data_path,
            data_path_contains=data_path_contains,
            data_path_endswith=data_path_endswith,
            data_path_gt=data_path_gt,
            data_path_gte=data_path_gte,
            data_path_icontains=data_path_icontains,
            data_path_iendswith=data_path_iendswith,
            data_path_iexact=data_path_iexact,
            data_path_in=data_path_in,
            data_path_iregex=data_path_iregex,
            data_path_isnull=data_path_isnull,
            data_path_istartswith=data_path_istartswith,
            data_path_lt=data_path_lt,
            data_path_lte=data_path_lte,
            data_path_range=data_path_range,
            data_path_regex=data_path_regex,
            data_path_startswith=data_path_startswith,
            file_format=file_format,
            file_format_contains=file_format_contains,
            file_format_endswith=file_format_endswith,
            file_format_gt=file_format_gt,
            file_format_gte=file_format_gte,
            file_format_icontains=file_format_icontains,
            file_format_iendswith=file_format_iendswith,
            file_format_iexact=file_format_iexact,
            file_format_in=file_format_in,
            file_format_iregex=file_format_iregex,
            file_format_isnull=file_format_isnull,
            file_format_istartswith=file_format_istartswith,
            file_format_lt=file_format_lt,
            file_format_lte=file_format_lte,
            file_format_range=file_format_range,
            file_format_regex=file_format_regex,
            file_format_startswith=file_format_startswith,
            identifier=identifier,
            identifier_in=identifier_in,
            identifier_isnull=identifier_isnull,
            limit=limit,
            migrationproperty=migrationproperty,
            migrationproperty_in=migrationproperty_in,
            migrationproperty_isnull=migrationproperty_isnull,
            note=note,
            note_in=note_in,
            note_isnull=note_isnull,
            number_of_files=number_of_files,
            number_of_files_contained_by=number_of_files_contained_by,
            number_of_files_contains=number_of_files_contains,
            number_of_files_endswith=number_of_files_endswith,
            number_of_files_gt=number_of_files_gt,
            number_of_files_gte=number_of_files_gte,
            number_of_files_icontains=number_of_files_icontains,
            number_of_files_iendswith=number_of_files_iendswith,
            number_of_files_iexact=number_of_files_iexact,
            number_of_files_in=number_of_files_in,
            number_of_files_iregex=number_of_files_iregex,
            number_of_files_isnull=number_of_files_isnull,
            number_of_files_istartswith=number_of_files_istartswith,
            number_of_files_lt=number_of_files_lt,
            number_of_files_lte=number_of_files_lte,
            number_of_files_range=number_of_files_range,
            number_of_files_regex=number_of_files_regex,
            number_of_files_startswith=number_of_files_startswith,
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
            observation_ob_id=observation_ob_id,
            observation_ob_id_in=observation_ob_id_in,
            observation_uuid=observation_uuid,
            observation_uuid_in=observation_uuid_in,
            offset=offset,
            old_data_path=old_data_path,
            old_data_path_in=old_data_path_in,
            old_data_path_isnull=old_data_path_isnull,
            onlineresource=onlineresource,
            onlineresource_in=onlineresource_in,
            onlineresource_isnull=onlineresource_isnull,
            ordering=ordering,
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
            storage_location=storage_location,
            storage_location_contains=storage_location_contains,
            storage_location_endswith=storage_location_endswith,
            storage_location_gt=storage_location_gt,
            storage_location_gte=storage_location_gte,
            storage_location_icontains=storage_location_icontains,
            storage_location_iendswith=storage_location_iendswith,
            storage_location_iexact=storage_location_iexact,
            storage_location_in=storage_location_in,
            storage_location_iregex=storage_location_iregex,
            storage_location_isnull=storage_location_isnull,
            storage_location_istartswith=storage_location_istartswith,
            storage_location_lt=storage_location_lt,
            storage_location_lte=storage_location_lte,
            storage_location_range=storage_location_range,
            storage_location_regex=storage_location_regex,
            storage_location_startswith=storage_location_startswith,
            storage_status=storage_status,
            storage_status_contains=storage_status_contains,
            storage_status_endswith=storage_status_endswith,
            storage_status_gt=storage_status_gt,
            storage_status_gte=storage_status_gte,
            storage_status_icontains=storage_status_icontains,
            storage_status_iendswith=storage_status_iendswith,
            storage_status_iexact=storage_status_iexact,
            storage_status_in=storage_status_in,
            storage_status_iregex=storage_status_iregex,
            storage_status_isnull=storage_status_isnull,
            storage_status_istartswith=storage_status_istartswith,
            storage_status_lt=storage_status_lt,
            storage_status_lte=storage_status_lte,
            storage_status_range=storage_status_range,
            storage_status_regex=storage_status_regex,
            storage_status_startswith=storage_status_startswith,
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
            volume=volume,
            volume_contained_by=volume_contained_by,
            volume_contains=volume_contains,
            volume_endswith=volume_endswith,
            volume_gt=volume_gt,
            volume_gte=volume_gte,
            volume_icontains=volume_icontains,
            volume_iendswith=volume_iendswith,
            volume_iexact=volume_iexact,
            volume_in=volume_in,
            volume_iregex=volume_iregex,
            volume_isnull=volume_isnull,
            volume_istartswith=volume_istartswith,
            volume_lt=volume_lt,
            volume_lte=volume_lte,
            volume_range=volume_range,
            volume_regex=volume_regex,
            volume_startswith=volume_startswith,
        )
    ).parsed
