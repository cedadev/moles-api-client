from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_result_write_list import PaginatedResultWriteList
from ...models.results_list_ceda_curation_category import ResultsListCEDACurationCategory
from ...models.results_list_storage_location import ResultsListStorageLocation
from ...models.results_list_storage_status import ResultsListStorageStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    curation_category: Union[Unset, ResultsListCEDACurationCategory] = UNSET,
    curation_category_contains: Union[Unset, str] = UNSET,
    curation_category_endswith: Union[Unset, str] = UNSET,
    curation_category_gt: Union[Unset, str] = UNSET,
    curation_category_gte: Union[Unset, str] = UNSET,
    curation_category_icontains: Union[Unset, str] = UNSET,
    curation_category_iendswith: Union[Unset, str] = UNSET,
    curation_category_iexact: Union[Unset, str] = UNSET,
    curation_category_in: Union[Unset, list[str]] = UNSET,
    curation_category_iregex: Union[Unset, str] = UNSET,
    curation_category_isnull: Union[Unset, bool] = UNSET,
    curation_category_istartswith: Union[Unset, str] = UNSET,
    curation_category_lt: Union[Unset, str] = UNSET,
    curation_category_lte: Union[Unset, str] = UNSET,
    curation_category_range: Union[Unset, list[str]] = UNSET,
    curation_category_regex: Union[Unset, str] = UNSET,
    curation_category_startswith: Union[Unset, str] = UNSET,
    data_path: Union[Unset, str] = UNSET,
    data_path_contains: Union[Unset, str] = UNSET,
    data_path_endswith: Union[Unset, str] = UNSET,
    data_path_gt: Union[Unset, str] = UNSET,
    data_path_gte: Union[Unset, str] = UNSET,
    data_path_icontains: Union[Unset, str] = UNSET,
    data_path_iendswith: Union[Unset, str] = UNSET,
    data_path_iexact: Union[Unset, str] = UNSET,
    data_path_in: Union[Unset, list[str]] = UNSET,
    data_path_iregex: Union[Unset, str] = UNSET,
    data_path_isnull: Union[Unset, bool] = UNSET,
    data_path_istartswith: Union[Unset, str] = UNSET,
    data_path_lt: Union[Unset, str] = UNSET,
    data_path_lte: Union[Unset, str] = UNSET,
    data_path_range: Union[Unset, list[str]] = UNSET,
    data_path_regex: Union[Unset, str] = UNSET,
    data_path_startswith: Union[Unset, str] = UNSET,
    file_format: Union[Unset, str] = UNSET,
    file_format_contains: Union[Unset, str] = UNSET,
    file_format_endswith: Union[Unset, str] = UNSET,
    file_format_gt: Union[Unset, str] = UNSET,
    file_format_gte: Union[Unset, str] = UNSET,
    file_format_icontains: Union[Unset, str] = UNSET,
    file_format_iendswith: Union[Unset, str] = UNSET,
    file_format_iexact: Union[Unset, str] = UNSET,
    file_format_in: Union[Unset, list[str]] = UNSET,
    file_format_iregex: Union[Unset, str] = UNSET,
    file_format_isnull: Union[Unset, bool] = UNSET,
    file_format_istartswith: Union[Unset, str] = UNSET,
    file_format_lt: Union[Unset, str] = UNSET,
    file_format_lte: Union[Unset, str] = UNSET,
    file_format_range: Union[Unset, list[str]] = UNSET,
    file_format_regex: Union[Unset, str] = UNSET,
    file_format_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    number_of_files: Union[Unset, int] = UNSET,
    number_of_files_contained_by: Union[Unset, int] = UNSET,
    number_of_files_contains: Union[Unset, int] = UNSET,
    number_of_files_endswith: Union[Unset, int] = UNSET,
    number_of_files_gt: Union[Unset, int] = UNSET,
    number_of_files_gte: Union[Unset, int] = UNSET,
    number_of_files_icontains: Union[Unset, int] = UNSET,
    number_of_files_iendswith: Union[Unset, int] = UNSET,
    number_of_files_iexact: Union[Unset, int] = UNSET,
    number_of_files_in: Union[Unset, list[int]] = UNSET,
    number_of_files_iregex: Union[Unset, int] = UNSET,
    number_of_files_isnull: Union[Unset, bool] = UNSET,
    number_of_files_istartswith: Union[Unset, int] = UNSET,
    number_of_files_lt: Union[Unset, int] = UNSET,
    number_of_files_lte: Union[Unset, int] = UNSET,
    number_of_files_range: Union[Unset, list[int]] = UNSET,
    number_of_files_regex: Union[Unset, int] = UNSET,
    number_of_files_startswith: Union[Unset, int] = UNSET,
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
    observation_ob_id: Union[Unset, int] = UNSET,
    observation_ob_id_in: Union[Unset, list[int]] = UNSET,
    observation_uuid: Union[Unset, str] = UNSET,
    observation_uuid_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    referenceable_ptr: Union[Unset, int] = UNSET,
    referenceable_ptr_gt: Union[Unset, int] = UNSET,
    referenceable_ptr_gte: Union[Unset, int] = UNSET,
    referenceable_ptr_in: Union[Unset, list[int]] = UNSET,
    referenceable_ptr_isnull: Union[Unset, bool] = UNSET,
    referenceable_ptr_lt: Union[Unset, int] = UNSET,
    referenceable_ptr_lte: Union[Unset, int] = UNSET,
    short_code: Union[Unset, str] = UNSET,
    short_code_contains: Union[Unset, str] = UNSET,
    short_code_endswith: Union[Unset, str] = UNSET,
    short_code_gt: Union[Unset, str] = UNSET,
    short_code_gte: Union[Unset, str] = UNSET,
    short_code_icontains: Union[Unset, str] = UNSET,
    short_code_iendswith: Union[Unset, str] = UNSET,
    short_code_iexact: Union[Unset, str] = UNSET,
    short_code_in: Union[Unset, list[str]] = UNSET,
    short_code_iregex: Union[Unset, str] = UNSET,
    short_code_isnull: Union[Unset, bool] = UNSET,
    short_code_istartswith: Union[Unset, str] = UNSET,
    short_code_lt: Union[Unset, str] = UNSET,
    short_code_lte: Union[Unset, str] = UNSET,
    short_code_range: Union[Unset, list[str]] = UNSET,
    short_code_regex: Union[Unset, str] = UNSET,
    short_code_startswith: Union[Unset, str] = UNSET,
    storage_location: Union[Unset, ResultsListStorageLocation] = UNSET,
    storage_location_contains: Union[Unset, str] = UNSET,
    storage_location_endswith: Union[Unset, str] = UNSET,
    storage_location_gt: Union[Unset, str] = UNSET,
    storage_location_gte: Union[Unset, str] = UNSET,
    storage_location_icontains: Union[Unset, str] = UNSET,
    storage_location_iendswith: Union[Unset, str] = UNSET,
    storage_location_iexact: Union[Unset, str] = UNSET,
    storage_location_in: Union[Unset, list[str]] = UNSET,
    storage_location_iregex: Union[Unset, str] = UNSET,
    storage_location_isnull: Union[Unset, bool] = UNSET,
    storage_location_istartswith: Union[Unset, str] = UNSET,
    storage_location_lt: Union[Unset, str] = UNSET,
    storage_location_lte: Union[Unset, str] = UNSET,
    storage_location_range: Union[Unset, list[str]] = UNSET,
    storage_location_regex: Union[Unset, str] = UNSET,
    storage_location_startswith: Union[Unset, str] = UNSET,
    storage_status: Union[Unset, ResultsListStorageStatus] = UNSET,
    storage_status_contains: Union[Unset, str] = UNSET,
    storage_status_endswith: Union[Unset, str] = UNSET,
    storage_status_gt: Union[Unset, str] = UNSET,
    storage_status_gte: Union[Unset, str] = UNSET,
    storage_status_icontains: Union[Unset, str] = UNSET,
    storage_status_iendswith: Union[Unset, str] = UNSET,
    storage_status_iexact: Union[Unset, str] = UNSET,
    storage_status_in: Union[Unset, list[str]] = UNSET,
    storage_status_iregex: Union[Unset, str] = UNSET,
    storage_status_isnull: Union[Unset, bool] = UNSET,
    storage_status_istartswith: Union[Unset, str] = UNSET,
    storage_status_lt: Union[Unset, str] = UNSET,
    storage_status_lte: Union[Unset, str] = UNSET,
    storage_status_range: Union[Unset, list[str]] = UNSET,
    storage_status_regex: Union[Unset, str] = UNSET,
    storage_status_startswith: Union[Unset, str] = UNSET,
    uuid: Union[Unset, str] = UNSET,
    uuid_contains: Union[Unset, str] = UNSET,
    uuid_endswith: Union[Unset, str] = UNSET,
    uuid_gt: Union[Unset, str] = UNSET,
    uuid_gte: Union[Unset, str] = UNSET,
    uuid_icontains: Union[Unset, str] = UNSET,
    uuid_iendswith: Union[Unset, str] = UNSET,
    uuid_iexact: Union[Unset, str] = UNSET,
    uuid_in: Union[Unset, list[str]] = UNSET,
    uuid_iregex: Union[Unset, str] = UNSET,
    uuid_isnull: Union[Unset, bool] = UNSET,
    uuid_istartswith: Union[Unset, str] = UNSET,
    uuid_lt: Union[Unset, str] = UNSET,
    uuid_lte: Union[Unset, str] = UNSET,
    uuid_range: Union[Unset, list[str]] = UNSET,
    uuid_regex: Union[Unset, str] = UNSET,
    uuid_startswith: Union[Unset, str] = UNSET,
    volume: Union[Unset, int] = UNSET,
    volume_contained_by: Union[Unset, int] = UNSET,
    volume_contains: Union[Unset, int] = UNSET,
    volume_endswith: Union[Unset, int] = UNSET,
    volume_gt: Union[Unset, int] = UNSET,
    volume_gte: Union[Unset, int] = UNSET,
    volume_icontains: Union[Unset, int] = UNSET,
    volume_iendswith: Union[Unset, int] = UNSET,
    volume_iexact: Union[Unset, int] = UNSET,
    volume_in: Union[Unset, list[int]] = UNSET,
    volume_iregex: Union[Unset, int] = UNSET,
    volume_isnull: Union[Unset, bool] = UNSET,
    volume_istartswith: Union[Unset, int] = UNSET,
    volume_lt: Union[Unset, int] = UNSET,
    volume_lte: Union[Unset, int] = UNSET,
    volume_range: Union[Unset, list[int]] = UNSET,
    volume_regex: Union[Unset, int] = UNSET,
    volume_startswith: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_curation_category: Union[Unset, str] = UNSET
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

    json_curation_category_in: Union[Unset, list[str]] = UNSET
    if not isinstance(curation_category_in, Unset):
        json_curation_category_in = curation_category_in

    params["curationCategory__in"] = json_curation_category_in

    params["curationCategory__iregex"] = curation_category_iregex

    params["curationCategory__isnull"] = curation_category_isnull

    params["curationCategory__istartswith"] = curation_category_istartswith

    params["curationCategory__lt"] = curation_category_lt

    params["curationCategory__lte"] = curation_category_lte

    json_curation_category_range: Union[Unset, list[str]] = UNSET
    if not isinstance(curation_category_range, Unset):
        json_curation_category_range = curation_category_range

    params["curationCategory__range"] = json_curation_category_range

    params["curationCategory__regex"] = curation_category_regex

    params["curationCategory__startswith"] = curation_category_startswith

    params["dataPath"] = data_path

    params["dataPath__contains"] = data_path_contains

    params["dataPath__endswith"] = data_path_endswith

    params["dataPath__gt"] = data_path_gt

    params["dataPath__gte"] = data_path_gte

    params["dataPath__icontains"] = data_path_icontains

    params["dataPath__iendswith"] = data_path_iendswith

    params["dataPath__iexact"] = data_path_iexact

    json_data_path_in: Union[Unset, list[str]] = UNSET
    if not isinstance(data_path_in, Unset):
        json_data_path_in = data_path_in

    params["dataPath__in"] = json_data_path_in

    params["dataPath__iregex"] = data_path_iregex

    params["dataPath__isnull"] = data_path_isnull

    params["dataPath__istartswith"] = data_path_istartswith

    params["dataPath__lt"] = data_path_lt

    params["dataPath__lte"] = data_path_lte

    json_data_path_range: Union[Unset, list[str]] = UNSET
    if not isinstance(data_path_range, Unset):
        json_data_path_range = data_path_range

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

    json_file_format_in: Union[Unset, list[str]] = UNSET
    if not isinstance(file_format_in, Unset):
        json_file_format_in = file_format_in

    params["fileFormat__in"] = json_file_format_in

    params["fileFormat__iregex"] = file_format_iregex

    params["fileFormat__isnull"] = file_format_isnull

    params["fileFormat__istartswith"] = file_format_istartswith

    params["fileFormat__lt"] = file_format_lt

    params["fileFormat__lte"] = file_format_lte

    json_file_format_range: Union[Unset, list[str]] = UNSET
    if not isinstance(file_format_range, Unset):
        json_file_format_range = file_format_range

    params["fileFormat__range"] = json_file_format_range

    params["fileFormat__regex"] = file_format_regex

    params["fileFormat__startswith"] = file_format_startswith

    params["limit"] = limit

    params["numberOfFiles"] = number_of_files

    params["numberOfFiles__contained_by"] = number_of_files_contained_by

    params["numberOfFiles__contains"] = number_of_files_contains

    params["numberOfFiles__endswith"] = number_of_files_endswith

    params["numberOfFiles__gt"] = number_of_files_gt

    params["numberOfFiles__gte"] = number_of_files_gte

    params["numberOfFiles__icontains"] = number_of_files_icontains

    params["numberOfFiles__iendswith"] = number_of_files_iendswith

    params["numberOfFiles__iexact"] = number_of_files_iexact

    json_number_of_files_in: Union[Unset, list[int]] = UNSET
    if not isinstance(number_of_files_in, Unset):
        json_number_of_files_in = number_of_files_in

    params["numberOfFiles__in"] = json_number_of_files_in

    params["numberOfFiles__iregex"] = number_of_files_iregex

    params["numberOfFiles__isnull"] = number_of_files_isnull

    params["numberOfFiles__istartswith"] = number_of_files_istartswith

    params["numberOfFiles__lt"] = number_of_files_lt

    params["numberOfFiles__lte"] = number_of_files_lte

    json_number_of_files_range: Union[Unset, list[int]] = UNSET
    if not isinstance(number_of_files_range, Unset):
        json_number_of_files_range = number_of_files_range

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

    json_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_in, Unset):
        json_ob_id_in = ob_id_in

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ob_id_range

    params["ob_id__range"] = json_ob_id_range

    params["ob_id__regex"] = ob_id_regex

    params["ob_id__startswith"] = ob_id_startswith

    params["observation__ob_id"] = observation_ob_id

    json_observation_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(observation_ob_id_in, Unset):
        json_observation_ob_id_in = observation_ob_id_in

    params["observation__ob_id__in"] = json_observation_ob_id_in

    params["observation__uuid"] = observation_uuid

    json_observation_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(observation_uuid_in, Unset):
        json_observation_uuid_in = observation_uuid_in

    params["observation__uuid__in"] = json_observation_uuid_in

    params["offset"] = offset

    params["ordering"] = ordering

    params["referenceable_ptr"] = referenceable_ptr

    params["referenceable_ptr__gt"] = referenceable_ptr_gt

    params["referenceable_ptr__gte"] = referenceable_ptr_gte

    json_referenceable_ptr_in: Union[Unset, list[int]] = UNSET
    if not isinstance(referenceable_ptr_in, Unset):
        json_referenceable_ptr_in = referenceable_ptr_in

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

    json_short_code_in: Union[Unset, list[str]] = UNSET
    if not isinstance(short_code_in, Unset):
        json_short_code_in = short_code_in

    params["short_code__in"] = json_short_code_in

    params["short_code__iregex"] = short_code_iregex

    params["short_code__isnull"] = short_code_isnull

    params["short_code__istartswith"] = short_code_istartswith

    params["short_code__lt"] = short_code_lt

    params["short_code__lte"] = short_code_lte

    json_short_code_range: Union[Unset, list[str]] = UNSET
    if not isinstance(short_code_range, Unset):
        json_short_code_range = short_code_range

    params["short_code__range"] = json_short_code_range

    params["short_code__regex"] = short_code_regex

    params["short_code__startswith"] = short_code_startswith

    json_storage_location: Union[Unset, str] = UNSET
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

    json_storage_location_in: Union[Unset, list[str]] = UNSET
    if not isinstance(storage_location_in, Unset):
        json_storage_location_in = storage_location_in

    params["storageLocation__in"] = json_storage_location_in

    params["storageLocation__iregex"] = storage_location_iregex

    params["storageLocation__isnull"] = storage_location_isnull

    params["storageLocation__istartswith"] = storage_location_istartswith

    params["storageLocation__lt"] = storage_location_lt

    params["storageLocation__lte"] = storage_location_lte

    json_storage_location_range: Union[Unset, list[str]] = UNSET
    if not isinstance(storage_location_range, Unset):
        json_storage_location_range = storage_location_range

    params["storageLocation__range"] = json_storage_location_range

    params["storageLocation__regex"] = storage_location_regex

    params["storageLocation__startswith"] = storage_location_startswith

    json_storage_status: Union[Unset, str] = UNSET
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

    json_storage_status_in: Union[Unset, list[str]] = UNSET
    if not isinstance(storage_status_in, Unset):
        json_storage_status_in = storage_status_in

    params["storageStatus__in"] = json_storage_status_in

    params["storageStatus__iregex"] = storage_status_iregex

    params["storageStatus__isnull"] = storage_status_isnull

    params["storageStatus__istartswith"] = storage_status_istartswith

    params["storageStatus__lt"] = storage_status_lt

    params["storageStatus__lte"] = storage_status_lte

    json_storage_status_range: Union[Unset, list[str]] = UNSET
    if not isinstance(storage_status_range, Unset):
        json_storage_status_range = storage_status_range

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

    json_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(uuid_in, Unset):
        json_uuid_in = uuid_in

    params["uuid__in"] = json_uuid_in

    params["uuid__iregex"] = uuid_iregex

    params["uuid__isnull"] = uuid_isnull

    params["uuid__istartswith"] = uuid_istartswith

    params["uuid__lt"] = uuid_lt

    params["uuid__lte"] = uuid_lte

    json_uuid_range: Union[Unset, list[str]] = UNSET
    if not isinstance(uuid_range, Unset):
        json_uuid_range = uuid_range

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

    json_volume_in: Union[Unset, list[int]] = UNSET
    if not isinstance(volume_in, Unset):
        json_volume_in = volume_in

    params["volume__in"] = json_volume_in

    params["volume__iregex"] = volume_iregex

    params["volume__isnull"] = volume_isnull

    params["volume__istartswith"] = volume_istartswith

    params["volume__lt"] = volume_lt

    params["volume__lte"] = volume_lte

    json_volume_range: Union[Unset, list[int]] = UNSET
    if not isinstance(volume_range, Unset):
        json_volume_range = volume_range

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedResultWriteList]:
    if response.status_code == 200:
        response_200 = PaginatedResultWriteList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedResultWriteList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    curation_category: Union[Unset, ResultsListCEDACurationCategory] = UNSET,
    curation_category_contains: Union[Unset, str] = UNSET,
    curation_category_endswith: Union[Unset, str] = UNSET,
    curation_category_gt: Union[Unset, str] = UNSET,
    curation_category_gte: Union[Unset, str] = UNSET,
    curation_category_icontains: Union[Unset, str] = UNSET,
    curation_category_iendswith: Union[Unset, str] = UNSET,
    curation_category_iexact: Union[Unset, str] = UNSET,
    curation_category_in: Union[Unset, list[str]] = UNSET,
    curation_category_iregex: Union[Unset, str] = UNSET,
    curation_category_isnull: Union[Unset, bool] = UNSET,
    curation_category_istartswith: Union[Unset, str] = UNSET,
    curation_category_lt: Union[Unset, str] = UNSET,
    curation_category_lte: Union[Unset, str] = UNSET,
    curation_category_range: Union[Unset, list[str]] = UNSET,
    curation_category_regex: Union[Unset, str] = UNSET,
    curation_category_startswith: Union[Unset, str] = UNSET,
    data_path: Union[Unset, str] = UNSET,
    data_path_contains: Union[Unset, str] = UNSET,
    data_path_endswith: Union[Unset, str] = UNSET,
    data_path_gt: Union[Unset, str] = UNSET,
    data_path_gte: Union[Unset, str] = UNSET,
    data_path_icontains: Union[Unset, str] = UNSET,
    data_path_iendswith: Union[Unset, str] = UNSET,
    data_path_iexact: Union[Unset, str] = UNSET,
    data_path_in: Union[Unset, list[str]] = UNSET,
    data_path_iregex: Union[Unset, str] = UNSET,
    data_path_isnull: Union[Unset, bool] = UNSET,
    data_path_istartswith: Union[Unset, str] = UNSET,
    data_path_lt: Union[Unset, str] = UNSET,
    data_path_lte: Union[Unset, str] = UNSET,
    data_path_range: Union[Unset, list[str]] = UNSET,
    data_path_regex: Union[Unset, str] = UNSET,
    data_path_startswith: Union[Unset, str] = UNSET,
    file_format: Union[Unset, str] = UNSET,
    file_format_contains: Union[Unset, str] = UNSET,
    file_format_endswith: Union[Unset, str] = UNSET,
    file_format_gt: Union[Unset, str] = UNSET,
    file_format_gte: Union[Unset, str] = UNSET,
    file_format_icontains: Union[Unset, str] = UNSET,
    file_format_iendswith: Union[Unset, str] = UNSET,
    file_format_iexact: Union[Unset, str] = UNSET,
    file_format_in: Union[Unset, list[str]] = UNSET,
    file_format_iregex: Union[Unset, str] = UNSET,
    file_format_isnull: Union[Unset, bool] = UNSET,
    file_format_istartswith: Union[Unset, str] = UNSET,
    file_format_lt: Union[Unset, str] = UNSET,
    file_format_lte: Union[Unset, str] = UNSET,
    file_format_range: Union[Unset, list[str]] = UNSET,
    file_format_regex: Union[Unset, str] = UNSET,
    file_format_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    number_of_files: Union[Unset, int] = UNSET,
    number_of_files_contained_by: Union[Unset, int] = UNSET,
    number_of_files_contains: Union[Unset, int] = UNSET,
    number_of_files_endswith: Union[Unset, int] = UNSET,
    number_of_files_gt: Union[Unset, int] = UNSET,
    number_of_files_gte: Union[Unset, int] = UNSET,
    number_of_files_icontains: Union[Unset, int] = UNSET,
    number_of_files_iendswith: Union[Unset, int] = UNSET,
    number_of_files_iexact: Union[Unset, int] = UNSET,
    number_of_files_in: Union[Unset, list[int]] = UNSET,
    number_of_files_iregex: Union[Unset, int] = UNSET,
    number_of_files_isnull: Union[Unset, bool] = UNSET,
    number_of_files_istartswith: Union[Unset, int] = UNSET,
    number_of_files_lt: Union[Unset, int] = UNSET,
    number_of_files_lte: Union[Unset, int] = UNSET,
    number_of_files_range: Union[Unset, list[int]] = UNSET,
    number_of_files_regex: Union[Unset, int] = UNSET,
    number_of_files_startswith: Union[Unset, int] = UNSET,
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
    observation_ob_id: Union[Unset, int] = UNSET,
    observation_ob_id_in: Union[Unset, list[int]] = UNSET,
    observation_uuid: Union[Unset, str] = UNSET,
    observation_uuid_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    referenceable_ptr: Union[Unset, int] = UNSET,
    referenceable_ptr_gt: Union[Unset, int] = UNSET,
    referenceable_ptr_gte: Union[Unset, int] = UNSET,
    referenceable_ptr_in: Union[Unset, list[int]] = UNSET,
    referenceable_ptr_isnull: Union[Unset, bool] = UNSET,
    referenceable_ptr_lt: Union[Unset, int] = UNSET,
    referenceable_ptr_lte: Union[Unset, int] = UNSET,
    short_code: Union[Unset, str] = UNSET,
    short_code_contains: Union[Unset, str] = UNSET,
    short_code_endswith: Union[Unset, str] = UNSET,
    short_code_gt: Union[Unset, str] = UNSET,
    short_code_gte: Union[Unset, str] = UNSET,
    short_code_icontains: Union[Unset, str] = UNSET,
    short_code_iendswith: Union[Unset, str] = UNSET,
    short_code_iexact: Union[Unset, str] = UNSET,
    short_code_in: Union[Unset, list[str]] = UNSET,
    short_code_iregex: Union[Unset, str] = UNSET,
    short_code_isnull: Union[Unset, bool] = UNSET,
    short_code_istartswith: Union[Unset, str] = UNSET,
    short_code_lt: Union[Unset, str] = UNSET,
    short_code_lte: Union[Unset, str] = UNSET,
    short_code_range: Union[Unset, list[str]] = UNSET,
    short_code_regex: Union[Unset, str] = UNSET,
    short_code_startswith: Union[Unset, str] = UNSET,
    storage_location: Union[Unset, ResultsListStorageLocation] = UNSET,
    storage_location_contains: Union[Unset, str] = UNSET,
    storage_location_endswith: Union[Unset, str] = UNSET,
    storage_location_gt: Union[Unset, str] = UNSET,
    storage_location_gte: Union[Unset, str] = UNSET,
    storage_location_icontains: Union[Unset, str] = UNSET,
    storage_location_iendswith: Union[Unset, str] = UNSET,
    storage_location_iexact: Union[Unset, str] = UNSET,
    storage_location_in: Union[Unset, list[str]] = UNSET,
    storage_location_iregex: Union[Unset, str] = UNSET,
    storage_location_isnull: Union[Unset, bool] = UNSET,
    storage_location_istartswith: Union[Unset, str] = UNSET,
    storage_location_lt: Union[Unset, str] = UNSET,
    storage_location_lte: Union[Unset, str] = UNSET,
    storage_location_range: Union[Unset, list[str]] = UNSET,
    storage_location_regex: Union[Unset, str] = UNSET,
    storage_location_startswith: Union[Unset, str] = UNSET,
    storage_status: Union[Unset, ResultsListStorageStatus] = UNSET,
    storage_status_contains: Union[Unset, str] = UNSET,
    storage_status_endswith: Union[Unset, str] = UNSET,
    storage_status_gt: Union[Unset, str] = UNSET,
    storage_status_gte: Union[Unset, str] = UNSET,
    storage_status_icontains: Union[Unset, str] = UNSET,
    storage_status_iendswith: Union[Unset, str] = UNSET,
    storage_status_iexact: Union[Unset, str] = UNSET,
    storage_status_in: Union[Unset, list[str]] = UNSET,
    storage_status_iregex: Union[Unset, str] = UNSET,
    storage_status_isnull: Union[Unset, bool] = UNSET,
    storage_status_istartswith: Union[Unset, str] = UNSET,
    storage_status_lt: Union[Unset, str] = UNSET,
    storage_status_lte: Union[Unset, str] = UNSET,
    storage_status_range: Union[Unset, list[str]] = UNSET,
    storage_status_regex: Union[Unset, str] = UNSET,
    storage_status_startswith: Union[Unset, str] = UNSET,
    uuid: Union[Unset, str] = UNSET,
    uuid_contains: Union[Unset, str] = UNSET,
    uuid_endswith: Union[Unset, str] = UNSET,
    uuid_gt: Union[Unset, str] = UNSET,
    uuid_gte: Union[Unset, str] = UNSET,
    uuid_icontains: Union[Unset, str] = UNSET,
    uuid_iendswith: Union[Unset, str] = UNSET,
    uuid_iexact: Union[Unset, str] = UNSET,
    uuid_in: Union[Unset, list[str]] = UNSET,
    uuid_iregex: Union[Unset, str] = UNSET,
    uuid_isnull: Union[Unset, bool] = UNSET,
    uuid_istartswith: Union[Unset, str] = UNSET,
    uuid_lt: Union[Unset, str] = UNSET,
    uuid_lte: Union[Unset, str] = UNSET,
    uuid_range: Union[Unset, list[str]] = UNSET,
    uuid_regex: Union[Unset, str] = UNSET,
    uuid_startswith: Union[Unset, str] = UNSET,
    volume: Union[Unset, int] = UNSET,
    volume_contained_by: Union[Unset, int] = UNSET,
    volume_contains: Union[Unset, int] = UNSET,
    volume_endswith: Union[Unset, int] = UNSET,
    volume_gt: Union[Unset, int] = UNSET,
    volume_gte: Union[Unset, int] = UNSET,
    volume_icontains: Union[Unset, int] = UNSET,
    volume_iendswith: Union[Unset, int] = UNSET,
    volume_iexact: Union[Unset, int] = UNSET,
    volume_in: Union[Unset, list[int]] = UNSET,
    volume_iregex: Union[Unset, int] = UNSET,
    volume_isnull: Union[Unset, bool] = UNSET,
    volume_istartswith: Union[Unset, int] = UNSET,
    volume_lt: Union[Unset, int] = UNSET,
    volume_lte: Union[Unset, int] = UNSET,
    volume_range: Union[Unset, list[int]] = UNSET,
    volume_regex: Union[Unset, int] = UNSET,
    volume_startswith: Union[Unset, int] = UNSET,
) -> Response[PaginatedResultWriteList]:
    """Get a list of Result objects. Results have a 1:1 mapping with Observations.

    Args:
        curation_category (Union[Unset, ResultsListCEDACurationCategory]):
        curation_category_contains (Union[Unset, str]):
        curation_category_endswith (Union[Unset, str]):
        curation_category_gt (Union[Unset, str]):
        curation_category_gte (Union[Unset, str]):
        curation_category_icontains (Union[Unset, str]):
        curation_category_iendswith (Union[Unset, str]):
        curation_category_iexact (Union[Unset, str]):
        curation_category_in (Union[Unset, list[str]]):
        curation_category_iregex (Union[Unset, str]):
        curation_category_isnull (Union[Unset, bool]):
        curation_category_istartswith (Union[Unset, str]):
        curation_category_lt (Union[Unset, str]):
        curation_category_lte (Union[Unset, str]):
        curation_category_range (Union[Unset, list[str]]):
        curation_category_regex (Union[Unset, str]):
        curation_category_startswith (Union[Unset, str]):
        data_path (Union[Unset, str]):
        data_path_contains (Union[Unset, str]):
        data_path_endswith (Union[Unset, str]):
        data_path_gt (Union[Unset, str]):
        data_path_gte (Union[Unset, str]):
        data_path_icontains (Union[Unset, str]):
        data_path_iendswith (Union[Unset, str]):
        data_path_iexact (Union[Unset, str]):
        data_path_in (Union[Unset, list[str]]):
        data_path_iregex (Union[Unset, str]):
        data_path_isnull (Union[Unset, bool]):
        data_path_istartswith (Union[Unset, str]):
        data_path_lt (Union[Unset, str]):
        data_path_lte (Union[Unset, str]):
        data_path_range (Union[Unset, list[str]]):
        data_path_regex (Union[Unset, str]):
        data_path_startswith (Union[Unset, str]):
        file_format (Union[Unset, str]):
        file_format_contains (Union[Unset, str]):
        file_format_endswith (Union[Unset, str]):
        file_format_gt (Union[Unset, str]):
        file_format_gte (Union[Unset, str]):
        file_format_icontains (Union[Unset, str]):
        file_format_iendswith (Union[Unset, str]):
        file_format_iexact (Union[Unset, str]):
        file_format_in (Union[Unset, list[str]]):
        file_format_iregex (Union[Unset, str]):
        file_format_isnull (Union[Unset, bool]):
        file_format_istartswith (Union[Unset, str]):
        file_format_lt (Union[Unset, str]):
        file_format_lte (Union[Unset, str]):
        file_format_range (Union[Unset, list[str]]):
        file_format_regex (Union[Unset, str]):
        file_format_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        number_of_files (Union[Unset, int]):
        number_of_files_contained_by (Union[Unset, int]):
        number_of_files_contains (Union[Unset, int]):
        number_of_files_endswith (Union[Unset, int]):
        number_of_files_gt (Union[Unset, int]):
        number_of_files_gte (Union[Unset, int]):
        number_of_files_icontains (Union[Unset, int]):
        number_of_files_iendswith (Union[Unset, int]):
        number_of_files_iexact (Union[Unset, int]):
        number_of_files_in (Union[Unset, list[int]]):
        number_of_files_iregex (Union[Unset, int]):
        number_of_files_isnull (Union[Unset, bool]):
        number_of_files_istartswith (Union[Unset, int]):
        number_of_files_lt (Union[Unset, int]):
        number_of_files_lte (Union[Unset, int]):
        number_of_files_range (Union[Unset, list[int]]):
        number_of_files_regex (Union[Unset, int]):
        number_of_files_startswith (Union[Unset, int]):
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
        observation_ob_id (Union[Unset, int]):
        observation_ob_id_in (Union[Unset, list[int]]):
        observation_uuid (Union[Unset, str]):
        observation_uuid_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        referenceable_ptr (Union[Unset, int]):
        referenceable_ptr_gt (Union[Unset, int]):
        referenceable_ptr_gte (Union[Unset, int]):
        referenceable_ptr_in (Union[Unset, list[int]]):
        referenceable_ptr_isnull (Union[Unset, bool]):
        referenceable_ptr_lt (Union[Unset, int]):
        referenceable_ptr_lte (Union[Unset, int]):
        short_code (Union[Unset, str]):
        short_code_contains (Union[Unset, str]):
        short_code_endswith (Union[Unset, str]):
        short_code_gt (Union[Unset, str]):
        short_code_gte (Union[Unset, str]):
        short_code_icontains (Union[Unset, str]):
        short_code_iendswith (Union[Unset, str]):
        short_code_iexact (Union[Unset, str]):
        short_code_in (Union[Unset, list[str]]):
        short_code_iregex (Union[Unset, str]):
        short_code_isnull (Union[Unset, bool]):
        short_code_istartswith (Union[Unset, str]):
        short_code_lt (Union[Unset, str]):
        short_code_lte (Union[Unset, str]):
        short_code_range (Union[Unset, list[str]]):
        short_code_regex (Union[Unset, str]):
        short_code_startswith (Union[Unset, str]):
        storage_location (Union[Unset, ResultsListStorageLocation]):
        storage_location_contains (Union[Unset, str]):
        storage_location_endswith (Union[Unset, str]):
        storage_location_gt (Union[Unset, str]):
        storage_location_gte (Union[Unset, str]):
        storage_location_icontains (Union[Unset, str]):
        storage_location_iendswith (Union[Unset, str]):
        storage_location_iexact (Union[Unset, str]):
        storage_location_in (Union[Unset, list[str]]):
        storage_location_iregex (Union[Unset, str]):
        storage_location_isnull (Union[Unset, bool]):
        storage_location_istartswith (Union[Unset, str]):
        storage_location_lt (Union[Unset, str]):
        storage_location_lte (Union[Unset, str]):
        storage_location_range (Union[Unset, list[str]]):
        storage_location_regex (Union[Unset, str]):
        storage_location_startswith (Union[Unset, str]):
        storage_status (Union[Unset, ResultsListStorageStatus]):
        storage_status_contains (Union[Unset, str]):
        storage_status_endswith (Union[Unset, str]):
        storage_status_gt (Union[Unset, str]):
        storage_status_gte (Union[Unset, str]):
        storage_status_icontains (Union[Unset, str]):
        storage_status_iendswith (Union[Unset, str]):
        storage_status_iexact (Union[Unset, str]):
        storage_status_in (Union[Unset, list[str]]):
        storage_status_iregex (Union[Unset, str]):
        storage_status_isnull (Union[Unset, bool]):
        storage_status_istartswith (Union[Unset, str]):
        storage_status_lt (Union[Unset, str]):
        storage_status_lte (Union[Unset, str]):
        storage_status_range (Union[Unset, list[str]]):
        storage_status_regex (Union[Unset, str]):
        storage_status_startswith (Union[Unset, str]):
        uuid (Union[Unset, str]):
        uuid_contains (Union[Unset, str]):
        uuid_endswith (Union[Unset, str]):
        uuid_gt (Union[Unset, str]):
        uuid_gte (Union[Unset, str]):
        uuid_icontains (Union[Unset, str]):
        uuid_iendswith (Union[Unset, str]):
        uuid_iexact (Union[Unset, str]):
        uuid_in (Union[Unset, list[str]]):
        uuid_iregex (Union[Unset, str]):
        uuid_isnull (Union[Unset, bool]):
        uuid_istartswith (Union[Unset, str]):
        uuid_lt (Union[Unset, str]):
        uuid_lte (Union[Unset, str]):
        uuid_range (Union[Unset, list[str]]):
        uuid_regex (Union[Unset, str]):
        uuid_startswith (Union[Unset, str]):
        volume (Union[Unset, int]):
        volume_contained_by (Union[Unset, int]):
        volume_contains (Union[Unset, int]):
        volume_endswith (Union[Unset, int]):
        volume_gt (Union[Unset, int]):
        volume_gte (Union[Unset, int]):
        volume_icontains (Union[Unset, int]):
        volume_iendswith (Union[Unset, int]):
        volume_iexact (Union[Unset, int]):
        volume_in (Union[Unset, list[int]]):
        volume_iregex (Union[Unset, int]):
        volume_isnull (Union[Unset, bool]):
        volume_istartswith (Union[Unset, int]):
        volume_lt (Union[Unset, int]):
        volume_lte (Union[Unset, int]):
        volume_range (Union[Unset, list[int]]):
        volume_regex (Union[Unset, int]):
        volume_startswith (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResultWriteList]
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
        limit=limit,
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
        observation_ob_id=observation_ob_id,
        observation_ob_id_in=observation_ob_id_in,
        observation_uuid=observation_uuid,
        observation_uuid_in=observation_uuid_in,
        offset=offset,
        ordering=ordering,
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
    curation_category: Union[Unset, ResultsListCEDACurationCategory] = UNSET,
    curation_category_contains: Union[Unset, str] = UNSET,
    curation_category_endswith: Union[Unset, str] = UNSET,
    curation_category_gt: Union[Unset, str] = UNSET,
    curation_category_gte: Union[Unset, str] = UNSET,
    curation_category_icontains: Union[Unset, str] = UNSET,
    curation_category_iendswith: Union[Unset, str] = UNSET,
    curation_category_iexact: Union[Unset, str] = UNSET,
    curation_category_in: Union[Unset, list[str]] = UNSET,
    curation_category_iregex: Union[Unset, str] = UNSET,
    curation_category_isnull: Union[Unset, bool] = UNSET,
    curation_category_istartswith: Union[Unset, str] = UNSET,
    curation_category_lt: Union[Unset, str] = UNSET,
    curation_category_lte: Union[Unset, str] = UNSET,
    curation_category_range: Union[Unset, list[str]] = UNSET,
    curation_category_regex: Union[Unset, str] = UNSET,
    curation_category_startswith: Union[Unset, str] = UNSET,
    data_path: Union[Unset, str] = UNSET,
    data_path_contains: Union[Unset, str] = UNSET,
    data_path_endswith: Union[Unset, str] = UNSET,
    data_path_gt: Union[Unset, str] = UNSET,
    data_path_gte: Union[Unset, str] = UNSET,
    data_path_icontains: Union[Unset, str] = UNSET,
    data_path_iendswith: Union[Unset, str] = UNSET,
    data_path_iexact: Union[Unset, str] = UNSET,
    data_path_in: Union[Unset, list[str]] = UNSET,
    data_path_iregex: Union[Unset, str] = UNSET,
    data_path_isnull: Union[Unset, bool] = UNSET,
    data_path_istartswith: Union[Unset, str] = UNSET,
    data_path_lt: Union[Unset, str] = UNSET,
    data_path_lte: Union[Unset, str] = UNSET,
    data_path_range: Union[Unset, list[str]] = UNSET,
    data_path_regex: Union[Unset, str] = UNSET,
    data_path_startswith: Union[Unset, str] = UNSET,
    file_format: Union[Unset, str] = UNSET,
    file_format_contains: Union[Unset, str] = UNSET,
    file_format_endswith: Union[Unset, str] = UNSET,
    file_format_gt: Union[Unset, str] = UNSET,
    file_format_gte: Union[Unset, str] = UNSET,
    file_format_icontains: Union[Unset, str] = UNSET,
    file_format_iendswith: Union[Unset, str] = UNSET,
    file_format_iexact: Union[Unset, str] = UNSET,
    file_format_in: Union[Unset, list[str]] = UNSET,
    file_format_iregex: Union[Unset, str] = UNSET,
    file_format_isnull: Union[Unset, bool] = UNSET,
    file_format_istartswith: Union[Unset, str] = UNSET,
    file_format_lt: Union[Unset, str] = UNSET,
    file_format_lte: Union[Unset, str] = UNSET,
    file_format_range: Union[Unset, list[str]] = UNSET,
    file_format_regex: Union[Unset, str] = UNSET,
    file_format_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    number_of_files: Union[Unset, int] = UNSET,
    number_of_files_contained_by: Union[Unset, int] = UNSET,
    number_of_files_contains: Union[Unset, int] = UNSET,
    number_of_files_endswith: Union[Unset, int] = UNSET,
    number_of_files_gt: Union[Unset, int] = UNSET,
    number_of_files_gte: Union[Unset, int] = UNSET,
    number_of_files_icontains: Union[Unset, int] = UNSET,
    number_of_files_iendswith: Union[Unset, int] = UNSET,
    number_of_files_iexact: Union[Unset, int] = UNSET,
    number_of_files_in: Union[Unset, list[int]] = UNSET,
    number_of_files_iregex: Union[Unset, int] = UNSET,
    number_of_files_isnull: Union[Unset, bool] = UNSET,
    number_of_files_istartswith: Union[Unset, int] = UNSET,
    number_of_files_lt: Union[Unset, int] = UNSET,
    number_of_files_lte: Union[Unset, int] = UNSET,
    number_of_files_range: Union[Unset, list[int]] = UNSET,
    number_of_files_regex: Union[Unset, int] = UNSET,
    number_of_files_startswith: Union[Unset, int] = UNSET,
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
    observation_ob_id: Union[Unset, int] = UNSET,
    observation_ob_id_in: Union[Unset, list[int]] = UNSET,
    observation_uuid: Union[Unset, str] = UNSET,
    observation_uuid_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    referenceable_ptr: Union[Unset, int] = UNSET,
    referenceable_ptr_gt: Union[Unset, int] = UNSET,
    referenceable_ptr_gte: Union[Unset, int] = UNSET,
    referenceable_ptr_in: Union[Unset, list[int]] = UNSET,
    referenceable_ptr_isnull: Union[Unset, bool] = UNSET,
    referenceable_ptr_lt: Union[Unset, int] = UNSET,
    referenceable_ptr_lte: Union[Unset, int] = UNSET,
    short_code: Union[Unset, str] = UNSET,
    short_code_contains: Union[Unset, str] = UNSET,
    short_code_endswith: Union[Unset, str] = UNSET,
    short_code_gt: Union[Unset, str] = UNSET,
    short_code_gte: Union[Unset, str] = UNSET,
    short_code_icontains: Union[Unset, str] = UNSET,
    short_code_iendswith: Union[Unset, str] = UNSET,
    short_code_iexact: Union[Unset, str] = UNSET,
    short_code_in: Union[Unset, list[str]] = UNSET,
    short_code_iregex: Union[Unset, str] = UNSET,
    short_code_isnull: Union[Unset, bool] = UNSET,
    short_code_istartswith: Union[Unset, str] = UNSET,
    short_code_lt: Union[Unset, str] = UNSET,
    short_code_lte: Union[Unset, str] = UNSET,
    short_code_range: Union[Unset, list[str]] = UNSET,
    short_code_regex: Union[Unset, str] = UNSET,
    short_code_startswith: Union[Unset, str] = UNSET,
    storage_location: Union[Unset, ResultsListStorageLocation] = UNSET,
    storage_location_contains: Union[Unset, str] = UNSET,
    storage_location_endswith: Union[Unset, str] = UNSET,
    storage_location_gt: Union[Unset, str] = UNSET,
    storage_location_gte: Union[Unset, str] = UNSET,
    storage_location_icontains: Union[Unset, str] = UNSET,
    storage_location_iendswith: Union[Unset, str] = UNSET,
    storage_location_iexact: Union[Unset, str] = UNSET,
    storage_location_in: Union[Unset, list[str]] = UNSET,
    storage_location_iregex: Union[Unset, str] = UNSET,
    storage_location_isnull: Union[Unset, bool] = UNSET,
    storage_location_istartswith: Union[Unset, str] = UNSET,
    storage_location_lt: Union[Unset, str] = UNSET,
    storage_location_lte: Union[Unset, str] = UNSET,
    storage_location_range: Union[Unset, list[str]] = UNSET,
    storage_location_regex: Union[Unset, str] = UNSET,
    storage_location_startswith: Union[Unset, str] = UNSET,
    storage_status: Union[Unset, ResultsListStorageStatus] = UNSET,
    storage_status_contains: Union[Unset, str] = UNSET,
    storage_status_endswith: Union[Unset, str] = UNSET,
    storage_status_gt: Union[Unset, str] = UNSET,
    storage_status_gte: Union[Unset, str] = UNSET,
    storage_status_icontains: Union[Unset, str] = UNSET,
    storage_status_iendswith: Union[Unset, str] = UNSET,
    storage_status_iexact: Union[Unset, str] = UNSET,
    storage_status_in: Union[Unset, list[str]] = UNSET,
    storage_status_iregex: Union[Unset, str] = UNSET,
    storage_status_isnull: Union[Unset, bool] = UNSET,
    storage_status_istartswith: Union[Unset, str] = UNSET,
    storage_status_lt: Union[Unset, str] = UNSET,
    storage_status_lte: Union[Unset, str] = UNSET,
    storage_status_range: Union[Unset, list[str]] = UNSET,
    storage_status_regex: Union[Unset, str] = UNSET,
    storage_status_startswith: Union[Unset, str] = UNSET,
    uuid: Union[Unset, str] = UNSET,
    uuid_contains: Union[Unset, str] = UNSET,
    uuid_endswith: Union[Unset, str] = UNSET,
    uuid_gt: Union[Unset, str] = UNSET,
    uuid_gte: Union[Unset, str] = UNSET,
    uuid_icontains: Union[Unset, str] = UNSET,
    uuid_iendswith: Union[Unset, str] = UNSET,
    uuid_iexact: Union[Unset, str] = UNSET,
    uuid_in: Union[Unset, list[str]] = UNSET,
    uuid_iregex: Union[Unset, str] = UNSET,
    uuid_isnull: Union[Unset, bool] = UNSET,
    uuid_istartswith: Union[Unset, str] = UNSET,
    uuid_lt: Union[Unset, str] = UNSET,
    uuid_lte: Union[Unset, str] = UNSET,
    uuid_range: Union[Unset, list[str]] = UNSET,
    uuid_regex: Union[Unset, str] = UNSET,
    uuid_startswith: Union[Unset, str] = UNSET,
    volume: Union[Unset, int] = UNSET,
    volume_contained_by: Union[Unset, int] = UNSET,
    volume_contains: Union[Unset, int] = UNSET,
    volume_endswith: Union[Unset, int] = UNSET,
    volume_gt: Union[Unset, int] = UNSET,
    volume_gte: Union[Unset, int] = UNSET,
    volume_icontains: Union[Unset, int] = UNSET,
    volume_iendswith: Union[Unset, int] = UNSET,
    volume_iexact: Union[Unset, int] = UNSET,
    volume_in: Union[Unset, list[int]] = UNSET,
    volume_iregex: Union[Unset, int] = UNSET,
    volume_isnull: Union[Unset, bool] = UNSET,
    volume_istartswith: Union[Unset, int] = UNSET,
    volume_lt: Union[Unset, int] = UNSET,
    volume_lte: Union[Unset, int] = UNSET,
    volume_range: Union[Unset, list[int]] = UNSET,
    volume_regex: Union[Unset, int] = UNSET,
    volume_startswith: Union[Unset, int] = UNSET,
) -> Optional[PaginatedResultWriteList]:
    """Get a list of Result objects. Results have a 1:1 mapping with Observations.

    Args:
        curation_category (Union[Unset, ResultsListCEDACurationCategory]):
        curation_category_contains (Union[Unset, str]):
        curation_category_endswith (Union[Unset, str]):
        curation_category_gt (Union[Unset, str]):
        curation_category_gte (Union[Unset, str]):
        curation_category_icontains (Union[Unset, str]):
        curation_category_iendswith (Union[Unset, str]):
        curation_category_iexact (Union[Unset, str]):
        curation_category_in (Union[Unset, list[str]]):
        curation_category_iregex (Union[Unset, str]):
        curation_category_isnull (Union[Unset, bool]):
        curation_category_istartswith (Union[Unset, str]):
        curation_category_lt (Union[Unset, str]):
        curation_category_lte (Union[Unset, str]):
        curation_category_range (Union[Unset, list[str]]):
        curation_category_regex (Union[Unset, str]):
        curation_category_startswith (Union[Unset, str]):
        data_path (Union[Unset, str]):
        data_path_contains (Union[Unset, str]):
        data_path_endswith (Union[Unset, str]):
        data_path_gt (Union[Unset, str]):
        data_path_gte (Union[Unset, str]):
        data_path_icontains (Union[Unset, str]):
        data_path_iendswith (Union[Unset, str]):
        data_path_iexact (Union[Unset, str]):
        data_path_in (Union[Unset, list[str]]):
        data_path_iregex (Union[Unset, str]):
        data_path_isnull (Union[Unset, bool]):
        data_path_istartswith (Union[Unset, str]):
        data_path_lt (Union[Unset, str]):
        data_path_lte (Union[Unset, str]):
        data_path_range (Union[Unset, list[str]]):
        data_path_regex (Union[Unset, str]):
        data_path_startswith (Union[Unset, str]):
        file_format (Union[Unset, str]):
        file_format_contains (Union[Unset, str]):
        file_format_endswith (Union[Unset, str]):
        file_format_gt (Union[Unset, str]):
        file_format_gte (Union[Unset, str]):
        file_format_icontains (Union[Unset, str]):
        file_format_iendswith (Union[Unset, str]):
        file_format_iexact (Union[Unset, str]):
        file_format_in (Union[Unset, list[str]]):
        file_format_iregex (Union[Unset, str]):
        file_format_isnull (Union[Unset, bool]):
        file_format_istartswith (Union[Unset, str]):
        file_format_lt (Union[Unset, str]):
        file_format_lte (Union[Unset, str]):
        file_format_range (Union[Unset, list[str]]):
        file_format_regex (Union[Unset, str]):
        file_format_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        number_of_files (Union[Unset, int]):
        number_of_files_contained_by (Union[Unset, int]):
        number_of_files_contains (Union[Unset, int]):
        number_of_files_endswith (Union[Unset, int]):
        number_of_files_gt (Union[Unset, int]):
        number_of_files_gte (Union[Unset, int]):
        number_of_files_icontains (Union[Unset, int]):
        number_of_files_iendswith (Union[Unset, int]):
        number_of_files_iexact (Union[Unset, int]):
        number_of_files_in (Union[Unset, list[int]]):
        number_of_files_iregex (Union[Unset, int]):
        number_of_files_isnull (Union[Unset, bool]):
        number_of_files_istartswith (Union[Unset, int]):
        number_of_files_lt (Union[Unset, int]):
        number_of_files_lte (Union[Unset, int]):
        number_of_files_range (Union[Unset, list[int]]):
        number_of_files_regex (Union[Unset, int]):
        number_of_files_startswith (Union[Unset, int]):
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
        observation_ob_id (Union[Unset, int]):
        observation_ob_id_in (Union[Unset, list[int]]):
        observation_uuid (Union[Unset, str]):
        observation_uuid_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        referenceable_ptr (Union[Unset, int]):
        referenceable_ptr_gt (Union[Unset, int]):
        referenceable_ptr_gte (Union[Unset, int]):
        referenceable_ptr_in (Union[Unset, list[int]]):
        referenceable_ptr_isnull (Union[Unset, bool]):
        referenceable_ptr_lt (Union[Unset, int]):
        referenceable_ptr_lte (Union[Unset, int]):
        short_code (Union[Unset, str]):
        short_code_contains (Union[Unset, str]):
        short_code_endswith (Union[Unset, str]):
        short_code_gt (Union[Unset, str]):
        short_code_gte (Union[Unset, str]):
        short_code_icontains (Union[Unset, str]):
        short_code_iendswith (Union[Unset, str]):
        short_code_iexact (Union[Unset, str]):
        short_code_in (Union[Unset, list[str]]):
        short_code_iregex (Union[Unset, str]):
        short_code_isnull (Union[Unset, bool]):
        short_code_istartswith (Union[Unset, str]):
        short_code_lt (Union[Unset, str]):
        short_code_lte (Union[Unset, str]):
        short_code_range (Union[Unset, list[str]]):
        short_code_regex (Union[Unset, str]):
        short_code_startswith (Union[Unset, str]):
        storage_location (Union[Unset, ResultsListStorageLocation]):
        storage_location_contains (Union[Unset, str]):
        storage_location_endswith (Union[Unset, str]):
        storage_location_gt (Union[Unset, str]):
        storage_location_gte (Union[Unset, str]):
        storage_location_icontains (Union[Unset, str]):
        storage_location_iendswith (Union[Unset, str]):
        storage_location_iexact (Union[Unset, str]):
        storage_location_in (Union[Unset, list[str]]):
        storage_location_iregex (Union[Unset, str]):
        storage_location_isnull (Union[Unset, bool]):
        storage_location_istartswith (Union[Unset, str]):
        storage_location_lt (Union[Unset, str]):
        storage_location_lte (Union[Unset, str]):
        storage_location_range (Union[Unset, list[str]]):
        storage_location_regex (Union[Unset, str]):
        storage_location_startswith (Union[Unset, str]):
        storage_status (Union[Unset, ResultsListStorageStatus]):
        storage_status_contains (Union[Unset, str]):
        storage_status_endswith (Union[Unset, str]):
        storage_status_gt (Union[Unset, str]):
        storage_status_gte (Union[Unset, str]):
        storage_status_icontains (Union[Unset, str]):
        storage_status_iendswith (Union[Unset, str]):
        storage_status_iexact (Union[Unset, str]):
        storage_status_in (Union[Unset, list[str]]):
        storage_status_iregex (Union[Unset, str]):
        storage_status_isnull (Union[Unset, bool]):
        storage_status_istartswith (Union[Unset, str]):
        storage_status_lt (Union[Unset, str]):
        storage_status_lte (Union[Unset, str]):
        storage_status_range (Union[Unset, list[str]]):
        storage_status_regex (Union[Unset, str]):
        storage_status_startswith (Union[Unset, str]):
        uuid (Union[Unset, str]):
        uuid_contains (Union[Unset, str]):
        uuid_endswith (Union[Unset, str]):
        uuid_gt (Union[Unset, str]):
        uuid_gte (Union[Unset, str]):
        uuid_icontains (Union[Unset, str]):
        uuid_iendswith (Union[Unset, str]):
        uuid_iexact (Union[Unset, str]):
        uuid_in (Union[Unset, list[str]]):
        uuid_iregex (Union[Unset, str]):
        uuid_isnull (Union[Unset, bool]):
        uuid_istartswith (Union[Unset, str]):
        uuid_lt (Union[Unset, str]):
        uuid_lte (Union[Unset, str]):
        uuid_range (Union[Unset, list[str]]):
        uuid_regex (Union[Unset, str]):
        uuid_startswith (Union[Unset, str]):
        volume (Union[Unset, int]):
        volume_contained_by (Union[Unset, int]):
        volume_contains (Union[Unset, int]):
        volume_endswith (Union[Unset, int]):
        volume_gt (Union[Unset, int]):
        volume_gte (Union[Unset, int]):
        volume_icontains (Union[Unset, int]):
        volume_iendswith (Union[Unset, int]):
        volume_iexact (Union[Unset, int]):
        volume_in (Union[Unset, list[int]]):
        volume_iregex (Union[Unset, int]):
        volume_isnull (Union[Unset, bool]):
        volume_istartswith (Union[Unset, int]):
        volume_lt (Union[Unset, int]):
        volume_lte (Union[Unset, int]):
        volume_range (Union[Unset, list[int]]):
        volume_regex (Union[Unset, int]):
        volume_startswith (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResultWriteList
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
        limit=limit,
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
        observation_ob_id=observation_ob_id,
        observation_ob_id_in=observation_ob_id_in,
        observation_uuid=observation_uuid,
        observation_uuid_in=observation_uuid_in,
        offset=offset,
        ordering=ordering,
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
    curation_category: Union[Unset, ResultsListCEDACurationCategory] = UNSET,
    curation_category_contains: Union[Unset, str] = UNSET,
    curation_category_endswith: Union[Unset, str] = UNSET,
    curation_category_gt: Union[Unset, str] = UNSET,
    curation_category_gte: Union[Unset, str] = UNSET,
    curation_category_icontains: Union[Unset, str] = UNSET,
    curation_category_iendswith: Union[Unset, str] = UNSET,
    curation_category_iexact: Union[Unset, str] = UNSET,
    curation_category_in: Union[Unset, list[str]] = UNSET,
    curation_category_iregex: Union[Unset, str] = UNSET,
    curation_category_isnull: Union[Unset, bool] = UNSET,
    curation_category_istartswith: Union[Unset, str] = UNSET,
    curation_category_lt: Union[Unset, str] = UNSET,
    curation_category_lte: Union[Unset, str] = UNSET,
    curation_category_range: Union[Unset, list[str]] = UNSET,
    curation_category_regex: Union[Unset, str] = UNSET,
    curation_category_startswith: Union[Unset, str] = UNSET,
    data_path: Union[Unset, str] = UNSET,
    data_path_contains: Union[Unset, str] = UNSET,
    data_path_endswith: Union[Unset, str] = UNSET,
    data_path_gt: Union[Unset, str] = UNSET,
    data_path_gte: Union[Unset, str] = UNSET,
    data_path_icontains: Union[Unset, str] = UNSET,
    data_path_iendswith: Union[Unset, str] = UNSET,
    data_path_iexact: Union[Unset, str] = UNSET,
    data_path_in: Union[Unset, list[str]] = UNSET,
    data_path_iregex: Union[Unset, str] = UNSET,
    data_path_isnull: Union[Unset, bool] = UNSET,
    data_path_istartswith: Union[Unset, str] = UNSET,
    data_path_lt: Union[Unset, str] = UNSET,
    data_path_lte: Union[Unset, str] = UNSET,
    data_path_range: Union[Unset, list[str]] = UNSET,
    data_path_regex: Union[Unset, str] = UNSET,
    data_path_startswith: Union[Unset, str] = UNSET,
    file_format: Union[Unset, str] = UNSET,
    file_format_contains: Union[Unset, str] = UNSET,
    file_format_endswith: Union[Unset, str] = UNSET,
    file_format_gt: Union[Unset, str] = UNSET,
    file_format_gte: Union[Unset, str] = UNSET,
    file_format_icontains: Union[Unset, str] = UNSET,
    file_format_iendswith: Union[Unset, str] = UNSET,
    file_format_iexact: Union[Unset, str] = UNSET,
    file_format_in: Union[Unset, list[str]] = UNSET,
    file_format_iregex: Union[Unset, str] = UNSET,
    file_format_isnull: Union[Unset, bool] = UNSET,
    file_format_istartswith: Union[Unset, str] = UNSET,
    file_format_lt: Union[Unset, str] = UNSET,
    file_format_lte: Union[Unset, str] = UNSET,
    file_format_range: Union[Unset, list[str]] = UNSET,
    file_format_regex: Union[Unset, str] = UNSET,
    file_format_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    number_of_files: Union[Unset, int] = UNSET,
    number_of_files_contained_by: Union[Unset, int] = UNSET,
    number_of_files_contains: Union[Unset, int] = UNSET,
    number_of_files_endswith: Union[Unset, int] = UNSET,
    number_of_files_gt: Union[Unset, int] = UNSET,
    number_of_files_gte: Union[Unset, int] = UNSET,
    number_of_files_icontains: Union[Unset, int] = UNSET,
    number_of_files_iendswith: Union[Unset, int] = UNSET,
    number_of_files_iexact: Union[Unset, int] = UNSET,
    number_of_files_in: Union[Unset, list[int]] = UNSET,
    number_of_files_iregex: Union[Unset, int] = UNSET,
    number_of_files_isnull: Union[Unset, bool] = UNSET,
    number_of_files_istartswith: Union[Unset, int] = UNSET,
    number_of_files_lt: Union[Unset, int] = UNSET,
    number_of_files_lte: Union[Unset, int] = UNSET,
    number_of_files_range: Union[Unset, list[int]] = UNSET,
    number_of_files_regex: Union[Unset, int] = UNSET,
    number_of_files_startswith: Union[Unset, int] = UNSET,
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
    observation_ob_id: Union[Unset, int] = UNSET,
    observation_ob_id_in: Union[Unset, list[int]] = UNSET,
    observation_uuid: Union[Unset, str] = UNSET,
    observation_uuid_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    referenceable_ptr: Union[Unset, int] = UNSET,
    referenceable_ptr_gt: Union[Unset, int] = UNSET,
    referenceable_ptr_gte: Union[Unset, int] = UNSET,
    referenceable_ptr_in: Union[Unset, list[int]] = UNSET,
    referenceable_ptr_isnull: Union[Unset, bool] = UNSET,
    referenceable_ptr_lt: Union[Unset, int] = UNSET,
    referenceable_ptr_lte: Union[Unset, int] = UNSET,
    short_code: Union[Unset, str] = UNSET,
    short_code_contains: Union[Unset, str] = UNSET,
    short_code_endswith: Union[Unset, str] = UNSET,
    short_code_gt: Union[Unset, str] = UNSET,
    short_code_gte: Union[Unset, str] = UNSET,
    short_code_icontains: Union[Unset, str] = UNSET,
    short_code_iendswith: Union[Unset, str] = UNSET,
    short_code_iexact: Union[Unset, str] = UNSET,
    short_code_in: Union[Unset, list[str]] = UNSET,
    short_code_iregex: Union[Unset, str] = UNSET,
    short_code_isnull: Union[Unset, bool] = UNSET,
    short_code_istartswith: Union[Unset, str] = UNSET,
    short_code_lt: Union[Unset, str] = UNSET,
    short_code_lte: Union[Unset, str] = UNSET,
    short_code_range: Union[Unset, list[str]] = UNSET,
    short_code_regex: Union[Unset, str] = UNSET,
    short_code_startswith: Union[Unset, str] = UNSET,
    storage_location: Union[Unset, ResultsListStorageLocation] = UNSET,
    storage_location_contains: Union[Unset, str] = UNSET,
    storage_location_endswith: Union[Unset, str] = UNSET,
    storage_location_gt: Union[Unset, str] = UNSET,
    storage_location_gte: Union[Unset, str] = UNSET,
    storage_location_icontains: Union[Unset, str] = UNSET,
    storage_location_iendswith: Union[Unset, str] = UNSET,
    storage_location_iexact: Union[Unset, str] = UNSET,
    storage_location_in: Union[Unset, list[str]] = UNSET,
    storage_location_iregex: Union[Unset, str] = UNSET,
    storage_location_isnull: Union[Unset, bool] = UNSET,
    storage_location_istartswith: Union[Unset, str] = UNSET,
    storage_location_lt: Union[Unset, str] = UNSET,
    storage_location_lte: Union[Unset, str] = UNSET,
    storage_location_range: Union[Unset, list[str]] = UNSET,
    storage_location_regex: Union[Unset, str] = UNSET,
    storage_location_startswith: Union[Unset, str] = UNSET,
    storage_status: Union[Unset, ResultsListStorageStatus] = UNSET,
    storage_status_contains: Union[Unset, str] = UNSET,
    storage_status_endswith: Union[Unset, str] = UNSET,
    storage_status_gt: Union[Unset, str] = UNSET,
    storage_status_gte: Union[Unset, str] = UNSET,
    storage_status_icontains: Union[Unset, str] = UNSET,
    storage_status_iendswith: Union[Unset, str] = UNSET,
    storage_status_iexact: Union[Unset, str] = UNSET,
    storage_status_in: Union[Unset, list[str]] = UNSET,
    storage_status_iregex: Union[Unset, str] = UNSET,
    storage_status_isnull: Union[Unset, bool] = UNSET,
    storage_status_istartswith: Union[Unset, str] = UNSET,
    storage_status_lt: Union[Unset, str] = UNSET,
    storage_status_lte: Union[Unset, str] = UNSET,
    storage_status_range: Union[Unset, list[str]] = UNSET,
    storage_status_regex: Union[Unset, str] = UNSET,
    storage_status_startswith: Union[Unset, str] = UNSET,
    uuid: Union[Unset, str] = UNSET,
    uuid_contains: Union[Unset, str] = UNSET,
    uuid_endswith: Union[Unset, str] = UNSET,
    uuid_gt: Union[Unset, str] = UNSET,
    uuid_gte: Union[Unset, str] = UNSET,
    uuid_icontains: Union[Unset, str] = UNSET,
    uuid_iendswith: Union[Unset, str] = UNSET,
    uuid_iexact: Union[Unset, str] = UNSET,
    uuid_in: Union[Unset, list[str]] = UNSET,
    uuid_iregex: Union[Unset, str] = UNSET,
    uuid_isnull: Union[Unset, bool] = UNSET,
    uuid_istartswith: Union[Unset, str] = UNSET,
    uuid_lt: Union[Unset, str] = UNSET,
    uuid_lte: Union[Unset, str] = UNSET,
    uuid_range: Union[Unset, list[str]] = UNSET,
    uuid_regex: Union[Unset, str] = UNSET,
    uuid_startswith: Union[Unset, str] = UNSET,
    volume: Union[Unset, int] = UNSET,
    volume_contained_by: Union[Unset, int] = UNSET,
    volume_contains: Union[Unset, int] = UNSET,
    volume_endswith: Union[Unset, int] = UNSET,
    volume_gt: Union[Unset, int] = UNSET,
    volume_gte: Union[Unset, int] = UNSET,
    volume_icontains: Union[Unset, int] = UNSET,
    volume_iendswith: Union[Unset, int] = UNSET,
    volume_iexact: Union[Unset, int] = UNSET,
    volume_in: Union[Unset, list[int]] = UNSET,
    volume_iregex: Union[Unset, int] = UNSET,
    volume_isnull: Union[Unset, bool] = UNSET,
    volume_istartswith: Union[Unset, int] = UNSET,
    volume_lt: Union[Unset, int] = UNSET,
    volume_lte: Union[Unset, int] = UNSET,
    volume_range: Union[Unset, list[int]] = UNSET,
    volume_regex: Union[Unset, int] = UNSET,
    volume_startswith: Union[Unset, int] = UNSET,
) -> Response[PaginatedResultWriteList]:
    """Get a list of Result objects. Results have a 1:1 mapping with Observations.

    Args:
        curation_category (Union[Unset, ResultsListCEDACurationCategory]):
        curation_category_contains (Union[Unset, str]):
        curation_category_endswith (Union[Unset, str]):
        curation_category_gt (Union[Unset, str]):
        curation_category_gte (Union[Unset, str]):
        curation_category_icontains (Union[Unset, str]):
        curation_category_iendswith (Union[Unset, str]):
        curation_category_iexact (Union[Unset, str]):
        curation_category_in (Union[Unset, list[str]]):
        curation_category_iregex (Union[Unset, str]):
        curation_category_isnull (Union[Unset, bool]):
        curation_category_istartswith (Union[Unset, str]):
        curation_category_lt (Union[Unset, str]):
        curation_category_lte (Union[Unset, str]):
        curation_category_range (Union[Unset, list[str]]):
        curation_category_regex (Union[Unset, str]):
        curation_category_startswith (Union[Unset, str]):
        data_path (Union[Unset, str]):
        data_path_contains (Union[Unset, str]):
        data_path_endswith (Union[Unset, str]):
        data_path_gt (Union[Unset, str]):
        data_path_gte (Union[Unset, str]):
        data_path_icontains (Union[Unset, str]):
        data_path_iendswith (Union[Unset, str]):
        data_path_iexact (Union[Unset, str]):
        data_path_in (Union[Unset, list[str]]):
        data_path_iregex (Union[Unset, str]):
        data_path_isnull (Union[Unset, bool]):
        data_path_istartswith (Union[Unset, str]):
        data_path_lt (Union[Unset, str]):
        data_path_lte (Union[Unset, str]):
        data_path_range (Union[Unset, list[str]]):
        data_path_regex (Union[Unset, str]):
        data_path_startswith (Union[Unset, str]):
        file_format (Union[Unset, str]):
        file_format_contains (Union[Unset, str]):
        file_format_endswith (Union[Unset, str]):
        file_format_gt (Union[Unset, str]):
        file_format_gte (Union[Unset, str]):
        file_format_icontains (Union[Unset, str]):
        file_format_iendswith (Union[Unset, str]):
        file_format_iexact (Union[Unset, str]):
        file_format_in (Union[Unset, list[str]]):
        file_format_iregex (Union[Unset, str]):
        file_format_isnull (Union[Unset, bool]):
        file_format_istartswith (Union[Unset, str]):
        file_format_lt (Union[Unset, str]):
        file_format_lte (Union[Unset, str]):
        file_format_range (Union[Unset, list[str]]):
        file_format_regex (Union[Unset, str]):
        file_format_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        number_of_files (Union[Unset, int]):
        number_of_files_contained_by (Union[Unset, int]):
        number_of_files_contains (Union[Unset, int]):
        number_of_files_endswith (Union[Unset, int]):
        number_of_files_gt (Union[Unset, int]):
        number_of_files_gte (Union[Unset, int]):
        number_of_files_icontains (Union[Unset, int]):
        number_of_files_iendswith (Union[Unset, int]):
        number_of_files_iexact (Union[Unset, int]):
        number_of_files_in (Union[Unset, list[int]]):
        number_of_files_iregex (Union[Unset, int]):
        number_of_files_isnull (Union[Unset, bool]):
        number_of_files_istartswith (Union[Unset, int]):
        number_of_files_lt (Union[Unset, int]):
        number_of_files_lte (Union[Unset, int]):
        number_of_files_range (Union[Unset, list[int]]):
        number_of_files_regex (Union[Unset, int]):
        number_of_files_startswith (Union[Unset, int]):
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
        observation_ob_id (Union[Unset, int]):
        observation_ob_id_in (Union[Unset, list[int]]):
        observation_uuid (Union[Unset, str]):
        observation_uuid_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        referenceable_ptr (Union[Unset, int]):
        referenceable_ptr_gt (Union[Unset, int]):
        referenceable_ptr_gte (Union[Unset, int]):
        referenceable_ptr_in (Union[Unset, list[int]]):
        referenceable_ptr_isnull (Union[Unset, bool]):
        referenceable_ptr_lt (Union[Unset, int]):
        referenceable_ptr_lte (Union[Unset, int]):
        short_code (Union[Unset, str]):
        short_code_contains (Union[Unset, str]):
        short_code_endswith (Union[Unset, str]):
        short_code_gt (Union[Unset, str]):
        short_code_gte (Union[Unset, str]):
        short_code_icontains (Union[Unset, str]):
        short_code_iendswith (Union[Unset, str]):
        short_code_iexact (Union[Unset, str]):
        short_code_in (Union[Unset, list[str]]):
        short_code_iregex (Union[Unset, str]):
        short_code_isnull (Union[Unset, bool]):
        short_code_istartswith (Union[Unset, str]):
        short_code_lt (Union[Unset, str]):
        short_code_lte (Union[Unset, str]):
        short_code_range (Union[Unset, list[str]]):
        short_code_regex (Union[Unset, str]):
        short_code_startswith (Union[Unset, str]):
        storage_location (Union[Unset, ResultsListStorageLocation]):
        storage_location_contains (Union[Unset, str]):
        storage_location_endswith (Union[Unset, str]):
        storage_location_gt (Union[Unset, str]):
        storage_location_gte (Union[Unset, str]):
        storage_location_icontains (Union[Unset, str]):
        storage_location_iendswith (Union[Unset, str]):
        storage_location_iexact (Union[Unset, str]):
        storage_location_in (Union[Unset, list[str]]):
        storage_location_iregex (Union[Unset, str]):
        storage_location_isnull (Union[Unset, bool]):
        storage_location_istartswith (Union[Unset, str]):
        storage_location_lt (Union[Unset, str]):
        storage_location_lte (Union[Unset, str]):
        storage_location_range (Union[Unset, list[str]]):
        storage_location_regex (Union[Unset, str]):
        storage_location_startswith (Union[Unset, str]):
        storage_status (Union[Unset, ResultsListStorageStatus]):
        storage_status_contains (Union[Unset, str]):
        storage_status_endswith (Union[Unset, str]):
        storage_status_gt (Union[Unset, str]):
        storage_status_gte (Union[Unset, str]):
        storage_status_icontains (Union[Unset, str]):
        storage_status_iendswith (Union[Unset, str]):
        storage_status_iexact (Union[Unset, str]):
        storage_status_in (Union[Unset, list[str]]):
        storage_status_iregex (Union[Unset, str]):
        storage_status_isnull (Union[Unset, bool]):
        storage_status_istartswith (Union[Unset, str]):
        storage_status_lt (Union[Unset, str]):
        storage_status_lte (Union[Unset, str]):
        storage_status_range (Union[Unset, list[str]]):
        storage_status_regex (Union[Unset, str]):
        storage_status_startswith (Union[Unset, str]):
        uuid (Union[Unset, str]):
        uuid_contains (Union[Unset, str]):
        uuid_endswith (Union[Unset, str]):
        uuid_gt (Union[Unset, str]):
        uuid_gte (Union[Unset, str]):
        uuid_icontains (Union[Unset, str]):
        uuid_iendswith (Union[Unset, str]):
        uuid_iexact (Union[Unset, str]):
        uuid_in (Union[Unset, list[str]]):
        uuid_iregex (Union[Unset, str]):
        uuid_isnull (Union[Unset, bool]):
        uuid_istartswith (Union[Unset, str]):
        uuid_lt (Union[Unset, str]):
        uuid_lte (Union[Unset, str]):
        uuid_range (Union[Unset, list[str]]):
        uuid_regex (Union[Unset, str]):
        uuid_startswith (Union[Unset, str]):
        volume (Union[Unset, int]):
        volume_contained_by (Union[Unset, int]):
        volume_contains (Union[Unset, int]):
        volume_endswith (Union[Unset, int]):
        volume_gt (Union[Unset, int]):
        volume_gte (Union[Unset, int]):
        volume_icontains (Union[Unset, int]):
        volume_iendswith (Union[Unset, int]):
        volume_iexact (Union[Unset, int]):
        volume_in (Union[Unset, list[int]]):
        volume_iregex (Union[Unset, int]):
        volume_isnull (Union[Unset, bool]):
        volume_istartswith (Union[Unset, int]):
        volume_lt (Union[Unset, int]):
        volume_lte (Union[Unset, int]):
        volume_range (Union[Unset, list[int]]):
        volume_regex (Union[Unset, int]):
        volume_startswith (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedResultWriteList]
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
        limit=limit,
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
        observation_ob_id=observation_ob_id,
        observation_ob_id_in=observation_ob_id_in,
        observation_uuid=observation_uuid,
        observation_uuid_in=observation_uuid_in,
        offset=offset,
        ordering=ordering,
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
    curation_category: Union[Unset, ResultsListCEDACurationCategory] = UNSET,
    curation_category_contains: Union[Unset, str] = UNSET,
    curation_category_endswith: Union[Unset, str] = UNSET,
    curation_category_gt: Union[Unset, str] = UNSET,
    curation_category_gte: Union[Unset, str] = UNSET,
    curation_category_icontains: Union[Unset, str] = UNSET,
    curation_category_iendswith: Union[Unset, str] = UNSET,
    curation_category_iexact: Union[Unset, str] = UNSET,
    curation_category_in: Union[Unset, list[str]] = UNSET,
    curation_category_iregex: Union[Unset, str] = UNSET,
    curation_category_isnull: Union[Unset, bool] = UNSET,
    curation_category_istartswith: Union[Unset, str] = UNSET,
    curation_category_lt: Union[Unset, str] = UNSET,
    curation_category_lte: Union[Unset, str] = UNSET,
    curation_category_range: Union[Unset, list[str]] = UNSET,
    curation_category_regex: Union[Unset, str] = UNSET,
    curation_category_startswith: Union[Unset, str] = UNSET,
    data_path: Union[Unset, str] = UNSET,
    data_path_contains: Union[Unset, str] = UNSET,
    data_path_endswith: Union[Unset, str] = UNSET,
    data_path_gt: Union[Unset, str] = UNSET,
    data_path_gte: Union[Unset, str] = UNSET,
    data_path_icontains: Union[Unset, str] = UNSET,
    data_path_iendswith: Union[Unset, str] = UNSET,
    data_path_iexact: Union[Unset, str] = UNSET,
    data_path_in: Union[Unset, list[str]] = UNSET,
    data_path_iregex: Union[Unset, str] = UNSET,
    data_path_isnull: Union[Unset, bool] = UNSET,
    data_path_istartswith: Union[Unset, str] = UNSET,
    data_path_lt: Union[Unset, str] = UNSET,
    data_path_lte: Union[Unset, str] = UNSET,
    data_path_range: Union[Unset, list[str]] = UNSET,
    data_path_regex: Union[Unset, str] = UNSET,
    data_path_startswith: Union[Unset, str] = UNSET,
    file_format: Union[Unset, str] = UNSET,
    file_format_contains: Union[Unset, str] = UNSET,
    file_format_endswith: Union[Unset, str] = UNSET,
    file_format_gt: Union[Unset, str] = UNSET,
    file_format_gte: Union[Unset, str] = UNSET,
    file_format_icontains: Union[Unset, str] = UNSET,
    file_format_iendswith: Union[Unset, str] = UNSET,
    file_format_iexact: Union[Unset, str] = UNSET,
    file_format_in: Union[Unset, list[str]] = UNSET,
    file_format_iregex: Union[Unset, str] = UNSET,
    file_format_isnull: Union[Unset, bool] = UNSET,
    file_format_istartswith: Union[Unset, str] = UNSET,
    file_format_lt: Union[Unset, str] = UNSET,
    file_format_lte: Union[Unset, str] = UNSET,
    file_format_range: Union[Unset, list[str]] = UNSET,
    file_format_regex: Union[Unset, str] = UNSET,
    file_format_startswith: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
    number_of_files: Union[Unset, int] = UNSET,
    number_of_files_contained_by: Union[Unset, int] = UNSET,
    number_of_files_contains: Union[Unset, int] = UNSET,
    number_of_files_endswith: Union[Unset, int] = UNSET,
    number_of_files_gt: Union[Unset, int] = UNSET,
    number_of_files_gte: Union[Unset, int] = UNSET,
    number_of_files_icontains: Union[Unset, int] = UNSET,
    number_of_files_iendswith: Union[Unset, int] = UNSET,
    number_of_files_iexact: Union[Unset, int] = UNSET,
    number_of_files_in: Union[Unset, list[int]] = UNSET,
    number_of_files_iregex: Union[Unset, int] = UNSET,
    number_of_files_isnull: Union[Unset, bool] = UNSET,
    number_of_files_istartswith: Union[Unset, int] = UNSET,
    number_of_files_lt: Union[Unset, int] = UNSET,
    number_of_files_lte: Union[Unset, int] = UNSET,
    number_of_files_range: Union[Unset, list[int]] = UNSET,
    number_of_files_regex: Union[Unset, int] = UNSET,
    number_of_files_startswith: Union[Unset, int] = UNSET,
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
    observation_ob_id: Union[Unset, int] = UNSET,
    observation_ob_id_in: Union[Unset, list[int]] = UNSET,
    observation_uuid: Union[Unset, str] = UNSET,
    observation_uuid_in: Union[Unset, list[str]] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    referenceable_ptr: Union[Unset, int] = UNSET,
    referenceable_ptr_gt: Union[Unset, int] = UNSET,
    referenceable_ptr_gte: Union[Unset, int] = UNSET,
    referenceable_ptr_in: Union[Unset, list[int]] = UNSET,
    referenceable_ptr_isnull: Union[Unset, bool] = UNSET,
    referenceable_ptr_lt: Union[Unset, int] = UNSET,
    referenceable_ptr_lte: Union[Unset, int] = UNSET,
    short_code: Union[Unset, str] = UNSET,
    short_code_contains: Union[Unset, str] = UNSET,
    short_code_endswith: Union[Unset, str] = UNSET,
    short_code_gt: Union[Unset, str] = UNSET,
    short_code_gte: Union[Unset, str] = UNSET,
    short_code_icontains: Union[Unset, str] = UNSET,
    short_code_iendswith: Union[Unset, str] = UNSET,
    short_code_iexact: Union[Unset, str] = UNSET,
    short_code_in: Union[Unset, list[str]] = UNSET,
    short_code_iregex: Union[Unset, str] = UNSET,
    short_code_isnull: Union[Unset, bool] = UNSET,
    short_code_istartswith: Union[Unset, str] = UNSET,
    short_code_lt: Union[Unset, str] = UNSET,
    short_code_lte: Union[Unset, str] = UNSET,
    short_code_range: Union[Unset, list[str]] = UNSET,
    short_code_regex: Union[Unset, str] = UNSET,
    short_code_startswith: Union[Unset, str] = UNSET,
    storage_location: Union[Unset, ResultsListStorageLocation] = UNSET,
    storage_location_contains: Union[Unset, str] = UNSET,
    storage_location_endswith: Union[Unset, str] = UNSET,
    storage_location_gt: Union[Unset, str] = UNSET,
    storage_location_gte: Union[Unset, str] = UNSET,
    storage_location_icontains: Union[Unset, str] = UNSET,
    storage_location_iendswith: Union[Unset, str] = UNSET,
    storage_location_iexact: Union[Unset, str] = UNSET,
    storage_location_in: Union[Unset, list[str]] = UNSET,
    storage_location_iregex: Union[Unset, str] = UNSET,
    storage_location_isnull: Union[Unset, bool] = UNSET,
    storage_location_istartswith: Union[Unset, str] = UNSET,
    storage_location_lt: Union[Unset, str] = UNSET,
    storage_location_lte: Union[Unset, str] = UNSET,
    storage_location_range: Union[Unset, list[str]] = UNSET,
    storage_location_regex: Union[Unset, str] = UNSET,
    storage_location_startswith: Union[Unset, str] = UNSET,
    storage_status: Union[Unset, ResultsListStorageStatus] = UNSET,
    storage_status_contains: Union[Unset, str] = UNSET,
    storage_status_endswith: Union[Unset, str] = UNSET,
    storage_status_gt: Union[Unset, str] = UNSET,
    storage_status_gte: Union[Unset, str] = UNSET,
    storage_status_icontains: Union[Unset, str] = UNSET,
    storage_status_iendswith: Union[Unset, str] = UNSET,
    storage_status_iexact: Union[Unset, str] = UNSET,
    storage_status_in: Union[Unset, list[str]] = UNSET,
    storage_status_iregex: Union[Unset, str] = UNSET,
    storage_status_isnull: Union[Unset, bool] = UNSET,
    storage_status_istartswith: Union[Unset, str] = UNSET,
    storage_status_lt: Union[Unset, str] = UNSET,
    storage_status_lte: Union[Unset, str] = UNSET,
    storage_status_range: Union[Unset, list[str]] = UNSET,
    storage_status_regex: Union[Unset, str] = UNSET,
    storage_status_startswith: Union[Unset, str] = UNSET,
    uuid: Union[Unset, str] = UNSET,
    uuid_contains: Union[Unset, str] = UNSET,
    uuid_endswith: Union[Unset, str] = UNSET,
    uuid_gt: Union[Unset, str] = UNSET,
    uuid_gte: Union[Unset, str] = UNSET,
    uuid_icontains: Union[Unset, str] = UNSET,
    uuid_iendswith: Union[Unset, str] = UNSET,
    uuid_iexact: Union[Unset, str] = UNSET,
    uuid_in: Union[Unset, list[str]] = UNSET,
    uuid_iregex: Union[Unset, str] = UNSET,
    uuid_isnull: Union[Unset, bool] = UNSET,
    uuid_istartswith: Union[Unset, str] = UNSET,
    uuid_lt: Union[Unset, str] = UNSET,
    uuid_lte: Union[Unset, str] = UNSET,
    uuid_range: Union[Unset, list[str]] = UNSET,
    uuid_regex: Union[Unset, str] = UNSET,
    uuid_startswith: Union[Unset, str] = UNSET,
    volume: Union[Unset, int] = UNSET,
    volume_contained_by: Union[Unset, int] = UNSET,
    volume_contains: Union[Unset, int] = UNSET,
    volume_endswith: Union[Unset, int] = UNSET,
    volume_gt: Union[Unset, int] = UNSET,
    volume_gte: Union[Unset, int] = UNSET,
    volume_icontains: Union[Unset, int] = UNSET,
    volume_iendswith: Union[Unset, int] = UNSET,
    volume_iexact: Union[Unset, int] = UNSET,
    volume_in: Union[Unset, list[int]] = UNSET,
    volume_iregex: Union[Unset, int] = UNSET,
    volume_isnull: Union[Unset, bool] = UNSET,
    volume_istartswith: Union[Unset, int] = UNSET,
    volume_lt: Union[Unset, int] = UNSET,
    volume_lte: Union[Unset, int] = UNSET,
    volume_range: Union[Unset, list[int]] = UNSET,
    volume_regex: Union[Unset, int] = UNSET,
    volume_startswith: Union[Unset, int] = UNSET,
) -> Optional[PaginatedResultWriteList]:
    """Get a list of Result objects. Results have a 1:1 mapping with Observations.

    Args:
        curation_category (Union[Unset, ResultsListCEDACurationCategory]):
        curation_category_contains (Union[Unset, str]):
        curation_category_endswith (Union[Unset, str]):
        curation_category_gt (Union[Unset, str]):
        curation_category_gte (Union[Unset, str]):
        curation_category_icontains (Union[Unset, str]):
        curation_category_iendswith (Union[Unset, str]):
        curation_category_iexact (Union[Unset, str]):
        curation_category_in (Union[Unset, list[str]]):
        curation_category_iregex (Union[Unset, str]):
        curation_category_isnull (Union[Unset, bool]):
        curation_category_istartswith (Union[Unset, str]):
        curation_category_lt (Union[Unset, str]):
        curation_category_lte (Union[Unset, str]):
        curation_category_range (Union[Unset, list[str]]):
        curation_category_regex (Union[Unset, str]):
        curation_category_startswith (Union[Unset, str]):
        data_path (Union[Unset, str]):
        data_path_contains (Union[Unset, str]):
        data_path_endswith (Union[Unset, str]):
        data_path_gt (Union[Unset, str]):
        data_path_gte (Union[Unset, str]):
        data_path_icontains (Union[Unset, str]):
        data_path_iendswith (Union[Unset, str]):
        data_path_iexact (Union[Unset, str]):
        data_path_in (Union[Unset, list[str]]):
        data_path_iregex (Union[Unset, str]):
        data_path_isnull (Union[Unset, bool]):
        data_path_istartswith (Union[Unset, str]):
        data_path_lt (Union[Unset, str]):
        data_path_lte (Union[Unset, str]):
        data_path_range (Union[Unset, list[str]]):
        data_path_regex (Union[Unset, str]):
        data_path_startswith (Union[Unset, str]):
        file_format (Union[Unset, str]):
        file_format_contains (Union[Unset, str]):
        file_format_endswith (Union[Unset, str]):
        file_format_gt (Union[Unset, str]):
        file_format_gte (Union[Unset, str]):
        file_format_icontains (Union[Unset, str]):
        file_format_iendswith (Union[Unset, str]):
        file_format_iexact (Union[Unset, str]):
        file_format_in (Union[Unset, list[str]]):
        file_format_iregex (Union[Unset, str]):
        file_format_isnull (Union[Unset, bool]):
        file_format_istartswith (Union[Unset, str]):
        file_format_lt (Union[Unset, str]):
        file_format_lte (Union[Unset, str]):
        file_format_range (Union[Unset, list[str]]):
        file_format_regex (Union[Unset, str]):
        file_format_startswith (Union[Unset, str]):
        limit (Union[Unset, int]):
        number_of_files (Union[Unset, int]):
        number_of_files_contained_by (Union[Unset, int]):
        number_of_files_contains (Union[Unset, int]):
        number_of_files_endswith (Union[Unset, int]):
        number_of_files_gt (Union[Unset, int]):
        number_of_files_gte (Union[Unset, int]):
        number_of_files_icontains (Union[Unset, int]):
        number_of_files_iendswith (Union[Unset, int]):
        number_of_files_iexact (Union[Unset, int]):
        number_of_files_in (Union[Unset, list[int]]):
        number_of_files_iregex (Union[Unset, int]):
        number_of_files_isnull (Union[Unset, bool]):
        number_of_files_istartswith (Union[Unset, int]):
        number_of_files_lt (Union[Unset, int]):
        number_of_files_lte (Union[Unset, int]):
        number_of_files_range (Union[Unset, list[int]]):
        number_of_files_regex (Union[Unset, int]):
        number_of_files_startswith (Union[Unset, int]):
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
        observation_ob_id (Union[Unset, int]):
        observation_ob_id_in (Union[Unset, list[int]]):
        observation_uuid (Union[Unset, str]):
        observation_uuid_in (Union[Unset, list[str]]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        referenceable_ptr (Union[Unset, int]):
        referenceable_ptr_gt (Union[Unset, int]):
        referenceable_ptr_gte (Union[Unset, int]):
        referenceable_ptr_in (Union[Unset, list[int]]):
        referenceable_ptr_isnull (Union[Unset, bool]):
        referenceable_ptr_lt (Union[Unset, int]):
        referenceable_ptr_lte (Union[Unset, int]):
        short_code (Union[Unset, str]):
        short_code_contains (Union[Unset, str]):
        short_code_endswith (Union[Unset, str]):
        short_code_gt (Union[Unset, str]):
        short_code_gte (Union[Unset, str]):
        short_code_icontains (Union[Unset, str]):
        short_code_iendswith (Union[Unset, str]):
        short_code_iexact (Union[Unset, str]):
        short_code_in (Union[Unset, list[str]]):
        short_code_iregex (Union[Unset, str]):
        short_code_isnull (Union[Unset, bool]):
        short_code_istartswith (Union[Unset, str]):
        short_code_lt (Union[Unset, str]):
        short_code_lte (Union[Unset, str]):
        short_code_range (Union[Unset, list[str]]):
        short_code_regex (Union[Unset, str]):
        short_code_startswith (Union[Unset, str]):
        storage_location (Union[Unset, ResultsListStorageLocation]):
        storage_location_contains (Union[Unset, str]):
        storage_location_endswith (Union[Unset, str]):
        storage_location_gt (Union[Unset, str]):
        storage_location_gte (Union[Unset, str]):
        storage_location_icontains (Union[Unset, str]):
        storage_location_iendswith (Union[Unset, str]):
        storage_location_iexact (Union[Unset, str]):
        storage_location_in (Union[Unset, list[str]]):
        storage_location_iregex (Union[Unset, str]):
        storage_location_isnull (Union[Unset, bool]):
        storage_location_istartswith (Union[Unset, str]):
        storage_location_lt (Union[Unset, str]):
        storage_location_lte (Union[Unset, str]):
        storage_location_range (Union[Unset, list[str]]):
        storage_location_regex (Union[Unset, str]):
        storage_location_startswith (Union[Unset, str]):
        storage_status (Union[Unset, ResultsListStorageStatus]):
        storage_status_contains (Union[Unset, str]):
        storage_status_endswith (Union[Unset, str]):
        storage_status_gt (Union[Unset, str]):
        storage_status_gte (Union[Unset, str]):
        storage_status_icontains (Union[Unset, str]):
        storage_status_iendswith (Union[Unset, str]):
        storage_status_iexact (Union[Unset, str]):
        storage_status_in (Union[Unset, list[str]]):
        storage_status_iregex (Union[Unset, str]):
        storage_status_isnull (Union[Unset, bool]):
        storage_status_istartswith (Union[Unset, str]):
        storage_status_lt (Union[Unset, str]):
        storage_status_lte (Union[Unset, str]):
        storage_status_range (Union[Unset, list[str]]):
        storage_status_regex (Union[Unset, str]):
        storage_status_startswith (Union[Unset, str]):
        uuid (Union[Unset, str]):
        uuid_contains (Union[Unset, str]):
        uuid_endswith (Union[Unset, str]):
        uuid_gt (Union[Unset, str]):
        uuid_gte (Union[Unset, str]):
        uuid_icontains (Union[Unset, str]):
        uuid_iendswith (Union[Unset, str]):
        uuid_iexact (Union[Unset, str]):
        uuid_in (Union[Unset, list[str]]):
        uuid_iregex (Union[Unset, str]):
        uuid_isnull (Union[Unset, bool]):
        uuid_istartswith (Union[Unset, str]):
        uuid_lt (Union[Unset, str]):
        uuid_lte (Union[Unset, str]):
        uuid_range (Union[Unset, list[str]]):
        uuid_regex (Union[Unset, str]):
        uuid_startswith (Union[Unset, str]):
        volume (Union[Unset, int]):
        volume_contained_by (Union[Unset, int]):
        volume_contains (Union[Unset, int]):
        volume_endswith (Union[Unset, int]):
        volume_gt (Union[Unset, int]):
        volume_gte (Union[Unset, int]):
        volume_icontains (Union[Unset, int]):
        volume_iendswith (Union[Unset, int]):
        volume_iexact (Union[Unset, int]):
        volume_in (Union[Unset, list[int]]):
        volume_iregex (Union[Unset, int]):
        volume_isnull (Union[Unset, bool]):
        volume_istartswith (Union[Unset, int]):
        volume_lt (Union[Unset, int]):
        volume_lte (Union[Unset, int]):
        volume_range (Union[Unset, list[int]]):
        volume_regex (Union[Unset, int]):
        volume_startswith (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedResultWriteList
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
            limit=limit,
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
            observation_ob_id=observation_ob_id,
            observation_ob_id_in=observation_ob_id_in,
            observation_uuid=observation_uuid,
            observation_uuid_in=observation_uuid_in,
            offset=offset,
            ordering=ordering,
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
