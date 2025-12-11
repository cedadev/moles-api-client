from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_input_output_description_read_list import PaginatedInputOutputDescriptionReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    computation_input_description: list[int] | Unset = UNSET,
    computation_input_description_in: list[int] | Unset = UNSET,
    computation_input_description_isnull: bool | Unset = UNSET,
    computation_output_description: list[int] | Unset = UNSET,
    computation_output_description_in: list[int] | Unset = UNSET,
    computation_output_description_isnull: bool | Unset = UNSET,
    description: str | Unset = UNSET,
    description_contains: str | Unset = UNSET,
    description_endswith: str | Unset = UNSET,
    description_gt: str | Unset = UNSET,
    description_gte: str | Unset = UNSET,
    description_icontains: str | Unset = UNSET,
    description_iendswith: str | Unset = UNSET,
    description_iexact: str | Unset = UNSET,
    description_in: list[str] | Unset = UNSET,
    description_iregex: str | Unset = UNSET,
    description_isnull: bool | Unset = UNSET,
    description_istartswith: str | Unset = UNSET,
    description_lt: str | Unset = UNSET,
    description_lte: str | Unset = UNSET,
    description_range: list[str] | Unset = UNSET,
    description_regex: str | Unset = UNSET,
    description_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    name_endswith: str | Unset = UNSET,
    name_gt: str | Unset = UNSET,
    name_gte: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_in: list[str] | Unset = UNSET,
    name_iregex: str | Unset = UNSET,
    name_isnull: bool | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    name_lt: str | Unset = UNSET,
    name_lte: str | Unset = UNSET,
    name_range: list[str] | Unset = UNSET,
    name_regex: str | Unset = UNSET,
    name_startswith: str | Unset = UNSET,
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

    json_acquisition: list[int] | Unset = UNSET
    if not isinstance(acquisition, Unset):
        json_acquisition = acquisition

    params["acquisition"] = json_acquisition

    json_acquisition_in: list[int] | Unset = UNSET
    if not isinstance(acquisition_in, Unset):
        json_acquisition_in = acquisition_in

    params["acquisition__in"] = json_acquisition_in

    params["acquisition__isnull"] = acquisition_isnull

    json_computation_input_description: list[int] | Unset = UNSET
    if not isinstance(computation_input_description, Unset):
        json_computation_input_description = computation_input_description

    params["computationInputDescription"] = json_computation_input_description

    json_computation_input_description_in: list[int] | Unset = UNSET
    if not isinstance(computation_input_description_in, Unset):
        json_computation_input_description_in = computation_input_description_in

    params["computationInputDescription__in"] = json_computation_input_description_in

    params["computationInputDescription__isnull"] = computation_input_description_isnull

    json_computation_output_description: list[int] | Unset = UNSET
    if not isinstance(computation_output_description, Unset):
        json_computation_output_description = computation_output_description

    params["computationOutputDescription"] = json_computation_output_description

    json_computation_output_description_in: list[int] | Unset = UNSET
    if not isinstance(computation_output_description_in, Unset):
        json_computation_output_description_in = computation_output_description_in

    params["computationOutputDescription__in"] = json_computation_output_description_in

    params["computationOutputDescription__isnull"] = computation_output_description_isnull

    params["description"] = description

    params["description__contains"] = description_contains

    params["description__endswith"] = description_endswith

    params["description__gt"] = description_gt

    params["description__gte"] = description_gte

    params["description__icontains"] = description_icontains

    params["description__iendswith"] = description_iendswith

    params["description__iexact"] = description_iexact

    json_description_in: list[str] | Unset = UNSET
    if not isinstance(description_in, Unset):
        json_description_in = description_in

    params["description__in"] = json_description_in

    params["description__iregex"] = description_iregex

    params["description__isnull"] = description_isnull

    params["description__istartswith"] = description_istartswith

    params["description__lt"] = description_lt

    params["description__lte"] = description_lte

    json_description_range: list[str] | Unset = UNSET
    if not isinstance(description_range, Unset):
        json_description_range = description_range

    params["description__range"] = json_description_range

    params["description__regex"] = description_regex

    params["description__startswith"] = description_startswith

    params["limit"] = limit

    params["name"] = name

    params["name__contains"] = name_contains

    params["name__endswith"] = name_endswith

    params["name__gt"] = name_gt

    params["name__gte"] = name_gte

    params["name__icontains"] = name_icontains

    params["name__iendswith"] = name_iendswith

    params["name__iexact"] = name_iexact

    json_name_in: list[str] | Unset = UNSET
    if not isinstance(name_in, Unset):
        json_name_in = name_in

    params["name__in"] = json_name_in

    params["name__iregex"] = name_iregex

    params["name__isnull"] = name_isnull

    params["name__istartswith"] = name_istartswith

    params["name__lt"] = name_lt

    params["name__lte"] = name_lte

    json_name_range: list[str] | Unset = UNSET
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/iods/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedInputOutputDescriptionReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedInputOutputDescriptionReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedInputOutputDescriptionReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    computation_input_description: list[int] | Unset = UNSET,
    computation_input_description_in: list[int] | Unset = UNSET,
    computation_input_description_isnull: bool | Unset = UNSET,
    computation_output_description: list[int] | Unset = UNSET,
    computation_output_description_in: list[int] | Unset = UNSET,
    computation_output_description_isnull: bool | Unset = UNSET,
    description: str | Unset = UNSET,
    description_contains: str | Unset = UNSET,
    description_endswith: str | Unset = UNSET,
    description_gt: str | Unset = UNSET,
    description_gte: str | Unset = UNSET,
    description_icontains: str | Unset = UNSET,
    description_iendswith: str | Unset = UNSET,
    description_iexact: str | Unset = UNSET,
    description_in: list[str] | Unset = UNSET,
    description_iregex: str | Unset = UNSET,
    description_isnull: bool | Unset = UNSET,
    description_istartswith: str | Unset = UNSET,
    description_lt: str | Unset = UNSET,
    description_lte: str | Unset = UNSET,
    description_range: list[str] | Unset = UNSET,
    description_regex: str | Unset = UNSET,
    description_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    name_endswith: str | Unset = UNSET,
    name_gt: str | Unset = UNSET,
    name_gte: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_in: list[str] | Unset = UNSET,
    name_iregex: str | Unset = UNSET,
    name_isnull: bool | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    name_lt: str | Unset = UNSET,
    name_lte: str | Unset = UNSET,
    name_range: list[str] | Unset = UNSET,
    name_regex: str | Unset = UNSET,
    name_startswith: str | Unset = UNSET,
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
) -> Response[PaginatedInputOutputDescriptionReadList]:
    """Get a list of InputOutputDescription objects.

    Args:
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        computation_input_description (list[int] | Unset):
        computation_input_description_in (list[int] | Unset):
        computation_input_description_isnull (bool | Unset):
        computation_output_description (list[int] | Unset):
        computation_output_description_in (list[int] | Unset):
        computation_output_description_isnull (bool | Unset):
        description (str | Unset):
        description_contains (str | Unset):
        description_endswith (str | Unset):
        description_gt (str | Unset):
        description_gte (str | Unset):
        description_icontains (str | Unset):
        description_iendswith (str | Unset):
        description_iexact (str | Unset):
        description_in (list[str] | Unset):
        description_iregex (str | Unset):
        description_isnull (bool | Unset):
        description_istartswith (str | Unset):
        description_lt (str | Unset):
        description_lte (str | Unset):
        description_range (list[str] | Unset):
        description_regex (str | Unset):
        description_startswith (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_contains (str | Unset):
        name_endswith (str | Unset):
        name_gt (str | Unset):
        name_gte (str | Unset):
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_in (list[str] | Unset):
        name_iregex (str | Unset):
        name_isnull (bool | Unset):
        name_istartswith (str | Unset):
        name_lt (str | Unset):
        name_lte (str | Unset):
        name_range (list[str] | Unset):
        name_regex (str | Unset):
        name_startswith (str | Unset):
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
        Response[PaginatedInputOutputDescriptionReadList]
    """

    kwargs = _get_kwargs(
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        computation_input_description=computation_input_description,
        computation_input_description_in=computation_input_description_in,
        computation_input_description_isnull=computation_input_description_isnull,
        computation_output_description=computation_output_description,
        computation_output_description_in=computation_output_description_in,
        computation_output_description_isnull=computation_output_description_isnull,
        description=description,
        description_contains=description_contains,
        description_endswith=description_endswith,
        description_gt=description_gt,
        description_gte=description_gte,
        description_icontains=description_icontains,
        description_iendswith=description_iendswith,
        description_iexact=description_iexact,
        description_in=description_in,
        description_iregex=description_iregex,
        description_isnull=description_isnull,
        description_istartswith=description_istartswith,
        description_lt=description_lt,
        description_lte=description_lte,
        description_range=description_range,
        description_regex=description_regex,
        description_startswith=description_startswith,
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
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    computation_input_description: list[int] | Unset = UNSET,
    computation_input_description_in: list[int] | Unset = UNSET,
    computation_input_description_isnull: bool | Unset = UNSET,
    computation_output_description: list[int] | Unset = UNSET,
    computation_output_description_in: list[int] | Unset = UNSET,
    computation_output_description_isnull: bool | Unset = UNSET,
    description: str | Unset = UNSET,
    description_contains: str | Unset = UNSET,
    description_endswith: str | Unset = UNSET,
    description_gt: str | Unset = UNSET,
    description_gte: str | Unset = UNSET,
    description_icontains: str | Unset = UNSET,
    description_iendswith: str | Unset = UNSET,
    description_iexact: str | Unset = UNSET,
    description_in: list[str] | Unset = UNSET,
    description_iregex: str | Unset = UNSET,
    description_isnull: bool | Unset = UNSET,
    description_istartswith: str | Unset = UNSET,
    description_lt: str | Unset = UNSET,
    description_lte: str | Unset = UNSET,
    description_range: list[str] | Unset = UNSET,
    description_regex: str | Unset = UNSET,
    description_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    name_endswith: str | Unset = UNSET,
    name_gt: str | Unset = UNSET,
    name_gte: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_in: list[str] | Unset = UNSET,
    name_iregex: str | Unset = UNSET,
    name_isnull: bool | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    name_lt: str | Unset = UNSET,
    name_lte: str | Unset = UNSET,
    name_range: list[str] | Unset = UNSET,
    name_regex: str | Unset = UNSET,
    name_startswith: str | Unset = UNSET,
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
) -> PaginatedInputOutputDescriptionReadList | None:
    """Get a list of InputOutputDescription objects.

    Args:
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        computation_input_description (list[int] | Unset):
        computation_input_description_in (list[int] | Unset):
        computation_input_description_isnull (bool | Unset):
        computation_output_description (list[int] | Unset):
        computation_output_description_in (list[int] | Unset):
        computation_output_description_isnull (bool | Unset):
        description (str | Unset):
        description_contains (str | Unset):
        description_endswith (str | Unset):
        description_gt (str | Unset):
        description_gte (str | Unset):
        description_icontains (str | Unset):
        description_iendswith (str | Unset):
        description_iexact (str | Unset):
        description_in (list[str] | Unset):
        description_iregex (str | Unset):
        description_isnull (bool | Unset):
        description_istartswith (str | Unset):
        description_lt (str | Unset):
        description_lte (str | Unset):
        description_range (list[str] | Unset):
        description_regex (str | Unset):
        description_startswith (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_contains (str | Unset):
        name_endswith (str | Unset):
        name_gt (str | Unset):
        name_gte (str | Unset):
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_in (list[str] | Unset):
        name_iregex (str | Unset):
        name_isnull (bool | Unset):
        name_istartswith (str | Unset):
        name_lt (str | Unset):
        name_lte (str | Unset):
        name_range (list[str] | Unset):
        name_regex (str | Unset):
        name_startswith (str | Unset):
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
        PaginatedInputOutputDescriptionReadList
    """

    return sync_detailed(
        client=client,
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        computation_input_description=computation_input_description,
        computation_input_description_in=computation_input_description_in,
        computation_input_description_isnull=computation_input_description_isnull,
        computation_output_description=computation_output_description,
        computation_output_description_in=computation_output_description_in,
        computation_output_description_isnull=computation_output_description_isnull,
        description=description,
        description_contains=description_contains,
        description_endswith=description_endswith,
        description_gt=description_gt,
        description_gte=description_gte,
        description_icontains=description_icontains,
        description_iendswith=description_iendswith,
        description_iexact=description_iexact,
        description_in=description_in,
        description_iregex=description_iregex,
        description_isnull=description_isnull,
        description_istartswith=description_istartswith,
        description_lt=description_lt,
        description_lte=description_lte,
        description_range=description_range,
        description_regex=description_regex,
        description_startswith=description_startswith,
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
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    computation_input_description: list[int] | Unset = UNSET,
    computation_input_description_in: list[int] | Unset = UNSET,
    computation_input_description_isnull: bool | Unset = UNSET,
    computation_output_description: list[int] | Unset = UNSET,
    computation_output_description_in: list[int] | Unset = UNSET,
    computation_output_description_isnull: bool | Unset = UNSET,
    description: str | Unset = UNSET,
    description_contains: str | Unset = UNSET,
    description_endswith: str | Unset = UNSET,
    description_gt: str | Unset = UNSET,
    description_gte: str | Unset = UNSET,
    description_icontains: str | Unset = UNSET,
    description_iendswith: str | Unset = UNSET,
    description_iexact: str | Unset = UNSET,
    description_in: list[str] | Unset = UNSET,
    description_iregex: str | Unset = UNSET,
    description_isnull: bool | Unset = UNSET,
    description_istartswith: str | Unset = UNSET,
    description_lt: str | Unset = UNSET,
    description_lte: str | Unset = UNSET,
    description_range: list[str] | Unset = UNSET,
    description_regex: str | Unset = UNSET,
    description_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    name_endswith: str | Unset = UNSET,
    name_gt: str | Unset = UNSET,
    name_gte: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_in: list[str] | Unset = UNSET,
    name_iregex: str | Unset = UNSET,
    name_isnull: bool | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    name_lt: str | Unset = UNSET,
    name_lte: str | Unset = UNSET,
    name_range: list[str] | Unset = UNSET,
    name_regex: str | Unset = UNSET,
    name_startswith: str | Unset = UNSET,
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
) -> Response[PaginatedInputOutputDescriptionReadList]:
    """Get a list of InputOutputDescription objects.

    Args:
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        computation_input_description (list[int] | Unset):
        computation_input_description_in (list[int] | Unset):
        computation_input_description_isnull (bool | Unset):
        computation_output_description (list[int] | Unset):
        computation_output_description_in (list[int] | Unset):
        computation_output_description_isnull (bool | Unset):
        description (str | Unset):
        description_contains (str | Unset):
        description_endswith (str | Unset):
        description_gt (str | Unset):
        description_gte (str | Unset):
        description_icontains (str | Unset):
        description_iendswith (str | Unset):
        description_iexact (str | Unset):
        description_in (list[str] | Unset):
        description_iregex (str | Unset):
        description_isnull (bool | Unset):
        description_istartswith (str | Unset):
        description_lt (str | Unset):
        description_lte (str | Unset):
        description_range (list[str] | Unset):
        description_regex (str | Unset):
        description_startswith (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_contains (str | Unset):
        name_endswith (str | Unset):
        name_gt (str | Unset):
        name_gte (str | Unset):
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_in (list[str] | Unset):
        name_iregex (str | Unset):
        name_isnull (bool | Unset):
        name_istartswith (str | Unset):
        name_lt (str | Unset):
        name_lte (str | Unset):
        name_range (list[str] | Unset):
        name_regex (str | Unset):
        name_startswith (str | Unset):
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
        Response[PaginatedInputOutputDescriptionReadList]
    """

    kwargs = _get_kwargs(
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        computation_input_description=computation_input_description,
        computation_input_description_in=computation_input_description_in,
        computation_input_description_isnull=computation_input_description_isnull,
        computation_output_description=computation_output_description,
        computation_output_description_in=computation_output_description_in,
        computation_output_description_isnull=computation_output_description_isnull,
        description=description,
        description_contains=description_contains,
        description_endswith=description_endswith,
        description_gt=description_gt,
        description_gte=description_gte,
        description_icontains=description_icontains,
        description_iendswith=description_iendswith,
        description_iexact=description_iexact,
        description_in=description_in,
        description_iregex=description_iregex,
        description_isnull=description_isnull,
        description_istartswith=description_istartswith,
        description_lt=description_lt,
        description_lte=description_lte,
        description_range=description_range,
        description_regex=description_regex,
        description_startswith=description_startswith,
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
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    computation_input_description: list[int] | Unset = UNSET,
    computation_input_description_in: list[int] | Unset = UNSET,
    computation_input_description_isnull: bool | Unset = UNSET,
    computation_output_description: list[int] | Unset = UNSET,
    computation_output_description_in: list[int] | Unset = UNSET,
    computation_output_description_isnull: bool | Unset = UNSET,
    description: str | Unset = UNSET,
    description_contains: str | Unset = UNSET,
    description_endswith: str | Unset = UNSET,
    description_gt: str | Unset = UNSET,
    description_gte: str | Unset = UNSET,
    description_icontains: str | Unset = UNSET,
    description_iendswith: str | Unset = UNSET,
    description_iexact: str | Unset = UNSET,
    description_in: list[str] | Unset = UNSET,
    description_iregex: str | Unset = UNSET,
    description_isnull: bool | Unset = UNSET,
    description_istartswith: str | Unset = UNSET,
    description_lt: str | Unset = UNSET,
    description_lte: str | Unset = UNSET,
    description_range: list[str] | Unset = UNSET,
    description_regex: str | Unset = UNSET,
    description_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    name: str | Unset = UNSET,
    name_contains: str | Unset = UNSET,
    name_endswith: str | Unset = UNSET,
    name_gt: str | Unset = UNSET,
    name_gte: str | Unset = UNSET,
    name_icontains: str | Unset = UNSET,
    name_iendswith: str | Unset = UNSET,
    name_iexact: str | Unset = UNSET,
    name_in: list[str] | Unset = UNSET,
    name_iregex: str | Unset = UNSET,
    name_isnull: bool | Unset = UNSET,
    name_istartswith: str | Unset = UNSET,
    name_lt: str | Unset = UNSET,
    name_lte: str | Unset = UNSET,
    name_range: list[str] | Unset = UNSET,
    name_regex: str | Unset = UNSET,
    name_startswith: str | Unset = UNSET,
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
) -> PaginatedInputOutputDescriptionReadList | None:
    """Get a list of InputOutputDescription objects.

    Args:
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        computation_input_description (list[int] | Unset):
        computation_input_description_in (list[int] | Unset):
        computation_input_description_isnull (bool | Unset):
        computation_output_description (list[int] | Unset):
        computation_output_description_in (list[int] | Unset):
        computation_output_description_isnull (bool | Unset):
        description (str | Unset):
        description_contains (str | Unset):
        description_endswith (str | Unset):
        description_gt (str | Unset):
        description_gte (str | Unset):
        description_icontains (str | Unset):
        description_iendswith (str | Unset):
        description_iexact (str | Unset):
        description_in (list[str] | Unset):
        description_iregex (str | Unset):
        description_isnull (bool | Unset):
        description_istartswith (str | Unset):
        description_lt (str | Unset):
        description_lte (str | Unset):
        description_range (list[str] | Unset):
        description_regex (str | Unset):
        description_startswith (str | Unset):
        limit (int | Unset):
        name (str | Unset):
        name_contains (str | Unset):
        name_endswith (str | Unset):
        name_gt (str | Unset):
        name_gte (str | Unset):
        name_icontains (str | Unset):
        name_iendswith (str | Unset):
        name_iexact (str | Unset):
        name_in (list[str] | Unset):
        name_iregex (str | Unset):
        name_isnull (bool | Unset):
        name_istartswith (str | Unset):
        name_lt (str | Unset):
        name_lte (str | Unset):
        name_range (list[str] | Unset):
        name_regex (str | Unset):
        name_startswith (str | Unset):
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
        PaginatedInputOutputDescriptionReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            acquisition=acquisition,
            acquisition_in=acquisition_in,
            acquisition_isnull=acquisition_isnull,
            computation_input_description=computation_input_description,
            computation_input_description_in=computation_input_description_in,
            computation_input_description_isnull=computation_input_description_isnull,
            computation_output_description=computation_output_description,
            computation_output_description_in=computation_output_description_in,
            computation_output_description_isnull=computation_output_description_isnull,
            description=description,
            description_contains=description_contains,
            description_endswith=description_endswith,
            description_gt=description_gt,
            description_gte=description_gte,
            description_icontains=description_icontains,
            description_iendswith=description_iendswith,
            description_iexact=description_iexact,
            description_in=description_in,
            description_iregex=description_iregex,
            description_isnull=description_isnull,
            description_istartswith=description_istartswith,
            description_lt=description_lt,
            description_lte=description_lte,
            description_range=description_range,
            description_regex=description_regex,
            description_startswith=description_startswith,
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
