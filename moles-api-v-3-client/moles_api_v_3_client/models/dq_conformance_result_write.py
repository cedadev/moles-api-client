from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DQConformanceResultWrite")


@_attrs_define
class DQConformanceResultWrite:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            ob_id (int):
            explanation (str):
            passes_test (bool | Unset):
            result_title (str | Unset):
            date (datetime.date | Unset):
    """

    ob_id: int
    explanation: str
    passes_test: bool | Unset = UNSET
    result_title: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id = self.ob_id

        explanation = self.explanation

        passes_test = self.passes_test

        result_title = self.result_title

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "explanation": explanation,
            }
        )
        if passes_test is not UNSET:
            field_dict["passesTest"] = passes_test
        if result_title is not UNSET:
            field_dict["resultTitle"] = result_title
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ob_id = d.pop("ob_id")

        explanation = d.pop("explanation")

        passes_test = d.pop("passesTest", UNSET)

        result_title = d.pop("resultTitle", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        dq_conformance_result_write = cls(
            ob_id=ob_id,
            explanation=explanation,
            passes_test=passes_test,
            result_title=result_title,
            date=date,
        )

        dq_conformance_result_write.additional_properties = d
        return dq_conformance_result_write

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
