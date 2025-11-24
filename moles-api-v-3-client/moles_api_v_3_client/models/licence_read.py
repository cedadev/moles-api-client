from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
            licence_classifications (list[LicenceClassificationRead] | None):
    """

    ob_id: int
    licence_url: str
    licence_classifications: list[LicenceClassificationRead] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        licence_url = self.licence_url

        licence_classifications: list[dict[str, Any]] | None
        if isinstance(self.licence_classifications, list):
            licence_classifications = []
            for licence_classifications_type_0_item_data in self.licence_classifications:
                licence_classifications_type_0_item = licence_classifications_type_0_item_data.to_dict()
                licence_classifications.append(licence_classifications_type_0_item)

        else:
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.licence_classification_read import LicenceClassificationRead

        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        licence_url = d.pop("licenceURL")

        def _parse_licence_classifications(data: object) -> list[LicenceClassificationRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                licence_classifications_type_0 = []
                _licence_classifications_type_0 = data
                for licence_classifications_type_0_item_data in _licence_classifications_type_0:
                    licence_classifications_type_0_item = LicenceClassificationRead.from_dict(
                        licence_classifications_type_0_item_data
                    )

                    licence_classifications_type_0.append(licence_classifications_type_0_item)

                return licence_classifications_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LicenceClassificationRead] | None, data)

        licence_classifications = _parse_licence_classifications(d.pop("licenceClassifications"))

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
