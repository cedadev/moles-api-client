from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.party_type_enum import PartyTypeEnum

T = TypeVar("T", bound="PartyRead")


@_attrs_define
class PartyRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            first_name (str):
            last_name (str):
            party_type (PartyTypeEnum): * `individual` - Individual
                * `organisation` - Organisation
            description (str):
            delivery_point (str):
            administrative_area (str):
            city (str):
            country (str):
            postal_code (str):
            electronic_email_address (str):
            phone (str):
            online_resource (str):
            responsiblepartyinfo_url (str):
    """

    ob_id: int
    first_name: str
    last_name: str
    party_type: PartyTypeEnum
    description: str
    delivery_point: str
    administrative_area: str
    city: str
    country: str
    postal_code: str
    electronic_email_address: str
    phone: str
    online_resource: str
    responsiblepartyinfo_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        first_name = self.first_name

        last_name = self.last_name

        party_type = self.party_type.value

        description = self.description

        delivery_point = self.delivery_point

        administrative_area = self.administrative_area

        city = self.city

        country = self.country

        postal_code = self.postal_code

        electronic_email_address = self.electronic_email_address

        phone = self.phone

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
        ob_id = d.pop("ob_id")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        party_type = PartyTypeEnum(d.pop("partyType"))

        description = d.pop("description")

        delivery_point = d.pop("deliveryPoint")

        administrative_area = d.pop("administrativeArea")

        city = d.pop("city")

        country = d.pop("country")

        postal_code = d.pop("postalCode")

        electronic_email_address = d.pop("electronicEmailAddress")

        phone = d.pop("phone")

        online_resource = d.pop("onlineResource")

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
