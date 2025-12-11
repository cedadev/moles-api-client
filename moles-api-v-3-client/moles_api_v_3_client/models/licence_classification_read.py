from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LicenceClassificationRead")


@_attrs_define
class LicenceClassificationRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            classification (None | str):
    """

    ob_id: int | None
    classification: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: int | None
        ob_id = self.ob_id

        classification: None | str
        classification = self.classification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "classification": classification,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_classification(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        classification = _parse_classification(d.pop("classification"))

        licence_classification_read = cls(
            ob_id=ob_id,
            classification=classification,
        )

        licence_classification_read.additional_properties = d
        return licence_classification_read

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
