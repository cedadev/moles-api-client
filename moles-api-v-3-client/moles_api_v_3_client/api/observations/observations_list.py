import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.observations_list_access_category import ObservationsListAccessCategory
from ...models.observations_list_data_status import ObservationsListDataStatus
from ...models.observations_list_data_update_frequency import ObservationsListDataUpdateFrequency
from ...models.observations_list_language import ObservationsListLanguage
from ...models.observations_list_publication_state import ObservationsListPublicationState
from ...models.observations_list_storage_location import ObservationsListStorageLocation
from ...models.observations_list_storage_status import ObservationsListStorageStatus
from ...models.paginated_observation_read_list import PaginatedObservationReadList
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
    creation_date: datetime.datetime | Unset = UNSET,
    creation_date_contained_by: datetime.datetime | Unset = UNSET,
    creation_date_contains: datetime.datetime | Unset = UNSET,
    creation_date_date: datetime.date | Unset = UNSET,
    creation_date_day: float | Unset = UNSET,
    creation_date_endswith: datetime.datetime | Unset = UNSET,
    creation_date_gt: datetime.datetime | Unset = UNSET,
    creation_date_gte: datetime.datetime | Unset = UNSET,
    creation_date_hour: float | Unset = UNSET,
    creation_date_icontains: datetime.datetime | Unset = UNSET,
    creation_date_iendswith: datetime.datetime | Unset = UNSET,
    creation_date_iexact: datetime.datetime | Unset = UNSET,
    creation_date_in: list[datetime.datetime] | Unset = UNSET,
    creation_date_iregex: datetime.datetime | Unset = UNSET,
    creation_date_isnull: bool | Unset = UNSET,
    creation_date_iso_week_day: float | Unset = UNSET,
    creation_date_iso_year: float | Unset = UNSET,
    creation_date_istartswith: datetime.datetime | Unset = UNSET,
    creation_date_lt: datetime.datetime | Unset = UNSET,
    creation_date_lte: datetime.datetime | Unset = UNSET,
    creation_date_minute: float | Unset = UNSET,
    creation_date_month: float | Unset = UNSET,
    creation_date_quarter: float | Unset = UNSET,
    creation_date_range: list[datetime.datetime] | Unset = UNSET,
    creation_date_regex: datetime.datetime | Unset = UNSET,
    creation_date_second: float | Unset = UNSET,
    creation_date_startswith: datetime.datetime | Unset = UNSET,
    creation_date_time: str | Unset = UNSET,
    creation_date_week: float | Unset = UNSET,
    creation_date_week_day: float | Unset = UNSET,
    creation_date_year: float | Unset = UNSET,
    data_lineage: str | Unset = UNSET,
    data_lineage_contains: str | Unset = UNSET,
    data_lineage_endswith: str | Unset = UNSET,
    data_lineage_gt: str | Unset = UNSET,
    data_lineage_gte: str | Unset = UNSET,
    data_lineage_icontains: str | Unset = UNSET,
    data_lineage_iendswith: str | Unset = UNSET,
    data_lineage_iexact: str | Unset = UNSET,
    data_lineage_in: list[str] | Unset = UNSET,
    data_lineage_iregex: str | Unset = UNSET,
    data_lineage_isnull: bool | Unset = UNSET,
    data_lineage_istartswith: str | Unset = UNSET,
    data_lineage_lt: str | Unset = UNSET,
    data_lineage_lte: str | Unset = UNSET,
    data_lineage_range: list[str] | Unset = UNSET,
    data_lineage_regex: str | Unset = UNSET,
    data_lineage_startswith: str | Unset = UNSET,
    data_published_time: datetime.datetime | Unset = UNSET,
    data_published_time_contained_by: datetime.datetime | Unset = UNSET,
    data_published_time_contains: datetime.datetime | Unset = UNSET,
    data_published_time_date: datetime.date | Unset = UNSET,
    data_published_time_day: float | Unset = UNSET,
    data_published_time_endswith: datetime.datetime | Unset = UNSET,
    data_published_time_gt: datetime.datetime | Unset = UNSET,
    data_published_time_gte: datetime.datetime | Unset = UNSET,
    data_published_time_hour: float | Unset = UNSET,
    data_published_time_icontains: datetime.datetime | Unset = UNSET,
    data_published_time_iendswith: datetime.datetime | Unset = UNSET,
    data_published_time_iexact: datetime.datetime | Unset = UNSET,
    data_published_time_in: list[datetime.datetime] | Unset = UNSET,
    data_published_time_iregex: datetime.datetime | Unset = UNSET,
    data_published_time_isnull: bool | Unset = UNSET,
    data_published_time_iso_week_day: float | Unset = UNSET,
    data_published_time_iso_year: float | Unset = UNSET,
    data_published_time_istartswith: datetime.datetime | Unset = UNSET,
    data_published_time_lt: datetime.datetime | Unset = UNSET,
    data_published_time_lte: datetime.datetime | Unset = UNSET,
    data_published_time_minute: float | Unset = UNSET,
    data_published_time_month: float | Unset = UNSET,
    data_published_time_quarter: float | Unset = UNSET,
    data_published_time_range: list[datetime.datetime] | Unset = UNSET,
    data_published_time_regex: datetime.datetime | Unset = UNSET,
    data_published_time_second: float | Unset = UNSET,
    data_published_time_startswith: datetime.datetime | Unset = UNSET,
    data_published_time_time: str | Unset = UNSET,
    data_published_time_week: float | Unset = UNSET,
    data_published_time_week_day: float | Unset = UNSET,
    data_published_time_year: float | Unset = UNSET,
    discovery_keywords_name: str | Unset = UNSET,
    discovery_keywords_name_contains: str | Unset = UNSET,
    doi_published_time: datetime.datetime | Unset = UNSET,
    doi_published_time_contained_by: datetime.datetime | Unset = UNSET,
    doi_published_time_contains: datetime.datetime | Unset = UNSET,
    doi_published_time_date: datetime.date | Unset = UNSET,
    doi_published_time_day: float | Unset = UNSET,
    doi_published_time_endswith: datetime.datetime | Unset = UNSET,
    doi_published_time_gt: datetime.datetime | Unset = UNSET,
    doi_published_time_gte: datetime.datetime | Unset = UNSET,
    doi_published_time_hour: float | Unset = UNSET,
    doi_published_time_icontains: datetime.datetime | Unset = UNSET,
    doi_published_time_iendswith: datetime.datetime | Unset = UNSET,
    doi_published_time_iexact: datetime.datetime | Unset = UNSET,
    doi_published_time_in: list[datetime.datetime] | Unset = UNSET,
    doi_published_time_iregex: datetime.datetime | Unset = UNSET,
    doi_published_time_isnull: bool | Unset = UNSET,
    doi_published_time_iso_week_day: float | Unset = UNSET,
    doi_published_time_iso_year: float | Unset = UNSET,
    doi_published_time_istartswith: datetime.datetime | Unset = UNSET,
    doi_published_time_lt: datetime.datetime | Unset = UNSET,
    doi_published_time_lte: datetime.datetime | Unset = UNSET,
    doi_published_time_minute: float | Unset = UNSET,
    doi_published_time_month: float | Unset = UNSET,
    doi_published_time_quarter: float | Unset = UNSET,
    doi_published_time_range: list[datetime.datetime] | Unset = UNSET,
    doi_published_time_regex: datetime.datetime | Unset = UNSET,
    doi_published_time_second: float | Unset = UNSET,
    doi_published_time_startswith: datetime.datetime | Unset = UNSET,
    doi_published_time_time: str | Unset = UNSET,
    doi_published_time_week: float | Unset = UNSET,
    doi_published_time_week_day: float | Unset = UNSET,
    doi_published_time_year: float | Unset = UNSET,
    dont_harvest_from_projects: bool | Unset = UNSET,
    dont_harvest_from_projects_contains: bool | Unset = UNSET,
    dont_harvest_from_projects_endswith: bool | Unset = UNSET,
    dont_harvest_from_projects_gt: bool | Unset = UNSET,
    dont_harvest_from_projects_gte: bool | Unset = UNSET,
    dont_harvest_from_projects_icontains: bool | Unset = UNSET,
    dont_harvest_from_projects_iendswith: bool | Unset = UNSET,
    dont_harvest_from_projects_iexact: bool | Unset = UNSET,
    dont_harvest_from_projects_in: list[bool] | Unset = UNSET,
    dont_harvest_from_projects_iregex: bool | Unset = UNSET,
    dont_harvest_from_projects_isnull: bool | Unset = UNSET,
    dont_harvest_from_projects_istartswith: bool | Unset = UNSET,
    dont_harvest_from_projects_lt: bool | Unset = UNSET,
    dont_harvest_from_projects_lte: bool | Unset = UNSET,
    dont_harvest_from_projects_range: list[bool] | Unset = UNSET,
    dont_harvest_from_projects_regex: bool | Unset = UNSET,
    dont_harvest_from_projects_startswith: bool | Unset = UNSET,
    feature_of_interest: str | Unset = UNSET,
    feature_of_interest_contains: str | Unset = UNSET,
    feature_of_interest_endswith: str | Unset = UNSET,
    feature_of_interest_gt: str | Unset = UNSET,
    feature_of_interest_gte: str | Unset = UNSET,
    feature_of_interest_icontains: str | Unset = UNSET,
    feature_of_interest_iendswith: str | Unset = UNSET,
    feature_of_interest_iexact: str | Unset = UNSET,
    feature_of_interest_in: list[str] | Unset = UNSET,
    feature_of_interest_iregex: str | Unset = UNSET,
    feature_of_interest_isnull: bool | Unset = UNSET,
    feature_of_interest_istartswith: str | Unset = UNSET,
    feature_of_interest_lt: str | Unset = UNSET,
    feature_of_interest_lte: str | Unset = UNSET,
    feature_of_interest_range: list[str] | Unset = UNSET,
    feature_of_interest_regex: str | Unset = UNSET,
    feature_of_interest_startswith: str | Unset = UNSET,
    geographic_extent: int | Unset = UNSET,
    geographic_extent_east_bound_longitude: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_gt: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_gte: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_lt: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_lte: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_range: list[float] | Unset = UNSET,
    geographic_extent_gt: int | Unset = UNSET,
    geographic_extent_gte: int | Unset = UNSET,
    geographic_extent_in: list[int] | Unset = UNSET,
    geographic_extent_isnull: bool | Unset = UNSET,
    geographic_extent_lt: int | Unset = UNSET,
    geographic_extent_lte: int | Unset = UNSET,
    geographic_extent_north_bound_latitude: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_gt: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_gte: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_lt: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_lte: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_range: list[float] | Unset = UNSET,
    geographic_extent_ob_id: int | Unset = UNSET,
    geographic_extent_ob_id_in: list[int] | Unset = UNSET,
    geographic_extent_south_bound_latitude: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_gt: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_gte: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_lt: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_lte: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_range: list[float] | Unset = UNSET,
    geographic_extent_west_bound_longitude: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_gt: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_gte: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_lt: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_lte: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_range: list[float] | Unset = UNSET,
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
    language: ObservationsListLanguage | Unset = UNSET,
    language_contains: str | Unset = UNSET,
    language_endswith: str | Unset = UNSET,
    language_gt: str | Unset = UNSET,
    language_gte: str | Unset = UNSET,
    language_icontains: str | Unset = UNSET,
    language_iendswith: str | Unset = UNSET,
    language_iexact: str | Unset = UNSET,
    language_in: list[str] | Unset = UNSET,
    language_iregex: str | Unset = UNSET,
    language_isnull: bool | Unset = UNSET,
    language_istartswith: str | Unset = UNSET,
    language_lt: str | Unset = UNSET,
    language_lte: str | Unset = UNSET,
    language_range: list[str] | Unset = UNSET,
    language_regex: str | Unset = UNSET,
    language_startswith: str | Unset = UNSET,
    last_updated_date: datetime.datetime | Unset = UNSET,
    last_updated_date_contained_by: datetime.datetime | Unset = UNSET,
    last_updated_date_contains: datetime.datetime | Unset = UNSET,
    last_updated_date_date: datetime.date | Unset = UNSET,
    last_updated_date_day: float | Unset = UNSET,
    last_updated_date_endswith: datetime.datetime | Unset = UNSET,
    last_updated_date_gt: datetime.datetime | Unset = UNSET,
    last_updated_date_gte: datetime.datetime | Unset = UNSET,
    last_updated_date_hour: float | Unset = UNSET,
    last_updated_date_icontains: datetime.datetime | Unset = UNSET,
    last_updated_date_iendswith: datetime.datetime | Unset = UNSET,
    last_updated_date_iexact: datetime.datetime | Unset = UNSET,
    last_updated_date_in: list[datetime.datetime] | Unset = UNSET,
    last_updated_date_iregex: datetime.datetime | Unset = UNSET,
    last_updated_date_isnull: bool | Unset = UNSET,
    last_updated_date_iso_week_day: float | Unset = UNSET,
    last_updated_date_iso_year: float | Unset = UNSET,
    last_updated_date_istartswith: datetime.datetime | Unset = UNSET,
    last_updated_date_lt: datetime.datetime | Unset = UNSET,
    last_updated_date_lte: datetime.datetime | Unset = UNSET,
    last_updated_date_minute: float | Unset = UNSET,
    last_updated_date_month: float | Unset = UNSET,
    last_updated_date_quarter: float | Unset = UNSET,
    last_updated_date_range: list[datetime.datetime] | Unset = UNSET,
    last_updated_date_regex: datetime.datetime | Unset = UNSET,
    last_updated_date_second: float | Unset = UNSET,
    last_updated_date_startswith: datetime.datetime | Unset = UNSET,
    last_updated_date_time: str | Unset = UNSET,
    last_updated_date_week: float | Unset = UNSET,
    last_updated_date_week_day: float | Unset = UNSET,
    last_updated_date_year: float | Unset = UNSET,
    latest_data_update_time: datetime.datetime | Unset = UNSET,
    latest_data_update_time_contained_by: datetime.datetime | Unset = UNSET,
    latest_data_update_time_contains: datetime.datetime | Unset = UNSET,
    latest_data_update_time_date: datetime.date | Unset = UNSET,
    latest_data_update_time_day: float | Unset = UNSET,
    latest_data_update_time_endswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_gt: datetime.datetime | Unset = UNSET,
    latest_data_update_time_gte: datetime.datetime | Unset = UNSET,
    latest_data_update_time_hour: float | Unset = UNSET,
    latest_data_update_time_icontains: datetime.datetime | Unset = UNSET,
    latest_data_update_time_iendswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_iexact: datetime.datetime | Unset = UNSET,
    latest_data_update_time_in: list[datetime.datetime] | Unset = UNSET,
    latest_data_update_time_iregex: datetime.datetime | Unset = UNSET,
    latest_data_update_time_isnull: bool | Unset = UNSET,
    latest_data_update_time_iso_week_day: float | Unset = UNSET,
    latest_data_update_time_iso_year: float | Unset = UNSET,
    latest_data_update_time_istartswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_lt: datetime.datetime | Unset = UNSET,
    latest_data_update_time_lte: datetime.datetime | Unset = UNSET,
    latest_data_update_time_minute: float | Unset = UNSET,
    latest_data_update_time_month: float | Unset = UNSET,
    latest_data_update_time_quarter: float | Unset = UNSET,
    latest_data_update_time_range: list[datetime.datetime] | Unset = UNSET,
    latest_data_update_time_regex: datetime.datetime | Unset = UNSET,
    latest_data_update_time_second: float | Unset = UNSET,
    latest_data_update_time_startswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_time: str | Unset = UNSET,
    latest_data_update_time_week: float | Unset = UNSET,
    latest_data_update_time_week_day: float | Unset = UNSET,
    latest_data_update_time_year: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    non_geographic_flag: bool | Unset = UNSET,
    non_geographic_flag_contains: bool | Unset = UNSET,
    non_geographic_flag_endswith: bool | Unset = UNSET,
    non_geographic_flag_gt: bool | Unset = UNSET,
    non_geographic_flag_gte: bool | Unset = UNSET,
    non_geographic_flag_icontains: bool | Unset = UNSET,
    non_geographic_flag_iendswith: bool | Unset = UNSET,
    non_geographic_flag_iexact: bool | Unset = UNSET,
    non_geographic_flag_in: list[bool] | Unset = UNSET,
    non_geographic_flag_iregex: bool | Unset = UNSET,
    non_geographic_flag_isnull: bool | Unset = UNSET,
    non_geographic_flag_istartswith: bool | Unset = UNSET,
    non_geographic_flag_lt: bool | Unset = UNSET,
    non_geographic_flag_lte: bool | Unset = UNSET,
    non_geographic_flag_range: list[bool] | Unset = UNSET,
    non_geographic_flag_regex: bool | Unset = UNSET,
    non_geographic_flag_startswith: bool | Unset = UNSET,
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
    permissions_access_category: ObservationsListAccessCategory | Unset = UNSET,
    permissions_access_category_in: list[str] | Unset = UNSET,
    permissions_access_roles: str | Unset = UNSET,
    permissions_access_roles_in: list[str] | Unset = UNSET,
    procedure_acquisition: int | Unset = UNSET,
    procedure_acquisition_gt: int | Unset = UNSET,
    procedure_acquisition_gte: int | Unset = UNSET,
    procedure_acquisition_in: list[int] | Unset = UNSET,
    procedure_acquisition_isnull: bool | Unset = UNSET,
    procedure_acquisition_lt: int | Unset = UNSET,
    procedure_acquisition_lte: int | Unset = UNSET,
    procedure_acquisition_ob_id: int | Unset = UNSET,
    procedure_acquisition_ob_id_in: list[int] | Unset = UNSET,
    procedure_acquisition_uuid: str | Unset = UNSET,
    procedure_acquisition_uuid_in: list[str] | Unset = UNSET,
    procedure_composite_process: int | Unset = UNSET,
    procedure_composite_process_gt: int | Unset = UNSET,
    procedure_composite_process_gte: int | Unset = UNSET,
    procedure_composite_process_in: list[int] | Unset = UNSET,
    procedure_composite_process_isnull: bool | Unset = UNSET,
    procedure_composite_process_lt: int | Unset = UNSET,
    procedure_composite_process_lte: int | Unset = UNSET,
    procedure_computation: int | Unset = UNSET,
    procedure_computation_gt: int | Unset = UNSET,
    procedure_computation_gte: int | Unset = UNSET,
    procedure_computation_in: list[int] | Unset = UNSET,
    procedure_computation_isnull: bool | Unset = UNSET,
    procedure_computation_lt: int | Unset = UNSET,
    procedure_computation_lte: int | Unset = UNSET,
    procedure_description: str | Unset = UNSET,
    procedure_description_contains: str | Unset = UNSET,
    procedure_description_endswith: str | Unset = UNSET,
    procedure_description_gt: str | Unset = UNSET,
    procedure_description_gte: str | Unset = UNSET,
    procedure_description_icontains: str | Unset = UNSET,
    procedure_description_iendswith: str | Unset = UNSET,
    procedure_description_iexact: str | Unset = UNSET,
    procedure_description_in: list[str] | Unset = UNSET,
    procedure_description_iregex: str | Unset = UNSET,
    procedure_description_isnull: bool | Unset = UNSET,
    procedure_description_istartswith: str | Unset = UNSET,
    procedure_description_lt: str | Unset = UNSET,
    procedure_description_lte: str | Unset = UNSET,
    procedure_description_range: list[str] | Unset = UNSET,
    procedure_description_regex: str | Unset = UNSET,
    procedure_description_startswith: str | Unset = UNSET,
    projects_ob_id: int | Unset = UNSET,
    projects_ob_id_in: list[int] | Unset = UNSET,
    projects_uuid: str | Unset = UNSET,
    projects_uuid_in: list[str] | Unset = UNSET,
    publication_state: ObservationsListPublicationState | Unset = UNSET,
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
    removed_data_reason: str | Unset = UNSET,
    removed_data_reason_contains: str | Unset = UNSET,
    removed_data_reason_endswith: str | Unset = UNSET,
    removed_data_reason_gt: str | Unset = UNSET,
    removed_data_reason_gte: str | Unset = UNSET,
    removed_data_reason_icontains: str | Unset = UNSET,
    removed_data_reason_iendswith: str | Unset = UNSET,
    removed_data_reason_iexact: str | Unset = UNSET,
    removed_data_reason_in: list[str] | Unset = UNSET,
    removed_data_reason_iregex: str | Unset = UNSET,
    removed_data_reason_isnull: bool | Unset = UNSET,
    removed_data_reason_istartswith: str | Unset = UNSET,
    removed_data_reason_lt: str | Unset = UNSET,
    removed_data_reason_lte: str | Unset = UNSET,
    removed_data_reason_range: list[str] | Unset = UNSET,
    removed_data_reason_regex: str | Unset = UNSET,
    removed_data_reason_startswith: str | Unset = UNSET,
    removed_data_time: datetime.datetime | Unset = UNSET,
    removed_data_time_contained_by: datetime.datetime | Unset = UNSET,
    removed_data_time_contains: datetime.datetime | Unset = UNSET,
    removed_data_time_date: datetime.date | Unset = UNSET,
    removed_data_time_day: float | Unset = UNSET,
    removed_data_time_endswith: datetime.datetime | Unset = UNSET,
    removed_data_time_gt: datetime.datetime | Unset = UNSET,
    removed_data_time_gte: datetime.datetime | Unset = UNSET,
    removed_data_time_hour: float | Unset = UNSET,
    removed_data_time_icontains: datetime.datetime | Unset = UNSET,
    removed_data_time_iendswith: datetime.datetime | Unset = UNSET,
    removed_data_time_iexact: datetime.datetime | Unset = UNSET,
    removed_data_time_in: list[datetime.datetime] | Unset = UNSET,
    removed_data_time_iregex: datetime.datetime | Unset = UNSET,
    removed_data_time_isnull: bool | Unset = UNSET,
    removed_data_time_iso_week_day: float | Unset = UNSET,
    removed_data_time_iso_year: float | Unset = UNSET,
    removed_data_time_istartswith: datetime.datetime | Unset = UNSET,
    removed_data_time_lt: datetime.datetime | Unset = UNSET,
    removed_data_time_lte: datetime.datetime | Unset = UNSET,
    removed_data_time_minute: float | Unset = UNSET,
    removed_data_time_month: float | Unset = UNSET,
    removed_data_time_quarter: float | Unset = UNSET,
    removed_data_time_range: list[datetime.datetime] | Unset = UNSET,
    removed_data_time_regex: datetime.datetime | Unset = UNSET,
    removed_data_time_second: float | Unset = UNSET,
    removed_data_time_startswith: datetime.datetime | Unset = UNSET,
    removed_data_time_time: str | Unset = UNSET,
    removed_data_time_week: float | Unset = UNSET,
    removed_data_time_week_day: float | Unset = UNSET,
    removed_data_time_year: float | Unset = UNSET,
    resolution: str | Unset = UNSET,
    resolution_contains: str | Unset = UNSET,
    resolution_endswith: str | Unset = UNSET,
    resolution_gt: str | Unset = UNSET,
    resolution_gte: str | Unset = UNSET,
    resolution_icontains: str | Unset = UNSET,
    resolution_iendswith: str | Unset = UNSET,
    resolution_iexact: str | Unset = UNSET,
    resolution_in: list[str] | Unset = UNSET,
    resolution_iregex: str | Unset = UNSET,
    resolution_isnull: bool | Unset = UNSET,
    resolution_istartswith: str | Unset = UNSET,
    resolution_lt: str | Unset = UNSET,
    resolution_lte: str | Unset = UNSET,
    resolution_range: list[str] | Unset = UNSET,
    resolution_regex: str | Unset = UNSET,
    resolution_startswith: str | Unset = UNSET,
    result_quality: int | Unset = UNSET,
    result_quality_date: datetime.date | Unset = UNSET,
    result_quality_date_gt: datetime.date | Unset = UNSET,
    result_quality_date_gte: datetime.date | Unset = UNSET,
    result_quality_date_lt: datetime.date | Unset = UNSET,
    result_quality_date_lte: datetime.date | Unset = UNSET,
    result_quality_date_range: list[datetime.date] | Unset = UNSET,
    result_quality_explanation: str | Unset = UNSET,
    result_quality_explanation_contains: str | Unset = UNSET,
    result_quality_gt: int | Unset = UNSET,
    result_quality_gte: int | Unset = UNSET,
    result_quality_in: list[int] | Unset = UNSET,
    result_quality_isnull: bool | Unset = UNSET,
    result_quality_lt: int | Unset = UNSET,
    result_quality_lte: int | Unset = UNSET,
    result_quality_ob_id: int | Unset = UNSET,
    result_quality_ob_id_in: list[int] | Unset = UNSET,
    result_quality_passes_test: bool | Unset = UNSET,
    result_quality_result_title: str | Unset = UNSET,
    result_quality_result_title_contains: str | Unset = UNSET,
    result_field: int | Unset = UNSET,
    result_field_data_path: str | Unset = UNSET,
    result_field_data_path_contains: str | Unset = UNSET,
    result_field_data_path_startswith: str | Unset = UNSET,
    result_field_file_format: str | Unset = UNSET,
    result_field_file_format_contains: str | Unset = UNSET,
    result_field_gt: int | Unset = UNSET,
    result_field_gte: int | Unset = UNSET,
    result_field_in: list[int] | Unset = UNSET,
    result_field_isnull: bool | Unset = UNSET,
    result_field_lt: int | Unset = UNSET,
    result_field_lte: int | Unset = UNSET,
    result_field_storage_location: ObservationsListStorageLocation | Unset = UNSET,
    result_field_storage_status: ObservationsListStorageStatus | Unset = UNSET,
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
    status: ObservationsListDataStatus | Unset = UNSET,
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
    submission_user_id: str | Unset = UNSET,
    submission_user_id_contains: str | Unset = UNSET,
    submission_user_id_endswith: str | Unset = UNSET,
    submission_user_id_gt: str | Unset = UNSET,
    submission_user_id_gte: str | Unset = UNSET,
    submission_user_id_icontains: str | Unset = UNSET,
    submission_user_id_iendswith: str | Unset = UNSET,
    submission_user_id_iexact: str | Unset = UNSET,
    submission_user_id_in: list[str] | Unset = UNSET,
    submission_user_id_iregex: str | Unset = UNSET,
    submission_user_id_isnull: bool | Unset = UNSET,
    submission_user_id_istartswith: str | Unset = UNSET,
    submission_user_id_lt: str | Unset = UNSET,
    submission_user_id_lte: str | Unset = UNSET,
    submission_user_id_range: list[str] | Unset = UNSET,
    submission_user_id_regex: str | Unset = UNSET,
    submission_user_id_startswith: str | Unset = UNSET,
    time_period: int | Unset = UNSET,
    time_period_end_time: datetime.datetime | Unset = UNSET,
    time_period_end_time_gt: datetime.datetime | Unset = UNSET,
    time_period_end_time_gte: datetime.datetime | Unset = UNSET,
    time_period_end_time_lt: datetime.datetime | Unset = UNSET,
    time_period_end_time_lte: datetime.datetime | Unset = UNSET,
    time_period_end_time_range: list[datetime.datetime] | Unset = UNSET,
    time_period_gt: int | Unset = UNSET,
    time_period_gte: int | Unset = UNSET,
    time_period_in: list[int] | Unset = UNSET,
    time_period_isnull: bool | Unset = UNSET,
    time_period_lt: int | Unset = UNSET,
    time_period_lte: int | Unset = UNSET,
    time_period_ob_id: int | Unset = UNSET,
    time_period_ob_id_in: list[int] | Unset = UNSET,
    time_period_start_time: datetime.datetime | Unset = UNSET,
    time_period_start_time_gt: datetime.datetime | Unset = UNSET,
    time_period_start_time_gte: datetime.datetime | Unset = UNSET,
    time_period_start_time_lt: datetime.datetime | Unset = UNSET,
    time_period_start_time_lte: datetime.datetime | Unset = UNSET,
    time_period_start_time_range: list[datetime.datetime] | Unset = UNSET,
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
    update_frequency: ObservationsListDataUpdateFrequency | Unset = UNSET,
    update_frequency_contains: str | Unset = UNSET,
    update_frequency_endswith: str | Unset = UNSET,
    update_frequency_gt: str | Unset = UNSET,
    update_frequency_gte: str | Unset = UNSET,
    update_frequency_icontains: str | Unset = UNSET,
    update_frequency_iendswith: str | Unset = UNSET,
    update_frequency_iexact: str | Unset = UNSET,
    update_frequency_in: list[str] | Unset = UNSET,
    update_frequency_iregex: str | Unset = UNSET,
    update_frequency_isnull: bool | Unset = UNSET,
    update_frequency_istartswith: str | Unset = UNSET,
    update_frequency_lt: str | Unset = UNSET,
    update_frequency_lte: str | Unset = UNSET,
    update_frequency_range: list[str] | Unset = UNSET,
    update_frequency_regex: str | Unset = UNSET,
    update_frequency_startswith: str | Unset = UNSET,
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
    valid_time_period: int | Unset = UNSET,
    valid_time_period_gt: int | Unset = UNSET,
    valid_time_period_gte: int | Unset = UNSET,
    valid_time_period_in: list[int] | Unset = UNSET,
    valid_time_period_isnull: bool | Unset = UNSET,
    valid_time_period_lt: int | Unset = UNSET,
    valid_time_period_lte: int | Unset = UNSET,
    vertical_extent: int | Unset = UNSET,
    vertical_extent_gt: int | Unset = UNSET,
    vertical_extent_gte: int | Unset = UNSET,
    vertical_extent_in: list[int] | Unset = UNSET,
    vertical_extent_isnull: bool | Unset = UNSET,
    vertical_extent_lt: int | Unset = UNSET,
    vertical_extent_lte: int | Unset = UNSET,
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

    json_creation_date: str | Unset = UNSET
    if not isinstance(creation_date, Unset):
        json_creation_date = creation_date.isoformat()
    params["creationDate"] = json_creation_date

    json_creation_date_contained_by: str | Unset = UNSET
    if not isinstance(creation_date_contained_by, Unset):
        json_creation_date_contained_by = creation_date_contained_by.isoformat()
    params["creationDate__contained_by"] = json_creation_date_contained_by

    json_creation_date_contains: str | Unset = UNSET
    if not isinstance(creation_date_contains, Unset):
        json_creation_date_contains = creation_date_contains.isoformat()
    params["creationDate__contains"] = json_creation_date_contains

    json_creation_date_date: str | Unset = UNSET
    if not isinstance(creation_date_date, Unset):
        json_creation_date_date = creation_date_date.isoformat()
    params["creationDate__date"] = json_creation_date_date

    params["creationDate__day"] = creation_date_day

    json_creation_date_endswith: str | Unset = UNSET
    if not isinstance(creation_date_endswith, Unset):
        json_creation_date_endswith = creation_date_endswith.isoformat()
    params["creationDate__endswith"] = json_creation_date_endswith

    json_creation_date_gt: str | Unset = UNSET
    if not isinstance(creation_date_gt, Unset):
        json_creation_date_gt = creation_date_gt.isoformat()
    params["creationDate__gt"] = json_creation_date_gt

    json_creation_date_gte: str | Unset = UNSET
    if not isinstance(creation_date_gte, Unset):
        json_creation_date_gte = creation_date_gte.isoformat()
    params["creationDate__gte"] = json_creation_date_gte

    params["creationDate__hour"] = creation_date_hour

    json_creation_date_icontains: str | Unset = UNSET
    if not isinstance(creation_date_icontains, Unset):
        json_creation_date_icontains = creation_date_icontains.isoformat()
    params["creationDate__icontains"] = json_creation_date_icontains

    json_creation_date_iendswith: str | Unset = UNSET
    if not isinstance(creation_date_iendswith, Unset):
        json_creation_date_iendswith = creation_date_iendswith.isoformat()
    params["creationDate__iendswith"] = json_creation_date_iendswith

    json_creation_date_iexact: str | Unset = UNSET
    if not isinstance(creation_date_iexact, Unset):
        json_creation_date_iexact = creation_date_iexact.isoformat()
    params["creationDate__iexact"] = json_creation_date_iexact

    json_creation_date_in: list[str] | Unset = UNSET
    if not isinstance(creation_date_in, Unset):
        json_creation_date_in = []
        for creation_date_in_item_data in creation_date_in:
            creation_date_in_item = creation_date_in_item_data.isoformat()
            json_creation_date_in.append(creation_date_in_item)

    params["creationDate__in"] = json_creation_date_in

    json_creation_date_iregex: str | Unset = UNSET
    if not isinstance(creation_date_iregex, Unset):
        json_creation_date_iregex = creation_date_iregex.isoformat()
    params["creationDate__iregex"] = json_creation_date_iregex

    params["creationDate__isnull"] = creation_date_isnull

    params["creationDate__iso_week_day"] = creation_date_iso_week_day

    params["creationDate__iso_year"] = creation_date_iso_year

    json_creation_date_istartswith: str | Unset = UNSET
    if not isinstance(creation_date_istartswith, Unset):
        json_creation_date_istartswith = creation_date_istartswith.isoformat()
    params["creationDate__istartswith"] = json_creation_date_istartswith

    json_creation_date_lt: str | Unset = UNSET
    if not isinstance(creation_date_lt, Unset):
        json_creation_date_lt = creation_date_lt.isoformat()
    params["creationDate__lt"] = json_creation_date_lt

    json_creation_date_lte: str | Unset = UNSET
    if not isinstance(creation_date_lte, Unset):
        json_creation_date_lte = creation_date_lte.isoformat()
    params["creationDate__lte"] = json_creation_date_lte

    params["creationDate__minute"] = creation_date_minute

    params["creationDate__month"] = creation_date_month

    params["creationDate__quarter"] = creation_date_quarter

    json_creation_date_range: list[str] | Unset = UNSET
    if not isinstance(creation_date_range, Unset):
        json_creation_date_range = []
        for creation_date_range_item_data in creation_date_range:
            creation_date_range_item = creation_date_range_item_data.isoformat()
            json_creation_date_range.append(creation_date_range_item)

    params["creationDate__range"] = json_creation_date_range

    json_creation_date_regex: str | Unset = UNSET
    if not isinstance(creation_date_regex, Unset):
        json_creation_date_regex = creation_date_regex.isoformat()
    params["creationDate__regex"] = json_creation_date_regex

    params["creationDate__second"] = creation_date_second

    json_creation_date_startswith: str | Unset = UNSET
    if not isinstance(creation_date_startswith, Unset):
        json_creation_date_startswith = creation_date_startswith.isoformat()
    params["creationDate__startswith"] = json_creation_date_startswith

    params["creationDate__time"] = creation_date_time

    params["creationDate__week"] = creation_date_week

    params["creationDate__week_day"] = creation_date_week_day

    params["creationDate__year"] = creation_date_year

    params["dataLineage"] = data_lineage

    params["dataLineage__contains"] = data_lineage_contains

    params["dataLineage__endswith"] = data_lineage_endswith

    params["dataLineage__gt"] = data_lineage_gt

    params["dataLineage__gte"] = data_lineage_gte

    params["dataLineage__icontains"] = data_lineage_icontains

    params["dataLineage__iendswith"] = data_lineage_iendswith

    params["dataLineage__iexact"] = data_lineage_iexact

    json_data_lineage_in: list[str] | Unset = UNSET
    if not isinstance(data_lineage_in, Unset):
        json_data_lineage_in = ",".join(map(str, data_lineage_in))

    params["dataLineage__in"] = json_data_lineage_in

    params["dataLineage__iregex"] = data_lineage_iregex

    params["dataLineage__isnull"] = data_lineage_isnull

    params["dataLineage__istartswith"] = data_lineage_istartswith

    params["dataLineage__lt"] = data_lineage_lt

    params["dataLineage__lte"] = data_lineage_lte

    json_data_lineage_range: list[str] | Unset = UNSET
    if not isinstance(data_lineage_range, Unset):
        json_data_lineage_range = ",".join(map(str, data_lineage_range))

    params["dataLineage__range"] = json_data_lineage_range

    params["dataLineage__regex"] = data_lineage_regex

    params["dataLineage__startswith"] = data_lineage_startswith

    json_data_published_time: str | Unset = UNSET
    if not isinstance(data_published_time, Unset):
        json_data_published_time = data_published_time.isoformat()
    params["dataPublishedTime"] = json_data_published_time

    json_data_published_time_contained_by: str | Unset = UNSET
    if not isinstance(data_published_time_contained_by, Unset):
        json_data_published_time_contained_by = data_published_time_contained_by.isoformat()
    params["dataPublishedTime__contained_by"] = json_data_published_time_contained_by

    json_data_published_time_contains: str | Unset = UNSET
    if not isinstance(data_published_time_contains, Unset):
        json_data_published_time_contains = data_published_time_contains.isoformat()
    params["dataPublishedTime__contains"] = json_data_published_time_contains

    json_data_published_time_date: str | Unset = UNSET
    if not isinstance(data_published_time_date, Unset):
        json_data_published_time_date = data_published_time_date.isoformat()
    params["dataPublishedTime__date"] = json_data_published_time_date

    params["dataPublishedTime__day"] = data_published_time_day

    json_data_published_time_endswith: str | Unset = UNSET
    if not isinstance(data_published_time_endswith, Unset):
        json_data_published_time_endswith = data_published_time_endswith.isoformat()
    params["dataPublishedTime__endswith"] = json_data_published_time_endswith

    json_data_published_time_gt: str | Unset = UNSET
    if not isinstance(data_published_time_gt, Unset):
        json_data_published_time_gt = data_published_time_gt.isoformat()
    params["dataPublishedTime__gt"] = json_data_published_time_gt

    json_data_published_time_gte: str | Unset = UNSET
    if not isinstance(data_published_time_gte, Unset):
        json_data_published_time_gte = data_published_time_gte.isoformat()
    params["dataPublishedTime__gte"] = json_data_published_time_gte

    params["dataPublishedTime__hour"] = data_published_time_hour

    json_data_published_time_icontains: str | Unset = UNSET
    if not isinstance(data_published_time_icontains, Unset):
        json_data_published_time_icontains = data_published_time_icontains.isoformat()
    params["dataPublishedTime__icontains"] = json_data_published_time_icontains

    json_data_published_time_iendswith: str | Unset = UNSET
    if not isinstance(data_published_time_iendswith, Unset):
        json_data_published_time_iendswith = data_published_time_iendswith.isoformat()
    params["dataPublishedTime__iendswith"] = json_data_published_time_iendswith

    json_data_published_time_iexact: str | Unset = UNSET
    if not isinstance(data_published_time_iexact, Unset):
        json_data_published_time_iexact = data_published_time_iexact.isoformat()
    params["dataPublishedTime__iexact"] = json_data_published_time_iexact

    json_data_published_time_in: list[str] | Unset = UNSET
    if not isinstance(data_published_time_in, Unset):
        json_data_published_time_in = []
        for data_published_time_in_item_data in data_published_time_in:
            data_published_time_in_item = data_published_time_in_item_data.isoformat()
            json_data_published_time_in.append(data_published_time_in_item)

    params["dataPublishedTime__in"] = json_data_published_time_in

    json_data_published_time_iregex: str | Unset = UNSET
    if not isinstance(data_published_time_iregex, Unset):
        json_data_published_time_iregex = data_published_time_iregex.isoformat()
    params["dataPublishedTime__iregex"] = json_data_published_time_iregex

    params["dataPublishedTime__isnull"] = data_published_time_isnull

    params["dataPublishedTime__iso_week_day"] = data_published_time_iso_week_day

    params["dataPublishedTime__iso_year"] = data_published_time_iso_year

    json_data_published_time_istartswith: str | Unset = UNSET
    if not isinstance(data_published_time_istartswith, Unset):
        json_data_published_time_istartswith = data_published_time_istartswith.isoformat()
    params["dataPublishedTime__istartswith"] = json_data_published_time_istartswith

    json_data_published_time_lt: str | Unset = UNSET
    if not isinstance(data_published_time_lt, Unset):
        json_data_published_time_lt = data_published_time_lt.isoformat()
    params["dataPublishedTime__lt"] = json_data_published_time_lt

    json_data_published_time_lte: str | Unset = UNSET
    if not isinstance(data_published_time_lte, Unset):
        json_data_published_time_lte = data_published_time_lte.isoformat()
    params["dataPublishedTime__lte"] = json_data_published_time_lte

    params["dataPublishedTime__minute"] = data_published_time_minute

    params["dataPublishedTime__month"] = data_published_time_month

    params["dataPublishedTime__quarter"] = data_published_time_quarter

    json_data_published_time_range: list[str] | Unset = UNSET
    if not isinstance(data_published_time_range, Unset):
        json_data_published_time_range = []
        for data_published_time_range_item_data in data_published_time_range:
            data_published_time_range_item = data_published_time_range_item_data.isoformat()
            json_data_published_time_range.append(data_published_time_range_item)

    params["dataPublishedTime__range"] = json_data_published_time_range

    json_data_published_time_regex: str | Unset = UNSET
    if not isinstance(data_published_time_regex, Unset):
        json_data_published_time_regex = data_published_time_regex.isoformat()
    params["dataPublishedTime__regex"] = json_data_published_time_regex

    params["dataPublishedTime__second"] = data_published_time_second

    json_data_published_time_startswith: str | Unset = UNSET
    if not isinstance(data_published_time_startswith, Unset):
        json_data_published_time_startswith = data_published_time_startswith.isoformat()
    params["dataPublishedTime__startswith"] = json_data_published_time_startswith

    params["dataPublishedTime__time"] = data_published_time_time

    params["dataPublishedTime__week"] = data_published_time_week

    params["dataPublishedTime__week_day"] = data_published_time_week_day

    params["dataPublishedTime__year"] = data_published_time_year

    params["discoveryKeywords__name"] = discovery_keywords_name

    params["discoveryKeywords__name__contains"] = discovery_keywords_name_contains

    json_doi_published_time: str | Unset = UNSET
    if not isinstance(doi_published_time, Unset):
        json_doi_published_time = doi_published_time.isoformat()
    params["doiPublishedTime"] = json_doi_published_time

    json_doi_published_time_contained_by: str | Unset = UNSET
    if not isinstance(doi_published_time_contained_by, Unset):
        json_doi_published_time_contained_by = doi_published_time_contained_by.isoformat()
    params["doiPublishedTime__contained_by"] = json_doi_published_time_contained_by

    json_doi_published_time_contains: str | Unset = UNSET
    if not isinstance(doi_published_time_contains, Unset):
        json_doi_published_time_contains = doi_published_time_contains.isoformat()
    params["doiPublishedTime__contains"] = json_doi_published_time_contains

    json_doi_published_time_date: str | Unset = UNSET
    if not isinstance(doi_published_time_date, Unset):
        json_doi_published_time_date = doi_published_time_date.isoformat()
    params["doiPublishedTime__date"] = json_doi_published_time_date

    params["doiPublishedTime__day"] = doi_published_time_day

    json_doi_published_time_endswith: str | Unset = UNSET
    if not isinstance(doi_published_time_endswith, Unset):
        json_doi_published_time_endswith = doi_published_time_endswith.isoformat()
    params["doiPublishedTime__endswith"] = json_doi_published_time_endswith

    json_doi_published_time_gt: str | Unset = UNSET
    if not isinstance(doi_published_time_gt, Unset):
        json_doi_published_time_gt = doi_published_time_gt.isoformat()
    params["doiPublishedTime__gt"] = json_doi_published_time_gt

    json_doi_published_time_gte: str | Unset = UNSET
    if not isinstance(doi_published_time_gte, Unset):
        json_doi_published_time_gte = doi_published_time_gte.isoformat()
    params["doiPublishedTime__gte"] = json_doi_published_time_gte

    params["doiPublishedTime__hour"] = doi_published_time_hour

    json_doi_published_time_icontains: str | Unset = UNSET
    if not isinstance(doi_published_time_icontains, Unset):
        json_doi_published_time_icontains = doi_published_time_icontains.isoformat()
    params["doiPublishedTime__icontains"] = json_doi_published_time_icontains

    json_doi_published_time_iendswith: str | Unset = UNSET
    if not isinstance(doi_published_time_iendswith, Unset):
        json_doi_published_time_iendswith = doi_published_time_iendswith.isoformat()
    params["doiPublishedTime__iendswith"] = json_doi_published_time_iendswith

    json_doi_published_time_iexact: str | Unset = UNSET
    if not isinstance(doi_published_time_iexact, Unset):
        json_doi_published_time_iexact = doi_published_time_iexact.isoformat()
    params["doiPublishedTime__iexact"] = json_doi_published_time_iexact

    json_doi_published_time_in: list[str] | Unset = UNSET
    if not isinstance(doi_published_time_in, Unset):
        json_doi_published_time_in = []
        for doi_published_time_in_item_data in doi_published_time_in:
            doi_published_time_in_item = doi_published_time_in_item_data.isoformat()
            json_doi_published_time_in.append(doi_published_time_in_item)

    params["doiPublishedTime__in"] = json_doi_published_time_in

    json_doi_published_time_iregex: str | Unset = UNSET
    if not isinstance(doi_published_time_iregex, Unset):
        json_doi_published_time_iregex = doi_published_time_iregex.isoformat()
    params["doiPublishedTime__iregex"] = json_doi_published_time_iregex

    params["doiPublishedTime__isnull"] = doi_published_time_isnull

    params["doiPublishedTime__iso_week_day"] = doi_published_time_iso_week_day

    params["doiPublishedTime__iso_year"] = doi_published_time_iso_year

    json_doi_published_time_istartswith: str | Unset = UNSET
    if not isinstance(doi_published_time_istartswith, Unset):
        json_doi_published_time_istartswith = doi_published_time_istartswith.isoformat()
    params["doiPublishedTime__istartswith"] = json_doi_published_time_istartswith

    json_doi_published_time_lt: str | Unset = UNSET
    if not isinstance(doi_published_time_lt, Unset):
        json_doi_published_time_lt = doi_published_time_lt.isoformat()
    params["doiPublishedTime__lt"] = json_doi_published_time_lt

    json_doi_published_time_lte: str | Unset = UNSET
    if not isinstance(doi_published_time_lte, Unset):
        json_doi_published_time_lte = doi_published_time_lte.isoformat()
    params["doiPublishedTime__lte"] = json_doi_published_time_lte

    params["doiPublishedTime__minute"] = doi_published_time_minute

    params["doiPublishedTime__month"] = doi_published_time_month

    params["doiPublishedTime__quarter"] = doi_published_time_quarter

    json_doi_published_time_range: list[str] | Unset = UNSET
    if not isinstance(doi_published_time_range, Unset):
        json_doi_published_time_range = []
        for doi_published_time_range_item_data in doi_published_time_range:
            doi_published_time_range_item = doi_published_time_range_item_data.isoformat()
            json_doi_published_time_range.append(doi_published_time_range_item)

    params["doiPublishedTime__range"] = json_doi_published_time_range

    json_doi_published_time_regex: str | Unset = UNSET
    if not isinstance(doi_published_time_regex, Unset):
        json_doi_published_time_regex = doi_published_time_regex.isoformat()
    params["doiPublishedTime__regex"] = json_doi_published_time_regex

    params["doiPublishedTime__second"] = doi_published_time_second

    json_doi_published_time_startswith: str | Unset = UNSET
    if not isinstance(doi_published_time_startswith, Unset):
        json_doi_published_time_startswith = doi_published_time_startswith.isoformat()
    params["doiPublishedTime__startswith"] = json_doi_published_time_startswith

    params["doiPublishedTime__time"] = doi_published_time_time

    params["doiPublishedTime__week"] = doi_published_time_week

    params["doiPublishedTime__week_day"] = doi_published_time_week_day

    params["doiPublishedTime__year"] = doi_published_time_year

    params["dontHarvestFromProjects"] = dont_harvest_from_projects

    params["dontHarvestFromProjects__contains"] = dont_harvest_from_projects_contains

    params["dontHarvestFromProjects__endswith"] = dont_harvest_from_projects_endswith

    params["dontHarvestFromProjects__gt"] = dont_harvest_from_projects_gt

    params["dontHarvestFromProjects__gte"] = dont_harvest_from_projects_gte

    params["dontHarvestFromProjects__icontains"] = dont_harvest_from_projects_icontains

    params["dontHarvestFromProjects__iendswith"] = dont_harvest_from_projects_iendswith

    params["dontHarvestFromProjects__iexact"] = dont_harvest_from_projects_iexact

    json_dont_harvest_from_projects_in: list[bool] | Unset = UNSET
    if not isinstance(dont_harvest_from_projects_in, Unset):
        json_dont_harvest_from_projects_in = ",".join(map(str, dont_harvest_from_projects_in))

    params["dontHarvestFromProjects__in"] = json_dont_harvest_from_projects_in

    params["dontHarvestFromProjects__iregex"] = dont_harvest_from_projects_iregex

    params["dontHarvestFromProjects__isnull"] = dont_harvest_from_projects_isnull

    params["dontHarvestFromProjects__istartswith"] = dont_harvest_from_projects_istartswith

    params["dontHarvestFromProjects__lt"] = dont_harvest_from_projects_lt

    params["dontHarvestFromProjects__lte"] = dont_harvest_from_projects_lte

    json_dont_harvest_from_projects_range: list[bool] | Unset = UNSET
    if not isinstance(dont_harvest_from_projects_range, Unset):
        json_dont_harvest_from_projects_range = ",".join(map(str, dont_harvest_from_projects_range))

    params["dontHarvestFromProjects__range"] = json_dont_harvest_from_projects_range

    params["dontHarvestFromProjects__regex"] = dont_harvest_from_projects_regex

    params["dontHarvestFromProjects__startswith"] = dont_harvest_from_projects_startswith

    params["featureOfInterest"] = feature_of_interest

    params["featureOfInterest__contains"] = feature_of_interest_contains

    params["featureOfInterest__endswith"] = feature_of_interest_endswith

    params["featureOfInterest__gt"] = feature_of_interest_gt

    params["featureOfInterest__gte"] = feature_of_interest_gte

    params["featureOfInterest__icontains"] = feature_of_interest_icontains

    params["featureOfInterest__iendswith"] = feature_of_interest_iendswith

    params["featureOfInterest__iexact"] = feature_of_interest_iexact

    json_feature_of_interest_in: list[str] | Unset = UNSET
    if not isinstance(feature_of_interest_in, Unset):
        json_feature_of_interest_in = ",".join(map(str, feature_of_interest_in))

    params["featureOfInterest__in"] = json_feature_of_interest_in

    params["featureOfInterest__iregex"] = feature_of_interest_iregex

    params["featureOfInterest__isnull"] = feature_of_interest_isnull

    params["featureOfInterest__istartswith"] = feature_of_interest_istartswith

    params["featureOfInterest__lt"] = feature_of_interest_lt

    params["featureOfInterest__lte"] = feature_of_interest_lte

    json_feature_of_interest_range: list[str] | Unset = UNSET
    if not isinstance(feature_of_interest_range, Unset):
        json_feature_of_interest_range = ",".join(map(str, feature_of_interest_range))

    params["featureOfInterest__range"] = json_feature_of_interest_range

    params["featureOfInterest__regex"] = feature_of_interest_regex

    params["featureOfInterest__startswith"] = feature_of_interest_startswith

    params["geographicExtent"] = geographic_extent

    params["geographicExtent__eastBoundLongitude"] = geographic_extent_east_bound_longitude

    params["geographicExtent__eastBoundLongitude__gt"] = geographic_extent_east_bound_longitude_gt

    params["geographicExtent__eastBoundLongitude__gte"] = geographic_extent_east_bound_longitude_gte

    params["geographicExtent__eastBoundLongitude__lt"] = geographic_extent_east_bound_longitude_lt

    params["geographicExtent__eastBoundLongitude__lte"] = geographic_extent_east_bound_longitude_lte

    json_geographic_extent_east_bound_longitude_range: list[float] | Unset = UNSET
    if not isinstance(geographic_extent_east_bound_longitude_range, Unset):
        json_geographic_extent_east_bound_longitude_range = ",".join(
            map(str, geographic_extent_east_bound_longitude_range)
        )

    params["geographicExtent__eastBoundLongitude__range"] = json_geographic_extent_east_bound_longitude_range

    params["geographicExtent__gt"] = geographic_extent_gt

    params["geographicExtent__gte"] = geographic_extent_gte

    json_geographic_extent_in: list[int] | Unset = UNSET
    if not isinstance(geographic_extent_in, Unset):
        json_geographic_extent_in = ",".join(map(str, geographic_extent_in))

    params["geographicExtent__in"] = json_geographic_extent_in

    params["geographicExtent__isnull"] = geographic_extent_isnull

    params["geographicExtent__lt"] = geographic_extent_lt

    params["geographicExtent__lte"] = geographic_extent_lte

    params["geographicExtent__northBoundLatitude"] = geographic_extent_north_bound_latitude

    params["geographicExtent__northBoundLatitude__gt"] = geographic_extent_north_bound_latitude_gt

    params["geographicExtent__northBoundLatitude__gte"] = geographic_extent_north_bound_latitude_gte

    params["geographicExtent__northBoundLatitude__lt"] = geographic_extent_north_bound_latitude_lt

    params["geographicExtent__northBoundLatitude__lte"] = geographic_extent_north_bound_latitude_lte

    json_geographic_extent_north_bound_latitude_range: list[float] | Unset = UNSET
    if not isinstance(geographic_extent_north_bound_latitude_range, Unset):
        json_geographic_extent_north_bound_latitude_range = ",".join(
            map(str, geographic_extent_north_bound_latitude_range)
        )

    params["geographicExtent__northBoundLatitude__range"] = json_geographic_extent_north_bound_latitude_range

    params["geographicExtent__ob_id"] = geographic_extent_ob_id

    json_geographic_extent_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(geographic_extent_ob_id_in, Unset):
        json_geographic_extent_ob_id_in = ",".join(map(str, geographic_extent_ob_id_in))

    params["geographicExtent__ob_id__in"] = json_geographic_extent_ob_id_in

    params["geographicExtent__southBoundLatitude"] = geographic_extent_south_bound_latitude

    params["geographicExtent__southBoundLatitude__gt"] = geographic_extent_south_bound_latitude_gt

    params["geographicExtent__southBoundLatitude__gte"] = geographic_extent_south_bound_latitude_gte

    params["geographicExtent__southBoundLatitude__lt"] = geographic_extent_south_bound_latitude_lt

    params["geographicExtent__southBoundLatitude__lte"] = geographic_extent_south_bound_latitude_lte

    json_geographic_extent_south_bound_latitude_range: list[float] | Unset = UNSET
    if not isinstance(geographic_extent_south_bound_latitude_range, Unset):
        json_geographic_extent_south_bound_latitude_range = ",".join(
            map(str, geographic_extent_south_bound_latitude_range)
        )

    params["geographicExtent__southBoundLatitude__range"] = json_geographic_extent_south_bound_latitude_range

    params["geographicExtent__westBoundLongitude"] = geographic_extent_west_bound_longitude

    params["geographicExtent__westBoundLongitude__gt"] = geographic_extent_west_bound_longitude_gt

    params["geographicExtent__westBoundLongitude__gte"] = geographic_extent_west_bound_longitude_gte

    params["geographicExtent__westBoundLongitude__lt"] = geographic_extent_west_bound_longitude_lt

    params["geographicExtent__westBoundLongitude__lte"] = geographic_extent_west_bound_longitude_lte

    json_geographic_extent_west_bound_longitude_range: list[float] | Unset = UNSET
    if not isinstance(geographic_extent_west_bound_longitude_range, Unset):
        json_geographic_extent_west_bound_longitude_range = ",".join(
            map(str, geographic_extent_west_bound_longitude_range)
        )

    params["geographicExtent__westBoundLongitude__range"] = json_geographic_extent_west_bound_longitude_range

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

    json_language: str | Unset = UNSET
    if not isinstance(language, Unset):
        json_language = language.value

    params["language"] = json_language

    params["language__contains"] = language_contains

    params["language__endswith"] = language_endswith

    params["language__gt"] = language_gt

    params["language__gte"] = language_gte

    params["language__icontains"] = language_icontains

    params["language__iendswith"] = language_iendswith

    params["language__iexact"] = language_iexact

    json_language_in: list[str] | Unset = UNSET
    if not isinstance(language_in, Unset):
        json_language_in = ",".join(map(str, language_in))

    params["language__in"] = json_language_in

    params["language__iregex"] = language_iregex

    params["language__isnull"] = language_isnull

    params["language__istartswith"] = language_istartswith

    params["language__lt"] = language_lt

    params["language__lte"] = language_lte

    json_language_range: list[str] | Unset = UNSET
    if not isinstance(language_range, Unset):
        json_language_range = ",".join(map(str, language_range))

    params["language__range"] = json_language_range

    params["language__regex"] = language_regex

    params["language__startswith"] = language_startswith

    json_last_updated_date: str | Unset = UNSET
    if not isinstance(last_updated_date, Unset):
        json_last_updated_date = last_updated_date.isoformat()
    params["lastUpdatedDate"] = json_last_updated_date

    json_last_updated_date_contained_by: str | Unset = UNSET
    if not isinstance(last_updated_date_contained_by, Unset):
        json_last_updated_date_contained_by = last_updated_date_contained_by.isoformat()
    params["lastUpdatedDate__contained_by"] = json_last_updated_date_contained_by

    json_last_updated_date_contains: str | Unset = UNSET
    if not isinstance(last_updated_date_contains, Unset):
        json_last_updated_date_contains = last_updated_date_contains.isoformat()
    params["lastUpdatedDate__contains"] = json_last_updated_date_contains

    json_last_updated_date_date: str | Unset = UNSET
    if not isinstance(last_updated_date_date, Unset):
        json_last_updated_date_date = last_updated_date_date.isoformat()
    params["lastUpdatedDate__date"] = json_last_updated_date_date

    params["lastUpdatedDate__day"] = last_updated_date_day

    json_last_updated_date_endswith: str | Unset = UNSET
    if not isinstance(last_updated_date_endswith, Unset):
        json_last_updated_date_endswith = last_updated_date_endswith.isoformat()
    params["lastUpdatedDate__endswith"] = json_last_updated_date_endswith

    json_last_updated_date_gt: str | Unset = UNSET
    if not isinstance(last_updated_date_gt, Unset):
        json_last_updated_date_gt = last_updated_date_gt.isoformat()
    params["lastUpdatedDate__gt"] = json_last_updated_date_gt

    json_last_updated_date_gte: str | Unset = UNSET
    if not isinstance(last_updated_date_gte, Unset):
        json_last_updated_date_gte = last_updated_date_gte.isoformat()
    params["lastUpdatedDate__gte"] = json_last_updated_date_gte

    params["lastUpdatedDate__hour"] = last_updated_date_hour

    json_last_updated_date_icontains: str | Unset = UNSET
    if not isinstance(last_updated_date_icontains, Unset):
        json_last_updated_date_icontains = last_updated_date_icontains.isoformat()
    params["lastUpdatedDate__icontains"] = json_last_updated_date_icontains

    json_last_updated_date_iendswith: str | Unset = UNSET
    if not isinstance(last_updated_date_iendswith, Unset):
        json_last_updated_date_iendswith = last_updated_date_iendswith.isoformat()
    params["lastUpdatedDate__iendswith"] = json_last_updated_date_iendswith

    json_last_updated_date_iexact: str | Unset = UNSET
    if not isinstance(last_updated_date_iexact, Unset):
        json_last_updated_date_iexact = last_updated_date_iexact.isoformat()
    params["lastUpdatedDate__iexact"] = json_last_updated_date_iexact

    json_last_updated_date_in: list[str] | Unset = UNSET
    if not isinstance(last_updated_date_in, Unset):
        json_last_updated_date_in = []
        for last_updated_date_in_item_data in last_updated_date_in:
            last_updated_date_in_item = last_updated_date_in_item_data.isoformat()
            json_last_updated_date_in.append(last_updated_date_in_item)

    params["lastUpdatedDate__in"] = json_last_updated_date_in

    json_last_updated_date_iregex: str | Unset = UNSET
    if not isinstance(last_updated_date_iregex, Unset):
        json_last_updated_date_iregex = last_updated_date_iregex.isoformat()
    params["lastUpdatedDate__iregex"] = json_last_updated_date_iregex

    params["lastUpdatedDate__isnull"] = last_updated_date_isnull

    params["lastUpdatedDate__iso_week_day"] = last_updated_date_iso_week_day

    params["lastUpdatedDate__iso_year"] = last_updated_date_iso_year

    json_last_updated_date_istartswith: str | Unset = UNSET
    if not isinstance(last_updated_date_istartswith, Unset):
        json_last_updated_date_istartswith = last_updated_date_istartswith.isoformat()
    params["lastUpdatedDate__istartswith"] = json_last_updated_date_istartswith

    json_last_updated_date_lt: str | Unset = UNSET
    if not isinstance(last_updated_date_lt, Unset):
        json_last_updated_date_lt = last_updated_date_lt.isoformat()
    params["lastUpdatedDate__lt"] = json_last_updated_date_lt

    json_last_updated_date_lte: str | Unset = UNSET
    if not isinstance(last_updated_date_lte, Unset):
        json_last_updated_date_lte = last_updated_date_lte.isoformat()
    params["lastUpdatedDate__lte"] = json_last_updated_date_lte

    params["lastUpdatedDate__minute"] = last_updated_date_minute

    params["lastUpdatedDate__month"] = last_updated_date_month

    params["lastUpdatedDate__quarter"] = last_updated_date_quarter

    json_last_updated_date_range: list[str] | Unset = UNSET
    if not isinstance(last_updated_date_range, Unset):
        json_last_updated_date_range = []
        for last_updated_date_range_item_data in last_updated_date_range:
            last_updated_date_range_item = last_updated_date_range_item_data.isoformat()
            json_last_updated_date_range.append(last_updated_date_range_item)

    params["lastUpdatedDate__range"] = json_last_updated_date_range

    json_last_updated_date_regex: str | Unset = UNSET
    if not isinstance(last_updated_date_regex, Unset):
        json_last_updated_date_regex = last_updated_date_regex.isoformat()
    params["lastUpdatedDate__regex"] = json_last_updated_date_regex

    params["lastUpdatedDate__second"] = last_updated_date_second

    json_last_updated_date_startswith: str | Unset = UNSET
    if not isinstance(last_updated_date_startswith, Unset):
        json_last_updated_date_startswith = last_updated_date_startswith.isoformat()
    params["lastUpdatedDate__startswith"] = json_last_updated_date_startswith

    params["lastUpdatedDate__time"] = last_updated_date_time

    params["lastUpdatedDate__week"] = last_updated_date_week

    params["lastUpdatedDate__week_day"] = last_updated_date_week_day

    params["lastUpdatedDate__year"] = last_updated_date_year

    json_latest_data_update_time: str | Unset = UNSET
    if not isinstance(latest_data_update_time, Unset):
        json_latest_data_update_time = latest_data_update_time.isoformat()
    params["latestDataUpdateTime"] = json_latest_data_update_time

    json_latest_data_update_time_contained_by: str | Unset = UNSET
    if not isinstance(latest_data_update_time_contained_by, Unset):
        json_latest_data_update_time_contained_by = latest_data_update_time_contained_by.isoformat()
    params["latestDataUpdateTime__contained_by"] = json_latest_data_update_time_contained_by

    json_latest_data_update_time_contains: str | Unset = UNSET
    if not isinstance(latest_data_update_time_contains, Unset):
        json_latest_data_update_time_contains = latest_data_update_time_contains.isoformat()
    params["latestDataUpdateTime__contains"] = json_latest_data_update_time_contains

    json_latest_data_update_time_date: str | Unset = UNSET
    if not isinstance(latest_data_update_time_date, Unset):
        json_latest_data_update_time_date = latest_data_update_time_date.isoformat()
    params["latestDataUpdateTime__date"] = json_latest_data_update_time_date

    params["latestDataUpdateTime__day"] = latest_data_update_time_day

    json_latest_data_update_time_endswith: str | Unset = UNSET
    if not isinstance(latest_data_update_time_endswith, Unset):
        json_latest_data_update_time_endswith = latest_data_update_time_endswith.isoformat()
    params["latestDataUpdateTime__endswith"] = json_latest_data_update_time_endswith

    json_latest_data_update_time_gt: str | Unset = UNSET
    if not isinstance(latest_data_update_time_gt, Unset):
        json_latest_data_update_time_gt = latest_data_update_time_gt.isoformat()
    params["latestDataUpdateTime__gt"] = json_latest_data_update_time_gt

    json_latest_data_update_time_gte: str | Unset = UNSET
    if not isinstance(latest_data_update_time_gte, Unset):
        json_latest_data_update_time_gte = latest_data_update_time_gte.isoformat()
    params["latestDataUpdateTime__gte"] = json_latest_data_update_time_gte

    params["latestDataUpdateTime__hour"] = latest_data_update_time_hour

    json_latest_data_update_time_icontains: str | Unset = UNSET
    if not isinstance(latest_data_update_time_icontains, Unset):
        json_latest_data_update_time_icontains = latest_data_update_time_icontains.isoformat()
    params["latestDataUpdateTime__icontains"] = json_latest_data_update_time_icontains

    json_latest_data_update_time_iendswith: str | Unset = UNSET
    if not isinstance(latest_data_update_time_iendswith, Unset):
        json_latest_data_update_time_iendswith = latest_data_update_time_iendswith.isoformat()
    params["latestDataUpdateTime__iendswith"] = json_latest_data_update_time_iendswith

    json_latest_data_update_time_iexact: str | Unset = UNSET
    if not isinstance(latest_data_update_time_iexact, Unset):
        json_latest_data_update_time_iexact = latest_data_update_time_iexact.isoformat()
    params["latestDataUpdateTime__iexact"] = json_latest_data_update_time_iexact

    json_latest_data_update_time_in: list[str] | Unset = UNSET
    if not isinstance(latest_data_update_time_in, Unset):
        json_latest_data_update_time_in = []
        for latest_data_update_time_in_item_data in latest_data_update_time_in:
            latest_data_update_time_in_item = latest_data_update_time_in_item_data.isoformat()
            json_latest_data_update_time_in.append(latest_data_update_time_in_item)

    params["latestDataUpdateTime__in"] = json_latest_data_update_time_in

    json_latest_data_update_time_iregex: str | Unset = UNSET
    if not isinstance(latest_data_update_time_iregex, Unset):
        json_latest_data_update_time_iregex = latest_data_update_time_iregex.isoformat()
    params["latestDataUpdateTime__iregex"] = json_latest_data_update_time_iregex

    params["latestDataUpdateTime__isnull"] = latest_data_update_time_isnull

    params["latestDataUpdateTime__iso_week_day"] = latest_data_update_time_iso_week_day

    params["latestDataUpdateTime__iso_year"] = latest_data_update_time_iso_year

    json_latest_data_update_time_istartswith: str | Unset = UNSET
    if not isinstance(latest_data_update_time_istartswith, Unset):
        json_latest_data_update_time_istartswith = latest_data_update_time_istartswith.isoformat()
    params["latestDataUpdateTime__istartswith"] = json_latest_data_update_time_istartswith

    json_latest_data_update_time_lt: str | Unset = UNSET
    if not isinstance(latest_data_update_time_lt, Unset):
        json_latest_data_update_time_lt = latest_data_update_time_lt.isoformat()
    params["latestDataUpdateTime__lt"] = json_latest_data_update_time_lt

    json_latest_data_update_time_lte: str | Unset = UNSET
    if not isinstance(latest_data_update_time_lte, Unset):
        json_latest_data_update_time_lte = latest_data_update_time_lte.isoformat()
    params["latestDataUpdateTime__lte"] = json_latest_data_update_time_lte

    params["latestDataUpdateTime__minute"] = latest_data_update_time_minute

    params["latestDataUpdateTime__month"] = latest_data_update_time_month

    params["latestDataUpdateTime__quarter"] = latest_data_update_time_quarter

    json_latest_data_update_time_range: list[str] | Unset = UNSET
    if not isinstance(latest_data_update_time_range, Unset):
        json_latest_data_update_time_range = []
        for latest_data_update_time_range_item_data in latest_data_update_time_range:
            latest_data_update_time_range_item = latest_data_update_time_range_item_data.isoformat()
            json_latest_data_update_time_range.append(latest_data_update_time_range_item)

    params["latestDataUpdateTime__range"] = json_latest_data_update_time_range

    json_latest_data_update_time_regex: str | Unset = UNSET
    if not isinstance(latest_data_update_time_regex, Unset):
        json_latest_data_update_time_regex = latest_data_update_time_regex.isoformat()
    params["latestDataUpdateTime__regex"] = json_latest_data_update_time_regex

    params["latestDataUpdateTime__second"] = latest_data_update_time_second

    json_latest_data_update_time_startswith: str | Unset = UNSET
    if not isinstance(latest_data_update_time_startswith, Unset):
        json_latest_data_update_time_startswith = latest_data_update_time_startswith.isoformat()
    params["latestDataUpdateTime__startswith"] = json_latest_data_update_time_startswith

    params["latestDataUpdateTime__time"] = latest_data_update_time_time

    params["latestDataUpdateTime__week"] = latest_data_update_time_week

    params["latestDataUpdateTime__week_day"] = latest_data_update_time_week_day

    params["latestDataUpdateTime__year"] = latest_data_update_time_year

    params["limit"] = limit

    params["nonGeographicFlag"] = non_geographic_flag

    params["nonGeographicFlag__contains"] = non_geographic_flag_contains

    params["nonGeographicFlag__endswith"] = non_geographic_flag_endswith

    params["nonGeographicFlag__gt"] = non_geographic_flag_gt

    params["nonGeographicFlag__gte"] = non_geographic_flag_gte

    params["nonGeographicFlag__icontains"] = non_geographic_flag_icontains

    params["nonGeographicFlag__iendswith"] = non_geographic_flag_iendswith

    params["nonGeographicFlag__iexact"] = non_geographic_flag_iexact

    json_non_geographic_flag_in: list[bool] | Unset = UNSET
    if not isinstance(non_geographic_flag_in, Unset):
        json_non_geographic_flag_in = ",".join(map(str, non_geographic_flag_in))

    params["nonGeographicFlag__in"] = json_non_geographic_flag_in

    params["nonGeographicFlag__iregex"] = non_geographic_flag_iregex

    params["nonGeographicFlag__isnull"] = non_geographic_flag_isnull

    params["nonGeographicFlag__istartswith"] = non_geographic_flag_istartswith

    params["nonGeographicFlag__lt"] = non_geographic_flag_lt

    params["nonGeographicFlag__lte"] = non_geographic_flag_lte

    json_non_geographic_flag_range: list[bool] | Unset = UNSET
    if not isinstance(non_geographic_flag_range, Unset):
        json_non_geographic_flag_range = ",".join(map(str, non_geographic_flag_range))

    params["nonGeographicFlag__range"] = json_non_geographic_flag_range

    params["nonGeographicFlag__regex"] = non_geographic_flag_regex

    params["nonGeographicFlag__startswith"] = non_geographic_flag_startswith

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

    params["offset"] = offset

    params["ordering"] = ordering

    json_permissions_access_category: str | Unset = UNSET
    if not isinstance(permissions_access_category, Unset):
        json_permissions_access_category = permissions_access_category.value

    params["permissions__accessCategory"] = json_permissions_access_category

    json_permissions_access_category_in: list[str] | Unset = UNSET
    if not isinstance(permissions_access_category_in, Unset):
        json_permissions_access_category_in = ",".join(map(str, permissions_access_category_in))

    params["permissions__accessCategory__in"] = json_permissions_access_category_in

    params["permissions__accessRoles"] = permissions_access_roles

    json_permissions_access_roles_in: list[str] | Unset = UNSET
    if not isinstance(permissions_access_roles_in, Unset):
        json_permissions_access_roles_in = ",".join(map(str, permissions_access_roles_in))

    params["permissions__accessRoles__in"] = json_permissions_access_roles_in

    params["procedureAcquisition"] = procedure_acquisition

    params["procedureAcquisition__gt"] = procedure_acquisition_gt

    params["procedureAcquisition__gte"] = procedure_acquisition_gte

    json_procedure_acquisition_in: list[int] | Unset = UNSET
    if not isinstance(procedure_acquisition_in, Unset):
        json_procedure_acquisition_in = ",".join(map(str, procedure_acquisition_in))

    params["procedureAcquisition__in"] = json_procedure_acquisition_in

    params["procedureAcquisition__isnull"] = procedure_acquisition_isnull

    params["procedureAcquisition__lt"] = procedure_acquisition_lt

    params["procedureAcquisition__lte"] = procedure_acquisition_lte

    params["procedureAcquisition__ob_id"] = procedure_acquisition_ob_id

    json_procedure_acquisition_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(procedure_acquisition_ob_id_in, Unset):
        json_procedure_acquisition_ob_id_in = ",".join(map(str, procedure_acquisition_ob_id_in))

    params["procedureAcquisition__ob_id__in"] = json_procedure_acquisition_ob_id_in

    params["procedureAcquisition__uuid"] = procedure_acquisition_uuid

    json_procedure_acquisition_uuid_in: list[str] | Unset = UNSET
    if not isinstance(procedure_acquisition_uuid_in, Unset):
        json_procedure_acquisition_uuid_in = ",".join(map(str, procedure_acquisition_uuid_in))

    params["procedureAcquisition__uuid__in"] = json_procedure_acquisition_uuid_in

    params["procedureCompositeProcess"] = procedure_composite_process

    params["procedureCompositeProcess__gt"] = procedure_composite_process_gt

    params["procedureCompositeProcess__gte"] = procedure_composite_process_gte

    json_procedure_composite_process_in: list[int] | Unset = UNSET
    if not isinstance(procedure_composite_process_in, Unset):
        json_procedure_composite_process_in = ",".join(map(str, procedure_composite_process_in))

    params["procedureCompositeProcess__in"] = json_procedure_composite_process_in

    params["procedureCompositeProcess__isnull"] = procedure_composite_process_isnull

    params["procedureCompositeProcess__lt"] = procedure_composite_process_lt

    params["procedureCompositeProcess__lte"] = procedure_composite_process_lte

    params["procedureComputation"] = procedure_computation

    params["procedureComputation__gt"] = procedure_computation_gt

    params["procedureComputation__gte"] = procedure_computation_gte

    json_procedure_computation_in: list[int] | Unset = UNSET
    if not isinstance(procedure_computation_in, Unset):
        json_procedure_computation_in = ",".join(map(str, procedure_computation_in))

    params["procedureComputation__in"] = json_procedure_computation_in

    params["procedureComputation__isnull"] = procedure_computation_isnull

    params["procedureComputation__lt"] = procedure_computation_lt

    params["procedureComputation__lte"] = procedure_computation_lte

    params["procedureDescription"] = procedure_description

    params["procedureDescription__contains"] = procedure_description_contains

    params["procedureDescription__endswith"] = procedure_description_endswith

    params["procedureDescription__gt"] = procedure_description_gt

    params["procedureDescription__gte"] = procedure_description_gte

    params["procedureDescription__icontains"] = procedure_description_icontains

    params["procedureDescription__iendswith"] = procedure_description_iendswith

    params["procedureDescription__iexact"] = procedure_description_iexact

    json_procedure_description_in: list[str] | Unset = UNSET
    if not isinstance(procedure_description_in, Unset):
        json_procedure_description_in = ",".join(map(str, procedure_description_in))

    params["procedureDescription__in"] = json_procedure_description_in

    params["procedureDescription__iregex"] = procedure_description_iregex

    params["procedureDescription__isnull"] = procedure_description_isnull

    params["procedureDescription__istartswith"] = procedure_description_istartswith

    params["procedureDescription__lt"] = procedure_description_lt

    params["procedureDescription__lte"] = procedure_description_lte

    json_procedure_description_range: list[str] | Unset = UNSET
    if not isinstance(procedure_description_range, Unset):
        json_procedure_description_range = ",".join(map(str, procedure_description_range))

    params["procedureDescription__range"] = json_procedure_description_range

    params["procedureDescription__regex"] = procedure_description_regex

    params["procedureDescription__startswith"] = procedure_description_startswith

    params["projects__ob_id"] = projects_ob_id

    json_projects_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(projects_ob_id_in, Unset):
        json_projects_ob_id_in = ",".join(map(str, projects_ob_id_in))

    params["projects__ob_id__in"] = json_projects_ob_id_in

    params["projects__uuid"] = projects_uuid

    json_projects_uuid_in: list[str] | Unset = UNSET
    if not isinstance(projects_uuid_in, Unset):
        json_projects_uuid_in = ",".join(map(str, projects_uuid_in))

    params["projects__uuid__in"] = json_projects_uuid_in

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

    params["removedDataReason"] = removed_data_reason

    params["removedDataReason__contains"] = removed_data_reason_contains

    params["removedDataReason__endswith"] = removed_data_reason_endswith

    params["removedDataReason__gt"] = removed_data_reason_gt

    params["removedDataReason__gte"] = removed_data_reason_gte

    params["removedDataReason__icontains"] = removed_data_reason_icontains

    params["removedDataReason__iendswith"] = removed_data_reason_iendswith

    params["removedDataReason__iexact"] = removed_data_reason_iexact

    json_removed_data_reason_in: list[str] | Unset = UNSET
    if not isinstance(removed_data_reason_in, Unset):
        json_removed_data_reason_in = ",".join(map(str, removed_data_reason_in))

    params["removedDataReason__in"] = json_removed_data_reason_in

    params["removedDataReason__iregex"] = removed_data_reason_iregex

    params["removedDataReason__isnull"] = removed_data_reason_isnull

    params["removedDataReason__istartswith"] = removed_data_reason_istartswith

    params["removedDataReason__lt"] = removed_data_reason_lt

    params["removedDataReason__lte"] = removed_data_reason_lte

    json_removed_data_reason_range: list[str] | Unset = UNSET
    if not isinstance(removed_data_reason_range, Unset):
        json_removed_data_reason_range = ",".join(map(str, removed_data_reason_range))

    params["removedDataReason__range"] = json_removed_data_reason_range

    params["removedDataReason__regex"] = removed_data_reason_regex

    params["removedDataReason__startswith"] = removed_data_reason_startswith

    json_removed_data_time: str | Unset = UNSET
    if not isinstance(removed_data_time, Unset):
        json_removed_data_time = removed_data_time.isoformat()
    params["removedDataTime"] = json_removed_data_time

    json_removed_data_time_contained_by: str | Unset = UNSET
    if not isinstance(removed_data_time_contained_by, Unset):
        json_removed_data_time_contained_by = removed_data_time_contained_by.isoformat()
    params["removedDataTime__contained_by"] = json_removed_data_time_contained_by

    json_removed_data_time_contains: str | Unset = UNSET
    if not isinstance(removed_data_time_contains, Unset):
        json_removed_data_time_contains = removed_data_time_contains.isoformat()
    params["removedDataTime__contains"] = json_removed_data_time_contains

    json_removed_data_time_date: str | Unset = UNSET
    if not isinstance(removed_data_time_date, Unset):
        json_removed_data_time_date = removed_data_time_date.isoformat()
    params["removedDataTime__date"] = json_removed_data_time_date

    params["removedDataTime__day"] = removed_data_time_day

    json_removed_data_time_endswith: str | Unset = UNSET
    if not isinstance(removed_data_time_endswith, Unset):
        json_removed_data_time_endswith = removed_data_time_endswith.isoformat()
    params["removedDataTime__endswith"] = json_removed_data_time_endswith

    json_removed_data_time_gt: str | Unset = UNSET
    if not isinstance(removed_data_time_gt, Unset):
        json_removed_data_time_gt = removed_data_time_gt.isoformat()
    params["removedDataTime__gt"] = json_removed_data_time_gt

    json_removed_data_time_gte: str | Unset = UNSET
    if not isinstance(removed_data_time_gte, Unset):
        json_removed_data_time_gte = removed_data_time_gte.isoformat()
    params["removedDataTime__gte"] = json_removed_data_time_gte

    params["removedDataTime__hour"] = removed_data_time_hour

    json_removed_data_time_icontains: str | Unset = UNSET
    if not isinstance(removed_data_time_icontains, Unset):
        json_removed_data_time_icontains = removed_data_time_icontains.isoformat()
    params["removedDataTime__icontains"] = json_removed_data_time_icontains

    json_removed_data_time_iendswith: str | Unset = UNSET
    if not isinstance(removed_data_time_iendswith, Unset):
        json_removed_data_time_iendswith = removed_data_time_iendswith.isoformat()
    params["removedDataTime__iendswith"] = json_removed_data_time_iendswith

    json_removed_data_time_iexact: str | Unset = UNSET
    if not isinstance(removed_data_time_iexact, Unset):
        json_removed_data_time_iexact = removed_data_time_iexact.isoformat()
    params["removedDataTime__iexact"] = json_removed_data_time_iexact

    json_removed_data_time_in: list[str] | Unset = UNSET
    if not isinstance(removed_data_time_in, Unset):
        json_removed_data_time_in = []
        for removed_data_time_in_item_data in removed_data_time_in:
            removed_data_time_in_item = removed_data_time_in_item_data.isoformat()
            json_removed_data_time_in.append(removed_data_time_in_item)

    params["removedDataTime__in"] = json_removed_data_time_in

    json_removed_data_time_iregex: str | Unset = UNSET
    if not isinstance(removed_data_time_iregex, Unset):
        json_removed_data_time_iregex = removed_data_time_iregex.isoformat()
    params["removedDataTime__iregex"] = json_removed_data_time_iregex

    params["removedDataTime__isnull"] = removed_data_time_isnull

    params["removedDataTime__iso_week_day"] = removed_data_time_iso_week_day

    params["removedDataTime__iso_year"] = removed_data_time_iso_year

    json_removed_data_time_istartswith: str | Unset = UNSET
    if not isinstance(removed_data_time_istartswith, Unset):
        json_removed_data_time_istartswith = removed_data_time_istartswith.isoformat()
    params["removedDataTime__istartswith"] = json_removed_data_time_istartswith

    json_removed_data_time_lt: str | Unset = UNSET
    if not isinstance(removed_data_time_lt, Unset):
        json_removed_data_time_lt = removed_data_time_lt.isoformat()
    params["removedDataTime__lt"] = json_removed_data_time_lt

    json_removed_data_time_lte: str | Unset = UNSET
    if not isinstance(removed_data_time_lte, Unset):
        json_removed_data_time_lte = removed_data_time_lte.isoformat()
    params["removedDataTime__lte"] = json_removed_data_time_lte

    params["removedDataTime__minute"] = removed_data_time_minute

    params["removedDataTime__month"] = removed_data_time_month

    params["removedDataTime__quarter"] = removed_data_time_quarter

    json_removed_data_time_range: list[str] | Unset = UNSET
    if not isinstance(removed_data_time_range, Unset):
        json_removed_data_time_range = []
        for removed_data_time_range_item_data in removed_data_time_range:
            removed_data_time_range_item = removed_data_time_range_item_data.isoformat()
            json_removed_data_time_range.append(removed_data_time_range_item)

    params["removedDataTime__range"] = json_removed_data_time_range

    json_removed_data_time_regex: str | Unset = UNSET
    if not isinstance(removed_data_time_regex, Unset):
        json_removed_data_time_regex = removed_data_time_regex.isoformat()
    params["removedDataTime__regex"] = json_removed_data_time_regex

    params["removedDataTime__second"] = removed_data_time_second

    json_removed_data_time_startswith: str | Unset = UNSET
    if not isinstance(removed_data_time_startswith, Unset):
        json_removed_data_time_startswith = removed_data_time_startswith.isoformat()
    params["removedDataTime__startswith"] = json_removed_data_time_startswith

    params["removedDataTime__time"] = removed_data_time_time

    params["removedDataTime__week"] = removed_data_time_week

    params["removedDataTime__week_day"] = removed_data_time_week_day

    params["removedDataTime__year"] = removed_data_time_year

    params["resolution"] = resolution

    params["resolution__contains"] = resolution_contains

    params["resolution__endswith"] = resolution_endswith

    params["resolution__gt"] = resolution_gt

    params["resolution__gte"] = resolution_gte

    params["resolution__icontains"] = resolution_icontains

    params["resolution__iendswith"] = resolution_iendswith

    params["resolution__iexact"] = resolution_iexact

    json_resolution_in: list[str] | Unset = UNSET
    if not isinstance(resolution_in, Unset):
        json_resolution_in = ",".join(map(str, resolution_in))

    params["resolution__in"] = json_resolution_in

    params["resolution__iregex"] = resolution_iregex

    params["resolution__isnull"] = resolution_isnull

    params["resolution__istartswith"] = resolution_istartswith

    params["resolution__lt"] = resolution_lt

    params["resolution__lte"] = resolution_lte

    json_resolution_range: list[str] | Unset = UNSET
    if not isinstance(resolution_range, Unset):
        json_resolution_range = ",".join(map(str, resolution_range))

    params["resolution__range"] = json_resolution_range

    params["resolution__regex"] = resolution_regex

    params["resolution__startswith"] = resolution_startswith

    params["resultQuality"] = result_quality

    json_result_quality_date: str | Unset = UNSET
    if not isinstance(result_quality_date, Unset):
        json_result_quality_date = result_quality_date.isoformat()
    params["resultQuality__date"] = json_result_quality_date

    json_result_quality_date_gt: str | Unset = UNSET
    if not isinstance(result_quality_date_gt, Unset):
        json_result_quality_date_gt = result_quality_date_gt.isoformat()
    params["resultQuality__date__gt"] = json_result_quality_date_gt

    json_result_quality_date_gte: str | Unset = UNSET
    if not isinstance(result_quality_date_gte, Unset):
        json_result_quality_date_gte = result_quality_date_gte.isoformat()
    params["resultQuality__date__gte"] = json_result_quality_date_gte

    json_result_quality_date_lt: str | Unset = UNSET
    if not isinstance(result_quality_date_lt, Unset):
        json_result_quality_date_lt = result_quality_date_lt.isoformat()
    params["resultQuality__date__lt"] = json_result_quality_date_lt

    json_result_quality_date_lte: str | Unset = UNSET
    if not isinstance(result_quality_date_lte, Unset):
        json_result_quality_date_lte = result_quality_date_lte.isoformat()
    params["resultQuality__date__lte"] = json_result_quality_date_lte

    json_result_quality_date_range: list[str] | Unset = UNSET
    if not isinstance(result_quality_date_range, Unset):
        json_result_quality_date_range = []
        for result_quality_date_range_item_data in result_quality_date_range:
            result_quality_date_range_item = result_quality_date_range_item_data.isoformat()
            json_result_quality_date_range.append(result_quality_date_range_item)

    params["resultQuality__date__range"] = json_result_quality_date_range

    params["resultQuality__explanation"] = result_quality_explanation

    params["resultQuality__explanation__contains"] = result_quality_explanation_contains

    params["resultQuality__gt"] = result_quality_gt

    params["resultQuality__gte"] = result_quality_gte

    json_result_quality_in: list[int] | Unset = UNSET
    if not isinstance(result_quality_in, Unset):
        json_result_quality_in = ",".join(map(str, result_quality_in))

    params["resultQuality__in"] = json_result_quality_in

    params["resultQuality__isnull"] = result_quality_isnull

    params["resultQuality__lt"] = result_quality_lt

    params["resultQuality__lte"] = result_quality_lte

    params["resultQuality__ob_id"] = result_quality_ob_id

    json_result_quality_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(result_quality_ob_id_in, Unset):
        json_result_quality_ob_id_in = ",".join(map(str, result_quality_ob_id_in))

    params["resultQuality__ob_id__in"] = json_result_quality_ob_id_in

    params["resultQuality__passesTest"] = result_quality_passes_test

    params["resultQuality__resultTitle"] = result_quality_result_title

    params["resultQuality__resultTitle__contains"] = result_quality_result_title_contains

    params["result_field"] = result_field

    params["result_field__dataPath"] = result_field_data_path

    params["result_field__dataPath__contains"] = result_field_data_path_contains

    params["result_field__dataPath__startswith"] = result_field_data_path_startswith

    params["result_field__fileFormat"] = result_field_file_format

    params["result_field__fileFormat__contains"] = result_field_file_format_contains

    params["result_field__gt"] = result_field_gt

    params["result_field__gte"] = result_field_gte

    json_result_field_in: list[int] | Unset = UNSET
    if not isinstance(result_field_in, Unset):
        json_result_field_in = ",".join(map(str, result_field_in))

    params["result_field__in"] = json_result_field_in

    params["result_field__isnull"] = result_field_isnull

    params["result_field__lt"] = result_field_lt

    params["result_field__lte"] = result_field_lte

    json_result_field_storage_location: str | Unset = UNSET
    if not isinstance(result_field_storage_location, Unset):
        json_result_field_storage_location = result_field_storage_location.value

    params["result_field__storageLocation"] = json_result_field_storage_location

    json_result_field_storage_status: str | Unset = UNSET
    if not isinstance(result_field_storage_status, Unset):
        json_result_field_storage_status = result_field_storage_status.value

    params["result_field__storageStatus"] = json_result_field_storage_status

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

    params["submissionUserID"] = submission_user_id

    params["submissionUserID__contains"] = submission_user_id_contains

    params["submissionUserID__endswith"] = submission_user_id_endswith

    params["submissionUserID__gt"] = submission_user_id_gt

    params["submissionUserID__gte"] = submission_user_id_gte

    params["submissionUserID__icontains"] = submission_user_id_icontains

    params["submissionUserID__iendswith"] = submission_user_id_iendswith

    params["submissionUserID__iexact"] = submission_user_id_iexact

    json_submission_user_id_in: list[str] | Unset = UNSET
    if not isinstance(submission_user_id_in, Unset):
        json_submission_user_id_in = ",".join(map(str, submission_user_id_in))

    params["submissionUserID__in"] = json_submission_user_id_in

    params["submissionUserID__iregex"] = submission_user_id_iregex

    params["submissionUserID__isnull"] = submission_user_id_isnull

    params["submissionUserID__istartswith"] = submission_user_id_istartswith

    params["submissionUserID__lt"] = submission_user_id_lt

    params["submissionUserID__lte"] = submission_user_id_lte

    json_submission_user_id_range: list[str] | Unset = UNSET
    if not isinstance(submission_user_id_range, Unset):
        json_submission_user_id_range = ",".join(map(str, submission_user_id_range))

    params["submissionUserID__range"] = json_submission_user_id_range

    params["submissionUserID__regex"] = submission_user_id_regex

    params["submissionUserID__startswith"] = submission_user_id_startswith

    params["timePeriod"] = time_period

    json_time_period_end_time: str | Unset = UNSET
    if not isinstance(time_period_end_time, Unset):
        json_time_period_end_time = time_period_end_time.isoformat()
    params["timePeriod__endTime"] = json_time_period_end_time

    json_time_period_end_time_gt: str | Unset = UNSET
    if not isinstance(time_period_end_time_gt, Unset):
        json_time_period_end_time_gt = time_period_end_time_gt.isoformat()
    params["timePeriod__endTime__gt"] = json_time_period_end_time_gt

    json_time_period_end_time_gte: str | Unset = UNSET
    if not isinstance(time_period_end_time_gte, Unset):
        json_time_period_end_time_gte = time_period_end_time_gte.isoformat()
    params["timePeriod__endTime__gte"] = json_time_period_end_time_gte

    json_time_period_end_time_lt: str | Unset = UNSET
    if not isinstance(time_period_end_time_lt, Unset):
        json_time_period_end_time_lt = time_period_end_time_lt.isoformat()
    params["timePeriod__endTime__lt"] = json_time_period_end_time_lt

    json_time_period_end_time_lte: str | Unset = UNSET
    if not isinstance(time_period_end_time_lte, Unset):
        json_time_period_end_time_lte = time_period_end_time_lte.isoformat()
    params["timePeriod__endTime__lte"] = json_time_period_end_time_lte

    json_time_period_end_time_range: list[str] | Unset = UNSET
    if not isinstance(time_period_end_time_range, Unset):
        json_time_period_end_time_range = []
        for time_period_end_time_range_item_data in time_period_end_time_range:
            time_period_end_time_range_item = time_period_end_time_range_item_data.isoformat()
            json_time_period_end_time_range.append(time_period_end_time_range_item)

    params["timePeriod__endTime__range"] = json_time_period_end_time_range

    params["timePeriod__gt"] = time_period_gt

    params["timePeriod__gte"] = time_period_gte

    json_time_period_in: list[int] | Unset = UNSET
    if not isinstance(time_period_in, Unset):
        json_time_period_in = ",".join(map(str, time_period_in))

    params["timePeriod__in"] = json_time_period_in

    params["timePeriod__isnull"] = time_period_isnull

    params["timePeriod__lt"] = time_period_lt

    params["timePeriod__lte"] = time_period_lte

    params["timePeriod__ob_id"] = time_period_ob_id

    json_time_period_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(time_period_ob_id_in, Unset):
        json_time_period_ob_id_in = ",".join(map(str, time_period_ob_id_in))

    params["timePeriod__ob_id__in"] = json_time_period_ob_id_in

    json_time_period_start_time: str | Unset = UNSET
    if not isinstance(time_period_start_time, Unset):
        json_time_period_start_time = time_period_start_time.isoformat()
    params["timePeriod__startTime"] = json_time_period_start_time

    json_time_period_start_time_gt: str | Unset = UNSET
    if not isinstance(time_period_start_time_gt, Unset):
        json_time_period_start_time_gt = time_period_start_time_gt.isoformat()
    params["timePeriod__startTime__gt"] = json_time_period_start_time_gt

    json_time_period_start_time_gte: str | Unset = UNSET
    if not isinstance(time_period_start_time_gte, Unset):
        json_time_period_start_time_gte = time_period_start_time_gte.isoformat()
    params["timePeriod__startTime__gte"] = json_time_period_start_time_gte

    json_time_period_start_time_lt: str | Unset = UNSET
    if not isinstance(time_period_start_time_lt, Unset):
        json_time_period_start_time_lt = time_period_start_time_lt.isoformat()
    params["timePeriod__startTime__lt"] = json_time_period_start_time_lt

    json_time_period_start_time_lte: str | Unset = UNSET
    if not isinstance(time_period_start_time_lte, Unset):
        json_time_period_start_time_lte = time_period_start_time_lte.isoformat()
    params["timePeriod__startTime__lte"] = json_time_period_start_time_lte

    json_time_period_start_time_range: list[str] | Unset = UNSET
    if not isinstance(time_period_start_time_range, Unset):
        json_time_period_start_time_range = []
        for time_period_start_time_range_item_data in time_period_start_time_range:
            time_period_start_time_range_item = time_period_start_time_range_item_data.isoformat()
            json_time_period_start_time_range.append(time_period_start_time_range_item)

    params["timePeriod__startTime__range"] = json_time_period_start_time_range

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

    json_update_frequency: str | Unset = UNSET
    if not isinstance(update_frequency, Unset):
        json_update_frequency = update_frequency.value

    params["updateFrequency"] = json_update_frequency

    params["updateFrequency__contains"] = update_frequency_contains

    params["updateFrequency__endswith"] = update_frequency_endswith

    params["updateFrequency__gt"] = update_frequency_gt

    params["updateFrequency__gte"] = update_frequency_gte

    params["updateFrequency__icontains"] = update_frequency_icontains

    params["updateFrequency__iendswith"] = update_frequency_iendswith

    params["updateFrequency__iexact"] = update_frequency_iexact

    json_update_frequency_in: list[str] | Unset = UNSET
    if not isinstance(update_frequency_in, Unset):
        json_update_frequency_in = ",".join(map(str, update_frequency_in))

    params["updateFrequency__in"] = json_update_frequency_in

    params["updateFrequency__iregex"] = update_frequency_iregex

    params["updateFrequency__isnull"] = update_frequency_isnull

    params["updateFrequency__istartswith"] = update_frequency_istartswith

    params["updateFrequency__lt"] = update_frequency_lt

    params["updateFrequency__lte"] = update_frequency_lte

    json_update_frequency_range: list[str] | Unset = UNSET
    if not isinstance(update_frequency_range, Unset):
        json_update_frequency_range = ",".join(map(str, update_frequency_range))

    params["updateFrequency__range"] = json_update_frequency_range

    params["updateFrequency__regex"] = update_frequency_regex

    params["updateFrequency__startswith"] = update_frequency_startswith

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

    params["validTimePeriod"] = valid_time_period

    params["validTimePeriod__gt"] = valid_time_period_gt

    params["validTimePeriod__gte"] = valid_time_period_gte

    json_valid_time_period_in: list[int] | Unset = UNSET
    if not isinstance(valid_time_period_in, Unset):
        json_valid_time_period_in = ",".join(map(str, valid_time_period_in))

    params["validTimePeriod__in"] = json_valid_time_period_in

    params["validTimePeriod__isnull"] = valid_time_period_isnull

    params["validTimePeriod__lt"] = valid_time_period_lt

    params["validTimePeriod__lte"] = valid_time_period_lte

    params["verticalExtent"] = vertical_extent

    params["verticalExtent__gt"] = vertical_extent_gt

    params["verticalExtent__gte"] = vertical_extent_gte

    json_vertical_extent_in: list[int] | Unset = UNSET
    if not isinstance(vertical_extent_in, Unset):
        json_vertical_extent_in = ",".join(map(str, vertical_extent_in))

    params["verticalExtent__in"] = json_vertical_extent_in

    params["verticalExtent__isnull"] = vertical_extent_isnull

    params["verticalExtent__lt"] = vertical_extent_lt

    params["verticalExtent__lte"] = vertical_extent_lte

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/observations/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedObservationReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedObservationReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedObservationReadList]:
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
    creation_date: datetime.datetime | Unset = UNSET,
    creation_date_contained_by: datetime.datetime | Unset = UNSET,
    creation_date_contains: datetime.datetime | Unset = UNSET,
    creation_date_date: datetime.date | Unset = UNSET,
    creation_date_day: float | Unset = UNSET,
    creation_date_endswith: datetime.datetime | Unset = UNSET,
    creation_date_gt: datetime.datetime | Unset = UNSET,
    creation_date_gte: datetime.datetime | Unset = UNSET,
    creation_date_hour: float | Unset = UNSET,
    creation_date_icontains: datetime.datetime | Unset = UNSET,
    creation_date_iendswith: datetime.datetime | Unset = UNSET,
    creation_date_iexact: datetime.datetime | Unset = UNSET,
    creation_date_in: list[datetime.datetime] | Unset = UNSET,
    creation_date_iregex: datetime.datetime | Unset = UNSET,
    creation_date_isnull: bool | Unset = UNSET,
    creation_date_iso_week_day: float | Unset = UNSET,
    creation_date_iso_year: float | Unset = UNSET,
    creation_date_istartswith: datetime.datetime | Unset = UNSET,
    creation_date_lt: datetime.datetime | Unset = UNSET,
    creation_date_lte: datetime.datetime | Unset = UNSET,
    creation_date_minute: float | Unset = UNSET,
    creation_date_month: float | Unset = UNSET,
    creation_date_quarter: float | Unset = UNSET,
    creation_date_range: list[datetime.datetime] | Unset = UNSET,
    creation_date_regex: datetime.datetime | Unset = UNSET,
    creation_date_second: float | Unset = UNSET,
    creation_date_startswith: datetime.datetime | Unset = UNSET,
    creation_date_time: str | Unset = UNSET,
    creation_date_week: float | Unset = UNSET,
    creation_date_week_day: float | Unset = UNSET,
    creation_date_year: float | Unset = UNSET,
    data_lineage: str | Unset = UNSET,
    data_lineage_contains: str | Unset = UNSET,
    data_lineage_endswith: str | Unset = UNSET,
    data_lineage_gt: str | Unset = UNSET,
    data_lineage_gte: str | Unset = UNSET,
    data_lineage_icontains: str | Unset = UNSET,
    data_lineage_iendswith: str | Unset = UNSET,
    data_lineage_iexact: str | Unset = UNSET,
    data_lineage_in: list[str] | Unset = UNSET,
    data_lineage_iregex: str | Unset = UNSET,
    data_lineage_isnull: bool | Unset = UNSET,
    data_lineage_istartswith: str | Unset = UNSET,
    data_lineage_lt: str | Unset = UNSET,
    data_lineage_lte: str | Unset = UNSET,
    data_lineage_range: list[str] | Unset = UNSET,
    data_lineage_regex: str | Unset = UNSET,
    data_lineage_startswith: str | Unset = UNSET,
    data_published_time: datetime.datetime | Unset = UNSET,
    data_published_time_contained_by: datetime.datetime | Unset = UNSET,
    data_published_time_contains: datetime.datetime | Unset = UNSET,
    data_published_time_date: datetime.date | Unset = UNSET,
    data_published_time_day: float | Unset = UNSET,
    data_published_time_endswith: datetime.datetime | Unset = UNSET,
    data_published_time_gt: datetime.datetime | Unset = UNSET,
    data_published_time_gte: datetime.datetime | Unset = UNSET,
    data_published_time_hour: float | Unset = UNSET,
    data_published_time_icontains: datetime.datetime | Unset = UNSET,
    data_published_time_iendswith: datetime.datetime | Unset = UNSET,
    data_published_time_iexact: datetime.datetime | Unset = UNSET,
    data_published_time_in: list[datetime.datetime] | Unset = UNSET,
    data_published_time_iregex: datetime.datetime | Unset = UNSET,
    data_published_time_isnull: bool | Unset = UNSET,
    data_published_time_iso_week_day: float | Unset = UNSET,
    data_published_time_iso_year: float | Unset = UNSET,
    data_published_time_istartswith: datetime.datetime | Unset = UNSET,
    data_published_time_lt: datetime.datetime | Unset = UNSET,
    data_published_time_lte: datetime.datetime | Unset = UNSET,
    data_published_time_minute: float | Unset = UNSET,
    data_published_time_month: float | Unset = UNSET,
    data_published_time_quarter: float | Unset = UNSET,
    data_published_time_range: list[datetime.datetime] | Unset = UNSET,
    data_published_time_regex: datetime.datetime | Unset = UNSET,
    data_published_time_second: float | Unset = UNSET,
    data_published_time_startswith: datetime.datetime | Unset = UNSET,
    data_published_time_time: str | Unset = UNSET,
    data_published_time_week: float | Unset = UNSET,
    data_published_time_week_day: float | Unset = UNSET,
    data_published_time_year: float | Unset = UNSET,
    discovery_keywords_name: str | Unset = UNSET,
    discovery_keywords_name_contains: str | Unset = UNSET,
    doi_published_time: datetime.datetime | Unset = UNSET,
    doi_published_time_contained_by: datetime.datetime | Unset = UNSET,
    doi_published_time_contains: datetime.datetime | Unset = UNSET,
    doi_published_time_date: datetime.date | Unset = UNSET,
    doi_published_time_day: float | Unset = UNSET,
    doi_published_time_endswith: datetime.datetime | Unset = UNSET,
    doi_published_time_gt: datetime.datetime | Unset = UNSET,
    doi_published_time_gte: datetime.datetime | Unset = UNSET,
    doi_published_time_hour: float | Unset = UNSET,
    doi_published_time_icontains: datetime.datetime | Unset = UNSET,
    doi_published_time_iendswith: datetime.datetime | Unset = UNSET,
    doi_published_time_iexact: datetime.datetime | Unset = UNSET,
    doi_published_time_in: list[datetime.datetime] | Unset = UNSET,
    doi_published_time_iregex: datetime.datetime | Unset = UNSET,
    doi_published_time_isnull: bool | Unset = UNSET,
    doi_published_time_iso_week_day: float | Unset = UNSET,
    doi_published_time_iso_year: float | Unset = UNSET,
    doi_published_time_istartswith: datetime.datetime | Unset = UNSET,
    doi_published_time_lt: datetime.datetime | Unset = UNSET,
    doi_published_time_lte: datetime.datetime | Unset = UNSET,
    doi_published_time_minute: float | Unset = UNSET,
    doi_published_time_month: float | Unset = UNSET,
    doi_published_time_quarter: float | Unset = UNSET,
    doi_published_time_range: list[datetime.datetime] | Unset = UNSET,
    doi_published_time_regex: datetime.datetime | Unset = UNSET,
    doi_published_time_second: float | Unset = UNSET,
    doi_published_time_startswith: datetime.datetime | Unset = UNSET,
    doi_published_time_time: str | Unset = UNSET,
    doi_published_time_week: float | Unset = UNSET,
    doi_published_time_week_day: float | Unset = UNSET,
    doi_published_time_year: float | Unset = UNSET,
    dont_harvest_from_projects: bool | Unset = UNSET,
    dont_harvest_from_projects_contains: bool | Unset = UNSET,
    dont_harvest_from_projects_endswith: bool | Unset = UNSET,
    dont_harvest_from_projects_gt: bool | Unset = UNSET,
    dont_harvest_from_projects_gte: bool | Unset = UNSET,
    dont_harvest_from_projects_icontains: bool | Unset = UNSET,
    dont_harvest_from_projects_iendswith: bool | Unset = UNSET,
    dont_harvest_from_projects_iexact: bool | Unset = UNSET,
    dont_harvest_from_projects_in: list[bool] | Unset = UNSET,
    dont_harvest_from_projects_iregex: bool | Unset = UNSET,
    dont_harvest_from_projects_isnull: bool | Unset = UNSET,
    dont_harvest_from_projects_istartswith: bool | Unset = UNSET,
    dont_harvest_from_projects_lt: bool | Unset = UNSET,
    dont_harvest_from_projects_lte: bool | Unset = UNSET,
    dont_harvest_from_projects_range: list[bool] | Unset = UNSET,
    dont_harvest_from_projects_regex: bool | Unset = UNSET,
    dont_harvest_from_projects_startswith: bool | Unset = UNSET,
    feature_of_interest: str | Unset = UNSET,
    feature_of_interest_contains: str | Unset = UNSET,
    feature_of_interest_endswith: str | Unset = UNSET,
    feature_of_interest_gt: str | Unset = UNSET,
    feature_of_interest_gte: str | Unset = UNSET,
    feature_of_interest_icontains: str | Unset = UNSET,
    feature_of_interest_iendswith: str | Unset = UNSET,
    feature_of_interest_iexact: str | Unset = UNSET,
    feature_of_interest_in: list[str] | Unset = UNSET,
    feature_of_interest_iregex: str | Unset = UNSET,
    feature_of_interest_isnull: bool | Unset = UNSET,
    feature_of_interest_istartswith: str | Unset = UNSET,
    feature_of_interest_lt: str | Unset = UNSET,
    feature_of_interest_lte: str | Unset = UNSET,
    feature_of_interest_range: list[str] | Unset = UNSET,
    feature_of_interest_regex: str | Unset = UNSET,
    feature_of_interest_startswith: str | Unset = UNSET,
    geographic_extent: int | Unset = UNSET,
    geographic_extent_east_bound_longitude: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_gt: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_gte: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_lt: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_lte: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_range: list[float] | Unset = UNSET,
    geographic_extent_gt: int | Unset = UNSET,
    geographic_extent_gte: int | Unset = UNSET,
    geographic_extent_in: list[int] | Unset = UNSET,
    geographic_extent_isnull: bool | Unset = UNSET,
    geographic_extent_lt: int | Unset = UNSET,
    geographic_extent_lte: int | Unset = UNSET,
    geographic_extent_north_bound_latitude: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_gt: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_gte: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_lt: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_lte: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_range: list[float] | Unset = UNSET,
    geographic_extent_ob_id: int | Unset = UNSET,
    geographic_extent_ob_id_in: list[int] | Unset = UNSET,
    geographic_extent_south_bound_latitude: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_gt: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_gte: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_lt: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_lte: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_range: list[float] | Unset = UNSET,
    geographic_extent_west_bound_longitude: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_gt: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_gte: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_lt: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_lte: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_range: list[float] | Unset = UNSET,
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
    language: ObservationsListLanguage | Unset = UNSET,
    language_contains: str | Unset = UNSET,
    language_endswith: str | Unset = UNSET,
    language_gt: str | Unset = UNSET,
    language_gte: str | Unset = UNSET,
    language_icontains: str | Unset = UNSET,
    language_iendswith: str | Unset = UNSET,
    language_iexact: str | Unset = UNSET,
    language_in: list[str] | Unset = UNSET,
    language_iregex: str | Unset = UNSET,
    language_isnull: bool | Unset = UNSET,
    language_istartswith: str | Unset = UNSET,
    language_lt: str | Unset = UNSET,
    language_lte: str | Unset = UNSET,
    language_range: list[str] | Unset = UNSET,
    language_regex: str | Unset = UNSET,
    language_startswith: str | Unset = UNSET,
    last_updated_date: datetime.datetime | Unset = UNSET,
    last_updated_date_contained_by: datetime.datetime | Unset = UNSET,
    last_updated_date_contains: datetime.datetime | Unset = UNSET,
    last_updated_date_date: datetime.date | Unset = UNSET,
    last_updated_date_day: float | Unset = UNSET,
    last_updated_date_endswith: datetime.datetime | Unset = UNSET,
    last_updated_date_gt: datetime.datetime | Unset = UNSET,
    last_updated_date_gte: datetime.datetime | Unset = UNSET,
    last_updated_date_hour: float | Unset = UNSET,
    last_updated_date_icontains: datetime.datetime | Unset = UNSET,
    last_updated_date_iendswith: datetime.datetime | Unset = UNSET,
    last_updated_date_iexact: datetime.datetime | Unset = UNSET,
    last_updated_date_in: list[datetime.datetime] | Unset = UNSET,
    last_updated_date_iregex: datetime.datetime | Unset = UNSET,
    last_updated_date_isnull: bool | Unset = UNSET,
    last_updated_date_iso_week_day: float | Unset = UNSET,
    last_updated_date_iso_year: float | Unset = UNSET,
    last_updated_date_istartswith: datetime.datetime | Unset = UNSET,
    last_updated_date_lt: datetime.datetime | Unset = UNSET,
    last_updated_date_lte: datetime.datetime | Unset = UNSET,
    last_updated_date_minute: float | Unset = UNSET,
    last_updated_date_month: float | Unset = UNSET,
    last_updated_date_quarter: float | Unset = UNSET,
    last_updated_date_range: list[datetime.datetime] | Unset = UNSET,
    last_updated_date_regex: datetime.datetime | Unset = UNSET,
    last_updated_date_second: float | Unset = UNSET,
    last_updated_date_startswith: datetime.datetime | Unset = UNSET,
    last_updated_date_time: str | Unset = UNSET,
    last_updated_date_week: float | Unset = UNSET,
    last_updated_date_week_day: float | Unset = UNSET,
    last_updated_date_year: float | Unset = UNSET,
    latest_data_update_time: datetime.datetime | Unset = UNSET,
    latest_data_update_time_contained_by: datetime.datetime | Unset = UNSET,
    latest_data_update_time_contains: datetime.datetime | Unset = UNSET,
    latest_data_update_time_date: datetime.date | Unset = UNSET,
    latest_data_update_time_day: float | Unset = UNSET,
    latest_data_update_time_endswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_gt: datetime.datetime | Unset = UNSET,
    latest_data_update_time_gte: datetime.datetime | Unset = UNSET,
    latest_data_update_time_hour: float | Unset = UNSET,
    latest_data_update_time_icontains: datetime.datetime | Unset = UNSET,
    latest_data_update_time_iendswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_iexact: datetime.datetime | Unset = UNSET,
    latest_data_update_time_in: list[datetime.datetime] | Unset = UNSET,
    latest_data_update_time_iregex: datetime.datetime | Unset = UNSET,
    latest_data_update_time_isnull: bool | Unset = UNSET,
    latest_data_update_time_iso_week_day: float | Unset = UNSET,
    latest_data_update_time_iso_year: float | Unset = UNSET,
    latest_data_update_time_istartswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_lt: datetime.datetime | Unset = UNSET,
    latest_data_update_time_lte: datetime.datetime | Unset = UNSET,
    latest_data_update_time_minute: float | Unset = UNSET,
    latest_data_update_time_month: float | Unset = UNSET,
    latest_data_update_time_quarter: float | Unset = UNSET,
    latest_data_update_time_range: list[datetime.datetime] | Unset = UNSET,
    latest_data_update_time_regex: datetime.datetime | Unset = UNSET,
    latest_data_update_time_second: float | Unset = UNSET,
    latest_data_update_time_startswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_time: str | Unset = UNSET,
    latest_data_update_time_week: float | Unset = UNSET,
    latest_data_update_time_week_day: float | Unset = UNSET,
    latest_data_update_time_year: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    non_geographic_flag: bool | Unset = UNSET,
    non_geographic_flag_contains: bool | Unset = UNSET,
    non_geographic_flag_endswith: bool | Unset = UNSET,
    non_geographic_flag_gt: bool | Unset = UNSET,
    non_geographic_flag_gte: bool | Unset = UNSET,
    non_geographic_flag_icontains: bool | Unset = UNSET,
    non_geographic_flag_iendswith: bool | Unset = UNSET,
    non_geographic_flag_iexact: bool | Unset = UNSET,
    non_geographic_flag_in: list[bool] | Unset = UNSET,
    non_geographic_flag_iregex: bool | Unset = UNSET,
    non_geographic_flag_isnull: bool | Unset = UNSET,
    non_geographic_flag_istartswith: bool | Unset = UNSET,
    non_geographic_flag_lt: bool | Unset = UNSET,
    non_geographic_flag_lte: bool | Unset = UNSET,
    non_geographic_flag_range: list[bool] | Unset = UNSET,
    non_geographic_flag_regex: bool | Unset = UNSET,
    non_geographic_flag_startswith: bool | Unset = UNSET,
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
    permissions_access_category: ObservationsListAccessCategory | Unset = UNSET,
    permissions_access_category_in: list[str] | Unset = UNSET,
    permissions_access_roles: str | Unset = UNSET,
    permissions_access_roles_in: list[str] | Unset = UNSET,
    procedure_acquisition: int | Unset = UNSET,
    procedure_acquisition_gt: int | Unset = UNSET,
    procedure_acquisition_gte: int | Unset = UNSET,
    procedure_acquisition_in: list[int] | Unset = UNSET,
    procedure_acquisition_isnull: bool | Unset = UNSET,
    procedure_acquisition_lt: int | Unset = UNSET,
    procedure_acquisition_lte: int | Unset = UNSET,
    procedure_acquisition_ob_id: int | Unset = UNSET,
    procedure_acquisition_ob_id_in: list[int] | Unset = UNSET,
    procedure_acquisition_uuid: str | Unset = UNSET,
    procedure_acquisition_uuid_in: list[str] | Unset = UNSET,
    procedure_composite_process: int | Unset = UNSET,
    procedure_composite_process_gt: int | Unset = UNSET,
    procedure_composite_process_gte: int | Unset = UNSET,
    procedure_composite_process_in: list[int] | Unset = UNSET,
    procedure_composite_process_isnull: bool | Unset = UNSET,
    procedure_composite_process_lt: int | Unset = UNSET,
    procedure_composite_process_lte: int | Unset = UNSET,
    procedure_computation: int | Unset = UNSET,
    procedure_computation_gt: int | Unset = UNSET,
    procedure_computation_gte: int | Unset = UNSET,
    procedure_computation_in: list[int] | Unset = UNSET,
    procedure_computation_isnull: bool | Unset = UNSET,
    procedure_computation_lt: int | Unset = UNSET,
    procedure_computation_lte: int | Unset = UNSET,
    procedure_description: str | Unset = UNSET,
    procedure_description_contains: str | Unset = UNSET,
    procedure_description_endswith: str | Unset = UNSET,
    procedure_description_gt: str | Unset = UNSET,
    procedure_description_gte: str | Unset = UNSET,
    procedure_description_icontains: str | Unset = UNSET,
    procedure_description_iendswith: str | Unset = UNSET,
    procedure_description_iexact: str | Unset = UNSET,
    procedure_description_in: list[str] | Unset = UNSET,
    procedure_description_iregex: str | Unset = UNSET,
    procedure_description_isnull: bool | Unset = UNSET,
    procedure_description_istartswith: str | Unset = UNSET,
    procedure_description_lt: str | Unset = UNSET,
    procedure_description_lte: str | Unset = UNSET,
    procedure_description_range: list[str] | Unset = UNSET,
    procedure_description_regex: str | Unset = UNSET,
    procedure_description_startswith: str | Unset = UNSET,
    projects_ob_id: int | Unset = UNSET,
    projects_ob_id_in: list[int] | Unset = UNSET,
    projects_uuid: str | Unset = UNSET,
    projects_uuid_in: list[str] | Unset = UNSET,
    publication_state: ObservationsListPublicationState | Unset = UNSET,
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
    removed_data_reason: str | Unset = UNSET,
    removed_data_reason_contains: str | Unset = UNSET,
    removed_data_reason_endswith: str | Unset = UNSET,
    removed_data_reason_gt: str | Unset = UNSET,
    removed_data_reason_gte: str | Unset = UNSET,
    removed_data_reason_icontains: str | Unset = UNSET,
    removed_data_reason_iendswith: str | Unset = UNSET,
    removed_data_reason_iexact: str | Unset = UNSET,
    removed_data_reason_in: list[str] | Unset = UNSET,
    removed_data_reason_iregex: str | Unset = UNSET,
    removed_data_reason_isnull: bool | Unset = UNSET,
    removed_data_reason_istartswith: str | Unset = UNSET,
    removed_data_reason_lt: str | Unset = UNSET,
    removed_data_reason_lte: str | Unset = UNSET,
    removed_data_reason_range: list[str] | Unset = UNSET,
    removed_data_reason_regex: str | Unset = UNSET,
    removed_data_reason_startswith: str | Unset = UNSET,
    removed_data_time: datetime.datetime | Unset = UNSET,
    removed_data_time_contained_by: datetime.datetime | Unset = UNSET,
    removed_data_time_contains: datetime.datetime | Unset = UNSET,
    removed_data_time_date: datetime.date | Unset = UNSET,
    removed_data_time_day: float | Unset = UNSET,
    removed_data_time_endswith: datetime.datetime | Unset = UNSET,
    removed_data_time_gt: datetime.datetime | Unset = UNSET,
    removed_data_time_gte: datetime.datetime | Unset = UNSET,
    removed_data_time_hour: float | Unset = UNSET,
    removed_data_time_icontains: datetime.datetime | Unset = UNSET,
    removed_data_time_iendswith: datetime.datetime | Unset = UNSET,
    removed_data_time_iexact: datetime.datetime | Unset = UNSET,
    removed_data_time_in: list[datetime.datetime] | Unset = UNSET,
    removed_data_time_iregex: datetime.datetime | Unset = UNSET,
    removed_data_time_isnull: bool | Unset = UNSET,
    removed_data_time_iso_week_day: float | Unset = UNSET,
    removed_data_time_iso_year: float | Unset = UNSET,
    removed_data_time_istartswith: datetime.datetime | Unset = UNSET,
    removed_data_time_lt: datetime.datetime | Unset = UNSET,
    removed_data_time_lte: datetime.datetime | Unset = UNSET,
    removed_data_time_minute: float | Unset = UNSET,
    removed_data_time_month: float | Unset = UNSET,
    removed_data_time_quarter: float | Unset = UNSET,
    removed_data_time_range: list[datetime.datetime] | Unset = UNSET,
    removed_data_time_regex: datetime.datetime | Unset = UNSET,
    removed_data_time_second: float | Unset = UNSET,
    removed_data_time_startswith: datetime.datetime | Unset = UNSET,
    removed_data_time_time: str | Unset = UNSET,
    removed_data_time_week: float | Unset = UNSET,
    removed_data_time_week_day: float | Unset = UNSET,
    removed_data_time_year: float | Unset = UNSET,
    resolution: str | Unset = UNSET,
    resolution_contains: str | Unset = UNSET,
    resolution_endswith: str | Unset = UNSET,
    resolution_gt: str | Unset = UNSET,
    resolution_gte: str | Unset = UNSET,
    resolution_icontains: str | Unset = UNSET,
    resolution_iendswith: str | Unset = UNSET,
    resolution_iexact: str | Unset = UNSET,
    resolution_in: list[str] | Unset = UNSET,
    resolution_iregex: str | Unset = UNSET,
    resolution_isnull: bool | Unset = UNSET,
    resolution_istartswith: str | Unset = UNSET,
    resolution_lt: str | Unset = UNSET,
    resolution_lte: str | Unset = UNSET,
    resolution_range: list[str] | Unset = UNSET,
    resolution_regex: str | Unset = UNSET,
    resolution_startswith: str | Unset = UNSET,
    result_quality: int | Unset = UNSET,
    result_quality_date: datetime.date | Unset = UNSET,
    result_quality_date_gt: datetime.date | Unset = UNSET,
    result_quality_date_gte: datetime.date | Unset = UNSET,
    result_quality_date_lt: datetime.date | Unset = UNSET,
    result_quality_date_lte: datetime.date | Unset = UNSET,
    result_quality_date_range: list[datetime.date] | Unset = UNSET,
    result_quality_explanation: str | Unset = UNSET,
    result_quality_explanation_contains: str | Unset = UNSET,
    result_quality_gt: int | Unset = UNSET,
    result_quality_gte: int | Unset = UNSET,
    result_quality_in: list[int] | Unset = UNSET,
    result_quality_isnull: bool | Unset = UNSET,
    result_quality_lt: int | Unset = UNSET,
    result_quality_lte: int | Unset = UNSET,
    result_quality_ob_id: int | Unset = UNSET,
    result_quality_ob_id_in: list[int] | Unset = UNSET,
    result_quality_passes_test: bool | Unset = UNSET,
    result_quality_result_title: str | Unset = UNSET,
    result_quality_result_title_contains: str | Unset = UNSET,
    result_field: int | Unset = UNSET,
    result_field_data_path: str | Unset = UNSET,
    result_field_data_path_contains: str | Unset = UNSET,
    result_field_data_path_startswith: str | Unset = UNSET,
    result_field_file_format: str | Unset = UNSET,
    result_field_file_format_contains: str | Unset = UNSET,
    result_field_gt: int | Unset = UNSET,
    result_field_gte: int | Unset = UNSET,
    result_field_in: list[int] | Unset = UNSET,
    result_field_isnull: bool | Unset = UNSET,
    result_field_lt: int | Unset = UNSET,
    result_field_lte: int | Unset = UNSET,
    result_field_storage_location: ObservationsListStorageLocation | Unset = UNSET,
    result_field_storage_status: ObservationsListStorageStatus | Unset = UNSET,
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
    status: ObservationsListDataStatus | Unset = UNSET,
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
    submission_user_id: str | Unset = UNSET,
    submission_user_id_contains: str | Unset = UNSET,
    submission_user_id_endswith: str | Unset = UNSET,
    submission_user_id_gt: str | Unset = UNSET,
    submission_user_id_gte: str | Unset = UNSET,
    submission_user_id_icontains: str | Unset = UNSET,
    submission_user_id_iendswith: str | Unset = UNSET,
    submission_user_id_iexact: str | Unset = UNSET,
    submission_user_id_in: list[str] | Unset = UNSET,
    submission_user_id_iregex: str | Unset = UNSET,
    submission_user_id_isnull: bool | Unset = UNSET,
    submission_user_id_istartswith: str | Unset = UNSET,
    submission_user_id_lt: str | Unset = UNSET,
    submission_user_id_lte: str | Unset = UNSET,
    submission_user_id_range: list[str] | Unset = UNSET,
    submission_user_id_regex: str | Unset = UNSET,
    submission_user_id_startswith: str | Unset = UNSET,
    time_period: int | Unset = UNSET,
    time_period_end_time: datetime.datetime | Unset = UNSET,
    time_period_end_time_gt: datetime.datetime | Unset = UNSET,
    time_period_end_time_gte: datetime.datetime | Unset = UNSET,
    time_period_end_time_lt: datetime.datetime | Unset = UNSET,
    time_period_end_time_lte: datetime.datetime | Unset = UNSET,
    time_period_end_time_range: list[datetime.datetime] | Unset = UNSET,
    time_period_gt: int | Unset = UNSET,
    time_period_gte: int | Unset = UNSET,
    time_period_in: list[int] | Unset = UNSET,
    time_period_isnull: bool | Unset = UNSET,
    time_period_lt: int | Unset = UNSET,
    time_period_lte: int | Unset = UNSET,
    time_period_ob_id: int | Unset = UNSET,
    time_period_ob_id_in: list[int] | Unset = UNSET,
    time_period_start_time: datetime.datetime | Unset = UNSET,
    time_period_start_time_gt: datetime.datetime | Unset = UNSET,
    time_period_start_time_gte: datetime.datetime | Unset = UNSET,
    time_period_start_time_lt: datetime.datetime | Unset = UNSET,
    time_period_start_time_lte: datetime.datetime | Unset = UNSET,
    time_period_start_time_range: list[datetime.datetime] | Unset = UNSET,
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
    update_frequency: ObservationsListDataUpdateFrequency | Unset = UNSET,
    update_frequency_contains: str | Unset = UNSET,
    update_frequency_endswith: str | Unset = UNSET,
    update_frequency_gt: str | Unset = UNSET,
    update_frequency_gte: str | Unset = UNSET,
    update_frequency_icontains: str | Unset = UNSET,
    update_frequency_iendswith: str | Unset = UNSET,
    update_frequency_iexact: str | Unset = UNSET,
    update_frequency_in: list[str] | Unset = UNSET,
    update_frequency_iregex: str | Unset = UNSET,
    update_frequency_isnull: bool | Unset = UNSET,
    update_frequency_istartswith: str | Unset = UNSET,
    update_frequency_lt: str | Unset = UNSET,
    update_frequency_lte: str | Unset = UNSET,
    update_frequency_range: list[str] | Unset = UNSET,
    update_frequency_regex: str | Unset = UNSET,
    update_frequency_startswith: str | Unset = UNSET,
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
    valid_time_period: int | Unset = UNSET,
    valid_time_period_gt: int | Unset = UNSET,
    valid_time_period_gte: int | Unset = UNSET,
    valid_time_period_in: list[int] | Unset = UNSET,
    valid_time_period_isnull: bool | Unset = UNSET,
    valid_time_period_lt: int | Unset = UNSET,
    valid_time_period_lte: int | Unset = UNSET,
    vertical_extent: int | Unset = UNSET,
    vertical_extent_gt: int | Unset = UNSET,
    vertical_extent_gte: int | Unset = UNSET,
    vertical_extent_in: list[int] | Unset = UNSET,
    vertical_extent_isnull: bool | Unset = UNSET,
    vertical_extent_lt: int | Unset = UNSET,
    vertical_extent_lte: int | Unset = UNSET,
) -> Response[PaginatedObservationReadList]:
    """Get a list of Observation objects.

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
        creation_date (datetime.datetime | Unset):
        creation_date_contained_by (datetime.datetime | Unset):
        creation_date_contains (datetime.datetime | Unset):
        creation_date_date (datetime.date | Unset):
        creation_date_day (float | Unset):
        creation_date_endswith (datetime.datetime | Unset):
        creation_date_gt (datetime.datetime | Unset):
        creation_date_gte (datetime.datetime | Unset):
        creation_date_hour (float | Unset):
        creation_date_icontains (datetime.datetime | Unset):
        creation_date_iendswith (datetime.datetime | Unset):
        creation_date_iexact (datetime.datetime | Unset):
        creation_date_in (list[datetime.datetime] | Unset):
        creation_date_iregex (datetime.datetime | Unset):
        creation_date_isnull (bool | Unset):
        creation_date_iso_week_day (float | Unset):
        creation_date_iso_year (float | Unset):
        creation_date_istartswith (datetime.datetime | Unset):
        creation_date_lt (datetime.datetime | Unset):
        creation_date_lte (datetime.datetime | Unset):
        creation_date_minute (float | Unset):
        creation_date_month (float | Unset):
        creation_date_quarter (float | Unset):
        creation_date_range (list[datetime.datetime] | Unset):
        creation_date_regex (datetime.datetime | Unset):
        creation_date_second (float | Unset):
        creation_date_startswith (datetime.datetime | Unset):
        creation_date_time (str | Unset):
        creation_date_week (float | Unset):
        creation_date_week_day (float | Unset):
        creation_date_year (float | Unset):
        data_lineage (str | Unset):
        data_lineage_contains (str | Unset):
        data_lineage_endswith (str | Unset):
        data_lineage_gt (str | Unset):
        data_lineage_gte (str | Unset):
        data_lineage_icontains (str | Unset):
        data_lineage_iendswith (str | Unset):
        data_lineage_iexact (str | Unset):
        data_lineage_in (list[str] | Unset):
        data_lineage_iregex (str | Unset):
        data_lineage_isnull (bool | Unset):
        data_lineage_istartswith (str | Unset):
        data_lineage_lt (str | Unset):
        data_lineage_lte (str | Unset):
        data_lineage_range (list[str] | Unset):
        data_lineage_regex (str | Unset):
        data_lineage_startswith (str | Unset):
        data_published_time (datetime.datetime | Unset):
        data_published_time_contained_by (datetime.datetime | Unset):
        data_published_time_contains (datetime.datetime | Unset):
        data_published_time_date (datetime.date | Unset):
        data_published_time_day (float | Unset):
        data_published_time_endswith (datetime.datetime | Unset):
        data_published_time_gt (datetime.datetime | Unset):
        data_published_time_gte (datetime.datetime | Unset):
        data_published_time_hour (float | Unset):
        data_published_time_icontains (datetime.datetime | Unset):
        data_published_time_iendswith (datetime.datetime | Unset):
        data_published_time_iexact (datetime.datetime | Unset):
        data_published_time_in (list[datetime.datetime] | Unset):
        data_published_time_iregex (datetime.datetime | Unset):
        data_published_time_isnull (bool | Unset):
        data_published_time_iso_week_day (float | Unset):
        data_published_time_iso_year (float | Unset):
        data_published_time_istartswith (datetime.datetime | Unset):
        data_published_time_lt (datetime.datetime | Unset):
        data_published_time_lte (datetime.datetime | Unset):
        data_published_time_minute (float | Unset):
        data_published_time_month (float | Unset):
        data_published_time_quarter (float | Unset):
        data_published_time_range (list[datetime.datetime] | Unset):
        data_published_time_regex (datetime.datetime | Unset):
        data_published_time_second (float | Unset):
        data_published_time_startswith (datetime.datetime | Unset):
        data_published_time_time (str | Unset):
        data_published_time_week (float | Unset):
        data_published_time_week_day (float | Unset):
        data_published_time_year (float | Unset):
        discovery_keywords_name (str | Unset):
        discovery_keywords_name_contains (str | Unset):
        doi_published_time (datetime.datetime | Unset):
        doi_published_time_contained_by (datetime.datetime | Unset):
        doi_published_time_contains (datetime.datetime | Unset):
        doi_published_time_date (datetime.date | Unset):
        doi_published_time_day (float | Unset):
        doi_published_time_endswith (datetime.datetime | Unset):
        doi_published_time_gt (datetime.datetime | Unset):
        doi_published_time_gte (datetime.datetime | Unset):
        doi_published_time_hour (float | Unset):
        doi_published_time_icontains (datetime.datetime | Unset):
        doi_published_time_iendswith (datetime.datetime | Unset):
        doi_published_time_iexact (datetime.datetime | Unset):
        doi_published_time_in (list[datetime.datetime] | Unset):
        doi_published_time_iregex (datetime.datetime | Unset):
        doi_published_time_isnull (bool | Unset):
        doi_published_time_iso_week_day (float | Unset):
        doi_published_time_iso_year (float | Unset):
        doi_published_time_istartswith (datetime.datetime | Unset):
        doi_published_time_lt (datetime.datetime | Unset):
        doi_published_time_lte (datetime.datetime | Unset):
        doi_published_time_minute (float | Unset):
        doi_published_time_month (float | Unset):
        doi_published_time_quarter (float | Unset):
        doi_published_time_range (list[datetime.datetime] | Unset):
        doi_published_time_regex (datetime.datetime | Unset):
        doi_published_time_second (float | Unset):
        doi_published_time_startswith (datetime.datetime | Unset):
        doi_published_time_time (str | Unset):
        doi_published_time_week (float | Unset):
        doi_published_time_week_day (float | Unset):
        doi_published_time_year (float | Unset):
        dont_harvest_from_projects (bool | Unset):
        dont_harvest_from_projects_contains (bool | Unset):
        dont_harvest_from_projects_endswith (bool | Unset):
        dont_harvest_from_projects_gt (bool | Unset):
        dont_harvest_from_projects_gte (bool | Unset):
        dont_harvest_from_projects_icontains (bool | Unset):
        dont_harvest_from_projects_iendswith (bool | Unset):
        dont_harvest_from_projects_iexact (bool | Unset):
        dont_harvest_from_projects_in (list[bool] | Unset):
        dont_harvest_from_projects_iregex (bool | Unset):
        dont_harvest_from_projects_isnull (bool | Unset):
        dont_harvest_from_projects_istartswith (bool | Unset):
        dont_harvest_from_projects_lt (bool | Unset):
        dont_harvest_from_projects_lte (bool | Unset):
        dont_harvest_from_projects_range (list[bool] | Unset):
        dont_harvest_from_projects_regex (bool | Unset):
        dont_harvest_from_projects_startswith (bool | Unset):
        feature_of_interest (str | Unset):
        feature_of_interest_contains (str | Unset):
        feature_of_interest_endswith (str | Unset):
        feature_of_interest_gt (str | Unset):
        feature_of_interest_gte (str | Unset):
        feature_of_interest_icontains (str | Unset):
        feature_of_interest_iendswith (str | Unset):
        feature_of_interest_iexact (str | Unset):
        feature_of_interest_in (list[str] | Unset):
        feature_of_interest_iregex (str | Unset):
        feature_of_interest_isnull (bool | Unset):
        feature_of_interest_istartswith (str | Unset):
        feature_of_interest_lt (str | Unset):
        feature_of_interest_lte (str | Unset):
        feature_of_interest_range (list[str] | Unset):
        feature_of_interest_regex (str | Unset):
        feature_of_interest_startswith (str | Unset):
        geographic_extent (int | Unset):
        geographic_extent_east_bound_longitude (float | Unset):
        geographic_extent_east_bound_longitude_gt (float | Unset):
        geographic_extent_east_bound_longitude_gte (float | Unset):
        geographic_extent_east_bound_longitude_lt (float | Unset):
        geographic_extent_east_bound_longitude_lte (float | Unset):
        geographic_extent_east_bound_longitude_range (list[float] | Unset):
        geographic_extent_gt (int | Unset):
        geographic_extent_gte (int | Unset):
        geographic_extent_in (list[int] | Unset):
        geographic_extent_isnull (bool | Unset):
        geographic_extent_lt (int | Unset):
        geographic_extent_lte (int | Unset):
        geographic_extent_north_bound_latitude (float | Unset):
        geographic_extent_north_bound_latitude_gt (float | Unset):
        geographic_extent_north_bound_latitude_gte (float | Unset):
        geographic_extent_north_bound_latitude_lt (float | Unset):
        geographic_extent_north_bound_latitude_lte (float | Unset):
        geographic_extent_north_bound_latitude_range (list[float] | Unset):
        geographic_extent_ob_id (int | Unset):
        geographic_extent_ob_id_in (list[int] | Unset):
        geographic_extent_south_bound_latitude (float | Unset):
        geographic_extent_south_bound_latitude_gt (float | Unset):
        geographic_extent_south_bound_latitude_gte (float | Unset):
        geographic_extent_south_bound_latitude_lt (float | Unset):
        geographic_extent_south_bound_latitude_lte (float | Unset):
        geographic_extent_south_bound_latitude_range (list[float] | Unset):
        geographic_extent_west_bound_longitude (float | Unset):
        geographic_extent_west_bound_longitude_gt (float | Unset):
        geographic_extent_west_bound_longitude_gte (float | Unset):
        geographic_extent_west_bound_longitude_lt (float | Unset):
        geographic_extent_west_bound_longitude_lte (float | Unset):
        geographic_extent_west_bound_longitude_range (list[float] | Unset):
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
        language (ObservationsListLanguage | Unset):
        language_contains (str | Unset):
        language_endswith (str | Unset):
        language_gt (str | Unset):
        language_gte (str | Unset):
        language_icontains (str | Unset):
        language_iendswith (str | Unset):
        language_iexact (str | Unset):
        language_in (list[str] | Unset):
        language_iregex (str | Unset):
        language_isnull (bool | Unset):
        language_istartswith (str | Unset):
        language_lt (str | Unset):
        language_lte (str | Unset):
        language_range (list[str] | Unset):
        language_regex (str | Unset):
        language_startswith (str | Unset):
        last_updated_date (datetime.datetime | Unset):
        last_updated_date_contained_by (datetime.datetime | Unset):
        last_updated_date_contains (datetime.datetime | Unset):
        last_updated_date_date (datetime.date | Unset):
        last_updated_date_day (float | Unset):
        last_updated_date_endswith (datetime.datetime | Unset):
        last_updated_date_gt (datetime.datetime | Unset):
        last_updated_date_gte (datetime.datetime | Unset):
        last_updated_date_hour (float | Unset):
        last_updated_date_icontains (datetime.datetime | Unset):
        last_updated_date_iendswith (datetime.datetime | Unset):
        last_updated_date_iexact (datetime.datetime | Unset):
        last_updated_date_in (list[datetime.datetime] | Unset):
        last_updated_date_iregex (datetime.datetime | Unset):
        last_updated_date_isnull (bool | Unset):
        last_updated_date_iso_week_day (float | Unset):
        last_updated_date_iso_year (float | Unset):
        last_updated_date_istartswith (datetime.datetime | Unset):
        last_updated_date_lt (datetime.datetime | Unset):
        last_updated_date_lte (datetime.datetime | Unset):
        last_updated_date_minute (float | Unset):
        last_updated_date_month (float | Unset):
        last_updated_date_quarter (float | Unset):
        last_updated_date_range (list[datetime.datetime] | Unset):
        last_updated_date_regex (datetime.datetime | Unset):
        last_updated_date_second (float | Unset):
        last_updated_date_startswith (datetime.datetime | Unset):
        last_updated_date_time (str | Unset):
        last_updated_date_week (float | Unset):
        last_updated_date_week_day (float | Unset):
        last_updated_date_year (float | Unset):
        latest_data_update_time (datetime.datetime | Unset):
        latest_data_update_time_contained_by (datetime.datetime | Unset):
        latest_data_update_time_contains (datetime.datetime | Unset):
        latest_data_update_time_date (datetime.date | Unset):
        latest_data_update_time_day (float | Unset):
        latest_data_update_time_endswith (datetime.datetime | Unset):
        latest_data_update_time_gt (datetime.datetime | Unset):
        latest_data_update_time_gte (datetime.datetime | Unset):
        latest_data_update_time_hour (float | Unset):
        latest_data_update_time_icontains (datetime.datetime | Unset):
        latest_data_update_time_iendswith (datetime.datetime | Unset):
        latest_data_update_time_iexact (datetime.datetime | Unset):
        latest_data_update_time_in (list[datetime.datetime] | Unset):
        latest_data_update_time_iregex (datetime.datetime | Unset):
        latest_data_update_time_isnull (bool | Unset):
        latest_data_update_time_iso_week_day (float | Unset):
        latest_data_update_time_iso_year (float | Unset):
        latest_data_update_time_istartswith (datetime.datetime | Unset):
        latest_data_update_time_lt (datetime.datetime | Unset):
        latest_data_update_time_lte (datetime.datetime | Unset):
        latest_data_update_time_minute (float | Unset):
        latest_data_update_time_month (float | Unset):
        latest_data_update_time_quarter (float | Unset):
        latest_data_update_time_range (list[datetime.datetime] | Unset):
        latest_data_update_time_regex (datetime.datetime | Unset):
        latest_data_update_time_second (float | Unset):
        latest_data_update_time_startswith (datetime.datetime | Unset):
        latest_data_update_time_time (str | Unset):
        latest_data_update_time_week (float | Unset):
        latest_data_update_time_week_day (float | Unset):
        latest_data_update_time_year (float | Unset):
        limit (int | Unset):
        non_geographic_flag (bool | Unset):
        non_geographic_flag_contains (bool | Unset):
        non_geographic_flag_endswith (bool | Unset):
        non_geographic_flag_gt (bool | Unset):
        non_geographic_flag_gte (bool | Unset):
        non_geographic_flag_icontains (bool | Unset):
        non_geographic_flag_iendswith (bool | Unset):
        non_geographic_flag_iexact (bool | Unset):
        non_geographic_flag_in (list[bool] | Unset):
        non_geographic_flag_iregex (bool | Unset):
        non_geographic_flag_isnull (bool | Unset):
        non_geographic_flag_istartswith (bool | Unset):
        non_geographic_flag_lt (bool | Unset):
        non_geographic_flag_lte (bool | Unset):
        non_geographic_flag_range (list[bool] | Unset):
        non_geographic_flag_regex (bool | Unset):
        non_geographic_flag_startswith (bool | Unset):
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
        permissions_access_category (ObservationsListAccessCategory | Unset):
        permissions_access_category_in (list[str] | Unset):
        permissions_access_roles (str | Unset):
        permissions_access_roles_in (list[str] | Unset):
        procedure_acquisition (int | Unset):
        procedure_acquisition_gt (int | Unset):
        procedure_acquisition_gte (int | Unset):
        procedure_acquisition_in (list[int] | Unset):
        procedure_acquisition_isnull (bool | Unset):
        procedure_acquisition_lt (int | Unset):
        procedure_acquisition_lte (int | Unset):
        procedure_acquisition_ob_id (int | Unset):
        procedure_acquisition_ob_id_in (list[int] | Unset):
        procedure_acquisition_uuid (str | Unset):
        procedure_acquisition_uuid_in (list[str] | Unset):
        procedure_composite_process (int | Unset):
        procedure_composite_process_gt (int | Unset):
        procedure_composite_process_gte (int | Unset):
        procedure_composite_process_in (list[int] | Unset):
        procedure_composite_process_isnull (bool | Unset):
        procedure_composite_process_lt (int | Unset):
        procedure_composite_process_lte (int | Unset):
        procedure_computation (int | Unset):
        procedure_computation_gt (int | Unset):
        procedure_computation_gte (int | Unset):
        procedure_computation_in (list[int] | Unset):
        procedure_computation_isnull (bool | Unset):
        procedure_computation_lt (int | Unset):
        procedure_computation_lte (int | Unset):
        procedure_description (str | Unset):
        procedure_description_contains (str | Unset):
        procedure_description_endswith (str | Unset):
        procedure_description_gt (str | Unset):
        procedure_description_gte (str | Unset):
        procedure_description_icontains (str | Unset):
        procedure_description_iendswith (str | Unset):
        procedure_description_iexact (str | Unset):
        procedure_description_in (list[str] | Unset):
        procedure_description_iregex (str | Unset):
        procedure_description_isnull (bool | Unset):
        procedure_description_istartswith (str | Unset):
        procedure_description_lt (str | Unset):
        procedure_description_lte (str | Unset):
        procedure_description_range (list[str] | Unset):
        procedure_description_regex (str | Unset):
        procedure_description_startswith (str | Unset):
        projects_ob_id (int | Unset):
        projects_ob_id_in (list[int] | Unset):
        projects_uuid (str | Unset):
        projects_uuid_in (list[str] | Unset):
        publication_state (ObservationsListPublicationState | Unset):
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
        removed_data_reason (str | Unset):
        removed_data_reason_contains (str | Unset):
        removed_data_reason_endswith (str | Unset):
        removed_data_reason_gt (str | Unset):
        removed_data_reason_gte (str | Unset):
        removed_data_reason_icontains (str | Unset):
        removed_data_reason_iendswith (str | Unset):
        removed_data_reason_iexact (str | Unset):
        removed_data_reason_in (list[str] | Unset):
        removed_data_reason_iregex (str | Unset):
        removed_data_reason_isnull (bool | Unset):
        removed_data_reason_istartswith (str | Unset):
        removed_data_reason_lt (str | Unset):
        removed_data_reason_lte (str | Unset):
        removed_data_reason_range (list[str] | Unset):
        removed_data_reason_regex (str | Unset):
        removed_data_reason_startswith (str | Unset):
        removed_data_time (datetime.datetime | Unset):
        removed_data_time_contained_by (datetime.datetime | Unset):
        removed_data_time_contains (datetime.datetime | Unset):
        removed_data_time_date (datetime.date | Unset):
        removed_data_time_day (float | Unset):
        removed_data_time_endswith (datetime.datetime | Unset):
        removed_data_time_gt (datetime.datetime | Unset):
        removed_data_time_gte (datetime.datetime | Unset):
        removed_data_time_hour (float | Unset):
        removed_data_time_icontains (datetime.datetime | Unset):
        removed_data_time_iendswith (datetime.datetime | Unset):
        removed_data_time_iexact (datetime.datetime | Unset):
        removed_data_time_in (list[datetime.datetime] | Unset):
        removed_data_time_iregex (datetime.datetime | Unset):
        removed_data_time_isnull (bool | Unset):
        removed_data_time_iso_week_day (float | Unset):
        removed_data_time_iso_year (float | Unset):
        removed_data_time_istartswith (datetime.datetime | Unset):
        removed_data_time_lt (datetime.datetime | Unset):
        removed_data_time_lte (datetime.datetime | Unset):
        removed_data_time_minute (float | Unset):
        removed_data_time_month (float | Unset):
        removed_data_time_quarter (float | Unset):
        removed_data_time_range (list[datetime.datetime] | Unset):
        removed_data_time_regex (datetime.datetime | Unset):
        removed_data_time_second (float | Unset):
        removed_data_time_startswith (datetime.datetime | Unset):
        removed_data_time_time (str | Unset):
        removed_data_time_week (float | Unset):
        removed_data_time_week_day (float | Unset):
        removed_data_time_year (float | Unset):
        resolution (str | Unset):
        resolution_contains (str | Unset):
        resolution_endswith (str | Unset):
        resolution_gt (str | Unset):
        resolution_gte (str | Unset):
        resolution_icontains (str | Unset):
        resolution_iendswith (str | Unset):
        resolution_iexact (str | Unset):
        resolution_in (list[str] | Unset):
        resolution_iregex (str | Unset):
        resolution_isnull (bool | Unset):
        resolution_istartswith (str | Unset):
        resolution_lt (str | Unset):
        resolution_lte (str | Unset):
        resolution_range (list[str] | Unset):
        resolution_regex (str | Unset):
        resolution_startswith (str | Unset):
        result_quality (int | Unset):
        result_quality_date (datetime.date | Unset):
        result_quality_date_gt (datetime.date | Unset):
        result_quality_date_gte (datetime.date | Unset):
        result_quality_date_lt (datetime.date | Unset):
        result_quality_date_lte (datetime.date | Unset):
        result_quality_date_range (list[datetime.date] | Unset):
        result_quality_explanation (str | Unset):
        result_quality_explanation_contains (str | Unset):
        result_quality_gt (int | Unset):
        result_quality_gte (int | Unset):
        result_quality_in (list[int] | Unset):
        result_quality_isnull (bool | Unset):
        result_quality_lt (int | Unset):
        result_quality_lte (int | Unset):
        result_quality_ob_id (int | Unset):
        result_quality_ob_id_in (list[int] | Unset):
        result_quality_passes_test (bool | Unset):
        result_quality_result_title (str | Unset):
        result_quality_result_title_contains (str | Unset):
        result_field (int | Unset):
        result_field_data_path (str | Unset):
        result_field_data_path_contains (str | Unset):
        result_field_data_path_startswith (str | Unset):
        result_field_file_format (str | Unset):
        result_field_file_format_contains (str | Unset):
        result_field_gt (int | Unset):
        result_field_gte (int | Unset):
        result_field_in (list[int] | Unset):
        result_field_isnull (bool | Unset):
        result_field_lt (int | Unset):
        result_field_lte (int | Unset):
        result_field_storage_location (ObservationsListStorageLocation | Unset):
        result_field_storage_status (ObservationsListStorageStatus | Unset):
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
        status (ObservationsListDataStatus | Unset):
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
        submission_user_id (str | Unset):
        submission_user_id_contains (str | Unset):
        submission_user_id_endswith (str | Unset):
        submission_user_id_gt (str | Unset):
        submission_user_id_gte (str | Unset):
        submission_user_id_icontains (str | Unset):
        submission_user_id_iendswith (str | Unset):
        submission_user_id_iexact (str | Unset):
        submission_user_id_in (list[str] | Unset):
        submission_user_id_iregex (str | Unset):
        submission_user_id_isnull (bool | Unset):
        submission_user_id_istartswith (str | Unset):
        submission_user_id_lt (str | Unset):
        submission_user_id_lte (str | Unset):
        submission_user_id_range (list[str] | Unset):
        submission_user_id_regex (str | Unset):
        submission_user_id_startswith (str | Unset):
        time_period (int | Unset):
        time_period_end_time (datetime.datetime | Unset):
        time_period_end_time_gt (datetime.datetime | Unset):
        time_period_end_time_gte (datetime.datetime | Unset):
        time_period_end_time_lt (datetime.datetime | Unset):
        time_period_end_time_lte (datetime.datetime | Unset):
        time_period_end_time_range (list[datetime.datetime] | Unset):
        time_period_gt (int | Unset):
        time_period_gte (int | Unset):
        time_period_in (list[int] | Unset):
        time_period_isnull (bool | Unset):
        time_period_lt (int | Unset):
        time_period_lte (int | Unset):
        time_period_ob_id (int | Unset):
        time_period_ob_id_in (list[int] | Unset):
        time_period_start_time (datetime.datetime | Unset):
        time_period_start_time_gt (datetime.datetime | Unset):
        time_period_start_time_gte (datetime.datetime | Unset):
        time_period_start_time_lt (datetime.datetime | Unset):
        time_period_start_time_lte (datetime.datetime | Unset):
        time_period_start_time_range (list[datetime.datetime] | Unset):
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
        update_frequency (ObservationsListDataUpdateFrequency | Unset):
        update_frequency_contains (str | Unset):
        update_frequency_endswith (str | Unset):
        update_frequency_gt (str | Unset):
        update_frequency_gte (str | Unset):
        update_frequency_icontains (str | Unset):
        update_frequency_iendswith (str | Unset):
        update_frequency_iexact (str | Unset):
        update_frequency_in (list[str] | Unset):
        update_frequency_iregex (str | Unset):
        update_frequency_isnull (bool | Unset):
        update_frequency_istartswith (str | Unset):
        update_frequency_lt (str | Unset):
        update_frequency_lte (str | Unset):
        update_frequency_range (list[str] | Unset):
        update_frequency_regex (str | Unset):
        update_frequency_startswith (str | Unset):
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
        valid_time_period (int | Unset):
        valid_time_period_gt (int | Unset):
        valid_time_period_gte (int | Unset):
        valid_time_period_in (list[int] | Unset):
        valid_time_period_isnull (bool | Unset):
        valid_time_period_lt (int | Unset):
        valid_time_period_lte (int | Unset):
        vertical_extent (int | Unset):
        vertical_extent_gt (int | Unset):
        vertical_extent_gte (int | Unset):
        vertical_extent_in (list[int] | Unset):
        vertical_extent_isnull (bool | Unset):
        vertical_extent_lt (int | Unset):
        vertical_extent_lte (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedObservationReadList]
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
        creation_date=creation_date,
        creation_date_contained_by=creation_date_contained_by,
        creation_date_contains=creation_date_contains,
        creation_date_date=creation_date_date,
        creation_date_day=creation_date_day,
        creation_date_endswith=creation_date_endswith,
        creation_date_gt=creation_date_gt,
        creation_date_gte=creation_date_gte,
        creation_date_hour=creation_date_hour,
        creation_date_icontains=creation_date_icontains,
        creation_date_iendswith=creation_date_iendswith,
        creation_date_iexact=creation_date_iexact,
        creation_date_in=creation_date_in,
        creation_date_iregex=creation_date_iregex,
        creation_date_isnull=creation_date_isnull,
        creation_date_iso_week_day=creation_date_iso_week_day,
        creation_date_iso_year=creation_date_iso_year,
        creation_date_istartswith=creation_date_istartswith,
        creation_date_lt=creation_date_lt,
        creation_date_lte=creation_date_lte,
        creation_date_minute=creation_date_minute,
        creation_date_month=creation_date_month,
        creation_date_quarter=creation_date_quarter,
        creation_date_range=creation_date_range,
        creation_date_regex=creation_date_regex,
        creation_date_second=creation_date_second,
        creation_date_startswith=creation_date_startswith,
        creation_date_time=creation_date_time,
        creation_date_week=creation_date_week,
        creation_date_week_day=creation_date_week_day,
        creation_date_year=creation_date_year,
        data_lineage=data_lineage,
        data_lineage_contains=data_lineage_contains,
        data_lineage_endswith=data_lineage_endswith,
        data_lineage_gt=data_lineage_gt,
        data_lineage_gte=data_lineage_gte,
        data_lineage_icontains=data_lineage_icontains,
        data_lineage_iendswith=data_lineage_iendswith,
        data_lineage_iexact=data_lineage_iexact,
        data_lineage_in=data_lineage_in,
        data_lineage_iregex=data_lineage_iregex,
        data_lineage_isnull=data_lineage_isnull,
        data_lineage_istartswith=data_lineage_istartswith,
        data_lineage_lt=data_lineage_lt,
        data_lineage_lte=data_lineage_lte,
        data_lineage_range=data_lineage_range,
        data_lineage_regex=data_lineage_regex,
        data_lineage_startswith=data_lineage_startswith,
        data_published_time=data_published_time,
        data_published_time_contained_by=data_published_time_contained_by,
        data_published_time_contains=data_published_time_contains,
        data_published_time_date=data_published_time_date,
        data_published_time_day=data_published_time_day,
        data_published_time_endswith=data_published_time_endswith,
        data_published_time_gt=data_published_time_gt,
        data_published_time_gte=data_published_time_gte,
        data_published_time_hour=data_published_time_hour,
        data_published_time_icontains=data_published_time_icontains,
        data_published_time_iendswith=data_published_time_iendswith,
        data_published_time_iexact=data_published_time_iexact,
        data_published_time_in=data_published_time_in,
        data_published_time_iregex=data_published_time_iregex,
        data_published_time_isnull=data_published_time_isnull,
        data_published_time_iso_week_day=data_published_time_iso_week_day,
        data_published_time_iso_year=data_published_time_iso_year,
        data_published_time_istartswith=data_published_time_istartswith,
        data_published_time_lt=data_published_time_lt,
        data_published_time_lte=data_published_time_lte,
        data_published_time_minute=data_published_time_minute,
        data_published_time_month=data_published_time_month,
        data_published_time_quarter=data_published_time_quarter,
        data_published_time_range=data_published_time_range,
        data_published_time_regex=data_published_time_regex,
        data_published_time_second=data_published_time_second,
        data_published_time_startswith=data_published_time_startswith,
        data_published_time_time=data_published_time_time,
        data_published_time_week=data_published_time_week,
        data_published_time_week_day=data_published_time_week_day,
        data_published_time_year=data_published_time_year,
        discovery_keywords_name=discovery_keywords_name,
        discovery_keywords_name_contains=discovery_keywords_name_contains,
        doi_published_time=doi_published_time,
        doi_published_time_contained_by=doi_published_time_contained_by,
        doi_published_time_contains=doi_published_time_contains,
        doi_published_time_date=doi_published_time_date,
        doi_published_time_day=doi_published_time_day,
        doi_published_time_endswith=doi_published_time_endswith,
        doi_published_time_gt=doi_published_time_gt,
        doi_published_time_gte=doi_published_time_gte,
        doi_published_time_hour=doi_published_time_hour,
        doi_published_time_icontains=doi_published_time_icontains,
        doi_published_time_iendswith=doi_published_time_iendswith,
        doi_published_time_iexact=doi_published_time_iexact,
        doi_published_time_in=doi_published_time_in,
        doi_published_time_iregex=doi_published_time_iregex,
        doi_published_time_isnull=doi_published_time_isnull,
        doi_published_time_iso_week_day=doi_published_time_iso_week_day,
        doi_published_time_iso_year=doi_published_time_iso_year,
        doi_published_time_istartswith=doi_published_time_istartswith,
        doi_published_time_lt=doi_published_time_lt,
        doi_published_time_lte=doi_published_time_lte,
        doi_published_time_minute=doi_published_time_minute,
        doi_published_time_month=doi_published_time_month,
        doi_published_time_quarter=doi_published_time_quarter,
        doi_published_time_range=doi_published_time_range,
        doi_published_time_regex=doi_published_time_regex,
        doi_published_time_second=doi_published_time_second,
        doi_published_time_startswith=doi_published_time_startswith,
        doi_published_time_time=doi_published_time_time,
        doi_published_time_week=doi_published_time_week,
        doi_published_time_week_day=doi_published_time_week_day,
        doi_published_time_year=doi_published_time_year,
        dont_harvest_from_projects=dont_harvest_from_projects,
        dont_harvest_from_projects_contains=dont_harvest_from_projects_contains,
        dont_harvest_from_projects_endswith=dont_harvest_from_projects_endswith,
        dont_harvest_from_projects_gt=dont_harvest_from_projects_gt,
        dont_harvest_from_projects_gte=dont_harvest_from_projects_gte,
        dont_harvest_from_projects_icontains=dont_harvest_from_projects_icontains,
        dont_harvest_from_projects_iendswith=dont_harvest_from_projects_iendswith,
        dont_harvest_from_projects_iexact=dont_harvest_from_projects_iexact,
        dont_harvest_from_projects_in=dont_harvest_from_projects_in,
        dont_harvest_from_projects_iregex=dont_harvest_from_projects_iregex,
        dont_harvest_from_projects_isnull=dont_harvest_from_projects_isnull,
        dont_harvest_from_projects_istartswith=dont_harvest_from_projects_istartswith,
        dont_harvest_from_projects_lt=dont_harvest_from_projects_lt,
        dont_harvest_from_projects_lte=dont_harvest_from_projects_lte,
        dont_harvest_from_projects_range=dont_harvest_from_projects_range,
        dont_harvest_from_projects_regex=dont_harvest_from_projects_regex,
        dont_harvest_from_projects_startswith=dont_harvest_from_projects_startswith,
        feature_of_interest=feature_of_interest,
        feature_of_interest_contains=feature_of_interest_contains,
        feature_of_interest_endswith=feature_of_interest_endswith,
        feature_of_interest_gt=feature_of_interest_gt,
        feature_of_interest_gte=feature_of_interest_gte,
        feature_of_interest_icontains=feature_of_interest_icontains,
        feature_of_interest_iendswith=feature_of_interest_iendswith,
        feature_of_interest_iexact=feature_of_interest_iexact,
        feature_of_interest_in=feature_of_interest_in,
        feature_of_interest_iregex=feature_of_interest_iregex,
        feature_of_interest_isnull=feature_of_interest_isnull,
        feature_of_interest_istartswith=feature_of_interest_istartswith,
        feature_of_interest_lt=feature_of_interest_lt,
        feature_of_interest_lte=feature_of_interest_lte,
        feature_of_interest_range=feature_of_interest_range,
        feature_of_interest_regex=feature_of_interest_regex,
        feature_of_interest_startswith=feature_of_interest_startswith,
        geographic_extent=geographic_extent,
        geographic_extent_east_bound_longitude=geographic_extent_east_bound_longitude,
        geographic_extent_east_bound_longitude_gt=geographic_extent_east_bound_longitude_gt,
        geographic_extent_east_bound_longitude_gte=geographic_extent_east_bound_longitude_gte,
        geographic_extent_east_bound_longitude_lt=geographic_extent_east_bound_longitude_lt,
        geographic_extent_east_bound_longitude_lte=geographic_extent_east_bound_longitude_lte,
        geographic_extent_east_bound_longitude_range=geographic_extent_east_bound_longitude_range,
        geographic_extent_gt=geographic_extent_gt,
        geographic_extent_gte=geographic_extent_gte,
        geographic_extent_in=geographic_extent_in,
        geographic_extent_isnull=geographic_extent_isnull,
        geographic_extent_lt=geographic_extent_lt,
        geographic_extent_lte=geographic_extent_lte,
        geographic_extent_north_bound_latitude=geographic_extent_north_bound_latitude,
        geographic_extent_north_bound_latitude_gt=geographic_extent_north_bound_latitude_gt,
        geographic_extent_north_bound_latitude_gte=geographic_extent_north_bound_latitude_gte,
        geographic_extent_north_bound_latitude_lt=geographic_extent_north_bound_latitude_lt,
        geographic_extent_north_bound_latitude_lte=geographic_extent_north_bound_latitude_lte,
        geographic_extent_north_bound_latitude_range=geographic_extent_north_bound_latitude_range,
        geographic_extent_ob_id=geographic_extent_ob_id,
        geographic_extent_ob_id_in=geographic_extent_ob_id_in,
        geographic_extent_south_bound_latitude=geographic_extent_south_bound_latitude,
        geographic_extent_south_bound_latitude_gt=geographic_extent_south_bound_latitude_gt,
        geographic_extent_south_bound_latitude_gte=geographic_extent_south_bound_latitude_gte,
        geographic_extent_south_bound_latitude_lt=geographic_extent_south_bound_latitude_lt,
        geographic_extent_south_bound_latitude_lte=geographic_extent_south_bound_latitude_lte,
        geographic_extent_south_bound_latitude_range=geographic_extent_south_bound_latitude_range,
        geographic_extent_west_bound_longitude=geographic_extent_west_bound_longitude,
        geographic_extent_west_bound_longitude_gt=geographic_extent_west_bound_longitude_gt,
        geographic_extent_west_bound_longitude_gte=geographic_extent_west_bound_longitude_gte,
        geographic_extent_west_bound_longitude_lt=geographic_extent_west_bound_longitude_lt,
        geographic_extent_west_bound_longitude_lte=geographic_extent_west_bound_longitude_lte,
        geographic_extent_west_bound_longitude_range=geographic_extent_west_bound_longitude_range,
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
        language=language,
        language_contains=language_contains,
        language_endswith=language_endswith,
        language_gt=language_gt,
        language_gte=language_gte,
        language_icontains=language_icontains,
        language_iendswith=language_iendswith,
        language_iexact=language_iexact,
        language_in=language_in,
        language_iregex=language_iregex,
        language_isnull=language_isnull,
        language_istartswith=language_istartswith,
        language_lt=language_lt,
        language_lte=language_lte,
        language_range=language_range,
        language_regex=language_regex,
        language_startswith=language_startswith,
        last_updated_date=last_updated_date,
        last_updated_date_contained_by=last_updated_date_contained_by,
        last_updated_date_contains=last_updated_date_contains,
        last_updated_date_date=last_updated_date_date,
        last_updated_date_day=last_updated_date_day,
        last_updated_date_endswith=last_updated_date_endswith,
        last_updated_date_gt=last_updated_date_gt,
        last_updated_date_gte=last_updated_date_gte,
        last_updated_date_hour=last_updated_date_hour,
        last_updated_date_icontains=last_updated_date_icontains,
        last_updated_date_iendswith=last_updated_date_iendswith,
        last_updated_date_iexact=last_updated_date_iexact,
        last_updated_date_in=last_updated_date_in,
        last_updated_date_iregex=last_updated_date_iregex,
        last_updated_date_isnull=last_updated_date_isnull,
        last_updated_date_iso_week_day=last_updated_date_iso_week_day,
        last_updated_date_iso_year=last_updated_date_iso_year,
        last_updated_date_istartswith=last_updated_date_istartswith,
        last_updated_date_lt=last_updated_date_lt,
        last_updated_date_lte=last_updated_date_lte,
        last_updated_date_minute=last_updated_date_minute,
        last_updated_date_month=last_updated_date_month,
        last_updated_date_quarter=last_updated_date_quarter,
        last_updated_date_range=last_updated_date_range,
        last_updated_date_regex=last_updated_date_regex,
        last_updated_date_second=last_updated_date_second,
        last_updated_date_startswith=last_updated_date_startswith,
        last_updated_date_time=last_updated_date_time,
        last_updated_date_week=last_updated_date_week,
        last_updated_date_week_day=last_updated_date_week_day,
        last_updated_date_year=last_updated_date_year,
        latest_data_update_time=latest_data_update_time,
        latest_data_update_time_contained_by=latest_data_update_time_contained_by,
        latest_data_update_time_contains=latest_data_update_time_contains,
        latest_data_update_time_date=latest_data_update_time_date,
        latest_data_update_time_day=latest_data_update_time_day,
        latest_data_update_time_endswith=latest_data_update_time_endswith,
        latest_data_update_time_gt=latest_data_update_time_gt,
        latest_data_update_time_gte=latest_data_update_time_gte,
        latest_data_update_time_hour=latest_data_update_time_hour,
        latest_data_update_time_icontains=latest_data_update_time_icontains,
        latest_data_update_time_iendswith=latest_data_update_time_iendswith,
        latest_data_update_time_iexact=latest_data_update_time_iexact,
        latest_data_update_time_in=latest_data_update_time_in,
        latest_data_update_time_iregex=latest_data_update_time_iregex,
        latest_data_update_time_isnull=latest_data_update_time_isnull,
        latest_data_update_time_iso_week_day=latest_data_update_time_iso_week_day,
        latest_data_update_time_iso_year=latest_data_update_time_iso_year,
        latest_data_update_time_istartswith=latest_data_update_time_istartswith,
        latest_data_update_time_lt=latest_data_update_time_lt,
        latest_data_update_time_lte=latest_data_update_time_lte,
        latest_data_update_time_minute=latest_data_update_time_minute,
        latest_data_update_time_month=latest_data_update_time_month,
        latest_data_update_time_quarter=latest_data_update_time_quarter,
        latest_data_update_time_range=latest_data_update_time_range,
        latest_data_update_time_regex=latest_data_update_time_regex,
        latest_data_update_time_second=latest_data_update_time_second,
        latest_data_update_time_startswith=latest_data_update_time_startswith,
        latest_data_update_time_time=latest_data_update_time_time,
        latest_data_update_time_week=latest_data_update_time_week,
        latest_data_update_time_week_day=latest_data_update_time_week_day,
        latest_data_update_time_year=latest_data_update_time_year,
        limit=limit,
        non_geographic_flag=non_geographic_flag,
        non_geographic_flag_contains=non_geographic_flag_contains,
        non_geographic_flag_endswith=non_geographic_flag_endswith,
        non_geographic_flag_gt=non_geographic_flag_gt,
        non_geographic_flag_gte=non_geographic_flag_gte,
        non_geographic_flag_icontains=non_geographic_flag_icontains,
        non_geographic_flag_iendswith=non_geographic_flag_iendswith,
        non_geographic_flag_iexact=non_geographic_flag_iexact,
        non_geographic_flag_in=non_geographic_flag_in,
        non_geographic_flag_iregex=non_geographic_flag_iregex,
        non_geographic_flag_isnull=non_geographic_flag_isnull,
        non_geographic_flag_istartswith=non_geographic_flag_istartswith,
        non_geographic_flag_lt=non_geographic_flag_lt,
        non_geographic_flag_lte=non_geographic_flag_lte,
        non_geographic_flag_range=non_geographic_flag_range,
        non_geographic_flag_regex=non_geographic_flag_regex,
        non_geographic_flag_startswith=non_geographic_flag_startswith,
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
        permissions_access_category=permissions_access_category,
        permissions_access_category_in=permissions_access_category_in,
        permissions_access_roles=permissions_access_roles,
        permissions_access_roles_in=permissions_access_roles_in,
        procedure_acquisition=procedure_acquisition,
        procedure_acquisition_gt=procedure_acquisition_gt,
        procedure_acquisition_gte=procedure_acquisition_gte,
        procedure_acquisition_in=procedure_acquisition_in,
        procedure_acquisition_isnull=procedure_acquisition_isnull,
        procedure_acquisition_lt=procedure_acquisition_lt,
        procedure_acquisition_lte=procedure_acquisition_lte,
        procedure_acquisition_ob_id=procedure_acquisition_ob_id,
        procedure_acquisition_ob_id_in=procedure_acquisition_ob_id_in,
        procedure_acquisition_uuid=procedure_acquisition_uuid,
        procedure_acquisition_uuid_in=procedure_acquisition_uuid_in,
        procedure_composite_process=procedure_composite_process,
        procedure_composite_process_gt=procedure_composite_process_gt,
        procedure_composite_process_gte=procedure_composite_process_gte,
        procedure_composite_process_in=procedure_composite_process_in,
        procedure_composite_process_isnull=procedure_composite_process_isnull,
        procedure_composite_process_lt=procedure_composite_process_lt,
        procedure_composite_process_lte=procedure_composite_process_lte,
        procedure_computation=procedure_computation,
        procedure_computation_gt=procedure_computation_gt,
        procedure_computation_gte=procedure_computation_gte,
        procedure_computation_in=procedure_computation_in,
        procedure_computation_isnull=procedure_computation_isnull,
        procedure_computation_lt=procedure_computation_lt,
        procedure_computation_lte=procedure_computation_lte,
        procedure_description=procedure_description,
        procedure_description_contains=procedure_description_contains,
        procedure_description_endswith=procedure_description_endswith,
        procedure_description_gt=procedure_description_gt,
        procedure_description_gte=procedure_description_gte,
        procedure_description_icontains=procedure_description_icontains,
        procedure_description_iendswith=procedure_description_iendswith,
        procedure_description_iexact=procedure_description_iexact,
        procedure_description_in=procedure_description_in,
        procedure_description_iregex=procedure_description_iregex,
        procedure_description_isnull=procedure_description_isnull,
        procedure_description_istartswith=procedure_description_istartswith,
        procedure_description_lt=procedure_description_lt,
        procedure_description_lte=procedure_description_lte,
        procedure_description_range=procedure_description_range,
        procedure_description_regex=procedure_description_regex,
        procedure_description_startswith=procedure_description_startswith,
        projects_ob_id=projects_ob_id,
        projects_ob_id_in=projects_ob_id_in,
        projects_uuid=projects_uuid,
        projects_uuid_in=projects_uuid_in,
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
        removed_data_reason=removed_data_reason,
        removed_data_reason_contains=removed_data_reason_contains,
        removed_data_reason_endswith=removed_data_reason_endswith,
        removed_data_reason_gt=removed_data_reason_gt,
        removed_data_reason_gte=removed_data_reason_gte,
        removed_data_reason_icontains=removed_data_reason_icontains,
        removed_data_reason_iendswith=removed_data_reason_iendswith,
        removed_data_reason_iexact=removed_data_reason_iexact,
        removed_data_reason_in=removed_data_reason_in,
        removed_data_reason_iregex=removed_data_reason_iregex,
        removed_data_reason_isnull=removed_data_reason_isnull,
        removed_data_reason_istartswith=removed_data_reason_istartswith,
        removed_data_reason_lt=removed_data_reason_lt,
        removed_data_reason_lte=removed_data_reason_lte,
        removed_data_reason_range=removed_data_reason_range,
        removed_data_reason_regex=removed_data_reason_regex,
        removed_data_reason_startswith=removed_data_reason_startswith,
        removed_data_time=removed_data_time,
        removed_data_time_contained_by=removed_data_time_contained_by,
        removed_data_time_contains=removed_data_time_contains,
        removed_data_time_date=removed_data_time_date,
        removed_data_time_day=removed_data_time_day,
        removed_data_time_endswith=removed_data_time_endswith,
        removed_data_time_gt=removed_data_time_gt,
        removed_data_time_gte=removed_data_time_gte,
        removed_data_time_hour=removed_data_time_hour,
        removed_data_time_icontains=removed_data_time_icontains,
        removed_data_time_iendswith=removed_data_time_iendswith,
        removed_data_time_iexact=removed_data_time_iexact,
        removed_data_time_in=removed_data_time_in,
        removed_data_time_iregex=removed_data_time_iregex,
        removed_data_time_isnull=removed_data_time_isnull,
        removed_data_time_iso_week_day=removed_data_time_iso_week_day,
        removed_data_time_iso_year=removed_data_time_iso_year,
        removed_data_time_istartswith=removed_data_time_istartswith,
        removed_data_time_lt=removed_data_time_lt,
        removed_data_time_lte=removed_data_time_lte,
        removed_data_time_minute=removed_data_time_minute,
        removed_data_time_month=removed_data_time_month,
        removed_data_time_quarter=removed_data_time_quarter,
        removed_data_time_range=removed_data_time_range,
        removed_data_time_regex=removed_data_time_regex,
        removed_data_time_second=removed_data_time_second,
        removed_data_time_startswith=removed_data_time_startswith,
        removed_data_time_time=removed_data_time_time,
        removed_data_time_week=removed_data_time_week,
        removed_data_time_week_day=removed_data_time_week_day,
        removed_data_time_year=removed_data_time_year,
        resolution=resolution,
        resolution_contains=resolution_contains,
        resolution_endswith=resolution_endswith,
        resolution_gt=resolution_gt,
        resolution_gte=resolution_gte,
        resolution_icontains=resolution_icontains,
        resolution_iendswith=resolution_iendswith,
        resolution_iexact=resolution_iexact,
        resolution_in=resolution_in,
        resolution_iregex=resolution_iregex,
        resolution_isnull=resolution_isnull,
        resolution_istartswith=resolution_istartswith,
        resolution_lt=resolution_lt,
        resolution_lte=resolution_lte,
        resolution_range=resolution_range,
        resolution_regex=resolution_regex,
        resolution_startswith=resolution_startswith,
        result_quality=result_quality,
        result_quality_date=result_quality_date,
        result_quality_date_gt=result_quality_date_gt,
        result_quality_date_gte=result_quality_date_gte,
        result_quality_date_lt=result_quality_date_lt,
        result_quality_date_lte=result_quality_date_lte,
        result_quality_date_range=result_quality_date_range,
        result_quality_explanation=result_quality_explanation,
        result_quality_explanation_contains=result_quality_explanation_contains,
        result_quality_gt=result_quality_gt,
        result_quality_gte=result_quality_gte,
        result_quality_in=result_quality_in,
        result_quality_isnull=result_quality_isnull,
        result_quality_lt=result_quality_lt,
        result_quality_lte=result_quality_lte,
        result_quality_ob_id=result_quality_ob_id,
        result_quality_ob_id_in=result_quality_ob_id_in,
        result_quality_passes_test=result_quality_passes_test,
        result_quality_result_title=result_quality_result_title,
        result_quality_result_title_contains=result_quality_result_title_contains,
        result_field=result_field,
        result_field_data_path=result_field_data_path,
        result_field_data_path_contains=result_field_data_path_contains,
        result_field_data_path_startswith=result_field_data_path_startswith,
        result_field_file_format=result_field_file_format,
        result_field_file_format_contains=result_field_file_format_contains,
        result_field_gt=result_field_gt,
        result_field_gte=result_field_gte,
        result_field_in=result_field_in,
        result_field_isnull=result_field_isnull,
        result_field_lt=result_field_lt,
        result_field_lte=result_field_lte,
        result_field_storage_location=result_field_storage_location,
        result_field_storage_status=result_field_storage_status,
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
        submission_user_id=submission_user_id,
        submission_user_id_contains=submission_user_id_contains,
        submission_user_id_endswith=submission_user_id_endswith,
        submission_user_id_gt=submission_user_id_gt,
        submission_user_id_gte=submission_user_id_gte,
        submission_user_id_icontains=submission_user_id_icontains,
        submission_user_id_iendswith=submission_user_id_iendswith,
        submission_user_id_iexact=submission_user_id_iexact,
        submission_user_id_in=submission_user_id_in,
        submission_user_id_iregex=submission_user_id_iregex,
        submission_user_id_isnull=submission_user_id_isnull,
        submission_user_id_istartswith=submission_user_id_istartswith,
        submission_user_id_lt=submission_user_id_lt,
        submission_user_id_lte=submission_user_id_lte,
        submission_user_id_range=submission_user_id_range,
        submission_user_id_regex=submission_user_id_regex,
        submission_user_id_startswith=submission_user_id_startswith,
        time_period=time_period,
        time_period_end_time=time_period_end_time,
        time_period_end_time_gt=time_period_end_time_gt,
        time_period_end_time_gte=time_period_end_time_gte,
        time_period_end_time_lt=time_period_end_time_lt,
        time_period_end_time_lte=time_period_end_time_lte,
        time_period_end_time_range=time_period_end_time_range,
        time_period_gt=time_period_gt,
        time_period_gte=time_period_gte,
        time_period_in=time_period_in,
        time_period_isnull=time_period_isnull,
        time_period_lt=time_period_lt,
        time_period_lte=time_period_lte,
        time_period_ob_id=time_period_ob_id,
        time_period_ob_id_in=time_period_ob_id_in,
        time_period_start_time=time_period_start_time,
        time_period_start_time_gt=time_period_start_time_gt,
        time_period_start_time_gte=time_period_start_time_gte,
        time_period_start_time_lt=time_period_start_time_lt,
        time_period_start_time_lte=time_period_start_time_lte,
        time_period_start_time_range=time_period_start_time_range,
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
        update_frequency=update_frequency,
        update_frequency_contains=update_frequency_contains,
        update_frequency_endswith=update_frequency_endswith,
        update_frequency_gt=update_frequency_gt,
        update_frequency_gte=update_frequency_gte,
        update_frequency_icontains=update_frequency_icontains,
        update_frequency_iendswith=update_frequency_iendswith,
        update_frequency_iexact=update_frequency_iexact,
        update_frequency_in=update_frequency_in,
        update_frequency_iregex=update_frequency_iregex,
        update_frequency_isnull=update_frequency_isnull,
        update_frequency_istartswith=update_frequency_istartswith,
        update_frequency_lt=update_frequency_lt,
        update_frequency_lte=update_frequency_lte,
        update_frequency_range=update_frequency_range,
        update_frequency_regex=update_frequency_regex,
        update_frequency_startswith=update_frequency_startswith,
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
        valid_time_period=valid_time_period,
        valid_time_period_gt=valid_time_period_gt,
        valid_time_period_gte=valid_time_period_gte,
        valid_time_period_in=valid_time_period_in,
        valid_time_period_isnull=valid_time_period_isnull,
        valid_time_period_lt=valid_time_period_lt,
        valid_time_period_lte=valid_time_period_lte,
        vertical_extent=vertical_extent,
        vertical_extent_gt=vertical_extent_gt,
        vertical_extent_gte=vertical_extent_gte,
        vertical_extent_in=vertical_extent_in,
        vertical_extent_isnull=vertical_extent_isnull,
        vertical_extent_lt=vertical_extent_lt,
        vertical_extent_lte=vertical_extent_lte,
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
    creation_date: datetime.datetime | Unset = UNSET,
    creation_date_contained_by: datetime.datetime | Unset = UNSET,
    creation_date_contains: datetime.datetime | Unset = UNSET,
    creation_date_date: datetime.date | Unset = UNSET,
    creation_date_day: float | Unset = UNSET,
    creation_date_endswith: datetime.datetime | Unset = UNSET,
    creation_date_gt: datetime.datetime | Unset = UNSET,
    creation_date_gte: datetime.datetime | Unset = UNSET,
    creation_date_hour: float | Unset = UNSET,
    creation_date_icontains: datetime.datetime | Unset = UNSET,
    creation_date_iendswith: datetime.datetime | Unset = UNSET,
    creation_date_iexact: datetime.datetime | Unset = UNSET,
    creation_date_in: list[datetime.datetime] | Unset = UNSET,
    creation_date_iregex: datetime.datetime | Unset = UNSET,
    creation_date_isnull: bool | Unset = UNSET,
    creation_date_iso_week_day: float | Unset = UNSET,
    creation_date_iso_year: float | Unset = UNSET,
    creation_date_istartswith: datetime.datetime | Unset = UNSET,
    creation_date_lt: datetime.datetime | Unset = UNSET,
    creation_date_lte: datetime.datetime | Unset = UNSET,
    creation_date_minute: float | Unset = UNSET,
    creation_date_month: float | Unset = UNSET,
    creation_date_quarter: float | Unset = UNSET,
    creation_date_range: list[datetime.datetime] | Unset = UNSET,
    creation_date_regex: datetime.datetime | Unset = UNSET,
    creation_date_second: float | Unset = UNSET,
    creation_date_startswith: datetime.datetime | Unset = UNSET,
    creation_date_time: str | Unset = UNSET,
    creation_date_week: float | Unset = UNSET,
    creation_date_week_day: float | Unset = UNSET,
    creation_date_year: float | Unset = UNSET,
    data_lineage: str | Unset = UNSET,
    data_lineage_contains: str | Unset = UNSET,
    data_lineage_endswith: str | Unset = UNSET,
    data_lineage_gt: str | Unset = UNSET,
    data_lineage_gte: str | Unset = UNSET,
    data_lineage_icontains: str | Unset = UNSET,
    data_lineage_iendswith: str | Unset = UNSET,
    data_lineage_iexact: str | Unset = UNSET,
    data_lineage_in: list[str] | Unset = UNSET,
    data_lineage_iregex: str | Unset = UNSET,
    data_lineage_isnull: bool | Unset = UNSET,
    data_lineage_istartswith: str | Unset = UNSET,
    data_lineage_lt: str | Unset = UNSET,
    data_lineage_lte: str | Unset = UNSET,
    data_lineage_range: list[str] | Unset = UNSET,
    data_lineage_regex: str | Unset = UNSET,
    data_lineage_startswith: str | Unset = UNSET,
    data_published_time: datetime.datetime | Unset = UNSET,
    data_published_time_contained_by: datetime.datetime | Unset = UNSET,
    data_published_time_contains: datetime.datetime | Unset = UNSET,
    data_published_time_date: datetime.date | Unset = UNSET,
    data_published_time_day: float | Unset = UNSET,
    data_published_time_endswith: datetime.datetime | Unset = UNSET,
    data_published_time_gt: datetime.datetime | Unset = UNSET,
    data_published_time_gte: datetime.datetime | Unset = UNSET,
    data_published_time_hour: float | Unset = UNSET,
    data_published_time_icontains: datetime.datetime | Unset = UNSET,
    data_published_time_iendswith: datetime.datetime | Unset = UNSET,
    data_published_time_iexact: datetime.datetime | Unset = UNSET,
    data_published_time_in: list[datetime.datetime] | Unset = UNSET,
    data_published_time_iregex: datetime.datetime | Unset = UNSET,
    data_published_time_isnull: bool | Unset = UNSET,
    data_published_time_iso_week_day: float | Unset = UNSET,
    data_published_time_iso_year: float | Unset = UNSET,
    data_published_time_istartswith: datetime.datetime | Unset = UNSET,
    data_published_time_lt: datetime.datetime | Unset = UNSET,
    data_published_time_lte: datetime.datetime | Unset = UNSET,
    data_published_time_minute: float | Unset = UNSET,
    data_published_time_month: float | Unset = UNSET,
    data_published_time_quarter: float | Unset = UNSET,
    data_published_time_range: list[datetime.datetime] | Unset = UNSET,
    data_published_time_regex: datetime.datetime | Unset = UNSET,
    data_published_time_second: float | Unset = UNSET,
    data_published_time_startswith: datetime.datetime | Unset = UNSET,
    data_published_time_time: str | Unset = UNSET,
    data_published_time_week: float | Unset = UNSET,
    data_published_time_week_day: float | Unset = UNSET,
    data_published_time_year: float | Unset = UNSET,
    discovery_keywords_name: str | Unset = UNSET,
    discovery_keywords_name_contains: str | Unset = UNSET,
    doi_published_time: datetime.datetime | Unset = UNSET,
    doi_published_time_contained_by: datetime.datetime | Unset = UNSET,
    doi_published_time_contains: datetime.datetime | Unset = UNSET,
    doi_published_time_date: datetime.date | Unset = UNSET,
    doi_published_time_day: float | Unset = UNSET,
    doi_published_time_endswith: datetime.datetime | Unset = UNSET,
    doi_published_time_gt: datetime.datetime | Unset = UNSET,
    doi_published_time_gte: datetime.datetime | Unset = UNSET,
    doi_published_time_hour: float | Unset = UNSET,
    doi_published_time_icontains: datetime.datetime | Unset = UNSET,
    doi_published_time_iendswith: datetime.datetime | Unset = UNSET,
    doi_published_time_iexact: datetime.datetime | Unset = UNSET,
    doi_published_time_in: list[datetime.datetime] | Unset = UNSET,
    doi_published_time_iregex: datetime.datetime | Unset = UNSET,
    doi_published_time_isnull: bool | Unset = UNSET,
    doi_published_time_iso_week_day: float | Unset = UNSET,
    doi_published_time_iso_year: float | Unset = UNSET,
    doi_published_time_istartswith: datetime.datetime | Unset = UNSET,
    doi_published_time_lt: datetime.datetime | Unset = UNSET,
    doi_published_time_lte: datetime.datetime | Unset = UNSET,
    doi_published_time_minute: float | Unset = UNSET,
    doi_published_time_month: float | Unset = UNSET,
    doi_published_time_quarter: float | Unset = UNSET,
    doi_published_time_range: list[datetime.datetime] | Unset = UNSET,
    doi_published_time_regex: datetime.datetime | Unset = UNSET,
    doi_published_time_second: float | Unset = UNSET,
    doi_published_time_startswith: datetime.datetime | Unset = UNSET,
    doi_published_time_time: str | Unset = UNSET,
    doi_published_time_week: float | Unset = UNSET,
    doi_published_time_week_day: float | Unset = UNSET,
    doi_published_time_year: float | Unset = UNSET,
    dont_harvest_from_projects: bool | Unset = UNSET,
    dont_harvest_from_projects_contains: bool | Unset = UNSET,
    dont_harvest_from_projects_endswith: bool | Unset = UNSET,
    dont_harvest_from_projects_gt: bool | Unset = UNSET,
    dont_harvest_from_projects_gte: bool | Unset = UNSET,
    dont_harvest_from_projects_icontains: bool | Unset = UNSET,
    dont_harvest_from_projects_iendswith: bool | Unset = UNSET,
    dont_harvest_from_projects_iexact: bool | Unset = UNSET,
    dont_harvest_from_projects_in: list[bool] | Unset = UNSET,
    dont_harvest_from_projects_iregex: bool | Unset = UNSET,
    dont_harvest_from_projects_isnull: bool | Unset = UNSET,
    dont_harvest_from_projects_istartswith: bool | Unset = UNSET,
    dont_harvest_from_projects_lt: bool | Unset = UNSET,
    dont_harvest_from_projects_lte: bool | Unset = UNSET,
    dont_harvest_from_projects_range: list[bool] | Unset = UNSET,
    dont_harvest_from_projects_regex: bool | Unset = UNSET,
    dont_harvest_from_projects_startswith: bool | Unset = UNSET,
    feature_of_interest: str | Unset = UNSET,
    feature_of_interest_contains: str | Unset = UNSET,
    feature_of_interest_endswith: str | Unset = UNSET,
    feature_of_interest_gt: str | Unset = UNSET,
    feature_of_interest_gte: str | Unset = UNSET,
    feature_of_interest_icontains: str | Unset = UNSET,
    feature_of_interest_iendswith: str | Unset = UNSET,
    feature_of_interest_iexact: str | Unset = UNSET,
    feature_of_interest_in: list[str] | Unset = UNSET,
    feature_of_interest_iregex: str | Unset = UNSET,
    feature_of_interest_isnull: bool | Unset = UNSET,
    feature_of_interest_istartswith: str | Unset = UNSET,
    feature_of_interest_lt: str | Unset = UNSET,
    feature_of_interest_lte: str | Unset = UNSET,
    feature_of_interest_range: list[str] | Unset = UNSET,
    feature_of_interest_regex: str | Unset = UNSET,
    feature_of_interest_startswith: str | Unset = UNSET,
    geographic_extent: int | Unset = UNSET,
    geographic_extent_east_bound_longitude: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_gt: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_gte: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_lt: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_lte: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_range: list[float] | Unset = UNSET,
    geographic_extent_gt: int | Unset = UNSET,
    geographic_extent_gte: int | Unset = UNSET,
    geographic_extent_in: list[int] | Unset = UNSET,
    geographic_extent_isnull: bool | Unset = UNSET,
    geographic_extent_lt: int | Unset = UNSET,
    geographic_extent_lte: int | Unset = UNSET,
    geographic_extent_north_bound_latitude: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_gt: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_gte: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_lt: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_lte: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_range: list[float] | Unset = UNSET,
    geographic_extent_ob_id: int | Unset = UNSET,
    geographic_extent_ob_id_in: list[int] | Unset = UNSET,
    geographic_extent_south_bound_latitude: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_gt: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_gte: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_lt: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_lte: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_range: list[float] | Unset = UNSET,
    geographic_extent_west_bound_longitude: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_gt: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_gte: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_lt: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_lte: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_range: list[float] | Unset = UNSET,
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
    language: ObservationsListLanguage | Unset = UNSET,
    language_contains: str | Unset = UNSET,
    language_endswith: str | Unset = UNSET,
    language_gt: str | Unset = UNSET,
    language_gte: str | Unset = UNSET,
    language_icontains: str | Unset = UNSET,
    language_iendswith: str | Unset = UNSET,
    language_iexact: str | Unset = UNSET,
    language_in: list[str] | Unset = UNSET,
    language_iregex: str | Unset = UNSET,
    language_isnull: bool | Unset = UNSET,
    language_istartswith: str | Unset = UNSET,
    language_lt: str | Unset = UNSET,
    language_lte: str | Unset = UNSET,
    language_range: list[str] | Unset = UNSET,
    language_regex: str | Unset = UNSET,
    language_startswith: str | Unset = UNSET,
    last_updated_date: datetime.datetime | Unset = UNSET,
    last_updated_date_contained_by: datetime.datetime | Unset = UNSET,
    last_updated_date_contains: datetime.datetime | Unset = UNSET,
    last_updated_date_date: datetime.date | Unset = UNSET,
    last_updated_date_day: float | Unset = UNSET,
    last_updated_date_endswith: datetime.datetime | Unset = UNSET,
    last_updated_date_gt: datetime.datetime | Unset = UNSET,
    last_updated_date_gte: datetime.datetime | Unset = UNSET,
    last_updated_date_hour: float | Unset = UNSET,
    last_updated_date_icontains: datetime.datetime | Unset = UNSET,
    last_updated_date_iendswith: datetime.datetime | Unset = UNSET,
    last_updated_date_iexact: datetime.datetime | Unset = UNSET,
    last_updated_date_in: list[datetime.datetime] | Unset = UNSET,
    last_updated_date_iregex: datetime.datetime | Unset = UNSET,
    last_updated_date_isnull: bool | Unset = UNSET,
    last_updated_date_iso_week_day: float | Unset = UNSET,
    last_updated_date_iso_year: float | Unset = UNSET,
    last_updated_date_istartswith: datetime.datetime | Unset = UNSET,
    last_updated_date_lt: datetime.datetime | Unset = UNSET,
    last_updated_date_lte: datetime.datetime | Unset = UNSET,
    last_updated_date_minute: float | Unset = UNSET,
    last_updated_date_month: float | Unset = UNSET,
    last_updated_date_quarter: float | Unset = UNSET,
    last_updated_date_range: list[datetime.datetime] | Unset = UNSET,
    last_updated_date_regex: datetime.datetime | Unset = UNSET,
    last_updated_date_second: float | Unset = UNSET,
    last_updated_date_startswith: datetime.datetime | Unset = UNSET,
    last_updated_date_time: str | Unset = UNSET,
    last_updated_date_week: float | Unset = UNSET,
    last_updated_date_week_day: float | Unset = UNSET,
    last_updated_date_year: float | Unset = UNSET,
    latest_data_update_time: datetime.datetime | Unset = UNSET,
    latest_data_update_time_contained_by: datetime.datetime | Unset = UNSET,
    latest_data_update_time_contains: datetime.datetime | Unset = UNSET,
    latest_data_update_time_date: datetime.date | Unset = UNSET,
    latest_data_update_time_day: float | Unset = UNSET,
    latest_data_update_time_endswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_gt: datetime.datetime | Unset = UNSET,
    latest_data_update_time_gte: datetime.datetime | Unset = UNSET,
    latest_data_update_time_hour: float | Unset = UNSET,
    latest_data_update_time_icontains: datetime.datetime | Unset = UNSET,
    latest_data_update_time_iendswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_iexact: datetime.datetime | Unset = UNSET,
    latest_data_update_time_in: list[datetime.datetime] | Unset = UNSET,
    latest_data_update_time_iregex: datetime.datetime | Unset = UNSET,
    latest_data_update_time_isnull: bool | Unset = UNSET,
    latest_data_update_time_iso_week_day: float | Unset = UNSET,
    latest_data_update_time_iso_year: float | Unset = UNSET,
    latest_data_update_time_istartswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_lt: datetime.datetime | Unset = UNSET,
    latest_data_update_time_lte: datetime.datetime | Unset = UNSET,
    latest_data_update_time_minute: float | Unset = UNSET,
    latest_data_update_time_month: float | Unset = UNSET,
    latest_data_update_time_quarter: float | Unset = UNSET,
    latest_data_update_time_range: list[datetime.datetime] | Unset = UNSET,
    latest_data_update_time_regex: datetime.datetime | Unset = UNSET,
    latest_data_update_time_second: float | Unset = UNSET,
    latest_data_update_time_startswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_time: str | Unset = UNSET,
    latest_data_update_time_week: float | Unset = UNSET,
    latest_data_update_time_week_day: float | Unset = UNSET,
    latest_data_update_time_year: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    non_geographic_flag: bool | Unset = UNSET,
    non_geographic_flag_contains: bool | Unset = UNSET,
    non_geographic_flag_endswith: bool | Unset = UNSET,
    non_geographic_flag_gt: bool | Unset = UNSET,
    non_geographic_flag_gte: bool | Unset = UNSET,
    non_geographic_flag_icontains: bool | Unset = UNSET,
    non_geographic_flag_iendswith: bool | Unset = UNSET,
    non_geographic_flag_iexact: bool | Unset = UNSET,
    non_geographic_flag_in: list[bool] | Unset = UNSET,
    non_geographic_flag_iregex: bool | Unset = UNSET,
    non_geographic_flag_isnull: bool | Unset = UNSET,
    non_geographic_flag_istartswith: bool | Unset = UNSET,
    non_geographic_flag_lt: bool | Unset = UNSET,
    non_geographic_flag_lte: bool | Unset = UNSET,
    non_geographic_flag_range: list[bool] | Unset = UNSET,
    non_geographic_flag_regex: bool | Unset = UNSET,
    non_geographic_flag_startswith: bool | Unset = UNSET,
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
    permissions_access_category: ObservationsListAccessCategory | Unset = UNSET,
    permissions_access_category_in: list[str] | Unset = UNSET,
    permissions_access_roles: str | Unset = UNSET,
    permissions_access_roles_in: list[str] | Unset = UNSET,
    procedure_acquisition: int | Unset = UNSET,
    procedure_acquisition_gt: int | Unset = UNSET,
    procedure_acquisition_gte: int | Unset = UNSET,
    procedure_acquisition_in: list[int] | Unset = UNSET,
    procedure_acquisition_isnull: bool | Unset = UNSET,
    procedure_acquisition_lt: int | Unset = UNSET,
    procedure_acquisition_lte: int | Unset = UNSET,
    procedure_acquisition_ob_id: int | Unset = UNSET,
    procedure_acquisition_ob_id_in: list[int] | Unset = UNSET,
    procedure_acquisition_uuid: str | Unset = UNSET,
    procedure_acquisition_uuid_in: list[str] | Unset = UNSET,
    procedure_composite_process: int | Unset = UNSET,
    procedure_composite_process_gt: int | Unset = UNSET,
    procedure_composite_process_gte: int | Unset = UNSET,
    procedure_composite_process_in: list[int] | Unset = UNSET,
    procedure_composite_process_isnull: bool | Unset = UNSET,
    procedure_composite_process_lt: int | Unset = UNSET,
    procedure_composite_process_lte: int | Unset = UNSET,
    procedure_computation: int | Unset = UNSET,
    procedure_computation_gt: int | Unset = UNSET,
    procedure_computation_gte: int | Unset = UNSET,
    procedure_computation_in: list[int] | Unset = UNSET,
    procedure_computation_isnull: bool | Unset = UNSET,
    procedure_computation_lt: int | Unset = UNSET,
    procedure_computation_lte: int | Unset = UNSET,
    procedure_description: str | Unset = UNSET,
    procedure_description_contains: str | Unset = UNSET,
    procedure_description_endswith: str | Unset = UNSET,
    procedure_description_gt: str | Unset = UNSET,
    procedure_description_gte: str | Unset = UNSET,
    procedure_description_icontains: str | Unset = UNSET,
    procedure_description_iendswith: str | Unset = UNSET,
    procedure_description_iexact: str | Unset = UNSET,
    procedure_description_in: list[str] | Unset = UNSET,
    procedure_description_iregex: str | Unset = UNSET,
    procedure_description_isnull: bool | Unset = UNSET,
    procedure_description_istartswith: str | Unset = UNSET,
    procedure_description_lt: str | Unset = UNSET,
    procedure_description_lte: str | Unset = UNSET,
    procedure_description_range: list[str] | Unset = UNSET,
    procedure_description_regex: str | Unset = UNSET,
    procedure_description_startswith: str | Unset = UNSET,
    projects_ob_id: int | Unset = UNSET,
    projects_ob_id_in: list[int] | Unset = UNSET,
    projects_uuid: str | Unset = UNSET,
    projects_uuid_in: list[str] | Unset = UNSET,
    publication_state: ObservationsListPublicationState | Unset = UNSET,
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
    removed_data_reason: str | Unset = UNSET,
    removed_data_reason_contains: str | Unset = UNSET,
    removed_data_reason_endswith: str | Unset = UNSET,
    removed_data_reason_gt: str | Unset = UNSET,
    removed_data_reason_gte: str | Unset = UNSET,
    removed_data_reason_icontains: str | Unset = UNSET,
    removed_data_reason_iendswith: str | Unset = UNSET,
    removed_data_reason_iexact: str | Unset = UNSET,
    removed_data_reason_in: list[str] | Unset = UNSET,
    removed_data_reason_iregex: str | Unset = UNSET,
    removed_data_reason_isnull: bool | Unset = UNSET,
    removed_data_reason_istartswith: str | Unset = UNSET,
    removed_data_reason_lt: str | Unset = UNSET,
    removed_data_reason_lte: str | Unset = UNSET,
    removed_data_reason_range: list[str] | Unset = UNSET,
    removed_data_reason_regex: str | Unset = UNSET,
    removed_data_reason_startswith: str | Unset = UNSET,
    removed_data_time: datetime.datetime | Unset = UNSET,
    removed_data_time_contained_by: datetime.datetime | Unset = UNSET,
    removed_data_time_contains: datetime.datetime | Unset = UNSET,
    removed_data_time_date: datetime.date | Unset = UNSET,
    removed_data_time_day: float | Unset = UNSET,
    removed_data_time_endswith: datetime.datetime | Unset = UNSET,
    removed_data_time_gt: datetime.datetime | Unset = UNSET,
    removed_data_time_gte: datetime.datetime | Unset = UNSET,
    removed_data_time_hour: float | Unset = UNSET,
    removed_data_time_icontains: datetime.datetime | Unset = UNSET,
    removed_data_time_iendswith: datetime.datetime | Unset = UNSET,
    removed_data_time_iexact: datetime.datetime | Unset = UNSET,
    removed_data_time_in: list[datetime.datetime] | Unset = UNSET,
    removed_data_time_iregex: datetime.datetime | Unset = UNSET,
    removed_data_time_isnull: bool | Unset = UNSET,
    removed_data_time_iso_week_day: float | Unset = UNSET,
    removed_data_time_iso_year: float | Unset = UNSET,
    removed_data_time_istartswith: datetime.datetime | Unset = UNSET,
    removed_data_time_lt: datetime.datetime | Unset = UNSET,
    removed_data_time_lte: datetime.datetime | Unset = UNSET,
    removed_data_time_minute: float | Unset = UNSET,
    removed_data_time_month: float | Unset = UNSET,
    removed_data_time_quarter: float | Unset = UNSET,
    removed_data_time_range: list[datetime.datetime] | Unset = UNSET,
    removed_data_time_regex: datetime.datetime | Unset = UNSET,
    removed_data_time_second: float | Unset = UNSET,
    removed_data_time_startswith: datetime.datetime | Unset = UNSET,
    removed_data_time_time: str | Unset = UNSET,
    removed_data_time_week: float | Unset = UNSET,
    removed_data_time_week_day: float | Unset = UNSET,
    removed_data_time_year: float | Unset = UNSET,
    resolution: str | Unset = UNSET,
    resolution_contains: str | Unset = UNSET,
    resolution_endswith: str | Unset = UNSET,
    resolution_gt: str | Unset = UNSET,
    resolution_gte: str | Unset = UNSET,
    resolution_icontains: str | Unset = UNSET,
    resolution_iendswith: str | Unset = UNSET,
    resolution_iexact: str | Unset = UNSET,
    resolution_in: list[str] | Unset = UNSET,
    resolution_iregex: str | Unset = UNSET,
    resolution_isnull: bool | Unset = UNSET,
    resolution_istartswith: str | Unset = UNSET,
    resolution_lt: str | Unset = UNSET,
    resolution_lte: str | Unset = UNSET,
    resolution_range: list[str] | Unset = UNSET,
    resolution_regex: str | Unset = UNSET,
    resolution_startswith: str | Unset = UNSET,
    result_quality: int | Unset = UNSET,
    result_quality_date: datetime.date | Unset = UNSET,
    result_quality_date_gt: datetime.date | Unset = UNSET,
    result_quality_date_gte: datetime.date | Unset = UNSET,
    result_quality_date_lt: datetime.date | Unset = UNSET,
    result_quality_date_lte: datetime.date | Unset = UNSET,
    result_quality_date_range: list[datetime.date] | Unset = UNSET,
    result_quality_explanation: str | Unset = UNSET,
    result_quality_explanation_contains: str | Unset = UNSET,
    result_quality_gt: int | Unset = UNSET,
    result_quality_gte: int | Unset = UNSET,
    result_quality_in: list[int] | Unset = UNSET,
    result_quality_isnull: bool | Unset = UNSET,
    result_quality_lt: int | Unset = UNSET,
    result_quality_lte: int | Unset = UNSET,
    result_quality_ob_id: int | Unset = UNSET,
    result_quality_ob_id_in: list[int] | Unset = UNSET,
    result_quality_passes_test: bool | Unset = UNSET,
    result_quality_result_title: str | Unset = UNSET,
    result_quality_result_title_contains: str | Unset = UNSET,
    result_field: int | Unset = UNSET,
    result_field_data_path: str | Unset = UNSET,
    result_field_data_path_contains: str | Unset = UNSET,
    result_field_data_path_startswith: str | Unset = UNSET,
    result_field_file_format: str | Unset = UNSET,
    result_field_file_format_contains: str | Unset = UNSET,
    result_field_gt: int | Unset = UNSET,
    result_field_gte: int | Unset = UNSET,
    result_field_in: list[int] | Unset = UNSET,
    result_field_isnull: bool | Unset = UNSET,
    result_field_lt: int | Unset = UNSET,
    result_field_lte: int | Unset = UNSET,
    result_field_storage_location: ObservationsListStorageLocation | Unset = UNSET,
    result_field_storage_status: ObservationsListStorageStatus | Unset = UNSET,
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
    status: ObservationsListDataStatus | Unset = UNSET,
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
    submission_user_id: str | Unset = UNSET,
    submission_user_id_contains: str | Unset = UNSET,
    submission_user_id_endswith: str | Unset = UNSET,
    submission_user_id_gt: str | Unset = UNSET,
    submission_user_id_gte: str | Unset = UNSET,
    submission_user_id_icontains: str | Unset = UNSET,
    submission_user_id_iendswith: str | Unset = UNSET,
    submission_user_id_iexact: str | Unset = UNSET,
    submission_user_id_in: list[str] | Unset = UNSET,
    submission_user_id_iregex: str | Unset = UNSET,
    submission_user_id_isnull: bool | Unset = UNSET,
    submission_user_id_istartswith: str | Unset = UNSET,
    submission_user_id_lt: str | Unset = UNSET,
    submission_user_id_lte: str | Unset = UNSET,
    submission_user_id_range: list[str] | Unset = UNSET,
    submission_user_id_regex: str | Unset = UNSET,
    submission_user_id_startswith: str | Unset = UNSET,
    time_period: int | Unset = UNSET,
    time_period_end_time: datetime.datetime | Unset = UNSET,
    time_period_end_time_gt: datetime.datetime | Unset = UNSET,
    time_period_end_time_gte: datetime.datetime | Unset = UNSET,
    time_period_end_time_lt: datetime.datetime | Unset = UNSET,
    time_period_end_time_lte: datetime.datetime | Unset = UNSET,
    time_period_end_time_range: list[datetime.datetime] | Unset = UNSET,
    time_period_gt: int | Unset = UNSET,
    time_period_gte: int | Unset = UNSET,
    time_period_in: list[int] | Unset = UNSET,
    time_period_isnull: bool | Unset = UNSET,
    time_period_lt: int | Unset = UNSET,
    time_period_lte: int | Unset = UNSET,
    time_period_ob_id: int | Unset = UNSET,
    time_period_ob_id_in: list[int] | Unset = UNSET,
    time_period_start_time: datetime.datetime | Unset = UNSET,
    time_period_start_time_gt: datetime.datetime | Unset = UNSET,
    time_period_start_time_gte: datetime.datetime | Unset = UNSET,
    time_period_start_time_lt: datetime.datetime | Unset = UNSET,
    time_period_start_time_lte: datetime.datetime | Unset = UNSET,
    time_period_start_time_range: list[datetime.datetime] | Unset = UNSET,
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
    update_frequency: ObservationsListDataUpdateFrequency | Unset = UNSET,
    update_frequency_contains: str | Unset = UNSET,
    update_frequency_endswith: str | Unset = UNSET,
    update_frequency_gt: str | Unset = UNSET,
    update_frequency_gte: str | Unset = UNSET,
    update_frequency_icontains: str | Unset = UNSET,
    update_frequency_iendswith: str | Unset = UNSET,
    update_frequency_iexact: str | Unset = UNSET,
    update_frequency_in: list[str] | Unset = UNSET,
    update_frequency_iregex: str | Unset = UNSET,
    update_frequency_isnull: bool | Unset = UNSET,
    update_frequency_istartswith: str | Unset = UNSET,
    update_frequency_lt: str | Unset = UNSET,
    update_frequency_lte: str | Unset = UNSET,
    update_frequency_range: list[str] | Unset = UNSET,
    update_frequency_regex: str | Unset = UNSET,
    update_frequency_startswith: str | Unset = UNSET,
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
    valid_time_period: int | Unset = UNSET,
    valid_time_period_gt: int | Unset = UNSET,
    valid_time_period_gte: int | Unset = UNSET,
    valid_time_period_in: list[int] | Unset = UNSET,
    valid_time_period_isnull: bool | Unset = UNSET,
    valid_time_period_lt: int | Unset = UNSET,
    valid_time_period_lte: int | Unset = UNSET,
    vertical_extent: int | Unset = UNSET,
    vertical_extent_gt: int | Unset = UNSET,
    vertical_extent_gte: int | Unset = UNSET,
    vertical_extent_in: list[int] | Unset = UNSET,
    vertical_extent_isnull: bool | Unset = UNSET,
    vertical_extent_lt: int | Unset = UNSET,
    vertical_extent_lte: int | Unset = UNSET,
) -> PaginatedObservationReadList | None:
    """Get a list of Observation objects.

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
        creation_date (datetime.datetime | Unset):
        creation_date_contained_by (datetime.datetime | Unset):
        creation_date_contains (datetime.datetime | Unset):
        creation_date_date (datetime.date | Unset):
        creation_date_day (float | Unset):
        creation_date_endswith (datetime.datetime | Unset):
        creation_date_gt (datetime.datetime | Unset):
        creation_date_gte (datetime.datetime | Unset):
        creation_date_hour (float | Unset):
        creation_date_icontains (datetime.datetime | Unset):
        creation_date_iendswith (datetime.datetime | Unset):
        creation_date_iexact (datetime.datetime | Unset):
        creation_date_in (list[datetime.datetime] | Unset):
        creation_date_iregex (datetime.datetime | Unset):
        creation_date_isnull (bool | Unset):
        creation_date_iso_week_day (float | Unset):
        creation_date_iso_year (float | Unset):
        creation_date_istartswith (datetime.datetime | Unset):
        creation_date_lt (datetime.datetime | Unset):
        creation_date_lte (datetime.datetime | Unset):
        creation_date_minute (float | Unset):
        creation_date_month (float | Unset):
        creation_date_quarter (float | Unset):
        creation_date_range (list[datetime.datetime] | Unset):
        creation_date_regex (datetime.datetime | Unset):
        creation_date_second (float | Unset):
        creation_date_startswith (datetime.datetime | Unset):
        creation_date_time (str | Unset):
        creation_date_week (float | Unset):
        creation_date_week_day (float | Unset):
        creation_date_year (float | Unset):
        data_lineage (str | Unset):
        data_lineage_contains (str | Unset):
        data_lineage_endswith (str | Unset):
        data_lineage_gt (str | Unset):
        data_lineage_gte (str | Unset):
        data_lineage_icontains (str | Unset):
        data_lineage_iendswith (str | Unset):
        data_lineage_iexact (str | Unset):
        data_lineage_in (list[str] | Unset):
        data_lineage_iregex (str | Unset):
        data_lineage_isnull (bool | Unset):
        data_lineage_istartswith (str | Unset):
        data_lineage_lt (str | Unset):
        data_lineage_lte (str | Unset):
        data_lineage_range (list[str] | Unset):
        data_lineage_regex (str | Unset):
        data_lineage_startswith (str | Unset):
        data_published_time (datetime.datetime | Unset):
        data_published_time_contained_by (datetime.datetime | Unset):
        data_published_time_contains (datetime.datetime | Unset):
        data_published_time_date (datetime.date | Unset):
        data_published_time_day (float | Unset):
        data_published_time_endswith (datetime.datetime | Unset):
        data_published_time_gt (datetime.datetime | Unset):
        data_published_time_gte (datetime.datetime | Unset):
        data_published_time_hour (float | Unset):
        data_published_time_icontains (datetime.datetime | Unset):
        data_published_time_iendswith (datetime.datetime | Unset):
        data_published_time_iexact (datetime.datetime | Unset):
        data_published_time_in (list[datetime.datetime] | Unset):
        data_published_time_iregex (datetime.datetime | Unset):
        data_published_time_isnull (bool | Unset):
        data_published_time_iso_week_day (float | Unset):
        data_published_time_iso_year (float | Unset):
        data_published_time_istartswith (datetime.datetime | Unset):
        data_published_time_lt (datetime.datetime | Unset):
        data_published_time_lte (datetime.datetime | Unset):
        data_published_time_minute (float | Unset):
        data_published_time_month (float | Unset):
        data_published_time_quarter (float | Unset):
        data_published_time_range (list[datetime.datetime] | Unset):
        data_published_time_regex (datetime.datetime | Unset):
        data_published_time_second (float | Unset):
        data_published_time_startswith (datetime.datetime | Unset):
        data_published_time_time (str | Unset):
        data_published_time_week (float | Unset):
        data_published_time_week_day (float | Unset):
        data_published_time_year (float | Unset):
        discovery_keywords_name (str | Unset):
        discovery_keywords_name_contains (str | Unset):
        doi_published_time (datetime.datetime | Unset):
        doi_published_time_contained_by (datetime.datetime | Unset):
        doi_published_time_contains (datetime.datetime | Unset):
        doi_published_time_date (datetime.date | Unset):
        doi_published_time_day (float | Unset):
        doi_published_time_endswith (datetime.datetime | Unset):
        doi_published_time_gt (datetime.datetime | Unset):
        doi_published_time_gte (datetime.datetime | Unset):
        doi_published_time_hour (float | Unset):
        doi_published_time_icontains (datetime.datetime | Unset):
        doi_published_time_iendswith (datetime.datetime | Unset):
        doi_published_time_iexact (datetime.datetime | Unset):
        doi_published_time_in (list[datetime.datetime] | Unset):
        doi_published_time_iregex (datetime.datetime | Unset):
        doi_published_time_isnull (bool | Unset):
        doi_published_time_iso_week_day (float | Unset):
        doi_published_time_iso_year (float | Unset):
        doi_published_time_istartswith (datetime.datetime | Unset):
        doi_published_time_lt (datetime.datetime | Unset):
        doi_published_time_lte (datetime.datetime | Unset):
        doi_published_time_minute (float | Unset):
        doi_published_time_month (float | Unset):
        doi_published_time_quarter (float | Unset):
        doi_published_time_range (list[datetime.datetime] | Unset):
        doi_published_time_regex (datetime.datetime | Unset):
        doi_published_time_second (float | Unset):
        doi_published_time_startswith (datetime.datetime | Unset):
        doi_published_time_time (str | Unset):
        doi_published_time_week (float | Unset):
        doi_published_time_week_day (float | Unset):
        doi_published_time_year (float | Unset):
        dont_harvest_from_projects (bool | Unset):
        dont_harvest_from_projects_contains (bool | Unset):
        dont_harvest_from_projects_endswith (bool | Unset):
        dont_harvest_from_projects_gt (bool | Unset):
        dont_harvest_from_projects_gte (bool | Unset):
        dont_harvest_from_projects_icontains (bool | Unset):
        dont_harvest_from_projects_iendswith (bool | Unset):
        dont_harvest_from_projects_iexact (bool | Unset):
        dont_harvest_from_projects_in (list[bool] | Unset):
        dont_harvest_from_projects_iregex (bool | Unset):
        dont_harvest_from_projects_isnull (bool | Unset):
        dont_harvest_from_projects_istartswith (bool | Unset):
        dont_harvest_from_projects_lt (bool | Unset):
        dont_harvest_from_projects_lte (bool | Unset):
        dont_harvest_from_projects_range (list[bool] | Unset):
        dont_harvest_from_projects_regex (bool | Unset):
        dont_harvest_from_projects_startswith (bool | Unset):
        feature_of_interest (str | Unset):
        feature_of_interest_contains (str | Unset):
        feature_of_interest_endswith (str | Unset):
        feature_of_interest_gt (str | Unset):
        feature_of_interest_gte (str | Unset):
        feature_of_interest_icontains (str | Unset):
        feature_of_interest_iendswith (str | Unset):
        feature_of_interest_iexact (str | Unset):
        feature_of_interest_in (list[str] | Unset):
        feature_of_interest_iregex (str | Unset):
        feature_of_interest_isnull (bool | Unset):
        feature_of_interest_istartswith (str | Unset):
        feature_of_interest_lt (str | Unset):
        feature_of_interest_lte (str | Unset):
        feature_of_interest_range (list[str] | Unset):
        feature_of_interest_regex (str | Unset):
        feature_of_interest_startswith (str | Unset):
        geographic_extent (int | Unset):
        geographic_extent_east_bound_longitude (float | Unset):
        geographic_extent_east_bound_longitude_gt (float | Unset):
        geographic_extent_east_bound_longitude_gte (float | Unset):
        geographic_extent_east_bound_longitude_lt (float | Unset):
        geographic_extent_east_bound_longitude_lte (float | Unset):
        geographic_extent_east_bound_longitude_range (list[float] | Unset):
        geographic_extent_gt (int | Unset):
        geographic_extent_gte (int | Unset):
        geographic_extent_in (list[int] | Unset):
        geographic_extent_isnull (bool | Unset):
        geographic_extent_lt (int | Unset):
        geographic_extent_lte (int | Unset):
        geographic_extent_north_bound_latitude (float | Unset):
        geographic_extent_north_bound_latitude_gt (float | Unset):
        geographic_extent_north_bound_latitude_gte (float | Unset):
        geographic_extent_north_bound_latitude_lt (float | Unset):
        geographic_extent_north_bound_latitude_lte (float | Unset):
        geographic_extent_north_bound_latitude_range (list[float] | Unset):
        geographic_extent_ob_id (int | Unset):
        geographic_extent_ob_id_in (list[int] | Unset):
        geographic_extent_south_bound_latitude (float | Unset):
        geographic_extent_south_bound_latitude_gt (float | Unset):
        geographic_extent_south_bound_latitude_gte (float | Unset):
        geographic_extent_south_bound_latitude_lt (float | Unset):
        geographic_extent_south_bound_latitude_lte (float | Unset):
        geographic_extent_south_bound_latitude_range (list[float] | Unset):
        geographic_extent_west_bound_longitude (float | Unset):
        geographic_extent_west_bound_longitude_gt (float | Unset):
        geographic_extent_west_bound_longitude_gte (float | Unset):
        geographic_extent_west_bound_longitude_lt (float | Unset):
        geographic_extent_west_bound_longitude_lte (float | Unset):
        geographic_extent_west_bound_longitude_range (list[float] | Unset):
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
        language (ObservationsListLanguage | Unset):
        language_contains (str | Unset):
        language_endswith (str | Unset):
        language_gt (str | Unset):
        language_gte (str | Unset):
        language_icontains (str | Unset):
        language_iendswith (str | Unset):
        language_iexact (str | Unset):
        language_in (list[str] | Unset):
        language_iregex (str | Unset):
        language_isnull (bool | Unset):
        language_istartswith (str | Unset):
        language_lt (str | Unset):
        language_lte (str | Unset):
        language_range (list[str] | Unset):
        language_regex (str | Unset):
        language_startswith (str | Unset):
        last_updated_date (datetime.datetime | Unset):
        last_updated_date_contained_by (datetime.datetime | Unset):
        last_updated_date_contains (datetime.datetime | Unset):
        last_updated_date_date (datetime.date | Unset):
        last_updated_date_day (float | Unset):
        last_updated_date_endswith (datetime.datetime | Unset):
        last_updated_date_gt (datetime.datetime | Unset):
        last_updated_date_gte (datetime.datetime | Unset):
        last_updated_date_hour (float | Unset):
        last_updated_date_icontains (datetime.datetime | Unset):
        last_updated_date_iendswith (datetime.datetime | Unset):
        last_updated_date_iexact (datetime.datetime | Unset):
        last_updated_date_in (list[datetime.datetime] | Unset):
        last_updated_date_iregex (datetime.datetime | Unset):
        last_updated_date_isnull (bool | Unset):
        last_updated_date_iso_week_day (float | Unset):
        last_updated_date_iso_year (float | Unset):
        last_updated_date_istartswith (datetime.datetime | Unset):
        last_updated_date_lt (datetime.datetime | Unset):
        last_updated_date_lte (datetime.datetime | Unset):
        last_updated_date_minute (float | Unset):
        last_updated_date_month (float | Unset):
        last_updated_date_quarter (float | Unset):
        last_updated_date_range (list[datetime.datetime] | Unset):
        last_updated_date_regex (datetime.datetime | Unset):
        last_updated_date_second (float | Unset):
        last_updated_date_startswith (datetime.datetime | Unset):
        last_updated_date_time (str | Unset):
        last_updated_date_week (float | Unset):
        last_updated_date_week_day (float | Unset):
        last_updated_date_year (float | Unset):
        latest_data_update_time (datetime.datetime | Unset):
        latest_data_update_time_contained_by (datetime.datetime | Unset):
        latest_data_update_time_contains (datetime.datetime | Unset):
        latest_data_update_time_date (datetime.date | Unset):
        latest_data_update_time_day (float | Unset):
        latest_data_update_time_endswith (datetime.datetime | Unset):
        latest_data_update_time_gt (datetime.datetime | Unset):
        latest_data_update_time_gte (datetime.datetime | Unset):
        latest_data_update_time_hour (float | Unset):
        latest_data_update_time_icontains (datetime.datetime | Unset):
        latest_data_update_time_iendswith (datetime.datetime | Unset):
        latest_data_update_time_iexact (datetime.datetime | Unset):
        latest_data_update_time_in (list[datetime.datetime] | Unset):
        latest_data_update_time_iregex (datetime.datetime | Unset):
        latest_data_update_time_isnull (bool | Unset):
        latest_data_update_time_iso_week_day (float | Unset):
        latest_data_update_time_iso_year (float | Unset):
        latest_data_update_time_istartswith (datetime.datetime | Unset):
        latest_data_update_time_lt (datetime.datetime | Unset):
        latest_data_update_time_lte (datetime.datetime | Unset):
        latest_data_update_time_minute (float | Unset):
        latest_data_update_time_month (float | Unset):
        latest_data_update_time_quarter (float | Unset):
        latest_data_update_time_range (list[datetime.datetime] | Unset):
        latest_data_update_time_regex (datetime.datetime | Unset):
        latest_data_update_time_second (float | Unset):
        latest_data_update_time_startswith (datetime.datetime | Unset):
        latest_data_update_time_time (str | Unset):
        latest_data_update_time_week (float | Unset):
        latest_data_update_time_week_day (float | Unset):
        latest_data_update_time_year (float | Unset):
        limit (int | Unset):
        non_geographic_flag (bool | Unset):
        non_geographic_flag_contains (bool | Unset):
        non_geographic_flag_endswith (bool | Unset):
        non_geographic_flag_gt (bool | Unset):
        non_geographic_flag_gte (bool | Unset):
        non_geographic_flag_icontains (bool | Unset):
        non_geographic_flag_iendswith (bool | Unset):
        non_geographic_flag_iexact (bool | Unset):
        non_geographic_flag_in (list[bool] | Unset):
        non_geographic_flag_iregex (bool | Unset):
        non_geographic_flag_isnull (bool | Unset):
        non_geographic_flag_istartswith (bool | Unset):
        non_geographic_flag_lt (bool | Unset):
        non_geographic_flag_lte (bool | Unset):
        non_geographic_flag_range (list[bool] | Unset):
        non_geographic_flag_regex (bool | Unset):
        non_geographic_flag_startswith (bool | Unset):
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
        permissions_access_category (ObservationsListAccessCategory | Unset):
        permissions_access_category_in (list[str] | Unset):
        permissions_access_roles (str | Unset):
        permissions_access_roles_in (list[str] | Unset):
        procedure_acquisition (int | Unset):
        procedure_acquisition_gt (int | Unset):
        procedure_acquisition_gte (int | Unset):
        procedure_acquisition_in (list[int] | Unset):
        procedure_acquisition_isnull (bool | Unset):
        procedure_acquisition_lt (int | Unset):
        procedure_acquisition_lte (int | Unset):
        procedure_acquisition_ob_id (int | Unset):
        procedure_acquisition_ob_id_in (list[int] | Unset):
        procedure_acquisition_uuid (str | Unset):
        procedure_acquisition_uuid_in (list[str] | Unset):
        procedure_composite_process (int | Unset):
        procedure_composite_process_gt (int | Unset):
        procedure_composite_process_gte (int | Unset):
        procedure_composite_process_in (list[int] | Unset):
        procedure_composite_process_isnull (bool | Unset):
        procedure_composite_process_lt (int | Unset):
        procedure_composite_process_lte (int | Unset):
        procedure_computation (int | Unset):
        procedure_computation_gt (int | Unset):
        procedure_computation_gte (int | Unset):
        procedure_computation_in (list[int] | Unset):
        procedure_computation_isnull (bool | Unset):
        procedure_computation_lt (int | Unset):
        procedure_computation_lte (int | Unset):
        procedure_description (str | Unset):
        procedure_description_contains (str | Unset):
        procedure_description_endswith (str | Unset):
        procedure_description_gt (str | Unset):
        procedure_description_gte (str | Unset):
        procedure_description_icontains (str | Unset):
        procedure_description_iendswith (str | Unset):
        procedure_description_iexact (str | Unset):
        procedure_description_in (list[str] | Unset):
        procedure_description_iregex (str | Unset):
        procedure_description_isnull (bool | Unset):
        procedure_description_istartswith (str | Unset):
        procedure_description_lt (str | Unset):
        procedure_description_lte (str | Unset):
        procedure_description_range (list[str] | Unset):
        procedure_description_regex (str | Unset):
        procedure_description_startswith (str | Unset):
        projects_ob_id (int | Unset):
        projects_ob_id_in (list[int] | Unset):
        projects_uuid (str | Unset):
        projects_uuid_in (list[str] | Unset):
        publication_state (ObservationsListPublicationState | Unset):
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
        removed_data_reason (str | Unset):
        removed_data_reason_contains (str | Unset):
        removed_data_reason_endswith (str | Unset):
        removed_data_reason_gt (str | Unset):
        removed_data_reason_gte (str | Unset):
        removed_data_reason_icontains (str | Unset):
        removed_data_reason_iendswith (str | Unset):
        removed_data_reason_iexact (str | Unset):
        removed_data_reason_in (list[str] | Unset):
        removed_data_reason_iregex (str | Unset):
        removed_data_reason_isnull (bool | Unset):
        removed_data_reason_istartswith (str | Unset):
        removed_data_reason_lt (str | Unset):
        removed_data_reason_lte (str | Unset):
        removed_data_reason_range (list[str] | Unset):
        removed_data_reason_regex (str | Unset):
        removed_data_reason_startswith (str | Unset):
        removed_data_time (datetime.datetime | Unset):
        removed_data_time_contained_by (datetime.datetime | Unset):
        removed_data_time_contains (datetime.datetime | Unset):
        removed_data_time_date (datetime.date | Unset):
        removed_data_time_day (float | Unset):
        removed_data_time_endswith (datetime.datetime | Unset):
        removed_data_time_gt (datetime.datetime | Unset):
        removed_data_time_gte (datetime.datetime | Unset):
        removed_data_time_hour (float | Unset):
        removed_data_time_icontains (datetime.datetime | Unset):
        removed_data_time_iendswith (datetime.datetime | Unset):
        removed_data_time_iexact (datetime.datetime | Unset):
        removed_data_time_in (list[datetime.datetime] | Unset):
        removed_data_time_iregex (datetime.datetime | Unset):
        removed_data_time_isnull (bool | Unset):
        removed_data_time_iso_week_day (float | Unset):
        removed_data_time_iso_year (float | Unset):
        removed_data_time_istartswith (datetime.datetime | Unset):
        removed_data_time_lt (datetime.datetime | Unset):
        removed_data_time_lte (datetime.datetime | Unset):
        removed_data_time_minute (float | Unset):
        removed_data_time_month (float | Unset):
        removed_data_time_quarter (float | Unset):
        removed_data_time_range (list[datetime.datetime] | Unset):
        removed_data_time_regex (datetime.datetime | Unset):
        removed_data_time_second (float | Unset):
        removed_data_time_startswith (datetime.datetime | Unset):
        removed_data_time_time (str | Unset):
        removed_data_time_week (float | Unset):
        removed_data_time_week_day (float | Unset):
        removed_data_time_year (float | Unset):
        resolution (str | Unset):
        resolution_contains (str | Unset):
        resolution_endswith (str | Unset):
        resolution_gt (str | Unset):
        resolution_gte (str | Unset):
        resolution_icontains (str | Unset):
        resolution_iendswith (str | Unset):
        resolution_iexact (str | Unset):
        resolution_in (list[str] | Unset):
        resolution_iregex (str | Unset):
        resolution_isnull (bool | Unset):
        resolution_istartswith (str | Unset):
        resolution_lt (str | Unset):
        resolution_lte (str | Unset):
        resolution_range (list[str] | Unset):
        resolution_regex (str | Unset):
        resolution_startswith (str | Unset):
        result_quality (int | Unset):
        result_quality_date (datetime.date | Unset):
        result_quality_date_gt (datetime.date | Unset):
        result_quality_date_gte (datetime.date | Unset):
        result_quality_date_lt (datetime.date | Unset):
        result_quality_date_lte (datetime.date | Unset):
        result_quality_date_range (list[datetime.date] | Unset):
        result_quality_explanation (str | Unset):
        result_quality_explanation_contains (str | Unset):
        result_quality_gt (int | Unset):
        result_quality_gte (int | Unset):
        result_quality_in (list[int] | Unset):
        result_quality_isnull (bool | Unset):
        result_quality_lt (int | Unset):
        result_quality_lte (int | Unset):
        result_quality_ob_id (int | Unset):
        result_quality_ob_id_in (list[int] | Unset):
        result_quality_passes_test (bool | Unset):
        result_quality_result_title (str | Unset):
        result_quality_result_title_contains (str | Unset):
        result_field (int | Unset):
        result_field_data_path (str | Unset):
        result_field_data_path_contains (str | Unset):
        result_field_data_path_startswith (str | Unset):
        result_field_file_format (str | Unset):
        result_field_file_format_contains (str | Unset):
        result_field_gt (int | Unset):
        result_field_gte (int | Unset):
        result_field_in (list[int] | Unset):
        result_field_isnull (bool | Unset):
        result_field_lt (int | Unset):
        result_field_lte (int | Unset):
        result_field_storage_location (ObservationsListStorageLocation | Unset):
        result_field_storage_status (ObservationsListStorageStatus | Unset):
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
        status (ObservationsListDataStatus | Unset):
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
        submission_user_id (str | Unset):
        submission_user_id_contains (str | Unset):
        submission_user_id_endswith (str | Unset):
        submission_user_id_gt (str | Unset):
        submission_user_id_gte (str | Unset):
        submission_user_id_icontains (str | Unset):
        submission_user_id_iendswith (str | Unset):
        submission_user_id_iexact (str | Unset):
        submission_user_id_in (list[str] | Unset):
        submission_user_id_iregex (str | Unset):
        submission_user_id_isnull (bool | Unset):
        submission_user_id_istartswith (str | Unset):
        submission_user_id_lt (str | Unset):
        submission_user_id_lte (str | Unset):
        submission_user_id_range (list[str] | Unset):
        submission_user_id_regex (str | Unset):
        submission_user_id_startswith (str | Unset):
        time_period (int | Unset):
        time_period_end_time (datetime.datetime | Unset):
        time_period_end_time_gt (datetime.datetime | Unset):
        time_period_end_time_gte (datetime.datetime | Unset):
        time_period_end_time_lt (datetime.datetime | Unset):
        time_period_end_time_lte (datetime.datetime | Unset):
        time_period_end_time_range (list[datetime.datetime] | Unset):
        time_period_gt (int | Unset):
        time_period_gte (int | Unset):
        time_period_in (list[int] | Unset):
        time_period_isnull (bool | Unset):
        time_period_lt (int | Unset):
        time_period_lte (int | Unset):
        time_period_ob_id (int | Unset):
        time_period_ob_id_in (list[int] | Unset):
        time_period_start_time (datetime.datetime | Unset):
        time_period_start_time_gt (datetime.datetime | Unset):
        time_period_start_time_gte (datetime.datetime | Unset):
        time_period_start_time_lt (datetime.datetime | Unset):
        time_period_start_time_lte (datetime.datetime | Unset):
        time_period_start_time_range (list[datetime.datetime] | Unset):
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
        update_frequency (ObservationsListDataUpdateFrequency | Unset):
        update_frequency_contains (str | Unset):
        update_frequency_endswith (str | Unset):
        update_frequency_gt (str | Unset):
        update_frequency_gte (str | Unset):
        update_frequency_icontains (str | Unset):
        update_frequency_iendswith (str | Unset):
        update_frequency_iexact (str | Unset):
        update_frequency_in (list[str] | Unset):
        update_frequency_iregex (str | Unset):
        update_frequency_isnull (bool | Unset):
        update_frequency_istartswith (str | Unset):
        update_frequency_lt (str | Unset):
        update_frequency_lte (str | Unset):
        update_frequency_range (list[str] | Unset):
        update_frequency_regex (str | Unset):
        update_frequency_startswith (str | Unset):
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
        valid_time_period (int | Unset):
        valid_time_period_gt (int | Unset):
        valid_time_period_gte (int | Unset):
        valid_time_period_in (list[int] | Unset):
        valid_time_period_isnull (bool | Unset):
        valid_time_period_lt (int | Unset):
        valid_time_period_lte (int | Unset):
        vertical_extent (int | Unset):
        vertical_extent_gt (int | Unset):
        vertical_extent_gte (int | Unset):
        vertical_extent_in (list[int] | Unset):
        vertical_extent_isnull (bool | Unset):
        vertical_extent_lt (int | Unset):
        vertical_extent_lte (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedObservationReadList
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
        creation_date=creation_date,
        creation_date_contained_by=creation_date_contained_by,
        creation_date_contains=creation_date_contains,
        creation_date_date=creation_date_date,
        creation_date_day=creation_date_day,
        creation_date_endswith=creation_date_endswith,
        creation_date_gt=creation_date_gt,
        creation_date_gte=creation_date_gte,
        creation_date_hour=creation_date_hour,
        creation_date_icontains=creation_date_icontains,
        creation_date_iendswith=creation_date_iendswith,
        creation_date_iexact=creation_date_iexact,
        creation_date_in=creation_date_in,
        creation_date_iregex=creation_date_iregex,
        creation_date_isnull=creation_date_isnull,
        creation_date_iso_week_day=creation_date_iso_week_day,
        creation_date_iso_year=creation_date_iso_year,
        creation_date_istartswith=creation_date_istartswith,
        creation_date_lt=creation_date_lt,
        creation_date_lte=creation_date_lte,
        creation_date_minute=creation_date_minute,
        creation_date_month=creation_date_month,
        creation_date_quarter=creation_date_quarter,
        creation_date_range=creation_date_range,
        creation_date_regex=creation_date_regex,
        creation_date_second=creation_date_second,
        creation_date_startswith=creation_date_startswith,
        creation_date_time=creation_date_time,
        creation_date_week=creation_date_week,
        creation_date_week_day=creation_date_week_day,
        creation_date_year=creation_date_year,
        data_lineage=data_lineage,
        data_lineage_contains=data_lineage_contains,
        data_lineage_endswith=data_lineage_endswith,
        data_lineage_gt=data_lineage_gt,
        data_lineage_gte=data_lineage_gte,
        data_lineage_icontains=data_lineage_icontains,
        data_lineage_iendswith=data_lineage_iendswith,
        data_lineage_iexact=data_lineage_iexact,
        data_lineage_in=data_lineage_in,
        data_lineage_iregex=data_lineage_iregex,
        data_lineage_isnull=data_lineage_isnull,
        data_lineage_istartswith=data_lineage_istartswith,
        data_lineage_lt=data_lineage_lt,
        data_lineage_lte=data_lineage_lte,
        data_lineage_range=data_lineage_range,
        data_lineage_regex=data_lineage_regex,
        data_lineage_startswith=data_lineage_startswith,
        data_published_time=data_published_time,
        data_published_time_contained_by=data_published_time_contained_by,
        data_published_time_contains=data_published_time_contains,
        data_published_time_date=data_published_time_date,
        data_published_time_day=data_published_time_day,
        data_published_time_endswith=data_published_time_endswith,
        data_published_time_gt=data_published_time_gt,
        data_published_time_gte=data_published_time_gte,
        data_published_time_hour=data_published_time_hour,
        data_published_time_icontains=data_published_time_icontains,
        data_published_time_iendswith=data_published_time_iendswith,
        data_published_time_iexact=data_published_time_iexact,
        data_published_time_in=data_published_time_in,
        data_published_time_iregex=data_published_time_iregex,
        data_published_time_isnull=data_published_time_isnull,
        data_published_time_iso_week_day=data_published_time_iso_week_day,
        data_published_time_iso_year=data_published_time_iso_year,
        data_published_time_istartswith=data_published_time_istartswith,
        data_published_time_lt=data_published_time_lt,
        data_published_time_lte=data_published_time_lte,
        data_published_time_minute=data_published_time_minute,
        data_published_time_month=data_published_time_month,
        data_published_time_quarter=data_published_time_quarter,
        data_published_time_range=data_published_time_range,
        data_published_time_regex=data_published_time_regex,
        data_published_time_second=data_published_time_second,
        data_published_time_startswith=data_published_time_startswith,
        data_published_time_time=data_published_time_time,
        data_published_time_week=data_published_time_week,
        data_published_time_week_day=data_published_time_week_day,
        data_published_time_year=data_published_time_year,
        discovery_keywords_name=discovery_keywords_name,
        discovery_keywords_name_contains=discovery_keywords_name_contains,
        doi_published_time=doi_published_time,
        doi_published_time_contained_by=doi_published_time_contained_by,
        doi_published_time_contains=doi_published_time_contains,
        doi_published_time_date=doi_published_time_date,
        doi_published_time_day=doi_published_time_day,
        doi_published_time_endswith=doi_published_time_endswith,
        doi_published_time_gt=doi_published_time_gt,
        doi_published_time_gte=doi_published_time_gte,
        doi_published_time_hour=doi_published_time_hour,
        doi_published_time_icontains=doi_published_time_icontains,
        doi_published_time_iendswith=doi_published_time_iendswith,
        doi_published_time_iexact=doi_published_time_iexact,
        doi_published_time_in=doi_published_time_in,
        doi_published_time_iregex=doi_published_time_iregex,
        doi_published_time_isnull=doi_published_time_isnull,
        doi_published_time_iso_week_day=doi_published_time_iso_week_day,
        doi_published_time_iso_year=doi_published_time_iso_year,
        doi_published_time_istartswith=doi_published_time_istartswith,
        doi_published_time_lt=doi_published_time_lt,
        doi_published_time_lte=doi_published_time_lte,
        doi_published_time_minute=doi_published_time_minute,
        doi_published_time_month=doi_published_time_month,
        doi_published_time_quarter=doi_published_time_quarter,
        doi_published_time_range=doi_published_time_range,
        doi_published_time_regex=doi_published_time_regex,
        doi_published_time_second=doi_published_time_second,
        doi_published_time_startswith=doi_published_time_startswith,
        doi_published_time_time=doi_published_time_time,
        doi_published_time_week=doi_published_time_week,
        doi_published_time_week_day=doi_published_time_week_day,
        doi_published_time_year=doi_published_time_year,
        dont_harvest_from_projects=dont_harvest_from_projects,
        dont_harvest_from_projects_contains=dont_harvest_from_projects_contains,
        dont_harvest_from_projects_endswith=dont_harvest_from_projects_endswith,
        dont_harvest_from_projects_gt=dont_harvest_from_projects_gt,
        dont_harvest_from_projects_gte=dont_harvest_from_projects_gte,
        dont_harvest_from_projects_icontains=dont_harvest_from_projects_icontains,
        dont_harvest_from_projects_iendswith=dont_harvest_from_projects_iendswith,
        dont_harvest_from_projects_iexact=dont_harvest_from_projects_iexact,
        dont_harvest_from_projects_in=dont_harvest_from_projects_in,
        dont_harvest_from_projects_iregex=dont_harvest_from_projects_iregex,
        dont_harvest_from_projects_isnull=dont_harvest_from_projects_isnull,
        dont_harvest_from_projects_istartswith=dont_harvest_from_projects_istartswith,
        dont_harvest_from_projects_lt=dont_harvest_from_projects_lt,
        dont_harvest_from_projects_lte=dont_harvest_from_projects_lte,
        dont_harvest_from_projects_range=dont_harvest_from_projects_range,
        dont_harvest_from_projects_regex=dont_harvest_from_projects_regex,
        dont_harvest_from_projects_startswith=dont_harvest_from_projects_startswith,
        feature_of_interest=feature_of_interest,
        feature_of_interest_contains=feature_of_interest_contains,
        feature_of_interest_endswith=feature_of_interest_endswith,
        feature_of_interest_gt=feature_of_interest_gt,
        feature_of_interest_gte=feature_of_interest_gte,
        feature_of_interest_icontains=feature_of_interest_icontains,
        feature_of_interest_iendswith=feature_of_interest_iendswith,
        feature_of_interest_iexact=feature_of_interest_iexact,
        feature_of_interest_in=feature_of_interest_in,
        feature_of_interest_iregex=feature_of_interest_iregex,
        feature_of_interest_isnull=feature_of_interest_isnull,
        feature_of_interest_istartswith=feature_of_interest_istartswith,
        feature_of_interest_lt=feature_of_interest_lt,
        feature_of_interest_lte=feature_of_interest_lte,
        feature_of_interest_range=feature_of_interest_range,
        feature_of_interest_regex=feature_of_interest_regex,
        feature_of_interest_startswith=feature_of_interest_startswith,
        geographic_extent=geographic_extent,
        geographic_extent_east_bound_longitude=geographic_extent_east_bound_longitude,
        geographic_extent_east_bound_longitude_gt=geographic_extent_east_bound_longitude_gt,
        geographic_extent_east_bound_longitude_gte=geographic_extent_east_bound_longitude_gte,
        geographic_extent_east_bound_longitude_lt=geographic_extent_east_bound_longitude_lt,
        geographic_extent_east_bound_longitude_lte=geographic_extent_east_bound_longitude_lte,
        geographic_extent_east_bound_longitude_range=geographic_extent_east_bound_longitude_range,
        geographic_extent_gt=geographic_extent_gt,
        geographic_extent_gte=geographic_extent_gte,
        geographic_extent_in=geographic_extent_in,
        geographic_extent_isnull=geographic_extent_isnull,
        geographic_extent_lt=geographic_extent_lt,
        geographic_extent_lte=geographic_extent_lte,
        geographic_extent_north_bound_latitude=geographic_extent_north_bound_latitude,
        geographic_extent_north_bound_latitude_gt=geographic_extent_north_bound_latitude_gt,
        geographic_extent_north_bound_latitude_gte=geographic_extent_north_bound_latitude_gte,
        geographic_extent_north_bound_latitude_lt=geographic_extent_north_bound_latitude_lt,
        geographic_extent_north_bound_latitude_lte=geographic_extent_north_bound_latitude_lte,
        geographic_extent_north_bound_latitude_range=geographic_extent_north_bound_latitude_range,
        geographic_extent_ob_id=geographic_extent_ob_id,
        geographic_extent_ob_id_in=geographic_extent_ob_id_in,
        geographic_extent_south_bound_latitude=geographic_extent_south_bound_latitude,
        geographic_extent_south_bound_latitude_gt=geographic_extent_south_bound_latitude_gt,
        geographic_extent_south_bound_latitude_gte=geographic_extent_south_bound_latitude_gte,
        geographic_extent_south_bound_latitude_lt=geographic_extent_south_bound_latitude_lt,
        geographic_extent_south_bound_latitude_lte=geographic_extent_south_bound_latitude_lte,
        geographic_extent_south_bound_latitude_range=geographic_extent_south_bound_latitude_range,
        geographic_extent_west_bound_longitude=geographic_extent_west_bound_longitude,
        geographic_extent_west_bound_longitude_gt=geographic_extent_west_bound_longitude_gt,
        geographic_extent_west_bound_longitude_gte=geographic_extent_west_bound_longitude_gte,
        geographic_extent_west_bound_longitude_lt=geographic_extent_west_bound_longitude_lt,
        geographic_extent_west_bound_longitude_lte=geographic_extent_west_bound_longitude_lte,
        geographic_extent_west_bound_longitude_range=geographic_extent_west_bound_longitude_range,
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
        language=language,
        language_contains=language_contains,
        language_endswith=language_endswith,
        language_gt=language_gt,
        language_gte=language_gte,
        language_icontains=language_icontains,
        language_iendswith=language_iendswith,
        language_iexact=language_iexact,
        language_in=language_in,
        language_iregex=language_iregex,
        language_isnull=language_isnull,
        language_istartswith=language_istartswith,
        language_lt=language_lt,
        language_lte=language_lte,
        language_range=language_range,
        language_regex=language_regex,
        language_startswith=language_startswith,
        last_updated_date=last_updated_date,
        last_updated_date_contained_by=last_updated_date_contained_by,
        last_updated_date_contains=last_updated_date_contains,
        last_updated_date_date=last_updated_date_date,
        last_updated_date_day=last_updated_date_day,
        last_updated_date_endswith=last_updated_date_endswith,
        last_updated_date_gt=last_updated_date_gt,
        last_updated_date_gte=last_updated_date_gte,
        last_updated_date_hour=last_updated_date_hour,
        last_updated_date_icontains=last_updated_date_icontains,
        last_updated_date_iendswith=last_updated_date_iendswith,
        last_updated_date_iexact=last_updated_date_iexact,
        last_updated_date_in=last_updated_date_in,
        last_updated_date_iregex=last_updated_date_iregex,
        last_updated_date_isnull=last_updated_date_isnull,
        last_updated_date_iso_week_day=last_updated_date_iso_week_day,
        last_updated_date_iso_year=last_updated_date_iso_year,
        last_updated_date_istartswith=last_updated_date_istartswith,
        last_updated_date_lt=last_updated_date_lt,
        last_updated_date_lte=last_updated_date_lte,
        last_updated_date_minute=last_updated_date_minute,
        last_updated_date_month=last_updated_date_month,
        last_updated_date_quarter=last_updated_date_quarter,
        last_updated_date_range=last_updated_date_range,
        last_updated_date_regex=last_updated_date_regex,
        last_updated_date_second=last_updated_date_second,
        last_updated_date_startswith=last_updated_date_startswith,
        last_updated_date_time=last_updated_date_time,
        last_updated_date_week=last_updated_date_week,
        last_updated_date_week_day=last_updated_date_week_day,
        last_updated_date_year=last_updated_date_year,
        latest_data_update_time=latest_data_update_time,
        latest_data_update_time_contained_by=latest_data_update_time_contained_by,
        latest_data_update_time_contains=latest_data_update_time_contains,
        latest_data_update_time_date=latest_data_update_time_date,
        latest_data_update_time_day=latest_data_update_time_day,
        latest_data_update_time_endswith=latest_data_update_time_endswith,
        latest_data_update_time_gt=latest_data_update_time_gt,
        latest_data_update_time_gte=latest_data_update_time_gte,
        latest_data_update_time_hour=latest_data_update_time_hour,
        latest_data_update_time_icontains=latest_data_update_time_icontains,
        latest_data_update_time_iendswith=latest_data_update_time_iendswith,
        latest_data_update_time_iexact=latest_data_update_time_iexact,
        latest_data_update_time_in=latest_data_update_time_in,
        latest_data_update_time_iregex=latest_data_update_time_iregex,
        latest_data_update_time_isnull=latest_data_update_time_isnull,
        latest_data_update_time_iso_week_day=latest_data_update_time_iso_week_day,
        latest_data_update_time_iso_year=latest_data_update_time_iso_year,
        latest_data_update_time_istartswith=latest_data_update_time_istartswith,
        latest_data_update_time_lt=latest_data_update_time_lt,
        latest_data_update_time_lte=latest_data_update_time_lte,
        latest_data_update_time_minute=latest_data_update_time_minute,
        latest_data_update_time_month=latest_data_update_time_month,
        latest_data_update_time_quarter=latest_data_update_time_quarter,
        latest_data_update_time_range=latest_data_update_time_range,
        latest_data_update_time_regex=latest_data_update_time_regex,
        latest_data_update_time_second=latest_data_update_time_second,
        latest_data_update_time_startswith=latest_data_update_time_startswith,
        latest_data_update_time_time=latest_data_update_time_time,
        latest_data_update_time_week=latest_data_update_time_week,
        latest_data_update_time_week_day=latest_data_update_time_week_day,
        latest_data_update_time_year=latest_data_update_time_year,
        limit=limit,
        non_geographic_flag=non_geographic_flag,
        non_geographic_flag_contains=non_geographic_flag_contains,
        non_geographic_flag_endswith=non_geographic_flag_endswith,
        non_geographic_flag_gt=non_geographic_flag_gt,
        non_geographic_flag_gte=non_geographic_flag_gte,
        non_geographic_flag_icontains=non_geographic_flag_icontains,
        non_geographic_flag_iendswith=non_geographic_flag_iendswith,
        non_geographic_flag_iexact=non_geographic_flag_iexact,
        non_geographic_flag_in=non_geographic_flag_in,
        non_geographic_flag_iregex=non_geographic_flag_iregex,
        non_geographic_flag_isnull=non_geographic_flag_isnull,
        non_geographic_flag_istartswith=non_geographic_flag_istartswith,
        non_geographic_flag_lt=non_geographic_flag_lt,
        non_geographic_flag_lte=non_geographic_flag_lte,
        non_geographic_flag_range=non_geographic_flag_range,
        non_geographic_flag_regex=non_geographic_flag_regex,
        non_geographic_flag_startswith=non_geographic_flag_startswith,
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
        permissions_access_category=permissions_access_category,
        permissions_access_category_in=permissions_access_category_in,
        permissions_access_roles=permissions_access_roles,
        permissions_access_roles_in=permissions_access_roles_in,
        procedure_acquisition=procedure_acquisition,
        procedure_acquisition_gt=procedure_acquisition_gt,
        procedure_acquisition_gte=procedure_acquisition_gte,
        procedure_acquisition_in=procedure_acquisition_in,
        procedure_acquisition_isnull=procedure_acquisition_isnull,
        procedure_acquisition_lt=procedure_acquisition_lt,
        procedure_acquisition_lte=procedure_acquisition_lte,
        procedure_acquisition_ob_id=procedure_acquisition_ob_id,
        procedure_acquisition_ob_id_in=procedure_acquisition_ob_id_in,
        procedure_acquisition_uuid=procedure_acquisition_uuid,
        procedure_acquisition_uuid_in=procedure_acquisition_uuid_in,
        procedure_composite_process=procedure_composite_process,
        procedure_composite_process_gt=procedure_composite_process_gt,
        procedure_composite_process_gte=procedure_composite_process_gte,
        procedure_composite_process_in=procedure_composite_process_in,
        procedure_composite_process_isnull=procedure_composite_process_isnull,
        procedure_composite_process_lt=procedure_composite_process_lt,
        procedure_composite_process_lte=procedure_composite_process_lte,
        procedure_computation=procedure_computation,
        procedure_computation_gt=procedure_computation_gt,
        procedure_computation_gte=procedure_computation_gte,
        procedure_computation_in=procedure_computation_in,
        procedure_computation_isnull=procedure_computation_isnull,
        procedure_computation_lt=procedure_computation_lt,
        procedure_computation_lte=procedure_computation_lte,
        procedure_description=procedure_description,
        procedure_description_contains=procedure_description_contains,
        procedure_description_endswith=procedure_description_endswith,
        procedure_description_gt=procedure_description_gt,
        procedure_description_gte=procedure_description_gte,
        procedure_description_icontains=procedure_description_icontains,
        procedure_description_iendswith=procedure_description_iendswith,
        procedure_description_iexact=procedure_description_iexact,
        procedure_description_in=procedure_description_in,
        procedure_description_iregex=procedure_description_iregex,
        procedure_description_isnull=procedure_description_isnull,
        procedure_description_istartswith=procedure_description_istartswith,
        procedure_description_lt=procedure_description_lt,
        procedure_description_lte=procedure_description_lte,
        procedure_description_range=procedure_description_range,
        procedure_description_regex=procedure_description_regex,
        procedure_description_startswith=procedure_description_startswith,
        projects_ob_id=projects_ob_id,
        projects_ob_id_in=projects_ob_id_in,
        projects_uuid=projects_uuid,
        projects_uuid_in=projects_uuid_in,
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
        removed_data_reason=removed_data_reason,
        removed_data_reason_contains=removed_data_reason_contains,
        removed_data_reason_endswith=removed_data_reason_endswith,
        removed_data_reason_gt=removed_data_reason_gt,
        removed_data_reason_gte=removed_data_reason_gte,
        removed_data_reason_icontains=removed_data_reason_icontains,
        removed_data_reason_iendswith=removed_data_reason_iendswith,
        removed_data_reason_iexact=removed_data_reason_iexact,
        removed_data_reason_in=removed_data_reason_in,
        removed_data_reason_iregex=removed_data_reason_iregex,
        removed_data_reason_isnull=removed_data_reason_isnull,
        removed_data_reason_istartswith=removed_data_reason_istartswith,
        removed_data_reason_lt=removed_data_reason_lt,
        removed_data_reason_lte=removed_data_reason_lte,
        removed_data_reason_range=removed_data_reason_range,
        removed_data_reason_regex=removed_data_reason_regex,
        removed_data_reason_startswith=removed_data_reason_startswith,
        removed_data_time=removed_data_time,
        removed_data_time_contained_by=removed_data_time_contained_by,
        removed_data_time_contains=removed_data_time_contains,
        removed_data_time_date=removed_data_time_date,
        removed_data_time_day=removed_data_time_day,
        removed_data_time_endswith=removed_data_time_endswith,
        removed_data_time_gt=removed_data_time_gt,
        removed_data_time_gte=removed_data_time_gte,
        removed_data_time_hour=removed_data_time_hour,
        removed_data_time_icontains=removed_data_time_icontains,
        removed_data_time_iendswith=removed_data_time_iendswith,
        removed_data_time_iexact=removed_data_time_iexact,
        removed_data_time_in=removed_data_time_in,
        removed_data_time_iregex=removed_data_time_iregex,
        removed_data_time_isnull=removed_data_time_isnull,
        removed_data_time_iso_week_day=removed_data_time_iso_week_day,
        removed_data_time_iso_year=removed_data_time_iso_year,
        removed_data_time_istartswith=removed_data_time_istartswith,
        removed_data_time_lt=removed_data_time_lt,
        removed_data_time_lte=removed_data_time_lte,
        removed_data_time_minute=removed_data_time_minute,
        removed_data_time_month=removed_data_time_month,
        removed_data_time_quarter=removed_data_time_quarter,
        removed_data_time_range=removed_data_time_range,
        removed_data_time_regex=removed_data_time_regex,
        removed_data_time_second=removed_data_time_second,
        removed_data_time_startswith=removed_data_time_startswith,
        removed_data_time_time=removed_data_time_time,
        removed_data_time_week=removed_data_time_week,
        removed_data_time_week_day=removed_data_time_week_day,
        removed_data_time_year=removed_data_time_year,
        resolution=resolution,
        resolution_contains=resolution_contains,
        resolution_endswith=resolution_endswith,
        resolution_gt=resolution_gt,
        resolution_gte=resolution_gte,
        resolution_icontains=resolution_icontains,
        resolution_iendswith=resolution_iendswith,
        resolution_iexact=resolution_iexact,
        resolution_in=resolution_in,
        resolution_iregex=resolution_iregex,
        resolution_isnull=resolution_isnull,
        resolution_istartswith=resolution_istartswith,
        resolution_lt=resolution_lt,
        resolution_lte=resolution_lte,
        resolution_range=resolution_range,
        resolution_regex=resolution_regex,
        resolution_startswith=resolution_startswith,
        result_quality=result_quality,
        result_quality_date=result_quality_date,
        result_quality_date_gt=result_quality_date_gt,
        result_quality_date_gte=result_quality_date_gte,
        result_quality_date_lt=result_quality_date_lt,
        result_quality_date_lte=result_quality_date_lte,
        result_quality_date_range=result_quality_date_range,
        result_quality_explanation=result_quality_explanation,
        result_quality_explanation_contains=result_quality_explanation_contains,
        result_quality_gt=result_quality_gt,
        result_quality_gte=result_quality_gte,
        result_quality_in=result_quality_in,
        result_quality_isnull=result_quality_isnull,
        result_quality_lt=result_quality_lt,
        result_quality_lte=result_quality_lte,
        result_quality_ob_id=result_quality_ob_id,
        result_quality_ob_id_in=result_quality_ob_id_in,
        result_quality_passes_test=result_quality_passes_test,
        result_quality_result_title=result_quality_result_title,
        result_quality_result_title_contains=result_quality_result_title_contains,
        result_field=result_field,
        result_field_data_path=result_field_data_path,
        result_field_data_path_contains=result_field_data_path_contains,
        result_field_data_path_startswith=result_field_data_path_startswith,
        result_field_file_format=result_field_file_format,
        result_field_file_format_contains=result_field_file_format_contains,
        result_field_gt=result_field_gt,
        result_field_gte=result_field_gte,
        result_field_in=result_field_in,
        result_field_isnull=result_field_isnull,
        result_field_lt=result_field_lt,
        result_field_lte=result_field_lte,
        result_field_storage_location=result_field_storage_location,
        result_field_storage_status=result_field_storage_status,
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
        submission_user_id=submission_user_id,
        submission_user_id_contains=submission_user_id_contains,
        submission_user_id_endswith=submission_user_id_endswith,
        submission_user_id_gt=submission_user_id_gt,
        submission_user_id_gte=submission_user_id_gte,
        submission_user_id_icontains=submission_user_id_icontains,
        submission_user_id_iendswith=submission_user_id_iendswith,
        submission_user_id_iexact=submission_user_id_iexact,
        submission_user_id_in=submission_user_id_in,
        submission_user_id_iregex=submission_user_id_iregex,
        submission_user_id_isnull=submission_user_id_isnull,
        submission_user_id_istartswith=submission_user_id_istartswith,
        submission_user_id_lt=submission_user_id_lt,
        submission_user_id_lte=submission_user_id_lte,
        submission_user_id_range=submission_user_id_range,
        submission_user_id_regex=submission_user_id_regex,
        submission_user_id_startswith=submission_user_id_startswith,
        time_period=time_period,
        time_period_end_time=time_period_end_time,
        time_period_end_time_gt=time_period_end_time_gt,
        time_period_end_time_gte=time_period_end_time_gte,
        time_period_end_time_lt=time_period_end_time_lt,
        time_period_end_time_lte=time_period_end_time_lte,
        time_period_end_time_range=time_period_end_time_range,
        time_period_gt=time_period_gt,
        time_period_gte=time_period_gte,
        time_period_in=time_period_in,
        time_period_isnull=time_period_isnull,
        time_period_lt=time_period_lt,
        time_period_lte=time_period_lte,
        time_period_ob_id=time_period_ob_id,
        time_period_ob_id_in=time_period_ob_id_in,
        time_period_start_time=time_period_start_time,
        time_period_start_time_gt=time_period_start_time_gt,
        time_period_start_time_gte=time_period_start_time_gte,
        time_period_start_time_lt=time_period_start_time_lt,
        time_period_start_time_lte=time_period_start_time_lte,
        time_period_start_time_range=time_period_start_time_range,
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
        update_frequency=update_frequency,
        update_frequency_contains=update_frequency_contains,
        update_frequency_endswith=update_frequency_endswith,
        update_frequency_gt=update_frequency_gt,
        update_frequency_gte=update_frequency_gte,
        update_frequency_icontains=update_frequency_icontains,
        update_frequency_iendswith=update_frequency_iendswith,
        update_frequency_iexact=update_frequency_iexact,
        update_frequency_in=update_frequency_in,
        update_frequency_iregex=update_frequency_iregex,
        update_frequency_isnull=update_frequency_isnull,
        update_frequency_istartswith=update_frequency_istartswith,
        update_frequency_lt=update_frequency_lt,
        update_frequency_lte=update_frequency_lte,
        update_frequency_range=update_frequency_range,
        update_frequency_regex=update_frequency_regex,
        update_frequency_startswith=update_frequency_startswith,
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
        valid_time_period=valid_time_period,
        valid_time_period_gt=valid_time_period_gt,
        valid_time_period_gte=valid_time_period_gte,
        valid_time_period_in=valid_time_period_in,
        valid_time_period_isnull=valid_time_period_isnull,
        valid_time_period_lt=valid_time_period_lt,
        valid_time_period_lte=valid_time_period_lte,
        vertical_extent=vertical_extent,
        vertical_extent_gt=vertical_extent_gt,
        vertical_extent_gte=vertical_extent_gte,
        vertical_extent_in=vertical_extent_in,
        vertical_extent_isnull=vertical_extent_isnull,
        vertical_extent_lt=vertical_extent_lt,
        vertical_extent_lte=vertical_extent_lte,
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
    creation_date: datetime.datetime | Unset = UNSET,
    creation_date_contained_by: datetime.datetime | Unset = UNSET,
    creation_date_contains: datetime.datetime | Unset = UNSET,
    creation_date_date: datetime.date | Unset = UNSET,
    creation_date_day: float | Unset = UNSET,
    creation_date_endswith: datetime.datetime | Unset = UNSET,
    creation_date_gt: datetime.datetime | Unset = UNSET,
    creation_date_gte: datetime.datetime | Unset = UNSET,
    creation_date_hour: float | Unset = UNSET,
    creation_date_icontains: datetime.datetime | Unset = UNSET,
    creation_date_iendswith: datetime.datetime | Unset = UNSET,
    creation_date_iexact: datetime.datetime | Unset = UNSET,
    creation_date_in: list[datetime.datetime] | Unset = UNSET,
    creation_date_iregex: datetime.datetime | Unset = UNSET,
    creation_date_isnull: bool | Unset = UNSET,
    creation_date_iso_week_day: float | Unset = UNSET,
    creation_date_iso_year: float | Unset = UNSET,
    creation_date_istartswith: datetime.datetime | Unset = UNSET,
    creation_date_lt: datetime.datetime | Unset = UNSET,
    creation_date_lte: datetime.datetime | Unset = UNSET,
    creation_date_minute: float | Unset = UNSET,
    creation_date_month: float | Unset = UNSET,
    creation_date_quarter: float | Unset = UNSET,
    creation_date_range: list[datetime.datetime] | Unset = UNSET,
    creation_date_regex: datetime.datetime | Unset = UNSET,
    creation_date_second: float | Unset = UNSET,
    creation_date_startswith: datetime.datetime | Unset = UNSET,
    creation_date_time: str | Unset = UNSET,
    creation_date_week: float | Unset = UNSET,
    creation_date_week_day: float | Unset = UNSET,
    creation_date_year: float | Unset = UNSET,
    data_lineage: str | Unset = UNSET,
    data_lineage_contains: str | Unset = UNSET,
    data_lineage_endswith: str | Unset = UNSET,
    data_lineage_gt: str | Unset = UNSET,
    data_lineage_gte: str | Unset = UNSET,
    data_lineage_icontains: str | Unset = UNSET,
    data_lineage_iendswith: str | Unset = UNSET,
    data_lineage_iexact: str | Unset = UNSET,
    data_lineage_in: list[str] | Unset = UNSET,
    data_lineage_iregex: str | Unset = UNSET,
    data_lineage_isnull: bool | Unset = UNSET,
    data_lineage_istartswith: str | Unset = UNSET,
    data_lineage_lt: str | Unset = UNSET,
    data_lineage_lte: str | Unset = UNSET,
    data_lineage_range: list[str] | Unset = UNSET,
    data_lineage_regex: str | Unset = UNSET,
    data_lineage_startswith: str | Unset = UNSET,
    data_published_time: datetime.datetime | Unset = UNSET,
    data_published_time_contained_by: datetime.datetime | Unset = UNSET,
    data_published_time_contains: datetime.datetime | Unset = UNSET,
    data_published_time_date: datetime.date | Unset = UNSET,
    data_published_time_day: float | Unset = UNSET,
    data_published_time_endswith: datetime.datetime | Unset = UNSET,
    data_published_time_gt: datetime.datetime | Unset = UNSET,
    data_published_time_gte: datetime.datetime | Unset = UNSET,
    data_published_time_hour: float | Unset = UNSET,
    data_published_time_icontains: datetime.datetime | Unset = UNSET,
    data_published_time_iendswith: datetime.datetime | Unset = UNSET,
    data_published_time_iexact: datetime.datetime | Unset = UNSET,
    data_published_time_in: list[datetime.datetime] | Unset = UNSET,
    data_published_time_iregex: datetime.datetime | Unset = UNSET,
    data_published_time_isnull: bool | Unset = UNSET,
    data_published_time_iso_week_day: float | Unset = UNSET,
    data_published_time_iso_year: float | Unset = UNSET,
    data_published_time_istartswith: datetime.datetime | Unset = UNSET,
    data_published_time_lt: datetime.datetime | Unset = UNSET,
    data_published_time_lte: datetime.datetime | Unset = UNSET,
    data_published_time_minute: float | Unset = UNSET,
    data_published_time_month: float | Unset = UNSET,
    data_published_time_quarter: float | Unset = UNSET,
    data_published_time_range: list[datetime.datetime] | Unset = UNSET,
    data_published_time_regex: datetime.datetime | Unset = UNSET,
    data_published_time_second: float | Unset = UNSET,
    data_published_time_startswith: datetime.datetime | Unset = UNSET,
    data_published_time_time: str | Unset = UNSET,
    data_published_time_week: float | Unset = UNSET,
    data_published_time_week_day: float | Unset = UNSET,
    data_published_time_year: float | Unset = UNSET,
    discovery_keywords_name: str | Unset = UNSET,
    discovery_keywords_name_contains: str | Unset = UNSET,
    doi_published_time: datetime.datetime | Unset = UNSET,
    doi_published_time_contained_by: datetime.datetime | Unset = UNSET,
    doi_published_time_contains: datetime.datetime | Unset = UNSET,
    doi_published_time_date: datetime.date | Unset = UNSET,
    doi_published_time_day: float | Unset = UNSET,
    doi_published_time_endswith: datetime.datetime | Unset = UNSET,
    doi_published_time_gt: datetime.datetime | Unset = UNSET,
    doi_published_time_gte: datetime.datetime | Unset = UNSET,
    doi_published_time_hour: float | Unset = UNSET,
    doi_published_time_icontains: datetime.datetime | Unset = UNSET,
    doi_published_time_iendswith: datetime.datetime | Unset = UNSET,
    doi_published_time_iexact: datetime.datetime | Unset = UNSET,
    doi_published_time_in: list[datetime.datetime] | Unset = UNSET,
    doi_published_time_iregex: datetime.datetime | Unset = UNSET,
    doi_published_time_isnull: bool | Unset = UNSET,
    doi_published_time_iso_week_day: float | Unset = UNSET,
    doi_published_time_iso_year: float | Unset = UNSET,
    doi_published_time_istartswith: datetime.datetime | Unset = UNSET,
    doi_published_time_lt: datetime.datetime | Unset = UNSET,
    doi_published_time_lte: datetime.datetime | Unset = UNSET,
    doi_published_time_minute: float | Unset = UNSET,
    doi_published_time_month: float | Unset = UNSET,
    doi_published_time_quarter: float | Unset = UNSET,
    doi_published_time_range: list[datetime.datetime] | Unset = UNSET,
    doi_published_time_regex: datetime.datetime | Unset = UNSET,
    doi_published_time_second: float | Unset = UNSET,
    doi_published_time_startswith: datetime.datetime | Unset = UNSET,
    doi_published_time_time: str | Unset = UNSET,
    doi_published_time_week: float | Unset = UNSET,
    doi_published_time_week_day: float | Unset = UNSET,
    doi_published_time_year: float | Unset = UNSET,
    dont_harvest_from_projects: bool | Unset = UNSET,
    dont_harvest_from_projects_contains: bool | Unset = UNSET,
    dont_harvest_from_projects_endswith: bool | Unset = UNSET,
    dont_harvest_from_projects_gt: bool | Unset = UNSET,
    dont_harvest_from_projects_gte: bool | Unset = UNSET,
    dont_harvest_from_projects_icontains: bool | Unset = UNSET,
    dont_harvest_from_projects_iendswith: bool | Unset = UNSET,
    dont_harvest_from_projects_iexact: bool | Unset = UNSET,
    dont_harvest_from_projects_in: list[bool] | Unset = UNSET,
    dont_harvest_from_projects_iregex: bool | Unset = UNSET,
    dont_harvest_from_projects_isnull: bool | Unset = UNSET,
    dont_harvest_from_projects_istartswith: bool | Unset = UNSET,
    dont_harvest_from_projects_lt: bool | Unset = UNSET,
    dont_harvest_from_projects_lte: bool | Unset = UNSET,
    dont_harvest_from_projects_range: list[bool] | Unset = UNSET,
    dont_harvest_from_projects_regex: bool | Unset = UNSET,
    dont_harvest_from_projects_startswith: bool | Unset = UNSET,
    feature_of_interest: str | Unset = UNSET,
    feature_of_interest_contains: str | Unset = UNSET,
    feature_of_interest_endswith: str | Unset = UNSET,
    feature_of_interest_gt: str | Unset = UNSET,
    feature_of_interest_gte: str | Unset = UNSET,
    feature_of_interest_icontains: str | Unset = UNSET,
    feature_of_interest_iendswith: str | Unset = UNSET,
    feature_of_interest_iexact: str | Unset = UNSET,
    feature_of_interest_in: list[str] | Unset = UNSET,
    feature_of_interest_iregex: str | Unset = UNSET,
    feature_of_interest_isnull: bool | Unset = UNSET,
    feature_of_interest_istartswith: str | Unset = UNSET,
    feature_of_interest_lt: str | Unset = UNSET,
    feature_of_interest_lte: str | Unset = UNSET,
    feature_of_interest_range: list[str] | Unset = UNSET,
    feature_of_interest_regex: str | Unset = UNSET,
    feature_of_interest_startswith: str | Unset = UNSET,
    geographic_extent: int | Unset = UNSET,
    geographic_extent_east_bound_longitude: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_gt: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_gte: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_lt: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_lte: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_range: list[float] | Unset = UNSET,
    geographic_extent_gt: int | Unset = UNSET,
    geographic_extent_gte: int | Unset = UNSET,
    geographic_extent_in: list[int] | Unset = UNSET,
    geographic_extent_isnull: bool | Unset = UNSET,
    geographic_extent_lt: int | Unset = UNSET,
    geographic_extent_lte: int | Unset = UNSET,
    geographic_extent_north_bound_latitude: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_gt: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_gte: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_lt: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_lte: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_range: list[float] | Unset = UNSET,
    geographic_extent_ob_id: int | Unset = UNSET,
    geographic_extent_ob_id_in: list[int] | Unset = UNSET,
    geographic_extent_south_bound_latitude: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_gt: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_gte: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_lt: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_lte: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_range: list[float] | Unset = UNSET,
    geographic_extent_west_bound_longitude: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_gt: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_gte: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_lt: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_lte: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_range: list[float] | Unset = UNSET,
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
    language: ObservationsListLanguage | Unset = UNSET,
    language_contains: str | Unset = UNSET,
    language_endswith: str | Unset = UNSET,
    language_gt: str | Unset = UNSET,
    language_gte: str | Unset = UNSET,
    language_icontains: str | Unset = UNSET,
    language_iendswith: str | Unset = UNSET,
    language_iexact: str | Unset = UNSET,
    language_in: list[str] | Unset = UNSET,
    language_iregex: str | Unset = UNSET,
    language_isnull: bool | Unset = UNSET,
    language_istartswith: str | Unset = UNSET,
    language_lt: str | Unset = UNSET,
    language_lte: str | Unset = UNSET,
    language_range: list[str] | Unset = UNSET,
    language_regex: str | Unset = UNSET,
    language_startswith: str | Unset = UNSET,
    last_updated_date: datetime.datetime | Unset = UNSET,
    last_updated_date_contained_by: datetime.datetime | Unset = UNSET,
    last_updated_date_contains: datetime.datetime | Unset = UNSET,
    last_updated_date_date: datetime.date | Unset = UNSET,
    last_updated_date_day: float | Unset = UNSET,
    last_updated_date_endswith: datetime.datetime | Unset = UNSET,
    last_updated_date_gt: datetime.datetime | Unset = UNSET,
    last_updated_date_gte: datetime.datetime | Unset = UNSET,
    last_updated_date_hour: float | Unset = UNSET,
    last_updated_date_icontains: datetime.datetime | Unset = UNSET,
    last_updated_date_iendswith: datetime.datetime | Unset = UNSET,
    last_updated_date_iexact: datetime.datetime | Unset = UNSET,
    last_updated_date_in: list[datetime.datetime] | Unset = UNSET,
    last_updated_date_iregex: datetime.datetime | Unset = UNSET,
    last_updated_date_isnull: bool | Unset = UNSET,
    last_updated_date_iso_week_day: float | Unset = UNSET,
    last_updated_date_iso_year: float | Unset = UNSET,
    last_updated_date_istartswith: datetime.datetime | Unset = UNSET,
    last_updated_date_lt: datetime.datetime | Unset = UNSET,
    last_updated_date_lte: datetime.datetime | Unset = UNSET,
    last_updated_date_minute: float | Unset = UNSET,
    last_updated_date_month: float | Unset = UNSET,
    last_updated_date_quarter: float | Unset = UNSET,
    last_updated_date_range: list[datetime.datetime] | Unset = UNSET,
    last_updated_date_regex: datetime.datetime | Unset = UNSET,
    last_updated_date_second: float | Unset = UNSET,
    last_updated_date_startswith: datetime.datetime | Unset = UNSET,
    last_updated_date_time: str | Unset = UNSET,
    last_updated_date_week: float | Unset = UNSET,
    last_updated_date_week_day: float | Unset = UNSET,
    last_updated_date_year: float | Unset = UNSET,
    latest_data_update_time: datetime.datetime | Unset = UNSET,
    latest_data_update_time_contained_by: datetime.datetime | Unset = UNSET,
    latest_data_update_time_contains: datetime.datetime | Unset = UNSET,
    latest_data_update_time_date: datetime.date | Unset = UNSET,
    latest_data_update_time_day: float | Unset = UNSET,
    latest_data_update_time_endswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_gt: datetime.datetime | Unset = UNSET,
    latest_data_update_time_gte: datetime.datetime | Unset = UNSET,
    latest_data_update_time_hour: float | Unset = UNSET,
    latest_data_update_time_icontains: datetime.datetime | Unset = UNSET,
    latest_data_update_time_iendswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_iexact: datetime.datetime | Unset = UNSET,
    latest_data_update_time_in: list[datetime.datetime] | Unset = UNSET,
    latest_data_update_time_iregex: datetime.datetime | Unset = UNSET,
    latest_data_update_time_isnull: bool | Unset = UNSET,
    latest_data_update_time_iso_week_day: float | Unset = UNSET,
    latest_data_update_time_iso_year: float | Unset = UNSET,
    latest_data_update_time_istartswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_lt: datetime.datetime | Unset = UNSET,
    latest_data_update_time_lte: datetime.datetime | Unset = UNSET,
    latest_data_update_time_minute: float | Unset = UNSET,
    latest_data_update_time_month: float | Unset = UNSET,
    latest_data_update_time_quarter: float | Unset = UNSET,
    latest_data_update_time_range: list[datetime.datetime] | Unset = UNSET,
    latest_data_update_time_regex: datetime.datetime | Unset = UNSET,
    latest_data_update_time_second: float | Unset = UNSET,
    latest_data_update_time_startswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_time: str | Unset = UNSET,
    latest_data_update_time_week: float | Unset = UNSET,
    latest_data_update_time_week_day: float | Unset = UNSET,
    latest_data_update_time_year: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    non_geographic_flag: bool | Unset = UNSET,
    non_geographic_flag_contains: bool | Unset = UNSET,
    non_geographic_flag_endswith: bool | Unset = UNSET,
    non_geographic_flag_gt: bool | Unset = UNSET,
    non_geographic_flag_gte: bool | Unset = UNSET,
    non_geographic_flag_icontains: bool | Unset = UNSET,
    non_geographic_flag_iendswith: bool | Unset = UNSET,
    non_geographic_flag_iexact: bool | Unset = UNSET,
    non_geographic_flag_in: list[bool] | Unset = UNSET,
    non_geographic_flag_iregex: bool | Unset = UNSET,
    non_geographic_flag_isnull: bool | Unset = UNSET,
    non_geographic_flag_istartswith: bool | Unset = UNSET,
    non_geographic_flag_lt: bool | Unset = UNSET,
    non_geographic_flag_lte: bool | Unset = UNSET,
    non_geographic_flag_range: list[bool] | Unset = UNSET,
    non_geographic_flag_regex: bool | Unset = UNSET,
    non_geographic_flag_startswith: bool | Unset = UNSET,
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
    permissions_access_category: ObservationsListAccessCategory | Unset = UNSET,
    permissions_access_category_in: list[str] | Unset = UNSET,
    permissions_access_roles: str | Unset = UNSET,
    permissions_access_roles_in: list[str] | Unset = UNSET,
    procedure_acquisition: int | Unset = UNSET,
    procedure_acquisition_gt: int | Unset = UNSET,
    procedure_acquisition_gte: int | Unset = UNSET,
    procedure_acquisition_in: list[int] | Unset = UNSET,
    procedure_acquisition_isnull: bool | Unset = UNSET,
    procedure_acquisition_lt: int | Unset = UNSET,
    procedure_acquisition_lte: int | Unset = UNSET,
    procedure_acquisition_ob_id: int | Unset = UNSET,
    procedure_acquisition_ob_id_in: list[int] | Unset = UNSET,
    procedure_acquisition_uuid: str | Unset = UNSET,
    procedure_acquisition_uuid_in: list[str] | Unset = UNSET,
    procedure_composite_process: int | Unset = UNSET,
    procedure_composite_process_gt: int | Unset = UNSET,
    procedure_composite_process_gte: int | Unset = UNSET,
    procedure_composite_process_in: list[int] | Unset = UNSET,
    procedure_composite_process_isnull: bool | Unset = UNSET,
    procedure_composite_process_lt: int | Unset = UNSET,
    procedure_composite_process_lte: int | Unset = UNSET,
    procedure_computation: int | Unset = UNSET,
    procedure_computation_gt: int | Unset = UNSET,
    procedure_computation_gte: int | Unset = UNSET,
    procedure_computation_in: list[int] | Unset = UNSET,
    procedure_computation_isnull: bool | Unset = UNSET,
    procedure_computation_lt: int | Unset = UNSET,
    procedure_computation_lte: int | Unset = UNSET,
    procedure_description: str | Unset = UNSET,
    procedure_description_contains: str | Unset = UNSET,
    procedure_description_endswith: str | Unset = UNSET,
    procedure_description_gt: str | Unset = UNSET,
    procedure_description_gte: str | Unset = UNSET,
    procedure_description_icontains: str | Unset = UNSET,
    procedure_description_iendswith: str | Unset = UNSET,
    procedure_description_iexact: str | Unset = UNSET,
    procedure_description_in: list[str] | Unset = UNSET,
    procedure_description_iregex: str | Unset = UNSET,
    procedure_description_isnull: bool | Unset = UNSET,
    procedure_description_istartswith: str | Unset = UNSET,
    procedure_description_lt: str | Unset = UNSET,
    procedure_description_lte: str | Unset = UNSET,
    procedure_description_range: list[str] | Unset = UNSET,
    procedure_description_regex: str | Unset = UNSET,
    procedure_description_startswith: str | Unset = UNSET,
    projects_ob_id: int | Unset = UNSET,
    projects_ob_id_in: list[int] | Unset = UNSET,
    projects_uuid: str | Unset = UNSET,
    projects_uuid_in: list[str] | Unset = UNSET,
    publication_state: ObservationsListPublicationState | Unset = UNSET,
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
    removed_data_reason: str | Unset = UNSET,
    removed_data_reason_contains: str | Unset = UNSET,
    removed_data_reason_endswith: str | Unset = UNSET,
    removed_data_reason_gt: str | Unset = UNSET,
    removed_data_reason_gte: str | Unset = UNSET,
    removed_data_reason_icontains: str | Unset = UNSET,
    removed_data_reason_iendswith: str | Unset = UNSET,
    removed_data_reason_iexact: str | Unset = UNSET,
    removed_data_reason_in: list[str] | Unset = UNSET,
    removed_data_reason_iregex: str | Unset = UNSET,
    removed_data_reason_isnull: bool | Unset = UNSET,
    removed_data_reason_istartswith: str | Unset = UNSET,
    removed_data_reason_lt: str | Unset = UNSET,
    removed_data_reason_lte: str | Unset = UNSET,
    removed_data_reason_range: list[str] | Unset = UNSET,
    removed_data_reason_regex: str | Unset = UNSET,
    removed_data_reason_startswith: str | Unset = UNSET,
    removed_data_time: datetime.datetime | Unset = UNSET,
    removed_data_time_contained_by: datetime.datetime | Unset = UNSET,
    removed_data_time_contains: datetime.datetime | Unset = UNSET,
    removed_data_time_date: datetime.date | Unset = UNSET,
    removed_data_time_day: float | Unset = UNSET,
    removed_data_time_endswith: datetime.datetime | Unset = UNSET,
    removed_data_time_gt: datetime.datetime | Unset = UNSET,
    removed_data_time_gte: datetime.datetime | Unset = UNSET,
    removed_data_time_hour: float | Unset = UNSET,
    removed_data_time_icontains: datetime.datetime | Unset = UNSET,
    removed_data_time_iendswith: datetime.datetime | Unset = UNSET,
    removed_data_time_iexact: datetime.datetime | Unset = UNSET,
    removed_data_time_in: list[datetime.datetime] | Unset = UNSET,
    removed_data_time_iregex: datetime.datetime | Unset = UNSET,
    removed_data_time_isnull: bool | Unset = UNSET,
    removed_data_time_iso_week_day: float | Unset = UNSET,
    removed_data_time_iso_year: float | Unset = UNSET,
    removed_data_time_istartswith: datetime.datetime | Unset = UNSET,
    removed_data_time_lt: datetime.datetime | Unset = UNSET,
    removed_data_time_lte: datetime.datetime | Unset = UNSET,
    removed_data_time_minute: float | Unset = UNSET,
    removed_data_time_month: float | Unset = UNSET,
    removed_data_time_quarter: float | Unset = UNSET,
    removed_data_time_range: list[datetime.datetime] | Unset = UNSET,
    removed_data_time_regex: datetime.datetime | Unset = UNSET,
    removed_data_time_second: float | Unset = UNSET,
    removed_data_time_startswith: datetime.datetime | Unset = UNSET,
    removed_data_time_time: str | Unset = UNSET,
    removed_data_time_week: float | Unset = UNSET,
    removed_data_time_week_day: float | Unset = UNSET,
    removed_data_time_year: float | Unset = UNSET,
    resolution: str | Unset = UNSET,
    resolution_contains: str | Unset = UNSET,
    resolution_endswith: str | Unset = UNSET,
    resolution_gt: str | Unset = UNSET,
    resolution_gte: str | Unset = UNSET,
    resolution_icontains: str | Unset = UNSET,
    resolution_iendswith: str | Unset = UNSET,
    resolution_iexact: str | Unset = UNSET,
    resolution_in: list[str] | Unset = UNSET,
    resolution_iregex: str | Unset = UNSET,
    resolution_isnull: bool | Unset = UNSET,
    resolution_istartswith: str | Unset = UNSET,
    resolution_lt: str | Unset = UNSET,
    resolution_lte: str | Unset = UNSET,
    resolution_range: list[str] | Unset = UNSET,
    resolution_regex: str | Unset = UNSET,
    resolution_startswith: str | Unset = UNSET,
    result_quality: int | Unset = UNSET,
    result_quality_date: datetime.date | Unset = UNSET,
    result_quality_date_gt: datetime.date | Unset = UNSET,
    result_quality_date_gte: datetime.date | Unset = UNSET,
    result_quality_date_lt: datetime.date | Unset = UNSET,
    result_quality_date_lte: datetime.date | Unset = UNSET,
    result_quality_date_range: list[datetime.date] | Unset = UNSET,
    result_quality_explanation: str | Unset = UNSET,
    result_quality_explanation_contains: str | Unset = UNSET,
    result_quality_gt: int | Unset = UNSET,
    result_quality_gte: int | Unset = UNSET,
    result_quality_in: list[int] | Unset = UNSET,
    result_quality_isnull: bool | Unset = UNSET,
    result_quality_lt: int | Unset = UNSET,
    result_quality_lte: int | Unset = UNSET,
    result_quality_ob_id: int | Unset = UNSET,
    result_quality_ob_id_in: list[int] | Unset = UNSET,
    result_quality_passes_test: bool | Unset = UNSET,
    result_quality_result_title: str | Unset = UNSET,
    result_quality_result_title_contains: str | Unset = UNSET,
    result_field: int | Unset = UNSET,
    result_field_data_path: str | Unset = UNSET,
    result_field_data_path_contains: str | Unset = UNSET,
    result_field_data_path_startswith: str | Unset = UNSET,
    result_field_file_format: str | Unset = UNSET,
    result_field_file_format_contains: str | Unset = UNSET,
    result_field_gt: int | Unset = UNSET,
    result_field_gte: int | Unset = UNSET,
    result_field_in: list[int] | Unset = UNSET,
    result_field_isnull: bool | Unset = UNSET,
    result_field_lt: int | Unset = UNSET,
    result_field_lte: int | Unset = UNSET,
    result_field_storage_location: ObservationsListStorageLocation | Unset = UNSET,
    result_field_storage_status: ObservationsListStorageStatus | Unset = UNSET,
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
    status: ObservationsListDataStatus | Unset = UNSET,
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
    submission_user_id: str | Unset = UNSET,
    submission_user_id_contains: str | Unset = UNSET,
    submission_user_id_endswith: str | Unset = UNSET,
    submission_user_id_gt: str | Unset = UNSET,
    submission_user_id_gte: str | Unset = UNSET,
    submission_user_id_icontains: str | Unset = UNSET,
    submission_user_id_iendswith: str | Unset = UNSET,
    submission_user_id_iexact: str | Unset = UNSET,
    submission_user_id_in: list[str] | Unset = UNSET,
    submission_user_id_iregex: str | Unset = UNSET,
    submission_user_id_isnull: bool | Unset = UNSET,
    submission_user_id_istartswith: str | Unset = UNSET,
    submission_user_id_lt: str | Unset = UNSET,
    submission_user_id_lte: str | Unset = UNSET,
    submission_user_id_range: list[str] | Unset = UNSET,
    submission_user_id_regex: str | Unset = UNSET,
    submission_user_id_startswith: str | Unset = UNSET,
    time_period: int | Unset = UNSET,
    time_period_end_time: datetime.datetime | Unset = UNSET,
    time_period_end_time_gt: datetime.datetime | Unset = UNSET,
    time_period_end_time_gte: datetime.datetime | Unset = UNSET,
    time_period_end_time_lt: datetime.datetime | Unset = UNSET,
    time_period_end_time_lte: datetime.datetime | Unset = UNSET,
    time_period_end_time_range: list[datetime.datetime] | Unset = UNSET,
    time_period_gt: int | Unset = UNSET,
    time_period_gte: int | Unset = UNSET,
    time_period_in: list[int] | Unset = UNSET,
    time_period_isnull: bool | Unset = UNSET,
    time_period_lt: int | Unset = UNSET,
    time_period_lte: int | Unset = UNSET,
    time_period_ob_id: int | Unset = UNSET,
    time_period_ob_id_in: list[int] | Unset = UNSET,
    time_period_start_time: datetime.datetime | Unset = UNSET,
    time_period_start_time_gt: datetime.datetime | Unset = UNSET,
    time_period_start_time_gte: datetime.datetime | Unset = UNSET,
    time_period_start_time_lt: datetime.datetime | Unset = UNSET,
    time_period_start_time_lte: datetime.datetime | Unset = UNSET,
    time_period_start_time_range: list[datetime.datetime] | Unset = UNSET,
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
    update_frequency: ObservationsListDataUpdateFrequency | Unset = UNSET,
    update_frequency_contains: str | Unset = UNSET,
    update_frequency_endswith: str | Unset = UNSET,
    update_frequency_gt: str | Unset = UNSET,
    update_frequency_gte: str | Unset = UNSET,
    update_frequency_icontains: str | Unset = UNSET,
    update_frequency_iendswith: str | Unset = UNSET,
    update_frequency_iexact: str | Unset = UNSET,
    update_frequency_in: list[str] | Unset = UNSET,
    update_frequency_iregex: str | Unset = UNSET,
    update_frequency_isnull: bool | Unset = UNSET,
    update_frequency_istartswith: str | Unset = UNSET,
    update_frequency_lt: str | Unset = UNSET,
    update_frequency_lte: str | Unset = UNSET,
    update_frequency_range: list[str] | Unset = UNSET,
    update_frequency_regex: str | Unset = UNSET,
    update_frequency_startswith: str | Unset = UNSET,
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
    valid_time_period: int | Unset = UNSET,
    valid_time_period_gt: int | Unset = UNSET,
    valid_time_period_gte: int | Unset = UNSET,
    valid_time_period_in: list[int] | Unset = UNSET,
    valid_time_period_isnull: bool | Unset = UNSET,
    valid_time_period_lt: int | Unset = UNSET,
    valid_time_period_lte: int | Unset = UNSET,
    vertical_extent: int | Unset = UNSET,
    vertical_extent_gt: int | Unset = UNSET,
    vertical_extent_gte: int | Unset = UNSET,
    vertical_extent_in: list[int] | Unset = UNSET,
    vertical_extent_isnull: bool | Unset = UNSET,
    vertical_extent_lt: int | Unset = UNSET,
    vertical_extent_lte: int | Unset = UNSET,
) -> Response[PaginatedObservationReadList]:
    """Get a list of Observation objects.

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
        creation_date (datetime.datetime | Unset):
        creation_date_contained_by (datetime.datetime | Unset):
        creation_date_contains (datetime.datetime | Unset):
        creation_date_date (datetime.date | Unset):
        creation_date_day (float | Unset):
        creation_date_endswith (datetime.datetime | Unset):
        creation_date_gt (datetime.datetime | Unset):
        creation_date_gte (datetime.datetime | Unset):
        creation_date_hour (float | Unset):
        creation_date_icontains (datetime.datetime | Unset):
        creation_date_iendswith (datetime.datetime | Unset):
        creation_date_iexact (datetime.datetime | Unset):
        creation_date_in (list[datetime.datetime] | Unset):
        creation_date_iregex (datetime.datetime | Unset):
        creation_date_isnull (bool | Unset):
        creation_date_iso_week_day (float | Unset):
        creation_date_iso_year (float | Unset):
        creation_date_istartswith (datetime.datetime | Unset):
        creation_date_lt (datetime.datetime | Unset):
        creation_date_lte (datetime.datetime | Unset):
        creation_date_minute (float | Unset):
        creation_date_month (float | Unset):
        creation_date_quarter (float | Unset):
        creation_date_range (list[datetime.datetime] | Unset):
        creation_date_regex (datetime.datetime | Unset):
        creation_date_second (float | Unset):
        creation_date_startswith (datetime.datetime | Unset):
        creation_date_time (str | Unset):
        creation_date_week (float | Unset):
        creation_date_week_day (float | Unset):
        creation_date_year (float | Unset):
        data_lineage (str | Unset):
        data_lineage_contains (str | Unset):
        data_lineage_endswith (str | Unset):
        data_lineage_gt (str | Unset):
        data_lineage_gte (str | Unset):
        data_lineage_icontains (str | Unset):
        data_lineage_iendswith (str | Unset):
        data_lineage_iexact (str | Unset):
        data_lineage_in (list[str] | Unset):
        data_lineage_iregex (str | Unset):
        data_lineage_isnull (bool | Unset):
        data_lineage_istartswith (str | Unset):
        data_lineage_lt (str | Unset):
        data_lineage_lte (str | Unset):
        data_lineage_range (list[str] | Unset):
        data_lineage_regex (str | Unset):
        data_lineage_startswith (str | Unset):
        data_published_time (datetime.datetime | Unset):
        data_published_time_contained_by (datetime.datetime | Unset):
        data_published_time_contains (datetime.datetime | Unset):
        data_published_time_date (datetime.date | Unset):
        data_published_time_day (float | Unset):
        data_published_time_endswith (datetime.datetime | Unset):
        data_published_time_gt (datetime.datetime | Unset):
        data_published_time_gte (datetime.datetime | Unset):
        data_published_time_hour (float | Unset):
        data_published_time_icontains (datetime.datetime | Unset):
        data_published_time_iendswith (datetime.datetime | Unset):
        data_published_time_iexact (datetime.datetime | Unset):
        data_published_time_in (list[datetime.datetime] | Unset):
        data_published_time_iregex (datetime.datetime | Unset):
        data_published_time_isnull (bool | Unset):
        data_published_time_iso_week_day (float | Unset):
        data_published_time_iso_year (float | Unset):
        data_published_time_istartswith (datetime.datetime | Unset):
        data_published_time_lt (datetime.datetime | Unset):
        data_published_time_lte (datetime.datetime | Unset):
        data_published_time_minute (float | Unset):
        data_published_time_month (float | Unset):
        data_published_time_quarter (float | Unset):
        data_published_time_range (list[datetime.datetime] | Unset):
        data_published_time_regex (datetime.datetime | Unset):
        data_published_time_second (float | Unset):
        data_published_time_startswith (datetime.datetime | Unset):
        data_published_time_time (str | Unset):
        data_published_time_week (float | Unset):
        data_published_time_week_day (float | Unset):
        data_published_time_year (float | Unset):
        discovery_keywords_name (str | Unset):
        discovery_keywords_name_contains (str | Unset):
        doi_published_time (datetime.datetime | Unset):
        doi_published_time_contained_by (datetime.datetime | Unset):
        doi_published_time_contains (datetime.datetime | Unset):
        doi_published_time_date (datetime.date | Unset):
        doi_published_time_day (float | Unset):
        doi_published_time_endswith (datetime.datetime | Unset):
        doi_published_time_gt (datetime.datetime | Unset):
        doi_published_time_gte (datetime.datetime | Unset):
        doi_published_time_hour (float | Unset):
        doi_published_time_icontains (datetime.datetime | Unset):
        doi_published_time_iendswith (datetime.datetime | Unset):
        doi_published_time_iexact (datetime.datetime | Unset):
        doi_published_time_in (list[datetime.datetime] | Unset):
        doi_published_time_iregex (datetime.datetime | Unset):
        doi_published_time_isnull (bool | Unset):
        doi_published_time_iso_week_day (float | Unset):
        doi_published_time_iso_year (float | Unset):
        doi_published_time_istartswith (datetime.datetime | Unset):
        doi_published_time_lt (datetime.datetime | Unset):
        doi_published_time_lte (datetime.datetime | Unset):
        doi_published_time_minute (float | Unset):
        doi_published_time_month (float | Unset):
        doi_published_time_quarter (float | Unset):
        doi_published_time_range (list[datetime.datetime] | Unset):
        doi_published_time_regex (datetime.datetime | Unset):
        doi_published_time_second (float | Unset):
        doi_published_time_startswith (datetime.datetime | Unset):
        doi_published_time_time (str | Unset):
        doi_published_time_week (float | Unset):
        doi_published_time_week_day (float | Unset):
        doi_published_time_year (float | Unset):
        dont_harvest_from_projects (bool | Unset):
        dont_harvest_from_projects_contains (bool | Unset):
        dont_harvest_from_projects_endswith (bool | Unset):
        dont_harvest_from_projects_gt (bool | Unset):
        dont_harvest_from_projects_gte (bool | Unset):
        dont_harvest_from_projects_icontains (bool | Unset):
        dont_harvest_from_projects_iendswith (bool | Unset):
        dont_harvest_from_projects_iexact (bool | Unset):
        dont_harvest_from_projects_in (list[bool] | Unset):
        dont_harvest_from_projects_iregex (bool | Unset):
        dont_harvest_from_projects_isnull (bool | Unset):
        dont_harvest_from_projects_istartswith (bool | Unset):
        dont_harvest_from_projects_lt (bool | Unset):
        dont_harvest_from_projects_lte (bool | Unset):
        dont_harvest_from_projects_range (list[bool] | Unset):
        dont_harvest_from_projects_regex (bool | Unset):
        dont_harvest_from_projects_startswith (bool | Unset):
        feature_of_interest (str | Unset):
        feature_of_interest_contains (str | Unset):
        feature_of_interest_endswith (str | Unset):
        feature_of_interest_gt (str | Unset):
        feature_of_interest_gte (str | Unset):
        feature_of_interest_icontains (str | Unset):
        feature_of_interest_iendswith (str | Unset):
        feature_of_interest_iexact (str | Unset):
        feature_of_interest_in (list[str] | Unset):
        feature_of_interest_iregex (str | Unset):
        feature_of_interest_isnull (bool | Unset):
        feature_of_interest_istartswith (str | Unset):
        feature_of_interest_lt (str | Unset):
        feature_of_interest_lte (str | Unset):
        feature_of_interest_range (list[str] | Unset):
        feature_of_interest_regex (str | Unset):
        feature_of_interest_startswith (str | Unset):
        geographic_extent (int | Unset):
        geographic_extent_east_bound_longitude (float | Unset):
        geographic_extent_east_bound_longitude_gt (float | Unset):
        geographic_extent_east_bound_longitude_gte (float | Unset):
        geographic_extent_east_bound_longitude_lt (float | Unset):
        geographic_extent_east_bound_longitude_lte (float | Unset):
        geographic_extent_east_bound_longitude_range (list[float] | Unset):
        geographic_extent_gt (int | Unset):
        geographic_extent_gte (int | Unset):
        geographic_extent_in (list[int] | Unset):
        geographic_extent_isnull (bool | Unset):
        geographic_extent_lt (int | Unset):
        geographic_extent_lte (int | Unset):
        geographic_extent_north_bound_latitude (float | Unset):
        geographic_extent_north_bound_latitude_gt (float | Unset):
        geographic_extent_north_bound_latitude_gte (float | Unset):
        geographic_extent_north_bound_latitude_lt (float | Unset):
        geographic_extent_north_bound_latitude_lte (float | Unset):
        geographic_extent_north_bound_latitude_range (list[float] | Unset):
        geographic_extent_ob_id (int | Unset):
        geographic_extent_ob_id_in (list[int] | Unset):
        geographic_extent_south_bound_latitude (float | Unset):
        geographic_extent_south_bound_latitude_gt (float | Unset):
        geographic_extent_south_bound_latitude_gte (float | Unset):
        geographic_extent_south_bound_latitude_lt (float | Unset):
        geographic_extent_south_bound_latitude_lte (float | Unset):
        geographic_extent_south_bound_latitude_range (list[float] | Unset):
        geographic_extent_west_bound_longitude (float | Unset):
        geographic_extent_west_bound_longitude_gt (float | Unset):
        geographic_extent_west_bound_longitude_gte (float | Unset):
        geographic_extent_west_bound_longitude_lt (float | Unset):
        geographic_extent_west_bound_longitude_lte (float | Unset):
        geographic_extent_west_bound_longitude_range (list[float] | Unset):
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
        language (ObservationsListLanguage | Unset):
        language_contains (str | Unset):
        language_endswith (str | Unset):
        language_gt (str | Unset):
        language_gte (str | Unset):
        language_icontains (str | Unset):
        language_iendswith (str | Unset):
        language_iexact (str | Unset):
        language_in (list[str] | Unset):
        language_iregex (str | Unset):
        language_isnull (bool | Unset):
        language_istartswith (str | Unset):
        language_lt (str | Unset):
        language_lte (str | Unset):
        language_range (list[str] | Unset):
        language_regex (str | Unset):
        language_startswith (str | Unset):
        last_updated_date (datetime.datetime | Unset):
        last_updated_date_contained_by (datetime.datetime | Unset):
        last_updated_date_contains (datetime.datetime | Unset):
        last_updated_date_date (datetime.date | Unset):
        last_updated_date_day (float | Unset):
        last_updated_date_endswith (datetime.datetime | Unset):
        last_updated_date_gt (datetime.datetime | Unset):
        last_updated_date_gte (datetime.datetime | Unset):
        last_updated_date_hour (float | Unset):
        last_updated_date_icontains (datetime.datetime | Unset):
        last_updated_date_iendswith (datetime.datetime | Unset):
        last_updated_date_iexact (datetime.datetime | Unset):
        last_updated_date_in (list[datetime.datetime] | Unset):
        last_updated_date_iregex (datetime.datetime | Unset):
        last_updated_date_isnull (bool | Unset):
        last_updated_date_iso_week_day (float | Unset):
        last_updated_date_iso_year (float | Unset):
        last_updated_date_istartswith (datetime.datetime | Unset):
        last_updated_date_lt (datetime.datetime | Unset):
        last_updated_date_lte (datetime.datetime | Unset):
        last_updated_date_minute (float | Unset):
        last_updated_date_month (float | Unset):
        last_updated_date_quarter (float | Unset):
        last_updated_date_range (list[datetime.datetime] | Unset):
        last_updated_date_regex (datetime.datetime | Unset):
        last_updated_date_second (float | Unset):
        last_updated_date_startswith (datetime.datetime | Unset):
        last_updated_date_time (str | Unset):
        last_updated_date_week (float | Unset):
        last_updated_date_week_day (float | Unset):
        last_updated_date_year (float | Unset):
        latest_data_update_time (datetime.datetime | Unset):
        latest_data_update_time_contained_by (datetime.datetime | Unset):
        latest_data_update_time_contains (datetime.datetime | Unset):
        latest_data_update_time_date (datetime.date | Unset):
        latest_data_update_time_day (float | Unset):
        latest_data_update_time_endswith (datetime.datetime | Unset):
        latest_data_update_time_gt (datetime.datetime | Unset):
        latest_data_update_time_gte (datetime.datetime | Unset):
        latest_data_update_time_hour (float | Unset):
        latest_data_update_time_icontains (datetime.datetime | Unset):
        latest_data_update_time_iendswith (datetime.datetime | Unset):
        latest_data_update_time_iexact (datetime.datetime | Unset):
        latest_data_update_time_in (list[datetime.datetime] | Unset):
        latest_data_update_time_iregex (datetime.datetime | Unset):
        latest_data_update_time_isnull (bool | Unset):
        latest_data_update_time_iso_week_day (float | Unset):
        latest_data_update_time_iso_year (float | Unset):
        latest_data_update_time_istartswith (datetime.datetime | Unset):
        latest_data_update_time_lt (datetime.datetime | Unset):
        latest_data_update_time_lte (datetime.datetime | Unset):
        latest_data_update_time_minute (float | Unset):
        latest_data_update_time_month (float | Unset):
        latest_data_update_time_quarter (float | Unset):
        latest_data_update_time_range (list[datetime.datetime] | Unset):
        latest_data_update_time_regex (datetime.datetime | Unset):
        latest_data_update_time_second (float | Unset):
        latest_data_update_time_startswith (datetime.datetime | Unset):
        latest_data_update_time_time (str | Unset):
        latest_data_update_time_week (float | Unset):
        latest_data_update_time_week_day (float | Unset):
        latest_data_update_time_year (float | Unset):
        limit (int | Unset):
        non_geographic_flag (bool | Unset):
        non_geographic_flag_contains (bool | Unset):
        non_geographic_flag_endswith (bool | Unset):
        non_geographic_flag_gt (bool | Unset):
        non_geographic_flag_gte (bool | Unset):
        non_geographic_flag_icontains (bool | Unset):
        non_geographic_flag_iendswith (bool | Unset):
        non_geographic_flag_iexact (bool | Unset):
        non_geographic_flag_in (list[bool] | Unset):
        non_geographic_flag_iregex (bool | Unset):
        non_geographic_flag_isnull (bool | Unset):
        non_geographic_flag_istartswith (bool | Unset):
        non_geographic_flag_lt (bool | Unset):
        non_geographic_flag_lte (bool | Unset):
        non_geographic_flag_range (list[bool] | Unset):
        non_geographic_flag_regex (bool | Unset):
        non_geographic_flag_startswith (bool | Unset):
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
        permissions_access_category (ObservationsListAccessCategory | Unset):
        permissions_access_category_in (list[str] | Unset):
        permissions_access_roles (str | Unset):
        permissions_access_roles_in (list[str] | Unset):
        procedure_acquisition (int | Unset):
        procedure_acquisition_gt (int | Unset):
        procedure_acquisition_gte (int | Unset):
        procedure_acquisition_in (list[int] | Unset):
        procedure_acquisition_isnull (bool | Unset):
        procedure_acquisition_lt (int | Unset):
        procedure_acquisition_lte (int | Unset):
        procedure_acquisition_ob_id (int | Unset):
        procedure_acquisition_ob_id_in (list[int] | Unset):
        procedure_acquisition_uuid (str | Unset):
        procedure_acquisition_uuid_in (list[str] | Unset):
        procedure_composite_process (int | Unset):
        procedure_composite_process_gt (int | Unset):
        procedure_composite_process_gte (int | Unset):
        procedure_composite_process_in (list[int] | Unset):
        procedure_composite_process_isnull (bool | Unset):
        procedure_composite_process_lt (int | Unset):
        procedure_composite_process_lte (int | Unset):
        procedure_computation (int | Unset):
        procedure_computation_gt (int | Unset):
        procedure_computation_gte (int | Unset):
        procedure_computation_in (list[int] | Unset):
        procedure_computation_isnull (bool | Unset):
        procedure_computation_lt (int | Unset):
        procedure_computation_lte (int | Unset):
        procedure_description (str | Unset):
        procedure_description_contains (str | Unset):
        procedure_description_endswith (str | Unset):
        procedure_description_gt (str | Unset):
        procedure_description_gte (str | Unset):
        procedure_description_icontains (str | Unset):
        procedure_description_iendswith (str | Unset):
        procedure_description_iexact (str | Unset):
        procedure_description_in (list[str] | Unset):
        procedure_description_iregex (str | Unset):
        procedure_description_isnull (bool | Unset):
        procedure_description_istartswith (str | Unset):
        procedure_description_lt (str | Unset):
        procedure_description_lte (str | Unset):
        procedure_description_range (list[str] | Unset):
        procedure_description_regex (str | Unset):
        procedure_description_startswith (str | Unset):
        projects_ob_id (int | Unset):
        projects_ob_id_in (list[int] | Unset):
        projects_uuid (str | Unset):
        projects_uuid_in (list[str] | Unset):
        publication_state (ObservationsListPublicationState | Unset):
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
        removed_data_reason (str | Unset):
        removed_data_reason_contains (str | Unset):
        removed_data_reason_endswith (str | Unset):
        removed_data_reason_gt (str | Unset):
        removed_data_reason_gte (str | Unset):
        removed_data_reason_icontains (str | Unset):
        removed_data_reason_iendswith (str | Unset):
        removed_data_reason_iexact (str | Unset):
        removed_data_reason_in (list[str] | Unset):
        removed_data_reason_iregex (str | Unset):
        removed_data_reason_isnull (bool | Unset):
        removed_data_reason_istartswith (str | Unset):
        removed_data_reason_lt (str | Unset):
        removed_data_reason_lte (str | Unset):
        removed_data_reason_range (list[str] | Unset):
        removed_data_reason_regex (str | Unset):
        removed_data_reason_startswith (str | Unset):
        removed_data_time (datetime.datetime | Unset):
        removed_data_time_contained_by (datetime.datetime | Unset):
        removed_data_time_contains (datetime.datetime | Unset):
        removed_data_time_date (datetime.date | Unset):
        removed_data_time_day (float | Unset):
        removed_data_time_endswith (datetime.datetime | Unset):
        removed_data_time_gt (datetime.datetime | Unset):
        removed_data_time_gte (datetime.datetime | Unset):
        removed_data_time_hour (float | Unset):
        removed_data_time_icontains (datetime.datetime | Unset):
        removed_data_time_iendswith (datetime.datetime | Unset):
        removed_data_time_iexact (datetime.datetime | Unset):
        removed_data_time_in (list[datetime.datetime] | Unset):
        removed_data_time_iregex (datetime.datetime | Unset):
        removed_data_time_isnull (bool | Unset):
        removed_data_time_iso_week_day (float | Unset):
        removed_data_time_iso_year (float | Unset):
        removed_data_time_istartswith (datetime.datetime | Unset):
        removed_data_time_lt (datetime.datetime | Unset):
        removed_data_time_lte (datetime.datetime | Unset):
        removed_data_time_minute (float | Unset):
        removed_data_time_month (float | Unset):
        removed_data_time_quarter (float | Unset):
        removed_data_time_range (list[datetime.datetime] | Unset):
        removed_data_time_regex (datetime.datetime | Unset):
        removed_data_time_second (float | Unset):
        removed_data_time_startswith (datetime.datetime | Unset):
        removed_data_time_time (str | Unset):
        removed_data_time_week (float | Unset):
        removed_data_time_week_day (float | Unset):
        removed_data_time_year (float | Unset):
        resolution (str | Unset):
        resolution_contains (str | Unset):
        resolution_endswith (str | Unset):
        resolution_gt (str | Unset):
        resolution_gte (str | Unset):
        resolution_icontains (str | Unset):
        resolution_iendswith (str | Unset):
        resolution_iexact (str | Unset):
        resolution_in (list[str] | Unset):
        resolution_iregex (str | Unset):
        resolution_isnull (bool | Unset):
        resolution_istartswith (str | Unset):
        resolution_lt (str | Unset):
        resolution_lte (str | Unset):
        resolution_range (list[str] | Unset):
        resolution_regex (str | Unset):
        resolution_startswith (str | Unset):
        result_quality (int | Unset):
        result_quality_date (datetime.date | Unset):
        result_quality_date_gt (datetime.date | Unset):
        result_quality_date_gte (datetime.date | Unset):
        result_quality_date_lt (datetime.date | Unset):
        result_quality_date_lte (datetime.date | Unset):
        result_quality_date_range (list[datetime.date] | Unset):
        result_quality_explanation (str | Unset):
        result_quality_explanation_contains (str | Unset):
        result_quality_gt (int | Unset):
        result_quality_gte (int | Unset):
        result_quality_in (list[int] | Unset):
        result_quality_isnull (bool | Unset):
        result_quality_lt (int | Unset):
        result_quality_lte (int | Unset):
        result_quality_ob_id (int | Unset):
        result_quality_ob_id_in (list[int] | Unset):
        result_quality_passes_test (bool | Unset):
        result_quality_result_title (str | Unset):
        result_quality_result_title_contains (str | Unset):
        result_field (int | Unset):
        result_field_data_path (str | Unset):
        result_field_data_path_contains (str | Unset):
        result_field_data_path_startswith (str | Unset):
        result_field_file_format (str | Unset):
        result_field_file_format_contains (str | Unset):
        result_field_gt (int | Unset):
        result_field_gte (int | Unset):
        result_field_in (list[int] | Unset):
        result_field_isnull (bool | Unset):
        result_field_lt (int | Unset):
        result_field_lte (int | Unset):
        result_field_storage_location (ObservationsListStorageLocation | Unset):
        result_field_storage_status (ObservationsListStorageStatus | Unset):
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
        status (ObservationsListDataStatus | Unset):
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
        submission_user_id (str | Unset):
        submission_user_id_contains (str | Unset):
        submission_user_id_endswith (str | Unset):
        submission_user_id_gt (str | Unset):
        submission_user_id_gte (str | Unset):
        submission_user_id_icontains (str | Unset):
        submission_user_id_iendswith (str | Unset):
        submission_user_id_iexact (str | Unset):
        submission_user_id_in (list[str] | Unset):
        submission_user_id_iregex (str | Unset):
        submission_user_id_isnull (bool | Unset):
        submission_user_id_istartswith (str | Unset):
        submission_user_id_lt (str | Unset):
        submission_user_id_lte (str | Unset):
        submission_user_id_range (list[str] | Unset):
        submission_user_id_regex (str | Unset):
        submission_user_id_startswith (str | Unset):
        time_period (int | Unset):
        time_period_end_time (datetime.datetime | Unset):
        time_period_end_time_gt (datetime.datetime | Unset):
        time_period_end_time_gte (datetime.datetime | Unset):
        time_period_end_time_lt (datetime.datetime | Unset):
        time_period_end_time_lte (datetime.datetime | Unset):
        time_period_end_time_range (list[datetime.datetime] | Unset):
        time_period_gt (int | Unset):
        time_period_gte (int | Unset):
        time_period_in (list[int] | Unset):
        time_period_isnull (bool | Unset):
        time_period_lt (int | Unset):
        time_period_lte (int | Unset):
        time_period_ob_id (int | Unset):
        time_period_ob_id_in (list[int] | Unset):
        time_period_start_time (datetime.datetime | Unset):
        time_period_start_time_gt (datetime.datetime | Unset):
        time_period_start_time_gte (datetime.datetime | Unset):
        time_period_start_time_lt (datetime.datetime | Unset):
        time_period_start_time_lte (datetime.datetime | Unset):
        time_period_start_time_range (list[datetime.datetime] | Unset):
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
        update_frequency (ObservationsListDataUpdateFrequency | Unset):
        update_frequency_contains (str | Unset):
        update_frequency_endswith (str | Unset):
        update_frequency_gt (str | Unset):
        update_frequency_gte (str | Unset):
        update_frequency_icontains (str | Unset):
        update_frequency_iendswith (str | Unset):
        update_frequency_iexact (str | Unset):
        update_frequency_in (list[str] | Unset):
        update_frequency_iregex (str | Unset):
        update_frequency_isnull (bool | Unset):
        update_frequency_istartswith (str | Unset):
        update_frequency_lt (str | Unset):
        update_frequency_lte (str | Unset):
        update_frequency_range (list[str] | Unset):
        update_frequency_regex (str | Unset):
        update_frequency_startswith (str | Unset):
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
        valid_time_period (int | Unset):
        valid_time_period_gt (int | Unset):
        valid_time_period_gte (int | Unset):
        valid_time_period_in (list[int] | Unset):
        valid_time_period_isnull (bool | Unset):
        valid_time_period_lt (int | Unset):
        valid_time_period_lte (int | Unset):
        vertical_extent (int | Unset):
        vertical_extent_gt (int | Unset):
        vertical_extent_gte (int | Unset):
        vertical_extent_in (list[int] | Unset):
        vertical_extent_isnull (bool | Unset):
        vertical_extent_lt (int | Unset):
        vertical_extent_lte (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedObservationReadList]
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
        creation_date=creation_date,
        creation_date_contained_by=creation_date_contained_by,
        creation_date_contains=creation_date_contains,
        creation_date_date=creation_date_date,
        creation_date_day=creation_date_day,
        creation_date_endswith=creation_date_endswith,
        creation_date_gt=creation_date_gt,
        creation_date_gte=creation_date_gte,
        creation_date_hour=creation_date_hour,
        creation_date_icontains=creation_date_icontains,
        creation_date_iendswith=creation_date_iendswith,
        creation_date_iexact=creation_date_iexact,
        creation_date_in=creation_date_in,
        creation_date_iregex=creation_date_iregex,
        creation_date_isnull=creation_date_isnull,
        creation_date_iso_week_day=creation_date_iso_week_day,
        creation_date_iso_year=creation_date_iso_year,
        creation_date_istartswith=creation_date_istartswith,
        creation_date_lt=creation_date_lt,
        creation_date_lte=creation_date_lte,
        creation_date_minute=creation_date_minute,
        creation_date_month=creation_date_month,
        creation_date_quarter=creation_date_quarter,
        creation_date_range=creation_date_range,
        creation_date_regex=creation_date_regex,
        creation_date_second=creation_date_second,
        creation_date_startswith=creation_date_startswith,
        creation_date_time=creation_date_time,
        creation_date_week=creation_date_week,
        creation_date_week_day=creation_date_week_day,
        creation_date_year=creation_date_year,
        data_lineage=data_lineage,
        data_lineage_contains=data_lineage_contains,
        data_lineage_endswith=data_lineage_endswith,
        data_lineage_gt=data_lineage_gt,
        data_lineage_gte=data_lineage_gte,
        data_lineage_icontains=data_lineage_icontains,
        data_lineage_iendswith=data_lineage_iendswith,
        data_lineage_iexact=data_lineage_iexact,
        data_lineage_in=data_lineage_in,
        data_lineage_iregex=data_lineage_iregex,
        data_lineage_isnull=data_lineage_isnull,
        data_lineage_istartswith=data_lineage_istartswith,
        data_lineage_lt=data_lineage_lt,
        data_lineage_lte=data_lineage_lte,
        data_lineage_range=data_lineage_range,
        data_lineage_regex=data_lineage_regex,
        data_lineage_startswith=data_lineage_startswith,
        data_published_time=data_published_time,
        data_published_time_contained_by=data_published_time_contained_by,
        data_published_time_contains=data_published_time_contains,
        data_published_time_date=data_published_time_date,
        data_published_time_day=data_published_time_day,
        data_published_time_endswith=data_published_time_endswith,
        data_published_time_gt=data_published_time_gt,
        data_published_time_gte=data_published_time_gte,
        data_published_time_hour=data_published_time_hour,
        data_published_time_icontains=data_published_time_icontains,
        data_published_time_iendswith=data_published_time_iendswith,
        data_published_time_iexact=data_published_time_iexact,
        data_published_time_in=data_published_time_in,
        data_published_time_iregex=data_published_time_iregex,
        data_published_time_isnull=data_published_time_isnull,
        data_published_time_iso_week_day=data_published_time_iso_week_day,
        data_published_time_iso_year=data_published_time_iso_year,
        data_published_time_istartswith=data_published_time_istartswith,
        data_published_time_lt=data_published_time_lt,
        data_published_time_lte=data_published_time_lte,
        data_published_time_minute=data_published_time_minute,
        data_published_time_month=data_published_time_month,
        data_published_time_quarter=data_published_time_quarter,
        data_published_time_range=data_published_time_range,
        data_published_time_regex=data_published_time_regex,
        data_published_time_second=data_published_time_second,
        data_published_time_startswith=data_published_time_startswith,
        data_published_time_time=data_published_time_time,
        data_published_time_week=data_published_time_week,
        data_published_time_week_day=data_published_time_week_day,
        data_published_time_year=data_published_time_year,
        discovery_keywords_name=discovery_keywords_name,
        discovery_keywords_name_contains=discovery_keywords_name_contains,
        doi_published_time=doi_published_time,
        doi_published_time_contained_by=doi_published_time_contained_by,
        doi_published_time_contains=doi_published_time_contains,
        doi_published_time_date=doi_published_time_date,
        doi_published_time_day=doi_published_time_day,
        doi_published_time_endswith=doi_published_time_endswith,
        doi_published_time_gt=doi_published_time_gt,
        doi_published_time_gte=doi_published_time_gte,
        doi_published_time_hour=doi_published_time_hour,
        doi_published_time_icontains=doi_published_time_icontains,
        doi_published_time_iendswith=doi_published_time_iendswith,
        doi_published_time_iexact=doi_published_time_iexact,
        doi_published_time_in=doi_published_time_in,
        doi_published_time_iregex=doi_published_time_iregex,
        doi_published_time_isnull=doi_published_time_isnull,
        doi_published_time_iso_week_day=doi_published_time_iso_week_day,
        doi_published_time_iso_year=doi_published_time_iso_year,
        doi_published_time_istartswith=doi_published_time_istartswith,
        doi_published_time_lt=doi_published_time_lt,
        doi_published_time_lte=doi_published_time_lte,
        doi_published_time_minute=doi_published_time_minute,
        doi_published_time_month=doi_published_time_month,
        doi_published_time_quarter=doi_published_time_quarter,
        doi_published_time_range=doi_published_time_range,
        doi_published_time_regex=doi_published_time_regex,
        doi_published_time_second=doi_published_time_second,
        doi_published_time_startswith=doi_published_time_startswith,
        doi_published_time_time=doi_published_time_time,
        doi_published_time_week=doi_published_time_week,
        doi_published_time_week_day=doi_published_time_week_day,
        doi_published_time_year=doi_published_time_year,
        dont_harvest_from_projects=dont_harvest_from_projects,
        dont_harvest_from_projects_contains=dont_harvest_from_projects_contains,
        dont_harvest_from_projects_endswith=dont_harvest_from_projects_endswith,
        dont_harvest_from_projects_gt=dont_harvest_from_projects_gt,
        dont_harvest_from_projects_gte=dont_harvest_from_projects_gte,
        dont_harvest_from_projects_icontains=dont_harvest_from_projects_icontains,
        dont_harvest_from_projects_iendswith=dont_harvest_from_projects_iendswith,
        dont_harvest_from_projects_iexact=dont_harvest_from_projects_iexact,
        dont_harvest_from_projects_in=dont_harvest_from_projects_in,
        dont_harvest_from_projects_iregex=dont_harvest_from_projects_iregex,
        dont_harvest_from_projects_isnull=dont_harvest_from_projects_isnull,
        dont_harvest_from_projects_istartswith=dont_harvest_from_projects_istartswith,
        dont_harvest_from_projects_lt=dont_harvest_from_projects_lt,
        dont_harvest_from_projects_lte=dont_harvest_from_projects_lte,
        dont_harvest_from_projects_range=dont_harvest_from_projects_range,
        dont_harvest_from_projects_regex=dont_harvest_from_projects_regex,
        dont_harvest_from_projects_startswith=dont_harvest_from_projects_startswith,
        feature_of_interest=feature_of_interest,
        feature_of_interest_contains=feature_of_interest_contains,
        feature_of_interest_endswith=feature_of_interest_endswith,
        feature_of_interest_gt=feature_of_interest_gt,
        feature_of_interest_gte=feature_of_interest_gte,
        feature_of_interest_icontains=feature_of_interest_icontains,
        feature_of_interest_iendswith=feature_of_interest_iendswith,
        feature_of_interest_iexact=feature_of_interest_iexact,
        feature_of_interest_in=feature_of_interest_in,
        feature_of_interest_iregex=feature_of_interest_iregex,
        feature_of_interest_isnull=feature_of_interest_isnull,
        feature_of_interest_istartswith=feature_of_interest_istartswith,
        feature_of_interest_lt=feature_of_interest_lt,
        feature_of_interest_lte=feature_of_interest_lte,
        feature_of_interest_range=feature_of_interest_range,
        feature_of_interest_regex=feature_of_interest_regex,
        feature_of_interest_startswith=feature_of_interest_startswith,
        geographic_extent=geographic_extent,
        geographic_extent_east_bound_longitude=geographic_extent_east_bound_longitude,
        geographic_extent_east_bound_longitude_gt=geographic_extent_east_bound_longitude_gt,
        geographic_extent_east_bound_longitude_gte=geographic_extent_east_bound_longitude_gte,
        geographic_extent_east_bound_longitude_lt=geographic_extent_east_bound_longitude_lt,
        geographic_extent_east_bound_longitude_lte=geographic_extent_east_bound_longitude_lte,
        geographic_extent_east_bound_longitude_range=geographic_extent_east_bound_longitude_range,
        geographic_extent_gt=geographic_extent_gt,
        geographic_extent_gte=geographic_extent_gte,
        geographic_extent_in=geographic_extent_in,
        geographic_extent_isnull=geographic_extent_isnull,
        geographic_extent_lt=geographic_extent_lt,
        geographic_extent_lte=geographic_extent_lte,
        geographic_extent_north_bound_latitude=geographic_extent_north_bound_latitude,
        geographic_extent_north_bound_latitude_gt=geographic_extent_north_bound_latitude_gt,
        geographic_extent_north_bound_latitude_gte=geographic_extent_north_bound_latitude_gte,
        geographic_extent_north_bound_latitude_lt=geographic_extent_north_bound_latitude_lt,
        geographic_extent_north_bound_latitude_lte=geographic_extent_north_bound_latitude_lte,
        geographic_extent_north_bound_latitude_range=geographic_extent_north_bound_latitude_range,
        geographic_extent_ob_id=geographic_extent_ob_id,
        geographic_extent_ob_id_in=geographic_extent_ob_id_in,
        geographic_extent_south_bound_latitude=geographic_extent_south_bound_latitude,
        geographic_extent_south_bound_latitude_gt=geographic_extent_south_bound_latitude_gt,
        geographic_extent_south_bound_latitude_gte=geographic_extent_south_bound_latitude_gte,
        geographic_extent_south_bound_latitude_lt=geographic_extent_south_bound_latitude_lt,
        geographic_extent_south_bound_latitude_lte=geographic_extent_south_bound_latitude_lte,
        geographic_extent_south_bound_latitude_range=geographic_extent_south_bound_latitude_range,
        geographic_extent_west_bound_longitude=geographic_extent_west_bound_longitude,
        geographic_extent_west_bound_longitude_gt=geographic_extent_west_bound_longitude_gt,
        geographic_extent_west_bound_longitude_gte=geographic_extent_west_bound_longitude_gte,
        geographic_extent_west_bound_longitude_lt=geographic_extent_west_bound_longitude_lt,
        geographic_extent_west_bound_longitude_lte=geographic_extent_west_bound_longitude_lte,
        geographic_extent_west_bound_longitude_range=geographic_extent_west_bound_longitude_range,
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
        language=language,
        language_contains=language_contains,
        language_endswith=language_endswith,
        language_gt=language_gt,
        language_gte=language_gte,
        language_icontains=language_icontains,
        language_iendswith=language_iendswith,
        language_iexact=language_iexact,
        language_in=language_in,
        language_iregex=language_iregex,
        language_isnull=language_isnull,
        language_istartswith=language_istartswith,
        language_lt=language_lt,
        language_lte=language_lte,
        language_range=language_range,
        language_regex=language_regex,
        language_startswith=language_startswith,
        last_updated_date=last_updated_date,
        last_updated_date_contained_by=last_updated_date_contained_by,
        last_updated_date_contains=last_updated_date_contains,
        last_updated_date_date=last_updated_date_date,
        last_updated_date_day=last_updated_date_day,
        last_updated_date_endswith=last_updated_date_endswith,
        last_updated_date_gt=last_updated_date_gt,
        last_updated_date_gte=last_updated_date_gte,
        last_updated_date_hour=last_updated_date_hour,
        last_updated_date_icontains=last_updated_date_icontains,
        last_updated_date_iendswith=last_updated_date_iendswith,
        last_updated_date_iexact=last_updated_date_iexact,
        last_updated_date_in=last_updated_date_in,
        last_updated_date_iregex=last_updated_date_iregex,
        last_updated_date_isnull=last_updated_date_isnull,
        last_updated_date_iso_week_day=last_updated_date_iso_week_day,
        last_updated_date_iso_year=last_updated_date_iso_year,
        last_updated_date_istartswith=last_updated_date_istartswith,
        last_updated_date_lt=last_updated_date_lt,
        last_updated_date_lte=last_updated_date_lte,
        last_updated_date_minute=last_updated_date_minute,
        last_updated_date_month=last_updated_date_month,
        last_updated_date_quarter=last_updated_date_quarter,
        last_updated_date_range=last_updated_date_range,
        last_updated_date_regex=last_updated_date_regex,
        last_updated_date_second=last_updated_date_second,
        last_updated_date_startswith=last_updated_date_startswith,
        last_updated_date_time=last_updated_date_time,
        last_updated_date_week=last_updated_date_week,
        last_updated_date_week_day=last_updated_date_week_day,
        last_updated_date_year=last_updated_date_year,
        latest_data_update_time=latest_data_update_time,
        latest_data_update_time_contained_by=latest_data_update_time_contained_by,
        latest_data_update_time_contains=latest_data_update_time_contains,
        latest_data_update_time_date=latest_data_update_time_date,
        latest_data_update_time_day=latest_data_update_time_day,
        latest_data_update_time_endswith=latest_data_update_time_endswith,
        latest_data_update_time_gt=latest_data_update_time_gt,
        latest_data_update_time_gte=latest_data_update_time_gte,
        latest_data_update_time_hour=latest_data_update_time_hour,
        latest_data_update_time_icontains=latest_data_update_time_icontains,
        latest_data_update_time_iendswith=latest_data_update_time_iendswith,
        latest_data_update_time_iexact=latest_data_update_time_iexact,
        latest_data_update_time_in=latest_data_update_time_in,
        latest_data_update_time_iregex=latest_data_update_time_iregex,
        latest_data_update_time_isnull=latest_data_update_time_isnull,
        latest_data_update_time_iso_week_day=latest_data_update_time_iso_week_day,
        latest_data_update_time_iso_year=latest_data_update_time_iso_year,
        latest_data_update_time_istartswith=latest_data_update_time_istartswith,
        latest_data_update_time_lt=latest_data_update_time_lt,
        latest_data_update_time_lte=latest_data_update_time_lte,
        latest_data_update_time_minute=latest_data_update_time_minute,
        latest_data_update_time_month=latest_data_update_time_month,
        latest_data_update_time_quarter=latest_data_update_time_quarter,
        latest_data_update_time_range=latest_data_update_time_range,
        latest_data_update_time_regex=latest_data_update_time_regex,
        latest_data_update_time_second=latest_data_update_time_second,
        latest_data_update_time_startswith=latest_data_update_time_startswith,
        latest_data_update_time_time=latest_data_update_time_time,
        latest_data_update_time_week=latest_data_update_time_week,
        latest_data_update_time_week_day=latest_data_update_time_week_day,
        latest_data_update_time_year=latest_data_update_time_year,
        limit=limit,
        non_geographic_flag=non_geographic_flag,
        non_geographic_flag_contains=non_geographic_flag_contains,
        non_geographic_flag_endswith=non_geographic_flag_endswith,
        non_geographic_flag_gt=non_geographic_flag_gt,
        non_geographic_flag_gte=non_geographic_flag_gte,
        non_geographic_flag_icontains=non_geographic_flag_icontains,
        non_geographic_flag_iendswith=non_geographic_flag_iendswith,
        non_geographic_flag_iexact=non_geographic_flag_iexact,
        non_geographic_flag_in=non_geographic_flag_in,
        non_geographic_flag_iregex=non_geographic_flag_iregex,
        non_geographic_flag_isnull=non_geographic_flag_isnull,
        non_geographic_flag_istartswith=non_geographic_flag_istartswith,
        non_geographic_flag_lt=non_geographic_flag_lt,
        non_geographic_flag_lte=non_geographic_flag_lte,
        non_geographic_flag_range=non_geographic_flag_range,
        non_geographic_flag_regex=non_geographic_flag_regex,
        non_geographic_flag_startswith=non_geographic_flag_startswith,
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
        permissions_access_category=permissions_access_category,
        permissions_access_category_in=permissions_access_category_in,
        permissions_access_roles=permissions_access_roles,
        permissions_access_roles_in=permissions_access_roles_in,
        procedure_acquisition=procedure_acquisition,
        procedure_acquisition_gt=procedure_acquisition_gt,
        procedure_acquisition_gte=procedure_acquisition_gte,
        procedure_acquisition_in=procedure_acquisition_in,
        procedure_acquisition_isnull=procedure_acquisition_isnull,
        procedure_acquisition_lt=procedure_acquisition_lt,
        procedure_acquisition_lte=procedure_acquisition_lte,
        procedure_acquisition_ob_id=procedure_acquisition_ob_id,
        procedure_acquisition_ob_id_in=procedure_acquisition_ob_id_in,
        procedure_acquisition_uuid=procedure_acquisition_uuid,
        procedure_acquisition_uuid_in=procedure_acquisition_uuid_in,
        procedure_composite_process=procedure_composite_process,
        procedure_composite_process_gt=procedure_composite_process_gt,
        procedure_composite_process_gte=procedure_composite_process_gte,
        procedure_composite_process_in=procedure_composite_process_in,
        procedure_composite_process_isnull=procedure_composite_process_isnull,
        procedure_composite_process_lt=procedure_composite_process_lt,
        procedure_composite_process_lte=procedure_composite_process_lte,
        procedure_computation=procedure_computation,
        procedure_computation_gt=procedure_computation_gt,
        procedure_computation_gte=procedure_computation_gte,
        procedure_computation_in=procedure_computation_in,
        procedure_computation_isnull=procedure_computation_isnull,
        procedure_computation_lt=procedure_computation_lt,
        procedure_computation_lte=procedure_computation_lte,
        procedure_description=procedure_description,
        procedure_description_contains=procedure_description_contains,
        procedure_description_endswith=procedure_description_endswith,
        procedure_description_gt=procedure_description_gt,
        procedure_description_gte=procedure_description_gte,
        procedure_description_icontains=procedure_description_icontains,
        procedure_description_iendswith=procedure_description_iendswith,
        procedure_description_iexact=procedure_description_iexact,
        procedure_description_in=procedure_description_in,
        procedure_description_iregex=procedure_description_iregex,
        procedure_description_isnull=procedure_description_isnull,
        procedure_description_istartswith=procedure_description_istartswith,
        procedure_description_lt=procedure_description_lt,
        procedure_description_lte=procedure_description_lte,
        procedure_description_range=procedure_description_range,
        procedure_description_regex=procedure_description_regex,
        procedure_description_startswith=procedure_description_startswith,
        projects_ob_id=projects_ob_id,
        projects_ob_id_in=projects_ob_id_in,
        projects_uuid=projects_uuid,
        projects_uuid_in=projects_uuid_in,
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
        removed_data_reason=removed_data_reason,
        removed_data_reason_contains=removed_data_reason_contains,
        removed_data_reason_endswith=removed_data_reason_endswith,
        removed_data_reason_gt=removed_data_reason_gt,
        removed_data_reason_gte=removed_data_reason_gte,
        removed_data_reason_icontains=removed_data_reason_icontains,
        removed_data_reason_iendswith=removed_data_reason_iendswith,
        removed_data_reason_iexact=removed_data_reason_iexact,
        removed_data_reason_in=removed_data_reason_in,
        removed_data_reason_iregex=removed_data_reason_iregex,
        removed_data_reason_isnull=removed_data_reason_isnull,
        removed_data_reason_istartswith=removed_data_reason_istartswith,
        removed_data_reason_lt=removed_data_reason_lt,
        removed_data_reason_lte=removed_data_reason_lte,
        removed_data_reason_range=removed_data_reason_range,
        removed_data_reason_regex=removed_data_reason_regex,
        removed_data_reason_startswith=removed_data_reason_startswith,
        removed_data_time=removed_data_time,
        removed_data_time_contained_by=removed_data_time_contained_by,
        removed_data_time_contains=removed_data_time_contains,
        removed_data_time_date=removed_data_time_date,
        removed_data_time_day=removed_data_time_day,
        removed_data_time_endswith=removed_data_time_endswith,
        removed_data_time_gt=removed_data_time_gt,
        removed_data_time_gte=removed_data_time_gte,
        removed_data_time_hour=removed_data_time_hour,
        removed_data_time_icontains=removed_data_time_icontains,
        removed_data_time_iendswith=removed_data_time_iendswith,
        removed_data_time_iexact=removed_data_time_iexact,
        removed_data_time_in=removed_data_time_in,
        removed_data_time_iregex=removed_data_time_iregex,
        removed_data_time_isnull=removed_data_time_isnull,
        removed_data_time_iso_week_day=removed_data_time_iso_week_day,
        removed_data_time_iso_year=removed_data_time_iso_year,
        removed_data_time_istartswith=removed_data_time_istartswith,
        removed_data_time_lt=removed_data_time_lt,
        removed_data_time_lte=removed_data_time_lte,
        removed_data_time_minute=removed_data_time_minute,
        removed_data_time_month=removed_data_time_month,
        removed_data_time_quarter=removed_data_time_quarter,
        removed_data_time_range=removed_data_time_range,
        removed_data_time_regex=removed_data_time_regex,
        removed_data_time_second=removed_data_time_second,
        removed_data_time_startswith=removed_data_time_startswith,
        removed_data_time_time=removed_data_time_time,
        removed_data_time_week=removed_data_time_week,
        removed_data_time_week_day=removed_data_time_week_day,
        removed_data_time_year=removed_data_time_year,
        resolution=resolution,
        resolution_contains=resolution_contains,
        resolution_endswith=resolution_endswith,
        resolution_gt=resolution_gt,
        resolution_gte=resolution_gte,
        resolution_icontains=resolution_icontains,
        resolution_iendswith=resolution_iendswith,
        resolution_iexact=resolution_iexact,
        resolution_in=resolution_in,
        resolution_iregex=resolution_iregex,
        resolution_isnull=resolution_isnull,
        resolution_istartswith=resolution_istartswith,
        resolution_lt=resolution_lt,
        resolution_lte=resolution_lte,
        resolution_range=resolution_range,
        resolution_regex=resolution_regex,
        resolution_startswith=resolution_startswith,
        result_quality=result_quality,
        result_quality_date=result_quality_date,
        result_quality_date_gt=result_quality_date_gt,
        result_quality_date_gte=result_quality_date_gte,
        result_quality_date_lt=result_quality_date_lt,
        result_quality_date_lte=result_quality_date_lte,
        result_quality_date_range=result_quality_date_range,
        result_quality_explanation=result_quality_explanation,
        result_quality_explanation_contains=result_quality_explanation_contains,
        result_quality_gt=result_quality_gt,
        result_quality_gte=result_quality_gte,
        result_quality_in=result_quality_in,
        result_quality_isnull=result_quality_isnull,
        result_quality_lt=result_quality_lt,
        result_quality_lte=result_quality_lte,
        result_quality_ob_id=result_quality_ob_id,
        result_quality_ob_id_in=result_quality_ob_id_in,
        result_quality_passes_test=result_quality_passes_test,
        result_quality_result_title=result_quality_result_title,
        result_quality_result_title_contains=result_quality_result_title_contains,
        result_field=result_field,
        result_field_data_path=result_field_data_path,
        result_field_data_path_contains=result_field_data_path_contains,
        result_field_data_path_startswith=result_field_data_path_startswith,
        result_field_file_format=result_field_file_format,
        result_field_file_format_contains=result_field_file_format_contains,
        result_field_gt=result_field_gt,
        result_field_gte=result_field_gte,
        result_field_in=result_field_in,
        result_field_isnull=result_field_isnull,
        result_field_lt=result_field_lt,
        result_field_lte=result_field_lte,
        result_field_storage_location=result_field_storage_location,
        result_field_storage_status=result_field_storage_status,
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
        submission_user_id=submission_user_id,
        submission_user_id_contains=submission_user_id_contains,
        submission_user_id_endswith=submission_user_id_endswith,
        submission_user_id_gt=submission_user_id_gt,
        submission_user_id_gte=submission_user_id_gte,
        submission_user_id_icontains=submission_user_id_icontains,
        submission_user_id_iendswith=submission_user_id_iendswith,
        submission_user_id_iexact=submission_user_id_iexact,
        submission_user_id_in=submission_user_id_in,
        submission_user_id_iregex=submission_user_id_iregex,
        submission_user_id_isnull=submission_user_id_isnull,
        submission_user_id_istartswith=submission_user_id_istartswith,
        submission_user_id_lt=submission_user_id_lt,
        submission_user_id_lte=submission_user_id_lte,
        submission_user_id_range=submission_user_id_range,
        submission_user_id_regex=submission_user_id_regex,
        submission_user_id_startswith=submission_user_id_startswith,
        time_period=time_period,
        time_period_end_time=time_period_end_time,
        time_period_end_time_gt=time_period_end_time_gt,
        time_period_end_time_gte=time_period_end_time_gte,
        time_period_end_time_lt=time_period_end_time_lt,
        time_period_end_time_lte=time_period_end_time_lte,
        time_period_end_time_range=time_period_end_time_range,
        time_period_gt=time_period_gt,
        time_period_gte=time_period_gte,
        time_period_in=time_period_in,
        time_period_isnull=time_period_isnull,
        time_period_lt=time_period_lt,
        time_period_lte=time_period_lte,
        time_period_ob_id=time_period_ob_id,
        time_period_ob_id_in=time_period_ob_id_in,
        time_period_start_time=time_period_start_time,
        time_period_start_time_gt=time_period_start_time_gt,
        time_period_start_time_gte=time_period_start_time_gte,
        time_period_start_time_lt=time_period_start_time_lt,
        time_period_start_time_lte=time_period_start_time_lte,
        time_period_start_time_range=time_period_start_time_range,
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
        update_frequency=update_frequency,
        update_frequency_contains=update_frequency_contains,
        update_frequency_endswith=update_frequency_endswith,
        update_frequency_gt=update_frequency_gt,
        update_frequency_gte=update_frequency_gte,
        update_frequency_icontains=update_frequency_icontains,
        update_frequency_iendswith=update_frequency_iendswith,
        update_frequency_iexact=update_frequency_iexact,
        update_frequency_in=update_frequency_in,
        update_frequency_iregex=update_frequency_iregex,
        update_frequency_isnull=update_frequency_isnull,
        update_frequency_istartswith=update_frequency_istartswith,
        update_frequency_lt=update_frequency_lt,
        update_frequency_lte=update_frequency_lte,
        update_frequency_range=update_frequency_range,
        update_frequency_regex=update_frequency_regex,
        update_frequency_startswith=update_frequency_startswith,
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
        valid_time_period=valid_time_period,
        valid_time_period_gt=valid_time_period_gt,
        valid_time_period_gte=valid_time_period_gte,
        valid_time_period_in=valid_time_period_in,
        valid_time_period_isnull=valid_time_period_isnull,
        valid_time_period_lt=valid_time_period_lt,
        valid_time_period_lte=valid_time_period_lte,
        vertical_extent=vertical_extent,
        vertical_extent_gt=vertical_extent_gt,
        vertical_extent_gte=vertical_extent_gte,
        vertical_extent_in=vertical_extent_in,
        vertical_extent_isnull=vertical_extent_isnull,
        vertical_extent_lt=vertical_extent_lt,
        vertical_extent_lte=vertical_extent_lte,
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
    creation_date: datetime.datetime | Unset = UNSET,
    creation_date_contained_by: datetime.datetime | Unset = UNSET,
    creation_date_contains: datetime.datetime | Unset = UNSET,
    creation_date_date: datetime.date | Unset = UNSET,
    creation_date_day: float | Unset = UNSET,
    creation_date_endswith: datetime.datetime | Unset = UNSET,
    creation_date_gt: datetime.datetime | Unset = UNSET,
    creation_date_gte: datetime.datetime | Unset = UNSET,
    creation_date_hour: float | Unset = UNSET,
    creation_date_icontains: datetime.datetime | Unset = UNSET,
    creation_date_iendswith: datetime.datetime | Unset = UNSET,
    creation_date_iexact: datetime.datetime | Unset = UNSET,
    creation_date_in: list[datetime.datetime] | Unset = UNSET,
    creation_date_iregex: datetime.datetime | Unset = UNSET,
    creation_date_isnull: bool | Unset = UNSET,
    creation_date_iso_week_day: float | Unset = UNSET,
    creation_date_iso_year: float | Unset = UNSET,
    creation_date_istartswith: datetime.datetime | Unset = UNSET,
    creation_date_lt: datetime.datetime | Unset = UNSET,
    creation_date_lte: datetime.datetime | Unset = UNSET,
    creation_date_minute: float | Unset = UNSET,
    creation_date_month: float | Unset = UNSET,
    creation_date_quarter: float | Unset = UNSET,
    creation_date_range: list[datetime.datetime] | Unset = UNSET,
    creation_date_regex: datetime.datetime | Unset = UNSET,
    creation_date_second: float | Unset = UNSET,
    creation_date_startswith: datetime.datetime | Unset = UNSET,
    creation_date_time: str | Unset = UNSET,
    creation_date_week: float | Unset = UNSET,
    creation_date_week_day: float | Unset = UNSET,
    creation_date_year: float | Unset = UNSET,
    data_lineage: str | Unset = UNSET,
    data_lineage_contains: str | Unset = UNSET,
    data_lineage_endswith: str | Unset = UNSET,
    data_lineage_gt: str | Unset = UNSET,
    data_lineage_gte: str | Unset = UNSET,
    data_lineage_icontains: str | Unset = UNSET,
    data_lineage_iendswith: str | Unset = UNSET,
    data_lineage_iexact: str | Unset = UNSET,
    data_lineage_in: list[str] | Unset = UNSET,
    data_lineage_iregex: str | Unset = UNSET,
    data_lineage_isnull: bool | Unset = UNSET,
    data_lineage_istartswith: str | Unset = UNSET,
    data_lineage_lt: str | Unset = UNSET,
    data_lineage_lte: str | Unset = UNSET,
    data_lineage_range: list[str] | Unset = UNSET,
    data_lineage_regex: str | Unset = UNSET,
    data_lineage_startswith: str | Unset = UNSET,
    data_published_time: datetime.datetime | Unset = UNSET,
    data_published_time_contained_by: datetime.datetime | Unset = UNSET,
    data_published_time_contains: datetime.datetime | Unset = UNSET,
    data_published_time_date: datetime.date | Unset = UNSET,
    data_published_time_day: float | Unset = UNSET,
    data_published_time_endswith: datetime.datetime | Unset = UNSET,
    data_published_time_gt: datetime.datetime | Unset = UNSET,
    data_published_time_gte: datetime.datetime | Unset = UNSET,
    data_published_time_hour: float | Unset = UNSET,
    data_published_time_icontains: datetime.datetime | Unset = UNSET,
    data_published_time_iendswith: datetime.datetime | Unset = UNSET,
    data_published_time_iexact: datetime.datetime | Unset = UNSET,
    data_published_time_in: list[datetime.datetime] | Unset = UNSET,
    data_published_time_iregex: datetime.datetime | Unset = UNSET,
    data_published_time_isnull: bool | Unset = UNSET,
    data_published_time_iso_week_day: float | Unset = UNSET,
    data_published_time_iso_year: float | Unset = UNSET,
    data_published_time_istartswith: datetime.datetime | Unset = UNSET,
    data_published_time_lt: datetime.datetime | Unset = UNSET,
    data_published_time_lte: datetime.datetime | Unset = UNSET,
    data_published_time_minute: float | Unset = UNSET,
    data_published_time_month: float | Unset = UNSET,
    data_published_time_quarter: float | Unset = UNSET,
    data_published_time_range: list[datetime.datetime] | Unset = UNSET,
    data_published_time_regex: datetime.datetime | Unset = UNSET,
    data_published_time_second: float | Unset = UNSET,
    data_published_time_startswith: datetime.datetime | Unset = UNSET,
    data_published_time_time: str | Unset = UNSET,
    data_published_time_week: float | Unset = UNSET,
    data_published_time_week_day: float | Unset = UNSET,
    data_published_time_year: float | Unset = UNSET,
    discovery_keywords_name: str | Unset = UNSET,
    discovery_keywords_name_contains: str | Unset = UNSET,
    doi_published_time: datetime.datetime | Unset = UNSET,
    doi_published_time_contained_by: datetime.datetime | Unset = UNSET,
    doi_published_time_contains: datetime.datetime | Unset = UNSET,
    doi_published_time_date: datetime.date | Unset = UNSET,
    doi_published_time_day: float | Unset = UNSET,
    doi_published_time_endswith: datetime.datetime | Unset = UNSET,
    doi_published_time_gt: datetime.datetime | Unset = UNSET,
    doi_published_time_gte: datetime.datetime | Unset = UNSET,
    doi_published_time_hour: float | Unset = UNSET,
    doi_published_time_icontains: datetime.datetime | Unset = UNSET,
    doi_published_time_iendswith: datetime.datetime | Unset = UNSET,
    doi_published_time_iexact: datetime.datetime | Unset = UNSET,
    doi_published_time_in: list[datetime.datetime] | Unset = UNSET,
    doi_published_time_iregex: datetime.datetime | Unset = UNSET,
    doi_published_time_isnull: bool | Unset = UNSET,
    doi_published_time_iso_week_day: float | Unset = UNSET,
    doi_published_time_iso_year: float | Unset = UNSET,
    doi_published_time_istartswith: datetime.datetime | Unset = UNSET,
    doi_published_time_lt: datetime.datetime | Unset = UNSET,
    doi_published_time_lte: datetime.datetime | Unset = UNSET,
    doi_published_time_minute: float | Unset = UNSET,
    doi_published_time_month: float | Unset = UNSET,
    doi_published_time_quarter: float | Unset = UNSET,
    doi_published_time_range: list[datetime.datetime] | Unset = UNSET,
    doi_published_time_regex: datetime.datetime | Unset = UNSET,
    doi_published_time_second: float | Unset = UNSET,
    doi_published_time_startswith: datetime.datetime | Unset = UNSET,
    doi_published_time_time: str | Unset = UNSET,
    doi_published_time_week: float | Unset = UNSET,
    doi_published_time_week_day: float | Unset = UNSET,
    doi_published_time_year: float | Unset = UNSET,
    dont_harvest_from_projects: bool | Unset = UNSET,
    dont_harvest_from_projects_contains: bool | Unset = UNSET,
    dont_harvest_from_projects_endswith: bool | Unset = UNSET,
    dont_harvest_from_projects_gt: bool | Unset = UNSET,
    dont_harvest_from_projects_gte: bool | Unset = UNSET,
    dont_harvest_from_projects_icontains: bool | Unset = UNSET,
    dont_harvest_from_projects_iendswith: bool | Unset = UNSET,
    dont_harvest_from_projects_iexact: bool | Unset = UNSET,
    dont_harvest_from_projects_in: list[bool] | Unset = UNSET,
    dont_harvest_from_projects_iregex: bool | Unset = UNSET,
    dont_harvest_from_projects_isnull: bool | Unset = UNSET,
    dont_harvest_from_projects_istartswith: bool | Unset = UNSET,
    dont_harvest_from_projects_lt: bool | Unset = UNSET,
    dont_harvest_from_projects_lte: bool | Unset = UNSET,
    dont_harvest_from_projects_range: list[bool] | Unset = UNSET,
    dont_harvest_from_projects_regex: bool | Unset = UNSET,
    dont_harvest_from_projects_startswith: bool | Unset = UNSET,
    feature_of_interest: str | Unset = UNSET,
    feature_of_interest_contains: str | Unset = UNSET,
    feature_of_interest_endswith: str | Unset = UNSET,
    feature_of_interest_gt: str | Unset = UNSET,
    feature_of_interest_gte: str | Unset = UNSET,
    feature_of_interest_icontains: str | Unset = UNSET,
    feature_of_interest_iendswith: str | Unset = UNSET,
    feature_of_interest_iexact: str | Unset = UNSET,
    feature_of_interest_in: list[str] | Unset = UNSET,
    feature_of_interest_iregex: str | Unset = UNSET,
    feature_of_interest_isnull: bool | Unset = UNSET,
    feature_of_interest_istartswith: str | Unset = UNSET,
    feature_of_interest_lt: str | Unset = UNSET,
    feature_of_interest_lte: str | Unset = UNSET,
    feature_of_interest_range: list[str] | Unset = UNSET,
    feature_of_interest_regex: str | Unset = UNSET,
    feature_of_interest_startswith: str | Unset = UNSET,
    geographic_extent: int | Unset = UNSET,
    geographic_extent_east_bound_longitude: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_gt: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_gte: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_lt: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_lte: float | Unset = UNSET,
    geographic_extent_east_bound_longitude_range: list[float] | Unset = UNSET,
    geographic_extent_gt: int | Unset = UNSET,
    geographic_extent_gte: int | Unset = UNSET,
    geographic_extent_in: list[int] | Unset = UNSET,
    geographic_extent_isnull: bool | Unset = UNSET,
    geographic_extent_lt: int | Unset = UNSET,
    geographic_extent_lte: int | Unset = UNSET,
    geographic_extent_north_bound_latitude: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_gt: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_gte: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_lt: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_lte: float | Unset = UNSET,
    geographic_extent_north_bound_latitude_range: list[float] | Unset = UNSET,
    geographic_extent_ob_id: int | Unset = UNSET,
    geographic_extent_ob_id_in: list[int] | Unset = UNSET,
    geographic_extent_south_bound_latitude: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_gt: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_gte: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_lt: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_lte: float | Unset = UNSET,
    geographic_extent_south_bound_latitude_range: list[float] | Unset = UNSET,
    geographic_extent_west_bound_longitude: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_gt: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_gte: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_lt: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_lte: float | Unset = UNSET,
    geographic_extent_west_bound_longitude_range: list[float] | Unset = UNSET,
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
    language: ObservationsListLanguage | Unset = UNSET,
    language_contains: str | Unset = UNSET,
    language_endswith: str | Unset = UNSET,
    language_gt: str | Unset = UNSET,
    language_gte: str | Unset = UNSET,
    language_icontains: str | Unset = UNSET,
    language_iendswith: str | Unset = UNSET,
    language_iexact: str | Unset = UNSET,
    language_in: list[str] | Unset = UNSET,
    language_iregex: str | Unset = UNSET,
    language_isnull: bool | Unset = UNSET,
    language_istartswith: str | Unset = UNSET,
    language_lt: str | Unset = UNSET,
    language_lte: str | Unset = UNSET,
    language_range: list[str] | Unset = UNSET,
    language_regex: str | Unset = UNSET,
    language_startswith: str | Unset = UNSET,
    last_updated_date: datetime.datetime | Unset = UNSET,
    last_updated_date_contained_by: datetime.datetime | Unset = UNSET,
    last_updated_date_contains: datetime.datetime | Unset = UNSET,
    last_updated_date_date: datetime.date | Unset = UNSET,
    last_updated_date_day: float | Unset = UNSET,
    last_updated_date_endswith: datetime.datetime | Unset = UNSET,
    last_updated_date_gt: datetime.datetime | Unset = UNSET,
    last_updated_date_gte: datetime.datetime | Unset = UNSET,
    last_updated_date_hour: float | Unset = UNSET,
    last_updated_date_icontains: datetime.datetime | Unset = UNSET,
    last_updated_date_iendswith: datetime.datetime | Unset = UNSET,
    last_updated_date_iexact: datetime.datetime | Unset = UNSET,
    last_updated_date_in: list[datetime.datetime] | Unset = UNSET,
    last_updated_date_iregex: datetime.datetime | Unset = UNSET,
    last_updated_date_isnull: bool | Unset = UNSET,
    last_updated_date_iso_week_day: float | Unset = UNSET,
    last_updated_date_iso_year: float | Unset = UNSET,
    last_updated_date_istartswith: datetime.datetime | Unset = UNSET,
    last_updated_date_lt: datetime.datetime | Unset = UNSET,
    last_updated_date_lte: datetime.datetime | Unset = UNSET,
    last_updated_date_minute: float | Unset = UNSET,
    last_updated_date_month: float | Unset = UNSET,
    last_updated_date_quarter: float | Unset = UNSET,
    last_updated_date_range: list[datetime.datetime] | Unset = UNSET,
    last_updated_date_regex: datetime.datetime | Unset = UNSET,
    last_updated_date_second: float | Unset = UNSET,
    last_updated_date_startswith: datetime.datetime | Unset = UNSET,
    last_updated_date_time: str | Unset = UNSET,
    last_updated_date_week: float | Unset = UNSET,
    last_updated_date_week_day: float | Unset = UNSET,
    last_updated_date_year: float | Unset = UNSET,
    latest_data_update_time: datetime.datetime | Unset = UNSET,
    latest_data_update_time_contained_by: datetime.datetime | Unset = UNSET,
    latest_data_update_time_contains: datetime.datetime | Unset = UNSET,
    latest_data_update_time_date: datetime.date | Unset = UNSET,
    latest_data_update_time_day: float | Unset = UNSET,
    latest_data_update_time_endswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_gt: datetime.datetime | Unset = UNSET,
    latest_data_update_time_gte: datetime.datetime | Unset = UNSET,
    latest_data_update_time_hour: float | Unset = UNSET,
    latest_data_update_time_icontains: datetime.datetime | Unset = UNSET,
    latest_data_update_time_iendswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_iexact: datetime.datetime | Unset = UNSET,
    latest_data_update_time_in: list[datetime.datetime] | Unset = UNSET,
    latest_data_update_time_iregex: datetime.datetime | Unset = UNSET,
    latest_data_update_time_isnull: bool | Unset = UNSET,
    latest_data_update_time_iso_week_day: float | Unset = UNSET,
    latest_data_update_time_iso_year: float | Unset = UNSET,
    latest_data_update_time_istartswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_lt: datetime.datetime | Unset = UNSET,
    latest_data_update_time_lte: datetime.datetime | Unset = UNSET,
    latest_data_update_time_minute: float | Unset = UNSET,
    latest_data_update_time_month: float | Unset = UNSET,
    latest_data_update_time_quarter: float | Unset = UNSET,
    latest_data_update_time_range: list[datetime.datetime] | Unset = UNSET,
    latest_data_update_time_regex: datetime.datetime | Unset = UNSET,
    latest_data_update_time_second: float | Unset = UNSET,
    latest_data_update_time_startswith: datetime.datetime | Unset = UNSET,
    latest_data_update_time_time: str | Unset = UNSET,
    latest_data_update_time_week: float | Unset = UNSET,
    latest_data_update_time_week_day: float | Unset = UNSET,
    latest_data_update_time_year: float | Unset = UNSET,
    limit: int | Unset = UNSET,
    non_geographic_flag: bool | Unset = UNSET,
    non_geographic_flag_contains: bool | Unset = UNSET,
    non_geographic_flag_endswith: bool | Unset = UNSET,
    non_geographic_flag_gt: bool | Unset = UNSET,
    non_geographic_flag_gte: bool | Unset = UNSET,
    non_geographic_flag_icontains: bool | Unset = UNSET,
    non_geographic_flag_iendswith: bool | Unset = UNSET,
    non_geographic_flag_iexact: bool | Unset = UNSET,
    non_geographic_flag_in: list[bool] | Unset = UNSET,
    non_geographic_flag_iregex: bool | Unset = UNSET,
    non_geographic_flag_isnull: bool | Unset = UNSET,
    non_geographic_flag_istartswith: bool | Unset = UNSET,
    non_geographic_flag_lt: bool | Unset = UNSET,
    non_geographic_flag_lte: bool | Unset = UNSET,
    non_geographic_flag_range: list[bool] | Unset = UNSET,
    non_geographic_flag_regex: bool | Unset = UNSET,
    non_geographic_flag_startswith: bool | Unset = UNSET,
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
    permissions_access_category: ObservationsListAccessCategory | Unset = UNSET,
    permissions_access_category_in: list[str] | Unset = UNSET,
    permissions_access_roles: str | Unset = UNSET,
    permissions_access_roles_in: list[str] | Unset = UNSET,
    procedure_acquisition: int | Unset = UNSET,
    procedure_acquisition_gt: int | Unset = UNSET,
    procedure_acquisition_gte: int | Unset = UNSET,
    procedure_acquisition_in: list[int] | Unset = UNSET,
    procedure_acquisition_isnull: bool | Unset = UNSET,
    procedure_acquisition_lt: int | Unset = UNSET,
    procedure_acquisition_lte: int | Unset = UNSET,
    procedure_acquisition_ob_id: int | Unset = UNSET,
    procedure_acquisition_ob_id_in: list[int] | Unset = UNSET,
    procedure_acquisition_uuid: str | Unset = UNSET,
    procedure_acquisition_uuid_in: list[str] | Unset = UNSET,
    procedure_composite_process: int | Unset = UNSET,
    procedure_composite_process_gt: int | Unset = UNSET,
    procedure_composite_process_gte: int | Unset = UNSET,
    procedure_composite_process_in: list[int] | Unset = UNSET,
    procedure_composite_process_isnull: bool | Unset = UNSET,
    procedure_composite_process_lt: int | Unset = UNSET,
    procedure_composite_process_lte: int | Unset = UNSET,
    procedure_computation: int | Unset = UNSET,
    procedure_computation_gt: int | Unset = UNSET,
    procedure_computation_gte: int | Unset = UNSET,
    procedure_computation_in: list[int] | Unset = UNSET,
    procedure_computation_isnull: bool | Unset = UNSET,
    procedure_computation_lt: int | Unset = UNSET,
    procedure_computation_lte: int | Unset = UNSET,
    procedure_description: str | Unset = UNSET,
    procedure_description_contains: str | Unset = UNSET,
    procedure_description_endswith: str | Unset = UNSET,
    procedure_description_gt: str | Unset = UNSET,
    procedure_description_gte: str | Unset = UNSET,
    procedure_description_icontains: str | Unset = UNSET,
    procedure_description_iendswith: str | Unset = UNSET,
    procedure_description_iexact: str | Unset = UNSET,
    procedure_description_in: list[str] | Unset = UNSET,
    procedure_description_iregex: str | Unset = UNSET,
    procedure_description_isnull: bool | Unset = UNSET,
    procedure_description_istartswith: str | Unset = UNSET,
    procedure_description_lt: str | Unset = UNSET,
    procedure_description_lte: str | Unset = UNSET,
    procedure_description_range: list[str] | Unset = UNSET,
    procedure_description_regex: str | Unset = UNSET,
    procedure_description_startswith: str | Unset = UNSET,
    projects_ob_id: int | Unset = UNSET,
    projects_ob_id_in: list[int] | Unset = UNSET,
    projects_uuid: str | Unset = UNSET,
    projects_uuid_in: list[str] | Unset = UNSET,
    publication_state: ObservationsListPublicationState | Unset = UNSET,
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
    removed_data_reason: str | Unset = UNSET,
    removed_data_reason_contains: str | Unset = UNSET,
    removed_data_reason_endswith: str | Unset = UNSET,
    removed_data_reason_gt: str | Unset = UNSET,
    removed_data_reason_gte: str | Unset = UNSET,
    removed_data_reason_icontains: str | Unset = UNSET,
    removed_data_reason_iendswith: str | Unset = UNSET,
    removed_data_reason_iexact: str | Unset = UNSET,
    removed_data_reason_in: list[str] | Unset = UNSET,
    removed_data_reason_iregex: str | Unset = UNSET,
    removed_data_reason_isnull: bool | Unset = UNSET,
    removed_data_reason_istartswith: str | Unset = UNSET,
    removed_data_reason_lt: str | Unset = UNSET,
    removed_data_reason_lte: str | Unset = UNSET,
    removed_data_reason_range: list[str] | Unset = UNSET,
    removed_data_reason_regex: str | Unset = UNSET,
    removed_data_reason_startswith: str | Unset = UNSET,
    removed_data_time: datetime.datetime | Unset = UNSET,
    removed_data_time_contained_by: datetime.datetime | Unset = UNSET,
    removed_data_time_contains: datetime.datetime | Unset = UNSET,
    removed_data_time_date: datetime.date | Unset = UNSET,
    removed_data_time_day: float | Unset = UNSET,
    removed_data_time_endswith: datetime.datetime | Unset = UNSET,
    removed_data_time_gt: datetime.datetime | Unset = UNSET,
    removed_data_time_gte: datetime.datetime | Unset = UNSET,
    removed_data_time_hour: float | Unset = UNSET,
    removed_data_time_icontains: datetime.datetime | Unset = UNSET,
    removed_data_time_iendswith: datetime.datetime | Unset = UNSET,
    removed_data_time_iexact: datetime.datetime | Unset = UNSET,
    removed_data_time_in: list[datetime.datetime] | Unset = UNSET,
    removed_data_time_iregex: datetime.datetime | Unset = UNSET,
    removed_data_time_isnull: bool | Unset = UNSET,
    removed_data_time_iso_week_day: float | Unset = UNSET,
    removed_data_time_iso_year: float | Unset = UNSET,
    removed_data_time_istartswith: datetime.datetime | Unset = UNSET,
    removed_data_time_lt: datetime.datetime | Unset = UNSET,
    removed_data_time_lte: datetime.datetime | Unset = UNSET,
    removed_data_time_minute: float | Unset = UNSET,
    removed_data_time_month: float | Unset = UNSET,
    removed_data_time_quarter: float | Unset = UNSET,
    removed_data_time_range: list[datetime.datetime] | Unset = UNSET,
    removed_data_time_regex: datetime.datetime | Unset = UNSET,
    removed_data_time_second: float | Unset = UNSET,
    removed_data_time_startswith: datetime.datetime | Unset = UNSET,
    removed_data_time_time: str | Unset = UNSET,
    removed_data_time_week: float | Unset = UNSET,
    removed_data_time_week_day: float | Unset = UNSET,
    removed_data_time_year: float | Unset = UNSET,
    resolution: str | Unset = UNSET,
    resolution_contains: str | Unset = UNSET,
    resolution_endswith: str | Unset = UNSET,
    resolution_gt: str | Unset = UNSET,
    resolution_gte: str | Unset = UNSET,
    resolution_icontains: str | Unset = UNSET,
    resolution_iendswith: str | Unset = UNSET,
    resolution_iexact: str | Unset = UNSET,
    resolution_in: list[str] | Unset = UNSET,
    resolution_iregex: str | Unset = UNSET,
    resolution_isnull: bool | Unset = UNSET,
    resolution_istartswith: str | Unset = UNSET,
    resolution_lt: str | Unset = UNSET,
    resolution_lte: str | Unset = UNSET,
    resolution_range: list[str] | Unset = UNSET,
    resolution_regex: str | Unset = UNSET,
    resolution_startswith: str | Unset = UNSET,
    result_quality: int | Unset = UNSET,
    result_quality_date: datetime.date | Unset = UNSET,
    result_quality_date_gt: datetime.date | Unset = UNSET,
    result_quality_date_gte: datetime.date | Unset = UNSET,
    result_quality_date_lt: datetime.date | Unset = UNSET,
    result_quality_date_lte: datetime.date | Unset = UNSET,
    result_quality_date_range: list[datetime.date] | Unset = UNSET,
    result_quality_explanation: str | Unset = UNSET,
    result_quality_explanation_contains: str | Unset = UNSET,
    result_quality_gt: int | Unset = UNSET,
    result_quality_gte: int | Unset = UNSET,
    result_quality_in: list[int] | Unset = UNSET,
    result_quality_isnull: bool | Unset = UNSET,
    result_quality_lt: int | Unset = UNSET,
    result_quality_lte: int | Unset = UNSET,
    result_quality_ob_id: int | Unset = UNSET,
    result_quality_ob_id_in: list[int] | Unset = UNSET,
    result_quality_passes_test: bool | Unset = UNSET,
    result_quality_result_title: str | Unset = UNSET,
    result_quality_result_title_contains: str | Unset = UNSET,
    result_field: int | Unset = UNSET,
    result_field_data_path: str | Unset = UNSET,
    result_field_data_path_contains: str | Unset = UNSET,
    result_field_data_path_startswith: str | Unset = UNSET,
    result_field_file_format: str | Unset = UNSET,
    result_field_file_format_contains: str | Unset = UNSET,
    result_field_gt: int | Unset = UNSET,
    result_field_gte: int | Unset = UNSET,
    result_field_in: list[int] | Unset = UNSET,
    result_field_isnull: bool | Unset = UNSET,
    result_field_lt: int | Unset = UNSET,
    result_field_lte: int | Unset = UNSET,
    result_field_storage_location: ObservationsListStorageLocation | Unset = UNSET,
    result_field_storage_status: ObservationsListStorageStatus | Unset = UNSET,
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
    status: ObservationsListDataStatus | Unset = UNSET,
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
    submission_user_id: str | Unset = UNSET,
    submission_user_id_contains: str | Unset = UNSET,
    submission_user_id_endswith: str | Unset = UNSET,
    submission_user_id_gt: str | Unset = UNSET,
    submission_user_id_gte: str | Unset = UNSET,
    submission_user_id_icontains: str | Unset = UNSET,
    submission_user_id_iendswith: str | Unset = UNSET,
    submission_user_id_iexact: str | Unset = UNSET,
    submission_user_id_in: list[str] | Unset = UNSET,
    submission_user_id_iregex: str | Unset = UNSET,
    submission_user_id_isnull: bool | Unset = UNSET,
    submission_user_id_istartswith: str | Unset = UNSET,
    submission_user_id_lt: str | Unset = UNSET,
    submission_user_id_lte: str | Unset = UNSET,
    submission_user_id_range: list[str] | Unset = UNSET,
    submission_user_id_regex: str | Unset = UNSET,
    submission_user_id_startswith: str | Unset = UNSET,
    time_period: int | Unset = UNSET,
    time_period_end_time: datetime.datetime | Unset = UNSET,
    time_period_end_time_gt: datetime.datetime | Unset = UNSET,
    time_period_end_time_gte: datetime.datetime | Unset = UNSET,
    time_period_end_time_lt: datetime.datetime | Unset = UNSET,
    time_period_end_time_lte: datetime.datetime | Unset = UNSET,
    time_period_end_time_range: list[datetime.datetime] | Unset = UNSET,
    time_period_gt: int | Unset = UNSET,
    time_period_gte: int | Unset = UNSET,
    time_period_in: list[int] | Unset = UNSET,
    time_period_isnull: bool | Unset = UNSET,
    time_period_lt: int | Unset = UNSET,
    time_period_lte: int | Unset = UNSET,
    time_period_ob_id: int | Unset = UNSET,
    time_period_ob_id_in: list[int] | Unset = UNSET,
    time_period_start_time: datetime.datetime | Unset = UNSET,
    time_period_start_time_gt: datetime.datetime | Unset = UNSET,
    time_period_start_time_gte: datetime.datetime | Unset = UNSET,
    time_period_start_time_lt: datetime.datetime | Unset = UNSET,
    time_period_start_time_lte: datetime.datetime | Unset = UNSET,
    time_period_start_time_range: list[datetime.datetime] | Unset = UNSET,
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
    update_frequency: ObservationsListDataUpdateFrequency | Unset = UNSET,
    update_frequency_contains: str | Unset = UNSET,
    update_frequency_endswith: str | Unset = UNSET,
    update_frequency_gt: str | Unset = UNSET,
    update_frequency_gte: str | Unset = UNSET,
    update_frequency_icontains: str | Unset = UNSET,
    update_frequency_iendswith: str | Unset = UNSET,
    update_frequency_iexact: str | Unset = UNSET,
    update_frequency_in: list[str] | Unset = UNSET,
    update_frequency_iregex: str | Unset = UNSET,
    update_frequency_isnull: bool | Unset = UNSET,
    update_frequency_istartswith: str | Unset = UNSET,
    update_frequency_lt: str | Unset = UNSET,
    update_frequency_lte: str | Unset = UNSET,
    update_frequency_range: list[str] | Unset = UNSET,
    update_frequency_regex: str | Unset = UNSET,
    update_frequency_startswith: str | Unset = UNSET,
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
    valid_time_period: int | Unset = UNSET,
    valid_time_period_gt: int | Unset = UNSET,
    valid_time_period_gte: int | Unset = UNSET,
    valid_time_period_in: list[int] | Unset = UNSET,
    valid_time_period_isnull: bool | Unset = UNSET,
    valid_time_period_lt: int | Unset = UNSET,
    valid_time_period_lte: int | Unset = UNSET,
    vertical_extent: int | Unset = UNSET,
    vertical_extent_gt: int | Unset = UNSET,
    vertical_extent_gte: int | Unset = UNSET,
    vertical_extent_in: list[int] | Unset = UNSET,
    vertical_extent_isnull: bool | Unset = UNSET,
    vertical_extent_lt: int | Unset = UNSET,
    vertical_extent_lte: int | Unset = UNSET,
) -> PaginatedObservationReadList | None:
    """Get a list of Observation objects.

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
        creation_date (datetime.datetime | Unset):
        creation_date_contained_by (datetime.datetime | Unset):
        creation_date_contains (datetime.datetime | Unset):
        creation_date_date (datetime.date | Unset):
        creation_date_day (float | Unset):
        creation_date_endswith (datetime.datetime | Unset):
        creation_date_gt (datetime.datetime | Unset):
        creation_date_gte (datetime.datetime | Unset):
        creation_date_hour (float | Unset):
        creation_date_icontains (datetime.datetime | Unset):
        creation_date_iendswith (datetime.datetime | Unset):
        creation_date_iexact (datetime.datetime | Unset):
        creation_date_in (list[datetime.datetime] | Unset):
        creation_date_iregex (datetime.datetime | Unset):
        creation_date_isnull (bool | Unset):
        creation_date_iso_week_day (float | Unset):
        creation_date_iso_year (float | Unset):
        creation_date_istartswith (datetime.datetime | Unset):
        creation_date_lt (datetime.datetime | Unset):
        creation_date_lte (datetime.datetime | Unset):
        creation_date_minute (float | Unset):
        creation_date_month (float | Unset):
        creation_date_quarter (float | Unset):
        creation_date_range (list[datetime.datetime] | Unset):
        creation_date_regex (datetime.datetime | Unset):
        creation_date_second (float | Unset):
        creation_date_startswith (datetime.datetime | Unset):
        creation_date_time (str | Unset):
        creation_date_week (float | Unset):
        creation_date_week_day (float | Unset):
        creation_date_year (float | Unset):
        data_lineage (str | Unset):
        data_lineage_contains (str | Unset):
        data_lineage_endswith (str | Unset):
        data_lineage_gt (str | Unset):
        data_lineage_gte (str | Unset):
        data_lineage_icontains (str | Unset):
        data_lineage_iendswith (str | Unset):
        data_lineage_iexact (str | Unset):
        data_lineage_in (list[str] | Unset):
        data_lineage_iregex (str | Unset):
        data_lineage_isnull (bool | Unset):
        data_lineage_istartswith (str | Unset):
        data_lineage_lt (str | Unset):
        data_lineage_lte (str | Unset):
        data_lineage_range (list[str] | Unset):
        data_lineage_regex (str | Unset):
        data_lineage_startswith (str | Unset):
        data_published_time (datetime.datetime | Unset):
        data_published_time_contained_by (datetime.datetime | Unset):
        data_published_time_contains (datetime.datetime | Unset):
        data_published_time_date (datetime.date | Unset):
        data_published_time_day (float | Unset):
        data_published_time_endswith (datetime.datetime | Unset):
        data_published_time_gt (datetime.datetime | Unset):
        data_published_time_gte (datetime.datetime | Unset):
        data_published_time_hour (float | Unset):
        data_published_time_icontains (datetime.datetime | Unset):
        data_published_time_iendswith (datetime.datetime | Unset):
        data_published_time_iexact (datetime.datetime | Unset):
        data_published_time_in (list[datetime.datetime] | Unset):
        data_published_time_iregex (datetime.datetime | Unset):
        data_published_time_isnull (bool | Unset):
        data_published_time_iso_week_day (float | Unset):
        data_published_time_iso_year (float | Unset):
        data_published_time_istartswith (datetime.datetime | Unset):
        data_published_time_lt (datetime.datetime | Unset):
        data_published_time_lte (datetime.datetime | Unset):
        data_published_time_minute (float | Unset):
        data_published_time_month (float | Unset):
        data_published_time_quarter (float | Unset):
        data_published_time_range (list[datetime.datetime] | Unset):
        data_published_time_regex (datetime.datetime | Unset):
        data_published_time_second (float | Unset):
        data_published_time_startswith (datetime.datetime | Unset):
        data_published_time_time (str | Unset):
        data_published_time_week (float | Unset):
        data_published_time_week_day (float | Unset):
        data_published_time_year (float | Unset):
        discovery_keywords_name (str | Unset):
        discovery_keywords_name_contains (str | Unset):
        doi_published_time (datetime.datetime | Unset):
        doi_published_time_contained_by (datetime.datetime | Unset):
        doi_published_time_contains (datetime.datetime | Unset):
        doi_published_time_date (datetime.date | Unset):
        doi_published_time_day (float | Unset):
        doi_published_time_endswith (datetime.datetime | Unset):
        doi_published_time_gt (datetime.datetime | Unset):
        doi_published_time_gte (datetime.datetime | Unset):
        doi_published_time_hour (float | Unset):
        doi_published_time_icontains (datetime.datetime | Unset):
        doi_published_time_iendswith (datetime.datetime | Unset):
        doi_published_time_iexact (datetime.datetime | Unset):
        doi_published_time_in (list[datetime.datetime] | Unset):
        doi_published_time_iregex (datetime.datetime | Unset):
        doi_published_time_isnull (bool | Unset):
        doi_published_time_iso_week_day (float | Unset):
        doi_published_time_iso_year (float | Unset):
        doi_published_time_istartswith (datetime.datetime | Unset):
        doi_published_time_lt (datetime.datetime | Unset):
        doi_published_time_lte (datetime.datetime | Unset):
        doi_published_time_minute (float | Unset):
        doi_published_time_month (float | Unset):
        doi_published_time_quarter (float | Unset):
        doi_published_time_range (list[datetime.datetime] | Unset):
        doi_published_time_regex (datetime.datetime | Unset):
        doi_published_time_second (float | Unset):
        doi_published_time_startswith (datetime.datetime | Unset):
        doi_published_time_time (str | Unset):
        doi_published_time_week (float | Unset):
        doi_published_time_week_day (float | Unset):
        doi_published_time_year (float | Unset):
        dont_harvest_from_projects (bool | Unset):
        dont_harvest_from_projects_contains (bool | Unset):
        dont_harvest_from_projects_endswith (bool | Unset):
        dont_harvest_from_projects_gt (bool | Unset):
        dont_harvest_from_projects_gte (bool | Unset):
        dont_harvest_from_projects_icontains (bool | Unset):
        dont_harvest_from_projects_iendswith (bool | Unset):
        dont_harvest_from_projects_iexact (bool | Unset):
        dont_harvest_from_projects_in (list[bool] | Unset):
        dont_harvest_from_projects_iregex (bool | Unset):
        dont_harvest_from_projects_isnull (bool | Unset):
        dont_harvest_from_projects_istartswith (bool | Unset):
        dont_harvest_from_projects_lt (bool | Unset):
        dont_harvest_from_projects_lte (bool | Unset):
        dont_harvest_from_projects_range (list[bool] | Unset):
        dont_harvest_from_projects_regex (bool | Unset):
        dont_harvest_from_projects_startswith (bool | Unset):
        feature_of_interest (str | Unset):
        feature_of_interest_contains (str | Unset):
        feature_of_interest_endswith (str | Unset):
        feature_of_interest_gt (str | Unset):
        feature_of_interest_gte (str | Unset):
        feature_of_interest_icontains (str | Unset):
        feature_of_interest_iendswith (str | Unset):
        feature_of_interest_iexact (str | Unset):
        feature_of_interest_in (list[str] | Unset):
        feature_of_interest_iregex (str | Unset):
        feature_of_interest_isnull (bool | Unset):
        feature_of_interest_istartswith (str | Unset):
        feature_of_interest_lt (str | Unset):
        feature_of_interest_lte (str | Unset):
        feature_of_interest_range (list[str] | Unset):
        feature_of_interest_regex (str | Unset):
        feature_of_interest_startswith (str | Unset):
        geographic_extent (int | Unset):
        geographic_extent_east_bound_longitude (float | Unset):
        geographic_extent_east_bound_longitude_gt (float | Unset):
        geographic_extent_east_bound_longitude_gte (float | Unset):
        geographic_extent_east_bound_longitude_lt (float | Unset):
        geographic_extent_east_bound_longitude_lte (float | Unset):
        geographic_extent_east_bound_longitude_range (list[float] | Unset):
        geographic_extent_gt (int | Unset):
        geographic_extent_gte (int | Unset):
        geographic_extent_in (list[int] | Unset):
        geographic_extent_isnull (bool | Unset):
        geographic_extent_lt (int | Unset):
        geographic_extent_lte (int | Unset):
        geographic_extent_north_bound_latitude (float | Unset):
        geographic_extent_north_bound_latitude_gt (float | Unset):
        geographic_extent_north_bound_latitude_gte (float | Unset):
        geographic_extent_north_bound_latitude_lt (float | Unset):
        geographic_extent_north_bound_latitude_lte (float | Unset):
        geographic_extent_north_bound_latitude_range (list[float] | Unset):
        geographic_extent_ob_id (int | Unset):
        geographic_extent_ob_id_in (list[int] | Unset):
        geographic_extent_south_bound_latitude (float | Unset):
        geographic_extent_south_bound_latitude_gt (float | Unset):
        geographic_extent_south_bound_latitude_gte (float | Unset):
        geographic_extent_south_bound_latitude_lt (float | Unset):
        geographic_extent_south_bound_latitude_lte (float | Unset):
        geographic_extent_south_bound_latitude_range (list[float] | Unset):
        geographic_extent_west_bound_longitude (float | Unset):
        geographic_extent_west_bound_longitude_gt (float | Unset):
        geographic_extent_west_bound_longitude_gte (float | Unset):
        geographic_extent_west_bound_longitude_lt (float | Unset):
        geographic_extent_west_bound_longitude_lte (float | Unset):
        geographic_extent_west_bound_longitude_range (list[float] | Unset):
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
        language (ObservationsListLanguage | Unset):
        language_contains (str | Unset):
        language_endswith (str | Unset):
        language_gt (str | Unset):
        language_gte (str | Unset):
        language_icontains (str | Unset):
        language_iendswith (str | Unset):
        language_iexact (str | Unset):
        language_in (list[str] | Unset):
        language_iregex (str | Unset):
        language_isnull (bool | Unset):
        language_istartswith (str | Unset):
        language_lt (str | Unset):
        language_lte (str | Unset):
        language_range (list[str] | Unset):
        language_regex (str | Unset):
        language_startswith (str | Unset):
        last_updated_date (datetime.datetime | Unset):
        last_updated_date_contained_by (datetime.datetime | Unset):
        last_updated_date_contains (datetime.datetime | Unset):
        last_updated_date_date (datetime.date | Unset):
        last_updated_date_day (float | Unset):
        last_updated_date_endswith (datetime.datetime | Unset):
        last_updated_date_gt (datetime.datetime | Unset):
        last_updated_date_gte (datetime.datetime | Unset):
        last_updated_date_hour (float | Unset):
        last_updated_date_icontains (datetime.datetime | Unset):
        last_updated_date_iendswith (datetime.datetime | Unset):
        last_updated_date_iexact (datetime.datetime | Unset):
        last_updated_date_in (list[datetime.datetime] | Unset):
        last_updated_date_iregex (datetime.datetime | Unset):
        last_updated_date_isnull (bool | Unset):
        last_updated_date_iso_week_day (float | Unset):
        last_updated_date_iso_year (float | Unset):
        last_updated_date_istartswith (datetime.datetime | Unset):
        last_updated_date_lt (datetime.datetime | Unset):
        last_updated_date_lte (datetime.datetime | Unset):
        last_updated_date_minute (float | Unset):
        last_updated_date_month (float | Unset):
        last_updated_date_quarter (float | Unset):
        last_updated_date_range (list[datetime.datetime] | Unset):
        last_updated_date_regex (datetime.datetime | Unset):
        last_updated_date_second (float | Unset):
        last_updated_date_startswith (datetime.datetime | Unset):
        last_updated_date_time (str | Unset):
        last_updated_date_week (float | Unset):
        last_updated_date_week_day (float | Unset):
        last_updated_date_year (float | Unset):
        latest_data_update_time (datetime.datetime | Unset):
        latest_data_update_time_contained_by (datetime.datetime | Unset):
        latest_data_update_time_contains (datetime.datetime | Unset):
        latest_data_update_time_date (datetime.date | Unset):
        latest_data_update_time_day (float | Unset):
        latest_data_update_time_endswith (datetime.datetime | Unset):
        latest_data_update_time_gt (datetime.datetime | Unset):
        latest_data_update_time_gte (datetime.datetime | Unset):
        latest_data_update_time_hour (float | Unset):
        latest_data_update_time_icontains (datetime.datetime | Unset):
        latest_data_update_time_iendswith (datetime.datetime | Unset):
        latest_data_update_time_iexact (datetime.datetime | Unset):
        latest_data_update_time_in (list[datetime.datetime] | Unset):
        latest_data_update_time_iregex (datetime.datetime | Unset):
        latest_data_update_time_isnull (bool | Unset):
        latest_data_update_time_iso_week_day (float | Unset):
        latest_data_update_time_iso_year (float | Unset):
        latest_data_update_time_istartswith (datetime.datetime | Unset):
        latest_data_update_time_lt (datetime.datetime | Unset):
        latest_data_update_time_lte (datetime.datetime | Unset):
        latest_data_update_time_minute (float | Unset):
        latest_data_update_time_month (float | Unset):
        latest_data_update_time_quarter (float | Unset):
        latest_data_update_time_range (list[datetime.datetime] | Unset):
        latest_data_update_time_regex (datetime.datetime | Unset):
        latest_data_update_time_second (float | Unset):
        latest_data_update_time_startswith (datetime.datetime | Unset):
        latest_data_update_time_time (str | Unset):
        latest_data_update_time_week (float | Unset):
        latest_data_update_time_week_day (float | Unset):
        latest_data_update_time_year (float | Unset):
        limit (int | Unset):
        non_geographic_flag (bool | Unset):
        non_geographic_flag_contains (bool | Unset):
        non_geographic_flag_endswith (bool | Unset):
        non_geographic_flag_gt (bool | Unset):
        non_geographic_flag_gte (bool | Unset):
        non_geographic_flag_icontains (bool | Unset):
        non_geographic_flag_iendswith (bool | Unset):
        non_geographic_flag_iexact (bool | Unset):
        non_geographic_flag_in (list[bool] | Unset):
        non_geographic_flag_iregex (bool | Unset):
        non_geographic_flag_isnull (bool | Unset):
        non_geographic_flag_istartswith (bool | Unset):
        non_geographic_flag_lt (bool | Unset):
        non_geographic_flag_lte (bool | Unset):
        non_geographic_flag_range (list[bool] | Unset):
        non_geographic_flag_regex (bool | Unset):
        non_geographic_flag_startswith (bool | Unset):
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
        permissions_access_category (ObservationsListAccessCategory | Unset):
        permissions_access_category_in (list[str] | Unset):
        permissions_access_roles (str | Unset):
        permissions_access_roles_in (list[str] | Unset):
        procedure_acquisition (int | Unset):
        procedure_acquisition_gt (int | Unset):
        procedure_acquisition_gte (int | Unset):
        procedure_acquisition_in (list[int] | Unset):
        procedure_acquisition_isnull (bool | Unset):
        procedure_acquisition_lt (int | Unset):
        procedure_acquisition_lte (int | Unset):
        procedure_acquisition_ob_id (int | Unset):
        procedure_acquisition_ob_id_in (list[int] | Unset):
        procedure_acquisition_uuid (str | Unset):
        procedure_acquisition_uuid_in (list[str] | Unset):
        procedure_composite_process (int | Unset):
        procedure_composite_process_gt (int | Unset):
        procedure_composite_process_gte (int | Unset):
        procedure_composite_process_in (list[int] | Unset):
        procedure_composite_process_isnull (bool | Unset):
        procedure_composite_process_lt (int | Unset):
        procedure_composite_process_lte (int | Unset):
        procedure_computation (int | Unset):
        procedure_computation_gt (int | Unset):
        procedure_computation_gte (int | Unset):
        procedure_computation_in (list[int] | Unset):
        procedure_computation_isnull (bool | Unset):
        procedure_computation_lt (int | Unset):
        procedure_computation_lte (int | Unset):
        procedure_description (str | Unset):
        procedure_description_contains (str | Unset):
        procedure_description_endswith (str | Unset):
        procedure_description_gt (str | Unset):
        procedure_description_gte (str | Unset):
        procedure_description_icontains (str | Unset):
        procedure_description_iendswith (str | Unset):
        procedure_description_iexact (str | Unset):
        procedure_description_in (list[str] | Unset):
        procedure_description_iregex (str | Unset):
        procedure_description_isnull (bool | Unset):
        procedure_description_istartswith (str | Unset):
        procedure_description_lt (str | Unset):
        procedure_description_lte (str | Unset):
        procedure_description_range (list[str] | Unset):
        procedure_description_regex (str | Unset):
        procedure_description_startswith (str | Unset):
        projects_ob_id (int | Unset):
        projects_ob_id_in (list[int] | Unset):
        projects_uuid (str | Unset):
        projects_uuid_in (list[str] | Unset):
        publication_state (ObservationsListPublicationState | Unset):
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
        removed_data_reason (str | Unset):
        removed_data_reason_contains (str | Unset):
        removed_data_reason_endswith (str | Unset):
        removed_data_reason_gt (str | Unset):
        removed_data_reason_gte (str | Unset):
        removed_data_reason_icontains (str | Unset):
        removed_data_reason_iendswith (str | Unset):
        removed_data_reason_iexact (str | Unset):
        removed_data_reason_in (list[str] | Unset):
        removed_data_reason_iregex (str | Unset):
        removed_data_reason_isnull (bool | Unset):
        removed_data_reason_istartswith (str | Unset):
        removed_data_reason_lt (str | Unset):
        removed_data_reason_lte (str | Unset):
        removed_data_reason_range (list[str] | Unset):
        removed_data_reason_regex (str | Unset):
        removed_data_reason_startswith (str | Unset):
        removed_data_time (datetime.datetime | Unset):
        removed_data_time_contained_by (datetime.datetime | Unset):
        removed_data_time_contains (datetime.datetime | Unset):
        removed_data_time_date (datetime.date | Unset):
        removed_data_time_day (float | Unset):
        removed_data_time_endswith (datetime.datetime | Unset):
        removed_data_time_gt (datetime.datetime | Unset):
        removed_data_time_gte (datetime.datetime | Unset):
        removed_data_time_hour (float | Unset):
        removed_data_time_icontains (datetime.datetime | Unset):
        removed_data_time_iendswith (datetime.datetime | Unset):
        removed_data_time_iexact (datetime.datetime | Unset):
        removed_data_time_in (list[datetime.datetime] | Unset):
        removed_data_time_iregex (datetime.datetime | Unset):
        removed_data_time_isnull (bool | Unset):
        removed_data_time_iso_week_day (float | Unset):
        removed_data_time_iso_year (float | Unset):
        removed_data_time_istartswith (datetime.datetime | Unset):
        removed_data_time_lt (datetime.datetime | Unset):
        removed_data_time_lte (datetime.datetime | Unset):
        removed_data_time_minute (float | Unset):
        removed_data_time_month (float | Unset):
        removed_data_time_quarter (float | Unset):
        removed_data_time_range (list[datetime.datetime] | Unset):
        removed_data_time_regex (datetime.datetime | Unset):
        removed_data_time_second (float | Unset):
        removed_data_time_startswith (datetime.datetime | Unset):
        removed_data_time_time (str | Unset):
        removed_data_time_week (float | Unset):
        removed_data_time_week_day (float | Unset):
        removed_data_time_year (float | Unset):
        resolution (str | Unset):
        resolution_contains (str | Unset):
        resolution_endswith (str | Unset):
        resolution_gt (str | Unset):
        resolution_gte (str | Unset):
        resolution_icontains (str | Unset):
        resolution_iendswith (str | Unset):
        resolution_iexact (str | Unset):
        resolution_in (list[str] | Unset):
        resolution_iregex (str | Unset):
        resolution_isnull (bool | Unset):
        resolution_istartswith (str | Unset):
        resolution_lt (str | Unset):
        resolution_lte (str | Unset):
        resolution_range (list[str] | Unset):
        resolution_regex (str | Unset):
        resolution_startswith (str | Unset):
        result_quality (int | Unset):
        result_quality_date (datetime.date | Unset):
        result_quality_date_gt (datetime.date | Unset):
        result_quality_date_gte (datetime.date | Unset):
        result_quality_date_lt (datetime.date | Unset):
        result_quality_date_lte (datetime.date | Unset):
        result_quality_date_range (list[datetime.date] | Unset):
        result_quality_explanation (str | Unset):
        result_quality_explanation_contains (str | Unset):
        result_quality_gt (int | Unset):
        result_quality_gte (int | Unset):
        result_quality_in (list[int] | Unset):
        result_quality_isnull (bool | Unset):
        result_quality_lt (int | Unset):
        result_quality_lte (int | Unset):
        result_quality_ob_id (int | Unset):
        result_quality_ob_id_in (list[int] | Unset):
        result_quality_passes_test (bool | Unset):
        result_quality_result_title (str | Unset):
        result_quality_result_title_contains (str | Unset):
        result_field (int | Unset):
        result_field_data_path (str | Unset):
        result_field_data_path_contains (str | Unset):
        result_field_data_path_startswith (str | Unset):
        result_field_file_format (str | Unset):
        result_field_file_format_contains (str | Unset):
        result_field_gt (int | Unset):
        result_field_gte (int | Unset):
        result_field_in (list[int] | Unset):
        result_field_isnull (bool | Unset):
        result_field_lt (int | Unset):
        result_field_lte (int | Unset):
        result_field_storage_location (ObservationsListStorageLocation | Unset):
        result_field_storage_status (ObservationsListStorageStatus | Unset):
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
        status (ObservationsListDataStatus | Unset):
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
        submission_user_id (str | Unset):
        submission_user_id_contains (str | Unset):
        submission_user_id_endswith (str | Unset):
        submission_user_id_gt (str | Unset):
        submission_user_id_gte (str | Unset):
        submission_user_id_icontains (str | Unset):
        submission_user_id_iendswith (str | Unset):
        submission_user_id_iexact (str | Unset):
        submission_user_id_in (list[str] | Unset):
        submission_user_id_iregex (str | Unset):
        submission_user_id_isnull (bool | Unset):
        submission_user_id_istartswith (str | Unset):
        submission_user_id_lt (str | Unset):
        submission_user_id_lte (str | Unset):
        submission_user_id_range (list[str] | Unset):
        submission_user_id_regex (str | Unset):
        submission_user_id_startswith (str | Unset):
        time_period (int | Unset):
        time_period_end_time (datetime.datetime | Unset):
        time_period_end_time_gt (datetime.datetime | Unset):
        time_period_end_time_gte (datetime.datetime | Unset):
        time_period_end_time_lt (datetime.datetime | Unset):
        time_period_end_time_lte (datetime.datetime | Unset):
        time_period_end_time_range (list[datetime.datetime] | Unset):
        time_period_gt (int | Unset):
        time_period_gte (int | Unset):
        time_period_in (list[int] | Unset):
        time_period_isnull (bool | Unset):
        time_period_lt (int | Unset):
        time_period_lte (int | Unset):
        time_period_ob_id (int | Unset):
        time_period_ob_id_in (list[int] | Unset):
        time_period_start_time (datetime.datetime | Unset):
        time_period_start_time_gt (datetime.datetime | Unset):
        time_period_start_time_gte (datetime.datetime | Unset):
        time_period_start_time_lt (datetime.datetime | Unset):
        time_period_start_time_lte (datetime.datetime | Unset):
        time_period_start_time_range (list[datetime.datetime] | Unset):
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
        update_frequency (ObservationsListDataUpdateFrequency | Unset):
        update_frequency_contains (str | Unset):
        update_frequency_endswith (str | Unset):
        update_frequency_gt (str | Unset):
        update_frequency_gte (str | Unset):
        update_frequency_icontains (str | Unset):
        update_frequency_iendswith (str | Unset):
        update_frequency_iexact (str | Unset):
        update_frequency_in (list[str] | Unset):
        update_frequency_iregex (str | Unset):
        update_frequency_isnull (bool | Unset):
        update_frequency_istartswith (str | Unset):
        update_frequency_lt (str | Unset):
        update_frequency_lte (str | Unset):
        update_frequency_range (list[str] | Unset):
        update_frequency_regex (str | Unset):
        update_frequency_startswith (str | Unset):
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
        valid_time_period (int | Unset):
        valid_time_period_gt (int | Unset):
        valid_time_period_gte (int | Unset):
        valid_time_period_in (list[int] | Unset):
        valid_time_period_isnull (bool | Unset):
        valid_time_period_lt (int | Unset):
        valid_time_period_lte (int | Unset):
        vertical_extent (int | Unset):
        vertical_extent_gt (int | Unset):
        vertical_extent_gte (int | Unset):
        vertical_extent_in (list[int] | Unset):
        vertical_extent_isnull (bool | Unset):
        vertical_extent_lt (int | Unset):
        vertical_extent_lte (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedObservationReadList
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
            creation_date=creation_date,
            creation_date_contained_by=creation_date_contained_by,
            creation_date_contains=creation_date_contains,
            creation_date_date=creation_date_date,
            creation_date_day=creation_date_day,
            creation_date_endswith=creation_date_endswith,
            creation_date_gt=creation_date_gt,
            creation_date_gte=creation_date_gte,
            creation_date_hour=creation_date_hour,
            creation_date_icontains=creation_date_icontains,
            creation_date_iendswith=creation_date_iendswith,
            creation_date_iexact=creation_date_iexact,
            creation_date_in=creation_date_in,
            creation_date_iregex=creation_date_iregex,
            creation_date_isnull=creation_date_isnull,
            creation_date_iso_week_day=creation_date_iso_week_day,
            creation_date_iso_year=creation_date_iso_year,
            creation_date_istartswith=creation_date_istartswith,
            creation_date_lt=creation_date_lt,
            creation_date_lte=creation_date_lte,
            creation_date_minute=creation_date_minute,
            creation_date_month=creation_date_month,
            creation_date_quarter=creation_date_quarter,
            creation_date_range=creation_date_range,
            creation_date_regex=creation_date_regex,
            creation_date_second=creation_date_second,
            creation_date_startswith=creation_date_startswith,
            creation_date_time=creation_date_time,
            creation_date_week=creation_date_week,
            creation_date_week_day=creation_date_week_day,
            creation_date_year=creation_date_year,
            data_lineage=data_lineage,
            data_lineage_contains=data_lineage_contains,
            data_lineage_endswith=data_lineage_endswith,
            data_lineage_gt=data_lineage_gt,
            data_lineage_gte=data_lineage_gte,
            data_lineage_icontains=data_lineage_icontains,
            data_lineage_iendswith=data_lineage_iendswith,
            data_lineage_iexact=data_lineage_iexact,
            data_lineage_in=data_lineage_in,
            data_lineage_iregex=data_lineage_iregex,
            data_lineage_isnull=data_lineage_isnull,
            data_lineage_istartswith=data_lineage_istartswith,
            data_lineage_lt=data_lineage_lt,
            data_lineage_lte=data_lineage_lte,
            data_lineage_range=data_lineage_range,
            data_lineage_regex=data_lineage_regex,
            data_lineage_startswith=data_lineage_startswith,
            data_published_time=data_published_time,
            data_published_time_contained_by=data_published_time_contained_by,
            data_published_time_contains=data_published_time_contains,
            data_published_time_date=data_published_time_date,
            data_published_time_day=data_published_time_day,
            data_published_time_endswith=data_published_time_endswith,
            data_published_time_gt=data_published_time_gt,
            data_published_time_gte=data_published_time_gte,
            data_published_time_hour=data_published_time_hour,
            data_published_time_icontains=data_published_time_icontains,
            data_published_time_iendswith=data_published_time_iendswith,
            data_published_time_iexact=data_published_time_iexact,
            data_published_time_in=data_published_time_in,
            data_published_time_iregex=data_published_time_iregex,
            data_published_time_isnull=data_published_time_isnull,
            data_published_time_iso_week_day=data_published_time_iso_week_day,
            data_published_time_iso_year=data_published_time_iso_year,
            data_published_time_istartswith=data_published_time_istartswith,
            data_published_time_lt=data_published_time_lt,
            data_published_time_lte=data_published_time_lte,
            data_published_time_minute=data_published_time_minute,
            data_published_time_month=data_published_time_month,
            data_published_time_quarter=data_published_time_quarter,
            data_published_time_range=data_published_time_range,
            data_published_time_regex=data_published_time_regex,
            data_published_time_second=data_published_time_second,
            data_published_time_startswith=data_published_time_startswith,
            data_published_time_time=data_published_time_time,
            data_published_time_week=data_published_time_week,
            data_published_time_week_day=data_published_time_week_day,
            data_published_time_year=data_published_time_year,
            discovery_keywords_name=discovery_keywords_name,
            discovery_keywords_name_contains=discovery_keywords_name_contains,
            doi_published_time=doi_published_time,
            doi_published_time_contained_by=doi_published_time_contained_by,
            doi_published_time_contains=doi_published_time_contains,
            doi_published_time_date=doi_published_time_date,
            doi_published_time_day=doi_published_time_day,
            doi_published_time_endswith=doi_published_time_endswith,
            doi_published_time_gt=doi_published_time_gt,
            doi_published_time_gte=doi_published_time_gte,
            doi_published_time_hour=doi_published_time_hour,
            doi_published_time_icontains=doi_published_time_icontains,
            doi_published_time_iendswith=doi_published_time_iendswith,
            doi_published_time_iexact=doi_published_time_iexact,
            doi_published_time_in=doi_published_time_in,
            doi_published_time_iregex=doi_published_time_iregex,
            doi_published_time_isnull=doi_published_time_isnull,
            doi_published_time_iso_week_day=doi_published_time_iso_week_day,
            doi_published_time_iso_year=doi_published_time_iso_year,
            doi_published_time_istartswith=doi_published_time_istartswith,
            doi_published_time_lt=doi_published_time_lt,
            doi_published_time_lte=doi_published_time_lte,
            doi_published_time_minute=doi_published_time_minute,
            doi_published_time_month=doi_published_time_month,
            doi_published_time_quarter=doi_published_time_quarter,
            doi_published_time_range=doi_published_time_range,
            doi_published_time_regex=doi_published_time_regex,
            doi_published_time_second=doi_published_time_second,
            doi_published_time_startswith=doi_published_time_startswith,
            doi_published_time_time=doi_published_time_time,
            doi_published_time_week=doi_published_time_week,
            doi_published_time_week_day=doi_published_time_week_day,
            doi_published_time_year=doi_published_time_year,
            dont_harvest_from_projects=dont_harvest_from_projects,
            dont_harvest_from_projects_contains=dont_harvest_from_projects_contains,
            dont_harvest_from_projects_endswith=dont_harvest_from_projects_endswith,
            dont_harvest_from_projects_gt=dont_harvest_from_projects_gt,
            dont_harvest_from_projects_gte=dont_harvest_from_projects_gte,
            dont_harvest_from_projects_icontains=dont_harvest_from_projects_icontains,
            dont_harvest_from_projects_iendswith=dont_harvest_from_projects_iendswith,
            dont_harvest_from_projects_iexact=dont_harvest_from_projects_iexact,
            dont_harvest_from_projects_in=dont_harvest_from_projects_in,
            dont_harvest_from_projects_iregex=dont_harvest_from_projects_iregex,
            dont_harvest_from_projects_isnull=dont_harvest_from_projects_isnull,
            dont_harvest_from_projects_istartswith=dont_harvest_from_projects_istartswith,
            dont_harvest_from_projects_lt=dont_harvest_from_projects_lt,
            dont_harvest_from_projects_lte=dont_harvest_from_projects_lte,
            dont_harvest_from_projects_range=dont_harvest_from_projects_range,
            dont_harvest_from_projects_regex=dont_harvest_from_projects_regex,
            dont_harvest_from_projects_startswith=dont_harvest_from_projects_startswith,
            feature_of_interest=feature_of_interest,
            feature_of_interest_contains=feature_of_interest_contains,
            feature_of_interest_endswith=feature_of_interest_endswith,
            feature_of_interest_gt=feature_of_interest_gt,
            feature_of_interest_gte=feature_of_interest_gte,
            feature_of_interest_icontains=feature_of_interest_icontains,
            feature_of_interest_iendswith=feature_of_interest_iendswith,
            feature_of_interest_iexact=feature_of_interest_iexact,
            feature_of_interest_in=feature_of_interest_in,
            feature_of_interest_iregex=feature_of_interest_iregex,
            feature_of_interest_isnull=feature_of_interest_isnull,
            feature_of_interest_istartswith=feature_of_interest_istartswith,
            feature_of_interest_lt=feature_of_interest_lt,
            feature_of_interest_lte=feature_of_interest_lte,
            feature_of_interest_range=feature_of_interest_range,
            feature_of_interest_regex=feature_of_interest_regex,
            feature_of_interest_startswith=feature_of_interest_startswith,
            geographic_extent=geographic_extent,
            geographic_extent_east_bound_longitude=geographic_extent_east_bound_longitude,
            geographic_extent_east_bound_longitude_gt=geographic_extent_east_bound_longitude_gt,
            geographic_extent_east_bound_longitude_gte=geographic_extent_east_bound_longitude_gte,
            geographic_extent_east_bound_longitude_lt=geographic_extent_east_bound_longitude_lt,
            geographic_extent_east_bound_longitude_lte=geographic_extent_east_bound_longitude_lte,
            geographic_extent_east_bound_longitude_range=geographic_extent_east_bound_longitude_range,
            geographic_extent_gt=geographic_extent_gt,
            geographic_extent_gte=geographic_extent_gte,
            geographic_extent_in=geographic_extent_in,
            geographic_extent_isnull=geographic_extent_isnull,
            geographic_extent_lt=geographic_extent_lt,
            geographic_extent_lte=geographic_extent_lte,
            geographic_extent_north_bound_latitude=geographic_extent_north_bound_latitude,
            geographic_extent_north_bound_latitude_gt=geographic_extent_north_bound_latitude_gt,
            geographic_extent_north_bound_latitude_gte=geographic_extent_north_bound_latitude_gte,
            geographic_extent_north_bound_latitude_lt=geographic_extent_north_bound_latitude_lt,
            geographic_extent_north_bound_latitude_lte=geographic_extent_north_bound_latitude_lte,
            geographic_extent_north_bound_latitude_range=geographic_extent_north_bound_latitude_range,
            geographic_extent_ob_id=geographic_extent_ob_id,
            geographic_extent_ob_id_in=geographic_extent_ob_id_in,
            geographic_extent_south_bound_latitude=geographic_extent_south_bound_latitude,
            geographic_extent_south_bound_latitude_gt=geographic_extent_south_bound_latitude_gt,
            geographic_extent_south_bound_latitude_gte=geographic_extent_south_bound_latitude_gte,
            geographic_extent_south_bound_latitude_lt=geographic_extent_south_bound_latitude_lt,
            geographic_extent_south_bound_latitude_lte=geographic_extent_south_bound_latitude_lte,
            geographic_extent_south_bound_latitude_range=geographic_extent_south_bound_latitude_range,
            geographic_extent_west_bound_longitude=geographic_extent_west_bound_longitude,
            geographic_extent_west_bound_longitude_gt=geographic_extent_west_bound_longitude_gt,
            geographic_extent_west_bound_longitude_gte=geographic_extent_west_bound_longitude_gte,
            geographic_extent_west_bound_longitude_lt=geographic_extent_west_bound_longitude_lt,
            geographic_extent_west_bound_longitude_lte=geographic_extent_west_bound_longitude_lte,
            geographic_extent_west_bound_longitude_range=geographic_extent_west_bound_longitude_range,
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
            language=language,
            language_contains=language_contains,
            language_endswith=language_endswith,
            language_gt=language_gt,
            language_gte=language_gte,
            language_icontains=language_icontains,
            language_iendswith=language_iendswith,
            language_iexact=language_iexact,
            language_in=language_in,
            language_iregex=language_iregex,
            language_isnull=language_isnull,
            language_istartswith=language_istartswith,
            language_lt=language_lt,
            language_lte=language_lte,
            language_range=language_range,
            language_regex=language_regex,
            language_startswith=language_startswith,
            last_updated_date=last_updated_date,
            last_updated_date_contained_by=last_updated_date_contained_by,
            last_updated_date_contains=last_updated_date_contains,
            last_updated_date_date=last_updated_date_date,
            last_updated_date_day=last_updated_date_day,
            last_updated_date_endswith=last_updated_date_endswith,
            last_updated_date_gt=last_updated_date_gt,
            last_updated_date_gte=last_updated_date_gte,
            last_updated_date_hour=last_updated_date_hour,
            last_updated_date_icontains=last_updated_date_icontains,
            last_updated_date_iendswith=last_updated_date_iendswith,
            last_updated_date_iexact=last_updated_date_iexact,
            last_updated_date_in=last_updated_date_in,
            last_updated_date_iregex=last_updated_date_iregex,
            last_updated_date_isnull=last_updated_date_isnull,
            last_updated_date_iso_week_day=last_updated_date_iso_week_day,
            last_updated_date_iso_year=last_updated_date_iso_year,
            last_updated_date_istartswith=last_updated_date_istartswith,
            last_updated_date_lt=last_updated_date_lt,
            last_updated_date_lte=last_updated_date_lte,
            last_updated_date_minute=last_updated_date_minute,
            last_updated_date_month=last_updated_date_month,
            last_updated_date_quarter=last_updated_date_quarter,
            last_updated_date_range=last_updated_date_range,
            last_updated_date_regex=last_updated_date_regex,
            last_updated_date_second=last_updated_date_second,
            last_updated_date_startswith=last_updated_date_startswith,
            last_updated_date_time=last_updated_date_time,
            last_updated_date_week=last_updated_date_week,
            last_updated_date_week_day=last_updated_date_week_day,
            last_updated_date_year=last_updated_date_year,
            latest_data_update_time=latest_data_update_time,
            latest_data_update_time_contained_by=latest_data_update_time_contained_by,
            latest_data_update_time_contains=latest_data_update_time_contains,
            latest_data_update_time_date=latest_data_update_time_date,
            latest_data_update_time_day=latest_data_update_time_day,
            latest_data_update_time_endswith=latest_data_update_time_endswith,
            latest_data_update_time_gt=latest_data_update_time_gt,
            latest_data_update_time_gte=latest_data_update_time_gte,
            latest_data_update_time_hour=latest_data_update_time_hour,
            latest_data_update_time_icontains=latest_data_update_time_icontains,
            latest_data_update_time_iendswith=latest_data_update_time_iendswith,
            latest_data_update_time_iexact=latest_data_update_time_iexact,
            latest_data_update_time_in=latest_data_update_time_in,
            latest_data_update_time_iregex=latest_data_update_time_iregex,
            latest_data_update_time_isnull=latest_data_update_time_isnull,
            latest_data_update_time_iso_week_day=latest_data_update_time_iso_week_day,
            latest_data_update_time_iso_year=latest_data_update_time_iso_year,
            latest_data_update_time_istartswith=latest_data_update_time_istartswith,
            latest_data_update_time_lt=latest_data_update_time_lt,
            latest_data_update_time_lte=latest_data_update_time_lte,
            latest_data_update_time_minute=latest_data_update_time_minute,
            latest_data_update_time_month=latest_data_update_time_month,
            latest_data_update_time_quarter=latest_data_update_time_quarter,
            latest_data_update_time_range=latest_data_update_time_range,
            latest_data_update_time_regex=latest_data_update_time_regex,
            latest_data_update_time_second=latest_data_update_time_second,
            latest_data_update_time_startswith=latest_data_update_time_startswith,
            latest_data_update_time_time=latest_data_update_time_time,
            latest_data_update_time_week=latest_data_update_time_week,
            latest_data_update_time_week_day=latest_data_update_time_week_day,
            latest_data_update_time_year=latest_data_update_time_year,
            limit=limit,
            non_geographic_flag=non_geographic_flag,
            non_geographic_flag_contains=non_geographic_flag_contains,
            non_geographic_flag_endswith=non_geographic_flag_endswith,
            non_geographic_flag_gt=non_geographic_flag_gt,
            non_geographic_flag_gte=non_geographic_flag_gte,
            non_geographic_flag_icontains=non_geographic_flag_icontains,
            non_geographic_flag_iendswith=non_geographic_flag_iendswith,
            non_geographic_flag_iexact=non_geographic_flag_iexact,
            non_geographic_flag_in=non_geographic_flag_in,
            non_geographic_flag_iregex=non_geographic_flag_iregex,
            non_geographic_flag_isnull=non_geographic_flag_isnull,
            non_geographic_flag_istartswith=non_geographic_flag_istartswith,
            non_geographic_flag_lt=non_geographic_flag_lt,
            non_geographic_flag_lte=non_geographic_flag_lte,
            non_geographic_flag_range=non_geographic_flag_range,
            non_geographic_flag_regex=non_geographic_flag_regex,
            non_geographic_flag_startswith=non_geographic_flag_startswith,
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
            permissions_access_category=permissions_access_category,
            permissions_access_category_in=permissions_access_category_in,
            permissions_access_roles=permissions_access_roles,
            permissions_access_roles_in=permissions_access_roles_in,
            procedure_acquisition=procedure_acquisition,
            procedure_acquisition_gt=procedure_acquisition_gt,
            procedure_acquisition_gte=procedure_acquisition_gte,
            procedure_acquisition_in=procedure_acquisition_in,
            procedure_acquisition_isnull=procedure_acquisition_isnull,
            procedure_acquisition_lt=procedure_acquisition_lt,
            procedure_acquisition_lte=procedure_acquisition_lte,
            procedure_acquisition_ob_id=procedure_acquisition_ob_id,
            procedure_acquisition_ob_id_in=procedure_acquisition_ob_id_in,
            procedure_acquisition_uuid=procedure_acquisition_uuid,
            procedure_acquisition_uuid_in=procedure_acquisition_uuid_in,
            procedure_composite_process=procedure_composite_process,
            procedure_composite_process_gt=procedure_composite_process_gt,
            procedure_composite_process_gte=procedure_composite_process_gte,
            procedure_composite_process_in=procedure_composite_process_in,
            procedure_composite_process_isnull=procedure_composite_process_isnull,
            procedure_composite_process_lt=procedure_composite_process_lt,
            procedure_composite_process_lte=procedure_composite_process_lte,
            procedure_computation=procedure_computation,
            procedure_computation_gt=procedure_computation_gt,
            procedure_computation_gte=procedure_computation_gte,
            procedure_computation_in=procedure_computation_in,
            procedure_computation_isnull=procedure_computation_isnull,
            procedure_computation_lt=procedure_computation_lt,
            procedure_computation_lte=procedure_computation_lte,
            procedure_description=procedure_description,
            procedure_description_contains=procedure_description_contains,
            procedure_description_endswith=procedure_description_endswith,
            procedure_description_gt=procedure_description_gt,
            procedure_description_gte=procedure_description_gte,
            procedure_description_icontains=procedure_description_icontains,
            procedure_description_iendswith=procedure_description_iendswith,
            procedure_description_iexact=procedure_description_iexact,
            procedure_description_in=procedure_description_in,
            procedure_description_iregex=procedure_description_iregex,
            procedure_description_isnull=procedure_description_isnull,
            procedure_description_istartswith=procedure_description_istartswith,
            procedure_description_lt=procedure_description_lt,
            procedure_description_lte=procedure_description_lte,
            procedure_description_range=procedure_description_range,
            procedure_description_regex=procedure_description_regex,
            procedure_description_startswith=procedure_description_startswith,
            projects_ob_id=projects_ob_id,
            projects_ob_id_in=projects_ob_id_in,
            projects_uuid=projects_uuid,
            projects_uuid_in=projects_uuid_in,
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
            removed_data_reason=removed_data_reason,
            removed_data_reason_contains=removed_data_reason_contains,
            removed_data_reason_endswith=removed_data_reason_endswith,
            removed_data_reason_gt=removed_data_reason_gt,
            removed_data_reason_gte=removed_data_reason_gte,
            removed_data_reason_icontains=removed_data_reason_icontains,
            removed_data_reason_iendswith=removed_data_reason_iendswith,
            removed_data_reason_iexact=removed_data_reason_iexact,
            removed_data_reason_in=removed_data_reason_in,
            removed_data_reason_iregex=removed_data_reason_iregex,
            removed_data_reason_isnull=removed_data_reason_isnull,
            removed_data_reason_istartswith=removed_data_reason_istartswith,
            removed_data_reason_lt=removed_data_reason_lt,
            removed_data_reason_lte=removed_data_reason_lte,
            removed_data_reason_range=removed_data_reason_range,
            removed_data_reason_regex=removed_data_reason_regex,
            removed_data_reason_startswith=removed_data_reason_startswith,
            removed_data_time=removed_data_time,
            removed_data_time_contained_by=removed_data_time_contained_by,
            removed_data_time_contains=removed_data_time_contains,
            removed_data_time_date=removed_data_time_date,
            removed_data_time_day=removed_data_time_day,
            removed_data_time_endswith=removed_data_time_endswith,
            removed_data_time_gt=removed_data_time_gt,
            removed_data_time_gte=removed_data_time_gte,
            removed_data_time_hour=removed_data_time_hour,
            removed_data_time_icontains=removed_data_time_icontains,
            removed_data_time_iendswith=removed_data_time_iendswith,
            removed_data_time_iexact=removed_data_time_iexact,
            removed_data_time_in=removed_data_time_in,
            removed_data_time_iregex=removed_data_time_iregex,
            removed_data_time_isnull=removed_data_time_isnull,
            removed_data_time_iso_week_day=removed_data_time_iso_week_day,
            removed_data_time_iso_year=removed_data_time_iso_year,
            removed_data_time_istartswith=removed_data_time_istartswith,
            removed_data_time_lt=removed_data_time_lt,
            removed_data_time_lte=removed_data_time_lte,
            removed_data_time_minute=removed_data_time_minute,
            removed_data_time_month=removed_data_time_month,
            removed_data_time_quarter=removed_data_time_quarter,
            removed_data_time_range=removed_data_time_range,
            removed_data_time_regex=removed_data_time_regex,
            removed_data_time_second=removed_data_time_second,
            removed_data_time_startswith=removed_data_time_startswith,
            removed_data_time_time=removed_data_time_time,
            removed_data_time_week=removed_data_time_week,
            removed_data_time_week_day=removed_data_time_week_day,
            removed_data_time_year=removed_data_time_year,
            resolution=resolution,
            resolution_contains=resolution_contains,
            resolution_endswith=resolution_endswith,
            resolution_gt=resolution_gt,
            resolution_gte=resolution_gte,
            resolution_icontains=resolution_icontains,
            resolution_iendswith=resolution_iendswith,
            resolution_iexact=resolution_iexact,
            resolution_in=resolution_in,
            resolution_iregex=resolution_iregex,
            resolution_isnull=resolution_isnull,
            resolution_istartswith=resolution_istartswith,
            resolution_lt=resolution_lt,
            resolution_lte=resolution_lte,
            resolution_range=resolution_range,
            resolution_regex=resolution_regex,
            resolution_startswith=resolution_startswith,
            result_quality=result_quality,
            result_quality_date=result_quality_date,
            result_quality_date_gt=result_quality_date_gt,
            result_quality_date_gte=result_quality_date_gte,
            result_quality_date_lt=result_quality_date_lt,
            result_quality_date_lte=result_quality_date_lte,
            result_quality_date_range=result_quality_date_range,
            result_quality_explanation=result_quality_explanation,
            result_quality_explanation_contains=result_quality_explanation_contains,
            result_quality_gt=result_quality_gt,
            result_quality_gte=result_quality_gte,
            result_quality_in=result_quality_in,
            result_quality_isnull=result_quality_isnull,
            result_quality_lt=result_quality_lt,
            result_quality_lte=result_quality_lte,
            result_quality_ob_id=result_quality_ob_id,
            result_quality_ob_id_in=result_quality_ob_id_in,
            result_quality_passes_test=result_quality_passes_test,
            result_quality_result_title=result_quality_result_title,
            result_quality_result_title_contains=result_quality_result_title_contains,
            result_field=result_field,
            result_field_data_path=result_field_data_path,
            result_field_data_path_contains=result_field_data_path_contains,
            result_field_data_path_startswith=result_field_data_path_startswith,
            result_field_file_format=result_field_file_format,
            result_field_file_format_contains=result_field_file_format_contains,
            result_field_gt=result_field_gt,
            result_field_gte=result_field_gte,
            result_field_in=result_field_in,
            result_field_isnull=result_field_isnull,
            result_field_lt=result_field_lt,
            result_field_lte=result_field_lte,
            result_field_storage_location=result_field_storage_location,
            result_field_storage_status=result_field_storage_status,
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
            submission_user_id=submission_user_id,
            submission_user_id_contains=submission_user_id_contains,
            submission_user_id_endswith=submission_user_id_endswith,
            submission_user_id_gt=submission_user_id_gt,
            submission_user_id_gte=submission_user_id_gte,
            submission_user_id_icontains=submission_user_id_icontains,
            submission_user_id_iendswith=submission_user_id_iendswith,
            submission_user_id_iexact=submission_user_id_iexact,
            submission_user_id_in=submission_user_id_in,
            submission_user_id_iregex=submission_user_id_iregex,
            submission_user_id_isnull=submission_user_id_isnull,
            submission_user_id_istartswith=submission_user_id_istartswith,
            submission_user_id_lt=submission_user_id_lt,
            submission_user_id_lte=submission_user_id_lte,
            submission_user_id_range=submission_user_id_range,
            submission_user_id_regex=submission_user_id_regex,
            submission_user_id_startswith=submission_user_id_startswith,
            time_period=time_period,
            time_period_end_time=time_period_end_time,
            time_period_end_time_gt=time_period_end_time_gt,
            time_period_end_time_gte=time_period_end_time_gte,
            time_period_end_time_lt=time_period_end_time_lt,
            time_period_end_time_lte=time_period_end_time_lte,
            time_period_end_time_range=time_period_end_time_range,
            time_period_gt=time_period_gt,
            time_period_gte=time_period_gte,
            time_period_in=time_period_in,
            time_period_isnull=time_period_isnull,
            time_period_lt=time_period_lt,
            time_period_lte=time_period_lte,
            time_period_ob_id=time_period_ob_id,
            time_period_ob_id_in=time_period_ob_id_in,
            time_period_start_time=time_period_start_time,
            time_period_start_time_gt=time_period_start_time_gt,
            time_period_start_time_gte=time_period_start_time_gte,
            time_period_start_time_lt=time_period_start_time_lt,
            time_period_start_time_lte=time_period_start_time_lte,
            time_period_start_time_range=time_period_start_time_range,
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
            update_frequency=update_frequency,
            update_frequency_contains=update_frequency_contains,
            update_frequency_endswith=update_frequency_endswith,
            update_frequency_gt=update_frequency_gt,
            update_frequency_gte=update_frequency_gte,
            update_frequency_icontains=update_frequency_icontains,
            update_frequency_iendswith=update_frequency_iendswith,
            update_frequency_iexact=update_frequency_iexact,
            update_frequency_in=update_frequency_in,
            update_frequency_iregex=update_frequency_iregex,
            update_frequency_isnull=update_frequency_isnull,
            update_frequency_istartswith=update_frequency_istartswith,
            update_frequency_lt=update_frequency_lt,
            update_frequency_lte=update_frequency_lte,
            update_frequency_range=update_frequency_range,
            update_frequency_regex=update_frequency_regex,
            update_frequency_startswith=update_frequency_startswith,
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
            valid_time_period=valid_time_period,
            valid_time_period_gt=valid_time_period_gt,
            valid_time_period_gte=valid_time_period_gte,
            valid_time_period_in=valid_time_period_in,
            valid_time_period_isnull=valid_time_period_isnull,
            valid_time_period_lt=valid_time_period_lt,
            valid_time_period_lte=valid_time_period_lte,
            vertical_extent=vertical_extent,
            vertical_extent_gt=vertical_extent_gt,
            vertical_extent_gte=vertical_extent_gte,
            vertical_extent_in=vertical_extent_in,
            vertical_extent_isnull=vertical_extent_isnull,
            vertical_extent_lt=vertical_extent_lt,
            vertical_extent_lte=vertical_extent_lte,
        )
    ).parsed
