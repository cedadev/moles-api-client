from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.instruments_list_instrument_type import InstrumentsListInstrumentType
from ...models.paginated_instrument_read_list import PaginatedInstrumentReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    instrument_type: InstrumentsListInstrumentType | Unset = UNSET,
    instrument_type_contains: str | Unset = UNSET,
    instrument_type_endswith: str | Unset = UNSET,
    instrument_type_gt: str | Unset = UNSET,
    instrument_type_gte: str | Unset = UNSET,
    instrument_type_icontains: str | Unset = UNSET,
    instrument_type_iendswith: str | Unset = UNSET,
    instrument_type_iexact: str | Unset = UNSET,
    instrument_type_in: list[str] | Unset = UNSET,
    instrument_type_iregex: str | Unset = UNSET,
    instrument_type_isnull: bool | Unset = UNSET,
    instrument_type_istartswith: str | Unset = UNSET,
    instrument_type_lt: str | Unset = UNSET,
    instrument_type_lte: str | Unset = UNSET,
    instrument_type_range: list[str] | Unset = UNSET,
    instrument_type_regex: str | Unset = UNSET,
    instrument_type_startswith: str | Unset = UNSET,
    keywords: str | Unset = UNSET,
    keywords_contains: str | Unset = UNSET,
    keywords_endswith: str | Unset = UNSET,
    keywords_gt: str | Unset = UNSET,
    keywords_gte: str | Unset = UNSET,
    keywords_icontains: str | Unset = UNSET,
    keywords_iendswith: str | Unset = UNSET,
    keywords_iexact: str | Unset = UNSET,
    keywords_in: list[str] | Unset = UNSET,
    keywords_iregex: str | Unset = UNSET,
    keywords_isnull: bool | Unset = UNSET,
    keywords_istartswith: str | Unset = UNSET,
    keywords_lt: str | Unset = UNSET,
    keywords_lte: str | Unset = UNSET,
    keywords_range: list[str] | Unset = UNSET,
    keywords_regex: str | Unset = UNSET,
    keywords_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ob_id: int | Unset = UNSET,
    ob_id_contained_by: int | Unset = UNSET,
    ob_id_contains: int | Unset = UNSET,
    ob_id_endswith: int | Unset = UNSET,
    ob_id_gt: int | Unset = UNSET,
    ob_id_gte: int | Unset = UNSET,
    ob_id_icontains: int | Unset = UNSET,
    ob_id_iendswith: int | Unset = UNSET,
    ob_id_iexact: int | Unset = UNSET,
    ob_id_in: list[int] | Unset = UNSET,
    ob_id_iregex: int | Unset = UNSET,
    ob_id_isnull: bool | Unset = UNSET,
    ob_id_istartswith: int | Unset = UNSET,
    ob_id_lt: int | Unset = UNSET,
    ob_id_lte: int | Unset = UNSET,
    ob_id_range: list[int] | Unset = UNSET,
    ob_id_regex: int | Unset = UNSET,
    ob_id_startswith: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_gt: int | Unset = UNSET,
    referenceable_ptr_gte: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    referenceable_ptr_lt: int | Unset = UNSET,
    referenceable_ptr_lte: int | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["abstract"] = abstract

    params["abstract__contains"] = abstract_contains

    params["abstract__endswith"] = abstract_endswith

    params["abstract__gt"] = abstract_gt

    params["abstract__gte"] = abstract_gte

    params["abstract__icontains"] = abstract_icontains

    params["abstract__iendswith"] = abstract_iendswith

    params["abstract__iexact"] = abstract_iexact

    json_abstract_in: list[str] | Unset = UNSET
    if not isinstance(abstract_in, Unset):
        json_abstract_in = ",".join(map(str, abstract_in))

    params["abstract__in"] = json_abstract_in

    params["abstract__iregex"] = abstract_iregex

    params["abstract__isnull"] = abstract_isnull

    params["abstract__istartswith"] = abstract_istartswith

    params["abstract__lt"] = abstract_lt

    params["abstract__lte"] = abstract_lte

    json_abstract_range: list[str] | Unset = UNSET
    if not isinstance(abstract_range, Unset):
        json_abstract_range = ",".join(map(str, abstract_range))

    params["abstract__range"] = json_abstract_range

    params["abstract__regex"] = abstract_regex

    params["abstract__startswith"] = abstract_startswith

    json_instrument_type: str | Unset = UNSET
    if not isinstance(instrument_type, Unset):
        json_instrument_type = instrument_type.value

    params["instrumentType"] = json_instrument_type

    params["instrumentType__contains"] = instrument_type_contains

    params["instrumentType__endswith"] = instrument_type_endswith

    params["instrumentType__gt"] = instrument_type_gt

    params["instrumentType__gte"] = instrument_type_gte

    params["instrumentType__icontains"] = instrument_type_icontains

    params["instrumentType__iendswith"] = instrument_type_iendswith

    params["instrumentType__iexact"] = instrument_type_iexact

    json_instrument_type_in: list[str] | Unset = UNSET
    if not isinstance(instrument_type_in, Unset):
        json_instrument_type_in = ",".join(map(str, instrument_type_in))

    params["instrumentType__in"] = json_instrument_type_in

    params["instrumentType__iregex"] = instrument_type_iregex

    params["instrumentType__isnull"] = instrument_type_isnull

    params["instrumentType__istartswith"] = instrument_type_istartswith

    params["instrumentType__lt"] = instrument_type_lt

    params["instrumentType__lte"] = instrument_type_lte

    json_instrument_type_range: list[str] | Unset = UNSET
    if not isinstance(instrument_type_range, Unset):
        json_instrument_type_range = ",".join(map(str, instrument_type_range))

    params["instrumentType__range"] = json_instrument_type_range

    params["instrumentType__regex"] = instrument_type_regex

    params["instrumentType__startswith"] = instrument_type_startswith

    params["keywords"] = keywords

    params["keywords__contains"] = keywords_contains

    params["keywords__endswith"] = keywords_endswith

    params["keywords__gt"] = keywords_gt

    params["keywords__gte"] = keywords_gte

    params["keywords__icontains"] = keywords_icontains

    params["keywords__iendswith"] = keywords_iendswith

    params["keywords__iexact"] = keywords_iexact

    json_keywords_in: list[str] | Unset = UNSET
    if not isinstance(keywords_in, Unset):
        json_keywords_in = ",".join(map(str, keywords_in))

    params["keywords__in"] = json_keywords_in

    params["keywords__iregex"] = keywords_iregex

    params["keywords__isnull"] = keywords_isnull

    params["keywords__istartswith"] = keywords_istartswith

    params["keywords__lt"] = keywords_lt

    params["keywords__lte"] = keywords_lte

    json_keywords_range: list[str] | Unset = UNSET
    if not isinstance(keywords_range, Unset):
        json_keywords_range = ",".join(map(str, keywords_range))

    params["keywords__range"] = json_keywords_range

    params["keywords__regex"] = keywords_regex

    params["keywords__startswith"] = keywords_startswith

    params["limit"] = limit

    params["ob_id"] = ob_id

    params["ob_id__contained_by"] = ob_id_contained_by

    params["ob_id__contains"] = ob_id_contains

    params["ob_id__endswith"] = ob_id_endswith

    params["ob_id__gt"] = ob_id_gt

    params["ob_id__gte"] = ob_id_gte

    params["ob_id__icontains"] = ob_id_icontains

    params["ob_id__iendswith"] = ob_id_iendswith

    params["ob_id__iexact"] = ob_id_iexact

    json_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(ob_id_in, Unset):
        json_ob_id_in = ",".join(map(str, ob_id_in))

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: list[int] | Unset = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ",".join(map(str, ob_id_range))

    params["ob_id__range"] = json_ob_id_range

    params["ob_id__regex"] = ob_id_regex

    params["ob_id__startswith"] = ob_id_startswith

    params["offset"] = offset

    params["ordering"] = ordering

    params["referenceable_ptr"] = referenceable_ptr

    params["referenceable_ptr__gt"] = referenceable_ptr_gt

    params["referenceable_ptr__gte"] = referenceable_ptr_gte

    json_referenceable_ptr_in: list[int] | Unset = UNSET
    if not isinstance(referenceable_ptr_in, Unset):
        json_referenceable_ptr_in = ",".join(map(str, referenceable_ptr_in))

    params["referenceable_ptr__in"] = json_referenceable_ptr_in

    params["referenceable_ptr__isnull"] = referenceable_ptr_isnull

    params["referenceable_ptr__lt"] = referenceable_ptr_lt

    params["referenceable_ptr__lte"] = referenceable_ptr_lte

    params["short_code"] = short_code

    params["short_code__contains"] = short_code_contains

    params["short_code__endswith"] = short_code_endswith

    params["short_code__gt"] = short_code_gt

    params["short_code__gte"] = short_code_gte

    params["short_code__icontains"] = short_code_icontains

    params["short_code__iendswith"] = short_code_iendswith

    params["short_code__iexact"] = short_code_iexact

    json_short_code_in: list[str] | Unset = UNSET
    if not isinstance(short_code_in, Unset):
        json_short_code_in = ",".join(map(str, short_code_in))

    params["short_code__in"] = json_short_code_in

    params["short_code__iregex"] = short_code_iregex

    params["short_code__isnull"] = short_code_isnull

    params["short_code__istartswith"] = short_code_istartswith

    params["short_code__lt"] = short_code_lt

    params["short_code__lte"] = short_code_lte

    json_short_code_range: list[str] | Unset = UNSET
    if not isinstance(short_code_range, Unset):
        json_short_code_range = ",".join(map(str, short_code_range))

    params["short_code__range"] = json_short_code_range

    params["short_code__regex"] = short_code_regex

    params["short_code__startswith"] = short_code_startswith

    params["title"] = title

    params["title__contains"] = title_contains

    params["title__endswith"] = title_endswith

    params["title__gt"] = title_gt

    params["title__gte"] = title_gte

    params["title__icontains"] = title_icontains

    params["title__iendswith"] = title_iendswith

    params["title__iexact"] = title_iexact

    json_title_in: list[str] | Unset = UNSET
    if not isinstance(title_in, Unset):
        json_title_in = ",".join(map(str, title_in))

    params["title__in"] = json_title_in

    params["title__iregex"] = title_iregex

    params["title__isnull"] = title_isnull

    params["title__istartswith"] = title_istartswith

    params["title__lt"] = title_lt

    params["title__lte"] = title_lte

    json_title_range: list[str] | Unset = UNSET
    if not isinstance(title_range, Unset):
        json_title_range = ",".join(map(str, title_range))

    params["title__range"] = json_title_range

    params["title__regex"] = title_regex

    params["title__startswith"] = title_startswith

    params["uuid"] = uuid

    params["uuid__contains"] = uuid_contains

    params["uuid__endswith"] = uuid_endswith

    params["uuid__gt"] = uuid_gt

    params["uuid__gte"] = uuid_gte

    params["uuid__icontains"] = uuid_icontains

    params["uuid__iendswith"] = uuid_iendswith

    params["uuid__iexact"] = uuid_iexact

    json_uuid_in: list[str] | Unset = UNSET
    if not isinstance(uuid_in, Unset):
        json_uuid_in = ",".join(map(str, uuid_in))

    params["uuid__in"] = json_uuid_in

    params["uuid__iregex"] = uuid_iregex

    params["uuid__isnull"] = uuid_isnull

    params["uuid__istartswith"] = uuid_istartswith

    params["uuid__lt"] = uuid_lt

    params["uuid__lte"] = uuid_lte

    json_uuid_range: list[str] | Unset = UNSET
    if not isinstance(uuid_range, Unset):
        json_uuid_range = ",".join(map(str, uuid_range))

    params["uuid__range"] = json_uuid_range

    params["uuid__regex"] = uuid_regex

    params["uuid__startswith"] = uuid_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/instruments/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedInstrumentReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedInstrumentReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedInstrumentReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    instrument_type: InstrumentsListInstrumentType | Unset = UNSET,
    instrument_type_contains: str | Unset = UNSET,
    instrument_type_endswith: str | Unset = UNSET,
    instrument_type_gt: str | Unset = UNSET,
    instrument_type_gte: str | Unset = UNSET,
    instrument_type_icontains: str | Unset = UNSET,
    instrument_type_iendswith: str | Unset = UNSET,
    instrument_type_iexact: str | Unset = UNSET,
    instrument_type_in: list[str] | Unset = UNSET,
    instrument_type_iregex: str | Unset = UNSET,
    instrument_type_isnull: bool | Unset = UNSET,
    instrument_type_istartswith: str | Unset = UNSET,
    instrument_type_lt: str | Unset = UNSET,
    instrument_type_lte: str | Unset = UNSET,
    instrument_type_range: list[str] | Unset = UNSET,
    instrument_type_regex: str | Unset = UNSET,
    instrument_type_startswith: str | Unset = UNSET,
    keywords: str | Unset = UNSET,
    keywords_contains: str | Unset = UNSET,
    keywords_endswith: str | Unset = UNSET,
    keywords_gt: str | Unset = UNSET,
    keywords_gte: str | Unset = UNSET,
    keywords_icontains: str | Unset = UNSET,
    keywords_iendswith: str | Unset = UNSET,
    keywords_iexact: str | Unset = UNSET,
    keywords_in: list[str] | Unset = UNSET,
    keywords_iregex: str | Unset = UNSET,
    keywords_isnull: bool | Unset = UNSET,
    keywords_istartswith: str | Unset = UNSET,
    keywords_lt: str | Unset = UNSET,
    keywords_lte: str | Unset = UNSET,
    keywords_range: list[str] | Unset = UNSET,
    keywords_regex: str | Unset = UNSET,
    keywords_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ob_id: int | Unset = UNSET,
    ob_id_contained_by: int | Unset = UNSET,
    ob_id_contains: int | Unset = UNSET,
    ob_id_endswith: int | Unset = UNSET,
    ob_id_gt: int | Unset = UNSET,
    ob_id_gte: int | Unset = UNSET,
    ob_id_icontains: int | Unset = UNSET,
    ob_id_iendswith: int | Unset = UNSET,
    ob_id_iexact: int | Unset = UNSET,
    ob_id_in: list[int] | Unset = UNSET,
    ob_id_iregex: int | Unset = UNSET,
    ob_id_isnull: bool | Unset = UNSET,
    ob_id_istartswith: int | Unset = UNSET,
    ob_id_lt: int | Unset = UNSET,
    ob_id_lte: int | Unset = UNSET,
    ob_id_range: list[int] | Unset = UNSET,
    ob_id_regex: int | Unset = UNSET,
    ob_id_startswith: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_gt: int | Unset = UNSET,
    referenceable_ptr_gte: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    referenceable_ptr_lt: int | Unset = UNSET,
    referenceable_ptr_lte: int | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> Response[PaginatedInstrumentReadList]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        instrument_type (InstrumentsListInstrumentType | Unset):
        instrument_type_contains (str | Unset):
        instrument_type_endswith (str | Unset):
        instrument_type_gt (str | Unset):
        instrument_type_gte (str | Unset):
        instrument_type_icontains (str | Unset):
        instrument_type_iendswith (str | Unset):
        instrument_type_iexact (str | Unset):
        instrument_type_in (list[str] | Unset):
        instrument_type_iregex (str | Unset):
        instrument_type_isnull (bool | Unset):
        instrument_type_istartswith (str | Unset):
        instrument_type_lt (str | Unset):
        instrument_type_lte (str | Unset):
        instrument_type_range (list[str] | Unset):
        instrument_type_regex (str | Unset):
        instrument_type_startswith (str | Unset):
        keywords (str | Unset):
        keywords_contains (str | Unset):
        keywords_endswith (str | Unset):
        keywords_gt (str | Unset):
        keywords_gte (str | Unset):
        keywords_icontains (str | Unset):
        keywords_iendswith (str | Unset):
        keywords_iexact (str | Unset):
        keywords_in (list[str] | Unset):
        keywords_iregex (str | Unset):
        keywords_isnull (bool | Unset):
        keywords_istartswith (str | Unset):
        keywords_lt (str | Unset):
        keywords_lte (str | Unset):
        keywords_range (list[str] | Unset):
        keywords_regex (str | Unset):
        keywords_startswith (str | Unset):
        limit (int | Unset):
        ob_id (int | Unset):
        ob_id_contained_by (int | Unset):
        ob_id_contains (int | Unset):
        ob_id_endswith (int | Unset):
        ob_id_gt (int | Unset):
        ob_id_gte (int | Unset):
        ob_id_icontains (int | Unset):
        ob_id_iendswith (int | Unset):
        ob_id_iexact (int | Unset):
        ob_id_in (list[int] | Unset):
        ob_id_iregex (int | Unset):
        ob_id_isnull (bool | Unset):
        ob_id_istartswith (int | Unset):
        ob_id_lt (int | Unset):
        ob_id_lte (int | Unset):
        ob_id_range (list[int] | Unset):
        ob_id_regex (int | Unset):
        ob_id_startswith (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_gt (int | Unset):
        referenceable_ptr_gte (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        referenceable_ptr_lt (int | Unset):
        referenceable_ptr_lte (int | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedInstrumentReadList]
    """

    kwargs = _get_kwargs(
        abstract=abstract,
        abstract_contains=abstract_contains,
        abstract_endswith=abstract_endswith,
        abstract_gt=abstract_gt,
        abstract_gte=abstract_gte,
        abstract_icontains=abstract_icontains,
        abstract_iendswith=abstract_iendswith,
        abstract_iexact=abstract_iexact,
        abstract_in=abstract_in,
        abstract_iregex=abstract_iregex,
        abstract_isnull=abstract_isnull,
        abstract_istartswith=abstract_istartswith,
        abstract_lt=abstract_lt,
        abstract_lte=abstract_lte,
        abstract_range=abstract_range,
        abstract_regex=abstract_regex,
        abstract_startswith=abstract_startswith,
        instrument_type=instrument_type,
        instrument_type_contains=instrument_type_contains,
        instrument_type_endswith=instrument_type_endswith,
        instrument_type_gt=instrument_type_gt,
        instrument_type_gte=instrument_type_gte,
        instrument_type_icontains=instrument_type_icontains,
        instrument_type_iendswith=instrument_type_iendswith,
        instrument_type_iexact=instrument_type_iexact,
        instrument_type_in=instrument_type_in,
        instrument_type_iregex=instrument_type_iregex,
        instrument_type_isnull=instrument_type_isnull,
        instrument_type_istartswith=instrument_type_istartswith,
        instrument_type_lt=instrument_type_lt,
        instrument_type_lte=instrument_type_lte,
        instrument_type_range=instrument_type_range,
        instrument_type_regex=instrument_type_regex,
        instrument_type_startswith=instrument_type_startswith,
        keywords=keywords,
        keywords_contains=keywords_contains,
        keywords_endswith=keywords_endswith,
        keywords_gt=keywords_gt,
        keywords_gte=keywords_gte,
        keywords_icontains=keywords_icontains,
        keywords_iendswith=keywords_iendswith,
        keywords_iexact=keywords_iexact,
        keywords_in=keywords_in,
        keywords_iregex=keywords_iregex,
        keywords_isnull=keywords_isnull,
        keywords_istartswith=keywords_istartswith,
        keywords_lt=keywords_lt,
        keywords_lte=keywords_lte,
        keywords_range=keywords_range,
        keywords_regex=keywords_regex,
        keywords_startswith=keywords_startswith,
        limit=limit,
        ob_id=ob_id,
        ob_id_contained_by=ob_id_contained_by,
        ob_id_contains=ob_id_contains,
        ob_id_endswith=ob_id_endswith,
        ob_id_gt=ob_id_gt,
        ob_id_gte=ob_id_gte,
        ob_id_icontains=ob_id_icontains,
        ob_id_iendswith=ob_id_iendswith,
        ob_id_iexact=ob_id_iexact,
        ob_id_in=ob_id_in,
        ob_id_iregex=ob_id_iregex,
        ob_id_isnull=ob_id_isnull,
        ob_id_istartswith=ob_id_istartswith,
        ob_id_lt=ob_id_lt,
        ob_id_lte=ob_id_lte,
        ob_id_range=ob_id_range,
        ob_id_regex=ob_id_regex,
        ob_id_startswith=ob_id_startswith,
        offset=offset,
        ordering=ordering,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_gt=referenceable_ptr_gt,
        referenceable_ptr_gte=referenceable_ptr_gte,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        referenceable_ptr_lt=referenceable_ptr_lt,
        referenceable_ptr_lte=referenceable_ptr_lte,
        short_code=short_code,
        short_code_contains=short_code_contains,
        short_code_endswith=short_code_endswith,
        short_code_gt=short_code_gt,
        short_code_gte=short_code_gte,
        short_code_icontains=short_code_icontains,
        short_code_iendswith=short_code_iendswith,
        short_code_iexact=short_code_iexact,
        short_code_in=short_code_in,
        short_code_iregex=short_code_iregex,
        short_code_isnull=short_code_isnull,
        short_code_istartswith=short_code_istartswith,
        short_code_lt=short_code_lt,
        short_code_lte=short_code_lte,
        short_code_range=short_code_range,
        short_code_regex=short_code_regex,
        short_code_startswith=short_code_startswith,
        title=title,
        title_contains=title_contains,
        title_endswith=title_endswith,
        title_gt=title_gt,
        title_gte=title_gte,
        title_icontains=title_icontains,
        title_iendswith=title_iendswith,
        title_iexact=title_iexact,
        title_in=title_in,
        title_iregex=title_iregex,
        title_isnull=title_isnull,
        title_istartswith=title_istartswith,
        title_lt=title_lt,
        title_lte=title_lte,
        title_range=title_range,
        title_regex=title_regex,
        title_startswith=title_startswith,
        uuid=uuid,
        uuid_contains=uuid_contains,
        uuid_endswith=uuid_endswith,
        uuid_gt=uuid_gt,
        uuid_gte=uuid_gte,
        uuid_icontains=uuid_icontains,
        uuid_iendswith=uuid_iendswith,
        uuid_iexact=uuid_iexact,
        uuid_in=uuid_in,
        uuid_iregex=uuid_iregex,
        uuid_isnull=uuid_isnull,
        uuid_istartswith=uuid_istartswith,
        uuid_lt=uuid_lt,
        uuid_lte=uuid_lte,
        uuid_range=uuid_range,
        uuid_regex=uuid_regex,
        uuid_startswith=uuid_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    instrument_type: InstrumentsListInstrumentType | Unset = UNSET,
    instrument_type_contains: str | Unset = UNSET,
    instrument_type_endswith: str | Unset = UNSET,
    instrument_type_gt: str | Unset = UNSET,
    instrument_type_gte: str | Unset = UNSET,
    instrument_type_icontains: str | Unset = UNSET,
    instrument_type_iendswith: str | Unset = UNSET,
    instrument_type_iexact: str | Unset = UNSET,
    instrument_type_in: list[str] | Unset = UNSET,
    instrument_type_iregex: str | Unset = UNSET,
    instrument_type_isnull: bool | Unset = UNSET,
    instrument_type_istartswith: str | Unset = UNSET,
    instrument_type_lt: str | Unset = UNSET,
    instrument_type_lte: str | Unset = UNSET,
    instrument_type_range: list[str] | Unset = UNSET,
    instrument_type_regex: str | Unset = UNSET,
    instrument_type_startswith: str | Unset = UNSET,
    keywords: str | Unset = UNSET,
    keywords_contains: str | Unset = UNSET,
    keywords_endswith: str | Unset = UNSET,
    keywords_gt: str | Unset = UNSET,
    keywords_gte: str | Unset = UNSET,
    keywords_icontains: str | Unset = UNSET,
    keywords_iendswith: str | Unset = UNSET,
    keywords_iexact: str | Unset = UNSET,
    keywords_in: list[str] | Unset = UNSET,
    keywords_iregex: str | Unset = UNSET,
    keywords_isnull: bool | Unset = UNSET,
    keywords_istartswith: str | Unset = UNSET,
    keywords_lt: str | Unset = UNSET,
    keywords_lte: str | Unset = UNSET,
    keywords_range: list[str] | Unset = UNSET,
    keywords_regex: str | Unset = UNSET,
    keywords_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ob_id: int | Unset = UNSET,
    ob_id_contained_by: int | Unset = UNSET,
    ob_id_contains: int | Unset = UNSET,
    ob_id_endswith: int | Unset = UNSET,
    ob_id_gt: int | Unset = UNSET,
    ob_id_gte: int | Unset = UNSET,
    ob_id_icontains: int | Unset = UNSET,
    ob_id_iendswith: int | Unset = UNSET,
    ob_id_iexact: int | Unset = UNSET,
    ob_id_in: list[int] | Unset = UNSET,
    ob_id_iregex: int | Unset = UNSET,
    ob_id_isnull: bool | Unset = UNSET,
    ob_id_istartswith: int | Unset = UNSET,
    ob_id_lt: int | Unset = UNSET,
    ob_id_lte: int | Unset = UNSET,
    ob_id_range: list[int] | Unset = UNSET,
    ob_id_regex: int | Unset = UNSET,
    ob_id_startswith: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_gt: int | Unset = UNSET,
    referenceable_ptr_gte: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    referenceable_ptr_lt: int | Unset = UNSET,
    referenceable_ptr_lte: int | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> PaginatedInstrumentReadList | None:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        instrument_type (InstrumentsListInstrumentType | Unset):
        instrument_type_contains (str | Unset):
        instrument_type_endswith (str | Unset):
        instrument_type_gt (str | Unset):
        instrument_type_gte (str | Unset):
        instrument_type_icontains (str | Unset):
        instrument_type_iendswith (str | Unset):
        instrument_type_iexact (str | Unset):
        instrument_type_in (list[str] | Unset):
        instrument_type_iregex (str | Unset):
        instrument_type_isnull (bool | Unset):
        instrument_type_istartswith (str | Unset):
        instrument_type_lt (str | Unset):
        instrument_type_lte (str | Unset):
        instrument_type_range (list[str] | Unset):
        instrument_type_regex (str | Unset):
        instrument_type_startswith (str | Unset):
        keywords (str | Unset):
        keywords_contains (str | Unset):
        keywords_endswith (str | Unset):
        keywords_gt (str | Unset):
        keywords_gte (str | Unset):
        keywords_icontains (str | Unset):
        keywords_iendswith (str | Unset):
        keywords_iexact (str | Unset):
        keywords_in (list[str] | Unset):
        keywords_iregex (str | Unset):
        keywords_isnull (bool | Unset):
        keywords_istartswith (str | Unset):
        keywords_lt (str | Unset):
        keywords_lte (str | Unset):
        keywords_range (list[str] | Unset):
        keywords_regex (str | Unset):
        keywords_startswith (str | Unset):
        limit (int | Unset):
        ob_id (int | Unset):
        ob_id_contained_by (int | Unset):
        ob_id_contains (int | Unset):
        ob_id_endswith (int | Unset):
        ob_id_gt (int | Unset):
        ob_id_gte (int | Unset):
        ob_id_icontains (int | Unset):
        ob_id_iendswith (int | Unset):
        ob_id_iexact (int | Unset):
        ob_id_in (list[int] | Unset):
        ob_id_iregex (int | Unset):
        ob_id_isnull (bool | Unset):
        ob_id_istartswith (int | Unset):
        ob_id_lt (int | Unset):
        ob_id_lte (int | Unset):
        ob_id_range (list[int] | Unset):
        ob_id_regex (int | Unset):
        ob_id_startswith (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_gt (int | Unset):
        referenceable_ptr_gte (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        referenceable_ptr_lt (int | Unset):
        referenceable_ptr_lte (int | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedInstrumentReadList
    """

    return sync_detailed(
        client=client,
        abstract=abstract,
        abstract_contains=abstract_contains,
        abstract_endswith=abstract_endswith,
        abstract_gt=abstract_gt,
        abstract_gte=abstract_gte,
        abstract_icontains=abstract_icontains,
        abstract_iendswith=abstract_iendswith,
        abstract_iexact=abstract_iexact,
        abstract_in=abstract_in,
        abstract_iregex=abstract_iregex,
        abstract_isnull=abstract_isnull,
        abstract_istartswith=abstract_istartswith,
        abstract_lt=abstract_lt,
        abstract_lte=abstract_lte,
        abstract_range=abstract_range,
        abstract_regex=abstract_regex,
        abstract_startswith=abstract_startswith,
        instrument_type=instrument_type,
        instrument_type_contains=instrument_type_contains,
        instrument_type_endswith=instrument_type_endswith,
        instrument_type_gt=instrument_type_gt,
        instrument_type_gte=instrument_type_gte,
        instrument_type_icontains=instrument_type_icontains,
        instrument_type_iendswith=instrument_type_iendswith,
        instrument_type_iexact=instrument_type_iexact,
        instrument_type_in=instrument_type_in,
        instrument_type_iregex=instrument_type_iregex,
        instrument_type_isnull=instrument_type_isnull,
        instrument_type_istartswith=instrument_type_istartswith,
        instrument_type_lt=instrument_type_lt,
        instrument_type_lte=instrument_type_lte,
        instrument_type_range=instrument_type_range,
        instrument_type_regex=instrument_type_regex,
        instrument_type_startswith=instrument_type_startswith,
        keywords=keywords,
        keywords_contains=keywords_contains,
        keywords_endswith=keywords_endswith,
        keywords_gt=keywords_gt,
        keywords_gte=keywords_gte,
        keywords_icontains=keywords_icontains,
        keywords_iendswith=keywords_iendswith,
        keywords_iexact=keywords_iexact,
        keywords_in=keywords_in,
        keywords_iregex=keywords_iregex,
        keywords_isnull=keywords_isnull,
        keywords_istartswith=keywords_istartswith,
        keywords_lt=keywords_lt,
        keywords_lte=keywords_lte,
        keywords_range=keywords_range,
        keywords_regex=keywords_regex,
        keywords_startswith=keywords_startswith,
        limit=limit,
        ob_id=ob_id,
        ob_id_contained_by=ob_id_contained_by,
        ob_id_contains=ob_id_contains,
        ob_id_endswith=ob_id_endswith,
        ob_id_gt=ob_id_gt,
        ob_id_gte=ob_id_gte,
        ob_id_icontains=ob_id_icontains,
        ob_id_iendswith=ob_id_iendswith,
        ob_id_iexact=ob_id_iexact,
        ob_id_in=ob_id_in,
        ob_id_iregex=ob_id_iregex,
        ob_id_isnull=ob_id_isnull,
        ob_id_istartswith=ob_id_istartswith,
        ob_id_lt=ob_id_lt,
        ob_id_lte=ob_id_lte,
        ob_id_range=ob_id_range,
        ob_id_regex=ob_id_regex,
        ob_id_startswith=ob_id_startswith,
        offset=offset,
        ordering=ordering,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_gt=referenceable_ptr_gt,
        referenceable_ptr_gte=referenceable_ptr_gte,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        referenceable_ptr_lt=referenceable_ptr_lt,
        referenceable_ptr_lte=referenceable_ptr_lte,
        short_code=short_code,
        short_code_contains=short_code_contains,
        short_code_endswith=short_code_endswith,
        short_code_gt=short_code_gt,
        short_code_gte=short_code_gte,
        short_code_icontains=short_code_icontains,
        short_code_iendswith=short_code_iendswith,
        short_code_iexact=short_code_iexact,
        short_code_in=short_code_in,
        short_code_iregex=short_code_iregex,
        short_code_isnull=short_code_isnull,
        short_code_istartswith=short_code_istartswith,
        short_code_lt=short_code_lt,
        short_code_lte=short_code_lte,
        short_code_range=short_code_range,
        short_code_regex=short_code_regex,
        short_code_startswith=short_code_startswith,
        title=title,
        title_contains=title_contains,
        title_endswith=title_endswith,
        title_gt=title_gt,
        title_gte=title_gte,
        title_icontains=title_icontains,
        title_iendswith=title_iendswith,
        title_iexact=title_iexact,
        title_in=title_in,
        title_iregex=title_iregex,
        title_isnull=title_isnull,
        title_istartswith=title_istartswith,
        title_lt=title_lt,
        title_lte=title_lte,
        title_range=title_range,
        title_regex=title_regex,
        title_startswith=title_startswith,
        uuid=uuid,
        uuid_contains=uuid_contains,
        uuid_endswith=uuid_endswith,
        uuid_gt=uuid_gt,
        uuid_gte=uuid_gte,
        uuid_icontains=uuid_icontains,
        uuid_iendswith=uuid_iendswith,
        uuid_iexact=uuid_iexact,
        uuid_in=uuid_in,
        uuid_iregex=uuid_iregex,
        uuid_isnull=uuid_isnull,
        uuid_istartswith=uuid_istartswith,
        uuid_lt=uuid_lt,
        uuid_lte=uuid_lte,
        uuid_range=uuid_range,
        uuid_regex=uuid_regex,
        uuid_startswith=uuid_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    instrument_type: InstrumentsListInstrumentType | Unset = UNSET,
    instrument_type_contains: str | Unset = UNSET,
    instrument_type_endswith: str | Unset = UNSET,
    instrument_type_gt: str | Unset = UNSET,
    instrument_type_gte: str | Unset = UNSET,
    instrument_type_icontains: str | Unset = UNSET,
    instrument_type_iendswith: str | Unset = UNSET,
    instrument_type_iexact: str | Unset = UNSET,
    instrument_type_in: list[str] | Unset = UNSET,
    instrument_type_iregex: str | Unset = UNSET,
    instrument_type_isnull: bool | Unset = UNSET,
    instrument_type_istartswith: str | Unset = UNSET,
    instrument_type_lt: str | Unset = UNSET,
    instrument_type_lte: str | Unset = UNSET,
    instrument_type_range: list[str] | Unset = UNSET,
    instrument_type_regex: str | Unset = UNSET,
    instrument_type_startswith: str | Unset = UNSET,
    keywords: str | Unset = UNSET,
    keywords_contains: str | Unset = UNSET,
    keywords_endswith: str | Unset = UNSET,
    keywords_gt: str | Unset = UNSET,
    keywords_gte: str | Unset = UNSET,
    keywords_icontains: str | Unset = UNSET,
    keywords_iendswith: str | Unset = UNSET,
    keywords_iexact: str | Unset = UNSET,
    keywords_in: list[str] | Unset = UNSET,
    keywords_iregex: str | Unset = UNSET,
    keywords_isnull: bool | Unset = UNSET,
    keywords_istartswith: str | Unset = UNSET,
    keywords_lt: str | Unset = UNSET,
    keywords_lte: str | Unset = UNSET,
    keywords_range: list[str] | Unset = UNSET,
    keywords_regex: str | Unset = UNSET,
    keywords_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ob_id: int | Unset = UNSET,
    ob_id_contained_by: int | Unset = UNSET,
    ob_id_contains: int | Unset = UNSET,
    ob_id_endswith: int | Unset = UNSET,
    ob_id_gt: int | Unset = UNSET,
    ob_id_gte: int | Unset = UNSET,
    ob_id_icontains: int | Unset = UNSET,
    ob_id_iendswith: int | Unset = UNSET,
    ob_id_iexact: int | Unset = UNSET,
    ob_id_in: list[int] | Unset = UNSET,
    ob_id_iregex: int | Unset = UNSET,
    ob_id_isnull: bool | Unset = UNSET,
    ob_id_istartswith: int | Unset = UNSET,
    ob_id_lt: int | Unset = UNSET,
    ob_id_lte: int | Unset = UNSET,
    ob_id_range: list[int] | Unset = UNSET,
    ob_id_regex: int | Unset = UNSET,
    ob_id_startswith: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_gt: int | Unset = UNSET,
    referenceable_ptr_gte: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    referenceable_ptr_lt: int | Unset = UNSET,
    referenceable_ptr_lte: int | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> Response[PaginatedInstrumentReadList]:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        instrument_type (InstrumentsListInstrumentType | Unset):
        instrument_type_contains (str | Unset):
        instrument_type_endswith (str | Unset):
        instrument_type_gt (str | Unset):
        instrument_type_gte (str | Unset):
        instrument_type_icontains (str | Unset):
        instrument_type_iendswith (str | Unset):
        instrument_type_iexact (str | Unset):
        instrument_type_in (list[str] | Unset):
        instrument_type_iregex (str | Unset):
        instrument_type_isnull (bool | Unset):
        instrument_type_istartswith (str | Unset):
        instrument_type_lt (str | Unset):
        instrument_type_lte (str | Unset):
        instrument_type_range (list[str] | Unset):
        instrument_type_regex (str | Unset):
        instrument_type_startswith (str | Unset):
        keywords (str | Unset):
        keywords_contains (str | Unset):
        keywords_endswith (str | Unset):
        keywords_gt (str | Unset):
        keywords_gte (str | Unset):
        keywords_icontains (str | Unset):
        keywords_iendswith (str | Unset):
        keywords_iexact (str | Unset):
        keywords_in (list[str] | Unset):
        keywords_iregex (str | Unset):
        keywords_isnull (bool | Unset):
        keywords_istartswith (str | Unset):
        keywords_lt (str | Unset):
        keywords_lte (str | Unset):
        keywords_range (list[str] | Unset):
        keywords_regex (str | Unset):
        keywords_startswith (str | Unset):
        limit (int | Unset):
        ob_id (int | Unset):
        ob_id_contained_by (int | Unset):
        ob_id_contains (int | Unset):
        ob_id_endswith (int | Unset):
        ob_id_gt (int | Unset):
        ob_id_gte (int | Unset):
        ob_id_icontains (int | Unset):
        ob_id_iendswith (int | Unset):
        ob_id_iexact (int | Unset):
        ob_id_in (list[int] | Unset):
        ob_id_iregex (int | Unset):
        ob_id_isnull (bool | Unset):
        ob_id_istartswith (int | Unset):
        ob_id_lt (int | Unset):
        ob_id_lte (int | Unset):
        ob_id_range (list[int] | Unset):
        ob_id_regex (int | Unset):
        ob_id_startswith (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_gt (int | Unset):
        referenceable_ptr_gte (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        referenceable_ptr_lt (int | Unset):
        referenceable_ptr_lte (int | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedInstrumentReadList]
    """

    kwargs = _get_kwargs(
        abstract=abstract,
        abstract_contains=abstract_contains,
        abstract_endswith=abstract_endswith,
        abstract_gt=abstract_gt,
        abstract_gte=abstract_gte,
        abstract_icontains=abstract_icontains,
        abstract_iendswith=abstract_iendswith,
        abstract_iexact=abstract_iexact,
        abstract_in=abstract_in,
        abstract_iregex=abstract_iregex,
        abstract_isnull=abstract_isnull,
        abstract_istartswith=abstract_istartswith,
        abstract_lt=abstract_lt,
        abstract_lte=abstract_lte,
        abstract_range=abstract_range,
        abstract_regex=abstract_regex,
        abstract_startswith=abstract_startswith,
        instrument_type=instrument_type,
        instrument_type_contains=instrument_type_contains,
        instrument_type_endswith=instrument_type_endswith,
        instrument_type_gt=instrument_type_gt,
        instrument_type_gte=instrument_type_gte,
        instrument_type_icontains=instrument_type_icontains,
        instrument_type_iendswith=instrument_type_iendswith,
        instrument_type_iexact=instrument_type_iexact,
        instrument_type_in=instrument_type_in,
        instrument_type_iregex=instrument_type_iregex,
        instrument_type_isnull=instrument_type_isnull,
        instrument_type_istartswith=instrument_type_istartswith,
        instrument_type_lt=instrument_type_lt,
        instrument_type_lte=instrument_type_lte,
        instrument_type_range=instrument_type_range,
        instrument_type_regex=instrument_type_regex,
        instrument_type_startswith=instrument_type_startswith,
        keywords=keywords,
        keywords_contains=keywords_contains,
        keywords_endswith=keywords_endswith,
        keywords_gt=keywords_gt,
        keywords_gte=keywords_gte,
        keywords_icontains=keywords_icontains,
        keywords_iendswith=keywords_iendswith,
        keywords_iexact=keywords_iexact,
        keywords_in=keywords_in,
        keywords_iregex=keywords_iregex,
        keywords_isnull=keywords_isnull,
        keywords_istartswith=keywords_istartswith,
        keywords_lt=keywords_lt,
        keywords_lte=keywords_lte,
        keywords_range=keywords_range,
        keywords_regex=keywords_regex,
        keywords_startswith=keywords_startswith,
        limit=limit,
        ob_id=ob_id,
        ob_id_contained_by=ob_id_contained_by,
        ob_id_contains=ob_id_contains,
        ob_id_endswith=ob_id_endswith,
        ob_id_gt=ob_id_gt,
        ob_id_gte=ob_id_gte,
        ob_id_icontains=ob_id_icontains,
        ob_id_iendswith=ob_id_iendswith,
        ob_id_iexact=ob_id_iexact,
        ob_id_in=ob_id_in,
        ob_id_iregex=ob_id_iregex,
        ob_id_isnull=ob_id_isnull,
        ob_id_istartswith=ob_id_istartswith,
        ob_id_lt=ob_id_lt,
        ob_id_lte=ob_id_lte,
        ob_id_range=ob_id_range,
        ob_id_regex=ob_id_regex,
        ob_id_startswith=ob_id_startswith,
        offset=offset,
        ordering=ordering,
        referenceable_ptr=referenceable_ptr,
        referenceable_ptr_gt=referenceable_ptr_gt,
        referenceable_ptr_gte=referenceable_ptr_gte,
        referenceable_ptr_in=referenceable_ptr_in,
        referenceable_ptr_isnull=referenceable_ptr_isnull,
        referenceable_ptr_lt=referenceable_ptr_lt,
        referenceable_ptr_lte=referenceable_ptr_lte,
        short_code=short_code,
        short_code_contains=short_code_contains,
        short_code_endswith=short_code_endswith,
        short_code_gt=short_code_gt,
        short_code_gte=short_code_gte,
        short_code_icontains=short_code_icontains,
        short_code_iendswith=short_code_iendswith,
        short_code_iexact=short_code_iexact,
        short_code_in=short_code_in,
        short_code_iregex=short_code_iregex,
        short_code_isnull=short_code_isnull,
        short_code_istartswith=short_code_istartswith,
        short_code_lt=short_code_lt,
        short_code_lte=short_code_lte,
        short_code_range=short_code_range,
        short_code_regex=short_code_regex,
        short_code_startswith=short_code_startswith,
        title=title,
        title_contains=title_contains,
        title_endswith=title_endswith,
        title_gt=title_gt,
        title_gte=title_gte,
        title_icontains=title_icontains,
        title_iendswith=title_iendswith,
        title_iexact=title_iexact,
        title_in=title_in,
        title_iregex=title_iregex,
        title_isnull=title_isnull,
        title_istartswith=title_istartswith,
        title_lt=title_lt,
        title_lte=title_lte,
        title_range=title_range,
        title_regex=title_regex,
        title_startswith=title_startswith,
        uuid=uuid,
        uuid_contains=uuid_contains,
        uuid_endswith=uuid_endswith,
        uuid_gt=uuid_gt,
        uuid_gte=uuid_gte,
        uuid_icontains=uuid_icontains,
        uuid_iendswith=uuid_iendswith,
        uuid_iexact=uuid_iexact,
        uuid_in=uuid_in,
        uuid_iregex=uuid_iregex,
        uuid_isnull=uuid_isnull,
        uuid_istartswith=uuid_istartswith,
        uuid_lt=uuid_lt,
        uuid_lte=uuid_lte,
        uuid_range=uuid_range,
        uuid_regex=uuid_regex,
        uuid_startswith=uuid_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    abstract: str | Unset = UNSET,
    abstract_contains: str | Unset = UNSET,
    abstract_endswith: str | Unset = UNSET,
    abstract_gt: str | Unset = UNSET,
    abstract_gte: str | Unset = UNSET,
    abstract_icontains: str | Unset = UNSET,
    abstract_iendswith: str | Unset = UNSET,
    abstract_iexact: str | Unset = UNSET,
    abstract_in: list[str] | Unset = UNSET,
    abstract_iregex: str | Unset = UNSET,
    abstract_isnull: bool | Unset = UNSET,
    abstract_istartswith: str | Unset = UNSET,
    abstract_lt: str | Unset = UNSET,
    abstract_lte: str | Unset = UNSET,
    abstract_range: list[str] | Unset = UNSET,
    abstract_regex: str | Unset = UNSET,
    abstract_startswith: str | Unset = UNSET,
    instrument_type: InstrumentsListInstrumentType | Unset = UNSET,
    instrument_type_contains: str | Unset = UNSET,
    instrument_type_endswith: str | Unset = UNSET,
    instrument_type_gt: str | Unset = UNSET,
    instrument_type_gte: str | Unset = UNSET,
    instrument_type_icontains: str | Unset = UNSET,
    instrument_type_iendswith: str | Unset = UNSET,
    instrument_type_iexact: str | Unset = UNSET,
    instrument_type_in: list[str] | Unset = UNSET,
    instrument_type_iregex: str | Unset = UNSET,
    instrument_type_isnull: bool | Unset = UNSET,
    instrument_type_istartswith: str | Unset = UNSET,
    instrument_type_lt: str | Unset = UNSET,
    instrument_type_lte: str | Unset = UNSET,
    instrument_type_range: list[str] | Unset = UNSET,
    instrument_type_regex: str | Unset = UNSET,
    instrument_type_startswith: str | Unset = UNSET,
    keywords: str | Unset = UNSET,
    keywords_contains: str | Unset = UNSET,
    keywords_endswith: str | Unset = UNSET,
    keywords_gt: str | Unset = UNSET,
    keywords_gte: str | Unset = UNSET,
    keywords_icontains: str | Unset = UNSET,
    keywords_iendswith: str | Unset = UNSET,
    keywords_iexact: str | Unset = UNSET,
    keywords_in: list[str] | Unset = UNSET,
    keywords_iregex: str | Unset = UNSET,
    keywords_isnull: bool | Unset = UNSET,
    keywords_istartswith: str | Unset = UNSET,
    keywords_lt: str | Unset = UNSET,
    keywords_lte: str | Unset = UNSET,
    keywords_range: list[str] | Unset = UNSET,
    keywords_regex: str | Unset = UNSET,
    keywords_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    ob_id: int | Unset = UNSET,
    ob_id_contained_by: int | Unset = UNSET,
    ob_id_contains: int | Unset = UNSET,
    ob_id_endswith: int | Unset = UNSET,
    ob_id_gt: int | Unset = UNSET,
    ob_id_gte: int | Unset = UNSET,
    ob_id_icontains: int | Unset = UNSET,
    ob_id_iendswith: int | Unset = UNSET,
    ob_id_iexact: int | Unset = UNSET,
    ob_id_in: list[int] | Unset = UNSET,
    ob_id_iregex: int | Unset = UNSET,
    ob_id_isnull: bool | Unset = UNSET,
    ob_id_istartswith: int | Unset = UNSET,
    ob_id_lt: int | Unset = UNSET,
    ob_id_lte: int | Unset = UNSET,
    ob_id_range: list[int] | Unset = UNSET,
    ob_id_regex: int | Unset = UNSET,
    ob_id_startswith: int | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    referenceable_ptr: int | Unset = UNSET,
    referenceable_ptr_gt: int | Unset = UNSET,
    referenceable_ptr_gte: int | Unset = UNSET,
    referenceable_ptr_in: list[int] | Unset = UNSET,
    referenceable_ptr_isnull: bool | Unset = UNSET,
    referenceable_ptr_lt: int | Unset = UNSET,
    referenceable_ptr_lte: int | Unset = UNSET,
    short_code: str | Unset = UNSET,
    short_code_contains: str | Unset = UNSET,
    short_code_endswith: str | Unset = UNSET,
    short_code_gt: str | Unset = UNSET,
    short_code_gte: str | Unset = UNSET,
    short_code_icontains: str | Unset = UNSET,
    short_code_iendswith: str | Unset = UNSET,
    short_code_iexact: str | Unset = UNSET,
    short_code_in: list[str] | Unset = UNSET,
    short_code_iregex: str | Unset = UNSET,
    short_code_isnull: bool | Unset = UNSET,
    short_code_istartswith: str | Unset = UNSET,
    short_code_lt: str | Unset = UNSET,
    short_code_lte: str | Unset = UNSET,
    short_code_range: list[str] | Unset = UNSET,
    short_code_regex: str | Unset = UNSET,
    short_code_startswith: str | Unset = UNSET,
    title: str | Unset = UNSET,
    title_contains: str | Unset = UNSET,
    title_endswith: str | Unset = UNSET,
    title_gt: str | Unset = UNSET,
    title_gte: str | Unset = UNSET,
    title_icontains: str | Unset = UNSET,
    title_iendswith: str | Unset = UNSET,
    title_iexact: str | Unset = UNSET,
    title_in: list[str] | Unset = UNSET,
    title_iregex: str | Unset = UNSET,
    title_isnull: bool | Unset = UNSET,
    title_istartswith: str | Unset = UNSET,
    title_lt: str | Unset = UNSET,
    title_lte: str | Unset = UNSET,
    title_range: list[str] | Unset = UNSET,
    title_regex: str | Unset = UNSET,
    title_startswith: str | Unset = UNSET,
    uuid: str | Unset = UNSET,
    uuid_contains: str | Unset = UNSET,
    uuid_endswith: str | Unset = UNSET,
    uuid_gt: str | Unset = UNSET,
    uuid_gte: str | Unset = UNSET,
    uuid_icontains: str | Unset = UNSET,
    uuid_iendswith: str | Unset = UNSET,
    uuid_iexact: str | Unset = UNSET,
    uuid_in: list[str] | Unset = UNSET,
    uuid_iregex: str | Unset = UNSET,
    uuid_isnull: bool | Unset = UNSET,
    uuid_istartswith: str | Unset = UNSET,
    uuid_lt: str | Unset = UNSET,
    uuid_lte: str | Unset = UNSET,
    uuid_range: list[str] | Unset = UNSET,
    uuid_regex: str | Unset = UNSET,
    uuid_startswith: str | Unset = UNSET,
) -> PaginatedInstrumentReadList | None:
    """Get a list of Instrument objects. Instruments have a 1:1 mapping with Observations.

    Args:
        abstract (str | Unset):
        abstract_contains (str | Unset):
        abstract_endswith (str | Unset):
        abstract_gt (str | Unset):
        abstract_gte (str | Unset):
        abstract_icontains (str | Unset):
        abstract_iendswith (str | Unset):
        abstract_iexact (str | Unset):
        abstract_in (list[str] | Unset):
        abstract_iregex (str | Unset):
        abstract_isnull (bool | Unset):
        abstract_istartswith (str | Unset):
        abstract_lt (str | Unset):
        abstract_lte (str | Unset):
        abstract_range (list[str] | Unset):
        abstract_regex (str | Unset):
        abstract_startswith (str | Unset):
        instrument_type (InstrumentsListInstrumentType | Unset):
        instrument_type_contains (str | Unset):
        instrument_type_endswith (str | Unset):
        instrument_type_gt (str | Unset):
        instrument_type_gte (str | Unset):
        instrument_type_icontains (str | Unset):
        instrument_type_iendswith (str | Unset):
        instrument_type_iexact (str | Unset):
        instrument_type_in (list[str] | Unset):
        instrument_type_iregex (str | Unset):
        instrument_type_isnull (bool | Unset):
        instrument_type_istartswith (str | Unset):
        instrument_type_lt (str | Unset):
        instrument_type_lte (str | Unset):
        instrument_type_range (list[str] | Unset):
        instrument_type_regex (str | Unset):
        instrument_type_startswith (str | Unset):
        keywords (str | Unset):
        keywords_contains (str | Unset):
        keywords_endswith (str | Unset):
        keywords_gt (str | Unset):
        keywords_gte (str | Unset):
        keywords_icontains (str | Unset):
        keywords_iendswith (str | Unset):
        keywords_iexact (str | Unset):
        keywords_in (list[str] | Unset):
        keywords_iregex (str | Unset):
        keywords_isnull (bool | Unset):
        keywords_istartswith (str | Unset):
        keywords_lt (str | Unset):
        keywords_lte (str | Unset):
        keywords_range (list[str] | Unset):
        keywords_regex (str | Unset):
        keywords_startswith (str | Unset):
        limit (int | Unset):
        ob_id (int | Unset):
        ob_id_contained_by (int | Unset):
        ob_id_contains (int | Unset):
        ob_id_endswith (int | Unset):
        ob_id_gt (int | Unset):
        ob_id_gte (int | Unset):
        ob_id_icontains (int | Unset):
        ob_id_iendswith (int | Unset):
        ob_id_iexact (int | Unset):
        ob_id_in (list[int] | Unset):
        ob_id_iregex (int | Unset):
        ob_id_isnull (bool | Unset):
        ob_id_istartswith (int | Unset):
        ob_id_lt (int | Unset):
        ob_id_lte (int | Unset):
        ob_id_range (list[int] | Unset):
        ob_id_regex (int | Unset):
        ob_id_startswith (int | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        referenceable_ptr (int | Unset):
        referenceable_ptr_gt (int | Unset):
        referenceable_ptr_gte (int | Unset):
        referenceable_ptr_in (list[int] | Unset):
        referenceable_ptr_isnull (bool | Unset):
        referenceable_ptr_lt (int | Unset):
        referenceable_ptr_lte (int | Unset):
        short_code (str | Unset):
        short_code_contains (str | Unset):
        short_code_endswith (str | Unset):
        short_code_gt (str | Unset):
        short_code_gte (str | Unset):
        short_code_icontains (str | Unset):
        short_code_iendswith (str | Unset):
        short_code_iexact (str | Unset):
        short_code_in (list[str] | Unset):
        short_code_iregex (str | Unset):
        short_code_isnull (bool | Unset):
        short_code_istartswith (str | Unset):
        short_code_lt (str | Unset):
        short_code_lte (str | Unset):
        short_code_range (list[str] | Unset):
        short_code_regex (str | Unset):
        short_code_startswith (str | Unset):
        title (str | Unset):
        title_contains (str | Unset):
        title_endswith (str | Unset):
        title_gt (str | Unset):
        title_gte (str | Unset):
        title_icontains (str | Unset):
        title_iendswith (str | Unset):
        title_iexact (str | Unset):
        title_in (list[str] | Unset):
        title_iregex (str | Unset):
        title_isnull (bool | Unset):
        title_istartswith (str | Unset):
        title_lt (str | Unset):
        title_lte (str | Unset):
        title_range (list[str] | Unset):
        title_regex (str | Unset):
        title_startswith (str | Unset):
        uuid (str | Unset):
        uuid_contains (str | Unset):
        uuid_endswith (str | Unset):
        uuid_gt (str | Unset):
        uuid_gte (str | Unset):
        uuid_icontains (str | Unset):
        uuid_iendswith (str | Unset):
        uuid_iexact (str | Unset):
        uuid_in (list[str] | Unset):
        uuid_iregex (str | Unset):
        uuid_isnull (bool | Unset):
        uuid_istartswith (str | Unset):
        uuid_lt (str | Unset):
        uuid_lte (str | Unset):
        uuid_range (list[str] | Unset):
        uuid_regex (str | Unset):
        uuid_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedInstrumentReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            abstract=abstract,
            abstract_contains=abstract_contains,
            abstract_endswith=abstract_endswith,
            abstract_gt=abstract_gt,
            abstract_gte=abstract_gte,
            abstract_icontains=abstract_icontains,
            abstract_iendswith=abstract_iendswith,
            abstract_iexact=abstract_iexact,
            abstract_in=abstract_in,
            abstract_iregex=abstract_iregex,
            abstract_isnull=abstract_isnull,
            abstract_istartswith=abstract_istartswith,
            abstract_lt=abstract_lt,
            abstract_lte=abstract_lte,
            abstract_range=abstract_range,
            abstract_regex=abstract_regex,
            abstract_startswith=abstract_startswith,
            instrument_type=instrument_type,
            instrument_type_contains=instrument_type_contains,
            instrument_type_endswith=instrument_type_endswith,
            instrument_type_gt=instrument_type_gt,
            instrument_type_gte=instrument_type_gte,
            instrument_type_icontains=instrument_type_icontains,
            instrument_type_iendswith=instrument_type_iendswith,
            instrument_type_iexact=instrument_type_iexact,
            instrument_type_in=instrument_type_in,
            instrument_type_iregex=instrument_type_iregex,
            instrument_type_isnull=instrument_type_isnull,
            instrument_type_istartswith=instrument_type_istartswith,
            instrument_type_lt=instrument_type_lt,
            instrument_type_lte=instrument_type_lte,
            instrument_type_range=instrument_type_range,
            instrument_type_regex=instrument_type_regex,
            instrument_type_startswith=instrument_type_startswith,
            keywords=keywords,
            keywords_contains=keywords_contains,
            keywords_endswith=keywords_endswith,
            keywords_gt=keywords_gt,
            keywords_gte=keywords_gte,
            keywords_icontains=keywords_icontains,
            keywords_iendswith=keywords_iendswith,
            keywords_iexact=keywords_iexact,
            keywords_in=keywords_in,
            keywords_iregex=keywords_iregex,
            keywords_isnull=keywords_isnull,
            keywords_istartswith=keywords_istartswith,
            keywords_lt=keywords_lt,
            keywords_lte=keywords_lte,
            keywords_range=keywords_range,
            keywords_regex=keywords_regex,
            keywords_startswith=keywords_startswith,
            limit=limit,
            ob_id=ob_id,
            ob_id_contained_by=ob_id_contained_by,
            ob_id_contains=ob_id_contains,
            ob_id_endswith=ob_id_endswith,
            ob_id_gt=ob_id_gt,
            ob_id_gte=ob_id_gte,
            ob_id_icontains=ob_id_icontains,
            ob_id_iendswith=ob_id_iendswith,
            ob_id_iexact=ob_id_iexact,
            ob_id_in=ob_id_in,
            ob_id_iregex=ob_id_iregex,
            ob_id_isnull=ob_id_isnull,
            ob_id_istartswith=ob_id_istartswith,
            ob_id_lt=ob_id_lt,
            ob_id_lte=ob_id_lte,
            ob_id_range=ob_id_range,
            ob_id_regex=ob_id_regex,
            ob_id_startswith=ob_id_startswith,
            offset=offset,
            ordering=ordering,
            referenceable_ptr=referenceable_ptr,
            referenceable_ptr_gt=referenceable_ptr_gt,
            referenceable_ptr_gte=referenceable_ptr_gte,
            referenceable_ptr_in=referenceable_ptr_in,
            referenceable_ptr_isnull=referenceable_ptr_isnull,
            referenceable_ptr_lt=referenceable_ptr_lt,
            referenceable_ptr_lte=referenceable_ptr_lte,
            short_code=short_code,
            short_code_contains=short_code_contains,
            short_code_endswith=short_code_endswith,
            short_code_gt=short_code_gt,
            short_code_gte=short_code_gte,
            short_code_icontains=short_code_icontains,
            short_code_iendswith=short_code_iendswith,
            short_code_iexact=short_code_iexact,
            short_code_in=short_code_in,
            short_code_iregex=short_code_iregex,
            short_code_isnull=short_code_isnull,
            short_code_istartswith=short_code_istartswith,
            short_code_lt=short_code_lt,
            short_code_lte=short_code_lte,
            short_code_range=short_code_range,
            short_code_regex=short_code_regex,
            short_code_startswith=short_code_startswith,
            title=title,
            title_contains=title_contains,
            title_endswith=title_endswith,
            title_gt=title_gt,
            title_gte=title_gte,
            title_icontains=title_icontains,
            title_iendswith=title_iendswith,
            title_iexact=title_iexact,
            title_in=title_in,
            title_iregex=title_iregex,
            title_isnull=title_isnull,
            title_istartswith=title_istartswith,
            title_lt=title_lt,
            title_lte=title_lte,
            title_range=title_range,
            title_regex=title_regex,
            title_startswith=title_startswith,
            uuid=uuid,
            uuid_contains=uuid_contains,
            uuid_endswith=uuid_endswith,
            uuid_gt=uuid_gt,
            uuid_gte=uuid_gte,
            uuid_icontains=uuid_icontains,
            uuid_iendswith=uuid_iendswith,
            uuid_iexact=uuid_iexact,
            uuid_in=uuid_in,
            uuid_iregex=uuid_iregex,
            uuid_isnull=uuid_isnull,
            uuid_istartswith=uuid_istartswith,
            uuid_lt=uuid_lt,
            uuid_lte=uuid_lte,
            uuid_range=uuid_range,
            uuid_regex=uuid_regex,
            uuid_startswith=uuid_startswith,
        )
    ).parsed
