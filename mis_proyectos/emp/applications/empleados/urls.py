from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

app_name = 'empleado_app'

urlpatterns = [
   path('lista-empleados-admin/', 
         views.ListEmpleadosAdmin.as_view(),
         name = 'empleados_admin'),

   path('empleadosbydept/<shortname>/', 
         views.ListByDept.as_view(),
         name = 'empleados_by_dept'),
   path('listar-todo-empleados/', 
         views.ListAllEmpleados.as_view(),
         name = 'empleados_all'),
   path('listar-por-area/', 
         views.ListAllByDept.as_view(),
         name = 'empleados_area'),
   path('listar-por-area-por-kword/', 
         views.ListEmpByKword.as_view()),
   path('buscar-emp-por-habili/', 
         views.ListEmpByHabili.as_view()),
   path('ver-detalles/<pk>', 
         views.EmpleadoDetailView.as_view(),
         name = "empleado_detail"),

   path('add-empleado/', 
         views.EmpleadoCreateView.as_view(),
         name = "empleado_add"),

   path('success/', 
         views.SuccessView.as_view(), 
         name = 'correcto'),
   path('update-empleado/<pk>', 
        views.EmpleadoUpdateView.as_view(), 
        name = 'modificar_empleado'),
   path('delete-empleado/<pk>', 
    views.EmpleadoDeleteView.as_view(), 
    name = 'borrar_empleado'),
   path('', 
    views.InicioView.as_view(), 
    name = 'inicio')
]
