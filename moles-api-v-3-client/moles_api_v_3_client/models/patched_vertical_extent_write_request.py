from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedVerticalExtentWriteRequest")


@_attrs_define
class PatchedVerticalExtentWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            highest_level_bound (float | Unset):
            lowest_level_bound (float | Unset):
            units (str | Unset):
    """

    highest_level_bound: float | Unset = UNSET
    lowest_level_bound: float | Unset = UNSET
    units: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        highest_level_bound = self.highest_level_bound

        lowest_level_bound = self.lowest_level_bound

        units = self.units

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if highest_level_bound is not UNSET:
            field_dict["highestLevelBound"] = highest_level_bound
        if lowest_level_bound is not UNSET:
            field_dict["lowestLevelBound"] = lowest_level_bound
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        highest_level_bound = d.pop("highestLevelBound", UNSET)

        lowest_level_bound = d.pop("lowestLevelBound", UNSET)

        units = d.pop("units", UNSET)

        patched_vertical_extent_write_request = cls(
            highest_level_bound=highest_level_bound,
            lowest_level_bound=lowest_level_bound,
            units=units,
        )

        patched_vertical_extent_write_request.additional_properties = d
        return patched_vertical_extent_write_request

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
