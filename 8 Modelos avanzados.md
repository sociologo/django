# Manejo avanzado de modelos en django (Managers)

Un Manager en Django es una clase que proporciona una interfaz para realizar consultas a la base de datos a través de los modelos. Cada modelo en una aplicación Django tiene al menos un Manager, y el Manager predeterminado se llama objects. Los Managers permiten definir métodos personalizados para realizar consultas específicas y modificar el conjunto de consultas inicial que devuelve el Manager.

Características principales:

- **Interfaz de consulta**: Los Managers son responsables de todas las consultas de base de datos relacionadas con un modelo. Por ejemplo, MyModel.objects.all() utiliza el Manager predeterminado objects para recuperar todos los registros del modelo MyModel.
- **Personalización**: Puedes crear Managers personalizados para añadir métodos específicos que realicen consultas complejas o filtradas. Esto se hace extendiendo la clase models.Manager y añadiendo métodos personalizados.
- **Modificación del QuerySet inicial**: Puedes sobrescribir el método get_queryset() en un Manager personalizado para modificar el conjunto de consultas inicial que devuelve el Manager. Esto es útil para aplicar filtros predeterminados a todas las consultas realizadas a través de ese Manager.
  
## 1 La base de datos biblioteca

![image](https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7)


## 2 Construyendo la aplicacion **biblioteca**

2.1 Creamos el entorno virtual **entorno_2**
```
C:\> cd mis_entornos
C:\mis_entornos> python -m venv entorno_2
C:\mis_entornos> cd entorno_2/Scripts
C:\mis_entornos\entorno_2\Scripts> activate
(entorno_2) C:\mis_entornos\entorno_2\Scripts> cd \
(entorno_2) C:\>
```

2.2 Instalamos las aplicaciones necesarias:
```
(entorno_2) C:\> pip install django
(entorno_2) C:\> pip install unipath
(entorno_2) C:\> python.exe -m pip install --upgrade pip
(entorno_2) C:\> pip install psycopg2-binary
(entorno_2) C:\> pip install django-ckeditor
(entorno_2) C:\> pip install Pillow
```
2.3 Creamos nuestro directorio de trabajo **biblio** y vamos a él:
```
(entorno_2) C:\> cd \mis_proyectos\biblio
```

2.4 Creamos el proyecto:
```
(entorno_2) C:\mis_proyectos\biblio> django-admin startproject biblioteca
```

2.5 Configuracion del proyecto:

2.5.1 Creamos una nueva carpeta llamada **settings** y dentro de ella los archivos **base.py**, **local.py** y **prod.py**. En esta carpeta también creamos un archivo __init__.py para indicarle que dentro existirá código python.

