from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedInstrumentPlatformPairWrite")


@_attrs_define
class PatchedInstrumentPlatformPairWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (Union[Unset, int]):
            platform (Union[Unset, int]):
            instrument (Union[Unset, int]):
            related_to (Union[Unset, str]):
    """

    ob_id: Union[Unset, int] = UNSET
    platform: Union[Unset, int] = UNSET
    instrument: Union[Unset, int] = UNSET
    related_to: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        platform = self.platform

        instrument = self.instrument

        related_to = self.related_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if instrument is not UNSET:
            field_dict["instrument"] = instrument
        if related_to is not UNSET:
            field_dict["relatedTo"] = related_to

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.ob_id, Unset):
            files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        if not isinstance(self.platform, Unset):
            files.append(("platform", (None, str(self.platform).encode(), "text/plain")))

        if not isinstance(self.instrument, Unset):
            files.append(("instrument", (None, str(self.instrument).encode(), "text/plain")))

        if not isinstance(self.related_to, Unset):
            files.append(("relatedTo", (None, str(self.related_to).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        platform = d.pop("platform", UNSET)

        instrument = d.pop("instrument", UNSET)

        related_to = d.pop("relatedTo", UNSET)

        patched_instrument_platform_pair_write = cls(
            ob_id=ob_id,
            platform=platform,
            instrument=instrument,
            related_to=related_to,
        )

        patched_instrument_platform_pair_write.additional_properties = d
        return patched_instrument_platform_pair_write

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
