from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcedureAcquisitionWriteRequest")


@_attrs_define
class ProcedureAcquisitionWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            title (str):
            abstract (str | Unset):
            output_description (int | None | Unset):
            image_details (list[int] | Unset):
            independent_instrument (list[int] | Unset):
            mobile_platform_operation (list[int] | Unset):
    """

    title: str
    abstract: str | Unset = UNSET
    output_description: int | None | Unset = UNSET
    image_details: list[int] | Unset = UNSET
    independent_instrument: list[int] | Unset = UNSET
    mobile_platform_operation: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        abstract = self.abstract

        output_description: int | None | Unset
        if isinstance(self.output_description, Unset):
            output_description = UNSET
        else:
            output_description = self.output_description

        image_details: list[int] | Unset = UNSET
        if not isinstance(self.image_details, Unset):
            image_details = ",".join(map(str, self.image_details))

        independent_instrument: list[int] | Unset = UNSET
        if not isinstance(self.independent_instrument, Unset):
            independent_instrument = ",".join(map(str, self.independent_instrument))

        mobile_platform_operation: list[int] | Unset = UNSET
        if not isinstance(self.mobile_platform_operation, Unset):
            mobile_platform_operation = ",".join(map(str, self.mobile_platform_operation))

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        abstract = d.pop("abstract", UNSET)

        def _parse_output_description(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        output_description = _parse_output_description(d.pop("outputDescription", UNSET))

        image_details = cast(list[int], d.pop("imageDetails", UNSET))

        independent_instrument = cast(list[int], d.pop("independentInstrument", UNSET))

        mobile_platform_operation = cast(list[int], d.pop("mobilePlatformOperation", UNSET))

        procedure_acquisition_write_request = cls(
            title=title,
            abstract=abstract,
            output_description=output_description,
            image_details=image_details,
            independent_instrument=independent_instrument,
            mobile_platform_operation=mobile_platform_operation,
        )

        procedure_acquisition_write_request.additional_properties = d
        return procedure_acquisition_write_request

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
