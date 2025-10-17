import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.language_enum import LanguageEnum
from ..models.publication_state_cbb_enum import PublicationStateCbbEnum
from ..models.status_enum import StatusEnum
from ..models.update_frequency_enum import UpdateFrequencyEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constraints_read import ConstraintsRead
    from ..models.discovery_service_id_read import DiscoveryServiceIdRead
    from ..models.dq_conformance_result_read import DQConformanceResultRead
    from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
    from ..models.inspire_theme_read import InspireThemeRead
    from ..models.referenceable import Referenceable
    from ..models.related_result import RelatedResult
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
            title (str):
            abstract (str):
            creation_date (Union[None, datetime.datetime]):
            last_updated_date (Union[None, datetime.datetime]):
            latest_data_update_time (Union[None, datetime.datetime]):
            update_frequency (UpdateFrequencyEnum): * `continual` - continual
                * `daily` - daily
                * `weekly` - weekly
                * `fortnightly` - fortnightly
                * `monthly` - monthly
                * `quarterly` - quarterly
                * `biannually` - biannually
                * `annually` - annually
                * `asNeeded` - as needed
                * `irregular` - irregular
                * `notPlanned` - not planned
                * `unknown` - unknown
            data_lineage (str):
            removed_data_reason (str):
            keywords (str):
            publication_state (PublicationStateCbbEnum): * `working` - Working
                * `preview` - Preview
                * `published` - Published
                * `citable` - Citable
                * `old` - Old
                * `removed` - Removed
            non_geographic_flag (bool):
            dont_harvest_from_projects (bool):
            geographic_extent (Union['GeographicBoundingBoxRead', None]):
            language (LanguageEnum): * `English` - English
            resolution (str):
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
            vertical_extent (Union['VerticalExtentRead', None]):
            result_field (RelatedResult):
            time_period (Union['TimePeriod', None]):
            result_quality (Union['DQConformanceResultRead', None]):
            data_published_time (Union[None, datetime.datetime]):
            doi_published_time (Union[None, datetime.datetime]):
            removed_data_time (Union[None, datetime.datetime]):
            valid_time_period (Union['TimePeriod', None]):
            procedure_acquisition (Union['Referenceable', None]):
            procedure_computation (Union['Referenceable', None]):
            procedure_composite_process (Union['Referenceable', None]):
            image_details (list[int]):
            discovery_keywords (list['DiscoveryServiceIdRead']):
            permissions (list['ConstraintsRead']):
            projects (list['Referenceable']):
            inspire_theme (list['InspireThemeRead']):
            topic_category (list['TopicCategoryRead']):
            vocabulary_keywords (list['VocabularyTermRead']):
            responsiblepartyinfo_set (list[int]):
            observationcollection_set (list[int]):
            phenomena (list[int]):
            identifier_set (list[int]):
            uuid (Union[Unset, str]):
    """

    title: str
    abstract: str
    creation_date: Union[None, datetime.datetime]
    last_updated_date: Union[None, datetime.datetime]
    latest_data_update_time: Union[None, datetime.datetime]
    update_frequency: UpdateFrequencyEnum
    data_lineage: str
    removed_data_reason: str
    keywords: str
    publication_state: PublicationStateCbbEnum
    non_geographic_flag: bool
    dont_harvest_from_projects: bool
    geographic_extent: Union["GeographicBoundingBoxRead", None]
    language: LanguageEnum
    resolution: str
    status: StatusEnum
    vertical_extent: Union["VerticalExtentRead", None]
    result_field: "RelatedResult"
    time_period: Union["TimePeriod", None]
    result_quality: Union["DQConformanceResultRead", None]
    data_published_time: Union[None, datetime.datetime]
    doi_published_time: Union[None, datetime.datetime]
    removed_data_time: Union[None, datetime.datetime]
    valid_time_period: Union["TimePeriod", None]
    procedure_acquisition: Union["Referenceable", None]
    procedure_computation: Union["Referenceable", None]
    procedure_composite_process: Union["Referenceable", None]
    image_details: list[int]
    discovery_keywords: list["DiscoveryServiceIdRead"]
    permissions: list["ConstraintsRead"]
    projects: list["Referenceable"]
    inspire_theme: list["InspireThemeRead"]
    topic_category: list["TopicCategoryRead"]
    vocabulary_keywords: list["VocabularyTermRead"]
    responsiblepartyinfo_set: list[int]
    observationcollection_set: list[int]
    phenomena: list[int]
    identifier_set: list[int]
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dq_conformance_result_read import DQConformanceResultRead
        from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
        from ..models.referenceable import Referenceable
        from ..models.time_period import TimePeriod
        from ..models.vertical_extent_read import VerticalExtentRead

        title = self.title

        abstract = self.abstract

        creation_date: Union[None, str]
        if isinstance(self.creation_date, datetime.datetime):
            creation_date = self.creation_date.isoformat()
        else:
            creation_date = self.creation_date

        last_updated_date: Union[None, str]
        if isinstance(self.last_updated_date, datetime.datetime):
            last_updated_date = self.last_updated_date.isoformat()
        else:
            last_updated_date = self.last_updated_date

        latest_data_update_time: Union[None, str]
        if isinstance(self.latest_data_update_time, datetime.datetime):
            latest_data_update_time = self.latest_data_update_time.isoformat()
        else:
            latest_data_update_time = self.latest_data_update_time

        update_frequency = self.update_frequency.value

        data_lineage = self.data_lineage

        removed_data_reason = self.removed_data_reason

        keywords = self.keywords

        publication_state = self.publication_state.value

        non_geographic_flag = self.non_geographic_flag

        dont_harvest_from_projects = self.dont_harvest_from_projects

        geographic_extent: Union[None, dict[str, Any]]
        if isinstance(self.geographic_extent, GeographicBoundingBoxRead):
            geographic_extent = self.geographic_extent.to_dict()
        else:
            geographic_extent = self.geographic_extent

        language = self.language.value

        resolution = self.resolution

        status = self.status.value

        vertical_extent: Union[None, dict[str, Any]]
        if isinstance(self.vertical_extent, VerticalExtentRead):
            vertical_extent = self.vertical_extent.to_dict()
        else:
            vertical_extent = self.vertical_extent

        result_field = self.result_field.to_dict()

        time_period: Union[None, dict[str, Any]]
        if isinstance(self.time_period, TimePeriod):
            time_period = self.time_period.to_dict()
        else:
            time_period = self.time_period

        result_quality: Union[None, dict[str, Any]]
        if isinstance(self.result_quality, DQConformanceResultRead):
            result_quality = self.result_quality.to_dict()
        else:
            result_quality = self.result_quality

        data_published_time: Union[None, str]
        if isinstance(self.data_published_time, datetime.datetime):
            data_published_time = self.data_published_time.isoformat()
        else:
            data_published_time = self.data_published_time

        doi_published_time: Union[None, str]
        if isinstance(self.doi_published_time, datetime.datetime):
            doi_published_time = self.doi_published_time.isoformat()
        else:
            doi_published_time = self.doi_published_time

        removed_data_time: Union[None, str]
        if isinstance(self.removed_data_time, datetime.datetime):
            removed_data_time = self.removed_data_time.isoformat()
        else:
            removed_data_time = self.removed_data_time

        valid_time_period: Union[None, dict[str, Any]]
        if isinstance(self.valid_time_period, TimePeriod):
            valid_time_period = self.valid_time_period.to_dict()
        else:
            valid_time_period = self.valid_time_period

        procedure_acquisition: Union[None, dict[str, Any]]
        if isinstance(self.procedure_acquisition, Referenceable):
            procedure_acquisition = self.procedure_acquisition.to_dict()
        else:
            procedure_acquisition = self.procedure_acquisition

        procedure_computation: Union[None, dict[str, Any]]
        if isinstance(self.procedure_computation, Referenceable):
            procedure_computation = self.procedure_computation.to_dict()
        else:
            procedure_computation = self.procedure_computation

        procedure_composite_process: Union[None, dict[str, Any]]
        if isinstance(self.procedure_composite_process, Referenceable):
            procedure_composite_process = self.procedure_composite_process.to_dict()
        else:
            procedure_composite_process = self.procedure_composite_process

        image_details = self.image_details

        discovery_keywords = []
        for discovery_keywords_item_data in self.discovery_keywords:
            discovery_keywords_item = discovery_keywords_item_data.to_dict()
            discovery_keywords.append(discovery_keywords_item)

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.to_dict()
            permissions.append(permissions_item)

        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        inspire_theme = []
        for inspire_theme_item_data in self.inspire_theme:
            inspire_theme_item = inspire_theme_item_data.to_dict()
            inspire_theme.append(inspire_theme_item)

        topic_category = []
        for topic_category_item_data in self.topic_category:
            topic_category_item = topic_category_item_data.to_dict()
            topic_category.append(topic_category_item)

        vocabulary_keywords = []
        for vocabulary_keywords_item_data in self.vocabulary_keywords:
            vocabulary_keywords_item = vocabulary_keywords_item_data.to_dict()
            vocabulary_keywords.append(vocabulary_keywords_item)

        responsiblepartyinfo_set = self.responsiblepartyinfo_set

        observationcollection_set = self.observationcollection_set

        phenomena = self.phenomena

        identifier_set = self.identifier_set

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
                "geographicExtent": geographic_extent,
                "language": language,
                "resolution": resolution,
                "status": status,
                "verticalExtent": vertical_extent,
                "result_field": result_field,
                "timePeriod": time_period,
                "resultQuality": result_quality,
                "dataPublishedTime": data_published_time,
                "doiPublishedTime": doi_published_time,
                "removedDataTime": removed_data_time,
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
                "vocabularyKeywords": vocabulary_keywords,
                "responsiblepartyinfo_set": responsiblepartyinfo_set,
                "observationcollection_set": observationcollection_set,
                "phenomena": phenomena,
                "identifier_set": identifier_set,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constraints_read import ConstraintsRead
        from ..models.discovery_service_id_read import DiscoveryServiceIdRead
        from ..models.dq_conformance_result_read import DQConformanceResultRead
        from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
        from ..models.inspire_theme_read import InspireThemeRead
        from ..models.referenceable import Referenceable
        from ..models.related_result import RelatedResult
        from ..models.time_period import TimePeriod
        from ..models.topic_category_read import TopicCategoryRead
        from ..models.vertical_extent_read import VerticalExtentRead
        from ..models.vocabulary_term_read import VocabularyTermRead

        d = dict(src_dict)
        title = d.pop("title")

        abstract = d.pop("abstract")

        def _parse_creation_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_date_type_0 = isoparse(data)

                return creation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        creation_date = _parse_creation_date(d.pop("creationDate"))

        def _parse_last_updated_date(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_date_type_0 = isoparse(data)

                return last_updated_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        last_updated_date = _parse_last_updated_date(d.pop("lastUpdatedDate"))

        def _parse_latest_data_update_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_data_update_time_type_0 = isoparse(data)

                return latest_data_update_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        latest_data_update_time = _parse_latest_data_update_time(d.pop("latestDataUpdateTime"))

        update_frequency = UpdateFrequencyEnum(d.pop("updateFrequency"))

        data_lineage = d.pop("dataLineage")

        removed_data_reason = d.pop("removedDataReason")

        keywords = d.pop("keywords")

        publication_state = PublicationStateCbbEnum(d.pop("publicationState"))

        non_geographic_flag = d.pop("nonGeographicFlag")

        dont_harvest_from_projects = d.pop("dontHarvestFromProjects")

        def _parse_geographic_extent(data: object) -> Union["GeographicBoundingBoxRead", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                geographic_extent_type_1 = GeographicBoundingBoxRead.from_dict(data)

                return geographic_extent_type_1
            except:  # noqa: E722
                pass
            return cast(Union["GeographicBoundingBoxRead", None], data)

        geographic_extent = _parse_geographic_extent(d.pop("geographicExtent"))

        language = LanguageEnum(d.pop("language"))

        resolution = d.pop("resolution")

        status = StatusEnum(d.pop("status"))

        def _parse_vertical_extent(data: object) -> Union["VerticalExtentRead", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vertical_extent_type_1 = VerticalExtentRead.from_dict(data)

                return vertical_extent_type_1
            except:  # noqa: E722
                pass
            return cast(Union["VerticalExtentRead", None], data)

        vertical_extent = _parse_vertical_extent(d.pop("verticalExtent"))

        result_field = RelatedResult.from_dict(d.pop("result_field"))

        def _parse_time_period(data: object) -> Union["TimePeriod", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_period_type_1 = TimePeriod.from_dict(data)

                return time_period_type_1
            except:  # noqa: E722
                pass
            return cast(Union["TimePeriod", None], data)

        time_period = _parse_time_period(d.pop("timePeriod"))

        def _parse_result_quality(data: object) -> Union["DQConformanceResultRead", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_quality_type_1 = DQConformanceResultRead.from_dict(data)

                return result_quality_type_1
            except:  # noqa: E722
                pass
            return cast(Union["DQConformanceResultRead", None], data)

        result_quality = _parse_result_quality(d.pop("resultQuality"))

        def _parse_data_published_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_published_time_type_0 = isoparse(data)

                return data_published_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        data_published_time = _parse_data_published_time(d.pop("dataPublishedTime"))

        def _parse_doi_published_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                doi_published_time_type_0 = isoparse(data)

                return doi_published_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        doi_published_time = _parse_doi_published_time(d.pop("doiPublishedTime"))

        def _parse_removed_data_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                removed_data_time_type_0 = isoparse(data)

                return removed_data_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        removed_data_time = _parse_removed_data_time(d.pop("removedDataTime"))

        def _parse_valid_time_period(data: object) -> Union["TimePeriod", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                valid_time_period_type_1 = TimePeriod.from_dict(data)

                return valid_time_period_type_1
            except:  # noqa: E722
                pass
            return cast(Union["TimePeriod", None], data)

        valid_time_period = _parse_valid_time_period(d.pop("validTimePeriod"))

        def _parse_procedure_acquisition(data: object) -> Union["Referenceable", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                procedure_acquisition_type_1 = Referenceable.from_dict(data)

                return procedure_acquisition_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Referenceable", None], data)

        procedure_acquisition = _parse_procedure_acquisition(d.pop("procedureAcquisition"))

        def _parse_procedure_computation(data: object) -> Union["Referenceable", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                procedure_computation_type_1 = Referenceable.from_dict(data)

                return procedure_computation_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Referenceable", None], data)

        procedure_computation = _parse_procedure_computation(d.pop("procedureComputation"))

        def _parse_procedure_composite_process(data: object) -> Union["Referenceable", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                procedure_composite_process_type_1 = Referenceable.from_dict(data)

                return procedure_composite_process_type_1
            except:  # noqa: E722
                pass
            return cast(Union["Referenceable", None], data)

        procedure_composite_process = _parse_procedure_composite_process(d.pop("procedureCompositeProcess"))

        image_details = cast(list[int], d.pop("imageDetails"))

        discovery_keywords = []
        _discovery_keywords = d.pop("discoveryKeywords")
        for discovery_keywords_item_data in _discovery_keywords:
            discovery_keywords_item = DiscoveryServiceIdRead.from_dict(discovery_keywords_item_data)

            discovery_keywords.append(discovery_keywords_item)

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = ConstraintsRead.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = Referenceable.from_dict(projects_item_data)

            projects.append(projects_item)

        inspire_theme = []
        _inspire_theme = d.pop("inspireTheme")
        for inspire_theme_item_data in _inspire_theme:
            inspire_theme_item = InspireThemeRead.from_dict(inspire_theme_item_data)

            inspire_theme.append(inspire_theme_item)

        topic_category = []
        _topic_category = d.pop("topicCategory")
        for topic_category_item_data in _topic_category:
            topic_category_item = TopicCategoryRead.from_dict(topic_category_item_data)

            topic_category.append(topic_category_item)

        vocabulary_keywords = []
        _vocabulary_keywords = d.pop("vocabularyKeywords")
        for vocabulary_keywords_item_data in _vocabulary_keywords:
            vocabulary_keywords_item = VocabularyTermRead.from_dict(vocabulary_keywords_item_data)

            vocabulary_keywords.append(vocabulary_keywords_item)

        responsiblepartyinfo_set = cast(list[int], d.pop("responsiblepartyinfo_set"))

        observationcollection_set = cast(list[int], d.pop("observationcollection_set"))

        phenomena = cast(list[int], d.pop("phenomena"))

        identifier_set = cast(list[int], d.pop("identifier_set"))

        uuid = d.pop("uuid", UNSET)

        observation_read = cls(
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
            responsiblepartyinfo_set=responsiblepartyinfo_set,
            observationcollection_set=observationcollection_set,
            phenomena=phenomena,
            identifier_set=identifier_set,
            uuid=uuid,
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
