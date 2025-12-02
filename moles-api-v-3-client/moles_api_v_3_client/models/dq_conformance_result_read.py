from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DQConformanceResultRead")


@_attrs_define
class DQConformanceResultRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            explanation (None | str):
            passes_test (bool | None):
            result_title (None | str):
            date (datetime.date | None):
    """

    ob_id: int | None
    explanation: None | str
    passes_test: bool | None
    result_title: None | str
    date: datetime.date | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ob_id: int | None
        ob_id = self.ob_id

        explanation: None | str
        explanation = self.explanation

        passes_test: bool | None
        passes_test = self.passes_test

        result_title: None | str
        result_title = self.result_title

        date: None | str
        if isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

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

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_explanation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        explanation = _parse_explanation(d.pop("explanation"))

        def _parse_passes_test(data: object) -> bool | None:
            if data is None:
                return data
            return cast(bool | None, data)

        passes_test = _parse_passes_test(d.pop("passesTest"))

        def _parse_result_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        result_title = _parse_result_title(d.pop("resultTitle"))

        def _parse_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data).date()

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        date = _parse_date(d.pop("date"))

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
