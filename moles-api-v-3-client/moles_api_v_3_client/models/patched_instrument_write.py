from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum
from ..models.instrument_type_enum import InstrumentTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedInstrumentWrite")


@_attrs_define
class PatchedInstrumentWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (Union[Unset, int]):
            uuid (Union[Unset, str]):
            short_code (Union[Unset, str]):
            title (Union[Unset, str]):
            abstract (Union[Unset, str]):
            keywords (Union[Unset, str]):
            instrument_type (Union[BlankEnum, InstrumentTypeEnum, Unset]):
            image_details (Union[Unset, list[int]]):
            sub_instrument (Union[Unset, list[int]]):
    """

    ob_id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    short_code: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    abstract: Union[Unset, str] = UNSET
    keywords: Union[Unset, str] = UNSET
    instrument_type: Union[BlankEnum, InstrumentTypeEnum, Unset] = UNSET
    image_details: Union[Unset, list[int]] = UNSET
    sub_instrument: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        abstract = self.abstract

        keywords = self.keywords

        instrument_type: Union[Unset, str]
        if isinstance(self.instrument_type, Unset):
            instrument_type = UNSET
        elif isinstance(self.instrument_type, InstrumentTypeEnum):
            instrument_type = self.instrument_type.value
        else:
            instrument_type = self.instrument_type.value

        image_details: Union[Unset, list[int]] = UNSET
        if not isinstance(self.image_details, Unset):
            image_details = self.image_details

        sub_instrument: Union[Unset, list[int]] = UNSET
        if not isinstance(self.sub_instrument, Unset):
            sub_instrument = self.sub_instrument

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ob_id is not UNSET:
            field_dict["ob_id"] = ob_id
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if short_code is not UNSET:
            field_dict["short_code"] = short_code
        if title is not UNSET:
            field_dict["title"] = title
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if instrument_type is not UNSET:
            field_dict["instrumentType"] = instrument_type
        if image_details is not UNSET:
            field_dict["imageDetails"] = image_details
        if sub_instrument is not UNSET:
            field_dict["subInstrument"] = sub_instrument

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.ob_id, Unset):
            files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        if not isinstance(self.uuid, Unset):
            files.append(("uuid", (None, str(self.uuid).encode(), "text/plain")))

        if not isinstance(self.short_code, Unset):
            files.append(("short_code", (None, str(self.short_code).encode(), "text/plain")))

        if not isinstance(self.title, Unset):
            files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.abstract, Unset):
            files.append(("abstract", (None, str(self.abstract).encode(), "text/plain")))

        if not isinstance(self.keywords, Unset):
            files.append(("keywords", (None, str(self.keywords).encode(), "text/plain")))

        if not isinstance(self.instrument_type, Unset):
            if isinstance(self.instrument_type, InstrumentTypeEnum):
                files.append(("instrumentType", (None, str(self.instrument_type.value).encode(), "text/plain")))
            else:
                files.append(("instrumentType", (None, str(self.instrument_type.value).encode(), "text/plain")))

        if not isinstance(self.image_details, Unset):
            for image_details_item_element in self.image_details:
                files.append(("imageDetails", (None, str(image_details_item_element).encode(), "text/plain")))

        if not isinstance(self.sub_instrument, Unset):
            for sub_instrument_item_element in self.sub_instrument:
                files.append(("subInstrument", (None, str(sub_instrument_item_element).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id", UNSET)

        uuid = d.pop("uuid", UNSET)

        short_code = d.pop("short_code", UNSET)

        title = d.pop("title", UNSET)

        abstract = d.pop("abstract", UNSET)

        keywords = d.pop("keywords", UNSET)

        def _parse_instrument_type(data: object) -> Union[BlankEnum, InstrumentTypeEnum, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                instrument_type_type_0 = InstrumentTypeEnum(data)

                return instrument_type_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            instrument_type_type_1 = BlankEnum(data)

            return instrument_type_type_1

        instrument_type = _parse_instrument_type(d.pop("instrumentType", UNSET))

        image_details = cast(list[int], d.pop("imageDetails", UNSET))

        sub_instrument = cast(list[int], d.pop("subInstrument", UNSET))

        patched_instrument_write = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            keywords=keywords,
            instrument_type=instrument_type,
            image_details=image_details,
            sub_instrument=sub_instrument,
        )

        patched_instrument_write.additional_properties = d
        return patched_instrument_write

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
