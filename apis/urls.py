from django.contrib import admin
from django.urls import path
from .views import apis, keyword

app_name='apis'

urlpatterns = [
    path('populate-apis/', apis),
    path('keyword/', keyword),
]