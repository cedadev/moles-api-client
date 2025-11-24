from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_referenceable_list import PaginatedReferenceableList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
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
        "url": "/api/v3/referenceables/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedReferenceableList | None:
    if response.status_code == 200:
        response_200 = PaginatedReferenceableList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedReferenceableList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
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
) -> Response[PaginatedReferenceableList]:
    """Get a list of Referenceable objects. This is the base class for the main record types in the CEDA
    data catalogue.

    Args:
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
        Response[PaginatedReferenceableList]
    """

    kwargs = _get_kwargs(
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
) -> PaginatedReferenceableList | None:
    """Get a list of Referenceable objects. This is the base class for the main record types in the CEDA
    data catalogue.

    Args:
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
        PaginatedReferenceableList
    """

    return sync_detailed(
        client=client,
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
) -> Response[PaginatedReferenceableList]:
    """Get a list of Referenceable objects. This is the base class for the main record types in the CEDA
    data catalogue.

    Args:
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
        Response[PaginatedReferenceableList]
    """

    kwargs = _get_kwargs(
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
) -> PaginatedReferenceableList | None:
    """Get a list of Referenceable objects. This is the base class for the main record types in the CEDA
    data catalogue.

    Args:
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
        PaginatedReferenceableList
    """

    return (
        await asyncio_detailed(
            client=client,
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
