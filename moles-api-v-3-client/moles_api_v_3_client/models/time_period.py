import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimePeriod")


@_attrs_define
class TimePeriod:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            start_time (datetime.datetime):
            end_time (Union[None, Unset, datetime.datetime]):
    """

    ob_id: int
    start_time: datetime.datetime
    end_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        start_time = self.start_time.isoformat()

        end_time: Union[None, Unset, str]
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "startTime": start_time,
            }
        )
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("ob_id", (None, str(self.ob_id).encode(), "text/plain")))

        files.append(("startTime", (None, self.start_time.isoformat().encode(), "text/plain")))

        if not isinstance(self.end_time, Unset):
            if isinstance(self.end_time, datetime.datetime):
                files.append(("endTime", (None, self.end_time.isoformat().encode(), "text/plain")))
            else:
                files.append(("endTime", (None, str(self.end_time).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        start_time = isoparse(d.pop("startTime"))

        def _parse_end_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_time = _parse_end_time(d.pop("endTime", UNSET))

        time_period = cls(
            ob_id=ob_id,
            start_time=start_time,
            end_time=end_time,
        )

        time_period.additional_properties = d
        return time_period

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
