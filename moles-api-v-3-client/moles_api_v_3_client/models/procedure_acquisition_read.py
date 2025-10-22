from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
            ob_id (int):
            uuid (str):
            short_code (str):
            title (str):
            abstract (str):
            image_details (list[Union[None, int]]):
            mobile_platform_operation (Union[None, list['SimpleRead']]):
            instrumentplatformpair_set (Union[None, list['InstrumentPlatformPairRead']]):
    """

    ob_id: int
    uuid: str
    short_code: str
    title: str
    abstract: str
    image_details: list[Union[None, int]]
    mobile_platform_operation: Union[None, list["SimpleRead"]]
    instrumentplatformpair_set: Union[None, list["InstrumentPlatformPairRead"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        uuid = self.uuid

        short_code = self.short_code

        title = self.title

        abstract = self.abstract

        image_details = []
        for image_details_item_data in self.image_details:
            image_details_item: Union[None, int]
            image_details_item = image_details_item_data
            image_details.append(image_details_item)

        mobile_platform_operation: Union[None, list[dict[str, Any]]]
        if isinstance(self.mobile_platform_operation, list):
            mobile_platform_operation = []
            for mobile_platform_operation_type_0_item_data in self.mobile_platform_operation:
                mobile_platform_operation_type_0_item = mobile_platform_operation_type_0_item_data.to_dict()
                mobile_platform_operation.append(mobile_platform_operation_type_0_item)

        else:
            mobile_platform_operation = self.mobile_platform_operation

        instrumentplatformpair_set: Union[None, list[dict[str, Any]]]
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
        ob_id = d.pop("ob_id")

        uuid = d.pop("uuid")

        short_code = d.pop("short_code")

        title = d.pop("title")

        abstract = d.pop("abstract")

        image_details = []
        _image_details = d.pop("imageDetails")
        for image_details_item_data in _image_details:

            def _parse_image_details_item(data: object) -> Union[None, int]:
                if data is None:
                    return data
                return cast(Union[None, int], data)

            image_details_item = _parse_image_details_item(image_details_item_data)

            image_details.append(image_details_item)

        def _parse_mobile_platform_operation(data: object) -> Union[None, list["SimpleRead"]]:
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
            except:  # noqa: E722
                pass
            return cast(Union[None, list["SimpleRead"]], data)

        mobile_platform_operation = _parse_mobile_platform_operation(d.pop("mobilePlatformOperation"))

        def _parse_instrumentplatformpair_set(data: object) -> Union[None, list["InstrumentPlatformPairRead"]]:
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
            except:  # noqa: E722
                pass
            return cast(Union[None, list["InstrumentPlatformPairRead"]], data)

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
