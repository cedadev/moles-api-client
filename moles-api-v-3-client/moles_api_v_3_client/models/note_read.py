from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.referenceable import Referenceable


T = TypeVar("T", bound="NoteRead")


@_attrs_define
class NoteRead:
    """A mixin that adds 'simple_fields' as ReadOnlyFields
    and reorders them to the top.

        Attributes:
            ob_id (int | None):
            comments (None | str):
            date (datetime.datetime | None):
            commentator (int | None):
            related_record (None | Referenceable):
    """

    ob_id: int | None
    comments: None | str
    date: datetime.datetime | None
    commentator: int | None
    related_record: None | Referenceable
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.referenceable import Referenceable

        ob_id: int | None
        ob_id = self.ob_id

        comments: None | str
        comments = self.comments

        date: None | str
        if isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        commentator: int | None
        commentator = self.commentator

        related_record: dict[str, Any] | None
        if isinstance(self.related_record, Referenceable):
            related_record = self.related_record.to_dict()
        else:
            related_record = self.related_record

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ob_id": ob_id,
                "comments": comments,
                "date": date,
                "commentator": commentator,
                "relatedRecord": related_record,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referenceable import Referenceable

        d = dict(src_dict)

        def _parse_ob_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ob_id = _parse_ob_id(d.pop("ob_id"))

        def _parse_comments(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        comments = _parse_comments(d.pop("comments"))

        def _parse_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        date = _parse_date(d.pop("date"))

        def _parse_commentator(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        commentator = _parse_commentator(d.pop("commentator"))

        def _parse_related_record(data: object) -> None | Referenceable:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                related_record_type_1 = Referenceable.from_dict(data)

                return related_record_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Referenceable, data)

        related_record = _parse_related_record(d.pop("relatedRecord"))

        note_read = cls(
            ob_id=ob_id,
            comments=comments,
            date=date,
            commentator=commentator,
            related_record=related_record,
        )

        note_read.additional_properties = d
        return note_read

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
