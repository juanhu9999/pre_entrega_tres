from django.urls import path
from entrega.views import inicio, ingresar_datos, buscar_datos

urlpatterns = [
    path('', inicio, name="inicio"),
    path('ingresar_datos', ingresar_datos, name="ingresar_datos"),
    path('buscar_datos', buscar_datos, name="buscar_datos"),

]