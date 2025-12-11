from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.party_type_enum import PartyTypeEnum

T = TypeVar("T", bound="PartyRead")


@_attrs_define
class PartyRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            first_name (None | str):
            last_name (None | str):
            party_type (None | PartyTypeEnum):
            description (None | str):
            delivery_point (None | str):
            administrative_area (None | str):
            city (None | str):
            country (None | str):
            postal_code (None | str):
            electronic_email_address (None | str):
            phone (None | str):
            online_resource (None | str):
            responsiblepartyinfo_url (str):
    """

    ob_id: int | None
    first_name: None | str
    last_name: None | str
    party_type: None | PartyTypeEnum
    description: None | str
    delivery_point: None | str
    administrative_area: None | str
    city: None | str
    country: None | str
    postal_code: None | str
    electronic_email_address: None | str
    phone: None | str
    online_resource: None | str
    responsiblepartyinfo_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: int | None
        ob_id = self.ob_id

        first_name: None | str
        first_name = self.first_name

        last_name: None | str
        last_name = self.last_name

        party_type: None | str
        if isinstance(self.party_type, PartyTypeEnum):
            party_type = self.party_type.value
        else:
            party_type = self.party_type

        description: None | str
        description = self.description

        delivery_point: None | str
        delivery_point = self.delivery_point

        administrative_area: None | str
        administrative_area = self.administrative_area

        city: None | str
        city = self.city

        country: None | str
        country = self.country

        postal_code: None | str
        postal_code = self.postal_code

        electronic_email_address: None | str
        electronic_email_address = self.electronic_email_address

        phone: None | str
        phone = self.phone

        online_resource: None | str
        online_resource = self.online_resource

        responsiblepartyinfo_url = self.responsiblepartyinfo_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "firstName": first_name,
                "lastName": last_name,
                "partyType": party_type,
                "description": description,
                "deliveryPoint": delivery_point,
                "administrativeArea": administrative_area,
                "city": city,
                "country": country,
                "postalCode": postal_code,
                "electronicEmailAddress": electronic_email_address,
                "phone": phone,
                "onlineResource": online_resource,
                "responsiblepartyinfo_url": responsiblepartyinfo_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("firstName"))

        def _parse_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_name = _parse_last_name(d.pop("lastName"))

        def _parse_party_type(data: object) -> None | PartyTypeEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                party_type_type_1 = PartyTypeEnum(data)

                return party_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PartyTypeEnum, data)

        party_type = _parse_party_type(d.pop("partyType"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_delivery_point(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        delivery_point = _parse_delivery_point(d.pop("deliveryPoint"))

        def _parse_administrative_area(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        administrative_area = _parse_administrative_area(d.pop("administrativeArea"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        def _parse_postal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postal_code = _parse_postal_code(d.pop("postalCode"))

        def _parse_electronic_email_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        electronic_email_address = _parse_electronic_email_address(d.pop("electronicEmailAddress"))

        def _parse_phone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone = _parse_phone(d.pop("phone"))

        def _parse_online_resource(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        online_resource = _parse_online_resource(d.pop("onlineResource"))

        responsiblepartyinfo_url = d.pop("responsiblepartyinfo_url")

        party_read = cls(
            ob_id=ob_id,
            first_name=first_name,
            last_name=last_name,
            party_type=party_type,
            description=description,
            delivery_point=delivery_point,
            administrative_area=administrative_area,
            city=city,
            country=country,
            postal_code=postal_code,
            electronic_email_address=electronic_email_address,
            phone=phone,
            online_resource=online_resource,
            responsiblepartyinfo_url=responsiblepartyinfo_url,
        )

        party_read.additional_properties = d
        return party_read

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
