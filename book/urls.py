from django.urls import path

from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:danie_id>/', views.przepis, name='przepis'),
    path('skladniki/', views.lista_skladnikow, name='lista_skladnikow')
]