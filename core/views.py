from django.shortcuts import render
from django.http import JsonResponse
from core import applicationIOT


def temperatura(request):
    context = {
        'scopo': applicationIOT.get_data_device(),
    }
    return render(request, 'core/index.html', context)


def api(request):
    return JsonResponse(applicationIOT.get_data_device(), safe=False)

