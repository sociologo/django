from django.shortcuts import render # type: ignore
from django.views.generic.edit import FormView # type: ignore
from .forms import EmpleadoYDepartamento
from applications.empleados.models import Empleado
from .models import Departamento
from django.urls import reverse_lazy # type: ignore
from django.views.generic import ListView # type: ignore


class NuevoEmpleadoYDepartamento(FormView):
   template_name = 'depa/nuevoempleadoydepartamento.html'
   form_class = EmpleadoYDepartamento
   success_url = reverse_lazy('empleado_app:exito')

   def form_valid(self, form):

      depa = Departamento(
         name = form.cleaned_data['departamento'],
         short_name = form.cleaned_data['shortname']
      )
      depa.save()

      nombre = form.cleaned_data['nombre']
      apellido = form.cleaned_data['apellido']
      Empleado.objects.create(
         first_name = nombre,
         last_name = apellido,
         job = '1',
         departamento = depa
      )
      return super(NuevoEmpleadoYDepartamento, self).form_valid(form)
   

class ListarDepartamentos(ListView):
    model = Departamento
    template_name = "depa/listardepartamentos.html"
    context_object_name = "departamentos"

