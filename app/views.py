import logging
import requests

from http import HTTPStatus
from urllib.parse import urljoin

from django.conf import settings
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):
    # Fetch via API first.
    try:
        response = requests.get(
            urljoin(settings.API_URL, reverse('contacts_api')),
            timeout=settings.REQUEST_TIMEOUT,
        )
        response.raise_for_status()
    except requests.RequestException:
        logging.warning("Failed to fetch contacts via API.", exc_info=True)
        # Try to use cached version instead.
        contact_list = cache.get('contacts')
    else:
        contact_list = response.json()
        cache.set('contacts', contact_list, None)
    # Render the contact list.
    status = HTTPStatus.OK if contact_list is not None else HTTPStatus.SERVICE_UNAVAILABLE
    return render(request, r"app/index.html", {'contact_list': contact_list}, status=status)


def image(request: HttpRequest):
    url = request.GET.get('url')
    if not url:
        return HttpResponse(status=HTTPStatus.BAD_REQUEST, content='Missing image URL.')
    # Assume that different images use different URLs.
    # Thus, always use cached version first.
    cache_key = 'image:' + url
    content = cache.get(cache_key)
    if not content:
        try:
            response = requests.get(
                urljoin(settings.API_URL, reverse('image_api')),
                timeout=settings.REQUEST_TIMEOUT,
                params={'url': url},
            )
        except requests.RequestException:
            logging.warning('Failed to fetch image via API.', exc_info=True)
            return HttpResponse(content='Failed to fetch image.', status=HTTPStatus.SERVICE_UNAVAILABLE)
        else:
            content = {'content': response.content, 'content_type': response.headers['content-type']}
            cache.set(cache_key, content, None)
    return HttpResponse(content=content['content'], content_type=content['content_type'])
