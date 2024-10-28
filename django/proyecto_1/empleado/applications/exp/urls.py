from django.urls import path # type: ignore
from . import views

app_name = 'exp_app'

urlpatterns = [
    path('home/', 
         views.IndexView.as_view()),
    path('lista/', 
         views.Prueba_ListView.as_view()),
    path('lista_prueba/', 
         views.MODEL_PRUEBAListView.as_view()),
    path('add/', 
         views.PruebaCreateView.as_view(), 
         name = 'exp_add'),
    path('success/', 
         views.SuccessView.as_view(), 
         name = 'correcto'),
]
