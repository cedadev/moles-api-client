from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.function_enum import FunctionEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnlineResourceWriteRequest")


@_attrs_define
class OnlineResourceWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            linkage (str):
            related_to (str):
            function (BlankEnum | FunctionEnum | None | Unset):
            name (None | str | Unset):
    """

    linkage: str
    related_to: str
    function: BlankEnum | FunctionEnum | None | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkage = self.linkage

        related_to = self.related_to

        function: None | str | Unset
        if isinstance(self.function, Unset):
            function = UNSET
        elif isinstance(self.function, FunctionEnum):
            function = self.function.value
        elif isinstance(self.function, BlankEnum):
            function = self.function.value
        else:
            function = self.function

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "linkage": linkage,
                "relatedTo": related_to,
            }
        )
        if function is not UNSET:
            field_dict["function"] = function
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        linkage = d.pop("linkage")

        related_to = d.pop("relatedTo")

        def _parse_function(data: object) -> BlankEnum | FunctionEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                function_type_0 = FunctionEnum(data)

                return function_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                function_type_1 = BlankEnum(data)

                return function_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | FunctionEnum | None | Unset, data)

        function = _parse_function(d.pop("function", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        online_resource_write_request = cls(
            linkage=linkage,
            related_to=related_to,
            function=function,
            name=name,
        )

        online_resource_write_request.additional_properties = d
        return online_resource_write_request

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
