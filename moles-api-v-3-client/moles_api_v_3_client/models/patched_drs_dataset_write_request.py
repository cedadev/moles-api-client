from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedDRSDatasetWriteRequest")


@_attrs_define
class PatchedDRSDatasetWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            drs_id (Union[Unset, str]):
            version (Union[Unset, str]):
            directory (Union[Unset, str]):
            related_to (Union[Unset, int]):
    """

    drs_id: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    directory: Union[Unset, str] = UNSET
    related_to: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        drs_id = self.drs_id

        version = self.version

        directory = self.directory

        related_to = self.related_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if drs_id is not UNSET:
            field_dict["drsId"] = drs_id
        if version is not UNSET:
            field_dict["version"] = version
        if directory is not UNSET:
            field_dict["directory"] = directory
        if related_to is not UNSET:
            field_dict["relatedTo"] = related_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        drs_id = d.pop("drsId", UNSET)

        version = d.pop("version", UNSET)

        directory = d.pop("directory", UNSET)

        related_to = d.pop("relatedTo", UNSET)

        patched_drs_dataset_write_request = cls(
            drs_id=drs_id,
            version=version,
            directory=directory,
            related_to=related_to,
        )

        patched_drs_dataset_write_request.additional_properties = d
        return patched_drs_dataset_write_request

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
