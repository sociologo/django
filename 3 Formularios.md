# Formularios

Aca voy 26 de febrero

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




aca voy iniciando la clase 59.
26 febrero.
                
#### 2.2.1 Validaciones con ModelForm

ModelForm en Django es una clase que permite crear y personalizar formularios basados en los modelos de una aplicación de manera automática.








<br>
<br>
<br>
<br>
<br>
---

#### 2.2.2 Personalizaciones con ModelForm (widgets)

### 2.2 La clase Form y la vista FormView

Los formularios Form no están vinculados directamente a un solo modelo, por lo que nos sirven cuando deseamos ingresar registros asociados a modelos distintos. Vamos a hacer esto sobre nuestra app que contiene los modelos **empleado** y **departamento**.

1 En la aplicación **departamento** construiremos un nuevo forms.py en el que registraremos campos de un departamento y un empleado asociado a él:

![image](https://github.com/user-attachments/assets/6a881efe-9557-45e6-b2cd-5eee8b64bd78)

2 En la aplicación **departamento** construiremos la vista NewDepartmentView en el que registraremos campos de un departamento y un empleado asociado a él:

Primero, el código importa varias herramientas y componentes necesarios para trabajar con Django, incluyendo funciones para renderizar plantillas, manejar URLs, y vistas genéricas que facilitan la creación de formularios y plantillas.

Luego, se define una vista llamada SuccessView que simplemente muestra una página de éxito cuando se accede a ella. Esta página se utiliza para informar al usuario que una operación se ha completado correctamente.

La parte principal del código es una vista llamada NewDepartmentView. Esta vista se encarga de mostrar un formulario al usuario para que pueda crear un nuevo departamento. Cuando el usuario envía el formulario, la vista verifica que los datos sean válidos.

Si los datos son válidos, la vista crea un nuevo departamento utilizando la información proporcionada por el usuario. Además, también crea un nuevo empleado asociado a este departamento, utilizando otros datos del formulario. Una vez que ambos registros se han guardado correctamente en la base de datos, el usuario es redirigido a una página de éxito.

En resumen, este código maneja la creación de un nuevo departamento y un empleado asociado, asegurándose de que ambos se guarden correctamente en la base de datos y proporcionando retroalimentación al usuario sobre el éxito de la operación.

![image](https://github.com/user-attachments/assets/ccc97b4f-ae20-4e5a-a1a8-e44b39c4dfdb)

3 Construímos las URLS para activar las vistas.
![image](https://github.com/user-attachments/assets/d9628226-345e-40d6-894b-43305563e431)
![image](https://github.com/user-attachments/assets/d8cbc229-9544-45a8-943a-53162980ec38)

4 Creamos los htmls asociados a las vistas:
![image](https://github.com/user-attachments/assets/b505c12d-6305-47b1-8965-da79b552bd15)
![image](https://github.com/user-attachments/assets/4cbcdcd3-e31b-42e6-bf52-2def56165ad5)

5 Ingresamos un nuevo registro y verificamos:
![image](https://github.com/user-attachments/assets/51177aae-b6f2-42f8-8f37-5e921b7333c4)
![image](https://github.com/user-attachments/assets/9b3de7a6-dc54-4b63-a78f-d5ffeda6a009)
![image](https://github.com/user-attachments/assets/3b296643-d1d4-40fb-9b08-52ec787d6b50)












