import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.language_enum import LanguageEnum
from ..models.publication_state_cbb_enum import PublicationStateCbbEnum
from ..models.status_enum import StatusEnum
from ..models.update_frequency_enum import UpdateFrequencyEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedObservationWriteRequest")


@_attrs_define
class PatchedObservationWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            title (Union[Unset, str]):
            abstract (Union[Unset, str]):
            creation_date (Union[None, Unset, datetime.datetime]):
            last_updated_date (Union[None, Unset, datetime.datetime]):
            latest_data_update_time (Union[None, Unset, datetime.datetime]):
            update_frequency (Union[BlankEnum, Unset, UpdateFrequencyEnum]):
            data_lineage (Union[Unset, str]):
            removed_data_reason (Union[Unset, str]):
            keywords (Union[Unset, str]):
            publication_state (Union[BlankEnum, PublicationStateCbbEnum, Unset]):
            non_geographic_flag (Union[Unset, bool]):
            dont_harvest_from_projects (Union[Unset, bool]):
            geographic_extent (Union[None, Unset, int]):
            language (Union[BlankEnum, LanguageEnum, Unset]):
            resolution (Union[Unset, str]):
            status (Union[Unset, StatusEnum]): * `planned` - Planned (pre)
                * `required` - Required (pre)
                * `underDevelopment` - Under Development (pre)
                * `pending` - Pending (pre)
                * `tentative` - Tentative (pre)
                * `withdrawn` - Withdrawn (pre)
                * `ongoing` - Ongoing (live)
                * `completed` - Completed (live)
                * `final` - Final (live)
                * `superseded` - Superseded (past)
                * `obsolete` - Obsolete (past)
                * `historicalArchive` - Historical Archive (past)
                * `retired` - Retired (past)
                * `deprecated` - Deprecated (past)
            vertical_extent (Union[None, Unset, int]):
            result_field (Union[None, Unset, int]):
            time_period (Union[None, Unset, int]):
            result_quality (Union[None, Unset, int]):
            data_published_time (Union[None, Unset, datetime.datetime]):
            doi_published_time (Union[None, Unset, datetime.datetime]):
            removed_data_time (Union[None, Unset, datetime.datetime]):
            valid_time_period (Union[None, Unset, int]):
            procedure_acquisition (Union[None, Unset, int]):
            procedure_computation (Union[None, Unset, int]):
            procedure_composite_process (Union[None, Unset, int]):
            image_details (Union[Unset, list[int]]):
            discovery_keywords (Union[Unset, list[int]]):
            permissions (Union[Unset, list[int]]):
            projects (Union[Unset, list[int]]):
            inspire_theme (Union[Unset, list[int]]):
            topic_category (Union[Unset, list[int]]):
            vocabulary_keywords (Union[Unset, list[int]]):
    """

    title: Union[Unset, str] = UNSET
    abstract: Union[Unset, str] = UNSET
    creation_date: Union[None, Unset, datetime.datetime] = UNSET
    last_updated_date: Union[None, Unset, datetime.datetime] = UNSET
    latest_data_update_time: Union[None, Unset, datetime.datetime] = UNSET
    update_frequency: Union[BlankEnum, Unset, UpdateFrequencyEnum] = UNSET
    data_lineage: Union[Unset, str] = UNSET
    removed_data_reason: Union[Unset, str] = UNSET
    keywords: Union[Unset, str] = UNSET
    publication_state: Union[BlankEnum, PublicationStateCbbEnum, Unset] = UNSET
    non_geographic_flag: Union[Unset, bool] = UNSET
    dont_harvest_from_projects: Union[Unset, bool] = UNSET
    geographic_extent: Union[None, Unset, int] = UNSET
    language: Union[BlankEnum, LanguageEnum, Unset] = UNSET
    resolution: Union[Unset, str] = UNSET
    status: Union[Unset, StatusEnum] = UNSET
    vertical_extent: Union[None, Unset, int] = UNSET
    result_field: Union[None, Unset, int] = UNSET
    time_period: Union[None, Unset, int] = UNSET
    result_quality: Union[None, Unset, int] = UNSET
    data_published_time: Union[None, Unset, datetime.datetime] = UNSET
    doi_published_time: Union[None, Unset, datetime.datetime] = UNSET
    removed_data_time: Union[None, Unset, datetime.datetime] = UNSET
    valid_time_period: Union[None, Unset, int] = UNSET
    procedure_acquisition: Union[None, Unset, int] = UNSET
    procedure_computation: Union[None, Unset, int] = UNSET
    procedure_composite_process: Union[None, Unset, int] = UNSET
    image_details: Union[Unset, list[int]] = UNSET
    discovery_keywords: Union[Unset, list[int]] = UNSET
    permissions: Union[Unset, list[int]] = UNSET
    projects: Union[Unset, list[int]] = UNSET
    inspire_theme: Union[Unset, list[int]] = UNSET
    topic_category: Union[Unset, list[int]] = UNSET
    vocabulary_keywords: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        abstract = self.abstract

        creation_date: Union[None, Unset, str]
        if isinstance(self.creation_date, Unset):
            creation_date = UNSET
        elif isinstance(self.creation_date, datetime.datetime):
            creation_date = self.creation_date.isoformat()
        else:
            creation_date = self.creation_date

        last_updated_date: Union[None, Unset, str]
        if isinstance(self.last_updated_date, Unset):
            last_updated_date = UNSET
        elif isinstance(self.last_updated_date, datetime.datetime):
            last_updated_date = self.last_updated_date.isoformat()
        else:
            last_updated_date = self.last_updated_date

        latest_data_update_time: Union[None, Unset, str]
        if isinstance(self.latest_data_update_time, Unset):
            latest_data_update_time = UNSET
        elif isinstance(self.latest_data_update_time, datetime.datetime):
            latest_data_update_time = self.latest_data_update_time.isoformat()
        else:
            latest_data_update_time = self.latest_data_update_time

        update_frequency: Union[Unset, str]
        if isinstance(self.update_frequency, Unset):
            update_frequency = UNSET
        elif isinstance(self.update_frequency, UpdateFrequencyEnum):
            update_frequency = self.update_frequency.value
        else:
            update_frequency = self.update_frequency.value

        data_lineage = self.data_lineage

        removed_data_reason = self.removed_data_reason

        keywords = self.keywords

        publication_state: Union[Unset, str]
        if isinstance(self.publication_state, Unset):
            publication_state = UNSET
        elif isinstance(self.publication_state, PublicationStateCbbEnum):
            publication_state = self.publication_state.value
        else:
            publication_state = self.publication_state.value

        non_geographic_flag = self.non_geographic_flag

        dont_harvest_from_projects = self.dont_harvest_from_projects

        geographic_extent: Union[None, Unset, int]
        if isinstance(self.geographic_extent, Unset):
            geographic_extent = UNSET
        else:
            geographic_extent = self.geographic_extent

        language: Union[Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        elif isinstance(self.language, LanguageEnum):
            language = self.language.value
        else:
            language = self.language.value

        resolution = self.resolution

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        vertical_extent: Union[None, Unset, int]
        if isinstance(self.vertical_extent, Unset):
            vertical_extent = UNSET
        else:
            vertical_extent = self.vertical_extent

        result_field: Union[None, Unset, int]
        if isinstance(self.result_field, Unset):
            result_field = UNSET
        else:
            result_field = self.result_field

        time_period: Union[None, Unset, int]
        if isinstance(self.time_period, Unset):
            time_period = UNSET
        else:
            time_period = self.time_period

        result_quality: Union[None, Unset, int]
        if isinstance(self.result_quality, Unset):
            result_quality = UNSET
        else:
            result_quality = self.result_quality

        data_published_time: Union[None, Unset, str]
        if isinstance(self.data_published_time, Unset):
            data_published_time = UNSET
        elif isinstance(self.data_published_time, datetime.datetime):
            data_published_time = self.data_published_time.isoformat()
        else:
            data_published_time = self.data_published_time

        doi_published_time: Union[None, Unset, str]
        if isinstance(self.doi_published_time, Unset):
            doi_published_time = UNSET
        elif isinstance(self.doi_published_time, datetime.datetime):
            doi_published_time = self.doi_published_time.isoformat()
        else:
            doi_published_time = self.doi_published_time

        removed_data_time: Union[None, Unset, str]
        if isinstance(self.removed_data_time, Unset):
            removed_data_time = UNSET
        elif isinstance(self.removed_data_time, datetime.datetime):
            removed_data_time = self.removed_data_time.isoformat()
        else:
            removed_data_time = self.removed_data_time

        valid_time_period: Union[None, Unset, int]
        if isinstance(self.valid_time_period, Unset):
            valid_time_period = UNSET
        else:
            valid_time_period = self.valid_time_period

        procedure_acquisition: Union[None, Unset, int]
        if isinstance(self.procedure_acquisition, Unset):
            procedure_acquisition = UNSET
        else:
            procedure_acquisition = self.procedure_acquisition

        procedure_computation: Union[None, Unset, int]
        if isinstance(self.procedure_computation, Unset):
            procedure_computation = UNSET
        else:
            procedure_computation = self.procedure_computation

        procedure_composite_process: Union[None, Unset, int]
        if isinstance(self.procedure_composite_process, Unset):
            procedure_composite_process = UNSET
        else:
            procedure_composite_process = self.procedure_composite_process

        image_details: Union[Unset, list[int]] = UNSET
        if not isinstance(self.image_details, Unset):
            image_details = ",".join(self.image_details)

        discovery_keywords: Union[Unset, list[int]] = UNSET
        if not isinstance(self.discovery_keywords, Unset):
            discovery_keywords = ",".join(self.discovery_keywords)

        permissions: Union[Unset, list[int]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = ",".join(self.permissions)

        projects: Union[Unset, list[int]] = UNSET
        if not isinstance(self.projects, Unset):
            projects = ",".join(self.projects)

        inspire_theme: Union[Unset, list[int]] = UNSET
        if not isinstance(self.inspire_theme, Unset):
            inspire_theme = ",".join(self.inspire_theme)

        topic_category: Union[Unset, list[int]] = UNSET
        if not isinstance(self.topic_category, Unset):
            topic_category = ",".join(self.topic_category)

        vocabulary_keywords: Union[Unset, list[int]] = UNSET
        if not isinstance(self.vocabulary_keywords, Unset):
            vocabulary_keywords = ",".join(self.vocabulary_keywords)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if last_updated_date is not UNSET:
            field_dict["lastUpdatedDate"] = last_updated_date
        if latest_data_update_time is not UNSET:
            field_dict["latestDataUpdateTime"] = latest_data_update_time
        if update_frequency is not UNSET:
            field_dict["updateFrequency"] = update_frequency
        if data_lineage is not UNSET:
            field_dict["dataLineage"] = data_lineage
        if removed_data_reason is not UNSET:
            field_dict["removedDataReason"] = removed_data_reason
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if publication_state is not UNSET:
            field_dict["publicationState"] = publication_state
        if non_geographic_flag is not UNSET:
            field_dict["nonGeographicFlag"] = non_geographic_flag
        if dont_harvest_from_projects is not UNSET:
            field_dict["dontHarvestFromProjects"] = dont_harvest_from_projects
        if geographic_extent is not UNSET:
            field_dict["geographicExtent"] = geographic_extent
        if language is not UNSET:
            field_dict["language"] = language
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if status is not UNSET:
            field_dict["status"] = status
        if vertical_extent is not UNSET:
            field_dict["verticalExtent"] = vertical_extent
        if result_field is not UNSET:
            field_dict["result_field"] = result_field
        if time_period is not UNSET:
            field_dict["timePeriod"] = time_period
        if result_quality is not UNSET:
            field_dict["resultQuality"] = result_quality
        if data_published_time is not UNSET:
            field_dict["dataPublishedTime"] = data_published_time
        if doi_published_time is not UNSET:
            field_dict["doiPublishedTime"] = doi_published_time
        if removed_data_time is not UNSET:
            field_dict["removedDataTime"] = removed_data_time
        if valid_time_period is not UNSET:
            field_dict["validTimePeriod"] = valid_time_period
        if procedure_acquisition is not UNSET:
            field_dict["procedureAcquisition"] = procedure_acquisition
        if procedure_computation is not UNSET:
            field_dict["procedureComputation"] = procedure_computation
        if procedure_composite_process is not UNSET:
            field_dict["procedureCompositeProcess"] = procedure_composite_process
        if image_details is not UNSET:
            field_dict["imageDetails"] = image_details
        if discovery_keywords is not UNSET:
            field_dict["discoveryKeywords"] = discovery_keywords
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if projects is not UNSET:
            field_dict["projects"] = projects
        if inspire_theme is not UNSET:
            field_dict["inspireTheme"] = inspire_theme
        if topic_category is not UNSET:
            field_dict["topicCategory"] = topic_category
        if vocabulary_keywords is not UNSET:
            field_dict["vocabularyKeywords"] = vocabulary_keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        abstract = d.pop("abstract", UNSET)

        def _parse_creation_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_date_type_0 = isoparse(data)

                return creation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        creation_date = _parse_creation_date(d.pop("creationDate", UNSET))

        def _parse_last_updated_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_date_type_0 = isoparse(data)

                return last_updated_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_updated_date = _parse_last_updated_date(d.pop("lastUpdatedDate", UNSET))

        def _parse_latest_data_update_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_data_update_time_type_0 = isoparse(data)

                return latest_data_update_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        latest_data_update_time = _parse_latest_data_update_time(d.pop("latestDataUpdateTime", UNSET))

        def _parse_update_frequency(data: object) -> Union[BlankEnum, Unset, UpdateFrequencyEnum]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_frequency_type_0 = UpdateFrequencyEnum(data)

                return update_frequency_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            update_frequency_type_1 = BlankEnum(data)

            return update_frequency_type_1

        update_frequency = _parse_update_frequency(d.pop("updateFrequency", UNSET))

        data_lineage = d.pop("dataLineage", UNSET)

        removed_data_reason = d.pop("removedDataReason", UNSET)

        keywords = d.pop("keywords", UNSET)

        def _parse_publication_state(data: object) -> Union[BlankEnum, PublicationStateCbbEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publication_state_type_0 = PublicationStateCbbEnum(data)

                return publication_state_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            publication_state_type_1 = BlankEnum(data)

            return publication_state_type_1

        publication_state = _parse_publication_state(d.pop("publicationState", UNSET))

        non_geographic_flag = d.pop("nonGeographicFlag", UNSET)

        dont_harvest_from_projects = d.pop("dontHarvestFromProjects", UNSET)

        def _parse_geographic_extent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        geographic_extent = _parse_geographic_extent(d.pop("geographicExtent", UNSET))

        def _parse_language(data: object) -> Union[BlankEnum, LanguageEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                language_type_0 = LanguageEnum(data)

                return language_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            language_type_1 = BlankEnum(data)

            return language_type_1

        language = _parse_language(d.pop("language", UNSET))

        resolution = d.pop("resolution", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusEnum(_status)

        def _parse_vertical_extent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        vertical_extent = _parse_vertical_extent(d.pop("verticalExtent", UNSET))

        def _parse_result_field(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        result_field = _parse_result_field(d.pop("result_field", UNSET))

        def _parse_time_period(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        time_period = _parse_time_period(d.pop("timePeriod", UNSET))

        def _parse_result_quality(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        result_quality = _parse_result_quality(d.pop("resultQuality", UNSET))

        def _parse_data_published_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_published_time_type_0 = isoparse(data)

                return data_published_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        data_published_time = _parse_data_published_time(d.pop("dataPublishedTime", UNSET))

        def _parse_doi_published_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                doi_published_time_type_0 = isoparse(data)

                return doi_published_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        doi_published_time = _parse_doi_published_time(d.pop("doiPublishedTime", UNSET))

        def _parse_removed_data_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                removed_data_time_type_0 = isoparse(data)

                return removed_data_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        removed_data_time = _parse_removed_data_time(d.pop("removedDataTime", UNSET))

        def _parse_valid_time_period(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        valid_time_period = _parse_valid_time_period(d.pop("validTimePeriod", UNSET))

        def _parse_procedure_acquisition(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        procedure_acquisition = _parse_procedure_acquisition(d.pop("procedureAcquisition", UNSET))

        def _parse_procedure_computation(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        procedure_computation = _parse_procedure_computation(d.pop("procedureComputation", UNSET))

        def _parse_procedure_composite_process(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        procedure_composite_process = _parse_procedure_composite_process(d.pop("procedureCompositeProcess", UNSET))

        image_details = cast(list[int], d.pop("imageDetails", UNSET))

        discovery_keywords = cast(list[int], d.pop("discoveryKeywords", UNSET))

        permissions = cast(list[int], d.pop("permissions", UNSET))

        projects = cast(list[int], d.pop("projects", UNSET))

        inspire_theme = cast(list[int], d.pop("inspireTheme", UNSET))

        topic_category = cast(list[int], d.pop("topicCategory", UNSET))

        vocabulary_keywords = cast(list[int], d.pop("vocabularyKeywords", UNSET))

        patched_observation_write_request = cls(
            title=title,
            abstract=abstract,
            creation_date=creation_date,
            last_updated_date=last_updated_date,
            latest_data_update_time=latest_data_update_time,
            update_frequency=update_frequency,
            data_lineage=data_lineage,
            removed_data_reason=removed_data_reason,
            keywords=keywords,
            publication_state=publication_state,
            non_geographic_flag=non_geographic_flag,
            dont_harvest_from_projects=dont_harvest_from_projects,
            geographic_extent=geographic_extent,
            language=language,
            resolution=resolution,
            status=status,
            vertical_extent=vertical_extent,
            result_field=result_field,
            time_period=time_period,
            result_quality=result_quality,
            data_published_time=data_published_time,
            doi_published_time=doi_published_time,
            removed_data_time=removed_data_time,
            valid_time_period=valid_time_period,
            procedure_acquisition=procedure_acquisition,
            procedure_computation=procedure_computation,
            procedure_composite_process=procedure_composite_process,
            image_details=image_details,
            discovery_keywords=discovery_keywords,
            permissions=permissions,
            projects=projects,
            inspire_theme=inspire_theme,
            topic_category=topic_category,
            vocabulary_keywords=vocabulary_keywords,
        )

        patched_observation_write_request.additional_properties = d
        return patched_observation_write_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
