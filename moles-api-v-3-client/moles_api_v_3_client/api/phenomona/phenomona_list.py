from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_phenomenon_list import PaginatedPhenomenonList
from ...models.phenomona_list_terms_label import PhenomonaListTermsLabel
from ...models.phenomona_list_terms_vocabulary import PhenomonaListTermsVocabulary
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    names_name: Union[Unset, str] = UNSET,
    names_name_contains: Union[Unset, str] = UNSET,
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
    terms_label: Union[Unset, PhenomonaListTermsLabel] = UNSET,
    terms_label_contains: Union[Unset, str] = UNSET,
    terms_label_in: Union[Unset, list[str]] = UNSET,
    terms_value: Union[Unset, str] = UNSET,
    terms_value_contains: Union[Unset, str] = UNSET,
    terms_value_in: Union[Unset, list[str]] = UNSET,
    terms_vocabulary: Union[Unset, PhenomonaListTermsVocabulary] = UNSET,
    terms_vocabulary_contains: Union[Unset, str] = UNSET,
    terms_vocabulary_in: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["names__name"] = names_name

    params["names__name__contains"] = names_name_contains

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

    json_terms_label: Union[Unset, str] = UNSET
    if not isinstance(terms_label, Unset):
        json_terms_label = terms_label.value

    params["terms__label"] = json_terms_label

    params["terms__label__contains"] = terms_label_contains

    json_terms_label_in: Union[Unset, list[str]] = UNSET
    if not isinstance(terms_label_in, Unset):
        json_terms_label_in = terms_label_in

    params["terms__label__in"] = json_terms_label_in

    params["terms__value"] = terms_value

    params["terms__value__contains"] = terms_value_contains

    json_terms_value_in: Union[Unset, list[str]] = UNSET
    if not isinstance(terms_value_in, Unset):
        json_terms_value_in = terms_value_in

    params["terms__value__in"] = json_terms_value_in

    json_terms_vocabulary: Union[Unset, str] = UNSET
    if not isinstance(terms_vocabulary, Unset):
        json_terms_vocabulary = terms_vocabulary.value

    params["terms__vocabulary"] = json_terms_vocabulary

    params["terms__vocabulary__contains"] = terms_vocabulary_contains

    json_terms_vocabulary_in: Union[Unset, list[str]] = UNSET
    if not isinstance(terms_vocabulary_in, Unset):
        json_terms_vocabulary_in = terms_vocabulary_in

    params["terms__vocabulary__in"] = json_terms_vocabulary_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/phenomona/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedPhenomenonList]:
    if response.status_code == 200:
        response_200 = PaginatedPhenomenonList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedPhenomenonList]:
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
    names_name: Union[Unset, str] = UNSET,
    names_name_contains: Union[Unset, str] = UNSET,
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
    terms_label: Union[Unset, PhenomonaListTermsLabel] = UNSET,
    terms_label_contains: Union[Unset, str] = UNSET,
    terms_label_in: Union[Unset, list[str]] = UNSET,
    terms_value: Union[Unset, str] = UNSET,
    terms_value_contains: Union[Unset, str] = UNSET,
    terms_value_in: Union[Unset, list[str]] = UNSET,
    terms_vocabulary: Union[Unset, PhenomonaListTermsVocabulary] = UNSET,
    terms_vocabulary_contains: Union[Unset, str] = UNSET,
    terms_vocabulary_in: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedPhenomenonList]:
    """Get a list of Phenomenon objects. Phenomena have many to many mapping with Observations.

    Args:
        limit (Union[Unset, int]):
        names_name (Union[Unset, str]):
        names_name_contains (Union[Unset, str]):
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
        terms_label (Union[Unset, PhenomonaListTermsLabel]):
        terms_label_contains (Union[Unset, str]):
        terms_label_in (Union[Unset, list[str]]):
        terms_value (Union[Unset, str]):
        terms_value_contains (Union[Unset, str]):
        terms_value_in (Union[Unset, list[str]]):
        terms_vocabulary (Union[Unset, PhenomonaListTermsVocabulary]):
        terms_vocabulary_contains (Union[Unset, str]):
        terms_vocabulary_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPhenomenonList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        names_name=names_name,
        names_name_contains=names_name_contains,
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
        terms_label=terms_label,
        terms_label_contains=terms_label_contains,
        terms_label_in=terms_label_in,
        terms_value=terms_value,
        terms_value_contains=terms_value_contains,
        terms_value_in=terms_value_in,
        terms_vocabulary=terms_vocabulary,
        terms_vocabulary_contains=terms_vocabulary_contains,
        terms_vocabulary_in=terms_vocabulary_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    names_name: Union[Unset, str] = UNSET,
    names_name_contains: Union[Unset, str] = UNSET,
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
    terms_label: Union[Unset, PhenomonaListTermsLabel] = UNSET,
    terms_label_contains: Union[Unset, str] = UNSET,
    terms_label_in: Union[Unset, list[str]] = UNSET,
    terms_value: Union[Unset, str] = UNSET,
    terms_value_contains: Union[Unset, str] = UNSET,
    terms_value_in: Union[Unset, list[str]] = UNSET,
    terms_vocabulary: Union[Unset, PhenomonaListTermsVocabulary] = UNSET,
    terms_vocabulary_contains: Union[Unset, str] = UNSET,
    terms_vocabulary_in: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedPhenomenonList]:
    """Get a list of Phenomenon objects. Phenomena have many to many mapping with Observations.

    Args:
        limit (Union[Unset, int]):
        names_name (Union[Unset, str]):
        names_name_contains (Union[Unset, str]):
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
        terms_label (Union[Unset, PhenomonaListTermsLabel]):
        terms_label_contains (Union[Unset, str]):
        terms_label_in (Union[Unset, list[str]]):
        terms_value (Union[Unset, str]):
        terms_value_contains (Union[Unset, str]):
        terms_value_in (Union[Unset, list[str]]):
        terms_vocabulary (Union[Unset, PhenomonaListTermsVocabulary]):
        terms_vocabulary_contains (Union[Unset, str]):
        terms_vocabulary_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPhenomenonList
    """

    return sync_detailed(
        client=client,
        limit=limit,
        names_name=names_name,
        names_name_contains=names_name_contains,
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
        terms_label=terms_label,
        terms_label_contains=terms_label_contains,
        terms_label_in=terms_label_in,
        terms_value=terms_value,
        terms_value_contains=terms_value_contains,
        terms_value_in=terms_value_in,
        terms_vocabulary=terms_vocabulary,
        terms_vocabulary_contains=terms_vocabulary_contains,
        terms_vocabulary_in=terms_vocabulary_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    names_name: Union[Unset, str] = UNSET,
    names_name_contains: Union[Unset, str] = UNSET,
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
    terms_label: Union[Unset, PhenomonaListTermsLabel] = UNSET,
    terms_label_contains: Union[Unset, str] = UNSET,
    terms_label_in: Union[Unset, list[str]] = UNSET,
    terms_value: Union[Unset, str] = UNSET,
    terms_value_contains: Union[Unset, str] = UNSET,
    terms_value_in: Union[Unset, list[str]] = UNSET,
    terms_vocabulary: Union[Unset, PhenomonaListTermsVocabulary] = UNSET,
    terms_vocabulary_contains: Union[Unset, str] = UNSET,
    terms_vocabulary_in: Union[Unset, list[str]] = UNSET,
) -> Response[PaginatedPhenomenonList]:
    """Get a list of Phenomenon objects. Phenomena have many to many mapping with Observations.

    Args:
        limit (Union[Unset, int]):
        names_name (Union[Unset, str]):
        names_name_contains (Union[Unset, str]):
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
        terms_label (Union[Unset, PhenomonaListTermsLabel]):
        terms_label_contains (Union[Unset, str]):
        terms_label_in (Union[Unset, list[str]]):
        terms_value (Union[Unset, str]):
        terms_value_contains (Union[Unset, str]):
        terms_value_in (Union[Unset, list[str]]):
        terms_vocabulary (Union[Unset, PhenomonaListTermsVocabulary]):
        terms_vocabulary_contains (Union[Unset, str]):
        terms_vocabulary_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPhenomenonList]
    """

    kwargs = _get_kwargs(
        limit=limit,
        names_name=names_name,
        names_name_contains=names_name_contains,
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
        terms_label=terms_label,
        terms_label_contains=terms_label_contains,
        terms_label_in=terms_label_in,
        terms_value=terms_value,
        terms_value_contains=terms_value_contains,
        terms_value_in=terms_value_in,
        terms_vocabulary=terms_vocabulary,
        terms_vocabulary_contains=terms_vocabulary_contains,
        terms_vocabulary_in=terms_vocabulary_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = UNSET,
    names_name: Union[Unset, str] = UNSET,
    names_name_contains: Union[Unset, str] = UNSET,
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
    terms_label: Union[Unset, PhenomonaListTermsLabel] = UNSET,
    terms_label_contains: Union[Unset, str] = UNSET,
    terms_label_in: Union[Unset, list[str]] = UNSET,
    terms_value: Union[Unset, str] = UNSET,
    terms_value_contains: Union[Unset, str] = UNSET,
    terms_value_in: Union[Unset, list[str]] = UNSET,
    terms_vocabulary: Union[Unset, PhenomonaListTermsVocabulary] = UNSET,
    terms_vocabulary_contains: Union[Unset, str] = UNSET,
    terms_vocabulary_in: Union[Unset, list[str]] = UNSET,
) -> Optional[PaginatedPhenomenonList]:
    """Get a list of Phenomenon objects. Phenomena have many to many mapping with Observations.

    Args:
        limit (Union[Unset, int]):
        names_name (Union[Unset, str]):
        names_name_contains (Union[Unset, str]):
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
        terms_label (Union[Unset, PhenomonaListTermsLabel]):
        terms_label_contains (Union[Unset, str]):
        terms_label_in (Union[Unset, list[str]]):
        terms_value (Union[Unset, str]):
        terms_value_contains (Union[Unset, str]):
        terms_value_in (Union[Unset, list[str]]):
        terms_vocabulary (Union[Unset, PhenomonaListTermsVocabulary]):
        terms_vocabulary_contains (Union[Unset, str]):
        terms_vocabulary_in (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPhenomenonList
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            names_name=names_name,
            names_name_contains=names_name_contains,
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
            terms_label=terms_label,
            terms_label_contains=terms_label_contains,
            terms_label_in=terms_label_in,
            terms_value=terms_value,
            terms_value_contains=terms_value_contains,
            terms_value_in=terms_value_in,
            terms_vocabulary=terms_vocabulary,
            terms_vocabulary_contains=terms_vocabulary_contains,
            terms_vocabulary_in=terms_vocabulary_in,
        )
    ).parsed
