from django.urls import path # type: ignore
from . import views

urlpatterns = [
   path('pruebas/', 
      views.PruebasCreateView.as_view(), 
      name = 'pruebas')
]
