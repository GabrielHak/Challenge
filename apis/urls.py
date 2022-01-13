from django.contrib import admin
from django.urls import path
from .views import apis, keyword, category, ordered_list, item

app_name='apis'

urlpatterns = [
    path('populate-apis/', apis),
    path('keyword/<key>/', keyword),
    path('category/<category>/', category),
    path('ordered-list/', ordered_list),
    path('item/<int:id>/', item)
]