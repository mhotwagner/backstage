from django.conf.urls import url, include

from rest_framework import routers

from .views import (
    HealthCheck,
    ProfileViewSet,
    ScrittiViewSet, OpereViewSet,
    FotiListView, FotiDetailView,
    OpereListView, OpereDetailView,
)

router = routers.DefaultRouter()
# router.register(r'foti', FotiViewSet)
router.register(r'scritti', ScrittiViewSet)
router.register(r'opere', OpereViewSet)
# router.register(r'profile', ProfileViewSet)
router.register(r'facade', ProfileViewSet)


urlpatterns = [
    url(r'^$', HealthCheck.as_view()),

    url(r'^', include(router.urls)),

    url(r'^foti/$', FotiListView.as_view(), name='foti_list_endpoint'),
    url(r'^foti/(?P<pk>[0-9]+)/$', FotiDetailView.as_view(), name='foti_detail_endpoint'),
    url(r'^opere/$', OpereListView.as_view(), name='opere_list_endpoint'),
    url(r'^opere/(?P<id>[0-9]+)/$', OpereDetailView.as_view(), name='opere_detail_endpoint'),
]