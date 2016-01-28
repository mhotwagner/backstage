from django.conf.urls import url, include

from rest_framework import routers

from .views import (
    HealthCheck,
    ProfileViewSet,
    FotiViewSet, ScrittiViewSet, OpereViewSet,
)

router = routers.DefaultRouter()
router.register(r'foti', FotiViewSet)
router.register(r'scritti', ScrittiViewSet)
router.register(r'opere', OpereViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'facade', ProfileViewSet)


urlpatterns = [
    url(r'^$', HealthCheck.as_view()),
    url(r'^', include(router.urls)),
]