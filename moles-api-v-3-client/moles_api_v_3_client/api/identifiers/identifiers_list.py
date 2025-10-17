from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.identifiers_list_identifier_type import IdentifiersListIdentifierType
from ...models.paginated_identifier_write_list import PaginatedIdentifierWriteList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identifier_type: Union[Unset, IdentifiersListIdentifierType] = UNSET,
    identifier_type_contains: Union[Unset, str] = UNSET,
    identifier_type_endswith: Union[Unset, str] = UNSET,
    identifier_type_gt: Union[Unset, str] = UNSET,
    identifier_type_gte: Union[Unset, str] = UNSET,
    identifier_type_icontains: Union[Unset, str] = UNSET,
    identifier_type_iendswith: Union[Unset, str] = UNSET,
    identifier_type_iexact: Union[Unset, str] = UNSET,
    identifier_type_in: Union[Unset, list[str]] = UNSET,
    identifier_type_iregex: Union[Unset, str] = UNSET,
    identifier_type_isnull: Union[Unset, bool] = UNSET,
    identifier_type_istartswith: Union[Unset, str] = UNSET,
    identifier_type_lt: Union[Unset, str] = UNSET,
    identifier_type_lte: Union[Unset, str] = UNSET,
    identifier_type_range: Union[Unset, list[str]] = UNSET,
    identifier_type_regex: Union[Unset, str] = UNSET,
    identifier_type_startswith: Union[Unset, str] = UNSET,
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
    short_url: Union[Unset, str] = UNSET,
    short_url_contains: Union[Unset, str] = UNSET,
    short_url_endswith: Union[Unset, str] = UNSET,
    short_url_gt: Union[Unset, str] = UNSET,
    short_url_gte: Union[Unset, str] = UNSET,
    short_url_icontains: Union[Unset, str] = UNSET,
    short_url_iendswith: Union[Unset, str] = UNSET,
    short_url_iexact: Union[Unset, str] = UNSET,
    short_url_in: Union[Unset, list[str]] = UNSET,
    short_url_iregex: Union[Unset, str] = UNSET,
    short_url_isnull: Union[Unset, bool] = UNSET,
    short_url_istartswith: Union[Unset, str] = UNSET,
    short_url_lt: Union[Unset, str] = UNSET,
    short_url_lte: Union[Unset, str] = UNSET,
    short_url_range: Union[Unset, list[str]] = UNSET,
    short_url_regex: Union[Unset, str] = UNSET,
    short_url_startswith: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    url_contains: Union[Unset, str] = UNSET,
    url_endswith: Union[Unset, str] = UNSET,
    url_gt: Union[Unset, str] = UNSET,
    url_gte: Union[Unset, str] = UNSET,
    url_icontains: Union[Unset, str] = UNSET,
    url_iendswith: Union[Unset, str] = UNSET,
    url_iexact: Union[Unset, str] = UNSET,
    url_in: Union[Unset, list[str]] = UNSET,
    url_iregex: Union[Unset, str] = UNSET,
    url_isnull: Union[Unset, bool] = UNSET,
    url_istartswith: Union[Unset, str] = UNSET,
    url_lt: Union[Unset, str] = UNSET,
    url_lte: Union[Unset, str] = UNSET,
    url_range: Union[Unset, list[str]] = UNSET,
    url_regex: Union[Unset, str] = UNSET,
    url_startswith: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(identifier_type, Unset):
        json_identifier_type = identifier_type.value

    params["identifierType"] = json_identifier_type

    params["identifierType__contains"] = identifier_type_contains

    params["identifierType__endswith"] = identifier_type_endswith

    params["identifierType__gt"] = identifier_type_gt

    params["identifierType__gte"] = identifier_type_gte

    params["identifierType__icontains"] = identifier_type_icontains

    params["identifierType__iendswith"] = identifier_type_iendswith

    params["identifierType__iexact"] = identifier_type_iexact

    json_identifier_type_in: Union[Unset, list[str]] = UNSET
    if not isinstance(identifier_type_in, Unset):
        json_identifier_type_in = identifier_type_in

    params["identifierType__in"] = json_identifier_type_in

    params["identifierType__iregex"] = identifier_type_iregex

    params["identifierType__isnull"] = identifier_type_isnull

    params["identifierType__istartswith"] = identifier_type_istartswith

    params["identifierType__lt"] = identifier_type_lt

    params["identifierType__lte"] = identifier_type_lte

    json_identifier_type_range: Union[Unset, list[str]] = UNSET
    if not isinstance(identifier_type_range, Unset):
        json_identifier_type_range = identifier_type_range

    params["identifierType__range"] = json_identifier_type_range

    params["identifierType__regex"] = identifier_type_regex

    params["identifierType__startswith"] = identifier_type_startswith

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

    params["shortUrl"] = short_url

    params["shortUrl__contains"] = short_url_contains

    params["shortUrl__endswith"] = short_url_endswith

    params["shortUrl__gt"] = short_url_gt

    params["shortUrl__gte"] = short_url_gte

    params["shortUrl__icontains"] = short_url_icontains

    params["shortUrl__iendswith"] = short_url_iendswith

    params["shortUrl__iexact"] = short_url_iexact

    json_short_url_in: Union[Unset, list[str]] = UNSET
    if not isinstance(short_url_in, Unset):
        json_short_url_in = short_url_in

    params["shortUrl__in"] = json_short_url_in

    params["shortUrl__iregex"] = short_url_iregex

    params["shortUrl__isnull"] = short_url_isnull

    params["shortUrl__istartswith"] = short_url_istartswith

    params["shortUrl__lt"] = short_url_lt

    params["shortUrl__lte"] = short_url_lte

    json_short_url_range: Union[Unset, list[str]] = UNSET
    if not isinstance(short_url_range, Unset):
        json_short_url_range = short_url_range

    params["shortUrl__range"] = json_short_url_range

    params["shortUrl__regex"] = short_url_regex

    params["shortUrl__startswith"] = short_url_startswith

    params["url"] = url_query

    params["url__contains"] = url_contains

    params["url__endswith"] = url_endswith

    params["url__gt"] = url_gt

    params["url__gte"] = url_gte

    params["url__icontains"] = url_icontains

    params["url__iendswith"] = url_iendswith

    params["url__iexact"] = url_iexact

    json_url_in: Union[Unset, list[str]] = UNSET
    if not isinstance(url_in, Unset):
        json_url_in = url_in

    params["url__in"] = json_url_in

    params["url__iregex"] = url_iregex

    params["url__isnull"] = url_isnull

    params["url__istartswith"] = url_istartswith

    params["url__lt"] = url_lt

    params["url__lte"] = url_lte

    json_url_range: Union[Unset, list[str]] = UNSET
    if not isinstance(url_range, Unset):
        json_url_range = url_range

    params["url__range"] = json_url_range

    params["url__regex"] = url_regex

    params["url__startswith"] = url_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/identifiers/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedIdentifierWriteList]:
    if response.status_code == 200:
        response_200 = PaginatedIdentifierWriteList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedIdentifierWriteList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    identifier_type: Union[Unset, IdentifiersListIdentifierType] = UNSET,
    identifier_type_contains: Union[Unset, str] = UNSET,
    identifier_type_endswith: Union[Unset, str] = UNSET,
    identifier_type_gt: Union[Unset, str] = UNSET,
    identifier_type_gte: Union[Unset, str] = UNSET,
    identifier_type_icontains: Union[Unset, str] = UNSET,
    identifier_type_iendswith: Union[Unset, str] = UNSET,
    identifier_type_iexact: Union[Unset, str] = UNSET,
    identifier_type_in: Union[Unset, list[str]] = UNSET,
    identifier_type_iregex: Union[Unset, str] = UNSET,
    identifier_type_isnull: Union[Unset, bool] = UNSET,
    identifier_type_istartswith: Union[Unset, str] = UNSET,
    identifier_type_lt: Union[Unset, str] = UNSET,
    identifier_type_lte: Union[Unset, str] = UNSET,
    identifier_type_range: Union[Unset, list[str]] = UNSET,
    identifier_type_regex: Union[Unset, str] = UNSET,
    identifier_type_startswith: Union[Unset, str] = UNSET,
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
    short_url: Union[Unset, str] = UNSET,
    short_url_contains: Union[Unset, str] = UNSET,
    short_url_endswith: Union[Unset, str] = UNSET,
    short_url_gt: Union[Unset, str] = UNSET,
    short_url_gte: Union[Unset, str] = UNSET,
    short_url_icontains: Union[Unset, str] = UNSET,
    short_url_iendswith: Union[Unset, str] = UNSET,
    short_url_iexact: Union[Unset, str] = UNSET,
    short_url_in: Union[Unset, list[str]] = UNSET,
    short_url_iregex: Union[Unset, str] = UNSET,
    short_url_isnull: Union[Unset, bool] = UNSET,
    short_url_istartswith: Union[Unset, str] = UNSET,
    short_url_lt: Union[Unset, str] = UNSET,
    short_url_lte: Union[Unset, str] = UNSET,
    short_url_range: Union[Unset, list[str]] = UNSET,
    short_url_regex: Union[Unset, str] = UNSET,
    short_url_startswith: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    url_contains: Union[Unset, str] = UNSET,
    url_endswith: Union[Unset, str] = UNSET,
    url_gt: Union[Unset, str] = UNSET,
    url_gte: Union[Unset, str] = UNSET,
    url_icontains: Union[Unset, str] = UNSET,
    url_iendswith: Union[Unset, str] = UNSET,
    url_iexact: Union[Unset, str] = UNSET,
    url_in: Union[Unset, list[str]] = UNSET,
    url_iregex: Union[Unset, str] = UNSET,
    url_isnull: Union[Unset, bool] = UNSET,
    url_istartswith: Union[Unset, str] = UNSET,
    url_lt: Union[Unset, str] = UNSET,
    url_lte: Union[Unset, str] = UNSET,
    url_range: Union[Unset, list[str]] = UNSET,
    url_regex: Union[Unset, str] = UNSET,
    url_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedIdentifierWriteList]:
    """Get a list of Identifier objects. Idenfifiers have a 1..*:1 mapping with Observations.

    Args:
        identifier_type (Union[Unset, IdentifiersListIdentifierType]):
        identifier_type_contains (Union[Unset, str]):
        identifier_type_endswith (Union[Unset, str]):
        identifier_type_gt (Union[Unset, str]):
        identifier_type_gte (Union[Unset, str]):
        identifier_type_icontains (Union[Unset, str]):
        identifier_type_iendswith (Union[Unset, str]):
        identifier_type_iexact (Union[Unset, str]):
        identifier_type_in (Union[Unset, list[str]]):
        identifier_type_iregex (Union[Unset, str]):
        identifier_type_isnull (Union[Unset, bool]):
        identifier_type_istartswith (Union[Unset, str]):
        identifier_type_lt (Union[Unset, str]):
        identifier_type_lte (Union[Unset, str]):
        identifier_type_range (Union[Unset, list[str]]):
        identifier_type_regex (Union[Unset, str]):
        identifier_type_startswith (Union[Unset, str]):
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
        short_url (Union[Unset, str]):
        short_url_contains (Union[Unset, str]):
        short_url_endswith (Union[Unset, str]):
        short_url_gt (Union[Unset, str]):
        short_url_gte (Union[Unset, str]):
        short_url_icontains (Union[Unset, str]):
        short_url_iendswith (Union[Unset, str]):
        short_url_iexact (Union[Unset, str]):
        short_url_in (Union[Unset, list[str]]):
        short_url_iregex (Union[Unset, str]):
        short_url_isnull (Union[Unset, bool]):
        short_url_istartswith (Union[Unset, str]):
        short_url_lt (Union[Unset, str]):
        short_url_lte (Union[Unset, str]):
        short_url_range (Union[Unset, list[str]]):
        short_url_regex (Union[Unset, str]):
        short_url_startswith (Union[Unset, str]):
        url_query (Union[Unset, str]):
        url_contains (Union[Unset, str]):
        url_endswith (Union[Unset, str]):
        url_gt (Union[Unset, str]):
        url_gte (Union[Unset, str]):
        url_icontains (Union[Unset, str]):
        url_iendswith (Union[Unset, str]):
        url_iexact (Union[Unset, str]):
        url_in (Union[Unset, list[str]]):
        url_iregex (Union[Unset, str]):
        url_isnull (Union[Unset, bool]):
        url_istartswith (Union[Unset, str]):
        url_lt (Union[Unset, str]):
        url_lte (Union[Unset, str]):
        url_range (Union[Unset, list[str]]):
        url_regex (Union[Unset, str]):
        url_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIdentifierWriteList]
    """

    kwargs = _get_kwargs(
        identifier_type=identifier_type,
        identifier_type_contains=identifier_type_contains,
        identifier_type_endswith=identifier_type_endswith,
        identifier_type_gt=identifier_type_gt,
        identifier_type_gte=identifier_type_gte,
        identifier_type_icontains=identifier_type_icontains,
        identifier_type_iendswith=identifier_type_iendswith,
        identifier_type_iexact=identifier_type_iexact,
        identifier_type_in=identifier_type_in,
        identifier_type_iregex=identifier_type_iregex,
        identifier_type_isnull=identifier_type_isnull,
        identifier_type_istartswith=identifier_type_istartswith,
        identifier_type_lt=identifier_type_lt,
        identifier_type_lte=identifier_type_lte,
        identifier_type_range=identifier_type_range,
        identifier_type_regex=identifier_type_regex,
        identifier_type_startswith=identifier_type_startswith,
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
        short_url=short_url,
        short_url_contains=short_url_contains,
        short_url_endswith=short_url_endswith,
        short_url_gt=short_url_gt,
        short_url_gte=short_url_gte,
        short_url_icontains=short_url_icontains,
        short_url_iendswith=short_url_iendswith,
        short_url_iexact=short_url_iexact,
        short_url_in=short_url_in,
        short_url_iregex=short_url_iregex,
        short_url_isnull=short_url_isnull,
        short_url_istartswith=short_url_istartswith,
        short_url_lt=short_url_lt,
        short_url_lte=short_url_lte,
        short_url_range=short_url_range,
        short_url_regex=short_url_regex,
        short_url_startswith=short_url_startswith,
        url_query=url_query,
        url_contains=url_contains,
        url_endswith=url_endswith,
        url_gt=url_gt,
        url_gte=url_gte,
        url_icontains=url_icontains,
        url_iendswith=url_iendswith,
        url_iexact=url_iexact,
        url_in=url_in,
        url_iregex=url_iregex,
        url_isnull=url_isnull,
        url_istartswith=url_istartswith,
        url_lt=url_lt,
        url_lte=url_lte,
        url_range=url_range,
        url_regex=url_regex,
        url_startswith=url_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    identifier_type: Union[Unset, IdentifiersListIdentifierType] = UNSET,
    identifier_type_contains: Union[Unset, str] = UNSET,
    identifier_type_endswith: Union[Unset, str] = UNSET,
    identifier_type_gt: Union[Unset, str] = UNSET,
    identifier_type_gte: Union[Unset, str] = UNSET,
    identifier_type_icontains: Union[Unset, str] = UNSET,
    identifier_type_iendswith: Union[Unset, str] = UNSET,
    identifier_type_iexact: Union[Unset, str] = UNSET,
    identifier_type_in: Union[Unset, list[str]] = UNSET,
    identifier_type_iregex: Union[Unset, str] = UNSET,
    identifier_type_isnull: Union[Unset, bool] = UNSET,
    identifier_type_istartswith: Union[Unset, str] = UNSET,
    identifier_type_lt: Union[Unset, str] = UNSET,
    identifier_type_lte: Union[Unset, str] = UNSET,
    identifier_type_range: Union[Unset, list[str]] = UNSET,
    identifier_type_regex: Union[Unset, str] = UNSET,
    identifier_type_startswith: Union[Unset, str] = UNSET,
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
    short_url: Union[Unset, str] = UNSET,
    short_url_contains: Union[Unset, str] = UNSET,
    short_url_endswith: Union[Unset, str] = UNSET,
    short_url_gt: Union[Unset, str] = UNSET,
    short_url_gte: Union[Unset, str] = UNSET,
    short_url_icontains: Union[Unset, str] = UNSET,
    short_url_iendswith: Union[Unset, str] = UNSET,
    short_url_iexact: Union[Unset, str] = UNSET,
    short_url_in: Union[Unset, list[str]] = UNSET,
    short_url_iregex: Union[Unset, str] = UNSET,
    short_url_isnull: Union[Unset, bool] = UNSET,
    short_url_istartswith: Union[Unset, str] = UNSET,
    short_url_lt: Union[Unset, str] = UNSET,
    short_url_lte: Union[Unset, str] = UNSET,
    short_url_range: Union[Unset, list[str]] = UNSET,
    short_url_regex: Union[Unset, str] = UNSET,
    short_url_startswith: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    url_contains: Union[Unset, str] = UNSET,
    url_endswith: Union[Unset, str] = UNSET,
    url_gt: Union[Unset, str] = UNSET,
    url_gte: Union[Unset, str] = UNSET,
    url_icontains: Union[Unset, str] = UNSET,
    url_iendswith: Union[Unset, str] = UNSET,
    url_iexact: Union[Unset, str] = UNSET,
    url_in: Union[Unset, list[str]] = UNSET,
    url_iregex: Union[Unset, str] = UNSET,
    url_isnull: Union[Unset, bool] = UNSET,
    url_istartswith: Union[Unset, str] = UNSET,
    url_lt: Union[Unset, str] = UNSET,
    url_lte: Union[Unset, str] = UNSET,
    url_range: Union[Unset, list[str]] = UNSET,
    url_regex: Union[Unset, str] = UNSET,
    url_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedIdentifierWriteList]:
    """Get a list of Identifier objects. Idenfifiers have a 1..*:1 mapping with Observations.

    Args:
        identifier_type (Union[Unset, IdentifiersListIdentifierType]):
        identifier_type_contains (Union[Unset, str]):
        identifier_type_endswith (Union[Unset, str]):
        identifier_type_gt (Union[Unset, str]):
        identifier_type_gte (Union[Unset, str]):
        identifier_type_icontains (Union[Unset, str]):
        identifier_type_iendswith (Union[Unset, str]):
        identifier_type_iexact (Union[Unset, str]):
        identifier_type_in (Union[Unset, list[str]]):
        identifier_type_iregex (Union[Unset, str]):
        identifier_type_isnull (Union[Unset, bool]):
        identifier_type_istartswith (Union[Unset, str]):
        identifier_type_lt (Union[Unset, str]):
        identifier_type_lte (Union[Unset, str]):
        identifier_type_range (Union[Unset, list[str]]):
        identifier_type_regex (Union[Unset, str]):
        identifier_type_startswith (Union[Unset, str]):
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
        short_url (Union[Unset, str]):
        short_url_contains (Union[Unset, str]):
        short_url_endswith (Union[Unset, str]):
        short_url_gt (Union[Unset, str]):
        short_url_gte (Union[Unset, str]):
        short_url_icontains (Union[Unset, str]):
        short_url_iendswith (Union[Unset, str]):
        short_url_iexact (Union[Unset, str]):
        short_url_in (Union[Unset, list[str]]):
        short_url_iregex (Union[Unset, str]):
        short_url_isnull (Union[Unset, bool]):
        short_url_istartswith (Union[Unset, str]):
        short_url_lt (Union[Unset, str]):
        short_url_lte (Union[Unset, str]):
        short_url_range (Union[Unset, list[str]]):
        short_url_regex (Union[Unset, str]):
        short_url_startswith (Union[Unset, str]):
        url_query (Union[Unset, str]):
        url_contains (Union[Unset, str]):
        url_endswith (Union[Unset, str]):
        url_gt (Union[Unset, str]):
        url_gte (Union[Unset, str]):
        url_icontains (Union[Unset, str]):
        url_iendswith (Union[Unset, str]):
        url_iexact (Union[Unset, str]):
        url_in (Union[Unset, list[str]]):
        url_iregex (Union[Unset, str]):
        url_isnull (Union[Unset, bool]):
        url_istartswith (Union[Unset, str]):
        url_lt (Union[Unset, str]):
        url_lte (Union[Unset, str]):
        url_range (Union[Unset, list[str]]):
        url_regex (Union[Unset, str]):
        url_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIdentifierWriteList
    """

    return sync_detailed(
        client=client,
        identifier_type=identifier_type,
        identifier_type_contains=identifier_type_contains,
        identifier_type_endswith=identifier_type_endswith,
        identifier_type_gt=identifier_type_gt,
        identifier_type_gte=identifier_type_gte,
        identifier_type_icontains=identifier_type_icontains,
        identifier_type_iendswith=identifier_type_iendswith,
        identifier_type_iexact=identifier_type_iexact,
        identifier_type_in=identifier_type_in,
        identifier_type_iregex=identifier_type_iregex,
        identifier_type_isnull=identifier_type_isnull,
        identifier_type_istartswith=identifier_type_istartswith,
        identifier_type_lt=identifier_type_lt,
        identifier_type_lte=identifier_type_lte,
        identifier_type_range=identifier_type_range,
        identifier_type_regex=identifier_type_regex,
        identifier_type_startswith=identifier_type_startswith,
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
        short_url=short_url,
        short_url_contains=short_url_contains,
        short_url_endswith=short_url_endswith,
        short_url_gt=short_url_gt,
        short_url_gte=short_url_gte,
        short_url_icontains=short_url_icontains,
        short_url_iendswith=short_url_iendswith,
        short_url_iexact=short_url_iexact,
        short_url_in=short_url_in,
        short_url_iregex=short_url_iregex,
        short_url_isnull=short_url_isnull,
        short_url_istartswith=short_url_istartswith,
        short_url_lt=short_url_lt,
        short_url_lte=short_url_lte,
        short_url_range=short_url_range,
        short_url_regex=short_url_regex,
        short_url_startswith=short_url_startswith,
        url_query=url_query,
        url_contains=url_contains,
        url_endswith=url_endswith,
        url_gt=url_gt,
        url_gte=url_gte,
        url_icontains=url_icontains,
        url_iendswith=url_iendswith,
        url_iexact=url_iexact,
        url_in=url_in,
        url_iregex=url_iregex,
        url_isnull=url_isnull,
        url_istartswith=url_istartswith,
        url_lt=url_lt,
        url_lte=url_lte,
        url_range=url_range,
        url_regex=url_regex,
        url_startswith=url_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    identifier_type: Union[Unset, IdentifiersListIdentifierType] = UNSET,
    identifier_type_contains: Union[Unset, str] = UNSET,
    identifier_type_endswith: Union[Unset, str] = UNSET,
    identifier_type_gt: Union[Unset, str] = UNSET,
    identifier_type_gte: Union[Unset, str] = UNSET,
    identifier_type_icontains: Union[Unset, str] = UNSET,
    identifier_type_iendswith: Union[Unset, str] = UNSET,
    identifier_type_iexact: Union[Unset, str] = UNSET,
    identifier_type_in: Union[Unset, list[str]] = UNSET,
    identifier_type_iregex: Union[Unset, str] = UNSET,
    identifier_type_isnull: Union[Unset, bool] = UNSET,
    identifier_type_istartswith: Union[Unset, str] = UNSET,
    identifier_type_lt: Union[Unset, str] = UNSET,
    identifier_type_lte: Union[Unset, str] = UNSET,
    identifier_type_range: Union[Unset, list[str]] = UNSET,
    identifier_type_regex: Union[Unset, str] = UNSET,
    identifier_type_startswith: Union[Unset, str] = UNSET,
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
    short_url: Union[Unset, str] = UNSET,
    short_url_contains: Union[Unset, str] = UNSET,
    short_url_endswith: Union[Unset, str] = UNSET,
    short_url_gt: Union[Unset, str] = UNSET,
    short_url_gte: Union[Unset, str] = UNSET,
    short_url_icontains: Union[Unset, str] = UNSET,
    short_url_iendswith: Union[Unset, str] = UNSET,
    short_url_iexact: Union[Unset, str] = UNSET,
    short_url_in: Union[Unset, list[str]] = UNSET,
    short_url_iregex: Union[Unset, str] = UNSET,
    short_url_isnull: Union[Unset, bool] = UNSET,
    short_url_istartswith: Union[Unset, str] = UNSET,
    short_url_lt: Union[Unset, str] = UNSET,
    short_url_lte: Union[Unset, str] = UNSET,
    short_url_range: Union[Unset, list[str]] = UNSET,
    short_url_regex: Union[Unset, str] = UNSET,
    short_url_startswith: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    url_contains: Union[Unset, str] = UNSET,
    url_endswith: Union[Unset, str] = UNSET,
    url_gt: Union[Unset, str] = UNSET,
    url_gte: Union[Unset, str] = UNSET,
    url_icontains: Union[Unset, str] = UNSET,
    url_iendswith: Union[Unset, str] = UNSET,
    url_iexact: Union[Unset, str] = UNSET,
    url_in: Union[Unset, list[str]] = UNSET,
    url_iregex: Union[Unset, str] = UNSET,
    url_isnull: Union[Unset, bool] = UNSET,
    url_istartswith: Union[Unset, str] = UNSET,
    url_lt: Union[Unset, str] = UNSET,
    url_lte: Union[Unset, str] = UNSET,
    url_range: Union[Unset, list[str]] = UNSET,
    url_regex: Union[Unset, str] = UNSET,
    url_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedIdentifierWriteList]:
    """Get a list of Identifier objects. Idenfifiers have a 1..*:1 mapping with Observations.

    Args:
        identifier_type (Union[Unset, IdentifiersListIdentifierType]):
        identifier_type_contains (Union[Unset, str]):
        identifier_type_endswith (Union[Unset, str]):
        identifier_type_gt (Union[Unset, str]):
        identifier_type_gte (Union[Unset, str]):
        identifier_type_icontains (Union[Unset, str]):
        identifier_type_iendswith (Union[Unset, str]):
        identifier_type_iexact (Union[Unset, str]):
        identifier_type_in (Union[Unset, list[str]]):
        identifier_type_iregex (Union[Unset, str]):
        identifier_type_isnull (Union[Unset, bool]):
        identifier_type_istartswith (Union[Unset, str]):
        identifier_type_lt (Union[Unset, str]):
        identifier_type_lte (Union[Unset, str]):
        identifier_type_range (Union[Unset, list[str]]):
        identifier_type_regex (Union[Unset, str]):
        identifier_type_startswith (Union[Unset, str]):
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
        short_url (Union[Unset, str]):
        short_url_contains (Union[Unset, str]):
        short_url_endswith (Union[Unset, str]):
        short_url_gt (Union[Unset, str]):
        short_url_gte (Union[Unset, str]):
        short_url_icontains (Union[Unset, str]):
        short_url_iendswith (Union[Unset, str]):
        short_url_iexact (Union[Unset, str]):
        short_url_in (Union[Unset, list[str]]):
        short_url_iregex (Union[Unset, str]):
        short_url_isnull (Union[Unset, bool]):
        short_url_istartswith (Union[Unset, str]):
        short_url_lt (Union[Unset, str]):
        short_url_lte (Union[Unset, str]):
        short_url_range (Union[Unset, list[str]]):
        short_url_regex (Union[Unset, str]):
        short_url_startswith (Union[Unset, str]):
        url_query (Union[Unset, str]):
        url_contains (Union[Unset, str]):
        url_endswith (Union[Unset, str]):
        url_gt (Union[Unset, str]):
        url_gte (Union[Unset, str]):
        url_icontains (Union[Unset, str]):
        url_iendswith (Union[Unset, str]):
        url_iexact (Union[Unset, str]):
        url_in (Union[Unset, list[str]]):
        url_iregex (Union[Unset, str]):
        url_isnull (Union[Unset, bool]):
        url_istartswith (Union[Unset, str]):
        url_lt (Union[Unset, str]):
        url_lte (Union[Unset, str]):
        url_range (Union[Unset, list[str]]):
        url_regex (Union[Unset, str]):
        url_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedIdentifierWriteList]
    """

    kwargs = _get_kwargs(
        identifier_type=identifier_type,
        identifier_type_contains=identifier_type_contains,
        identifier_type_endswith=identifier_type_endswith,
        identifier_type_gt=identifier_type_gt,
        identifier_type_gte=identifier_type_gte,
        identifier_type_icontains=identifier_type_icontains,
        identifier_type_iendswith=identifier_type_iendswith,
        identifier_type_iexact=identifier_type_iexact,
        identifier_type_in=identifier_type_in,
        identifier_type_iregex=identifier_type_iregex,
        identifier_type_isnull=identifier_type_isnull,
        identifier_type_istartswith=identifier_type_istartswith,
        identifier_type_lt=identifier_type_lt,
        identifier_type_lte=identifier_type_lte,
        identifier_type_range=identifier_type_range,
        identifier_type_regex=identifier_type_regex,
        identifier_type_startswith=identifier_type_startswith,
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
        short_url=short_url,
        short_url_contains=short_url_contains,
        short_url_endswith=short_url_endswith,
        short_url_gt=short_url_gt,
        short_url_gte=short_url_gte,
        short_url_icontains=short_url_icontains,
        short_url_iendswith=short_url_iendswith,
        short_url_iexact=short_url_iexact,
        short_url_in=short_url_in,
        short_url_iregex=short_url_iregex,
        short_url_isnull=short_url_isnull,
        short_url_istartswith=short_url_istartswith,
        short_url_lt=short_url_lt,
        short_url_lte=short_url_lte,
        short_url_range=short_url_range,
        short_url_regex=short_url_regex,
        short_url_startswith=short_url_startswith,
        url_query=url_query,
        url_contains=url_contains,
        url_endswith=url_endswith,
        url_gt=url_gt,
        url_gte=url_gte,
        url_icontains=url_icontains,
        url_iendswith=url_iendswith,
        url_iexact=url_iexact,
        url_in=url_in,
        url_iregex=url_iregex,
        url_isnull=url_isnull,
        url_istartswith=url_istartswith,
        url_lt=url_lt,
        url_lte=url_lte,
        url_range=url_range,
        url_regex=url_regex,
        url_startswith=url_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    identifier_type: Union[Unset, IdentifiersListIdentifierType] = UNSET,
    identifier_type_contains: Union[Unset, str] = UNSET,
    identifier_type_endswith: Union[Unset, str] = UNSET,
    identifier_type_gt: Union[Unset, str] = UNSET,
    identifier_type_gte: Union[Unset, str] = UNSET,
    identifier_type_icontains: Union[Unset, str] = UNSET,
    identifier_type_iendswith: Union[Unset, str] = UNSET,
    identifier_type_iexact: Union[Unset, str] = UNSET,
    identifier_type_in: Union[Unset, list[str]] = UNSET,
    identifier_type_iregex: Union[Unset, str] = UNSET,
    identifier_type_isnull: Union[Unset, bool] = UNSET,
    identifier_type_istartswith: Union[Unset, str] = UNSET,
    identifier_type_lt: Union[Unset, str] = UNSET,
    identifier_type_lte: Union[Unset, str] = UNSET,
    identifier_type_range: Union[Unset, list[str]] = UNSET,
    identifier_type_regex: Union[Unset, str] = UNSET,
    identifier_type_startswith: Union[Unset, str] = UNSET,
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
    short_url: Union[Unset, str] = UNSET,
    short_url_contains: Union[Unset, str] = UNSET,
    short_url_endswith: Union[Unset, str] = UNSET,
    short_url_gt: Union[Unset, str] = UNSET,
    short_url_gte: Union[Unset, str] = UNSET,
    short_url_icontains: Union[Unset, str] = UNSET,
    short_url_iendswith: Union[Unset, str] = UNSET,
    short_url_iexact: Union[Unset, str] = UNSET,
    short_url_in: Union[Unset, list[str]] = UNSET,
    short_url_iregex: Union[Unset, str] = UNSET,
    short_url_isnull: Union[Unset, bool] = UNSET,
    short_url_istartswith: Union[Unset, str] = UNSET,
    short_url_lt: Union[Unset, str] = UNSET,
    short_url_lte: Union[Unset, str] = UNSET,
    short_url_range: Union[Unset, list[str]] = UNSET,
    short_url_regex: Union[Unset, str] = UNSET,
    short_url_startswith: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    url_contains: Union[Unset, str] = UNSET,
    url_endswith: Union[Unset, str] = UNSET,
    url_gt: Union[Unset, str] = UNSET,
    url_gte: Union[Unset, str] = UNSET,
    url_icontains: Union[Unset, str] = UNSET,
    url_iendswith: Union[Unset, str] = UNSET,
    url_iexact: Union[Unset, str] = UNSET,
    url_in: Union[Unset, list[str]] = UNSET,
    url_iregex: Union[Unset, str] = UNSET,
    url_isnull: Union[Unset, bool] = UNSET,
    url_istartswith: Union[Unset, str] = UNSET,
    url_lt: Union[Unset, str] = UNSET,
    url_lte: Union[Unset, str] = UNSET,
    url_range: Union[Unset, list[str]] = UNSET,
    url_regex: Union[Unset, str] = UNSET,
    url_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedIdentifierWriteList]:
    """Get a list of Identifier objects. Idenfifiers have a 1..*:1 mapping with Observations.

    Args:
        identifier_type (Union[Unset, IdentifiersListIdentifierType]):
        identifier_type_contains (Union[Unset, str]):
        identifier_type_endswith (Union[Unset, str]):
        identifier_type_gt (Union[Unset, str]):
        identifier_type_gte (Union[Unset, str]):
        identifier_type_icontains (Union[Unset, str]):
        identifier_type_iendswith (Union[Unset, str]):
        identifier_type_iexact (Union[Unset, str]):
        identifier_type_in (Union[Unset, list[str]]):
        identifier_type_iregex (Union[Unset, str]):
        identifier_type_isnull (Union[Unset, bool]):
        identifier_type_istartswith (Union[Unset, str]):
        identifier_type_lt (Union[Unset, str]):
        identifier_type_lte (Union[Unset, str]):
        identifier_type_range (Union[Unset, list[str]]):
        identifier_type_regex (Union[Unset, str]):
        identifier_type_startswith (Union[Unset, str]):
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
        short_url (Union[Unset, str]):
        short_url_contains (Union[Unset, str]):
        short_url_endswith (Union[Unset, str]):
        short_url_gt (Union[Unset, str]):
        short_url_gte (Union[Unset, str]):
        short_url_icontains (Union[Unset, str]):
        short_url_iendswith (Union[Unset, str]):
        short_url_iexact (Union[Unset, str]):
        short_url_in (Union[Unset, list[str]]):
        short_url_iregex (Union[Unset, str]):
        short_url_isnull (Union[Unset, bool]):
        short_url_istartswith (Union[Unset, str]):
        short_url_lt (Union[Unset, str]):
        short_url_lte (Union[Unset, str]):
        short_url_range (Union[Unset, list[str]]):
        short_url_regex (Union[Unset, str]):
        short_url_startswith (Union[Unset, str]):
        url_query (Union[Unset, str]):
        url_contains (Union[Unset, str]):
        url_endswith (Union[Unset, str]):
        url_gt (Union[Unset, str]):
        url_gte (Union[Unset, str]):
        url_icontains (Union[Unset, str]):
        url_iendswith (Union[Unset, str]):
        url_iexact (Union[Unset, str]):
        url_in (Union[Unset, list[str]]):
        url_iregex (Union[Unset, str]):
        url_isnull (Union[Unset, bool]):
        url_istartswith (Union[Unset, str]):
        url_lt (Union[Unset, str]):
        url_lte (Union[Unset, str]):
        url_range (Union[Unset, list[str]]):
        url_regex (Union[Unset, str]):
        url_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedIdentifierWriteList
    """

    return (
        await asyncio_detailed(
            client=client,
            identifier_type=identifier_type,
            identifier_type_contains=identifier_type_contains,
            identifier_type_endswith=identifier_type_endswith,
            identifier_type_gt=identifier_type_gt,
            identifier_type_gte=identifier_type_gte,
            identifier_type_icontains=identifier_type_icontains,
            identifier_type_iendswith=identifier_type_iendswith,
            identifier_type_iexact=identifier_type_iexact,
            identifier_type_in=identifier_type_in,
            identifier_type_iregex=identifier_type_iregex,
            identifier_type_isnull=identifier_type_isnull,
            identifier_type_istartswith=identifier_type_istartswith,
            identifier_type_lt=identifier_type_lt,
            identifier_type_lte=identifier_type_lte,
            identifier_type_range=identifier_type_range,
            identifier_type_regex=identifier_type_regex,
            identifier_type_startswith=identifier_type_startswith,
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
            short_url=short_url,
            short_url_contains=short_url_contains,
            short_url_endswith=short_url_endswith,
            short_url_gt=short_url_gt,
            short_url_gte=short_url_gte,
            short_url_icontains=short_url_icontains,
            short_url_iendswith=short_url_iendswith,
            short_url_iexact=short_url_iexact,
            short_url_in=short_url_in,
            short_url_iregex=short_url_iregex,
            short_url_isnull=short_url_isnull,
            short_url_istartswith=short_url_istartswith,
            short_url_lt=short_url_lt,
            short_url_lte=short_url_lte,
            short_url_range=short_url_range,
            short_url_regex=short_url_regex,
            short_url_startswith=short_url_startswith,
            url_query=url_query,
            url_contains=url_contains,
            url_endswith=url_endswith,
            url_gt=url_gt,
            url_gte=url_gte,
            url_icontains=url_icontains,
            url_iendswith=url_iendswith,
            url_iexact=url_iexact,
            url_in=url_in,
            url_iregex=url_iregex,
            url_isnull=url_isnull,
            url_istartswith=url_istartswith,
            url_lt=url_lt,
            url_lte=url_lte,
            url_range=url_range,
            url_regex=url_regex,
            url_startswith=url_startswith,
        )
    ).parsed
