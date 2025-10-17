import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DQConformanceResultRead")


@_attrs_define
class DQConformanceResultRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int):
            explanation (str):
            passes_test (bool):
            result_title (str):
            date (datetime.date):
    """

    ob_id: int
    explanation: str
    passes_test: bool
    result_title: str
    date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        explanation = self.explanation

        passes_test = self.passes_test

        result_title = self.result_title

        date = self.date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "explanation": explanation,
                "passesTest": passes_test,
                "resultTitle": result_title,
                "date": date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        explanation = d.pop("explanation")

        passes_test = d.pop("passesTest")

        result_title = d.pop("resultTitle")

        date = isoparse(d.pop("date")).date()

        dq_conformance_result_read = cls(
            ob_id=ob_id,
            explanation=explanation,
            passes_test=passes_test,
            result_title=result_title,
            date=date,
        )

        dq_conformance_result_read.additional_properties = d
        return dq_conformance_result_read

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
