from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PhenomenonTerm")


@_attrs_define
class PhenomenonTerm:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (None | str):
            label (None | str):
            value (None | str):
            vocabulary (None | str):
    """

    ob_id: None | str
    label: None | str
    value: None | str
    vocabulary: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: None | str
        ob_id = self.ob_id

        label: None | str
        label = self.label

        value: None | str
        value = self.value

        vocabulary: None | str
        vocabulary = self.vocabulary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "label": label,
                "value": value,
                "vocabulary": vocabulary,
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

        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))

        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))

        def _parse_vocabulary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        vocabulary = _parse_vocabulary(d.pop("vocabulary"))

        phenomenon_term = cls(
            ob_id=ob_id,
            label=label,
            value=value,
            vocabulary=vocabulary,
        )

        phenomenon_term.additional_properties = d
        return phenomenon_term

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
