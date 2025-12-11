from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SimpleRead")


@_attrs_define
class SimpleRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (None | str):
            uuid (None | str):
            short_code (None | str):
            title (None | str):
            abstract (None | str):
    """

    ob_id: None | str
    uuid: None | str
    short_code: None | str
    title: None | str
    abstract: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: None | str
        ob_id = self.ob_id

        uuid: None | str
        uuid = self.uuid

        short_code: None | str
        short_code = self.short_code

        title: None | str
        title = self.title

        abstract: None | str
        abstract = self.abstract

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "short_code": short_code,
                "title": title,
                "abstract": abstract,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ob_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

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

        simple_read = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
        )

        simple_read.additional_properties = d
        return simple_read

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
