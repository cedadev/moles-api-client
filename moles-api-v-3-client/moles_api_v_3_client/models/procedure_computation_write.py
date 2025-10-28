from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcedureComputationWrite")


@_attrs_define
class ProcedureComputationWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            uuid (str):
            short_code (str):
            title (str):
            abstract (Union[Unset, str]):
            keywords (Union[Unset, str]):
            input_description (Union[None, Unset, int]):
            output_description (Union[None, Unset, int]):
            software_reference (Union[None, Unset, int]):
            image_details (Union[Unset, list[int]]):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    abstract: Union[Unset, str] = UNSET
    keywords: Union[Unset, str] = UNSET
    input_description: Union[None, Unset, int] = UNSET
    output_description: Union[None, Unset, int] = UNSET
    software_reference: Union[None, Unset, int] = UNSET
    image_details: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        abstract = self.abstract

        keywords = self.keywords

        input_description: Union[None, Unset, int]
        if isinstance(self.input_description, Unset):
            input_description = UNSET
        else:
            input_description = self.input_description

        output_description: Union[None, Unset, int]
        if isinstance(self.output_description, Unset):
            output_description = UNSET
        else:
            output_description = self.output_description

        software_reference: Union[None, Unset, int]
        if isinstance(self.software_reference, Unset):
            software_reference = UNSET
        else:
            software_reference = self.software_reference

        image_details: Union[Unset, list[int]] = UNSET
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
        if input_description is not UNSET:
            field_dict["inputDescription"] = input_description
        if output_description is not UNSET:
            field_dict["outputDescription"] = output_description
        if software_reference is not UNSET:
            field_dict["softwareReference"] = software_reference
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

        def _parse_input_description(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        input_description = _parse_input_description(d.pop("inputDescription", UNSET))

        def _parse_output_description(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        output_description = _parse_output_description(d.pop("outputDescription", UNSET))

        def _parse_software_reference(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        software_reference = _parse_software_reference(d.pop("softwareReference", UNSET))

        image_details = cast(list[int], d.pop("imageDetails", UNSET))

        procedure_computation_write = cls(
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
        )

        procedure_computation_write.additional_properties = d
        return procedure_computation_write

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
