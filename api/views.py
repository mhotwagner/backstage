from django.http import HttpResponse, Http404
from django.views.generic import View

from rest_framework import generics, status
from rest_framework import viewsets as rest_framework_viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ProfileViewSet(rest_framework_viewsets.ModelViewSet):
    """
    Facade/Profile List View
    """
    queryset = Profile.objects.filter()
    serializer_class = ProfileSerializer


class FotiListView(generics.ListCreateAPIView):
    queryset = Foto.objects.all().order_by('date')
    serializer_class = FotoSerializer


class FotiDetailView(generics.RetrieveUpdateAPIView):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer


class ScrittiListView(generics.ListAPIView):
    queryset = Scritto.objects.all().order_by('date')
    serializer_class = ScrittoSerializer


class ScrittiDetailView(generics.RetrieveAPIView):
    queryset = Scritto.objects.all()
    serializer_class = ScrittoSerializer


class OpereListView(APIView):
    queryset = Opera.objects

    def get(self, request, format=None):
        opere = Opera.objects.all()
        opere_serializer = OperaSerializer(opere, many=True)
        return Response(opere_serializer.data)

    def post(self, request, format=None):
        opere_serializer = OperaSerializer(data=request.data)

        if opere_serializer.is_valid():
            opere_serializer.save()
            return Response(opere_serializer.data, status=status.HTTP_201_CREATED)
        return Response(opere_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OpereDetailView(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, id):
        try:
            return Opera.objects.get(id=id)
        except Opera.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        opera = self.get_object(id)
        opera_serializer = OperaSerializer(opera)
        return Response(opera_serializer.data)

    def put(self, request, id, format=None):

        opera = self.get_object(id)
        print(opera)
        opera_serializer = OperaSerializer(opera, data=request.data)
        if opera_serializer.is_valid():
            opera_serializer.save()
            return Response(opera_serializer.data)
        return Response(opera_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        opera = self.get_object(id)
        opera.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
