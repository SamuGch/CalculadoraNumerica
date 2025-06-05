from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Aquí puedes agregar otras vistas si lo deseas, por ejemplo:
    # path('resultado/', views.resultado, name='resultado'),
]
