from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.blank_enum import BlankEnum
from ..models.publication_state_cbb_enum import PublicationStateCbbEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedObservationCollectionWriteRequest")


@_attrs_define
class PatchedObservationCollectionWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            title (str | Unset):
            abstract (str | Unset):
            keywords (str | Unset):
            publication_state (BlankEnum | PublicationStateCbbEnum | Unset):
            data_published_time (datetime.datetime | None | Unset):
            doi_published_time (datetime.datetime | None | Unset):
            dont_harvest_from_projects (bool | Unset):
            image_details (list[int] | Unset):
            discovery_keywords (list[int] | Unset):
            member (list[int] | Unset):
    """

    title: str | Unset = UNSET
    abstract: str | Unset = UNSET
    keywords: str | Unset = UNSET
    publication_state: BlankEnum | PublicationStateCbbEnum | Unset = UNSET
    data_published_time: datetime.datetime | None | Unset = UNSET
    doi_published_time: datetime.datetime | None | Unset = UNSET
    dont_harvest_from_projects: bool | Unset = UNSET
    image_details: list[int] | Unset = UNSET
    discovery_keywords: list[int] | Unset = UNSET
    member: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        abstract = self.abstract

        keywords = self.keywords

        publication_state: str | Unset
        if isinstance(self.publication_state, Unset):
            publication_state = UNSET
        elif isinstance(self.publication_state, PublicationStateCbbEnum):
            publication_state = self.publication_state.value
        else:
            publication_state = self.publication_state.value

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

        dont_harvest_from_projects = self.dont_harvest_from_projects

        image_details: list[int] | Unset = UNSET
        if not isinstance(self.image_details, Unset):
            image_details = ",".join(map(str, self.image_details))

        discovery_keywords: list[int] | Unset = UNSET
        if not isinstance(self.discovery_keywords, Unset):
            discovery_keywords = ",".join(map(str, self.discovery_keywords))

        member: list[int] | Unset = UNSET
        if not isinstance(self.member, Unset):
            member = ",".join(map(str, self.member))

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if publication_state is not UNSET:
            field_dict["publicationState"] = publication_state
        if data_published_time is not UNSET:
            field_dict["dataPublishedTime"] = data_published_time
        if doi_published_time is not UNSET:
            field_dict["doiPublishedTime"] = doi_published_time
        if dont_harvest_from_projects is not UNSET:
            field_dict["dontHarvestFromProjects"] = dont_harvest_from_projects
        if image_details is not UNSET:
            field_dict["imageDetails"] = image_details
        if discovery_keywords is not UNSET:
            field_dict["discoveryKeywords"] = discovery_keywords
        if member is not UNSET:
            field_dict["member"] = member

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        abstract = d.pop("abstract", UNSET)

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

        dont_harvest_from_projects = d.pop("dontHarvestFromProjects", UNSET)

        image_details = cast(list[int], d.pop("imageDetails", UNSET))

        discovery_keywords = cast(list[int], d.pop("discoveryKeywords", UNSET))

        member = cast(list[int], d.pop("member", UNSET))

        patched_observation_collection_write_request = cls(
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
        )

        patched_observation_collection_write_request.additional_properties = d
        return patched_observation_collection_write_request

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
