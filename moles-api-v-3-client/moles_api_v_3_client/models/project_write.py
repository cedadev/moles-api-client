from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum
from ..models.project_write_publication_state_enum import ProjectWritePublicationStateEnum
from ..models.status_enum import StatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectWrite")


@_attrs_define
class ProjectWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            uuid (str):
            short_code (str):
            title (str):
            observation_collection (list[str]):
            abstract (Union[None, Unset, str]):
            publication_state (Union[BlankEnum, ProjectWritePublicationStateEnum, Unset]):
            parent_project (Union[None, Unset, int]):
            keywords (Union[Unset, str]):
            status (Union[BlankEnum, StatusEnum, Unset]):
            image_details (Union[Unset, list[int]]):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    observation_collection: list[str]
    abstract: Union[None, Unset, str] = UNSET
    publication_state: Union[BlankEnum, ProjectWritePublicationStateEnum, Unset] = UNSET
    parent_project: Union[None, Unset, int] = UNSET
    keywords: Union[Unset, str] = UNSET
    status: Union[BlankEnum, StatusEnum, Unset] = UNSET
    image_details: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        observation_collection = self.observation_collection

        abstract: Union[None, Unset, str]
        if isinstance(self.abstract, Unset):
            abstract = UNSET
        else:
            abstract = self.abstract

        publication_state: Union[Unset, str]
        if isinstance(self.publication_state, Unset):
            publication_state = UNSET
        elif isinstance(self.publication_state, ProjectWritePublicationStateEnum):
            publication_state = self.publication_state.value
        else:
            publication_state = self.publication_state.value

        parent_project: Union[None, Unset, int]
        if isinstance(self.parent_project, Unset):
            parent_project = UNSET
        else:
            parent_project = self.parent_project

        keywords = self.keywords

        status: Union[Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, StatusEnum):
            status = self.status.value
        else:
            status = self.status.value

        image_details: Union[Unset, list[int]] = UNSET
        if not isinstance(self.image_details, Unset):
            image_details = self.image_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "short_code": short_code,
                "title": title,
                "observationCollection": observation_collection,
            }
        )
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if publication_state is not UNSET:
            field_dict["publicationState"] = publication_state
        if parent_project is not UNSET:
            field_dict["parentProject"] = parent_project
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if status is not UNSET:
            field_dict["status"] = status
        if image_details is not UNSET:
            field_dict["imageDetails"] = image_details

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        files.append(("uuid", (None, str(self.uuid).encode(), "text/plain")))

        files.append(("short_code", (None, str(self.short_code).encode(), "text/plain")))

        files.append(("title", (None, str(self.title).encode(), "text/plain")))

        for observation_collection_item_element in self.observation_collection:
            files.append(
                ("observationCollection", (None, str(observation_collection_item_element).encode(), "text/plain"))
            )

        if not isinstance(self.abstract, Unset):
            if isinstance(self.abstract, str):
                files.append(("abstract", (None, str(self.abstract).encode(), "text/plain")))
            else:
                files.append(("abstract", (None, str(self.abstract).encode(), "text/plain")))

        if not isinstance(self.publication_state, Unset):
            if isinstance(self.publication_state, ProjectWritePublicationStateEnum):
                files.append(("publicationState", (None, str(self.publication_state.value).encode(), "text/plain")))
            else:
                files.append(("publicationState", (None, str(self.publication_state.value).encode(), "text/plain")))

        if not isinstance(self.parent_project, Unset):
            if isinstance(self.parent_project, int):
                files.append(("parentProject", (None, str(self.parent_project).encode(), "text/plain")))
            else:
                files.append(("parentProject", (None, str(self.parent_project).encode(), "text/plain")))

        if not isinstance(self.keywords, Unset):
            files.append(("keywords", (None, str(self.keywords).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            if isinstance(self.status, StatusEnum):
                files.append(("status", (None, str(self.status.value).encode(), "text/plain")))
            else:
                files.append(("status", (None, str(self.status.value).encode(), "text/plain")))

        if not isinstance(self.image_details, Unset):
            for image_details_item_element in self.image_details:
                files.append(("imageDetails", (None, str(image_details_item_element).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        uuid = d.pop("uuid")

        short_code = d.pop("short_code")

        title = d.pop("title")

        observation_collection = cast(list[str], d.pop("observationCollection"))

        def _parse_abstract(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abstract = _parse_abstract(d.pop("abstract", UNSET))

        def _parse_publication_state(data: object) -> Union[BlankEnum, ProjectWritePublicationStateEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publication_state_type_0 = ProjectWritePublicationStateEnum(data)

                return publication_state_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            publication_state_type_1 = BlankEnum(data)

            return publication_state_type_1

        publication_state = _parse_publication_state(d.pop("publicationState", UNSET))

        def _parse_parent_project(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_project = _parse_parent_project(d.pop("parentProject", UNSET))

        keywords = d.pop("keywords", UNSET)

        def _parse_status(data: object) -> Union[BlankEnum, StatusEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = StatusEnum(data)

                return status_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            status_type_1 = BlankEnum(data)

            return status_type_1

        status = _parse_status(d.pop("status", UNSET))

        image_details = cast(list[int], d.pop("imageDetails", UNSET))

        project_write = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            observation_collection=observation_collection,
            abstract=abstract,
            publication_state=publication_state,
            parent_project=parent_project,
            keywords=keywords,
            status=status,
            image_details=image_details,
        )

        project_write.additional_properties = d
        return project_write

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
