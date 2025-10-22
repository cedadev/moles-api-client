from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.simple_read import SimpleRead


T = TypeVar("T", bound="InstrumentPlatformPairRead")


@_attrs_define
class InstrumentPlatformPairRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            platform (Union['SimpleRead', None]):
            instrument (Union['SimpleRead', None]):
            related_to (Union['SimpleRead', None]):
    """

    ob_id: int
    platform: Union["SimpleRead", None]
    instrument: Union["SimpleRead", None]
    related_to: Union["SimpleRead", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_read import SimpleRead

        ob_id = self.ob_id

        platform: Union[None, dict[str, Any]]
        if isinstance(self.platform, SimpleRead):
            platform = self.platform.to_dict()
        else:
            platform = self.platform

        instrument: Union[None, dict[str, Any]]
        if isinstance(self.instrument, SimpleRead):
            instrument = self.instrument.to_dict()
        else:
            instrument = self.instrument

        related_to: Union[None, dict[str, Any]]
        if isinstance(self.related_to, SimpleRead):
            related_to = self.related_to.to_dict()
        else:
            related_to = self.related_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "platform": platform,
                "instrument": instrument,
                "relatedTo": related_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_read import SimpleRead

        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        def _parse_platform(data: object) -> Union["SimpleRead", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_type_1 = SimpleRead.from_dict(data)

                return platform_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SimpleRead", None], data)

        platform = _parse_platform(d.pop("platform"))

        def _parse_instrument(data: object) -> Union["SimpleRead", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                instrument_type_1 = SimpleRead.from_dict(data)

                return instrument_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SimpleRead", None], data)

        instrument = _parse_instrument(d.pop("instrument"))

        def _parse_related_to(data: object) -> Union["SimpleRead", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                related_to_type_1 = SimpleRead.from_dict(data)

                return related_to_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SimpleRead", None], data)

        related_to = _parse_related_to(d.pop("relatedTo"))

        instrument_platform_pair_read = cls(
            ob_id=ob_id,
            platform=platform,
            instrument=instrument,
            related_to=related_to,
        )

        instrument_platform_pair_read.additional_properties = d
        return instrument_platform_pair_read

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
