from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.language_enum import LanguageEnum
from ..models.publication_state_cbb_enum import PublicationStateCbbEnum
from ..models.status_enum import StatusEnum
from ..models.update_frequency_enum import UpdateFrequencyEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObservationWriteRequest")


@_attrs_define
class ObservationWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            title (str):
            status (StatusEnum): * `planned` - Planned (pre)
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
            abstract (str | Unset):
            creation_date (datetime.datetime | None | Unset):
            last_updated_date (datetime.datetime | None | Unset):
            latest_data_update_time (datetime.datetime | None | Unset):
            update_frequency (BlankEnum | Unset | UpdateFrequencyEnum):
            data_lineage (str | Unset):
            removed_data_reason (str | Unset):
            keywords (str | Unset):
            publication_state (BlankEnum | PublicationStateCbbEnum | Unset):
            non_geographic_flag (bool | Unset):
            dont_harvest_from_projects (bool | Unset):
            geographic_extent (int | None | Unset):
            language (BlankEnum | LanguageEnum | Unset):
            resolution (str | Unset):
            vertical_extent (int | None | Unset):
            result_field (int | None | Unset):
            time_period (int | None | Unset):
            result_quality (int | None | Unset):
            data_published_time (datetime.datetime | None | Unset):
            doi_published_time (datetime.datetime | None | Unset):
            removed_data_time (datetime.datetime | None | Unset):
            valid_time_period (int | None | Unset):
            procedure_acquisition (int | None | Unset):
            procedure_computation (int | None | Unset):
            procedure_composite_process (int | None | Unset):
            image_details (list[int] | Unset):
            discovery_keywords (list[int] | Unset):
            permissions (list[int] | Unset):
            projects (list[int] | Unset):
            inspire_theme (list[int] | Unset):
            topic_category (list[int] | Unset):
            vocabulary_keywords (list[int] | Unset):
    """

    title: str
    status: StatusEnum
    abstract: str | Unset = UNSET
    creation_date: datetime.datetime | None | Unset = UNSET
    last_updated_date: datetime.datetime | None | Unset = UNSET
    latest_data_update_time: datetime.datetime | None | Unset = UNSET
    update_frequency: BlankEnum | Unset | UpdateFrequencyEnum = UNSET
    data_lineage: str | Unset = UNSET
    removed_data_reason: str | Unset = UNSET
    keywords: str | Unset = UNSET
    publication_state: BlankEnum | PublicationStateCbbEnum | Unset = UNSET
    non_geographic_flag: bool | Unset = UNSET
    dont_harvest_from_projects: bool | Unset = UNSET
    geographic_extent: int | None | Unset = UNSET
    language: BlankEnum | LanguageEnum | Unset = UNSET
    resolution: str | Unset = UNSET
    vertical_extent: int | None | Unset = UNSET
    result_field: int | None | Unset = UNSET
    time_period: int | None | Unset = UNSET
    result_quality: int | None | Unset = UNSET
    data_published_time: datetime.datetime | None | Unset = UNSET
    doi_published_time: datetime.datetime | None | Unset = UNSET
    removed_data_time: datetime.datetime | None | Unset = UNSET
    valid_time_period: int | None | Unset = UNSET
    procedure_acquisition: int | None | Unset = UNSET
    procedure_computation: int | None | Unset = UNSET
    procedure_composite_process: int | None | Unset = UNSET
    image_details: list[int] | Unset = UNSET
    discovery_keywords: list[int] | Unset = UNSET
    permissions: list[int] | Unset = UNSET
    projects: list[int] | Unset = UNSET
    inspire_theme: list[int] | Unset = UNSET
    topic_category: list[int] | Unset = UNSET
    vocabulary_keywords: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        status = self.status.value

        abstract = self.abstract

        creation_date: None | str | Unset
        if isinstance(self.creation_date, Unset):
            creation_date = UNSET
        elif isinstance(self.creation_date, datetime.datetime):
            creation_date = self.creation_date.isoformat()
        else:
            creation_date = self.creation_date

        last_updated_date: None | str | Unset
        if isinstance(self.last_updated_date, Unset):
            last_updated_date = UNSET
        elif isinstance(self.last_updated_date, datetime.datetime):
            last_updated_date = self.last_updated_date.isoformat()
        else:
            last_updated_date = self.last_updated_date

        latest_data_update_time: None | str | Unset
        if isinstance(self.latest_data_update_time, Unset):
            latest_data_update_time = UNSET
        elif isinstance(self.latest_data_update_time, datetime.datetime):
            latest_data_update_time = self.latest_data_update_time.isoformat()
        else:
            latest_data_update_time = self.latest_data_update_time

        update_frequency: str | Unset
        if isinstance(self.update_frequency, Unset):
            update_frequency = UNSET
        elif isinstance(self.update_frequency, UpdateFrequencyEnum):
            update_frequency = self.update_frequency.value
        else:
            update_frequency = self.update_frequency.value

        data_lineage = self.data_lineage

        removed_data_reason = self.removed_data_reason

        keywords = self.keywords

        publication_state: str | Unset
        if isinstance(self.publication_state, Unset):
            publication_state = UNSET
        elif isinstance(self.publication_state, PublicationStateCbbEnum):
            publication_state = self.publication_state.value
        else:
            publication_state = self.publication_state.value

        non_geographic_flag = self.non_geographic_flag

        dont_harvest_from_projects = self.dont_harvest_from_projects

        geographic_extent: int | None | Unset
        if isinstance(self.geographic_extent, Unset):
            geographic_extent = UNSET
        else:
            geographic_extent = self.geographic_extent

        language: str | Unset
        if isinstance(self.language, Unset):
            language = UNSET
        elif isinstance(self.language, LanguageEnum):
            language = self.language.value
        else:
            language = self.language.value

        resolution = self.resolution

        vertical_extent: int | None | Unset
        if isinstance(self.vertical_extent, Unset):
            vertical_extent = UNSET
        else:
            vertical_extent = self.vertical_extent

        result_field: int | None | Unset
        if isinstance(self.result_field, Unset):
            result_field = UNSET
        else:
            result_field = self.result_field

        time_period: int | None | Unset
        if isinstance(self.time_period, Unset):
            time_period = UNSET
        else:
            time_period = self.time_period

        result_quality: int | None | Unset
        if isinstance(self.result_quality, Unset):
            result_quality = UNSET
        else:
            result_quality = self.result_quality

        data_published_time: None | str | Unset
        if isinstance(self.data_published_time, Unset):
            data_published_time = UNSET
        elif isinstance(self.data_published_time, datetime.datetime):
            data_published_time = self.data_published_time.isoformat()
        else:
            data_published_time = self.data_published_time

        doi_published_time: None | str | Unset
        if isinstance(self.doi_published_time, Unset):
            doi_published_time = UNSET
        elif isinstance(self.doi_published_time, datetime.datetime):
            doi_published_time = self.doi_published_time.isoformat()
        else:
            doi_published_time = self.doi_published_time

        removed_data_time: None | str | Unset
        if isinstance(self.removed_data_time, Unset):
            removed_data_time = UNSET
        elif isinstance(self.removed_data_time, datetime.datetime):
            removed_data_time = self.removed_data_time.isoformat()
        else:
            removed_data_time = self.removed_data_time

        valid_time_period: int | None | Unset
        if isinstance(self.valid_time_period, Unset):
            valid_time_period = UNSET
        else:
            valid_time_period = self.valid_time_period

        procedure_acquisition: int | None | Unset
        if isinstance(self.procedure_acquisition, Unset):
            procedure_acquisition = UNSET
        else:
            procedure_acquisition = self.procedure_acquisition

        procedure_computation: int | None | Unset
        if isinstance(self.procedure_computation, Unset):
            procedure_computation = UNSET
        else:
            procedure_computation = self.procedure_computation

        procedure_composite_process: int | None | Unset
        if isinstance(self.procedure_composite_process, Unset):
            procedure_composite_process = UNSET
        else:
            procedure_composite_process = self.procedure_composite_process

        image_details: list[int] | Unset = UNSET
        if not isinstance(self.image_details, Unset):
            image_details = ",".join(map(str, self.image_details))

        discovery_keywords: list[int] | Unset = UNSET
        if not isinstance(self.discovery_keywords, Unset):
            discovery_keywords = ",".join(map(str, self.discovery_keywords))

        permissions: list[int] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = ",".join(map(str, self.permissions))

        projects: list[int] | Unset = UNSET
        if not isinstance(self.projects, Unset):
            projects = ",".join(map(str, self.projects))

        inspire_theme: list[int] | Unset = UNSET
        if not isinstance(self.inspire_theme, Unset):
            inspire_theme = ",".join(map(str, self.inspire_theme))

        topic_category: list[int] | Unset = UNSET
        if not isinstance(self.topic_category, Unset):
            topic_category = ",".join(map(str, self.topic_category))

        vocabulary_keywords: list[int] | Unset = UNSET
        if not isinstance(self.vocabulary_keywords, Unset):
            vocabulary_keywords = ",".join(map(str, self.vocabulary_keywords))

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "status": status,
            }
        )
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
        title = d.pop("title")

        status = StatusEnum(d.pop("status"))

        abstract = d.pop("abstract", UNSET)

        def _parse_creation_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_date_type_0 = isoparse(data)

                return creation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        creation_date = _parse_creation_date(d.pop("creationDate", UNSET))

        def _parse_last_updated_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_date_type_0 = isoparse(data)

                return last_updated_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_updated_date = _parse_last_updated_date(d.pop("lastUpdatedDate", UNSET))

        def _parse_latest_data_update_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_data_update_time_type_0 = isoparse(data)

                return latest_data_update_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        latest_data_update_time = _parse_latest_data_update_time(d.pop("latestDataUpdateTime", UNSET))

        def _parse_update_frequency(data: object) -> BlankEnum | Unset | UpdateFrequencyEnum:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_frequency_type_0 = UpdateFrequencyEnum(data)

                return update_frequency_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            update_frequency_type_1 = BlankEnum(data)

            return update_frequency_type_1

        update_frequency = _parse_update_frequency(d.pop("updateFrequency", UNSET))

        data_lineage = d.pop("dataLineage", UNSET)

        removed_data_reason = d.pop("removedDataReason", UNSET)

        keywords = d.pop("keywords", UNSET)

        def _parse_publication_state(data: object) -> BlankEnum | PublicationStateCbbEnum | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publication_state_type_0 = PublicationStateCbbEnum(data)

                return publication_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            publication_state_type_1 = BlankEnum(data)

            return publication_state_type_1

        publication_state = _parse_publication_state(d.pop("publicationState", UNSET))

        non_geographic_flag = d.pop("nonGeographicFlag", UNSET)

        dont_harvest_from_projects = d.pop("dontHarvestFromProjects", UNSET)

        def _parse_geographic_extent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        geographic_extent = _parse_geographic_extent(d.pop("geographicExtent", UNSET))

        def _parse_language(data: object) -> BlankEnum | LanguageEnum | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                language_type_0 = LanguageEnum(data)

                return language_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            language_type_1 = BlankEnum(data)

            return language_type_1

        language = _parse_language(d.pop("language", UNSET))

        resolution = d.pop("resolution", UNSET)

        def _parse_vertical_extent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vertical_extent = _parse_vertical_extent(d.pop("verticalExtent", UNSET))

        def _parse_result_field(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_field = _parse_result_field(d.pop("result_field", UNSET))

        def _parse_time_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_period = _parse_time_period(d.pop("timePeriod", UNSET))

        def _parse_result_quality(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        result_quality = _parse_result_quality(d.pop("resultQuality", UNSET))

        def _parse_data_published_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_published_time_type_0 = isoparse(data)

                return data_published_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        data_published_time = _parse_data_published_time(d.pop("dataPublishedTime", UNSET))

        def _parse_doi_published_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                doi_published_time_type_0 = isoparse(data)

                return doi_published_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        doi_published_time = _parse_doi_published_time(d.pop("doiPublishedTime", UNSET))

        def _parse_removed_data_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                removed_data_time_type_0 = isoparse(data)

                return removed_data_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        removed_data_time = _parse_removed_data_time(d.pop("removedDataTime", UNSET))

        def _parse_valid_time_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        valid_time_period = _parse_valid_time_period(d.pop("validTimePeriod", UNSET))

        def _parse_procedure_acquisition(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        procedure_acquisition = _parse_procedure_acquisition(d.pop("procedureAcquisition", UNSET))

        def _parse_procedure_computation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        procedure_computation = _parse_procedure_computation(d.pop("procedureComputation", UNSET))

        def _parse_procedure_composite_process(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        procedure_composite_process = _parse_procedure_composite_process(d.pop("procedureCompositeProcess", UNSET))

        image_details = cast(list[int], d.pop("imageDetails", UNSET))

        discovery_keywords = cast(list[int], d.pop("discoveryKeywords", UNSET))

        permissions = cast(list[int], d.pop("permissions", UNSET))

        projects = cast(list[int], d.pop("projects", UNSET))

        inspire_theme = cast(list[int], d.pop("inspireTheme", UNSET))

        topic_category = cast(list[int], d.pop("topicCategory", UNSET))

        vocabulary_keywords = cast(list[int], d.pop("vocabularyKeywords", UNSET))

        observation_write_request = cls(
            title=title,
            status=status,
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

        observation_write_request.additional_properties = d
        return observation_write_request

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
