from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from recipes.views import home
from . import views

urlpatterns = [
    path('', views.home ),
]
