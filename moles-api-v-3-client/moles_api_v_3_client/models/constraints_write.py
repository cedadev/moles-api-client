from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.access_category_enum import AccessCategoryEnum

T = TypeVar("T", bound="ConstraintsWrite")


@_attrs_define
class ConstraintsWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            access_constraints (Union[None, str]):
            access_category (AccessCategoryEnum): * `public` - Public access no restriction
                * `registered` - Available to any registered user (no dataset registration required)
                * `restricted` - Dataset registration required
            access_roles (Union[None, str]):
            label (Union[None, str]):
            licence (Union[None, int]):
    """

    ob_id: int
    access_constraints: Union[None, str]
    access_category: AccessCategoryEnum
    access_roles: Union[None, str]
    label: Union[None, str]
    licence: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        access_constraints: Union[None, str]
        access_constraints = self.access_constraints

        access_category = self.access_category.value

        access_roles: Union[None, str]
        access_roles = self.access_roles

        label: Union[None, str]
        label = self.label

        licence: Union[None, int]
        licence = self.licence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "accessConstraints": access_constraints,
                "accessCategory": access_category,
                "accessRoles": access_roles,
                "label": label,
                "licence": licence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        def _parse_access_constraints(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        access_constraints = _parse_access_constraints(d.pop("accessConstraints"))

        access_category = AccessCategoryEnum(d.pop("accessCategory"))

        def _parse_access_roles(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        access_roles = _parse_access_roles(d.pop("accessRoles"))

        def _parse_label(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        label = _parse_label(d.pop("label"))

        def _parse_licence(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        licence = _parse_licence(d.pop("licence"))

        constraints_write = cls(
            ob_id=ob_id,
            access_constraints=access_constraints,
            access_category=access_category,
            access_roles=access_roles,
            label=label,
            licence=licence,
        )

        constraints_write.additional_properties = d
        return constraints_write

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
