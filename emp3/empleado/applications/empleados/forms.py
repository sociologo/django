from django import forms # type: ignore
from .models import Empleado # type: ignore

class EmpleadoForm(forms.ModelForm):

   class Meta:

      model = Empleado
      fields = ('first_name',
                'last_name',
                'job',
                'departamento',
                'avatar',
                'habilidades',
                )
      widgets = {
         'habilidades': forms.CheckboxSelectMultiple()
      }
