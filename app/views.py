import logging
import requests

from http import HTTPStatus
from urllib.parse import urljoin

from django.conf import settings
from django.core.cache import cache, caches
from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    # Fetch via API first.
    try:
        response = requests.get(
            urljoin(settings.API_URL, reverse('contacts')),
            timeout=settings.REQUEST_TIMEOUT,
        )
        response.raise_for_status()
    except requests.RequestException:
        logging.warning("Failed to fetch contacts with API.", exc_info=True)
        # Try to use cached version instead.
        contact_list = cache.get('contacts')
    else:
        contact_list = response.json()
        cache.set('contacts', contact_list, None)
    # Render the contact list.
    status = HTTPStatus.OK if contact_list is not None else HTTPStatus.SERVICE_UNAVAILABLE
    return render(request, r"app/index.html", {'contact_list': contact_list}, status=status)


def image(request: HttpRequest):
    pass
