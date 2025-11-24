from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_enum import RoleEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponsiblePartyInfoWriteRequest")


@_attrs_define
class ResponsiblePartyInfoWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            party (int):
            role (RoleEnum): * `author` - Author
                * `ceda_officer` - CEDA Officer
                * `co_investigator` - Co-Investigator
                * `curator` - Curator
                * `custodian` - Custodian
                * `data_owner` - Data Owner
                * `distributor` - Distributor
                * `funder` - Funder
                * `metadata_owner` - Metadata Owner
                * `operator` - Operator
                * `principal_investigator` - Principal Investigator
                * `point_of_contact` - Point of Contact
                * `publisher` - Publisher
            related_to (str):
            priority (int | None | Unset):
    """

    party: int
    role: RoleEnum
    related_to: str
    priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party = self.party

        role = self.role.value

        related_to = self.related_to

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "party": party,
                "role": role,
                "relatedTo": related_to,
            }
        )
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        party = d.pop("party")

        role = RoleEnum(d.pop("role"))

        related_to = d.pop("relatedTo")

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        responsible_party_info_write_request = cls(
            party=party,
            role=role,
            related_to=related_to,
            priority=priority,
        )

        responsible_party_info_write_request.additional_properties = d
        return responsible_party_info_write_request

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
