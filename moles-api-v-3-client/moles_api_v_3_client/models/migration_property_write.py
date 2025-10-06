import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MigrationPropertyWrite")


@_attrs_define
class MigrationPropertyWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            id (int):
            ob_ref (int):
            key (str):
            value (str):
            modified (datetime.date):
    """

    id: int
    ob_ref: int
    key: str
    value: str
    modified: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ob_ref = self.ob_ref

        key = self.key

        value = self.value

        modified = self.modified.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ob_ref": ob_ref,
                "key": key,
                "value": value,
                "modified": modified,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        ob_ref = d.pop("ob_ref")

        key = d.pop("key")

        value = d.pop("value")

        modified = isoparse(d.pop("modified")).date()

        migration_property_write = cls(
            id=id,
            ob_ref=ob_ref,
            key=key,
            value=value,
            modified=modified,
        )

        migration_property_write.additional_properties = d
        return migration_property_write

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
