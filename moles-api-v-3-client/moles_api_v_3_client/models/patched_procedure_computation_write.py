from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedProcedureComputationWrite")


@_attrs_define
class PatchedProcedureComputationWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (Union[Unset, int]):
            uuid (Union[Unset, str]):
            short_code (Union[Unset, str]):
            title (Union[Unset, str]):
            abstract (Union[Unset, str]):
            keywords (Union[Unset, str]):
            input_description (Union[None, Unset, int]):
            output_description (Union[None, Unset, int]):
            software_reference (Union[None, Unset, int]):
            image_details (Union[Unset, list[int]]):
    """

    ob_id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    short_code: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
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
            image_details = self.image_details

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
        if input_description is not UNSET:
            field_dict["inputDescription"] = input_description
        if output_description is not UNSET:
            field_dict["outputDescription"] = output_description
        if software_reference is not UNSET:
            field_dict["softwareReference"] = software_reference
        if image_details is not UNSET:
            field_dict["imageDetails"] = image_details

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

        if not isinstance(self.input_description, Unset):
            if isinstance(self.input_description, int):
                files.append(("inputDescription", (None, str(self.input_description).encode(), "text/plain")))
            else:
                files.append(("inputDescription", (None, str(self.input_description).encode(), "text/plain")))

        if not isinstance(self.output_description, Unset):
            if isinstance(self.output_description, int):
                files.append(("outputDescription", (None, str(self.output_description).encode(), "text/plain")))
            else:
                files.append(("outputDescription", (None, str(self.output_description).encode(), "text/plain")))

        if not isinstance(self.software_reference, Unset):
            if isinstance(self.software_reference, int):
                files.append(("softwareReference", (None, str(self.software_reference).encode(), "text/plain")))
            else:
                files.append(("softwareReference", (None, str(self.software_reference).encode(), "text/plain")))

        if not isinstance(self.image_details, Unset):
            for image_details_item_element in self.image_details:
                files.append(("imageDetails", (None, str(image_details_item_element).encode(), "text/plain")))

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

        patched_procedure_computation_write = cls(
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

        patched_procedure_computation_write.additional_properties = d
        return patched_procedure_computation_write

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
