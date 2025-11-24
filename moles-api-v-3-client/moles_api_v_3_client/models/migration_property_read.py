from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MigrationPropertyRead")


@_attrs_define
class MigrationPropertyRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            id (int):
            key (str):
            value (str):
            modified (datetime.date):
            ob_ref (int | None):
    """

    id: int
    key: str
    value: str
    modified: datetime.date
    ob_ref: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        key = self.key

        value = self.value

        modified = self.modified.isoformat()

        ob_ref: int | None
        ob_ref = self.ob_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "key": key,
                "value": value,
                "modified": modified,
                "ob_ref": ob_ref,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        key = d.pop("key")

        value = d.pop("value")

        modified = isoparse(d.pop("modified")).date()

        def _parse_ob_ref(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_ref = _parse_ob_ref(d.pop("ob_ref"))

        migration_property_read = cls(
            id=id,
            key=key,
            value=value,
            modified=modified,
            ob_ref=ob_ref,
        )

        migration_property_read.additional_properties = d
        return migration_property_read

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
