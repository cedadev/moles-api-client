from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="LicenceWrite")


@_attrs_define
class LicenceWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            licence_url (str):
            licence_classifications (list[int]):
    """

    ob_id: int
    licence_url: str
    licence_classifications: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        licence_url = self.licence_url

        licence_classifications = self.licence_classifications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "licenceURL": licence_url,
                "licenceClassifications": licence_classifications,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        files.append(("licenceURL", (None, str(self.licence_url).encode(), "text/plain")))

        for licence_classifications_item_element in self.licence_classifications:
            files.append(
                ("licenceClassifications", (None, str(licence_classifications_item_element).encode(), "text/plain"))
            )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        licence_url = d.pop("licenceURL")

        licence_classifications = cast(list[int], d.pop("licenceClassifications"))

        licence_write = cls(
            ob_id=ob_id,
            licence_url=licence_url,
            licence_classifications=licence_classifications,
        )

        licence_write.additional_properties = d
        return licence_write

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
