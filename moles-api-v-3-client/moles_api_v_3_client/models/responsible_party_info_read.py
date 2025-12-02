from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_enum import RoleEnum

if TYPE_CHECKING:
    from ..models.party_read import PartyRead
    from ..models.referenceable import Referenceable


T = TypeVar("T", bound="ResponsiblePartyInfoRead")


@_attrs_define
class ResponsiblePartyInfoRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            priority (int | None):
            role (None | RoleEnum):
            party (PartyRead): A mixin that adds 'simple_fields' as ReadOnlyFields
                and reorders them to the top.
            related_to (Referenceable): A mixin that adds 'simple_fields' as ReadOnlyFields
                and reorders them to the top.
    """

    ob_id: int | None
    priority: int | None
    role: None | RoleEnum
    party: PartyRead
    related_to: Referenceable
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: int | None
        ob_id = self.ob_id

        priority: int | None
        priority = self.priority

        role: None | str
        if isinstance(self.role, RoleEnum):
            role = self.role.value
        else:
            role = self.role

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
        from ..models.referenceable import Referenceable

        d = dict(src_dict)

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_priority(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        priority = _parse_priority(d.pop("priority"))

        def _parse_role(data: object) -> None | RoleEnum:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_1 = RoleEnum(data)

                return role_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RoleEnum, data)

        role = _parse_role(d.pop("role"))

        party = PartyRead.from_dict(d.pop("party"))

        related_to = Referenceable.from_dict(d.pop("relatedTo"))

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
