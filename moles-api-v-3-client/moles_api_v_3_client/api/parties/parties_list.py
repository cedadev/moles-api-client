from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_party_read_list import PaginatedPartyReadList
from ...models.parties_list_type import PartiesListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    administrative_area: Union[Unset, str] = UNSET,
    administrative_area_contains: Union[Unset, str] = UNSET,
    administrative_area_endswith: Union[Unset, str] = UNSET,
    administrative_area_gt: Union[Unset, str] = UNSET,
    administrative_area_gte: Union[Unset, str] = UNSET,
    administrative_area_icontains: Union[Unset, str] = UNSET,
    administrative_area_iendswith: Union[Unset, str] = UNSET,
    administrative_area_iexact: Union[Unset, str] = UNSET,
    administrative_area_in: Union[Unset, list[str]] = UNSET,
    administrative_area_iregex: Union[Unset, str] = UNSET,
    administrative_area_isnull: Union[Unset, bool] = UNSET,
    administrative_area_istartswith: Union[Unset, str] = UNSET,
    administrative_area_lt: Union[Unset, str] = UNSET,
    administrative_area_lte: Union[Unset, str] = UNSET,
    administrative_area_range: Union[Unset, list[str]] = UNSET,
    administrative_area_regex: Union[Unset, str] = UNSET,
    administrative_area_startswith: Union[Unset, str] = UNSET,
    city: Union[Unset, str] = UNSET,
    city_contains: Union[Unset, str] = UNSET,
    city_endswith: Union[Unset, str] = UNSET,
    city_gt: Union[Unset, str] = UNSET,
    city_gte: Union[Unset, str] = UNSET,
    city_icontains: Union[Unset, str] = UNSET,
    city_iendswith: Union[Unset, str] = UNSET,
    city_iexact: Union[Unset, str] = UNSET,
    city_in: Union[Unset, list[str]] = UNSET,
    city_iregex: Union[Unset, str] = UNSET,
    city_isnull: Union[Unset, bool] = UNSET,
    city_istartswith: Union[Unset, str] = UNSET,
    city_lt: Union[Unset, str] = UNSET,
    city_lte: Union[Unset, str] = UNSET,
    city_range: Union[Unset, list[str]] = UNSET,
    city_regex: Union[Unset, str] = UNSET,
    city_startswith: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    country_contains: Union[Unset, str] = UNSET,
    country_endswith: Union[Unset, str] = UNSET,
    country_gt: Union[Unset, str] = UNSET,
    country_gte: Union[Unset, str] = UNSET,
    country_icontains: Union[Unset, str] = UNSET,
    country_iendswith: Union[Unset, str] = UNSET,
    country_iexact: Union[Unset, str] = UNSET,
    country_in: Union[Unset, list[str]] = UNSET,
    country_iregex: Union[Unset, str] = UNSET,
    country_isnull: Union[Unset, bool] = UNSET,
    country_istartswith: Union[Unset, str] = UNSET,
    country_lt: Union[Unset, str] = UNSET,
    country_lte: Union[Unset, str] = UNSET,
    country_range: Union[Unset, list[str]] = UNSET,
    country_regex: Union[Unset, str] = UNSET,
    country_startswith: Union[Unset, str] = UNSET,
    delivery_point: Union[Unset, str] = UNSET,
    delivery_point_contains: Union[Unset, str] = UNSET,
    delivery_point_endswith: Union[Unset, str] = UNSET,
    delivery_point_gt: Union[Unset, str] = UNSET,
    delivery_point_gte: Union[Unset, str] = UNSET,
    delivery_point_icontains: Union[Unset, str] = UNSET,
    delivery_point_iendswith: Union[Unset, str] = UNSET,
    delivery_point_iexact: Union[Unset, str] = UNSET,
    delivery_point_in: Union[Unset, list[str]] = UNSET,
    delivery_point_iregex: Union[Unset, str] = UNSET,
    delivery_point_isnull: Union[Unset, bool] = UNSET,
    delivery_point_istartswith: Union[Unset, str] = UNSET,
    delivery_point_lt: Union[Unset, str] = UNSET,
    delivery_point_lte: Union[Unset, str] = UNSET,
    delivery_point_range: Union[Unset, list[str]] = UNSET,
    delivery_point_regex: Union[Unset, str] = UNSET,
    delivery_point_startswith: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    description_contains: Union[Unset, str] = UNSET,
    description_endswith: Union[Unset, str] = UNSET,
    description_gt: Union[Unset, str] = UNSET,
    description_gte: Union[Unset, str] = UNSET,
    description_icontains: Union[Unset, str] = UNSET,
    description_iendswith: Union[Unset, str] = UNSET,
    description_iexact: Union[Unset, str] = UNSET,
    description_in: Union[Unset, list[str]] = UNSET,
    description_iregex: Union[Unset, str] = UNSET,
    description_isnull: Union[Unset, bool] = UNSET,
    description_istartswith: Union[Unset, str] = UNSET,
    description_lt: Union[Unset, str] = UNSET,
    description_lte: Union[Unset, str] = UNSET,
    description_range: Union[Unset, list[str]] = UNSET,
    description_regex: Union[Unset, str] = UNSET,
    description_startswith: Union[Unset, str] = UNSET,
    electronic_email_address: Union[Unset, str] = UNSET,
    electronic_email_address_contains: Union[Unset, str] = UNSET,
    electronic_email_address_endswith: Union[Unset, str] = UNSET,
    electronic_email_address_gt: Union[Unset, str] = UNSET,
    electronic_email_address_gte: Union[Unset, str] = UNSET,
    electronic_email_address_icontains: Union[Unset, str] = UNSET,
    electronic_email_address_iendswith: Union[Unset, str] = UNSET,
    electronic_email_address_iexact: Union[Unset, str] = UNSET,
    electronic_email_address_in: Union[Unset, list[str]] = UNSET,
    electronic_email_address_iregex: Union[Unset, str] = UNSET,
    electronic_email_address_isnull: Union[Unset, bool] = UNSET,
    electronic_email_address_istartswith: Union[Unset, str] = UNSET,
    electronic_email_address_lt: Union[Unset, str] = UNSET,
    electronic_email_address_lte: Union[Unset, str] = UNSET,
    electronic_email_address_range: Union[Unset, list[str]] = UNSET,
    electronic_email_address_regex: Union[Unset, str] = UNSET,
    electronic_email_address_startswith: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    first_name_contains: Union[Unset, str] = UNSET,
    first_name_endswith: Union[Unset, str] = UNSET,
    first_name_gt: Union[Unset, str] = UNSET,
    first_name_gte: Union[Unset, str] = UNSET,
    first_name_icontains: Union[Unset, str] = UNSET,
    first_name_iendswith: Union[Unset, str] = UNSET,
    first_name_iexact: Union[Unset, str] = UNSET,
    first_name_in: Union[Unset, list[str]] = UNSET,
    first_name_iregex: Union[Unset, str] = UNSET,
    first_name_isnull: Union[Unset, bool] = UNSET,
    first_name_istartswith: Union[Unset, str] = UNSET,
    first_name_lt: Union[Unset, str] = UNSET,
    first_name_lte: Union[Unset, str] = UNSET,
    first_name_range: Union[Unset, list[str]] = UNSET,
    first_name_regex: Union[Unset, str] = UNSET,
    first_name_startswith: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    last_name_contains: Union[Unset, str] = UNSET,
    last_name_endswith: Union[Unset, str] = UNSET,
    last_name_gt: Union[Unset, str] = UNSET,
    last_name_gte: Union[Unset, str] = UNSET,
    last_name_icontains: Union[Unset, str] = UNSET,
    last_name_iendswith: Union[Unset, str] = UNSET,
    last_name_iexact: Union[Unset, str] = UNSET,
    last_name_in: Union[Unset, list[str]] = UNSET,
    last_name_iregex: Union[Unset, str] = UNSET,
    last_name_isnull: Union[Unset, bool] = UNSET,
    last_name_istartswith: Union[Unset, str] = UNSET,
    last_name_lt: Union[Unset, str] = UNSET,
    last_name_lte: Union[Unset, str] = UNSET,
    last_name_range: Union[Unset, list[str]] = UNSET,
    last_name_regex: Union[Unset, str] = UNSET,
    last_name_startswith: Union[Unset, str] = UNSET,
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
    online_resource: Union[Unset, str] = UNSET,
    online_resource_contains: Union[Unset, str] = UNSET,
    online_resource_endswith: Union[Unset, str] = UNSET,
    online_resource_gt: Union[Unset, str] = UNSET,
    online_resource_gte: Union[Unset, str] = UNSET,
    online_resource_icontains: Union[Unset, str] = UNSET,
    online_resource_iendswith: Union[Unset, str] = UNSET,
    online_resource_iexact: Union[Unset, str] = UNSET,
    online_resource_in: Union[Unset, list[str]] = UNSET,
    online_resource_iregex: Union[Unset, str] = UNSET,
    online_resource_isnull: Union[Unset, bool] = UNSET,
    online_resource_istartswith: Union[Unset, str] = UNSET,
    online_resource_lt: Union[Unset, str] = UNSET,
    online_resource_lte: Union[Unset, str] = UNSET,
    online_resource_range: Union[Unset, list[str]] = UNSET,
    online_resource_regex: Union[Unset, str] = UNSET,
    online_resource_startswith: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    party_type: Union[Unset, PartiesListType] = UNSET,
    party_type_contains: Union[Unset, str] = UNSET,
    party_type_endswith: Union[Unset, str] = UNSET,
    party_type_gt: Union[Unset, str] = UNSET,
    party_type_gte: Union[Unset, str] = UNSET,
    party_type_icontains: Union[Unset, str] = UNSET,
    party_type_iendswith: Union[Unset, str] = UNSET,
    party_type_iexact: Union[Unset, str] = UNSET,
    party_type_in: Union[Unset, list[str]] = UNSET,
    party_type_iregex: Union[Unset, str] = UNSET,
    party_type_isnull: Union[Unset, bool] = UNSET,
    party_type_istartswith: Union[Unset, str] = UNSET,
    party_type_lt: Union[Unset, str] = UNSET,
    party_type_lte: Union[Unset, str] = UNSET,
    party_type_range: Union[Unset, list[str]] = UNSET,
    party_type_regex: Union[Unset, str] = UNSET,
    party_type_startswith: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    phone_contains: Union[Unset, str] = UNSET,
    phone_endswith: Union[Unset, str] = UNSET,
    phone_gt: Union[Unset, str] = UNSET,
    phone_gte: Union[Unset, str] = UNSET,
    phone_icontains: Union[Unset, str] = UNSET,
    phone_iendswith: Union[Unset, str] = UNSET,
    phone_iexact: Union[Unset, str] = UNSET,
    phone_in: Union[Unset, list[str]] = UNSET,
    phone_iregex: Union[Unset, str] = UNSET,
    phone_isnull: Union[Unset, bool] = UNSET,
    phone_istartswith: Union[Unset, str] = UNSET,
    phone_lt: Union[Unset, str] = UNSET,
    phone_lte: Union[Unset, str] = UNSET,
    phone_range: Union[Unset, list[str]] = UNSET,
    phone_regex: Union[Unset, str] = UNSET,
    phone_startswith: Union[Unset, str] = UNSET,
    postal_code: Union[Unset, str] = UNSET,
    postal_code_contains: Union[Unset, str] = UNSET,
    postal_code_endswith: Union[Unset, str] = UNSET,
    postal_code_gt: Union[Unset, str] = UNSET,
    postal_code_gte: Union[Unset, str] = UNSET,
    postal_code_icontains: Union[Unset, str] = UNSET,
    postal_code_iendswith: Union[Unset, str] = UNSET,
    postal_code_iexact: Union[Unset, str] = UNSET,
    postal_code_in: Union[Unset, list[str]] = UNSET,
    postal_code_iregex: Union[Unset, str] = UNSET,
    postal_code_isnull: Union[Unset, bool] = UNSET,
    postal_code_istartswith: Union[Unset, str] = UNSET,
    postal_code_lt: Union[Unset, str] = UNSET,
    postal_code_lte: Union[Unset, str] = UNSET,
    postal_code_range: Union[Unset, list[str]] = UNSET,
    postal_code_regex: Union[Unset, str] = UNSET,
    postal_code_startswith: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["administrativeArea"] = administrative_area

    params["administrativeArea__contains"] = administrative_area_contains

    params["administrativeArea__endswith"] = administrative_area_endswith

    params["administrativeArea__gt"] = administrative_area_gt

    params["administrativeArea__gte"] = administrative_area_gte

    params["administrativeArea__icontains"] = administrative_area_icontains

    params["administrativeArea__iendswith"] = administrative_area_iendswith

    params["administrativeArea__iexact"] = administrative_area_iexact

    json_administrative_area_in: Union[Unset, list[str]] = UNSET
    if not isinstance(administrative_area_in, Unset):
        json_administrative_area_in = administrative_area_in

    params["administrativeArea__in"] = json_administrative_area_in

    params["administrativeArea__iregex"] = administrative_area_iregex

    params["administrativeArea__isnull"] = administrative_area_isnull

    params["administrativeArea__istartswith"] = administrative_area_istartswith

    params["administrativeArea__lt"] = administrative_area_lt

    params["administrativeArea__lte"] = administrative_area_lte

    json_administrative_area_range: Union[Unset, list[str]] = UNSET
    if not isinstance(administrative_area_range, Unset):
        json_administrative_area_range = administrative_area_range

    params["administrativeArea__range"] = json_administrative_area_range

    params["administrativeArea__regex"] = administrative_area_regex

    params["administrativeArea__startswith"] = administrative_area_startswith

    params["city"] = city

    params["city__contains"] = city_contains

    params["city__endswith"] = city_endswith

    params["city__gt"] = city_gt

    params["city__gte"] = city_gte

    params["city__icontains"] = city_icontains

    params["city__iendswith"] = city_iendswith

    params["city__iexact"] = city_iexact

    json_city_in: Union[Unset, list[str]] = UNSET
    if not isinstance(city_in, Unset):
        json_city_in = city_in

    params["city__in"] = json_city_in

    params["city__iregex"] = city_iregex

    params["city__isnull"] = city_isnull

    params["city__istartswith"] = city_istartswith

    params["city__lt"] = city_lt

    params["city__lte"] = city_lte

    json_city_range: Union[Unset, list[str]] = UNSET
    if not isinstance(city_range, Unset):
        json_city_range = city_range

    params["city__range"] = json_city_range

    params["city__regex"] = city_regex

    params["city__startswith"] = city_startswith

    params["country"] = country

    params["country__contains"] = country_contains

    params["country__endswith"] = country_endswith

    params["country__gt"] = country_gt

    params["country__gte"] = country_gte

    params["country__icontains"] = country_icontains

    params["country__iendswith"] = country_iendswith

    params["country__iexact"] = country_iexact

    json_country_in: Union[Unset, list[str]] = UNSET
    if not isinstance(country_in, Unset):
        json_country_in = country_in

    params["country__in"] = json_country_in

    params["country__iregex"] = country_iregex

    params["country__isnull"] = country_isnull

    params["country__istartswith"] = country_istartswith

    params["country__lt"] = country_lt

    params["country__lte"] = country_lte

    json_country_range: Union[Unset, list[str]] = UNSET
    if not isinstance(country_range, Unset):
        json_country_range = country_range

    params["country__range"] = json_country_range

    params["country__regex"] = country_regex

    params["country__startswith"] = country_startswith

    params["deliveryPoint"] = delivery_point

    params["deliveryPoint__contains"] = delivery_point_contains

    params["deliveryPoint__endswith"] = delivery_point_endswith

    params["deliveryPoint__gt"] = delivery_point_gt

    params["deliveryPoint__gte"] = delivery_point_gte

    params["deliveryPoint__icontains"] = delivery_point_icontains

    params["deliveryPoint__iendswith"] = delivery_point_iendswith

    params["deliveryPoint__iexact"] = delivery_point_iexact

    json_delivery_point_in: Union[Unset, list[str]] = UNSET
    if not isinstance(delivery_point_in, Unset):
        json_delivery_point_in = delivery_point_in

    params["deliveryPoint__in"] = json_delivery_point_in

    params["deliveryPoint__iregex"] = delivery_point_iregex

    params["deliveryPoint__isnull"] = delivery_point_isnull

    params["deliveryPoint__istartswith"] = delivery_point_istartswith

    params["deliveryPoint__lt"] = delivery_point_lt

    params["deliveryPoint__lte"] = delivery_point_lte

    json_delivery_point_range: Union[Unset, list[str]] = UNSET
    if not isinstance(delivery_point_range, Unset):
        json_delivery_point_range = delivery_point_range

    params["deliveryPoint__range"] = json_delivery_point_range

    params["deliveryPoint__regex"] = delivery_point_regex

    params["deliveryPoint__startswith"] = delivery_point_startswith

    params["description"] = description

    params["description__contains"] = description_contains

    params["description__endswith"] = description_endswith

    params["description__gt"] = description_gt

    params["description__gte"] = description_gte

    params["description__icontains"] = description_icontains

    params["description__iendswith"] = description_iendswith

    params["description__iexact"] = description_iexact

    json_description_in: Union[Unset, list[str]] = UNSET
    if not isinstance(description_in, Unset):
        json_description_in = description_in

    params["description__in"] = json_description_in

    params["description__iregex"] = description_iregex

    params["description__isnull"] = description_isnull

    params["description__istartswith"] = description_istartswith

    params["description__lt"] = description_lt

    params["description__lte"] = description_lte

    json_description_range: Union[Unset, list[str]] = UNSET
    if not isinstance(description_range, Unset):
        json_description_range = description_range

    params["description__range"] = json_description_range

    params["description__regex"] = description_regex

    params["description__startswith"] = description_startswith

    params["electronicEmailAddress"] = electronic_email_address

    params["electronicEmailAddress__contains"] = electronic_email_address_contains

    params["electronicEmailAddress__endswith"] = electronic_email_address_endswith

    params["electronicEmailAddress__gt"] = electronic_email_address_gt

    params["electronicEmailAddress__gte"] = electronic_email_address_gte

    params["electronicEmailAddress__icontains"] = electronic_email_address_icontains

    params["electronicEmailAddress__iendswith"] = electronic_email_address_iendswith

    params["electronicEmailAddress__iexact"] = electronic_email_address_iexact

    json_electronic_email_address_in: Union[Unset, list[str]] = UNSET
    if not isinstance(electronic_email_address_in, Unset):
        json_electronic_email_address_in = electronic_email_address_in

    params["electronicEmailAddress__in"] = json_electronic_email_address_in

    params["electronicEmailAddress__iregex"] = electronic_email_address_iregex

    params["electronicEmailAddress__isnull"] = electronic_email_address_isnull

    params["electronicEmailAddress__istartswith"] = electronic_email_address_istartswith

    params["electronicEmailAddress__lt"] = electronic_email_address_lt

    params["electronicEmailAddress__lte"] = electronic_email_address_lte

    json_electronic_email_address_range: Union[Unset, list[str]] = UNSET
    if not isinstance(electronic_email_address_range, Unset):
        json_electronic_email_address_range = electronic_email_address_range

    params["electronicEmailAddress__range"] = json_electronic_email_address_range

    params["electronicEmailAddress__regex"] = electronic_email_address_regex

    params["electronicEmailAddress__startswith"] = electronic_email_address_startswith

    params["firstName"] = first_name

    params["firstName__contains"] = first_name_contains

    params["firstName__endswith"] = first_name_endswith

    params["firstName__gt"] = first_name_gt

    params["firstName__gte"] = first_name_gte

    params["firstName__icontains"] = first_name_icontains

    params["firstName__iendswith"] = first_name_iendswith

    params["firstName__iexact"] = first_name_iexact

    json_first_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_in, Unset):
        json_first_name_in = first_name_in

    params["firstName__in"] = json_first_name_in

    params["firstName__iregex"] = first_name_iregex

    params["firstName__isnull"] = first_name_isnull

    params["firstName__istartswith"] = first_name_istartswith

    params["firstName__lt"] = first_name_lt

    params["firstName__lte"] = first_name_lte

    json_first_name_range: Union[Unset, list[str]] = UNSET
    if not isinstance(first_name_range, Unset):
        json_first_name_range = first_name_range

    params["firstName__range"] = json_first_name_range

    params["firstName__regex"] = first_name_regex

    params["firstName__startswith"] = first_name_startswith

    params["lastName"] = last_name

    params["lastName__contains"] = last_name_contains

    params["lastName__endswith"] = last_name_endswith

    params["lastName__gt"] = last_name_gt

    params["lastName__gte"] = last_name_gte

    params["lastName__icontains"] = last_name_icontains

    params["lastName__iendswith"] = last_name_iendswith

    params["lastName__iexact"] = last_name_iexact

    json_last_name_in: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_in, Unset):
        json_last_name_in = last_name_in

    params["lastName__in"] = json_last_name_in

    params["lastName__iregex"] = last_name_iregex

    params["lastName__isnull"] = last_name_isnull

    params["lastName__istartswith"] = last_name_istartswith

    params["lastName__lt"] = last_name_lt

    params["lastName__lte"] = last_name_lte

    json_last_name_range: Union[Unset, list[str]] = UNSET
    if not isinstance(last_name_range, Unset):
        json_last_name_range = last_name_range

    params["lastName__range"] = json_last_name_range

    params["lastName__regex"] = last_name_regex

    params["lastName__startswith"] = last_name_startswith

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

    params["onlineResource"] = online_resource

    params["onlineResource__contains"] = online_resource_contains

    params["onlineResource__endswith"] = online_resource_endswith

    params["onlineResource__gt"] = online_resource_gt

    params["onlineResource__gte"] = online_resource_gte

    params["onlineResource__icontains"] = online_resource_icontains

    params["onlineResource__iendswith"] = online_resource_iendswith

    params["onlineResource__iexact"] = online_resource_iexact

    json_online_resource_in: Union[Unset, list[str]] = UNSET
    if not isinstance(online_resource_in, Unset):
        json_online_resource_in = online_resource_in

    params["onlineResource__in"] = json_online_resource_in

    params["onlineResource__iregex"] = online_resource_iregex

    params["onlineResource__isnull"] = online_resource_isnull

    params["onlineResource__istartswith"] = online_resource_istartswith

    params["onlineResource__lt"] = online_resource_lt

    params["onlineResource__lte"] = online_resource_lte

    json_online_resource_range: Union[Unset, list[str]] = UNSET
    if not isinstance(online_resource_range, Unset):
        json_online_resource_range = online_resource_range

    params["onlineResource__range"] = json_online_resource_range

    params["onlineResource__regex"] = online_resource_regex

    params["onlineResource__startswith"] = online_resource_startswith

    params["ordering"] = ordering

    json_party_type: Union[Unset, str] = UNSET
    if not isinstance(party_type, Unset):
        json_party_type = party_type.value

    params["partyType"] = json_party_type

    params["partyType__contains"] = party_type_contains

    params["partyType__endswith"] = party_type_endswith

    params["partyType__gt"] = party_type_gt

    params["partyType__gte"] = party_type_gte

    params["partyType__icontains"] = party_type_icontains

    params["partyType__iendswith"] = party_type_iendswith

    params["partyType__iexact"] = party_type_iexact

    json_party_type_in: Union[Unset, list[str]] = UNSET
    if not isinstance(party_type_in, Unset):
        json_party_type_in = party_type_in

    params["partyType__in"] = json_party_type_in

    params["partyType__iregex"] = party_type_iregex

    params["partyType__isnull"] = party_type_isnull

    params["partyType__istartswith"] = party_type_istartswith

    params["partyType__lt"] = party_type_lt

    params["partyType__lte"] = party_type_lte

    json_party_type_range: Union[Unset, list[str]] = UNSET
    if not isinstance(party_type_range, Unset):
        json_party_type_range = party_type_range

    params["partyType__range"] = json_party_type_range

    params["partyType__regex"] = party_type_regex

    params["partyType__startswith"] = party_type_startswith

    params["phone"] = phone

    params["phone__contains"] = phone_contains

    params["phone__endswith"] = phone_endswith

    params["phone__gt"] = phone_gt

    params["phone__gte"] = phone_gte

    params["phone__icontains"] = phone_icontains

    params["phone__iendswith"] = phone_iendswith

    params["phone__iexact"] = phone_iexact

    json_phone_in: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_in, Unset):
        json_phone_in = phone_in

    params["phone__in"] = json_phone_in

    params["phone__iregex"] = phone_iregex

    params["phone__isnull"] = phone_isnull

    params["phone__istartswith"] = phone_istartswith

    params["phone__lt"] = phone_lt

    params["phone__lte"] = phone_lte

    json_phone_range: Union[Unset, list[str]] = UNSET
    if not isinstance(phone_range, Unset):
        json_phone_range = phone_range

    params["phone__range"] = json_phone_range

    params["phone__regex"] = phone_regex

    params["phone__startswith"] = phone_startswith

    params["postalCode"] = postal_code

    params["postalCode__contains"] = postal_code_contains

    params["postalCode__endswith"] = postal_code_endswith

    params["postalCode__gt"] = postal_code_gt

    params["postalCode__gte"] = postal_code_gte

    params["postalCode__icontains"] = postal_code_icontains

    params["postalCode__iendswith"] = postal_code_iendswith

    params["postalCode__iexact"] = postal_code_iexact

    json_postal_code_in: Union[Unset, list[str]] = UNSET
    if not isinstance(postal_code_in, Unset):
        json_postal_code_in = postal_code_in

    params["postalCode__in"] = json_postal_code_in

    params["postalCode__iregex"] = postal_code_iregex

    params["postalCode__isnull"] = postal_code_isnull

    params["postalCode__istartswith"] = postal_code_istartswith

    params["postalCode__lt"] = postal_code_lt

    params["postalCode__lte"] = postal_code_lte

    json_postal_code_range: Union[Unset, list[str]] = UNSET
    if not isinstance(postal_code_range, Unset):
        json_postal_code_range = postal_code_range

    params["postalCode__range"] = json_postal_code_range

    params["postalCode__regex"] = postal_code_regex

    params["postalCode__startswith"] = postal_code_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/parties/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedPartyReadList]:
    if response.status_code == 200:
        response_200 = PaginatedPartyReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedPartyReadList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    administrative_area: Union[Unset, str] = UNSET,
    administrative_area_contains: Union[Unset, str] = UNSET,
    administrative_area_endswith: Union[Unset, str] = UNSET,
    administrative_area_gt: Union[Unset, str] = UNSET,
    administrative_area_gte: Union[Unset, str] = UNSET,
    administrative_area_icontains: Union[Unset, str] = UNSET,
    administrative_area_iendswith: Union[Unset, str] = UNSET,
    administrative_area_iexact: Union[Unset, str] = UNSET,
    administrative_area_in: Union[Unset, list[str]] = UNSET,
    administrative_area_iregex: Union[Unset, str] = UNSET,
    administrative_area_isnull: Union[Unset, bool] = UNSET,
    administrative_area_istartswith: Union[Unset, str] = UNSET,
    administrative_area_lt: Union[Unset, str] = UNSET,
    administrative_area_lte: Union[Unset, str] = UNSET,
    administrative_area_range: Union[Unset, list[str]] = UNSET,
    administrative_area_regex: Union[Unset, str] = UNSET,
    administrative_area_startswith: Union[Unset, str] = UNSET,
    city: Union[Unset, str] = UNSET,
    city_contains: Union[Unset, str] = UNSET,
    city_endswith: Union[Unset, str] = UNSET,
    city_gt: Union[Unset, str] = UNSET,
    city_gte: Union[Unset, str] = UNSET,
    city_icontains: Union[Unset, str] = UNSET,
    city_iendswith: Union[Unset, str] = UNSET,
    city_iexact: Union[Unset, str] = UNSET,
    city_in: Union[Unset, list[str]] = UNSET,
    city_iregex: Union[Unset, str] = UNSET,
    city_isnull: Union[Unset, bool] = UNSET,
    city_istartswith: Union[Unset, str] = UNSET,
    city_lt: Union[Unset, str] = UNSET,
    city_lte: Union[Unset, str] = UNSET,
    city_range: Union[Unset, list[str]] = UNSET,
    city_regex: Union[Unset, str] = UNSET,
    city_startswith: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    country_contains: Union[Unset, str] = UNSET,
    country_endswith: Union[Unset, str] = UNSET,
    country_gt: Union[Unset, str] = UNSET,
    country_gte: Union[Unset, str] = UNSET,
    country_icontains: Union[Unset, str] = UNSET,
    country_iendswith: Union[Unset, str] = UNSET,
    country_iexact: Union[Unset, str] = UNSET,
    country_in: Union[Unset, list[str]] = UNSET,
    country_iregex: Union[Unset, str] = UNSET,
    country_isnull: Union[Unset, bool] = UNSET,
    country_istartswith: Union[Unset, str] = UNSET,
    country_lt: Union[Unset, str] = UNSET,
    country_lte: Union[Unset, str] = UNSET,
    country_range: Union[Unset, list[str]] = UNSET,
    country_regex: Union[Unset, str] = UNSET,
    country_startswith: Union[Unset, str] = UNSET,
    delivery_point: Union[Unset, str] = UNSET,
    delivery_point_contains: Union[Unset, str] = UNSET,
    delivery_point_endswith: Union[Unset, str] = UNSET,
    delivery_point_gt: Union[Unset, str] = UNSET,
    delivery_point_gte: Union[Unset, str] = UNSET,
    delivery_point_icontains: Union[Unset, str] = UNSET,
    delivery_point_iendswith: Union[Unset, str] = UNSET,
    delivery_point_iexact: Union[Unset, str] = UNSET,
    delivery_point_in: Union[Unset, list[str]] = UNSET,
    delivery_point_iregex: Union[Unset, str] = UNSET,
    delivery_point_isnull: Union[Unset, bool] = UNSET,
    delivery_point_istartswith: Union[Unset, str] = UNSET,
    delivery_point_lt: Union[Unset, str] = UNSET,
    delivery_point_lte: Union[Unset, str] = UNSET,
    delivery_point_range: Union[Unset, list[str]] = UNSET,
    delivery_point_regex: Union[Unset, str] = UNSET,
    delivery_point_startswith: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    description_contains: Union[Unset, str] = UNSET,
    description_endswith: Union[Unset, str] = UNSET,
    description_gt: Union[Unset, str] = UNSET,
    description_gte: Union[Unset, str] = UNSET,
    description_icontains: Union[Unset, str] = UNSET,
    description_iendswith: Union[Unset, str] = UNSET,
    description_iexact: Union[Unset, str] = UNSET,
    description_in: Union[Unset, list[str]] = UNSET,
    description_iregex: Union[Unset, str] = UNSET,
    description_isnull: Union[Unset, bool] = UNSET,
    description_istartswith: Union[Unset, str] = UNSET,
    description_lt: Union[Unset, str] = UNSET,
    description_lte: Union[Unset, str] = UNSET,
    description_range: Union[Unset, list[str]] = UNSET,
    description_regex: Union[Unset, str] = UNSET,
    description_startswith: Union[Unset, str] = UNSET,
    electronic_email_address: Union[Unset, str] = UNSET,
    electronic_email_address_contains: Union[Unset, str] = UNSET,
    electronic_email_address_endswith: Union[Unset, str] = UNSET,
    electronic_email_address_gt: Union[Unset, str] = UNSET,
    electronic_email_address_gte: Union[Unset, str] = UNSET,
    electronic_email_address_icontains: Union[Unset, str] = UNSET,
    electronic_email_address_iendswith: Union[Unset, str] = UNSET,
    electronic_email_address_iexact: Union[Unset, str] = UNSET,
    electronic_email_address_in: Union[Unset, list[str]] = UNSET,
    electronic_email_address_iregex: Union[Unset, str] = UNSET,
    electronic_email_address_isnull: Union[Unset, bool] = UNSET,
    electronic_email_address_istartswith: Union[Unset, str] = UNSET,
    electronic_email_address_lt: Union[Unset, str] = UNSET,
    electronic_email_address_lte: Union[Unset, str] = UNSET,
    electronic_email_address_range: Union[Unset, list[str]] = UNSET,
    electronic_email_address_regex: Union[Unset, str] = UNSET,
    electronic_email_address_startswith: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    first_name_contains: Union[Unset, str] = UNSET,
    first_name_endswith: Union[Unset, str] = UNSET,
    first_name_gt: Union[Unset, str] = UNSET,
    first_name_gte: Union[Unset, str] = UNSET,
    first_name_icontains: Union[Unset, str] = UNSET,
    first_name_iendswith: Union[Unset, str] = UNSET,
    first_name_iexact: Union[Unset, str] = UNSET,
    first_name_in: Union[Unset, list[str]] = UNSET,
    first_name_iregex: Union[Unset, str] = UNSET,
    first_name_isnull: Union[Unset, bool] = UNSET,
    first_name_istartswith: Union[Unset, str] = UNSET,
    first_name_lt: Union[Unset, str] = UNSET,
    first_name_lte: Union[Unset, str] = UNSET,
    first_name_range: Union[Unset, list[str]] = UNSET,
    first_name_regex: Union[Unset, str] = UNSET,
    first_name_startswith: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    last_name_contains: Union[Unset, str] = UNSET,
    last_name_endswith: Union[Unset, str] = UNSET,
    last_name_gt: Union[Unset, str] = UNSET,
    last_name_gte: Union[Unset, str] = UNSET,
    last_name_icontains: Union[Unset, str] = UNSET,
    last_name_iendswith: Union[Unset, str] = UNSET,
    last_name_iexact: Union[Unset, str] = UNSET,
    last_name_in: Union[Unset, list[str]] = UNSET,
    last_name_iregex: Union[Unset, str] = UNSET,
    last_name_isnull: Union[Unset, bool] = UNSET,
    last_name_istartswith: Union[Unset, str] = UNSET,
    last_name_lt: Union[Unset, str] = UNSET,
    last_name_lte: Union[Unset, str] = UNSET,
    last_name_range: Union[Unset, list[str]] = UNSET,
    last_name_regex: Union[Unset, str] = UNSET,
    last_name_startswith: Union[Unset, str] = UNSET,
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
    online_resource: Union[Unset, str] = UNSET,
    online_resource_contains: Union[Unset, str] = UNSET,
    online_resource_endswith: Union[Unset, str] = UNSET,
    online_resource_gt: Union[Unset, str] = UNSET,
    online_resource_gte: Union[Unset, str] = UNSET,
    online_resource_icontains: Union[Unset, str] = UNSET,
    online_resource_iendswith: Union[Unset, str] = UNSET,
    online_resource_iexact: Union[Unset, str] = UNSET,
    online_resource_in: Union[Unset, list[str]] = UNSET,
    online_resource_iregex: Union[Unset, str] = UNSET,
    online_resource_isnull: Union[Unset, bool] = UNSET,
    online_resource_istartswith: Union[Unset, str] = UNSET,
    online_resource_lt: Union[Unset, str] = UNSET,
    online_resource_lte: Union[Unset, str] = UNSET,
    online_resource_range: Union[Unset, list[str]] = UNSET,
    online_resource_regex: Union[Unset, str] = UNSET,
    online_resource_startswith: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    party_type: Union[Unset, PartiesListType] = UNSET,
    party_type_contains: Union[Unset, str] = UNSET,
    party_type_endswith: Union[Unset, str] = UNSET,
    party_type_gt: Union[Unset, str] = UNSET,
    party_type_gte: Union[Unset, str] = UNSET,
    party_type_icontains: Union[Unset, str] = UNSET,
    party_type_iendswith: Union[Unset, str] = UNSET,
    party_type_iexact: Union[Unset, str] = UNSET,
    party_type_in: Union[Unset, list[str]] = UNSET,
    party_type_iregex: Union[Unset, str] = UNSET,
    party_type_isnull: Union[Unset, bool] = UNSET,
    party_type_istartswith: Union[Unset, str] = UNSET,
    party_type_lt: Union[Unset, str] = UNSET,
    party_type_lte: Union[Unset, str] = UNSET,
    party_type_range: Union[Unset, list[str]] = UNSET,
    party_type_regex: Union[Unset, str] = UNSET,
    party_type_startswith: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    phone_contains: Union[Unset, str] = UNSET,
    phone_endswith: Union[Unset, str] = UNSET,
    phone_gt: Union[Unset, str] = UNSET,
    phone_gte: Union[Unset, str] = UNSET,
    phone_icontains: Union[Unset, str] = UNSET,
    phone_iendswith: Union[Unset, str] = UNSET,
    phone_iexact: Union[Unset, str] = UNSET,
    phone_in: Union[Unset, list[str]] = UNSET,
    phone_iregex: Union[Unset, str] = UNSET,
    phone_isnull: Union[Unset, bool] = UNSET,
    phone_istartswith: Union[Unset, str] = UNSET,
    phone_lt: Union[Unset, str] = UNSET,
    phone_lte: Union[Unset, str] = UNSET,
    phone_range: Union[Unset, list[str]] = UNSET,
    phone_regex: Union[Unset, str] = UNSET,
    phone_startswith: Union[Unset, str] = UNSET,
    postal_code: Union[Unset, str] = UNSET,
    postal_code_contains: Union[Unset, str] = UNSET,
    postal_code_endswith: Union[Unset, str] = UNSET,
    postal_code_gt: Union[Unset, str] = UNSET,
    postal_code_gte: Union[Unset, str] = UNSET,
    postal_code_icontains: Union[Unset, str] = UNSET,
    postal_code_iendswith: Union[Unset, str] = UNSET,
    postal_code_iexact: Union[Unset, str] = UNSET,
    postal_code_in: Union[Unset, list[str]] = UNSET,
    postal_code_iregex: Union[Unset, str] = UNSET,
    postal_code_isnull: Union[Unset, bool] = UNSET,
    postal_code_istartswith: Union[Unset, str] = UNSET,
    postal_code_lt: Union[Unset, str] = UNSET,
    postal_code_lte: Union[Unset, str] = UNSET,
    postal_code_range: Union[Unset, list[str]] = UNSET,
    postal_code_regex: Union[Unset, str] = UNSET,
    postal_code_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedPartyReadList]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        administrative_area (Union[Unset, str]):
        administrative_area_contains (Union[Unset, str]):
        administrative_area_endswith (Union[Unset, str]):
        administrative_area_gt (Union[Unset, str]):
        administrative_area_gte (Union[Unset, str]):
        administrative_area_icontains (Union[Unset, str]):
        administrative_area_iendswith (Union[Unset, str]):
        administrative_area_iexact (Union[Unset, str]):
        administrative_area_in (Union[Unset, list[str]]):
        administrative_area_iregex (Union[Unset, str]):
        administrative_area_isnull (Union[Unset, bool]):
        administrative_area_istartswith (Union[Unset, str]):
        administrative_area_lt (Union[Unset, str]):
        administrative_area_lte (Union[Unset, str]):
        administrative_area_range (Union[Unset, list[str]]):
        administrative_area_regex (Union[Unset, str]):
        administrative_area_startswith (Union[Unset, str]):
        city (Union[Unset, str]):
        city_contains (Union[Unset, str]):
        city_endswith (Union[Unset, str]):
        city_gt (Union[Unset, str]):
        city_gte (Union[Unset, str]):
        city_icontains (Union[Unset, str]):
        city_iendswith (Union[Unset, str]):
        city_iexact (Union[Unset, str]):
        city_in (Union[Unset, list[str]]):
        city_iregex (Union[Unset, str]):
        city_isnull (Union[Unset, bool]):
        city_istartswith (Union[Unset, str]):
        city_lt (Union[Unset, str]):
        city_lte (Union[Unset, str]):
        city_range (Union[Unset, list[str]]):
        city_regex (Union[Unset, str]):
        city_startswith (Union[Unset, str]):
        country (Union[Unset, str]):
        country_contains (Union[Unset, str]):
        country_endswith (Union[Unset, str]):
        country_gt (Union[Unset, str]):
        country_gte (Union[Unset, str]):
        country_icontains (Union[Unset, str]):
        country_iendswith (Union[Unset, str]):
        country_iexact (Union[Unset, str]):
        country_in (Union[Unset, list[str]]):
        country_iregex (Union[Unset, str]):
        country_isnull (Union[Unset, bool]):
        country_istartswith (Union[Unset, str]):
        country_lt (Union[Unset, str]):
        country_lte (Union[Unset, str]):
        country_range (Union[Unset, list[str]]):
        country_regex (Union[Unset, str]):
        country_startswith (Union[Unset, str]):
        delivery_point (Union[Unset, str]):
        delivery_point_contains (Union[Unset, str]):
        delivery_point_endswith (Union[Unset, str]):
        delivery_point_gt (Union[Unset, str]):
        delivery_point_gte (Union[Unset, str]):
        delivery_point_icontains (Union[Unset, str]):
        delivery_point_iendswith (Union[Unset, str]):
        delivery_point_iexact (Union[Unset, str]):
        delivery_point_in (Union[Unset, list[str]]):
        delivery_point_iregex (Union[Unset, str]):
        delivery_point_isnull (Union[Unset, bool]):
        delivery_point_istartswith (Union[Unset, str]):
        delivery_point_lt (Union[Unset, str]):
        delivery_point_lte (Union[Unset, str]):
        delivery_point_range (Union[Unset, list[str]]):
        delivery_point_regex (Union[Unset, str]):
        delivery_point_startswith (Union[Unset, str]):
        description (Union[Unset, str]):
        description_contains (Union[Unset, str]):
        description_endswith (Union[Unset, str]):
        description_gt (Union[Unset, str]):
        description_gte (Union[Unset, str]):
        description_icontains (Union[Unset, str]):
        description_iendswith (Union[Unset, str]):
        description_iexact (Union[Unset, str]):
        description_in (Union[Unset, list[str]]):
        description_iregex (Union[Unset, str]):
        description_isnull (Union[Unset, bool]):
        description_istartswith (Union[Unset, str]):
        description_lt (Union[Unset, str]):
        description_lte (Union[Unset, str]):
        description_range (Union[Unset, list[str]]):
        description_regex (Union[Unset, str]):
        description_startswith (Union[Unset, str]):
        electronic_email_address (Union[Unset, str]):
        electronic_email_address_contains (Union[Unset, str]):
        electronic_email_address_endswith (Union[Unset, str]):
        electronic_email_address_gt (Union[Unset, str]):
        electronic_email_address_gte (Union[Unset, str]):
        electronic_email_address_icontains (Union[Unset, str]):
        electronic_email_address_iendswith (Union[Unset, str]):
        electronic_email_address_iexact (Union[Unset, str]):
        electronic_email_address_in (Union[Unset, list[str]]):
        electronic_email_address_iregex (Union[Unset, str]):
        electronic_email_address_isnull (Union[Unset, bool]):
        electronic_email_address_istartswith (Union[Unset, str]):
        electronic_email_address_lt (Union[Unset, str]):
        electronic_email_address_lte (Union[Unset, str]):
        electronic_email_address_range (Union[Unset, list[str]]):
        electronic_email_address_regex (Union[Unset, str]):
        electronic_email_address_startswith (Union[Unset, str]):
        first_name (Union[Unset, str]):
        first_name_contains (Union[Unset, str]):
        first_name_endswith (Union[Unset, str]):
        first_name_gt (Union[Unset, str]):
        first_name_gte (Union[Unset, str]):
        first_name_icontains (Union[Unset, str]):
        first_name_iendswith (Union[Unset, str]):
        first_name_iexact (Union[Unset, str]):
        first_name_in (Union[Unset, list[str]]):
        first_name_iregex (Union[Unset, str]):
        first_name_isnull (Union[Unset, bool]):
        first_name_istartswith (Union[Unset, str]):
        first_name_lt (Union[Unset, str]):
        first_name_lte (Union[Unset, str]):
        first_name_range (Union[Unset, list[str]]):
        first_name_regex (Union[Unset, str]):
        first_name_startswith (Union[Unset, str]):
        last_name (Union[Unset, str]):
        last_name_contains (Union[Unset, str]):
        last_name_endswith (Union[Unset, str]):
        last_name_gt (Union[Unset, str]):
        last_name_gte (Union[Unset, str]):
        last_name_icontains (Union[Unset, str]):
        last_name_iendswith (Union[Unset, str]):
        last_name_iexact (Union[Unset, str]):
        last_name_in (Union[Unset, list[str]]):
        last_name_iregex (Union[Unset, str]):
        last_name_isnull (Union[Unset, bool]):
        last_name_istartswith (Union[Unset, str]):
        last_name_lt (Union[Unset, str]):
        last_name_lte (Union[Unset, str]):
        last_name_range (Union[Unset, list[str]]):
        last_name_regex (Union[Unset, str]):
        last_name_startswith (Union[Unset, str]):
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
        online_resource (Union[Unset, str]):
        online_resource_contains (Union[Unset, str]):
        online_resource_endswith (Union[Unset, str]):
        online_resource_gt (Union[Unset, str]):
        online_resource_gte (Union[Unset, str]):
        online_resource_icontains (Union[Unset, str]):
        online_resource_iendswith (Union[Unset, str]):
        online_resource_iexact (Union[Unset, str]):
        online_resource_in (Union[Unset, list[str]]):
        online_resource_iregex (Union[Unset, str]):
        online_resource_isnull (Union[Unset, bool]):
        online_resource_istartswith (Union[Unset, str]):
        online_resource_lt (Union[Unset, str]):
        online_resource_lte (Union[Unset, str]):
        online_resource_range (Union[Unset, list[str]]):
        online_resource_regex (Union[Unset, str]):
        online_resource_startswith (Union[Unset, str]):
        ordering (Union[Unset, str]):
        party_type (Union[Unset, PartiesListType]):
        party_type_contains (Union[Unset, str]):
        party_type_endswith (Union[Unset, str]):
        party_type_gt (Union[Unset, str]):
        party_type_gte (Union[Unset, str]):
        party_type_icontains (Union[Unset, str]):
        party_type_iendswith (Union[Unset, str]):
        party_type_iexact (Union[Unset, str]):
        party_type_in (Union[Unset, list[str]]):
        party_type_iregex (Union[Unset, str]):
        party_type_isnull (Union[Unset, bool]):
        party_type_istartswith (Union[Unset, str]):
        party_type_lt (Union[Unset, str]):
        party_type_lte (Union[Unset, str]):
        party_type_range (Union[Unset, list[str]]):
        party_type_regex (Union[Unset, str]):
        party_type_startswith (Union[Unset, str]):
        phone (Union[Unset, str]):
        phone_contains (Union[Unset, str]):
        phone_endswith (Union[Unset, str]):
        phone_gt (Union[Unset, str]):
        phone_gte (Union[Unset, str]):
        phone_icontains (Union[Unset, str]):
        phone_iendswith (Union[Unset, str]):
        phone_iexact (Union[Unset, str]):
        phone_in (Union[Unset, list[str]]):
        phone_iregex (Union[Unset, str]):
        phone_isnull (Union[Unset, bool]):
        phone_istartswith (Union[Unset, str]):
        phone_lt (Union[Unset, str]):
        phone_lte (Union[Unset, str]):
        phone_range (Union[Unset, list[str]]):
        phone_regex (Union[Unset, str]):
        phone_startswith (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        postal_code_contains (Union[Unset, str]):
        postal_code_endswith (Union[Unset, str]):
        postal_code_gt (Union[Unset, str]):
        postal_code_gte (Union[Unset, str]):
        postal_code_icontains (Union[Unset, str]):
        postal_code_iendswith (Union[Unset, str]):
        postal_code_iexact (Union[Unset, str]):
        postal_code_in (Union[Unset, list[str]]):
        postal_code_iregex (Union[Unset, str]):
        postal_code_isnull (Union[Unset, bool]):
        postal_code_istartswith (Union[Unset, str]):
        postal_code_lt (Union[Unset, str]):
        postal_code_lte (Union[Unset, str]):
        postal_code_range (Union[Unset, list[str]]):
        postal_code_regex (Union[Unset, str]):
        postal_code_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPartyReadList]
    """

    kwargs = _get_kwargs(
        administrative_area=administrative_area,
        administrative_area_contains=administrative_area_contains,
        administrative_area_endswith=administrative_area_endswith,
        administrative_area_gt=administrative_area_gt,
        administrative_area_gte=administrative_area_gte,
        administrative_area_icontains=administrative_area_icontains,
        administrative_area_iendswith=administrative_area_iendswith,
        administrative_area_iexact=administrative_area_iexact,
        administrative_area_in=administrative_area_in,
        administrative_area_iregex=administrative_area_iregex,
        administrative_area_isnull=administrative_area_isnull,
        administrative_area_istartswith=administrative_area_istartswith,
        administrative_area_lt=administrative_area_lt,
        administrative_area_lte=administrative_area_lte,
        administrative_area_range=administrative_area_range,
        administrative_area_regex=administrative_area_regex,
        administrative_area_startswith=administrative_area_startswith,
        city=city,
        city_contains=city_contains,
        city_endswith=city_endswith,
        city_gt=city_gt,
        city_gte=city_gte,
        city_icontains=city_icontains,
        city_iendswith=city_iendswith,
        city_iexact=city_iexact,
        city_in=city_in,
        city_iregex=city_iregex,
        city_isnull=city_isnull,
        city_istartswith=city_istartswith,
        city_lt=city_lt,
        city_lte=city_lte,
        city_range=city_range,
        city_regex=city_regex,
        city_startswith=city_startswith,
        country=country,
        country_contains=country_contains,
        country_endswith=country_endswith,
        country_gt=country_gt,
        country_gte=country_gte,
        country_icontains=country_icontains,
        country_iendswith=country_iendswith,
        country_iexact=country_iexact,
        country_in=country_in,
        country_iregex=country_iregex,
        country_isnull=country_isnull,
        country_istartswith=country_istartswith,
        country_lt=country_lt,
        country_lte=country_lte,
        country_range=country_range,
        country_regex=country_regex,
        country_startswith=country_startswith,
        delivery_point=delivery_point,
        delivery_point_contains=delivery_point_contains,
        delivery_point_endswith=delivery_point_endswith,
        delivery_point_gt=delivery_point_gt,
        delivery_point_gte=delivery_point_gte,
        delivery_point_icontains=delivery_point_icontains,
        delivery_point_iendswith=delivery_point_iendswith,
        delivery_point_iexact=delivery_point_iexact,
        delivery_point_in=delivery_point_in,
        delivery_point_iregex=delivery_point_iregex,
        delivery_point_isnull=delivery_point_isnull,
        delivery_point_istartswith=delivery_point_istartswith,
        delivery_point_lt=delivery_point_lt,
        delivery_point_lte=delivery_point_lte,
        delivery_point_range=delivery_point_range,
        delivery_point_regex=delivery_point_regex,
        delivery_point_startswith=delivery_point_startswith,
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
        electronic_email_address=electronic_email_address,
        electronic_email_address_contains=electronic_email_address_contains,
        electronic_email_address_endswith=electronic_email_address_endswith,
        electronic_email_address_gt=electronic_email_address_gt,
        electronic_email_address_gte=electronic_email_address_gte,
        electronic_email_address_icontains=electronic_email_address_icontains,
        electronic_email_address_iendswith=electronic_email_address_iendswith,
        electronic_email_address_iexact=electronic_email_address_iexact,
        electronic_email_address_in=electronic_email_address_in,
        electronic_email_address_iregex=electronic_email_address_iregex,
        electronic_email_address_isnull=electronic_email_address_isnull,
        electronic_email_address_istartswith=electronic_email_address_istartswith,
        electronic_email_address_lt=electronic_email_address_lt,
        electronic_email_address_lte=electronic_email_address_lte,
        electronic_email_address_range=electronic_email_address_range,
        electronic_email_address_regex=electronic_email_address_regex,
        electronic_email_address_startswith=electronic_email_address_startswith,
        first_name=first_name,
        first_name_contains=first_name_contains,
        first_name_endswith=first_name_endswith,
        first_name_gt=first_name_gt,
        first_name_gte=first_name_gte,
        first_name_icontains=first_name_icontains,
        first_name_iendswith=first_name_iendswith,
        first_name_iexact=first_name_iexact,
        first_name_in=first_name_in,
        first_name_iregex=first_name_iregex,
        first_name_isnull=first_name_isnull,
        first_name_istartswith=first_name_istartswith,
        first_name_lt=first_name_lt,
        first_name_lte=first_name_lte,
        first_name_range=first_name_range,
        first_name_regex=first_name_regex,
        first_name_startswith=first_name_startswith,
        last_name=last_name,
        last_name_contains=last_name_contains,
        last_name_endswith=last_name_endswith,
        last_name_gt=last_name_gt,
        last_name_gte=last_name_gte,
        last_name_icontains=last_name_icontains,
        last_name_iendswith=last_name_iendswith,
        last_name_iexact=last_name_iexact,
        last_name_in=last_name_in,
        last_name_iregex=last_name_iregex,
        last_name_isnull=last_name_isnull,
        last_name_istartswith=last_name_istartswith,
        last_name_lt=last_name_lt,
        last_name_lte=last_name_lte,
        last_name_range=last_name_range,
        last_name_regex=last_name_regex,
        last_name_startswith=last_name_startswith,
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
        online_resource=online_resource,
        online_resource_contains=online_resource_contains,
        online_resource_endswith=online_resource_endswith,
        online_resource_gt=online_resource_gt,
        online_resource_gte=online_resource_gte,
        online_resource_icontains=online_resource_icontains,
        online_resource_iendswith=online_resource_iendswith,
        online_resource_iexact=online_resource_iexact,
        online_resource_in=online_resource_in,
        online_resource_iregex=online_resource_iregex,
        online_resource_isnull=online_resource_isnull,
        online_resource_istartswith=online_resource_istartswith,
        online_resource_lt=online_resource_lt,
        online_resource_lte=online_resource_lte,
        online_resource_range=online_resource_range,
        online_resource_regex=online_resource_regex,
        online_resource_startswith=online_resource_startswith,
        ordering=ordering,
        party_type=party_type,
        party_type_contains=party_type_contains,
        party_type_endswith=party_type_endswith,
        party_type_gt=party_type_gt,
        party_type_gte=party_type_gte,
        party_type_icontains=party_type_icontains,
        party_type_iendswith=party_type_iendswith,
        party_type_iexact=party_type_iexact,
        party_type_in=party_type_in,
        party_type_iregex=party_type_iregex,
        party_type_isnull=party_type_isnull,
        party_type_istartswith=party_type_istartswith,
        party_type_lt=party_type_lt,
        party_type_lte=party_type_lte,
        party_type_range=party_type_range,
        party_type_regex=party_type_regex,
        party_type_startswith=party_type_startswith,
        phone=phone,
        phone_contains=phone_contains,
        phone_endswith=phone_endswith,
        phone_gt=phone_gt,
        phone_gte=phone_gte,
        phone_icontains=phone_icontains,
        phone_iendswith=phone_iendswith,
        phone_iexact=phone_iexact,
        phone_in=phone_in,
        phone_iregex=phone_iregex,
        phone_isnull=phone_isnull,
        phone_istartswith=phone_istartswith,
        phone_lt=phone_lt,
        phone_lte=phone_lte,
        phone_range=phone_range,
        phone_regex=phone_regex,
        phone_startswith=phone_startswith,
        postal_code=postal_code,
        postal_code_contains=postal_code_contains,
        postal_code_endswith=postal_code_endswith,
        postal_code_gt=postal_code_gt,
        postal_code_gte=postal_code_gte,
        postal_code_icontains=postal_code_icontains,
        postal_code_iendswith=postal_code_iendswith,
        postal_code_iexact=postal_code_iexact,
        postal_code_in=postal_code_in,
        postal_code_iregex=postal_code_iregex,
        postal_code_isnull=postal_code_isnull,
        postal_code_istartswith=postal_code_istartswith,
        postal_code_lt=postal_code_lt,
        postal_code_lte=postal_code_lte,
        postal_code_range=postal_code_range,
        postal_code_regex=postal_code_regex,
        postal_code_startswith=postal_code_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    administrative_area: Union[Unset, str] = UNSET,
    administrative_area_contains: Union[Unset, str] = UNSET,
    administrative_area_endswith: Union[Unset, str] = UNSET,
    administrative_area_gt: Union[Unset, str] = UNSET,
    administrative_area_gte: Union[Unset, str] = UNSET,
    administrative_area_icontains: Union[Unset, str] = UNSET,
    administrative_area_iendswith: Union[Unset, str] = UNSET,
    administrative_area_iexact: Union[Unset, str] = UNSET,
    administrative_area_in: Union[Unset, list[str]] = UNSET,
    administrative_area_iregex: Union[Unset, str] = UNSET,
    administrative_area_isnull: Union[Unset, bool] = UNSET,
    administrative_area_istartswith: Union[Unset, str] = UNSET,
    administrative_area_lt: Union[Unset, str] = UNSET,
    administrative_area_lte: Union[Unset, str] = UNSET,
    administrative_area_range: Union[Unset, list[str]] = UNSET,
    administrative_area_regex: Union[Unset, str] = UNSET,
    administrative_area_startswith: Union[Unset, str] = UNSET,
    city: Union[Unset, str] = UNSET,
    city_contains: Union[Unset, str] = UNSET,
    city_endswith: Union[Unset, str] = UNSET,
    city_gt: Union[Unset, str] = UNSET,
    city_gte: Union[Unset, str] = UNSET,
    city_icontains: Union[Unset, str] = UNSET,
    city_iendswith: Union[Unset, str] = UNSET,
    city_iexact: Union[Unset, str] = UNSET,
    city_in: Union[Unset, list[str]] = UNSET,
    city_iregex: Union[Unset, str] = UNSET,
    city_isnull: Union[Unset, bool] = UNSET,
    city_istartswith: Union[Unset, str] = UNSET,
    city_lt: Union[Unset, str] = UNSET,
    city_lte: Union[Unset, str] = UNSET,
    city_range: Union[Unset, list[str]] = UNSET,
    city_regex: Union[Unset, str] = UNSET,
    city_startswith: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    country_contains: Union[Unset, str] = UNSET,
    country_endswith: Union[Unset, str] = UNSET,
    country_gt: Union[Unset, str] = UNSET,
    country_gte: Union[Unset, str] = UNSET,
    country_icontains: Union[Unset, str] = UNSET,
    country_iendswith: Union[Unset, str] = UNSET,
    country_iexact: Union[Unset, str] = UNSET,
    country_in: Union[Unset, list[str]] = UNSET,
    country_iregex: Union[Unset, str] = UNSET,
    country_isnull: Union[Unset, bool] = UNSET,
    country_istartswith: Union[Unset, str] = UNSET,
    country_lt: Union[Unset, str] = UNSET,
    country_lte: Union[Unset, str] = UNSET,
    country_range: Union[Unset, list[str]] = UNSET,
    country_regex: Union[Unset, str] = UNSET,
    country_startswith: Union[Unset, str] = UNSET,
    delivery_point: Union[Unset, str] = UNSET,
    delivery_point_contains: Union[Unset, str] = UNSET,
    delivery_point_endswith: Union[Unset, str] = UNSET,
    delivery_point_gt: Union[Unset, str] = UNSET,
    delivery_point_gte: Union[Unset, str] = UNSET,
    delivery_point_icontains: Union[Unset, str] = UNSET,
    delivery_point_iendswith: Union[Unset, str] = UNSET,
    delivery_point_iexact: Union[Unset, str] = UNSET,
    delivery_point_in: Union[Unset, list[str]] = UNSET,
    delivery_point_iregex: Union[Unset, str] = UNSET,
    delivery_point_isnull: Union[Unset, bool] = UNSET,
    delivery_point_istartswith: Union[Unset, str] = UNSET,
    delivery_point_lt: Union[Unset, str] = UNSET,
    delivery_point_lte: Union[Unset, str] = UNSET,
    delivery_point_range: Union[Unset, list[str]] = UNSET,
    delivery_point_regex: Union[Unset, str] = UNSET,
    delivery_point_startswith: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    description_contains: Union[Unset, str] = UNSET,
    description_endswith: Union[Unset, str] = UNSET,
    description_gt: Union[Unset, str] = UNSET,
    description_gte: Union[Unset, str] = UNSET,
    description_icontains: Union[Unset, str] = UNSET,
    description_iendswith: Union[Unset, str] = UNSET,
    description_iexact: Union[Unset, str] = UNSET,
    description_in: Union[Unset, list[str]] = UNSET,
    description_iregex: Union[Unset, str] = UNSET,
    description_isnull: Union[Unset, bool] = UNSET,
    description_istartswith: Union[Unset, str] = UNSET,
    description_lt: Union[Unset, str] = UNSET,
    description_lte: Union[Unset, str] = UNSET,
    description_range: Union[Unset, list[str]] = UNSET,
    description_regex: Union[Unset, str] = UNSET,
    description_startswith: Union[Unset, str] = UNSET,
    electronic_email_address: Union[Unset, str] = UNSET,
    electronic_email_address_contains: Union[Unset, str] = UNSET,
    electronic_email_address_endswith: Union[Unset, str] = UNSET,
    electronic_email_address_gt: Union[Unset, str] = UNSET,
    electronic_email_address_gte: Union[Unset, str] = UNSET,
    electronic_email_address_icontains: Union[Unset, str] = UNSET,
    electronic_email_address_iendswith: Union[Unset, str] = UNSET,
    electronic_email_address_iexact: Union[Unset, str] = UNSET,
    electronic_email_address_in: Union[Unset, list[str]] = UNSET,
    electronic_email_address_iregex: Union[Unset, str] = UNSET,
    electronic_email_address_isnull: Union[Unset, bool] = UNSET,
    electronic_email_address_istartswith: Union[Unset, str] = UNSET,
    electronic_email_address_lt: Union[Unset, str] = UNSET,
    electronic_email_address_lte: Union[Unset, str] = UNSET,
    electronic_email_address_range: Union[Unset, list[str]] = UNSET,
    electronic_email_address_regex: Union[Unset, str] = UNSET,
    electronic_email_address_startswith: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    first_name_contains: Union[Unset, str] = UNSET,
    first_name_endswith: Union[Unset, str] = UNSET,
    first_name_gt: Union[Unset, str] = UNSET,
    first_name_gte: Union[Unset, str] = UNSET,
    first_name_icontains: Union[Unset, str] = UNSET,
    first_name_iendswith: Union[Unset, str] = UNSET,
    first_name_iexact: Union[Unset, str] = UNSET,
    first_name_in: Union[Unset, list[str]] = UNSET,
    first_name_iregex: Union[Unset, str] = UNSET,
    first_name_isnull: Union[Unset, bool] = UNSET,
    first_name_istartswith: Union[Unset, str] = UNSET,
    first_name_lt: Union[Unset, str] = UNSET,
    first_name_lte: Union[Unset, str] = UNSET,
    first_name_range: Union[Unset, list[str]] = UNSET,
    first_name_regex: Union[Unset, str] = UNSET,
    first_name_startswith: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    last_name_contains: Union[Unset, str] = UNSET,
    last_name_endswith: Union[Unset, str] = UNSET,
    last_name_gt: Union[Unset, str] = UNSET,
    last_name_gte: Union[Unset, str] = UNSET,
    last_name_icontains: Union[Unset, str] = UNSET,
    last_name_iendswith: Union[Unset, str] = UNSET,
    last_name_iexact: Union[Unset, str] = UNSET,
    last_name_in: Union[Unset, list[str]] = UNSET,
    last_name_iregex: Union[Unset, str] = UNSET,
    last_name_isnull: Union[Unset, bool] = UNSET,
    last_name_istartswith: Union[Unset, str] = UNSET,
    last_name_lt: Union[Unset, str] = UNSET,
    last_name_lte: Union[Unset, str] = UNSET,
    last_name_range: Union[Unset, list[str]] = UNSET,
    last_name_regex: Union[Unset, str] = UNSET,
    last_name_startswith: Union[Unset, str] = UNSET,
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
    online_resource: Union[Unset, str] = UNSET,
    online_resource_contains: Union[Unset, str] = UNSET,
    online_resource_endswith: Union[Unset, str] = UNSET,
    online_resource_gt: Union[Unset, str] = UNSET,
    online_resource_gte: Union[Unset, str] = UNSET,
    online_resource_icontains: Union[Unset, str] = UNSET,
    online_resource_iendswith: Union[Unset, str] = UNSET,
    online_resource_iexact: Union[Unset, str] = UNSET,
    online_resource_in: Union[Unset, list[str]] = UNSET,
    online_resource_iregex: Union[Unset, str] = UNSET,
    online_resource_isnull: Union[Unset, bool] = UNSET,
    online_resource_istartswith: Union[Unset, str] = UNSET,
    online_resource_lt: Union[Unset, str] = UNSET,
    online_resource_lte: Union[Unset, str] = UNSET,
    online_resource_range: Union[Unset, list[str]] = UNSET,
    online_resource_regex: Union[Unset, str] = UNSET,
    online_resource_startswith: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    party_type: Union[Unset, PartiesListType] = UNSET,
    party_type_contains: Union[Unset, str] = UNSET,
    party_type_endswith: Union[Unset, str] = UNSET,
    party_type_gt: Union[Unset, str] = UNSET,
    party_type_gte: Union[Unset, str] = UNSET,
    party_type_icontains: Union[Unset, str] = UNSET,
    party_type_iendswith: Union[Unset, str] = UNSET,
    party_type_iexact: Union[Unset, str] = UNSET,
    party_type_in: Union[Unset, list[str]] = UNSET,
    party_type_iregex: Union[Unset, str] = UNSET,
    party_type_isnull: Union[Unset, bool] = UNSET,
    party_type_istartswith: Union[Unset, str] = UNSET,
    party_type_lt: Union[Unset, str] = UNSET,
    party_type_lte: Union[Unset, str] = UNSET,
    party_type_range: Union[Unset, list[str]] = UNSET,
    party_type_regex: Union[Unset, str] = UNSET,
    party_type_startswith: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    phone_contains: Union[Unset, str] = UNSET,
    phone_endswith: Union[Unset, str] = UNSET,
    phone_gt: Union[Unset, str] = UNSET,
    phone_gte: Union[Unset, str] = UNSET,
    phone_icontains: Union[Unset, str] = UNSET,
    phone_iendswith: Union[Unset, str] = UNSET,
    phone_iexact: Union[Unset, str] = UNSET,
    phone_in: Union[Unset, list[str]] = UNSET,
    phone_iregex: Union[Unset, str] = UNSET,
    phone_isnull: Union[Unset, bool] = UNSET,
    phone_istartswith: Union[Unset, str] = UNSET,
    phone_lt: Union[Unset, str] = UNSET,
    phone_lte: Union[Unset, str] = UNSET,
    phone_range: Union[Unset, list[str]] = UNSET,
    phone_regex: Union[Unset, str] = UNSET,
    phone_startswith: Union[Unset, str] = UNSET,
    postal_code: Union[Unset, str] = UNSET,
    postal_code_contains: Union[Unset, str] = UNSET,
    postal_code_endswith: Union[Unset, str] = UNSET,
    postal_code_gt: Union[Unset, str] = UNSET,
    postal_code_gte: Union[Unset, str] = UNSET,
    postal_code_icontains: Union[Unset, str] = UNSET,
    postal_code_iendswith: Union[Unset, str] = UNSET,
    postal_code_iexact: Union[Unset, str] = UNSET,
    postal_code_in: Union[Unset, list[str]] = UNSET,
    postal_code_iregex: Union[Unset, str] = UNSET,
    postal_code_isnull: Union[Unset, bool] = UNSET,
    postal_code_istartswith: Union[Unset, str] = UNSET,
    postal_code_lt: Union[Unset, str] = UNSET,
    postal_code_lte: Union[Unset, str] = UNSET,
    postal_code_range: Union[Unset, list[str]] = UNSET,
    postal_code_regex: Union[Unset, str] = UNSET,
    postal_code_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedPartyReadList]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        administrative_area (Union[Unset, str]):
        administrative_area_contains (Union[Unset, str]):
        administrative_area_endswith (Union[Unset, str]):
        administrative_area_gt (Union[Unset, str]):
        administrative_area_gte (Union[Unset, str]):
        administrative_area_icontains (Union[Unset, str]):
        administrative_area_iendswith (Union[Unset, str]):
        administrative_area_iexact (Union[Unset, str]):
        administrative_area_in (Union[Unset, list[str]]):
        administrative_area_iregex (Union[Unset, str]):
        administrative_area_isnull (Union[Unset, bool]):
        administrative_area_istartswith (Union[Unset, str]):
        administrative_area_lt (Union[Unset, str]):
        administrative_area_lte (Union[Unset, str]):
        administrative_area_range (Union[Unset, list[str]]):
        administrative_area_regex (Union[Unset, str]):
        administrative_area_startswith (Union[Unset, str]):
        city (Union[Unset, str]):
        city_contains (Union[Unset, str]):
        city_endswith (Union[Unset, str]):
        city_gt (Union[Unset, str]):
        city_gte (Union[Unset, str]):
        city_icontains (Union[Unset, str]):
        city_iendswith (Union[Unset, str]):
        city_iexact (Union[Unset, str]):
        city_in (Union[Unset, list[str]]):
        city_iregex (Union[Unset, str]):
        city_isnull (Union[Unset, bool]):
        city_istartswith (Union[Unset, str]):
        city_lt (Union[Unset, str]):
        city_lte (Union[Unset, str]):
        city_range (Union[Unset, list[str]]):
        city_regex (Union[Unset, str]):
        city_startswith (Union[Unset, str]):
        country (Union[Unset, str]):
        country_contains (Union[Unset, str]):
        country_endswith (Union[Unset, str]):
        country_gt (Union[Unset, str]):
        country_gte (Union[Unset, str]):
        country_icontains (Union[Unset, str]):
        country_iendswith (Union[Unset, str]):
        country_iexact (Union[Unset, str]):
        country_in (Union[Unset, list[str]]):
        country_iregex (Union[Unset, str]):
        country_isnull (Union[Unset, bool]):
        country_istartswith (Union[Unset, str]):
        country_lt (Union[Unset, str]):
        country_lte (Union[Unset, str]):
        country_range (Union[Unset, list[str]]):
        country_regex (Union[Unset, str]):
        country_startswith (Union[Unset, str]):
        delivery_point (Union[Unset, str]):
        delivery_point_contains (Union[Unset, str]):
        delivery_point_endswith (Union[Unset, str]):
        delivery_point_gt (Union[Unset, str]):
        delivery_point_gte (Union[Unset, str]):
        delivery_point_icontains (Union[Unset, str]):
        delivery_point_iendswith (Union[Unset, str]):
        delivery_point_iexact (Union[Unset, str]):
        delivery_point_in (Union[Unset, list[str]]):
        delivery_point_iregex (Union[Unset, str]):
        delivery_point_isnull (Union[Unset, bool]):
        delivery_point_istartswith (Union[Unset, str]):
        delivery_point_lt (Union[Unset, str]):
        delivery_point_lte (Union[Unset, str]):
        delivery_point_range (Union[Unset, list[str]]):
        delivery_point_regex (Union[Unset, str]):
        delivery_point_startswith (Union[Unset, str]):
        description (Union[Unset, str]):
        description_contains (Union[Unset, str]):
        description_endswith (Union[Unset, str]):
        description_gt (Union[Unset, str]):
        description_gte (Union[Unset, str]):
        description_icontains (Union[Unset, str]):
        description_iendswith (Union[Unset, str]):
        description_iexact (Union[Unset, str]):
        description_in (Union[Unset, list[str]]):
        description_iregex (Union[Unset, str]):
        description_isnull (Union[Unset, bool]):
        description_istartswith (Union[Unset, str]):
        description_lt (Union[Unset, str]):
        description_lte (Union[Unset, str]):
        description_range (Union[Unset, list[str]]):
        description_regex (Union[Unset, str]):
        description_startswith (Union[Unset, str]):
        electronic_email_address (Union[Unset, str]):
        electronic_email_address_contains (Union[Unset, str]):
        electronic_email_address_endswith (Union[Unset, str]):
        electronic_email_address_gt (Union[Unset, str]):
        electronic_email_address_gte (Union[Unset, str]):
        electronic_email_address_icontains (Union[Unset, str]):
        electronic_email_address_iendswith (Union[Unset, str]):
        electronic_email_address_iexact (Union[Unset, str]):
        electronic_email_address_in (Union[Unset, list[str]]):
        electronic_email_address_iregex (Union[Unset, str]):
        electronic_email_address_isnull (Union[Unset, bool]):
        electronic_email_address_istartswith (Union[Unset, str]):
        electronic_email_address_lt (Union[Unset, str]):
        electronic_email_address_lte (Union[Unset, str]):
        electronic_email_address_range (Union[Unset, list[str]]):
        electronic_email_address_regex (Union[Unset, str]):
        electronic_email_address_startswith (Union[Unset, str]):
        first_name (Union[Unset, str]):
        first_name_contains (Union[Unset, str]):
        first_name_endswith (Union[Unset, str]):
        first_name_gt (Union[Unset, str]):
        first_name_gte (Union[Unset, str]):
        first_name_icontains (Union[Unset, str]):
        first_name_iendswith (Union[Unset, str]):
        first_name_iexact (Union[Unset, str]):
        first_name_in (Union[Unset, list[str]]):
        first_name_iregex (Union[Unset, str]):
        first_name_isnull (Union[Unset, bool]):
        first_name_istartswith (Union[Unset, str]):
        first_name_lt (Union[Unset, str]):
        first_name_lte (Union[Unset, str]):
        first_name_range (Union[Unset, list[str]]):
        first_name_regex (Union[Unset, str]):
        first_name_startswith (Union[Unset, str]):
        last_name (Union[Unset, str]):
        last_name_contains (Union[Unset, str]):
        last_name_endswith (Union[Unset, str]):
        last_name_gt (Union[Unset, str]):
        last_name_gte (Union[Unset, str]):
        last_name_icontains (Union[Unset, str]):
        last_name_iendswith (Union[Unset, str]):
        last_name_iexact (Union[Unset, str]):
        last_name_in (Union[Unset, list[str]]):
        last_name_iregex (Union[Unset, str]):
        last_name_isnull (Union[Unset, bool]):
        last_name_istartswith (Union[Unset, str]):
        last_name_lt (Union[Unset, str]):
        last_name_lte (Union[Unset, str]):
        last_name_range (Union[Unset, list[str]]):
        last_name_regex (Union[Unset, str]):
        last_name_startswith (Union[Unset, str]):
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
        online_resource (Union[Unset, str]):
        online_resource_contains (Union[Unset, str]):
        online_resource_endswith (Union[Unset, str]):
        online_resource_gt (Union[Unset, str]):
        online_resource_gte (Union[Unset, str]):
        online_resource_icontains (Union[Unset, str]):
        online_resource_iendswith (Union[Unset, str]):
        online_resource_iexact (Union[Unset, str]):
        online_resource_in (Union[Unset, list[str]]):
        online_resource_iregex (Union[Unset, str]):
        online_resource_isnull (Union[Unset, bool]):
        online_resource_istartswith (Union[Unset, str]):
        online_resource_lt (Union[Unset, str]):
        online_resource_lte (Union[Unset, str]):
        online_resource_range (Union[Unset, list[str]]):
        online_resource_regex (Union[Unset, str]):
        online_resource_startswith (Union[Unset, str]):
        ordering (Union[Unset, str]):
        party_type (Union[Unset, PartiesListType]):
        party_type_contains (Union[Unset, str]):
        party_type_endswith (Union[Unset, str]):
        party_type_gt (Union[Unset, str]):
        party_type_gte (Union[Unset, str]):
        party_type_icontains (Union[Unset, str]):
        party_type_iendswith (Union[Unset, str]):
        party_type_iexact (Union[Unset, str]):
        party_type_in (Union[Unset, list[str]]):
        party_type_iregex (Union[Unset, str]):
        party_type_isnull (Union[Unset, bool]):
        party_type_istartswith (Union[Unset, str]):
        party_type_lt (Union[Unset, str]):
        party_type_lte (Union[Unset, str]):
        party_type_range (Union[Unset, list[str]]):
        party_type_regex (Union[Unset, str]):
        party_type_startswith (Union[Unset, str]):
        phone (Union[Unset, str]):
        phone_contains (Union[Unset, str]):
        phone_endswith (Union[Unset, str]):
        phone_gt (Union[Unset, str]):
        phone_gte (Union[Unset, str]):
        phone_icontains (Union[Unset, str]):
        phone_iendswith (Union[Unset, str]):
        phone_iexact (Union[Unset, str]):
        phone_in (Union[Unset, list[str]]):
        phone_iregex (Union[Unset, str]):
        phone_isnull (Union[Unset, bool]):
        phone_istartswith (Union[Unset, str]):
        phone_lt (Union[Unset, str]):
        phone_lte (Union[Unset, str]):
        phone_range (Union[Unset, list[str]]):
        phone_regex (Union[Unset, str]):
        phone_startswith (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        postal_code_contains (Union[Unset, str]):
        postal_code_endswith (Union[Unset, str]):
        postal_code_gt (Union[Unset, str]):
        postal_code_gte (Union[Unset, str]):
        postal_code_icontains (Union[Unset, str]):
        postal_code_iendswith (Union[Unset, str]):
        postal_code_iexact (Union[Unset, str]):
        postal_code_in (Union[Unset, list[str]]):
        postal_code_iregex (Union[Unset, str]):
        postal_code_isnull (Union[Unset, bool]):
        postal_code_istartswith (Union[Unset, str]):
        postal_code_lt (Union[Unset, str]):
        postal_code_lte (Union[Unset, str]):
        postal_code_range (Union[Unset, list[str]]):
        postal_code_regex (Union[Unset, str]):
        postal_code_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPartyReadList
    """

    return sync_detailed(
        client=client,
        administrative_area=administrative_area,
        administrative_area_contains=administrative_area_contains,
        administrative_area_endswith=administrative_area_endswith,
        administrative_area_gt=administrative_area_gt,
        administrative_area_gte=administrative_area_gte,
        administrative_area_icontains=administrative_area_icontains,
        administrative_area_iendswith=administrative_area_iendswith,
        administrative_area_iexact=administrative_area_iexact,
        administrative_area_in=administrative_area_in,
        administrative_area_iregex=administrative_area_iregex,
        administrative_area_isnull=administrative_area_isnull,
        administrative_area_istartswith=administrative_area_istartswith,
        administrative_area_lt=administrative_area_lt,
        administrative_area_lte=administrative_area_lte,
        administrative_area_range=administrative_area_range,
        administrative_area_regex=administrative_area_regex,
        administrative_area_startswith=administrative_area_startswith,
        city=city,
        city_contains=city_contains,
        city_endswith=city_endswith,
        city_gt=city_gt,
        city_gte=city_gte,
        city_icontains=city_icontains,
        city_iendswith=city_iendswith,
        city_iexact=city_iexact,
        city_in=city_in,
        city_iregex=city_iregex,
        city_isnull=city_isnull,
        city_istartswith=city_istartswith,
        city_lt=city_lt,
        city_lte=city_lte,
        city_range=city_range,
        city_regex=city_regex,
        city_startswith=city_startswith,
        country=country,
        country_contains=country_contains,
        country_endswith=country_endswith,
        country_gt=country_gt,
        country_gte=country_gte,
        country_icontains=country_icontains,
        country_iendswith=country_iendswith,
        country_iexact=country_iexact,
        country_in=country_in,
        country_iregex=country_iregex,
        country_isnull=country_isnull,
        country_istartswith=country_istartswith,
        country_lt=country_lt,
        country_lte=country_lte,
        country_range=country_range,
        country_regex=country_regex,
        country_startswith=country_startswith,
        delivery_point=delivery_point,
        delivery_point_contains=delivery_point_contains,
        delivery_point_endswith=delivery_point_endswith,
        delivery_point_gt=delivery_point_gt,
        delivery_point_gte=delivery_point_gte,
        delivery_point_icontains=delivery_point_icontains,
        delivery_point_iendswith=delivery_point_iendswith,
        delivery_point_iexact=delivery_point_iexact,
        delivery_point_in=delivery_point_in,
        delivery_point_iregex=delivery_point_iregex,
        delivery_point_isnull=delivery_point_isnull,
        delivery_point_istartswith=delivery_point_istartswith,
        delivery_point_lt=delivery_point_lt,
        delivery_point_lte=delivery_point_lte,
        delivery_point_range=delivery_point_range,
        delivery_point_regex=delivery_point_regex,
        delivery_point_startswith=delivery_point_startswith,
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
        electronic_email_address=electronic_email_address,
        electronic_email_address_contains=electronic_email_address_contains,
        electronic_email_address_endswith=electronic_email_address_endswith,
        electronic_email_address_gt=electronic_email_address_gt,
        electronic_email_address_gte=electronic_email_address_gte,
        electronic_email_address_icontains=electronic_email_address_icontains,
        electronic_email_address_iendswith=electronic_email_address_iendswith,
        electronic_email_address_iexact=electronic_email_address_iexact,
        electronic_email_address_in=electronic_email_address_in,
        electronic_email_address_iregex=electronic_email_address_iregex,
        electronic_email_address_isnull=electronic_email_address_isnull,
        electronic_email_address_istartswith=electronic_email_address_istartswith,
        electronic_email_address_lt=electronic_email_address_lt,
        electronic_email_address_lte=electronic_email_address_lte,
        electronic_email_address_range=electronic_email_address_range,
        electronic_email_address_regex=electronic_email_address_regex,
        electronic_email_address_startswith=electronic_email_address_startswith,
        first_name=first_name,
        first_name_contains=first_name_contains,
        first_name_endswith=first_name_endswith,
        first_name_gt=first_name_gt,
        first_name_gte=first_name_gte,
        first_name_icontains=first_name_icontains,
        first_name_iendswith=first_name_iendswith,
        first_name_iexact=first_name_iexact,
        first_name_in=first_name_in,
        first_name_iregex=first_name_iregex,
        first_name_isnull=first_name_isnull,
        first_name_istartswith=first_name_istartswith,
        first_name_lt=first_name_lt,
        first_name_lte=first_name_lte,
        first_name_range=first_name_range,
        first_name_regex=first_name_regex,
        first_name_startswith=first_name_startswith,
        last_name=last_name,
        last_name_contains=last_name_contains,
        last_name_endswith=last_name_endswith,
        last_name_gt=last_name_gt,
        last_name_gte=last_name_gte,
        last_name_icontains=last_name_icontains,
        last_name_iendswith=last_name_iendswith,
        last_name_iexact=last_name_iexact,
        last_name_in=last_name_in,
        last_name_iregex=last_name_iregex,
        last_name_isnull=last_name_isnull,
        last_name_istartswith=last_name_istartswith,
        last_name_lt=last_name_lt,
        last_name_lte=last_name_lte,
        last_name_range=last_name_range,
        last_name_regex=last_name_regex,
        last_name_startswith=last_name_startswith,
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
        online_resource=online_resource,
        online_resource_contains=online_resource_contains,
        online_resource_endswith=online_resource_endswith,
        online_resource_gt=online_resource_gt,
        online_resource_gte=online_resource_gte,
        online_resource_icontains=online_resource_icontains,
        online_resource_iendswith=online_resource_iendswith,
        online_resource_iexact=online_resource_iexact,
        online_resource_in=online_resource_in,
        online_resource_iregex=online_resource_iregex,
        online_resource_isnull=online_resource_isnull,
        online_resource_istartswith=online_resource_istartswith,
        online_resource_lt=online_resource_lt,
        online_resource_lte=online_resource_lte,
        online_resource_range=online_resource_range,
        online_resource_regex=online_resource_regex,
        online_resource_startswith=online_resource_startswith,
        ordering=ordering,
        party_type=party_type,
        party_type_contains=party_type_contains,
        party_type_endswith=party_type_endswith,
        party_type_gt=party_type_gt,
        party_type_gte=party_type_gte,
        party_type_icontains=party_type_icontains,
        party_type_iendswith=party_type_iendswith,
        party_type_iexact=party_type_iexact,
        party_type_in=party_type_in,
        party_type_iregex=party_type_iregex,
        party_type_isnull=party_type_isnull,
        party_type_istartswith=party_type_istartswith,
        party_type_lt=party_type_lt,
        party_type_lte=party_type_lte,
        party_type_range=party_type_range,
        party_type_regex=party_type_regex,
        party_type_startswith=party_type_startswith,
        phone=phone,
        phone_contains=phone_contains,
        phone_endswith=phone_endswith,
        phone_gt=phone_gt,
        phone_gte=phone_gte,
        phone_icontains=phone_icontains,
        phone_iendswith=phone_iendswith,
        phone_iexact=phone_iexact,
        phone_in=phone_in,
        phone_iregex=phone_iregex,
        phone_isnull=phone_isnull,
        phone_istartswith=phone_istartswith,
        phone_lt=phone_lt,
        phone_lte=phone_lte,
        phone_range=phone_range,
        phone_regex=phone_regex,
        phone_startswith=phone_startswith,
        postal_code=postal_code,
        postal_code_contains=postal_code_contains,
        postal_code_endswith=postal_code_endswith,
        postal_code_gt=postal_code_gt,
        postal_code_gte=postal_code_gte,
        postal_code_icontains=postal_code_icontains,
        postal_code_iendswith=postal_code_iendswith,
        postal_code_iexact=postal_code_iexact,
        postal_code_in=postal_code_in,
        postal_code_iregex=postal_code_iregex,
        postal_code_isnull=postal_code_isnull,
        postal_code_istartswith=postal_code_istartswith,
        postal_code_lt=postal_code_lt,
        postal_code_lte=postal_code_lte,
        postal_code_range=postal_code_range,
        postal_code_regex=postal_code_regex,
        postal_code_startswith=postal_code_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    administrative_area: Union[Unset, str] = UNSET,
    administrative_area_contains: Union[Unset, str] = UNSET,
    administrative_area_endswith: Union[Unset, str] = UNSET,
    administrative_area_gt: Union[Unset, str] = UNSET,
    administrative_area_gte: Union[Unset, str] = UNSET,
    administrative_area_icontains: Union[Unset, str] = UNSET,
    administrative_area_iendswith: Union[Unset, str] = UNSET,
    administrative_area_iexact: Union[Unset, str] = UNSET,
    administrative_area_in: Union[Unset, list[str]] = UNSET,
    administrative_area_iregex: Union[Unset, str] = UNSET,
    administrative_area_isnull: Union[Unset, bool] = UNSET,
    administrative_area_istartswith: Union[Unset, str] = UNSET,
    administrative_area_lt: Union[Unset, str] = UNSET,
    administrative_area_lte: Union[Unset, str] = UNSET,
    administrative_area_range: Union[Unset, list[str]] = UNSET,
    administrative_area_regex: Union[Unset, str] = UNSET,
    administrative_area_startswith: Union[Unset, str] = UNSET,
    city: Union[Unset, str] = UNSET,
    city_contains: Union[Unset, str] = UNSET,
    city_endswith: Union[Unset, str] = UNSET,
    city_gt: Union[Unset, str] = UNSET,
    city_gte: Union[Unset, str] = UNSET,
    city_icontains: Union[Unset, str] = UNSET,
    city_iendswith: Union[Unset, str] = UNSET,
    city_iexact: Union[Unset, str] = UNSET,
    city_in: Union[Unset, list[str]] = UNSET,
    city_iregex: Union[Unset, str] = UNSET,
    city_isnull: Union[Unset, bool] = UNSET,
    city_istartswith: Union[Unset, str] = UNSET,
    city_lt: Union[Unset, str] = UNSET,
    city_lte: Union[Unset, str] = UNSET,
    city_range: Union[Unset, list[str]] = UNSET,
    city_regex: Union[Unset, str] = UNSET,
    city_startswith: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    country_contains: Union[Unset, str] = UNSET,
    country_endswith: Union[Unset, str] = UNSET,
    country_gt: Union[Unset, str] = UNSET,
    country_gte: Union[Unset, str] = UNSET,
    country_icontains: Union[Unset, str] = UNSET,
    country_iendswith: Union[Unset, str] = UNSET,
    country_iexact: Union[Unset, str] = UNSET,
    country_in: Union[Unset, list[str]] = UNSET,
    country_iregex: Union[Unset, str] = UNSET,
    country_isnull: Union[Unset, bool] = UNSET,
    country_istartswith: Union[Unset, str] = UNSET,
    country_lt: Union[Unset, str] = UNSET,
    country_lte: Union[Unset, str] = UNSET,
    country_range: Union[Unset, list[str]] = UNSET,
    country_regex: Union[Unset, str] = UNSET,
    country_startswith: Union[Unset, str] = UNSET,
    delivery_point: Union[Unset, str] = UNSET,
    delivery_point_contains: Union[Unset, str] = UNSET,
    delivery_point_endswith: Union[Unset, str] = UNSET,
    delivery_point_gt: Union[Unset, str] = UNSET,
    delivery_point_gte: Union[Unset, str] = UNSET,
    delivery_point_icontains: Union[Unset, str] = UNSET,
    delivery_point_iendswith: Union[Unset, str] = UNSET,
    delivery_point_iexact: Union[Unset, str] = UNSET,
    delivery_point_in: Union[Unset, list[str]] = UNSET,
    delivery_point_iregex: Union[Unset, str] = UNSET,
    delivery_point_isnull: Union[Unset, bool] = UNSET,
    delivery_point_istartswith: Union[Unset, str] = UNSET,
    delivery_point_lt: Union[Unset, str] = UNSET,
    delivery_point_lte: Union[Unset, str] = UNSET,
    delivery_point_range: Union[Unset, list[str]] = UNSET,
    delivery_point_regex: Union[Unset, str] = UNSET,
    delivery_point_startswith: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    description_contains: Union[Unset, str] = UNSET,
    description_endswith: Union[Unset, str] = UNSET,
    description_gt: Union[Unset, str] = UNSET,
    description_gte: Union[Unset, str] = UNSET,
    description_icontains: Union[Unset, str] = UNSET,
    description_iendswith: Union[Unset, str] = UNSET,
    description_iexact: Union[Unset, str] = UNSET,
    description_in: Union[Unset, list[str]] = UNSET,
    description_iregex: Union[Unset, str] = UNSET,
    description_isnull: Union[Unset, bool] = UNSET,
    description_istartswith: Union[Unset, str] = UNSET,
    description_lt: Union[Unset, str] = UNSET,
    description_lte: Union[Unset, str] = UNSET,
    description_range: Union[Unset, list[str]] = UNSET,
    description_regex: Union[Unset, str] = UNSET,
    description_startswith: Union[Unset, str] = UNSET,
    electronic_email_address: Union[Unset, str] = UNSET,
    electronic_email_address_contains: Union[Unset, str] = UNSET,
    electronic_email_address_endswith: Union[Unset, str] = UNSET,
    electronic_email_address_gt: Union[Unset, str] = UNSET,
    electronic_email_address_gte: Union[Unset, str] = UNSET,
    electronic_email_address_icontains: Union[Unset, str] = UNSET,
    electronic_email_address_iendswith: Union[Unset, str] = UNSET,
    electronic_email_address_iexact: Union[Unset, str] = UNSET,
    electronic_email_address_in: Union[Unset, list[str]] = UNSET,
    electronic_email_address_iregex: Union[Unset, str] = UNSET,
    electronic_email_address_isnull: Union[Unset, bool] = UNSET,
    electronic_email_address_istartswith: Union[Unset, str] = UNSET,
    electronic_email_address_lt: Union[Unset, str] = UNSET,
    electronic_email_address_lte: Union[Unset, str] = UNSET,
    electronic_email_address_range: Union[Unset, list[str]] = UNSET,
    electronic_email_address_regex: Union[Unset, str] = UNSET,
    electronic_email_address_startswith: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    first_name_contains: Union[Unset, str] = UNSET,
    first_name_endswith: Union[Unset, str] = UNSET,
    first_name_gt: Union[Unset, str] = UNSET,
    first_name_gte: Union[Unset, str] = UNSET,
    first_name_icontains: Union[Unset, str] = UNSET,
    first_name_iendswith: Union[Unset, str] = UNSET,
    first_name_iexact: Union[Unset, str] = UNSET,
    first_name_in: Union[Unset, list[str]] = UNSET,
    first_name_iregex: Union[Unset, str] = UNSET,
    first_name_isnull: Union[Unset, bool] = UNSET,
    first_name_istartswith: Union[Unset, str] = UNSET,
    first_name_lt: Union[Unset, str] = UNSET,
    first_name_lte: Union[Unset, str] = UNSET,
    first_name_range: Union[Unset, list[str]] = UNSET,
    first_name_regex: Union[Unset, str] = UNSET,
    first_name_startswith: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    last_name_contains: Union[Unset, str] = UNSET,
    last_name_endswith: Union[Unset, str] = UNSET,
    last_name_gt: Union[Unset, str] = UNSET,
    last_name_gte: Union[Unset, str] = UNSET,
    last_name_icontains: Union[Unset, str] = UNSET,
    last_name_iendswith: Union[Unset, str] = UNSET,
    last_name_iexact: Union[Unset, str] = UNSET,
    last_name_in: Union[Unset, list[str]] = UNSET,
    last_name_iregex: Union[Unset, str] = UNSET,
    last_name_isnull: Union[Unset, bool] = UNSET,
    last_name_istartswith: Union[Unset, str] = UNSET,
    last_name_lt: Union[Unset, str] = UNSET,
    last_name_lte: Union[Unset, str] = UNSET,
    last_name_range: Union[Unset, list[str]] = UNSET,
    last_name_regex: Union[Unset, str] = UNSET,
    last_name_startswith: Union[Unset, str] = UNSET,
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
    online_resource: Union[Unset, str] = UNSET,
    online_resource_contains: Union[Unset, str] = UNSET,
    online_resource_endswith: Union[Unset, str] = UNSET,
    online_resource_gt: Union[Unset, str] = UNSET,
    online_resource_gte: Union[Unset, str] = UNSET,
    online_resource_icontains: Union[Unset, str] = UNSET,
    online_resource_iendswith: Union[Unset, str] = UNSET,
    online_resource_iexact: Union[Unset, str] = UNSET,
    online_resource_in: Union[Unset, list[str]] = UNSET,
    online_resource_iregex: Union[Unset, str] = UNSET,
    online_resource_isnull: Union[Unset, bool] = UNSET,
    online_resource_istartswith: Union[Unset, str] = UNSET,
    online_resource_lt: Union[Unset, str] = UNSET,
    online_resource_lte: Union[Unset, str] = UNSET,
    online_resource_range: Union[Unset, list[str]] = UNSET,
    online_resource_regex: Union[Unset, str] = UNSET,
    online_resource_startswith: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    party_type: Union[Unset, PartiesListType] = UNSET,
    party_type_contains: Union[Unset, str] = UNSET,
    party_type_endswith: Union[Unset, str] = UNSET,
    party_type_gt: Union[Unset, str] = UNSET,
    party_type_gte: Union[Unset, str] = UNSET,
    party_type_icontains: Union[Unset, str] = UNSET,
    party_type_iendswith: Union[Unset, str] = UNSET,
    party_type_iexact: Union[Unset, str] = UNSET,
    party_type_in: Union[Unset, list[str]] = UNSET,
    party_type_iregex: Union[Unset, str] = UNSET,
    party_type_isnull: Union[Unset, bool] = UNSET,
    party_type_istartswith: Union[Unset, str] = UNSET,
    party_type_lt: Union[Unset, str] = UNSET,
    party_type_lte: Union[Unset, str] = UNSET,
    party_type_range: Union[Unset, list[str]] = UNSET,
    party_type_regex: Union[Unset, str] = UNSET,
    party_type_startswith: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    phone_contains: Union[Unset, str] = UNSET,
    phone_endswith: Union[Unset, str] = UNSET,
    phone_gt: Union[Unset, str] = UNSET,
    phone_gte: Union[Unset, str] = UNSET,
    phone_icontains: Union[Unset, str] = UNSET,
    phone_iendswith: Union[Unset, str] = UNSET,
    phone_iexact: Union[Unset, str] = UNSET,
    phone_in: Union[Unset, list[str]] = UNSET,
    phone_iregex: Union[Unset, str] = UNSET,
    phone_isnull: Union[Unset, bool] = UNSET,
    phone_istartswith: Union[Unset, str] = UNSET,
    phone_lt: Union[Unset, str] = UNSET,
    phone_lte: Union[Unset, str] = UNSET,
    phone_range: Union[Unset, list[str]] = UNSET,
    phone_regex: Union[Unset, str] = UNSET,
    phone_startswith: Union[Unset, str] = UNSET,
    postal_code: Union[Unset, str] = UNSET,
    postal_code_contains: Union[Unset, str] = UNSET,
    postal_code_endswith: Union[Unset, str] = UNSET,
    postal_code_gt: Union[Unset, str] = UNSET,
    postal_code_gte: Union[Unset, str] = UNSET,
    postal_code_icontains: Union[Unset, str] = UNSET,
    postal_code_iendswith: Union[Unset, str] = UNSET,
    postal_code_iexact: Union[Unset, str] = UNSET,
    postal_code_in: Union[Unset, list[str]] = UNSET,
    postal_code_iregex: Union[Unset, str] = UNSET,
    postal_code_isnull: Union[Unset, bool] = UNSET,
    postal_code_istartswith: Union[Unset, str] = UNSET,
    postal_code_lt: Union[Unset, str] = UNSET,
    postal_code_lte: Union[Unset, str] = UNSET,
    postal_code_range: Union[Unset, list[str]] = UNSET,
    postal_code_regex: Union[Unset, str] = UNSET,
    postal_code_startswith: Union[Unset, str] = UNSET,
) -> Response[PaginatedPartyReadList]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        administrative_area (Union[Unset, str]):
        administrative_area_contains (Union[Unset, str]):
        administrative_area_endswith (Union[Unset, str]):
        administrative_area_gt (Union[Unset, str]):
        administrative_area_gte (Union[Unset, str]):
        administrative_area_icontains (Union[Unset, str]):
        administrative_area_iendswith (Union[Unset, str]):
        administrative_area_iexact (Union[Unset, str]):
        administrative_area_in (Union[Unset, list[str]]):
        administrative_area_iregex (Union[Unset, str]):
        administrative_area_isnull (Union[Unset, bool]):
        administrative_area_istartswith (Union[Unset, str]):
        administrative_area_lt (Union[Unset, str]):
        administrative_area_lte (Union[Unset, str]):
        administrative_area_range (Union[Unset, list[str]]):
        administrative_area_regex (Union[Unset, str]):
        administrative_area_startswith (Union[Unset, str]):
        city (Union[Unset, str]):
        city_contains (Union[Unset, str]):
        city_endswith (Union[Unset, str]):
        city_gt (Union[Unset, str]):
        city_gte (Union[Unset, str]):
        city_icontains (Union[Unset, str]):
        city_iendswith (Union[Unset, str]):
        city_iexact (Union[Unset, str]):
        city_in (Union[Unset, list[str]]):
        city_iregex (Union[Unset, str]):
        city_isnull (Union[Unset, bool]):
        city_istartswith (Union[Unset, str]):
        city_lt (Union[Unset, str]):
        city_lte (Union[Unset, str]):
        city_range (Union[Unset, list[str]]):
        city_regex (Union[Unset, str]):
        city_startswith (Union[Unset, str]):
        country (Union[Unset, str]):
        country_contains (Union[Unset, str]):
        country_endswith (Union[Unset, str]):
        country_gt (Union[Unset, str]):
        country_gte (Union[Unset, str]):
        country_icontains (Union[Unset, str]):
        country_iendswith (Union[Unset, str]):
        country_iexact (Union[Unset, str]):
        country_in (Union[Unset, list[str]]):
        country_iregex (Union[Unset, str]):
        country_isnull (Union[Unset, bool]):
        country_istartswith (Union[Unset, str]):
        country_lt (Union[Unset, str]):
        country_lte (Union[Unset, str]):
        country_range (Union[Unset, list[str]]):
        country_regex (Union[Unset, str]):
        country_startswith (Union[Unset, str]):
        delivery_point (Union[Unset, str]):
        delivery_point_contains (Union[Unset, str]):
        delivery_point_endswith (Union[Unset, str]):
        delivery_point_gt (Union[Unset, str]):
        delivery_point_gte (Union[Unset, str]):
        delivery_point_icontains (Union[Unset, str]):
        delivery_point_iendswith (Union[Unset, str]):
        delivery_point_iexact (Union[Unset, str]):
        delivery_point_in (Union[Unset, list[str]]):
        delivery_point_iregex (Union[Unset, str]):
        delivery_point_isnull (Union[Unset, bool]):
        delivery_point_istartswith (Union[Unset, str]):
        delivery_point_lt (Union[Unset, str]):
        delivery_point_lte (Union[Unset, str]):
        delivery_point_range (Union[Unset, list[str]]):
        delivery_point_regex (Union[Unset, str]):
        delivery_point_startswith (Union[Unset, str]):
        description (Union[Unset, str]):
        description_contains (Union[Unset, str]):
        description_endswith (Union[Unset, str]):
        description_gt (Union[Unset, str]):
        description_gte (Union[Unset, str]):
        description_icontains (Union[Unset, str]):
        description_iendswith (Union[Unset, str]):
        description_iexact (Union[Unset, str]):
        description_in (Union[Unset, list[str]]):
        description_iregex (Union[Unset, str]):
        description_isnull (Union[Unset, bool]):
        description_istartswith (Union[Unset, str]):
        description_lt (Union[Unset, str]):
        description_lte (Union[Unset, str]):
        description_range (Union[Unset, list[str]]):
        description_regex (Union[Unset, str]):
        description_startswith (Union[Unset, str]):
        electronic_email_address (Union[Unset, str]):
        electronic_email_address_contains (Union[Unset, str]):
        electronic_email_address_endswith (Union[Unset, str]):
        electronic_email_address_gt (Union[Unset, str]):
        electronic_email_address_gte (Union[Unset, str]):
        electronic_email_address_icontains (Union[Unset, str]):
        electronic_email_address_iendswith (Union[Unset, str]):
        electronic_email_address_iexact (Union[Unset, str]):
        electronic_email_address_in (Union[Unset, list[str]]):
        electronic_email_address_iregex (Union[Unset, str]):
        electronic_email_address_isnull (Union[Unset, bool]):
        electronic_email_address_istartswith (Union[Unset, str]):
        electronic_email_address_lt (Union[Unset, str]):
        electronic_email_address_lte (Union[Unset, str]):
        electronic_email_address_range (Union[Unset, list[str]]):
        electronic_email_address_regex (Union[Unset, str]):
        electronic_email_address_startswith (Union[Unset, str]):
        first_name (Union[Unset, str]):
        first_name_contains (Union[Unset, str]):
        first_name_endswith (Union[Unset, str]):
        first_name_gt (Union[Unset, str]):
        first_name_gte (Union[Unset, str]):
        first_name_icontains (Union[Unset, str]):
        first_name_iendswith (Union[Unset, str]):
        first_name_iexact (Union[Unset, str]):
        first_name_in (Union[Unset, list[str]]):
        first_name_iregex (Union[Unset, str]):
        first_name_isnull (Union[Unset, bool]):
        first_name_istartswith (Union[Unset, str]):
        first_name_lt (Union[Unset, str]):
        first_name_lte (Union[Unset, str]):
        first_name_range (Union[Unset, list[str]]):
        first_name_regex (Union[Unset, str]):
        first_name_startswith (Union[Unset, str]):
        last_name (Union[Unset, str]):
        last_name_contains (Union[Unset, str]):
        last_name_endswith (Union[Unset, str]):
        last_name_gt (Union[Unset, str]):
        last_name_gte (Union[Unset, str]):
        last_name_icontains (Union[Unset, str]):
        last_name_iendswith (Union[Unset, str]):
        last_name_iexact (Union[Unset, str]):
        last_name_in (Union[Unset, list[str]]):
        last_name_iregex (Union[Unset, str]):
        last_name_isnull (Union[Unset, bool]):
        last_name_istartswith (Union[Unset, str]):
        last_name_lt (Union[Unset, str]):
        last_name_lte (Union[Unset, str]):
        last_name_range (Union[Unset, list[str]]):
        last_name_regex (Union[Unset, str]):
        last_name_startswith (Union[Unset, str]):
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
        online_resource (Union[Unset, str]):
        online_resource_contains (Union[Unset, str]):
        online_resource_endswith (Union[Unset, str]):
        online_resource_gt (Union[Unset, str]):
        online_resource_gte (Union[Unset, str]):
        online_resource_icontains (Union[Unset, str]):
        online_resource_iendswith (Union[Unset, str]):
        online_resource_iexact (Union[Unset, str]):
        online_resource_in (Union[Unset, list[str]]):
        online_resource_iregex (Union[Unset, str]):
        online_resource_isnull (Union[Unset, bool]):
        online_resource_istartswith (Union[Unset, str]):
        online_resource_lt (Union[Unset, str]):
        online_resource_lte (Union[Unset, str]):
        online_resource_range (Union[Unset, list[str]]):
        online_resource_regex (Union[Unset, str]):
        online_resource_startswith (Union[Unset, str]):
        ordering (Union[Unset, str]):
        party_type (Union[Unset, PartiesListType]):
        party_type_contains (Union[Unset, str]):
        party_type_endswith (Union[Unset, str]):
        party_type_gt (Union[Unset, str]):
        party_type_gte (Union[Unset, str]):
        party_type_icontains (Union[Unset, str]):
        party_type_iendswith (Union[Unset, str]):
        party_type_iexact (Union[Unset, str]):
        party_type_in (Union[Unset, list[str]]):
        party_type_iregex (Union[Unset, str]):
        party_type_isnull (Union[Unset, bool]):
        party_type_istartswith (Union[Unset, str]):
        party_type_lt (Union[Unset, str]):
        party_type_lte (Union[Unset, str]):
        party_type_range (Union[Unset, list[str]]):
        party_type_regex (Union[Unset, str]):
        party_type_startswith (Union[Unset, str]):
        phone (Union[Unset, str]):
        phone_contains (Union[Unset, str]):
        phone_endswith (Union[Unset, str]):
        phone_gt (Union[Unset, str]):
        phone_gte (Union[Unset, str]):
        phone_icontains (Union[Unset, str]):
        phone_iendswith (Union[Unset, str]):
        phone_iexact (Union[Unset, str]):
        phone_in (Union[Unset, list[str]]):
        phone_iregex (Union[Unset, str]):
        phone_isnull (Union[Unset, bool]):
        phone_istartswith (Union[Unset, str]):
        phone_lt (Union[Unset, str]):
        phone_lte (Union[Unset, str]):
        phone_range (Union[Unset, list[str]]):
        phone_regex (Union[Unset, str]):
        phone_startswith (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        postal_code_contains (Union[Unset, str]):
        postal_code_endswith (Union[Unset, str]):
        postal_code_gt (Union[Unset, str]):
        postal_code_gte (Union[Unset, str]):
        postal_code_icontains (Union[Unset, str]):
        postal_code_iendswith (Union[Unset, str]):
        postal_code_iexact (Union[Unset, str]):
        postal_code_in (Union[Unset, list[str]]):
        postal_code_iregex (Union[Unset, str]):
        postal_code_isnull (Union[Unset, bool]):
        postal_code_istartswith (Union[Unset, str]):
        postal_code_lt (Union[Unset, str]):
        postal_code_lte (Union[Unset, str]):
        postal_code_range (Union[Unset, list[str]]):
        postal_code_regex (Union[Unset, str]):
        postal_code_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedPartyReadList]
    """

    kwargs = _get_kwargs(
        administrative_area=administrative_area,
        administrative_area_contains=administrative_area_contains,
        administrative_area_endswith=administrative_area_endswith,
        administrative_area_gt=administrative_area_gt,
        administrative_area_gte=administrative_area_gte,
        administrative_area_icontains=administrative_area_icontains,
        administrative_area_iendswith=administrative_area_iendswith,
        administrative_area_iexact=administrative_area_iexact,
        administrative_area_in=administrative_area_in,
        administrative_area_iregex=administrative_area_iregex,
        administrative_area_isnull=administrative_area_isnull,
        administrative_area_istartswith=administrative_area_istartswith,
        administrative_area_lt=administrative_area_lt,
        administrative_area_lte=administrative_area_lte,
        administrative_area_range=administrative_area_range,
        administrative_area_regex=administrative_area_regex,
        administrative_area_startswith=administrative_area_startswith,
        city=city,
        city_contains=city_contains,
        city_endswith=city_endswith,
        city_gt=city_gt,
        city_gte=city_gte,
        city_icontains=city_icontains,
        city_iendswith=city_iendswith,
        city_iexact=city_iexact,
        city_in=city_in,
        city_iregex=city_iregex,
        city_isnull=city_isnull,
        city_istartswith=city_istartswith,
        city_lt=city_lt,
        city_lte=city_lte,
        city_range=city_range,
        city_regex=city_regex,
        city_startswith=city_startswith,
        country=country,
        country_contains=country_contains,
        country_endswith=country_endswith,
        country_gt=country_gt,
        country_gte=country_gte,
        country_icontains=country_icontains,
        country_iendswith=country_iendswith,
        country_iexact=country_iexact,
        country_in=country_in,
        country_iregex=country_iregex,
        country_isnull=country_isnull,
        country_istartswith=country_istartswith,
        country_lt=country_lt,
        country_lte=country_lte,
        country_range=country_range,
        country_regex=country_regex,
        country_startswith=country_startswith,
        delivery_point=delivery_point,
        delivery_point_contains=delivery_point_contains,
        delivery_point_endswith=delivery_point_endswith,
        delivery_point_gt=delivery_point_gt,
        delivery_point_gte=delivery_point_gte,
        delivery_point_icontains=delivery_point_icontains,
        delivery_point_iendswith=delivery_point_iendswith,
        delivery_point_iexact=delivery_point_iexact,
        delivery_point_in=delivery_point_in,
        delivery_point_iregex=delivery_point_iregex,
        delivery_point_isnull=delivery_point_isnull,
        delivery_point_istartswith=delivery_point_istartswith,
        delivery_point_lt=delivery_point_lt,
        delivery_point_lte=delivery_point_lte,
        delivery_point_range=delivery_point_range,
        delivery_point_regex=delivery_point_regex,
        delivery_point_startswith=delivery_point_startswith,
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
        electronic_email_address=electronic_email_address,
        electronic_email_address_contains=electronic_email_address_contains,
        electronic_email_address_endswith=electronic_email_address_endswith,
        electronic_email_address_gt=electronic_email_address_gt,
        electronic_email_address_gte=electronic_email_address_gte,
        electronic_email_address_icontains=electronic_email_address_icontains,
        electronic_email_address_iendswith=electronic_email_address_iendswith,
        electronic_email_address_iexact=electronic_email_address_iexact,
        electronic_email_address_in=electronic_email_address_in,
        electronic_email_address_iregex=electronic_email_address_iregex,
        electronic_email_address_isnull=electronic_email_address_isnull,
        electronic_email_address_istartswith=electronic_email_address_istartswith,
        electronic_email_address_lt=electronic_email_address_lt,
        electronic_email_address_lte=electronic_email_address_lte,
        electronic_email_address_range=electronic_email_address_range,
        electronic_email_address_regex=electronic_email_address_regex,
        electronic_email_address_startswith=electronic_email_address_startswith,
        first_name=first_name,
        first_name_contains=first_name_contains,
        first_name_endswith=first_name_endswith,
        first_name_gt=first_name_gt,
        first_name_gte=first_name_gte,
        first_name_icontains=first_name_icontains,
        first_name_iendswith=first_name_iendswith,
        first_name_iexact=first_name_iexact,
        first_name_in=first_name_in,
        first_name_iregex=first_name_iregex,
        first_name_isnull=first_name_isnull,
        first_name_istartswith=first_name_istartswith,
        first_name_lt=first_name_lt,
        first_name_lte=first_name_lte,
        first_name_range=first_name_range,
        first_name_regex=first_name_regex,
        first_name_startswith=first_name_startswith,
        last_name=last_name,
        last_name_contains=last_name_contains,
        last_name_endswith=last_name_endswith,
        last_name_gt=last_name_gt,
        last_name_gte=last_name_gte,
        last_name_icontains=last_name_icontains,
        last_name_iendswith=last_name_iendswith,
        last_name_iexact=last_name_iexact,
        last_name_in=last_name_in,
        last_name_iregex=last_name_iregex,
        last_name_isnull=last_name_isnull,
        last_name_istartswith=last_name_istartswith,
        last_name_lt=last_name_lt,
        last_name_lte=last_name_lte,
        last_name_range=last_name_range,
        last_name_regex=last_name_regex,
        last_name_startswith=last_name_startswith,
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
        online_resource=online_resource,
        online_resource_contains=online_resource_contains,
        online_resource_endswith=online_resource_endswith,
        online_resource_gt=online_resource_gt,
        online_resource_gte=online_resource_gte,
        online_resource_icontains=online_resource_icontains,
        online_resource_iendswith=online_resource_iendswith,
        online_resource_iexact=online_resource_iexact,
        online_resource_in=online_resource_in,
        online_resource_iregex=online_resource_iregex,
        online_resource_isnull=online_resource_isnull,
        online_resource_istartswith=online_resource_istartswith,
        online_resource_lt=online_resource_lt,
        online_resource_lte=online_resource_lte,
        online_resource_range=online_resource_range,
        online_resource_regex=online_resource_regex,
        online_resource_startswith=online_resource_startswith,
        ordering=ordering,
        party_type=party_type,
        party_type_contains=party_type_contains,
        party_type_endswith=party_type_endswith,
        party_type_gt=party_type_gt,
        party_type_gte=party_type_gte,
        party_type_icontains=party_type_icontains,
        party_type_iendswith=party_type_iendswith,
        party_type_iexact=party_type_iexact,
        party_type_in=party_type_in,
        party_type_iregex=party_type_iregex,
        party_type_isnull=party_type_isnull,
        party_type_istartswith=party_type_istartswith,
        party_type_lt=party_type_lt,
        party_type_lte=party_type_lte,
        party_type_range=party_type_range,
        party_type_regex=party_type_regex,
        party_type_startswith=party_type_startswith,
        phone=phone,
        phone_contains=phone_contains,
        phone_endswith=phone_endswith,
        phone_gt=phone_gt,
        phone_gte=phone_gte,
        phone_icontains=phone_icontains,
        phone_iendswith=phone_iendswith,
        phone_iexact=phone_iexact,
        phone_in=phone_in,
        phone_iregex=phone_iregex,
        phone_isnull=phone_isnull,
        phone_istartswith=phone_istartswith,
        phone_lt=phone_lt,
        phone_lte=phone_lte,
        phone_range=phone_range,
        phone_regex=phone_regex,
        phone_startswith=phone_startswith,
        postal_code=postal_code,
        postal_code_contains=postal_code_contains,
        postal_code_endswith=postal_code_endswith,
        postal_code_gt=postal_code_gt,
        postal_code_gte=postal_code_gte,
        postal_code_icontains=postal_code_icontains,
        postal_code_iendswith=postal_code_iendswith,
        postal_code_iexact=postal_code_iexact,
        postal_code_in=postal_code_in,
        postal_code_iregex=postal_code_iregex,
        postal_code_isnull=postal_code_isnull,
        postal_code_istartswith=postal_code_istartswith,
        postal_code_lt=postal_code_lt,
        postal_code_lte=postal_code_lte,
        postal_code_range=postal_code_range,
        postal_code_regex=postal_code_regex,
        postal_code_startswith=postal_code_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    administrative_area: Union[Unset, str] = UNSET,
    administrative_area_contains: Union[Unset, str] = UNSET,
    administrative_area_endswith: Union[Unset, str] = UNSET,
    administrative_area_gt: Union[Unset, str] = UNSET,
    administrative_area_gte: Union[Unset, str] = UNSET,
    administrative_area_icontains: Union[Unset, str] = UNSET,
    administrative_area_iendswith: Union[Unset, str] = UNSET,
    administrative_area_iexact: Union[Unset, str] = UNSET,
    administrative_area_in: Union[Unset, list[str]] = UNSET,
    administrative_area_iregex: Union[Unset, str] = UNSET,
    administrative_area_isnull: Union[Unset, bool] = UNSET,
    administrative_area_istartswith: Union[Unset, str] = UNSET,
    administrative_area_lt: Union[Unset, str] = UNSET,
    administrative_area_lte: Union[Unset, str] = UNSET,
    administrative_area_range: Union[Unset, list[str]] = UNSET,
    administrative_area_regex: Union[Unset, str] = UNSET,
    administrative_area_startswith: Union[Unset, str] = UNSET,
    city: Union[Unset, str] = UNSET,
    city_contains: Union[Unset, str] = UNSET,
    city_endswith: Union[Unset, str] = UNSET,
    city_gt: Union[Unset, str] = UNSET,
    city_gte: Union[Unset, str] = UNSET,
    city_icontains: Union[Unset, str] = UNSET,
    city_iendswith: Union[Unset, str] = UNSET,
    city_iexact: Union[Unset, str] = UNSET,
    city_in: Union[Unset, list[str]] = UNSET,
    city_iregex: Union[Unset, str] = UNSET,
    city_isnull: Union[Unset, bool] = UNSET,
    city_istartswith: Union[Unset, str] = UNSET,
    city_lt: Union[Unset, str] = UNSET,
    city_lte: Union[Unset, str] = UNSET,
    city_range: Union[Unset, list[str]] = UNSET,
    city_regex: Union[Unset, str] = UNSET,
    city_startswith: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    country_contains: Union[Unset, str] = UNSET,
    country_endswith: Union[Unset, str] = UNSET,
    country_gt: Union[Unset, str] = UNSET,
    country_gte: Union[Unset, str] = UNSET,
    country_icontains: Union[Unset, str] = UNSET,
    country_iendswith: Union[Unset, str] = UNSET,
    country_iexact: Union[Unset, str] = UNSET,
    country_in: Union[Unset, list[str]] = UNSET,
    country_iregex: Union[Unset, str] = UNSET,
    country_isnull: Union[Unset, bool] = UNSET,
    country_istartswith: Union[Unset, str] = UNSET,
    country_lt: Union[Unset, str] = UNSET,
    country_lte: Union[Unset, str] = UNSET,
    country_range: Union[Unset, list[str]] = UNSET,
    country_regex: Union[Unset, str] = UNSET,
    country_startswith: Union[Unset, str] = UNSET,
    delivery_point: Union[Unset, str] = UNSET,
    delivery_point_contains: Union[Unset, str] = UNSET,
    delivery_point_endswith: Union[Unset, str] = UNSET,
    delivery_point_gt: Union[Unset, str] = UNSET,
    delivery_point_gte: Union[Unset, str] = UNSET,
    delivery_point_icontains: Union[Unset, str] = UNSET,
    delivery_point_iendswith: Union[Unset, str] = UNSET,
    delivery_point_iexact: Union[Unset, str] = UNSET,
    delivery_point_in: Union[Unset, list[str]] = UNSET,
    delivery_point_iregex: Union[Unset, str] = UNSET,
    delivery_point_isnull: Union[Unset, bool] = UNSET,
    delivery_point_istartswith: Union[Unset, str] = UNSET,
    delivery_point_lt: Union[Unset, str] = UNSET,
    delivery_point_lte: Union[Unset, str] = UNSET,
    delivery_point_range: Union[Unset, list[str]] = UNSET,
    delivery_point_regex: Union[Unset, str] = UNSET,
    delivery_point_startswith: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    description_contains: Union[Unset, str] = UNSET,
    description_endswith: Union[Unset, str] = UNSET,
    description_gt: Union[Unset, str] = UNSET,
    description_gte: Union[Unset, str] = UNSET,
    description_icontains: Union[Unset, str] = UNSET,
    description_iendswith: Union[Unset, str] = UNSET,
    description_iexact: Union[Unset, str] = UNSET,
    description_in: Union[Unset, list[str]] = UNSET,
    description_iregex: Union[Unset, str] = UNSET,
    description_isnull: Union[Unset, bool] = UNSET,
    description_istartswith: Union[Unset, str] = UNSET,
    description_lt: Union[Unset, str] = UNSET,
    description_lte: Union[Unset, str] = UNSET,
    description_range: Union[Unset, list[str]] = UNSET,
    description_regex: Union[Unset, str] = UNSET,
    description_startswith: Union[Unset, str] = UNSET,
    electronic_email_address: Union[Unset, str] = UNSET,
    electronic_email_address_contains: Union[Unset, str] = UNSET,
    electronic_email_address_endswith: Union[Unset, str] = UNSET,
    electronic_email_address_gt: Union[Unset, str] = UNSET,
    electronic_email_address_gte: Union[Unset, str] = UNSET,
    electronic_email_address_icontains: Union[Unset, str] = UNSET,
    electronic_email_address_iendswith: Union[Unset, str] = UNSET,
    electronic_email_address_iexact: Union[Unset, str] = UNSET,
    electronic_email_address_in: Union[Unset, list[str]] = UNSET,
    electronic_email_address_iregex: Union[Unset, str] = UNSET,
    electronic_email_address_isnull: Union[Unset, bool] = UNSET,
    electronic_email_address_istartswith: Union[Unset, str] = UNSET,
    electronic_email_address_lt: Union[Unset, str] = UNSET,
    electronic_email_address_lte: Union[Unset, str] = UNSET,
    electronic_email_address_range: Union[Unset, list[str]] = UNSET,
    electronic_email_address_regex: Union[Unset, str] = UNSET,
    electronic_email_address_startswith: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    first_name_contains: Union[Unset, str] = UNSET,
    first_name_endswith: Union[Unset, str] = UNSET,
    first_name_gt: Union[Unset, str] = UNSET,
    first_name_gte: Union[Unset, str] = UNSET,
    first_name_icontains: Union[Unset, str] = UNSET,
    first_name_iendswith: Union[Unset, str] = UNSET,
    first_name_iexact: Union[Unset, str] = UNSET,
    first_name_in: Union[Unset, list[str]] = UNSET,
    first_name_iregex: Union[Unset, str] = UNSET,
    first_name_isnull: Union[Unset, bool] = UNSET,
    first_name_istartswith: Union[Unset, str] = UNSET,
    first_name_lt: Union[Unset, str] = UNSET,
    first_name_lte: Union[Unset, str] = UNSET,
    first_name_range: Union[Unset, list[str]] = UNSET,
    first_name_regex: Union[Unset, str] = UNSET,
    first_name_startswith: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    last_name_contains: Union[Unset, str] = UNSET,
    last_name_endswith: Union[Unset, str] = UNSET,
    last_name_gt: Union[Unset, str] = UNSET,
    last_name_gte: Union[Unset, str] = UNSET,
    last_name_icontains: Union[Unset, str] = UNSET,
    last_name_iendswith: Union[Unset, str] = UNSET,
    last_name_iexact: Union[Unset, str] = UNSET,
    last_name_in: Union[Unset, list[str]] = UNSET,
    last_name_iregex: Union[Unset, str] = UNSET,
    last_name_isnull: Union[Unset, bool] = UNSET,
    last_name_istartswith: Union[Unset, str] = UNSET,
    last_name_lt: Union[Unset, str] = UNSET,
    last_name_lte: Union[Unset, str] = UNSET,
    last_name_range: Union[Unset, list[str]] = UNSET,
    last_name_regex: Union[Unset, str] = UNSET,
    last_name_startswith: Union[Unset, str] = UNSET,
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
    online_resource: Union[Unset, str] = UNSET,
    online_resource_contains: Union[Unset, str] = UNSET,
    online_resource_endswith: Union[Unset, str] = UNSET,
    online_resource_gt: Union[Unset, str] = UNSET,
    online_resource_gte: Union[Unset, str] = UNSET,
    online_resource_icontains: Union[Unset, str] = UNSET,
    online_resource_iendswith: Union[Unset, str] = UNSET,
    online_resource_iexact: Union[Unset, str] = UNSET,
    online_resource_in: Union[Unset, list[str]] = UNSET,
    online_resource_iregex: Union[Unset, str] = UNSET,
    online_resource_isnull: Union[Unset, bool] = UNSET,
    online_resource_istartswith: Union[Unset, str] = UNSET,
    online_resource_lt: Union[Unset, str] = UNSET,
    online_resource_lte: Union[Unset, str] = UNSET,
    online_resource_range: Union[Unset, list[str]] = UNSET,
    online_resource_regex: Union[Unset, str] = UNSET,
    online_resource_startswith: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    party_type: Union[Unset, PartiesListType] = UNSET,
    party_type_contains: Union[Unset, str] = UNSET,
    party_type_endswith: Union[Unset, str] = UNSET,
    party_type_gt: Union[Unset, str] = UNSET,
    party_type_gte: Union[Unset, str] = UNSET,
    party_type_icontains: Union[Unset, str] = UNSET,
    party_type_iendswith: Union[Unset, str] = UNSET,
    party_type_iexact: Union[Unset, str] = UNSET,
    party_type_in: Union[Unset, list[str]] = UNSET,
    party_type_iregex: Union[Unset, str] = UNSET,
    party_type_isnull: Union[Unset, bool] = UNSET,
    party_type_istartswith: Union[Unset, str] = UNSET,
    party_type_lt: Union[Unset, str] = UNSET,
    party_type_lte: Union[Unset, str] = UNSET,
    party_type_range: Union[Unset, list[str]] = UNSET,
    party_type_regex: Union[Unset, str] = UNSET,
    party_type_startswith: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    phone_contains: Union[Unset, str] = UNSET,
    phone_endswith: Union[Unset, str] = UNSET,
    phone_gt: Union[Unset, str] = UNSET,
    phone_gte: Union[Unset, str] = UNSET,
    phone_icontains: Union[Unset, str] = UNSET,
    phone_iendswith: Union[Unset, str] = UNSET,
    phone_iexact: Union[Unset, str] = UNSET,
    phone_in: Union[Unset, list[str]] = UNSET,
    phone_iregex: Union[Unset, str] = UNSET,
    phone_isnull: Union[Unset, bool] = UNSET,
    phone_istartswith: Union[Unset, str] = UNSET,
    phone_lt: Union[Unset, str] = UNSET,
    phone_lte: Union[Unset, str] = UNSET,
    phone_range: Union[Unset, list[str]] = UNSET,
    phone_regex: Union[Unset, str] = UNSET,
    phone_startswith: Union[Unset, str] = UNSET,
    postal_code: Union[Unset, str] = UNSET,
    postal_code_contains: Union[Unset, str] = UNSET,
    postal_code_endswith: Union[Unset, str] = UNSET,
    postal_code_gt: Union[Unset, str] = UNSET,
    postal_code_gte: Union[Unset, str] = UNSET,
    postal_code_icontains: Union[Unset, str] = UNSET,
    postal_code_iendswith: Union[Unset, str] = UNSET,
    postal_code_iexact: Union[Unset, str] = UNSET,
    postal_code_in: Union[Unset, list[str]] = UNSET,
    postal_code_iregex: Union[Unset, str] = UNSET,
    postal_code_isnull: Union[Unset, bool] = UNSET,
    postal_code_istartswith: Union[Unset, str] = UNSET,
    postal_code_lt: Union[Unset, str] = UNSET,
    postal_code_lte: Union[Unset, str] = UNSET,
    postal_code_range: Union[Unset, list[str]] = UNSET,
    postal_code_regex: Union[Unset, str] = UNSET,
    postal_code_startswith: Union[Unset, str] = UNSET,
) -> Optional[PaginatedPartyReadList]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        administrative_area (Union[Unset, str]):
        administrative_area_contains (Union[Unset, str]):
        administrative_area_endswith (Union[Unset, str]):
        administrative_area_gt (Union[Unset, str]):
        administrative_area_gte (Union[Unset, str]):
        administrative_area_icontains (Union[Unset, str]):
        administrative_area_iendswith (Union[Unset, str]):
        administrative_area_iexact (Union[Unset, str]):
        administrative_area_in (Union[Unset, list[str]]):
        administrative_area_iregex (Union[Unset, str]):
        administrative_area_isnull (Union[Unset, bool]):
        administrative_area_istartswith (Union[Unset, str]):
        administrative_area_lt (Union[Unset, str]):
        administrative_area_lte (Union[Unset, str]):
        administrative_area_range (Union[Unset, list[str]]):
        administrative_area_regex (Union[Unset, str]):
        administrative_area_startswith (Union[Unset, str]):
        city (Union[Unset, str]):
        city_contains (Union[Unset, str]):
        city_endswith (Union[Unset, str]):
        city_gt (Union[Unset, str]):
        city_gte (Union[Unset, str]):
        city_icontains (Union[Unset, str]):
        city_iendswith (Union[Unset, str]):
        city_iexact (Union[Unset, str]):
        city_in (Union[Unset, list[str]]):
        city_iregex (Union[Unset, str]):
        city_isnull (Union[Unset, bool]):
        city_istartswith (Union[Unset, str]):
        city_lt (Union[Unset, str]):
        city_lte (Union[Unset, str]):
        city_range (Union[Unset, list[str]]):
        city_regex (Union[Unset, str]):
        city_startswith (Union[Unset, str]):
        country (Union[Unset, str]):
        country_contains (Union[Unset, str]):
        country_endswith (Union[Unset, str]):
        country_gt (Union[Unset, str]):
        country_gte (Union[Unset, str]):
        country_icontains (Union[Unset, str]):
        country_iendswith (Union[Unset, str]):
        country_iexact (Union[Unset, str]):
        country_in (Union[Unset, list[str]]):
        country_iregex (Union[Unset, str]):
        country_isnull (Union[Unset, bool]):
        country_istartswith (Union[Unset, str]):
        country_lt (Union[Unset, str]):
        country_lte (Union[Unset, str]):
        country_range (Union[Unset, list[str]]):
        country_regex (Union[Unset, str]):
        country_startswith (Union[Unset, str]):
        delivery_point (Union[Unset, str]):
        delivery_point_contains (Union[Unset, str]):
        delivery_point_endswith (Union[Unset, str]):
        delivery_point_gt (Union[Unset, str]):
        delivery_point_gte (Union[Unset, str]):
        delivery_point_icontains (Union[Unset, str]):
        delivery_point_iendswith (Union[Unset, str]):
        delivery_point_iexact (Union[Unset, str]):
        delivery_point_in (Union[Unset, list[str]]):
        delivery_point_iregex (Union[Unset, str]):
        delivery_point_isnull (Union[Unset, bool]):
        delivery_point_istartswith (Union[Unset, str]):
        delivery_point_lt (Union[Unset, str]):
        delivery_point_lte (Union[Unset, str]):
        delivery_point_range (Union[Unset, list[str]]):
        delivery_point_regex (Union[Unset, str]):
        delivery_point_startswith (Union[Unset, str]):
        description (Union[Unset, str]):
        description_contains (Union[Unset, str]):
        description_endswith (Union[Unset, str]):
        description_gt (Union[Unset, str]):
        description_gte (Union[Unset, str]):
        description_icontains (Union[Unset, str]):
        description_iendswith (Union[Unset, str]):
        description_iexact (Union[Unset, str]):
        description_in (Union[Unset, list[str]]):
        description_iregex (Union[Unset, str]):
        description_isnull (Union[Unset, bool]):
        description_istartswith (Union[Unset, str]):
        description_lt (Union[Unset, str]):
        description_lte (Union[Unset, str]):
        description_range (Union[Unset, list[str]]):
        description_regex (Union[Unset, str]):
        description_startswith (Union[Unset, str]):
        electronic_email_address (Union[Unset, str]):
        electronic_email_address_contains (Union[Unset, str]):
        electronic_email_address_endswith (Union[Unset, str]):
        electronic_email_address_gt (Union[Unset, str]):
        electronic_email_address_gte (Union[Unset, str]):
        electronic_email_address_icontains (Union[Unset, str]):
        electronic_email_address_iendswith (Union[Unset, str]):
        electronic_email_address_iexact (Union[Unset, str]):
        electronic_email_address_in (Union[Unset, list[str]]):
        electronic_email_address_iregex (Union[Unset, str]):
        electronic_email_address_isnull (Union[Unset, bool]):
        electronic_email_address_istartswith (Union[Unset, str]):
        electronic_email_address_lt (Union[Unset, str]):
        electronic_email_address_lte (Union[Unset, str]):
        electronic_email_address_range (Union[Unset, list[str]]):
        electronic_email_address_regex (Union[Unset, str]):
        electronic_email_address_startswith (Union[Unset, str]):
        first_name (Union[Unset, str]):
        first_name_contains (Union[Unset, str]):
        first_name_endswith (Union[Unset, str]):
        first_name_gt (Union[Unset, str]):
        first_name_gte (Union[Unset, str]):
        first_name_icontains (Union[Unset, str]):
        first_name_iendswith (Union[Unset, str]):
        first_name_iexact (Union[Unset, str]):
        first_name_in (Union[Unset, list[str]]):
        first_name_iregex (Union[Unset, str]):
        first_name_isnull (Union[Unset, bool]):
        first_name_istartswith (Union[Unset, str]):
        first_name_lt (Union[Unset, str]):
        first_name_lte (Union[Unset, str]):
        first_name_range (Union[Unset, list[str]]):
        first_name_regex (Union[Unset, str]):
        first_name_startswith (Union[Unset, str]):
        last_name (Union[Unset, str]):
        last_name_contains (Union[Unset, str]):
        last_name_endswith (Union[Unset, str]):
        last_name_gt (Union[Unset, str]):
        last_name_gte (Union[Unset, str]):
        last_name_icontains (Union[Unset, str]):
        last_name_iendswith (Union[Unset, str]):
        last_name_iexact (Union[Unset, str]):
        last_name_in (Union[Unset, list[str]]):
        last_name_iregex (Union[Unset, str]):
        last_name_isnull (Union[Unset, bool]):
        last_name_istartswith (Union[Unset, str]):
        last_name_lt (Union[Unset, str]):
        last_name_lte (Union[Unset, str]):
        last_name_range (Union[Unset, list[str]]):
        last_name_regex (Union[Unset, str]):
        last_name_startswith (Union[Unset, str]):
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
        online_resource (Union[Unset, str]):
        online_resource_contains (Union[Unset, str]):
        online_resource_endswith (Union[Unset, str]):
        online_resource_gt (Union[Unset, str]):
        online_resource_gte (Union[Unset, str]):
        online_resource_icontains (Union[Unset, str]):
        online_resource_iendswith (Union[Unset, str]):
        online_resource_iexact (Union[Unset, str]):
        online_resource_in (Union[Unset, list[str]]):
        online_resource_iregex (Union[Unset, str]):
        online_resource_isnull (Union[Unset, bool]):
        online_resource_istartswith (Union[Unset, str]):
        online_resource_lt (Union[Unset, str]):
        online_resource_lte (Union[Unset, str]):
        online_resource_range (Union[Unset, list[str]]):
        online_resource_regex (Union[Unset, str]):
        online_resource_startswith (Union[Unset, str]):
        ordering (Union[Unset, str]):
        party_type (Union[Unset, PartiesListType]):
        party_type_contains (Union[Unset, str]):
        party_type_endswith (Union[Unset, str]):
        party_type_gt (Union[Unset, str]):
        party_type_gte (Union[Unset, str]):
        party_type_icontains (Union[Unset, str]):
        party_type_iendswith (Union[Unset, str]):
        party_type_iexact (Union[Unset, str]):
        party_type_in (Union[Unset, list[str]]):
        party_type_iregex (Union[Unset, str]):
        party_type_isnull (Union[Unset, bool]):
        party_type_istartswith (Union[Unset, str]):
        party_type_lt (Union[Unset, str]):
        party_type_lte (Union[Unset, str]):
        party_type_range (Union[Unset, list[str]]):
        party_type_regex (Union[Unset, str]):
        party_type_startswith (Union[Unset, str]):
        phone (Union[Unset, str]):
        phone_contains (Union[Unset, str]):
        phone_endswith (Union[Unset, str]):
        phone_gt (Union[Unset, str]):
        phone_gte (Union[Unset, str]):
        phone_icontains (Union[Unset, str]):
        phone_iendswith (Union[Unset, str]):
        phone_iexact (Union[Unset, str]):
        phone_in (Union[Unset, list[str]]):
        phone_iregex (Union[Unset, str]):
        phone_isnull (Union[Unset, bool]):
        phone_istartswith (Union[Unset, str]):
        phone_lt (Union[Unset, str]):
        phone_lte (Union[Unset, str]):
        phone_range (Union[Unset, list[str]]):
        phone_regex (Union[Unset, str]):
        phone_startswith (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        postal_code_contains (Union[Unset, str]):
        postal_code_endswith (Union[Unset, str]):
        postal_code_gt (Union[Unset, str]):
        postal_code_gte (Union[Unset, str]):
        postal_code_icontains (Union[Unset, str]):
        postal_code_iendswith (Union[Unset, str]):
        postal_code_iexact (Union[Unset, str]):
        postal_code_in (Union[Unset, list[str]]):
        postal_code_iregex (Union[Unset, str]):
        postal_code_isnull (Union[Unset, bool]):
        postal_code_istartswith (Union[Unset, str]):
        postal_code_lt (Union[Unset, str]):
        postal_code_lte (Union[Unset, str]):
        postal_code_range (Union[Unset, list[str]]):
        postal_code_regex (Union[Unset, str]):
        postal_code_startswith (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedPartyReadList
    """

    return (
        await asyncio_detailed(
            client=client,
            administrative_area=administrative_area,
            administrative_area_contains=administrative_area_contains,
            administrative_area_endswith=administrative_area_endswith,
            administrative_area_gt=administrative_area_gt,
            administrative_area_gte=administrative_area_gte,
            administrative_area_icontains=administrative_area_icontains,
            administrative_area_iendswith=administrative_area_iendswith,
            administrative_area_iexact=administrative_area_iexact,
            administrative_area_in=administrative_area_in,
            administrative_area_iregex=administrative_area_iregex,
            administrative_area_isnull=administrative_area_isnull,
            administrative_area_istartswith=administrative_area_istartswith,
            administrative_area_lt=administrative_area_lt,
            administrative_area_lte=administrative_area_lte,
            administrative_area_range=administrative_area_range,
            administrative_area_regex=administrative_area_regex,
            administrative_area_startswith=administrative_area_startswith,
            city=city,
            city_contains=city_contains,
            city_endswith=city_endswith,
            city_gt=city_gt,
            city_gte=city_gte,
            city_icontains=city_icontains,
            city_iendswith=city_iendswith,
            city_iexact=city_iexact,
            city_in=city_in,
            city_iregex=city_iregex,
            city_isnull=city_isnull,
            city_istartswith=city_istartswith,
            city_lt=city_lt,
            city_lte=city_lte,
            city_range=city_range,
            city_regex=city_regex,
            city_startswith=city_startswith,
            country=country,
            country_contains=country_contains,
            country_endswith=country_endswith,
            country_gt=country_gt,
            country_gte=country_gte,
            country_icontains=country_icontains,
            country_iendswith=country_iendswith,
            country_iexact=country_iexact,
            country_in=country_in,
            country_iregex=country_iregex,
            country_isnull=country_isnull,
            country_istartswith=country_istartswith,
            country_lt=country_lt,
            country_lte=country_lte,
            country_range=country_range,
            country_regex=country_regex,
            country_startswith=country_startswith,
            delivery_point=delivery_point,
            delivery_point_contains=delivery_point_contains,
            delivery_point_endswith=delivery_point_endswith,
            delivery_point_gt=delivery_point_gt,
            delivery_point_gte=delivery_point_gte,
            delivery_point_icontains=delivery_point_icontains,
            delivery_point_iendswith=delivery_point_iendswith,
            delivery_point_iexact=delivery_point_iexact,
            delivery_point_in=delivery_point_in,
            delivery_point_iregex=delivery_point_iregex,
            delivery_point_isnull=delivery_point_isnull,
            delivery_point_istartswith=delivery_point_istartswith,
            delivery_point_lt=delivery_point_lt,
            delivery_point_lte=delivery_point_lte,
            delivery_point_range=delivery_point_range,
            delivery_point_regex=delivery_point_regex,
            delivery_point_startswith=delivery_point_startswith,
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
            electronic_email_address=electronic_email_address,
            electronic_email_address_contains=electronic_email_address_contains,
            electronic_email_address_endswith=electronic_email_address_endswith,
            electronic_email_address_gt=electronic_email_address_gt,
            electronic_email_address_gte=electronic_email_address_gte,
            electronic_email_address_icontains=electronic_email_address_icontains,
            electronic_email_address_iendswith=electronic_email_address_iendswith,
            electronic_email_address_iexact=electronic_email_address_iexact,
            electronic_email_address_in=electronic_email_address_in,
            electronic_email_address_iregex=electronic_email_address_iregex,
            electronic_email_address_isnull=electronic_email_address_isnull,
            electronic_email_address_istartswith=electronic_email_address_istartswith,
            electronic_email_address_lt=electronic_email_address_lt,
            electronic_email_address_lte=electronic_email_address_lte,
            electronic_email_address_range=electronic_email_address_range,
            electronic_email_address_regex=electronic_email_address_regex,
            electronic_email_address_startswith=electronic_email_address_startswith,
            first_name=first_name,
            first_name_contains=first_name_contains,
            first_name_endswith=first_name_endswith,
            first_name_gt=first_name_gt,
            first_name_gte=first_name_gte,
            first_name_icontains=first_name_icontains,
            first_name_iendswith=first_name_iendswith,
            first_name_iexact=first_name_iexact,
            first_name_in=first_name_in,
            first_name_iregex=first_name_iregex,
            first_name_isnull=first_name_isnull,
            first_name_istartswith=first_name_istartswith,
            first_name_lt=first_name_lt,
            first_name_lte=first_name_lte,
            first_name_range=first_name_range,
            first_name_regex=first_name_regex,
            first_name_startswith=first_name_startswith,
            last_name=last_name,
            last_name_contains=last_name_contains,
            last_name_endswith=last_name_endswith,
            last_name_gt=last_name_gt,
            last_name_gte=last_name_gte,
            last_name_icontains=last_name_icontains,
            last_name_iendswith=last_name_iendswith,
            last_name_iexact=last_name_iexact,
            last_name_in=last_name_in,
            last_name_iregex=last_name_iregex,
            last_name_isnull=last_name_isnull,
            last_name_istartswith=last_name_istartswith,
            last_name_lt=last_name_lt,
            last_name_lte=last_name_lte,
            last_name_range=last_name_range,
            last_name_regex=last_name_regex,
            last_name_startswith=last_name_startswith,
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
            online_resource=online_resource,
            online_resource_contains=online_resource_contains,
            online_resource_endswith=online_resource_endswith,
            online_resource_gt=online_resource_gt,
            online_resource_gte=online_resource_gte,
            online_resource_icontains=online_resource_icontains,
            online_resource_iendswith=online_resource_iendswith,
            online_resource_iexact=online_resource_iexact,
            online_resource_in=online_resource_in,
            online_resource_iregex=online_resource_iregex,
            online_resource_isnull=online_resource_isnull,
            online_resource_istartswith=online_resource_istartswith,
            online_resource_lt=online_resource_lt,
            online_resource_lte=online_resource_lte,
            online_resource_range=online_resource_range,
            online_resource_regex=online_resource_regex,
            online_resource_startswith=online_resource_startswith,
            ordering=ordering,
            party_type=party_type,
            party_type_contains=party_type_contains,
            party_type_endswith=party_type_endswith,
            party_type_gt=party_type_gt,
            party_type_gte=party_type_gte,
            party_type_icontains=party_type_icontains,
            party_type_iendswith=party_type_iendswith,
            party_type_iexact=party_type_iexact,
            party_type_in=party_type_in,
            party_type_iregex=party_type_iregex,
            party_type_isnull=party_type_isnull,
            party_type_istartswith=party_type_istartswith,
            party_type_lt=party_type_lt,
            party_type_lte=party_type_lte,
            party_type_range=party_type_range,
            party_type_regex=party_type_regex,
            party_type_startswith=party_type_startswith,
            phone=phone,
            phone_contains=phone_contains,
            phone_endswith=phone_endswith,
            phone_gt=phone_gt,
            phone_gte=phone_gte,
            phone_icontains=phone_icontains,
            phone_iendswith=phone_iendswith,
            phone_iexact=phone_iexact,
            phone_in=phone_in,
            phone_iregex=phone_iregex,
            phone_isnull=phone_isnull,
            phone_istartswith=phone_istartswith,
            phone_lt=phone_lt,
            phone_lte=phone_lte,
            phone_range=phone_range,
            phone_regex=phone_regex,
            phone_startswith=phone_startswith,
            postal_code=postal_code,
            postal_code_contains=postal_code_contains,
            postal_code_endswith=postal_code_endswith,
            postal_code_gt=postal_code_gt,
            postal_code_gte=postal_code_gte,
            postal_code_icontains=postal_code_icontains,
            postal_code_iendswith=postal_code_iendswith,
            postal_code_iexact=postal_code_iexact,
            postal_code_in=postal_code_in,
            postal_code_iregex=postal_code_iregex,
            postal_code_isnull=postal_code_isnull,
            postal_code_istartswith=postal_code_istartswith,
            postal_code_lt=postal_code_lt,
            postal_code_lte=postal_code_lte,
            postal_code_range=postal_code_range,
            postal_code_regex=postal_code_regex,
            postal_code_startswith=postal_code_startswith,
        )
    ).parsed
