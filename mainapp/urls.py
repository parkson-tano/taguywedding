from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'taguy'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
