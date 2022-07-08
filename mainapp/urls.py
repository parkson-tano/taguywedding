from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'taguy'
urlpatterns = [
    path('', index, name='index'),
]
