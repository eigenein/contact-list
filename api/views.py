import csv
import logging

from http import HTTPStatus

import requests
import requests.exceptions

from django.conf import settings
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page

from api.parser import parse_contacts_csv


@cache_page(60)
def contacts(request: HttpRequest):
    try:
        response = requests.get(settings.CONTACT_LIST_URL, timeout=settings.REQUEST_TIMEOUT)
        response.raise_for_status()
        contact_list = list(parse_contacts_csv(response.text))
    except requests.exceptions.RequestException:
        # HTTP request failed. Report unavailability.
        logging.warning('Failed to fetch CSV.', exc_info=True)
        return HttpResponse(
            status=HTTPStatus.SERVICE_UNAVAILABLE,
            content='Data source is not available.',
        )
    except (csv.Error, ValueError) as ex:
        # Failed to process CSV.
        logging.warning('Failed to process CSV.', exc_info=True)
        return HttpResponse(
            status=HTTPStatus.SERVICE_UNAVAILABLE,
            content='Source is broken: %s' % ex,
        )
    else:
        return JsonResponse(contact_list, safe=False)


@cache_page(7 * 24 * 60 * 60)
def image(request: HttpRequest):
    url = request.GET.get('url')
    if not url:
        return HttpResponse(status=HTTPStatus.BAD_REQUEST, content='Missing image URL.')
    try:
        response = requests.get(url, timeout=settings.REQUEST_TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return HttpResponse(
            status=HTTPStatus.SERVICE_UNAVAILABLE,
            content='Image is not available.',
        )
    else:
        content_type = response.headers.get('content-type')
        if not content_type or not content_type.startswith("image/"):
            return HttpResponse(status=HTTPStatus.BAD_REQUEST, content='Invalid content type.')
        return HttpResponse(content=response.content, content_type=content_type)
