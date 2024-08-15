from django.urls import path
from entrega.views import inicio, ingresar_datos, buscar_datos, form_ingresar_datos_autos, form_ingresar_datos_camiones, form_ingresar_datos_motos

from django.urls import path
from entrega.views import inicio, ingresar_datos, buscar_datos, form_ingresar_datos_autos, form_ingresar_datos_camiones, form_ingresar_datos_motos, bd_vehiculos

urlpatterns = [
    path('', inicio, name="inicio"),
    path('ingresar_datos', ingresar_datos, name="ingresar_datos"),
    path('buscar_datos', buscar_datos, name="buscar_datos"),
    path('bd_vehiculos', bd_vehiculos, name="bd_vehiculos"),
    path('form_ingresar_datos_autos', form_ingresar_datos_autos, name="form_ingresar_datos_autos"),
    path('form_ingresar_datos_camiones', form_ingresar_datos_camiones, name="form_ingresar_datos_camiones"),
    path('form_ingresar_datos_motos', form_ingresar_datos_motos, name="form_ingresar_datos_motos"),
]