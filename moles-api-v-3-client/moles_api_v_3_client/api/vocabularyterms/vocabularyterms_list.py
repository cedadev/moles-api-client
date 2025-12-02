from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_vocabulary_term_read_list import PaginatedVocabularyTermReadList
from ...models.vocabularyterms_list_vocabulary_service import VocabularytermsListVocabularyService
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    resolved_term: str | Unset = UNSET,
    resolved_term_contains: str | Unset = UNSET,
    resolved_term_endswith: str | Unset = UNSET,
    resolved_term_gt: str | Unset = UNSET,
    resolved_term_gte: str | Unset = UNSET,
    resolved_term_icontains: str | Unset = UNSET,
    resolved_term_iendswith: str | Unset = UNSET,
    resolved_term_iexact: str | Unset = UNSET,
    resolved_term_in: list[str] | Unset = UNSET,
    resolved_term_iregex: str | Unset = UNSET,
    resolved_term_isnull: bool | Unset = UNSET,
    resolved_term_istartswith: str | Unset = UNSET,
    resolved_term_lt: str | Unset = UNSET,
    resolved_term_lte: str | Unset = UNSET,
    resolved_term_range: list[str] | Unset = UNSET,
    resolved_term_regex: str | Unset = UNSET,
    resolved_term_startswith: str | Unset = UNSET,
    uri: str | Unset = UNSET,
    uri_contains: str | Unset = UNSET,
    uri_endswith: str | Unset = UNSET,
    uri_gt: str | Unset = UNSET,
    uri_gte: str | Unset = UNSET,
    uri_icontains: str | Unset = UNSET,
    uri_iendswith: str | Unset = UNSET,
    uri_iexact: str | Unset = UNSET,
    uri_in: list[str] | Unset = UNSET,
    uri_iregex: str | Unset = UNSET,
    uri_isnull: bool | Unset = UNSET,
    uri_istartswith: str | Unset = UNSET,
    uri_lt: str | Unset = UNSET,
    uri_lte: str | Unset = UNSET,
    uri_range: list[str] | Unset = UNSET,
    uri_regex: str | Unset = UNSET,
    uri_startswith: str | Unset = UNSET,
    vocab_service: VocabularytermsListVocabularyService | Unset = UNSET,
    vocab_service_contains: str | Unset = UNSET,
    vocab_service_endswith: str | Unset = UNSET,
    vocab_service_gt: str | Unset = UNSET,
    vocab_service_gte: str | Unset = UNSET,
    vocab_service_icontains: str | Unset = UNSET,
    vocab_service_iendswith: str | Unset = UNSET,
    vocab_service_iexact: str | Unset = UNSET,
    vocab_service_in: list[str] | Unset = UNSET,
    vocab_service_iregex: str | Unset = UNSET,
    vocab_service_isnull: bool | Unset = UNSET,
    vocab_service_istartswith: str | Unset = UNSET,
    vocab_service_lt: str | Unset = UNSET,
    vocab_service_lte: str | Unset = UNSET,
    vocab_service_range: list[str] | Unset = UNSET,
    vocab_service_regex: str | Unset = UNSET,
    vocab_service_startswith: str | Unset = UNSET,
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

    json_observation: list[int] | Unset = UNSET
    if not isinstance(observation, Unset):
        json_observation = ",".join(map(str, observation))

    params["observation"] = json_observation

    json_observation_in: list[int] | Unset = UNSET
    if not isinstance(observation_in, Unset):
        json_observation_in = ",".join(map(str, observation_in))

    params["observation__in"] = json_observation_in

    params["observation__isnull"] = observation_isnull

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

    json_resolved_term_in: list[str] | Unset = UNSET
    if not isinstance(resolved_term_in, Unset):
        json_resolved_term_in = ",".join(map(str, resolved_term_in))

    params["resolvedTerm__in"] = json_resolved_term_in

    params["resolvedTerm__iregex"] = resolved_term_iregex

    params["resolvedTerm__isnull"] = resolved_term_isnull

    params["resolvedTerm__istartswith"] = resolved_term_istartswith

    params["resolvedTerm__lt"] = resolved_term_lt

    params["resolvedTerm__lte"] = resolved_term_lte

    json_resolved_term_range: list[str] | Unset = UNSET
    if not isinstance(resolved_term_range, Unset):
        json_resolved_term_range = ",".join(map(str, resolved_term_range))

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

    json_uri_in: list[str] | Unset = UNSET
    if not isinstance(uri_in, Unset):
        json_uri_in = ",".join(map(str, uri_in))

    params["uri__in"] = json_uri_in

    params["uri__iregex"] = uri_iregex

    params["uri__isnull"] = uri_isnull

    params["uri__istartswith"] = uri_istartswith

    params["uri__lt"] = uri_lt

    params["uri__lte"] = uri_lte

    json_uri_range: list[str] | Unset = UNSET
    if not isinstance(uri_range, Unset):
        json_uri_range = ",".join(map(str, uri_range))

    params["uri__range"] = json_uri_range

    params["uri__regex"] = uri_regex

    params["uri__startswith"] = uri_startswith

    json_vocab_service: str | Unset = UNSET
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

    json_vocab_service_in: list[str] | Unset = UNSET
    if not isinstance(vocab_service_in, Unset):
        json_vocab_service_in = ",".join(map(str, vocab_service_in))

    params["vocabService__in"] = json_vocab_service_in

    params["vocabService__iregex"] = vocab_service_iregex

    params["vocabService__isnull"] = vocab_service_isnull

    params["vocabService__istartswith"] = vocab_service_istartswith

    params["vocabService__lt"] = vocab_service_lt

    params["vocabService__lte"] = vocab_service_lte

    json_vocab_service_range: list[str] | Unset = UNSET
    if not isinstance(vocab_service_range, Unset):
        json_vocab_service_range = ",".join(map(str, vocab_service_range))

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PaginatedVocabularyTermReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedVocabularyTermReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PaginatedVocabularyTermReadList]:
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    resolved_term: str | Unset = UNSET,
    resolved_term_contains: str | Unset = UNSET,
    resolved_term_endswith: str | Unset = UNSET,
    resolved_term_gt: str | Unset = UNSET,
    resolved_term_gte: str | Unset = UNSET,
    resolved_term_icontains: str | Unset = UNSET,
    resolved_term_iendswith: str | Unset = UNSET,
    resolved_term_iexact: str | Unset = UNSET,
    resolved_term_in: list[str] | Unset = UNSET,
    resolved_term_iregex: str | Unset = UNSET,
    resolved_term_isnull: bool | Unset = UNSET,
    resolved_term_istartswith: str | Unset = UNSET,
    resolved_term_lt: str | Unset = UNSET,
    resolved_term_lte: str | Unset = UNSET,
    resolved_term_range: list[str] | Unset = UNSET,
    resolved_term_regex: str | Unset = UNSET,
    resolved_term_startswith: str | Unset = UNSET,
    uri: str | Unset = UNSET,
    uri_contains: str | Unset = UNSET,
    uri_endswith: str | Unset = UNSET,
    uri_gt: str | Unset = UNSET,
    uri_gte: str | Unset = UNSET,
    uri_icontains: str | Unset = UNSET,
    uri_iendswith: str | Unset = UNSET,
    uri_iexact: str | Unset = UNSET,
    uri_in: list[str] | Unset = UNSET,
    uri_iregex: str | Unset = UNSET,
    uri_isnull: bool | Unset = UNSET,
    uri_istartswith: str | Unset = UNSET,
    uri_lt: str | Unset = UNSET,
    uri_lte: str | Unset = UNSET,
    uri_range: list[str] | Unset = UNSET,
    uri_regex: str | Unset = UNSET,
    uri_startswith: str | Unset = UNSET,
    vocab_service: VocabularytermsListVocabularyService | Unset = UNSET,
    vocab_service_contains: str | Unset = UNSET,
    vocab_service_endswith: str | Unset = UNSET,
    vocab_service_gt: str | Unset = UNSET,
    vocab_service_gte: str | Unset = UNSET,
    vocab_service_icontains: str | Unset = UNSET,
    vocab_service_iendswith: str | Unset = UNSET,
    vocab_service_iexact: str | Unset = UNSET,
    vocab_service_in: list[str] | Unset = UNSET,
    vocab_service_iregex: str | Unset = UNSET,
    vocab_service_isnull: bool | Unset = UNSET,
    vocab_service_istartswith: str | Unset = UNSET,
    vocab_service_lt: str | Unset = UNSET,
    vocab_service_lte: str | Unset = UNSET,
    vocab_service_range: list[str] | Unset = UNSET,
    vocab_service_regex: str | Unset = UNSET,
    vocab_service_startswith: str | Unset = UNSET,
) -> Response[PaginatedVocabularyTermReadList]:
    """Get a list of Vocabulary terms objects.

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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        resolved_term (str | Unset):
        resolved_term_contains (str | Unset):
        resolved_term_endswith (str | Unset):
        resolved_term_gt (str | Unset):
        resolved_term_gte (str | Unset):
        resolved_term_icontains (str | Unset):
        resolved_term_iendswith (str | Unset):
        resolved_term_iexact (str | Unset):
        resolved_term_in (list[str] | Unset):
        resolved_term_iregex (str | Unset):
        resolved_term_isnull (bool | Unset):
        resolved_term_istartswith (str | Unset):
        resolved_term_lt (str | Unset):
        resolved_term_lte (str | Unset):
        resolved_term_range (list[str] | Unset):
        resolved_term_regex (str | Unset):
        resolved_term_startswith (str | Unset):
        uri (str | Unset):
        uri_contains (str | Unset):
        uri_endswith (str | Unset):
        uri_gt (str | Unset):
        uri_gte (str | Unset):
        uri_icontains (str | Unset):
        uri_iendswith (str | Unset):
        uri_iexact (str | Unset):
        uri_in (list[str] | Unset):
        uri_iregex (str | Unset):
        uri_isnull (bool | Unset):
        uri_istartswith (str | Unset):
        uri_lt (str | Unset):
        uri_lte (str | Unset):
        uri_range (list[str] | Unset):
        uri_regex (str | Unset):
        uri_startswith (str | Unset):
        vocab_service (VocabularytermsListVocabularyService | Unset):
        vocab_service_contains (str | Unset):
        vocab_service_endswith (str | Unset):
        vocab_service_gt (str | Unset):
        vocab_service_gte (str | Unset):
        vocab_service_icontains (str | Unset):
        vocab_service_iendswith (str | Unset):
        vocab_service_iexact (str | Unset):
        vocab_service_in (list[str] | Unset):
        vocab_service_iregex (str | Unset):
        vocab_service_isnull (bool | Unset):
        vocab_service_istartswith (str | Unset):
        vocab_service_lt (str | Unset):
        vocab_service_lte (str | Unset):
        vocab_service_range (list[str] | Unset):
        vocab_service_regex (str | Unset):
        vocab_service_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVocabularyTermReadList]
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    resolved_term: str | Unset = UNSET,
    resolved_term_contains: str | Unset = UNSET,
    resolved_term_endswith: str | Unset = UNSET,
    resolved_term_gt: str | Unset = UNSET,
    resolved_term_gte: str | Unset = UNSET,
    resolved_term_icontains: str | Unset = UNSET,
    resolved_term_iendswith: str | Unset = UNSET,
    resolved_term_iexact: str | Unset = UNSET,
    resolved_term_in: list[str] | Unset = UNSET,
    resolved_term_iregex: str | Unset = UNSET,
    resolved_term_isnull: bool | Unset = UNSET,
    resolved_term_istartswith: str | Unset = UNSET,
    resolved_term_lt: str | Unset = UNSET,
    resolved_term_lte: str | Unset = UNSET,
    resolved_term_range: list[str] | Unset = UNSET,
    resolved_term_regex: str | Unset = UNSET,
    resolved_term_startswith: str | Unset = UNSET,
    uri: str | Unset = UNSET,
    uri_contains: str | Unset = UNSET,
    uri_endswith: str | Unset = UNSET,
    uri_gt: str | Unset = UNSET,
    uri_gte: str | Unset = UNSET,
    uri_icontains: str | Unset = UNSET,
    uri_iendswith: str | Unset = UNSET,
    uri_iexact: str | Unset = UNSET,
    uri_in: list[str] | Unset = UNSET,
    uri_iregex: str | Unset = UNSET,
    uri_isnull: bool | Unset = UNSET,
    uri_istartswith: str | Unset = UNSET,
    uri_lt: str | Unset = UNSET,
    uri_lte: str | Unset = UNSET,
    uri_range: list[str] | Unset = UNSET,
    uri_regex: str | Unset = UNSET,
    uri_startswith: str | Unset = UNSET,
    vocab_service: VocabularytermsListVocabularyService | Unset = UNSET,
    vocab_service_contains: str | Unset = UNSET,
    vocab_service_endswith: str | Unset = UNSET,
    vocab_service_gt: str | Unset = UNSET,
    vocab_service_gte: str | Unset = UNSET,
    vocab_service_icontains: str | Unset = UNSET,
    vocab_service_iendswith: str | Unset = UNSET,
    vocab_service_iexact: str | Unset = UNSET,
    vocab_service_in: list[str] | Unset = UNSET,
    vocab_service_iregex: str | Unset = UNSET,
    vocab_service_isnull: bool | Unset = UNSET,
    vocab_service_istartswith: str | Unset = UNSET,
    vocab_service_lt: str | Unset = UNSET,
    vocab_service_lte: str | Unset = UNSET,
    vocab_service_range: list[str] | Unset = UNSET,
    vocab_service_regex: str | Unset = UNSET,
    vocab_service_startswith: str | Unset = UNSET,
) -> PaginatedVocabularyTermReadList | None:
    """Get a list of Vocabulary terms objects.

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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        resolved_term (str | Unset):
        resolved_term_contains (str | Unset):
        resolved_term_endswith (str | Unset):
        resolved_term_gt (str | Unset):
        resolved_term_gte (str | Unset):
        resolved_term_icontains (str | Unset):
        resolved_term_iendswith (str | Unset):
        resolved_term_iexact (str | Unset):
        resolved_term_in (list[str] | Unset):
        resolved_term_iregex (str | Unset):
        resolved_term_isnull (bool | Unset):
        resolved_term_istartswith (str | Unset):
        resolved_term_lt (str | Unset):
        resolved_term_lte (str | Unset):
        resolved_term_range (list[str] | Unset):
        resolved_term_regex (str | Unset):
        resolved_term_startswith (str | Unset):
        uri (str | Unset):
        uri_contains (str | Unset):
        uri_endswith (str | Unset):
        uri_gt (str | Unset):
        uri_gte (str | Unset):
        uri_icontains (str | Unset):
        uri_iendswith (str | Unset):
        uri_iexact (str | Unset):
        uri_in (list[str] | Unset):
        uri_iregex (str | Unset):
        uri_isnull (bool | Unset):
        uri_istartswith (str | Unset):
        uri_lt (str | Unset):
        uri_lte (str | Unset):
        uri_range (list[str] | Unset):
        uri_regex (str | Unset):
        uri_startswith (str | Unset):
        vocab_service (VocabularytermsListVocabularyService | Unset):
        vocab_service_contains (str | Unset):
        vocab_service_endswith (str | Unset):
        vocab_service_gt (str | Unset):
        vocab_service_gte (str | Unset):
        vocab_service_icontains (str | Unset):
        vocab_service_iendswith (str | Unset):
        vocab_service_iexact (str | Unset):
        vocab_service_in (list[str] | Unset):
        vocab_service_iregex (str | Unset):
        vocab_service_isnull (bool | Unset):
        vocab_service_istartswith (str | Unset):
        vocab_service_lt (str | Unset):
        vocab_service_lte (str | Unset):
        vocab_service_range (list[str] | Unset):
        vocab_service_regex (str | Unset):
        vocab_service_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVocabularyTermReadList
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    resolved_term: str | Unset = UNSET,
    resolved_term_contains: str | Unset = UNSET,
    resolved_term_endswith: str | Unset = UNSET,
    resolved_term_gt: str | Unset = UNSET,
    resolved_term_gte: str | Unset = UNSET,
    resolved_term_icontains: str | Unset = UNSET,
    resolved_term_iendswith: str | Unset = UNSET,
    resolved_term_iexact: str | Unset = UNSET,
    resolved_term_in: list[str] | Unset = UNSET,
    resolved_term_iregex: str | Unset = UNSET,
    resolved_term_isnull: bool | Unset = UNSET,
    resolved_term_istartswith: str | Unset = UNSET,
    resolved_term_lt: str | Unset = UNSET,
    resolved_term_lte: str | Unset = UNSET,
    resolved_term_range: list[str] | Unset = UNSET,
    resolved_term_regex: str | Unset = UNSET,
    resolved_term_startswith: str | Unset = UNSET,
    uri: str | Unset = UNSET,
    uri_contains: str | Unset = UNSET,
    uri_endswith: str | Unset = UNSET,
    uri_gt: str | Unset = UNSET,
    uri_gte: str | Unset = UNSET,
    uri_icontains: str | Unset = UNSET,
    uri_iendswith: str | Unset = UNSET,
    uri_iexact: str | Unset = UNSET,
    uri_in: list[str] | Unset = UNSET,
    uri_iregex: str | Unset = UNSET,
    uri_isnull: bool | Unset = UNSET,
    uri_istartswith: str | Unset = UNSET,
    uri_lt: str | Unset = UNSET,
    uri_lte: str | Unset = UNSET,
    uri_range: list[str] | Unset = UNSET,
    uri_regex: str | Unset = UNSET,
    uri_startswith: str | Unset = UNSET,
    vocab_service: VocabularytermsListVocabularyService | Unset = UNSET,
    vocab_service_contains: str | Unset = UNSET,
    vocab_service_endswith: str | Unset = UNSET,
    vocab_service_gt: str | Unset = UNSET,
    vocab_service_gte: str | Unset = UNSET,
    vocab_service_icontains: str | Unset = UNSET,
    vocab_service_iendswith: str | Unset = UNSET,
    vocab_service_iexact: str | Unset = UNSET,
    vocab_service_in: list[str] | Unset = UNSET,
    vocab_service_iregex: str | Unset = UNSET,
    vocab_service_isnull: bool | Unset = UNSET,
    vocab_service_istartswith: str | Unset = UNSET,
    vocab_service_lt: str | Unset = UNSET,
    vocab_service_lte: str | Unset = UNSET,
    vocab_service_range: list[str] | Unset = UNSET,
    vocab_service_regex: str | Unset = UNSET,
    vocab_service_startswith: str | Unset = UNSET,
) -> Response[PaginatedVocabularyTermReadList]:
    """Get a list of Vocabulary terms objects.

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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        resolved_term (str | Unset):
        resolved_term_contains (str | Unset):
        resolved_term_endswith (str | Unset):
        resolved_term_gt (str | Unset):
        resolved_term_gte (str | Unset):
        resolved_term_icontains (str | Unset):
        resolved_term_iendswith (str | Unset):
        resolved_term_iexact (str | Unset):
        resolved_term_in (list[str] | Unset):
        resolved_term_iregex (str | Unset):
        resolved_term_isnull (bool | Unset):
        resolved_term_istartswith (str | Unset):
        resolved_term_lt (str | Unset):
        resolved_term_lte (str | Unset):
        resolved_term_range (list[str] | Unset):
        resolved_term_regex (str | Unset):
        resolved_term_startswith (str | Unset):
        uri (str | Unset):
        uri_contains (str | Unset):
        uri_endswith (str | Unset):
        uri_gt (str | Unset):
        uri_gte (str | Unset):
        uri_icontains (str | Unset):
        uri_iendswith (str | Unset):
        uri_iexact (str | Unset):
        uri_in (list[str] | Unset):
        uri_iregex (str | Unset):
        uri_isnull (bool | Unset):
        uri_istartswith (str | Unset):
        uri_lt (str | Unset):
        uri_lte (str | Unset):
        uri_range (list[str] | Unset):
        uri_regex (str | Unset):
        uri_startswith (str | Unset):
        vocab_service (VocabularytermsListVocabularyService | Unset):
        vocab_service_contains (str | Unset):
        vocab_service_endswith (str | Unset):
        vocab_service_gt (str | Unset):
        vocab_service_gte (str | Unset):
        vocab_service_icontains (str | Unset):
        vocab_service_iendswith (str | Unset):
        vocab_service_iexact (str | Unset):
        vocab_service_in (list[str] | Unset):
        vocab_service_iregex (str | Unset):
        vocab_service_isnull (bool | Unset):
        vocab_service_istartswith (str | Unset):
        vocab_service_lt (str | Unset):
        vocab_service_lte (str | Unset):
        vocab_service_range (list[str] | Unset):
        vocab_service_regex (str | Unset):
        vocab_service_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVocabularyTermReadList]
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
        observation=observation,
        observation_in=observation_in,
        observation_isnull=observation_isnull,
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
    observation: list[int] | Unset = UNSET,
    observation_in: list[int] | Unset = UNSET,
    observation_isnull: bool | Unset = UNSET,
    offset: int | Unset = UNSET,
    ordering: str | Unset = UNSET,
    resolved_term: str | Unset = UNSET,
    resolved_term_contains: str | Unset = UNSET,
    resolved_term_endswith: str | Unset = UNSET,
    resolved_term_gt: str | Unset = UNSET,
    resolved_term_gte: str | Unset = UNSET,
    resolved_term_icontains: str | Unset = UNSET,
    resolved_term_iendswith: str | Unset = UNSET,
    resolved_term_iexact: str | Unset = UNSET,
    resolved_term_in: list[str] | Unset = UNSET,
    resolved_term_iregex: str | Unset = UNSET,
    resolved_term_isnull: bool | Unset = UNSET,
    resolved_term_istartswith: str | Unset = UNSET,
    resolved_term_lt: str | Unset = UNSET,
    resolved_term_lte: str | Unset = UNSET,
    resolved_term_range: list[str] | Unset = UNSET,
    resolved_term_regex: str | Unset = UNSET,
    resolved_term_startswith: str | Unset = UNSET,
    uri: str | Unset = UNSET,
    uri_contains: str | Unset = UNSET,
    uri_endswith: str | Unset = UNSET,
    uri_gt: str | Unset = UNSET,
    uri_gte: str | Unset = UNSET,
    uri_icontains: str | Unset = UNSET,
    uri_iendswith: str | Unset = UNSET,
    uri_iexact: str | Unset = UNSET,
    uri_in: list[str] | Unset = UNSET,
    uri_iregex: str | Unset = UNSET,
    uri_isnull: bool | Unset = UNSET,
    uri_istartswith: str | Unset = UNSET,
    uri_lt: str | Unset = UNSET,
    uri_lte: str | Unset = UNSET,
    uri_range: list[str] | Unset = UNSET,
    uri_regex: str | Unset = UNSET,
    uri_startswith: str | Unset = UNSET,
    vocab_service: VocabularytermsListVocabularyService | Unset = UNSET,
    vocab_service_contains: str | Unset = UNSET,
    vocab_service_endswith: str | Unset = UNSET,
    vocab_service_gt: str | Unset = UNSET,
    vocab_service_gte: str | Unset = UNSET,
    vocab_service_icontains: str | Unset = UNSET,
    vocab_service_iendswith: str | Unset = UNSET,
    vocab_service_iexact: str | Unset = UNSET,
    vocab_service_in: list[str] | Unset = UNSET,
    vocab_service_iregex: str | Unset = UNSET,
    vocab_service_isnull: bool | Unset = UNSET,
    vocab_service_istartswith: str | Unset = UNSET,
    vocab_service_lt: str | Unset = UNSET,
    vocab_service_lte: str | Unset = UNSET,
    vocab_service_range: list[str] | Unset = UNSET,
    vocab_service_regex: str | Unset = UNSET,
    vocab_service_startswith: str | Unset = UNSET,
) -> PaginatedVocabularyTermReadList | None:
    """Get a list of Vocabulary terms objects.

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
        observation (list[int] | Unset):
        observation_in (list[int] | Unset):
        observation_isnull (bool | Unset):
        offset (int | Unset):
        ordering (str | Unset):
        resolved_term (str | Unset):
        resolved_term_contains (str | Unset):
        resolved_term_endswith (str | Unset):
        resolved_term_gt (str | Unset):
        resolved_term_gte (str | Unset):
        resolved_term_icontains (str | Unset):
        resolved_term_iendswith (str | Unset):
        resolved_term_iexact (str | Unset):
        resolved_term_in (list[str] | Unset):
        resolved_term_iregex (str | Unset):
        resolved_term_isnull (bool | Unset):
        resolved_term_istartswith (str | Unset):
        resolved_term_lt (str | Unset):
        resolved_term_lte (str | Unset):
        resolved_term_range (list[str] | Unset):
        resolved_term_regex (str | Unset):
        resolved_term_startswith (str | Unset):
        uri (str | Unset):
        uri_contains (str | Unset):
        uri_endswith (str | Unset):
        uri_gt (str | Unset):
        uri_gte (str | Unset):
        uri_icontains (str | Unset):
        uri_iendswith (str | Unset):
        uri_iexact (str | Unset):
        uri_in (list[str] | Unset):
        uri_iregex (str | Unset):
        uri_isnull (bool | Unset):
        uri_istartswith (str | Unset):
        uri_lt (str | Unset):
        uri_lte (str | Unset):
        uri_range (list[str] | Unset):
        uri_regex (str | Unset):
        uri_startswith (str | Unset):
        vocab_service (VocabularytermsListVocabularyService | Unset):
        vocab_service_contains (str | Unset):
        vocab_service_endswith (str | Unset):
        vocab_service_gt (str | Unset):
        vocab_service_gte (str | Unset):
        vocab_service_icontains (str | Unset):
        vocab_service_iendswith (str | Unset):
        vocab_service_iexact (str | Unset):
        vocab_service_in (list[str] | Unset):
        vocab_service_iregex (str | Unset):
        vocab_service_isnull (bool | Unset):
        vocab_service_istartswith (str | Unset):
        vocab_service_lt (str | Unset):
        vocab_service_lte (str | Unset):
        vocab_service_range (list[str] | Unset):
        vocab_service_regex (str | Unset):
        vocab_service_startswith (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVocabularyTermReadList
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
            observation=observation,
            observation_in=observation_in,
            observation_isnull=observation_isnull,
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
