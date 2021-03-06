# import json
from django.shortcuts import render
from django.http import JsonResponse
from core import applicationIOT
from core.models import Weather


def weather(request):
    return render(request, 'core/index.html')


def api(request):
    data = applicationIOT.get_data_device()
    temp = data['temperature']
    w = Weather(temp_in=50, temp_out=50, temp_water=50, pressure=50, humidity_in=50, humidity_out=50, voltage=34.5)
    w.save()
    context = {
        'temp': temp['value']
    }
    return JsonResponse(context, safe=False)
