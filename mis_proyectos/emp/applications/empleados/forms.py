from django import forms # type: ignore
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
   """Form definition for MODELNAME."""

   class Meta:
      """Meta definition for MODELNAMEform."""

      model = Empleado
      fields = ('first_name',
                'last_name',
                'job',
                'departamento',
                'avatar',
                'habilidades'
               )
      widgets ={
                "habilidades": forms.CheckboxSelectMultiple()
               }


