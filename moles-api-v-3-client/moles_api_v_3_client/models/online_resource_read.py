from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.function_enum import FunctionEnum

if TYPE_CHECKING:
    from ..models.referenceable import Referenceable


T = TypeVar("T", bound="OnlineResourceRead")


@_attrs_define
class OnlineResourceRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            function (BlankEnum | FunctionEnum | None):
            linkage (str):
            name (None | str):
            related_to (Referenceable): A mixin that adds 'simple_fields' as ReadOnlyFields
                and reorders them to the top.
    """

    ob_id: int
    function: BlankEnum | FunctionEnum | None
    linkage: str
    name: None | str
    related_to: Referenceable
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        function: None | str
        if isinstance(self.function, FunctionEnum):
            function = self.function.value
        elif isinstance(self.function, BlankEnum):
            function = self.function.value
        else:
            function = self.function

        linkage = self.linkage

        name: None | str
        name = self.name

        related_to = self.related_to.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "function": function,
                "linkage": linkage,
                "name": name,
                "relatedTo": related_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referenceable import Referenceable

        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        def _parse_function(data: object) -> BlankEnum | FunctionEnum | None:
            if data is None:
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
            return cast(BlankEnum | FunctionEnum | None, data)

        function = _parse_function(d.pop("function"))

        linkage = d.pop("linkage")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        related_to = Referenceable.from_dict(d.pop("relatedTo"))

        online_resource_read = cls(
            ob_id=ob_id,
            function=function,
            linkage=linkage,
            name=name,
            related_to=related_to,
        )

        online_resource_read.additional_properties = d
        return online_resource_read

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
