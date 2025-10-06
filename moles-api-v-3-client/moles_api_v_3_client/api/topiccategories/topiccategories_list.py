from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_topic_category_write_list import PaginatedTopicCategoryWriteList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    name_endswith: Union[Unset, str] = UNSET,
    name_gt: Union[Unset, str] = UNSET,
    name_gte: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    name_iendswith: Union[Unset, str] = UNSET,
    name_iexact: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    name_iregex: Union[Unset, str] = UNSET,
    name_isnull: Union[Unset, bool] = UNSET,
    name_istartswith: Union[Unset, str] = UNSET,
    name_lt: Union[Unset, str] = UNSET,
    name_lte: Union[Unset, str] = UNSET,
    name_range: Union[Unset, list[str]] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    name_startswith: Union[Unset, str] = UNSET,
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
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["name"] = name

    params["name__contains"] = name_contains

    params["name__endswith"] = name_endswith

    params["name__gt"] = name_gt

    params["name__gte"] = name_gte

    params["name__icontains"] = name_icontains

    params["name__iendswith"] = name_iendswith

    params["name__iexact"] = name_iexact

    json_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(name_in, Unset):
        json_name_in = name_in

    params["name__in"] = json_name_in

    params["name__iregex"] = name_iregex

    params["name__isnull"] = name_isnull

    params["name__istartswith"] = name_istartswith

    params["name__lt"] = name_lt

    params["name__lte"] = name_lte

    json_name_range: Union[Unset, list[str]] = UNSET
    if not isinstance(name_range, Unset):
        json_name_range = name_range

    params["name__range"] = json_name_range

    params["name__regex"] = name_regex

    params["name__startswith"] = name_startswith

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/topiccategories/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedTopicCategoryWriteList]:
    if response.status_code == 200:
        response_200 = PaginatedTopicCategoryWriteList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedTopicCategoryWriteList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    name_endswith: Union[Unset, str] = UNSET,
    name_gt: Union[Unset, str] = UNSET,
    name_gte: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    name_iendswith: Union[Unset, str] = UNSET,
    name_iexact: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    name_iregex: Union[Unset, str] = UNSET,
    name_isnull: Union[Unset, bool] = UNSET,
    name_istartswith: Union[Unset, str] = UNSET,
    name_lt: Union[Unset, str] = UNSET,
    name_lte: Union[Unset, str] = UNSET,
    name_range: Union[Unset, list[str]] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    name_startswith: Union[Unset, str] = UNSET,
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
) -> Response[PaginatedTopicCategoryWriteList]:
    """Get a list of TopicCategory objects.

    Args:
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):
        name_endswith (Union[Unset, str]):
        name_gt (Union[Unset, str]):
        name_gte (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        name_iendswith (Union[Unset, str]):
        name_iexact (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        name_iregex (Union[Unset, str]):
        name_isnull (Union[Unset, bool]):
        name_istartswith (Union[Unset, str]):
        name_lt (Union[Unset, str]):
        name_lte (Union[Unset, str]):
        name_range (Union[Unset, list[str]]):
        name_regex (Union[Unset, str]):
        name_startswith (Union[Unset, str]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTopicCategoryWriteList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        name=name,
        name_contains=name_contains,
        name_endswith=name_endswith,
        name_gt=name_gt,
        name_gte=name_gte,
        name_icontains=name_icontains,
        name_iendswith=name_iendswith,
        name_iexact=name_iexact,
        name_in=name_in,
        name_iregex=name_iregex,
        name_isnull=name_isnull,
        name_istartswith=name_istartswith,
        name_lt=name_lt,
        name_lte=name_lte,
        name_range=name_range,
        name_regex=name_regex,
        name_startswith=name_startswith,
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    name_endswith: Union[Unset, str] = UNSET,
    name_gt: Union[Unset, str] = UNSET,
    name_gte: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    name_iendswith: Union[Unset, str] = UNSET,
    name_iexact: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    name_iregex: Union[Unset, str] = UNSET,
    name_isnull: Union[Unset, bool] = UNSET,
    name_istartswith: Union[Unset, str] = UNSET,
    name_lt: Union[Unset, str] = UNSET,
    name_lte: Union[Unset, str] = UNSET,
    name_range: Union[Unset, list[str]] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    name_startswith: Union[Unset, str] = UNSET,
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
) -> Optional[PaginatedTopicCategoryWriteList]:
    """Get a list of TopicCategory objects.

    Args:
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):
        name_endswith (Union[Unset, str]):
        name_gt (Union[Unset, str]):
        name_gte (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        name_iendswith (Union[Unset, str]):
        name_iexact (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        name_iregex (Union[Unset, str]):
        name_isnull (Union[Unset, bool]):
        name_istartswith (Union[Unset, str]):
        name_lt (Union[Unset, str]):
        name_lte (Union[Unset, str]):
        name_range (Union[Unset, list[str]]):
        name_regex (Union[Unset, str]):
        name_startswith (Union[Unset, str]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTopicCategoryWriteList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        name=name,
        name_contains=name_contains,
        name_endswith=name_endswith,
        name_gt=name_gt,
        name_gte=name_gte,
        name_icontains=name_icontains,
        name_iendswith=name_iendswith,
        name_iexact=name_iexact,
        name_in=name_in,
        name_iregex=name_iregex,
        name_isnull=name_isnull,
        name_istartswith=name_istartswith,
        name_lt=name_lt,
        name_lte=name_lte,
        name_range=name_range,
        name_regex=name_regex,
        name_startswith=name_startswith,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    name_endswith: Union[Unset, str] = UNSET,
    name_gt: Union[Unset, str] = UNSET,
    name_gte: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    name_iendswith: Union[Unset, str] = UNSET,
    name_iexact: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    name_iregex: Union[Unset, str] = UNSET,
    name_isnull: Union[Unset, bool] = UNSET,
    name_istartswith: Union[Unset, str] = UNSET,
    name_lt: Union[Unset, str] = UNSET,
    name_lte: Union[Unset, str] = UNSET,
    name_range: Union[Unset, list[str]] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    name_startswith: Union[Unset, str] = UNSET,
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
) -> Response[PaginatedTopicCategoryWriteList]:
    """Get a list of TopicCategory objects.

    Args:
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):
        name_endswith (Union[Unset, str]):
        name_gt (Union[Unset, str]):
        name_gte (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        name_iendswith (Union[Unset, str]):
        name_iexact (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        name_iregex (Union[Unset, str]):
        name_isnull (Union[Unset, bool]):
        name_istartswith (Union[Unset, str]):
        name_lt (Union[Unset, str]):
        name_lte (Union[Unset, str]):
        name_range (Union[Unset, list[str]]):
        name_regex (Union[Unset, str]):
        name_startswith (Union[Unset, str]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedTopicCategoryWriteList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        name=name,
        name_contains=name_contains,
        name_endswith=name_endswith,
        name_gt=name_gt,
        name_gte=name_gte,
        name_icontains=name_icontains,
        name_iendswith=name_iendswith,
        name_iexact=name_iexact,
        name_in=name_in,
        name_iregex=name_iregex,
        name_isnull=name_isnull,
        name_istartswith=name_istartswith,
        name_lt=name_lt,
        name_lte=name_lte,
        name_range=name_range,
        name_regex=name_regex,
        name_startswith=name_startswith,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    name_endswith: Union[Unset, str] = UNSET,
    name_gt: Union[Unset, str] = UNSET,
    name_gte: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    name_iendswith: Union[Unset, str] = UNSET,
    name_iexact: Union[Unset, str] = UNSET,
    name_in: Union[Unset, list[str]] = UNSET,
    name_iregex: Union[Unset, str] = UNSET,
    name_isnull: Union[Unset, bool] = UNSET,
    name_istartswith: Union[Unset, str] = UNSET,
    name_lt: Union[Unset, str] = UNSET,
    name_lte: Union[Unset, str] = UNSET,
    name_range: Union[Unset, list[str]] = UNSET,
    name_regex: Union[Unset, str] = UNSET,
    name_startswith: Union[Unset, str] = UNSET,
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
) -> Optional[PaginatedTopicCategoryWriteList]:
    """Get a list of TopicCategory objects.

    Args:
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):
        name_endswith (Union[Unset, str]):
        name_gt (Union[Unset, str]):
        name_gte (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        name_iendswith (Union[Unset, str]):
        name_iexact (Union[Unset, str]):
        name_in (Union[Unset, list[str]]):
        name_iregex (Union[Unset, str]):
        name_isnull (Union[Unset, bool]):
        name_istartswith (Union[Unset, str]):
        name_lt (Union[Unset, str]):
        name_lte (Union[Unset, str]):
        name_range (Union[Unset, list[str]]):
        name_regex (Union[Unset, str]):
        name_startswith (Union[Unset, str]):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedTopicCategoryWriteList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            name=name,
            name_contains=name_contains,
            name_endswith=name_endswith,
            name_gt=name_gt,
            name_gte=name_gte,
            name_icontains=name_icontains,
            name_iendswith=name_iendswith,
            name_iexact=name_iexact,
            name_in=name_in,
            name_iregex=name_iregex,
            name_isnull=name_isnull,
            name_istartswith=name_istartswith,
            name_lt=name_lt,
            name_lte=name_lte,
            name_range=name_range,
            name_regex=name_regex,
            name_startswith=name_startswith,
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
        )
    ).parsed
