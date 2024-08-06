from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request,"entrega/inicio.html")

def ingresar_datos(request):
    return render(request,"entrega/ingresar_datos.html")

def buscar_datos(request):
    return render(request, "entrega/buscar_datos.html")
