from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_instrument_platform_pair_write_list import PaginatedInstrumentPlatformPairWriteList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    instrument: Union[Unset, int] = UNSET,
    instrument_gt: Union[Unset, int] = UNSET,
    instrument_gte: Union[Unset, int] = UNSET,
    instrument_in: Union[Unset, list[int]] = UNSET,
    instrument_isnull: Union[Unset, bool] = UNSET,
    instrument_lt: Union[Unset, int] = UNSET,
    instrument_lte: Union[Unset, int] = UNSET,
    instrument_ob_id: Union[Unset, int] = UNSET,
    instrument_ob_id_in: Union[Unset, list[int]] = UNSET,
    instrument_uuid: Union[Unset, str] = UNSET,
    instrument_uuid_in: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    ob_id: Union[Unset, int] = UNSET,
    ob_id_contained_by: Union[Unset, int] = UNSET,
    ob_id_contains: Union[Unset, int] = UNSET,
    ob_id_endswith: Union[Unset, int] = UNSET,
    ob_id_gt: Union[Unset, int] = UNSET,
    ob_id_gte: Union[Unset, int] = UNSET,
    ob_id_icontains: Union[Unset, int] = UNSET,
    ob_id_iendswith: Union[Unset, int] = UNSET,
    ob_id_iexact: Union[Unset, int] = UNSET,
    ob_id_in: Union[Unset, list[int]] = UNSET,
    ob_id_iregex: Union[Unset, int] = UNSET,
    ob_id_isnull: Union[Unset, bool] = UNSET,
    ob_id_istartswith: Union[Unset, int] = UNSET,
    ob_id_lt: Union[Unset, int] = UNSET,
    ob_id_lte: Union[Unset, int] = UNSET,
    ob_id_range: Union[Unset, list[int]] = UNSET,
    ob_id_regex: Union[Unset, int] = UNSET,
    ob_id_startswith: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    platform: Union[Unset, int] = UNSET,
    platform_gt: Union[Unset, int] = UNSET,
    platform_gte: Union[Unset, int] = UNSET,
    platform_in: Union[Unset, list[int]] = UNSET,
    platform_isnull: Union[Unset, bool] = UNSET,
    platform_lt: Union[Unset, int] = UNSET,
    platform_lte: Union[Unset, int] = UNSET,
    platform_ob_id: Union[Unset, int] = UNSET,
    platform_ob_id_in: Union[Unset, list[int]] = UNSET,
    platform_uuid: Union[Unset, str] = UNSET,
    platform_uuid_in: Union[Unset, list[str]] = UNSET,
    related_to: Union[Unset, int] = UNSET,
    related_to_gt: Union[Unset, int] = UNSET,
    related_to_gte: Union[Unset, int] = UNSET,
    related_to_in: Union[Unset, list[int]] = UNSET,
    related_to_isnull: Union[Unset, bool] = UNSET,
    related_to_lt: Union[Unset, int] = UNSET,
    related_to_lte: Union[Unset, int] = UNSET,
    related_to_ob_id: Union[Unset, int] = UNSET,
    related_to_ob_id_in: Union[Unset, list[int]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["instrument"] = instrument

    params["instrument__gt"] = instrument_gt

    params["instrument__gte"] = instrument_gte

    json_instrument_in: Union[Unset, list[int]] = UNSET
    if not isinstance(instrument_in, Unset):
        json_instrument_in = instrument_in

    params["instrument__in"] = json_instrument_in

    params["instrument__isnull"] = instrument_isnull

    params["instrument__lt"] = instrument_lt

    params["instrument__lte"] = instrument_lte

    params["instrument__ob_id"] = instrument_ob_id

    json_instrument_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(instrument_ob_id_in, Unset):
        json_instrument_ob_id_in = instrument_ob_id_in

    params["instrument__ob_id__in"] = json_instrument_ob_id_in

    params["instrument__uuid"] = instrument_uuid

    json_instrument_uuid_in: Union[Unset, list[str]] = UNSET
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

    json_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_in, Unset):
        json_ob_id_in = ob_id_in

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ob_id_range

    params["ob_id__range"] = json_ob_id_range

    params["ob_id__regex"] = ob_id_regex

    params["ob_id__startswith"] = ob_id_startswith

    params["offset"] = offset

    params["ordering"] = ordering

    params["platform"] = platform

    params["platform__gt"] = platform_gt

    params["platform__gte"] = platform_gte

    json_platform_in: Union[Unset, list[int]] = UNSET
    if not isinstance(platform_in, Unset):
        json_platform_in = platform_in

    params["platform__in"] = json_platform_in

    params["platform__isnull"] = platform_isnull

    params["platform__lt"] = platform_lt

    params["platform__lte"] = platform_lte

    params["platform__ob_id"] = platform_ob_id

    json_platform_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(platform_ob_id_in, Unset):
        json_platform_ob_id_in = platform_ob_id_in

    params["platform__ob_id__in"] = json_platform_ob_id_in

    params["platform__uuid"] = platform_uuid

    json_platform_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(platform_uuid_in, Unset):
        json_platform_uuid_in = platform_uuid_in

    params["platform__uuid__in"] = json_platform_uuid_in

    params["relatedTo"] = related_to

    params["relatedTo__gt"] = related_to_gt

    params["relatedTo__gte"] = related_to_gte

    json_related_to_in: Union[Unset, list[int]] = UNSET
    if not isinstance(related_to_in, Unset):
        json_related_to_in = related_to_in

    params["relatedTo__in"] = json_related_to_in

    params["relatedTo__isnull"] = related_to_isnull

    params["relatedTo__lt"] = related_to_lt

    params["relatedTo__lte"] = related_to_lte

    params["relatedTo__ob_id"] = related_to_ob_id

    json_related_to_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(related_to_ob_id_in, Unset):
        json_related_to_ob_id_in = related_to_ob_id_in

    params["relatedTo__ob_id__in"] = json_related_to_ob_id_in

    params["relatedTo__uuid"] = related_to_uuid

    json_related_to_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(related_to_uuid_in, Unset):
        json_related_to_uuid_in = related_to_uuid_in

    params["relatedTo__uuid__in"] = json_related_to_uuid_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/ipps/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedInstrumentPlatformPairWriteList]:
    if response.status_code == 200:
        response_200 = PaginatedInstrumentPlatformPairWriteList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedInstrumentPlatformPairWriteList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    instrument: Union[Unset, int] = UNSET,
    instrument_gt: Union[Unset, int] = UNSET,
    instrument_gte: Union[Unset, int] = UNSET,
    instrument_in: Union[Unset, list[int]] = UNSET,
    instrument_isnull: Union[Unset, bool] = UNSET,
    instrument_lt: Union[Unset, int] = UNSET,
    instrument_lte: Union[Unset, int] = UNSET,
    instrument_ob_id: Union[Unset, int] = UNSET,
    instrument_ob_id_in: Union[Unset, list[int]] = UNSET,
    instrument_uuid: Union[Unset, str] = UNSET,
    instrument_uuid_in: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    ob_id: Union[Unset, int] = UNSET,
    ob_id_contained_by: Union[Unset, int] = UNSET,
    ob_id_contains: Union[Unset, int] = UNSET,
    ob_id_endswith: Union[Unset, int] = UNSET,
    ob_id_gt: Union[Unset, int] = UNSET,
    ob_id_gte: Union[Unset, int] = UNSET,
    ob_id_icontains: Union[Unset, int] = UNSET,
    ob_id_iendswith: Union[Unset, int] = UNSET,
    ob_id_iexact: Union[Unset, int] = UNSET,
    ob_id_in: Union[Unset, list[int]] = UNSET,
    ob_id_iregex: Union[Unset, int] = UNSET,
    ob_id_isnull: Union[Unset, bool] = UNSET,
    ob_id_istartswith: Union[Unset, int] = UNSET,
    ob_id_lt: Union[Unset, int] = UNSET,
    ob_id_lte: Union[Unset, int] = UNSET,
    ob_id_range: Union[Unset, list[int]] = UNSET,
    ob_id_regex: Union[Unset, int] = UNSET,
    ob_id_startswith: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    platform: Union[Unset, int] = UNSET,
    platform_gt: Union[Unset, int] = UNSET,
    platform_gte: Union[Unset, int] = UNSET,
    platform_in: Union[Unset, list[int]] = UNSET,
    platform_isnull: Union[Unset, bool] = UNSET,
    platform_lt: Union[Unset, int] = UNSET,
    platform_lte: Union[Unset, int] = UNSET,
    platform_ob_id: Union[Unset, int] = UNSET,
    platform_ob_id_in: Union[Unset, list[int]] = UNSET,
    platform_uuid: Union[Unset, str] = UNSET,
    platform_uuid_in: Union[Unset, list[str]] = UNSET,
    related_to: Union[Unset, int] = UNSET,
    related_to_gt: Union[Unset, int] = UNSET,
    related_to_gte: Union[Unset, int] = UNSET,
    related_to_in: Union[Unset, list[int]] = UNSET,
    related_to_isnull: Union[Unset, bool] = UNSET,
    related_to_lt: Union[Unset, int] = UNSET,
    related_to_lte: Union[Unset, int] = UNSET,
    related_to_ob_id: Union[Unset, int] = UNSET,
    related_to_ob_id_in: Union[Unset, list[int]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedInstrumentPlatformPairWriteList]:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        instrument (Union[Unset, int]):
        instrument_gt (Union[Unset, int]):
        instrument_gte (Union[Unset, int]):
        instrument_in (Union[Unset, list[int]]):
        instrument_isnull (Union[Unset, bool]):
        instrument_lt (Union[Unset, int]):
        instrument_lte (Union[Unset, int]):
        instrument_ob_id (Union[Unset, int]):
        instrument_ob_id_in (Union[Unset, list[int]]):
        instrument_uuid (Union[Unset, str]):
        instrument_uuid_in (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        ob_id (Union[Unset, int]):
        ob_id_contained_by (Union[Unset, int]):
        ob_id_contains (Union[Unset, int]):
        ob_id_endswith (Union[Unset, int]):
        ob_id_gt (Union[Unset, int]):
        ob_id_gte (Union[Unset, int]):
        ob_id_icontains (Union[Unset, int]):
        ob_id_iendswith (Union[Unset, int]):
        ob_id_iexact (Union[Unset, int]):
        ob_id_in (Union[Unset, list[int]]):
        ob_id_iregex (Union[Unset, int]):
        ob_id_isnull (Union[Unset, bool]):
        ob_id_istartswith (Union[Unset, int]):
        ob_id_lt (Union[Unset, int]):
        ob_id_lte (Union[Unset, int]):
        ob_id_range (Union[Unset, list[int]]):
        ob_id_regex (Union[Unset, int]):
        ob_id_startswith (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        platform (Union[Unset, int]):
        platform_gt (Union[Unset, int]):
        platform_gte (Union[Unset, int]):
        platform_in (Union[Unset, list[int]]):
        platform_isnull (Union[Unset, bool]):
        platform_lt (Union[Unset, int]):
        platform_lte (Union[Unset, int]):
        platform_ob_id (Union[Unset, int]):
        platform_ob_id_in (Union[Unset, list[int]]):
        platform_uuid (Union[Unset, str]):
        platform_uuid_in (Union[Unset, list[str]]):
        related_to (Union[Unset, int]):
        related_to_gt (Union[Unset, int]):
        related_to_gte (Union[Unset, int]):
        related_to_in (Union[Unset, list[int]]):
        related_to_isnull (Union[Unset, bool]):
        related_to_lt (Union[Unset, int]):
        related_to_lte (Union[Unset, int]):
        related_to_ob_id (Union[Unset, int]):
        related_to_ob_id_in (Union[Unset, list[int]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedInstrumentPlatformPairWriteList]
    """

    kwargs = _get_kwargs(
        instrument=instrument,
        instrument_gt=instrument_gt,
        instrument_gte=instrument_gte,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        instrument_lt=instrument_lt,
        instrument_lte=instrument_lte,
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
        platform_gt=platform_gt,
        platform_gte=platform_gte,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        platform_lt=platform_lt,
        platform_lte=platform_lte,
        platform_ob_id=platform_ob_id,
        platform_ob_id_in=platform_ob_id_in,
        platform_uuid=platform_uuid,
        platform_uuid_in=platform_uuid_in,
        related_to=related_to,
        related_to_gt=related_to_gt,
        related_to_gte=related_to_gte,
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
        related_to_lt=related_to_lt,
        related_to_lte=related_to_lte,
        related_to_ob_id=related_to_ob_id,
        related_to_ob_id_in=related_to_ob_id_in,
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
    instrument: Union[Unset, int] = UNSET,
    instrument_gt: Union[Unset, int] = UNSET,
    instrument_gte: Union[Unset, int] = UNSET,
    instrument_in: Union[Unset, list[int]] = UNSET,
    instrument_isnull: Union[Unset, bool] = UNSET,
    instrument_lt: Union[Unset, int] = UNSET,
    instrument_lte: Union[Unset, int] = UNSET,
    instrument_ob_id: Union[Unset, int] = UNSET,
    instrument_ob_id_in: Union[Unset, list[int]] = UNSET,
    instrument_uuid: Union[Unset, str] = UNSET,
    instrument_uuid_in: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    ob_id: Union[Unset, int] = UNSET,
    ob_id_contained_by: Union[Unset, int] = UNSET,
    ob_id_contains: Union[Unset, int] = UNSET,
    ob_id_endswith: Union[Unset, int] = UNSET,
    ob_id_gt: Union[Unset, int] = UNSET,
    ob_id_gte: Union[Unset, int] = UNSET,
    ob_id_icontains: Union[Unset, int] = UNSET,
    ob_id_iendswith: Union[Unset, int] = UNSET,
    ob_id_iexact: Union[Unset, int] = UNSET,
    ob_id_in: Union[Unset, list[int]] = UNSET,
    ob_id_iregex: Union[Unset, int] = UNSET,
    ob_id_isnull: Union[Unset, bool] = UNSET,
    ob_id_istartswith: Union[Unset, int] = UNSET,
    ob_id_lt: Union[Unset, int] = UNSET,
    ob_id_lte: Union[Unset, int] = UNSET,
    ob_id_range: Union[Unset, list[int]] = UNSET,
    ob_id_regex: Union[Unset, int] = UNSET,
    ob_id_startswith: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    platform: Union[Unset, int] = UNSET,
    platform_gt: Union[Unset, int] = UNSET,
    platform_gte: Union[Unset, int] = UNSET,
    platform_in: Union[Unset, list[int]] = UNSET,
    platform_isnull: Union[Unset, bool] = UNSET,
    platform_lt: Union[Unset, int] = UNSET,
    platform_lte: Union[Unset, int] = UNSET,
    platform_ob_id: Union[Unset, int] = UNSET,
    platform_ob_id_in: Union[Unset, list[int]] = UNSET,
    platform_uuid: Union[Unset, str] = UNSET,
    platform_uuid_in: Union[Unset, list[str]] = UNSET,
    related_to: Union[Unset, int] = UNSET,
    related_to_gt: Union[Unset, int] = UNSET,
    related_to_gte: Union[Unset, int] = UNSET,
    related_to_in: Union[Unset, list[int]] = UNSET,
    related_to_isnull: Union[Unset, bool] = UNSET,
    related_to_lt: Union[Unset, int] = UNSET,
    related_to_lte: Union[Unset, int] = UNSET,
    related_to_ob_id: Union[Unset, int] = UNSET,
    related_to_ob_id_in: Union[Unset, list[int]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedInstrumentPlatformPairWriteList]:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        instrument (Union[Unset, int]):
        instrument_gt (Union[Unset, int]):
        instrument_gte (Union[Unset, int]):
        instrument_in (Union[Unset, list[int]]):
        instrument_isnull (Union[Unset, bool]):
        instrument_lt (Union[Unset, int]):
        instrument_lte (Union[Unset, int]):
        instrument_ob_id (Union[Unset, int]):
        instrument_ob_id_in (Union[Unset, list[int]]):
        instrument_uuid (Union[Unset, str]):
        instrument_uuid_in (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        ob_id (Union[Unset, int]):
        ob_id_contained_by (Union[Unset, int]):
        ob_id_contains (Union[Unset, int]):
        ob_id_endswith (Union[Unset, int]):
        ob_id_gt (Union[Unset, int]):
        ob_id_gte (Union[Unset, int]):
        ob_id_icontains (Union[Unset, int]):
        ob_id_iendswith (Union[Unset, int]):
        ob_id_iexact (Union[Unset, int]):
        ob_id_in (Union[Unset, list[int]]):
        ob_id_iregex (Union[Unset, int]):
        ob_id_isnull (Union[Unset, bool]):
        ob_id_istartswith (Union[Unset, int]):
        ob_id_lt (Union[Unset, int]):
        ob_id_lte (Union[Unset, int]):
        ob_id_range (Union[Unset, list[int]]):
        ob_id_regex (Union[Unset, int]):
        ob_id_startswith (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        platform (Union[Unset, int]):
        platform_gt (Union[Unset, int]):
        platform_gte (Union[Unset, int]):
        platform_in (Union[Unset, list[int]]):
        platform_isnull (Union[Unset, bool]):
        platform_lt (Union[Unset, int]):
        platform_lte (Union[Unset, int]):
        platform_ob_id (Union[Unset, int]):
        platform_ob_id_in (Union[Unset, list[int]]):
        platform_uuid (Union[Unset, str]):
        platform_uuid_in (Union[Unset, list[str]]):
        related_to (Union[Unset, int]):
        related_to_gt (Union[Unset, int]):
        related_to_gte (Union[Unset, int]):
        related_to_in (Union[Unset, list[int]]):
        related_to_isnull (Union[Unset, bool]):
        related_to_lt (Union[Unset, int]):
        related_to_lte (Union[Unset, int]):
        related_to_ob_id (Union[Unset, int]):
        related_to_ob_id_in (Union[Unset, list[int]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedInstrumentPlatformPairWriteList
    """

    return sync_detailed(
        client=client,
        instrument=instrument,
        instrument_gt=instrument_gt,
        instrument_gte=instrument_gte,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        instrument_lt=instrument_lt,
        instrument_lte=instrument_lte,
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
        platform_gt=platform_gt,
        platform_gte=platform_gte,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        platform_lt=platform_lt,
        platform_lte=platform_lte,
        platform_ob_id=platform_ob_id,
        platform_ob_id_in=platform_ob_id_in,
        platform_uuid=platform_uuid,
        platform_uuid_in=platform_uuid_in,
        related_to=related_to,
        related_to_gt=related_to_gt,
        related_to_gte=related_to_gte,
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
        related_to_lt=related_to_lt,
        related_to_lte=related_to_lte,
        related_to_ob_id=related_to_ob_id,
        related_to_ob_id_in=related_to_ob_id_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    instrument: Union[Unset, int] = UNSET,
    instrument_gt: Union[Unset, int] = UNSET,
    instrument_gte: Union[Unset, int] = UNSET,
    instrument_in: Union[Unset, list[int]] = UNSET,
    instrument_isnull: Union[Unset, bool] = UNSET,
    instrument_lt: Union[Unset, int] = UNSET,
    instrument_lte: Union[Unset, int] = UNSET,
    instrument_ob_id: Union[Unset, int] = UNSET,
    instrument_ob_id_in: Union[Unset, list[int]] = UNSET,
    instrument_uuid: Union[Unset, str] = UNSET,
    instrument_uuid_in: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    ob_id: Union[Unset, int] = UNSET,
    ob_id_contained_by: Union[Unset, int] = UNSET,
    ob_id_contains: Union[Unset, int] = UNSET,
    ob_id_endswith: Union[Unset, int] = UNSET,
    ob_id_gt: Union[Unset, int] = UNSET,
    ob_id_gte: Union[Unset, int] = UNSET,
    ob_id_icontains: Union[Unset, int] = UNSET,
    ob_id_iendswith: Union[Unset, int] = UNSET,
    ob_id_iexact: Union[Unset, int] = UNSET,
    ob_id_in: Union[Unset, list[int]] = UNSET,
    ob_id_iregex: Union[Unset, int] = UNSET,
    ob_id_isnull: Union[Unset, bool] = UNSET,
    ob_id_istartswith: Union[Unset, int] = UNSET,
    ob_id_lt: Union[Unset, int] = UNSET,
    ob_id_lte: Union[Unset, int] = UNSET,
    ob_id_range: Union[Unset, list[int]] = UNSET,
    ob_id_regex: Union[Unset, int] = UNSET,
    ob_id_startswith: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    platform: Union[Unset, int] = UNSET,
    platform_gt: Union[Unset, int] = UNSET,
    platform_gte: Union[Unset, int] = UNSET,
    platform_in: Union[Unset, list[int]] = UNSET,
    platform_isnull: Union[Unset, bool] = UNSET,
    platform_lt: Union[Unset, int] = UNSET,
    platform_lte: Union[Unset, int] = UNSET,
    platform_ob_id: Union[Unset, int] = UNSET,
    platform_ob_id_in: Union[Unset, list[int]] = UNSET,
    platform_uuid: Union[Unset, str] = UNSET,
    platform_uuid_in: Union[Unset, list[str]] = UNSET,
    related_to: Union[Unset, int] = UNSET,
    related_to_gt: Union[Unset, int] = UNSET,
    related_to_gte: Union[Unset, int] = UNSET,
    related_to_in: Union[Unset, list[int]] = UNSET,
    related_to_isnull: Union[Unset, bool] = UNSET,
    related_to_lt: Union[Unset, int] = UNSET,
    related_to_lte: Union[Unset, int] = UNSET,
    related_to_ob_id: Union[Unset, int] = UNSET,
    related_to_ob_id_in: Union[Unset, list[int]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedInstrumentPlatformPairWriteList]:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        instrument (Union[Unset, int]):
        instrument_gt (Union[Unset, int]):
        instrument_gte (Union[Unset, int]):
        instrument_in (Union[Unset, list[int]]):
        instrument_isnull (Union[Unset, bool]):
        instrument_lt (Union[Unset, int]):
        instrument_lte (Union[Unset, int]):
        instrument_ob_id (Union[Unset, int]):
        instrument_ob_id_in (Union[Unset, list[int]]):
        instrument_uuid (Union[Unset, str]):
        instrument_uuid_in (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        ob_id (Union[Unset, int]):
        ob_id_contained_by (Union[Unset, int]):
        ob_id_contains (Union[Unset, int]):
        ob_id_endswith (Union[Unset, int]):
        ob_id_gt (Union[Unset, int]):
        ob_id_gte (Union[Unset, int]):
        ob_id_icontains (Union[Unset, int]):
        ob_id_iendswith (Union[Unset, int]):
        ob_id_iexact (Union[Unset, int]):
        ob_id_in (Union[Unset, list[int]]):
        ob_id_iregex (Union[Unset, int]):
        ob_id_isnull (Union[Unset, bool]):
        ob_id_istartswith (Union[Unset, int]):
        ob_id_lt (Union[Unset, int]):
        ob_id_lte (Union[Unset, int]):
        ob_id_range (Union[Unset, list[int]]):
        ob_id_regex (Union[Unset, int]):
        ob_id_startswith (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        platform (Union[Unset, int]):
        platform_gt (Union[Unset, int]):
        platform_gte (Union[Unset, int]):
        platform_in (Union[Unset, list[int]]):
        platform_isnull (Union[Unset, bool]):
        platform_lt (Union[Unset, int]):
        platform_lte (Union[Unset, int]):
        platform_ob_id (Union[Unset, int]):
        platform_ob_id_in (Union[Unset, list[int]]):
        platform_uuid (Union[Unset, str]):
        platform_uuid_in (Union[Unset, list[str]]):
        related_to (Union[Unset, int]):
        related_to_gt (Union[Unset, int]):
        related_to_gte (Union[Unset, int]):
        related_to_in (Union[Unset, list[int]]):
        related_to_isnull (Union[Unset, bool]):
        related_to_lt (Union[Unset, int]):
        related_to_lte (Union[Unset, int]):
        related_to_ob_id (Union[Unset, int]):
        related_to_ob_id_in (Union[Unset, list[int]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedInstrumentPlatformPairWriteList]
    """

    kwargs = _get_kwargs(
        instrument=instrument,
        instrument_gt=instrument_gt,
        instrument_gte=instrument_gte,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        instrument_lt=instrument_lt,
        instrument_lte=instrument_lte,
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
        platform_gt=platform_gt,
        platform_gte=platform_gte,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        platform_lt=platform_lt,
        platform_lte=platform_lte,
        platform_ob_id=platform_ob_id,
        platform_ob_id_in=platform_ob_id_in,
        platform_uuid=platform_uuid,
        platform_uuid_in=platform_uuid_in,
        related_to=related_to,
        related_to_gt=related_to_gt,
        related_to_gte=related_to_gte,
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
        related_to_lt=related_to_lt,
        related_to_lte=related_to_lte,
        related_to_ob_id=related_to_ob_id,
        related_to_ob_id_in=related_to_ob_id_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    instrument: Union[Unset, int] = UNSET,
    instrument_gt: Union[Unset, int] = UNSET,
    instrument_gte: Union[Unset, int] = UNSET,
    instrument_in: Union[Unset, list[int]] = UNSET,
    instrument_isnull: Union[Unset, bool] = UNSET,
    instrument_lt: Union[Unset, int] = UNSET,
    instrument_lte: Union[Unset, int] = UNSET,
    instrument_ob_id: Union[Unset, int] = UNSET,
    instrument_ob_id_in: Union[Unset, list[int]] = UNSET,
    instrument_uuid: Union[Unset, str] = UNSET,
    instrument_uuid_in: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = UNSET,
    ob_id: Union[Unset, int] = UNSET,
    ob_id_contained_by: Union[Unset, int] = UNSET,
    ob_id_contains: Union[Unset, int] = UNSET,
    ob_id_endswith: Union[Unset, int] = UNSET,
    ob_id_gt: Union[Unset, int] = UNSET,
    ob_id_gte: Union[Unset, int] = UNSET,
    ob_id_icontains: Union[Unset, int] = UNSET,
    ob_id_iendswith: Union[Unset, int] = UNSET,
    ob_id_iexact: Union[Unset, int] = UNSET,
    ob_id_in: Union[Unset, list[int]] = UNSET,
    ob_id_iregex: Union[Unset, int] = UNSET,
    ob_id_isnull: Union[Unset, bool] = UNSET,
    ob_id_istartswith: Union[Unset, int] = UNSET,
    ob_id_lt: Union[Unset, int] = UNSET,
    ob_id_lte: Union[Unset, int] = UNSET,
    ob_id_range: Union[Unset, list[int]] = UNSET,
    ob_id_regex: Union[Unset, int] = UNSET,
    ob_id_startswith: Union[Unset, int] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    platform: Union[Unset, int] = UNSET,
    platform_gt: Union[Unset, int] = UNSET,
    platform_gte: Union[Unset, int] = UNSET,
    platform_in: Union[Unset, list[int]] = UNSET,
    platform_isnull: Union[Unset, bool] = UNSET,
    platform_lt: Union[Unset, int] = UNSET,
    platform_lte: Union[Unset, int] = UNSET,
    platform_ob_id: Union[Unset, int] = UNSET,
    platform_ob_id_in: Union[Unset, list[int]] = UNSET,
    platform_uuid: Union[Unset, str] = UNSET,
    platform_uuid_in: Union[Unset, list[str]] = UNSET,
    related_to: Union[Unset, int] = UNSET,
    related_to_gt: Union[Unset, int] = UNSET,
    related_to_gte: Union[Unset, int] = UNSET,
    related_to_in: Union[Unset, list[int]] = UNSET,
    related_to_isnull: Union[Unset, bool] = UNSET,
    related_to_lt: Union[Unset, int] = UNSET,
    related_to_lte: Union[Unset, int] = UNSET,
    related_to_ob_id: Union[Unset, int] = UNSET,
    related_to_ob_id_in: Union[Unset, list[int]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedInstrumentPlatformPairWriteList]:
    """Get a list of InstrumentPlaformPair objects. InstrumentPlaformPairs are used within Acquisitions
    which
    enable linking between Instruments, Platforms and Observations (though may be via
    CompositeProcesses).

    Args:
        instrument (Union[Unset, int]):
        instrument_gt (Union[Unset, int]):
        instrument_gte (Union[Unset, int]):
        instrument_in (Union[Unset, list[int]]):
        instrument_isnull (Union[Unset, bool]):
        instrument_lt (Union[Unset, int]):
        instrument_lte (Union[Unset, int]):
        instrument_ob_id (Union[Unset, int]):
        instrument_ob_id_in (Union[Unset, list[int]]):
        instrument_uuid (Union[Unset, str]):
        instrument_uuid_in (Union[Unset, list[str]]):
        limit (Union[Unset, int]):
        ob_id (Union[Unset, int]):
        ob_id_contained_by (Union[Unset, int]):
        ob_id_contains (Union[Unset, int]):
        ob_id_endswith (Union[Unset, int]):
        ob_id_gt (Union[Unset, int]):
        ob_id_gte (Union[Unset, int]):
        ob_id_icontains (Union[Unset, int]):
        ob_id_iendswith (Union[Unset, int]):
        ob_id_iexact (Union[Unset, int]):
        ob_id_in (Union[Unset, list[int]]):
        ob_id_iregex (Union[Unset, int]):
        ob_id_isnull (Union[Unset, bool]):
        ob_id_istartswith (Union[Unset, int]):
        ob_id_lt (Union[Unset, int]):
        ob_id_lte (Union[Unset, int]):
        ob_id_range (Union[Unset, list[int]]):
        ob_id_regex (Union[Unset, int]):
        ob_id_startswith (Union[Unset, int]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        platform (Union[Unset, int]):
        platform_gt (Union[Unset, int]):
        platform_gte (Union[Unset, int]):
        platform_in (Union[Unset, list[int]]):
        platform_isnull (Union[Unset, bool]):
        platform_lt (Union[Unset, int]):
        platform_lte (Union[Unset, int]):
        platform_ob_id (Union[Unset, int]):
        platform_ob_id_in (Union[Unset, list[int]]):
        platform_uuid (Union[Unset, str]):
        platform_uuid_in (Union[Unset, list[str]]):
        related_to (Union[Unset, int]):
        related_to_gt (Union[Unset, int]):
        related_to_gte (Union[Unset, int]):
        related_to_in (Union[Unset, list[int]]):
        related_to_isnull (Union[Unset, bool]):
        related_to_lt (Union[Unset, int]):
        related_to_lte (Union[Unset, int]):
        related_to_ob_id (Union[Unset, int]):
        related_to_ob_id_in (Union[Unset, list[int]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedInstrumentPlatformPairWriteList
    """

    return (
        await asyncio_detailed(
            client=client,
            instrument=instrument,
            instrument_gt=instrument_gt,
            instrument_gte=instrument_gte,
            instrument_in=instrument_in,
            instrument_isnull=instrument_isnull,
            instrument_lt=instrument_lt,
            instrument_lte=instrument_lte,
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
            platform_gt=platform_gt,
            platform_gte=platform_gte,
            platform_in=platform_in,
            platform_isnull=platform_isnull,
            platform_lt=platform_lt,
            platform_lte=platform_lte,
            platform_ob_id=platform_ob_id,
            platform_ob_id_in=platform_ob_id_in,
            platform_uuid=platform_uuid,
            platform_uuid_in=platform_uuid_in,
            related_to=related_to,
            related_to_gt=related_to_gt,
            related_to_gte=related_to_gte,
            related_to_in=related_to_in,
            related_to_isnull=related_to_isnull,
            related_to_lt=related_to_lt,
            related_to_lte=related_to_lte,
            related_to_ob_id=related_to_ob_id,
            related_to_ob_id_in=related_to_ob_id_in,
            related_to_uuid=related_to_uuid,
            related_to_uuid_in=related_to_uuid_in,
        )
    ).parsed
