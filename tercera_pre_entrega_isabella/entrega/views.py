from django.shortcuts import render
from django.http import HttpResponse
from entrega.models import Autos, Camiones, Motos

# Create your views here.

def inicio(request):
    return render(request,"entrega/inicio.html")

def ingresar_datos(request):
    return render(request,"entrega/ingresar_datos.html")

def form_ingresar_datos_autos(request):

    if request.method == 'POST':

        ingresar_datos = Autos(modelo=request.POST ['modelo'], matricula=request.POST ['matricula'])

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

def buscar_datos(request):
    query_modelo = request.GET.get('modelo', '')
    query_matricula = request.GET.get('matricula', '')
    resultados_autos = Autos.objects.filter(modelo__icontains=query_modelo, matricula__icontains=query_matricula)
    resultados_camiones = Camiones.objects.filter(modelo__icontains=query_modelo, matricula__icontains=query_matricula)
    resultados_motos = Motos.objects.filter(modelo__icontains=query_modelo, matricula__icontains=query_matricula)
    return render(request, "entrega/buscar_datos.html", {'resultados_autos': resultados_autos, 'resultados_camiones': resultados_camiones, 'resultados_motos': resultados_motos})
