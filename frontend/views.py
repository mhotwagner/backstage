from django.shortcuts import render

# Create your views here.
from foti.models import Foto


def index(request):
    return render(
        request=request,
        template_name='pages/index.html',
    )


def demo(request):
    return render(
        request=request,
        template_name='pages/demo.html',
    )


def photo_demo(request):
    print('in here')
    photos = Foto.objects.all()[:6]

    return render(
        request=request,
        template_name='pages/photo-demo.html',
        context={'photos_a': photos[:3], 'photos_b': photos[3:6], }
    )