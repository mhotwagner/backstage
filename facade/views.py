from django.http import HttpResponse
from django.shortcuts import render


def status(request):
    return HttpResponse('OK')
