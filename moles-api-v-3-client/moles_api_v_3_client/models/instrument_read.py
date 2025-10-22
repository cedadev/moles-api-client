from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum
from ..models.instrument_type_enum import InstrumentTypeEnum

if TYPE_CHECKING:
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="InstrumentRead")


@_attrs_define
class InstrumentRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            uuid (str):
            short_code (str):
            title (str):
            abstract (str):
            keywords (str):
            instrument_type (Union[BlankEnum, InstrumentTypeEnum]):
            image_details (list[Union[None, int]]):
            sub_instrument (Union[None, list['SimpleRead']]):
            identifier_set (list[Union[None, int]]):
            responsiblepartyinfo_set (list[Union[None, int]]):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    abstract: str
    keywords: str
    instrument_type: Union[BlankEnum, InstrumentTypeEnum]
    image_details: list[Union[None, int]]
    sub_instrument: Union[None, list["SimpleRead"]]
    identifier_set: list[Union[None, int]]
    responsiblepartyinfo_set: list[Union[None, int]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        abstract = self.abstract

        keywords = self.keywords

        instrument_type: str
        if isinstance(self.instrument_type, InstrumentTypeEnum):
            instrument_type = self.instrument_type.value
        else:
            instrument_type = self.instrument_type.value

        image_details = []
        for image_details_item_data in self.image_details:
            image_details_item: Union[None, int]
            image_details_item = image_details_item_data
            image_details.append(image_details_item)

        sub_instrument: Union[None, list[dict[str, Any]]]
        if isinstance(self.sub_instrument, list):
            sub_instrument = []
            for sub_instrument_type_0_item_data in self.sub_instrument:
                sub_instrument_type_0_item = sub_instrument_type_0_item_data.to_dict()
                sub_instrument.append(sub_instrument_type_0_item)

        else:
            sub_instrument = self.sub_instrument

        identifier_set = []
        for identifier_set_item_data in self.identifier_set:
            identifier_set_item: Union[None, int]
            identifier_set_item = identifier_set_item_data
            identifier_set.append(identifier_set_item)

        responsiblepartyinfo_set = []
        for responsiblepartyinfo_set_item_data in self.responsiblepartyinfo_set:
            responsiblepartyinfo_set_item: Union[None, int]
            responsiblepartyinfo_set_item = responsiblepartyinfo_set_item_data
            responsiblepartyinfo_set.append(responsiblepartyinfo_set_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "short_code": short_code,
                "title": title,
                "abstract": abstract,
                "keywords": keywords,
                "instrumentType": instrument_type,
                "imageDetails": image_details,
                "subInstrument": sub_instrument,
                "identifier_set": identifier_set,
                "responsiblepartyinfo_set": responsiblepartyinfo_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_read import SimpleRead

        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        uuid = d.pop("uuid")

        short_code = d.pop("short_code")

        title = d.pop("title")

        abstract = d.pop("abstract")

        keywords = d.pop("keywords")

        def _parse_instrument_type(data: object) -> Union[BlankEnum, InstrumentTypeEnum]:
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

        instrument_type = _parse_instrument_type(d.pop("instrumentType"))

        image_details = []
        _image_details = d.pop("imageDetails")
        for image_details_item_data in _image_details:

            def _parse_image_details_item(data: object) -> Union[None, int]:
                if data is None:
                    return data
                return cast(Union[None, int], data)

            image_details_item = _parse_image_details_item(image_details_item_data)

            image_details.append(image_details_item)

        def _parse_sub_instrument(data: object) -> Union[None, list["SimpleRead"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sub_instrument_type_0 = []
                _sub_instrument_type_0 = data
                for sub_instrument_type_0_item_data in _sub_instrument_type_0:
                    sub_instrument_type_0_item = SimpleRead.from_dict(sub_instrument_type_0_item_data)

                    sub_instrument_type_0.append(sub_instrument_type_0_item)

                return sub_instrument_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["SimpleRead"]], data)

        sub_instrument = _parse_sub_instrument(d.pop("subInstrument"))

        identifier_set = []
        _identifier_set = d.pop("identifier_set")
        for identifier_set_item_data in _identifier_set:

            def _parse_identifier_set_item(data: object) -> Union[None, int]:
                if data is None:
                    return data
                return cast(Union[None, int], data)

            identifier_set_item = _parse_identifier_set_item(identifier_set_item_data)

            identifier_set.append(identifier_set_item)

        responsiblepartyinfo_set = []
        _responsiblepartyinfo_set = d.pop("responsiblepartyinfo_set")
        for responsiblepartyinfo_set_item_data in _responsiblepartyinfo_set:

            def _parse_responsiblepartyinfo_set_item(data: object) -> Union[None, int]:
                if data is None:
                    return data
                return cast(Union[None, int], data)

            responsiblepartyinfo_set_item = _parse_responsiblepartyinfo_set_item(responsiblepartyinfo_set_item_data)

            responsiblepartyinfo_set.append(responsiblepartyinfo_set_item)

        instrument_read = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            keywords=keywords,
            instrument_type=instrument_type,
            image_details=image_details,
            sub_instrument=sub_instrument,
            identifier_set=identifier_set,
            responsiblepartyinfo_set=responsiblepartyinfo_set,
        )

        instrument_read.additional_properties = d
        return instrument_read

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
