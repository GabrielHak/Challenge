from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.views.generic import View
from django.shortcuts import render
from apis.models import Apis
import requests

# Create your views here.
res = requests.get('https://api.publicapis.org/entries')
content = res.json()

class apis(View):
    def post(self, request, *args, **kwargs):
        entries = content["entries"]
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
    
    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound()

class keyword(View):
    def post(self, request, key, *args, **kwargs):
        entries = list(Apis.objects.values())
        listTo = []
        for entrie in entries:
            if entrie['api'][0] == key.capitalize() or entrie['api'][0] == key.casefold():
                listTo.append(entrie)
        return JsonResponse(listTo, safe=False)

    def get(self, request, key, *args, **kwargs):
        return HttpResponseNotFound()

class category(View):
    def post(self, request, category, *args, **kwargs):
        entries = list(Apis.objects.filter(category=category.capitalize()).values())
        return JsonResponse(entries, safe=False)

    def get(self, request, category, *args, **kwargs):
        return HttpResponseNotFound()

class ordered_list(View):
    def post(self, request, *args, **kwargs):
        entries = list(Apis.objects.order_by('id').values())
        return JsonResponse(entries, safe=False)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotFound()

class item(View):
    def post(self, request, id, *args, **kwargs):
        entries = list(Apis.objects.filter(id=id).values())
        return JsonResponse(entries, safe=False)

    def get(self, request, id, *args, **kwargs):
        return HttpResponseNotFound()
