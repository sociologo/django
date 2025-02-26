# Vistas basadas en clases. Vistas genéricas.

## Las vistas genéricas son las que nos permiten realizar el CRUD.

[ccbv.co.uk](https://ccbv.co.uk)

script de arranque:

```bash
C:\Users\chris> cd /
C:\> cd mis_entornos/entorno_3/Scripts
C:\mis_entornos\entorno_3\Scripts> activate
(entorno_3) C:\mis_entornos\entorno_3\Scripts> cd \mis_proyectos\emp3\empleado
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

## Índice

* [1 La vista ListView](#1-El-método-ListView)
  * [a) Listar todos los empleados](#a-Listar-todos-los-empleados)
  * [b) Listar todos los empleados que pertenezcan a un departamento](#b-Listar-todos-los-empleados-que-pertenezcan-a-un-departamento)
  * [c) Listar todos los empleados que pertenezcan a un departamento filtrando por medio de una caja de texto](#c-Listar-todos-los-empleados-que-pertenezcan-a-un-departamento-filtrando-por-medio-de-una-caja-de-texto)
  * [Propiedades](#Propiedades)
   * [1 El atributo paginate_by](#1-El-atributo-paginate_by)
   * [2 El atributo ordering](#2-El-atributo-ordering)   
  * [d) Listar las habilidades de un empleado](#d-Listar-las-habilidades-de-un-empleado)
* [2 La vista DetailView](#2-El-método-DetailView)
* [3 La vista CreateView](#3-El-método-CreateView)
  * [Nuevos campos compuestos en el modelo de empleados](#Nuevos-campos-compuestos-en-el-modelo-de-empleados)
* [4 La vista UpdateView](#4-El-método-UpdateView)
* [5 La vista DeleteView](#5-El-método-DeleteView)

## 1 La vista ListView

[Documentacion ListView](https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/#listview)

El método **ListView** en Django es una vista genérica basada en clases utilizada para listar objetos de un modelo en una página web. 

Entrega tres grandes funcionalidades:

1 se encarga de obtener una lista de objetos de un modelo y renderizarlos en una plantilla.\
2 puede habilitar la paginación para dividir la lista de objetos en varias páginas.\
3 proporciona un **contexto** a la plantilla que incluye la lista de objetos y otros datos adicionales.

Implementaremos cinco requerimientos de listado sobre nuestra aplicación **empleados**.

a) Listar todos los empleados.\
b) Listar todos los empleados que pertenezcan a un departamento.\
c) Listar todos los empleados que pertenezcan a un departamento mediante urls con un filtro en una caja de texto.\
d) Listar las habilidades de un empleado.

### a) Listar todos los empleados.

1 En el archivo **views.py** de la aplicación **empleados** debemos importar el método **ListView**, el modelo **Empleado** y construir la clase **EmpleadosListView**:

```python
from django.shortcuts import render # type: ignore
from django.views.generic import(ListView) # type: ignore

from .models import Empleado

class EmpleadosListView(ListView):
    model = Empleado
    template_name = "empleado/list_all.html"
    context_object_name = 'lista'
```

2 Debemos activar nuestra vista genérica, para lo cual creamos el archivo **urls.py** en la aplicacion empleados, importamos las **views**, declaramos la url: **listar-todos-los-empleados** y hacemos el llamado a la clase sobre la cual hemos basado nuestra vista:

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
   path('listar-todos-los-empleados', views.EmpleadosListView.as_view())
]
```

3 La url recién declarada no la hemos activado en las urls principales de Django, para lo cual vamos al archivo urls.py de la aplicación **empleado** (acá se puede producir una confusión. La aplicación en singular **empleado** es la que alberga por completo nuestro proyecto; la aplicación el plural **empleados**, alberga la aplicación del contexto específico del modelo empleados).

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from applications.exp.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("applications.empleados.urls")),
]
```

![image](https://github.com/user-attachments/assets/c2261c67-ed33-46c2-8d21-5c611ee63a06)


4 Por último debemos construir el archivo **list_all.html** dentro de una carpeta **empleado** dentro de la carpeta **templates**:

```python
<h1>
   Lista de todos los empleados
