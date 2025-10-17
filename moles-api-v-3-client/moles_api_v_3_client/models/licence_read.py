from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.licence_classification_read import LicenceClassificationRead


T = TypeVar("T", bound="LicenceRead")


@_attrs_define
class LicenceRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            licence_url (str):
            licence_classifications (list['LicenceClassificationRead']):
    """

    ob_id: int
    licence_url: str
    licence_classifications: list["LicenceClassificationRead"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        licence_url = self.licence_url

        licence_classifications = []
        for licence_classifications_item_data in self.licence_classifications:
            licence_classifications_item = licence_classifications_item_data.to_dict()
            licence_classifications.append(licence_classifications_item)

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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.licence_classification_read import LicenceClassificationRead

        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        licence_url = d.pop("licenceURL")

        licence_classifications = []
        _licence_classifications = d.pop("licenceClassifications")
        for licence_classifications_item_data in _licence_classifications:
            licence_classifications_item = LicenceClassificationRead.from_dict(licence_classifications_item_data)

            licence_classifications.append(licence_classifications_item)

        licence_read = cls(
            ob_id=ob_id,
            licence_url=licence_url,
            licence_classifications=licence_classifications,
        )

        licence_read.additional_properties = d
        return licence_read

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
