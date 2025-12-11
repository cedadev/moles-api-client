from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_image_details_read_list import PaginatedImageDetailsReadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    computation: list[int] | Unset = UNSET,
    computation_in: list[int] | Unset = UNSET,
    computation_isnull: bool | Unset = UNSET,
    file_description: str | Unset = UNSET,
    file_description_contains: str | Unset = UNSET,
    file_description_endswith: str | Unset = UNSET,
    file_description_gt: str | Unset = UNSET,
    file_description_gte: str | Unset = UNSET,
    file_description_icontains: str | Unset = UNSET,
    file_description_iendswith: str | Unset = UNSET,
    file_description_iexact: str | Unset = UNSET,
    file_description_in: list[str] | Unset = UNSET,
    file_description_iregex: str | Unset = UNSET,
    file_description_isnull: bool | Unset = UNSET,
    file_description_istartswith: str | Unset = UNSET,
    file_description_lt: str | Unset = UNSET,
    file_description_lte: str | Unset = UNSET,
    file_description_range: list[str] | Unset = UNSET,
    file_description_regex: str | Unset = UNSET,
    file_description_startswith: str | Unset = UNSET,
    file_name: str | Unset = UNSET,
    file_name_contains: str | Unset = UNSET,
    file_name_endswith: str | Unset = UNSET,
    file_name_gt: str | Unset = UNSET,
    file_name_gte: str | Unset = UNSET,
    file_name_icontains: str | Unset = UNSET,
    file_name_iendswith: str | Unset = UNSET,
    file_name_iexact: str | Unset = UNSET,
    file_name_in: list[str] | Unset = UNSET,
    file_name_iregex: str | Unset = UNSET,
    file_name_isnull: bool | Unset = UNSET,
    file_name_istartswith: str | Unset = UNSET,
    file_name_lt: str | Unset = UNSET,
    file_name_lte: str | Unset = UNSET,
    file_name_range: list[str] | Unset = UNSET,
    file_name_regex: str | Unset = UNSET,
    file_name_startswith: str | Unset = UNSET,
    image_constraints: int | Unset = UNSET,
    image_constraints_in: list[int] | Unset = UNSET,
    image_constraints_isnull: bool | Unset = UNSET,
    instrument: list[int] | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    linkage: str | Unset = UNSET,
    linkage_contains: str | Unset = UNSET,
    linkage_endswith: str | Unset = UNSET,
    linkage_gt: str | Unset = UNSET,
    linkage_gte: str | Unset = UNSET,
    linkage_icontains: str | Unset = UNSET,
    linkage_iendswith: str | Unset = UNSET,
    linkage_iexact: str | Unset = UNSET,
    linkage_in: list[str] | Unset = UNSET,
    linkage_iregex: str | Unset = UNSET,
    linkage_isnull: bool | Unset = UNSET,
    linkage_istartswith: str | Unset = UNSET,
    linkage_lt: str | Unset = UNSET,
    linkage_lte: str | Unset = UNSET,
    linkage_range: list[str] | Unset = UNSET,
    linkage_regex: str | Unset = UNSET,
    linkage_startswith: str | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    observationcollection: list[int] | Unset = UNSET,
    observationcollection_in: list[int] | Unset = UNSET,
    observationcollection_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform: list[int] | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    project: list[int] | Unset = UNSET,
    project_in: list[int] | Unset = UNSET,
    project_isnull: bool | Unset = UNSET,
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

    json_computation: list[int] | Unset = UNSET
    if not isinstance(computation, Unset):
        json_computation = computation

    params["computation"] = json_computation

    json_computation_in: list[int] | Unset = UNSET
    if not isinstance(computation_in, Unset):
        json_computation_in = computation_in

    params["computation__in"] = json_computation_in

    params["computation__isnull"] = computation_isnull

    params["fileDescription"] = file_description

    params["fileDescription__contains"] = file_description_contains

    params["fileDescription__endswith"] = file_description_endswith

    params["fileDescription__gt"] = file_description_gt

    params["fileDescription__gte"] = file_description_gte

    params["fileDescription__icontains"] = file_description_icontains

    params["fileDescription__iendswith"] = file_description_iendswith

    params["fileDescription__iexact"] = file_description_iexact

    json_file_description_in: list[str] | Unset = UNSET
    if not isinstance(file_description_in, Unset):
        json_file_description_in = file_description_in

    params["fileDescription__in"] = json_file_description_in

    params["fileDescription__iregex"] = file_description_iregex

    params["fileDescription__isnull"] = file_description_isnull

    params["fileDescription__istartswith"] = file_description_istartswith

    params["fileDescription__lt"] = file_description_lt

    params["fileDescription__lte"] = file_description_lte

    json_file_description_range: list[str] | Unset = UNSET
    if not isinstance(file_description_range, Unset):
        json_file_description_range = file_description_range

    params["fileDescription__range"] = json_file_description_range

    params["fileDescription__regex"] = file_description_regex

    params["fileDescription__startswith"] = file_description_startswith

    params["fileName"] = file_name

    params["fileName__contains"] = file_name_contains

    params["fileName__endswith"] = file_name_endswith

    params["fileName__gt"] = file_name_gt

    params["fileName__gte"] = file_name_gte

    params["fileName__icontains"] = file_name_icontains

    params["fileName__iendswith"] = file_name_iendswith

    params["fileName__iexact"] = file_name_iexact

    json_file_name_in: list[str] | Unset = UNSET
    if not isinstance(file_name_in, Unset):
        json_file_name_in = file_name_in

    params["fileName__in"] = json_file_name_in

    params["fileName__iregex"] = file_name_iregex

    params["fileName__isnull"] = file_name_isnull

    params["fileName__istartswith"] = file_name_istartswith

    params["fileName__lt"] = file_name_lt

    params["fileName__lte"] = file_name_lte

    json_file_name_range: list[str] | Unset = UNSET
    if not isinstance(file_name_range, Unset):
        json_file_name_range = file_name_range

    params["fileName__range"] = json_file_name_range

    params["fileName__regex"] = file_name_regex

    params["fileName__startswith"] = file_name_startswith

    params["imageConstraints"] = image_constraints

    json_image_constraints_in: list[int] | Unset = UNSET
    if not isinstance(image_constraints_in, Unset):
        json_image_constraints_in = image_constraints_in

    params["imageConstraints__in"] = json_image_constraints_in

    params["imageConstraints__isnull"] = image_constraints_isnull

    json_instrument: list[int] | Unset = UNSET
    if not isinstance(instrument, Unset):
        json_instrument = instrument

    params["instrument"] = json_instrument

    json_instrument_in: list[int] | Unset = UNSET
    if not isinstance(instrument_in, Unset):
        json_instrument_in = instrument_in

    params["instrument__in"] = json_instrument_in

    params["instrument__isnull"] = instrument_isnull

    params["limit"] = limit

    params["linkage"] = linkage

    params["linkage__contains"] = linkage_contains

    params["linkage__endswith"] = linkage_endswith

    params["linkage__gt"] = linkage_gt

    params["linkage__gte"] = linkage_gte

    params["linkage__icontains"] = linkage_icontains

    params["linkage__iendswith"] = linkage_iendswith

    params["linkage__iexact"] = linkage_iexact

    json_linkage_in: list[str] | Unset = UNSET
    if not isinstance(linkage_in, Unset):
        json_linkage_in = linkage_in

    params["linkage__in"] = json_linkage_in

    params["linkage__iregex"] = linkage_iregex

    params["linkage__isnull"] = linkage_isnull

    params["linkage__istartswith"] = linkage_istartswith

    params["linkage__lt"] = linkage_lt

    params["linkage__lte"] = linkage_lte

    json_linkage_range: list[str] | Unset = UNSET
    if not isinstance(linkage_range, Unset):
        json_linkage_range = linkage_range

    params["linkage__range"] = json_linkage_range

    params["linkage__regex"] = linkage_regex

    params["linkage__startswith"] = linkage_startswith

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

    json_observation: list[int] | Unset = UNSET
    if not isinstance(observation, Unset):
        json_observation = observation

    params["observation"] = json_observation

    json_observation_in: list[int] | Unset = UNSET
    if not isinstance(observation_in, Unset):
        json_observation_in = observation_in

    params["observation__in"] = json_observation_in

    params["observation__isnull"] = observation_isnull

    json_observationcollection: list[int] | Unset = UNSET
    if not isinstance(observationcollection, Unset):
        json_observationcollection = observationcollection

    params["observationcollection"] = json_observationcollection

    json_observationcollection_in: list[int] | Unset = UNSET
    if not isinstance(observationcollection_in, Unset):
        json_observationcollection_in = observationcollection_in

    params["observationcollection__in"] = json_observationcollection_in

    params["observationcollection__isnull"] = observationcollection_isnull

    params["offset"] = offset

    params["ordering"] = ordering

    json_platform: list[int] | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform

    params["platform"] = json_platform

    json_platform_in: list[int] | Unset = UNSET
    if not isinstance(platform_in, Unset):
        json_platform_in = platform_in

    params["platform__in"] = json_platform_in

    params["platform__isnull"] = platform_isnull

    json_project: list[int] | Unset = UNSET
    if not isinstance(project, Unset):
        json_project = project

    params["project"] = json_project

    json_project_in: list[int] | Unset = UNSET
    if not isinstance(project_in, Unset):
        json_project_in = project_in

    params["project__in"] = json_project_in

    params["project__isnull"] = project_isnull

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/imagedetails/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedImageDetailsReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedImageDetailsReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedImageDetailsReadList]:
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
    computation: list[int] | Unset = UNSET,
    computation_in: list[int] | Unset = UNSET,
    computation_isnull: bool | Unset = UNSET,
    file_description: str | Unset = UNSET,
    file_description_contains: str | Unset = UNSET,
    file_description_endswith: str | Unset = UNSET,
    file_description_gt: str | Unset = UNSET,
    file_description_gte: str | Unset = UNSET,
    file_description_icontains: str | Unset = UNSET,
    file_description_iendswith: str | Unset = UNSET,
    file_description_iexact: str | Unset = UNSET,
    file_description_in: list[str] | Unset = UNSET,
    file_description_iregex: str | Unset = UNSET,
    file_description_isnull: bool | Unset = UNSET,
    file_description_istartswith: str | Unset = UNSET,
    file_description_lt: str | Unset = UNSET,
    file_description_lte: str | Unset = UNSET,
    file_description_range: list[str] | Unset = UNSET,
    file_description_regex: str | Unset = UNSET,
    file_description_startswith: str | Unset = UNSET,
    file_name: str | Unset = UNSET,
    file_name_contains: str | Unset = UNSET,
    file_name_endswith: str | Unset = UNSET,
    file_name_gt: str | Unset = UNSET,
    file_name_gte: str | Unset = UNSET,
    file_name_icontains: str | Unset = UNSET,
    file_name_iendswith: str | Unset = UNSET,
    file_name_iexact: str | Unset = UNSET,
    file_name_in: list[str] | Unset = UNSET,
    file_name_iregex: str | Unset = UNSET,
    file_name_isnull: bool | Unset = UNSET,
    file_name_istartswith: str | Unset = UNSET,
    file_name_lt: str | Unset = UNSET,
    file_name_lte: str | Unset = UNSET,
    file_name_range: list[str] | Unset = UNSET,
    file_name_regex: str | Unset = UNSET,
    file_name_startswith: str | Unset = UNSET,
    image_constraints: int | Unset = UNSET,
    image_constraints_in: list[int] | Unset = UNSET,
    image_constraints_isnull: bool | Unset = UNSET,
    instrument: list[int] | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    linkage: str | Unset = UNSET,
    linkage_contains: str | Unset = UNSET,
    linkage_endswith: str | Unset = UNSET,
    linkage_gt: str | Unset = UNSET,
    linkage_gte: str | Unset = UNSET,
    linkage_icontains: str | Unset = UNSET,
    linkage_iendswith: str | Unset = UNSET,
    linkage_iexact: str | Unset = UNSET,
    linkage_in: list[str] | Unset = UNSET,
    linkage_iregex: str | Unset = UNSET,
    linkage_isnull: bool | Unset = UNSET,
    linkage_istartswith: str | Unset = UNSET,
    linkage_lt: str | Unset = UNSET,
    linkage_lte: str | Unset = UNSET,
    linkage_range: list[str] | Unset = UNSET,
    linkage_regex: str | Unset = UNSET,
    linkage_startswith: str | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    observationcollection: list[int] | Unset = UNSET,
    observationcollection_in: list[int] | Unset = UNSET,
    observationcollection_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform: list[int] | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    project: list[int] | Unset = UNSET,
    project_in: list[int] | Unset = UNSET,
    project_isnull: bool | Unset = UNSET,
) -> Response[PaginatedImageDetailsReadList]:
    """Get a list of ImageDetails objects.

    Args:
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        computation (list[int] | Unset):
        computation_in (list[int] | Unset):
        computation_isnull (bool | Unset):
        file_description (str | Unset):
        file_description_contains (str | Unset):
        file_description_endswith (str | Unset):
        file_description_gt (str | Unset):
        file_description_gte (str | Unset):
        file_description_icontains (str | Unset):
        file_description_iendswith (str | Unset):
        file_description_iexact (str | Unset):
        file_description_in (list[str] | Unset):
        file_description_iregex (str | Unset):
        file_description_isnull (bool | Unset):
        file_description_istartswith (str | Unset):
        file_description_lt (str | Unset):
        file_description_lte (str | Unset):
        file_description_range (list[str] | Unset):
        file_description_regex (str | Unset):
        file_description_startswith (str | Unset):
        file_name (str | Unset):
        file_name_contains (str | Unset):
        file_name_endswith (str | Unset):
        file_name_gt (str | Unset):
        file_name_gte (str | Unset):
        file_name_icontains (str | Unset):
        file_name_iendswith (str | Unset):
        file_name_iexact (str | Unset):
        file_name_in (list[str] | Unset):
        file_name_iregex (str | Unset):
        file_name_isnull (bool | Unset):
        file_name_istartswith (str | Unset):
        file_name_lt (str | Unset):
        file_name_lte (str | Unset):
        file_name_range (list[str] | Unset):
        file_name_regex (str | Unset):
        file_name_startswith (str | Unset):
        image_constraints (int | Unset):
        image_constraints_in (list[int] | Unset):
        image_constraints_isnull (bool | Unset):
        instrument (list[int] | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        limit (int | Unset):
        linkage (str | Unset):
        linkage_contains (str | Unset):
        linkage_endswith (str | Unset):
        linkage_gt (str | Unset):
        linkage_gte (str | Unset):
        linkage_icontains (str | Unset):
        linkage_iendswith (str | Unset):
        linkage_iexact (str | Unset):
        linkage_in (list[str] | Unset):
        linkage_iregex (str | Unset):
        linkage_isnull (bool | Unset):
        linkage_istartswith (str | Unset):
        linkage_lt (str | Unset):
        linkage_lte (str | Unset):
        linkage_range (list[str] | Unset):
        linkage_regex (str | Unset):
        linkage_startswith (str | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        observationcollection (list[int] | Unset):
        observationcollection_in (list[int] | Unset):
        observationcollection_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        platform (list[int] | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        project (list[int] | Unset):
        project_in (list[int] | Unset):
        project_isnull (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedImageDetailsReadList]
    """

    kwargs = _get_kwargs(
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        computation=computation,
        computation_in=computation_in,
        computation_isnull=computation_isnull,
        file_description=file_description,
        file_description_contains=file_description_contains,
        file_description_endswith=file_description_endswith,
        file_description_gt=file_description_gt,
        file_description_gte=file_description_gte,
        file_description_icontains=file_description_icontains,
        file_description_iendswith=file_description_iendswith,
        file_description_iexact=file_description_iexact,
        file_description_in=file_description_in,
        file_description_iregex=file_description_iregex,
        file_description_isnull=file_description_isnull,
        file_description_istartswith=file_description_istartswith,
        file_description_lt=file_description_lt,
        file_description_lte=file_description_lte,
        file_description_range=file_description_range,
        file_description_regex=file_description_regex,
        file_description_startswith=file_description_startswith,
        file_name=file_name,
        file_name_contains=file_name_contains,
        file_name_endswith=file_name_endswith,
        file_name_gt=file_name_gt,
        file_name_gte=file_name_gte,
        file_name_icontains=file_name_icontains,
        file_name_iendswith=file_name_iendswith,
        file_name_iexact=file_name_iexact,
        file_name_in=file_name_in,
        file_name_iregex=file_name_iregex,
        file_name_isnull=file_name_isnull,
        file_name_istartswith=file_name_istartswith,
        file_name_lt=file_name_lt,
        file_name_lte=file_name_lte,
        file_name_range=file_name_range,
        file_name_regex=file_name_regex,
        file_name_startswith=file_name_startswith,
        image_constraints=image_constraints,
        image_constraints_in=image_constraints_in,
        image_constraints_isnull=image_constraints_isnull,
        instrument=instrument,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        limit=limit,
        linkage=linkage,
        linkage_contains=linkage_contains,
        linkage_endswith=linkage_endswith,
        linkage_gt=linkage_gt,
        linkage_gte=linkage_gte,
        linkage_icontains=linkage_icontains,
        linkage_iendswith=linkage_iendswith,
        linkage_iexact=linkage_iexact,
        linkage_in=linkage_in,
        linkage_iregex=linkage_iregex,
        linkage_isnull=linkage_isnull,
        linkage_istartswith=linkage_istartswith,
        linkage_lt=linkage_lt,
        linkage_lte=linkage_lte,
        linkage_range=linkage_range,
        linkage_regex=linkage_regex,
        linkage_startswith=linkage_startswith,
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
        observationcollection=observationcollection,
        observationcollection_in=observationcollection_in,
        observationcollection_isnull=observationcollection_isnull,
        offset=offset,
        ordering=ordering,
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        project=project,
        project_in=project_in,
        project_isnull=project_isnull,
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
    computation: list[int] | Unset = UNSET,
    computation_in: list[int] | Unset = UNSET,
    computation_isnull: bool | Unset = UNSET,
    file_description: str | Unset = UNSET,
    file_description_contains: str | Unset = UNSET,
    file_description_endswith: str | Unset = UNSET,
    file_description_gt: str | Unset = UNSET,
    file_description_gte: str | Unset = UNSET,
    file_description_icontains: str | Unset = UNSET,
    file_description_iendswith: str | Unset = UNSET,
    file_description_iexact: str | Unset = UNSET,
    file_description_in: list[str] | Unset = UNSET,
    file_description_iregex: str | Unset = UNSET,
    file_description_isnull: bool | Unset = UNSET,
    file_description_istartswith: str | Unset = UNSET,
    file_description_lt: str | Unset = UNSET,
    file_description_lte: str | Unset = UNSET,
    file_description_range: list[str] | Unset = UNSET,
    file_description_regex: str | Unset = UNSET,
    file_description_startswith: str | Unset = UNSET,
    file_name: str | Unset = UNSET,
    file_name_contains: str | Unset = UNSET,
    file_name_endswith: str | Unset = UNSET,
    file_name_gt: str | Unset = UNSET,
    file_name_gte: str | Unset = UNSET,
    file_name_icontains: str | Unset = UNSET,
    file_name_iendswith: str | Unset = UNSET,
    file_name_iexact: str | Unset = UNSET,
    file_name_in: list[str] | Unset = UNSET,
    file_name_iregex: str | Unset = UNSET,
    file_name_isnull: bool | Unset = UNSET,
    file_name_istartswith: str | Unset = UNSET,
    file_name_lt: str | Unset = UNSET,
    file_name_lte: str | Unset = UNSET,
    file_name_range: list[str] | Unset = UNSET,
    file_name_regex: str | Unset = UNSET,
    file_name_startswith: str | Unset = UNSET,
    image_constraints: int | Unset = UNSET,
    image_constraints_in: list[int] | Unset = UNSET,
    image_constraints_isnull: bool | Unset = UNSET,
    instrument: list[int] | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    linkage: str | Unset = UNSET,
    linkage_contains: str | Unset = UNSET,
    linkage_endswith: str | Unset = UNSET,
    linkage_gt: str | Unset = UNSET,
    linkage_gte: str | Unset = UNSET,
    linkage_icontains: str | Unset = UNSET,
    linkage_iendswith: str | Unset = UNSET,
    linkage_iexact: str | Unset = UNSET,
    linkage_in: list[str] | Unset = UNSET,
    linkage_iregex: str | Unset = UNSET,
    linkage_isnull: bool | Unset = UNSET,
    linkage_istartswith: str | Unset = UNSET,
    linkage_lt: str | Unset = UNSET,
    linkage_lte: str | Unset = UNSET,
    linkage_range: list[str] | Unset = UNSET,
    linkage_regex: str | Unset = UNSET,
    linkage_startswith: str | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    observationcollection: list[int] | Unset = UNSET,
    observationcollection_in: list[int] | Unset = UNSET,
    observationcollection_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform: list[int] | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    project: list[int] | Unset = UNSET,
    project_in: list[int] | Unset = UNSET,
    project_isnull: bool | Unset = UNSET,
) -> PaginatedImageDetailsReadList | None:
    """Get a list of ImageDetails objects.

    Args:
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        computation (list[int] | Unset):
        computation_in (list[int] | Unset):
        computation_isnull (bool | Unset):
        file_description (str | Unset):
        file_description_contains (str | Unset):
        file_description_endswith (str | Unset):
        file_description_gt (str | Unset):
        file_description_gte (str | Unset):
        file_description_icontains (str | Unset):
        file_description_iendswith (str | Unset):
        file_description_iexact (str | Unset):
        file_description_in (list[str] | Unset):
        file_description_iregex (str | Unset):
        file_description_isnull (bool | Unset):
        file_description_istartswith (str | Unset):
        file_description_lt (str | Unset):
        file_description_lte (str | Unset):
        file_description_range (list[str] | Unset):
        file_description_regex (str | Unset):
        file_description_startswith (str | Unset):
        file_name (str | Unset):
        file_name_contains (str | Unset):
        file_name_endswith (str | Unset):
        file_name_gt (str | Unset):
        file_name_gte (str | Unset):
        file_name_icontains (str | Unset):
        file_name_iendswith (str | Unset):
        file_name_iexact (str | Unset):
        file_name_in (list[str] | Unset):
        file_name_iregex (str | Unset):
        file_name_isnull (bool | Unset):
        file_name_istartswith (str | Unset):
        file_name_lt (str | Unset):
        file_name_lte (str | Unset):
        file_name_range (list[str] | Unset):
        file_name_regex (str | Unset):
        file_name_startswith (str | Unset):
        image_constraints (int | Unset):
        image_constraints_in (list[int] | Unset):
        image_constraints_isnull (bool | Unset):
        instrument (list[int] | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        limit (int | Unset):
        linkage (str | Unset):
        linkage_contains (str | Unset):
        linkage_endswith (str | Unset):
        linkage_gt (str | Unset):
        linkage_gte (str | Unset):
        linkage_icontains (str | Unset):
        linkage_iendswith (str | Unset):
        linkage_iexact (str | Unset):
        linkage_in (list[str] | Unset):
        linkage_iregex (str | Unset):
        linkage_isnull (bool | Unset):
        linkage_istartswith (str | Unset):
        linkage_lt (str | Unset):
        linkage_lte (str | Unset):
        linkage_range (list[str] | Unset):
        linkage_regex (str | Unset):
        linkage_startswith (str | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        observationcollection (list[int] | Unset):
        observationcollection_in (list[int] | Unset):
        observationcollection_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        platform (list[int] | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        project (list[int] | Unset):
        project_in (list[int] | Unset):
        project_isnull (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedImageDetailsReadList
    """

    return sync_detailed(
        client=client,
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        computation=computation,
        computation_in=computation_in,
        computation_isnull=computation_isnull,
        file_description=file_description,
        file_description_contains=file_description_contains,
        file_description_endswith=file_description_endswith,
        file_description_gt=file_description_gt,
        file_description_gte=file_description_gte,
        file_description_icontains=file_description_icontains,
        file_description_iendswith=file_description_iendswith,
        file_description_iexact=file_description_iexact,
        file_description_in=file_description_in,
        file_description_iregex=file_description_iregex,
        file_description_isnull=file_description_isnull,
        file_description_istartswith=file_description_istartswith,
        file_description_lt=file_description_lt,
        file_description_lte=file_description_lte,
        file_description_range=file_description_range,
        file_description_regex=file_description_regex,
        file_description_startswith=file_description_startswith,
        file_name=file_name,
        file_name_contains=file_name_contains,
        file_name_endswith=file_name_endswith,
        file_name_gt=file_name_gt,
        file_name_gte=file_name_gte,
        file_name_icontains=file_name_icontains,
        file_name_iendswith=file_name_iendswith,
        file_name_iexact=file_name_iexact,
        file_name_in=file_name_in,
        file_name_iregex=file_name_iregex,
        file_name_isnull=file_name_isnull,
        file_name_istartswith=file_name_istartswith,
        file_name_lt=file_name_lt,
        file_name_lte=file_name_lte,
        file_name_range=file_name_range,
        file_name_regex=file_name_regex,
        file_name_startswith=file_name_startswith,
        image_constraints=image_constraints,
        image_constraints_in=image_constraints_in,
        image_constraints_isnull=image_constraints_isnull,
        instrument=instrument,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        limit=limit,
        linkage=linkage,
        linkage_contains=linkage_contains,
        linkage_endswith=linkage_endswith,
        linkage_gt=linkage_gt,
        linkage_gte=linkage_gte,
        linkage_icontains=linkage_icontains,
        linkage_iendswith=linkage_iendswith,
        linkage_iexact=linkage_iexact,
        linkage_in=linkage_in,
        linkage_iregex=linkage_iregex,
        linkage_isnull=linkage_isnull,
        linkage_istartswith=linkage_istartswith,
        linkage_lt=linkage_lt,
        linkage_lte=linkage_lte,
        linkage_range=linkage_range,
        linkage_regex=linkage_regex,
        linkage_startswith=linkage_startswith,
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
        observationcollection=observationcollection,
        observationcollection_in=observationcollection_in,
        observationcollection_isnull=observationcollection_isnull,
        offset=offset,
        ordering=ordering,
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        project=project,
        project_in=project_in,
        project_isnull=project_isnull,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    computation: list[int] | Unset = UNSET,
    computation_in: list[int] | Unset = UNSET,
    computation_isnull: bool | Unset = UNSET,
    file_description: str | Unset = UNSET,
    file_description_contains: str | Unset = UNSET,
    file_description_endswith: str | Unset = UNSET,
    file_description_gt: str | Unset = UNSET,
    file_description_gte: str | Unset = UNSET,
    file_description_icontains: str | Unset = UNSET,
    file_description_iendswith: str | Unset = UNSET,
    file_description_iexact: str | Unset = UNSET,
    file_description_in: list[str] | Unset = UNSET,
    file_description_iregex: str | Unset = UNSET,
    file_description_isnull: bool | Unset = UNSET,
    file_description_istartswith: str | Unset = UNSET,
    file_description_lt: str | Unset = UNSET,
    file_description_lte: str | Unset = UNSET,
    file_description_range: list[str] | Unset = UNSET,
    file_description_regex: str | Unset = UNSET,
    file_description_startswith: str | Unset = UNSET,
    file_name: str | Unset = UNSET,
    file_name_contains: str | Unset = UNSET,
    file_name_endswith: str | Unset = UNSET,
    file_name_gt: str | Unset = UNSET,
    file_name_gte: str | Unset = UNSET,
    file_name_icontains: str | Unset = UNSET,
    file_name_iendswith: str | Unset = UNSET,
    file_name_iexact: str | Unset = UNSET,
    file_name_in: list[str] | Unset = UNSET,
    file_name_iregex: str | Unset = UNSET,
    file_name_isnull: bool | Unset = UNSET,
    file_name_istartswith: str | Unset = UNSET,
    file_name_lt: str | Unset = UNSET,
    file_name_lte: str | Unset = UNSET,
    file_name_range: list[str] | Unset = UNSET,
    file_name_regex: str | Unset = UNSET,
    file_name_startswith: str | Unset = UNSET,
    image_constraints: int | Unset = UNSET,
    image_constraints_in: list[int] | Unset = UNSET,
    image_constraints_isnull: bool | Unset = UNSET,
    instrument: list[int] | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    linkage: str | Unset = UNSET,
    linkage_contains: str | Unset = UNSET,
    linkage_endswith: str | Unset = UNSET,
    linkage_gt: str | Unset = UNSET,
    linkage_gte: str | Unset = UNSET,
    linkage_icontains: str | Unset = UNSET,
    linkage_iendswith: str | Unset = UNSET,
    linkage_iexact: str | Unset = UNSET,
    linkage_in: list[str] | Unset = UNSET,
    linkage_iregex: str | Unset = UNSET,
    linkage_isnull: bool | Unset = UNSET,
    linkage_istartswith: str | Unset = UNSET,
    linkage_lt: str | Unset = UNSET,
    linkage_lte: str | Unset = UNSET,
    linkage_range: list[str] | Unset = UNSET,
    linkage_regex: str | Unset = UNSET,
    linkage_startswith: str | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    observationcollection: list[int] | Unset = UNSET,
    observationcollection_in: list[int] | Unset = UNSET,
    observationcollection_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform: list[int] | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    project: list[int] | Unset = UNSET,
    project_in: list[int] | Unset = UNSET,
    project_isnull: bool | Unset = UNSET,
) -> Response[PaginatedImageDetailsReadList]:
    """Get a list of ImageDetails objects.

    Args:
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        computation (list[int] | Unset):
        computation_in (list[int] | Unset):
        computation_isnull (bool | Unset):
        file_description (str | Unset):
        file_description_contains (str | Unset):
        file_description_endswith (str | Unset):
        file_description_gt (str | Unset):
        file_description_gte (str | Unset):
        file_description_icontains (str | Unset):
        file_description_iendswith (str | Unset):
        file_description_iexact (str | Unset):
        file_description_in (list[str] | Unset):
        file_description_iregex (str | Unset):
        file_description_isnull (bool | Unset):
        file_description_istartswith (str | Unset):
        file_description_lt (str | Unset):
        file_description_lte (str | Unset):
        file_description_range (list[str] | Unset):
        file_description_regex (str | Unset):
        file_description_startswith (str | Unset):
        file_name (str | Unset):
        file_name_contains (str | Unset):
        file_name_endswith (str | Unset):
        file_name_gt (str | Unset):
        file_name_gte (str | Unset):
        file_name_icontains (str | Unset):
        file_name_iendswith (str | Unset):
        file_name_iexact (str | Unset):
        file_name_in (list[str] | Unset):
        file_name_iregex (str | Unset):
        file_name_isnull (bool | Unset):
        file_name_istartswith (str | Unset):
        file_name_lt (str | Unset):
        file_name_lte (str | Unset):
        file_name_range (list[str] | Unset):
        file_name_regex (str | Unset):
        file_name_startswith (str | Unset):
        image_constraints (int | Unset):
        image_constraints_in (list[int] | Unset):
        image_constraints_isnull (bool | Unset):
        instrument (list[int] | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        limit (int | Unset):
        linkage (str | Unset):
        linkage_contains (str | Unset):
        linkage_endswith (str | Unset):
        linkage_gt (str | Unset):
        linkage_gte (str | Unset):
        linkage_icontains (str | Unset):
        linkage_iendswith (str | Unset):
        linkage_iexact (str | Unset):
        linkage_in (list[str] | Unset):
        linkage_iregex (str | Unset):
        linkage_isnull (bool | Unset):
        linkage_istartswith (str | Unset):
        linkage_lt (str | Unset):
        linkage_lte (str | Unset):
        linkage_range (list[str] | Unset):
        linkage_regex (str | Unset):
        linkage_startswith (str | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        observationcollection (list[int] | Unset):
        observationcollection_in (list[int] | Unset):
        observationcollection_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        platform (list[int] | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        project (list[int] | Unset):
        project_in (list[int] | Unset):
        project_isnull (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedImageDetailsReadList]
    """

    kwargs = _get_kwargs(
        acquisition=acquisition,
        acquisition_in=acquisition_in,
        acquisition_isnull=acquisition_isnull,
        computation=computation,
        computation_in=computation_in,
        computation_isnull=computation_isnull,
        file_description=file_description,
        file_description_contains=file_description_contains,
        file_description_endswith=file_description_endswith,
        file_description_gt=file_description_gt,
        file_description_gte=file_description_gte,
        file_description_icontains=file_description_icontains,
        file_description_iendswith=file_description_iendswith,
        file_description_iexact=file_description_iexact,
        file_description_in=file_description_in,
        file_description_iregex=file_description_iregex,
        file_description_isnull=file_description_isnull,
        file_description_istartswith=file_description_istartswith,
        file_description_lt=file_description_lt,
        file_description_lte=file_description_lte,
        file_description_range=file_description_range,
        file_description_regex=file_description_regex,
        file_description_startswith=file_description_startswith,
        file_name=file_name,
        file_name_contains=file_name_contains,
        file_name_endswith=file_name_endswith,
        file_name_gt=file_name_gt,
        file_name_gte=file_name_gte,
        file_name_icontains=file_name_icontains,
        file_name_iendswith=file_name_iendswith,
        file_name_iexact=file_name_iexact,
        file_name_in=file_name_in,
        file_name_iregex=file_name_iregex,
        file_name_isnull=file_name_isnull,
        file_name_istartswith=file_name_istartswith,
        file_name_lt=file_name_lt,
        file_name_lte=file_name_lte,
        file_name_range=file_name_range,
        file_name_regex=file_name_regex,
        file_name_startswith=file_name_startswith,
        image_constraints=image_constraints,
        image_constraints_in=image_constraints_in,
        image_constraints_isnull=image_constraints_isnull,
        instrument=instrument,
        instrument_in=instrument_in,
        instrument_isnull=instrument_isnull,
        limit=limit,
        linkage=linkage,
        linkage_contains=linkage_contains,
        linkage_endswith=linkage_endswith,
        linkage_gt=linkage_gt,
        linkage_gte=linkage_gte,
        linkage_icontains=linkage_icontains,
        linkage_iendswith=linkage_iendswith,
        linkage_iexact=linkage_iexact,
        linkage_in=linkage_in,
        linkage_iregex=linkage_iregex,
        linkage_isnull=linkage_isnull,
        linkage_istartswith=linkage_istartswith,
        linkage_lt=linkage_lt,
        linkage_lte=linkage_lte,
        linkage_range=linkage_range,
        linkage_regex=linkage_regex,
        linkage_startswith=linkage_startswith,
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
        observationcollection=observationcollection,
        observationcollection_in=observationcollection_in,
        observationcollection_isnull=observationcollection_isnull,
        offset=offset,
        ordering=ordering,
        platform=platform,
        platform_in=platform_in,
        platform_isnull=platform_isnull,
        project=project,
        project_in=project_in,
        project_isnull=project_isnull,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    acquisition: list[int] | Unset = UNSET,
    acquisition_in: list[int] | Unset = UNSET,
    acquisition_isnull: bool | Unset = UNSET,
    computation: list[int] | Unset = UNSET,
    computation_in: list[int] | Unset = UNSET,
    computation_isnull: bool | Unset = UNSET,
    file_description: str | Unset = UNSET,
    file_description_contains: str | Unset = UNSET,
    file_description_endswith: str | Unset = UNSET,
    file_description_gt: str | Unset = UNSET,
    file_description_gte: str | Unset = UNSET,
    file_description_icontains: str | Unset = UNSET,
    file_description_iendswith: str | Unset = UNSET,
    file_description_iexact: str | Unset = UNSET,
    file_description_in: list[str] | Unset = UNSET,
    file_description_iregex: str | Unset = UNSET,
    file_description_isnull: bool | Unset = UNSET,
    file_description_istartswith: str | Unset = UNSET,
    file_description_lt: str | Unset = UNSET,
    file_description_lte: str | Unset = UNSET,
    file_description_range: list[str] | Unset = UNSET,
    file_description_regex: str | Unset = UNSET,
    file_description_startswith: str | Unset = UNSET,
    file_name: str | Unset = UNSET,
    file_name_contains: str | Unset = UNSET,
    file_name_endswith: str | Unset = UNSET,
    file_name_gt: str | Unset = UNSET,
    file_name_gte: str | Unset = UNSET,
    file_name_icontains: str | Unset = UNSET,
    file_name_iendswith: str | Unset = UNSET,
    file_name_iexact: str | Unset = UNSET,
    file_name_in: list[str] | Unset = UNSET,
    file_name_iregex: str | Unset = UNSET,
    file_name_isnull: bool | Unset = UNSET,
    file_name_istartswith: str | Unset = UNSET,
    file_name_lt: str | Unset = UNSET,
    file_name_lte: str | Unset = UNSET,
    file_name_range: list[str] | Unset = UNSET,
    file_name_regex: str | Unset = UNSET,
    file_name_startswith: str | Unset = UNSET,
    image_constraints: int | Unset = UNSET,
    image_constraints_in: list[int] | Unset = UNSET,
    image_constraints_isnull: bool | Unset = UNSET,
    instrument: list[int] | Unset = UNSET,
    instrument_in: list[int] | Unset = UNSET,
    instrument_isnull: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    linkage: str | Unset = UNSET,
    linkage_contains: str | Unset = UNSET,
    linkage_endswith: str | Unset = UNSET,
    linkage_gt: str | Unset = UNSET,
    linkage_gte: str | Unset = UNSET,
    linkage_icontains: str | Unset = UNSET,
    linkage_iendswith: str | Unset = UNSET,
    linkage_iexact: str | Unset = UNSET,
    linkage_in: list[str] | Unset = UNSET,
    linkage_iregex: str | Unset = UNSET,
    linkage_isnull: bool | Unset = UNSET,
    linkage_istartswith: str | Unset = UNSET,
    linkage_lt: str | Unset = UNSET,
    linkage_lte: str | Unset = UNSET,
    linkage_range: list[str] | Unset = UNSET,
    linkage_regex: str | Unset = UNSET,
    linkage_startswith: str | Unset = UNSET,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    observationcollection: list[int] | Unset = UNSET,
    observationcollection_in: list[int] | Unset = UNSET,
    observationcollection_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    platform: list[int] | Unset = UNSET,
    platform_in: list[int] | Unset = UNSET,
    platform_isnull: bool | Unset = UNSET,
    project: list[int] | Unset = UNSET,
    project_in: list[int] | Unset = UNSET,
    project_isnull: bool | Unset = UNSET,
) -> PaginatedImageDetailsReadList | None:
    """Get a list of ImageDetails objects.

    Args:
        acquisition (list[int] | Unset):
        acquisition_in (list[int] | Unset):
        acquisition_isnull (bool | Unset):
        computation (list[int] | Unset):
        computation_in (list[int] | Unset):
        computation_isnull (bool | Unset):
        file_description (str | Unset):
        file_description_contains (str | Unset):
        file_description_endswith (str | Unset):
        file_description_gt (str | Unset):
        file_description_gte (str | Unset):
        file_description_icontains (str | Unset):
        file_description_iendswith (str | Unset):
        file_description_iexact (str | Unset):
        file_description_in (list[str] | Unset):
        file_description_iregex (str | Unset):
        file_description_isnull (bool | Unset):
        file_description_istartswith (str | Unset):
        file_description_lt (str | Unset):
        file_description_lte (str | Unset):
        file_description_range (list[str] | Unset):
        file_description_regex (str | Unset):
        file_description_startswith (str | Unset):
        file_name (str | Unset):
        file_name_contains (str | Unset):
        file_name_endswith (str | Unset):
        file_name_gt (str | Unset):
        file_name_gte (str | Unset):
        file_name_icontains (str | Unset):
        file_name_iendswith (str | Unset):
        file_name_iexact (str | Unset):
        file_name_in (list[str] | Unset):
        file_name_iregex (str | Unset):
        file_name_isnull (bool | Unset):
        file_name_istartswith (str | Unset):
        file_name_lt (str | Unset):
        file_name_lte (str | Unset):
        file_name_range (list[str] | Unset):
        file_name_regex (str | Unset):
        file_name_startswith (str | Unset):
        image_constraints (int | Unset):
        image_constraints_in (list[int] | Unset):
        image_constraints_isnull (bool | Unset):
        instrument (list[int] | Unset):
        instrument_in (list[int] | Unset):
        instrument_isnull (bool | Unset):
        limit (int | Unset):
        linkage (str | Unset):
        linkage_contains (str | Unset):
        linkage_endswith (str | Unset):
        linkage_gt (str | Unset):
        linkage_gte (str | Unset):
        linkage_icontains (str | Unset):
        linkage_iendswith (str | Unset):
        linkage_iexact (str | Unset):
        linkage_in (list[str] | Unset):
        linkage_iregex (str | Unset):
        linkage_isnull (bool | Unset):
        linkage_istartswith (str | Unset):
        linkage_lt (str | Unset):
        linkage_lte (str | Unset):
        linkage_range (list[str] | Unset):
        linkage_regex (str | Unset):
        linkage_startswith (str | Unset):
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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        observationcollection (list[int] | Unset):
        observationcollection_in (list[int] | Unset):
        observationcollection_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        platform (list[int] | Unset):
        platform_in (list[int] | Unset):
        platform_isnull (bool | Unset):
        project (list[int] | Unset):
        project_in (list[int] | Unset):
        project_isnull (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedImageDetailsReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            acquisition=acquisition,
            acquisition_in=acquisition_in,
            acquisition_isnull=acquisition_isnull,
            computation=computation,
            computation_in=computation_in,
            computation_isnull=computation_isnull,
            file_description=file_description,
            file_description_contains=file_description_contains,
            file_description_endswith=file_description_endswith,
            file_description_gt=file_description_gt,
            file_description_gte=file_description_gte,
            file_description_icontains=file_description_icontains,
            file_description_iendswith=file_description_iendswith,
            file_description_iexact=file_description_iexact,
            file_description_in=file_description_in,
            file_description_iregex=file_description_iregex,
            file_description_isnull=file_description_isnull,
            file_description_istartswith=file_description_istartswith,
            file_description_lt=file_description_lt,
            file_description_lte=file_description_lte,
            file_description_range=file_description_range,
            file_description_regex=file_description_regex,
            file_description_startswith=file_description_startswith,
            file_name=file_name,
            file_name_contains=file_name_contains,
            file_name_endswith=file_name_endswith,
            file_name_gt=file_name_gt,
            file_name_gte=file_name_gte,
            file_name_icontains=file_name_icontains,
            file_name_iendswith=file_name_iendswith,
            file_name_iexact=file_name_iexact,
            file_name_in=file_name_in,
            file_name_iregex=file_name_iregex,
            file_name_isnull=file_name_isnull,
            file_name_istartswith=file_name_istartswith,
            file_name_lt=file_name_lt,
            file_name_lte=file_name_lte,
            file_name_range=file_name_range,
            file_name_regex=file_name_regex,
            file_name_startswith=file_name_startswith,
            image_constraints=image_constraints,
            image_constraints_in=image_constraints_in,
            image_constraints_isnull=image_constraints_isnull,
            instrument=instrument,
            instrument_in=instrument_in,
            instrument_isnull=instrument_isnull,
            limit=limit,
            linkage=linkage,
            linkage_contains=linkage_contains,
            linkage_endswith=linkage_endswith,
            linkage_gt=linkage_gt,
            linkage_gte=linkage_gte,
            linkage_icontains=linkage_icontains,
            linkage_iendswith=linkage_iendswith,
            linkage_iexact=linkage_iexact,
            linkage_in=linkage_in,
            linkage_iregex=linkage_iregex,
            linkage_isnull=linkage_isnull,
            linkage_istartswith=linkage_istartswith,
            linkage_lt=linkage_lt,
            linkage_lte=linkage_lte,
            linkage_range=linkage_range,
            linkage_regex=linkage_regex,
            linkage_startswith=linkage_startswith,
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
            observation=observation,
            observation_in=observation_in,
            observation_isnull=observation_isnull,
            observationcollection=observationcollection,
            observationcollection_in=observationcollection_in,
            observationcollection_isnull=observationcollection_isnull,
            offset=offset,
            ordering=ordering,
            platform=platform,
            platform_in=platform_in,
            platform_isnull=platform_isnull,
            project=project,
            project_in=project_in,
            project_isnull=project_isnull,
        )
    ).parsed
