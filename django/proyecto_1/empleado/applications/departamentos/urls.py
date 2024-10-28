from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

app_name = 'department_app'

urlpatterns = [
    path('department-list/', 
        views.DepartamentoView.as_view(), 
        name = 'department_list'
         ),
    path('success/', 
         views.SuccessView.as_view(), 
         name = 'correcto'
         ),
    path('new-department/', 
        views.NewDepartmentView.as_view(), 
        name = 'new_department'
        )
]
