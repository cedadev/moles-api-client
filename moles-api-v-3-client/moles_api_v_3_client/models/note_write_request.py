from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NoteWriteRequest")


@_attrs_define
class NoteWriteRequest:
    """A mixin that allows specifying which fields to include in the serializer
    via the 'fields' keyword argument.

        Attributes:
            comments (str):
            related_record (str):
            commentator (int | None | Unset):
            date (datetime.datetime | None | Unset):
    """

    comments: str
    related_record: str
    commentator: int | None | Unset = UNSET
    date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        related_record = self.related_record

        commentator: int | None | Unset
        if isinstance(self.commentator, Unset):
            commentator = UNSET
        else:
            commentator = self.commentator

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comments": comments,
                "relatedRecord": related_record,
            }
        )
        if commentator is not UNSET:
            field_dict["commentator"] = commentator
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments")

        related_record = d.pop("relatedRecord")

        def _parse_commentator(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        commentator = _parse_commentator(d.pop("commentator", UNSET))

        def _parse_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        note_write_request = cls(
            comments=comments,
            related_record=related_record,
            commentator=commentator,
            date=date,
        )

        note_write_request.additional_properties = d
        return note_write_request

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
