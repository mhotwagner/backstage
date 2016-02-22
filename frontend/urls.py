from django.conf.urls import url, include

from rest_framework import routers

from .views import (
    index,
    demo)


urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^demo/$', demo, name='demo'),

]
