from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_enum import RoleEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedResponsiblePartyInfoWriteRequest")


@_attrs_define
class PatchedResponsiblePartyInfoWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            priority (int | None | Unset):
            party (int | Unset):
            role (RoleEnum | Unset): * `author` - Author
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
            related_to (str | Unset):
    """

    priority: int | None | Unset = UNSET
    party: int | Unset = UNSET
    role: RoleEnum | Unset = UNSET
    related_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        party = self.party

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        related_to = self.related_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if priority is not UNSET:
            field_dict["priority"] = priority
        if party is not UNSET:
            field_dict["party"] = party
        if role is not UNSET:
            field_dict["role"] = role
        if related_to is not UNSET:
            field_dict["relatedTo"] = related_to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        party = d.pop("party", UNSET)

        _role = d.pop("role", UNSET)
        role: RoleEnum | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RoleEnum(_role)

        related_to = d.pop("relatedTo", UNSET)

        patched_responsible_party_info_write_request = cls(
            priority=priority,
            party=party,
            role=role,
            related_to=related_to,
        )

        patched_responsible_party_info_write_request.additional_properties = d
        return patched_responsible_party_info_write_request

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
