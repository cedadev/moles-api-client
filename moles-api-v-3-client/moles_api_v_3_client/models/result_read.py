from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.curation_category_enum import CurationCategoryEnum
from ..models.storage_location_enum import StorageLocationEnum
from ..models.storage_status_enum import StorageStatusEnum

if TYPE_CHECKING:
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="ResultRead")


@_attrs_define
class ResultRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            uuid (None | str):
            short_code (None | str):
            curation_category (BlankEnum | CurationCategoryEnum | None):
            data_path (None | str):
            number_of_files (int | None):
            volume (int | None):
            file_format (None | str):
            storage_status (None | StorageStatusEnum):
            storage_location (None | StorageLocationEnum):
            old_data_path (list[SimpleRead]):
            observation (None | SimpleRead):
            onlineresource_set (list[int | None]):
    """

    ob_id: int | None
    uuid: None | str
    short_code: None | str
    curation_category: BlankEnum | CurationCategoryEnum | None
    data_path: None | str
    number_of_files: int | None
    volume: int | None
    file_format: None | str
    storage_status: None | StorageStatusEnum
    storage_location: None | StorageLocationEnum
    old_data_path: list[SimpleRead]
    observation: None | SimpleRead
    onlineresource_set: list[int | None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_read import SimpleRead

        ob_id: int | None
        ob_id = self.ob_id

        uuid: None | str
        uuid = self.uuid

        short_code: None | str
        short_code = self.short_code

        curation_category: None | str
        if isinstance(self.curation_category, CurationCategoryEnum):
            curation_category = self.curation_category.value
        elif isinstance(self.curation_category, BlankEnum):
            curation_category = self.curation_category.value
        else:
            curation_category = self.curation_category

        data_path: None | str
        data_path = self.data_path

        number_of_files: int | None
        number_of_files = self.number_of_files

        volume: int | None
        volume = self.volume

        file_format: None | str
        file_format = self.file_format

        storage_status: None | str
        if isinstance(self.storage_status, StorageStatusEnum):
            storage_status = self.storage_status.value
        else:
            storage_status = self.storage_status

        storage_location: None | str
        if isinstance(self.storage_location, StorageLocationEnum):
            storage_location = self.storage_location.value
        else:
            storage_location = self.storage_location

        old_data_path = []
        for old_data_path_item_data in self.old_data_path:
            old_data_path_item = old_data_path_item_data.to_dict()
            old_data_path.append(old_data_path_item)

        observation: dict[str, Any] | None
        if isinstance(self.observation, SimpleRead):
            observation = self.observation.to_dict()
        else:
            observation = self.observation

        onlineresource_set = []
        for onlineresource_set_item_data in self.onlineresource_set:
            onlineresource_set_item: int | None
            onlineresource_set_item = onlineresource_set_item_data
            onlineresource_set.append(onlineresource_set_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "short_code": short_code,
                "curationCategory": curation_category,
                "dataPath": data_path,
                "numberOfFiles": number_of_files,
                "volume": volume,
                "fileFormat": file_format,
                "storageStatus": storage_status,
                "storageLocation": storage_location,
                "oldDataPath": old_data_path,
                "observation": observation,
                "onlineresource_set": onlineresource_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_read import SimpleRead

        d = dict(src_dict)

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        uuid = _parse_uuid(d.pop("uuid"))

        def _parse_short_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        short_code = _parse_short_code(d.pop("short_code"))

        def _parse_curation_category(data: object) -> BlankEnum | CurationCategoryEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                curation_category_type_0 = CurationCategoryEnum(data)

                return curation_category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                curation_category_type_1 = BlankEnum(data)

                return curation_category_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | CurationCategoryEnum | None, data)

        curation_category = _parse_curation_category(d.pop("curationCategory"))

        def _parse_data_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        data_path = _parse_data_path(d.pop("dataPath"))

        def _parse_number_of_files(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        number_of_files = _parse_number_of_files(d.pop("numberOfFiles"))

        def _parse_volume(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        volume = _parse_volume(d.pop("volume"))

        def _parse_file_format(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_format = _parse_file_format(d.pop("fileFormat"))

        def _parse_storage_status(data: object) -> None | StorageStatusEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_status_type_1 = StorageStatusEnum(data)

                return storage_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StorageStatusEnum, data)

        storage_status = _parse_storage_status(d.pop("storageStatus"))

        def _parse_storage_location(data: object) -> None | StorageLocationEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_location_type_1 = StorageLocationEnum(data)

                return storage_location_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StorageLocationEnum, data)

        storage_location = _parse_storage_location(d.pop("storageLocation"))

        old_data_path = []
        _old_data_path = d.pop("oldDataPath")
        for old_data_path_item_data in _old_data_path:
            old_data_path_item = SimpleRead.from_dict(old_data_path_item_data)

            old_data_path.append(old_data_path_item)

        def _parse_observation(data: object) -> None | SimpleRead:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                observation_type_1 = SimpleRead.from_dict(data)

                return observation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SimpleRead, data)

        observation = _parse_observation(d.pop("observation"))

        onlineresource_set = []
        _onlineresource_set = d.pop("onlineresource_set")
        for onlineresource_set_item_data in _onlineresource_set:

            def _parse_onlineresource_set_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            onlineresource_set_item = _parse_onlineresource_set_item(onlineresource_set_item_data)

            onlineresource_set.append(onlineresource_set_item)

        result_read = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            curation_category=curation_category,
            data_path=data_path,
            number_of_files=number_of_files,
            volume=volume,
            file_format=file_format,
            storage_status=storage_status,
            storage_location=storage_location,
            old_data_path=old_data_path,
            observation=observation,
            onlineresource_set=onlineresource_set,
        )

        result_read.additional_properties = d
        return result_read

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
