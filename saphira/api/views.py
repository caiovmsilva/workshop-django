import datetime

from django.http import HttpResponse, JsonResponse

def get_datetime(request):
    return HttpResponse(datetime.datetime.utcnow())

def get_texto(request, texto):
    return HttpResponse("O texto escolhido foi '{}'".format(texto))
