from django.shortcuts import render

# Create your views here.


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

