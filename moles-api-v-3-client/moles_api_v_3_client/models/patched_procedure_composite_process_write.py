from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedProcedureCompositeProcessWrite")


@_attrs_define
class PatchedProcedureCompositeProcessWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (Union[Unset, int]):
            uuid (Union[Unset, str]):
            short_code (Union[Unset, str]):
            title (Union[Unset, str]):
            abstract (Union[Unset, str]):
            computation_component (Union[Unset, list[int]]):
            acquisition_component (Union[Unset, list[int]]):
    """

    ob_id: Union[Unset, int] = UNSET
    uuid: Union[Unset, str] = UNSET
    short_code: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    abstract: Union[Unset, str] = UNSET
    computation_component: Union[Unset, list[int]] = UNSET
    acquisition_component: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

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
        if computation_component is not UNSET:
            field_dict["computationComponent"] = computation_component
        if acquisition_component is not UNSET:
            field_dict["acquisitionComponent"] = acquisition_component

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

        if not isinstance(self.computation_component, Unset):
            for computation_component_item_element in self.computation_component:
                files.append(
                    ("computationComponent", (None, str(computation_component_item_element).encode(), "text/plain"))
                )

        if not isinstance(self.acquisition_component, Unset):
            for acquisition_component_item_element in self.acquisition_component:
                files.append(
                    ("acquisitionComponent", (None, str(acquisition_component_item_element).encode(), "text/plain"))
                )

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

        computation_component = cast(list[int], d.pop("computationComponent", UNSET))

        acquisition_component = cast(list[int], d.pop("acquisitionComponent", UNSET))

        patched_procedure_composite_process_write = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            computation_component=computation_component,
            acquisition_component=acquisition_component,
        )

        patched_procedure_composite_process_write.additional_properties = d
        return patched_procedure_composite_process_write

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
