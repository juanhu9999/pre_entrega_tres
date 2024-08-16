from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from .models import Autos, Camiones, Motos
from django.contrib.auth.models import User
from django.views import generic

@method_decorator(staff_member_required, name='dispatch')
class IngresarDatosView(TemplateView):
    template_name = "entrega/ingresar_datos.html"

# Create your views here.

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'entrega/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = AuthenticationForm()
        return context

class InicioView(TemplateView):
    template_name = "entrega/inicio.html"

class BuscarDatosView(TemplateView):
    template_name = "entrega/buscar_datos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modelo = self.request.GET.get('modelo')
        matricula = self.request.GET.get('matricula')

        if modelo or matricula:
            context['resultados_autos'] = Autos.objects.filter(modelo__icontains=modelo, matricula__icontains=matricula)
            context['resultados_camiones'] = Camiones.objects.filter(modelo__icontains=modelo, matricula__icontains=matricula)
            context['resultados_motos'] = Motos.objects.filter(modelo__icontains=modelo, matricula__icontains=matricula)

        return context

class BDVehiculosView(TemplateView):
    template_name = "entrega/bd_vehiculos.html"

class ResultadosView(TemplateView):
    template_name = "entrega/resultados.html"

class AboutMeView(TemplateView):
    template_name = "entrega/aboutme.html"

class CrearAutosView(CreateView):
    model = Autos
    template_name = "entrega/crear_autos.html"
    success_url = reverse_lazy('resultados')
    fields = ['modelo', 'matricula']

class ActualizarAutosView(UpdateView):
    model = Autos
    template_name = "entrega/actualizar.html"
    success_url = reverse_lazy('resultados')
    fields = ['modelo', 'matricula']

class BorrarAutosView(DeleteView):
    model = Autos
    template_name = "entrega/borrar.html"
    success_url = reverse_lazy('resultados')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

class CrearCamionesView(CreateView):
    model = Camiones
    template_name = "entrega/crear_camiones.html"
    success_url = reverse_lazy('resultados')
    fields = ['modelo', 'matricula']

class ActualizarCamionesView(UpdateView):
    model = Camiones
    template_name = "entrega/actualizar.html"
    success_url = reverse_lazy('resultados')
    fields = ['modelo', 'matricula']

class BorrarCamionesView(DeleteView):
    model = Camiones
    template_name = "entrega/borrar.html"
    success_url = reverse_lazy('resultados')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())

class CrearMotosView(CreateView):
    model = Motos
    template_name = "entrega/crear_motos.html"
    success_url = reverse_lazy('resultados')
    fields = ['modelo', 'matricula']

class ActualizarMotosView(UpdateView):
    model = Motos
    template_name = "entrega/actualizar.html"
    success_url = reverse_lazy('resultados')
    fields = ['modelo', 'matricula']

class BorrarMotosView(DeleteView):
    model = Motos
    template_name = "entrega/borrar.html"
    success_url = reverse_lazy('resultados')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
    
class ActualizarAutosView(UpdateView):
    model = Autos
    template_name = "entrega/actualizar_autos.html"
    fields = ['modelo', 'matricula']
    success_url = reverse_lazy('buscar_datos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['auto'] = self.get_object()
        return context

class ActualizarCamionesView(UpdateView):
    model = Camiones
    template_name = "entrega/actualizar_camiones.html"
    fields = ['modelo', 'matricula']
    success_url = reverse_lazy('buscar_datos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['camion'] = self.get_object()
        return context

class ActualizarMotosView(UpdateView):
    model = Motos
    template_name = "entrega/actualizar_motos.html"
    fields = ['modelo', 'matricula']
    success_url = reverse_lazy('buscar_datos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['moto'] = self.get_object()
        return context

class BDVehiculosView(TemplateView):
    template_name = "entrega/bd_vehiculos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autos'] = Autos.objects.all()
        context['camiones'] = Camiones.objects.all()
        context['motos'] = Motos.objects.all()
        return context


