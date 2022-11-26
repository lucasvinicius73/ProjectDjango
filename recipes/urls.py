from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from recipes.views import home

from . import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('recipes/search/', views.search, name="search"),
    path('recipes/category/<int:category_id>/', views.category, name="category" ),
    path('recipes/<int:id>/', views.recipe, name="recipe" ),
    path('', views.home, name="home" ),
]
