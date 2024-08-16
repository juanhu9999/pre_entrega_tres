from django.urls import path
from .views import (
    InicioView, BDVehiculosView, AboutMeView, IngresarDatosView, BuscarDatosView,
    CrearAutosView, ActualizarAutosView, BorrarAutosView,
    CrearCamionesView, ActualizarCamionesView, BorrarCamionesView,
    CrearMotosView, ActualizarMotosView, BorrarMotosView,
    ResultadosView, SignUp,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', InicioView.as_view(), name="inicio"),
    path('bd_vehiculos', BDVehiculosView.as_view(), name="bd_vehiculos"),
    path('aboutme', AboutMeView.as_view(), name="aboutme"),
    path('signup/', SignUp.as_view(), name='signup'),
    path('ingresar_datos/', IngresarDatosView.as_view(), name='ingresar_datos'),
    path('buscar_datos/', BuscarDatosView.as_view(), name='buscar_datos'),
    path('crear/autos/', CrearAutosView.as_view(), name="crear_autos"),
    path('actualizar/autos/<int:pk>/', ActualizarAutosView.as_view(), name="actualizar_autos"),
    path('borrar/autos/<int:pk>/', BorrarAutosView.as_view(), name="borrar_autos"),
    path('crear/camiones/', CrearCamionesView.as_view(), name="crear_camiones"),
    path('actualizar/camiones/<int:pk>/', ActualizarCamionesView.as_view(), name="actualizar_camiones"),
    path('borrar/camiones/<int:pk>/', BorrarCamionesView.as_view(), name="borrar_camiones"),
    path('crear/motos/', CrearMotosView.as_view(), name="crear_motos"),
    path('actualizar/motos/<int:pk>/', ActualizarMotosView.as_view(), name="actualizar_motos"),
    path('borrar/motos/<int:pk>/', BorrarMotosView.as_view(), name="borrar_motos"),
    path('resultados/', ResultadosView.as_view(), name='resultados'),
    path('login/', auth_views.LoginView.as_view(template_name='entrega/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]