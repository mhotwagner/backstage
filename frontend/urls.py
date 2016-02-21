from django.conf.urls import url, include

from rest_framework import routers

from .views import (
    index,
)


urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^index.html$', index, name='other_home'),
]
