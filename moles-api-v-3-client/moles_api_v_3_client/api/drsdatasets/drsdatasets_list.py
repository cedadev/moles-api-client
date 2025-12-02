from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_drs_dataset_read_list import PaginatedDRSDatasetReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    directory: str | Unset = UNSET,
    directory_contains: str | Unset = UNSET,
    directory_endswith: str | Unset = UNSET,
    directory_gt: str | Unset = UNSET,
    directory_gte: str | Unset = UNSET,
    directory_icontains: str | Unset = UNSET,
    directory_iendswith: str | Unset = UNSET,
    directory_iexact: str | Unset = UNSET,
    directory_in: list[str] | Unset = UNSET,
    directory_iregex: str | Unset = UNSET,
    directory_isnull: bool | Unset = UNSET,
    directory_istartswith: str | Unset = UNSET,
    directory_lt: str | Unset = UNSET,
    directory_lte: str | Unset = UNSET,
    directory_range: list[str] | Unset = UNSET,
    directory_regex: str | Unset = UNSET,
    directory_startswith: str | Unset = UNSET,
    drs_id: str | Unset = UNSET,
    drs_id_contains: str | Unset = UNSET,
    drs_id_endswith: str | Unset = UNSET,
    drs_id_gt: str | Unset = UNSET,
    drs_id_gte: str | Unset = UNSET,
    drs_id_icontains: str | Unset = UNSET,
    drs_id_iendswith: str | Unset = UNSET,
    drs_id_iexact: str | Unset = UNSET,
    drs_id_in: list[str] | Unset = UNSET,
    drs_id_iregex: str | Unset = UNSET,
    drs_id_isnull: bool | Unset = UNSET,
    drs_id_istartswith: str | Unset = UNSET,
    drs_id_lt: str | Unset = UNSET,
    drs_id_lte: str | Unset = UNSET,
    drs_id_range: list[str] | Unset = UNSET,
    drs_id_regex: str | Unset = UNSET,
    drs_id_startswith: str | Unset = UNSET,
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
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
    version: str | Unset = UNSET,
    version_contains: str | Unset = UNSET,
    version_endswith: str | Unset = UNSET,
    version_gt: str | Unset = UNSET,
    version_gte: str | Unset = UNSET,
    version_icontains: str | Unset = UNSET,
    version_iendswith: str | Unset = UNSET,
    version_iexact: str | Unset = UNSET,
    version_in: list[str] | Unset = UNSET,
    version_iregex: str | Unset = UNSET,
    version_isnull: bool | Unset = UNSET,
    version_istartswith: str | Unset = UNSET,
    version_lt: str | Unset = UNSET,
    version_lte: str | Unset = UNSET,
    version_range: list[str] | Unset = UNSET,
    version_regex: str | Unset = UNSET,
    version_startswith: str | Unset = UNSET,
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

    json_directory_in: list[str] | Unset = UNSET
    if not isinstance(directory_in, Unset):
        json_directory_in = ",".join(map(str, directory_in))

    params["directory__in"] = json_directory_in

    params["directory__iregex"] = directory_iregex

    params["directory__isnull"] = directory_isnull

    params["directory__istartswith"] = directory_istartswith

    params["directory__lt"] = directory_lt

    params["directory__lte"] = directory_lte

    json_directory_range: list[str] | Unset = UNSET
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

    json_drs_id_in: list[str] | Unset = UNSET
    if not isinstance(drs_id_in, Unset):
        json_drs_id_in = ",".join(map(str, drs_id_in))

    params["drsId__in"] = json_drs_id_in

    params["drsId__iregex"] = drs_id_iregex

    params["drsId__isnull"] = drs_id_isnull

    params["drsId__istartswith"] = drs_id_istartswith

    params["drsId__lt"] = drs_id_lt

    params["drsId__lte"] = drs_id_lte

    json_drs_id_range: list[str] | Unset = UNSET
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

    params["relatedTo"] = related_to

    json_related_to_in: list[int] | Unset = UNSET
    if not isinstance(related_to_in, Unset):
        json_related_to_in = ",".join(map(str, related_to_in))

    params["relatedTo__in"] = json_related_to_in

    params["relatedTo__isnull"] = related_to_isnull

    params["relatedTo__ob_id"] = related_to_ob_id

    json_related_to_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(related_to_ob_id_in, Unset):
        json_related_to_ob_id_in = ",".join(map(str, related_to_ob_id_in))

    params["relatedTo__ob_id__in"] = json_related_to_ob_id_in

    params["relatedTo__short_code"] = related_to_short_code

    json_related_to_short_code_in: list[str] | Unset = UNSET
    if not isinstance(related_to_short_code_in, Unset):
        json_related_to_short_code_in = ",".join(map(str, related_to_short_code_in))

    params["relatedTo__short_code__in"] = json_related_to_short_code_in

    params["relatedTo__uuid"] = related_to_uuid

    json_related_to_uuid_in: list[str] | Unset = UNSET
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

    json_version_in: list[str] | Unset = UNSET
    if not isinstance(version_in, Unset):
        json_version_in = ",".join(map(str, version_in))

    params["version__in"] = json_version_in

    params["version__iregex"] = version_iregex

    params["version__isnull"] = version_isnull

    params["version__istartswith"] = version_istartswith

    params["version__lt"] = version_lt

    params["version__lte"] = version_lte

    json_version_range: list[str] | Unset = UNSET
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedDRSDatasetReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedDRSDatasetReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    directory: str | Unset = UNSET,
    directory_contains: str | Unset = UNSET,
    directory_endswith: str | Unset = UNSET,
    directory_gt: str | Unset = UNSET,
    directory_gte: str | Unset = UNSET,
    directory_icontains: str | Unset = UNSET,
    directory_iendswith: str | Unset = UNSET,
    directory_iexact: str | Unset = UNSET,
    directory_in: list[str] | Unset = UNSET,
    directory_iregex: str | Unset = UNSET,
    directory_isnull: bool | Unset = UNSET,
    directory_istartswith: str | Unset = UNSET,
    directory_lt: str | Unset = UNSET,
    directory_lte: str | Unset = UNSET,
    directory_range: list[str] | Unset = UNSET,
    directory_regex: str | Unset = UNSET,
    directory_startswith: str | Unset = UNSET,
    drs_id: str | Unset = UNSET,
    drs_id_contains: str | Unset = UNSET,
    drs_id_endswith: str | Unset = UNSET,
    drs_id_gt: str | Unset = UNSET,
    drs_id_gte: str | Unset = UNSET,
    drs_id_icontains: str | Unset = UNSET,
    drs_id_iendswith: str | Unset = UNSET,
    drs_id_iexact: str | Unset = UNSET,
    drs_id_in: list[str] | Unset = UNSET,
    drs_id_iregex: str | Unset = UNSET,
    drs_id_isnull: bool | Unset = UNSET,
    drs_id_istartswith: str | Unset = UNSET,
    drs_id_lt: str | Unset = UNSET,
    drs_id_lte: str | Unset = UNSET,
    drs_id_range: list[str] | Unset = UNSET,
    drs_id_regex: str | Unset = UNSET,
    drs_id_startswith: str | Unset = UNSET,
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
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
    version: str | Unset = UNSET,
    version_contains: str | Unset = UNSET,
    version_endswith: str | Unset = UNSET,
    version_gt: str | Unset = UNSET,
    version_gte: str | Unset = UNSET,
    version_icontains: str | Unset = UNSET,
    version_iendswith: str | Unset = UNSET,
    version_iexact: str | Unset = UNSET,
    version_in: list[str] | Unset = UNSET,
    version_iregex: str | Unset = UNSET,
    version_isnull: bool | Unset = UNSET,
    version_istartswith: str | Unset = UNSET,
    version_lt: str | Unset = UNSET,
    version_lte: str | Unset = UNSET,
    version_range: list[str] | Unset = UNSET,
    version_regex: str | Unset = UNSET,
    version_startswith: str | Unset = UNSET,
) -> Response[PaginatedDRSDatasetReadList]:
    """Get a list of DRSDataset objects.

    Args:
        directory (str | Unset):
        directory_contains (str | Unset):
        directory_endswith (str | Unset):
        directory_gt (str | Unset):
        directory_gte (str | Unset):
        directory_icontains (str | Unset):
        directory_iendswith (str | Unset):
        directory_iexact (str | Unset):
        directory_in (list[str] | Unset):
        directory_iregex (str | Unset):
        directory_isnull (bool | Unset):
        directory_istartswith (str | Unset):
        directory_lt (str | Unset):
        directory_lte (str | Unset):
        directory_range (list[str] | Unset):
        directory_regex (str | Unset):
        directory_startswith (str | Unset):
        drs_id (str | Unset):
        drs_id_contains (str | Unset):
        drs_id_endswith (str | Unset):
        drs_id_gt (str | Unset):
        drs_id_gte (str | Unset):
        drs_id_icontains (str | Unset):
        drs_id_iendswith (str | Unset):
        drs_id_iexact (str | Unset):
        drs_id_in (list[str] | Unset):
        drs_id_iregex (str | Unset):
        drs_id_isnull (bool | Unset):
        drs_id_istartswith (str | Unset):
        drs_id_lt (str | Unset):
        drs_id_lte (str | Unset):
        drs_id_range (list[str] | Unset):
        drs_id_regex (str | Unset):
        drs_id_startswith (str | Unset):
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
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):
        version (str | Unset):
        version_contains (str | Unset):
        version_endswith (str | Unset):
        version_gt (str | Unset):
        version_gte (str | Unset):
        version_icontains (str | Unset):
        version_iendswith (str | Unset):
        version_iexact (str | Unset):
        version_in (list[str] | Unset):
        version_iregex (str | Unset):
        version_isnull (bool | Unset):
        version_istartswith (str | Unset):
        version_lt (str | Unset):
        version_lte (str | Unset):
        version_range (list[str] | Unset):
        version_regex (str | Unset):
        version_startswith (str | Unset):

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
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
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
    directory: str | Unset = UNSET,
    directory_contains: str | Unset = UNSET,
    directory_endswith: str | Unset = UNSET,
    directory_gt: str | Unset = UNSET,
    directory_gte: str | Unset = UNSET,
    directory_icontains: str | Unset = UNSET,
    directory_iendswith: str | Unset = UNSET,
    directory_iexact: str | Unset = UNSET,
    directory_in: list[str] | Unset = UNSET,
    directory_iregex: str | Unset = UNSET,
    directory_isnull: bool | Unset = UNSET,
    directory_istartswith: str | Unset = UNSET,
    directory_lt: str | Unset = UNSET,
    directory_lte: str | Unset = UNSET,
    directory_range: list[str] | Unset = UNSET,
    directory_regex: str | Unset = UNSET,
    directory_startswith: str | Unset = UNSET,
    drs_id: str | Unset = UNSET,
    drs_id_contains: str | Unset = UNSET,
    drs_id_endswith: str | Unset = UNSET,
    drs_id_gt: str | Unset = UNSET,
    drs_id_gte: str | Unset = UNSET,
    drs_id_icontains: str | Unset = UNSET,
    drs_id_iendswith: str | Unset = UNSET,
    drs_id_iexact: str | Unset = UNSET,
    drs_id_in: list[str] | Unset = UNSET,
    drs_id_iregex: str | Unset = UNSET,
    drs_id_isnull: bool | Unset = UNSET,
    drs_id_istartswith: str | Unset = UNSET,
    drs_id_lt: str | Unset = UNSET,
    drs_id_lte: str | Unset = UNSET,
    drs_id_range: list[str] | Unset = UNSET,
    drs_id_regex: str | Unset = UNSET,
    drs_id_startswith: str | Unset = UNSET,
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
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
    version: str | Unset = UNSET,
    version_contains: str | Unset = UNSET,
    version_endswith: str | Unset = UNSET,
    version_gt: str | Unset = UNSET,
    version_gte: str | Unset = UNSET,
    version_icontains: str | Unset = UNSET,
    version_iendswith: str | Unset = UNSET,
    version_iexact: str | Unset = UNSET,
    version_in: list[str] | Unset = UNSET,
    version_iregex: str | Unset = UNSET,
    version_isnull: bool | Unset = UNSET,
    version_istartswith: str | Unset = UNSET,
    version_lt: str | Unset = UNSET,
    version_lte: str | Unset = UNSET,
    version_range: list[str] | Unset = UNSET,
    version_regex: str | Unset = UNSET,
    version_startswith: str | Unset = UNSET,
) -> PaginatedDRSDatasetReadList | None:
    """Get a list of DRSDataset objects.

    Args:
        directory (str | Unset):
        directory_contains (str | Unset):
        directory_endswith (str | Unset):
        directory_gt (str | Unset):
        directory_gte (str | Unset):
        directory_icontains (str | Unset):
        directory_iendswith (str | Unset):
        directory_iexact (str | Unset):
        directory_in (list[str] | Unset):
        directory_iregex (str | Unset):
        directory_isnull (bool | Unset):
        directory_istartswith (str | Unset):
        directory_lt (str | Unset):
        directory_lte (str | Unset):
        directory_range (list[str] | Unset):
        directory_regex (str | Unset):
        directory_startswith (str | Unset):
        drs_id (str | Unset):
        drs_id_contains (str | Unset):
        drs_id_endswith (str | Unset):
        drs_id_gt (str | Unset):
        drs_id_gte (str | Unset):
        drs_id_icontains (str | Unset):
        drs_id_iendswith (str | Unset):
        drs_id_iexact (str | Unset):
        drs_id_in (list[str] | Unset):
        drs_id_iregex (str | Unset):
        drs_id_isnull (bool | Unset):
        drs_id_istartswith (str | Unset):
        drs_id_lt (str | Unset):
        drs_id_lte (str | Unset):
        drs_id_range (list[str] | Unset):
        drs_id_regex (str | Unset):
        drs_id_startswith (str | Unset):
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
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):
        version (str | Unset):
        version_contains (str | Unset):
        version_endswith (str | Unset):
        version_gt (str | Unset):
        version_gte (str | Unset):
        version_icontains (str | Unset):
        version_iendswith (str | Unset):
        version_iexact (str | Unset):
        version_in (list[str] | Unset):
        version_iregex (str | Unset):
        version_isnull (bool | Unset):
        version_istartswith (str | Unset):
        version_lt (str | Unset):
        version_lte (str | Unset):
        version_range (list[str] | Unset):
        version_regex (str | Unset):
        version_startswith (str | Unset):

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
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
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
    directory: str | Unset = UNSET,
    directory_contains: str | Unset = UNSET,
    directory_endswith: str | Unset = UNSET,
    directory_gt: str | Unset = UNSET,
    directory_gte: str | Unset = UNSET,
    directory_icontains: str | Unset = UNSET,
    directory_iendswith: str | Unset = UNSET,
    directory_iexact: str | Unset = UNSET,
    directory_in: list[str] | Unset = UNSET,
    directory_iregex: str | Unset = UNSET,
    directory_isnull: bool | Unset = UNSET,
    directory_istartswith: str | Unset = UNSET,
    directory_lt: str | Unset = UNSET,
    directory_lte: str | Unset = UNSET,
    directory_range: list[str] | Unset = UNSET,
    directory_regex: str | Unset = UNSET,
    directory_startswith: str | Unset = UNSET,
    drs_id: str | Unset = UNSET,
    drs_id_contains: str | Unset = UNSET,
    drs_id_endswith: str | Unset = UNSET,
    drs_id_gt: str | Unset = UNSET,
    drs_id_gte: str | Unset = UNSET,
    drs_id_icontains: str | Unset = UNSET,
    drs_id_iendswith: str | Unset = UNSET,
    drs_id_iexact: str | Unset = UNSET,
    drs_id_in: list[str] | Unset = UNSET,
    drs_id_iregex: str | Unset = UNSET,
    drs_id_isnull: bool | Unset = UNSET,
    drs_id_istartswith: str | Unset = UNSET,
    drs_id_lt: str | Unset = UNSET,
    drs_id_lte: str | Unset = UNSET,
    drs_id_range: list[str] | Unset = UNSET,
    drs_id_regex: str | Unset = UNSET,
    drs_id_startswith: str | Unset = UNSET,
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
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
    version: str | Unset = UNSET,
    version_contains: str | Unset = UNSET,
    version_endswith: str | Unset = UNSET,
    version_gt: str | Unset = UNSET,
    version_gte: str | Unset = UNSET,
    version_icontains: str | Unset = UNSET,
    version_iendswith: str | Unset = UNSET,
    version_iexact: str | Unset = UNSET,
    version_in: list[str] | Unset = UNSET,
    version_iregex: str | Unset = UNSET,
    version_isnull: bool | Unset = UNSET,
    version_istartswith: str | Unset = UNSET,
    version_lt: str | Unset = UNSET,
    version_lte: str | Unset = UNSET,
    version_range: list[str] | Unset = UNSET,
    version_regex: str | Unset = UNSET,
    version_startswith: str | Unset = UNSET,
) -> Response[PaginatedDRSDatasetReadList]:
    """Get a list of DRSDataset objects.

    Args:
        directory (str | Unset):
        directory_contains (str | Unset):
        directory_endswith (str | Unset):
        directory_gt (str | Unset):
        directory_gte (str | Unset):
        directory_icontains (str | Unset):
        directory_iendswith (str | Unset):
        directory_iexact (str | Unset):
        directory_in (list[str] | Unset):
        directory_iregex (str | Unset):
        directory_isnull (bool | Unset):
        directory_istartswith (str | Unset):
        directory_lt (str | Unset):
        directory_lte (str | Unset):
        directory_range (list[str] | Unset):
        directory_regex (str | Unset):
        directory_startswith (str | Unset):
        drs_id (str | Unset):
        drs_id_contains (str | Unset):
        drs_id_endswith (str | Unset):
        drs_id_gt (str | Unset):
        drs_id_gte (str | Unset):
        drs_id_icontains (str | Unset):
        drs_id_iendswith (str | Unset):
        drs_id_iexact (str | Unset):
        drs_id_in (list[str] | Unset):
        drs_id_iregex (str | Unset):
        drs_id_isnull (bool | Unset):
        drs_id_istartswith (str | Unset):
        drs_id_lt (str | Unset):
        drs_id_lte (str | Unset):
        drs_id_range (list[str] | Unset):
        drs_id_regex (str | Unset):
        drs_id_startswith (str | Unset):
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
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):
        version (str | Unset):
        version_contains (str | Unset):
        version_endswith (str | Unset):
        version_gt (str | Unset):
        version_gte (str | Unset):
        version_icontains (str | Unset):
        version_iendswith (str | Unset):
        version_iexact (str | Unset):
        version_in (list[str] | Unset):
        version_iregex (str | Unset):
        version_isnull (bool | Unset):
        version_istartswith (str | Unset):
        version_lt (str | Unset):
        version_lte (str | Unset):
        version_range (list[str] | Unset):
        version_regex (str | Unset):
        version_startswith (str | Unset):

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
        related_to_in=related_to_in,
        related_to_isnull=related_to_isnull,
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
    directory: str | Unset = UNSET,
    directory_contains: str | Unset = UNSET,
    directory_endswith: str | Unset = UNSET,
    directory_gt: str | Unset = UNSET,
    directory_gte: str | Unset = UNSET,
    directory_icontains: str | Unset = UNSET,
    directory_iendswith: str | Unset = UNSET,
    directory_iexact: str | Unset = UNSET,
    directory_in: list[str] | Unset = UNSET,
    directory_iregex: str | Unset = UNSET,
    directory_isnull: bool | Unset = UNSET,
    directory_istartswith: str | Unset = UNSET,
    directory_lt: str | Unset = UNSET,
    directory_lte: str | Unset = UNSET,
    directory_range: list[str] | Unset = UNSET,
    directory_regex: str | Unset = UNSET,
    directory_startswith: str | Unset = UNSET,
    drs_id: str | Unset = UNSET,
    drs_id_contains: str | Unset = UNSET,
    drs_id_endswith: str | Unset = UNSET,
    drs_id_gt: str | Unset = UNSET,
    drs_id_gte: str | Unset = UNSET,
    drs_id_icontains: str | Unset = UNSET,
    drs_id_iendswith: str | Unset = UNSET,
    drs_id_iexact: str | Unset = UNSET,
    drs_id_in: list[str] | Unset = UNSET,
    drs_id_iregex: str | Unset = UNSET,
    drs_id_isnull: bool | Unset = UNSET,
    drs_id_istartswith: str | Unset = UNSET,
    drs_id_lt: str | Unset = UNSET,
    drs_id_lte: str | Unset = UNSET,
    drs_id_range: list[str] | Unset = UNSET,
    drs_id_regex: str | Unset = UNSET,
    drs_id_startswith: str | Unset = UNSET,
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
    related_to: int | Unset = UNSET,
    related_to_in: list[int] | Unset = UNSET,
    related_to_isnull: bool | Unset = UNSET,
    related_to_ob_id: int | Unset = UNSET,
    related_to_ob_id_in: list[int] | Unset = UNSET,
    related_to_short_code: str | Unset = UNSET,
    related_to_short_code_in: list[str] | Unset = UNSET,
    related_to_uuid: str | Unset = UNSET,
    related_to_uuid_in: list[str] | Unset = UNSET,
    version: str | Unset = UNSET,
    version_contains: str | Unset = UNSET,
    version_endswith: str | Unset = UNSET,
    version_gt: str | Unset = UNSET,
    version_gte: str | Unset = UNSET,
    version_icontains: str | Unset = UNSET,
    version_iendswith: str | Unset = UNSET,
    version_iexact: str | Unset = UNSET,
    version_in: list[str] | Unset = UNSET,
    version_iregex: str | Unset = UNSET,
    version_isnull: bool | Unset = UNSET,
    version_istartswith: str | Unset = UNSET,
    version_lt: str | Unset = UNSET,
    version_lte: str | Unset = UNSET,
    version_range: list[str] | Unset = UNSET,
    version_regex: str | Unset = UNSET,
    version_startswith: str | Unset = UNSET,
) -> PaginatedDRSDatasetReadList | None:
    """Get a list of DRSDataset objects.

    Args:
        directory (str | Unset):
        directory_contains (str | Unset):
        directory_endswith (str | Unset):
        directory_gt (str | Unset):
        directory_gte (str | Unset):
        directory_icontains (str | Unset):
        directory_iendswith (str | Unset):
        directory_iexact (str | Unset):
        directory_in (list[str] | Unset):
        directory_iregex (str | Unset):
        directory_isnull (bool | Unset):
        directory_istartswith (str | Unset):
        directory_lt (str | Unset):
        directory_lte (str | Unset):
        directory_range (list[str] | Unset):
        directory_regex (str | Unset):
        directory_startswith (str | Unset):
        drs_id (str | Unset):
        drs_id_contains (str | Unset):
        drs_id_endswith (str | Unset):
        drs_id_gt (str | Unset):
        drs_id_gte (str | Unset):
        drs_id_icontains (str | Unset):
        drs_id_iendswith (str | Unset):
        drs_id_iexact (str | Unset):
        drs_id_in (list[str] | Unset):
        drs_id_iregex (str | Unset):
        drs_id_isnull (bool | Unset):
        drs_id_istartswith (str | Unset):
        drs_id_lt (str | Unset):
        drs_id_lte (str | Unset):
        drs_id_range (list[str] | Unset):
        drs_id_regex (str | Unset):
        drs_id_startswith (str | Unset):
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
        related_to (int | Unset):
        related_to_in (list[int] | Unset):
        related_to_isnull (bool | Unset):
        related_to_ob_id (int | Unset):
        related_to_ob_id_in (list[int] | Unset):
        related_to_short_code (str | Unset):
        related_to_short_code_in (list[str] | Unset):
        related_to_uuid (str | Unset):
        related_to_uuid_in (list[str] | Unset):
        version (str | Unset):
        version_contains (str | Unset):
        version_endswith (str | Unset):
        version_gt (str | Unset):
        version_gte (str | Unset):
        version_icontains (str | Unset):
        version_iendswith (str | Unset):
        version_iexact (str | Unset):
        version_in (list[str] | Unset):
        version_iregex (str | Unset):
        version_isnull (bool | Unset):
        version_istartswith (str | Unset):
        version_lt (str | Unset):
        version_lte (str | Unset):
        version_range (list[str] | Unset):
        version_regex (str | Unset):
        version_startswith (str | Unset):

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
            related_to_in=related_to_in,
            related_to_isnull=related_to_isnull,
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
