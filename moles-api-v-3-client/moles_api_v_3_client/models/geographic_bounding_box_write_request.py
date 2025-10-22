from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeographicBoundingBoxWriteRequest")


@_attrs_define
class GeographicBoundingBoxWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            bbox_name (Union[Unset, str]):
            east_bound_longitude (Union[Unset, float]):
            north_bound_latitude (Union[Unset, float]):
            west_bound_longitude (Union[Unset, float]):
            south_bound_latitude (Union[Unset, float]):
    """

    bbox_name: Union[Unset, str] = UNSET
    east_bound_longitude: Union[Unset, float] = UNSET
    north_bound_latitude: Union[Unset, float] = UNSET
    west_bound_longitude: Union[Unset, float] = UNSET
    south_bound_latitude: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bbox_name = self.bbox_name

        east_bound_longitude = self.east_bound_longitude

        north_bound_latitude = self.north_bound_latitude

        west_bound_longitude = self.west_bound_longitude

        south_bound_latitude = self.south_bound_latitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bbox_name is not UNSET:
            field_dict["bboxName"] = bbox_name
        if east_bound_longitude is not UNSET:
            field_dict["eastBoundLongitude"] = east_bound_longitude
        if north_bound_latitude is not UNSET:
            field_dict["northBoundLatitude"] = north_bound_latitude
        if west_bound_longitude is not UNSET:
            field_dict["westBoundLongitude"] = west_bound_longitude
        if south_bound_latitude is not UNSET:
            field_dict["southBoundLatitude"] = south_bound_latitude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bbox_name = d.pop("bboxName", UNSET)

        east_bound_longitude = d.pop("eastBoundLongitude", UNSET)

        north_bound_latitude = d.pop("northBoundLatitude", UNSET)

        west_bound_longitude = d.pop("westBoundLongitude", UNSET)

        south_bound_latitude = d.pop("southBoundLatitude", UNSET)

        geographic_bounding_box_write_request = cls(
            bbox_name=bbox_name,
            east_bound_longitude=east_bound_longitude,
            north_bound_latitude=north_bound_latitude,
            west_bound_longitude=west_bound_longitude,
            south_bound_latitude=south_bound_latitude,
        )

        geographic_bounding_box_write_request.additional_properties = d
        return geographic_bounding_box_write_request

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
