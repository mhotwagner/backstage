from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from foti.models import Foto
from opere.models import Opera
from scritti.models import Scritto


class OperaListView(View):
    def get(self, request):
        opere = Opera.objects.all()[:6]

        return render(
            request=request,
            template_name='pages/generic-list.html',
            context={
                'top_row': opere[:3],
                'bottom_row': opere[3:],
            },
        )


class FotoListView(View):
    def get(self, request):
        foti = Foto.objects.all()[:6]

        return render(
            request=request,
            template_name='pages/foto-list.html',
            context={
                'top_row': foti[:3],
                'bottom_row': foti[3:],
            },
        )


class ScrittoListView(View):
    def get(self, request):
        scritti = Scritto.objects.all()[:6]

        return render(
            request=request,
            template_name='pages/scritto-list.html',
            context={
                'top_row': scritti[:3],
                'bottom_row': scritti[3:],
            },
        )
