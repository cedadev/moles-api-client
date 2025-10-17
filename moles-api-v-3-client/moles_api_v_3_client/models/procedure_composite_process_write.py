from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcedureCompositeProcessWrite")


@_attrs_define
class ProcedureCompositeProcessWrite:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            uuid (str):
            short_code (str):
            title (str):
            computation_component (list[int]):
            acquisition_component (list[int]):
            abstract (Union[Unset, str]):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    computation_component: list[int]
    acquisition_component: list[int]
    abstract: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        computation_component = self.computation_component

        acquisition_component = self.acquisition_component

        abstract = self.abstract

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "short_code": short_code,
                "title": title,
                "computationComponent": computation_component,
                "acquisitionComponent": acquisition_component,
            }
        )
        if abstract is not UNSET:
            field_dict["abstract"] = abstract

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        uuid = d.pop("uuid")

        short_code = d.pop("short_code")

        title = d.pop("title")

        computation_component = cast(list[int], d.pop("computationComponent"))

        acquisition_component = cast(list[int], d.pop("acquisitionComponent"))

        abstract = d.pop("abstract", UNSET)

        procedure_composite_process_write = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            computation_component=computation_component,
            acquisition_component=acquisition_component,
            abstract=abstract,
        )

        procedure_composite_process_write.additional_properties = d
        return procedure_composite_process_write

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