![image](https://github.com/user-attachments/assets/7ab8f9bd-7f2e-4e20-a35c-648a45905d4c)

2.5.2 Copiamos todo de **settings.py** a **base.py** con la excepción de:

- la configuración de la base de datos(con DEBUG = True y ALLOWED_HOSTS = []) y
- STATIC_URL = '/static/', 
- ambas que llevamos a local.py.
  
![image](https://github.com/user-attachments/assets/c9e01425-aab3-43fe-9bf7-9c7926c9eb68)
![image](https://github.com/user-attachments/assets/4cd8c6b4-d596-4c81-a471-a8cd8496af83)
![image](https://github.com/user-attachments/assets/b75fe7b3-87e3-4f59-abc2-25010bab7cfd)
![image](https://github.com/user-attachments/assets/0ad357b7-e82b-4ec3-bffb-e93bb243f61a)

2.5.3 En **base.py** cambiamos las configuraciones de acuerdo a **unipath**.

![image](https://github.com/user-attachments/assets/29f9cecd-d948-4705-81aa-eda995e60ce3)

2.5.4 En **local.py** importamos en **base.py**

![image](https://github.com/user-attachments/assets/6029279a-18ee-42b8-9fdc-6ddd444efd29)

Unipath es una biblioteca de Python que proporciona una interfaz orientada a objetos para trabajar con rutas de archivos y directorios. Simplifica muchas de las operaciones comunes que se realizan con archivos y directorios, haciendo que el código sea más legible y fácil de mantener.

2.5.5 Creamos una carpeta templates a la altura del **manage.py** y configuramos la variable TEMPLATES en **base.py**

![image](https://github.com/user-attachments/assets/cd5792af-10d6-4612-849a-24a6e0cfaaee)
![image](https://github.com/user-attachments/assets/5c2d7225-9a46-4173-8427-c6c1b4ed7f30)

2.5.6 Configuramos **postgresql** en **local.py**
```
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# SECURITY WARNING: don't run with debug turned on in production!
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbiblioteca',
        'USER': 'chris',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
```

2.5.7 Creamos la base de datos en **postgres** 

- Vamos a la shell de postgres 16 en Windows:

- Damos enter hasta Contraseña para usuario postgres: para indicarle que cargue las opciones por defecto. Ingresamos 123456 y creamos nuestra base de datos.

- Creamos un usuario y le damos permisos para acceder a la base de datos recien creada:

```bash
Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Contraseña para usuario postgres:

psql (16.4)
ADVERTENCIA: El código de página de la consola (850) difiere del código
            de página de Windows (1252).
            Los caracteres de 8 bits pueden funcionar incorrectamente.
            Vea la página de referencia de psql «Notes for Windows users»
            para obtener más detalles.
Digite «help» para obtener ayuda.

postgres=# CREATE DATABASE dbbiblioteca;
CREATE DATABASE
postgres=# \c dbbiblioteca
Ahora está conectado a la base de datos «dbbiblioteca» con el usuario «postgres».
dbbiblioteca=# ALTER ROLE chris WITH PASSWORD '123456';
ALTER ROLE
dbbiblioteca=#
```

- Le damos al usuario permisos totales a la base de datos:
```
postgres=# \c dbbiblioteca
Ahora está conectado a la base de datos «dbbiblioteca» con el usuario «postgres».
dbbiblioteca=# GRANT USAGE ON SCHEMA public TO chris;
GRANT
dbbiblioteca=# GRANT CREATE ON SCHEMA public TO chris;
GRANT
dbbiblioteca=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO chris;
GRANT
dbbiblioteca=# GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO chris;
GRANT
dbbiblioteca=#
```

para linux es:
```bash
$ su postgres
Contraseña:
postgres$ createdb dbbiblioteca
postgres$ psql  dbbiblioteca
dbbiblioteca# alter user chris with password '123456';
```

2.6 Configuraciones para evitar **python manage.py runserver --settings=biblioteca.setttings.local**

Cambiamos en manage.py lo siguiente:

![image](https://github.com/user-attachments/assets/469aa24c-fec6-437c-ae7e-8c259ed8f412)

Cambiamos en wsgi.py lo siguiente:

![image](https://github.com/user-attachments/assets/25010979-847f-4010-bc2f-fa3a6dc9ac5a)

2.7 Hacemos las migraciones
```
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```

2.8 Creamos un superusuario para nuestra aplicación
```
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py  createsuperuser
```

chris\
123456

2.9 Ejecutamos nuestra aplicacion

```
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py runserver 
```

## 3 Creación de las aplicaciones

Haremos tres aplicaciones asociadas a los colores de las tablas de la base de datos.

<img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="60%">

1 Aplicación para la gestión de libros (rosa):

Tablas **Libro** y **Categoria**: Esta aplicación se encargará de todas las operaciones relacionadas con los libros y sus categorías. Incluirá modelos, vistas y formularios específicos para gestionar los detalles de los libros, como título, categoría, fecha de lanzamiento, portada, visitas, etc. También gestionará las categorías de los libros, permitiendo crear, actualizar y eliminar categorías.

2 Aplicación para la gestión de autores (azul):

Tabla **Autor**: Esta aplicación se centrará en la gestión de los autores. Incluirá funcionalidades para añadir, editar y eliminar autores, así como para gestionar sus detalles, como nombre, apellido, nacionalidad y edad. Esto permite una separación clara de responsabilidades y facilita la gestión de los datos de los autores de manera independiente.

3 Aplicación para la gestión de préstamos y lectores (verde):

Tablas **Prestamo** y **Lector**: Esta aplicación manejará todo lo relacionado con los préstamos de libros y la gestión de los lectores. Incluirá modelos y vistas para registrar préstamos, gestionar fechas de préstamo y devolución, y controlar si un libro ha sido devuelto. También gestionará los datos de los lectores, como nombre, apellido, nacionalidad y edad.

Ventajas de esta separación:

- Modularidad: Cada aplicación se encarga de una parte específica del sistema, lo que facilita el mantenimiento y la escalabilidad del proyecto.
- Reutilización: Las aplicaciones pueden ser reutilizadas en otros proyectos si es necesario.
- Separación de responsabilidades: Claramente define qué parte del código se encarga de qué funcionalidad, lo que facilita la colaboración en equipos de desarrollo.
- Facilidad de pruebas: Puedes probar cada aplicación de manera independiente, lo que simplifica la detección y corrección de errores.

3.1 Carpeta applications

Construimos dentro de nuestro proyecto una carpeta llamada **aplications** a la altura de manage.py, con un archivo __init__.py.

![image](https://github.com/user-attachments/assets/e3ec54c0-b2d1-4c01-ba81-ae7fcf7f1619)

3.2 Construccion de aplicaciones

Para construir aplicaciones lo hacemos desde la terminal ubicandonos en la carpeta **applications** con:

```
(entorno_2) C:\mis_proyectos\biblio\biblioteca\applications> django-admin startapp libro
(entorno_2) C:\mis_proyectos\biblio\biblioteca\applications> django-admin startapp autor
(entorno_2) C:\mis_proyectos\biblio\biblioteca\applications> django-admin startapp lector
```

3.3 Implementando los modelos de la base de datos y modificando el archivo apps.py en cada una de las aplicaciones:

3.3.1 en models.py y apps.py de la aplicacion autor:
```
from django.db import models # type: ignore

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
```
```
from django.apps import AppConfig # type: ignore
class AutorConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'applications.autor'
```

3.3.2 en models.py y apps.py de la aplicacion libro:
```
from django.db import models # type: ignore
from applications.autor.models import Autor

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores =  models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=200)
    fecha_lanzamiento = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portadas/')
    visitas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo
```
```
from django.apps import AppConfig # type: ignore
class LibroConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'applications.libro'
```

3.3.3 en models.py y apps.py de la aplicacion lector:
```
from django.db import models # type: ignore
from applications.libro.models import Libro

class Lector(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return self.libro.titulo
```
```
from django.apps import AppConfig # type: ignore
class LectorConfig(AppConfig):
   default_auto_field = 'django.db.models.BigAutoField'
   name = 'applications.lector'
```

3.4 Agregar las aplicaciones a **base.py** de la carpeta **settings**:

**Resulta delicado el orden con el que se declaren las aplicaciones aca**

El orden en el que declaras las aplicaciones en el archivo settings.py de Django es importante por varias razones:

- Dependencias entre aplicaciones: Algunas aplicaciones pueden depender de otras. Por ejemplo, si tienes una aplicación que extiende la funcionalidad de django.contrib.auth, esta debe ser declarada después de django.contrib.auth en INSTALLED_APPS.
- Sobrescritura de modelos: Si tienes aplicaciones que sobrescriben modelos de otras aplicaciones, el orden determinará cuál sobrescritura es efectiva. La última aplicación en la lista que sobrescriba un modelo será la que prevalezca.
- Migraciones: El orden puede afectar cómo se aplican las migraciones. Si una aplicación depende de los modelos de otra para sus migraciones, debe ser listada después de la aplicación de la que depende.
- Carga de señales: Las señales en Django se registran cuando la aplicación se carga. Si una señal depende de un modelo de otra aplicación, la aplicación que define el modelo debe ser cargada primero.
- Configuración de middleware: Aunque no es directamente parte de INSTALLED_APPS, el orden de las aplicaciones puede influir en cómo se configuran y aplican los middlewares, ya que algunos middlewares pueden depender de aplicaciones específicas.

![image](https://github.com/user-attachments/assets/918db0e9-a2e9-4797-8aed-4d26e6fbe8c2)


3.4 Hacemos las migraciones:
```
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```

## 4 Managers

### 4.1 Comencemos trabajando sobre la aplicación autor.

- Creamos en ella el archivo urls.py y dentro de él una url que apunte a la vista **ListAutores**:
  
![image](https://github.com/user-attachments/assets/45eed91b-2443-4863-bf9a-7d8945e9005e)

- En views creamos la vista **ListAutores**:

![image](https://github.com/user-attachments/assets/44df6e36-3a83-4afe-9d5c-d80eeff99523)

- Dentro de la carpeta **templates** creamos un **base.html** y una carpeta **autor** dentro de la que construiremos **lista.html**:

![image](https://github.com/user-attachments/assets/44a262ae-8b4f-491e-aa13-0e9f335a139d)

- Incluimos las urls dentro de las urls principales importando re_path e include:

![image](https://github.com/user-attachments/assets/25d0fa92-ae98-4c91-8486-d1f4e765b9d1)

- Creamos un archivo **managers.py**:

![image](https://github.com/user-attachments/assets/c1b84918-6669-4e6a-8418-db5dee461f5d)

- Conectando el modelo con los la clase del manager:

Necesitamos indicarle al modelo que, mediante un atributo, se conecte a la clase que acabamos de construir en **managers.py**:

![image](https://github.com/user-attachments/assets/ef3c3865-ac16-4ddc-b9e5-d1834f4a39ae)

- Editamos el archivo admin.py para poder ingresar datos desde el administrador de django:

![image](https://github.com/user-attachments/assets/f50fdf2e-23f0-4c60-9e80-4f8a131dc1ce)

- Veamos el resultado

![image](https://github.com/user-attachments/assets/c8bbd0a9-3891-4133-a5cf-2e70289edb24)

### 4.2 Filtros por nombre de autor

El lookup **__icontains** en Django se utiliza para realizar búsquedas de texto que no distinguen entre mayúsculas y minúsculas.

- 4.2.1 Modifiquemos la vista para aceptar un parametro.

![image](https://github.com/user-attachments/assets/6f394e11-aee8-4ca1-947e-78c5b36b3774)

- 4.2.2 Modificamos la vista para recibir el parametro y para construir la funcion que haga el filtro

![image](https://github.com/user-attachments/assets/c9933373-f82f-43f4-a04b-1fdc9b3d9cdf)

- 4.2.3 Construimos la clase dentro de manager.py utilizando filter() de la ORM de Django.

![image](https://github.com/user-attachments/assets/ca399513-c2c9-4b36-bae5-9c28d21f8b24)

### 4.3 Filtros por nombre o apellido de autor

El objeto **Q** en Django, representado por django.db.models.Q, se utiliza para construir consultas complejas que involucran múltiples condiciones, especialmente cuando necesitas combinar condiciones con operadores lógicos como AND y OR.

- Importamos la funcion Q y construimos la funcion en managers.py:
  
![image](https://github.com/user-attachments/assets/30275f44-c710-4f5a-906c-86cee0912246)

- Llamamos a la funcion creada en las vistas:
![image](https://github.com/user-attachments/assets/02f98214-5c54-47ed-9758-2f621606b453)

- Corrijamos el html:
![image](https://github.com/user-attachments/assets/773d4133-ac8b-45ab-9f68-3e9ddcc99780)

### 4.4 Exclude()

El método exclude() en Django se utiliza para filtrar objetos que no coinciden con los parámetros de búsqueda especificados. Es decir, devuelve un nuevo QuerySet que contiene objetos que no cumplen con los criterios dados.

![image](https://github.com/user-attachments/assets/4c920abf-3b88-4e32-910b-95e8102ad134)

![image](https://github.com/user-attachments/assets/7adaeef0-9234-439f-99f9-e678822f261b)

![image](https://github.com/user-attachments/assets/dc00250e-94c0-4e97-b393-3575341fce5e)

![image](https://github.com/user-attachments/assets/645e527b-97d7-48d0-a07a-c7fd07eaf5f8)


### Seleccionando por rango de edad y estableciendo criterios de orden en el despliegue:

```
def buscar_autor4(self, kword):
  resultado = self.filter(
     edad__gt = 32,
     edad__lt = 36,
     ).order_by('apellido','nombre','id')
  return resultado
```

![image](https://github.com/user-attachments/assets/e1c72865-6bae-48d9-9be0-1d5be2409118)

### 4.5 Filtros por fechas.

- Tenemos en nuestra aplicacion libro un campo llamado fecha de lanzamiento. Vamos a generar un filtro que nos permita listar los libros que han sido lanzados dentro de un rango de fechas.
  
- Creamos una url en urls.py de la aplicacion libro:
```
from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from . import views

urlpatterns = [
   path('libros/', 
      views.ListLibros.as_view(),
      name ='libros'),
]
```

- Creamos una vista en views.py de la aplicacion libro:
```
from django.shortcuts import render # type: ignore
from django.views.generic import ListView # type: ignore
from .models import Libro
      
class ListLibros(ListView):
   context_object_name ='lista_libros'
   template_name = 'libro/lista.html'

   def get_queryset(self):
      palabra_clave = self.request.GET.get('kword','')
      f1 = self.request.GET.get('fecha1','')
      f2 = self.request.GET.get('fecha2','')

      if f1 and f2:
         return Libro.objects.listar_libros2(palabra_clave, f1, f2)
      else:
         return Libro.objects.listar_libros1(palabra_clave)
```

- Creamos el manager en managers.py de la aplicacion libro:
```
import datetime
from django.db import models # type: ignore
from django.db.models import Q # type: ignore
   
class LibroManager(models.Manager):

   def listar_libros1(self, kword):
      resultado = self.filter(
         titulo__icontains = kword,
         fecha__range('2000-01-01','2010-01-01')
      )
      return resultado

   def listar_libros2(self, kword, fecha1, fecha2):

      date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
      date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()

      resultado = self.filter(
         titulo__icontains = kword,
         fecha__range(date1, date2)
      )
      return resultado
```

- Conectamos el manager con nuestro modelo en models.py de la aplicacion libros:
```
from django.db import models # type: ignore
from applications.autor.models import Autor

from .managers import LibroManager

class Categoria(models.Model):
   nombre = models.CharField(max_length=100)

   def __str__(self):
      return self.nombre

class Libro(models.Model):
   categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
   autores =  models.ManyToManyField(Autor)
   titulo = models.CharField(max_length=200)
   fecha_lanzamiento = models.DateField('Fecha de lanzamiento')
   portada = models.ImageField(upload_to='portadas/')
   visitas = models.PositiveIntegerField(default=0)

  objects = LibroManager()

   def __str__(self):
      return self.titulo
```

- En la carpeta templates creamos una nueva llamada libro y dentro de ella lista.html, donde agregamos dos controles para seleccionar un rango de fechas:
```
<h1>
   Lista de libros
</h1>

<p>
   <form method = "GET">{% csrf_token %}
      <input type = "text" id = "kword" name = "kword" palceholder = "Ingrese nombre">
      <input type = "date" name = "fecha1" id = "fecha1">
      <input type = "date" name = "fecha2" id = "fecha2">
      <button type = "submit">
         Consultar
      </button>
   </form>
</p>

<ul>   
   {% for l in lista_libros %}
      <li>{{l.titulo}} {{l.fecha}}</li>        
   {% endfor %}
</ul>
```

- Incluimos el path en las urls generales:
```
from django.contrib import admin # type: ignore
from django.urls import path, re_path, include # type: ignore

urlpatterns = [
   path('admin/', admin.site.urls),
   re_path('', include('applications.autor.urls')),
   re_path('', include('applications.libro.urls'))
]
```
























