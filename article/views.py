from django.shortcuts import render

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Rassilka
# Create your views here.
from .models import Rassilka
import json
import datetime

#редактирование данных
#@renderer_classes((JSONRenderer))
@csrf_exempt
def index(request):
    if request.method == 'POST':
        results = request.POST
        date_new = results["date_start"]
        id_ras = results["id"]
        ras = Rassilka.objects.get(id=id_ras)
        d = datetime.datetime.strptime(f"{date_new}", "%Y-%m-%dT%H:%M:%S")
        ras.date_start = d
        ras.save()
    return JsonResponse({'status': '1'}, status=200)

#https://djbook.ru/ch07s02.html

