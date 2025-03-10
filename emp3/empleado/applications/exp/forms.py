from django import forms # type: ignore
from .models import Prueba

class PruebasForm(forms.ModelForm):

   class Meta:
      model = Prueba
      fields = ('titulo',
                'subtitulo',
                'cantidad')
      widgets = {
         'titulo': forms.TextInput(
            attrs = {
               'placeholder': 'Ingrese texto aqui',
            }
         )
      }

   def clean_cantidad(self):
      cantidad = self.cleaned_data['cantidad']
      if cantidad < 10:
         raise forms.ValidationError('Ingrese un valor mayor o igual a 10')
      return cantidad      
