# Vistas basadas en clases

[ccbv.co.uk](https://ccbv.co.uk)

## Índice

* [1 El método ListView](#1-El-método-ListView)
  * [a) Listar todos los empleados](#a-Listar-todos-los-empleados)
  * [b) Listar todos los empleados que pertenezcan a un departamento](#b-Listar-todos-los-empleados-que-pertenezcan-a-un-departamento)
  * [c) Listar todos los empleados que pertenezcan a un departamento mediante urls con un filtro en una caja de texto](#c-Listar-todos-los-empleados-que-pertenezcan-a-un-departamento-mediante-urls-con-un-filtro-en-una-caja-de-texto)
  * [Algunas propiedades de la vista ListView](#Algunas-propiedades-de-la-vista-ListView)
    * [Paginación en la vista ListView](#Paginación-en-la-vista-ListView)
    * [Orden al listado](#Orden-al-listado)   
  * [d) Listar las habilidades de un empleado](#d-Listar-las-habilidades-de-un-empleado)
    
* [2 El método DetailView](#2-El-método-DetailView)

## 1 El método ListView

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

1 En el archivo **views.py** de la aplicación **empleados** debemos importar el método **ListView**, el modelo **Empleado** y construir la clase **ListAllEmpleados**:

![image](https://github.com/user-attachments/assets/491a04e7-d89c-4090-bc02-e62e51e4b613)

2 Debemos activar nuestra vista genérica, para lo cual vamos al archivo urls.py de la aplicacion empleados, importamos las **views**, declaramos la url: **listar-todo-empleado/** y hacemos el llamado a la clase sobre la cual hemos basado nuestra vista:

![image](https://github.com/user-attachments/assets/65b5777f-d842-4d0b-8396-43ffe3e926bc)

3 La url recién declarada no la hemos activado en las urls principales de Django, para lo cual vamos al archivo urls.py de la aplicación **empleado** (acá se puede producir una confusión. La aplicación en singular **empleado** es la que alberga por completo nuestro proyecto; la aplicación el plural **empleados**, alberga la aplicación del contexto específico del modelo empleados).

![image](https://github.com/user-attachments/assets/f3d27b19-6972-4d3c-b98e-766378bfcd00)

4 Por último debemos construir el archivo list_all.html dentro de una carpeta **persona** en la ruta de los **templates**:

![image](https://github.com/user-attachments/assets/a00d7484-f0e6-436a-a604-58b4f01aecd5)

en la que iteramos sobre registros de modelos para listarlos:

```
<h1>
    Lista de todos los empleados
</h1>

<ul>
    {% for e in lista %}
        <li>{{ e }}</li>
    {% endfor %}
</ul>
```

5 Y ejecutamos nuestro proyecto:

![image](https://github.com/user-attachments/assets/3d22080e-b269-43aa-b2de-2cc4f7c29a74)

### b) Listar todos los empleados que pertenezcan a un departamento.

Hagamos una modificación en en el archivo admin.py de **empleados** para que en el despliegue de registros de empleados vía nuestro administrador Django, también aparezca el filtro de departamentos:

![image](https://github.com/user-attachments/assets/a56029c8-95b0-41a0-bc18-9e16251719f2)

![image](https://github.com/user-attachments/assets/58b8a710-240f-43c1-a043-339758e38407)

Es éste el proceso que replicaremos con código utilizando el atributo **queryset**:

Primero haremos ésto en duro listando todos los empleados del departamento 'ciencias matemáticas'.

1 En **views.py** de la aplicación **empleados** construímos la clase **ListAllByDept**:

![image](https://github.com/user-attachments/assets/61ff3f4a-820c-4b58-87fa-cb570d968ba9)

2 En **urls.py** de la aplicación **empleado** le asignamos su ruta:

![image](https://github.com/user-attachments/assets/6874053f-f969-44c8-93a7-b5bd66a77bc1)

3 En la carpeta **persona** que está en la carpeta **templates** añadimos **AllByDept.html**:

![image](https://github.com/user-attachments/assets/2d933f85-416e-4ea8-8f3e-a54680b41a13)

4 y obtenemos:

![image](https://github.com/user-attachments/assets/4501354e-605f-4d0c-b97d-9d2b6e3f1a25)

que comprobamos es correcto:

![image](https://github.com/user-attachments/assets/f8380b72-1ec0-478b-a8fc-71bff0fee0f2)

Debemos utilizar ahora una forma eficiente para hacer lo anterior utilizando **get_queryset()**, filtrando a través de una caja de texto:






### c) Listar todos los empleados que pertenezcan a un departamento mediante urls con un filtro en una caja de texto.

1 Debemos utilizar el método **get_queryset** para recoger un parámetro desde la url. **kwards** es un método de Django que nos permite recoger elementos desde las urls.

![image](https://github.com/user-attachments/assets/a1a5d8bc-d7a8-49f2-b8d8-9f40adaa414f)

2 Necesitamos una caja de texto html para que el usuario pueda hacer una búsqueda filtrada. En la carpeta **persona** de templates construímos **by_kword.html**. Añadimos una clave de acceso {% csrf_token %}

![image](https://github.com/user-attachments/assets/978b96de-2042-459b-b419-71b71524291e)

Nuestro resultado de búsqueda para 'ciencias matemáticas' es:

![image](https://github.com/user-attachments/assets/086db168-ed34-425a-9edb-4f888c91402d)

Nuestro resultado de búsqueda para 'ciencias físicas' es:

![image](https://github.com/user-attachments/assets/793e997f-1ecb-4aa5-95a2-fcb05ff67450)


### Algunas propiedades de la vista ListView.

#### Paginación en la vista ListView.

La paginación es crucial al listar registros en Django por varias razones:

**Rendimiento**: Cargar todos los registros de una base de datos grande en una sola página puede ser muy lento y consumir muchos recursos del servidor. La paginación permite dividir los datos en partes más manejables, mejorando el rendimiento de la aplicación.

**Usabilidad**: Presentar demasiados datos en una sola página puede ser abrumador para los usuarios. La paginación facilita la navegación y hace que la interfaz sea más amigable y fácil de usar.

**Carga de Red**: Al limitar la cantidad de datos enviados al cliente en cada solicitud, se reduce la carga de red, lo que puede ser especialmente importante en aplicaciones con muchos usuarios concurrentes.

**Experiencia del Usuario**: La paginación permite a los usuarios encontrar y acceder a la información de manera más eficiente, mejorando su experiencia general en la aplicación.

Con **paginate_by** le indicamos a la clase **ListAllEmpleados** la cantidad de registros que despligue por página:

![image](https://github.com/user-attachments/assets/9dde698d-5393-4cd1-9855-daddaaec6c72)
![image](https://github.com/user-attachments/assets/29e4c2c9-6d3d-4a31-b419-926e4b27684e)
![image](https://github.com/user-attachments/assets/d1ef1023-dc74-4328-b906-bc657583d4a0)


#### Orden al listado.

El atributo **ordering** en la vista ListView de Django se utiliza para especificar el orden en que se deben mostrar los objetos en la lista. Este atributo espera una lista o tupla de nombres de campos por los cuales se debe ordenar el queryset. 

![image](https://github.com/user-attachments/assets/d87577d1-ca09-4e3a-a562-defd67768cd4)
![image](https://github.com/user-attachments/assets/b46c3c31-7cb5-4ad1-9f49-6b0d8d90c4e3)


### d) Listar las habilidades de un empleado.

Recordemos que **habilidades** con **empleado** es una relación de muchos a muchos:

![image](https://github.com/user-attachments/assets/474c08a0-0f4b-4b25-923f-d0a0abce7570)

1 Hacemos que en el listado de empleados del administrador de django se visualice el id de cada registro.
![image](https://github.com/user-attachments/assets/f6fb0e9f-c29d-4e34-b46a-7f8c241a83d4)
![image](https://github.com/user-attachments/assets/d5d6e353-d41b-48f5-90c4-17018d9bf6f0)

2 Construímos la vista **ListEmpByHabili** en la que recuperamos de un cuadro de texto el id de un empleado
y desplegamos la lista de sus habilidades. Le asignamos por defecto el valor id = 4 y añadimos un control de excepciones:

![image](https://github.com/user-attachments/assets/ce01ea5b-3613-41e7-9155-a09dbe3a18ad)







a) Construímos el método **get_queryset** dentro de la clase **ListEmpByHabili** en la vista de empleados:
```
class ListEmpByHabili(ListView):
    template_name = 'persona/by_habili.html'
    context_object_name = 'empleados_by_habili'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=11)
        return empleado.habilidades.all()
```
b) Creamos la url **buscar-emp-por-habili/** en la aplicación empleados:
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
c) en la carpeta **persona** de templates templates construimos **by_habili.html** para la caja de texto:
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

## 2 El método DetailView
