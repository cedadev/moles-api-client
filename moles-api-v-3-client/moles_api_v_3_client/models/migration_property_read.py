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
            id (int | None):
            key (None | str):
            value (None | str):
            modified (datetime.date | None):
            ob_ref (int | None):
    """

    id: int | None
    key: None | str
    value: None | str
    modified: datetime.date | None
    ob_ref: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: int | None
        id = self.id

        key: None | str
        key = self.key

        value: None | str
        value = self.value

        modified: None | str
        if isinstance(self.modified, datetime.date):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

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

        def _parse_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        id = _parse_id(d.pop("id"))

        def _parse_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key = _parse_key(d.pop("key"))

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        def _parse_modified(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_type_0 = isoparse(data).date()

                return modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        modified = _parse_modified(d.pop("modified"))

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
