from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vocab_service_enum import VocabServiceEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedVocabularyTermWrite")


@_attrs_define
class PatchedVocabularyTermWrite:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (Union[Unset, int]):
            vocab_service (Union[Unset, VocabServiceEnum]): * `clipc_skos_vocab` - CLIPC SKOS Vocabulary Service
                * `nerc_skos_vocab` - NERC SKOS Vocabulary Service
            uri (Union[Unset, str]):
            resolved_term (Union[None, Unset, str]):
    """

    ob_id: Union[Unset, int] = UNSET
    vocab_service: Union[Unset, VocabServiceEnum] = UNSET
    uri: Union[Unset, str] = UNSET
    resolved_term: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        vocab_service: Union[Unset, str] = UNSET
        if not isinstance(self.vocab_service, Unset):
            vocab_service = self.vocab_service.value

        uri = self.uri

        resolved_term: Union[None, Unset, str]
        if isinstance(self.resolved_term, Unset):
            resolved_term = UNSET
        else:
            resolved_term = self.resolved_term

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
        if vocab_service is not UNSET:
            field_dict["vocabService"] = vocab_service
        if uri is not UNSET:
            field_dict["uri"] = uri
        if resolved_term is not UNSET:
            field_dict["resolvedTerm"] = resolved_term

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        _vocab_service = d.pop("vocabService", UNSET)
        vocab_service: Union[Unset, VocabServiceEnum]
        if isinstance(_vocab_service, Unset):
            vocab_service = UNSET
        else:
            vocab_service = VocabServiceEnum(_vocab_service)

        uri = d.pop("uri", UNSET)

        def _parse_resolved_term(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resolved_term = _parse_resolved_term(d.pop("resolvedTerm", UNSET))

        patched_vocabulary_term_write = cls(
            ob_id=ob_id,
            vocab_service=vocab_service,
            uri=uri,
            resolved_term=resolved_term,
        )

        patched_vocabulary_term_write.additional_properties = d
        return patched_vocabulary_term_write

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
