from django.conf.urls import url
from django.views.generic.base import RedirectView

import app.views


urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    url(r'^image/?$', app.views.image, name='image'),
]
