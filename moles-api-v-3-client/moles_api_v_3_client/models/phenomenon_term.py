from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.label_enum import LabelEnum
from ..models.vocabulary_enum import VocabularyEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PhenomenonTerm")


@_attrs_define
class PhenomenonTerm:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            label (LabelEnum): * `units` - Units
                * `var_id` - variable Id
                * `standard_name` - Standard name
                * `long_name` - Long name
                * `gcmd_keyword` - GCMD keyword
                * `gcmd_url` - GCMD URL
                * `gcmd_name` - GCMD keyword
                * `alt_names` - Alternative Names
                * `names` - Names
            value (str):
            vocabulary (Union[BlankEnum, Unset, VocabularyEnum]):
    """

    ob_id: int
    label: LabelEnum
    value: str
    vocabulary: Union[BlankEnum, Unset, VocabularyEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        label = self.label.value

        value = self.value

        vocabulary: Union[Unset, str]
        if isinstance(self.vocabulary, Unset):
            vocabulary = UNSET
        elif isinstance(self.vocabulary, VocabularyEnum):
            vocabulary = self.vocabulary.value
        else:
            vocabulary = self.vocabulary.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "label": label,
                "value": value,
            }
        )
        if vocabulary is not UNSET:
            field_dict["vocabulary"] = vocabulary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        label = LabelEnum(d.pop("label"))

        value = d.pop("value")

        def _parse_vocabulary(data: object) -> Union[BlankEnum, Unset, VocabularyEnum]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vocabulary_type_0 = VocabularyEnum(data)

                return vocabulary_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            vocabulary_type_1 = BlankEnum(data)

            return vocabulary_type_1

        vocabulary = _parse_vocabulary(d.pop("vocabulary", UNSET))

        phenomenon_term = cls(
            ob_id=ob_id,
            label=label,
            value=value,
            vocabulary=vocabulary,
        )

        phenomenon_term.additional_properties = d
        return phenomenon_term

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
