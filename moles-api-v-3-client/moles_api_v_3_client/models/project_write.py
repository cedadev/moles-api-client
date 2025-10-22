from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.publication_state_6f9_enum import PublicationState6F9Enum
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
            abstract (Union[None, Unset, str]):
            publication_state (Union[BlankEnum, PublicationState6F9Enum, Unset]):
            parent_project (Union[None, Unset, int]):
            keywords (Union[Unset, str]):
            status (Union[BlankEnum, StatusEnum, Unset]):
            image_details (Union[Unset, list[int]]):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    abstract: Union[None, Unset, str] = UNSET
    publication_state: Union[BlankEnum, PublicationState6F9Enum, Unset] = UNSET
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

        abstract: Union[None, Unset, str]
        if isinstance(self.abstract, Unset):
            abstract = UNSET
        else:
            abstract = self.abstract

        publication_state: Union[Unset, str]
        if isinstance(self.publication_state, Unset):
            publication_state = UNSET
        elif isinstance(self.publication_state, PublicationState6F9Enum):
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        uuid = d.pop("uuid")

        short_code = d.pop("short_code")

        title = d.pop("title")

        def _parse_abstract(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abstract = _parse_abstract(d.pop("abstract", UNSET))

        def _parse_publication_state(data: object) -> Union[BlankEnum, PublicationState6F9Enum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                publication_state_type_0 = PublicationState6F9Enum(data)

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
