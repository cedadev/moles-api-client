from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.identifier_type_enum import IdentifierTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedIdentifierWrite")


@_attrs_define
class PatchedIdentifierWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (Union[Unset, int]):
            url (Union[Unset, str]):
            identifier_type (Union[Unset, IdentifierTypeEnum]): * `moles3_url` - MOLES3 URL
                * `moles2_url` - MOLES2 URL
                * `moles1_url` - MOLES1 URL
                * `doi` - DOI
                * `ceda_abbreviation` - CEDA Abbreviation
            related_to (Union[Unset, str]):
            short_url (Union[Unset, str]):
    """

    ob_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    identifier_type: Union[Unset, IdentifierTypeEnum] = UNSET
    related_to: Union[Unset, str] = UNSET
    short_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        url = self.url

        identifier_type: Union[Unset, str] = UNSET
        if not isinstance(self.identifier_type, Unset):
            identifier_type = self.identifier_type.value

        related_to = self.related_to

        short_url = self.short_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
        if url is not UNSET:
            field_dict["url"] = url
        if identifier_type is not UNSET:
            field_dict["identifierType"] = identifier_type
        if related_to is not UNSET:
            field_dict["relatedTo"] = related_to
        if short_url is not UNSET:
            field_dict["shortUrl"] = short_url

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.ob_id, Unset):
            files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        if not isinstance(self.url, Unset):
            files.append(("url", (None, str(self.url).encode(), "text/plain")))

        if not isinstance(self.identifier_type, Unset):
            files.append(("identifierType", (None, str(self.identifier_type.value).encode(), "text/plain")))

        if not isinstance(self.related_to, Unset):
            files.append(("relatedTo", (None, str(self.related_to).encode(), "text/plain")))

        if not isinstance(self.short_url, Unset):
            files.append(("shortUrl", (None, str(self.short_url).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        url = d.pop("url", UNSET)

        _identifier_type = d.pop("identifierType", UNSET)
        identifier_type: Union[Unset, IdentifierTypeEnum]
        if isinstance(_identifier_type, Unset):
            identifier_type = UNSET
        else:
            identifier_type = IdentifierTypeEnum(_identifier_type)

        related_to = d.pop("relatedTo", UNSET)

        short_url = d.pop("shortUrl", UNSET)

        patched_identifier_write = cls(
            ob_id=ob_id,
            url=url,
            identifier_type=identifier_type,
            related_to=related_to,
            short_url=short_url,
        )

        patched_identifier_write.additional_properties = d
        return patched_identifier_write

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
