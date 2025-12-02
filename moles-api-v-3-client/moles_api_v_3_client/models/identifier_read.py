from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identifier_type_enum import IdentifierTypeEnum

if TYPE_CHECKING:
    from ..models.referenceable import Referenceable


T = TypeVar("T", bound="IdentifierRead")


@_attrs_define
class IdentifierRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            url (None | str):
            identifier_type (IdentifierTypeEnum | None):
            short_url (None | str):
            related_to (None | Referenceable):
    """

    ob_id: int | None
    url: None | str
    identifier_type: IdentifierTypeEnum | None
    short_url: None | str
    related_to: None | Referenceable
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.referenceable import Referenceable

        ob_id: int | None
        ob_id = self.ob_id

        url: None | str
        url = self.url

        identifier_type: None | str
        if isinstance(self.identifier_type, IdentifierTypeEnum):
            identifier_type = self.identifier_type.value
        else:
            identifier_type = self.identifier_type

        short_url: None | str
        short_url = self.short_url

        related_to: dict[str, Any] | None
        if isinstance(self.related_to, Referenceable):
            related_to = self.related_to.to_dict()
        else:
            related_to = self.related_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "url": url,
                "identifierType": identifier_type,
                "shortUrl": short_url,
                "relatedTo": related_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referenceable import Referenceable

        d = dict(src_dict)

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(d.pop("url"))

        def _parse_identifier_type(data: object) -> IdentifierTypeEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                identifier_type_type_1 = IdentifierTypeEnum(data)

                return identifier_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IdentifierTypeEnum | None, data)

        identifier_type = _parse_identifier_type(d.pop("identifierType"))

        def _parse_short_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        short_url = _parse_short_url(d.pop("shortUrl"))

        def _parse_related_to(data: object) -> None | Referenceable:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                related_to_type_1 = Referenceable.from_dict(data)

                return related_to_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Referenceable, data)

        related_to = _parse_related_to(d.pop("relatedTo"))

        identifier_read = cls(
            ob_id=ob_id,
            url=url,
            identifier_type=identifier_type,
            short_url=short_url,
            related_to=related_to,
        )

        identifier_read.additional_properties = d
        return identifier_read

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
