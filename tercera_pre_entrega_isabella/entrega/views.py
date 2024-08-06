from django.shortcuts import render
from django.http import HttpResponse
from entrega.models import Autos, Camiones, Motos

# Create your views here.

def inicio(request):
    return render(request,"entrega/inicio.html")

def ingresar_datos(request):
    return render(request,"entrega/ingresar_datos.html")

def buscar_datos(request):
    return render(request, "entrega/buscar_datos.html")

def form_ingresar_datos_autos(request):

    if request.method == 'POST':

        ingresar_datos = Autos(modelo=request.POST ['modelos'], matricula=request.POST ['matricula'])

        ingresar_datos.save()

        return render(request, "entrega/inicio.html")
    return render(request, "entrega/ingresar_datos.html")

def form_ingresar_datos_camiones(request):
    if request.method == 'POST':
        ingresar_datos = Camiones(modelo=request.POST ['modelo'], matricula=request.POST ['matricula'])
        ingresar_datos.save()
        return render(request, "entrega/inicio.html")
    return render(request, "entrega/ingresar_datos.html")

def form_ingresar_datos_motos(request):
    if request.method == 'POST':
        ingresar_datos = Motos(modelo=request.POST ['modelo'], matricula=request.POST ['matricula'])
        ingresar_datos.save()
        return render(request, "entrega/inicio.html")
    return render(request, "entrega/ingresar_datos.html")
