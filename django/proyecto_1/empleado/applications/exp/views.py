from django.shortcuts import render # type: ignore
from django.urls import reverse_lazy # type: ignore
# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView # type: ignore

from applications.exp.forms import PruebaForm # type: ignore

from .models import Prueba

class IndexView(TemplateView):
    template_name = 'exp/home.html'

class Prueba_ListView(ListView):
    template_name = 'exp/lista.html'
    queryset = ['uno','dos','tres']
    context_object_name = 'lista_prueba'
 
class MODEL_PRUEBAListView(ListView):
    model = Prueba
    template_name = "exp/pruebas.html"
    context_object_name = 'lista_prueba'

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "exp/add.html"
    form_class = PruebaForm
    success_url = "reverse_lazy('exp_app:correcto')"

class SuccessView(TemplateView):
    template_name = 'exp/success.html'   
    


