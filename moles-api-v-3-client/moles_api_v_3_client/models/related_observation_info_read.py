from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.relation_type_enum import RelationTypeEnum

if TYPE_CHECKING:
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="RelatedObservationInfoRead")


@_attrs_define
class RelatedObservationInfoRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            relation_type (RelationTypeEnum): * `IsSupplementTo` - supplement to
                * `IsSupplementedBy` - supplemented by
                * `Continues` - continues
                * `IsNewVersionOf` - supersedes
                * `IsVariantFormOf` - a variant of
                * `IsIdenticalTo` - identical to
                * `HasMetadata` - uses metadata from
                * `IsDerivedFrom` - derived from
                * `IsPartOf` - is part of (dataset only)
            subject_observation (SimpleRead): A mixin that adds 'simple_fields' as ReadOnlyFields
                and reorders them to the top.
            object_observation (SimpleRead): A mixin that adds 'simple_fields' as ReadOnlyFields
                and reorders them to the top.
    """

    ob_id: int
    relation_type: RelationTypeEnum
    subject_observation: "SimpleRead"
    object_observation: "SimpleRead"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        relation_type = self.relation_type.value

        subject_observation = self.subject_observation.to_dict()

        object_observation = self.object_observation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "relationType": relation_type,
                "subjectObservation": subject_observation,
                "objectObservation": object_observation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_read import SimpleRead

        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        relation_type = RelationTypeEnum(d.pop("relationType"))

        subject_observation = SimpleRead.from_dict(d.pop("subjectObservation"))

        object_observation = SimpleRead.from_dict(d.pop("objectObservation"))

        related_observation_info_read = cls(
            ob_id=ob_id,
            relation_type=relation_type,
            subject_observation=subject_observation,
            object_observation=object_observation,
        )

        related_observation_info_read.additional_properties = d
        return related_observation_info_read

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
