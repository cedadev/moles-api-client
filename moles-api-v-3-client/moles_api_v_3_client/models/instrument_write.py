from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.instrument_type_enum import InstrumentTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstrumentWrite")


@_attrs_define
class InstrumentWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            uuid (str):
            short_code (str):
            title (str):
            abstract (str | Unset):
            keywords (str | Unset):
            instrument_type (BlankEnum | InstrumentTypeEnum | Unset):
            image_details (list[int] | Unset):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    abstract: str | Unset = UNSET
    keywords: str | Unset = UNSET
    instrument_type: BlankEnum | InstrumentTypeEnum | Unset = UNSET
    image_details: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        abstract = self.abstract

        keywords = self.keywords

        instrument_type: str | Unset
        if isinstance(self.instrument_type, Unset):
            instrument_type = UNSET
        elif isinstance(self.instrument_type, InstrumentTypeEnum):
            instrument_type = self.instrument_type.value
        else:
            instrument_type = self.instrument_type.value

        image_details: list[int] | Unset = UNSET
        if not isinstance(self.image_details, Unset):
            image_details = ",".join(map(str, self.image_details))

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "short_code": short_code,
                "title": title,
            }
        )
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if instrument_type is not UNSET:
            field_dict["instrumentType"] = instrument_type
        if image_details is not UNSET:
            field_dict["imageDetails"] = image_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        uuid = d.pop("uuid")

        short_code = d.pop("short_code")

        title = d.pop("title")

        abstract = d.pop("abstract", UNSET)

        keywords = d.pop("keywords", UNSET)

        def _parse_instrument_type(data: object) -> BlankEnum | InstrumentTypeEnum | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                instrument_type_type_0 = InstrumentTypeEnum(data)

                return instrument_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, str):
                raise TypeError()
            instrument_type_type_1 = BlankEnum(data)

            return instrument_type_type_1

        instrument_type = _parse_instrument_type(d.pop("instrumentType", UNSET))

        image_details = cast(list[int], d.pop("imageDetails", UNSET))

        instrument_write = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            keywords=keywords,
            instrument_type=instrument_type,
            image_details=image_details,
        )

        instrument_write.additional_properties = d
        return instrument_write

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
