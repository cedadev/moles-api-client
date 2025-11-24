from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vocab_service_enum import VocabServiceEnum

T = TypeVar("T", bound="VocabularyTermRead")


@_attrs_define
class VocabularyTermRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            vocab_service (VocabServiceEnum): * `clipc_skos_vocab` - CLIPC SKOS Vocabulary Service
                * `nerc_skos_vocab` - NERC SKOS Vocabulary Service
            uri (str):
            resolved_term (None | str):
    """

    ob_id: int
    vocab_service: VocabServiceEnum
    uri: str
    resolved_term: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        vocab_service = self.vocab_service.value

        uri = self.uri

        resolved_term: None | str
        resolved_term = self.resolved_term

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "vocabService": vocab_service,
                "uri": uri,
                "resolvedTerm": resolved_term,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        vocab_service = VocabServiceEnum(d.pop("vocabService"))

        uri = d.pop("uri")

        def _parse_resolved_term(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_term = _parse_resolved_term(d.pop("resolvedTerm"))

        vocabulary_term_read = cls(
            ob_id=ob_id,
            vocab_service=vocab_service,
            uri=uri,
            resolved_term=resolved_term,
        )

        vocabulary_term_read.additional_properties = d
        return vocabulary_term_read

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
