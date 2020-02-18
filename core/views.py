# import json
from django.shortcuts import render
from django.http import JsonResponse
from core import applicationIOT


def weather(request):
    data = applicationIOT.get_data_device()
    data = eval(str(data))

    temp = data['temperature']
    context = {
        'temp': temp['value']
    }
    return render(request, 'core/index.html', context)


def api(request):
    return JsonResponse(applicationIOT.get_data_device(), safe=False)

