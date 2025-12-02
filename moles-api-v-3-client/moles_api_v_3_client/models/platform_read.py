from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.platform_type_enum import PlatformTypeEnum

if TYPE_CHECKING:
    from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="PlatformRead")


@_attrs_define
class PlatformRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            uuid (None | str):
            short_code (None | str):
            title (None | str):
            abstract (None | str):
            keywords (None | str):
            platform_type (BlankEnum | None | PlatformTypeEnum):
            location (GeographicBoundingBoxRead | None):
            image_details (list[int | None]):
            child_platform (list[SimpleRead] | None):
            parent_platform (list[SimpleRead] | None):
            identifier_set (list[int | None]):
            responsiblepartyinfo_set (list[int | None]):
            onlineresource_set (list[int | None]):
    """

    ob_id: int | None
    uuid: None | str
    short_code: None | str
    title: None | str
    abstract: None | str
    keywords: None | str
    platform_type: BlankEnum | None | PlatformTypeEnum
    location: GeographicBoundingBoxRead | None
    image_details: list[int | None]
    child_platform: list[SimpleRead] | None
    parent_platform: list[SimpleRead] | None
    identifier_set: list[int | None]
    responsiblepartyinfo_set: list[int | None]
    onlineresource_set: list[int | None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead

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

        platform_type: None | str
        if isinstance(self.platform_type, PlatformTypeEnum):
            platform_type = self.platform_type.value
        elif isinstance(self.platform_type, BlankEnum):
            platform_type = self.platform_type.value
        else:
            platform_type = self.platform_type

        location: dict[str, Any] | None
        if isinstance(self.location, GeographicBoundingBoxRead):
            location = self.location.to_dict()
        else:
            location = self.location

        image_details = []
        for image_details_item_data in self.image_details:
            image_details_item: int | None
            image_details_item = image_details_item_data
            image_details.append(image_details_item)

        child_platform: list[dict[str, Any]] | None
        if isinstance(self.child_platform, list):
            child_platform = []
            for child_platform_type_0_item_data in self.child_platform:
                child_platform_type_0_item = child_platform_type_0_item_data.to_dict()
                child_platform.append(child_platform_type_0_item)

        else:
            child_platform = self.child_platform

        parent_platform: list[dict[str, Any]] | None
        if isinstance(self.parent_platform, list):
            parent_platform = []
            for parent_platform_type_0_item_data in self.parent_platform:
                parent_platform_type_0_item = parent_platform_type_0_item_data.to_dict()
                parent_platform.append(parent_platform_type_0_item)

        else:
            parent_platform = self.parent_platform

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
                "keywords": keywords,
                "platformType": platform_type,
                "location": location,
                "imageDetails": image_details,
                "childPlatform": child_platform,
                "parentPlatform": parent_platform,
                "identifier_set": identifier_set,
                "responsiblepartyinfo_set": responsiblepartyinfo_set,
                "onlineresource_set": onlineresource_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
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

        def _parse_platform_type(data: object) -> BlankEnum | None | PlatformTypeEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_type_0 = PlatformTypeEnum(data)

                return platform_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                platform_type_type_1 = BlankEnum(data)

                return platform_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | PlatformTypeEnum, data)

        platform_type = _parse_platform_type(d.pop("platformType"))

        def _parse_location(data: object) -> GeographicBoundingBoxRead | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_1 = GeographicBoundingBoxRead.from_dict(data)

                return location_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GeographicBoundingBoxRead | None, data)

        location = _parse_location(d.pop("location"))

        image_details = []
        _image_details = d.pop("imageDetails")
        for image_details_item_data in _image_details:

            def _parse_image_details_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            image_details_item = _parse_image_details_item(image_details_item_data)

            image_details.append(image_details_item)

        def _parse_child_platform(data: object) -> list[SimpleRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                child_platform_type_0 = []
                _child_platform_type_0 = data
                for child_platform_type_0_item_data in _child_platform_type_0:
                    child_platform_type_0_item = SimpleRead.from_dict(child_platform_type_0_item_data)

                    child_platform_type_0.append(child_platform_type_0_item)

                return child_platform_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleRead] | None, data)

        child_platform = _parse_child_platform(d.pop("childPlatform"))

        def _parse_parent_platform(data: object) -> list[SimpleRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                parent_platform_type_0 = []
                _parent_platform_type_0 = data
                for parent_platform_type_0_item_data in _parent_platform_type_0:
                    parent_platform_type_0_item = SimpleRead.from_dict(parent_platform_type_0_item_data)

                    parent_platform_type_0.append(parent_platform_type_0_item)

                return parent_platform_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleRead] | None, data)

        parent_platform = _parse_parent_platform(d.pop("parentPlatform"))

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

        platform_read = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            keywords=keywords,
            platform_type=platform_type,
            location=location,
            image_details=image_details,
            child_platform=child_platform,
            parent_platform=parent_platform,
            identifier_set=identifier_set,
            responsiblepartyinfo_set=responsiblepartyinfo_set,
            onlineresource_set=onlineresource_set,
        )

        platform_read.additional_properties = d
        return platform_read

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
