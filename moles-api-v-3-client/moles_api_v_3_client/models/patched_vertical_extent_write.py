from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedVerticalExtentWrite")


@_attrs_define
class PatchedVerticalExtentWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (Union[Unset, int]):
            highest_level_bound (Union[Unset, float]):
            lowest_level_bound (Union[Unset, float]):
            units (Union[Unset, str]):
    """

    ob_id: Union[Unset, int] = UNSET
    highest_level_bound: Union[Unset, float] = UNSET
    lowest_level_bound: Union[Unset, float] = UNSET
    units: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        highest_level_bound = self.highest_level_bound

        lowest_level_bound = self.lowest_level_bound

        units = self.units

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
        if highest_level_bound is not UNSET:
            field_dict["highestLevelBound"] = highest_level_bound
        if lowest_level_bound is not UNSET:
            field_dict["lowestLevelBound"] = lowest_level_bound
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.ob_id, Unset):
            files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        if not isinstance(self.highest_level_bound, Unset):
            files.append(("highestLevelBound", (None, str(self.highest_level_bound).encode(), "text/plain")))

        if not isinstance(self.lowest_level_bound, Unset):
            files.append(("lowestLevelBound", (None, str(self.lowest_level_bound).encode(), "text/plain")))

        if not isinstance(self.units, Unset):
            files.append(("units", (None, str(self.units).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        highest_level_bound = d.pop("highestLevelBound", UNSET)

        lowest_level_bound = d.pop("lowestLevelBound", UNSET)

        units = d.pop("units", UNSET)

        patched_vertical_extent_write = cls(
            ob_id=ob_id,
            highest_level_bound=highest_level_bound,
            lowest_level_bound=lowest_level_bound,
            units=units,
        )

        patched_vertical_extent_write.additional_properties = d
        return patched_vertical_extent_write

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
