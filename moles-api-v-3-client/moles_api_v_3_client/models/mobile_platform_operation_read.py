from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.status_enum import StatusEnum

if TYPE_CHECKING:
    from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
    from ..models.simple_read import SimpleRead
    from ..models.time_period import TimePeriod


T = TypeVar("T", bound="MobilePlatformOperationRead")


@_attrs_define
class MobilePlatformOperationRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            uuid (None | str):
            short_code (None | str):
            title (None | str):
            abstract (None | str):
            status (BlankEnum | None | StatusEnum):
            platform_field (None | SimpleRead):
            location (GeographicBoundingBoxRead | None):
            operation_time (None | TimePeriod):
            child_operation (None | SimpleRead):
    """

    ob_id: int | None
    uuid: None | str
    short_code: None | str
    title: None | str
    abstract: None | str
    status: BlankEnum | None | StatusEnum
    platform_field: None | SimpleRead
    location: GeographicBoundingBoxRead | None
    operation_time: None | TimePeriod
    child_operation: None | SimpleRead
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
        from ..models.simple_read import SimpleRead
        from ..models.time_period import TimePeriod

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

        status: None | str
        if isinstance(self.status, StatusEnum):
            status = self.status.value
        elif isinstance(self.status, BlankEnum):
            status = self.status.value
        else:
            status = self.status

        platform_field: dict[str, Any] | None
        if isinstance(self.platform_field, SimpleRead):
            platform_field = self.platform_field.to_dict()
        else:
            platform_field = self.platform_field

        location: dict[str, Any] | None
        if isinstance(self.location, GeographicBoundingBoxRead):
            location = self.location.to_dict()
        else:
            location = self.location

        operation_time: dict[str, Any] | None
        if isinstance(self.operation_time, TimePeriod):
            operation_time = self.operation_time.to_dict()
        else:
            operation_time = self.operation_time

        child_operation: dict[str, Any] | None
        if isinstance(self.child_operation, SimpleRead):
            child_operation = self.child_operation.to_dict()
        else:
            child_operation = self.child_operation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "short_code": short_code,
                "title": title,
                "abstract": abstract,
                "status": status,
                "platform_field": platform_field,
                "location": location,
                "operationTime": operation_time,
                "childOperation": child_operation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.geographic_bounding_box_read import GeographicBoundingBoxRead
        from ..models.simple_read import SimpleRead
        from ..models.time_period import TimePeriod

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

        def _parse_status(data: object) -> BlankEnum | None | StatusEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = StatusEnum(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = BlankEnum(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | None | StatusEnum, data)

        status = _parse_status(d.pop("status"))

        def _parse_platform_field(data: object) -> None | SimpleRead:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_field_type_1 = SimpleRead.from_dict(data)

                return platform_field_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SimpleRead, data)

        platform_field = _parse_platform_field(d.pop("platform_field"))

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

        def _parse_operation_time(data: object) -> None | TimePeriod:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                operation_time_type_1 = TimePeriod.from_dict(data)

                return operation_time_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TimePeriod, data)

        operation_time = _parse_operation_time(d.pop("operationTime"))

        def _parse_child_operation(data: object) -> None | SimpleRead:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                child_operation_type_1 = SimpleRead.from_dict(data)

                return child_operation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SimpleRead, data)

        child_operation = _parse_child_operation(d.pop("childOperation"))

        mobile_platform_operation_read = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            status=status,
            platform_field=platform_field,
            location=location,
            operation_time=operation_time,
            child_operation=child_operation,
        )

        mobile_platform_operation_read.additional_properties = d
        return mobile_platform_operation_read

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
