from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

app_name = "departamento_app"

urlpatterns = [
   path('listar-departamentos/', 
      views.ListarDepartamentos.as_view(), 
      name = 'listardepartamentos'),
   path('nuevo-empleado-y-departamento/', 
      views.NuevoEmpleadoYDepartamento.as_view(), 
      name = 'nuevoempleadoydepartamento')
]