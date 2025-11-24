from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedImageDetailsWriteRequest")


@_attrs_define
class PatchedImageDetailsWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            linkage (str | Unset):
            file_name (str | Unset):
    """

    linkage: str | Unset = UNSET
    file_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        linkage = self.linkage

        file_name = self.file_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if linkage is not UNSET:
            field_dict["linkage"] = linkage
        if file_name is not UNSET:
            field_dict["fileName"] = file_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        linkage = d.pop("linkage", UNSET)

        file_name = d.pop("fileName", UNSET)

        patched_image_details_write_request = cls(
            linkage=linkage,
            file_name=file_name,
        )

        patched_image_details_write_request.additional_properties = d
        return patched_image_details_write_request

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
