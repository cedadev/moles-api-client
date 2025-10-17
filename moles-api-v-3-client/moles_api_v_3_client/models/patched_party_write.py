from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.party_type_enum import PartyTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedPartyWrite")


@_attrs_define
class PatchedPartyWrite:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (Union[Unset, int]):
            first_name (Union[Unset, str]):
            last_name (Union[Unset, str]):
            party_type (Union[Unset, PartyTypeEnum]): * `individual` - Individual
                * `organisation` - Organisation
            description (Union[Unset, str]):
            delivery_point (Union[Unset, str]):
            administrative_area (Union[Unset, str]):
            city (Union[Unset, str]):
            country (Union[Unset, str]):
            postal_code (Union[Unset, str]):
            electronic_email_address (Union[Unset, str]):
            phone (Union[Unset, str]):
            online_resource (Union[Unset, str]):
            address_line_1 (Union[Unset, str]):
            address_line_2 (Union[Unset, str]):
    """

    ob_id: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    party_type: Union[Unset, PartyTypeEnum] = UNSET
    description: Union[Unset, str] = UNSET
    delivery_point: Union[Unset, str] = UNSET
    administrative_area: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    electronic_email_address: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    online_resource: Union[Unset, str] = UNSET
    address_line_1: Union[Unset, str] = UNSET
    address_line_2: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        first_name = self.first_name

        last_name = self.last_name

        party_type: Union[Unset, str] = UNSET
        if not isinstance(self.party_type, Unset):
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

        address_line_1 = self.address_line_1

        address_line_2 = self.address_line_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if party_type is not UNSET:
            field_dict["partyType"] = party_type
        if description is not UNSET:
            field_dict["description"] = description
        if delivery_point is not UNSET:
            field_dict["deliveryPoint"] = delivery_point
        if administrative_area is not UNSET:
            field_dict["administrativeArea"] = administrative_area
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if electronic_email_address is not UNSET:
            field_dict["electronicEmailAddress"] = electronic_email_address
        if phone is not UNSET:
            field_dict["phone"] = phone
        if online_resource is not UNSET:
            field_dict["onlineResource"] = online_resource
        if address_line_1 is not UNSET:
            field_dict["addressLine1"] = address_line_1
        if address_line_2 is not UNSET:
            field_dict["addressLine2"] = address_line_2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _party_type = d.pop("partyType", UNSET)
        party_type: Union[Unset, PartyTypeEnum]
        if isinstance(_party_type, Unset):
            party_type = UNSET
        else:
            party_type = PartyTypeEnum(_party_type)

        description = d.pop("description", UNSET)

        delivery_point = d.pop("deliveryPoint", UNSET)

        administrative_area = d.pop("administrativeArea", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        electronic_email_address = d.pop("electronicEmailAddress", UNSET)

        phone = d.pop("phone", UNSET)

        online_resource = d.pop("onlineResource", UNSET)

        address_line_1 = d.pop("addressLine1", UNSET)

        address_line_2 = d.pop("addressLine2", UNSET)

        patched_party_write = cls(
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
            address_line_1=address_line_1,
            address_line_2=address_line_2,
        )

        patched_party_write.additional_properties = d
        return patched_party_write

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
