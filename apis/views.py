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
    return render(request, 'todos.html', {'content':content})
