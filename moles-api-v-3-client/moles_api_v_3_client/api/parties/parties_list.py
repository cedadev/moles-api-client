from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_party_read_list import PaginatedPartyReadList
from ...models.parties_list_type import PartiesListType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    administrative_area: str | Unset = UNSET,
    administrative_area_contains: str | Unset = UNSET,
    administrative_area_endswith: str | Unset = UNSET,
    administrative_area_gt: str | Unset = UNSET,
    administrative_area_gte: str | Unset = UNSET,
    administrative_area_icontains: str | Unset = UNSET,
    administrative_area_iendswith: str | Unset = UNSET,
    administrative_area_iexact: str | Unset = UNSET,
    administrative_area_in: list[str] | Unset = UNSET,
    administrative_area_iregex: str | Unset = UNSET,
    administrative_area_isnull: bool | Unset = UNSET,
    administrative_area_istartswith: str | Unset = UNSET,
    administrative_area_lt: str | Unset = UNSET,
    administrative_area_lte: str | Unset = UNSET,
    administrative_area_range: list[str] | Unset = UNSET,
    administrative_area_regex: str | Unset = UNSET,
    administrative_area_startswith: str | Unset = UNSET,
    city: str | Unset = UNSET,
    city_contains: str | Unset = UNSET,
    city_endswith: str | Unset = UNSET,
    city_gt: str | Unset = UNSET,
    city_gte: str | Unset = UNSET,
    city_icontains: str | Unset = UNSET,
    city_iendswith: str | Unset = UNSET,
    city_iexact: str | Unset = UNSET,
    city_in: list[str] | Unset = UNSET,
    city_iregex: str | Unset = UNSET,
    city_isnull: bool | Unset = UNSET,
    city_istartswith: str | Unset = UNSET,
    city_lt: str | Unset = UNSET,
    city_lte: str | Unset = UNSET,
    city_range: list[str] | Unset = UNSET,
    city_regex: str | Unset = UNSET,
    city_startswith: str | Unset = UNSET,
    country: str | Unset = UNSET,
    country_contains: str | Unset = UNSET,
    country_endswith: str | Unset = UNSET,
    country_gt: str | Unset = UNSET,
    country_gte: str | Unset = UNSET,
    country_icontains: str | Unset = UNSET,
    country_iendswith: str | Unset = UNSET,
    country_iexact: str | Unset = UNSET,
    country_in: list[str] | Unset = UNSET,
    country_iregex: str | Unset = UNSET,
    country_isnull: bool | Unset = UNSET,
    country_istartswith: str | Unset = UNSET,
    country_lt: str | Unset = UNSET,
    country_lte: str | Unset = UNSET,
    country_range: list[str] | Unset = UNSET,
    country_regex: str | Unset = UNSET,
    country_startswith: str | Unset = UNSET,
    delivery_point: str | Unset = UNSET,
    delivery_point_contains: str | Unset = UNSET,
    delivery_point_endswith: str | Unset = UNSET,
    delivery_point_gt: str | Unset = UNSET,
    delivery_point_gte: str | Unset = UNSET,
    delivery_point_icontains: str | Unset = UNSET,
    delivery_point_iendswith: str | Unset = UNSET,
    delivery_point_iexact: str | Unset = UNSET,
    delivery_point_in: list[str] | Unset = UNSET,
    delivery_point_iregex: str | Unset = UNSET,
    delivery_point_isnull: bool | Unset = UNSET,
    delivery_point_istartswith: str | Unset = UNSET,
    delivery_point_lt: str | Unset = UNSET,
    delivery_point_lte: str | Unset = UNSET,
    delivery_point_range: list[str] | Unset = UNSET,
    delivery_point_regex: str | Unset = UNSET,
    delivery_point_startswith: str | Unset = UNSET,
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
    electronic_email_address: str | Unset = UNSET,
    electronic_email_address_contains: str | Unset = UNSET,
    electronic_email_address_endswith: str | Unset = UNSET,
    electronic_email_address_gt: str | Unset = UNSET,
    electronic_email_address_gte: str | Unset = UNSET,
    electronic_email_address_icontains: str | Unset = UNSET,
    electronic_email_address_iendswith: str | Unset = UNSET,
    electronic_email_address_iexact: str | Unset = UNSET,
    electronic_email_address_in: list[str] | Unset = UNSET,
    electronic_email_address_iregex: str | Unset = UNSET,
    electronic_email_address_isnull: bool | Unset = UNSET,
    electronic_email_address_istartswith: str | Unset = UNSET,
    electronic_email_address_lt: str | Unset = UNSET,
    electronic_email_address_lte: str | Unset = UNSET,
    electronic_email_address_range: list[str] | Unset = UNSET,
    electronic_email_address_regex: str | Unset = UNSET,
    electronic_email_address_startswith: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    first_name_contains: str | Unset = UNSET,
    first_name_endswith: str | Unset = UNSET,
    first_name_gt: str | Unset = UNSET,
    first_name_gte: str | Unset = UNSET,
    first_name_icontains: str | Unset = UNSET,
    first_name_iendswith: str | Unset = UNSET,
    first_name_iexact: str | Unset = UNSET,
    first_name_in: list[str] | Unset = UNSET,
    first_name_iregex: str | Unset = UNSET,
    first_name_isnull: bool | Unset = UNSET,
    first_name_istartswith: str | Unset = UNSET,
    first_name_lt: str | Unset = UNSET,
    first_name_lte: str | Unset = UNSET,
    first_name_range: list[str] | Unset = UNSET,
    first_name_regex: str | Unset = UNSET,
    first_name_startswith: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    last_name_contains: str | Unset = UNSET,
    last_name_endswith: str | Unset = UNSET,
    last_name_gt: str | Unset = UNSET,
    last_name_gte: str | Unset = UNSET,
    last_name_icontains: str | Unset = UNSET,
    last_name_iendswith: str | Unset = UNSET,
    last_name_iexact: str | Unset = UNSET,
    last_name_in: list[str] | Unset = UNSET,
    last_name_iregex: str | Unset = UNSET,
    last_name_isnull: bool | Unset = UNSET,
    last_name_istartswith: str | Unset = UNSET,
    last_name_lt: str | Unset = UNSET,
    last_name_lte: str | Unset = UNSET,
    last_name_range: list[str] | Unset = UNSET,
    last_name_regex: str | Unset = UNSET,
    last_name_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    online_resource: str | Unset = UNSET,
    online_resource_contains: str | Unset = UNSET,
    online_resource_endswith: str | Unset = UNSET,
    online_resource_gt: str | Unset = UNSET,
    online_resource_gte: str | Unset = UNSET,
    online_resource_icontains: str | Unset = UNSET,
    online_resource_iendswith: str | Unset = UNSET,
    online_resource_iexact: str | Unset = UNSET,
    online_resource_in: list[str] | Unset = UNSET,
    online_resource_iregex: str | Unset = UNSET,
    online_resource_isnull: bool | Unset = UNSET,
    online_resource_istartswith: str | Unset = UNSET,
    online_resource_lt: str | Unset = UNSET,
    online_resource_lte: str | Unset = UNSET,
    online_resource_range: list[str] | Unset = UNSET,
    online_resource_regex: str | Unset = UNSET,
    online_resource_startswith: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    party_type: PartiesListType | Unset = UNSET,
    party_type_contains: str | Unset = UNSET,
    party_type_endswith: str | Unset = UNSET,
    party_type_gt: str | Unset = UNSET,
    party_type_gte: str | Unset = UNSET,
    party_type_icontains: str | Unset = UNSET,
    party_type_iendswith: str | Unset = UNSET,
    party_type_iexact: str | Unset = UNSET,
    party_type_in: list[str] | Unset = UNSET,
    party_type_iregex: str | Unset = UNSET,
    party_type_isnull: bool | Unset = UNSET,
    party_type_istartswith: str | Unset = UNSET,
    party_type_lt: str | Unset = UNSET,
    party_type_lte: str | Unset = UNSET,
    party_type_range: list[str] | Unset = UNSET,
    party_type_regex: str | Unset = UNSET,
    party_type_startswith: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    phone_contains: str | Unset = UNSET,
    phone_endswith: str | Unset = UNSET,
    phone_gt: str | Unset = UNSET,
    phone_gte: str | Unset = UNSET,
    phone_icontains: str | Unset = UNSET,
    phone_iendswith: str | Unset = UNSET,
    phone_iexact: str | Unset = UNSET,
    phone_in: list[str] | Unset = UNSET,
    phone_iregex: str | Unset = UNSET,
    phone_isnull: bool | Unset = UNSET,
    phone_istartswith: str | Unset = UNSET,
    phone_lt: str | Unset = UNSET,
    phone_lte: str | Unset = UNSET,
    phone_range: list[str] | Unset = UNSET,
    phone_regex: str | Unset = UNSET,
    phone_startswith: str | Unset = UNSET,
    postal_code: str | Unset = UNSET,
    postal_code_contains: str | Unset = UNSET,
    postal_code_endswith: str | Unset = UNSET,
    postal_code_gt: str | Unset = UNSET,
    postal_code_gte: str | Unset = UNSET,
    postal_code_icontains: str | Unset = UNSET,
    postal_code_iendswith: str | Unset = UNSET,
    postal_code_iexact: str | Unset = UNSET,
    postal_code_in: list[str] | Unset = UNSET,
    postal_code_iregex: str | Unset = UNSET,
    postal_code_isnull: bool | Unset = UNSET,
    postal_code_istartswith: str | Unset = UNSET,
    postal_code_lt: str | Unset = UNSET,
    postal_code_lte: str | Unset = UNSET,
    postal_code_range: list[str] | Unset = UNSET,
    postal_code_regex: str | Unset = UNSET,
    postal_code_startswith: str | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
    reviewnote: list[int] | Unset = UNSET,
    reviewnote_in: list[int] | Unset = UNSET,
    reviewnote_isnull: bool | Unset = UNSET,
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

    json_administrative_area_in: list[str] | Unset = UNSET
    if not isinstance(administrative_area_in, Unset):
        json_administrative_area_in = ",".join(map(str, administrative_area_in))

    params["administrativeArea__in"] = json_administrative_area_in

    params["administrativeArea__iregex"] = administrative_area_iregex

    params["administrativeArea__isnull"] = administrative_area_isnull

    params["administrativeArea__istartswith"] = administrative_area_istartswith

    params["administrativeArea__lt"] = administrative_area_lt

    params["administrativeArea__lte"] = administrative_area_lte

    json_administrative_area_range: list[str] | Unset = UNSET
    if not isinstance(administrative_area_range, Unset):
        json_administrative_area_range = ",".join(map(str, administrative_area_range))

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

    json_city_in: list[str] | Unset = UNSET
    if not isinstance(city_in, Unset):
        json_city_in = ",".join(map(str, city_in))

    params["city__in"] = json_city_in

    params["city__iregex"] = city_iregex

    params["city__isnull"] = city_isnull

    params["city__istartswith"] = city_istartswith

    params["city__lt"] = city_lt

    params["city__lte"] = city_lte

    json_city_range: list[str] | Unset = UNSET
    if not isinstance(city_range, Unset):
        json_city_range = ",".join(map(str, city_range))

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

    json_country_in: list[str] | Unset = UNSET
    if not isinstance(country_in, Unset):
        json_country_in = ",".join(map(str, country_in))

    params["country__in"] = json_country_in

    params["country__iregex"] = country_iregex

    params["country__isnull"] = country_isnull

    params["country__istartswith"] = country_istartswith

    params["country__lt"] = country_lt

    params["country__lte"] = country_lte

    json_country_range: list[str] | Unset = UNSET
    if not isinstance(country_range, Unset):
        json_country_range = ",".join(map(str, country_range))

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

    json_delivery_point_in: list[str] | Unset = UNSET
    if not isinstance(delivery_point_in, Unset):
        json_delivery_point_in = ",".join(map(str, delivery_point_in))

    params["deliveryPoint__in"] = json_delivery_point_in

    params["deliveryPoint__iregex"] = delivery_point_iregex

    params["deliveryPoint__isnull"] = delivery_point_isnull

    params["deliveryPoint__istartswith"] = delivery_point_istartswith

    params["deliveryPoint__lt"] = delivery_point_lt

    params["deliveryPoint__lte"] = delivery_point_lte

    json_delivery_point_range: list[str] | Unset = UNSET
    if not isinstance(delivery_point_range, Unset):
        json_delivery_point_range = ",".join(map(str, delivery_point_range))

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

    json_description_in: list[str] | Unset = UNSET
    if not isinstance(description_in, Unset):
        json_description_in = ",".join(map(str, description_in))

    params["description__in"] = json_description_in

    params["description__iregex"] = description_iregex

    params["description__isnull"] = description_isnull

    params["description__istartswith"] = description_istartswith

    params["description__lt"] = description_lt

    params["description__lte"] = description_lte

    json_description_range: list[str] | Unset = UNSET
    if not isinstance(description_range, Unset):
        json_description_range = ",".join(map(str, description_range))

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

    json_electronic_email_address_in: list[str] | Unset = UNSET
    if not isinstance(electronic_email_address_in, Unset):
        json_electronic_email_address_in = ",".join(map(str, electronic_email_address_in))

    params["electronicEmailAddress__in"] = json_electronic_email_address_in

    params["electronicEmailAddress__iregex"] = electronic_email_address_iregex

    params["electronicEmailAddress__isnull"] = electronic_email_address_isnull

    params["electronicEmailAddress__istartswith"] = electronic_email_address_istartswith

    params["electronicEmailAddress__lt"] = electronic_email_address_lt

    params["electronicEmailAddress__lte"] = electronic_email_address_lte

    json_electronic_email_address_range: list[str] | Unset = UNSET
    if not isinstance(electronic_email_address_range, Unset):
        json_electronic_email_address_range = ",".join(map(str, electronic_email_address_range))

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

    json_first_name_in: list[str] | Unset = UNSET
    if not isinstance(first_name_in, Unset):
        json_first_name_in = ",".join(map(str, first_name_in))

    params["firstName__in"] = json_first_name_in

    params["firstName__iregex"] = first_name_iregex

    params["firstName__isnull"] = first_name_isnull

    params["firstName__istartswith"] = first_name_istartswith

    params["firstName__lt"] = first_name_lt

    params["firstName__lte"] = first_name_lte

    json_first_name_range: list[str] | Unset = UNSET
    if not isinstance(first_name_range, Unset):
        json_first_name_range = ",".join(map(str, first_name_range))

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

    json_last_name_in: list[str] | Unset = UNSET
    if not isinstance(last_name_in, Unset):
        json_last_name_in = ",".join(map(str, last_name_in))

    params["lastName__in"] = json_last_name_in

    params["lastName__iregex"] = last_name_iregex

    params["lastName__isnull"] = last_name_isnull

    params["lastName__istartswith"] = last_name_istartswith

    params["lastName__lt"] = last_name_lt

    params["lastName__lte"] = last_name_lte

    json_last_name_range: list[str] | Unset = UNSET
    if not isinstance(last_name_range, Unset):
        json_last_name_range = ",".join(map(str, last_name_range))

    params["lastName__range"] = json_last_name_range

    params["lastName__regex"] = last_name_regex

    params["lastName__startswith"] = last_name_startswith

    params["limit"] = limit

    json_note: list[int] | Unset = UNSET
    if not isinstance(note, Unset):
        json_note = ",".join(map(str, note))

    params["note"] = json_note

    json_note_in: list[int] | Unset = UNSET
    if not isinstance(note_in, Unset):
        json_note_in = ",".join(map(str, note_in))

    params["note__in"] = json_note_in

    params["note__isnull"] = note_isnull

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

    params["onlineResource"] = online_resource

    params["onlineResource__contains"] = online_resource_contains

    params["onlineResource__endswith"] = online_resource_endswith

    params["onlineResource__gt"] = online_resource_gt

    params["onlineResource__gte"] = online_resource_gte

    params["onlineResource__icontains"] = online_resource_icontains

    params["onlineResource__iendswith"] = online_resource_iendswith

    params["onlineResource__iexact"] = online_resource_iexact

    json_online_resource_in: list[str] | Unset = UNSET
    if not isinstance(online_resource_in, Unset):
        json_online_resource_in = ",".join(map(str, online_resource_in))

    params["onlineResource__in"] = json_online_resource_in

    params["onlineResource__iregex"] = online_resource_iregex

    params["onlineResource__isnull"] = online_resource_isnull

    params["onlineResource__istartswith"] = online_resource_istartswith

    params["onlineResource__lt"] = online_resource_lt

    params["onlineResource__lte"] = online_resource_lte

    json_online_resource_range: list[str] | Unset = UNSET
    if not isinstance(online_resource_range, Unset):
        json_online_resource_range = ",".join(map(str, online_resource_range))

    params["onlineResource__range"] = json_online_resource_range

    params["onlineResource__regex"] = online_resource_regex

    params["onlineResource__startswith"] = online_resource_startswith

    params["ordering"] = ordering

    json_party_type: str | Unset = UNSET
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

    json_party_type_in: list[str] | Unset = UNSET
    if not isinstance(party_type_in, Unset):
        json_party_type_in = ",".join(map(str, party_type_in))

    params["partyType__in"] = json_party_type_in

    params["partyType__iregex"] = party_type_iregex

    params["partyType__isnull"] = party_type_isnull

    params["partyType__istartswith"] = party_type_istartswith

    params["partyType__lt"] = party_type_lt

    params["partyType__lte"] = party_type_lte

    json_party_type_range: list[str] | Unset = UNSET
    if not isinstance(party_type_range, Unset):
        json_party_type_range = ",".join(map(str, party_type_range))

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

    json_phone_in: list[str] | Unset = UNSET
    if not isinstance(phone_in, Unset):
        json_phone_in = ",".join(map(str, phone_in))

    params["phone__in"] = json_phone_in

    params["phone__iregex"] = phone_iregex

    params["phone__isnull"] = phone_isnull

    params["phone__istartswith"] = phone_istartswith

    params["phone__lt"] = phone_lt

    params["phone__lte"] = phone_lte

    json_phone_range: list[str] | Unset = UNSET
    if not isinstance(phone_range, Unset):
        json_phone_range = ",".join(map(str, phone_range))

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

    json_postal_code_in: list[str] | Unset = UNSET
    if not isinstance(postal_code_in, Unset):
        json_postal_code_in = ",".join(map(str, postal_code_in))

    params["postalCode__in"] = json_postal_code_in

    params["postalCode__iregex"] = postal_code_iregex

    params["postalCode__isnull"] = postal_code_isnull

    params["postalCode__istartswith"] = postal_code_istartswith

    params["postalCode__lt"] = postal_code_lt

    params["postalCode__lte"] = postal_code_lte

    json_postal_code_range: list[str] | Unset = UNSET
    if not isinstance(postal_code_range, Unset):
        json_postal_code_range = ",".join(map(str, postal_code_range))

    params["postalCode__range"] = json_postal_code_range

    params["postalCode__regex"] = postal_code_regex

    params["postalCode__startswith"] = postal_code_startswith

    json_responsiblepartyinfo: list[int] | Unset = UNSET
    if not isinstance(responsiblepartyinfo, Unset):
        json_responsiblepartyinfo = ",".join(map(str, responsiblepartyinfo))

    params["responsiblepartyinfo"] = json_responsiblepartyinfo

    json_responsiblepartyinfo_in: list[int] | Unset = UNSET
    if not isinstance(responsiblepartyinfo_in, Unset):
        json_responsiblepartyinfo_in = ",".join(map(str, responsiblepartyinfo_in))

    params["responsiblepartyinfo__in"] = json_responsiblepartyinfo_in

    params["responsiblepartyinfo__isnull"] = responsiblepartyinfo_isnull

    json_review: list[int] | Unset = UNSET
    if not isinstance(review, Unset):
        json_review = ",".join(map(str, review))

    params["review"] = json_review

    json_review_in: list[int] | Unset = UNSET
    if not isinstance(review_in, Unset):
        json_review_in = ",".join(map(str, review_in))

    params["review__in"] = json_review_in

    params["review__isnull"] = review_isnull

    json_reviewnote: list[int] | Unset = UNSET
    if not isinstance(reviewnote, Unset):
        json_reviewnote = ",".join(map(str, reviewnote))

    params["reviewnote"] = json_reviewnote

    json_reviewnote_in: list[int] | Unset = UNSET
    if not isinstance(reviewnote_in, Unset):
        json_reviewnote_in = ",".join(map(str, reviewnote_in))

    params["reviewnote__in"] = json_reviewnote_in

    params["reviewnote__isnull"] = reviewnote_isnull

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v3/parties/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PaginatedPartyReadList | None:
    if response.status_code == 200:
        response_200 = PaginatedPartyReadList.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
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
    administrative_area: str | Unset = UNSET,
    administrative_area_contains: str | Unset = UNSET,
    administrative_area_endswith: str | Unset = UNSET,
    administrative_area_gt: str | Unset = UNSET,
    administrative_area_gte: str | Unset = UNSET,
    administrative_area_icontains: str | Unset = UNSET,
    administrative_area_iendswith: str | Unset = UNSET,
    administrative_area_iexact: str | Unset = UNSET,
    administrative_area_in: list[str] | Unset = UNSET,
    administrative_area_iregex: str | Unset = UNSET,
    administrative_area_isnull: bool | Unset = UNSET,
    administrative_area_istartswith: str | Unset = UNSET,
    administrative_area_lt: str | Unset = UNSET,
    administrative_area_lte: str | Unset = UNSET,
    administrative_area_range: list[str] | Unset = UNSET,
    administrative_area_regex: str | Unset = UNSET,
    administrative_area_startswith: str | Unset = UNSET,
    city: str | Unset = UNSET,
    city_contains: str | Unset = UNSET,
    city_endswith: str | Unset = UNSET,
    city_gt: str | Unset = UNSET,
    city_gte: str | Unset = UNSET,
    city_icontains: str | Unset = UNSET,
    city_iendswith: str | Unset = UNSET,
    city_iexact: str | Unset = UNSET,
    city_in: list[str] | Unset = UNSET,
    city_iregex: str | Unset = UNSET,
    city_isnull: bool | Unset = UNSET,
    city_istartswith: str | Unset = UNSET,
    city_lt: str | Unset = UNSET,
    city_lte: str | Unset = UNSET,
    city_range: list[str] | Unset = UNSET,
    city_regex: str | Unset = UNSET,
    city_startswith: str | Unset = UNSET,
    country: str | Unset = UNSET,
    country_contains: str | Unset = UNSET,
    country_endswith: str | Unset = UNSET,
    country_gt: str | Unset = UNSET,
    country_gte: str | Unset = UNSET,
    country_icontains: str | Unset = UNSET,
    country_iendswith: str | Unset = UNSET,
    country_iexact: str | Unset = UNSET,
    country_in: list[str] | Unset = UNSET,
    country_iregex: str | Unset = UNSET,
    country_isnull: bool | Unset = UNSET,
    country_istartswith: str | Unset = UNSET,
    country_lt: str | Unset = UNSET,
    country_lte: str | Unset = UNSET,
    country_range: list[str] | Unset = UNSET,
    country_regex: str | Unset = UNSET,
    country_startswith: str | Unset = UNSET,
    delivery_point: str | Unset = UNSET,
    delivery_point_contains: str | Unset = UNSET,
    delivery_point_endswith: str | Unset = UNSET,
    delivery_point_gt: str | Unset = UNSET,
    delivery_point_gte: str | Unset = UNSET,
    delivery_point_icontains: str | Unset = UNSET,
    delivery_point_iendswith: str | Unset = UNSET,
    delivery_point_iexact: str | Unset = UNSET,
    delivery_point_in: list[str] | Unset = UNSET,
    delivery_point_iregex: str | Unset = UNSET,
    delivery_point_isnull: bool | Unset = UNSET,
    delivery_point_istartswith: str | Unset = UNSET,
    delivery_point_lt: str | Unset = UNSET,
    delivery_point_lte: str | Unset = UNSET,
    delivery_point_range: list[str] | Unset = UNSET,
    delivery_point_regex: str | Unset = UNSET,
    delivery_point_startswith: str | Unset = UNSET,
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
    electronic_email_address: str | Unset = UNSET,
    electronic_email_address_contains: str | Unset = UNSET,
    electronic_email_address_endswith: str | Unset = UNSET,
    electronic_email_address_gt: str | Unset = UNSET,
    electronic_email_address_gte: str | Unset = UNSET,
    electronic_email_address_icontains: str | Unset = UNSET,
    electronic_email_address_iendswith: str | Unset = UNSET,
    electronic_email_address_iexact: str | Unset = UNSET,
    electronic_email_address_in: list[str] | Unset = UNSET,
    electronic_email_address_iregex: str | Unset = UNSET,
    electronic_email_address_isnull: bool | Unset = UNSET,
    electronic_email_address_istartswith: str | Unset = UNSET,
    electronic_email_address_lt: str | Unset = UNSET,
    electronic_email_address_lte: str | Unset = UNSET,
    electronic_email_address_range: list[str] | Unset = UNSET,
    electronic_email_address_regex: str | Unset = UNSET,
    electronic_email_address_startswith: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    first_name_contains: str | Unset = UNSET,
    first_name_endswith: str | Unset = UNSET,
    first_name_gt: str | Unset = UNSET,
    first_name_gte: str | Unset = UNSET,
    first_name_icontains: str | Unset = UNSET,
    first_name_iendswith: str | Unset = UNSET,
    first_name_iexact: str | Unset = UNSET,
    first_name_in: list[str] | Unset = UNSET,
    first_name_iregex: str | Unset = UNSET,
    first_name_isnull: bool | Unset = UNSET,
    first_name_istartswith: str | Unset = UNSET,
    first_name_lt: str | Unset = UNSET,
    first_name_lte: str | Unset = UNSET,
    first_name_range: list[str] | Unset = UNSET,
    first_name_regex: str | Unset = UNSET,
    first_name_startswith: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    last_name_contains: str | Unset = UNSET,
    last_name_endswith: str | Unset = UNSET,
    last_name_gt: str | Unset = UNSET,
    last_name_gte: str | Unset = UNSET,
    last_name_icontains: str | Unset = UNSET,
    last_name_iendswith: str | Unset = UNSET,
    last_name_iexact: str | Unset = UNSET,
    last_name_in: list[str] | Unset = UNSET,
    last_name_iregex: str | Unset = UNSET,
    last_name_isnull: bool | Unset = UNSET,
    last_name_istartswith: str | Unset = UNSET,
    last_name_lt: str | Unset = UNSET,
    last_name_lte: str | Unset = UNSET,
    last_name_range: list[str] | Unset = UNSET,
    last_name_regex: str | Unset = UNSET,
    last_name_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    online_resource: str | Unset = UNSET,
    online_resource_contains: str | Unset = UNSET,
    online_resource_endswith: str | Unset = UNSET,
    online_resource_gt: str | Unset = UNSET,
    online_resource_gte: str | Unset = UNSET,
    online_resource_icontains: str | Unset = UNSET,
    online_resource_iendswith: str | Unset = UNSET,
    online_resource_iexact: str | Unset = UNSET,
    online_resource_in: list[str] | Unset = UNSET,
    online_resource_iregex: str | Unset = UNSET,
    online_resource_isnull: bool | Unset = UNSET,
    online_resource_istartswith: str | Unset = UNSET,
    online_resource_lt: str | Unset = UNSET,
    online_resource_lte: str | Unset = UNSET,
    online_resource_range: list[str] | Unset = UNSET,
    online_resource_regex: str | Unset = UNSET,
    online_resource_startswith: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    party_type: PartiesListType | Unset = UNSET,
    party_type_contains: str | Unset = UNSET,
    party_type_endswith: str | Unset = UNSET,
    party_type_gt: str | Unset = UNSET,
    party_type_gte: str | Unset = UNSET,
    party_type_icontains: str | Unset = UNSET,
    party_type_iendswith: str | Unset = UNSET,
    party_type_iexact: str | Unset = UNSET,
    party_type_in: list[str] | Unset = UNSET,
    party_type_iregex: str | Unset = UNSET,
    party_type_isnull: bool | Unset = UNSET,
    party_type_istartswith: str | Unset = UNSET,
    party_type_lt: str | Unset = UNSET,
    party_type_lte: str | Unset = UNSET,
    party_type_range: list[str] | Unset = UNSET,
    party_type_regex: str | Unset = UNSET,
    party_type_startswith: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    phone_contains: str | Unset = UNSET,
    phone_endswith: str | Unset = UNSET,
    phone_gt: str | Unset = UNSET,
    phone_gte: str | Unset = UNSET,
    phone_icontains: str | Unset = UNSET,
    phone_iendswith: str | Unset = UNSET,
    phone_iexact: str | Unset = UNSET,
    phone_in: list[str] | Unset = UNSET,
    phone_iregex: str | Unset = UNSET,
    phone_isnull: bool | Unset = UNSET,
    phone_istartswith: str | Unset = UNSET,
    phone_lt: str | Unset = UNSET,
    phone_lte: str | Unset = UNSET,
    phone_range: list[str] | Unset = UNSET,
    phone_regex: str | Unset = UNSET,
    phone_startswith: str | Unset = UNSET,
    postal_code: str | Unset = UNSET,
    postal_code_contains: str | Unset = UNSET,
    postal_code_endswith: str | Unset = UNSET,
    postal_code_gt: str | Unset = UNSET,
    postal_code_gte: str | Unset = UNSET,
    postal_code_icontains: str | Unset = UNSET,
    postal_code_iendswith: str | Unset = UNSET,
    postal_code_iexact: str | Unset = UNSET,
    postal_code_in: list[str] | Unset = UNSET,
    postal_code_iregex: str | Unset = UNSET,
    postal_code_isnull: bool | Unset = UNSET,
    postal_code_istartswith: str | Unset = UNSET,
    postal_code_lt: str | Unset = UNSET,
    postal_code_lte: str | Unset = UNSET,
    postal_code_range: list[str] | Unset = UNSET,
    postal_code_regex: str | Unset = UNSET,
    postal_code_startswith: str | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
    reviewnote: list[int] | Unset = UNSET,
    reviewnote_in: list[int] | Unset = UNSET,
    reviewnote_isnull: bool | Unset = UNSET,
) -> Response[PaginatedPartyReadList]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        administrative_area (str | Unset):
        administrative_area_contains (str | Unset):
        administrative_area_endswith (str | Unset):
        administrative_area_gt (str | Unset):
        administrative_area_gte (str | Unset):
        administrative_area_icontains (str | Unset):
        administrative_area_iendswith (str | Unset):
        administrative_area_iexact (str | Unset):
        administrative_area_in (list[str] | Unset):
        administrative_area_iregex (str | Unset):
        administrative_area_isnull (bool | Unset):
        administrative_area_istartswith (str | Unset):
        administrative_area_lt (str | Unset):
        administrative_area_lte (str | Unset):
        administrative_area_range (list[str] | Unset):
        administrative_area_regex (str | Unset):
        administrative_area_startswith (str | Unset):
        city (str | Unset):
        city_contains (str | Unset):
        city_endswith (str | Unset):
        city_gt (str | Unset):
        city_gte (str | Unset):
        city_icontains (str | Unset):
        city_iendswith (str | Unset):
        city_iexact (str | Unset):
        city_in (list[str] | Unset):
        city_iregex (str | Unset):
        city_isnull (bool | Unset):
        city_istartswith (str | Unset):
        city_lt (str | Unset):
        city_lte (str | Unset):
        city_range (list[str] | Unset):
        city_regex (str | Unset):
        city_startswith (str | Unset):
        country (str | Unset):
        country_contains (str | Unset):
        country_endswith (str | Unset):
        country_gt (str | Unset):
        country_gte (str | Unset):
        country_icontains (str | Unset):
        country_iendswith (str | Unset):
        country_iexact (str | Unset):
        country_in (list[str] | Unset):
        country_iregex (str | Unset):
        country_isnull (bool | Unset):
        country_istartswith (str | Unset):
        country_lt (str | Unset):
        country_lte (str | Unset):
        country_range (list[str] | Unset):
        country_regex (str | Unset):
        country_startswith (str | Unset):
        delivery_point (str | Unset):
        delivery_point_contains (str | Unset):
        delivery_point_endswith (str | Unset):
        delivery_point_gt (str | Unset):
        delivery_point_gte (str | Unset):
        delivery_point_icontains (str | Unset):
        delivery_point_iendswith (str | Unset):
        delivery_point_iexact (str | Unset):
        delivery_point_in (list[str] | Unset):
        delivery_point_iregex (str | Unset):
        delivery_point_isnull (bool | Unset):
        delivery_point_istartswith (str | Unset):
        delivery_point_lt (str | Unset):
        delivery_point_lte (str | Unset):
        delivery_point_range (list[str] | Unset):
        delivery_point_regex (str | Unset):
        delivery_point_startswith (str | Unset):
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
        electronic_email_address (str | Unset):
        electronic_email_address_contains (str | Unset):
        electronic_email_address_endswith (str | Unset):
        electronic_email_address_gt (str | Unset):
        electronic_email_address_gte (str | Unset):
        electronic_email_address_icontains (str | Unset):
        electronic_email_address_iendswith (str | Unset):
        electronic_email_address_iexact (str | Unset):
        electronic_email_address_in (list[str] | Unset):
        electronic_email_address_iregex (str | Unset):
        electronic_email_address_isnull (bool | Unset):
        electronic_email_address_istartswith (str | Unset):
        electronic_email_address_lt (str | Unset):
        electronic_email_address_lte (str | Unset):
        electronic_email_address_range (list[str] | Unset):
        electronic_email_address_regex (str | Unset):
        electronic_email_address_startswith (str | Unset):
        first_name (str | Unset):
        first_name_contains (str | Unset):
        first_name_endswith (str | Unset):
        first_name_gt (str | Unset):
        first_name_gte (str | Unset):
        first_name_icontains (str | Unset):
        first_name_iendswith (str | Unset):
        first_name_iexact (str | Unset):
        first_name_in (list[str] | Unset):
        first_name_iregex (str | Unset):
        first_name_isnull (bool | Unset):
        first_name_istartswith (str | Unset):
        first_name_lt (str | Unset):
        first_name_lte (str | Unset):
        first_name_range (list[str] | Unset):
        first_name_regex (str | Unset):
        first_name_startswith (str | Unset):
        last_name (str | Unset):
        last_name_contains (str | Unset):
        last_name_endswith (str | Unset):
        last_name_gt (str | Unset):
        last_name_gte (str | Unset):
        last_name_icontains (str | Unset):
        last_name_iendswith (str | Unset):
        last_name_iexact (str | Unset):
        last_name_in (list[str] | Unset):
        last_name_iregex (str | Unset):
        last_name_isnull (bool | Unset):
        last_name_istartswith (str | Unset):
        last_name_lt (str | Unset):
        last_name_lte (str | Unset):
        last_name_range (list[str] | Unset):
        last_name_regex (str | Unset):
        last_name_startswith (str | Unset):
        limit (int | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        online_resource (str | Unset):
        online_resource_contains (str | Unset):
        online_resource_endswith (str | Unset):
        online_resource_gt (str | Unset):
        online_resource_gte (str | Unset):
        online_resource_icontains (str | Unset):
        online_resource_iendswith (str | Unset):
        online_resource_iexact (str | Unset):
        online_resource_in (list[str] | Unset):
        online_resource_iregex (str | Unset):
        online_resource_isnull (bool | Unset):
        online_resource_istartswith (str | Unset):
        online_resource_lt (str | Unset):
        online_resource_lte (str | Unset):
        online_resource_range (list[str] | Unset):
        online_resource_regex (str | Unset):
        online_resource_startswith (str | Unset):
        ordering (str | Unset):
        party_type (PartiesListType | Unset):
        party_type_contains (str | Unset):
        party_type_endswith (str | Unset):
        party_type_gt (str | Unset):
        party_type_gte (str | Unset):
        party_type_icontains (str | Unset):
        party_type_iendswith (str | Unset):
        party_type_iexact (str | Unset):
        party_type_in (list[str] | Unset):
        party_type_iregex (str | Unset):
        party_type_isnull (bool | Unset):
        party_type_istartswith (str | Unset):
        party_type_lt (str | Unset):
        party_type_lte (str | Unset):
        party_type_range (list[str] | Unset):
        party_type_regex (str | Unset):
        party_type_startswith (str | Unset):
        phone (str | Unset):
        phone_contains (str | Unset):
        phone_endswith (str | Unset):
        phone_gt (str | Unset):
        phone_gte (str | Unset):
        phone_icontains (str | Unset):
        phone_iendswith (str | Unset):
        phone_iexact (str | Unset):
        phone_in (list[str] | Unset):
        phone_iregex (str | Unset):
        phone_isnull (bool | Unset):
        phone_istartswith (str | Unset):
        phone_lt (str | Unset):
        phone_lte (str | Unset):
        phone_range (list[str] | Unset):
        phone_regex (str | Unset):
        phone_startswith (str | Unset):
        postal_code (str | Unset):
        postal_code_contains (str | Unset):
        postal_code_endswith (str | Unset):
        postal_code_gt (str | Unset):
        postal_code_gte (str | Unset):
        postal_code_icontains (str | Unset):
        postal_code_iendswith (str | Unset):
        postal_code_iexact (str | Unset):
        postal_code_in (list[str] | Unset):
        postal_code_iregex (str | Unset):
        postal_code_isnull (bool | Unset):
        postal_code_istartswith (str | Unset):
        postal_code_lt (str | Unset):
        postal_code_lte (str | Unset):
        postal_code_range (list[str] | Unset):
        postal_code_regex (str | Unset):
        postal_code_startswith (str | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
        reviewnote (list[int] | Unset):
        reviewnote_in (list[int] | Unset):
        reviewnote_isnull (bool | Unset):

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
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
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
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
        review=review,
        review_in=review_in,
        review_isnull=review_isnull,
        reviewnote=reviewnote,
        reviewnote_in=reviewnote_in,
        reviewnote_isnull=reviewnote_isnull,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    administrative_area: str | Unset = UNSET,
    administrative_area_contains: str | Unset = UNSET,
    administrative_area_endswith: str | Unset = UNSET,
    administrative_area_gt: str | Unset = UNSET,
    administrative_area_gte: str | Unset = UNSET,
    administrative_area_icontains: str | Unset = UNSET,
    administrative_area_iendswith: str | Unset = UNSET,
    administrative_area_iexact: str | Unset = UNSET,
    administrative_area_in: list[str] | Unset = UNSET,
    administrative_area_iregex: str | Unset = UNSET,
    administrative_area_isnull: bool | Unset = UNSET,
    administrative_area_istartswith: str | Unset = UNSET,
    administrative_area_lt: str | Unset = UNSET,
    administrative_area_lte: str | Unset = UNSET,
    administrative_area_range: list[str] | Unset = UNSET,
    administrative_area_regex: str | Unset = UNSET,
    administrative_area_startswith: str | Unset = UNSET,
    city: str | Unset = UNSET,
    city_contains: str | Unset = UNSET,
    city_endswith: str | Unset = UNSET,
    city_gt: str | Unset = UNSET,
    city_gte: str | Unset = UNSET,
    city_icontains: str | Unset = UNSET,
    city_iendswith: str | Unset = UNSET,
    city_iexact: str | Unset = UNSET,
    city_in: list[str] | Unset = UNSET,
    city_iregex: str | Unset = UNSET,
    city_isnull: bool | Unset = UNSET,
    city_istartswith: str | Unset = UNSET,
    city_lt: str | Unset = UNSET,
    city_lte: str | Unset = UNSET,
    city_range: list[str] | Unset = UNSET,
    city_regex: str | Unset = UNSET,
    city_startswith: str | Unset = UNSET,
    country: str | Unset = UNSET,
    country_contains: str | Unset = UNSET,
    country_endswith: str | Unset = UNSET,
    country_gt: str | Unset = UNSET,
    country_gte: str | Unset = UNSET,
    country_icontains: str | Unset = UNSET,
    country_iendswith: str | Unset = UNSET,
    country_iexact: str | Unset = UNSET,
    country_in: list[str] | Unset = UNSET,
    country_iregex: str | Unset = UNSET,
    country_isnull: bool | Unset = UNSET,
    country_istartswith: str | Unset = UNSET,
    country_lt: str | Unset = UNSET,
    country_lte: str | Unset = UNSET,
    country_range: list[str] | Unset = UNSET,
    country_regex: str | Unset = UNSET,
    country_startswith: str | Unset = UNSET,
    delivery_point: str | Unset = UNSET,
    delivery_point_contains: str | Unset = UNSET,
    delivery_point_endswith: str | Unset = UNSET,
    delivery_point_gt: str | Unset = UNSET,
    delivery_point_gte: str | Unset = UNSET,
    delivery_point_icontains: str | Unset = UNSET,
    delivery_point_iendswith: str | Unset = UNSET,
    delivery_point_iexact: str | Unset = UNSET,
    delivery_point_in: list[str] | Unset = UNSET,
    delivery_point_iregex: str | Unset = UNSET,
    delivery_point_isnull: bool | Unset = UNSET,
    delivery_point_istartswith: str | Unset = UNSET,
    delivery_point_lt: str | Unset = UNSET,
    delivery_point_lte: str | Unset = UNSET,
    delivery_point_range: list[str] | Unset = UNSET,
    delivery_point_regex: str | Unset = UNSET,
    delivery_point_startswith: str | Unset = UNSET,
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
    electronic_email_address: str | Unset = UNSET,
    electronic_email_address_contains: str | Unset = UNSET,
    electronic_email_address_endswith: str | Unset = UNSET,
    electronic_email_address_gt: str | Unset = UNSET,
    electronic_email_address_gte: str | Unset = UNSET,
    electronic_email_address_icontains: str | Unset = UNSET,
    electronic_email_address_iendswith: str | Unset = UNSET,
    electronic_email_address_iexact: str | Unset = UNSET,
    electronic_email_address_in: list[str] | Unset = UNSET,
    electronic_email_address_iregex: str | Unset = UNSET,
    electronic_email_address_isnull: bool | Unset = UNSET,
    electronic_email_address_istartswith: str | Unset = UNSET,
    electronic_email_address_lt: str | Unset = UNSET,
    electronic_email_address_lte: str | Unset = UNSET,
    electronic_email_address_range: list[str] | Unset = UNSET,
    electronic_email_address_regex: str | Unset = UNSET,
    electronic_email_address_startswith: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    first_name_contains: str | Unset = UNSET,
    first_name_endswith: str | Unset = UNSET,
    first_name_gt: str | Unset = UNSET,
    first_name_gte: str | Unset = UNSET,
    first_name_icontains: str | Unset = UNSET,
    first_name_iendswith: str | Unset = UNSET,
    first_name_iexact: str | Unset = UNSET,
    first_name_in: list[str] | Unset = UNSET,
    first_name_iregex: str | Unset = UNSET,
    first_name_isnull: bool | Unset = UNSET,
    first_name_istartswith: str | Unset = UNSET,
    first_name_lt: str | Unset = UNSET,
    first_name_lte: str | Unset = UNSET,
    first_name_range: list[str] | Unset = UNSET,
    first_name_regex: str | Unset = UNSET,
    first_name_startswith: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    last_name_contains: str | Unset = UNSET,
    last_name_endswith: str | Unset = UNSET,
    last_name_gt: str | Unset = UNSET,
    last_name_gte: str | Unset = UNSET,
    last_name_icontains: str | Unset = UNSET,
    last_name_iendswith: str | Unset = UNSET,
    last_name_iexact: str | Unset = UNSET,
    last_name_in: list[str] | Unset = UNSET,
    last_name_iregex: str | Unset = UNSET,
    last_name_isnull: bool | Unset = UNSET,
    last_name_istartswith: str | Unset = UNSET,
    last_name_lt: str | Unset = UNSET,
    last_name_lte: str | Unset = UNSET,
    last_name_range: list[str] | Unset = UNSET,
    last_name_regex: str | Unset = UNSET,
    last_name_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    online_resource: str | Unset = UNSET,
    online_resource_contains: str | Unset = UNSET,
    online_resource_endswith: str | Unset = UNSET,
    online_resource_gt: str | Unset = UNSET,
    online_resource_gte: str | Unset = UNSET,
    online_resource_icontains: str | Unset = UNSET,
    online_resource_iendswith: str | Unset = UNSET,
    online_resource_iexact: str | Unset = UNSET,
    online_resource_in: list[str] | Unset = UNSET,
    online_resource_iregex: str | Unset = UNSET,
    online_resource_isnull: bool | Unset = UNSET,
    online_resource_istartswith: str | Unset = UNSET,
    online_resource_lt: str | Unset = UNSET,
    online_resource_lte: str | Unset = UNSET,
    online_resource_range: list[str] | Unset = UNSET,
    online_resource_regex: str | Unset = UNSET,
    online_resource_startswith: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    party_type: PartiesListType | Unset = UNSET,
    party_type_contains: str | Unset = UNSET,
    party_type_endswith: str | Unset = UNSET,
    party_type_gt: str | Unset = UNSET,
    party_type_gte: str | Unset = UNSET,
    party_type_icontains: str | Unset = UNSET,
    party_type_iendswith: str | Unset = UNSET,
    party_type_iexact: str | Unset = UNSET,
    party_type_in: list[str] | Unset = UNSET,
    party_type_iregex: str | Unset = UNSET,
    party_type_isnull: bool | Unset = UNSET,
    party_type_istartswith: str | Unset = UNSET,
    party_type_lt: str | Unset = UNSET,
    party_type_lte: str | Unset = UNSET,
    party_type_range: list[str] | Unset = UNSET,
    party_type_regex: str | Unset = UNSET,
    party_type_startswith: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    phone_contains: str | Unset = UNSET,
    phone_endswith: str | Unset = UNSET,
    phone_gt: str | Unset = UNSET,
    phone_gte: str | Unset = UNSET,
    phone_icontains: str | Unset = UNSET,
    phone_iendswith: str | Unset = UNSET,
    phone_iexact: str | Unset = UNSET,
    phone_in: list[str] | Unset = UNSET,
    phone_iregex: str | Unset = UNSET,
    phone_isnull: bool | Unset = UNSET,
    phone_istartswith: str | Unset = UNSET,
    phone_lt: str | Unset = UNSET,
    phone_lte: str | Unset = UNSET,
    phone_range: list[str] | Unset = UNSET,
    phone_regex: str | Unset = UNSET,
    phone_startswith: str | Unset = UNSET,
    postal_code: str | Unset = UNSET,
    postal_code_contains: str | Unset = UNSET,
    postal_code_endswith: str | Unset = UNSET,
    postal_code_gt: str | Unset = UNSET,
    postal_code_gte: str | Unset = UNSET,
    postal_code_icontains: str | Unset = UNSET,
    postal_code_iendswith: str | Unset = UNSET,
    postal_code_iexact: str | Unset = UNSET,
    postal_code_in: list[str] | Unset = UNSET,
    postal_code_iregex: str | Unset = UNSET,
    postal_code_isnull: bool | Unset = UNSET,
    postal_code_istartswith: str | Unset = UNSET,
    postal_code_lt: str | Unset = UNSET,
    postal_code_lte: str | Unset = UNSET,
    postal_code_range: list[str] | Unset = UNSET,
    postal_code_regex: str | Unset = UNSET,
    postal_code_startswith: str | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
    reviewnote: list[int] | Unset = UNSET,
    reviewnote_in: list[int] | Unset = UNSET,
    reviewnote_isnull: bool | Unset = UNSET,
) -> PaginatedPartyReadList | None:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        administrative_area (str | Unset):
        administrative_area_contains (str | Unset):
        administrative_area_endswith (str | Unset):
        administrative_area_gt (str | Unset):
        administrative_area_gte (str | Unset):
        administrative_area_icontains (str | Unset):
        administrative_area_iendswith (str | Unset):
        administrative_area_iexact (str | Unset):
        administrative_area_in (list[str] | Unset):
        administrative_area_iregex (str | Unset):
        administrative_area_isnull (bool | Unset):
        administrative_area_istartswith (str | Unset):
        administrative_area_lt (str | Unset):
        administrative_area_lte (str | Unset):
        administrative_area_range (list[str] | Unset):
        administrative_area_regex (str | Unset):
        administrative_area_startswith (str | Unset):
        city (str | Unset):
        city_contains (str | Unset):
        city_endswith (str | Unset):
        city_gt (str | Unset):
        city_gte (str | Unset):
        city_icontains (str | Unset):
        city_iendswith (str | Unset):
        city_iexact (str | Unset):
        city_in (list[str] | Unset):
        city_iregex (str | Unset):
        city_isnull (bool | Unset):
        city_istartswith (str | Unset):
        city_lt (str | Unset):
        city_lte (str | Unset):
        city_range (list[str] | Unset):
        city_regex (str | Unset):
        city_startswith (str | Unset):
        country (str | Unset):
        country_contains (str | Unset):
        country_endswith (str | Unset):
        country_gt (str | Unset):
        country_gte (str | Unset):
        country_icontains (str | Unset):
        country_iendswith (str | Unset):
        country_iexact (str | Unset):
        country_in (list[str] | Unset):
        country_iregex (str | Unset):
        country_isnull (bool | Unset):
        country_istartswith (str | Unset):
        country_lt (str | Unset):
        country_lte (str | Unset):
        country_range (list[str] | Unset):
        country_regex (str | Unset):
        country_startswith (str | Unset):
        delivery_point (str | Unset):
        delivery_point_contains (str | Unset):
        delivery_point_endswith (str | Unset):
        delivery_point_gt (str | Unset):
        delivery_point_gte (str | Unset):
        delivery_point_icontains (str | Unset):
        delivery_point_iendswith (str | Unset):
        delivery_point_iexact (str | Unset):
        delivery_point_in (list[str] | Unset):
        delivery_point_iregex (str | Unset):
        delivery_point_isnull (bool | Unset):
        delivery_point_istartswith (str | Unset):
        delivery_point_lt (str | Unset):
        delivery_point_lte (str | Unset):
        delivery_point_range (list[str] | Unset):
        delivery_point_regex (str | Unset):
        delivery_point_startswith (str | Unset):
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
        electronic_email_address (str | Unset):
        electronic_email_address_contains (str | Unset):
        electronic_email_address_endswith (str | Unset):
        electronic_email_address_gt (str | Unset):
        electronic_email_address_gte (str | Unset):
        electronic_email_address_icontains (str | Unset):
        electronic_email_address_iendswith (str | Unset):
        electronic_email_address_iexact (str | Unset):
        electronic_email_address_in (list[str] | Unset):
        electronic_email_address_iregex (str | Unset):
        electronic_email_address_isnull (bool | Unset):
        electronic_email_address_istartswith (str | Unset):
        electronic_email_address_lt (str | Unset):
        electronic_email_address_lte (str | Unset):
        electronic_email_address_range (list[str] | Unset):
        electronic_email_address_regex (str | Unset):
        electronic_email_address_startswith (str | Unset):
        first_name (str | Unset):
        first_name_contains (str | Unset):
        first_name_endswith (str | Unset):
        first_name_gt (str | Unset):
        first_name_gte (str | Unset):
        first_name_icontains (str | Unset):
        first_name_iendswith (str | Unset):
        first_name_iexact (str | Unset):
        first_name_in (list[str] | Unset):
        first_name_iregex (str | Unset):
        first_name_isnull (bool | Unset):
        first_name_istartswith (str | Unset):
        first_name_lt (str | Unset):
        first_name_lte (str | Unset):
        first_name_range (list[str] | Unset):
        first_name_regex (str | Unset):
        first_name_startswith (str | Unset):
        last_name (str | Unset):
        last_name_contains (str | Unset):
        last_name_endswith (str | Unset):
        last_name_gt (str | Unset):
        last_name_gte (str | Unset):
        last_name_icontains (str | Unset):
        last_name_iendswith (str | Unset):
        last_name_iexact (str | Unset):
        last_name_in (list[str] | Unset):
        last_name_iregex (str | Unset):
        last_name_isnull (bool | Unset):
        last_name_istartswith (str | Unset):
        last_name_lt (str | Unset):
        last_name_lte (str | Unset):
        last_name_range (list[str] | Unset):
        last_name_regex (str | Unset):
        last_name_startswith (str | Unset):
        limit (int | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        online_resource (str | Unset):
        online_resource_contains (str | Unset):
        online_resource_endswith (str | Unset):
        online_resource_gt (str | Unset):
        online_resource_gte (str | Unset):
        online_resource_icontains (str | Unset):
        online_resource_iendswith (str | Unset):
        online_resource_iexact (str | Unset):
        online_resource_in (list[str] | Unset):
        online_resource_iregex (str | Unset):
        online_resource_isnull (bool | Unset):
        online_resource_istartswith (str | Unset):
        online_resource_lt (str | Unset):
        online_resource_lte (str | Unset):
        online_resource_range (list[str] | Unset):
        online_resource_regex (str | Unset):
        online_resource_startswith (str | Unset):
        ordering (str | Unset):
        party_type (PartiesListType | Unset):
        party_type_contains (str | Unset):
        party_type_endswith (str | Unset):
        party_type_gt (str | Unset):
        party_type_gte (str | Unset):
        party_type_icontains (str | Unset):
        party_type_iendswith (str | Unset):
        party_type_iexact (str | Unset):
        party_type_in (list[str] | Unset):
        party_type_iregex (str | Unset):
        party_type_isnull (bool | Unset):
        party_type_istartswith (str | Unset):
        party_type_lt (str | Unset):
        party_type_lte (str | Unset):
        party_type_range (list[str] | Unset):
        party_type_regex (str | Unset):
        party_type_startswith (str | Unset):
        phone (str | Unset):
        phone_contains (str | Unset):
        phone_endswith (str | Unset):
        phone_gt (str | Unset):
        phone_gte (str | Unset):
        phone_icontains (str | Unset):
        phone_iendswith (str | Unset):
        phone_iexact (str | Unset):
        phone_in (list[str] | Unset):
        phone_iregex (str | Unset):
        phone_isnull (bool | Unset):
        phone_istartswith (str | Unset):
        phone_lt (str | Unset):
        phone_lte (str | Unset):
        phone_range (list[str] | Unset):
        phone_regex (str | Unset):
        phone_startswith (str | Unset):
        postal_code (str | Unset):
        postal_code_contains (str | Unset):
        postal_code_endswith (str | Unset):
        postal_code_gt (str | Unset):
        postal_code_gte (str | Unset):
        postal_code_icontains (str | Unset):
        postal_code_iendswith (str | Unset):
        postal_code_iexact (str | Unset):
        postal_code_in (list[str] | Unset):
        postal_code_iregex (str | Unset):
        postal_code_isnull (bool | Unset):
        postal_code_istartswith (str | Unset):
        postal_code_lt (str | Unset):
        postal_code_lte (str | Unset):
        postal_code_range (list[str] | Unset):
        postal_code_regex (str | Unset):
        postal_code_startswith (str | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
        reviewnote (list[int] | Unset):
        reviewnote_in (list[int] | Unset):
        reviewnote_isnull (bool | Unset):

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
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
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
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
        review=review,
        review_in=review_in,
        review_isnull=review_isnull,
        reviewnote=reviewnote,
        reviewnote_in=reviewnote_in,
        reviewnote_isnull=reviewnote_isnull,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    administrative_area: str | Unset = UNSET,
    administrative_area_contains: str | Unset = UNSET,
    administrative_area_endswith: str | Unset = UNSET,
    administrative_area_gt: str | Unset = UNSET,
    administrative_area_gte: str | Unset = UNSET,
    administrative_area_icontains: str | Unset = UNSET,
    administrative_area_iendswith: str | Unset = UNSET,
    administrative_area_iexact: str | Unset = UNSET,
    administrative_area_in: list[str] | Unset = UNSET,
    administrative_area_iregex: str | Unset = UNSET,
    administrative_area_isnull: bool | Unset = UNSET,
    administrative_area_istartswith: str | Unset = UNSET,
    administrative_area_lt: str | Unset = UNSET,
    administrative_area_lte: str | Unset = UNSET,
    administrative_area_range: list[str] | Unset = UNSET,
    administrative_area_regex: str | Unset = UNSET,
    administrative_area_startswith: str | Unset = UNSET,
    city: str | Unset = UNSET,
    city_contains: str | Unset = UNSET,
    city_endswith: str | Unset = UNSET,
    city_gt: str | Unset = UNSET,
    city_gte: str | Unset = UNSET,
    city_icontains: str | Unset = UNSET,
    city_iendswith: str | Unset = UNSET,
    city_iexact: str | Unset = UNSET,
    city_in: list[str] | Unset = UNSET,
    city_iregex: str | Unset = UNSET,
    city_isnull: bool | Unset = UNSET,
    city_istartswith: str | Unset = UNSET,
    city_lt: str | Unset = UNSET,
    city_lte: str | Unset = UNSET,
    city_range: list[str] | Unset = UNSET,
    city_regex: str | Unset = UNSET,
    city_startswith: str | Unset = UNSET,
    country: str | Unset = UNSET,
    country_contains: str | Unset = UNSET,
    country_endswith: str | Unset = UNSET,
    country_gt: str | Unset = UNSET,
    country_gte: str | Unset = UNSET,
    country_icontains: str | Unset = UNSET,
    country_iendswith: str | Unset = UNSET,
    country_iexact: str | Unset = UNSET,
    country_in: list[str] | Unset = UNSET,
    country_iregex: str | Unset = UNSET,
    country_isnull: bool | Unset = UNSET,
    country_istartswith: str | Unset = UNSET,
    country_lt: str | Unset = UNSET,
    country_lte: str | Unset = UNSET,
    country_range: list[str] | Unset = UNSET,
    country_regex: str | Unset = UNSET,
    country_startswith: str | Unset = UNSET,
    delivery_point: str | Unset = UNSET,
    delivery_point_contains: str | Unset = UNSET,
    delivery_point_endswith: str | Unset = UNSET,
    delivery_point_gt: str | Unset = UNSET,
    delivery_point_gte: str | Unset = UNSET,
    delivery_point_icontains: str | Unset = UNSET,
    delivery_point_iendswith: str | Unset = UNSET,
    delivery_point_iexact: str | Unset = UNSET,
    delivery_point_in: list[str] | Unset = UNSET,
    delivery_point_iregex: str | Unset = UNSET,
    delivery_point_isnull: bool | Unset = UNSET,
    delivery_point_istartswith: str | Unset = UNSET,
    delivery_point_lt: str | Unset = UNSET,
    delivery_point_lte: str | Unset = UNSET,
    delivery_point_range: list[str] | Unset = UNSET,
    delivery_point_regex: str | Unset = UNSET,
    delivery_point_startswith: str | Unset = UNSET,
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
    electronic_email_address: str | Unset = UNSET,
    electronic_email_address_contains: str | Unset = UNSET,
    electronic_email_address_endswith: str | Unset = UNSET,
    electronic_email_address_gt: str | Unset = UNSET,
    electronic_email_address_gte: str | Unset = UNSET,
    electronic_email_address_icontains: str | Unset = UNSET,
    electronic_email_address_iendswith: str | Unset = UNSET,
    electronic_email_address_iexact: str | Unset = UNSET,
    electronic_email_address_in: list[str] | Unset = UNSET,
    electronic_email_address_iregex: str | Unset = UNSET,
    electronic_email_address_isnull: bool | Unset = UNSET,
    electronic_email_address_istartswith: str | Unset = UNSET,
    electronic_email_address_lt: str | Unset = UNSET,
    electronic_email_address_lte: str | Unset = UNSET,
    electronic_email_address_range: list[str] | Unset = UNSET,
    electronic_email_address_regex: str | Unset = UNSET,
    electronic_email_address_startswith: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    first_name_contains: str | Unset = UNSET,
    first_name_endswith: str | Unset = UNSET,
    first_name_gt: str | Unset = UNSET,
    first_name_gte: str | Unset = UNSET,
    first_name_icontains: str | Unset = UNSET,
    first_name_iendswith: str | Unset = UNSET,
    first_name_iexact: str | Unset = UNSET,
    first_name_in: list[str] | Unset = UNSET,
    first_name_iregex: str | Unset = UNSET,
    first_name_isnull: bool | Unset = UNSET,
    first_name_istartswith: str | Unset = UNSET,
    first_name_lt: str | Unset = UNSET,
    first_name_lte: str | Unset = UNSET,
    first_name_range: list[str] | Unset = UNSET,
    first_name_regex: str | Unset = UNSET,
    first_name_startswith: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    last_name_contains: str | Unset = UNSET,
    last_name_endswith: str | Unset = UNSET,
    last_name_gt: str | Unset = UNSET,
    last_name_gte: str | Unset = UNSET,
    last_name_icontains: str | Unset = UNSET,
    last_name_iendswith: str | Unset = UNSET,
    last_name_iexact: str | Unset = UNSET,
    last_name_in: list[str] | Unset = UNSET,
    last_name_iregex: str | Unset = UNSET,
    last_name_isnull: bool | Unset = UNSET,
    last_name_istartswith: str | Unset = UNSET,
    last_name_lt: str | Unset = UNSET,
    last_name_lte: str | Unset = UNSET,
    last_name_range: list[str] | Unset = UNSET,
    last_name_regex: str | Unset = UNSET,
    last_name_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    online_resource: str | Unset = UNSET,
    online_resource_contains: str | Unset = UNSET,
    online_resource_endswith: str | Unset = UNSET,
    online_resource_gt: str | Unset = UNSET,
    online_resource_gte: str | Unset = UNSET,
    online_resource_icontains: str | Unset = UNSET,
    online_resource_iendswith: str | Unset = UNSET,
    online_resource_iexact: str | Unset = UNSET,
    online_resource_in: list[str] | Unset = UNSET,
    online_resource_iregex: str | Unset = UNSET,
    online_resource_isnull: bool | Unset = UNSET,
    online_resource_istartswith: str | Unset = UNSET,
    online_resource_lt: str | Unset = UNSET,
    online_resource_lte: str | Unset = UNSET,
    online_resource_range: list[str] | Unset = UNSET,
    online_resource_regex: str | Unset = UNSET,
    online_resource_startswith: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    party_type: PartiesListType | Unset = UNSET,
    party_type_contains: str | Unset = UNSET,
    party_type_endswith: str | Unset = UNSET,
    party_type_gt: str | Unset = UNSET,
    party_type_gte: str | Unset = UNSET,
    party_type_icontains: str | Unset = UNSET,
    party_type_iendswith: str | Unset = UNSET,
    party_type_iexact: str | Unset = UNSET,
    party_type_in: list[str] | Unset = UNSET,
    party_type_iregex: str | Unset = UNSET,
    party_type_isnull: bool | Unset = UNSET,
    party_type_istartswith: str | Unset = UNSET,
    party_type_lt: str | Unset = UNSET,
    party_type_lte: str | Unset = UNSET,
    party_type_range: list[str] | Unset = UNSET,
    party_type_regex: str | Unset = UNSET,
    party_type_startswith: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    phone_contains: str | Unset = UNSET,
    phone_endswith: str | Unset = UNSET,
    phone_gt: str | Unset = UNSET,
    phone_gte: str | Unset = UNSET,
    phone_icontains: str | Unset = UNSET,
    phone_iendswith: str | Unset = UNSET,
    phone_iexact: str | Unset = UNSET,
    phone_in: list[str] | Unset = UNSET,
    phone_iregex: str | Unset = UNSET,
    phone_isnull: bool | Unset = UNSET,
    phone_istartswith: str | Unset = UNSET,
    phone_lt: str | Unset = UNSET,
    phone_lte: str | Unset = UNSET,
    phone_range: list[str] | Unset = UNSET,
    phone_regex: str | Unset = UNSET,
    phone_startswith: str | Unset = UNSET,
    postal_code: str | Unset = UNSET,
    postal_code_contains: str | Unset = UNSET,
    postal_code_endswith: str | Unset = UNSET,
    postal_code_gt: str | Unset = UNSET,
    postal_code_gte: str | Unset = UNSET,
    postal_code_icontains: str | Unset = UNSET,
    postal_code_iendswith: str | Unset = UNSET,
    postal_code_iexact: str | Unset = UNSET,
    postal_code_in: list[str] | Unset = UNSET,
    postal_code_iregex: str | Unset = UNSET,
    postal_code_isnull: bool | Unset = UNSET,
    postal_code_istartswith: str | Unset = UNSET,
    postal_code_lt: str | Unset = UNSET,
    postal_code_lte: str | Unset = UNSET,
    postal_code_range: list[str] | Unset = UNSET,
    postal_code_regex: str | Unset = UNSET,
    postal_code_startswith: str | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
    reviewnote: list[int] | Unset = UNSET,
    reviewnote_in: list[int] | Unset = UNSET,
    reviewnote_isnull: bool | Unset = UNSET,
) -> Response[PaginatedPartyReadList]:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        administrative_area (str | Unset):
        administrative_area_contains (str | Unset):
        administrative_area_endswith (str | Unset):
        administrative_area_gt (str | Unset):
        administrative_area_gte (str | Unset):
        administrative_area_icontains (str | Unset):
        administrative_area_iendswith (str | Unset):
        administrative_area_iexact (str | Unset):
        administrative_area_in (list[str] | Unset):
        administrative_area_iregex (str | Unset):
        administrative_area_isnull (bool | Unset):
        administrative_area_istartswith (str | Unset):
        administrative_area_lt (str | Unset):
        administrative_area_lte (str | Unset):
        administrative_area_range (list[str] | Unset):
        administrative_area_regex (str | Unset):
        administrative_area_startswith (str | Unset):
        city (str | Unset):
        city_contains (str | Unset):
        city_endswith (str | Unset):
        city_gt (str | Unset):
        city_gte (str | Unset):
        city_icontains (str | Unset):
        city_iendswith (str | Unset):
        city_iexact (str | Unset):
        city_in (list[str] | Unset):
        city_iregex (str | Unset):
        city_isnull (bool | Unset):
        city_istartswith (str | Unset):
        city_lt (str | Unset):
        city_lte (str | Unset):
        city_range (list[str] | Unset):
        city_regex (str | Unset):
        city_startswith (str | Unset):
        country (str | Unset):
        country_contains (str | Unset):
        country_endswith (str | Unset):
        country_gt (str | Unset):
        country_gte (str | Unset):
        country_icontains (str | Unset):
        country_iendswith (str | Unset):
        country_iexact (str | Unset):
        country_in (list[str] | Unset):
        country_iregex (str | Unset):
        country_isnull (bool | Unset):
        country_istartswith (str | Unset):
        country_lt (str | Unset):
        country_lte (str | Unset):
        country_range (list[str] | Unset):
        country_regex (str | Unset):
        country_startswith (str | Unset):
        delivery_point (str | Unset):
        delivery_point_contains (str | Unset):
        delivery_point_endswith (str | Unset):
        delivery_point_gt (str | Unset):
        delivery_point_gte (str | Unset):
        delivery_point_icontains (str | Unset):
        delivery_point_iendswith (str | Unset):
        delivery_point_iexact (str | Unset):
        delivery_point_in (list[str] | Unset):
        delivery_point_iregex (str | Unset):
        delivery_point_isnull (bool | Unset):
        delivery_point_istartswith (str | Unset):
        delivery_point_lt (str | Unset):
        delivery_point_lte (str | Unset):
        delivery_point_range (list[str] | Unset):
        delivery_point_regex (str | Unset):
        delivery_point_startswith (str | Unset):
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
        electronic_email_address (str | Unset):
        electronic_email_address_contains (str | Unset):
        electronic_email_address_endswith (str | Unset):
        electronic_email_address_gt (str | Unset):
        electronic_email_address_gte (str | Unset):
        electronic_email_address_icontains (str | Unset):
        electronic_email_address_iendswith (str | Unset):
        electronic_email_address_iexact (str | Unset):
        electronic_email_address_in (list[str] | Unset):
        electronic_email_address_iregex (str | Unset):
        electronic_email_address_isnull (bool | Unset):
        electronic_email_address_istartswith (str | Unset):
        electronic_email_address_lt (str | Unset):
        electronic_email_address_lte (str | Unset):
        electronic_email_address_range (list[str] | Unset):
        electronic_email_address_regex (str | Unset):
        electronic_email_address_startswith (str | Unset):
        first_name (str | Unset):
        first_name_contains (str | Unset):
        first_name_endswith (str | Unset):
        first_name_gt (str | Unset):
        first_name_gte (str | Unset):
        first_name_icontains (str | Unset):
        first_name_iendswith (str | Unset):
        first_name_iexact (str | Unset):
        first_name_in (list[str] | Unset):
        first_name_iregex (str | Unset):
        first_name_isnull (bool | Unset):
        first_name_istartswith (str | Unset):
        first_name_lt (str | Unset):
        first_name_lte (str | Unset):
        first_name_range (list[str] | Unset):
        first_name_regex (str | Unset):
        first_name_startswith (str | Unset):
        last_name (str | Unset):
        last_name_contains (str | Unset):
        last_name_endswith (str | Unset):
        last_name_gt (str | Unset):
        last_name_gte (str | Unset):
        last_name_icontains (str | Unset):
        last_name_iendswith (str | Unset):
        last_name_iexact (str | Unset):
        last_name_in (list[str] | Unset):
        last_name_iregex (str | Unset):
        last_name_isnull (bool | Unset):
        last_name_istartswith (str | Unset):
        last_name_lt (str | Unset):
        last_name_lte (str | Unset):
        last_name_range (list[str] | Unset):
        last_name_regex (str | Unset):
        last_name_startswith (str | Unset):
        limit (int | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        online_resource (str | Unset):
        online_resource_contains (str | Unset):
        online_resource_endswith (str | Unset):
        online_resource_gt (str | Unset):
        online_resource_gte (str | Unset):
        online_resource_icontains (str | Unset):
        online_resource_iendswith (str | Unset):
        online_resource_iexact (str | Unset):
        online_resource_in (list[str] | Unset):
        online_resource_iregex (str | Unset):
        online_resource_isnull (bool | Unset):
        online_resource_istartswith (str | Unset):
        online_resource_lt (str | Unset):
        online_resource_lte (str | Unset):
        online_resource_range (list[str] | Unset):
        online_resource_regex (str | Unset):
        online_resource_startswith (str | Unset):
        ordering (str | Unset):
        party_type (PartiesListType | Unset):
        party_type_contains (str | Unset):
        party_type_endswith (str | Unset):
        party_type_gt (str | Unset):
        party_type_gte (str | Unset):
        party_type_icontains (str | Unset):
        party_type_iendswith (str | Unset):
        party_type_iexact (str | Unset):
        party_type_in (list[str] | Unset):
        party_type_iregex (str | Unset):
        party_type_isnull (bool | Unset):
        party_type_istartswith (str | Unset):
        party_type_lt (str | Unset):
        party_type_lte (str | Unset):
        party_type_range (list[str] | Unset):
        party_type_regex (str | Unset):
        party_type_startswith (str | Unset):
        phone (str | Unset):
        phone_contains (str | Unset):
        phone_endswith (str | Unset):
        phone_gt (str | Unset):
        phone_gte (str | Unset):
        phone_icontains (str | Unset):
        phone_iendswith (str | Unset):
        phone_iexact (str | Unset):
        phone_in (list[str] | Unset):
        phone_iregex (str | Unset):
        phone_isnull (bool | Unset):
        phone_istartswith (str | Unset):
        phone_lt (str | Unset):
        phone_lte (str | Unset):
        phone_range (list[str] | Unset):
        phone_regex (str | Unset):
        phone_startswith (str | Unset):
        postal_code (str | Unset):
        postal_code_contains (str | Unset):
        postal_code_endswith (str | Unset):
        postal_code_gt (str | Unset):
        postal_code_gte (str | Unset):
        postal_code_icontains (str | Unset):
        postal_code_iendswith (str | Unset):
        postal_code_iexact (str | Unset):
        postal_code_in (list[str] | Unset):
        postal_code_iregex (str | Unset):
        postal_code_isnull (bool | Unset):
        postal_code_istartswith (str | Unset):
        postal_code_lt (str | Unset):
        postal_code_lte (str | Unset):
        postal_code_range (list[str] | Unset):
        postal_code_regex (str | Unset):
        postal_code_startswith (str | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
        reviewnote (list[int] | Unset):
        reviewnote_in (list[int] | Unset):
        reviewnote_isnull (bool | Unset):

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
        note=note,
        note_in=note_in,
        note_isnull=note_isnull,
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
        responsiblepartyinfo=responsiblepartyinfo,
        responsiblepartyinfo_in=responsiblepartyinfo_in,
        responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
        review=review,
        review_in=review_in,
        review_isnull=review_isnull,
        reviewnote=reviewnote,
        reviewnote_in=reviewnote_in,
        reviewnote_isnull=reviewnote_isnull,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    administrative_area: str | Unset = UNSET,
    administrative_area_contains: str | Unset = UNSET,
    administrative_area_endswith: str | Unset = UNSET,
    administrative_area_gt: str | Unset = UNSET,
    administrative_area_gte: str | Unset = UNSET,
    administrative_area_icontains: str | Unset = UNSET,
    administrative_area_iendswith: str | Unset = UNSET,
    administrative_area_iexact: str | Unset = UNSET,
    administrative_area_in: list[str] | Unset = UNSET,
    administrative_area_iregex: str | Unset = UNSET,
    administrative_area_isnull: bool | Unset = UNSET,
    administrative_area_istartswith: str | Unset = UNSET,
    administrative_area_lt: str | Unset = UNSET,
    administrative_area_lte: str | Unset = UNSET,
    administrative_area_range: list[str] | Unset = UNSET,
    administrative_area_regex: str | Unset = UNSET,
    administrative_area_startswith: str | Unset = UNSET,
    city: str | Unset = UNSET,
    city_contains: str | Unset = UNSET,
    city_endswith: str | Unset = UNSET,
    city_gt: str | Unset = UNSET,
    city_gte: str | Unset = UNSET,
    city_icontains: str | Unset = UNSET,
    city_iendswith: str | Unset = UNSET,
    city_iexact: str | Unset = UNSET,
    city_in: list[str] | Unset = UNSET,
    city_iregex: str | Unset = UNSET,
    city_isnull: bool | Unset = UNSET,
    city_istartswith: str | Unset = UNSET,
    city_lt: str | Unset = UNSET,
    city_lte: str | Unset = UNSET,
    city_range: list[str] | Unset = UNSET,
    city_regex: str | Unset = UNSET,
    city_startswith: str | Unset = UNSET,
    country: str | Unset = UNSET,
    country_contains: str | Unset = UNSET,
    country_endswith: str | Unset = UNSET,
    country_gt: str | Unset = UNSET,
    country_gte: str | Unset = UNSET,
    country_icontains: str | Unset = UNSET,
    country_iendswith: str | Unset = UNSET,
    country_iexact: str | Unset = UNSET,
    country_in: list[str] | Unset = UNSET,
    country_iregex: str | Unset = UNSET,
    country_isnull: bool | Unset = UNSET,
    country_istartswith: str | Unset = UNSET,
    country_lt: str | Unset = UNSET,
    country_lte: str | Unset = UNSET,
    country_range: list[str] | Unset = UNSET,
    country_regex: str | Unset = UNSET,
    country_startswith: str | Unset = UNSET,
    delivery_point: str | Unset = UNSET,
    delivery_point_contains: str | Unset = UNSET,
    delivery_point_endswith: str | Unset = UNSET,
    delivery_point_gt: str | Unset = UNSET,
    delivery_point_gte: str | Unset = UNSET,
    delivery_point_icontains: str | Unset = UNSET,
    delivery_point_iendswith: str | Unset = UNSET,
    delivery_point_iexact: str | Unset = UNSET,
    delivery_point_in: list[str] | Unset = UNSET,
    delivery_point_iregex: str | Unset = UNSET,
    delivery_point_isnull: bool | Unset = UNSET,
    delivery_point_istartswith: str | Unset = UNSET,
    delivery_point_lt: str | Unset = UNSET,
    delivery_point_lte: str | Unset = UNSET,
    delivery_point_range: list[str] | Unset = UNSET,
    delivery_point_regex: str | Unset = UNSET,
    delivery_point_startswith: str | Unset = UNSET,
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
    electronic_email_address: str | Unset = UNSET,
    electronic_email_address_contains: str | Unset = UNSET,
    electronic_email_address_endswith: str | Unset = UNSET,
    electronic_email_address_gt: str | Unset = UNSET,
    electronic_email_address_gte: str | Unset = UNSET,
    electronic_email_address_icontains: str | Unset = UNSET,
    electronic_email_address_iendswith: str | Unset = UNSET,
    electronic_email_address_iexact: str | Unset = UNSET,
    electronic_email_address_in: list[str] | Unset = UNSET,
    electronic_email_address_iregex: str | Unset = UNSET,
    electronic_email_address_isnull: bool | Unset = UNSET,
    electronic_email_address_istartswith: str | Unset = UNSET,
    electronic_email_address_lt: str | Unset = UNSET,
    electronic_email_address_lte: str | Unset = UNSET,
    electronic_email_address_range: list[str] | Unset = UNSET,
    electronic_email_address_regex: str | Unset = UNSET,
    electronic_email_address_startswith: str | Unset = UNSET,
    first_name: str | Unset = UNSET,
    first_name_contains: str | Unset = UNSET,
    first_name_endswith: str | Unset = UNSET,
    first_name_gt: str | Unset = UNSET,
    first_name_gte: str | Unset = UNSET,
    first_name_icontains: str | Unset = UNSET,
    first_name_iendswith: str | Unset = UNSET,
    first_name_iexact: str | Unset = UNSET,
    first_name_in: list[str] | Unset = UNSET,
    first_name_iregex: str | Unset = UNSET,
    first_name_isnull: bool | Unset = UNSET,
    first_name_istartswith: str | Unset = UNSET,
    first_name_lt: str | Unset = UNSET,
    first_name_lte: str | Unset = UNSET,
    first_name_range: list[str] | Unset = UNSET,
    first_name_regex: str | Unset = UNSET,
    first_name_startswith: str | Unset = UNSET,
    last_name: str | Unset = UNSET,
    last_name_contains: str | Unset = UNSET,
    last_name_endswith: str | Unset = UNSET,
    last_name_gt: str | Unset = UNSET,
    last_name_gte: str | Unset = UNSET,
    last_name_icontains: str | Unset = UNSET,
    last_name_iendswith: str | Unset = UNSET,
    last_name_iexact: str | Unset = UNSET,
    last_name_in: list[str] | Unset = UNSET,
    last_name_iregex: str | Unset = UNSET,
    last_name_isnull: bool | Unset = UNSET,
    last_name_istartswith: str | Unset = UNSET,
    last_name_lt: str | Unset = UNSET,
    last_name_lte: str | Unset = UNSET,
    last_name_range: list[str] | Unset = UNSET,
    last_name_regex: str | Unset = UNSET,
    last_name_startswith: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    note: list[int] | Unset = UNSET,
    note_in: list[int] | Unset = UNSET,
    note_isnull: bool | Unset = UNSET,
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
    online_resource: str | Unset = UNSET,
    online_resource_contains: str | Unset = UNSET,
    online_resource_endswith: str | Unset = UNSET,
    online_resource_gt: str | Unset = UNSET,
    online_resource_gte: str | Unset = UNSET,
    online_resource_icontains: str | Unset = UNSET,
    online_resource_iendswith: str | Unset = UNSET,
    online_resource_iexact: str | Unset = UNSET,
    online_resource_in: list[str] | Unset = UNSET,
    online_resource_iregex: str | Unset = UNSET,
    online_resource_isnull: bool | Unset = UNSET,
    online_resource_istartswith: str | Unset = UNSET,
    online_resource_lt: str | Unset = UNSET,
    online_resource_lte: str | Unset = UNSET,
    online_resource_range: list[str] | Unset = UNSET,
    online_resource_regex: str | Unset = UNSET,
    online_resource_startswith: str | Unset = UNSET,
    ordering: str | Unset = UNSET,
    party_type: PartiesListType | Unset = UNSET,
    party_type_contains: str | Unset = UNSET,
    party_type_endswith: str | Unset = UNSET,
    party_type_gt: str | Unset = UNSET,
    party_type_gte: str | Unset = UNSET,
    party_type_icontains: str | Unset = UNSET,
    party_type_iendswith: str | Unset = UNSET,
    party_type_iexact: str | Unset = UNSET,
    party_type_in: list[str] | Unset = UNSET,
    party_type_iregex: str | Unset = UNSET,
    party_type_isnull: bool | Unset = UNSET,
    party_type_istartswith: str | Unset = UNSET,
    party_type_lt: str | Unset = UNSET,
    party_type_lte: str | Unset = UNSET,
    party_type_range: list[str] | Unset = UNSET,
    party_type_regex: str | Unset = UNSET,
    party_type_startswith: str | Unset = UNSET,
    phone: str | Unset = UNSET,
    phone_contains: str | Unset = UNSET,
    phone_endswith: str | Unset = UNSET,
    phone_gt: str | Unset = UNSET,
    phone_gte: str | Unset = UNSET,
    phone_icontains: str | Unset = UNSET,
    phone_iendswith: str | Unset = UNSET,
    phone_iexact: str | Unset = UNSET,
    phone_in: list[str] | Unset = UNSET,
    phone_iregex: str | Unset = UNSET,
    phone_isnull: bool | Unset = UNSET,
    phone_istartswith: str | Unset = UNSET,
    phone_lt: str | Unset = UNSET,
    phone_lte: str | Unset = UNSET,
    phone_range: list[str] | Unset = UNSET,
    phone_regex: str | Unset = UNSET,
    phone_startswith: str | Unset = UNSET,
    postal_code: str | Unset = UNSET,
    postal_code_contains: str | Unset = UNSET,
    postal_code_endswith: str | Unset = UNSET,
    postal_code_gt: str | Unset = UNSET,
    postal_code_gte: str | Unset = UNSET,
    postal_code_icontains: str | Unset = UNSET,
    postal_code_iendswith: str | Unset = UNSET,
    postal_code_iexact: str | Unset = UNSET,
    postal_code_in: list[str] | Unset = UNSET,
    postal_code_iregex: str | Unset = UNSET,
    postal_code_isnull: bool | Unset = UNSET,
    postal_code_istartswith: str | Unset = UNSET,
    postal_code_lt: str | Unset = UNSET,
    postal_code_lte: str | Unset = UNSET,
    postal_code_range: list[str] | Unset = UNSET,
    postal_code_regex: str | Unset = UNSET,
    postal_code_startswith: str | Unset = UNSET,
    responsiblepartyinfo: list[int] | Unset = UNSET,
    responsiblepartyinfo_in: list[int] | Unset = UNSET,
    responsiblepartyinfo_isnull: bool | Unset = UNSET,
    review: list[int] | Unset = UNSET,
    review_in: list[int] | Unset = UNSET,
    review_isnull: bool | Unset = UNSET,
    reviewnote: list[int] | Unset = UNSET,
    reviewnote_in: list[int] | Unset = UNSET,
    reviewnote_isnull: bool | Unset = UNSET,
) -> PaginatedPartyReadList | None:
    """Get a list of Party objects. Parties have a many to many mapping with a number of record types which
    are listed through the responsiblepartyinfo end point as connected to via the
    responsiblepartyinfo_set serialisation.

    Args:
        administrative_area (str | Unset):
        administrative_area_contains (str | Unset):
        administrative_area_endswith (str | Unset):
        administrative_area_gt (str | Unset):
        administrative_area_gte (str | Unset):
        administrative_area_icontains (str | Unset):
        administrative_area_iendswith (str | Unset):
        administrative_area_iexact (str | Unset):
        administrative_area_in (list[str] | Unset):
        administrative_area_iregex (str | Unset):
        administrative_area_isnull (bool | Unset):
        administrative_area_istartswith (str | Unset):
        administrative_area_lt (str | Unset):
        administrative_area_lte (str | Unset):
        administrative_area_range (list[str] | Unset):
        administrative_area_regex (str | Unset):
        administrative_area_startswith (str | Unset):
        city (str | Unset):
        city_contains (str | Unset):
        city_endswith (str | Unset):
        city_gt (str | Unset):
        city_gte (str | Unset):
        city_icontains (str | Unset):
        city_iendswith (str | Unset):
        city_iexact (str | Unset):
        city_in (list[str] | Unset):
        city_iregex (str | Unset):
        city_isnull (bool | Unset):
        city_istartswith (str | Unset):
        city_lt (str | Unset):
        city_lte (str | Unset):
        city_range (list[str] | Unset):
        city_regex (str | Unset):
        city_startswith (str | Unset):
        country (str | Unset):
        country_contains (str | Unset):
        country_endswith (str | Unset):
        country_gt (str | Unset):
        country_gte (str | Unset):
        country_icontains (str | Unset):
        country_iendswith (str | Unset):
        country_iexact (str | Unset):
        country_in (list[str] | Unset):
        country_iregex (str | Unset):
        country_isnull (bool | Unset):
        country_istartswith (str | Unset):
        country_lt (str | Unset):
        country_lte (str | Unset):
        country_range (list[str] | Unset):
        country_regex (str | Unset):
        country_startswith (str | Unset):
        delivery_point (str | Unset):
        delivery_point_contains (str | Unset):
        delivery_point_endswith (str | Unset):
        delivery_point_gt (str | Unset):
        delivery_point_gte (str | Unset):
        delivery_point_icontains (str | Unset):
        delivery_point_iendswith (str | Unset):
        delivery_point_iexact (str | Unset):
        delivery_point_in (list[str] | Unset):
        delivery_point_iregex (str | Unset):
        delivery_point_isnull (bool | Unset):
        delivery_point_istartswith (str | Unset):
        delivery_point_lt (str | Unset):
        delivery_point_lte (str | Unset):
        delivery_point_range (list[str] | Unset):
        delivery_point_regex (str | Unset):
        delivery_point_startswith (str | Unset):
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
        electronic_email_address (str | Unset):
        electronic_email_address_contains (str | Unset):
        electronic_email_address_endswith (str | Unset):
        electronic_email_address_gt (str | Unset):
        electronic_email_address_gte (str | Unset):
        electronic_email_address_icontains (str | Unset):
        electronic_email_address_iendswith (str | Unset):
        electronic_email_address_iexact (str | Unset):
        electronic_email_address_in (list[str] | Unset):
        electronic_email_address_iregex (str | Unset):
        electronic_email_address_isnull (bool | Unset):
        electronic_email_address_istartswith (str | Unset):
        electronic_email_address_lt (str | Unset):
        electronic_email_address_lte (str | Unset):
        electronic_email_address_range (list[str] | Unset):
        electronic_email_address_regex (str | Unset):
        electronic_email_address_startswith (str | Unset):
        first_name (str | Unset):
        first_name_contains (str | Unset):
        first_name_endswith (str | Unset):
        first_name_gt (str | Unset):
        first_name_gte (str | Unset):
        first_name_icontains (str | Unset):
        first_name_iendswith (str | Unset):
        first_name_iexact (str | Unset):
        first_name_in (list[str] | Unset):
        first_name_iregex (str | Unset):
        first_name_isnull (bool | Unset):
        first_name_istartswith (str | Unset):
        first_name_lt (str | Unset):
        first_name_lte (str | Unset):
        first_name_range (list[str] | Unset):
        first_name_regex (str | Unset):
        first_name_startswith (str | Unset):
        last_name (str | Unset):
        last_name_contains (str | Unset):
        last_name_endswith (str | Unset):
        last_name_gt (str | Unset):
        last_name_gte (str | Unset):
        last_name_icontains (str | Unset):
        last_name_iendswith (str | Unset):
        last_name_iexact (str | Unset):
        last_name_in (list[str] | Unset):
        last_name_iregex (str | Unset):
        last_name_isnull (bool | Unset):
        last_name_istartswith (str | Unset):
        last_name_lt (str | Unset):
        last_name_lte (str | Unset):
        last_name_range (list[str] | Unset):
        last_name_regex (str | Unset):
        last_name_startswith (str | Unset):
        limit (int | Unset):
        note (list[int] | Unset):
        note_in (list[int] | Unset):
        note_isnull (bool | Unset):
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
        online_resource (str | Unset):
        online_resource_contains (str | Unset):
        online_resource_endswith (str | Unset):
        online_resource_gt (str | Unset):
        online_resource_gte (str | Unset):
        online_resource_icontains (str | Unset):
        online_resource_iendswith (str | Unset):
        online_resource_iexact (str | Unset):
        online_resource_in (list[str] | Unset):
        online_resource_iregex (str | Unset):
        online_resource_isnull (bool | Unset):
        online_resource_istartswith (str | Unset):
        online_resource_lt (str | Unset):
        online_resource_lte (str | Unset):
        online_resource_range (list[str] | Unset):
        online_resource_regex (str | Unset):
        online_resource_startswith (str | Unset):
        ordering (str | Unset):
        party_type (PartiesListType | Unset):
        party_type_contains (str | Unset):
        party_type_endswith (str | Unset):
        party_type_gt (str | Unset):
        party_type_gte (str | Unset):
        party_type_icontains (str | Unset):
        party_type_iendswith (str | Unset):
        party_type_iexact (str | Unset):
        party_type_in (list[str] | Unset):
        party_type_iregex (str | Unset):
        party_type_isnull (bool | Unset):
        party_type_istartswith (str | Unset):
        party_type_lt (str | Unset):
        party_type_lte (str | Unset):
        party_type_range (list[str] | Unset):
        party_type_regex (str | Unset):
        party_type_startswith (str | Unset):
        phone (str | Unset):
        phone_contains (str | Unset):
        phone_endswith (str | Unset):
        phone_gt (str | Unset):
        phone_gte (str | Unset):
        phone_icontains (str | Unset):
        phone_iendswith (str | Unset):
        phone_iexact (str | Unset):
        phone_in (list[str] | Unset):
        phone_iregex (str | Unset):
        phone_isnull (bool | Unset):
        phone_istartswith (str | Unset):
        phone_lt (str | Unset):
        phone_lte (str | Unset):
        phone_range (list[str] | Unset):
        phone_regex (str | Unset):
        phone_startswith (str | Unset):
        postal_code (str | Unset):
        postal_code_contains (str | Unset):
        postal_code_endswith (str | Unset):
        postal_code_gt (str | Unset):
        postal_code_gte (str | Unset):
        postal_code_icontains (str | Unset):
        postal_code_iendswith (str | Unset):
        postal_code_iexact (str | Unset):
        postal_code_in (list[str] | Unset):
        postal_code_iregex (str | Unset):
        postal_code_isnull (bool | Unset):
        postal_code_istartswith (str | Unset):
        postal_code_lt (str | Unset):
        postal_code_lte (str | Unset):
        postal_code_range (list[str] | Unset):
        postal_code_regex (str | Unset):
        postal_code_startswith (str | Unset):
        responsiblepartyinfo (list[int] | Unset):
        responsiblepartyinfo_in (list[int] | Unset):
        responsiblepartyinfo_isnull (bool | Unset):
        review (list[int] | Unset):
        review_in (list[int] | Unset):
        review_isnull (bool | Unset):
        reviewnote (list[int] | Unset):
        reviewnote_in (list[int] | Unset):
        reviewnote_isnull (bool | Unset):

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
            note=note,
            note_in=note_in,
            note_isnull=note_isnull,
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
            responsiblepartyinfo=responsiblepartyinfo,
            responsiblepartyinfo_in=responsiblepartyinfo_in,
            responsiblepartyinfo_isnull=responsiblepartyinfo_isnull,
            review=review,
            review_in=review_in,
            review_isnull=review_isnull,
            reviewnote=reviewnote,
            reviewnote_in=reviewnote_in,
            reviewnote_isnull=reviewnote_isnull,
        )
    ).parsed
