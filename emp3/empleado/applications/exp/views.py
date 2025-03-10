from django.views.generic import ( # type: ignore
   CreateView)  # type: ignore

from .models import Prueba
from .forms import PruebasForm
from django.urls import reverse_lazy # type: ignore

class PruebasCreateView(CreateView):
   model = Prueba
   template_name = "home/pruebas.html"
   form_class = PruebasForm
   success_url = reverse_lazy('empleado_app:exito')