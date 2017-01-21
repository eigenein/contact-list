from django.conf.urls import url

import api.views


urlpatterns = [
    url(r"^contacts/?$", api.views.contacts, name='contacts'),
    url(r"^image/?$", api.views.image, name='image'),
]
