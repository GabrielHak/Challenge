from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from apis.models import Apis
import requests

# Create your views here.
res = requests.get('https://api.publicapis.org/entries')
content = res.json()

def apis(request):
    entries = content["entries"]
    # list = []
    for entrie in entries:
        api = entrie["API"]
        description = entrie["Description"]
        auth = entrie["Auth"]
        https = entrie["HTTPS"]
        cors = entrie["Cors"]
        link = entrie["Link"]
        category = entrie["Category"]
        Apis(api=api, description=description, auth=auth, https=https, cors=cors, link=link, category=category).save()

    return HttpResponse(api)

def keyword(request):
    entries = list(Apis.objects.values())
    return JsonResponse(entries, safe=False)

def category(request, category):
    entries = list(Apis.objects.filter(category=category).values())
    return JsonResponse(entries, safe=False)

def ordered_list(request):
    entries = list(Apis.objects.order_by('id').values())
    return JsonResponse(entries, safe=False)

def item(request, id):
    entries = list(Apis.objects.filter(id=id).values())
    return JsonResponse(entries, safe=False)
