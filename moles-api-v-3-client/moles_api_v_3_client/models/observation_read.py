from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.language_enum import LanguageEnum
from ..models.publication_state_cbb_enum import PublicationStateCbbEnum
from ..models.status_enum import StatusEnum
from ..models.update_frequency_enum import UpdateFrequencyEnum

if TYPE_CHECKING:
    from ..models.constraints_read import ConstraintsRead
    from ..models.discovery_service_id_read import DiscoveryServiceIdRead
    from ..models.dq_conformance_result_read import DQConformanceResultRead
    from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
    from ..models.inspire_theme_read import InspireThemeRead
    from ..models.related_result import RelatedResult
    from ..models.simple_read import SimpleRead
    from ..models.time_period import TimePeriod
    from ..models.topic_category_read import TopicCategoryRead
    from ..models.vertical_extent_read import VerticalExtentRead
    from ..models.vocabulary_term_read import VocabularyTermRead


T = TypeVar("T", bound="ObservationRead")


@_attrs_define
class ObservationRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            uuid (None | str):
            title (None | str):
            abstract (None | str):
            creation_date (datetime.datetime | None):
            last_updated_date (datetime.datetime | None):
            latest_data_update_time (datetime.datetime | None):
            update_frequency (BlankEnum | None | UpdateFrequencyEnum):
            data_lineage (None | str):
            removed_data_reason (None | str):
            keywords (None | str):
            publication_state (BlankEnum | None | PublicationStateCbbEnum):
            non_geographic_flag (bool | None):
            dont_harvest_from_projects (bool | None):
            language (BlankEnum | LanguageEnum | None):
            resolution (None | str):
            status (None | StatusEnum):
            data_published_time (datetime.datetime | None):
            doi_published_time (datetime.datetime | None):
            removed_data_time (datetime.datetime | None):
            geographic_extent (GeographicBoundingBoxRead | None):
            vertical_extent (None | VerticalExtentRead):
            result_field (RelatedResult):
            time_period (None | TimePeriod):
            result_quality (DQConformanceResultRead | None):
            valid_time_period (None | TimePeriod):
            procedure_acquisition (None | SimpleRead):
            procedure_computation (None | SimpleRead):
            procedure_composite_process (None | SimpleRead):
            image_details (list[int | None]):
            discovery_keywords (list[DiscoveryServiceIdRead] | None):
            permissions (list[ConstraintsRead] | None):
            projects (list[SimpleRead] | None):
            inspire_theme (list[InspireThemeRead] | None):
            topic_category (list[TopicCategoryRead] | None):
            phenomena (list[int | None]):
            vocabulary_keywords (list[VocabularyTermRead] | None):
            identifier_set (list[int | None]):
            observationcollection_set (list[SimpleRead] | None):
            responsiblepartyinfo_set (list[int | None]):
            onlineresource_set (list[int | None]):
    """

    ob_id: int | None
    uuid: None | str
    title: None | str
    abstract: None | str
    creation_date: datetime.datetime | None
    last_updated_date: datetime.datetime | None
    latest_data_update_time: datetime.datetime | None
    update_frequency: BlankEnum | None | UpdateFrequencyEnum
    data_lineage: None | str
    removed_data_reason: None | str
    keywords: None | str
    publication_state: BlankEnum | None | PublicationStateCbbEnum
    non_geographic_flag: bool | None
    dont_harvest_from_projects: bool | None
    language: BlankEnum | LanguageEnum | None
    resolution: None | str
    status: None | StatusEnum
    data_published_time: datetime.datetime | None
    doi_published_time: datetime.datetime | None
    removed_data_time: datetime.datetime | None
    geographic_extent: GeographicBoundingBoxRead | None
    vertical_extent: None | VerticalExtentRead
    result_field: RelatedResult
    time_period: None | TimePeriod
    result_quality: DQConformanceResultRead | None
    valid_time_period: None | TimePeriod
    procedure_acquisition: None | SimpleRead
    procedure_computation: None | SimpleRead
    procedure_composite_process: None | SimpleRead
    image_details: list[int | None]
    discovery_keywords: list[DiscoveryServiceIdRead] | None
    permissions: list[ConstraintsRead] | None
    projects: list[SimpleRead] | None
    inspire_theme: list[InspireThemeRead] | None
    topic_category: list[TopicCategoryRead] | None
    phenomena: list[int | None]
    vocabulary_keywords: list[VocabularyTermRead] | None
    identifier_set: list[int | None]
    observationcollection_set: list[SimpleRead] | None
    responsiblepartyinfo_set: list[int | None]
    onlineresource_set: list[int | None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dq_conformance_result_read import DQConformanceResultRead
        from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
        from ..models.simple_read import SimpleRead
        from ..models.time_period import TimePeriod
        from ..models.vertical_extent_read import VerticalExtentRead

        ob_id: int | None
        ob_id = self.ob_id

        uuid: None | str
        uuid = self.uuid

        title: None | str
        title = self.title

        abstract: None | str
        abstract = self.abstract

        creation_date: None | str
        if isinstance(self.creation_date, datetime.datetime):
            creation_date = self.creation_date.isoformat()
        else:
            creation_date = self.creation_date

        last_updated_date: None | str
        if isinstance(self.last_updated_date, datetime.datetime):
            last_updated_date = self.last_updated_date.isoformat()
        else:
            last_updated_date = self.last_updated_date

        latest_data_update_time: None | str
        if isinstance(self.latest_data_update_time, datetime.datetime):
            latest_data_update_time = self.latest_data_update_time.isoformat()
        else:
            latest_data_update_time = self.latest_data_update_time

        update_frequency: None | str
        if isinstance(self.update_frequency, UpdateFrequencyEnum):
            update_frequency = self.update_frequency.value
        elif isinstance(self.update_frequency, BlankEnum):
            update_frequency = self.update_frequency.value
        else:
            update_frequency = self.update_frequency

        data_lineage: None | str
        data_lineage = self.data_lineage

        removed_data_reason: None | str
        removed_data_reason = self.removed_data_reason

        keywords: None | str
        keywords = self.keywords

        publication_state: None | str
        if isinstance(self.publication_state, PublicationStateCbbEnum):
            publication_state = self.publication_state.value
        elif isinstance(self.publication_state, BlankEnum):
            publication_state = self.publication_state.value
        else:
            publication_state = self.publication_state

        non_geographic_flag: bool | None
        non_geographic_flag = self.non_geographic_flag

        dont_harvest_from_projects: bool | None
        dont_harvest_from_projects = self.dont_harvest_from_projects

        language: None | str
        if isinstance(self.language, LanguageEnum):
            language = self.language.value
        elif isinstance(self.language, BlankEnum):
            language = self.language.value
        else:
            language = self.language

        resolution: None | str
        resolution = self.resolution

        status: None | str
        if isinstance(self.status, StatusEnum):
            status = self.status.value
        else:
            status = self.status

        data_published_time: None | str
        if isinstance(self.data_published_time, datetime.datetime):
            data_published_time = self.data_published_time.isoformat()
        else:
            data_published_time = self.data_published_time

        doi_published_time: None | str
        if isinstance(self.doi_published_time, datetime.datetime):
            doi_published_time = self.doi_published_time.isoformat()
        else:
            doi_published_time = self.doi_published_time

        removed_data_time: None | str
        if isinstance(self.removed_data_time, datetime.datetime):
            removed_data_time = self.removed_data_time.isoformat()
        else:
            removed_data_time = self.removed_data_time

        geographic_extent: dict[str, Any] | None
        if isinstance(self.geographic_extent, GeographicBoundingBoxRead):
            geographic_extent = self.geographic_extent.to_dict()
        else:
            geographic_extent = self.geographic_extent

        vertical_extent: dict[str, Any] | None
        if isinstance(self.vertical_extent, VerticalExtentRead):
            vertical_extent = self.vertical_extent.to_dict()
        else:
            vertical_extent = self.vertical_extent

        result_field = self.result_field.to_dict()

        time_period: dict[str, Any] | None
        if isinstance(self.time_period, TimePeriod):
            time_period = self.time_period.to_dict()
        else:
            time_period = self.time_period

        result_quality: dict[str, Any] | None
        if isinstance(self.result_quality, DQConformanceResultRead):
            result_quality = self.result_quality.to_dict()
        else:
            result_quality = self.result_quality

        valid_time_period: dict[str, Any] | None
        if isinstance(self.valid_time_period, TimePeriod):
            valid_time_period = self.valid_time_period.to_dict()
        else:
            valid_time_period = self.valid_time_period

        procedure_acquisition: dict[str, Any] | None
        if isinstance(self.procedure_acquisition, SimpleRead):
            procedure_acquisition = self.procedure_acquisition.to_dict()
        else:
            procedure_acquisition = self.procedure_acquisition

        procedure_computation: dict[str, Any] | None
        if isinstance(self.procedure_computation, SimpleRead):
            procedure_computation = self.procedure_computation.to_dict()
        else:
            procedure_computation = self.procedure_computation

        procedure_composite_process: dict[str, Any] | None
        if isinstance(self.procedure_composite_process, SimpleRead):
            procedure_composite_process = self.procedure_composite_process.to_dict()
        else:
            procedure_composite_process = self.procedure_composite_process

        image_details = []
        for image_details_item_data in self.image_details:
            image_details_item: int | None
            image_details_item = image_details_item_data
            image_details.append(image_details_item)

        discovery_keywords: list[dict[str, Any]] | None
        if isinstance(self.discovery_keywords, list):
            discovery_keywords = []
            for discovery_keywords_type_0_item_data in self.discovery_keywords:
                discovery_keywords_type_0_item = discovery_keywords_type_0_item_data.to_dict()
                discovery_keywords.append(discovery_keywords_type_0_item)

        else:
            discovery_keywords = self.discovery_keywords

        permissions: list[dict[str, Any]] | None
        if isinstance(self.permissions, list):
            permissions = []
            for permissions_type_0_item_data in self.permissions:
                permissions_type_0_item = permissions_type_0_item_data.to_dict()
                permissions.append(permissions_type_0_item)

        else:
            permissions = self.permissions

        projects: list[dict[str, Any]] | None
        if isinstance(self.projects, list):
            projects = []
            for projects_type_0_item_data in self.projects:
                projects_type_0_item = projects_type_0_item_data.to_dict()
                projects.append(projects_type_0_item)

        else:
            projects = self.projects

        inspire_theme: list[dict[str, Any]] | None
        if isinstance(self.inspire_theme, list):
            inspire_theme = []
            for inspire_theme_type_0_item_data in self.inspire_theme:
                inspire_theme_type_0_item = inspire_theme_type_0_item_data.to_dict()
                inspire_theme.append(inspire_theme_type_0_item)

        else:
            inspire_theme = self.inspire_theme

        topic_category: list[dict[str, Any]] | None
        if isinstance(self.topic_category, list):
            topic_category = []
            for topic_category_type_0_item_data in self.topic_category:
                topic_category_type_0_item = topic_category_type_0_item_data.to_dict()
                topic_category.append(topic_category_type_0_item)

        else:
            topic_category = self.topic_category

        phenomena = []
        for phenomena_item_data in self.phenomena:
            phenomena_item: int | None
            phenomena_item = phenomena_item_data
            phenomena.append(phenomena_item)

        vocabulary_keywords: list[dict[str, Any]] | None
        if isinstance(self.vocabulary_keywords, list):
            vocabulary_keywords = []
            for vocabulary_keywords_type_0_item_data in self.vocabulary_keywords:
                vocabulary_keywords_type_0_item = vocabulary_keywords_type_0_item_data.to_dict()
                vocabulary_keywords.append(vocabulary_keywords_type_0_item)

        else:
            vocabulary_keywords = self.vocabulary_keywords

        identifier_set = []
        for identifier_set_item_data in self.identifier_set:
            identifier_set_item: int | None
            identifier_set_item = identifier_set_item_data
            identifier_set.append(identifier_set_item)

        observationcollection_set: list[dict[str, Any]] | None
        if isinstance(self.observationcollection_set, list):
            observationcollection_set = []
            for observationcollection_set_type_0_item_data in self.observationcollection_set:
                observationcollection_set_type_0_item = observationcollection_set_type_0_item_data.to_dict()
                observationcollection_set.append(observationcollection_set_type_0_item)

        else:
            observationcollection_set = self.observationcollection_set

        responsiblepartyinfo_set = []
        for responsiblepartyinfo_set_item_data in self.responsiblepartyinfo_set:
            responsiblepartyinfo_set_item: int | None
            responsiblepartyinfo_set_item = responsiblepartyinfo_set_item_data
            responsiblepartyinfo_set.append(responsiblepartyinfo_set_item)

        onlineresource_set = []
        for onlineresource_set_item_data in self.onlineresource_set:
            onlineresource_set_item: int | None
            onlineresource_set_item = onlineresource_set_item_data
            onlineresource_set.append(onlineresource_set_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "title": title,
                "abstract": abstract,
                "creationDate": creation_date,
                "lastUpdatedDate": last_updated_date,
                "latestDataUpdateTime": latest_data_update_time,
                "updateFrequency": update_frequency,
                "dataLineage": data_lineage,
                "removedDataReason": removed_data_reason,
                "keywords": keywords,
                "publicationState": publication_state,
                "nonGeographicFlag": non_geographic_flag,
                "dontHarvestFromProjects": dont_harvest_from_projects,
                "language": language,
                "resolution": resolution,
                "status": status,
                "dataPublishedTime": data_published_time,
                "doiPublishedTime": doi_published_time,
                "removedDataTime": removed_data_time,
                "geographicExtent": geographic_extent,
                "verticalExtent": vertical_extent,
                "result_field": result_field,
                "timePeriod": time_period,
                "resultQuality": result_quality,
                "validTimePeriod": valid_time_period,
                "procedureAcquisition": procedure_acquisition,
                "procedureComputation": procedure_computation,
                "procedureCompositeProcess": procedure_composite_process,
                "imageDetails": image_details,
                "discoveryKeywords": discovery_keywords,
                "permissions": permissions,
                "projects": projects,
                "inspireTheme": inspire_theme,
                "topicCategory": topic_category,
                "phenomena": phenomena,
                "vocabularyKeywords": vocabulary_keywords,
                "identifier_set": identifier_set,
                "observationcollection_set": observationcollection_set,
                "responsiblepartyinfo_set": responsiblepartyinfo_set,
                "onlineresource_set": onlineresource_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constraints_read import ConstraintsRead
        from ..models.discovery_service_id_read import DiscoveryServiceIdRead
        from ..models.dq_conformance_result_read import DQConformanceResultRead
        from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
        from ..models.inspire_theme_read import InspireThemeRead
        from ..models.related_result import RelatedResult
        from ..models.simple_read import SimpleRead
        from ..models.time_period import TimePeriod
        from ..models.topic_category_read import TopicCategoryRead
        from ..models.vertical_extent_read import VerticalExtentRead
        from ..models.vocabulary_term_read import VocabularyTermRead

        d = dict(src_dict)

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        uuid = _parse_uuid(d.pop("uuid"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_abstract(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        abstract = _parse_abstract(d.pop("abstract"))

        def _parse_creation_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_date_type_0 = isoparse(data)

                return creation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        creation_date = _parse_creation_date(d.pop("creationDate"))

        def _parse_last_updated_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_date_type_0 = isoparse(data)

                return last_updated_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_updated_date = _parse_last_updated_date(d.pop("lastUpdatedDate"))

        def _parse_latest_data_update_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_data_update_time_type_0 = isoparse(data)

                return latest_data_update_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        latest_data_update_time = _parse_latest_data_update_time(d.pop("latestDataUpdateTime"))

        def _parse_update_frequency(data: object) -> BlankEnum | None | UpdateFrequencyEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_frequency_type_0 = UpdateFrequencyEnum(data)

                return update_frequency_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_frequency_type_1 = BlankEnum(data)

                return update_frequency_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | UpdateFrequencyEnum, data)

        update_frequency = _parse_update_frequency(d.pop("updateFrequency"))

        def _parse_data_lineage(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        data_lineage = _parse_data_lineage(d.pop("dataLineage"))

        def _parse_removed_data_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        removed_data_reason = _parse_removed_data_reason(d.pop("removedDataReason"))

        def _parse_keywords(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        keywords = _parse_keywords(d.pop("keywords"))

        def _parse_publication_state(data: object) -> BlankEnum | None | PublicationStateCbbEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publication_state_type_0 = PublicationStateCbbEnum(data)

                return publication_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publication_state_type_1 = BlankEnum(data)

                return publication_state_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | PublicationStateCbbEnum, data)

        publication_state = _parse_publication_state(d.pop("publicationState"))

        def _parse_non_geographic_flag(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        non_geographic_flag = _parse_non_geographic_flag(d.pop("nonGeographicFlag"))

        def _parse_dont_harvest_from_projects(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        dont_harvest_from_projects = _parse_dont_harvest_from_projects(d.pop("dontHarvestFromProjects"))

        def _parse_language(data: object) -> BlankEnum | LanguageEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                language_type_0 = LanguageEnum(data)

                return language_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                language_type_1 = BlankEnum(data)

                return language_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | LanguageEnum | None, data)

        language = _parse_language(d.pop("language"))

        def _parse_resolution(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolution = _parse_resolution(d.pop("resolution"))

        def _parse_status(data: object) -> None | StatusEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = StatusEnum(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StatusEnum, data)

        status = _parse_status(d.pop("status"))

        def _parse_data_published_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_published_time_type_0 = isoparse(data)

                return data_published_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        data_published_time = _parse_data_published_time(d.pop("dataPublishedTime"))

        def _parse_doi_published_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                doi_published_time_type_0 = isoparse(data)

                return doi_published_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        doi_published_time = _parse_doi_published_time(d.pop("doiPublishedTime"))

        def _parse_removed_data_time(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                removed_data_time_type_0 = isoparse(data)

                return removed_data_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        removed_data_time = _parse_removed_data_time(d.pop("removedDataTime"))

        def _parse_geographic_extent(data: object) -> GeographicBoundingBoxRead | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geographic_extent_type_1 = GeographicBoundingBoxRead.from_dict(data)

                return geographic_extent_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GeographicBoundingBoxRead | None, data)

        geographic_extent = _parse_geographic_extent(d.pop("geographicExtent"))

        def _parse_vertical_extent(data: object) -> None | VerticalExtentRead:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vertical_extent_type_1 = VerticalExtentRead.from_dict(data)

                return vertical_extent_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | VerticalExtentRead, data)

        vertical_extent = _parse_vertical_extent(d.pop("verticalExtent"))

        result_field = RelatedResult.from_dict(d.pop("result_field"))

        def _parse_time_period(data: object) -> None | TimePeriod:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_period_type_1 = TimePeriod.from_dict(data)

                return time_period_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TimePeriod, data)

        time_period = _parse_time_period(d.pop("timePeriod"))

        def _parse_result_quality(data: object) -> DQConformanceResultRead | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_quality_type_1 = DQConformanceResultRead.from_dict(data)

                return result_quality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DQConformanceResultRead | None, data)

        result_quality = _parse_result_quality(d.pop("resultQuality"))

        def _parse_valid_time_period(data: object) -> None | TimePeriod:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                valid_time_period_type_1 = TimePeriod.from_dict(data)

                return valid_time_period_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TimePeriod, data)

        valid_time_period = _parse_valid_time_period(d.pop("validTimePeriod"))

        def _parse_procedure_acquisition(data: object) -> None | SimpleRead:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                procedure_acquisition_type_1 = SimpleRead.from_dict(data)

                return procedure_acquisition_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SimpleRead, data)

        procedure_acquisition = _parse_procedure_acquisition(d.pop("procedureAcquisition"))

        def _parse_procedure_computation(data: object) -> None | SimpleRead:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                procedure_computation_type_1 = SimpleRead.from_dict(data)

                return procedure_computation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SimpleRead, data)

        procedure_computation = _parse_procedure_computation(d.pop("procedureComputation"))

        def _parse_procedure_composite_process(data: object) -> None | SimpleRead:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                procedure_composite_process_type_1 = SimpleRead.from_dict(data)

                return procedure_composite_process_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SimpleRead, data)

        procedure_composite_process = _parse_procedure_composite_process(d.pop("procedureCompositeProcess"))

        image_details = []
        _image_details = d.pop("imageDetails")
        for image_details_item_data in _image_details:

            def _parse_image_details_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            image_details_item = _parse_image_details_item(image_details_item_data)

            image_details.append(image_details_item)

        def _parse_discovery_keywords(data: object) -> list[DiscoveryServiceIdRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                discovery_keywords_type_0 = []
                _discovery_keywords_type_0 = data
                for discovery_keywords_type_0_item_data in _discovery_keywords_type_0:
                    discovery_keywords_type_0_item = DiscoveryServiceIdRead.from_dict(
                        discovery_keywords_type_0_item_data
                    )

                    discovery_keywords_type_0.append(discovery_keywords_type_0_item)

                return discovery_keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DiscoveryServiceIdRead] | None, data)

        discovery_keywords = _parse_discovery_keywords(d.pop("discoveryKeywords"))

        def _parse_permissions(data: object) -> list[ConstraintsRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_type_0 = []
                _permissions_type_0 = data
                for permissions_type_0_item_data in _permissions_type_0:
                    permissions_type_0_item = ConstraintsRead.from_dict(permissions_type_0_item_data)

                    permissions_type_0.append(permissions_type_0_item)

                return permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConstraintsRead] | None, data)

        permissions = _parse_permissions(d.pop("permissions"))

        def _parse_projects(data: object) -> list[SimpleRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                projects_type_0 = []
                _projects_type_0 = data
                for projects_type_0_item_data in _projects_type_0:
                    projects_type_0_item = SimpleRead.from_dict(projects_type_0_item_data)

                    projects_type_0.append(projects_type_0_item)

                return projects_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleRead] | None, data)

        projects = _parse_projects(d.pop("projects"))

        def _parse_inspire_theme(data: object) -> list[InspireThemeRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inspire_theme_type_0 = []
                _inspire_theme_type_0 = data
                for inspire_theme_type_0_item_data in _inspire_theme_type_0:
                    inspire_theme_type_0_item = InspireThemeRead.from_dict(inspire_theme_type_0_item_data)

                    inspire_theme_type_0.append(inspire_theme_type_0_item)

                return inspire_theme_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InspireThemeRead] | None, data)

        inspire_theme = _parse_inspire_theme(d.pop("inspireTheme"))

        def _parse_topic_category(data: object) -> list[TopicCategoryRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                topic_category_type_0 = []
                _topic_category_type_0 = data
                for topic_category_type_0_item_data in _topic_category_type_0:
                    topic_category_type_0_item = TopicCategoryRead.from_dict(topic_category_type_0_item_data)

                    topic_category_type_0.append(topic_category_type_0_item)

                return topic_category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TopicCategoryRead] | None, data)

        topic_category = _parse_topic_category(d.pop("topicCategory"))

        phenomena = []
        _phenomena = d.pop("phenomena")
        for phenomena_item_data in _phenomena:

            def _parse_phenomena_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            phenomena_item = _parse_phenomena_item(phenomena_item_data)

            phenomena.append(phenomena_item)

        def _parse_vocabulary_keywords(data: object) -> list[VocabularyTermRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                vocabulary_keywords_type_0 = []
                _vocabulary_keywords_type_0 = data
                for vocabulary_keywords_type_0_item_data in _vocabulary_keywords_type_0:
                    vocabulary_keywords_type_0_item = VocabularyTermRead.from_dict(vocabulary_keywords_type_0_item_data)

                    vocabulary_keywords_type_0.append(vocabulary_keywords_type_0_item)

                return vocabulary_keywords_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VocabularyTermRead] | None, data)

        vocabulary_keywords = _parse_vocabulary_keywords(d.pop("vocabularyKeywords"))

        identifier_set = []
        _identifier_set = d.pop("identifier_set")
        for identifier_set_item_data in _identifier_set:

            def _parse_identifier_set_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            identifier_set_item = _parse_identifier_set_item(identifier_set_item_data)

            identifier_set.append(identifier_set_item)

        def _parse_observationcollection_set(data: object) -> list[SimpleRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                observationcollection_set_type_0 = []
                _observationcollection_set_type_0 = data
                for observationcollection_set_type_0_item_data in _observationcollection_set_type_0:
                    observationcollection_set_type_0_item = SimpleRead.from_dict(
                        observationcollection_set_type_0_item_data
                    )

                    observationcollection_set_type_0.append(observationcollection_set_type_0_item)

                return observationcollection_set_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleRead] | None, data)

        observationcollection_set = _parse_observationcollection_set(d.pop("observationcollection_set"))

        responsiblepartyinfo_set = []
        _responsiblepartyinfo_set = d.pop("responsiblepartyinfo_set")
        for responsiblepartyinfo_set_item_data in _responsiblepartyinfo_set:

            def _parse_responsiblepartyinfo_set_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            responsiblepartyinfo_set_item = _parse_responsiblepartyinfo_set_item(responsiblepartyinfo_set_item_data)

            responsiblepartyinfo_set.append(responsiblepartyinfo_set_item)

        onlineresource_set = []
        _onlineresource_set = d.pop("onlineresource_set")
        for onlineresource_set_item_data in _onlineresource_set:

            def _parse_onlineresource_set_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            onlineresource_set_item = _parse_onlineresource_set_item(onlineresource_set_item_data)

            onlineresource_set.append(onlineresource_set_item)

        observation_read = cls(
            ob_id=ob_id,
            uuid=uuid,
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
            language=language,
            resolution=resolution,
            status=status,
            data_published_time=data_published_time,
            doi_published_time=doi_published_time,
            removed_data_time=removed_data_time,
            geographic_extent=geographic_extent,
            vertical_extent=vertical_extent,
            result_field=result_field,
            time_period=time_period,
            result_quality=result_quality,
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
            phenomena=phenomena,
            vocabulary_keywords=vocabulary_keywords,
            identifier_set=identifier_set,
            observationcollection_set=observationcollection_set,
            responsiblepartyinfo_set=responsiblepartyinfo_set,
            onlineresource_set=onlineresource_set,
        )

        observation_read.additional_properties = d
        return observation_read

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
