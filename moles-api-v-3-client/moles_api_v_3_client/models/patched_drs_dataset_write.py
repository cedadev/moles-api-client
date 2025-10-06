from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedDRSDatasetWrite")


@_attrs_define
class PatchedDRSDatasetWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (Union[Unset, int]):
            drs_id (Union[Unset, str]):
            version (Union[Unset, str]):
            directory (Union[Unset, str]):
            related_to (Union[Unset, int]):
    """

    ob_id: Union[Unset, int] = UNSET
    drs_id: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    directory: Union[Unset, str] = UNSET
    related_to: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        drs_id = self.drs_id

        version = self.version

        directory = self.directory

        related_to = self.related_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
        if drs_id is not UNSET:
            field_dict["drsId"] = drs_id
        if version is not UNSET:
            field_dict["version"] = version
        if directory is not UNSET:
            field_dict["directory"] = directory
        if related_to is not UNSET:
            field_dict["relatedTo"] = related_to

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.ob_id, Unset):
            files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        if not isinstance(self.drs_id, Unset):
            files.append(("drsId", (None, str(self.drs_id).encode(), "text/plain")))

        if not isinstance(self.version, Unset):
            files.append(("version", (None, str(self.version).encode(), "text/plain")))

        if not isinstance(self.directory, Unset):
            files.append(("directory", (None, str(self.directory).encode(), "text/plain")))

        if not isinstance(self.related_to, Unset):
            files.append(("relatedTo", (None, str(self.related_to).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        drs_id = d.pop("drsId", UNSET)

        version = d.pop("version", UNSET)

        directory = d.pop("directory", UNSET)

        related_to = d.pop("relatedTo", UNSET)

        patched_drs_dataset_write = cls(
            ob_id=ob_id,
            drs_id=drs_id,
            version=version,
            directory=directory,
            related_to=related_to,
        )

        patched_drs_dataset_write.additional_properties = d
        return patched_drs_dataset_write

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
