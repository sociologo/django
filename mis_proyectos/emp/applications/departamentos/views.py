from django.shortcuts import render # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views.generic.edit import( # type: ignore
    FormView
)
from django.views.generic import( # type: ignore
    TemplateView
)
from .forms import NewDepartmentForm
from applications.empleados.models import Empleado
from .models import Departamento

from django.views.generic import( # type: ignore
    ListView
)

class DepartamentoView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departments"

class SuccessView(TemplateView):

    template_name = 'departamento/success.html'

class NewDepartmentView(FormView):

    template_name = "departamento/new_department.html"
    form_class = NewDepartmentForm
    success_url = reverse_lazy('department_app:department_list')

    def form_valid(self, form):

        depa = Departamento(
            name = form.cleaned_data["departamento"],
            short_name = form.cleaned_data["shortname"]
            )
        depa.save()
        
        nombre = form.cleaned_data["nombre"]
        apellido = form.cleaned_data["apellido"]

        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = "1",
            departamento = depa
        )    
        return super(NewDepartmentView, self).form_valid(form)



