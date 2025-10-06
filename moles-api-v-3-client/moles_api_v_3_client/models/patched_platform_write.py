from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum
from ..models.platform_type_enum import PlatformTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedPlatformWrite")


@_attrs_define
class PatchedPlatformWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (Union[Unset, int]):
            title (Union[Unset, str]):
            abstract (Union[Unset, str]):
            keywords (Union[Unset, str]):
            child_platform (Union[Unset, list[str]]):
            platform_type (Union[BlankEnum, PlatformTypeEnum, Unset]):
            location (Union[Unset, int]):
    """

    ob_id: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    abstract: Union[Unset, str] = UNSET
    keywords: Union[Unset, str] = UNSET
    child_platform: Union[Unset, list[str]] = UNSET
    platform_type: Union[BlankEnum, PlatformTypeEnum, Unset] = UNSET
    location: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        title = self.title

        abstract = self.abstract

        keywords = self.keywords

        child_platform: Union[Unset, list[str]] = UNSET
        if not isinstance(self.child_platform, Unset):
            child_platform = self.child_platform

        platform_type: Union[Unset, str]
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
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.ob_id, Unset):
            files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.abstract, Unset):
            files.append(("abstract", (None, str(self.abstract).encode(), "text/plain")))

        if not isinstance(self.keywords, Unset):
            files.append(("keywords", (None, str(self.keywords).encode(), "text/plain")))

        if not isinstance(self.child_platform, Unset):
            for child_platform_item_element in self.child_platform:
                files.append(("childPlatform", (None, str(child_platform_item_element).encode(), "text/plain")))

        if not isinstance(self.platform_type, Unset):
            if isinstance(self.platform_type, PlatformTypeEnum):
                files.append(("platformType", (None, str(self.platform_type.value).encode(), "text/plain")))
            else:
                files.append(("platformType", (None, str(self.platform_type.value).encode(), "text/plain")))

        if not isinstance(self.location, Unset):
            files.append(("location", (None, str(self.location).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        title = d.pop("title", UNSET)

        abstract = d.pop("abstract", UNSET)

        keywords = d.pop("keywords", UNSET)

        child_platform = cast(list[str], d.pop("childPlatform", UNSET))

        def _parse_platform_type(data: object) -> Union[BlankEnum, PlatformTypeEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_type_0 = PlatformTypeEnum(data)

                return platform_type_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            platform_type_type_1 = BlankEnum(data)

            return platform_type_type_1

        platform_type = _parse_platform_type(d.pop("platformType", UNSET))

        location = d.pop("location", UNSET)

        patched_platform_write = cls(
            ob_id=ob_id,
            title=title,
            abstract=abstract,
            keywords=keywords,
            child_platform=child_platform,
            platform_type=platform_type,
            location=location,
        )

        patched_platform_write.additional_properties = d
        return patched_platform_write

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
