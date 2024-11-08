from django import forms # type: ignore
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Prueba
        fields = ('titulo',
                  'subtitulo',
                  'cantidad',)
        
        widgets = {
            "titulo" : forms.TextInput(
                attrs = {
                    "placeholder": "Ingrese texto aquí"
                }
            )
        }
        
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 10:
            raise forms.ValidationError("Ingrese un valor mayor o igual a 10")
        return cantidad
    
    
