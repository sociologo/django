from django.shortcuts import render # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views.generic import( # type: ignore
   ListView, 
   DetailView,
   CreateView,
   TemplateView,
   UpdateView,
   DeleteView) # type: ignore

from .models import Empleado
from .forms import EmpleadoForm
class Inicio(TemplateView):
    template_name = "inicio.html"

class EmpleadosListView(ListView):
   template_name = "empleado/list_all.html"
   context_object_name = 'lista'
   paginate_by = 4
   ordering = 'first_name'

   def get_queryset(self):
      palabra_clave = self.request.GET.get('kword', '')
      lista = Empleado.objects.filter(
         full_name__icontains = palabra_clave
      )
      return lista

class ListaPorDeptListView(ListView):
   template_name = "empleado/listapordept.html"
   queryset = Empleado.objects.filter(
      departamento__short_name = 'mate'
   )

class EmpleadoPorKword(ListView):
   template_name = "empleado/empleadoporkword.html"
   context_object_name = 'empleadoporkword'

   def get_queryset(self):
      palabra_clave = self.request.GET.get('kword', '')
      empleado = Empleado.objects.filter(
         departamento__short_name = palabra_clave
      )
      return empleado.all()
   

# Vista encargada del ultimo requerimiento:

class EmpleadoPorDepa(ListView):
   template_name = "empleado/empleadopordepa.html"
   context_object_name = 'empleadopordepa'

   def get_queryset(self):
      palabra_clave = self.kwargs['sn'] # type: ignore
      lista = Empleado.objects.filter(
         departamento__short_name = palabra_clave
      )
      return lista 


class ListEmpByHabili(ListView):
   template_name = "empleado/listempbyhabili.html"
   context_object_name = 'listempbyhabili'

   def get_queryset(self):
      palabra_clave = self.request.GET.get('kword', None)
      if palabra_clave is not None:
         palabra_clave = int(palabra_clave)
         empleado = Empleado.objects.get(id = palabra_clave)
         return empleado.habilidades.all()
    
class DetalleDelEmpleado(DetailView):
   model = Empleado
   template_name = "empleado/detalledelempleado.html"
   context_object_name = 'detalledelempleado'

   def get_context_data(self, **kwargs):
       context = super(DetalleDelEmpleado, self).get_context_data(**kwargs)
       context['titulo'] = 'Empleado del mes' 
       return context
   
class IngresoExitoso(TemplateView):
    template_name = "empleado/ingresoexitoso.html"

class CrearEmpleado(CreateView):
   model = Empleado
   template_name = "empleado/crearempleado.html"
   form_class = EmpleadoForm
   success_url = reverse_lazy('empleado_app:adminempleados')

   def form_valid(self, form):
      empleado = form.save(commit = False)
      empleado.full_name = empleado.first_name + ' ' + empleado.last_name
      empleado.save()
      return super(CrearEmpleado, self).form_valid(form)
   

class ActualizarEmpleado(UpdateView):
   model = Empleado
   template_name = "empleado/actualizarempleado.html"
   fields = ['first_name',
             'last_name',
             'job',
             'departamento',
             'habilidades'] 
   success_url = reverse_lazy('empleado_app:adminempleados')


class EliminarEmpleado(DeleteView):
   model = Empleado
   template_name = "empleado/eliminarempleado.html"
   success_url = reverse_lazy('empleado_app:adminempleados')
   context_object_name = 'eliminarempleado'

class AdminEmpleados(ListView):
   template_name = "empleado/adminempleados.html"
   context_object_name = 'adminempleados'
   paginate_by = 10
   ordering = 'first_name'
   model = Empleado