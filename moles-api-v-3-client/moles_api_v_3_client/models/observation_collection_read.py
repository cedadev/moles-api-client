from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.publication_state_cbb_enum import PublicationStateCbbEnum

if TYPE_CHECKING:
    from ..models.discovery_service_id_read import DiscoveryServiceIdRead
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="ObservationCollectionRead")


@_attrs_define
class ObservationCollectionRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            uuid (None | str):
            short_code (None | str):
            title (None | str):
            abstract (None | str):
            keywords (None | str):
            publication_state (BlankEnum | None | PublicationStateCbbEnum):
            data_published_time (datetime.datetime | None):
            doi_published_time (datetime.datetime | None):
            dont_harvest_from_projects (bool | None):
            image_details (list[int | None]):
            discovery_keywords (list[DiscoveryServiceIdRead]):
            member (list[SimpleRead] | None):
            identifier_set (list[int | None]):
            responsiblepartyinfo_set (list[int | None]):
            onlineresource_set (list[int | None]):
            project_set (list[int | None]):
    """

    ob_id: int | None
    uuid: None | str
    short_code: None | str
    title: None | str
    abstract: None | str
    keywords: None | str
    publication_state: BlankEnum | None | PublicationStateCbbEnum
    data_published_time: datetime.datetime | None
    doi_published_time: datetime.datetime | None
    dont_harvest_from_projects: bool | None
    image_details: list[int | None]
    discovery_keywords: list[DiscoveryServiceIdRead]
    member: list[SimpleRead] | None
    identifier_set: list[int | None]
    responsiblepartyinfo_set: list[int | None]
    onlineresource_set: list[int | None]
    project_set: list[int | None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: int | None
        ob_id = self.ob_id

        uuid: None | str
        uuid = self.uuid

        short_code: None | str
        short_code = self.short_code

        title: None | str
        title = self.title

        abstract: None | str
        abstract = self.abstract

        keywords: None | str
        keywords = self.keywords

        publication_state: None | str
        if isinstance(self.publication_state, PublicationStateCbbEnum):
            publication_state = self.publication_state.value
        elif isinstance(self.publication_state, BlankEnum):
            publication_state = self.publication_state.value
        else:
            publication_state = self.publication_state

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

        dont_harvest_from_projects: bool | None
        dont_harvest_from_projects = self.dont_harvest_from_projects

        image_details = []
        for image_details_item_data in self.image_details:
            image_details_item: int | None
            image_details_item = image_details_item_data
            image_details.append(image_details_item)

        discovery_keywords = []
        for discovery_keywords_item_data in self.discovery_keywords:
            discovery_keywords_item = discovery_keywords_item_data.to_dict()
            discovery_keywords.append(discovery_keywords_item)

        member: list[dict[str, Any]] | None
        if isinstance(self.member, list):
            member = []
            for member_type_0_item_data in self.member:
                member_type_0_item = member_type_0_item_data.to_dict()
                member.append(member_type_0_item)

        else:
            member = self.member

        identifier_set = []
        for identifier_set_item_data in self.identifier_set:
            identifier_set_item: int | None
            identifier_set_item = identifier_set_item_data
            identifier_set.append(identifier_set_item)

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

        project_set = []
        for project_set_item_data in self.project_set:
            project_set_item: int | None
            project_set_item = project_set_item_data
            project_set.append(project_set_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "short_code": short_code,
                "title": title,
                "abstract": abstract,
                "keywords": keywords,
                "publicationState": publication_state,
                "dataPublishedTime": data_published_time,
                "doiPublishedTime": doi_published_time,
                "dontHarvestFromProjects": dont_harvest_from_projects,
                "imageDetails": image_details,
                "discoveryKeywords": discovery_keywords,
                "member": member,
                "identifier_set": identifier_set,
                "responsiblepartyinfo_set": responsiblepartyinfo_set,
                "onlineresource_set": onlineresource_set,
                "project_set": project_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discovery_service_id_read import DiscoveryServiceIdRead
        from ..models.simple_read import SimpleRead

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

        def _parse_short_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        short_code = _parse_short_code(d.pop("short_code"))

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

        def _parse_dont_harvest_from_projects(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        dont_harvest_from_projects = _parse_dont_harvest_from_projects(d.pop("dontHarvestFromProjects"))

        image_details = []
        _image_details = d.pop("imageDetails")
        for image_details_item_data in _image_details:

            def _parse_image_details_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            image_details_item = _parse_image_details_item(image_details_item_data)

            image_details.append(image_details_item)

        discovery_keywords = []
        _discovery_keywords = d.pop("discoveryKeywords")
        for discovery_keywords_item_data in _discovery_keywords:
            discovery_keywords_item = DiscoveryServiceIdRead.from_dict(discovery_keywords_item_data)

            discovery_keywords.append(discovery_keywords_item)

        def _parse_member(data: object) -> list[SimpleRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                member_type_0 = []
                _member_type_0 = data
                for member_type_0_item_data in _member_type_0:
                    member_type_0_item = SimpleRead.from_dict(member_type_0_item_data)

                    member_type_0.append(member_type_0_item)

                return member_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleRead] | None, data)

        member = _parse_member(d.pop("member"))

        identifier_set = []
        _identifier_set = d.pop("identifier_set")
        for identifier_set_item_data in _identifier_set:

            def _parse_identifier_set_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            identifier_set_item = _parse_identifier_set_item(identifier_set_item_data)

            identifier_set.append(identifier_set_item)

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

        project_set = []
        _project_set = d.pop("project_set")
        for project_set_item_data in _project_set:

            def _parse_project_set_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            project_set_item = _parse_project_set_item(project_set_item_data)

            project_set.append(project_set_item)

        observation_collection_read = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            keywords=keywords,
            publication_state=publication_state,
            data_published_time=data_published_time,
            doi_published_time=doi_published_time,
            dont_harvest_from_projects=dont_harvest_from_projects,
            image_details=image_details,
            discovery_keywords=discovery_keywords,
            member=member,
            identifier_set=identifier_set,
            responsiblepartyinfo_set=responsiblepartyinfo_set,
            onlineresource_set=onlineresource_set,
            project_set=project_set,
        )

        observation_collection_read.additional_properties = d
        return observation_collection_read

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
