

# Diseño gráfico del proyecto y puesta a punto de su funcionalidad

Script de arranque:

```bash
C:\Users\chris> cd /
C:\> cd mis_entornos/entorno_3/Scripts
C:\mis_entornos\entorno_3\Scripts> activate
(entorno_3) C:\mis_entornos\entorno_3\Scripts> cd \mis_proyectos\emp3\empleado
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

## Índice

* [1 Crear un proyecto Django](#1-crear-un-proyecto-django)
  * [11 Creamos carpetas de trabajo](#11-Creamos-carpetas-de-trabajo)

## 1 Construyendo la pantalla de inicio

### 1 Herencia

1 base.html e inicio.html

En la carpeta **templates** construimos el archivo **base.html** del cual heredaremos a **inicio.html**. 

**base.html**

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="stylesheet" href="{% static 'css/foundation.min.css' %}">
   <title>

      {% block title  %}
         
      {% endblock title %}

   </title>
</head>
<body>

   {% block content %}
         
   {% endblock content %}

</body>
</html>
```

2 El TemplateView

En **views.py** de la app **empleados** creamos una vista TemplateView asociada al html **inicio.html**

```python
class Inicio(TemplateView):
    template_name = "inicio.html"
```

3 Activamos la url de la vista

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

app_name = "empleado_app"

urlpatterns = [
   path('', 
      views.Inicio.as_view(), 
      name = 'inicio'),

# some code...

]
```

4 construímos **inicio.html**

```html
{% extends 'base.html' %}

{% block title  %}
   Pagina de inicio del sistema empleados         
{% endblock title %}

{% block content %}
   Bienvenido a la pagina de inicio del sistema empleados      
{% endblock content %}
```

5 Verificamos:

![image](https://github.com/user-attachments/assets/cb17b8d6-ca72-42fa-a88f-dd6b5cef89df)


### 2 Includes. La cabecera

Dentro de la carpeta **templates**, crearemos otra llamada **includes** para incluir fragmentos de plantillas dentro de una plantilla principal. En ella construimos el archivo: **header.html**.

Includes se utiliza para insertar contenido de otra plantilla directamente en la actual, con `{% include %}`. Esto es útil para piezas reutilizables más pequeñas, como menús, barras de navegación o widgets. No implica herencia; simplemente incluye ese fragmento de plantilla "tal cual".

1 En la carpeta includes construimos header.html copiando Top Bar de Navigation en Foundation

```html
<div class="top-bar">
   <div class="top-bar-left">
      <ul class="dropdown menu" data-dropdown-menu>
         <li class="menu-text">Site Title</li>
         <li>
            <a href="#">One</a>
            <ul class="menu vertical">
            <li><a href="#">One</a></li>
            <li><a href="#">Two</a></li>
            <li><a href="#">Three</a></li>
            </ul>
         </li>
         <li><a href="#">Two</a></li>
         <li><a href="#">Three</a></li>
      </ul>
      </div>
      <div class="top-bar-right">
      <ul class="menu">
         <li><input type="search" placeholder="Search"></li>
         <li><button type="button" class="button">Search</button></li>
      </ul>
   </div>
 </div>
```

2 En inicio.html agregamos el include:

```html
{% extends 'base.html' %}

{% block title  %}
   Pagina de inicio del sistema empleados         
{% endblock title %}

{% block content %}

   {% include 'includes/header.html' %}
 
   <style>
      p {
          text-indent: 30px; /* Ajusta el tamaño de la sangría según lo desees */
      }
  </style>
        
   <p>Bienvenido a la pagina de inicio del sistema empleados </p>

{% endblock content %}
```

3 En base.html agregamos las siguiente líneas:

```html
<script src="{% static 'js/vendor/jquery.js' %}"></script>
<script src="{% static 'js/vendor/what-input.js' %}"></script>
<script src="{% static 'js/vendor/foundation.min.js' %}"></script>
<script>
  $(document).foundation();
