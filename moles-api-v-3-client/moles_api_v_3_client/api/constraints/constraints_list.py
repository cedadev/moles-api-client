from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constraints_list_access_category import ConstraintsListAccessCategory
from ...models.paginated_constraints_write_list import PaginatedConstraintsWriteList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    access_category: Union[Unset, ConstraintsListAccessCategory] = UNSET,
    access_category_contains: Union[Unset, str] = UNSET,
    access_category_endswith: Union[Unset, str] = UNSET,
    access_category_gt: Union[Unset, str] = UNSET,
    access_category_gte: Union[Unset, str] = UNSET,
    access_category_icontains: Union[Unset, str] = UNSET,
    access_category_iendswith: Union[Unset, str] = UNSET,
    access_category_iexact: Union[Unset, str] = UNSET,
    access_category_in: Union[Unset, list[str]] = UNSET,
    access_category_iregex: Union[Unset, str] = UNSET,
    access_category_isnull: Union[Unset, bool] = UNSET,
    access_category_istartswith: Union[Unset, str] = UNSET,
    access_category_lt: Union[Unset, str] = UNSET,
    access_category_lte: Union[Unset, str] = UNSET,
    access_category_range: Union[Unset, list[str]] = UNSET,
    access_category_regex: Union[Unset, str] = UNSET,
    access_category_startswith: Union[Unset, str] = UNSET,
    access_constraints: Union[Unset, str] = UNSET,
    access_constraints_contains: Union[Unset, str] = UNSET,
    access_constraints_endswith: Union[Unset, str] = UNSET,
    access_constraints_gt: Union[Unset, str] = UNSET,
    access_constraints_gte: Union[Unset, str] = UNSET,
    access_constraints_icontains: Union[Unset, str] = UNSET,
    access_constraints_iendswith: Union[Unset, str] = UNSET,
    access_constraints_iexact: Union[Unset, str] = UNSET,
    access_constraints_in: Union[Unset, list[str]] = UNSET,
    access_constraints_iregex: Union[Unset, str] = UNSET,
    access_constraints_isnull: Union[Unset, bool] = UNSET,
    access_constraints_istartswith: Union[Unset, str] = UNSET,
    access_constraints_lt: Union[Unset, str] = UNSET,
    access_constraints_lte: Union[Unset, str] = UNSET,
    access_constraints_range: Union[Unset, list[str]] = UNSET,
    access_constraints_regex: Union[Unset, str] = UNSET,
    access_constraints_startswith: Union[Unset, str] = UNSET,
    access_roles: Union[Unset, str] = UNSET,
    access_roles_contains: Union[Unset, str] = UNSET,
    access_roles_endswith: Union[Unset, str] = UNSET,
    access_roles_gt: Union[Unset, str] = UNSET,
    access_roles_gte: Union[Unset, str] = UNSET,
    access_roles_icontains: Union[Unset, str] = UNSET,
    access_roles_iendswith: Union[Unset, str] = UNSET,
    access_roles_iexact: Union[Unset, str] = UNSET,
    access_roles_in: Union[Unset, list[str]] = UNSET,
    access_roles_iregex: Union[Unset, str] = UNSET,
    access_roles_isnull: Union[Unset, bool] = UNSET,
    access_roles_istartswith: Union[Unset, str] = UNSET,
    access_roles_lt: Union[Unset, str] = UNSET,
    access_roles_lte: Union[Unset, str] = UNSET,
    access_roles_range: Union[Unset, list[str]] = UNSET,
    access_roles_regex: Union[Unset, str] = UNSET,
    access_roles_startswith: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    label_contains: Union[Unset, str] = UNSET,
    label_endswith: Union[Unset, str] = UNSET,
    label_gt: Union[Unset, str] = UNSET,
    label_gte: Union[Unset, str] = UNSET,
    label_icontains: Union[Unset, str] = UNSET,
    label_iendswith: Union[Unset, str] = UNSET,
    label_iexact: Union[Unset, str] = UNSET,
    label_in: Union[Unset, list[str]] = UNSET,
    label_iregex: Union[Unset, str] = UNSET,
    label_isnull: Union[Unset, bool] = UNSET,
    label_istartswith: Union[Unset, str] = UNSET,
    label_lt: Union[Unset, str] = UNSET,
    label_lte: Union[Unset, str] = UNSET,
    label_range: Union[Unset, list[str]] = UNSET,
    label_regex: Union[Unset, str] = UNSET,
    label_startswith: Union[Unset, str] = UNSET,
    licence: Union[Unset, int] = UNSET,
    licence_gt: Union[Unset, int] = UNSET,
    licence_gte: Union[Unset, int] = UNSET,
    licence_in: Union[Unset, list[int]] = UNSET,
    licence_isnull: Union[Unset, bool] = UNSET,
    licence_licence_classifications_classification: Union[Unset, str] = UNSET,
    licence_licence_classifications_classification_contains: Union[Unset, str] = UNSET,
    licence_licence_url: Union[Unset, str] = UNSET,
    licence_licence_url_contains: Union[Unset, str] = UNSET,
    licence_licence_url_in: Union[Unset, list[str]] = UNSET,
    licence_lt: Union[Unset, int] = UNSET,
    licence_lte: Union[Unset, int] = UNSET,
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
    use_limitation: Union[Unset, str] = UNSET,
    use_limitation_contains: Union[Unset, str] = UNSET,
    use_limitation_endswith: Union[Unset, str] = UNSET,
    use_limitation_gt: Union[Unset, str] = UNSET,
    use_limitation_gte: Union[Unset, str] = UNSET,
    use_limitation_icontains: Union[Unset, str] = UNSET,
    use_limitation_iendswith: Union[Unset, str] = UNSET,
    use_limitation_iexact: Union[Unset, str] = UNSET,
    use_limitation_in: Union[Unset, list[str]] = UNSET,
    use_limitation_iregex: Union[Unset, str] = UNSET,
    use_limitation_isnull: Union[Unset, bool] = UNSET,
    use_limitation_istartswith: Union[Unset, str] = UNSET,
    use_limitation_lt: Union[Unset, str] = UNSET,
    use_limitation_lte: Union[Unset, str] = UNSET,
    use_limitation_range: Union[Unset, list[str]] = UNSET,
    use_limitation_regex: Union[Unset, str] = UNSET,
    use_limitation_startswith: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_access_category: Union[Unset, str] = UNSET
    if not isinstance(access_category, Unset):
        json_access_category = access_category.value

    params["accessCategory"] = json_access_category

    params["accessCategory__contains"] = access_category_contains

    params["accessCategory__endswith"] = access_category_endswith

    params["accessCategory__gt"] = access_category_gt

    params["accessCategory__gte"] = access_category_gte

    params["accessCategory__icontains"] = access_category_icontains

    params["accessCategory__iendswith"] = access_category_iendswith

    params["accessCategory__iexact"] = access_category_iexact

    json_access_category_in: Union[Unset, list[str]] = UNSET
    if not isinstance(access_category_in, Unset):
        json_access_category_in = access_category_in

    params["accessCategory__in"] = json_access_category_in

    params["accessCategory__iregex"] = access_category_iregex

    params["accessCategory__isnull"] = access_category_isnull

    params["accessCategory__istartswith"] = access_category_istartswith

    params["accessCategory__lt"] = access_category_lt

    params["accessCategory__lte"] = access_category_lte

    json_access_category_range: Union[Unset, list[str]] = UNSET
    if not isinstance(access_category_range, Unset):
        json_access_category_range = access_category_range

    params["accessCategory__range"] = json_access_category_range

    params["accessCategory__regex"] = access_category_regex

    params["accessCategory__startswith"] = access_category_startswith

    params["accessConstraints"] = access_constraints

    params["accessConstraints__contains"] = access_constraints_contains

    params["accessConstraints__endswith"] = access_constraints_endswith

    params["accessConstraints__gt"] = access_constraints_gt

    params["accessConstraints__gte"] = access_constraints_gte

    params["accessConstraints__icontains"] = access_constraints_icontains

    params["accessConstraints__iendswith"] = access_constraints_iendswith

    params["accessConstraints__iexact"] = access_constraints_iexact

    json_access_constraints_in: Union[Unset, list[str]] = UNSET
    if not isinstance(access_constraints_in, Unset):
        json_access_constraints_in = access_constraints_in

    params["accessConstraints__in"] = json_access_constraints_in

    params["accessConstraints__iregex"] = access_constraints_iregex

    params["accessConstraints__isnull"] = access_constraints_isnull

    params["accessConstraints__istartswith"] = access_constraints_istartswith

    params["accessConstraints__lt"] = access_constraints_lt

    params["accessConstraints__lte"] = access_constraints_lte

    json_access_constraints_range: Union[Unset, list[str]] = UNSET
    if not isinstance(access_constraints_range, Unset):
        json_access_constraints_range = access_constraints_range

    params["accessConstraints__range"] = json_access_constraints_range

    params["accessConstraints__regex"] = access_constraints_regex

    params["accessConstraints__startswith"] = access_constraints_startswith

    params["accessRoles"] = access_roles

    params["accessRoles__contains"] = access_roles_contains

    params["accessRoles__endswith"] = access_roles_endswith

    params["accessRoles__gt"] = access_roles_gt

    params["accessRoles__gte"] = access_roles_gte

    params["accessRoles__icontains"] = access_roles_icontains

    params["accessRoles__iendswith"] = access_roles_iendswith

    params["accessRoles__iexact"] = access_roles_iexact

    json_access_roles_in: Union[Unset, list[str]] = UNSET
    if not isinstance(access_roles_in, Unset):
        json_access_roles_in = access_roles_in

    params["accessRoles__in"] = json_access_roles_in

    params["accessRoles__iregex"] = access_roles_iregex

    params["accessRoles__isnull"] = access_roles_isnull

    params["accessRoles__istartswith"] = access_roles_istartswith

    params["accessRoles__lt"] = access_roles_lt

    params["accessRoles__lte"] = access_roles_lte

    json_access_roles_range: Union[Unset, list[str]] = UNSET
    if not isinstance(access_roles_range, Unset):
        json_access_roles_range = access_roles_range

    params["accessRoles__range"] = json_access_roles_range

    params["accessRoles__regex"] = access_roles_regex

    params["accessRoles__startswith"] = access_roles_startswith

    params["label"] = label

    params["label__contains"] = label_contains

    params["label__endswith"] = label_endswith

    params["label__gt"] = label_gt

    params["label__gte"] = label_gte

    params["label__icontains"] = label_icontains

    params["label__iendswith"] = label_iendswith

    params["label__iexact"] = label_iexact

    json_label_in: Union[Unset, list[str]] = UNSET
    if not isinstance(label_in, Unset):
        json_label_in = label_in

    params["label__in"] = json_label_in

    params["label__iregex"] = label_iregex

    params["label__isnull"] = label_isnull

    params["label__istartswith"] = label_istartswith

    params["label__lt"] = label_lt

    params["label__lte"] = label_lte

    json_label_range: Union[Unset, list[str]] = UNSET
    if not isinstance(label_range, Unset):
        json_label_range = label_range

    params["label__range"] = json_label_range

    params["label__regex"] = label_regex

    params["label__startswith"] = label_startswith

    params["licence"] = licence

    params["licence__gt"] = licence_gt

    params["licence__gte"] = licence_gte

    json_licence_in: Union[Unset, list[int]] = UNSET
    if not isinstance(licence_in, Unset):
        json_licence_in = licence_in

    params["licence__in"] = json_licence_in

    params["licence__isnull"] = licence_isnull

    params["licence__licenceClassifications__classification"] = licence_licence_classifications_classification

    params["licence__licenceClassifications__classification__contains"] = (
        licence_licence_classifications_classification_contains
    )

    params["licence__licenceURL"] = licence_licence_url

    params["licence__licenceURL__contains"] = licence_licence_url_contains

    json_licence_licence_url_in: Union[Unset, list[str]] = UNSET
    if not isinstance(licence_licence_url_in, Unset):
        json_licence_licence_url_in = licence_licence_url_in

    params["licence__licenceURL__in"] = json_licence_licence_url_in

    params["licence__lt"] = licence_lt

    params["licence__lte"] = licence_lte

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

    params["useLimitation"] = use_limitation

    params["useLimitation__contains"] = use_limitation_contains

    params["useLimitation__endswith"] = use_limitation_endswith

    params["useLimitation__gt"] = use_limitation_gt

    params["useLimitation__gte"] = use_limitation_gte

    params["useLimitation__icontains"] = use_limitation_icontains

    params["useLimitation__iendswith"] = use_limitation_iendswith

    params["useLimitation__iexact"] = use_limitation_iexact

    json_use_limitation_in: Union[Unset, list[str]] = UNSET
    if not isinstance(use_limitation_in, Unset):
        json_use_limitation_in = use_limitation_in

    params["useLimitation__in"] = json_use_limitation_in

    params["useLimitation__iregex"] = use_limitation_iregex

    params["useLimitation__isnull"] = use_limitation_isnull

    params["useLimitation__istartswith"] = use_limitation_istartswith

    params["useLimitation__lt"] = use_limitation_lt

    params["useLimitation__lte"] = use_limitation_lte

    json_use_limitation_range: Union[Unset, list[str]] = UNSET
    if not isinstance(use_limitation_range, Unset):
        json_use_limitation_range = use_limitation_range

    params["useLimitation__range"] = json_use_limitation_range

    params["useLimitation__regex"] = use_limitation_regex

    params["useLimitation__startswith"] = use_limitation_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/constraints/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedConstraintsWriteList]:
    if response.status_code == 200:
        response_200 = PaginatedConstraintsWriteList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedConstraintsWriteList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    access_category: Union[Unset, ConstraintsListAccessCategory] = UNSET,
    access_category_contains: Union[Unset, str] = UNSET,
    access_category_endswith: Union[Unset, str] = UNSET,
    access_category_gt: Union[Unset, str] = UNSET,
    access_category_gte: Union[Unset, str] = UNSET,
    access_category_icontains: Union[Unset, str] = UNSET,
    access_category_iendswith: Union[Unset, str] = UNSET,
    access_category_iexact: Union[Unset, str] = UNSET,
    access_category_in: Union[Unset, list[str]] = UNSET,
    access_category_iregex: Union[Unset, str] = UNSET,
    access_category_isnull: Union[Unset, bool] = UNSET,
    access_category_istartswith: Union[Unset, str] = UNSET,
    access_category_lt: Union[Unset, str] = UNSET,
    access_category_lte: Union[Unset, str] = UNSET,
    access_category_range: Union[Unset, list[str]] = UNSET,
    access_category_regex: Union[Unset, str] = UNSET,
    access_category_startswith: Union[Unset, str] = UNSET,
    access_constraints: Union[Unset, str] = UNSET,
    access_constraints_contains: Union[Unset, str] = UNSET,
    access_constraints_endswith: Union[Unset, str] = UNSET,
    access_constraints_gt: Union[Unset, str] = UNSET,
    access_constraints_gte: Union[Unset, str] = UNSET,
    access_constraints_icontains: Union[Unset, str] = UNSET,
    access_constraints_iendswith: Union[Unset, str] = UNSET,
    access_constraints_iexact: Union[Unset, str] = UNSET,
    access_constraints_in: Union[Unset, list[str]] = UNSET,
    access_constraints_iregex: Union[Unset, str] = UNSET,
    access_constraints_isnull: Union[Unset, bool] = UNSET,
    access_constraints_istartswith: Union[Unset, str] = UNSET,
    access_constraints_lt: Union[Unset, str] = UNSET,
    access_constraints_lte: Union[Unset, str] = UNSET,
    access_constraints_range: Union[Unset, list[str]] = UNSET,
    access_constraints_regex: Union[Unset, str] = UNSET,
    access_constraints_startswith: Union[Unset, str] = UNSET,
    access_roles: Union[Unset, str] = UNSET,
    access_roles_contains: Union[Unset, str] = UNSET,
    access_roles_endswith: Union[Unset, str] = UNSET,
    access_roles_gt: Union[Unset, str] = UNSET,
    access_roles_gte: Union[Unset, str] = UNSET,
    access_roles_icontains: Union[Unset, str] = UNSET,
    access_roles_iendswith: Union[Unset, str] = UNSET,
    access_roles_iexact: Union[Unset, str] = UNSET,
    access_roles_in: Union[Unset, list[str]] = UNSET,
    access_roles_iregex: Union[Unset, str] = UNSET,
    access_roles_isnull: Union[Unset, bool] = UNSET,
    access_roles_istartswith: Union[Unset, str] = UNSET,
    access_roles_lt: Union[Unset, str] = UNSET,
    access_roles_lte: Union[Unset, str] = UNSET,
    access_roles_range: Union[Unset, list[str]] = UNSET,
    access_roles_regex: Union[Unset, str] = UNSET,
    access_roles_startswith: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    label_contains: Union[Unset, str] = UNSET,
    label_endswith: Union[Unset, str] = UNSET,
    label_gt: Union[Unset, str] = UNSET,
    label_gte: Union[Unset, str] = UNSET,
    label_icontains: Union[Unset, str] = UNSET,
    label_iendswith: Union[Unset, str] = UNSET,
    label_iexact: Union[Unset, str] = UNSET,
    label_in: Union[Unset, list[str]] = UNSET,
    label_iregex: Union[Unset, str] = UNSET,
    label_isnull: Union[Unset, bool] = UNSET,
    label_istartswith: Union[Unset, str] = UNSET,
    label_lt: Union[Unset, str] = UNSET,
    label_lte: Union[Unset, str] = UNSET,
    label_range: Union[Unset, list[str]] = UNSET,
    label_regex: Union[Unset, str] = UNSET,
    label_startswith: Union[Unset, str] = UNSET,
    licence: Union[Unset, int] = UNSET,
    licence_gt: Union[Unset, int] = UNSET,
    licence_gte: Union[Unset, int] = UNSET,
    licence_in: Union[Unset, list[int]] = UNSET,
    licence_isnull: Union[Unset, bool] = UNSET,
    licence_licence_classifications_classification: Union[Unset, str] = UNSET,
    licence_licence_classifications_classification_contains: Union[Unset, str] = UNSET,
    licence_licence_url: Union[Unset, str] = UNSET,
    licence_licence_url_contains: Union[Unset, str] = UNSET,
    licence_licence_url_in: Union[Unset, list[str]] = UNSET,
    licence_lt: Union[Unset, int] = UNSET,
    licence_lte: Union[Unset, int] = UNSET,
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
    use_limitation: Union[Unset, str] = UNSET,
    use_limitation_contains: Union[Unset, str] = UNSET,
    use_limitation_endswith: Union[Unset, str] = UNSET,
    use_limitation_gt: Union[Unset, str] = UNSET,
    use_limitation_gte: Union[Unset, str] = UNSET,
    use_limitation_icontains: Union[Unset, str] = UNSET,
    use_limitation_iendswith: Union[Unset, str] = UNSET,
    use_limitation_iexact: Union[Unset, str] = UNSET,
    use_limitation_in: Union[Unset, list[str]] = UNSET,
    use_limitation_iregex: Union[Unset, str] = UNSET,
    use_limitation_isnull: Union[Unset, bool] = UNSET,
    use_limitation_istartswith: Union[Unset, str] = UNSET,
    use_limitation_lt: Union[Unset, str] = UNSET,
    use_limitation_lte: Union[Unset, str] = UNSET,
    use_limitation_range: Union[Unset, list[str]] = UNSET,
    use_limitation_regex: Union[Unset, str] = UNSET,
    use_limitation_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedConstraintsWriteList]:
    """Get a list of Constraints objects.

    Args:
        access_category (Union[Unset, ConstraintsListAccessCategory]):
        access_category_contains (Union[Unset, str]):
        access_category_endswith (Union[Unset, str]):
        access_category_gt (Union[Unset, str]):
        access_category_gte (Union[Unset, str]):
        access_category_icontains (Union[Unset, str]):
        access_category_iendswith (Union[Unset, str]):
        access_category_iexact (Union[Unset, str]):
        access_category_in (Union[Unset, list[str]]):
        access_category_iregex (Union[Unset, str]):
        access_category_isnull (Union[Unset, bool]):
        access_category_istartswith (Union[Unset, str]):
        access_category_lt (Union[Unset, str]):
        access_category_lte (Union[Unset, str]):
        access_category_range (Union[Unset, list[str]]):
        access_category_regex (Union[Unset, str]):
        access_category_startswith (Union[Unset, str]):
        access_constraints (Union[Unset, str]):
        access_constraints_contains (Union[Unset, str]):
        access_constraints_endswith (Union[Unset, str]):
        access_constraints_gt (Union[Unset, str]):
        access_constraints_gte (Union[Unset, str]):
        access_constraints_icontains (Union[Unset, str]):
        access_constraints_iendswith (Union[Unset, str]):
        access_constraints_iexact (Union[Unset, str]):
        access_constraints_in (Union[Unset, list[str]]):
        access_constraints_iregex (Union[Unset, str]):
        access_constraints_isnull (Union[Unset, bool]):
        access_constraints_istartswith (Union[Unset, str]):
        access_constraints_lt (Union[Unset, str]):
        access_constraints_lte (Union[Unset, str]):
        access_constraints_range (Union[Unset, list[str]]):
        access_constraints_regex (Union[Unset, str]):
        access_constraints_startswith (Union[Unset, str]):
        access_roles (Union[Unset, str]):
        access_roles_contains (Union[Unset, str]):
        access_roles_endswith (Union[Unset, str]):
        access_roles_gt (Union[Unset, str]):
        access_roles_gte (Union[Unset, str]):
        access_roles_icontains (Union[Unset, str]):
        access_roles_iendswith (Union[Unset, str]):
        access_roles_iexact (Union[Unset, str]):
        access_roles_in (Union[Unset, list[str]]):
        access_roles_iregex (Union[Unset, str]):
        access_roles_isnull (Union[Unset, bool]):
        access_roles_istartswith (Union[Unset, str]):
        access_roles_lt (Union[Unset, str]):
        access_roles_lte (Union[Unset, str]):
        access_roles_range (Union[Unset, list[str]]):
        access_roles_regex (Union[Unset, str]):
        access_roles_startswith (Union[Unset, str]):
        label (Union[Unset, str]):
        label_contains (Union[Unset, str]):
        label_endswith (Union[Unset, str]):
        label_gt (Union[Unset, str]):
        label_gte (Union[Unset, str]):
        label_icontains (Union[Unset, str]):
        label_iendswith (Union[Unset, str]):
        label_iexact (Union[Unset, str]):
        label_in (Union[Unset, list[str]]):
        label_iregex (Union[Unset, str]):
        label_isnull (Union[Unset, bool]):
        label_istartswith (Union[Unset, str]):
        label_lt (Union[Unset, str]):
        label_lte (Union[Unset, str]):
        label_range (Union[Unset, list[str]]):
        label_regex (Union[Unset, str]):
        label_startswith (Union[Unset, str]):
        licence (Union[Unset, int]):
        licence_gt (Union[Unset, int]):
        licence_gte (Union[Unset, int]):
        licence_in (Union[Unset, list[int]]):
        licence_isnull (Union[Unset, bool]):
        licence_licence_classifications_classification (Union[Unset, str]):
        licence_licence_classifications_classification_contains (Union[Unset, str]):
        licence_licence_url (Union[Unset, str]):
        licence_licence_url_contains (Union[Unset, str]):
        licence_licence_url_in (Union[Unset, list[str]]):
        licence_lt (Union[Unset, int]):
        licence_lte (Union[Unset, int]):
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
        use_limitation (Union[Unset, str]):
        use_limitation_contains (Union[Unset, str]):
        use_limitation_endswith (Union[Unset, str]):
        use_limitation_gt (Union[Unset, str]):
        use_limitation_gte (Union[Unset, str]):
        use_limitation_icontains (Union[Unset, str]):
        use_limitation_iendswith (Union[Unset, str]):
        use_limitation_iexact (Union[Unset, str]):
        use_limitation_in (Union[Unset, list[str]]):
        use_limitation_iregex (Union[Unset, str]):
        use_limitation_isnull (Union[Unset, bool]):
        use_limitation_istartswith (Union[Unset, str]):
        use_limitation_lt (Union[Unset, str]):
        use_limitation_lte (Union[Unset, str]):
        use_limitation_range (Union[Unset, list[str]]):
        use_limitation_regex (Union[Unset, str]):
        use_limitation_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConstraintsWriteList]
    """

    kwargs = _get_kwargs(
        access_category=access_category,
        access_category_contains=access_category_contains,
        access_category_endswith=access_category_endswith,
        access_category_gt=access_category_gt,
        access_category_gte=access_category_gte,
        access_category_icontains=access_category_icontains,
        access_category_iendswith=access_category_iendswith,
        access_category_iexact=access_category_iexact,
        access_category_in=access_category_in,
        access_category_iregex=access_category_iregex,
        access_category_isnull=access_category_isnull,
        access_category_istartswith=access_category_istartswith,
        access_category_lt=access_category_lt,
        access_category_lte=access_category_lte,
        access_category_range=access_category_range,
        access_category_regex=access_category_regex,
        access_category_startswith=access_category_startswith,
        access_constraints=access_constraints,
        access_constraints_contains=access_constraints_contains,
        access_constraints_endswith=access_constraints_endswith,
        access_constraints_gt=access_constraints_gt,
        access_constraints_gte=access_constraints_gte,
        access_constraints_icontains=access_constraints_icontains,
        access_constraints_iendswith=access_constraints_iendswith,
        access_constraints_iexact=access_constraints_iexact,
        access_constraints_in=access_constraints_in,
        access_constraints_iregex=access_constraints_iregex,
        access_constraints_isnull=access_constraints_isnull,
        access_constraints_istartswith=access_constraints_istartswith,
        access_constraints_lt=access_constraints_lt,
        access_constraints_lte=access_constraints_lte,
        access_constraints_range=access_constraints_range,
        access_constraints_regex=access_constraints_regex,
        access_constraints_startswith=access_constraints_startswith,
        access_roles=access_roles,
        access_roles_contains=access_roles_contains,
        access_roles_endswith=access_roles_endswith,
        access_roles_gt=access_roles_gt,
        access_roles_gte=access_roles_gte,
        access_roles_icontains=access_roles_icontains,
        access_roles_iendswith=access_roles_iendswith,
        access_roles_iexact=access_roles_iexact,
        access_roles_in=access_roles_in,
        access_roles_iregex=access_roles_iregex,
        access_roles_isnull=access_roles_isnull,
        access_roles_istartswith=access_roles_istartswith,
        access_roles_lt=access_roles_lt,
        access_roles_lte=access_roles_lte,
        access_roles_range=access_roles_range,
        access_roles_regex=access_roles_regex,
        access_roles_startswith=access_roles_startswith,
        label=label,
        label_contains=label_contains,
        label_endswith=label_endswith,
        label_gt=label_gt,
        label_gte=label_gte,
        label_icontains=label_icontains,
        label_iendswith=label_iendswith,
        label_iexact=label_iexact,
        label_in=label_in,
        label_iregex=label_iregex,
        label_isnull=label_isnull,
        label_istartswith=label_istartswith,
        label_lt=label_lt,
        label_lte=label_lte,
        label_range=label_range,
        label_regex=label_regex,
        label_startswith=label_startswith,
        licence=licence,
        licence_gt=licence_gt,
        licence_gte=licence_gte,
        licence_in=licence_in,
        licence_isnull=licence_isnull,
        licence_licence_classifications_classification=licence_licence_classifications_classification,
        licence_licence_classifications_classification_contains=licence_licence_classifications_classification_contains,
        licence_licence_url=licence_licence_url,
        licence_licence_url_contains=licence_licence_url_contains,
        licence_licence_url_in=licence_licence_url_in,
        licence_lt=licence_lt,
        licence_lte=licence_lte,
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
        use_limitation=use_limitation,
        use_limitation_contains=use_limitation_contains,
        use_limitation_endswith=use_limitation_endswith,
        use_limitation_gt=use_limitation_gt,
        use_limitation_gte=use_limitation_gte,
        use_limitation_icontains=use_limitation_icontains,
        use_limitation_iendswith=use_limitation_iendswith,
        use_limitation_iexact=use_limitation_iexact,
        use_limitation_in=use_limitation_in,
        use_limitation_iregex=use_limitation_iregex,
        use_limitation_isnull=use_limitation_isnull,
        use_limitation_istartswith=use_limitation_istartswith,
        use_limitation_lt=use_limitation_lt,
        use_limitation_lte=use_limitation_lte,
        use_limitation_range=use_limitation_range,
        use_limitation_regex=use_limitation_regex,
        use_limitation_startswith=use_limitation_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    access_category: Union[Unset, ConstraintsListAccessCategory] = UNSET,
    access_category_contains: Union[Unset, str] = UNSET,
    access_category_endswith: Union[Unset, str] = UNSET,
    access_category_gt: Union[Unset, str] = UNSET,
    access_category_gte: Union[Unset, str] = UNSET,
    access_category_icontains: Union[Unset, str] = UNSET,
    access_category_iendswith: Union[Unset, str] = UNSET,
    access_category_iexact: Union[Unset, str] = UNSET,
    access_category_in: Union[Unset, list[str]] = UNSET,
    access_category_iregex: Union[Unset, str] = UNSET,
    access_category_isnull: Union[Unset, bool] = UNSET,
    access_category_istartswith: Union[Unset, str] = UNSET,
    access_category_lt: Union[Unset, str] = UNSET,
    access_category_lte: Union[Unset, str] = UNSET,
    access_category_range: Union[Unset, list[str]] = UNSET,
    access_category_regex: Union[Unset, str] = UNSET,
    access_category_startswith: Union[Unset, str] = UNSET,
    access_constraints: Union[Unset, str] = UNSET,
    access_constraints_contains: Union[Unset, str] = UNSET,
    access_constraints_endswith: Union[Unset, str] = UNSET,
    access_constraints_gt: Union[Unset, str] = UNSET,
    access_constraints_gte: Union[Unset, str] = UNSET,
    access_constraints_icontains: Union[Unset, str] = UNSET,
    access_constraints_iendswith: Union[Unset, str] = UNSET,
    access_constraints_iexact: Union[Unset, str] = UNSET,
    access_constraints_in: Union[Unset, list[str]] = UNSET,
    access_constraints_iregex: Union[Unset, str] = UNSET,
    access_constraints_isnull: Union[Unset, bool] = UNSET,
    access_constraints_istartswith: Union[Unset, str] = UNSET,
    access_constraints_lt: Union[Unset, str] = UNSET,
    access_constraints_lte: Union[Unset, str] = UNSET,
    access_constraints_range: Union[Unset, list[str]] = UNSET,
    access_constraints_regex: Union[Unset, str] = UNSET,
    access_constraints_startswith: Union[Unset, str] = UNSET,
    access_roles: Union[Unset, str] = UNSET,
    access_roles_contains: Union[Unset, str] = UNSET,
    access_roles_endswith: Union[Unset, str] = UNSET,
    access_roles_gt: Union[Unset, str] = UNSET,
    access_roles_gte: Union[Unset, str] = UNSET,
    access_roles_icontains: Union[Unset, str] = UNSET,
    access_roles_iendswith: Union[Unset, str] = UNSET,
    access_roles_iexact: Union[Unset, str] = UNSET,
    access_roles_in: Union[Unset, list[str]] = UNSET,
    access_roles_iregex: Union[Unset, str] = UNSET,
    access_roles_isnull: Union[Unset, bool] = UNSET,
    access_roles_istartswith: Union[Unset, str] = UNSET,
    access_roles_lt: Union[Unset, str] = UNSET,
    access_roles_lte: Union[Unset, str] = UNSET,
    access_roles_range: Union[Unset, list[str]] = UNSET,
    access_roles_regex: Union[Unset, str] = UNSET,
    access_roles_startswith: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    label_contains: Union[Unset, str] = UNSET,
    label_endswith: Union[Unset, str] = UNSET,
    label_gt: Union[Unset, str] = UNSET,
    label_gte: Union[Unset, str] = UNSET,
    label_icontains: Union[Unset, str] = UNSET,
    label_iendswith: Union[Unset, str] = UNSET,
    label_iexact: Union[Unset, str] = UNSET,
    label_in: Union[Unset, list[str]] = UNSET,
    label_iregex: Union[Unset, str] = UNSET,
    label_isnull: Union[Unset, bool] = UNSET,
    label_istartswith: Union[Unset, str] = UNSET,
    label_lt: Union[Unset, str] = UNSET,
    label_lte: Union[Unset, str] = UNSET,
    label_range: Union[Unset, list[str]] = UNSET,
    label_regex: Union[Unset, str] = UNSET,
    label_startswith: Union[Unset, str] = UNSET,
    licence: Union[Unset, int] = UNSET,
    licence_gt: Union[Unset, int] = UNSET,
    licence_gte: Union[Unset, int] = UNSET,
    licence_in: Union[Unset, list[int]] = UNSET,
    licence_isnull: Union[Unset, bool] = UNSET,
    licence_licence_classifications_classification: Union[Unset, str] = UNSET,
    licence_licence_classifications_classification_contains: Union[Unset, str] = UNSET,
    licence_licence_url: Union[Unset, str] = UNSET,
    licence_licence_url_contains: Union[Unset, str] = UNSET,
    licence_licence_url_in: Union[Unset, list[str]] = UNSET,
    licence_lt: Union[Unset, int] = UNSET,
    licence_lte: Union[Unset, int] = UNSET,
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
    use_limitation: Union[Unset, str] = UNSET,
    use_limitation_contains: Union[Unset, str] = UNSET,
    use_limitation_endswith: Union[Unset, str] = UNSET,
    use_limitation_gt: Union[Unset, str] = UNSET,
    use_limitation_gte: Union[Unset, str] = UNSET,
    use_limitation_icontains: Union[Unset, str] = UNSET,
    use_limitation_iendswith: Union[Unset, str] = UNSET,
    use_limitation_iexact: Union[Unset, str] = UNSET,
    use_limitation_in: Union[Unset, list[str]] = UNSET,
    use_limitation_iregex: Union[Unset, str] = UNSET,
    use_limitation_isnull: Union[Unset, bool] = UNSET,
    use_limitation_istartswith: Union[Unset, str] = UNSET,
    use_limitation_lt: Union[Unset, str] = UNSET,
    use_limitation_lte: Union[Unset, str] = UNSET,
    use_limitation_range: Union[Unset, list[str]] = UNSET,
    use_limitation_regex: Union[Unset, str] = UNSET,
    use_limitation_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedConstraintsWriteList]:
    """Get a list of Constraints objects.

    Args:
        access_category (Union[Unset, ConstraintsListAccessCategory]):
        access_category_contains (Union[Unset, str]):
        access_category_endswith (Union[Unset, str]):
        access_category_gt (Union[Unset, str]):
        access_category_gte (Union[Unset, str]):
        access_category_icontains (Union[Unset, str]):
        access_category_iendswith (Union[Unset, str]):
        access_category_iexact (Union[Unset, str]):
        access_category_in (Union[Unset, list[str]]):
        access_category_iregex (Union[Unset, str]):
        access_category_isnull (Union[Unset, bool]):
        access_category_istartswith (Union[Unset, str]):
        access_category_lt (Union[Unset, str]):
        access_category_lte (Union[Unset, str]):
        access_category_range (Union[Unset, list[str]]):
        access_category_regex (Union[Unset, str]):
        access_category_startswith (Union[Unset, str]):
        access_constraints (Union[Unset, str]):
        access_constraints_contains (Union[Unset, str]):
        access_constraints_endswith (Union[Unset, str]):
        access_constraints_gt (Union[Unset, str]):
        access_constraints_gte (Union[Unset, str]):
        access_constraints_icontains (Union[Unset, str]):
        access_constraints_iendswith (Union[Unset, str]):
        access_constraints_iexact (Union[Unset, str]):
        access_constraints_in (Union[Unset, list[str]]):
        access_constraints_iregex (Union[Unset, str]):
        access_constraints_isnull (Union[Unset, bool]):
        access_constraints_istartswith (Union[Unset, str]):
        access_constraints_lt (Union[Unset, str]):
        access_constraints_lte (Union[Unset, str]):
        access_constraints_range (Union[Unset, list[str]]):
        access_constraints_regex (Union[Unset, str]):
        access_constraints_startswith (Union[Unset, str]):
        access_roles (Union[Unset, str]):
        access_roles_contains (Union[Unset, str]):
        access_roles_endswith (Union[Unset, str]):
        access_roles_gt (Union[Unset, str]):
        access_roles_gte (Union[Unset, str]):
        access_roles_icontains (Union[Unset, str]):
        access_roles_iendswith (Union[Unset, str]):
        access_roles_iexact (Union[Unset, str]):
        access_roles_in (Union[Unset, list[str]]):
        access_roles_iregex (Union[Unset, str]):
        access_roles_isnull (Union[Unset, bool]):
        access_roles_istartswith (Union[Unset, str]):
        access_roles_lt (Union[Unset, str]):
        access_roles_lte (Union[Unset, str]):
        access_roles_range (Union[Unset, list[str]]):
        access_roles_regex (Union[Unset, str]):
        access_roles_startswith (Union[Unset, str]):
        label (Union[Unset, str]):
        label_contains (Union[Unset, str]):
        label_endswith (Union[Unset, str]):
        label_gt (Union[Unset, str]):
        label_gte (Union[Unset, str]):
        label_icontains (Union[Unset, str]):
        label_iendswith (Union[Unset, str]):
        label_iexact (Union[Unset, str]):
        label_in (Union[Unset, list[str]]):
        label_iregex (Union[Unset, str]):
        label_isnull (Union[Unset, bool]):
        label_istartswith (Union[Unset, str]):
        label_lt (Union[Unset, str]):
        label_lte (Union[Unset, str]):
        label_range (Union[Unset, list[str]]):
        label_regex (Union[Unset, str]):
        label_startswith (Union[Unset, str]):
        licence (Union[Unset, int]):
        licence_gt (Union[Unset, int]):
        licence_gte (Union[Unset, int]):
        licence_in (Union[Unset, list[int]]):
        licence_isnull (Union[Unset, bool]):
        licence_licence_classifications_classification (Union[Unset, str]):
        licence_licence_classifications_classification_contains (Union[Unset, str]):
        licence_licence_url (Union[Unset, str]):
        licence_licence_url_contains (Union[Unset, str]):
        licence_licence_url_in (Union[Unset, list[str]]):
        licence_lt (Union[Unset, int]):
        licence_lte (Union[Unset, int]):
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
        use_limitation (Union[Unset, str]):
        use_limitation_contains (Union[Unset, str]):
        use_limitation_endswith (Union[Unset, str]):
        use_limitation_gt (Union[Unset, str]):
        use_limitation_gte (Union[Unset, str]):
        use_limitation_icontains (Union[Unset, str]):
        use_limitation_iendswith (Union[Unset, str]):
        use_limitation_iexact (Union[Unset, str]):
        use_limitation_in (Union[Unset, list[str]]):
        use_limitation_iregex (Union[Unset, str]):
        use_limitation_isnull (Union[Unset, bool]):
        use_limitation_istartswith (Union[Unset, str]):
        use_limitation_lt (Union[Unset, str]):
        use_limitation_lte (Union[Unset, str]):
        use_limitation_range (Union[Unset, list[str]]):
        use_limitation_regex (Union[Unset, str]):
        use_limitation_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConstraintsWriteList
    """

    return sync_detailed(
        client=client,
        access_category=access_category,
        access_category_contains=access_category_contains,
        access_category_endswith=access_category_endswith,
        access_category_gt=access_category_gt,
        access_category_gte=access_category_gte,
        access_category_icontains=access_category_icontains,
        access_category_iendswith=access_category_iendswith,
        access_category_iexact=access_category_iexact,
        access_category_in=access_category_in,
        access_category_iregex=access_category_iregex,
        access_category_isnull=access_category_isnull,
        access_category_istartswith=access_category_istartswith,
        access_category_lt=access_category_lt,
        access_category_lte=access_category_lte,
        access_category_range=access_category_range,
        access_category_regex=access_category_regex,
        access_category_startswith=access_category_startswith,
        access_constraints=access_constraints,
        access_constraints_contains=access_constraints_contains,
        access_constraints_endswith=access_constraints_endswith,
        access_constraints_gt=access_constraints_gt,
        access_constraints_gte=access_constraints_gte,
        access_constraints_icontains=access_constraints_icontains,
        access_constraints_iendswith=access_constraints_iendswith,
        access_constraints_iexact=access_constraints_iexact,
        access_constraints_in=access_constraints_in,
        access_constraints_iregex=access_constraints_iregex,
        access_constraints_isnull=access_constraints_isnull,
        access_constraints_istartswith=access_constraints_istartswith,
        access_constraints_lt=access_constraints_lt,
        access_constraints_lte=access_constraints_lte,
        access_constraints_range=access_constraints_range,
        access_constraints_regex=access_constraints_regex,
        access_constraints_startswith=access_constraints_startswith,
        access_roles=access_roles,
        access_roles_contains=access_roles_contains,
        access_roles_endswith=access_roles_endswith,
        access_roles_gt=access_roles_gt,
        access_roles_gte=access_roles_gte,
        access_roles_icontains=access_roles_icontains,
        access_roles_iendswith=access_roles_iendswith,
        access_roles_iexact=access_roles_iexact,
        access_roles_in=access_roles_in,
        access_roles_iregex=access_roles_iregex,
        access_roles_isnull=access_roles_isnull,
        access_roles_istartswith=access_roles_istartswith,
        access_roles_lt=access_roles_lt,
        access_roles_lte=access_roles_lte,
        access_roles_range=access_roles_range,
        access_roles_regex=access_roles_regex,
        access_roles_startswith=access_roles_startswith,
        label=label,
        label_contains=label_contains,
        label_endswith=label_endswith,
        label_gt=label_gt,
        label_gte=label_gte,
        label_icontains=label_icontains,
        label_iendswith=label_iendswith,
        label_iexact=label_iexact,
        label_in=label_in,
        label_iregex=label_iregex,
        label_isnull=label_isnull,
        label_istartswith=label_istartswith,
        label_lt=label_lt,
        label_lte=label_lte,
        label_range=label_range,
        label_regex=label_regex,
        label_startswith=label_startswith,
        licence=licence,
        licence_gt=licence_gt,
        licence_gte=licence_gte,
        licence_in=licence_in,
        licence_isnull=licence_isnull,
        licence_licence_classifications_classification=licence_licence_classifications_classification,
        licence_licence_classifications_classification_contains=licence_licence_classifications_classification_contains,
        licence_licence_url=licence_licence_url,
        licence_licence_url_contains=licence_licence_url_contains,
        licence_licence_url_in=licence_licence_url_in,
        licence_lt=licence_lt,
        licence_lte=licence_lte,
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
        use_limitation=use_limitation,
        use_limitation_contains=use_limitation_contains,
        use_limitation_endswith=use_limitation_endswith,
        use_limitation_gt=use_limitation_gt,
        use_limitation_gte=use_limitation_gte,
        use_limitation_icontains=use_limitation_icontains,
        use_limitation_iendswith=use_limitation_iendswith,
        use_limitation_iexact=use_limitation_iexact,
        use_limitation_in=use_limitation_in,
        use_limitation_iregex=use_limitation_iregex,
        use_limitation_isnull=use_limitation_isnull,
        use_limitation_istartswith=use_limitation_istartswith,
        use_limitation_lt=use_limitation_lt,
        use_limitation_lte=use_limitation_lte,
        use_limitation_range=use_limitation_range,
        use_limitation_regex=use_limitation_regex,
        use_limitation_startswith=use_limitation_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    access_category: Union[Unset, ConstraintsListAccessCategory] = UNSET,
    access_category_contains: Union[Unset, str] = UNSET,
    access_category_endswith: Union[Unset, str] = UNSET,
    access_category_gt: Union[Unset, str] = UNSET,
    access_category_gte: Union[Unset, str] = UNSET,
    access_category_icontains: Union[Unset, str] = UNSET,
    access_category_iendswith: Union[Unset, str] = UNSET,
    access_category_iexact: Union[Unset, str] = UNSET,
    access_category_in: Union[Unset, list[str]] = UNSET,
    access_category_iregex: Union[Unset, str] = UNSET,
    access_category_isnull: Union[Unset, bool] = UNSET,
    access_category_istartswith: Union[Unset, str] = UNSET,
    access_category_lt: Union[Unset, str] = UNSET,
    access_category_lte: Union[Unset, str] = UNSET,
    access_category_range: Union[Unset, list[str]] = UNSET,
    access_category_regex: Union[Unset, str] = UNSET,
    access_category_startswith: Union[Unset, str] = UNSET,
    access_constraints: Union[Unset, str] = UNSET,
    access_constraints_contains: Union[Unset, str] = UNSET,
    access_constraints_endswith: Union[Unset, str] = UNSET,
    access_constraints_gt: Union[Unset, str] = UNSET,
    access_constraints_gte: Union[Unset, str] = UNSET,
    access_constraints_icontains: Union[Unset, str] = UNSET,
    access_constraints_iendswith: Union[Unset, str] = UNSET,
    access_constraints_iexact: Union[Unset, str] = UNSET,
    access_constraints_in: Union[Unset, list[str]] = UNSET,
    access_constraints_iregex: Union[Unset, str] = UNSET,
    access_constraints_isnull: Union[Unset, bool] = UNSET,
    access_constraints_istartswith: Union[Unset, str] = UNSET,
    access_constraints_lt: Union[Unset, str] = UNSET,
    access_constraints_lte: Union[Unset, str] = UNSET,
    access_constraints_range: Union[Unset, list[str]] = UNSET,
    access_constraints_regex: Union[Unset, str] = UNSET,
    access_constraints_startswith: Union[Unset, str] = UNSET,
    access_roles: Union[Unset, str] = UNSET,
    access_roles_contains: Union[Unset, str] = UNSET,
    access_roles_endswith: Union[Unset, str] = UNSET,
    access_roles_gt: Union[Unset, str] = UNSET,
    access_roles_gte: Union[Unset, str] = UNSET,
    access_roles_icontains: Union[Unset, str] = UNSET,
    access_roles_iendswith: Union[Unset, str] = UNSET,
    access_roles_iexact: Union[Unset, str] = UNSET,
    access_roles_in: Union[Unset, list[str]] = UNSET,
    access_roles_iregex: Union[Unset, str] = UNSET,
    access_roles_isnull: Union[Unset, bool] = UNSET,
    access_roles_istartswith: Union[Unset, str] = UNSET,
    access_roles_lt: Union[Unset, str] = UNSET,
    access_roles_lte: Union[Unset, str] = UNSET,
    access_roles_range: Union[Unset, list[str]] = UNSET,
    access_roles_regex: Union[Unset, str] = UNSET,
    access_roles_startswith: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    label_contains: Union[Unset, str] = UNSET,
    label_endswith: Union[Unset, str] = UNSET,
    label_gt: Union[Unset, str] = UNSET,
    label_gte: Union[Unset, str] = UNSET,
    label_icontains: Union[Unset, str] = UNSET,
    label_iendswith: Union[Unset, str] = UNSET,
    label_iexact: Union[Unset, str] = UNSET,
    label_in: Union[Unset, list[str]] = UNSET,
    label_iregex: Union[Unset, str] = UNSET,
    label_isnull: Union[Unset, bool] = UNSET,
    label_istartswith: Union[Unset, str] = UNSET,
    label_lt: Union[Unset, str] = UNSET,
    label_lte: Union[Unset, str] = UNSET,
    label_range: Union[Unset, list[str]] = UNSET,
    label_regex: Union[Unset, str] = UNSET,
    label_startswith: Union[Unset, str] = UNSET,
    licence: Union[Unset, int] = UNSET,
    licence_gt: Union[Unset, int] = UNSET,
    licence_gte: Union[Unset, int] = UNSET,
    licence_in: Union[Unset, list[int]] = UNSET,
    licence_isnull: Union[Unset, bool] = UNSET,
    licence_licence_classifications_classification: Union[Unset, str] = UNSET,
    licence_licence_classifications_classification_contains: Union[Unset, str] = UNSET,
    licence_licence_url: Union[Unset, str] = UNSET,
    licence_licence_url_contains: Union[Unset, str] = UNSET,
    licence_licence_url_in: Union[Unset, list[str]] = UNSET,
    licence_lt: Union[Unset, int] = UNSET,
    licence_lte: Union[Unset, int] = UNSET,
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
    use_limitation: Union[Unset, str] = UNSET,
    use_limitation_contains: Union[Unset, str] = UNSET,
    use_limitation_endswith: Union[Unset, str] = UNSET,
    use_limitation_gt: Union[Unset, str] = UNSET,
    use_limitation_gte: Union[Unset, str] = UNSET,
    use_limitation_icontains: Union[Unset, str] = UNSET,
    use_limitation_iendswith: Union[Unset, str] = UNSET,
    use_limitation_iexact: Union[Unset, str] = UNSET,
    use_limitation_in: Union[Unset, list[str]] = UNSET,
    use_limitation_iregex: Union[Unset, str] = UNSET,
    use_limitation_isnull: Union[Unset, bool] = UNSET,
    use_limitation_istartswith: Union[Unset, str] = UNSET,
    use_limitation_lt: Union[Unset, str] = UNSET,
    use_limitation_lte: Union[Unset, str] = UNSET,
    use_limitation_range: Union[Unset, list[str]] = UNSET,
    use_limitation_regex: Union[Unset, str] = UNSET,
    use_limitation_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedConstraintsWriteList]:
    """Get a list of Constraints objects.

    Args:
        access_category (Union[Unset, ConstraintsListAccessCategory]):
        access_category_contains (Union[Unset, str]):
        access_category_endswith (Union[Unset, str]):
        access_category_gt (Union[Unset, str]):
        access_category_gte (Union[Unset, str]):
        access_category_icontains (Union[Unset, str]):
        access_category_iendswith (Union[Unset, str]):
        access_category_iexact (Union[Unset, str]):
        access_category_in (Union[Unset, list[str]]):
        access_category_iregex (Union[Unset, str]):
        access_category_isnull (Union[Unset, bool]):
        access_category_istartswith (Union[Unset, str]):
        access_category_lt (Union[Unset, str]):
        access_category_lte (Union[Unset, str]):
        access_category_range (Union[Unset, list[str]]):
        access_category_regex (Union[Unset, str]):
        access_category_startswith (Union[Unset, str]):
        access_constraints (Union[Unset, str]):
        access_constraints_contains (Union[Unset, str]):
        access_constraints_endswith (Union[Unset, str]):
        access_constraints_gt (Union[Unset, str]):
        access_constraints_gte (Union[Unset, str]):
        access_constraints_icontains (Union[Unset, str]):
        access_constraints_iendswith (Union[Unset, str]):
        access_constraints_iexact (Union[Unset, str]):
        access_constraints_in (Union[Unset, list[str]]):
        access_constraints_iregex (Union[Unset, str]):
        access_constraints_isnull (Union[Unset, bool]):
        access_constraints_istartswith (Union[Unset, str]):
        access_constraints_lt (Union[Unset, str]):
        access_constraints_lte (Union[Unset, str]):
        access_constraints_range (Union[Unset, list[str]]):
        access_constraints_regex (Union[Unset, str]):
        access_constraints_startswith (Union[Unset, str]):
        access_roles (Union[Unset, str]):
        access_roles_contains (Union[Unset, str]):
        access_roles_endswith (Union[Unset, str]):
        access_roles_gt (Union[Unset, str]):
        access_roles_gte (Union[Unset, str]):
        access_roles_icontains (Union[Unset, str]):
        access_roles_iendswith (Union[Unset, str]):
        access_roles_iexact (Union[Unset, str]):
        access_roles_in (Union[Unset, list[str]]):
        access_roles_iregex (Union[Unset, str]):
        access_roles_isnull (Union[Unset, bool]):
        access_roles_istartswith (Union[Unset, str]):
        access_roles_lt (Union[Unset, str]):
        access_roles_lte (Union[Unset, str]):
        access_roles_range (Union[Unset, list[str]]):
        access_roles_regex (Union[Unset, str]):
        access_roles_startswith (Union[Unset, str]):
        label (Union[Unset, str]):
        label_contains (Union[Unset, str]):
        label_endswith (Union[Unset, str]):
        label_gt (Union[Unset, str]):
        label_gte (Union[Unset, str]):
        label_icontains (Union[Unset, str]):
        label_iendswith (Union[Unset, str]):
        label_iexact (Union[Unset, str]):
        label_in (Union[Unset, list[str]]):
        label_iregex (Union[Unset, str]):
        label_isnull (Union[Unset, bool]):
        label_istartswith (Union[Unset, str]):
        label_lt (Union[Unset, str]):
        label_lte (Union[Unset, str]):
        label_range (Union[Unset, list[str]]):
        label_regex (Union[Unset, str]):
        label_startswith (Union[Unset, str]):
        licence (Union[Unset, int]):
        licence_gt (Union[Unset, int]):
        licence_gte (Union[Unset, int]):
        licence_in (Union[Unset, list[int]]):
        licence_isnull (Union[Unset, bool]):
        licence_licence_classifications_classification (Union[Unset, str]):
        licence_licence_classifications_classification_contains (Union[Unset, str]):
        licence_licence_url (Union[Unset, str]):
        licence_licence_url_contains (Union[Unset, str]):
        licence_licence_url_in (Union[Unset, list[str]]):
        licence_lt (Union[Unset, int]):
        licence_lte (Union[Unset, int]):
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
        use_limitation (Union[Unset, str]):
        use_limitation_contains (Union[Unset, str]):
        use_limitation_endswith (Union[Unset, str]):
        use_limitation_gt (Union[Unset, str]):
        use_limitation_gte (Union[Unset, str]):
        use_limitation_icontains (Union[Unset, str]):
        use_limitation_iendswith (Union[Unset, str]):
        use_limitation_iexact (Union[Unset, str]):
        use_limitation_in (Union[Unset, list[str]]):
        use_limitation_iregex (Union[Unset, str]):
        use_limitation_isnull (Union[Unset, bool]):
        use_limitation_istartswith (Union[Unset, str]):
        use_limitation_lt (Union[Unset, str]):
        use_limitation_lte (Union[Unset, str]):
        use_limitation_range (Union[Unset, list[str]]):
        use_limitation_regex (Union[Unset, str]):
        use_limitation_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedConstraintsWriteList]
    """

    kwargs = _get_kwargs(
        access_category=access_category,
        access_category_contains=access_category_contains,
        access_category_endswith=access_category_endswith,
        access_category_gt=access_category_gt,
        access_category_gte=access_category_gte,
        access_category_icontains=access_category_icontains,
        access_category_iendswith=access_category_iendswith,
        access_category_iexact=access_category_iexact,
        access_category_in=access_category_in,
        access_category_iregex=access_category_iregex,
        access_category_isnull=access_category_isnull,
        access_category_istartswith=access_category_istartswith,
        access_category_lt=access_category_lt,
        access_category_lte=access_category_lte,
        access_category_range=access_category_range,
        access_category_regex=access_category_regex,
        access_category_startswith=access_category_startswith,
        access_constraints=access_constraints,
        access_constraints_contains=access_constraints_contains,
        access_constraints_endswith=access_constraints_endswith,
        access_constraints_gt=access_constraints_gt,
        access_constraints_gte=access_constraints_gte,
        access_constraints_icontains=access_constraints_icontains,
        access_constraints_iendswith=access_constraints_iendswith,
        access_constraints_iexact=access_constraints_iexact,
        access_constraints_in=access_constraints_in,
        access_constraints_iregex=access_constraints_iregex,
        access_constraints_isnull=access_constraints_isnull,
        access_constraints_istartswith=access_constraints_istartswith,
        access_constraints_lt=access_constraints_lt,
        access_constraints_lte=access_constraints_lte,
        access_constraints_range=access_constraints_range,
        access_constraints_regex=access_constraints_regex,
        access_constraints_startswith=access_constraints_startswith,
        access_roles=access_roles,
        access_roles_contains=access_roles_contains,
        access_roles_endswith=access_roles_endswith,
        access_roles_gt=access_roles_gt,
        access_roles_gte=access_roles_gte,
        access_roles_icontains=access_roles_icontains,
        access_roles_iendswith=access_roles_iendswith,
        access_roles_iexact=access_roles_iexact,
        access_roles_in=access_roles_in,
        access_roles_iregex=access_roles_iregex,
        access_roles_isnull=access_roles_isnull,
        access_roles_istartswith=access_roles_istartswith,
        access_roles_lt=access_roles_lt,
        access_roles_lte=access_roles_lte,
        access_roles_range=access_roles_range,
        access_roles_regex=access_roles_regex,
        access_roles_startswith=access_roles_startswith,
        label=label,
        label_contains=label_contains,
        label_endswith=label_endswith,
        label_gt=label_gt,
        label_gte=label_gte,
        label_icontains=label_icontains,
        label_iendswith=label_iendswith,
        label_iexact=label_iexact,
        label_in=label_in,
        label_iregex=label_iregex,
        label_isnull=label_isnull,
        label_istartswith=label_istartswith,
        label_lt=label_lt,
        label_lte=label_lte,
        label_range=label_range,
        label_regex=label_regex,
        label_startswith=label_startswith,
        licence=licence,
        licence_gt=licence_gt,
        licence_gte=licence_gte,
        licence_in=licence_in,
        licence_isnull=licence_isnull,
        licence_licence_classifications_classification=licence_licence_classifications_classification,
        licence_licence_classifications_classification_contains=licence_licence_classifications_classification_contains,
        licence_licence_url=licence_licence_url,
        licence_licence_url_contains=licence_licence_url_contains,
        licence_licence_url_in=licence_licence_url_in,
        licence_lt=licence_lt,
        licence_lte=licence_lte,
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
        use_limitation=use_limitation,
        use_limitation_contains=use_limitation_contains,
        use_limitation_endswith=use_limitation_endswith,
        use_limitation_gt=use_limitation_gt,
        use_limitation_gte=use_limitation_gte,
        use_limitation_icontains=use_limitation_icontains,
        use_limitation_iendswith=use_limitation_iendswith,
        use_limitation_iexact=use_limitation_iexact,
        use_limitation_in=use_limitation_in,
        use_limitation_iregex=use_limitation_iregex,
        use_limitation_isnull=use_limitation_isnull,
        use_limitation_istartswith=use_limitation_istartswith,
        use_limitation_lt=use_limitation_lt,
        use_limitation_lte=use_limitation_lte,
        use_limitation_range=use_limitation_range,
        use_limitation_regex=use_limitation_regex,
        use_limitation_startswith=use_limitation_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    access_category: Union[Unset, ConstraintsListAccessCategory] = UNSET,
    access_category_contains: Union[Unset, str] = UNSET,
    access_category_endswith: Union[Unset, str] = UNSET,
    access_category_gt: Union[Unset, str] = UNSET,
    access_category_gte: Union[Unset, str] = UNSET,
    access_category_icontains: Union[Unset, str] = UNSET,
    access_category_iendswith: Union[Unset, str] = UNSET,
    access_category_iexact: Union[Unset, str] = UNSET,
    access_category_in: Union[Unset, list[str]] = UNSET,
    access_category_iregex: Union[Unset, str] = UNSET,
    access_category_isnull: Union[Unset, bool] = UNSET,
    access_category_istartswith: Union[Unset, str] = UNSET,
    access_category_lt: Union[Unset, str] = UNSET,
    access_category_lte: Union[Unset, str] = UNSET,
    access_category_range: Union[Unset, list[str]] = UNSET,
    access_category_regex: Union[Unset, str] = UNSET,
    access_category_startswith: Union[Unset, str] = UNSET,
    access_constraints: Union[Unset, str] = UNSET,
    access_constraints_contains: Union[Unset, str] = UNSET,
    access_constraints_endswith: Union[Unset, str] = UNSET,
    access_constraints_gt: Union[Unset, str] = UNSET,
    access_constraints_gte: Union[Unset, str] = UNSET,
    access_constraints_icontains: Union[Unset, str] = UNSET,
    access_constraints_iendswith: Union[Unset, str] = UNSET,
    access_constraints_iexact: Union[Unset, str] = UNSET,
    access_constraints_in: Union[Unset, list[str]] = UNSET,
    access_constraints_iregex: Union[Unset, str] = UNSET,
    access_constraints_isnull: Union[Unset, bool] = UNSET,
    access_constraints_istartswith: Union[Unset, str] = UNSET,
    access_constraints_lt: Union[Unset, str] = UNSET,
    access_constraints_lte: Union[Unset, str] = UNSET,
    access_constraints_range: Union[Unset, list[str]] = UNSET,
    access_constraints_regex: Union[Unset, str] = UNSET,
    access_constraints_startswith: Union[Unset, str] = UNSET,
    access_roles: Union[Unset, str] = UNSET,
    access_roles_contains: Union[Unset, str] = UNSET,
    access_roles_endswith: Union[Unset, str] = UNSET,
    access_roles_gt: Union[Unset, str] = UNSET,
    access_roles_gte: Union[Unset, str] = UNSET,
    access_roles_icontains: Union[Unset, str] = UNSET,
    access_roles_iendswith: Union[Unset, str] = UNSET,
    access_roles_iexact: Union[Unset, str] = UNSET,
    access_roles_in: Union[Unset, list[str]] = UNSET,
    access_roles_iregex: Union[Unset, str] = UNSET,
    access_roles_isnull: Union[Unset, bool] = UNSET,
    access_roles_istartswith: Union[Unset, str] = UNSET,
    access_roles_lt: Union[Unset, str] = UNSET,
    access_roles_lte: Union[Unset, str] = UNSET,
    access_roles_range: Union[Unset, list[str]] = UNSET,
    access_roles_regex: Union[Unset, str] = UNSET,
    access_roles_startswith: Union[Unset, str] = UNSET,
    label: Union[Unset, str] = UNSET,
    label_contains: Union[Unset, str] = UNSET,
    label_endswith: Union[Unset, str] = UNSET,
    label_gt: Union[Unset, str] = UNSET,
    label_gte: Union[Unset, str] = UNSET,
    label_icontains: Union[Unset, str] = UNSET,
    label_iendswith: Union[Unset, str] = UNSET,
    label_iexact: Union[Unset, str] = UNSET,
    label_in: Union[Unset, list[str]] = UNSET,
    label_iregex: Union[Unset, str] = UNSET,
    label_isnull: Union[Unset, bool] = UNSET,
    label_istartswith: Union[Unset, str] = UNSET,
    label_lt: Union[Unset, str] = UNSET,
    label_lte: Union[Unset, str] = UNSET,
    label_range: Union[Unset, list[str]] = UNSET,
    label_regex: Union[Unset, str] = UNSET,
    label_startswith: Union[Unset, str] = UNSET,
    licence: Union[Unset, int] = UNSET,
    licence_gt: Union[Unset, int] = UNSET,
    licence_gte: Union[Unset, int] = UNSET,
    licence_in: Union[Unset, list[int]] = UNSET,
    licence_isnull: Union[Unset, bool] = UNSET,
    licence_licence_classifications_classification: Union[Unset, str] = UNSET,
    licence_licence_classifications_classification_contains: Union[Unset, str] = UNSET,
    licence_licence_url: Union[Unset, str] = UNSET,
    licence_licence_url_contains: Union[Unset, str] = UNSET,
    licence_licence_url_in: Union[Unset, list[str]] = UNSET,
    licence_lt: Union[Unset, int] = UNSET,
    licence_lte: Union[Unset, int] = UNSET,
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
    use_limitation: Union[Unset, str] = UNSET,
    use_limitation_contains: Union[Unset, str] = UNSET,
    use_limitation_endswith: Union[Unset, str] = UNSET,
    use_limitation_gt: Union[Unset, str] = UNSET,
    use_limitation_gte: Union[Unset, str] = UNSET,
    use_limitation_icontains: Union[Unset, str] = UNSET,
    use_limitation_iendswith: Union[Unset, str] = UNSET,
    use_limitation_iexact: Union[Unset, str] = UNSET,
    use_limitation_in: Union[Unset, list[str]] = UNSET,
    use_limitation_iregex: Union[Unset, str] = UNSET,
    use_limitation_isnull: Union[Unset, bool] = UNSET,
    use_limitation_istartswith: Union[Unset, str] = UNSET,
    use_limitation_lt: Union[Unset, str] = UNSET,
    use_limitation_lte: Union[Unset, str] = UNSET,
    use_limitation_range: Union[Unset, list[str]] = UNSET,
    use_limitation_regex: Union[Unset, str] = UNSET,
    use_limitation_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedConstraintsWriteList]:
    """Get a list of Constraints objects.

    Args:
        access_category (Union[Unset, ConstraintsListAccessCategory]):
        access_category_contains (Union[Unset, str]):
        access_category_endswith (Union[Unset, str]):
        access_category_gt (Union[Unset, str]):
        access_category_gte (Union[Unset, str]):
        access_category_icontains (Union[Unset, str]):
        access_category_iendswith (Union[Unset, str]):
        access_category_iexact (Union[Unset, str]):
        access_category_in (Union[Unset, list[str]]):
        access_category_iregex (Union[Unset, str]):
        access_category_isnull (Union[Unset, bool]):
        access_category_istartswith (Union[Unset, str]):
        access_category_lt (Union[Unset, str]):
        access_category_lte (Union[Unset, str]):
        access_category_range (Union[Unset, list[str]]):
        access_category_regex (Union[Unset, str]):
        access_category_startswith (Union[Unset, str]):
        access_constraints (Union[Unset, str]):
        access_constraints_contains (Union[Unset, str]):
        access_constraints_endswith (Union[Unset, str]):
        access_constraints_gt (Union[Unset, str]):
        access_constraints_gte (Union[Unset, str]):
        access_constraints_icontains (Union[Unset, str]):
        access_constraints_iendswith (Union[Unset, str]):
        access_constraints_iexact (Union[Unset, str]):
        access_constraints_in (Union[Unset, list[str]]):
        access_constraints_iregex (Union[Unset, str]):
        access_constraints_isnull (Union[Unset, bool]):
        access_constraints_istartswith (Union[Unset, str]):
        access_constraints_lt (Union[Unset, str]):
        access_constraints_lte (Union[Unset, str]):
        access_constraints_range (Union[Unset, list[str]]):
        access_constraints_regex (Union[Unset, str]):
        access_constraints_startswith (Union[Unset, str]):
        access_roles (Union[Unset, str]):
        access_roles_contains (Union[Unset, str]):
        access_roles_endswith (Union[Unset, str]):
        access_roles_gt (Union[Unset, str]):
        access_roles_gte (Union[Unset, str]):
        access_roles_icontains (Union[Unset, str]):
        access_roles_iendswith (Union[Unset, str]):
        access_roles_iexact (Union[Unset, str]):
        access_roles_in (Union[Unset, list[str]]):
        access_roles_iregex (Union[Unset, str]):
        access_roles_isnull (Union[Unset, bool]):
        access_roles_istartswith (Union[Unset, str]):
        access_roles_lt (Union[Unset, str]):
        access_roles_lte (Union[Unset, str]):
        access_roles_range (Union[Unset, list[str]]):
        access_roles_regex (Union[Unset, str]):
        access_roles_startswith (Union[Unset, str]):
        label (Union[Unset, str]):
        label_contains (Union[Unset, str]):
        label_endswith (Union[Unset, str]):
        label_gt (Union[Unset, str]):
        label_gte (Union[Unset, str]):
        label_icontains (Union[Unset, str]):
        label_iendswith (Union[Unset, str]):
        label_iexact (Union[Unset, str]):
        label_in (Union[Unset, list[str]]):
        label_iregex (Union[Unset, str]):
        label_isnull (Union[Unset, bool]):
        label_istartswith (Union[Unset, str]):
        label_lt (Union[Unset, str]):
        label_lte (Union[Unset, str]):
        label_range (Union[Unset, list[str]]):
        label_regex (Union[Unset, str]):
        label_startswith (Union[Unset, str]):
        licence (Union[Unset, int]):
        licence_gt (Union[Unset, int]):
        licence_gte (Union[Unset, int]):
        licence_in (Union[Unset, list[int]]):
        licence_isnull (Union[Unset, bool]):
        licence_licence_classifications_classification (Union[Unset, str]):
        licence_licence_classifications_classification_contains (Union[Unset, str]):
        licence_licence_url (Union[Unset, str]):
        licence_licence_url_contains (Union[Unset, str]):
        licence_licence_url_in (Union[Unset, list[str]]):
        licence_lt (Union[Unset, int]):
        licence_lte (Union[Unset, int]):
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
        use_limitation (Union[Unset, str]):
        use_limitation_contains (Union[Unset, str]):
        use_limitation_endswith (Union[Unset, str]):
        use_limitation_gt (Union[Unset, str]):
        use_limitation_gte (Union[Unset, str]):
        use_limitation_icontains (Union[Unset, str]):
        use_limitation_iendswith (Union[Unset, str]):
        use_limitation_iexact (Union[Unset, str]):
        use_limitation_in (Union[Unset, list[str]]):
        use_limitation_iregex (Union[Unset, str]):
        use_limitation_isnull (Union[Unset, bool]):
        use_limitation_istartswith (Union[Unset, str]):
        use_limitation_lt (Union[Unset, str]):
        use_limitation_lte (Union[Unset, str]):
        use_limitation_range (Union[Unset, list[str]]):
        use_limitation_regex (Union[Unset, str]):
        use_limitation_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedConstraintsWriteList
    """

    return (
        await asyncio_detailed(
            client=client,
            access_category=access_category,
            access_category_contains=access_category_contains,
            access_category_endswith=access_category_endswith,
            access_category_gt=access_category_gt,
            access_category_gte=access_category_gte,
            access_category_icontains=access_category_icontains,
            access_category_iendswith=access_category_iendswith,
            access_category_iexact=access_category_iexact,
            access_category_in=access_category_in,
            access_category_iregex=access_category_iregex,
            access_category_isnull=access_category_isnull,
            access_category_istartswith=access_category_istartswith,
            access_category_lt=access_category_lt,
            access_category_lte=access_category_lte,
            access_category_range=access_category_range,
            access_category_regex=access_category_regex,
            access_category_startswith=access_category_startswith,
            access_constraints=access_constraints,
            access_constraints_contains=access_constraints_contains,
            access_constraints_endswith=access_constraints_endswith,
            access_constraints_gt=access_constraints_gt,
            access_constraints_gte=access_constraints_gte,
            access_constraints_icontains=access_constraints_icontains,
            access_constraints_iendswith=access_constraints_iendswith,
            access_constraints_iexact=access_constraints_iexact,
            access_constraints_in=access_constraints_in,
            access_constraints_iregex=access_constraints_iregex,
            access_constraints_isnull=access_constraints_isnull,
            access_constraints_istartswith=access_constraints_istartswith,
            access_constraints_lt=access_constraints_lt,
            access_constraints_lte=access_constraints_lte,
            access_constraints_range=access_constraints_range,
            access_constraints_regex=access_constraints_regex,
            access_constraints_startswith=access_constraints_startswith,
            access_roles=access_roles,
            access_roles_contains=access_roles_contains,
            access_roles_endswith=access_roles_endswith,
            access_roles_gt=access_roles_gt,
            access_roles_gte=access_roles_gte,
            access_roles_icontains=access_roles_icontains,
            access_roles_iendswith=access_roles_iendswith,
            access_roles_iexact=access_roles_iexact,
            access_roles_in=access_roles_in,
            access_roles_iregex=access_roles_iregex,
            access_roles_isnull=access_roles_isnull,
            access_roles_istartswith=access_roles_istartswith,
            access_roles_lt=access_roles_lt,
            access_roles_lte=access_roles_lte,
            access_roles_range=access_roles_range,
            access_roles_regex=access_roles_regex,
            access_roles_startswith=access_roles_startswith,
            label=label,
            label_contains=label_contains,
            label_endswith=label_endswith,
            label_gt=label_gt,
            label_gte=label_gte,
            label_icontains=label_icontains,
            label_iendswith=label_iendswith,
            label_iexact=label_iexact,
            label_in=label_in,
            label_iregex=label_iregex,
            label_isnull=label_isnull,
            label_istartswith=label_istartswith,
            label_lt=label_lt,
            label_lte=label_lte,
            label_range=label_range,
            label_regex=label_regex,
            label_startswith=label_startswith,
            licence=licence,
            licence_gt=licence_gt,
            licence_gte=licence_gte,
            licence_in=licence_in,
            licence_isnull=licence_isnull,
            licence_licence_classifications_classification=licence_licence_classifications_classification,
            licence_licence_classifications_classification_contains=licence_licence_classifications_classification_contains,
            licence_licence_url=licence_licence_url,
            licence_licence_url_contains=licence_licence_url_contains,
            licence_licence_url_in=licence_licence_url_in,
            licence_lt=licence_lt,
            licence_lte=licence_lte,
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
            use_limitation=use_limitation,
            use_limitation_contains=use_limitation_contains,
            use_limitation_endswith=use_limitation_endswith,
            use_limitation_gt=use_limitation_gt,
            use_limitation_gte=use_limitation_gte,
            use_limitation_icontains=use_limitation_icontains,
            use_limitation_iendswith=use_limitation_iendswith,
            use_limitation_iexact=use_limitation_iexact,
            use_limitation_in=use_limitation_in,
            use_limitation_iregex=use_limitation_iregex,
            use_limitation_isnull=use_limitation_isnull,
            use_limitation_istartswith=use_limitation_istartswith,
            use_limitation_lt=use_limitation_lt,
            use_limitation_lte=use_limitation_lte,
            use_limitation_range=use_limitation_range,
            use_limitation_regex=use_limitation_regex,
            use_limitation_startswith=use_limitation_startswith,
        )
    ).parsed
