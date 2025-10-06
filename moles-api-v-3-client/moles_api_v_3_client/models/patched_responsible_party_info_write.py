from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.role_enum import RoleEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedResponsiblePartyInfoWrite")


@_attrs_define
class PatchedResponsiblePartyInfoWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (Union[Unset, int]):
            priority (Union[None, Unset, int]):
            party (Union[Unset, int]):
            role (Union[Unset, RoleEnum]): * `author` - Author
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
            related_to (Union[Unset, str]):
    """

    ob_id: Union[Unset, int] = UNSET
    priority: Union[None, Unset, int] = UNSET
    party: Union[Unset, int] = UNSET
    role: Union[Unset, RoleEnum] = UNSET
    related_to: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        priority: Union[None, Unset, int]
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        party = self.party

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        related_to = self.related_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if party is not UNSET:
            field_dict["party"] = party
        if role is not UNSET:
            field_dict["role"] = role
        if related_to is not UNSET:
            field_dict["relatedTo"] = related_to

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.ob_id, Unset):
            files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        if not isinstance(self.priority, Unset):
            if isinstance(self.priority, int):
                files.append(("priority", (None, str(self.priority).encode(), "text/plain")))
            else:
                files.append(("priority", (None, str(self.priority).encode(), "text/plain")))

        if not isinstance(self.party, Unset):
            files.append(("party", (None, str(self.party).encode(), "text/plain")))

        if not isinstance(self.role, Unset):
            files.append(("role", (None, str(self.role.value).encode(), "text/plain")))

        if not isinstance(self.related_to, Unset):
            files.append(("relatedTo", (None, str(self.related_to).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        def _parse_priority(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        priority = _parse_priority(d.pop("priority", UNSET))

        party = d.pop("party", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, RoleEnum]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RoleEnum(_role)

        related_to = d.pop("relatedTo", UNSET)

        patched_responsible_party_info_write = cls(
            ob_id=ob_id,
            priority=priority,
            party=party,
            role=role,
            related_to=related_to,
        )

        patched_responsible_party_info_write.additional_properties = d
        return patched_responsible_party_info_write

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
