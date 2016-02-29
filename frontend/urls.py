from django.conf import settings
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

from rest_framework import routers

from .views import (
    demo, photo_demo,
    OperaListView,
    FotoListView, ScrittoListView)


urlpatterns = [
    url(r'^$', OperaListView.as_view(), name='home'),
    url(r'^photos/$', FotoListView.as_view(), name='photos'),
    url(r'^writing/$', ScrittoListView.as_view(), name='writing'),

    # url(r'^demo/$', demo, name='demo'),
    # url(r'^photo-demo/$', photo_demo, name='photo_demo'),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
