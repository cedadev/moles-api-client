from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_enum import RoleEnum

if TYPE_CHECKING:
    from ..models.party_read import PartyRead
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="ResponsiblePartyInfoRead")


@_attrs_define
class ResponsiblePartyInfoRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            priority (Union[None, int]):
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
            party (PartyRead): A mixin that adds 'simple_fields' as ReadOnlyFields
                and reorders them to the top.
            related_to (SimpleRead): A mixin that adds 'simple_fields' as ReadOnlyFields
                and reorders them to the top.
    """

    ob_id: int
    priority: Union[None, int]
    role: RoleEnum
    party: "PartyRead"
    related_to: "SimpleRead"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        priority: Union[None, int]
        priority = self.priority

        role = self.role.value

        party = self.party.to_dict()

        related_to = self.related_to.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "priority": priority,
                "role": role,
                "party": party,
                "relatedTo": related_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.party_read import PartyRead
        from ..models.simple_read import SimpleRead

        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        def _parse_priority(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        priority = _parse_priority(d.pop("priority"))

        role = RoleEnum(d.pop("role"))

        party = PartyRead.from_dict(d.pop("party"))

        related_to = SimpleRead.from_dict(d.pop("relatedTo"))

        responsible_party_info_read = cls(
            ob_id=ob_id,
            priority=priority,
            role=role,
            party=party,
            related_to=related_to,
        )

        responsible_party_info_read.additional_properties = d
        return responsible_party_info_read

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
