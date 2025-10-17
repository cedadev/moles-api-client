from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.storage_location_enum import StorageLocationEnum
from ..models.storage_status_enum import StorageStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="RelatedResult")


@_attrs_define
class RelatedResult:
    """
    Attributes:
        ob_id (int):
        data_path (str):
        old_data_path (Union[Unset, list[int]]):
        storage_location (Union[Unset, StorageLocationEnum]): * `internal` - internal
            * `external` - external
        storage_status (Union[Unset, StorageStatusEnum]): * `online` - online
            * `offline` - offline
        volume (Union[Unset, int]):
        number_of_files (Union[Unset, int]):
        file_format (Union[None, Unset, str]):
    """

    ob_id: int
    data_path: str
    old_data_path: Union[Unset, list[int]] = UNSET
    storage_location: Union[Unset, StorageLocationEnum] = UNSET
    storage_status: Union[Unset, StorageStatusEnum] = UNSET
    volume: Union[Unset, int] = UNSET
    number_of_files: Union[Unset, int] = UNSET
    file_format: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        data_path = self.data_path

        old_data_path: Union[Unset, list[int]] = UNSET
        if not isinstance(self.old_data_path, Unset):
            old_data_path = self.old_data_path

        storage_location: Union[Unset, str] = UNSET
        if not isinstance(self.storage_location, Unset):
            storage_location = self.storage_location.value

        storage_status: Union[Unset, str] = UNSET
        if not isinstance(self.storage_status, Unset):
            storage_status = self.storage_status.value

        volume = self.volume

        number_of_files = self.number_of_files

        file_format: Union[None, Unset, str]
        if isinstance(self.file_format, Unset):
            file_format = UNSET
        else:
            file_format = self.file_format

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "dataPath": data_path,
            }
        )
        if old_data_path is not UNSET:
            field_dict["oldDataPath"] = old_data_path
        if storage_location is not UNSET:
            field_dict["storageLocation"] = storage_location
        if storage_status is not UNSET:
            field_dict["storageStatus"] = storage_status
        if volume is not UNSET:
            field_dict["volume"] = volume
        if number_of_files is not UNSET:
            field_dict["numberOfFiles"] = number_of_files
        if file_format is not UNSET:
            field_dict["fileFormat"] = file_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        data_path = d.pop("dataPath")

        old_data_path = cast(list[int], d.pop("oldDataPath", UNSET))

        _storage_location = d.pop("storageLocation", UNSET)
        storage_location: Union[Unset, StorageLocationEnum]
        if isinstance(_storage_location, Unset):
            storage_location = UNSET
        else:
            storage_location = StorageLocationEnum(_storage_location)

        _storage_status = d.pop("storageStatus", UNSET)
        storage_status: Union[Unset, StorageStatusEnum]
        if isinstance(_storage_status, Unset):
            storage_status = UNSET
        else:
            storage_status = StorageStatusEnum(_storage_status)

        volume = d.pop("volume", UNSET)

        number_of_files = d.pop("numberOfFiles", UNSET)

        def _parse_file_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        file_format = _parse_file_format(d.pop("fileFormat", UNSET))

        related_result = cls(
            ob_id=ob_id,
            data_path=data_path,
            old_data_path=old_data_path,
            storage_location=storage_location,
            storage_status=storage_status,
            volume=volume,
            number_of_files=number_of_files,
            file_format=file_format,
        )

        related_result.additional_properties = d
        return related_result

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
