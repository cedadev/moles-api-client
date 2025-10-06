from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="InstrumentPlatformPairWrite")


@_attrs_define
class InstrumentPlatformPairWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            platform (int):
            instrument (int):
            related_to (str):
    """

    ob_id: int
    platform: int
    instrument: int
    related_to: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        platform = self.platform

        instrument = self.instrument

        related_to = self.related_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "platform": platform,
                "instrument": instrument,
                "relatedTo": related_to,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        files.append(("platform", (None, str(self.platform).encode(), "text/plain")))

        files.append(("instrument", (None, str(self.instrument).encode(), "text/plain")))

        files.append(("relatedTo", (None, str(self.related_to).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        platform = d.pop("platform")

        instrument = d.pop("instrument")

        related_to = d.pop("relatedTo")

        instrument_platform_pair_write = cls(
            ob_id=ob_id,
            platform=platform,
            instrument=instrument,
            related_to=related_to,
        )

        instrument_platform_pair_write.additional_properties = d
        return instrument_platform_pair_write

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
