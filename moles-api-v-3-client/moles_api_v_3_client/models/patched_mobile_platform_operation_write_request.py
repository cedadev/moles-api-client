from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.status_enum import StatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedMobilePlatformOperationWriteRequest")


@_attrs_define
class PatchedMobilePlatformOperationWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            title (str | Unset):
            abstract (str | Unset):
            platform_field (int | Unset):
            location (int | None | Unset):
            status (BlankEnum | StatusEnum | Unset):
            operation_time (int | None | Unset):
            child_operation (int | None | Unset):
    """

    title: str | Unset = UNSET
    abstract: str | Unset = UNSET
    platform_field: int | Unset = UNSET
    location: int | None | Unset = UNSET
    status: BlankEnum | StatusEnum | Unset = UNSET
    operation_time: int | None | Unset = UNSET
    child_operation: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        abstract = self.abstract

        platform_field = self.platform_field

        location: int | None | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        status: str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, StatusEnum):
            status = self.status.value
        else:
            status = self.status.value

        operation_time: int | None | Unset
        if isinstance(self.operation_time, Unset):
            operation_time = UNSET
        else:
            operation_time = self.operation_time

        child_operation: int | None | Unset
        if isinstance(self.child_operation, Unset):
            child_operation = UNSET
        else:
            child_operation = self.child_operation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if platform_field is not UNSET:
            field_dict["platform_field"] = platform_field
        if location is not UNSET:
            field_dict["location"] = location
        if status is not UNSET:
            field_dict["status"] = status
        if operation_time is not UNSET:
            field_dict["operationTime"] = operation_time
        if child_operation is not UNSET:
            field_dict["childOperation"] = child_operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        abstract = d.pop("abstract", UNSET)

        platform_field = d.pop("platform_field", UNSET)

        def _parse_location(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

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

        def _parse_operation_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        operation_time = _parse_operation_time(d.pop("operationTime", UNSET))

        def _parse_child_operation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        child_operation = _parse_child_operation(d.pop("childOperation", UNSET))

        patched_mobile_platform_operation_write_request = cls(
            title=title,
            abstract=abstract,
            platform_field=platform_field,
            location=location,
            status=status,
            operation_time=operation_time,
            child_operation=child_operation,
        )

        patched_mobile_platform_operation_write_request.additional_properties = d
        return patched_mobile_platform_operation_write_request

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
