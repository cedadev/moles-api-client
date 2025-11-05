from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
            ob_id (int):
            uuid (str):
            short_code (str):
            curation_category (Union[BlankEnum, CurationCategoryEnum]):
            data_path (str):
            number_of_files (int):
            volume (int):
            file_format (Union[None, str]):
            storage_status (StorageStatusEnum): * `online` - online
                * `offline` - offline
            storage_location (StorageLocationEnum): * `internal` - internal
                * `external` - external
            old_data_path (list['SimpleRead']):
            observation (SimpleRead): A mixin that adds 'simple_fields' as ReadOnlyFields
                and reorders them to the top.
            onlineresource_set (list[Union[None, int]]):
    """

    ob_id: int
    uuid: str
    short_code: str
    curation_category: Union[BlankEnum, CurationCategoryEnum]
    data_path: str
    number_of_files: int
    volume: int
    file_format: Union[None, str]
    storage_status: StorageStatusEnum
    storage_location: StorageLocationEnum
    old_data_path: list["SimpleRead"]
    observation: "SimpleRead"
    onlineresource_set: list[Union[None, int]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        curation_category: str
        if isinstance(self.curation_category, CurationCategoryEnum):
            curation_category = self.curation_category.value
        else:
            curation_category = self.curation_category.value

        data_path = self.data_path

        number_of_files = self.number_of_files

        volume = self.volume

        file_format: Union[None, str]
        file_format = self.file_format

        storage_status = self.storage_status.value

        storage_location = self.storage_location.value

        old_data_path = []
        for old_data_path_item_data in self.old_data_path:
            old_data_path_item = old_data_path_item_data.to_dict()
            old_data_path.append(old_data_path_item)

        observation = self.observation.to_dict()

        onlineresource_set = []
        for onlineresource_set_item_data in self.onlineresource_set:
            onlineresource_set_item: Union[None, int]
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
        ob_id = d.pop("ob_id")

        uuid = d.pop("uuid")

        short_code = d.pop("short_code")

        def _parse_curation_category(data: object) -> Union[BlankEnum, CurationCategoryEnum]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                curation_category_type_0 = CurationCategoryEnum(data)

                return curation_category_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            curation_category_type_1 = BlankEnum(data)

            return curation_category_type_1

        curation_category = _parse_curation_category(d.pop("curationCategory"))

        data_path = d.pop("dataPath")

        number_of_files = d.pop("numberOfFiles")

        volume = d.pop("volume")

        def _parse_file_format(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        file_format = _parse_file_format(d.pop("fileFormat"))

        storage_status = StorageStatusEnum(d.pop("storageStatus"))

        storage_location = StorageLocationEnum(d.pop("storageLocation"))

        old_data_path = []
        _old_data_path = d.pop("oldDataPath")
        for old_data_path_item_data in _old_data_path:
            old_data_path_item = SimpleRead.from_dict(old_data_path_item_data)

            old_data_path.append(old_data_path_item)

        observation = SimpleRead.from_dict(d.pop("observation"))

        onlineresource_set = []
        _onlineresource_set = d.pop("onlineresource_set")
        for onlineresource_set_item_data in _onlineresource_set:

            def _parse_onlineresource_set_item(data: object) -> Union[None, int]:
                if data is None:
                    return data
                return cast(Union[None, int], data)

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
