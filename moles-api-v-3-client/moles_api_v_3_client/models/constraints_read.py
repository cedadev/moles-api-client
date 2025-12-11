from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.access_category_enum import AccessCategoryEnum

if TYPE_CHECKING:
    from ..models.licence_read import LicenceRead


T = TypeVar("T", bound="ConstraintsRead")


@_attrs_define
class ConstraintsRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            access_constraints (None | str):
            access_category (AccessCategoryEnum | None):
            access_roles (None | str):
            label (None | str):
            licence (LicenceRead | None):
    """

    ob_id: int | None
    access_constraints: None | str
    access_category: AccessCategoryEnum | None
    access_roles: None | str
    label: None | str
    licence: LicenceRead | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.licence_read import LicenceRead

        ob_id: int | None
        ob_id = self.ob_id

        access_constraints: None | str
        access_constraints = self.access_constraints

        access_category: None | str
        if isinstance(self.access_category, AccessCategoryEnum):
            access_category = self.access_category.value
        else:
            access_category = self.access_category

        access_roles: None | str
        access_roles = self.access_roles

        label: None | str
        label = self.label

        licence: dict[str, Any] | None
        if isinstance(self.licence, LicenceRead):
            licence = self.licence.to_dict()
        else:
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
        from ..models.licence_read import LicenceRead

        d = dict(src_dict)

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_access_constraints(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        access_constraints = _parse_access_constraints(d.pop("accessConstraints"))

        def _parse_access_category(data: object) -> AccessCategoryEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_category_type_1 = AccessCategoryEnum(data)

                return access_category_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AccessCategoryEnum | None, data)

        access_category = _parse_access_category(d.pop("accessCategory"))

        def _parse_access_roles(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        access_roles = _parse_access_roles(d.pop("accessRoles"))

        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))

        def _parse_licence(data: object) -> LicenceRead | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                licence_type_1 = LicenceRead.from_dict(data)

                return licence_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LicenceRead | None, data)

        licence = _parse_licence(d.pop("licence"))

        constraints_read = cls(
            ob_id=ob_id,
            access_constraints=access_constraints,
            access_category=access_category,
            access_roles=access_roles,
            label=label,
            licence=licence,
        )

        constraints_read.additional_properties = d
        return constraints_read

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
