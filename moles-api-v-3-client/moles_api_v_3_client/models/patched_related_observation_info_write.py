from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.relation_type_enum import RelationTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedRelatedObservationInfoWrite")


@_attrs_define
class PatchedRelatedObservationInfoWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (Union[Unset, int]):
            subject_observation (Union[Unset, int]):
            relation_type (Union[Unset, RelationTypeEnum]): * `IsSupplementTo` - supplement to
                * `IsSupplementedBy` - supplemented by
                * `Continues` - continues
                * `IsNewVersionOf` - supersedes
                * `IsVariantFormOf` - a variant of
                * `IsIdenticalTo` - identical to
                * `HasMetadata` - uses metadata from
                * `IsDerivedFrom` - derived from
                * `IsPartOf` - is part of (dataset only)
            object_observation (Union[Unset, int]):
    """

    ob_id: Union[Unset, int] = UNSET
    subject_observation: Union[Unset, int] = UNSET
    relation_type: Union[Unset, RelationTypeEnum] = UNSET
    object_observation: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        subject_observation = self.subject_observation

        relation_type: Union[Unset, str] = UNSET
        if not isinstance(self.relation_type, Unset):
            relation_type = self.relation_type.value

        object_observation = self.object_observation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
        if subject_observation is not UNSET:
            field_dict["subjectObservation"] = subject_observation
        if relation_type is not UNSET:
            field_dict["relationType"] = relation_type
        if object_observation is not UNSET:
            field_dict["objectObservation"] = object_observation

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.ob_id, Unset):
            files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        if not isinstance(self.subject_observation, Unset):
            files.append(("subjectObservation", (None, str(self.subject_observation).encode(), "text/plain")))

        if not isinstance(self.relation_type, Unset):
            files.append(("relationType", (None, str(self.relation_type.value).encode(), "text/plain")))

        if not isinstance(self.object_observation, Unset):
            files.append(("objectObservation", (None, str(self.object_observation).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        subject_observation = d.pop("subjectObservation", UNSET)

        _relation_type = d.pop("relationType", UNSET)
        relation_type: Union[Unset, RelationTypeEnum]
        if isinstance(_relation_type, Unset):
            relation_type = UNSET
        else:
            relation_type = RelationTypeEnum(_relation_type)

        object_observation = d.pop("objectObservation", UNSET)

        patched_related_observation_info_write = cls(
            ob_id=ob_id,
            subject_observation=subject_observation,
            relation_type=relation_type,
            object_observation=object_observation,
        )

        patched_related_observation_info_write.additional_properties = d
        return patched_related_observation_info_write

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
