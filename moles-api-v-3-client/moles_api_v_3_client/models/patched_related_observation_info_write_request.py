from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relation_type_enum import RelationTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRelatedObservationInfoWriteRequest")


@_attrs_define
class PatchedRelatedObservationInfoWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            subject_observation (int | Unset):
            relation_type (RelationTypeEnum | Unset): * `IsSupplementTo` - supplement to
                * `IsSupplementedBy` - supplemented by
                * `Continues` - continues
                * `IsNewVersionOf` - supersedes
                * `IsVariantFormOf` - a variant of
                * `IsIdenticalTo` - identical to
                * `HasMetadata` - uses metadata from
                * `IsDerivedFrom` - derived from
                * `IsPartOf` - is part of (dataset only)
            object_observation (int | Unset):
    """

    subject_observation: int | Unset = UNSET
    relation_type: RelationTypeEnum | Unset = UNSET
    object_observation: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject_observation = self.subject_observation

        relation_type: str | Unset = UNSET
        if not isinstance(self.relation_type, Unset):
            relation_type = self.relation_type.value

        object_observation = self.object_observation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject_observation is not UNSET:
            field_dict["subjectObservation"] = subject_observation
        if relation_type is not UNSET:
            field_dict["relationType"] = relation_type
        if object_observation is not UNSET:
            field_dict["objectObservation"] = object_observation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject_observation = d.pop("subjectObservation", UNSET)

        _relation_type = d.pop("relationType", UNSET)
        relation_type: RelationTypeEnum | Unset
        if isinstance(_relation_type, Unset):
            relation_type = UNSET
        else:
            relation_type = RelationTypeEnum(_relation_type)

        object_observation = d.pop("objectObservation", UNSET)

        patched_related_observation_info_write_request = cls(
            subject_observation=subject_observation,
            relation_type=relation_type,
            object_observation=object_observation,
        )

        patched_related_observation_info_write_request.additional_properties = d
        return patched_related_observation_info_write_request

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
