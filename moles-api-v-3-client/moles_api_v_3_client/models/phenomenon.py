from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.phenomenon_name import PhenomenonName
    from ..models.phenomenon_term import PhenomenonTerm


T = TypeVar("T", bound="Phenomenon")


@_attrs_define
class Phenomenon:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (None | str):
            names (list[PhenomenonName]):
            terms (list[PhenomenonTerm]):
    """

    ob_id: None | str
    names: list[PhenomenonName]
    terms: list[PhenomenonTerm]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: None | str
        ob_id = self.ob_id

        names = []
        for names_item_data in self.names:
            names_item = names_item_data.to_dict()
            names.append(names_item)

        terms = []
        for terms_item_data in self.terms:
            terms_item = terms_item_data.to_dict()
            terms.append(terms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "names": names,
                "terms": terms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phenomenon_name import PhenomenonName
        from ..models.phenomenon_term import PhenomenonTerm

        d = dict(src_dict)

        def _parse_ob_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        names = []
        _names = d.pop("names")
        for names_item_data in _names:
            names_item = PhenomenonName.from_dict(names_item_data)

            names.append(names_item)

        terms = []
        _terms = d.pop("terms")
        for terms_item_data in _terms:
            terms_item = PhenomenonTerm.from_dict(terms_item_data)

            terms.append(terms_item)

        phenomenon = cls(
            ob_id=ob_id,
            names=names,
            terms=terms,
        )

        phenomenon.additional_properties = d
        return phenomenon

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
