from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_licence_read_list import PaginatedLicenceReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    constraints: list[int] | Unset = UNSET,
    constraints_in: list[int] | Unset = UNSET,
    constraints_isnull: bool | Unset = UNSET,
    licence_classifications: list[int] | Unset = UNSET,
    licence_classifications_classification: str | Unset = UNSET,
    licence_classifications_classification_in: list[str] | Unset = UNSET,
    licence_classifications_in: list[int] | Unset = UNSET,
    licence_classifications_isnull: bool | Unset = UNSET,
    licence_classifications_ob_id: int | Unset = UNSET,
    licence_classifications_ob_id_in: list[int] | Unset = UNSET,
    licence_url: str | Unset = UNSET,
    licence_url_contains: str | Unset = UNSET,
    licence_url_endswith: str | Unset = UNSET,
    licence_url_gt: str | Unset = UNSET,
    licence_url_gte: str | Unset = UNSET,
    licence_url_icontains: str | Unset = UNSET,
    licence_url_iendswith: str | Unset = UNSET,
    licence_url_iexact: str | Unset = UNSET,
    licence_url_in: list[str] | Unset = UNSET,
    licence_url_iregex: str | Unset = UNSET,
    licence_url_isnull: bool | Unset = UNSET,
    licence_url_istartswith: str | Unset = UNSET,
    licence_url_lt: str | Unset = UNSET,
    licence_url_lte: str | Unset = UNSET,
    licence_url_range: list[str] | Unset = UNSET,
    licence_url_regex: str | Unset = UNSET,
    licence_url_startswith: str | Unset = UNSET,
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
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_constraints: list[int] | Unset = UNSET
    if not isinstance(constraints, Unset):
        json_constraints = ",".join(map(str, constraints))

    params["constraints"] = json_constraints

    json_constraints_in: list[int] | Unset = UNSET
    if not isinstance(constraints_in, Unset):
        json_constraints_in = ",".join(map(str, constraints_in))

    params["constraints__in"] = json_constraints_in

    params["constraints__isnull"] = constraints_isnull

    json_licence_classifications: list[int] | Unset = UNSET
    if not isinstance(licence_classifications, Unset):
        json_licence_classifications = ",".join(map(str, licence_classifications))

    params["licenceClassifications"] = json_licence_classifications

    params["licenceClassifications__classification"] = licence_classifications_classification

    json_licence_classifications_classification_in: list[str] | Unset = UNSET
    if not isinstance(licence_classifications_classification_in, Unset):
        json_licence_classifications_classification_in = ",".join(map(str, licence_classifications_classification_in))

    params["licenceClassifications__classification__in"] = json_licence_classifications_classification_in

    json_licence_classifications_in: list[int] | Unset = UNSET
    if not isinstance(licence_classifications_in, Unset):
        json_licence_classifications_in = ",".join(map(str, licence_classifications_in))

    params["licenceClassifications__in"] = json_licence_classifications_in

    params["licenceClassifications__isnull"] = licence_classifications_isnull

    params["licenceClassifications__ob_id"] = licence_classifications_ob_id

    json_licence_classifications_ob_id_in: list[int] | Unset = UNSET
    if not isinstance(licence_classifications_ob_id_in, Unset):
        json_licence_classifications_ob_id_in = ",".join(map(str, licence_classifications_ob_id_in))

    params["licenceClassifications__ob_id__in"] = json_licence_classifications_ob_id_in

    params["licenceURL"] = licence_url

    params["licenceURL__contains"] = licence_url_contains

    params["licenceURL__endswith"] = licence_url_endswith

    params["licenceURL__gt"] = licence_url_gt

    params["licenceURL__gte"] = licence_url_gte

    params["licenceURL__icontains"] = licence_url_icontains

    params["licenceURL__iendswith"] = licence_url_iendswith

    params["licenceURL__iexact"] = licence_url_iexact

    json_licence_url_in: list[str] | Unset = UNSET
    if not isinstance(licence_url_in, Unset):
        json_licence_url_in = ",".join(map(str, licence_url_in))

    params["licenceURL__in"] = json_licence_url_in

    params["licenceURL__iregex"] = licence_url_iregex

    params["licenceURL__isnull"] = licence_url_isnull

    params["licenceURL__istartswith"] = licence_url_istartswith

    params["licenceURL__lt"] = licence_url_lt

    params["licenceURL__lte"] = licence_url_lte

    json_licence_url_range: list[str] | Unset = UNSET
    if not isinstance(licence_url_range, Unset):
        json_licence_url_range = ",".join(map(str, licence_url_range))

    params["licenceURL__range"] = json_licence_url_range

    params["licenceURL__regex"] = licence_url_regex

    params["licenceURL__startswith"] = licence_url_startswith

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/licences/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedLicenceReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedLicenceReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedLicenceReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    constraints: list[int] | Unset = UNSET,
    constraints_in: list[int] | Unset = UNSET,
    constraints_isnull: bool | Unset = UNSET,
    licence_classifications: list[int] | Unset = UNSET,
    licence_classifications_classification: str | Unset = UNSET,
    licence_classifications_classification_in: list[str] | Unset = UNSET,
    licence_classifications_in: list[int] | Unset = UNSET,
    licence_classifications_isnull: bool | Unset = UNSET,
    licence_classifications_ob_id: int | Unset = UNSET,
    licence_classifications_ob_id_in: list[int] | Unset = UNSET,
    licence_url: str | Unset = UNSET,
    licence_url_contains: str | Unset = UNSET,
    licence_url_endswith: str | Unset = UNSET,
    licence_url_gt: str | Unset = UNSET,
    licence_url_gte: str | Unset = UNSET,
    licence_url_icontains: str | Unset = UNSET,
    licence_url_iendswith: str | Unset = UNSET,
    licence_url_iexact: str | Unset = UNSET,
    licence_url_in: list[str] | Unset = UNSET,
    licence_url_iregex: str | Unset = UNSET,
    licence_url_isnull: bool | Unset = UNSET,
    licence_url_istartswith: str | Unset = UNSET,
    licence_url_lt: str | Unset = UNSET,
    licence_url_lte: str | Unset = UNSET,
    licence_url_range: list[str] | Unset = UNSET,
    licence_url_regex: str | Unset = UNSET,
    licence_url_startswith: str | Unset = UNSET,
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
) -> Response[PaginatedLicenceReadList]:
    """Get a list of Licence objects.

    Args:
        constraints (list[int] | Unset):
        constraints_in (list[int] | Unset):
        constraints_isnull (bool | Unset):
        licence_classifications (list[int] | Unset):
        licence_classifications_classification (str | Unset):
        licence_classifications_classification_in (list[str] | Unset):
        licence_classifications_in (list[int] | Unset):
        licence_classifications_isnull (bool | Unset):
        licence_classifications_ob_id (int | Unset):
        licence_classifications_ob_id_in (list[int] | Unset):
        licence_url (str | Unset):
        licence_url_contains (str | Unset):
        licence_url_endswith (str | Unset):
        licence_url_gt (str | Unset):
        licence_url_gte (str | Unset):
        licence_url_icontains (str | Unset):
        licence_url_iendswith (str | Unset):
        licence_url_iexact (str | Unset):
        licence_url_in (list[str] | Unset):
        licence_url_iregex (str | Unset):
        licence_url_isnull (bool | Unset):
        licence_url_istartswith (str | Unset):
        licence_url_lt (str | Unset):
        licence_url_lte (str | Unset):
        licence_url_range (list[str] | Unset):
        licence_url_regex (str | Unset):
        licence_url_startswith (str | Unset):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLicenceReadList]
    """

    kwargs = _get_kwargs(
        constraints=constraints,
        constraints_in=constraints_in,
        constraints_isnull=constraints_isnull,
        licence_classifications=licence_classifications,
        licence_classifications_classification=licence_classifications_classification,
        licence_classifications_classification_in=licence_classifications_classification_in,
        licence_classifications_in=licence_classifications_in,
        licence_classifications_isnull=licence_classifications_isnull,
        licence_classifications_ob_id=licence_classifications_ob_id,
        licence_classifications_ob_id_in=licence_classifications_ob_id_in,
        licence_url=licence_url,
        licence_url_contains=licence_url_contains,
        licence_url_endswith=licence_url_endswith,
        licence_url_gt=licence_url_gt,
        licence_url_gte=licence_url_gte,
        licence_url_icontains=licence_url_icontains,
        licence_url_iendswith=licence_url_iendswith,
        licence_url_iexact=licence_url_iexact,
        licence_url_in=licence_url_in,
        licence_url_iregex=licence_url_iregex,
        licence_url_isnull=licence_url_isnull,
        licence_url_istartswith=licence_url_istartswith,
        licence_url_lt=licence_url_lt,
        licence_url_lte=licence_url_lte,
        licence_url_range=licence_url_range,
        licence_url_regex=licence_url_regex,
        licence_url_startswith=licence_url_startswith,
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
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    constraints: list[int] | Unset = UNSET,
    constraints_in: list[int] | Unset = UNSET,
    constraints_isnull: bool | Unset = UNSET,
    licence_classifications: list[int] | Unset = UNSET,
    licence_classifications_classification: str | Unset = UNSET,
    licence_classifications_classification_in: list[str] | Unset = UNSET,
    licence_classifications_in: list[int] | Unset = UNSET,
    licence_classifications_isnull: bool | Unset = UNSET,
    licence_classifications_ob_id: int | Unset = UNSET,
    licence_classifications_ob_id_in: list[int] | Unset = UNSET,
    licence_url: str | Unset = UNSET,
    licence_url_contains: str | Unset = UNSET,
    licence_url_endswith: str | Unset = UNSET,
    licence_url_gt: str | Unset = UNSET,
    licence_url_gte: str | Unset = UNSET,
    licence_url_icontains: str | Unset = UNSET,
    licence_url_iendswith: str | Unset = UNSET,
    licence_url_iexact: str | Unset = UNSET,
    licence_url_in: list[str] | Unset = UNSET,
    licence_url_iregex: str | Unset = UNSET,
    licence_url_isnull: bool | Unset = UNSET,
    licence_url_istartswith: str | Unset = UNSET,
    licence_url_lt: str | Unset = UNSET,
    licence_url_lte: str | Unset = UNSET,
    licence_url_range: list[str] | Unset = UNSET,
    licence_url_regex: str | Unset = UNSET,
    licence_url_startswith: str | Unset = UNSET,
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
) -> PaginatedLicenceReadList | None:
    """Get a list of Licence objects.

    Args:
        constraints (list[int] | Unset):
        constraints_in (list[int] | Unset):
        constraints_isnull (bool | Unset):
        licence_classifications (list[int] | Unset):
        licence_classifications_classification (str | Unset):
        licence_classifications_classification_in (list[str] | Unset):
        licence_classifications_in (list[int] | Unset):
        licence_classifications_isnull (bool | Unset):
        licence_classifications_ob_id (int | Unset):
        licence_classifications_ob_id_in (list[int] | Unset):
        licence_url (str | Unset):
        licence_url_contains (str | Unset):
        licence_url_endswith (str | Unset):
        licence_url_gt (str | Unset):
        licence_url_gte (str | Unset):
        licence_url_icontains (str | Unset):
        licence_url_iendswith (str | Unset):
        licence_url_iexact (str | Unset):
        licence_url_in (list[str] | Unset):
        licence_url_iregex (str | Unset):
        licence_url_isnull (bool | Unset):
        licence_url_istartswith (str | Unset):
        licence_url_lt (str | Unset):
        licence_url_lte (str | Unset):
        licence_url_range (list[str] | Unset):
        licence_url_regex (str | Unset):
        licence_url_startswith (str | Unset):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLicenceReadList
    """

    return sync_detailed(
        client=client,
        constraints=constraints,
        constraints_in=constraints_in,
        constraints_isnull=constraints_isnull,
        licence_classifications=licence_classifications,
        licence_classifications_classification=licence_classifications_classification,
        licence_classifications_classification_in=licence_classifications_classification_in,
        licence_classifications_in=licence_classifications_in,
        licence_classifications_isnull=licence_classifications_isnull,
        licence_classifications_ob_id=licence_classifications_ob_id,
        licence_classifications_ob_id_in=licence_classifications_ob_id_in,
        licence_url=licence_url,
        licence_url_contains=licence_url_contains,
        licence_url_endswith=licence_url_endswith,
        licence_url_gt=licence_url_gt,
        licence_url_gte=licence_url_gte,
        licence_url_icontains=licence_url_icontains,
        licence_url_iendswith=licence_url_iendswith,
        licence_url_iexact=licence_url_iexact,
        licence_url_in=licence_url_in,
        licence_url_iregex=licence_url_iregex,
        licence_url_isnull=licence_url_isnull,
        licence_url_istartswith=licence_url_istartswith,
        licence_url_lt=licence_url_lt,
        licence_url_lte=licence_url_lte,
        licence_url_range=licence_url_range,
        licence_url_regex=licence_url_regex,
        licence_url_startswith=licence_url_startswith,
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    constraints: list[int] | Unset = UNSET,
    constraints_in: list[int] | Unset = UNSET,
    constraints_isnull: bool | Unset = UNSET,
    licence_classifications: list[int] | Unset = UNSET,
    licence_classifications_classification: str | Unset = UNSET,
    licence_classifications_classification_in: list[str] | Unset = UNSET,
    licence_classifications_in: list[int] | Unset = UNSET,
    licence_classifications_isnull: bool | Unset = UNSET,
    licence_classifications_ob_id: int | Unset = UNSET,
    licence_classifications_ob_id_in: list[int] | Unset = UNSET,
    licence_url: str | Unset = UNSET,
    licence_url_contains: str | Unset = UNSET,
    licence_url_endswith: str | Unset = UNSET,
    licence_url_gt: str | Unset = UNSET,
    licence_url_gte: str | Unset = UNSET,
    licence_url_icontains: str | Unset = UNSET,
    licence_url_iendswith: str | Unset = UNSET,
    licence_url_iexact: str | Unset = UNSET,
    licence_url_in: list[str] | Unset = UNSET,
    licence_url_iregex: str | Unset = UNSET,
    licence_url_isnull: bool | Unset = UNSET,
    licence_url_istartswith: str | Unset = UNSET,
    licence_url_lt: str | Unset = UNSET,
    licence_url_lte: str | Unset = UNSET,
    licence_url_range: list[str] | Unset = UNSET,
    licence_url_regex: str | Unset = UNSET,
    licence_url_startswith: str | Unset = UNSET,
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
) -> Response[PaginatedLicenceReadList]:
    """Get a list of Licence objects.

    Args:
        constraints (list[int] | Unset):
        constraints_in (list[int] | Unset):
        constraints_isnull (bool | Unset):
        licence_classifications (list[int] | Unset):
        licence_classifications_classification (str | Unset):
        licence_classifications_classification_in (list[str] | Unset):
        licence_classifications_in (list[int] | Unset):
        licence_classifications_isnull (bool | Unset):
        licence_classifications_ob_id (int | Unset):
        licence_classifications_ob_id_in (list[int] | Unset):
        licence_url (str | Unset):
        licence_url_contains (str | Unset):
        licence_url_endswith (str | Unset):
        licence_url_gt (str | Unset):
        licence_url_gte (str | Unset):
        licence_url_icontains (str | Unset):
        licence_url_iendswith (str | Unset):
        licence_url_iexact (str | Unset):
        licence_url_in (list[str] | Unset):
        licence_url_iregex (str | Unset):
        licence_url_isnull (bool | Unset):
        licence_url_istartswith (str | Unset):
        licence_url_lt (str | Unset):
        licence_url_lte (str | Unset):
        licence_url_range (list[str] | Unset):
        licence_url_regex (str | Unset):
        licence_url_startswith (str | Unset):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedLicenceReadList]
    """

    kwargs = _get_kwargs(
        constraints=constraints,
        constraints_in=constraints_in,
        constraints_isnull=constraints_isnull,
        licence_classifications=licence_classifications,
        licence_classifications_classification=licence_classifications_classification,
        licence_classifications_classification_in=licence_classifications_classification_in,
        licence_classifications_in=licence_classifications_in,
        licence_classifications_isnull=licence_classifications_isnull,
        licence_classifications_ob_id=licence_classifications_ob_id,
        licence_classifications_ob_id_in=licence_classifications_ob_id_in,
        licence_url=licence_url,
        licence_url_contains=licence_url_contains,
        licence_url_endswith=licence_url_endswith,
        licence_url_gt=licence_url_gt,
        licence_url_gte=licence_url_gte,
        licence_url_icontains=licence_url_icontains,
        licence_url_iendswith=licence_url_iendswith,
        licence_url_iexact=licence_url_iexact,
        licence_url_in=licence_url_in,
        licence_url_iregex=licence_url_iregex,
        licence_url_isnull=licence_url_isnull,
        licence_url_istartswith=licence_url_istartswith,
        licence_url_lt=licence_url_lt,
        licence_url_lte=licence_url_lte,
        licence_url_range=licence_url_range,
        licence_url_regex=licence_url_regex,
        licence_url_startswith=licence_url_startswith,
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
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    constraints: list[int] | Unset = UNSET,
    constraints_in: list[int] | Unset = UNSET,
    constraints_isnull: bool | Unset = UNSET,
    licence_classifications: list[int] | Unset = UNSET,
    licence_classifications_classification: str | Unset = UNSET,
    licence_classifications_classification_in: list[str] | Unset = UNSET,
    licence_classifications_in: list[int] | Unset = UNSET,
    licence_classifications_isnull: bool | Unset = UNSET,
    licence_classifications_ob_id: int | Unset = UNSET,
    licence_classifications_ob_id_in: list[int] | Unset = UNSET,
    licence_url: str | Unset = UNSET,
    licence_url_contains: str | Unset = UNSET,
    licence_url_endswith: str | Unset = UNSET,
    licence_url_gt: str | Unset = UNSET,
    licence_url_gte: str | Unset = UNSET,
    licence_url_icontains: str | Unset = UNSET,
    licence_url_iendswith: str | Unset = UNSET,
    licence_url_iexact: str | Unset = UNSET,
    licence_url_in: list[str] | Unset = UNSET,
    licence_url_iregex: str | Unset = UNSET,
    licence_url_isnull: bool | Unset = UNSET,
    licence_url_istartswith: str | Unset = UNSET,
    licence_url_lt: str | Unset = UNSET,
    licence_url_lte: str | Unset = UNSET,
    licence_url_range: list[str] | Unset = UNSET,
    licence_url_regex: str | Unset = UNSET,
    licence_url_startswith: str | Unset = UNSET,
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
) -> PaginatedLicenceReadList | None:
    """Get a list of Licence objects.

    Args:
        constraints (list[int] | Unset):
        constraints_in (list[int] | Unset):
        constraints_isnull (bool | Unset):
        licence_classifications (list[int] | Unset):
        licence_classifications_classification (str | Unset):
        licence_classifications_classification_in (list[str] | Unset):
        licence_classifications_in (list[int] | Unset):
        licence_classifications_isnull (bool | Unset):
        licence_classifications_ob_id (int | Unset):
        licence_classifications_ob_id_in (list[int] | Unset):
        licence_url (str | Unset):
        licence_url_contains (str | Unset):
        licence_url_endswith (str | Unset):
        licence_url_gt (str | Unset):
        licence_url_gte (str | Unset):
        licence_url_icontains (str | Unset):
        licence_url_iendswith (str | Unset):
        licence_url_iexact (str | Unset):
        licence_url_in (list[str] | Unset):
        licence_url_iregex (str | Unset):
        licence_url_isnull (bool | Unset):
        licence_url_istartswith (str | Unset):
        licence_url_lt (str | Unset):
        licence_url_lte (str | Unset):
        licence_url_range (list[str] | Unset):
        licence_url_regex (str | Unset):
        licence_url_startswith (str | Unset):
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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedLicenceReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            constraints=constraints,
            constraints_in=constraints_in,
            constraints_isnull=constraints_isnull,
            licence_classifications=licence_classifications,
            licence_classifications_classification=licence_classifications_classification,
            licence_classifications_classification_in=licence_classifications_classification_in,
            licence_classifications_in=licence_classifications_in,
            licence_classifications_isnull=licence_classifications_isnull,
            licence_classifications_ob_id=licence_classifications_ob_id,
            licence_classifications_ob_id_in=licence_classifications_ob_id_in,
            licence_url=licence_url,
            licence_url_contains=licence_url_contains,
            licence_url_endswith=licence_url_endswith,
            licence_url_gt=licence_url_gt,
            licence_url_gte=licence_url_gte,
            licence_url_icontains=licence_url_icontains,
            licence_url_iendswith=licence_url_iendswith,
            licence_url_iexact=licence_url_iexact,
            licence_url_in=licence_url_in,
            licence_url_iregex=licence_url_iregex,
            licence_url_isnull=licence_url_isnull,
            licence_url_istartswith=licence_url_istartswith,
            licence_url_lt=licence_url_lt,
            licence_url_lte=licence_url_lte,
            licence_url_range=licence_url_range,
            licence_url_regex=licence_url_regex,
            licence_url_startswith=licence_url_startswith,
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
        )
    ).parsed
