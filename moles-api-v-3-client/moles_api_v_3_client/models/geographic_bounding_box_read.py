from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GeographicBoundingBoxRead")


@_attrs_define
class GeographicBoundingBoxRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            bbox_name (None | str):
            east_bound_longitude (float | None):
            west_bound_longitude (float | None):
            south_bound_latitude (float | None):
            north_bound_latitude (float | None):
    """

    ob_id: int | None
    bbox_name: None | str
    east_bound_longitude: float | None
    west_bound_longitude: float | None
    south_bound_latitude: float | None
    north_bound_latitude: float | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: int | None
        ob_id = self.ob_id

        bbox_name: None | str
        bbox_name = self.bbox_name

        east_bound_longitude: float | None
        east_bound_longitude = self.east_bound_longitude

        west_bound_longitude: float | None
        west_bound_longitude = self.west_bound_longitude

        south_bound_latitude: float | None
        south_bound_latitude = self.south_bound_latitude

        north_bound_latitude: float | None
        north_bound_latitude = self.north_bound_latitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "bboxName": bbox_name,
                "eastBoundLongitude": east_bound_longitude,
                "westBoundLongitude": west_bound_longitude,
                "southBoundLatitude": south_bound_latitude,
                "northBoundLatitude": north_bound_latitude,
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

        def _parse_bbox_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bbox_name = _parse_bbox_name(d.pop("bboxName"))

        def _parse_east_bound_longitude(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        east_bound_longitude = _parse_east_bound_longitude(d.pop("eastBoundLongitude"))

        def _parse_west_bound_longitude(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        west_bound_longitude = _parse_west_bound_longitude(d.pop("westBoundLongitude"))

        def _parse_south_bound_latitude(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        south_bound_latitude = _parse_south_bound_latitude(d.pop("southBoundLatitude"))

        def _parse_north_bound_latitude(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        north_bound_latitude = _parse_north_bound_latitude(d.pop("northBoundLatitude"))

        geographic_bounding_box_read = cls(
            ob_id=ob_id,
            bbox_name=bbox_name,
            east_bound_longitude=east_bound_longitude,
            west_bound_longitude=west_bound_longitude,
            south_bound_latitude=south_bound_latitude,
            north_bound_latitude=north_bound_latitude,
        )

        geographic_bounding_box_read.additional_properties = d
        return geographic_bounding_box_read

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
