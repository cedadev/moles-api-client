from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="DRSDatasetRead")


@_attrs_define
class DRSDatasetRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            drs_id (None | str):
            version (None | str):
            directory (None | str):
            related_to (SimpleRead): A mixin that adds 'simple_fields' as ReadOnlyFields
                and reorders them to the top.
    """

    ob_id: int | None
    drs_id: None | str
    version: None | str
    directory: None | str
    related_to: SimpleRead
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: int | None
        ob_id = self.ob_id

        drs_id: None | str
        drs_id = self.drs_id

        version: None | str
        version = self.version

        directory: None | str
        directory = self.directory

        related_to = self.related_to.to_dict()

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
        from ..models.simple_read import SimpleRead

        d = dict(src_dict)

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_drs_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        drs_id = _parse_drs_id(d.pop("drsId"))

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))

        def _parse_directory(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        directory = _parse_directory(d.pop("directory"))

        related_to = SimpleRead.from_dict(d.pop("relatedTo"))

        drs_dataset_read = cls(
            ob_id=ob_id,
            drs_id=drs_id,
            version=version,
            directory=directory,
            related_to=related_to,
        )

        drs_dataset_read.additional_properties = d
        return drs_dataset_read

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