</h1>

<ul>
   {% for e in lista %}
      <li>
         {{e}}
      </li>
   {% endfor %}    
</ul>
```

5 Y ejecutamos nuestro proyecto:

![image](https://github.com/user-attachments/assets/1ffab5ad-a3cb-42b6-ba29-6883e223105d)


### b) Listar todos los empleados que pertenezcan a un departamento.

Este requerimiento es un filtro. A partir de determinado departamento queremos listar todos los empleados contenidos en él.

Como hemos visto podemos hacer esto modificando el archivo **admin.py** de **empleados** para que en el despliegue de registros de empleados vía nuestro administrador Django, también aparezca el filtro de departamentos:

```python
# ...

   search_fields = ('first_name',)
   list_filter = ('departamento', 'job', 'habilidades')
   filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
```

![image](https://github.com/user-attachments/assets/08fa5a43-ec64-4b47-ab21-415065ff6de7)

1 El método **queryset**

Este proceso lo haremos con código utilizando el atributo **queryset**. Primero haremos ésto en duro listando todos los empleados del departamento 'mate'. En **views.py** de la aplicación **empleados** construímos la clase **ListaPorDeptListView**:

```python
from django.shortcuts import render # type: ignore
from django.views.generic import(ListView) # type: ignore

from .models import Empleado

class EmpleadosListView(ListView):
    model = Empleado
    template_name = "empleado/list_all.html"
    context_object_name = 'lista'

class ListaPorDeptListView(ListView):
   template_name = "empleado/listapordept.html"
   queryset = Empleado.objects.filter(
       departamento__short_name = 'mate'
   )
```

2 En **urls.py** de la aplicación **empleado** le asignamos su ruta:

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
   path('listar-todos-los-empleados', views.EmpleadosListView.as_view()),
   path('listar-por-departamento', views.ListaPorDeptListView.as_view())
]
```

3 En la carpeta **persona** que está en la carpeta **templates** añadimos **listapordept.html**:

```python
<h1>
   Lista de empleados por departamento
</h1>

<ul>
   {% for e in object_list %}
      <li>
         {{e}}
      </li>
   {% endfor %} 
</ul>
```

4 y obtenemos:

