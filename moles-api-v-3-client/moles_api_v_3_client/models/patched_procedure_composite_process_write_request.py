from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedProcedureCompositeProcessWriteRequest")


@_attrs_define
class PatchedProcedureCompositeProcessWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            title (Union[Unset, str]):
            abstract (Union[Unset, str]):
            computation_component (Union[Unset, list[int]]):
            acquisition_component (Union[Unset, list[int]]):
    """

    title: Union[Unset, str] = UNSET
    abstract: Union[Unset, str] = UNSET
    computation_component: Union[Unset, list[int]] = UNSET
    acquisition_component: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        abstract = self.abstract

        computation_component: Union[Unset, list[int]] = UNSET
        if not isinstance(self.computation_component, Unset):
            computation_component = self.computation_component

        acquisition_component: Union[Unset, list[int]] = UNSET
        if not isinstance(self.acquisition_component, Unset):
            acquisition_component = self.acquisition_component

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if abstract is not UNSET:
            field_dict["abstract"] = abstract
        if computation_component is not UNSET:
            field_dict["computationComponent"] = computation_component
        if acquisition_component is not UNSET:
            field_dict["acquisitionComponent"] = acquisition_component

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        abstract = d.pop("abstract", UNSET)

        computation_component = cast(list[int], d.pop("computationComponent", UNSET))

        acquisition_component = cast(list[int], d.pop("acquisitionComponent", UNSET))

        patched_procedure_composite_process_write_request = cls(
            title=title,
            abstract=abstract,
            computation_component=computation_component,
            acquisition_component=acquisition_component,
        )

        patched_procedure_composite_process_write_request.additional_properties = d
        return patched_procedure_composite_process_write_request

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
