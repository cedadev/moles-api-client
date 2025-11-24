from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DRSDatasetWrite")


@_attrs_define
class DRSDatasetWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            drs_id (str):
            version (str):
            directory (str):
            related_to (int):
    """

    ob_id: int
    drs_id: str
    version: str
    directory: str
    related_to: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        drs_id = self.drs_id

        version = self.version

        directory = self.directory

        related_to = self.related_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "drsId": drs_id,
                "version": version,
                "directory": directory,
                "relatedTo": related_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        drs_id = d.pop("drsId")

        version = d.pop("version")

        directory = d.pop("directory")

        related_to = d.pop("relatedTo")

        drs_dataset_write = cls(
            ob_id=ob_id,
            drs_id=drs_id,
            version=version,
            directory=directory,
            related_to=related_to,
        )

        drs_dataset_write.additional_properties = d
        return drs_dataset_write

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
