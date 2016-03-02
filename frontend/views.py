from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from facade.models import Profile


class OperaListView(View):
    def get(self, request):

        opere = Profile.objects.first().homepage_features.all()
        profile = Profile.objects.first()

        return render(
            request=request,
            template_name='pages/generic-list.html',
            context={
                'top_row': opere[:3],
                'bottom_row': opere[3:],
                'profile': profile,
                'title': 'Home',
            },
        )


class FotoListView(View):
    def get(self, request):

        foti = Profile.objects.first().photo_features.all()
        profile = Profile.objects.first()

        return render(
            request=request,
            template_name='pages/generic-list.html',
            context={
                'top_row': foti[:3],
                'bottom_row': foti[3:],
                'profile': profile,
                'title': 'Photos',
            },
        )


class ScrittoListView(View):
    def get(self, request):

        scritti = Profile.objects.first().writing_features.all()
        profile = Profile.objects.first()

        return render(
            request=request,
            template_name='pages/generic-list.html',
            context={
                'top_row': scritti[:3],
                'bottom_row': scritti[3:],
                'profile': profile,
                'title': 'Writing'
            },
        )
