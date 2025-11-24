from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="ProcedureCompositeProcessRead")


@_attrs_define
class ProcedureCompositeProcessRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            uuid (str):
            title (str):
            abstract (str):
            computation_component (list[SimpleRead] | None):
            acquisition_component (list[SimpleRead] | None):
            identifier_set (list[int | None]):
            responsiblepartyinfo_set (list[int | None]):
    """

    ob_id: int
    uuid: str
    title: str
    abstract: str
    computation_component: list[SimpleRead] | None
    acquisition_component: list[SimpleRead] | None
    identifier_set: list[int | None]
    responsiblepartyinfo_set: list[int | None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        title = self.title

        abstract = self.abstract

        computation_component: list[dict[str, Any]] | None
        if isinstance(self.computation_component, list):
            computation_component = []
            for computation_component_type_0_item_data in self.computation_component:
                computation_component_type_0_item = computation_component_type_0_item_data.to_dict()
                computation_component.append(computation_component_type_0_item)

        else:
            computation_component = self.computation_component

        acquisition_component: list[dict[str, Any]] | None
        if isinstance(self.acquisition_component, list):
            acquisition_component = []
            for acquisition_component_type_0_item_data in self.acquisition_component:
                acquisition_component_type_0_item = acquisition_component_type_0_item_data.to_dict()
                acquisition_component.append(acquisition_component_type_0_item)

        else:
            acquisition_component = self.acquisition_component

        identifier_set = []
        for identifier_set_item_data in self.identifier_set:
            identifier_set_item: int | None
            identifier_set_item = identifier_set_item_data
            identifier_set.append(identifier_set_item)

        responsiblepartyinfo_set = []
        for responsiblepartyinfo_set_item_data in self.responsiblepartyinfo_set:
            responsiblepartyinfo_set_item: int | None
            responsiblepartyinfo_set_item = responsiblepartyinfo_set_item_data
            responsiblepartyinfo_set.append(responsiblepartyinfo_set_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "title": title,
                "abstract": abstract,
                "computationComponent": computation_component,
                "acquisitionComponent": acquisition_component,
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

        title = d.pop("title")

        abstract = d.pop("abstract")

        def _parse_computation_component(data: object) -> list[SimpleRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                computation_component_type_0 = []
                _computation_component_type_0 = data
                for computation_component_type_0_item_data in _computation_component_type_0:
                    computation_component_type_0_item = SimpleRead.from_dict(computation_component_type_0_item_data)

                    computation_component_type_0.append(computation_component_type_0_item)

                return computation_component_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleRead] | None, data)

        computation_component = _parse_computation_component(d.pop("computationComponent"))

        def _parse_acquisition_component(data: object) -> list[SimpleRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                acquisition_component_type_0 = []
                _acquisition_component_type_0 = data
                for acquisition_component_type_0_item_data in _acquisition_component_type_0:
                    acquisition_component_type_0_item = SimpleRead.from_dict(acquisition_component_type_0_item_data)

                    acquisition_component_type_0.append(acquisition_component_type_0_item)

                return acquisition_component_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleRead] | None, data)

        acquisition_component = _parse_acquisition_component(d.pop("acquisitionComponent"))

        identifier_set = []
        _identifier_set = d.pop("identifier_set")
        for identifier_set_item_data in _identifier_set:

            def _parse_identifier_set_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            identifier_set_item = _parse_identifier_set_item(identifier_set_item_data)

            identifier_set.append(identifier_set_item)

        responsiblepartyinfo_set = []
        _responsiblepartyinfo_set = d.pop("responsiblepartyinfo_set")
        for responsiblepartyinfo_set_item_data in _responsiblepartyinfo_set:

            def _parse_responsiblepartyinfo_set_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            responsiblepartyinfo_set_item = _parse_responsiblepartyinfo_set_item(responsiblepartyinfo_set_item_data)

            responsiblepartyinfo_set.append(responsiblepartyinfo_set_item)

        procedure_composite_process_read = cls(
            ob_id=ob_id,
            uuid=uuid,
            title=title,
            abstract=abstract,
            computation_component=computation_component,
            acquisition_component=acquisition_component,
            identifier_set=identifier_set,
            responsiblepartyinfo_set=responsiblepartyinfo_set,
        )

        procedure_composite_process_read.additional_properties = d
        return procedure_composite_process_read

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
