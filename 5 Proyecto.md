# Diseño gráfico del proyecto y puesta a punto de su funcionalidad

Script de arranque:

```bash
C:\Users\chris> cd /
C:\> cd mis_entornos/entorno_3/Scripts
C:\mis_entornos\entorno_3\Scripts> activate
(entorno_3) C:\mis_entornos\entorno_3\Scripts> cd \mis_proyectos\emp3\empleado
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

# Índice

* [1 Construyendo la pantalla de inicio](#1-Construyendo-la-pantalla-de-inicio)
  * [11 Herencia](#11-Herencia)
* [2 Includes](#2-Includes)
  * [21 La cabecera](#21-La-cabecera)
  * [22 Personalizando la cabecera](#22-Personalizando-la-cabecera)
* [3 Pantalla listar empleados](#3-Pantalla-listar-empleados)
  * [31 Formato y funcionalidad al boton listar](#31-Formato-y-funcionalidad-al-boton-listar)
  * [32 Funcionalidad al boton Buscar y Ver](#32-Funcionalidad-al-boton-Buscar-y-Ver)
    * [321 Boton buscar](#321-Boton-buscar)
    * [322 Boton Ver](#322-Boton-Ver)
  * [33 Paginacion](#33-Paginacion)
* [4 Pantalla listar departamentos con sus empleados](#4-Pantalla-listar-departamentos-con-sus-empleados)
* [5 Pantalla administrar](#5-Pantalla-administrar)
* [6 Editando la pantalla de actualizar](#6-Editando-la-pantalla-de-actualizar)
* [7 Editando la pantalla de Eliminar](#7-Editando-la-pantalla-de-Eliminar)
 
# 1 Construyendo la pantalla de inicio

## 11 Herencia

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


# 2 Includes 

## 21 La cabecera

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

## 22 Personalizando la cabecera

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

# 3 Pantalla listar empleados

## 31 Formato y funcionalidad al boton listar

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

## 32 Funcionalidad al boton Buscar y Ver

### 321 Boton buscar

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

### 322 Boton Ver

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


## 33 Paginacion

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

![image](https://github.com/user-attachments/assets/4b6c6b9c-c2f1-4afc-90cb-55982ce5f264)

# 4 Pantalla listar departamentos con sus empleados

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
            <a href="{% url 'departamento_app:listardepartamentos' %}">
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

#### Le entregamos funcionalidad al boton Ver empleados

5 Construimos la vista:

```python
class EmpleadoPorDepa(ListView):
   template_name = "empleado/empleadopordepa.html"
   context_object_name = 'empleadopordepa'

   def get_queryset(self):
      palabra_clave = self.kwargs['sn'] # type: ignore
      lista = Empleado.objects.filter(
         departamento__short_name = palabra_clave
      )
      return lista 
```

6 cuya url asociada es:

```python
# some code...
  path('empleadopordepa/<sn>', 
      views.EmpleadoPorDepa.as_view(),
      name = 'empleadopordepa'), 
# some code...
```

7 agregamos la url correcta:

```
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
            <a class="button warning" href="{% url 'empleado_app:empleadopordepa' departamento.short_name%}">
               Ver empleados
            </a>
         </td>
      </tr>
      {% endfor %}                                    
   </tbody>
</table>
```

8 Le damos diseño al despliegue de empleados **empleadopordepa.html** de la carpeta **empleado**:

```html
<h3>
   Lista de empleados
</h3>

<ul>
   {% for e in empleadopordepa %}
      <li>
         {{e}}
      </li>
   {% endfor %} 
</ul>
```

![image](https://github.com/user-attachments/assets/4b0bac70-13e5-4175-94d7-31d55be772b9)

```python
{% extends 'base.html' %}

{% block title %}
   Lista de empleados por departamento
{% endblock title %}
   
{% block content %}

   {% include 'includes/header.html' %}

   <div class="grid-container">
      <div class="grid-x">
         <div class="cell">
            Empleados por departamento
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
                  {% for e in empleadopordepa %}
                  <tr>
                     <td>{{e.id}}</td>
                     <td>{{e.first_name}}</td>
                     <td>{{e.last_name}}</td>
                     <td>{{e.departamento}}</td>
                     <td>
                        <a class="button warning" href="{% url 'empleado_app:detallesdelemp' e.id %}">
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

