from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.platform_type_enum import PlatformTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedPlatformWriteRequest")


@_attrs_define
class PatchedPlatformWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            title (str | Unset):
            abstract (str | Unset):
            keywords (str | Unset):
            child_platform (list[str] | Unset):
            platform_type (BlankEnum | PlatformTypeEnum | Unset):
            location (int | Unset):
    """

    title: str | Unset = UNSET
    abstract: str | Unset = UNSET
    keywords: str | Unset = UNSET
    child_platform: list[str] | Unset = UNSET
    platform_type: BlankEnum | PlatformTypeEnum | Unset = UNSET
    location: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        abstract = self.abstract

        keywords = self.keywords

        child_platform: list[str] | Unset = UNSET
        if not isinstance(self.child_platform, Unset):
            child_platform = self.child_platform

        platform_type: str | Unset
        if isinstance(self.platform_type, Unset):
            platform_type = UNSET
        elif isinstance(self.platform_type, PlatformTypeEnum):
            platform_type = self.platform_type.value
        else:
            platform_type = self.platform_type.value

        location = self.location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if child_platform is not UNSET:
            field_dict["childPlatform"] = child_platform
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        abstract = d.pop("abstract", UNSET)

        keywords = d.pop("keywords", UNSET)

        child_platform = cast(list[str], d.pop("childPlatform", UNSET))

        def _parse_platform_type(data: object) -> BlankEnum | PlatformTypeEnum | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_type_0 = PlatformTypeEnum(data)

                return platform_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            platform_type_type_1 = BlankEnum(data)

            return platform_type_type_1

        platform_type = _parse_platform_type(d.pop("platformType", UNSET))

        location = d.pop("location", UNSET)

        patched_platform_write_request = cls(
            title=title,
            abstract=abstract,
            keywords=keywords,
            child_platform=child_platform,
            platform_type=platform_type,
            location=location,
        )

        patched_platform_write_request.additional_properties = d
        return patched_platform_write_request

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
