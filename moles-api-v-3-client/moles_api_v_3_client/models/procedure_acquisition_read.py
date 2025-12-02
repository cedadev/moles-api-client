from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.instrument_platform_pair_read import InstrumentPlatformPairRead
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="ProcedureAcquisitionRead")


@_attrs_define
class ProcedureAcquisitionRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            uuid (None | str):
            short_code (None | str):
            title (None | str):
            abstract (None | str):
            image_details (list[int | None]):
            mobile_platform_operation (list[SimpleRead] | None):
            instrumentplatformpair_set (list[InstrumentPlatformPairRead] | None):
    """

    ob_id: int | None
    uuid: None | str
    short_code: None | str
    title: None | str
    abstract: None | str
    image_details: list[int | None]
    mobile_platform_operation: list[SimpleRead] | None
    instrumentplatformpair_set: list[InstrumentPlatformPairRead] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: int | None
        ob_id = self.ob_id

        uuid: None | str
        uuid = self.uuid

        short_code: None | str
        short_code = self.short_code

        title: None | str
        title = self.title

        abstract: None | str
        abstract = self.abstract

        image_details = []
        for image_details_item_data in self.image_details:
            image_details_item: int | None
            image_details_item = image_details_item_data
            image_details.append(image_details_item)

        mobile_platform_operation: list[dict[str, Any]] | None
        if isinstance(self.mobile_platform_operation, list):
            mobile_platform_operation = []
            for mobile_platform_operation_type_0_item_data in self.mobile_platform_operation:
                mobile_platform_operation_type_0_item = mobile_platform_operation_type_0_item_data.to_dict()
                mobile_platform_operation.append(mobile_platform_operation_type_0_item)

        else:
            mobile_platform_operation = self.mobile_platform_operation

        instrumentplatformpair_set: list[dict[str, Any]] | None
        if isinstance(self.instrumentplatformpair_set, list):
            instrumentplatformpair_set = []
            for instrumentplatformpair_set_type_0_item_data in self.instrumentplatformpair_set:
                instrumentplatformpair_set_type_0_item = instrumentplatformpair_set_type_0_item_data.to_dict()
                instrumentplatformpair_set.append(instrumentplatformpair_set_type_0_item)

        else:
            instrumentplatformpair_set = self.instrumentplatformpair_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "uuid": uuid,
                "short_code": short_code,
                "title": title,
                "abstract": abstract,
                "imageDetails": image_details,
                "mobilePlatformOperation": mobile_platform_operation,
                "instrumentplatformpair_set": instrumentplatformpair_set,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instrument_platform_pair_read import InstrumentPlatformPairRead
        from ..models.simple_read import SimpleRead

        d = dict(src_dict)

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_uuid(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        uuid = _parse_uuid(d.pop("uuid"))

        def _parse_short_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        short_code = _parse_short_code(d.pop("short_code"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))

        def _parse_abstract(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        abstract = _parse_abstract(d.pop("abstract"))

        image_details = []
        _image_details = d.pop("imageDetails")
        for image_details_item_data in _image_details:

            def _parse_image_details_item(data: object) -> int | None:
                if data is None:
                    return data
                return cast(int | None, data)

            image_details_item = _parse_image_details_item(image_details_item_data)

            image_details.append(image_details_item)

        def _parse_mobile_platform_operation(data: object) -> list[SimpleRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mobile_platform_operation_type_0 = []
                _mobile_platform_operation_type_0 = data
                for mobile_platform_operation_type_0_item_data in _mobile_platform_operation_type_0:
                    mobile_platform_operation_type_0_item = SimpleRead.from_dict(
                        mobile_platform_operation_type_0_item_data
                    )

                    mobile_platform_operation_type_0.append(mobile_platform_operation_type_0_item)

                return mobile_platform_operation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SimpleRead] | None, data)

        mobile_platform_operation = _parse_mobile_platform_operation(d.pop("mobilePlatformOperation"))

        def _parse_instrumentplatformpair_set(data: object) -> list[InstrumentPlatformPairRead] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                instrumentplatformpair_set_type_0 = []
                _instrumentplatformpair_set_type_0 = data
                for instrumentplatformpair_set_type_0_item_data in _instrumentplatformpair_set_type_0:
                    instrumentplatformpair_set_type_0_item = InstrumentPlatformPairRead.from_dict(
                        instrumentplatformpair_set_type_0_item_data
                    )

                    instrumentplatformpair_set_type_0.append(instrumentplatformpair_set_type_0_item)

                return instrumentplatformpair_set_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[InstrumentPlatformPairRead] | None, data)

        instrumentplatformpair_set = _parse_instrumentplatformpair_set(d.pop("instrumentplatformpair_set"))

        procedure_acquisition_read = cls(
            ob_id=ob_id,
            uuid=uuid,
            short_code=short_code,
            title=title,
            abstract=abstract,
            image_details=image_details,
            mobile_platform_operation=mobile_platform_operation,
            instrumentplatformpair_set=instrumentplatformpair_set,
        )

        procedure_acquisition_read.additional_properties = d
        return procedure_acquisition_read

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
