from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.publication_state_6f9_enum import PublicationState6F9Enum
from ..models.status_enum import StatusEnum

if TYPE_CHECKING:
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="ProjectRead")


@_attrs_define
class ProjectRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            uuid (str):
            short_code (str):
            title (str):
            abstract (None | str):
            publication_state (BlankEnum | PublicationState6F9Enum):
            keywords (str):
            status (BlankEnum | StatusEnum):
            parent_project (None | SimpleRead):
            sub_project (list[SimpleRead] | None):
            image_details (list[int | None]):
            observation_collection (list[SimpleRead] | None):
            identifier_set (list[int | None]):
            responsiblepartyinfo_set (list[int | None]):
            onlineresource_set (list[int | None]):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    abstract: None | str
    publication_state: BlankEnum | PublicationState6F9Enum
    keywords: str
    status: BlankEnum | StatusEnum
    parent_project: None | SimpleRead
    sub_project: list[SimpleRead] | None
    image_details: list[int | None]
    observation_collection: list[SimpleRead] | None
    identifier_set: list[int | None]
    responsiblepartyinfo_set: list[int | None]
    onlineresource_set: list[int | None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_read import SimpleRead

        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        abstract: None | str
        abstract = self.abstract

        publication_state: str
        if isinstance(self.publication_state, PublicationState6F9Enum):
            publication_state = self.publication_state.value
        else:
            publication_state = self.publication_state.value

        keywords = self.keywords

        status: str
        if isinstance(self.status, StatusEnum):
            status = self.status.value
        else:
            status = self.status.value

        parent_project: dict[str, Any] | None
        if isinstance(self.parent_project, SimpleRead):
            parent_project = self.parent_project.to_dict()
        else:
            parent_project = self.parent_project

        sub_project: list[dict[str, Any]] | None
        if isinstance(self.sub_project, list):
            sub_project = []
            for sub_project_type_0_item_data in self.sub_project:
                sub_project_type_0_item = sub_project_type_0_item_data.to_dict()
                sub_project.append(sub_project_type_0_item)

        else:
            sub_project = self.sub_project

        image_details = []
        for image_details_item_data in self.image_details:
            image_details_item: int | None
            image_details_item = image_details_item_data
            image_details.append(image_details_item)

        observation_collection: list[dict[str, Any]] | None
        if isinstance(self.observation_collection, list):
            observation_collection = []
            for observation_collection_type_0_item_data in self.observation_collection:
                observation_collection_type_0_item = observation_collection_type_0_item_data.to_dict()
                observation_collection.append(observation_collection_type_0_item)

        else:
            observation_collection = self.observation_collection

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "short_code": short_code,
                "title": title,
                "abstract": abstract,
                "publicationState": publication_state,
                "keywords": keywords,
                "status": status,
                "parentProject": parent_project,
                "subProject": sub_project,
                "imageDetails": image_details,
                "observationCollection": observation_collection,
                "identifier_set": identifier_set,
                "responsiblepartyinfo_set": responsiblepartyinfo_set,
                "onlineresource_set": onlineresource_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_read import SimpleRead

        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        uuid = d.pop("uuid")

        short_code = d.pop("short_code")

        title = d.pop("title")

        def _parse_abstract(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        abstract = _parse_abstract(d.pop("abstract"))

        def _parse_publication_state(data: object) -> BlankEnum | PublicationState6F9Enum:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publication_state_type_0 = PublicationState6F9Enum(data)

                return publication_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            publication_state_type_1 = BlankEnum(data)

            return publication_state_type_1

        publication_state = _parse_publication_state(d.pop("publicationState"))

        keywords = d.pop("keywords")

        def _parse_status(data: object) -> BlankEnum | StatusEnum:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = StatusEnum(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            status_type_1 = BlankEnum(data)

            return status_type_1

        status = _parse_status(d.pop("status"))

        def _parse_parent_project(data: object) -> None | SimpleRead:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_project_type_1 = SimpleRead.from_dict(data)

                return parent_project_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SimpleRead, data)

        parent_project = _parse_parent_project(d.pop("parentProject"))

        def _parse_sub_project(data: object) -> list[SimpleRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sub_project_type_0 = []
                _sub_project_type_0 = data
                for sub_project_type_0_item_data in _sub_project_type_0:
                    sub_project_type_0_item = SimpleRead.from_dict(sub_project_type_0_item_data)

                    sub_project_type_0.append(sub_project_type_0_item)

                return sub_project_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleRead] | None, data)

        sub_project = _parse_sub_project(d.pop("subProject"))

        image_details = []
        _image_details = d.pop("imageDetails")
        for image_details_item_data in _image_details:

            def _parse_image_details_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            image_details_item = _parse_image_details_item(image_details_item_data)

            image_details.append(image_details_item)

        def _parse_observation_collection(data: object) -> list[SimpleRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                observation_collection_type_0 = []
                _observation_collection_type_0 = data
                for observation_collection_type_0_item_data in _observation_collection_type_0:
                    observation_collection_type_0_item = SimpleRead.from_dict(observation_collection_type_0_item_data)

                    observation_collection_type_0.append(observation_collection_type_0_item)

                return observation_collection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleRead] | None, data)

        observation_collection = _parse_observation_collection(d.pop("observationCollection"))

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

        project_read = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            publication_state=publication_state,
            keywords=keywords,
            status=status,
            parent_project=parent_project,
            sub_project=sub_project,
            image_details=image_details,
            observation_collection=observation_collection,
            identifier_set=identifier_set,
            responsiblepartyinfo_set=responsiblepartyinfo_set,
            onlineresource_set=onlineresource_set,
        )

        project_read.additional_properties = d
        return project_read

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
