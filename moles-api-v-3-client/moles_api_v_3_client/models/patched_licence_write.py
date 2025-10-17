from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedLicenceWrite")


@_attrs_define
class PatchedLicenceWrite:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (Union[Unset, int]):
            licence_url (Union[Unset, str]):
            licence_classifications (Union[Unset, list[int]]):
    """

    ob_id: Union[Unset, int] = UNSET
    licence_url: Union[Unset, str] = UNSET
    licence_classifications: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        licence_url = self.licence_url

        licence_classifications: Union[Unset, list[int]] = UNSET
        if not isinstance(self.licence_classifications, Unset):
            licence_classifications = self.licence_classifications

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
        if licence_url is not UNSET:
            field_dict["licenceURL"] = licence_url
        if licence_classifications is not UNSET:
            field_dict["licenceClassifications"] = licence_classifications

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        licence_url = d.pop("licenceURL", UNSET)

        licence_classifications = cast(list[int], d.pop("licenceClassifications", UNSET))

        patched_licence_write = cls(
            ob_id=ob_id,
            licence_url=licence_url,
            licence_classifications=licence_classifications,
        )

        patched_licence_write.additional_properties = d
        return patched_licence_write

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
