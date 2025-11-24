from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relation_type_enum import RelationTypeEnum

T = TypeVar("T", bound="RelatedObservationInfoWrite")


@_attrs_define
class RelatedObservationInfoWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            subject_observation (int):
            relation_type (RelationTypeEnum): * `IsSupplementTo` - supplement to
                * `IsSupplementedBy` - supplemented by
                * `Continues` - continues
                * `IsNewVersionOf` - supersedes
                * `IsVariantFormOf` - a variant of
                * `IsIdenticalTo` - identical to
                * `HasMetadata` - uses metadata from
                * `IsDerivedFrom` - derived from
                * `IsPartOf` - is part of (dataset only)
            object_observation (int):
    """

    ob_id: int
    subject_observation: int
    relation_type: RelationTypeEnum
    object_observation: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        subject_observation = self.subject_observation

        relation_type = self.relation_type.value

        object_observation = self.object_observation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "subjectObservation": subject_observation,
                "relationType": relation_type,
                "objectObservation": object_observation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        subject_observation = d.pop("subjectObservation")

        relation_type = RelationTypeEnum(d.pop("relationType"))

        object_observation = d.pop("objectObservation")

        related_observation_info_write = cls(
            ob_id=ob_id,
            subject_observation=subject_observation,
            relation_type=relation_type,
            object_observation=object_observation,
        )

        related_observation_info_write.additional_properties = d
        return related_observation_info_write

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
