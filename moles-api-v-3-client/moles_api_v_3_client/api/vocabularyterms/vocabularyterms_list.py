from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_vocabulary_term_write_list import PaginatedVocabularyTermWriteList
from ...models.vocabularyterms_list_vocabulary_service import VocabularytermsListVocabularyService
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
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
    resolved_term: Union[Unset, str] = UNSET,
    resolved_term_contains: Union[Unset, str] = UNSET,
    resolved_term_endswith: Union[Unset, str] = UNSET,
    resolved_term_gt: Union[Unset, str] = UNSET,
    resolved_term_gte: Union[Unset, str] = UNSET,
    resolved_term_icontains: Union[Unset, str] = UNSET,
    resolved_term_iendswith: Union[Unset, str] = UNSET,
    resolved_term_iexact: Union[Unset, str] = UNSET,
    resolved_term_in: Union[Unset, list[str]] = UNSET,
    resolved_term_iregex: Union[Unset, str] = UNSET,
    resolved_term_isnull: Union[Unset, bool] = UNSET,
    resolved_term_istartswith: Union[Unset, str] = UNSET,
    resolved_term_lt: Union[Unset, str] = UNSET,
    resolved_term_lte: Union[Unset, str] = UNSET,
    resolved_term_range: Union[Unset, list[str]] = UNSET,
    resolved_term_regex: Union[Unset, str] = UNSET,
    resolved_term_startswith: Union[Unset, str] = UNSET,
    uri: Union[Unset, str] = UNSET,
    uri_contains: Union[Unset, str] = UNSET,
    uri_endswith: Union[Unset, str] = UNSET,
    uri_gt: Union[Unset, str] = UNSET,
    uri_gte: Union[Unset, str] = UNSET,
    uri_icontains: Union[Unset, str] = UNSET,
    uri_iendswith: Union[Unset, str] = UNSET,
    uri_iexact: Union[Unset, str] = UNSET,
    uri_in: Union[Unset, list[str]] = UNSET,
    uri_iregex: Union[Unset, str] = UNSET,
    uri_isnull: Union[Unset, bool] = UNSET,
    uri_istartswith: Union[Unset, str] = UNSET,
    uri_lt: Union[Unset, str] = UNSET,
    uri_lte: Union[Unset, str] = UNSET,
    uri_range: Union[Unset, list[str]] = UNSET,
    uri_regex: Union[Unset, str] = UNSET,
    uri_startswith: Union[Unset, str] = UNSET,
    vocab_service: Union[Unset, VocabularytermsListVocabularyService] = UNSET,
    vocab_service_contains: Union[Unset, str] = UNSET,
    vocab_service_endswith: Union[Unset, str] = UNSET,
    vocab_service_gt: Union[Unset, str] = UNSET,
    vocab_service_gte: Union[Unset, str] = UNSET,
    vocab_service_icontains: Union[Unset, str] = UNSET,
    vocab_service_iendswith: Union[Unset, str] = UNSET,
    vocab_service_iexact: Union[Unset, str] = UNSET,
    vocab_service_in: Union[Unset, list[str]] = UNSET,
    vocab_service_iregex: Union[Unset, str] = UNSET,
    vocab_service_isnull: Union[Unset, bool] = UNSET,
    vocab_service_istartswith: Union[Unset, str] = UNSET,
    vocab_service_lt: Union[Unset, str] = UNSET,
    vocab_service_lte: Union[Unset, str] = UNSET,
    vocab_service_range: Union[Unset, list[str]] = UNSET,
    vocab_service_regex: Union[Unset, str] = UNSET,
    vocab_service_startswith: Union[Unset, str] = UNSET,
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

    params["resolvedTerm"] = resolved_term

    params["resolvedTerm__contains"] = resolved_term_contains

    params["resolvedTerm__endswith"] = resolved_term_endswith

    params["resolvedTerm__gt"] = resolved_term_gt

    params["resolvedTerm__gte"] = resolved_term_gte

    params["resolvedTerm__icontains"] = resolved_term_icontains

    params["resolvedTerm__iendswith"] = resolved_term_iendswith

    params["resolvedTerm__iexact"] = resolved_term_iexact

    json_resolved_term_in: Union[Unset, list[str]] = UNSET
    if not isinstance(resolved_term_in, Unset):
        json_resolved_term_in = resolved_term_in

    params["resolvedTerm__in"] = json_resolved_term_in

    params["resolvedTerm__iregex"] = resolved_term_iregex

    params["resolvedTerm__isnull"] = resolved_term_isnull

    params["resolvedTerm__istartswith"] = resolved_term_istartswith

    params["resolvedTerm__lt"] = resolved_term_lt

    params["resolvedTerm__lte"] = resolved_term_lte

    json_resolved_term_range: Union[Unset, list[str]] = UNSET
    if not isinstance(resolved_term_range, Unset):
        json_resolved_term_range = resolved_term_range

    params["resolvedTerm__range"] = json_resolved_term_range

    params["resolvedTerm__regex"] = resolved_term_regex

    params["resolvedTerm__startswith"] = resolved_term_startswith

    params["uri"] = uri

    params["uri__contains"] = uri_contains

    params["uri__endswith"] = uri_endswith

    params["uri__gt"] = uri_gt

    params["uri__gte"] = uri_gte

    params["uri__icontains"] = uri_icontains

    params["uri__iendswith"] = uri_iendswith

    params["uri__iexact"] = uri_iexact

    json_uri_in: Union[Unset, list[str]] = UNSET
    if not isinstance(uri_in, Unset):
        json_uri_in = uri_in

    params["uri__in"] = json_uri_in

    params["uri__iregex"] = uri_iregex

    params["uri__isnull"] = uri_isnull

    params["uri__istartswith"] = uri_istartswith

    params["uri__lt"] = uri_lt

    params["uri__lte"] = uri_lte

    json_uri_range: Union[Unset, list[str]] = UNSET
    if not isinstance(uri_range, Unset):
        json_uri_range = uri_range

    params["uri__range"] = json_uri_range

    params["uri__regex"] = uri_regex

    params["uri__startswith"] = uri_startswith

    json_vocab_service: Union[Unset, str] = UNSET
    if not isinstance(vocab_service, Unset):
        json_vocab_service = vocab_service.value

    params["vocabService"] = json_vocab_service

    params["vocabService__contains"] = vocab_service_contains

    params["vocabService__endswith"] = vocab_service_endswith

    params["vocabService__gt"] = vocab_service_gt

    params["vocabService__gte"] = vocab_service_gte

    params["vocabService__icontains"] = vocab_service_icontains

    params["vocabService__iendswith"] = vocab_service_iendswith

    params["vocabService__iexact"] = vocab_service_iexact

    json_vocab_service_in: Union[Unset, list[str]] = UNSET
    if not isinstance(vocab_service_in, Unset):
        json_vocab_service_in = vocab_service_in

    params["vocabService__in"] = json_vocab_service_in

    params["vocabService__iregex"] = vocab_service_iregex

    params["vocabService__isnull"] = vocab_service_isnull

    params["vocabService__istartswith"] = vocab_service_istartswith

    params["vocabService__lt"] = vocab_service_lt

    params["vocabService__lte"] = vocab_service_lte

    json_vocab_service_range: Union[Unset, list[str]] = UNSET
    if not isinstance(vocab_service_range, Unset):
        json_vocab_service_range = vocab_service_range

    params["vocabService__range"] = json_vocab_service_range

    params["vocabService__regex"] = vocab_service_regex

    params["vocabService__startswith"] = vocab_service_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/vocabularyterms/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedVocabularyTermWriteList]:
    if response.status_code == 200:
        response_200 = PaginatedVocabularyTermWriteList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedVocabularyTermWriteList]:
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
    resolved_term: Union[Unset, str] = UNSET,
    resolved_term_contains: Union[Unset, str] = UNSET,
    resolved_term_endswith: Union[Unset, str] = UNSET,
    resolved_term_gt: Union[Unset, str] = UNSET,
    resolved_term_gte: Union[Unset, str] = UNSET,
    resolved_term_icontains: Union[Unset, str] = UNSET,
    resolved_term_iendswith: Union[Unset, str] = UNSET,
    resolved_term_iexact: Union[Unset, str] = UNSET,
    resolved_term_in: Union[Unset, list[str]] = UNSET,
    resolved_term_iregex: Union[Unset, str] = UNSET,
    resolved_term_isnull: Union[Unset, bool] = UNSET,
    resolved_term_istartswith: Union[Unset, str] = UNSET,
    resolved_term_lt: Union[Unset, str] = UNSET,
    resolved_term_lte: Union[Unset, str] = UNSET,
    resolved_term_range: Union[Unset, list[str]] = UNSET,
    resolved_term_regex: Union[Unset, str] = UNSET,
    resolved_term_startswith: Union[Unset, str] = UNSET,
    uri: Union[Unset, str] = UNSET,
    uri_contains: Union[Unset, str] = UNSET,
    uri_endswith: Union[Unset, str] = UNSET,
    uri_gt: Union[Unset, str] = UNSET,
    uri_gte: Union[Unset, str] = UNSET,
    uri_icontains: Union[Unset, str] = UNSET,
    uri_iendswith: Union[Unset, str] = UNSET,
    uri_iexact: Union[Unset, str] = UNSET,
    uri_in: Union[Unset, list[str]] = UNSET,
    uri_iregex: Union[Unset, str] = UNSET,
    uri_isnull: Union[Unset, bool] = UNSET,
    uri_istartswith: Union[Unset, str] = UNSET,
    uri_lt: Union[Unset, str] = UNSET,
    uri_lte: Union[Unset, str] = UNSET,
    uri_range: Union[Unset, list[str]] = UNSET,
    uri_regex: Union[Unset, str] = UNSET,
    uri_startswith: Union[Unset, str] = UNSET,
    vocab_service: Union[Unset, VocabularytermsListVocabularyService] = UNSET,
    vocab_service_contains: Union[Unset, str] = UNSET,
    vocab_service_endswith: Union[Unset, str] = UNSET,
    vocab_service_gt: Union[Unset, str] = UNSET,
    vocab_service_gte: Union[Unset, str] = UNSET,
    vocab_service_icontains: Union[Unset, str] = UNSET,
    vocab_service_iendswith: Union[Unset, str] = UNSET,
    vocab_service_iexact: Union[Unset, str] = UNSET,
    vocab_service_in: Union[Unset, list[str]] = UNSET,
    vocab_service_iregex: Union[Unset, str] = UNSET,
    vocab_service_isnull: Union[Unset, bool] = UNSET,
    vocab_service_istartswith: Union[Unset, str] = UNSET,
    vocab_service_lt: Union[Unset, str] = UNSET,
    vocab_service_lte: Union[Unset, str] = UNSET,
    vocab_service_range: Union[Unset, list[str]] = UNSET,
    vocab_service_regex: Union[Unset, str] = UNSET,
    vocab_service_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedVocabularyTermWriteList]:
    """Get a list of Vocabulary terms objects.

    Args:
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
        resolved_term (Union[Unset, str]):
        resolved_term_contains (Union[Unset, str]):
        resolved_term_endswith (Union[Unset, str]):
        resolved_term_gt (Union[Unset, str]):
        resolved_term_gte (Union[Unset, str]):
        resolved_term_icontains (Union[Unset, str]):
        resolved_term_iendswith (Union[Unset, str]):
        resolved_term_iexact (Union[Unset, str]):
        resolved_term_in (Union[Unset, list[str]]):
        resolved_term_iregex (Union[Unset, str]):
        resolved_term_isnull (Union[Unset, bool]):
        resolved_term_istartswith (Union[Unset, str]):
        resolved_term_lt (Union[Unset, str]):
        resolved_term_lte (Union[Unset, str]):
        resolved_term_range (Union[Unset, list[str]]):
        resolved_term_regex (Union[Unset, str]):
        resolved_term_startswith (Union[Unset, str]):
        uri (Union[Unset, str]):
        uri_contains (Union[Unset, str]):
        uri_endswith (Union[Unset, str]):
        uri_gt (Union[Unset, str]):
        uri_gte (Union[Unset, str]):
        uri_icontains (Union[Unset, str]):
        uri_iendswith (Union[Unset, str]):
        uri_iexact (Union[Unset, str]):
        uri_in (Union[Unset, list[str]]):
        uri_iregex (Union[Unset, str]):
        uri_isnull (Union[Unset, bool]):
        uri_istartswith (Union[Unset, str]):
        uri_lt (Union[Unset, str]):
        uri_lte (Union[Unset, str]):
        uri_range (Union[Unset, list[str]]):
        uri_regex (Union[Unset, str]):
        uri_startswith (Union[Unset, str]):
        vocab_service (Union[Unset, VocabularytermsListVocabularyService]):
        vocab_service_contains (Union[Unset, str]):
        vocab_service_endswith (Union[Unset, str]):
        vocab_service_gt (Union[Unset, str]):
        vocab_service_gte (Union[Unset, str]):
        vocab_service_icontains (Union[Unset, str]):
        vocab_service_iendswith (Union[Unset, str]):
        vocab_service_iexact (Union[Unset, str]):
        vocab_service_in (Union[Unset, list[str]]):
        vocab_service_iregex (Union[Unset, str]):
        vocab_service_isnull (Union[Unset, bool]):
        vocab_service_istartswith (Union[Unset, str]):
        vocab_service_lt (Union[Unset, str]):
        vocab_service_lte (Union[Unset, str]):
        vocab_service_range (Union[Unset, list[str]]):
        vocab_service_regex (Union[Unset, str]):
        vocab_service_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVocabularyTermWriteList]
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
        resolved_term=resolved_term,
        resolved_term_contains=resolved_term_contains,
        resolved_term_endswith=resolved_term_endswith,
        resolved_term_gt=resolved_term_gt,
        resolved_term_gte=resolved_term_gte,
        resolved_term_icontains=resolved_term_icontains,
        resolved_term_iendswith=resolved_term_iendswith,
        resolved_term_iexact=resolved_term_iexact,
        resolved_term_in=resolved_term_in,
        resolved_term_iregex=resolved_term_iregex,
        resolved_term_isnull=resolved_term_isnull,
        resolved_term_istartswith=resolved_term_istartswith,
        resolved_term_lt=resolved_term_lt,
        resolved_term_lte=resolved_term_lte,
        resolved_term_range=resolved_term_range,
        resolved_term_regex=resolved_term_regex,
        resolved_term_startswith=resolved_term_startswith,
        uri=uri,
        uri_contains=uri_contains,
        uri_endswith=uri_endswith,
        uri_gt=uri_gt,
        uri_gte=uri_gte,
        uri_icontains=uri_icontains,
        uri_iendswith=uri_iendswith,
        uri_iexact=uri_iexact,
        uri_in=uri_in,
        uri_iregex=uri_iregex,
        uri_isnull=uri_isnull,
        uri_istartswith=uri_istartswith,
        uri_lt=uri_lt,
        uri_lte=uri_lte,
        uri_range=uri_range,
        uri_regex=uri_regex,
        uri_startswith=uri_startswith,
        vocab_service=vocab_service,
        vocab_service_contains=vocab_service_contains,
        vocab_service_endswith=vocab_service_endswith,
        vocab_service_gt=vocab_service_gt,
        vocab_service_gte=vocab_service_gte,
        vocab_service_icontains=vocab_service_icontains,
        vocab_service_iendswith=vocab_service_iendswith,
        vocab_service_iexact=vocab_service_iexact,
        vocab_service_in=vocab_service_in,
        vocab_service_iregex=vocab_service_iregex,
        vocab_service_isnull=vocab_service_isnull,
        vocab_service_istartswith=vocab_service_istartswith,
        vocab_service_lt=vocab_service_lt,
        vocab_service_lte=vocab_service_lte,
        vocab_service_range=vocab_service_range,
        vocab_service_regex=vocab_service_regex,
        vocab_service_startswith=vocab_service_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
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
    resolved_term: Union[Unset, str] = UNSET,
    resolved_term_contains: Union[Unset, str] = UNSET,
    resolved_term_endswith: Union[Unset, str] = UNSET,
    resolved_term_gt: Union[Unset, str] = UNSET,
    resolved_term_gte: Union[Unset, str] = UNSET,
    resolved_term_icontains: Union[Unset, str] = UNSET,
    resolved_term_iendswith: Union[Unset, str] = UNSET,
    resolved_term_iexact: Union[Unset, str] = UNSET,
    resolved_term_in: Union[Unset, list[str]] = UNSET,
    resolved_term_iregex: Union[Unset, str] = UNSET,
    resolved_term_isnull: Union[Unset, bool] = UNSET,
    resolved_term_istartswith: Union[Unset, str] = UNSET,
    resolved_term_lt: Union[Unset, str] = UNSET,
    resolved_term_lte: Union[Unset, str] = UNSET,
    resolved_term_range: Union[Unset, list[str]] = UNSET,
    resolved_term_regex: Union[Unset, str] = UNSET,
    resolved_term_startswith: Union[Unset, str] = UNSET,
    uri: Union[Unset, str] = UNSET,
    uri_contains: Union[Unset, str] = UNSET,
    uri_endswith: Union[Unset, str] = UNSET,
    uri_gt: Union[Unset, str] = UNSET,
    uri_gte: Union[Unset, str] = UNSET,
    uri_icontains: Union[Unset, str] = UNSET,
    uri_iendswith: Union[Unset, str] = UNSET,
    uri_iexact: Union[Unset, str] = UNSET,
    uri_in: Union[Unset, list[str]] = UNSET,
    uri_iregex: Union[Unset, str] = UNSET,
    uri_isnull: Union[Unset, bool] = UNSET,
    uri_istartswith: Union[Unset, str] = UNSET,
    uri_lt: Union[Unset, str] = UNSET,
    uri_lte: Union[Unset, str] = UNSET,
    uri_range: Union[Unset, list[str]] = UNSET,
    uri_regex: Union[Unset, str] = UNSET,
    uri_startswith: Union[Unset, str] = UNSET,
    vocab_service: Union[Unset, VocabularytermsListVocabularyService] = UNSET,
    vocab_service_contains: Union[Unset, str] = UNSET,
    vocab_service_endswith: Union[Unset, str] = UNSET,
    vocab_service_gt: Union[Unset, str] = UNSET,
    vocab_service_gte: Union[Unset, str] = UNSET,
    vocab_service_icontains: Union[Unset, str] = UNSET,
    vocab_service_iendswith: Union[Unset, str] = UNSET,
    vocab_service_iexact: Union[Unset, str] = UNSET,
    vocab_service_in: Union[Unset, list[str]] = UNSET,
    vocab_service_iregex: Union[Unset, str] = UNSET,
    vocab_service_isnull: Union[Unset, bool] = UNSET,
    vocab_service_istartswith: Union[Unset, str] = UNSET,
    vocab_service_lt: Union[Unset, str] = UNSET,
    vocab_service_lte: Union[Unset, str] = UNSET,
    vocab_service_range: Union[Unset, list[str]] = UNSET,
    vocab_service_regex: Union[Unset, str] = UNSET,
    vocab_service_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedVocabularyTermWriteList]:
    """Get a list of Vocabulary terms objects.

    Args:
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
        resolved_term (Union[Unset, str]):
        resolved_term_contains (Union[Unset, str]):
        resolved_term_endswith (Union[Unset, str]):
        resolved_term_gt (Union[Unset, str]):
        resolved_term_gte (Union[Unset, str]):
        resolved_term_icontains (Union[Unset, str]):
        resolved_term_iendswith (Union[Unset, str]):
        resolved_term_iexact (Union[Unset, str]):
        resolved_term_in (Union[Unset, list[str]]):
        resolved_term_iregex (Union[Unset, str]):
        resolved_term_isnull (Union[Unset, bool]):
        resolved_term_istartswith (Union[Unset, str]):
        resolved_term_lt (Union[Unset, str]):
        resolved_term_lte (Union[Unset, str]):
        resolved_term_range (Union[Unset, list[str]]):
        resolved_term_regex (Union[Unset, str]):
        resolved_term_startswith (Union[Unset, str]):
        uri (Union[Unset, str]):
        uri_contains (Union[Unset, str]):
        uri_endswith (Union[Unset, str]):
        uri_gt (Union[Unset, str]):
        uri_gte (Union[Unset, str]):
        uri_icontains (Union[Unset, str]):
        uri_iendswith (Union[Unset, str]):
        uri_iexact (Union[Unset, str]):
        uri_in (Union[Unset, list[str]]):
        uri_iregex (Union[Unset, str]):
        uri_isnull (Union[Unset, bool]):
        uri_istartswith (Union[Unset, str]):
        uri_lt (Union[Unset, str]):
        uri_lte (Union[Unset, str]):
        uri_range (Union[Unset, list[str]]):
        uri_regex (Union[Unset, str]):
        uri_startswith (Union[Unset, str]):
        vocab_service (Union[Unset, VocabularytermsListVocabularyService]):
        vocab_service_contains (Union[Unset, str]):
        vocab_service_endswith (Union[Unset, str]):
        vocab_service_gt (Union[Unset, str]):
        vocab_service_gte (Union[Unset, str]):
        vocab_service_icontains (Union[Unset, str]):
        vocab_service_iendswith (Union[Unset, str]):
        vocab_service_iexact (Union[Unset, str]):
        vocab_service_in (Union[Unset, list[str]]):
        vocab_service_iregex (Union[Unset, str]):
        vocab_service_isnull (Union[Unset, bool]):
        vocab_service_istartswith (Union[Unset, str]):
        vocab_service_lt (Union[Unset, str]):
        vocab_service_lte (Union[Unset, str]):
        vocab_service_range (Union[Unset, list[str]]):
        vocab_service_regex (Union[Unset, str]):
        vocab_service_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVocabularyTermWriteList
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
        resolved_term=resolved_term,
        resolved_term_contains=resolved_term_contains,
        resolved_term_endswith=resolved_term_endswith,
        resolved_term_gt=resolved_term_gt,
        resolved_term_gte=resolved_term_gte,
        resolved_term_icontains=resolved_term_icontains,
        resolved_term_iendswith=resolved_term_iendswith,
        resolved_term_iexact=resolved_term_iexact,
        resolved_term_in=resolved_term_in,
        resolved_term_iregex=resolved_term_iregex,
        resolved_term_isnull=resolved_term_isnull,
        resolved_term_istartswith=resolved_term_istartswith,
        resolved_term_lt=resolved_term_lt,
        resolved_term_lte=resolved_term_lte,
        resolved_term_range=resolved_term_range,
        resolved_term_regex=resolved_term_regex,
        resolved_term_startswith=resolved_term_startswith,
        uri=uri,
        uri_contains=uri_contains,
        uri_endswith=uri_endswith,
        uri_gt=uri_gt,
        uri_gte=uri_gte,
        uri_icontains=uri_icontains,
        uri_iendswith=uri_iendswith,
        uri_iexact=uri_iexact,
        uri_in=uri_in,
        uri_iregex=uri_iregex,
        uri_isnull=uri_isnull,
        uri_istartswith=uri_istartswith,
        uri_lt=uri_lt,
        uri_lte=uri_lte,
        uri_range=uri_range,
        uri_regex=uri_regex,
        uri_startswith=uri_startswith,
        vocab_service=vocab_service,
        vocab_service_contains=vocab_service_contains,
        vocab_service_endswith=vocab_service_endswith,
        vocab_service_gt=vocab_service_gt,
        vocab_service_gte=vocab_service_gte,
        vocab_service_icontains=vocab_service_icontains,
        vocab_service_iendswith=vocab_service_iendswith,
        vocab_service_iexact=vocab_service_iexact,
        vocab_service_in=vocab_service_in,
        vocab_service_iregex=vocab_service_iregex,
        vocab_service_isnull=vocab_service_isnull,
        vocab_service_istartswith=vocab_service_istartswith,
        vocab_service_lt=vocab_service_lt,
        vocab_service_lte=vocab_service_lte,
        vocab_service_range=vocab_service_range,
        vocab_service_regex=vocab_service_regex,
        vocab_service_startswith=vocab_service_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
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
    resolved_term: Union[Unset, str] = UNSET,
    resolved_term_contains: Union[Unset, str] = UNSET,
    resolved_term_endswith: Union[Unset, str] = UNSET,
    resolved_term_gt: Union[Unset, str] = UNSET,
    resolved_term_gte: Union[Unset, str] = UNSET,
    resolved_term_icontains: Union[Unset, str] = UNSET,
    resolved_term_iendswith: Union[Unset, str] = UNSET,
    resolved_term_iexact: Union[Unset, str] = UNSET,
    resolved_term_in: Union[Unset, list[str]] = UNSET,
    resolved_term_iregex: Union[Unset, str] = UNSET,
    resolved_term_isnull: Union[Unset, bool] = UNSET,
    resolved_term_istartswith: Union[Unset, str] = UNSET,
    resolved_term_lt: Union[Unset, str] = UNSET,
    resolved_term_lte: Union[Unset, str] = UNSET,
    resolved_term_range: Union[Unset, list[str]] = UNSET,
    resolved_term_regex: Union[Unset, str] = UNSET,
    resolved_term_startswith: Union[Unset, str] = UNSET,
    uri: Union[Unset, str] = UNSET,
    uri_contains: Union[Unset, str] = UNSET,
    uri_endswith: Union[Unset, str] = UNSET,
    uri_gt: Union[Unset, str] = UNSET,
    uri_gte: Union[Unset, str] = UNSET,
    uri_icontains: Union[Unset, str] = UNSET,
    uri_iendswith: Union[Unset, str] = UNSET,
    uri_iexact: Union[Unset, str] = UNSET,
    uri_in: Union[Unset, list[str]] = UNSET,
    uri_iregex: Union[Unset, str] = UNSET,
    uri_isnull: Union[Unset, bool] = UNSET,
    uri_istartswith: Union[Unset, str] = UNSET,
    uri_lt: Union[Unset, str] = UNSET,
    uri_lte: Union[Unset, str] = UNSET,
    uri_range: Union[Unset, list[str]] = UNSET,
    uri_regex: Union[Unset, str] = UNSET,
    uri_startswith: Union[Unset, str] = UNSET,
    vocab_service: Union[Unset, VocabularytermsListVocabularyService] = UNSET,
    vocab_service_contains: Union[Unset, str] = UNSET,
    vocab_service_endswith: Union[Unset, str] = UNSET,
    vocab_service_gt: Union[Unset, str] = UNSET,
    vocab_service_gte: Union[Unset, str] = UNSET,
    vocab_service_icontains: Union[Unset, str] = UNSET,
    vocab_service_iendswith: Union[Unset, str] = UNSET,
    vocab_service_iexact: Union[Unset, str] = UNSET,
    vocab_service_in: Union[Unset, list[str]] = UNSET,
    vocab_service_iregex: Union[Unset, str] = UNSET,
    vocab_service_isnull: Union[Unset, bool] = UNSET,
    vocab_service_istartswith: Union[Unset, str] = UNSET,
    vocab_service_lt: Union[Unset, str] = UNSET,
    vocab_service_lte: Union[Unset, str] = UNSET,
    vocab_service_range: Union[Unset, list[str]] = UNSET,
    vocab_service_regex: Union[Unset, str] = UNSET,
    vocab_service_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedVocabularyTermWriteList]:
    """Get a list of Vocabulary terms objects.

    Args:
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
        resolved_term (Union[Unset, str]):
        resolved_term_contains (Union[Unset, str]):
        resolved_term_endswith (Union[Unset, str]):
        resolved_term_gt (Union[Unset, str]):
        resolved_term_gte (Union[Unset, str]):
        resolved_term_icontains (Union[Unset, str]):
        resolved_term_iendswith (Union[Unset, str]):
        resolved_term_iexact (Union[Unset, str]):
        resolved_term_in (Union[Unset, list[str]]):
        resolved_term_iregex (Union[Unset, str]):
        resolved_term_isnull (Union[Unset, bool]):
        resolved_term_istartswith (Union[Unset, str]):
        resolved_term_lt (Union[Unset, str]):
        resolved_term_lte (Union[Unset, str]):
        resolved_term_range (Union[Unset, list[str]]):
        resolved_term_regex (Union[Unset, str]):
        resolved_term_startswith (Union[Unset, str]):
        uri (Union[Unset, str]):
        uri_contains (Union[Unset, str]):
        uri_endswith (Union[Unset, str]):
        uri_gt (Union[Unset, str]):
        uri_gte (Union[Unset, str]):
        uri_icontains (Union[Unset, str]):
        uri_iendswith (Union[Unset, str]):
        uri_iexact (Union[Unset, str]):
        uri_in (Union[Unset, list[str]]):
        uri_iregex (Union[Unset, str]):
        uri_isnull (Union[Unset, bool]):
        uri_istartswith (Union[Unset, str]):
        uri_lt (Union[Unset, str]):
        uri_lte (Union[Unset, str]):
        uri_range (Union[Unset, list[str]]):
        uri_regex (Union[Unset, str]):
        uri_startswith (Union[Unset, str]):
        vocab_service (Union[Unset, VocabularytermsListVocabularyService]):
        vocab_service_contains (Union[Unset, str]):
        vocab_service_endswith (Union[Unset, str]):
        vocab_service_gt (Union[Unset, str]):
        vocab_service_gte (Union[Unset, str]):
        vocab_service_icontains (Union[Unset, str]):
        vocab_service_iendswith (Union[Unset, str]):
        vocab_service_iexact (Union[Unset, str]):
        vocab_service_in (Union[Unset, list[str]]):
        vocab_service_iregex (Union[Unset, str]):
        vocab_service_isnull (Union[Unset, bool]):
        vocab_service_istartswith (Union[Unset, str]):
        vocab_service_lt (Union[Unset, str]):
        vocab_service_lte (Union[Unset, str]):
        vocab_service_range (Union[Unset, list[str]]):
        vocab_service_regex (Union[Unset, str]):
        vocab_service_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVocabularyTermWriteList]
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
        resolved_term=resolved_term,
        resolved_term_contains=resolved_term_contains,
        resolved_term_endswith=resolved_term_endswith,
        resolved_term_gt=resolved_term_gt,
        resolved_term_gte=resolved_term_gte,
        resolved_term_icontains=resolved_term_icontains,
        resolved_term_iendswith=resolved_term_iendswith,
        resolved_term_iexact=resolved_term_iexact,
        resolved_term_in=resolved_term_in,
        resolved_term_iregex=resolved_term_iregex,
        resolved_term_isnull=resolved_term_isnull,
        resolved_term_istartswith=resolved_term_istartswith,
        resolved_term_lt=resolved_term_lt,
        resolved_term_lte=resolved_term_lte,
        resolved_term_range=resolved_term_range,
        resolved_term_regex=resolved_term_regex,
        resolved_term_startswith=resolved_term_startswith,
        uri=uri,
        uri_contains=uri_contains,
        uri_endswith=uri_endswith,
        uri_gt=uri_gt,
        uri_gte=uri_gte,
        uri_icontains=uri_icontains,
        uri_iendswith=uri_iendswith,
        uri_iexact=uri_iexact,
        uri_in=uri_in,
        uri_iregex=uri_iregex,
        uri_isnull=uri_isnull,
        uri_istartswith=uri_istartswith,
        uri_lt=uri_lt,
        uri_lte=uri_lte,
        uri_range=uri_range,
        uri_regex=uri_regex,
        uri_startswith=uri_startswith,
        vocab_service=vocab_service,
        vocab_service_contains=vocab_service_contains,
        vocab_service_endswith=vocab_service_endswith,
        vocab_service_gt=vocab_service_gt,
        vocab_service_gte=vocab_service_gte,
        vocab_service_icontains=vocab_service_icontains,
        vocab_service_iendswith=vocab_service_iendswith,
        vocab_service_iexact=vocab_service_iexact,
        vocab_service_in=vocab_service_in,
        vocab_service_iregex=vocab_service_iregex,
        vocab_service_isnull=vocab_service_isnull,
        vocab_service_istartswith=vocab_service_istartswith,
        vocab_service_lt=vocab_service_lt,
        vocab_service_lte=vocab_service_lte,
        vocab_service_range=vocab_service_range,
        vocab_service_regex=vocab_service_regex,
        vocab_service_startswith=vocab_service_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
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
    resolved_term: Union[Unset, str] = UNSET,
    resolved_term_contains: Union[Unset, str] = UNSET,
    resolved_term_endswith: Union[Unset, str] = UNSET,
    resolved_term_gt: Union[Unset, str] = UNSET,
    resolved_term_gte: Union[Unset, str] = UNSET,
    resolved_term_icontains: Union[Unset, str] = UNSET,
    resolved_term_iendswith: Union[Unset, str] = UNSET,
    resolved_term_iexact: Union[Unset, str] = UNSET,
    resolved_term_in: Union[Unset, list[str]] = UNSET,
    resolved_term_iregex: Union[Unset, str] = UNSET,
    resolved_term_isnull: Union[Unset, bool] = UNSET,
    resolved_term_istartswith: Union[Unset, str] = UNSET,
    resolved_term_lt: Union[Unset, str] = UNSET,
    resolved_term_lte: Union[Unset, str] = UNSET,
    resolved_term_range: Union[Unset, list[str]] = UNSET,
    resolved_term_regex: Union[Unset, str] = UNSET,
    resolved_term_startswith: Union[Unset, str] = UNSET,
    uri: Union[Unset, str] = UNSET,
    uri_contains: Union[Unset, str] = UNSET,
    uri_endswith: Union[Unset, str] = UNSET,
    uri_gt: Union[Unset, str] = UNSET,
    uri_gte: Union[Unset, str] = UNSET,
    uri_icontains: Union[Unset, str] = UNSET,
    uri_iendswith: Union[Unset, str] = UNSET,
    uri_iexact: Union[Unset, str] = UNSET,
    uri_in: Union[Unset, list[str]] = UNSET,
    uri_iregex: Union[Unset, str] = UNSET,
    uri_isnull: Union[Unset, bool] = UNSET,
    uri_istartswith: Union[Unset, str] = UNSET,
    uri_lt: Union[Unset, str] = UNSET,
    uri_lte: Union[Unset, str] = UNSET,
    uri_range: Union[Unset, list[str]] = UNSET,
    uri_regex: Union[Unset, str] = UNSET,
    uri_startswith: Union[Unset, str] = UNSET,
    vocab_service: Union[Unset, VocabularytermsListVocabularyService] = UNSET,
    vocab_service_contains: Union[Unset, str] = UNSET,
    vocab_service_endswith: Union[Unset, str] = UNSET,
    vocab_service_gt: Union[Unset, str] = UNSET,
    vocab_service_gte: Union[Unset, str] = UNSET,
    vocab_service_icontains: Union[Unset, str] = UNSET,
    vocab_service_iendswith: Union[Unset, str] = UNSET,
    vocab_service_iexact: Union[Unset, str] = UNSET,
    vocab_service_in: Union[Unset, list[str]] = UNSET,
    vocab_service_iregex: Union[Unset, str] = UNSET,
    vocab_service_isnull: Union[Unset, bool] = UNSET,
    vocab_service_istartswith: Union[Unset, str] = UNSET,
    vocab_service_lt: Union[Unset, str] = UNSET,
    vocab_service_lte: Union[Unset, str] = UNSET,
    vocab_service_range: Union[Unset, list[str]] = UNSET,
    vocab_service_regex: Union[Unset, str] = UNSET,
    vocab_service_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedVocabularyTermWriteList]:
    """Get a list of Vocabulary terms objects.

    Args:
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
        resolved_term (Union[Unset, str]):
        resolved_term_contains (Union[Unset, str]):
        resolved_term_endswith (Union[Unset, str]):
        resolved_term_gt (Union[Unset, str]):
        resolved_term_gte (Union[Unset, str]):
        resolved_term_icontains (Union[Unset, str]):
        resolved_term_iendswith (Union[Unset, str]):
        resolved_term_iexact (Union[Unset, str]):
        resolved_term_in (Union[Unset, list[str]]):
        resolved_term_iregex (Union[Unset, str]):
        resolved_term_isnull (Union[Unset, bool]):
        resolved_term_istartswith (Union[Unset, str]):
        resolved_term_lt (Union[Unset, str]):
        resolved_term_lte (Union[Unset, str]):
        resolved_term_range (Union[Unset, list[str]]):
        resolved_term_regex (Union[Unset, str]):
        resolved_term_startswith (Union[Unset, str]):
        uri (Union[Unset, str]):
        uri_contains (Union[Unset, str]):
        uri_endswith (Union[Unset, str]):
        uri_gt (Union[Unset, str]):
        uri_gte (Union[Unset, str]):
        uri_icontains (Union[Unset, str]):
        uri_iendswith (Union[Unset, str]):
        uri_iexact (Union[Unset, str]):
        uri_in (Union[Unset, list[str]]):
        uri_iregex (Union[Unset, str]):
        uri_isnull (Union[Unset, bool]):
        uri_istartswith (Union[Unset, str]):
        uri_lt (Union[Unset, str]):
        uri_lte (Union[Unset, str]):
        uri_range (Union[Unset, list[str]]):
        uri_regex (Union[Unset, str]):
        uri_startswith (Union[Unset, str]):
        vocab_service (Union[Unset, VocabularytermsListVocabularyService]):
        vocab_service_contains (Union[Unset, str]):
        vocab_service_endswith (Union[Unset, str]):
        vocab_service_gt (Union[Unset, str]):
        vocab_service_gte (Union[Unset, str]):
        vocab_service_icontains (Union[Unset, str]):
        vocab_service_iendswith (Union[Unset, str]):
        vocab_service_iexact (Union[Unset, str]):
        vocab_service_in (Union[Unset, list[str]]):
        vocab_service_iregex (Union[Unset, str]):
        vocab_service_isnull (Union[Unset, bool]):
        vocab_service_istartswith (Union[Unset, str]):
        vocab_service_lt (Union[Unset, str]):
        vocab_service_lte (Union[Unset, str]):
        vocab_service_range (Union[Unset, list[str]]):
        vocab_service_regex (Union[Unset, str]):
        vocab_service_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVocabularyTermWriteList
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
            resolved_term=resolved_term,
            resolved_term_contains=resolved_term_contains,
            resolved_term_endswith=resolved_term_endswith,
            resolved_term_gt=resolved_term_gt,
            resolved_term_gte=resolved_term_gte,
            resolved_term_icontains=resolved_term_icontains,
            resolved_term_iendswith=resolved_term_iendswith,
            resolved_term_iexact=resolved_term_iexact,
            resolved_term_in=resolved_term_in,
            resolved_term_iregex=resolved_term_iregex,
            resolved_term_isnull=resolved_term_isnull,
            resolved_term_istartswith=resolved_term_istartswith,
            resolved_term_lt=resolved_term_lt,
            resolved_term_lte=resolved_term_lte,
            resolved_term_range=resolved_term_range,
            resolved_term_regex=resolved_term_regex,
            resolved_term_startswith=resolved_term_startswith,
            uri=uri,
            uri_contains=uri_contains,
            uri_endswith=uri_endswith,
            uri_gt=uri_gt,
            uri_gte=uri_gte,
            uri_icontains=uri_icontains,
            uri_iendswith=uri_iendswith,
            uri_iexact=uri_iexact,
            uri_in=uri_in,
            uri_iregex=uri_iregex,
            uri_isnull=uri_isnull,
            uri_istartswith=uri_istartswith,
            uri_lt=uri_lt,
            uri_lte=uri_lte,
            uri_range=uri_range,
            uri_regex=uri_regex,
            uri_startswith=uri_startswith,
            vocab_service=vocab_service,
            vocab_service_contains=vocab_service_contains,
            vocab_service_endswith=vocab_service_endswith,
            vocab_service_gt=vocab_service_gt,
            vocab_service_gte=vocab_service_gte,
            vocab_service_icontains=vocab_service_icontains,
            vocab_service_iendswith=vocab_service_iendswith,
            vocab_service_iexact=vocab_service_iexact,
            vocab_service_in=vocab_service_in,
            vocab_service_iregex=vocab_service_iregex,
            vocab_service_isnull=vocab_service_isnull,
            vocab_service_istartswith=vocab_service_istartswith,
            vocab_service_lt=vocab_service_lt,
            vocab_service_lte=vocab_service_lte,
            vocab_service_range=vocab_service_range,
            vocab_service_regex=vocab_service_regex,
            vocab_service_startswith=vocab_service_startswith,
        )
    ).parsed
