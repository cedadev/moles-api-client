from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.platform_type_enum import PlatformTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlatformWrite")


@_attrs_define
class PlatformWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            title (str):
            abstract (Union[Unset, str]):
            keywords (Union[Unset, str]):
            platform_type (Union[BlankEnum, PlatformTypeEnum, Unset]):
    """

    ob_id: int
    title: str
    abstract: Union[Unset, str] = UNSET
    keywords: Union[Unset, str] = UNSET
    platform_type: Union[BlankEnum, PlatformTypeEnum, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        title = self.title

        abstract = self.abstract

        keywords = self.keywords

        platform_type: Union[Unset, str]
        if isinstance(self.platform_type, Unset):
            platform_type = UNSET
        elif isinstance(self.platform_type, PlatformTypeEnum):
            platform_type = self.platform_type.value
        else:
            platform_type = self.platform_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "title": title,
            }
        )
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if platform_type is not UNSET:
            field_dict["platformType"] = platform_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        title = d.pop("title")

        abstract = d.pop("abstract", UNSET)

        keywords = d.pop("keywords", UNSET)

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

        platform_write = cls(
            ob_id=ob_id,
            title=title,
            abstract=abstract,
            keywords=keywords,
            platform_type=platform_type,
        )

        platform_write.additional_properties = d
        return platform_write

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