![image](https://github.com/user-attachments/assets/f5d6e0cc-dbd0-4f2d-a406-e9c8d6a4bf5c)
![image](https://github.com/user-attachments/assets/ca40953a-001e-4e8d-a758-347c2a69bc85)

# 5 Pantalla administrar

Queremos desplegar una funcionalidad que nos permita desplegar una lista de empleados y poder eliminarlos o editarlos.

1 Construimos una vista ListView llamada AdminEmpleados en la app empleados:

```python
class AdminEmpleados(ListView):
   template_name = "empleado/adminempleados.html"
   context_object_name = 'adminempleados'
   paginate_by = 10
   ordering = 'first_name'
   model = Empleado
```

2 activamos su url asociada:

```python
path('admin-empleados/', 
   views.AdminEmpleados.as_view(),
   name = 'adminempleados'),
```

3 Construimos **adminempleados.html** que copiamos de **list_all.html** eliminando el bloque de formulario:

```html
{% extends 'base.html' %}

{% block content %}

{% include 'includes/header.html' %}

<div class="grid-container">
   <div class="grid-x">
      <h1 class="cell">
         Lista de empleados
      </h1>
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
               {% for e in adminempleados %}
               <tr>
                  <td>{{e.id}}</td>
                  <td>{{e.first_name}}</td>
                  <td>{{e.last_name}}</td>
                  <td>{{e.departamento}}</td>
                  <td>
                     <a class="button warning" href="{% url 'empleado_app:detallesdelemp' e.id %}">
                        Ver
                     </a>
                  </td>
               </tr>
              {% endfor %}  
            </tbody>
          </table>
      </div>
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

4 Editemos la seccion del boton. En vez de que aparezca uno diciendo Ver, deben existir dos, que digan editar y eliminar.

```html
<td>
   <a class="button warning" href="{% url 'empleado_app:detallesdelemp' e.id %}">
      Ver
   </a>
</td>
```

```html
<td>
   <a class="button success" href="#">
      Editar
   </a>
</td>
<td>
   <a class="button alert" href="#">
      Eliminar
   </a>
</td>
```

Recordemos que las vistar para editar y eliminar ya las hicimos. Las urls que las activan son respectivamente:

```python
class ActualizarEmpleado(UpdateView):
   model = Empleado
   template_name = "empleado/actualizarempleado.html"
   fields = ['first_name',
             'last_name',
             'job',
             'departamento',
             'habilidades'] 
   success_url = reverse_lazy('empleado_app:exito')


class EliminarEmpleado(DeleteView):
   model = Empleado
   template_name = "empleado/eliminarempleado.html"
   success_url = reverse_lazy('empleado_app:exito')
   context_object_name = 'eliminarempleado'
```

```python
path('actualizar-empleado/<pk>', 
   views.ActualizarEmpleado.as_view(), 
   name = 'actualizarempleado'),
path('eliminar-empleado/<pk>', 
   views.EliminarEmpleado.as_view(), 
   name = 'eliminarempleado'),
```

Entonces nuestra urls quedan:

```html
<td>
   <a class="button success" href="{% url 'empleado_app:actualizarempleado' e.id %}">
      Editar
   </a>
</td>
<td>
   <a class="button alert" href="{% url 'empleado_app:eliminarempleado' e.id %}">
      Eliminar
   </a>
</td>
```

5 Le damos funcionalidad al boton administrar de la cabecera header.html:

```html
<li>
   <a href="#">
      Administrar
   </a>
</li>
```

```html
<li>
   <a href="{% url 'empleado_app:adminempleados' %}">
      Administrar
   </a>
</li>
```

![image](https://github.com/user-attachments/assets/7eb9766f-73b1-4bc6-8837-4c8834c0ddd5)

# 6 Editando la pantalla de actualizar

Actualmente al darle clic a Actualizar se nos despliega lo siguiente:

![image](https://github.com/user-attachments/assets/601602bc-1028-460f-8b58-5686f4a01a0c)

entonces editemos **actualizarempleado.html**

```html
{% extends 'base.html' %}

{% block title %}
   Editar empleado
{% endblock title %}

{% block content %}
{% include 'includes/header.html' %}

<div class="grid-container">
   <div class="grid-x">
      <h1 class="cell">
         Modificar empleado
      </h1>
      <div class="cell">
         <form class="grid-x grid-margin-x" method="POST">{% csrf_token %}

            <div class="medium-6 cell">
               <label>Nombre
                 {{form.first_name}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Apellido
                 {{form.last_name}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Trabajo
                 {{form.job}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Departamento
                 {{form.departamento}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Habilidades
                 {{form.habilidades}}
               </label>
            </div>

            <div class="cell">
               <button type="submit" class="submit success button">Guardar</button>
            </div>
            
         </form>
      </div>
   </div>
</div>

{% endblock content %}
```

![image](https://github.com/user-attachments/assets/da63651f-93cc-440a-a402-2204f92b46a2)

6 Queremos que una vez un empleado sea editado volvamos a caer en la vista Administrar:

para ello modificamos en success_url:

```python
class ActualizarEmpleado(UpdateView):
   model = Empleado
   template_name = "empleado/actualizarempleado.html"
   fields = ['first_name',
             'last_name',
             'job',
             'departamento',
             'habilidades'] 
   success_url = reverse_lazy('empleado_app:adminempleados')
```

# 7 Editando la pantalla de Eliminar

1 Le damos estilos a la pagina **eliminarempleado.html**

```
{% extends 'base.html' %}

{% block title %}
   Eliminar empleados
{% endblock title %}
   
{% block content %}
{% include 'includes/header.html' %}

<div>
   <div>
      <h1 class="cell">
         Eliminar empleado: {{eliminarempleado.full_name}}
      </h1>
      <form class="cell" method = "POST">{% csrf_token %}
         <div class="callout secondary">
            <h5>Confirme que desea eliminar a este empleado</h5>
            <button type="submit" class="alert button">Confirmar</button>
          </div>
      </form>
   </div>
</div>
{% endblock content %}
```

2 Queremos que una vez un empleado sea eliminado volvamos a caer en la vista Administrar:

para ello modificamos en success_url:

```python
class EliminarEmpleado(DeleteView):
   model = Empleado
   template_name = "empleado/eliminarempleado.html"
   success_url = reverse_lazy('empleado_app:adminempleados')
   context_object_name = 'eliminarempleado'
```

# 8 Dando funcionalidad al boton de Registrar Nuevo empleado

1 Identifiquemos la vista que ya hemos construido y que hacia el registro:

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

   def form_valid(self, form):
      empleado = form.save(commit = False)
      empleado.full_name = empleado.first_name + ' ' + empleado.last_name
      empleado.save()
      return super(CrearEmpleado, self).form_valid(form)
```

2 Y la url que lo activa, 

```python
path('crear-emp', 
   views.CrearEmpleado.as_view(), 
   name = 'crearempleado'),
```

3 Llevamos la url a nuestro **header.html**:

```python
<div class="top-bar-right">
   <ul class="menu">
      <li>
         <input type="search" placeholder="Buscar empleado">
      </li>
      <li>
         <a href="{% url 'empleado_app:crearempleado' %}" class="button" class="button">Registrar nuevo</a>
      </li>
   </ul>
</div>
```

4 Le damos diseño al template **crearempleado.html**

```html
{% extends 'base.html' %}

{% block title %}
Registrar empleados
{% endblock title %}
   
{% block content %}
   {% include 'includes/header.html' %}

   <div class="grid-container">
      <div class="grid-x">
         <h1 class="cell">
            Registrar empleado 
         </h1>
         <form class="cell grid-x grid-margin-x" method = "POST">{% csrf_token %}
            <div class="medium-6 cell">
               <label>Nombre
                  {{form.first_name}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Apellido
                  {{form.last_name}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Trabajo
                  {{form.job}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Departamento
                  {{form.departamento}}
               </label>
            </div>
            <div class="medium-12 cell">
               <label>Habilidades
                  {{form.habilidades}}
               </label>
            </div>
            <div class="medium-12 cell">
               <button type="submit" class="button success">
                  Guardar
               </button>
             </div>
         </form>
      </div>
   </div>

{% endblock content %}
```

5 Al ingresar un registro, queremos que la aplicacion nos redirija a la pagina Administrar:

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
   success_url = reverse_lazy('empleado_app:adminempleados')

   def form_valid(self, form):
      empleado = form.save(commit = False)
      empleado.full_name = empleado.first_name + ' ' + empleado.last_name
      empleado.save()
      return super(CrearEmpleado, self).form_valid(form)
```

![image](https://github.com/user-attachments/assets/1fc3a59c-8930-4982-bd80-e427b6d986c6)

# 9 Administrando archivos multimedia

1 models.ImageField

Observemos el modelo que nos permite registrar un empleado:

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

la linea:

```python
avatar = models.ImageField(upload_to = 'empleado', blank = True, null = True)
```

indica que la imagen asociada al registro que ingresemos se ubicará en una carpeta llamada **empleados** (Django la crea si no existe). Construyamos una carpeta llamada **media** que la albergue. 

2 Configuracion en local.py

Debemos configurar correctamente la ruta de redireccionamiento, para ello vamos a **local.py** y agregamos la url para que se generen los archivos multimedia.

```python
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado101',
        'USER': 'chris101',
        'PASSWORD': 'nueva123456',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATIC_URL = 'static/'

STATICFILES_DIRS = [
   BASE_DIR / "static",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

3 Debemos registar esta URL en nuestro registro general de urls:

```python
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static  # type: ignore

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include("applications.empleados.urls")),
   path('', include("applications.exp.urls")),
   path('', include("applications.departamentos.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

4 En la vista agregamos el campo:

```python
class CrearEmpleado(CreateView):
   model = Empleado
   template_name = "empleado/crearempleado.html"
   fields = ['first_name',
             'last_name',
             'job',
             'departamento',
             'habilidades',
             'avatar'] 
   # fields = ('__all__')
   success_url = reverse_lazy('empleado_app:adminempleados')
```

5 Agregamos el campo en el formulario:

```python
# some code...

<div class="medium-12 cell">
   <label>Habilidades
      {{form.habilidades}}
   </label>
</div>
<div class="medium-12 cell">
   <label>Foto
      {{form.avatar}}
   </label>
</div>

# some code...
```

6 Debemos agregar al html enctype="multipart/form-data"

```python
{% extends 'base.html' %}

{% block title %}
Registrar empleados
{% endblock title %}
   
{% block content %}
   {% include 'includes/header.html' %}

   <div class="grid-container">
      <div class="grid-x">
         <h1 class="cell">
            Registrar empleado 
         </h1>
         <form class="cell grid-x grid-margin-x" method = "POST" enctype="multipart/form-data">{% csrf_token %}
            <div class="medium-6 cell">
               <label>Nombre
                  {{form.first_name}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Apellido
                  {{form.last_name}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Trabajo
                  {{form.job}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Departamento
                  {{form.departamento}}
               </label>
            </div>
            <div class="medium-12 cell">
               <label>Habilidades
                  {{form.habilidades}}
               </label>
            </div>
            <div class="medium-12 cell">
               <label>Foto
                  {{form.avatar}}
               </label>
            </div>
            <div class="medium-12 cell">
               <button type="submit" class="button success">
                  Guardar
               </button>
             </div>
         </form>
      </div>
   </div>

{% endblock content %}
```

7 Verificamos:

![image](https://github.com/user-attachments/assets/df5bc406-7d4e-4fab-a55f-37fa360ec9e2)

Abrimos la foto desde el administrador:

![image](https://github.com/user-attachments/assets/240ab96c-675d-4228-9efe-dee4764adbd5)

# 10 Ingresando registros en dos modelos simultáneamente.

1 La funcionalidad

Recordemos que ya hemos hecho la funcionalidad de esto en la aplicación **departamentos**:

```python
class NuevoEmpleadoYDepartamento(FormView):
   template_name = 'depa/nuevoempleadoydepartamento.html'
   form_class = EmpleadoYDepartamento
   success_url = reverse_lazy('empleado_app:exito')

   def form_valid(self, form):

      depa = Departamento(
         name = form.cleaned_data['departamento'],
         short_name = form.cleaned_data['shortname']
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

Asociado al siguiente formulario:

```python
from django import forms # type: ignore

class EmpleadoYDepartamento(forms.Form):
   nombre = forms.CharField(max_length=50)
   apellido = forms.CharField(max_length=50)
   departamento = forms.CharField(max_length=50)
   shortname = forms.CharField(max_length=20)
```

2 Necesitamos es personalizar **nuevoempleadoydepartamento.html**

```python
{% extends 'base.html' %}

{% block title %}
Registrar nuevo empleado y departamento
{% endblock title %}
   
{% block content %}
   {% include 'includes/header.html' %}

   <div class="grid-container">
      <div class="grid-x">
         <h1 class="cell">
            Registrar nuevo empleado y departamento 
         </h1>
         <form class="cell callout grid-x grid-margin-x" method = "POST">{% csrf_token %}
            <div class="medium-6 cell">
               <label>Nombre
                  {{form.nombre}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Apellido
                  {{form.apellido}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>departamento
                  {{form.departamento}}
               </label>
            </div>
            <div class="medium-6 cell">
               <label>Nombre corto
                  {{form.shortname}}
               </label>
            </div>
            <div class="medium-12 cell">
               <button type="submit" class="button success">
                  Guardar
               </button>
             </div>
         </form>
      </div>
   </div>

{% endblock content %}
```

3 Añadimos esta funcionalidad en el header:

```python
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
            <a href="{% url 'departamento_app:listardepartamentos' %}">
               Departamentos
            </a>
         </li>
         <li>
            <a href="{% url 'empleado_app:adminempleados' %}">
               Administrar
            </a>
         </li>
         <li>
            <a href="{% url 'departamento_app:nuevoempleadoydepartamento' %}">
               Ingresar empleado y departamento
            </a>
         </li>
      </ul>
   </div>
   <div class="top-bar-right">
      <ul class="menu">
         <li><input type="search" placeholder="Buscar empleado"></li>
         <a href="{% url 'empleado_app:crearempleado' %}" class="button" class="button">Registrar nuevo</a>
      </ul>
   </div>
 </div>
```

![image](https://github.com/user-attachments/assets/d82d1102-6402-43a8-8aed-ea60dbb5ad3d)

# 11 Dandole formato a la pantalla Ver Empleado.

1 Actualmente esta pantalla se despliega asi:

![image](https://github.com/user-attachments/assets/423e3146-bc2c-4d1f-bb7a-f64578cafee5)

2 Identifiquemos el template y su vista. Es **detalledelempleado.html**

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
<h1>
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

3 Démosle la estructura ya conocida copiando la estructura Card de Foundation:

Le añadimos una validación para el caso de que el registro no posea una imagen.

Utilizamos `get_job_display` en:

```html
<div class="card-divider">
  {{detalledelempleado.get_job_display}}
</div>
```
que funciona en un atributo del tipo `choices` para recuperar su valor real y no su número.

Habilidades es un conjunto, por lo que para recuperar sus datos debemos hacer una iteración:

```html
{% extends 'base.html' %}

{% load static %}

{% block title %}
   {{detalledelempleado.full_name}}
{% endblock title %}
   
{% block content %}
{% include 'includes/header.html' %}

<div class="grid-container">
   <div class="grid-x grid-margin-x align-center">
      <div class="cell large-4 card" style="width: 300px; margin-top: 10px;">
         <div class="card-divider">
           Trabajo:{{detalledelempleado.get_job_display}}
         </div>
         
         {% if detalledelempleado.avatar %}
            <img src="{{detalledelempleado.avatar.url}}">
         {% else %}
            <img src="{% static 'img/nohayimagen.jpg' %}">
         {% endif %}
            
         <div class="card-section">
            <h4>Nombre completo:{{detalledelempleado.full_name}}</h4>
            <p>Apellido:{{detalledelempleado.last_name}}</p>
            <p>Departamento:{{detalledelempleado.departamento.short_name}}</p>
            <p> 
               <span class="label">
                  Habilidades
               </span>
            </p>
            <ul class="vertical menu">
               {% for h in detalledelempleado.habilidades.all %}
                  <li>
                     {{h.habilidad}}
                  </li>
               {% endfor %}
            </ul>
         </div>
      </div>
   </div>
</div>

{% endblock content %}
```

4 Veamos ahora su despliegue:

![image](https://github.com/user-attachments/assets/9945157f-add7-4006-85e0-f795ae7c926b)

# 12 Personalizando campos con un formulario

***
***

<br>
<br>
<br>
<br>

aca voy
7 marzo.
voy iniciando la clase 93

<br>
<br>
<br>
<br>
---
---
























