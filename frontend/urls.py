from django.conf import settings
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static


from .views import (
    OperaListView,
    FotoListView,
    ScrittoListView,
    ProfileView)


urlpatterns = [
    url(r'^$', OperaListView.as_view(), name='home'),
    url(r'^about/$', ProfileView.as_view(), name='about'),
    url(r'^photos/$', FotoListView.as_view(), name='photos'),
    url(r'^writing/$', ScrittoListView.as_view(), name='writing'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
