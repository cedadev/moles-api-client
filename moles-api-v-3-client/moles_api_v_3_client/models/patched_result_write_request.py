from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.curation_category_enum import CurationCategoryEnum
from ..models.storage_location_enum import StorageLocationEnum
from ..models.storage_status_enum import StorageStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedResultWriteRequest")


@_attrs_define
class PatchedResultWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            curation_category (BlankEnum | CurationCategoryEnum | Unset):
            data_path (str | Unset):
            number_of_files (int | Unset):
            volume (int | Unset):
            file_format (None | str | Unset):
            storage_status (StorageStatusEnum | Unset): * `online` - online
                * `offline` - offline
            storage_location (StorageLocationEnum | Unset): * `internal` - internal
                * `external` - external
            old_data_path (list[int] | Unset):
    """

    curation_category: BlankEnum | CurationCategoryEnum | Unset = UNSET
    data_path: str | Unset = UNSET
    number_of_files: int | Unset = UNSET
    volume: int | Unset = UNSET
    file_format: None | str | Unset = UNSET
    storage_status: StorageStatusEnum | Unset = UNSET
    storage_location: StorageLocationEnum | Unset = UNSET
    old_data_path: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        curation_category: str | Unset
        if isinstance(self.curation_category, Unset):
            curation_category = UNSET
        elif isinstance(self.curation_category, CurationCategoryEnum):
            curation_category = self.curation_category.value
        else:
            curation_category = self.curation_category.value

        data_path = self.data_path

        number_of_files = self.number_of_files

        volume = self.volume

        file_format: None | str | Unset
        if isinstance(self.file_format, Unset):
            file_format = UNSET
        else:
            file_format = self.file_format

        storage_status: str | Unset = UNSET
        if not isinstance(self.storage_status, Unset):
            storage_status = self.storage_status.value

        storage_location: str | Unset = UNSET
        if not isinstance(self.storage_location, Unset):
            storage_location = self.storage_location.value

        old_data_path: list[int] | Unset = UNSET
        if not isinstance(self.old_data_path, Unset):
            old_data_path = self.old_data_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if curation_category is not UNSET:
            field_dict["curationCategory"] = curation_category
        if data_path is not UNSET:
            field_dict["dataPath"] = data_path
        if number_of_files is not UNSET:
            field_dict["numberOfFiles"] = number_of_files
        if volume is not UNSET:
            field_dict["volume"] = volume
        if file_format is not UNSET:
            field_dict["fileFormat"] = file_format
        if storage_status is not UNSET:
            field_dict["storageStatus"] = storage_status
        if storage_location is not UNSET:
            field_dict["storageLocation"] = storage_location
        if old_data_path is not UNSET:
            field_dict["oldDataPath"] = old_data_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_curation_category(data: object) -> BlankEnum | CurationCategoryEnum | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                curation_category_type_0 = CurationCategoryEnum(data)

                return curation_category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            curation_category_type_1 = BlankEnum(data)

            return curation_category_type_1

        curation_category = _parse_curation_category(d.pop("curationCategory", UNSET))

        data_path = d.pop("dataPath", UNSET)

        number_of_files = d.pop("numberOfFiles", UNSET)

        volume = d.pop("volume", UNSET)

        def _parse_file_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_format = _parse_file_format(d.pop("fileFormat", UNSET))

        _storage_status = d.pop("storageStatus", UNSET)
        storage_status: StorageStatusEnum | Unset
        if isinstance(_storage_status, Unset):
            storage_status = UNSET
        else:
            storage_status = StorageStatusEnum(_storage_status)

        _storage_location = d.pop("storageLocation", UNSET)
        storage_location: StorageLocationEnum | Unset
        if isinstance(_storage_location, Unset):
            storage_location = UNSET
        else:
            storage_location = StorageLocationEnum(_storage_location)

        old_data_path = cast(list[int], d.pop("oldDataPath", UNSET))

        patched_result_write_request = cls(
            curation_category=curation_category,
            data_path=data_path,
            number_of_files=number_of_files,
            volume=volume,
            file_format=file_format,
            storage_status=storage_status,
            storage_location=storage_location,
            old_data_path=old_data_path,
        )

        patched_result_write_request.additional_properties = d
        return patched_result_write_request

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
