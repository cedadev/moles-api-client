from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VerticalExtentRead")


@_attrs_define
class VerticalExtentRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            highest_level_bound (float):
            lowest_level_bound (float):
            units (str):
    """

    ob_id: int
    highest_level_bound: float
    lowest_level_bound: float
    units: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        highest_level_bound = self.highest_level_bound

        lowest_level_bound = self.lowest_level_bound

        units = self.units

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "highestLevelBound": highest_level_bound,
                "lowestLevelBound": lowest_level_bound,
                "units": units,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        highest_level_bound = d.pop("highestLevelBound")

        lowest_level_bound = d.pop("lowestLevelBound")

        units = d.pop("units")

        vertical_extent_read = cls(
            ob_id=ob_id,
            highest_level_bound=highest_level_bound,
            lowest_level_bound=lowest_level_bound,
            units=units,
        )

        vertical_extent_read.additional_properties = d
        return vertical_extent_read

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
