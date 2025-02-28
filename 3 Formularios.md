# Formularios

Script de arranque:

```bash
C:\Users\chris> cd /
C:\> cd mis_entornos/entorno_3/Scripts
C:\mis_entornos\entorno_3\Scripts> activate
(entorno_3) C:\mis_entornos\entorno_3\Scripts> cd \mis_proyectos\emp3\empleado
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

[Working with forms](https://docs.djangoproject.com/en/5.1/topics/forms/)

## Índice

* [El archivo forms.py](#1-El-archivo-forms.py)
  * [1 Formularios forms.ModelForm](#1-Formularios-formsModelForm)
  * [2 Formularios forms.Form](#2-Formularios-formsForm)

## 1 Construyento una CreateView de ejemplo

Vamos a nuestra app **exp** que hemos utilizado para realizar pruebas y construimos una vista CreateView

```python
from django.db import models # type: ignore

class Prueba(models.Model):
   titulo = models.CharField(max_length=30)
   subtitulo = models.CharField(max_length=30)
   cantidad = models.IntegerField()
```

```python
from django.views.generic import ( # type: ignore
   CreateView)  # type: ignore

from .models import Prueba
from django.urls import reverse_lazy # type: ignore

class PruebasCreateView(CreateView):
   model = Prueba
   template_name = "home/pruebas.html"
   fields = ['titulo','subtitulo','cantidad']
   success_url = reverse_lazy('empleado_app:exito')
```

```python
<h1> Prueba </h1>

<form method = "POST">{% csrf_token %}
   {{form.as_p}}
   <button type="submit">
      Agregar
   </button>
</form>
```

```python
from django.urls import path # type: ignore
from . import views

urlpatterns = [
   path('pruebas/', 
      views.PruebasCreateView.as_view(), 
      name = 'pruebas')
]
```

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include("applications.empleados.urls")),
   path('', include("applications.exp.urls")),
]
```

Verifiquemos

