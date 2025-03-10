from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

app_name = "empleado_app"

urlpatterns = [
   path('', 
      views.Inicio.as_view(), 
      name = 'inicio'),
   path('listar-todos-los-empleados', 
      views.EmpleadosListView.as_view(),
      name = 'listartodoslosempleados'),
   path('listar-por-departamento', 
      views.ListaPorDeptListView.as_view()),
   path('empleado-por-kword/<pk>', 
      views.EmpleadoPorKword.as_view(),
      name = 'empleadoporkword'),

   # url encargada del ultimo requerimiento:
   path('empleadopordepa/<sn>', 
      views.EmpleadoPorDepa.as_view(),
      name = 'empleadopordepa'),  

   path('buscar-habi-por-emp', 
      views.ListEmpByHabili.as_view()),
   path('detalles-del-emp/<pk>', 
      views.DetalleDelEmpleado.as_view(),
      name = 'detallesdelemp'),
   path('crear-emp', 
      views.CrearEmpleado.as_view(), 
      name = 'crearempleado'),
   path('ingreso-exitoso', 
      views.IngresoExitoso.as_view(), 
      name = 'exito'),
   path('actualizar-empleado/<pk>', 
      views.ActualizarEmpleado.as_view(), 
      name = 'actualizarempleado'),
   path('eliminar-empleado/<pk>', 
      views.EliminarEmpleado.as_view(), 
      name = 'eliminarempleado'),
   path('admin-empleados/', 
      views.AdminEmpleados.as_view(),
      name = 'adminempleados'),
]