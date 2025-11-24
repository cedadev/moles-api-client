from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProcedureComputationRead")


@_attrs_define
class ProcedureComputationRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            uuid (str):
            short_code (str):
            title (str):
            abstract (str):
            keywords (str):
            input_description (int | None):
            output_description (int | None):
            software_reference (int | None):
            image_details (list[int | None]):
            identifier_set (list[int | None]):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    abstract: str
    keywords: str
    input_description: int | None
    output_description: int | None
    software_reference: int | None
    image_details: list[int | None]
    identifier_set: list[int | None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        abstract = self.abstract

        keywords = self.keywords

        input_description: int | None
        input_description = self.input_description

        output_description: int | None
        output_description = self.output_description

        software_reference: int | None
        software_reference = self.software_reference

        image_details = []
        for image_details_item_data in self.image_details:
            image_details_item: int | None
            image_details_item = image_details_item_data
            image_details.append(image_details_item)

        identifier_set = []
        for identifier_set_item_data in self.identifier_set:
            identifier_set_item: int | None
            identifier_set_item = identifier_set_item_data
            identifier_set.append(identifier_set_item)

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
                "inputDescription": input_description,
                "outputDescription": output_description,
                "softwareReference": software_reference,
                "imageDetails": image_details,
                "identifier_set": identifier_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        uuid = d.pop("uuid")

        short_code = d.pop("short_code")

        title = d.pop("title")

        abstract = d.pop("abstract")

        keywords = d.pop("keywords")

        def _parse_input_description(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        input_description = _parse_input_description(d.pop("inputDescription"))

        def _parse_output_description(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        output_description = _parse_output_description(d.pop("outputDescription"))

        def _parse_software_reference(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        software_reference = _parse_software_reference(d.pop("softwareReference"))

        image_details = []
        _image_details = d.pop("imageDetails")
        for image_details_item_data in _image_details:

            def _parse_image_details_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            image_details_item = _parse_image_details_item(image_details_item_data)

            image_details.append(image_details_item)

        identifier_set = []
        _identifier_set = d.pop("identifier_set")
        for identifier_set_item_data in _identifier_set:

            def _parse_identifier_set_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            identifier_set_item = _parse_identifier_set_item(identifier_set_item_data)

            identifier_set.append(identifier_set_item)

        procedure_computation_read = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            keywords=keywords,
            input_description=input_description,
            output_description=output_description,
            software_reference=software_reference,
            image_details=image_details,
            identifier_set=identifier_set,
        )

        procedure_computation_read.additional_properties = d
        return procedure_computation_read

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
