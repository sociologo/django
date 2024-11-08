from django.http import HttpRequest, HttpResponse # type: ignore
from django.shortcuts import render # type: ignore

from django.urls import reverse_lazy # type: ignore

from django.views.generic import( # type: ignore
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

from .models import Empleado
from .models import Departamento
from .forms import EmpleadoForm

class ListEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    model = Empleado
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'

class InicioView(TemplateView):
    template_name = "inicio.html"

# 1 Listar todos los empleados de la empresa

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    # model = Empleado
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'lista'

    def get_queryset(self):
        # obtengo el nombre del departamento:
        palabra_clave = self.request.GET.get("kword", '')
        # quiero todos los empleados que pertenezcan a tal departamento:
        lista = Empleado.objects.filter(
            first_name__icontains = palabra_clave
        )
        return lista

# 2 Listar todos los empleados de la empresa por departamento

class ListAllByDept(ListView):
    template_name = 'persona/AllByDept.html'
    queryset = Empleado.objects.filter(
        departamento__short_name = 'ciencias matemáticas'
    )


class ListByDept(ListView):
    template_name = "persona/listbydept.html"
    context_object_name = "empleadosbydept"
    def get_queryset(self):
        area = self.kwargs["shortname"]
        # quiero todos los empleados que pertenezcan a tal departamento:
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista


# 3 Listar todos los empleados que pertenezcan a un departamento mediante urls con un filtro en una caja de texto.

class ListEmpByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        # obtengo el nombre del departamento:
        palabra_clave = self.request.GET.get("kword", '')
        # quiero todos los empleados que pertenezcan a tal departamento:
        empleado = Empleado.objects.filter(
            departamento__short_name = palabra_clave
        )
        return empleado.all()
 
class ListEmpByHabili(ListView):
    template_name = 'persona/by_habili.html'
    context_object_name = 'empleados_by_habili'

    def get_queryset(self):
        try:        
            # obtengo el id del empleado:
            id_del_emp = self.request.GET.get("kword", '')
            id_del_emp = int(id_del_emp)
        except ValueError:
            id_del_emp = 4 
        try:
            # obtengo el id del empleado:
            empleado = Empleado.objects.get(id=id_del_emp)
            # quiero todas las habilidades que pertenezcan a tal empleado:
            return empleado.habilidades.all()
        except Empleado.DoesNotExist:
            # Manejar el caso donde el empleado no existe
            return []   

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    context_object_name = 'detail_empleado'
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    
class SuccessView(TemplateView):
    template_name = 'persona/success.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def form_valid(self,form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ['first_name',
              'last_name',
              'job',
              'departamento',
              'habilidades']
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def post(self, request: HttpRequest, *args: str, **kwargs: reverse_lazy) -> HttpResponse: # type: ignore
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('empleado_app:empleados_admin')