from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.publication_state_6f9_enum import PublicationState6F9Enum
from ..models.status_enum import StatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectWriteRequest")


@_attrs_define
class ProjectWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            title (str):
            abstract (None | str | Unset):
            publication_state (BlankEnum | PublicationState6F9Enum | Unset):
            parent_project (int | None | Unset):
            keywords (str | Unset):
            status (BlankEnum | StatusEnum | Unset):
            image_details (list[int] | Unset):
            observation_collection (list[str] | Unset):
    """

    title: str
    abstract: None | str | Unset = UNSET
    publication_state: BlankEnum | PublicationState6F9Enum | Unset = UNSET
    parent_project: int | None | Unset = UNSET
    keywords: str | Unset = UNSET
    status: BlankEnum | StatusEnum | Unset = UNSET
    image_details: list[int] | Unset = UNSET
    observation_collection: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        abstract: None | str | Unset
        if isinstance(self.abstract, Unset):
            abstract = UNSET
        else:
            abstract = self.abstract

        publication_state: str | Unset
        if isinstance(self.publication_state, Unset):
            publication_state = UNSET
        elif isinstance(self.publication_state, PublicationState6F9Enum):
            publication_state = self.publication_state.value
        else:
            publication_state = self.publication_state.value

        parent_project: int | None | Unset
        if isinstance(self.parent_project, Unset):
            parent_project = UNSET
        else:
            parent_project = self.parent_project

        keywords = self.keywords

        status: str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, StatusEnum):
            status = self.status.value
        else:
            status = self.status.value

        image_details: list[int] | Unset = UNSET
        if not isinstance(self.image_details, Unset):
            image_details = ",".join(map(str, self.image_details))

        observation_collection: list[str] | Unset = UNSET
        if not isinstance(self.observation_collection, Unset):
            observation_collection = ",".join(map(str, self.observation_collection))

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        if observation_collection is not UNSET:
            field_dict["observationCollection"] = observation_collection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        def _parse_abstract(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        abstract = _parse_abstract(d.pop("abstract", UNSET))

        def _parse_publication_state(data: object) -> BlankEnum | PublicationState6F9Enum | Unset:
            if isinstance(data, Unset):
                return data
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

        publication_state = _parse_publication_state(d.pop("publicationState", UNSET))

        def _parse_parent_project(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_project = _parse_parent_project(d.pop("parentProject", UNSET))

        keywords = d.pop("keywords", UNSET)

        def _parse_status(data: object) -> BlankEnum | StatusEnum | Unset:
            if isinstance(data, Unset):
                return data
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

        status = _parse_status(d.pop("status", UNSET))

        image_details = cast(list[int], d.pop("imageDetails", UNSET))

        observation_collection = cast(list[str], d.pop("observationCollection", UNSET))

        project_write_request = cls(
            title=title,
            abstract=abstract,
            publication_state=publication_state,
            parent_project=parent_project,
            keywords=keywords,
            status=status,
            image_details=image_details,
            observation_collection=observation_collection,
        )

        project_write_request.additional_properties = d
        return project_write_request

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
