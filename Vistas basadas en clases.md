# 1 Vistas basadas en clases

[ccbv.co.uk](https://ccbv.co.uk)


## 1_1 El método ListView

[Documentacion ListView](https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/#listview)

El método ListView en Django es una vista genérica basada en clases que se utiliza para mostrar una lista de objetos. Es especialmente útil cuando necesitas mostrar una lista de elementos de un modelo en una página web. 

Funcionalidades:

1 ListView se encarga de obtener una lista de objetos de un modelo y renderizarlos en una plantilla.\
2 Paginación: Puedes habilitar la paginación para dividir la lista de objetos en varias páginas.\
3 Proporciona un **contexto** a la plantilla que incluye la lista de objetos y otros datos adicionales.

Implementaremos cinco requerimientos de listado sobre nuestra aplicacion **empleados**.

#### 18_1_1 Listar todos los empleados.

En el archivo views.py de la aplicacion empleados debemos importar el metodo ListView, el modelo Empleado y construir la siguiente clase:

![image](https://github.com/user-attachments/assets/c00ff6d7-4740-419b-a78f-b908726f5410)

2 Debemos activar nuestra vista generica para lo cual vamos al archivo urls.py de la aplicacion empleado, importamos las views y declaramos la url: listar-todo-empleado/ y hacemos el llamado a la clase sobre la cual hemos basado nuestra vista:

![image](https://github.com/user-attachments/assets/99ea6f61-5869-4061-8a52-4f5b5e5ec22c)

3 La url recien declarada no la hemos activado en las urls principales de Django, para lo cual vamos al archivo urls.py de la aplicacion empleado (aca se puede producir una confusion. Esta aplicacion empleado, en singular es la que alberga por completo nuestro proyecto, la aplicacion el plural empleados, alberga la aplicacion del contexto especifico del modelo empleados)

![image](https://github.com/user-attachments/assets/12e21b13-ace2-4110-aeeb-0c63cc89d0f6)

4 Por ultimo debemos construir el archivo html dentro de una carpeta persona en la ruta de los templates:

![image](https://github.com/user-attachments/assets/745c0f3d-d44e-4fe7-83f3-ae3c87d51b93)

Iteracion sobre registros de modelos para listarlos

```
<ul>
 {% for e in object_list %}
  <li>{{ e }}</li>
 {% endfor %}
</ul>
```

5 Y ejecutemos nuestro proyecto:

![image](https://github.com/user-attachments/assets/e189374d-2287-4d73-8a4a-78c12135ebec)

#### 18_1_2 Listar todos los empleados que pertenezcan a un area específica

Solo con fines pedagogicos haremos esto de forma bruta.

1 En **views.py** de la aplicacion empleado:

```
from django.shortcuts import render # type: ignore

from django.views.generic import( # type: ignore
    ListView
)

from .models import Empleado

# 1 Listar todos los empleados de la empresa

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    context_object_name = 'lista'

# 2 Listar todos los empleados de la empresa por departamento

class ListAllByDept(ListView):
    template_name = 'persona/AllByDept.html'
    queryset = Empleado.objects.filter(
        departamento__short_name = 'ciencias matemáticas'
    )
```

2 En **urls.py** de la aplicacion empleado:

```
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-por-area/', views.ListAllByDept.as_view()),
]
```

3 En la carpeta persona que esta en la carpeta templates anadimos list.html:

```
<h1>
    lista de todos los empleados
</h1>

<ul>
    {% for e in object_list %}
        <li>{{ e }}</li>
    {% endfor %}
</ul>
```

4 y obtenemos:

![image](https://github.com/user-attachments/assets/8d1bc43b-d62c-4740-8374-366c4883c6df)

#### 18_1_3 Listar todos los empleados que pertenezcan a un area específica mediante urls con un filtro en una caja de texto

1 Debemos utilizar el metodo **get_queryset** para recoger un parametro desde la url.
Es entonces que debemos agregar a la url lista-by-area/ un elemento de la siguiente manera:
lista-by-area<shortname>/

2 **kwards** es un metodo de Django que nos permite recoger elementos desde las urls, y con el que tomamos el elemento <shotname>.

3 Necesitamos una caja de texto html para que el usuario pueda definir su busqueda a listar.

4 Es importante no olvidar la clave de acceso {% csrf_token %}

Entonces:

a) Construimos el metodo dentro de una clase en la vista de empleados:
```
class ListEmpByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
        first_name = palabra_clave
        )
        return lista
```
b Creamos la url en la aplicacion empleados:
```

from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-por-area/', views.ListAllByDept.as_view()),
    path('buscar-emp-por-kword/', views.ListEmpByKword.as_view()),
]

```
c en la carpeta persona de templates templates construimos **by_kword.html** para la caja de texto
```
<h1>
    Buscar empleados por kword
</h1>
<form method="GET">{% csrf_token %}
    <input type="text" id="kword" name="kword" placeholder="Ingresa nombre">
    <button type="submit"> Buscar </button>
</form>
<h3>
    Lista resultado
</h3>
<ul>
    {% for e in empleados %}
        <li>{{ e }}</li>
    {% endfor %}
</ul>
```
![image](https://github.com/user-attachments/assets/a4ab7983-78e4-4734-9a66-73a54df63b65)

Nuestro resultado de busqueda para carlos es:

![image](https://github.com/user-attachments/assets/8d7961c8-446c-43b4-94d1-5a11a449c22e)

![image](https://github.com/user-attachments/assets/64449aba-4f81-4cdd-8a77-2acf0354db58)

#### 18_1_4 Paginación en la vista ListView

La paginación es crucial al listar registros en Django por varias razones:

Rendimiento: Cargar todos los registros de una base de datos grande en una sola página puede ser muy lento y consumir muchos recursos del servidor. La paginación permite dividir los datos en partes más manejables, mejorando el rendimiento de la aplicación.\
Usabilidad: Presentar demasiados datos en una sola página puede ser abrumador para los usuarios. La paginación facilita la navegación y hace que la interfaz sea más amigable y fácil de usar.\
Carga de Red: Al limitar la cantidad de datos enviados al cliente en cada solicitud, se reduce la carga de red, lo que puede ser especialmente importante en aplicaciones con muchos usuarios concurrentes.\
Experiencia del Usuario: La paginación permite a los usuarios encontrar y acceder a la información de manera más eficiente, mejorando su experiencia general en la aplicación.

![image](https://github.com/user-attachments/assets/aef71236-1754-455c-8fd3-331fc236c8f2)

```
# 1 Listar todos los empleados de la empresa

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    paginate_by = 3
    context_object_name = 'lista'
```

![image](https://github.com/user-attachments/assets/0ff4e393-7b66-4e87-8088-f120f5738bb6)

![image](https://github.com/user-attachments/assets/68daa866-cc3a-4091-96ca-033581bf5548)

Tambien podemos establecer un orden al listado.

```
# 1 Listar todos los empleados de la empresa

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    paginate_by = 3
    ordering = 'first_name'
    context_object_name = 'lista'
```

![image](https://github.com/user-attachments/assets/e1c86f92-88d3-42b1-b6c2-c2e99dd5b442)

#### 18_1_5 Listar las habilidades de un empleado

Recordemos que habilidades con empleados es una relacion de muchos a muchos.

1 Hacemos que en el listado de empleados del administrador de django se visualice el id de cada registro.

![image](https://github.com/user-attachments/assets/6fe81643-d81f-4e36-8829-ddf6482ed0d9)

![image](https://github.com/user-attachments/assets/ee1f9c05-795f-4beb-bab3-6a88c1839d12)





a) Construimos el metodo dentro de una clase en la vista de empleados:
```
class ListEmpByHabili(ListView):
    template_name = 'persona/by_habili.html'
    context_object_name = 'empleados_by_habili'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=11)
        return empleado.habilidades.all()
```
b Creamos la url en la aplicacion empleados:
```

from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-por-area/', views.ListAllByDept.as_view()),
    path('buscar-emp-por-kword/', views.ListEmpByKword.as_view()),
    path('buscar-emp-por-habili/', views.ListEmpByHabili.as_view()),
]

```
c en la carpeta persona de templates templates construimos **by_habili.html** para la caja de texto
```
<h1>
    Buscar empleados por Habilidad
</h1>
<form method="GET">{% csrf_token %}
    <input type="text" id="habili" name="habili" placeholder="Ingresa Habilidad">
    <button type="submit"> Buscar </button>
</form>
<h3>
    Lista resultado
</h3>
<ul>
    {% for e in empleados %}
        <li>{{ e }}</li>
    {% endfor %}
</ul>
```


### 18_2 El método DetailView