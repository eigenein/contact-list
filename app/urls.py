from django.conf.urls import url

import app.views


urlpatterns = [
    url(r'^$', app.views.index, name='index'),
    url(r'^image/?$', app.views.image, name='image'),
]
