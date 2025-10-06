from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcedureAcquisitionWrite")


@_attrs_define
class ProcedureAcquisitionWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            uuid (str):
            short_code (str):
            title (str):
            abstract (Union[Unset, str]):
            output_description (Union[None, Unset, int]):
            image_details (Union[Unset, list[int]]):
            independent_instrument (Union[Unset, list[int]]):
            mobile_platform_operation (Union[Unset, list[int]]):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    abstract: Union[Unset, str] = UNSET
    output_description: Union[None, Unset, int] = UNSET
    image_details: Union[Unset, list[int]] = UNSET
    independent_instrument: Union[Unset, list[int]] = UNSET
    mobile_platform_operation: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        abstract = self.abstract

        output_description: Union[None, Unset, int]
        if isinstance(self.output_description, Unset):
            output_description = UNSET
        else:
            output_description = self.output_description

        image_details: Union[Unset, list[int]] = UNSET
        if not isinstance(self.image_details, Unset):
            image_details = self.image_details

        independent_instrument: Union[Unset, list[int]] = UNSET
        if not isinstance(self.independent_instrument, Unset):
            independent_instrument = self.independent_instrument

        mobile_platform_operation: Union[Unset, list[int]] = UNSET
        if not isinstance(self.mobile_platform_operation, Unset):
            mobile_platform_operation = self.mobile_platform_operation

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
        if output_description is not UNSET:
            field_dict["outputDescription"] = output_description
        if image_details is not UNSET:
            field_dict["imageDetails"] = image_details
        if independent_instrument is not UNSET:
            field_dict["independentInstrument"] = independent_instrument
        if mobile_platform_operation is not UNSET:
            field_dict["mobilePlatformOperation"] = mobile_platform_operation

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        files.append(("uuid", (None, str(self.uuid).encode(), "text/plain")))

        files.append(("short_code", (None, str(self.short_code).encode(), "text/plain")))

        files.append(("title", (None, str(self.title).encode(), "text/plain")))

        if not isinstance(self.abstract, Unset):
            files.append(("abstract", (None, str(self.abstract).encode(), "text/plain")))

        if not isinstance(self.output_description, Unset):
            if isinstance(self.output_description, int):
                files.append(("outputDescription", (None, str(self.output_description).encode(), "text/plain")))
            else:
                files.append(("outputDescription", (None, str(self.output_description).encode(), "text/plain")))

        if not isinstance(self.image_details, Unset):
            for image_details_item_element in self.image_details:
                files.append(("imageDetails", (None, str(image_details_item_element).encode(), "text/plain")))

        if not isinstance(self.independent_instrument, Unset):
            for independent_instrument_item_element in self.independent_instrument:
                files.append(
                    ("independentInstrument", (None, str(independent_instrument_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.mobile_platform_operation, Unset):
            for mobile_platform_operation_item_element in self.mobile_platform_operation:
                files.append(
                    (
                        "mobilePlatformOperation",
                        (None, str(mobile_platform_operation_item_element).encode(), "text/plain"),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        uuid = d.pop("uuid")

        short_code = d.pop("short_code")

        title = d.pop("title")

        abstract = d.pop("abstract", UNSET)

        def _parse_output_description(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        output_description = _parse_output_description(d.pop("outputDescription", UNSET))

        image_details = cast(list[int], d.pop("imageDetails", UNSET))

        independent_instrument = cast(list[int], d.pop("independentInstrument", UNSET))

        mobile_platform_operation = cast(list[int], d.pop("mobilePlatformOperation", UNSET))

        procedure_acquisition_write = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            output_description=output_description,
            image_details=image_details,
            independent_instrument=independent_instrument,
            mobile_platform_operation=mobile_platform_operation,
        )

        procedure_acquisition_write.additional_properties = d
        return procedure_acquisition_write

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
