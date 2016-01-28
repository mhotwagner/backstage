from django.http import HttpResponse
from django.views.generic import View

from rest_framework import viewsets

from facade.models import Profile
from facade.serializers import ProfileSerializer
from foti.models import Foto
from foti.serializers import FotoSerializer
from scritti.models import Scritto
from scritti.serializers import ScrittoSerializer
from opere.models import Opera
from opere.serializers import OperaSerializer


class HealthCheck(View):
    def get(self, request):
        return HttpResponse('OK')


class ProfileViewSet(viewsets.ModelViewSet):
    """
    Facade/Profile List View
    """
    queryset = Profile.objects.filter()
    serializer_class = ProfileSerializer


class FotiViewSet(viewsets.ModelViewSet):
    """
    Foti List View
    """
    queryset = Foto.objects.all().order_by('date')
    serializer_class = FotoSerializer


class ScrittiViewSet(viewsets.ModelViewSet):
    """
    Scritti List View
    """
    queryset = Scritto.objects.all().order_by('date')
    serializer_class = ScrittoSerializer


class OpereViewSet(viewsets.ModelViewSet):
    """
    Opere List View
    """
    queryset = Opera.objects.all().order_by('created')
    serializer_class = OperaSerializer