![image](https://github.com/user-attachments/assets/b92b2031-215e-4611-9fd0-b9006bd916e0)

que comprobamos es correcto:

![image](https://github.com/user-attachments/assets/da9e0393-9959-4ae1-afd9-ac881e0a73b7)


Debemos utilizar ahora una forma eficiente para hacer lo anterior utilizando **get_queryset()**, filtrando a través de una caja de texto:

### c) Listar todos los empleados que pertenezcan a un departamento filtrando por medio de una caja de texto.

1 El método **get_queryset**

Debemos utilizar el método **get_queryset** para recoger un parámetro desde la url. **kwards** nos sirve para esto.
En views.py de la app empleado construimos la vista basada en clases **EmpleadoPorKwordListView**:

```python
# ...

class EmpleadoPorKwordListView(ListView):
   template_name = "empleado/empleadoporkword.html"
   context_object_name = 'empleadoporkword'

   def get_queryset(self):
      palabra_clave = self.request.GET.get('kword', '')
      empleado = Empleado.objects.filter(
         departamento__short_name = palabra_clave
      )
      return empleado.all()
```

2 Necesitamos una caja de texto html para que el usuario pueda hacer una búsqueda filtrada. En la carpeta **persona** de templates construímos **empleadoporkword.html**. Añadimos una clave de acceso {% csrf_token %}

```html
<h1>
   Buscar empleados por departamento
</h1>

<hr style = "border: none; height: 2px; background-color:red; width: 90%;" >
<br>

<form method = "GET">{% csrf_token %}
   <input type = "text" id="kword" name="kword" placeholder="Ingresa departamento">
   <button type="submit">
      Buscar
   </button>
</form>

<h3>
   Lista de empleados
</h3>

<ul>
   {% for e in empleadoporkword %}
      <li>
         {{e}}
      </li>
   {% endfor %} 
</ul>
```

3 Activamos la url en **urls.py** de la app **empleado**:

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
   path('listar-todos-los-empleados', views.EmpleadosListView.as_view()),
   path('listar-por-departamento', views.ListaPorDeptListView.as_view()),
   path('listar-por-kword', views.EmpleadoPorKwordListView.as_view())
]
```

4 Nuestro resultado de búsqueda para 'mate' es:

![image](https://github.com/user-attachments/assets/a870ee25-d7f6-462a-a13a-eab375676cf8)

### Propiedades.

#### 1 El atributo paginate_by.

La paginación es crucial al listar registros en Django por varias razones:

**Rendimiento**: Cargar todos los registros de una base de datos grande en una sola página puede ser muy lento y consumir muchos recursos del servidor. La paginación permite dividir los datos en partes más manejables, mejorando el rendimiento de la aplicación.

**Usabilidad**: Presentar demasiados datos en una sola página puede ser abrumador para los usuarios. La paginación facilita la navegación y hace que la interfaz sea más amigable y fácil de usar.

**Carga de Red**: Al limitar la cantidad de datos enviados al cliente en cada solicitud, se reduce la carga de red, lo que puede ser especialmente importante en aplicaciones con muchos usuarios concurrentes.

**Experiencia del Usuario**: La paginación permite a los usuarios encontrar y acceder a la información de manera más eficiente, mejorando su experiencia general en la aplicación.

Con **paginate_by** le indicamos a la clase **ListAllEmpleados** la cantidad de registros que despligue por página:

```python
class EmpleadosListView(ListView):
   model = Empleado
   template_name = "empleado/list_all.html"
   context_object_name = 'lista'
   paginate_by = 4
```

![image](https://github.com/user-attachments/assets/d4d66b71-87ed-4742-acd7-a36659f4f8ca)
![image](https://github.com/user-attachments/assets/36f52fa8-fdfc-45fa-9fb7-f1251228c8ce)


#### 2 El atributo ordering

El atributo **ordering** en la vista ListView de Django se utiliza para especificar el orden en que se deben mostrar los objetos en la lista. Este atributo espera una lista o tupla de nombres de campos por los cuales se debe ordenar el queryset. 

```
class EmpleadosListView(ListView):
   model = Empleado
   template_name = "empleado/list_all.html"
   context_object_name = 'lista'
   # paginate_by = 4
   ordering = 'first_name'
```

![image](https://github.com/user-attachments/assets/fc6611a4-aa9c-4d42-bff8-5a0e7dfde977)

### d) Listar las habilidades de un empleado.

Recordemos que **habilidades** con **empleado** es una relación de muchos a muchos:

![image](https://github.com/user-attachments/assets/474c08a0-0f4b-4b25-923f-d0a0abce7570)

1 Hacemos que en el listado de empleados del administrador de django se visualice el id de cada registro:

```python
class EmpleadoAdmin(admin.ModelAdmin):
   list_display = (
      'first_name',
      'last_name',
      'departamento',
      'job',
      'full_name',
      'id'
   )
```

![image](https://github.com/user-attachments/assets/f5386eb2-082d-4715-b89b-875a12ac96ec)

2 Construímos la vista **ListEmpByHabili** en la que recogemos el id de un empleado mediante una caja de texto. Para que el html asociado se despliegue por primera vez, debemos permitir que por defecto el valor de la caja sea None.

```python
class ListEmpByHabili(ListView):
   template_name = "empleado/listempbyhabili.html"
   context_object_name = 'listempbyhabili'

   def get_queryset(self):
      palabra_clave = self.request.GET.get('kword', None)
      if palabra_clave is not None:
         palabra_clave = int(palabra_clave)
         empleado = Empleado.objects.get(id = palabra_clave)
         return empleado.habilidades.all()
```

3 Activamos la vista:

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
   path('listar-todos-los-empleados', views.EmpleadosListView.as_view()),
   path('listar-por-departamento', views.ListaPorDeptListView.as_view()),
   path('listar-por-kword', views.EmpleadoPorKwordListView.as_view()),
   path('buscar-habi-por-emp', views.ListEmpByHabili.as_view())
]
```

4 Construímos el html **listempbyhabili.html**:

```html
<h1>
   Listar habilidades de un empleado
</h1>

<hr style = "border: none; height: 2px; background-color:red; width: 90%;" >
<br>

<form method = "GET">{% csrf_token %}
   <input type = "text" id="kword" name="kword" placeholder="Ingresa id del empleado">
   <button type="submit">
      Buscar
   </button>
</form>

<h3>
   Lista de habilidades
</h3>

<ul>
   {% for e in listempbyhabili %}
      <li>
         {{e}}
      </li>
   {% endfor %} 
</ul>
```

5 Buscamos por id = 4

![image](https://github.com/user-attachments/assets/28240682-c66b-4472-94a1-405ea88006fb)

![image](https://github.com/user-attachments/assets/d57e2b85-63c1-4ab7-8061-6a8c5123a094)


## 2 La vista DetailView

La vista DetailView en Django es una vista genérica basada en clases que se utiliza para mostrar los detalles de un solo objeto. 

Atributos Principales:

**model**: Especifica el modelo del objeto que se va a mostrar.\
**template_name**: Define el nombre de la plantilla que se utilizará para renderizar la vista. Si no se especifica, Django buscará una plantilla con el nombre <nombre_del_modelo>_detail.html.\
**context_object_name**: Define el nombre del objeto en el contexto de la plantilla. Por defecto, Django usa object, pero puedes cambiarlo a algo más descriptivo.

URL y Parámetros:

La URL que apunta a una DetailView generalmente incluye un parámetro que identifica al objeto, como un ID o un slug (en el contexto de desarrollo web, un slug es la parte final de una URL que identifica de manera única una página específica dentro de un sitio web. Por ejemplo, en la URL https://www.ejemplo.com/articulos/que-es-un-slug, el slug es **que-es-un-slug**. Los slugs son importantes para el SEO (optimización en motores de búsqueda) porque pueden contener palabras clave que ayudan a los motores de búsqueda a entender el contenido de la página. Un buen slug debe ser claro, conciso y relevante para el contenido de la página). Este parámetro se pasa a la vista para que pueda recuperar el objeto correcto de la base de datos.

Métodos Personalizables:

**get_queryset()**: Puedes sobrescribir este método para personalizar la consulta que obtiene el objeto.\
**get_context_data()**: Permite agregar datos adicionales al contexto que se pasa a la plantilla.

1 Creamos la vista basada en clases **DetalleDelEmpleado** del tipo **DetailView**:

```python
from django.shortcuts import render # type: ignore
from django.views.generic import( # type: ignore
   ListView, 
   DetailView) # type: ignore

# ...

class DetalleDelEmpleado(DetailView):
   model = Empleado
   template_name = "empleado/detalledelempleado.html"
   context_object_name = 'detalledelempleado'
```

2 Activamos la vista **declarando una URL con un pk**:

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
   path('listar-todos-los-empleados', views.EmpleadosListView.as_view()),
   path('listar-por-departamento', views.ListaPorDeptListView.as_view()),
   path('listar-por-kword', views.EmpleadoPorKwordListView.as_view()),
   path('buscar-habi-por-emp', views.ListEmpByHabili.as_view()),
   path('detalles-del-emp/<pk>', views.DetalleDelEmpleado.as_view())
]
```

3 Construimos el **detalledelempleado.html** asociado:

```html
<h1>
   Detalle de un empleado
</h1>

<hr style = "border: none; height: 2px; background-color:red; width: 90%;" >
<br>

<h3> Todos los detalles </h3>
{{detalledelempleado}}

<hr style = "border: none; height: 2px; background-color:green; width: 90%;" >
<p>{{detalledelempleado.first_name}}</p>
<p>{{detalledelempleado.last_name}}</p>
<p>{{detalledelempleado.job}}</p>
<p>{{detalledelempleado.departamento}}</p>
```

5 Accedemos a la URL con un pk específico:

![image](https://github.com/user-attachments/assets/0bd9abf6-a2a1-4d21-8ad5-d1b9915c1c5a)


### 1 El método **get_context_data**.

El método **get_context_data** se utiliza para agregar datos adicionales al contexto que se pasa a la plantilla. 

```python
class DetalleDelEmpleado(DetailView):
   model = Empleado
   template_name = "empleado/detalledelempleado.html"
   context_object_name = 'detalledelempleado'

   def get_context_data(self, **kwargs):
       context = super(DetalleDelEmpleado, self).get_context_data(**kwargs)
       context['titulo'] = 'Empleado del mes' 
       return context
```

```html
h1>
   Detalle de un empleado {{titulo}}
</h1>

<hr style = "border: none; height: 2px; background-color:red; width: 90%;" >
<br>

<h3> Todos los detalles </h3>
{{detalledelempleado}}

<hr style = "border: none; height: 2px; background-color:green; width: 90%;" >
<p>{{detalledelempleado.first_name}}</p>
<p>{{detalledelempleado.last_name}}</p>
<p>{{detalledelempleado.job}}</p>
<p>{{detalledelempleado.departamento}}</p>
```

![image](https://github.com/user-attachments/assets/a47d8023-4b7e-4609-b486-ac47cf9d8ba2)

## 3 La vista CreateView

### 3.1 Definición

CreateView es una vista genérica basada en clases proporcionada por Django para facilitar la creación de nuevos registros en el modelo de la base de datos. Esta vista proporciona una interfaz estandarizada para manejar la lógica de crear formularios y guardar datos en la base de datos.

¿Qué hace CreateView?

1 Renderiza un formulario: Automáticamente genera y renderiza un formulario basado en el modelo especificado.

2 Valida los datos del formulario: Cuando el formulario es enviado, CreateView valida los datos recibidos.

3 Guarda los datos: Si los datos son válidos, CreateView guarda el nuevo registro en la base de datos.

4 Redirige tras el éxito: Después de guardar el nuevo registro, CreateView puede redirigir a una página de éxito o cualquier otra URL especificada.

### 3.2 Los fields

Los fields son los atributos del modelo que defines y que representan las columnas en la base de datos. En el caso de una vista CreateView.

En Django, los fields en la vista CreateView son cruciales porque determinan qué campos del modelo se incluirán en el formulario que se presenta al usuario para crear una nueva instancia del modelo. Aquí hay algunas razones por las que son importantes:

**Control de Datos**: Permiten especificar exactamente qué campos del modelo deben ser rellenados por el usuario, asegurando que solo se recopile la información necesaria.

**Validación**: Los campos definidos en el formulario se validan automáticamente según las reglas establecidas en el modelo, lo que ayuda a mantener la integridad de los datos.

**Seguridad**: Al definir explícitamente los campos, se evita que usuarios malintencionados envíen datos no deseados o intenten modificar campos que no deberían ser accesibles.

**Facilidad de Uso**: Proporcionan una manera sencilla de generar formularios sin necesidad de escribir mucho código adicional, aprovechando las capacidades de las vistas basadas en clases (CBV) de Django

### 3.3 La vista **CrearEmpleado**:

```python
from django.shortcuts import render # type: ignore
from django.views.generic import( # type: ignore
   ListView, 
   DetailView,
   CreateView) # type: ignore

# ...

class CrearEmpleado(CreateView):
   model = Empleado
   template_name = "empleado/crearempleado.html"
   # fields = ['first_name','last_name','job'] 
   fields = ('__all__')
   success_url = '/crear-emp'
```

La clase **CrearEmpleado** es una vista basada en clases de Django que utiliza **CreateView** para manejar la creación de nuevos registros en el modelo **Empleado**. La propiedad **model** especifica que el modelo de la base de datos que se va a crear es **Empleado**. La propiedad **template_name** indica que la plantilla que se usará para renderizar el formulario es **crearempleado.html**, ubicada en el directorio empleado. La propiedad **fields** indica que todos los campos del modelo Empleado deben ser incluidos en el formulario, utilizando ('__all__'). La propiedad **success_url** define la URL a la que se redirigirá después de que el formulario se haya enviado y procesado correctamente. En este caso, la redirección es a la misma página, representada por el punto '/crear-emp'. 

Esta vista se encarga de renderizar un formulario basado en todos los campos del modelo **Empleado**, guardar los datos enviados en la base de datos si el formulario es válido, y redirigir a la misma página después de una creación exitosa.

### 3.4 El html

#### Diferencias entre los métodos GET y POST en el protocolo HTTP, especialmente en relación con las URLs:

#### Método GET

**Transmisión de Datos**: Los datos se envían a través de la URL como parámetros de consulta (query string). Por ejemplo, http://example.com/page?name=John&age=30.

**Visibilidad**: Los datos son visibles en la barra de direcciones del navegador, lo que puede ser menos seguro para información sensible.

**Uso Común**: Ideal para solicitudes de lectura, como obtener datos de un servidor sin realizar cambios en él.

**Limitaciones de Tamaño**: Tiene restricciones en la cantidad de datos que se pueden enviar debido a la longitud máxima de la URL.

#### Método POST

**Transmisión de Datos**: Los datos se envían en el cuerpo de la solicitud HTTP, no en la URL.

**Visibilidad**: Los datos no son visibles en la barra de direcciones del navegador, lo que proporciona mayor seguridad para información sensible.

**Uso Común**: Adecuado para solicitudes de escritura, como enviar datos a un servidor para ser procesados (por ejemplo, formularios de registro).

**Sin Limitaciones de Tamaño**: No tiene restricciones significativas en la cantidad de datos que se pueden enviar.

Debemos indicar una vez que se haya hecho el post a que pagina deseamos redireccionar.

```html
<h1> Registrar empleados </h1>

<!-- {{form}} -->

<form method = "POST">{% csrf_token %}
   <!-- {{form}} -->
   {{form.as_p}}
   <button type="submit">
      Agregar
   </button>
</form>
```

### 3.5 Activamos la vista 

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
   path('listar-todos-los-empleados', views.EmpleadosListView.as_view()),
   path('listar-por-departamento', views.ListaPorDeptListView.as_view()),
   path('listar-por-kword', views.EmpleadoPorKwordListView.as_view()),
   path('buscar-habi-por-emp', views.ListEmpByHabili.as_view()),
   path('detalles-del-emp/<pk>', views.DetalleDelEmpleado.as_view()),
   path('crear-emp', views.CrearEmpleado.as_view())
]
```

### 3.6 Creamos un registro 

![image](https://github.com/user-attachments/assets/1b03ad18-59ff-41da-b593-639244d8802e)
![image](https://github.com/user-attachments/assets/efb1d15a-cb12-4c40-b2dd-2a280b5a0056)

### 3.7 La vista TemplateView y el paquete **reverse_lazy**

No es buena practica utilizar en **success_url** la ruta en duro de la página web a la que vamos a querer redirigirnos una vez ingresado un registro, pues puede ser una url extensa o contener un parámetro. Existe una forma por la que podemos acceder a las url mediante un alias. Utilizaremos este método a continuación gracias al paquete **reverse_lazy** que nos redirigirá a una vista **TemplateView**.

1 Creamos la vista de registro

Construimos las vistas **CrearEmpleado** y el TemplateView **IngresoExitoso**

```python
from django.shortcuts import render # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views.generic import( # type: ignore
   ListView, 
   DetailView,
   CreateView,
   TemplateView) # type: ignore

# ...

class IngresoExitoso(TemplateView):
    template_name = "empleado/ingresoexitoso.html"

class CrearEmpleado(CreateView):
   model = Empleado
   template_name = "empleado/crearempleado.html"
   # fields = ['first_name','last_name','job'] 
   fields = ('__all__')
   success_url = reverse_lazy('empleado_app:exito')
```

2 Creamos el template **ingresoexitoso.html**

```html
<h2> Felicidades, ingreso exitoso! </h2>
```

3 Activamos las vistas

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

app_name = "empleado_app"

urlpatterns = [
   path('listar-todos-los-empleados', views.EmpleadosListView.as_view()),
   path('listar-por-departamento', views.ListaPorDeptListView.as_view()),
   path('listar-por-kword', views.EmpleadoPorKwordListView.as_view()),
   path('buscar-habi-por-emp', views.ListEmpByHabili.as_view()),
   path('detalles-del-emp/<pk>', views.DetalleDelEmpleado.as_view()),
   path('crear-emp', 
      views.CrearEmpleado.as_view(), ),
   path('ingreso-exitoso', 
      views.IngresoExitoso.as_view(), 
      name = 'exito')
]
```



### 3.8 El método **form_valid()**

El método **form_valid()** es comúnmente utilizado en vistas basadas en clases en Django que manejan formularios. Se invoca cuando un formulario ha sido validado exitosamente, lo que significa que los datos ingresados por el usuario son correctos y cumplen con todos los requisitos especificados en el formulario.

Este método tiene varios propósitos fundamentales:

Procesamiento de datos: Una vez que el formulario ha sido validado, form_valid() se utiliza para realizar acciones específicas con los datos del formulario. Esto podría incluir:

Guardar los datos en una base de datos.

Actualizar registros existentes.

Enviar correos electrónicos con la información proporcionada.

Realizar cualquier otra lógica de negocio necesaria.

Redirección o respuesta al usuario: Después de procesar los datos, el método form_valid() generalmente redirige al usuario a una página de confirmación o éxito, o devuelve una respuesta que indique que la operación se ha completado correctamente. Esta redirección o respuesta es crucial para una buena experiencia de usuario, ya que les indica que sus datos han sido procesados satisfactoriamente.

Personalización: form_valid() puede ser personalizado para realizar una variedad de acciones adicionales antes de redirigir al usuario. Esto permite a los desarrolladores añadir lógica de negocio específica y adaptarse a las necesidades particulares de la aplicación.

El método form_valid() es una parte fundamental del flujo de trabajo de cualquier vista en Django que maneja formularios. Su objetivo principal es asegurarse de que una vez que los datos del formulario son válidos, se procesen correctamente y se informe al usuario del éxito de la operación.

Supongamos que deseamos un nuevo campo compuesto de los elementos únicos 'nombre' y 'apellido' de un empleado. Para ello:

1 En el modelo de empleados construímos un nuevo campo llamado **full_name** no obligatorio.\

```python
class Empleado(models.Model):
   JOB_CHOICES = (
      ("0","Sociólogo"),
      ("1","Antropólogo"),
      ("2","Psicólogo"),
      ("3","Economista")
   )
   first_name = models.CharField("Nombres", max_length=60)
   last_name = models.CharField("Apellidos", max_length=60)
   full_name = models.CharField(
      "Nombre completo", 
      max_length=120, 
      blank = True)
   job = models.CharField("Trabajo", max_length=1, choices=JOB_CHOICES)
   departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to = 'empleado', blank = True, null = True)
   habilidades = models.ManyToManyField(Habilidades)
   hoja_vida = RichTextField()

   def __str__(self):
      return str(self.id) + "-" + self.first_name + "-" + self.last_name
```

2 En la vista especificamos los campos que deseamos sean ingresados para que no se despliegue el nuevo campo "Nombre completo" lo cual es innecesario.\

```python

# ...

class CrearEmpleado(CreateView):
   model = Empleado
   template_name = "empleado/crearempleado.html"
   fields = ['first_name',
             'last_name',
             'job',
             'departamento',
             'habilidades'] 
   # fields = ('__all__')
   success_url = reverse_lazy('empleado_app:exito')
```

3 Interceptamos el guardado de first_name y last_name en en la vista CreateView para generar el contenido del nuevo campo con el método **form_valid()**. Sólo cuando los datos ingresados son válidos se accede al método **form_valid()**.

```python
class CrearEmpleado(CreateView):
   model = Empleado
   template_name = "empleado/crearempleado.html"
   fields = ['first_name',
             'last_name',
             'job',
             'departamento',
             'habilidades'] 
   # fields = ('__all__')
   success_url = reverse_lazy('empleado_app:exito')

   def form_valid(self,form):
      empleado = form.save()
      empleado.full_name = empleado.first_name + ' ' + empleado.last_name
      empleado.save()
      return super(CrearEmpleado, self).form_valid(form)
```

Lo anterior no es óptimo pues estamos guardando innecesariamente el dato una segunda vez. Para evitar ésto hacemos:

```python
def form_valid(self,form):
   empleado = form.save(commit = false)
   empleado.full_name = empleado.first_name + ' ' + empleado.last_name
   empleado.save()
   return super(CrearEmpleado, self).form_valid(form)
```

4 guardamos los cambios, ejecutamos la migración (makemigrations y migrate), el servidor, registramos un nuevo empleado y verificamos.\

![image](https://github.com/user-attachments/assets/f62285f5-9625-45e5-b18c-3f895297d61a)

![image](https://github.com/user-attachments/assets/64977318-e521-4d28-bfe7-0595cd51e613)

![image](https://github.com/user-attachments/assets/d0e8a3b4-eef5-4910-a830-5f33cb26b78b)

![image](https://github.com/user-attachments/assets/998e40d0-d085-4eb5-be10-7d7b3c2a690d)

![image](https://github.com/user-attachments/assets/92ab934a-34fb-4491-aa3a-57ca6454e22b)

## 4 La vista UpdateView

El método UpdateView en Django es una vista genérica basada en clases que se utiliza para actualizar una instancia existente de un modelo en la base de datos. Hace:

Formulario de Edición: Muestra un formulario para editar un objeto existente. Este formulario se genera automáticamente a partir de la clase del modelo, a menos que se especifique una clase de formulario personalizada.\
Validación y Redisplay: Si hay errores de validación, vuelve a mostrar el formulario con los errores resaltados.\
Guardar Cambios: Guarda los cambios realizados en el objeto una vez que el formulario se envía correctamente.

Este método es útil para situaciones en las que necesitas permitir a los usuarios actualizar información existente, como editar un perfil de usuario o modificar un artículo en un blog.

1 Importamos la vista.
![image](https://github.com/user-attachments/assets/0bb860e4-5ea4-4667-b491-ea620246eadd)

2 Creamos la vista basada en clases EmpleadoUpdateView sobreescribiendo el método **post**:
El método **post()** permite guardar datos sin haber sido previamente validados por el método **form_valid()**
![image](https://github.com/user-attachments/assets/599dc1e7-31ed-4d4d-bd68-f8485333e44f)

3 Creamos el html respectivo.
![image](https://github.com/user-attachments/assets/2d0e445d-7d51-43de-987a-2287706101dd)

4 Activamos la vista con un &lt;pk&gt;.
![image](https://github.com/user-attachments/assets/ac7b3871-8a33-4fc0-a128-a449a23cbed5)

5 Actualizamos la informacion de un empleado.

No olvidemos acceder a esta URL adjuntado la pk asociada a un registro específico.
![image](https://github.com/user-attachments/assets/7c8f15cc-868e-462b-8296-955a81920876)
![image](https://github.com/user-attachments/assets/d374f642-abea-4da1-94cf-02fa31063ccc)

## 5 La vista DeleteView

1 Creamos una vista basada en clases EmpleadoDeleteView e importamos DeleteView
![image](https://github.com/user-attachments/assets/c81711e4-e789-4571-b1ab-0322de05f335)
![image](https://github.com/user-attachments/assets/8a7501de-a768-4741-8712-85e1705d6a99)

2 Creamos el html asociado
![image](https://github.com/user-attachments/assets/488df7a0-aba4-4cd2-805c-3e47d85a586a)

3 Activamos la vista asociándola con un &lt;pk&gt.
![image](https://github.com/user-attachments/assets/aa5bb9fb-185f-4688-b808-1fe2f3cd80ef)

4 Seleccionemos un registro a eliminar
![image](https://github.com/user-attachments/assets/102ee2dc-439b-4173-a35a-10f397103db1)

5 Ejecutemos la acción de nuestra vista Eliminar.
![image](https://github.com/user-attachments/assets/626b550a-0069-4ef0-aab6-6c2a6010d9e8)

6 Verifiquemos:
![image](https://github.com/user-attachments/assets/569a39b5-d229-42dd-a027-5fc420e37f60)





