from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_drs_dataset_read_list import PaginatedDRSDatasetReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    directory: Union[Unset, str] = UNSET,
    directory_contains: Union[Unset, str] = UNSET,
    directory_endswith: Union[Unset, str] = UNSET,
    directory_gt: Union[Unset, str] = UNSET,
    directory_gte: Union[Unset, str] = UNSET,
    directory_icontains: Union[Unset, str] = UNSET,
    directory_iendswith: Union[Unset, str] = UNSET,
    directory_iexact: Union[Unset, str] = UNSET,
    directory_in: Union[Unset, list[str]] = UNSET,
    directory_iregex: Union[Unset, str] = UNSET,
    directory_isnull: Union[Unset, bool] = UNSET,
    directory_istartswith: Union[Unset, str] = UNSET,
    directory_lt: Union[Unset, str] = UNSET,
    directory_lte: Union[Unset, str] = UNSET,
    directory_range: Union[Unset, list[str]] = UNSET,
    directory_regex: Union[Unset, str] = UNSET,
    directory_startswith: Union[Unset, str] = UNSET,
    drs_id: Union[Unset, str] = UNSET,
    drs_id_contains: Union[Unset, str] = UNSET,
    drs_id_endswith: Union[Unset, str] = UNSET,
    drs_id_gt: Union[Unset, str] = UNSET,
    drs_id_gte: Union[Unset, str] = UNSET,
    drs_id_icontains: Union[Unset, str] = UNSET,
    drs_id_iendswith: Union[Unset, str] = UNSET,
    drs_id_iexact: Union[Unset, str] = UNSET,
    drs_id_in: Union[Unset, list[str]] = UNSET,
    drs_id_iregex: Union[Unset, str] = UNSET,
    drs_id_isnull: Union[Unset, bool] = UNSET,
    drs_id_istartswith: Union[Unset, str] = UNSET,
    drs_id_lt: Union[Unset, str] = UNSET,
    drs_id_lte: Union[Unset, str] = UNSET,
    drs_id_range: Union[Unset, list[str]] = UNSET,
    drs_id_regex: Union[Unset, str] = UNSET,
    drs_id_startswith: Union[Unset, str] = UNSET,
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
    related_to_short_code: Union[Unset, str] = UNSET,
    related_to_short_code_in: Union[Unset, list[str]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
    version: Union[Unset, str] = UNSET,
    version_contains: Union[Unset, str] = UNSET,
    version_endswith: Union[Unset, str] = UNSET,
    version_gt: Union[Unset, str] = UNSET,
    version_gte: Union[Unset, str] = UNSET,
    version_icontains: Union[Unset, str] = UNSET,
    version_iendswith: Union[Unset, str] = UNSET,
    version_iexact: Union[Unset, str] = UNSET,
    version_in: Union[Unset, list[str]] = UNSET,
    version_iregex: Union[Unset, str] = UNSET,
    version_isnull: Union[Unset, bool] = UNSET,
    version_istartswith: Union[Unset, str] = UNSET,
    version_lt: Union[Unset, str] = UNSET,
    version_lte: Union[Unset, str] = UNSET,
    version_range: Union[Unset, list[str]] = UNSET,
    version_regex: Union[Unset, str] = UNSET,
    version_startswith: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["directory"] = directory

    params["directory__contains"] = directory_contains

    params["directory__endswith"] = directory_endswith

    params["directory__gt"] = directory_gt

    params["directory__gte"] = directory_gte

    params["directory__icontains"] = directory_icontains

    params["directory__iendswith"] = directory_iendswith

    params["directory__iexact"] = directory_iexact

    json_directory_in: Union[Unset, list[str]] = UNSET
    if not isinstance(directory_in, Unset):
        json_directory_in = ",".join(map(str, directory_in))

    params["directory__in"] = json_directory_in

    params["directory__iregex"] = directory_iregex

    params["directory__isnull"] = directory_isnull

    params["directory__istartswith"] = directory_istartswith

    params["directory__lt"] = directory_lt

    params["directory__lte"] = directory_lte

    json_directory_range: Union[Unset, list[str]] = UNSET
    if not isinstance(directory_range, Unset):
        json_directory_range = ",".join(map(str, directory_range))

    params["directory__range"] = json_directory_range

    params["directory__regex"] = directory_regex

    params["directory__startswith"] = directory_startswith

    params["drsId"] = drs_id

    params["drsId__contains"] = drs_id_contains

    params["drsId__endswith"] = drs_id_endswith

    params["drsId__gt"] = drs_id_gt

    params["drsId__gte"] = drs_id_gte

    params["drsId__icontains"] = drs_id_icontains

    params["drsId__iendswith"] = drs_id_iendswith

    params["drsId__iexact"] = drs_id_iexact

    json_drs_id_in: Union[Unset, list[str]] = UNSET
    if not isinstance(drs_id_in, Unset):
        json_drs_id_in = ",".join(map(str, drs_id_in))

    params["drsId__in"] = json_drs_id_in

    params["drsId__iregex"] = drs_id_iregex

    params["drsId__isnull"] = drs_id_isnull

    params["drsId__istartswith"] = drs_id_istartswith

    params["drsId__lt"] = drs_id_lt

    params["drsId__lte"] = drs_id_lte

    json_drs_id_range: Union[Unset, list[str]] = UNSET
    if not isinstance(drs_id_range, Unset):
        json_drs_id_range = ",".join(map(str, drs_id_range))

    params["drsId__range"] = json_drs_id_range

    params["drsId__regex"] = drs_id_regex

    params["drsId__startswith"] = drs_id_startswith

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
        json_ob_id_in = ",".join(map(str, ob_id_in))

    params["ob_id__in"] = json_ob_id_in

    params["ob_id__iregex"] = ob_id_iregex

    params["ob_id__isnull"] = ob_id_isnull

    params["ob_id__istartswith"] = ob_id_istartswith

    params["ob_id__lt"] = ob_id_lt

    params["ob_id__lte"] = ob_id_lte

    json_ob_id_range: Union[Unset, list[int]] = UNSET
    if not isinstance(ob_id_range, Unset):
        json_ob_id_range = ",".join(map(str, ob_id_range))

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
        json_related_to_in = ",".join(map(str, related_to_in))

    params["relatedTo__in"] = json_related_to_in

    params["relatedTo__isnull"] = related_to_isnull

    params["relatedTo__lt"] = related_to_lt

    params["relatedTo__lte"] = related_to_lte

    params["relatedTo__ob_id"] = related_to_ob_id

    json_related_to_ob_id_in: Union[Unset, list[int]] = UNSET
    if not isinstance(related_to_ob_id_in, Unset):
        json_related_to_ob_id_in = ",".join(map(str, related_to_ob_id_in))

    params["relatedTo__ob_id__in"] = json_related_to_ob_id_in

    params["relatedTo__short_code"] = related_to_short_code

    json_related_to_short_code_in: Union[Unset, list[str]] = UNSET
    if not isinstance(related_to_short_code_in, Unset):
        json_related_to_short_code_in = ",".join(map(str, related_to_short_code_in))

    params["relatedTo__short_code__in"] = json_related_to_short_code_in

    params["relatedTo__uuid"] = related_to_uuid

    json_related_to_uuid_in: Union[Unset, list[str]] = UNSET
    if not isinstance(related_to_uuid_in, Unset):
        json_related_to_uuid_in = ",".join(map(str, related_to_uuid_in))

    params["relatedTo__uuid__in"] = json_related_to_uuid_in

    params["version"] = version

    params["version__contains"] = version_contains

    params["version__endswith"] = version_endswith

    params["version__gt"] = version_gt

    params["version__gte"] = version_gte

    params["version__icontains"] = version_icontains

    params["version__iendswith"] = version_iendswith

    params["version__iexact"] = version_iexact

    json_version_in: Union[Unset, list[str]] = UNSET
    if not isinstance(version_in, Unset):
        json_version_in = ",".join(map(str, version_in))

    params["version__in"] = json_version_in

    params["version__iregex"] = version_iregex

    params["version__isnull"] = version_isnull

    params["version__istartswith"] = version_istartswith

    params["version__lt"] = version_lt

    params["version__lte"] = version_lte

    json_version_range: Union[Unset, list[str]] = UNSET
    if not isinstance(version_range, Unset):
        json_version_range = ",".join(map(str, version_range))

    params["version__range"] = json_version_range

    params["version__regex"] = version_regex

    params["version__startswith"] = version_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/drsdatasets/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedDRSDatasetReadList]:
    if response.status_code == 200:
        response_200 = PaginatedDRSDatasetReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedDRSDatasetReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    directory: Union[Unset, str] = UNSET,
    directory_contains: Union[Unset, str] = UNSET,
    directory_endswith: Union[Unset, str] = UNSET,
    directory_gt: Union[Unset, str] = UNSET,
    directory_gte: Union[Unset, str] = UNSET,
    directory_icontains: Union[Unset, str] = UNSET,
    directory_iendswith: Union[Unset, str] = UNSET,
    directory_iexact: Union[Unset, str] = UNSET,
    directory_in: Union[Unset, list[str]] = UNSET,
    directory_iregex: Union[Unset, str] = UNSET,
    directory_isnull: Union[Unset, bool] = UNSET,
    directory_istartswith: Union[Unset, str] = UNSET,
    directory_lt: Union[Unset, str] = UNSET,
    directory_lte: Union[Unset, str] = UNSET,
    directory_range: Union[Unset, list[str]] = UNSET,
    directory_regex: Union[Unset, str] = UNSET,
    directory_startswith: Union[Unset, str] = UNSET,
    drs_id: Union[Unset, str] = UNSET,
    drs_id_contains: Union[Unset, str] = UNSET,
    drs_id_endswith: Union[Unset, str] = UNSET,
    drs_id_gt: Union[Unset, str] = UNSET,
    drs_id_gte: Union[Unset, str] = UNSET,
    drs_id_icontains: Union[Unset, str] = UNSET,
    drs_id_iendswith: Union[Unset, str] = UNSET,
    drs_id_iexact: Union[Unset, str] = UNSET,
    drs_id_in: Union[Unset, list[str]] = UNSET,
    drs_id_iregex: Union[Unset, str] = UNSET,
    drs_id_isnull: Union[Unset, bool] = UNSET,
    drs_id_istartswith: Union[Unset, str] = UNSET,
    drs_id_lt: Union[Unset, str] = UNSET,
    drs_id_lte: Union[Unset, str] = UNSET,
    drs_id_range: Union[Unset, list[str]] = UNSET,
    drs_id_regex: Union[Unset, str] = UNSET,
    drs_id_startswith: Union[Unset, str] = UNSET,
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
    related_to_short_code: Union[Unset, str] = UNSET,
    related_to_short_code_in: Union[Unset, list[str]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
    version: Union[Unset, str] = UNSET,
    version_contains: Union[Unset, str] = UNSET,
    version_endswith: Union[Unset, str] = UNSET,
    version_gt: Union[Unset, str] = UNSET,
    version_gte: Union[Unset, str] = UNSET,
    version_icontains: Union[Unset, str] = UNSET,
    version_iendswith: Union[Unset, str] = UNSET,
    version_iexact: Union[Unset, str] = UNSET,
    version_in: Union[Unset, list[str]] = UNSET,
    version_iregex: Union[Unset, str] = UNSET,
    version_isnull: Union[Unset, bool] = UNSET,
    version_istartswith: Union[Unset, str] = UNSET,
    version_lt: Union[Unset, str] = UNSET,
    version_lte: Union[Unset, str] = UNSET,
    version_range: Union[Unset, list[str]] = UNSET,
    version_regex: Union[Unset, str] = UNSET,
    version_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedDRSDatasetReadList]:
    """Get a list of DRSDataset objects.

    Args:
        directory (Union[Unset, str]):
        directory_contains (Union[Unset, str]):
        directory_endswith (Union[Unset, str]):
        directory_gt (Union[Unset, str]):
        directory_gte (Union[Unset, str]):
        directory_icontains (Union[Unset, str]):
        directory_iendswith (Union[Unset, str]):
        directory_iexact (Union[Unset, str]):
        directory_in (Union[Unset, list[str]]):
        directory_iregex (Union[Unset, str]):
        directory_isnull (Union[Unset, bool]):
        directory_istartswith (Union[Unset, str]):
        directory_lt (Union[Unset, str]):
        directory_lte (Union[Unset, str]):
        directory_range (Union[Unset, list[str]]):
        directory_regex (Union[Unset, str]):
        directory_startswith (Union[Unset, str]):
        drs_id (Union[Unset, str]):
        drs_id_contains (Union[Unset, str]):
        drs_id_endswith (Union[Unset, str]):
        drs_id_gt (Union[Unset, str]):
        drs_id_gte (Union[Unset, str]):
        drs_id_icontains (Union[Unset, str]):
        drs_id_iendswith (Union[Unset, str]):
        drs_id_iexact (Union[Unset, str]):
        drs_id_in (Union[Unset, list[str]]):
        drs_id_iregex (Union[Unset, str]):
        drs_id_isnull (Union[Unset, bool]):
        drs_id_istartswith (Union[Unset, str]):
        drs_id_lt (Union[Unset, str]):
        drs_id_lte (Union[Unset, str]):
        drs_id_range (Union[Unset, list[str]]):
        drs_id_regex (Union[Unset, str]):
        drs_id_startswith (Union[Unset, str]):
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
        related_to_short_code (Union[Unset, str]):
        related_to_short_code_in (Union[Unset, list[str]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):
        version (Union[Unset, str]):
        version_contains (Union[Unset, str]):
        version_endswith (Union[Unset, str]):
        version_gt (Union[Unset, str]):
        version_gte (Union[Unset, str]):
        version_icontains (Union[Unset, str]):
        version_iendswith (Union[Unset, str]):
        version_iexact (Union[Unset, str]):
        version_in (Union[Unset, list[str]]):
        version_iregex (Union[Unset, str]):
        version_isnull (Union[Unset, bool]):
        version_istartswith (Union[Unset, str]):
        version_lt (Union[Unset, str]):
        version_lte (Union[Unset, str]):
        version_range (Union[Unset, list[str]]):
        version_regex (Union[Unset, str]):
        version_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDRSDatasetReadList]
    """

    kwargs = _get_kwargs(
        directory=directory,
        directory_contains=directory_contains,
        directory_endswith=directory_endswith,
        directory_gt=directory_gt,
        directory_gte=directory_gte,
        directory_icontains=directory_icontains,
        directory_iendswith=directory_iendswith,
        directory_iexact=directory_iexact,
        directory_in=directory_in,
        directory_iregex=directory_iregex,
        directory_isnull=directory_isnull,
        directory_istartswith=directory_istartswith,
        directory_lt=directory_lt,
        directory_lte=directory_lte,
        directory_range=directory_range,
        directory_regex=directory_regex,
        directory_startswith=directory_startswith,
        drs_id=drs_id,
        drs_id_contains=drs_id_contains,
        drs_id_endswith=drs_id_endswith,
        drs_id_gt=drs_id_gt,
        drs_id_gte=drs_id_gte,
        drs_id_icontains=drs_id_icontains,
        drs_id_iendswith=drs_id_iendswith,
        drs_id_iexact=drs_id_iexact,
        drs_id_in=drs_id_in,
        drs_id_iregex=drs_id_iregex,
        drs_id_isnull=drs_id_isnull,
        drs_id_istartswith=drs_id_istartswith,
        drs_id_lt=drs_id_lt,
        drs_id_lte=drs_id_lte,
        drs_id_range=drs_id_range,
        drs_id_regex=drs_id_regex,
        drs_id_startswith=drs_id_startswith,
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
        related_to_short_code=related_to_short_code,
        related_to_short_code_in=related_to_short_code_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
        version=version,
        version_contains=version_contains,
        version_endswith=version_endswith,
        version_gt=version_gt,
        version_gte=version_gte,
        version_icontains=version_icontains,
        version_iendswith=version_iendswith,
        version_iexact=version_iexact,
        version_in=version_in,
        version_iregex=version_iregex,
        version_isnull=version_isnull,
        version_istartswith=version_istartswith,
        version_lt=version_lt,
        version_lte=version_lte,
        version_range=version_range,
        version_regex=version_regex,
        version_startswith=version_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    directory: Union[Unset, str] = UNSET,
    directory_contains: Union[Unset, str] = UNSET,
    directory_endswith: Union[Unset, str] = UNSET,
    directory_gt: Union[Unset, str] = UNSET,
    directory_gte: Union[Unset, str] = UNSET,
    directory_icontains: Union[Unset, str] = UNSET,
    directory_iendswith: Union[Unset, str] = UNSET,
    directory_iexact: Union[Unset, str] = UNSET,
    directory_in: Union[Unset, list[str]] = UNSET,
    directory_iregex: Union[Unset, str] = UNSET,
    directory_isnull: Union[Unset, bool] = UNSET,
    directory_istartswith: Union[Unset, str] = UNSET,
    directory_lt: Union[Unset, str] = UNSET,
    directory_lte: Union[Unset, str] = UNSET,
    directory_range: Union[Unset, list[str]] = UNSET,
    directory_regex: Union[Unset, str] = UNSET,
    directory_startswith: Union[Unset, str] = UNSET,
    drs_id: Union[Unset, str] = UNSET,
    drs_id_contains: Union[Unset, str] = UNSET,
    drs_id_endswith: Union[Unset, str] = UNSET,
    drs_id_gt: Union[Unset, str] = UNSET,
    drs_id_gte: Union[Unset, str] = UNSET,
    drs_id_icontains: Union[Unset, str] = UNSET,
    drs_id_iendswith: Union[Unset, str] = UNSET,
    drs_id_iexact: Union[Unset, str] = UNSET,
    drs_id_in: Union[Unset, list[str]] = UNSET,
    drs_id_iregex: Union[Unset, str] = UNSET,
    drs_id_isnull: Union[Unset, bool] = UNSET,
    drs_id_istartswith: Union[Unset, str] = UNSET,
    drs_id_lt: Union[Unset, str] = UNSET,
    drs_id_lte: Union[Unset, str] = UNSET,
    drs_id_range: Union[Unset, list[str]] = UNSET,
    drs_id_regex: Union[Unset, str] = UNSET,
    drs_id_startswith: Union[Unset, str] = UNSET,
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
    related_to_short_code: Union[Unset, str] = UNSET,
    related_to_short_code_in: Union[Unset, list[str]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
    version: Union[Unset, str] = UNSET,
    version_contains: Union[Unset, str] = UNSET,
    version_endswith: Union[Unset, str] = UNSET,
    version_gt: Union[Unset, str] = UNSET,
    version_gte: Union[Unset, str] = UNSET,
    version_icontains: Union[Unset, str] = UNSET,
    version_iendswith: Union[Unset, str] = UNSET,
    version_iexact: Union[Unset, str] = UNSET,
    version_in: Union[Unset, list[str]] = UNSET,
    version_iregex: Union[Unset, str] = UNSET,
    version_isnull: Union[Unset, bool] = UNSET,
    version_istartswith: Union[Unset, str] = UNSET,
    version_lt: Union[Unset, str] = UNSET,
    version_lte: Union[Unset, str] = UNSET,
    version_range: Union[Unset, list[str]] = UNSET,
    version_regex: Union[Unset, str] = UNSET,
    version_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedDRSDatasetReadList]:
    """Get a list of DRSDataset objects.

    Args:
        directory (Union[Unset, str]):
        directory_contains (Union[Unset, str]):
        directory_endswith (Union[Unset, str]):
        directory_gt (Union[Unset, str]):
        directory_gte (Union[Unset, str]):
        directory_icontains (Union[Unset, str]):
        directory_iendswith (Union[Unset, str]):
        directory_iexact (Union[Unset, str]):
        directory_in (Union[Unset, list[str]]):
        directory_iregex (Union[Unset, str]):
        directory_isnull (Union[Unset, bool]):
        directory_istartswith (Union[Unset, str]):
        directory_lt (Union[Unset, str]):
        directory_lte (Union[Unset, str]):
        directory_range (Union[Unset, list[str]]):
        directory_regex (Union[Unset, str]):
        directory_startswith (Union[Unset, str]):
        drs_id (Union[Unset, str]):
        drs_id_contains (Union[Unset, str]):
        drs_id_endswith (Union[Unset, str]):
        drs_id_gt (Union[Unset, str]):
        drs_id_gte (Union[Unset, str]):
        drs_id_icontains (Union[Unset, str]):
        drs_id_iendswith (Union[Unset, str]):
        drs_id_iexact (Union[Unset, str]):
        drs_id_in (Union[Unset, list[str]]):
        drs_id_iregex (Union[Unset, str]):
        drs_id_isnull (Union[Unset, bool]):
        drs_id_istartswith (Union[Unset, str]):
        drs_id_lt (Union[Unset, str]):
        drs_id_lte (Union[Unset, str]):
        drs_id_range (Union[Unset, list[str]]):
        drs_id_regex (Union[Unset, str]):
        drs_id_startswith (Union[Unset, str]):
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
        related_to_short_code (Union[Unset, str]):
        related_to_short_code_in (Union[Unset, list[str]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):
        version (Union[Unset, str]):
        version_contains (Union[Unset, str]):
        version_endswith (Union[Unset, str]):
        version_gt (Union[Unset, str]):
        version_gte (Union[Unset, str]):
        version_icontains (Union[Unset, str]):
        version_iendswith (Union[Unset, str]):
        version_iexact (Union[Unset, str]):
        version_in (Union[Unset, list[str]]):
        version_iregex (Union[Unset, str]):
        version_isnull (Union[Unset, bool]):
        version_istartswith (Union[Unset, str]):
        version_lt (Union[Unset, str]):
        version_lte (Union[Unset, str]):
        version_range (Union[Unset, list[str]]):
        version_regex (Union[Unset, str]):
        version_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDRSDatasetReadList
    """

    return sync_detailed(
        client=client,
        directory=directory,
        directory_contains=directory_contains,
        directory_endswith=directory_endswith,
        directory_gt=directory_gt,
        directory_gte=directory_gte,
        directory_icontains=directory_icontains,
        directory_iendswith=directory_iendswith,
        directory_iexact=directory_iexact,
        directory_in=directory_in,
        directory_iregex=directory_iregex,
        directory_isnull=directory_isnull,
        directory_istartswith=directory_istartswith,
        directory_lt=directory_lt,
        directory_lte=directory_lte,
        directory_range=directory_range,
        directory_regex=directory_regex,
        directory_startswith=directory_startswith,
        drs_id=drs_id,
        drs_id_contains=drs_id_contains,
        drs_id_endswith=drs_id_endswith,
        drs_id_gt=drs_id_gt,
        drs_id_gte=drs_id_gte,
        drs_id_icontains=drs_id_icontains,
        drs_id_iendswith=drs_id_iendswith,
        drs_id_iexact=drs_id_iexact,
        drs_id_in=drs_id_in,
        drs_id_iregex=drs_id_iregex,
        drs_id_isnull=drs_id_isnull,
        drs_id_istartswith=drs_id_istartswith,
        drs_id_lt=drs_id_lt,
        drs_id_lte=drs_id_lte,
        drs_id_range=drs_id_range,
        drs_id_regex=drs_id_regex,
        drs_id_startswith=drs_id_startswith,
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
        related_to_short_code=related_to_short_code,
        related_to_short_code_in=related_to_short_code_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
        version=version,
        version_contains=version_contains,
        version_endswith=version_endswith,
        version_gt=version_gt,
        version_gte=version_gte,
        version_icontains=version_icontains,
        version_iendswith=version_iendswith,
        version_iexact=version_iexact,
        version_in=version_in,
        version_iregex=version_iregex,
        version_isnull=version_isnull,
        version_istartswith=version_istartswith,
        version_lt=version_lt,
        version_lte=version_lte,
        version_range=version_range,
        version_regex=version_regex,
        version_startswith=version_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    directory: Union[Unset, str] = UNSET,
    directory_contains: Union[Unset, str] = UNSET,
    directory_endswith: Union[Unset, str] = UNSET,
    directory_gt: Union[Unset, str] = UNSET,
    directory_gte: Union[Unset, str] = UNSET,
    directory_icontains: Union[Unset, str] = UNSET,
    directory_iendswith: Union[Unset, str] = UNSET,
    directory_iexact: Union[Unset, str] = UNSET,
    directory_in: Union[Unset, list[str]] = UNSET,
    directory_iregex: Union[Unset, str] = UNSET,
    directory_isnull: Union[Unset, bool] = UNSET,
    directory_istartswith: Union[Unset, str] = UNSET,
    directory_lt: Union[Unset, str] = UNSET,
    directory_lte: Union[Unset, str] = UNSET,
    directory_range: Union[Unset, list[str]] = UNSET,
    directory_regex: Union[Unset, str] = UNSET,
    directory_startswith: Union[Unset, str] = UNSET,
    drs_id: Union[Unset, str] = UNSET,
    drs_id_contains: Union[Unset, str] = UNSET,
    drs_id_endswith: Union[Unset, str] = UNSET,
    drs_id_gt: Union[Unset, str] = UNSET,
    drs_id_gte: Union[Unset, str] = UNSET,
    drs_id_icontains: Union[Unset, str] = UNSET,
    drs_id_iendswith: Union[Unset, str] = UNSET,
    drs_id_iexact: Union[Unset, str] = UNSET,
    drs_id_in: Union[Unset, list[str]] = UNSET,
    drs_id_iregex: Union[Unset, str] = UNSET,
    drs_id_isnull: Union[Unset, bool] = UNSET,
    drs_id_istartswith: Union[Unset, str] = UNSET,
    drs_id_lt: Union[Unset, str] = UNSET,
    drs_id_lte: Union[Unset, str] = UNSET,
    drs_id_range: Union[Unset, list[str]] = UNSET,
    drs_id_regex: Union[Unset, str] = UNSET,
    drs_id_startswith: Union[Unset, str] = UNSET,
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
    related_to_short_code: Union[Unset, str] = UNSET,
    related_to_short_code_in: Union[Unset, list[str]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
    version: Union[Unset, str] = UNSET,
    version_contains: Union[Unset, str] = UNSET,
    version_endswith: Union[Unset, str] = UNSET,
    version_gt: Union[Unset, str] = UNSET,
    version_gte: Union[Unset, str] = UNSET,
    version_icontains: Union[Unset, str] = UNSET,
    version_iendswith: Union[Unset, str] = UNSET,
    version_iexact: Union[Unset, str] = UNSET,
    version_in: Union[Unset, list[str]] = UNSET,
    version_iregex: Union[Unset, str] = UNSET,
    version_isnull: Union[Unset, bool] = UNSET,
    version_istartswith: Union[Unset, str] = UNSET,
    version_lt: Union[Unset, str] = UNSET,
    version_lte: Union[Unset, str] = UNSET,
    version_range: Union[Unset, list[str]] = UNSET,
    version_regex: Union[Unset, str] = UNSET,
    version_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedDRSDatasetReadList]:
    """Get a list of DRSDataset objects.

    Args:
        directory (Union[Unset, str]):
        directory_contains (Union[Unset, str]):
        directory_endswith (Union[Unset, str]):
        directory_gt (Union[Unset, str]):
        directory_gte (Union[Unset, str]):
        directory_icontains (Union[Unset, str]):
        directory_iendswith (Union[Unset, str]):
        directory_iexact (Union[Unset, str]):
        directory_in (Union[Unset, list[str]]):
        directory_iregex (Union[Unset, str]):
        directory_isnull (Union[Unset, bool]):
        directory_istartswith (Union[Unset, str]):
        directory_lt (Union[Unset, str]):
        directory_lte (Union[Unset, str]):
        directory_range (Union[Unset, list[str]]):
        directory_regex (Union[Unset, str]):
        directory_startswith (Union[Unset, str]):
        drs_id (Union[Unset, str]):
        drs_id_contains (Union[Unset, str]):
        drs_id_endswith (Union[Unset, str]):
        drs_id_gt (Union[Unset, str]):
        drs_id_gte (Union[Unset, str]):
        drs_id_icontains (Union[Unset, str]):
        drs_id_iendswith (Union[Unset, str]):
        drs_id_iexact (Union[Unset, str]):
        drs_id_in (Union[Unset, list[str]]):
        drs_id_iregex (Union[Unset, str]):
        drs_id_isnull (Union[Unset, bool]):
        drs_id_istartswith (Union[Unset, str]):
        drs_id_lt (Union[Unset, str]):
        drs_id_lte (Union[Unset, str]):
        drs_id_range (Union[Unset, list[str]]):
        drs_id_regex (Union[Unset, str]):
        drs_id_startswith (Union[Unset, str]):
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
        related_to_short_code (Union[Unset, str]):
        related_to_short_code_in (Union[Unset, list[str]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):
        version (Union[Unset, str]):
        version_contains (Union[Unset, str]):
        version_endswith (Union[Unset, str]):
        version_gt (Union[Unset, str]):
        version_gte (Union[Unset, str]):
        version_icontains (Union[Unset, str]):
        version_iendswith (Union[Unset, str]):
        version_iexact (Union[Unset, str]):
        version_in (Union[Unset, list[str]]):
        version_iregex (Union[Unset, str]):
        version_isnull (Union[Unset, bool]):
        version_istartswith (Union[Unset, str]):
        version_lt (Union[Unset, str]):
        version_lte (Union[Unset, str]):
        version_range (Union[Unset, list[str]]):
        version_regex (Union[Unset, str]):
        version_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedDRSDatasetReadList]
    """

    kwargs = _get_kwargs(
        directory=directory,
        directory_contains=directory_contains,
        directory_endswith=directory_endswith,
        directory_gt=directory_gt,
        directory_gte=directory_gte,
        directory_icontains=directory_icontains,
        directory_iendswith=directory_iendswith,
        directory_iexact=directory_iexact,
        directory_in=directory_in,
        directory_iregex=directory_iregex,
        directory_isnull=directory_isnull,
        directory_istartswith=directory_istartswith,
        directory_lt=directory_lt,
        directory_lte=directory_lte,
        directory_range=directory_range,
        directory_regex=directory_regex,
        directory_startswith=directory_startswith,
        drs_id=drs_id,
        drs_id_contains=drs_id_contains,
        drs_id_endswith=drs_id_endswith,
        drs_id_gt=drs_id_gt,
        drs_id_gte=drs_id_gte,
        drs_id_icontains=drs_id_icontains,
        drs_id_iendswith=drs_id_iendswith,
        drs_id_iexact=drs_id_iexact,
        drs_id_in=drs_id_in,
        drs_id_iregex=drs_id_iregex,
        drs_id_isnull=drs_id_isnull,
        drs_id_istartswith=drs_id_istartswith,
        drs_id_lt=drs_id_lt,
        drs_id_lte=drs_id_lte,
        drs_id_range=drs_id_range,
        drs_id_regex=drs_id_regex,
        drs_id_startswith=drs_id_startswith,
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
        related_to_short_code=related_to_short_code,
        related_to_short_code_in=related_to_short_code_in,
        related_to_uuid=related_to_uuid,
        related_to_uuid_in=related_to_uuid_in,
        version=version,
        version_contains=version_contains,
        version_endswith=version_endswith,
        version_gt=version_gt,
        version_gte=version_gte,
        version_icontains=version_icontains,
        version_iendswith=version_iendswith,
        version_iexact=version_iexact,
        version_in=version_in,
        version_iregex=version_iregex,
        version_isnull=version_isnull,
        version_istartswith=version_istartswith,
        version_lt=version_lt,
        version_lte=version_lte,
        version_range=version_range,
        version_regex=version_regex,
        version_startswith=version_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    directory: Union[Unset, str] = UNSET,
    directory_contains: Union[Unset, str] = UNSET,
    directory_endswith: Union[Unset, str] = UNSET,
    directory_gt: Union[Unset, str] = UNSET,
    directory_gte: Union[Unset, str] = UNSET,
    directory_icontains: Union[Unset, str] = UNSET,
    directory_iendswith: Union[Unset, str] = UNSET,
    directory_iexact: Union[Unset, str] = UNSET,
    directory_in: Union[Unset, list[str]] = UNSET,
    directory_iregex: Union[Unset, str] = UNSET,
    directory_isnull: Union[Unset, bool] = UNSET,
    directory_istartswith: Union[Unset, str] = UNSET,
    directory_lt: Union[Unset, str] = UNSET,
    directory_lte: Union[Unset, str] = UNSET,
    directory_range: Union[Unset, list[str]] = UNSET,
    directory_regex: Union[Unset, str] = UNSET,
    directory_startswith: Union[Unset, str] = UNSET,
    drs_id: Union[Unset, str] = UNSET,
    drs_id_contains: Union[Unset, str] = UNSET,
    drs_id_endswith: Union[Unset, str] = UNSET,
    drs_id_gt: Union[Unset, str] = UNSET,
    drs_id_gte: Union[Unset, str] = UNSET,
    drs_id_icontains: Union[Unset, str] = UNSET,
    drs_id_iendswith: Union[Unset, str] = UNSET,
    drs_id_iexact: Union[Unset, str] = UNSET,
    drs_id_in: Union[Unset, list[str]] = UNSET,
    drs_id_iregex: Union[Unset, str] = UNSET,
    drs_id_isnull: Union[Unset, bool] = UNSET,
    drs_id_istartswith: Union[Unset, str] = UNSET,
    drs_id_lt: Union[Unset, str] = UNSET,
    drs_id_lte: Union[Unset, str] = UNSET,
    drs_id_range: Union[Unset, list[str]] = UNSET,
    drs_id_regex: Union[Unset, str] = UNSET,
    drs_id_startswith: Union[Unset, str] = UNSET,
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
    related_to_short_code: Union[Unset, str] = UNSET,
    related_to_short_code_in: Union[Unset, list[str]] = UNSET,
    related_to_uuid: Union[Unset, str] = UNSET,
    related_to_uuid_in: Union[Unset, list[str]] = UNSET,
    version: Union[Unset, str] = UNSET,
    version_contains: Union[Unset, str] = UNSET,
    version_endswith: Union[Unset, str] = UNSET,
    version_gt: Union[Unset, str] = UNSET,
    version_gte: Union[Unset, str] = UNSET,
    version_icontains: Union[Unset, str] = UNSET,
    version_iendswith: Union[Unset, str] = UNSET,
    version_iexact: Union[Unset, str] = UNSET,
    version_in: Union[Unset, list[str]] = UNSET,
    version_iregex: Union[Unset, str] = UNSET,
    version_isnull: Union[Unset, bool] = UNSET,
    version_istartswith: Union[Unset, str] = UNSET,
    version_lt: Union[Unset, str] = UNSET,
    version_lte: Union[Unset, str] = UNSET,
    version_range: Union[Unset, list[str]] = UNSET,
    version_regex: Union[Unset, str] = UNSET,
    version_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedDRSDatasetReadList]:
    """Get a list of DRSDataset objects.

    Args:
        directory (Union[Unset, str]):
        directory_contains (Union[Unset, str]):
        directory_endswith (Union[Unset, str]):
        directory_gt (Union[Unset, str]):
        directory_gte (Union[Unset, str]):
        directory_icontains (Union[Unset, str]):
        directory_iendswith (Union[Unset, str]):
        directory_iexact (Union[Unset, str]):
        directory_in (Union[Unset, list[str]]):
        directory_iregex (Union[Unset, str]):
        directory_isnull (Union[Unset, bool]):
        directory_istartswith (Union[Unset, str]):
        directory_lt (Union[Unset, str]):
        directory_lte (Union[Unset, str]):
        directory_range (Union[Unset, list[str]]):
        directory_regex (Union[Unset, str]):
        directory_startswith (Union[Unset, str]):
        drs_id (Union[Unset, str]):
        drs_id_contains (Union[Unset, str]):
        drs_id_endswith (Union[Unset, str]):
        drs_id_gt (Union[Unset, str]):
        drs_id_gte (Union[Unset, str]):
        drs_id_icontains (Union[Unset, str]):
        drs_id_iendswith (Union[Unset, str]):
        drs_id_iexact (Union[Unset, str]):
        drs_id_in (Union[Unset, list[str]]):
        drs_id_iregex (Union[Unset, str]):
        drs_id_isnull (Union[Unset, bool]):
        drs_id_istartswith (Union[Unset, str]):
        drs_id_lt (Union[Unset, str]):
        drs_id_lte (Union[Unset, str]):
        drs_id_range (Union[Unset, list[str]]):
        drs_id_regex (Union[Unset, str]):
        drs_id_startswith (Union[Unset, str]):
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
        related_to_short_code (Union[Unset, str]):
        related_to_short_code_in (Union[Unset, list[str]]):
        related_to_uuid (Union[Unset, str]):
        related_to_uuid_in (Union[Unset, list[str]]):
        version (Union[Unset, str]):
        version_contains (Union[Unset, str]):
        version_endswith (Union[Unset, str]):
        version_gt (Union[Unset, str]):
        version_gte (Union[Unset, str]):
        version_icontains (Union[Unset, str]):
        version_iendswith (Union[Unset, str]):
        version_iexact (Union[Unset, str]):
        version_in (Union[Unset, list[str]]):
        version_iregex (Union[Unset, str]):
        version_isnull (Union[Unset, bool]):
        version_istartswith (Union[Unset, str]):
        version_lt (Union[Unset, str]):
        version_lte (Union[Unset, str]):
        version_range (Union[Unset, list[str]]):
        version_regex (Union[Unset, str]):
        version_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedDRSDatasetReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            directory=directory,
            directory_contains=directory_contains,
            directory_endswith=directory_endswith,
            directory_gt=directory_gt,
            directory_gte=directory_gte,
            directory_icontains=directory_icontains,
            directory_iendswith=directory_iendswith,
            directory_iexact=directory_iexact,
            directory_in=directory_in,
            directory_iregex=directory_iregex,
            directory_isnull=directory_isnull,
            directory_istartswith=directory_istartswith,
            directory_lt=directory_lt,
            directory_lte=directory_lte,
            directory_range=directory_range,
            directory_regex=directory_regex,
            directory_startswith=directory_startswith,
            drs_id=drs_id,
            drs_id_contains=drs_id_contains,
            drs_id_endswith=drs_id_endswith,
            drs_id_gt=drs_id_gt,
            drs_id_gte=drs_id_gte,
            drs_id_icontains=drs_id_icontains,
            drs_id_iendswith=drs_id_iendswith,
            drs_id_iexact=drs_id_iexact,
            drs_id_in=drs_id_in,
            drs_id_iregex=drs_id_iregex,
            drs_id_isnull=drs_id_isnull,
            drs_id_istartswith=drs_id_istartswith,
            drs_id_lt=drs_id_lt,
            drs_id_lte=drs_id_lte,
            drs_id_range=drs_id_range,
            drs_id_regex=drs_id_regex,
            drs_id_startswith=drs_id_startswith,
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
            related_to_short_code=related_to_short_code,
            related_to_short_code_in=related_to_short_code_in,
            related_to_uuid=related_to_uuid,
            related_to_uuid_in=related_to_uuid_in,
            version=version,
            version_contains=version_contains,
            version_endswith=version_endswith,
            version_gt=version_gt,
            version_gte=version_gte,
            version_icontains=version_icontains,
            version_iendswith=version_iendswith,
            version_iexact=version_iexact,
            version_in=version_in,
            version_iregex=version_iregex,
            version_isnull=version_isnull,
            version_istartswith=version_istartswith,
            version_lt=version_lt,
            version_lte=version_lte,
            version_range=version_range,
            version_regex=version_regex,
            version_startswith=version_startswith,
        )
    ).parsed
