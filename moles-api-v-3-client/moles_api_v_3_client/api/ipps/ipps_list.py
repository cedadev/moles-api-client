from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_instrument_platform_pair_read_list import PaginatedInstrumentPlatformPairReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    instrument: int | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    instrument_ob_id: int | Unset = UNSET,
    instrument_ob_id_in: list[int] | Unset = UNSET,
    instrument_uuid: str | Unset = UNSET,
    instrument_uuid_in: list[str] | Unset = UNSET,
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
    platform: int | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    platform_ob_id: int | Unset = UNSET,
    platform_ob_id_in: list[int] | Unset = UNSET,
    platform_uuid: str | Unset = UNSET,
    platform_uuid_in: list[str] | Unset = UNSET,
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["instrument"] = instrument

    json_instrument_in: list[int] | Unset = UNSET
    if not isinstance(instrument_in, Unset):
        json_instrument_in = instrument_in

    params["instrument__in"] = json_instrument_in

    params["instrument__isnull"] = instrument_isnull

    params["instrument__ob_id"] = instrument_ob_id

    json_instrument_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(instrument_ob_id_in, Unset):
        json_instrument_ob_id_in = instrument_ob_id_in

    params["instrument__ob_id__in"] = json_instrument_ob_id_in

    params["instrument__uuid"] = instrument_uuid

    json_instrument_uuid_in: list[str] | Unset = UNSET
    if not isinstance(instrument_uuid_in, Unset):
        json_instrument_uuid_in = instrument_uuid_in

    params["instrument__uuid__in"] = json_instrument_uuid_in

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
        json_ob_id_in = ob_id_in

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: list[int] | Unset = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ob_id_range

    params["ob_id__range"] = json_ob_id_range

    params["ob_id__regex"] = ob_id_regex

    params["ob_id__startswith"] = ob_id_startswith

    params["offset"] = offset

    params["ordering"] = ordering

    params["platform"] = platform

    json_platform_in: list[int] | Unset = UNSET
    if not isinstance(platform_in, Unset):
        json_platform_in = platform_in

    params["platform__in"] = json_platform_in

    params["platform__isnull"] = platform_isnull

    params["platform__ob_id"] = platform_ob_id

    json_platform_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(platform_ob_id_in, Unset):
        json_platform_ob_id_in = platform_ob_id_in

    params["platform__ob_id__in"] = json_platform_ob_id_in

    params["platform__uuid"] = platform_uuid

    json_platform_uuid_in: list[str] | Unset = UNSET
    if not isinstance(platform_uuid_in, Unset):
        json_platform_uuid_in = platform_uuid_in

    params["platform__uuid__in"] = json_platform_uuid_in

    params["relatedTo"] = related_to

    json_related_to_in: list[int] | Unset = UNSET
    if not isinstance(related_to_in, Unset):
        json_related_to_in = related_to_in

    params["relatedTo__in"] = json_related_to_in

    params["relatedTo__isnull"] = related_to_isnull

    params["relatedTo__ob_id"] = related_to_ob_id

    json_related_to_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(related_to_ob_id_in, Unset):
        json_related_to_ob_id_in = related_to_ob_id_in

    params["relatedTo__ob_id__in"] = json_related_to_ob_id_in

    params["relatedTo__short_code"] = related_to_short_code

    json_related_to_short_code_in: list[str] | Unset = UNSET
    if not isinstance(related_to_short_code_in, Unset):
        json_related_to_short_code_in = related_to_short_code_in

    params["relatedTo__short_code__in"] = json_related_to_short_code_in

    params["relatedTo__uuid"] = related_to_uuid

    json_related_to_uuid_in: list[str] | Unset = UNSET
    if not isinstance(related_to_uuid_in, Unset):
        json_related_to_uuid_in = related_to_uuid_in

    params["relatedTo__uuid__in"] = json_related_to_uuid_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/ipps/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedInstrumentPlatformPairReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedInstrumentPlatformPairReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedInstrumentPlatformPairReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    instrument: int | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    instrument_ob_id: int | Unset = UNSET,
    instrument_ob_id_in: list[int] | Unset = UNSET,
    instrument_uuid: str | Unset = UNSET,
    instrument_uuid_in: list[str] | Unset = UNSET,
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
    platform: int | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    platform_ob_id: int | Unset = UNSET,
    platform_ob_id_in: list[int] | Unset = UNSET,
    platform_uuid: str | Unset = UNSET,
    platform_uuid_in: list[str] | Unset = UNSET,
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
) -> Response[PaginatedInstrumentPlatformPairReadList]:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        instrument (int | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        instrument_ob_id (int | Unset):
        instrument_ob_id_in (list[int] | Unset):
        instrument_uuid (str | Unset):
        instrument_uuid_in (list[str] | Unset):
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
        platform (int | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        platform_ob_id (int | Unset):
        platform_ob_id_in (list[int] | Unset):
        platform_uuid (str | Unset):
        platform_uuid_in (list[str] | Unset):
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedInstrumentPlatformPairReadList]
    """

    kwargs = _get_kwargs(
        instrument=instrument,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        instrument_ob_id=instrument_ob_id,
        instrument_ob_id_in=instrument_ob_id_in,
        instrument_uuid=instrument_uuid,
        instrument_uuid_in=instrument_uuid_in,
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
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        platform_ob_id=platform_ob_id,
        platform_ob_id_in=platform_ob_id_in,
        platform_uuid=platform_uuid,
        platform_uuid_in=platform_uuid_in,
        related_to=related_to,
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
        related_to_ob_id=related_to_ob_id,
        related_to_ob_id_in=related_to_ob_id_in,
        related_to_short_code=related_to_short_code,
        related_to_short_code_in=related_to_short_code_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    instrument: int | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    instrument_ob_id: int | Unset = UNSET,
    instrument_ob_id_in: list[int] | Unset = UNSET,
    instrument_uuid: str | Unset = UNSET,
    instrument_uuid_in: list[str] | Unset = UNSET,
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
    platform: int | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    platform_ob_id: int | Unset = UNSET,
    platform_ob_id_in: list[int] | Unset = UNSET,
    platform_uuid: str | Unset = UNSET,
    platform_uuid_in: list[str] | Unset = UNSET,
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
) -> PaginatedInstrumentPlatformPairReadList | None:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        instrument (int | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        instrument_ob_id (int | Unset):
        instrument_ob_id_in (list[int] | Unset):
        instrument_uuid (str | Unset):
        instrument_uuid_in (list[str] | Unset):
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
        platform (int | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        platform_ob_id (int | Unset):
        platform_ob_id_in (list[int] | Unset):
        platform_uuid (str | Unset):
        platform_uuid_in (list[str] | Unset):
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedInstrumentPlatformPairReadList
    """

    return sync_detailed(
        client=client,
        instrument=instrument,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        instrument_ob_id=instrument_ob_id,
        instrument_ob_id_in=instrument_ob_id_in,
        instrument_uuid=instrument_uuid,
        instrument_uuid_in=instrument_uuid_in,
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
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        platform_ob_id=platform_ob_id,
        platform_ob_id_in=platform_ob_id_in,
        platform_uuid=platform_uuid,
        platform_uuid_in=platform_uuid_in,
        related_to=related_to,
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
        related_to_ob_id=related_to_ob_id,
        related_to_ob_id_in=related_to_ob_id_in,
        related_to_short_code=related_to_short_code,
        related_to_short_code_in=related_to_short_code_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    instrument: int | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    instrument_ob_id: int | Unset = UNSET,
    instrument_ob_id_in: list[int] | Unset = UNSET,
    instrument_uuid: str | Unset = UNSET,
    instrument_uuid_in: list[str] | Unset = UNSET,
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
    platform: int | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    platform_ob_id: int | Unset = UNSET,
    platform_ob_id_in: list[int] | Unset = UNSET,
    platform_uuid: str | Unset = UNSET,
    platform_uuid_in: list[str] | Unset = UNSET,
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
) -> Response[PaginatedInstrumentPlatformPairReadList]:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        instrument (int | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        instrument_ob_id (int | Unset):
        instrument_ob_id_in (list[int] | Unset):
        instrument_uuid (str | Unset):
        instrument_uuid_in (list[str] | Unset):
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
        platform (int | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        platform_ob_id (int | Unset):
        platform_ob_id_in (list[int] | Unset):
        platform_uuid (str | Unset):
        platform_uuid_in (list[str] | Unset):
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedInstrumentPlatformPairReadList]
    """

    kwargs = _get_kwargs(
        instrument=instrument,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        instrument_ob_id=instrument_ob_id,
        instrument_ob_id_in=instrument_ob_id_in,
        instrument_uuid=instrument_uuid,
        instrument_uuid_in=instrument_uuid_in,
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
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        platform_ob_id=platform_ob_id,
        platform_ob_id_in=platform_ob_id_in,
        platform_uuid=platform_uuid,
        platform_uuid_in=platform_uuid_in,
        related_to=related_to,
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
        related_to_ob_id=related_to_ob_id,
        related_to_ob_id_in=related_to_ob_id_in,
        related_to_short_code=related_to_short_code,
        related_to_short_code_in=related_to_short_code_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    instrument: int | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    instrument_ob_id: int | Unset = UNSET,
    instrument_ob_id_in: list[int] | Unset = UNSET,
    instrument_uuid: str | Unset = UNSET,
    instrument_uuid_in: list[str] | Unset = UNSET,
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
    platform: int | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    platform_ob_id: int | Unset = UNSET,
    platform_ob_id_in: list[int] | Unset = UNSET,
    platform_uuid: str | Unset = UNSET,
    platform_uuid_in: list[str] | Unset = UNSET,
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
) -> PaginatedInstrumentPlatformPairReadList | None:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        instrument (int | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        instrument_ob_id (int | Unset):
        instrument_ob_id_in (list[int] | Unset):
        instrument_uuid (str | Unset):
        instrument_uuid_in (list[str] | Unset):
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
        platform (int | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        platform_ob_id (int | Unset):
        platform_ob_id_in (list[int] | Unset):
        platform_uuid (str | Unset):
        platform_uuid_in (list[str] | Unset):
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedInstrumentPlatformPairReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            instrument=instrument,
            instrument_in=instrument_in,
            instrument_isnull=instrument_isnull,
            instrument_ob_id=instrument_ob_id,
            instrument_ob_id_in=instrument_ob_id_in,
            instrument_uuid=instrument_uuid,
            instrument_uuid_in=instrument_uuid_in,
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
            platform=platform,
            platform_in=platform_in,
            platform_isnull=platform_isnull,
            platform_ob_id=platform_ob_id,
            platform_ob_id_in=platform_ob_id_in,
            platform_uuid=platform_uuid,
            platform_uuid_in=platform_uuid_in,
            related_to=related_to,
            related_to_in=related_to_in,
            related_to_isnull=related_to_isnull,
            related_to_ob_id=related_to_ob_id,
            related_to_ob_id_in=related_to_ob_id_in,
            related_to_short_code=related_to_short_code,
            related_to_short_code_in=related_to_short_code_in,
            related_to_uuid=related_to_uuid,
            related_to_uuid_in=related_to_uuid_in,
        )
    ).parsed
