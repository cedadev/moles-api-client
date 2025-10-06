from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum
from ..models.status_enum import StatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MobilePlatformOperationWrite")


@_attrs_define
class MobilePlatformOperationWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            uuid (str):
            short_code (str):
            title (str):
            platform_field (int):
            abstract (Union[Unset, str]):
            location (Union[None, Unset, int]):
            status (Union[BlankEnum, StatusEnum, Unset]):
            operation_time (Union[None, Unset, int]):
            child_operation (Union[None, Unset, int]):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    platform_field: int
    abstract: Union[Unset, str] = UNSET
    location: Union[None, Unset, int] = UNSET
    status: Union[BlankEnum, StatusEnum, Unset] = UNSET
    operation_time: Union[None, Unset, int] = UNSET
    child_operation: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        platform_field = self.platform_field

        abstract = self.abstract

        location: Union[None, Unset, int]
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        status: Union[Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, StatusEnum):
            status = self.status.value
        else:
            status = self.status.value

        operation_time: Union[None, Unset, int]
        if isinstance(self.operation_time, Unset):
            operation_time = UNSET
        else:
            operation_time = self.operation_time

        child_operation: Union[None, Unset, int]
        if isinstance(self.child_operation, Unset):
            child_operation = UNSET
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
                "platform_field": platform_field,
            }
        )
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if location is not UNSET:
            field_dict["location"] = location
        if status is not UNSET:
            field_dict["status"] = status
        if operation_time is not UNSET:
            field_dict["operationTime"] = operation_time
        if child_operation is not UNSET:
            field_dict["childOperation"] = child_operation

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        files.append(("uuid", (None, str(self.uuid).encode(), "text/plain")))

        files.append(("short_code", (None, str(self.short_code).encode(), "text/plain")))

        files.append(("title", (None, str(self.title).encode(), "text/plain")))

        files.append(("platform_field", (None, str(self.platform_field).encode(), "text/plain")))

        if not isinstance(self.abstract, Unset):
            files.append(("abstract", (None, str(self.abstract).encode(), "text/plain")))

        if not isinstance(self.location, Unset):
            if isinstance(self.location, int):
                files.append(("location", (None, str(self.location).encode(), "text/plain")))
            else:
                files.append(("location", (None, str(self.location).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            if isinstance(self.status, StatusEnum):
                files.append(("status", (None, str(self.status.value).encode(), "text/plain")))
            else:
                files.append(("status", (None, str(self.status.value).encode(), "text/plain")))

        if not isinstance(self.operation_time, Unset):
            if isinstance(self.operation_time, int):
                files.append(("operationTime", (None, str(self.operation_time).encode(), "text/plain")))
            else:
                files.append(("operationTime", (None, str(self.operation_time).encode(), "text/plain")))

        if not isinstance(self.child_operation, Unset):
            if isinstance(self.child_operation, int):
                files.append(("childOperation", (None, str(self.child_operation).encode(), "text/plain")))
            else:
                files.append(("childOperation", (None, str(self.child_operation).encode(), "text/plain")))

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

        platform_field = d.pop("platform_field")

        abstract = d.pop("abstract", UNSET)

        def _parse_location(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        location = _parse_location(d.pop("location", UNSET))

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

        def _parse_operation_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        operation_time = _parse_operation_time(d.pop("operationTime", UNSET))

        def _parse_child_operation(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        child_operation = _parse_child_operation(d.pop("childOperation", UNSET))

        mobile_platform_operation_write = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            platform_field=platform_field,
            abstract=abstract,
            location=location,
            status=status,
            operation_time=operation_time,
            child_operation=child_operation,
        )

        mobile_platform_operation_write.additional_properties = d
        return mobile_platform_operation_write

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
