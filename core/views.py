from django.shortcuts import render
from urllib.request import urlopen, Request
from core import applicationIOT
from django.http import JsonResponse


def temperatura(request):
    context = {
        'scopo': applicationIOT.get_data_device(),
    }
    return render(request, 'core/index.html', context)


def api(request):
    return JsonResponse(applicationIOT.get_data_device(), safe=False)