![image](https://github.com/user-attachments/assets/6a1f36c4-5983-4290-b181-f843d007d5e3)
![image](https://github.com/user-attachments/assets/7d52dc2f-ae13-40ba-9327-1fbbe92ac71e)

## 2 El archivo forms.py

### 2.1 La clase ModelForm

Nuestra tarea será personalizar los campos del formulario. Para ello:

1 dentro de la app **exp**, creamos un nuevo archivo llamado **forms.py** y dentro de él escribimos el siguiente código:

```python
from django import forms # type: ignore
from .models import Prueba

class PruebasForm(forms.ModelForm):

   class Meta:
      model = Prueba
      fields = ('titulo',
                'subtitulo',
                'cantidad')
```

2 Importamos la clase PruebasForm en nuestra vista y las **vinculamos**:

```python
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
```

#### 2.1.1 Validaciones con ModelForm

Podemos hacer validaciones personalizadas en Django con el metodo `clean_`.

En Django, el prefijo `clean_` se utiliza en formularios para definir métodos de validación personalizados para campos específicos. Estos métodos permiten agregar reglas adicionales más allá de las validaciones predeterminadas de Django.

`cantidad = self.cleaned_data['cantidad']` obtiene el valor del campo cantidad desde el diccionario `cleaned_data`, que contiene los datos ingresados por el usuario ya validados por las verificaciones iniciales de Django.

```python
from django import forms # type: ignore
from .models import Prueba

class PruebasForm(forms.ModelForm):

   class Meta:
      model = Prueba
      fields = ('titulo',
                'subtitulo',
                'cantidad')

   def clean_cantidad(self):
      cantidad = self.cleaned_data['cantidad']
      if cantidad < 10:
         raise forms.ValidationError('Ingrese un valor mayor o igual a 10')
      return cantidad   
```

Todas las validaciones que hagas para los campos de la base de datos deben hacerse aqui en los formularios.

#### 2.1.2 Personalizaciones con ModelForm (widgets)

Este código está configurando un widget para un formulario. Los widgets son responsables de cómo se representa un campo en el formulario en el HTML generado. En este caso, se está usando un TextInput, que crea un campo de entrada de texto personalizado.

`'titulo': forms.TextInput(...)` indica que el campo llamado titulo en el formulario utilizará el widget TextInput. `TextInput` se traduce en un campo <input type="text"> en el HTML.

`attrs = {...}` es un diccionario que define los atributos HTML personalizados para el widget. En este caso:

`placeholder`, que añade un texto dentro del campo de entrada que desaparece cuando el usuario comienza a escribir. Aquí el texto sería: "Ingrese texto aquí".

```python
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
 ```

<br>
<br>
<br>
<br>

me faltan las clase 61, 62, 63.
27 febrero.

<br>
<br>
<br>
<br>
---
---

### 2.2 La clase Form y la vista FormView

Con ModelForm, ahorras tiempo porque los campos se generan automáticamente basados en un modelo, estando diseñado específicamente para trabajar con modelos de Django. Con Form, defines los campos manualmente y es más adecuado para formularios independientes que no se relacionan directamente con un modelo de base de datos.

Vamos a utilizar un formulario Form para ingresar simultaneamente datos en los modelos **empleado** y **departamento**.

1 En la aplicación **departamentos** construiremos un nuevo forms.py en el que registraremos campos de un departamento y un empleado asociado a él:

```python
from django import forms # type: ignore

class EmpleadoYDepartamento(forms.Form):
   nombre = forms.CharField(max_length=50)
   apellido = forms.CharField(max_length=50)
   departamento = forms.CharField(max_length=50)
   shortname = forms.CharField(max_length=20)
```
2 Construimos una vista FormView.

```python
from django.shortcuts import render # type: ignore
from django.views.generic.edit import FormView # type: ignore
from .forms import EmpleadoYDepartamento
from applications.empleados.models import Empleado
from .models import Departamento
from django.urls import reverse_lazy # type: ignore

class NuevoEmpleadoYDepartamento(FormView):
   template_name = 'depa/nuevoempleadoydepartamento.html'
   form_class = EmpleadoYDepartamento
   success_url = reverse_lazy('empleado_app:exito')

   def form_valid(self, form):

      depa = Departamento(
         name = form.cleaned_data['departamento'],
         shortname = form.cleaned_data['shortname']
      )
      depa.save()

      nombre = form.cleaned_data['nombre']
      apellido = form.cleaned_data['apellido']
      Empleado.objects.create(
         first_name = nombre,
         last_name = apellido,
         job = '1',
         departamento = depa
      )
      return super(NuevoEmpleadoYDepartamento, self).form_valid(form)
```

CreateView funciona sobre un solo modelo; FormView no.

3 Activamos la url de la vista

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

app_name = "departamento_app"

urlpatterns = [
   path('nuevo-empleado-y-departamento/', 
      views.NuevoEmpleadoYDepartamento.as_view(), 
      name = 'nuevoempleadoydepartamento')
]
```

4 Creamos el template **nuevoempleadoydepartamento.html**

```html
<h1> Registrar empleado y departamento </h1>

<form method = "POST">{% csrf_token %}
   <h3>
      Datos del empleado
   </h3>
   <p>
      {{form.nombre}}
   </p>
      {{form.apellido}}
   <h3>
      Datos del departamento
   </h3>
   <p>
      {{form.departamento}}
   </p>
      {{form.shortname}}
   <button type="submit">
      Agregar
   </button>
</form>
```

5 Registramos la app departamento en el sistema general de urls de django:

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include("applications.empleados.urls")),
   path('', include("applications.exp.urls")),
   path('', include("applications.departamentos.urls")),
]
``

6 Verificamos:

![image](https://github.com/user-attachments/assets/e53329e7-c69c-4f8f-9a2b-016d3b784521)












