from django.contrib import admin
from django.urls import path
from .views import apis, keyword, category, ordered_list, item

app_name='apis'

urlpatterns = [
    path('populate-apis/', apis.as_view()),
    path('keyword/<key>/', keyword.as_view()),
    path('category/<category>/', category.as_view()),
    path('ordered-list/', ordered_list.as_view()),
    path('item/<int:id>/', item.as_view())
]