</script>
```

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="stylesheet" href="{% static 'css/foundation.min.css' %}">
   <title>

      {% block title  %}
         
      {% endblock title %}

   </title>
</head>
<body>

   {% block content %}
         
   {% endblock content %}

   <script src="{% static 'js/vendor/jquery.js' %}"></script>
   <script src="{% static 'js/vendor/what-input.js' %}"></script>
   <script src="{% static 'js/vendor/foundation.min.js' %}"></script>
   <script>
     $(document).foundation();
   </script>

</body>
</html>
```

4 Verificamos:

![image](https://github.com/user-attachments/assets/cb2d32cc-6039-44e0-86de-8e55e7962665)

### 3 Personalizando la cabecera

1 Modificamos **header.html** como se indica a continuacion:

```html
<div class="top-bar">
   <div class="top-bar-left">
      <ul class="dropdown menu" data-dropdown-menu>
         <li class="menu-text">Empleados</li>
         <li>
            <a href="#">
               Listar
            </a>
         </li>
         <li>
            <a href="#">
               Departamentos
            </a>
         </li>
         <li>
            <a href="#">
               Administrar
            </a>
         </li>
      </ul>
      </div>
      <div class="top-bar-right">
      <ul class="menu">
         <li><input type="search" placeholder="Buscar empleado"></li>
         <li><button type="button" class="button">Registrar nuevo</button></li>
      </ul>
   </div>
 </div>
```

2 Anadimos imagenes

Copiamos código de Foundation de Media, Orbit y lo pegamos en **inicio.html** entre `{% block content %}`. Cargamos 3 imagenes dentro de la carpeta **img**, modificamos sus rutas y agregamos la expresion `{% load static %}`:

```html
{% extends 'base.html' %}

{% load static %}

{% block title  %}
   Pagina de inicio del sistema empleados         
{% endblock title %}

{% block content %}

   {% include 'includes/header.html' %}
 
Bienvenido a la pagina de inicio del sistema empleados 

<div class="orbit" role="region" aria-label="Favorite Space Pictures" data-orbit>
   <div class="orbit-wrapper">
      <div class="orbit-controls">
         <button class="orbit-previous"><span class="show-for-sr">Previous Slide</span>&#9664;&#xFE0E;</button>
         <button class="orbit-next"><span class="show-for-sr">Next Slide</span>&#9654;&#xFE0E;</button>
      </div>
      <ul class="orbit-container">
         <li class="is-active orbit-slide">
         <figure class="orbit-figure">
            <img class="orbit-image" src="{% static 'img/1.jpg' %}" alt="Space">
            <figcaption class="orbit-caption">Space, the final frontier.</figcaption>
         </figure>
         </li>
         <li class="orbit-slide">
         <figure class="orbit-figure">
            <img class="orbit-image" src="{% static 'img/2.jpg' %}" alt="Space">
            <figcaption class="orbit-caption">Lets Rocket!</figcaption>
         </figure>
         </li>
         <li class="orbit-slide">
         <figure class="orbit-figure">
            <img class="orbit-image" src="{% static 'img/3.jpg' %}" alt="Space">
            <figcaption class="orbit-caption">Encapsulating</figcaption>
         </figure>
         </li>
      </ul>
   </div>
   <nav class="orbit-bullets">
      <button class="is-active" data-slide="0">
         <span class="show-for-sr">First slide details.</span>
         <span class="show-for-sr" data-slide-active-label>Current Slide</span>
      </button>
      <button data-slide="1"><span class="show-for-sr">Second slide details.</span></button>
      <button data-slide="2"><span class="show-for-sr">Third slide details.</span></button>
      <button data-slide="3"><span class="show-for-sr">Fourth slide details.</span></button>
   </nav>
</div>

{% endblock content %}
```

3 Adjuntamos en inicio.html un bloque de bienvenida copiando de Foundation Container, Callout:

```html
{% extends 'base.html' %}

{% load static %}

{% block title  %}
   Pagina de inicio del sistema empleados         
{% endblock title %}

{% block content %}

   {% include 'includes/header.html' %}
     
Bienvenido a la pagina de inicio del sistema empleados 

<div class="orbit" role="region" aria-label="Favorite Space Pictures" data-orbit>
   <div class="orbit-wrapper">
      <div class="orbit-controls">
         <button class="orbit-previous"><span class="show-for-sr">Previous Slide</span>&#9664;&#xFE0E;</button>
         <button class="orbit-next"><span class="show-for-sr">Next Slide</span>&#9654;&#xFE0E;</button>
      </div>
      <ul class="orbit-container">
         <li class="is-active orbit-slide">
         <figure class="orbit-figure">
            <img class="orbit-image" src="{% static 'img/1.jpg' %}" alt="Space">
            <figcaption class="orbit-caption">Space, the final frontier.</figcaption>
         </figure>
         </li>
         <li class="orbit-slide">
         <figure class="orbit-figure">
            <img class="orbit-image" src="{% static 'img/2.jpg' %}" alt="Space">
            <figcaption class="orbit-caption">Lets Rocket!</figcaption>
         </figure>
         </li>
         <li class="orbit-slide">
         <figure class="orbit-figure">
            <img class="orbit-image" src="{% static 'img/3.jpg' %}" alt="Space">
            <figcaption class="orbit-caption">Encapsulating</figcaption>
         </figure>
         </li>
      </ul>
   </div>
</div>

<div class="grid-x align-center">
   <h1 class="cell large-8" style="font-size: 25px; text-align: center;">
      Bienvenido a la pagina de inicio   
   </h1>
   <div>
      <div class="callout secondary">
         <h5>Registro y control de empleados</h5>
         <p>caja callout</p>
         <a href="#">Ver empleados</a>
         </div>
   </div>
</div>

{% endblock content %}
```

4 Veamos como queda:

![image](https://github.com/user-attachments/assets/e87b65b5-5219-4029-aae5-b681c45d33d5)

## 2 Pantalla listar empleados

### 2.1 Formato y funcionalidad al boton listar

1 Queremos entregarle funcionalidad al botón:

![image](https://github.com/user-attachments/assets/6b4bf86b-e084-43bb-990a-f105bd22dfe4)

para ello asociamos correctamente la url en **header.html**:

```python

# some code...

app_name = "empleado_app"

urlpatterns = [
   path('', 
      views.Inicio.as_view(), 
      name = 'inicio'),
   path('listar-todos-los-empleados', 
      views.EmpleadosListView.as_view(),
      name = 'listartodoslosempleados'),

# some code...

```

```python

# some code...

<li class="menu-text">Empleados</li>
<li>
   <a href="{% url 'empleado_app:listartodoslosempleados' %}">
      Listar
   </a>
</li>
<li>

# some code...

```

2 Queremos entregarle diseño al despliegue de la lista:

Para ello modificamos nuestro **list_all.html** ya construido:

```html
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

El boton buscar, la tabla y el boton ver se extraen de Foundation.

```html
{% extends 'base.html' %}

{% block content %}

{% include 'includes/header.html' %}

<div class="grid-container">
   <div class="grid-x">
      <h1 class="cell">
      </h1>
      <div class="cell grid-x grid-margin-x">
         <div class="cell large-7">
            <input type="text" placeholder="buscar empleado">
         </div>
         <div class="cell large-2">
            <button type="button" class="success button">
               Buscar
            </button>
         </div>
      </div>
      <div class="cell">
         <table>
            <thead>
               <tr>
                  <th width="200">ID</th>
                  <th>NOMBRES</th>
                  <th width="150">APELLIDOS</th>
                  <th width="150">DEPARTAMENTO</th>
                  <th width="150">ACCION</th>
               </tr>
            </thead>
            <tbody>
               {% for e in lista %}
               <tr>
                  <td>{{e.id}}</td>
                  <td>{{e.first_name}}</td>
                  <td>{{e.last_name}}</td>
                  <td>{{e.departamento}}</td>
                  <td>
                     <a class="button warning" href="#">
                        Ver
                     </a>
                  </td>
               </tr>
              {% endfor %}  
            </tbody>
          </table>
      </div>
   </div>
</div>

{% endblock content %}
```

y verificamos:

![image](https://github.com/user-attachments/assets/723d5604-2085-4cc7-80a3-6a418332dbca)

### 2.2 Funcionalidad al boton Buscar y Ver

1 Boton buscar

1 La funcionalidad de este boton ya la tenemos en la clase **EmpleadoPorKwordListView** que listaba todos los empleados por un departamento:

```python
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

2 Vamos a copiar el metodo get_queryset(self) y modificarlo para que haga un filtro por un atributo de nombre en el modelo de empleados y lo copiaremos en la vista en la que trabajamos actualmente. En la clase **EmpleadosListView** utilizamos un **icontains**:

```python
class EmpleadosListView(ListView):
   template_name = "empleado/list_all.html"
   context_object_name = 'lista'
   paginate_by = 4
   ordering = 'first_name'

   def get_queryset(self):
      palabra_clave = self.request.GET.get('kword', '')
      lista = Empleado.objects.filter(
         full_name__icontains = palabra_clave
      )
      return lista
```

3 En **list_all.html** debemos ingresar un id y name en el input, crear un formulario especificandole el metodo GET, anadirle un token de autorizacion y el boton cambiarlo al tipo submit.

```html

/* some code */

<div class="grid-container">
   <div class="grid-x">
      <h1 class="cell">
      </h1>
      <form class="cell grid-x grid-margin-x" method="GET">{% csrf_token %}
         <div class="cell large-7">
            <input type="text" id="kword" name="kword" placeholder="buscar empleado">
         </div>
         <div class="cell large-2">
            <button type="submit" class="success button">
               Buscar
            </button>
         </div>
      </form>

/* some code */

```

2 Boton Ver

1 Ya tenemos esta funcionalidad en la vista **DetalleDelEmpleado**

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

2 Identificamos su url:

```python

# ... some code

path('detalles-del-emp/<pk>', 
   views.DetalleDelEmpleado.as_view(),
   name = 'detallesdelemp'),
# ... some code

```

3 En **list_all.html** direccionamos correctamente el href del boton agregandole el parametro:

```html

# ... some code

<td>{{e.id}}</td>
<td>{{e.first_name}}</td>
<td>{{e.last_name}}</td>
<td>{{e.departamento}}</td>
<td>
   <a class="button warning" href="{% url 'empleado_app:detallesdelemp' e.id %}">
      Ver
   </a>
</td>

# ... some code

```

4 Verificamos:

![image](https://github.com/user-attachments/assets/40bc7584-3623-4017-a191-817dd3a8def7)
![image](https://github.com/user-attachments/assets/3bdaae81-24f7-4f7c-bb62-549fa419edb6)
![image](https://github.com/user-attachments/assets/10974a20-fde1-4540-81be-37b7ab498b71)


### 2.3 Paginacion

Cuando a nuestra vista le indicamos un `paginate_by` se crea un objeto de paginacion llamado `page_object`

![image](https://github.com/user-attachments/assets/131055d2-3a95-451e-92cf-b79ee097fcd1)


Copiamos el codigo de Navigation Pagination en Foundation y lo cargamos el final de **list_all.html** dentro de un `<div>`



```html
<nav aria-label="Pagination">
  <ul class="pagination">
    <li class="pagination-previous disabled">Previous <span class="show-for-sr">page</span></li>
    <li class="current"><span class="show-for-sr">You're on page</span> 1</li>
    <li><a href="#" aria-label="Page 2">2</a></li>
    <li><a href="#" aria-label="Page 3">3</a></li>
    <li><a href="#" aria-label="Page 4">4</a></li>
    <li class="ellipsis" aria-hidden="true"></li>
    <li><a href="#" aria-label="Page 12">12</a></li>
    <li><a href="#" aria-label="Page 13">13</a></li>
    <li class="pagination-next"><a href="#" aria-label="Next page">Next <span class="show-for-sr">page</span></a></li>
  </ul>
</nav>
```

<br>
<br>
<br>
<br>

4 marzo.
clase 83 
5 10'

<br>
<br>
<br>
<br>
---
---

```python
# some code...
                        Ver
                     </a>
                  </td>
               </tr>
              {% endfor %}  
            </tbody>
          </table>
      </div>

      # bloque de paginación

      <div class="cell">
         {% if is_paginated %}
            <nav aria-label="Pagination">
               <ul class="pagination">  

                  {% if page_obj.has_previous %}
                     <li class="pagination-previous">
                        <a href="?page={{page_obj.previous_page_number}}">
                           Atras
                        </a> 
                     </li>
                  {% endif %}

                  # Si se está en la página actual, el número de página se resalta sino,
                  # el número no está resaltado pero tiene habilitado el link para ir a el.
        
                  {% for pagina in paginator.page_range %}
                     {% if pagina == page_obj.number  %} 
                        <li class="current">
                           {{pagina}}
                        </li>
                     {% else %}
                        <li class=""> 
                           <a href="?page={{pagina}}">
                              {{pagina}}
                           </a>
                        </li>
                     {% endif %}
                  {% endfor %}

                  {% if page_obj.has_next %}    
                  <li class="pagination-next">
                     <a href="?page={{page_obj.next_page_number}}">
                        Siguiente
                     </a> 
                  </li>
                  {% endif %}

               </ul>
            </nav>
         {% endif %}
      </div>

   </div>
</div>

{% endblock content %}
```

## 3 Pantalla listar departamentos con sus empleados

Queremos desarrollar una vista que liste todos los departamentos con sus nombres y nombres cortos y un botón que nos permita listar los empleados que pertenecen a cada uno.

1 Creamos una vista de tipo **ListView** en la app **departamento**:

```python
# some code...
from django.views.generic import ListView
# some code...
class ListarDepartamentos(ListView):
    model = Departamento
    template_name = "depa/listardepartamentos.html"
    context_object_name = "departamentos"
```

2 Construimos el **listardepartamentos.html** en la carpeta **depa**:

```html
{% extends 'base.html' %}

{% block title %}
   Lista de Departamentos
{% endblock title %}
   
{% block content %}
   {% include 'includes/header.html' %}
   <div class="grid-container">
         <div class="grid-x">
            <h1 class="cell">
               Lista de Departamentos
            </h1>
            <div class="cell">
               <table>
                  <tbody>
                     {% for departamento in departamentos %}
                     <tr>  
                        <td>
                           {{departamento.name}}
                        </td>
                        <td>
                           {{departamento.short_name}}
                        </td>
                        <td>
                           <a class="button warning" href="{#}">
                              Ver empleados
                           </a>
                        </td>
                     </tr>
                     {% endfor %}                                    
                  </tbody>
               </table>

            </div>
         </div>
   </div>
{% endblock content %}
```

3 Activamos la url de la vista

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

app_name = "departamento_app"

urlpatterns = [
   path('listar-departamentos/', 
      views.ListarDepartamentos.as_view(), 
      name = 'listardepartamentos'),
   path('nuevo-empleado-y-departamento/', 
      views.NuevoEmpleadoYDepartamento.as_view(), 
      name = 'nuevoempleadoydepartamento')
]
```

4 Activamos el link de departamentos en el header.html

```html
<div class="top-bar">
   <div class="top-bar-left">
      <ul class="dropdown menu" data-dropdown-menu>
         <li class="menu-text">Empleados</li>
         <li>
            <a href="{% url 'empleado_app:listartodoslosempleados' %}">
               Listar
            </a>
         </li>
         <li>
            <a href="{% url 'departamento_app:listar-departamentos' %}">
               Departamentos
            </a>
         </li>
         <li>
            <a href="#">
               Administrar
            </a>
         </li>
      </ul>
      </div>
      <div class="top-bar-right">
      <ul class="menu">
         <li><input type="search" placeholder="Buscar empleado"></li>
         <li><button type="button" class="button">Registrar nuevo</button></li>
      </ul>
   </div>
 </div>
```

5 Le entregamos funcionalidad al boton 'Ver empleados':

recordemos que esta vista ya la hemos construido en la app empledos:

```python
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

cuya url asociada es:

```python
# some code...
app_name = "empleado_app"

urlpatterns = [
   path('', 
      views.Inicio.as_view(), 
      name = 'inicio'),
   path('listar-todos-los-empleados', 
      views.EmpleadosListView.as_view(),
      name = 'listartodoslosempleados'),
   path('listar-por-departamento', 
      views.ListaPorDeptListView.as_view()),
   path('listar-por-kword', 
      views.EmpleadoPorKwordListView.as_view(),
      name = 'listarporkword'),
# some code...
```

6 agregamos la url correcta:

```
# some code...
<td>
   <a class="button warning" href="{% url 'empleado_app:listarporkword' departamento.short_name %}">
      Ver empleados
   </a>
</td>
# some code...
```

7 Le damos diseño al despliegue de empleados **empleadoporkword.html**:





***
***


***
## Construyendo la pagina de listado de departamentos con la funcionalidad de ver todos los empleados por departamento.

1 Construimos dentro del archivo **views.py** de nuestra aplicacion **departamentos** la vista basada en clases **DepartamentoView**, importando **ListView**. Cramos la vista con sus hmtl y rutas de activacion asociados.
![image](https://github.com/user-attachments/assets/26fae047-ff22-4d9f-97d5-14b59cbeb6ac)
![image](https://github.com/user-attachments/assets/77812958-e710-403c-8926-2a09e3a8889a)
![image](https://github.com/user-attachments/assets/39432ac5-f2b6-4690-a3c5-83f44535b4a3)

2 hacemos el vinculo de la cabecera dirigirse a la url de departamentos, donde seran listados. Por lo que modificamos header.html de la siguiente manera:
![image](https://github.com/user-attachments/assets/ca633886-2587-4685-8745-233a6a2809aa)

Recordemos asignarle un nombre al conjunto de urls de departamentos y hagamos editable el campo name del modelo Departamento:
![image](https://github.com/user-attachments/assets/b090f652-85cb-4954-9e15-9505f2b2b39c)
![image](https://github.com/user-attachments/assets/e8bae8e4-6cbb-4eeb-bb3f-c5d42d8ec8e3)

3 Hacemos la funcionalidad del boton Ver utilizando la vista basada en clase **ListByDept** del archivo views.py de la aplicacion empleados. A la url que activa esta vista le ponemos el nombre **empleados_by_dept** y la direccionamos apropiadamente en nuestra listbydept.html
![image](https://github.com/user-attachments/assets/a40b7c2c-c654-4cab-ae64-5cc12cb15769)
![image](https://github.com/user-attachments/assets/1dbd2420-8d60-4fb2-9c70-e134b980f390)
![image](https://github.com/user-attachments/assets/4754ee9d-3dd1-4a53-a810-0ad9f7bc8cff)

4 Veamos los resultados

![image](https://github.com/user-attachments/assets/a8264b03-a15c-4af2-89a3-c27aa0dbf9b0)
![image](https://github.com/user-attachments/assets/b71f0529-d9bf-4dff-bd33-1bae0771002f)





































