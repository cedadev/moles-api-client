from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identifier_type_enum import IdentifierTypeEnum

T = TypeVar("T", bound="IdentifierWrite")


@_attrs_define
class IdentifierWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            url (str):
            identifier_type (IdentifierTypeEnum): * `moles3_url` - MOLES3 URL
                * `moles2_url` - MOLES2 URL
                * `moles1_url` - MOLES1 URL
                * `doi` - DOI
                * `ceda_abbreviation` - CEDA Abbreviation
            short_url (str):
    """

    ob_id: int
    url: str
    identifier_type: IdentifierTypeEnum
    short_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        url = self.url

        identifier_type = self.identifier_type.value

        short_url = self.short_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "url": url,
                "identifierType": identifier_type,
                "shortUrl": short_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        url = d.pop("url")

        identifier_type = IdentifierTypeEnum(d.pop("identifierType"))

        short_url = d.pop("shortUrl")

        identifier_write = cls(
            ob_id=ob_id,
            url=url,
            identifier_type=identifier_type,
            short_url=short_url,
        )

        identifier_write.additional_properties = d
        return identifier_write

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
