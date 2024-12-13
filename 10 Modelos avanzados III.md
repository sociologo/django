# Modelos avanzados II

Debo corregir esto. En realidad este archivo es modelos avanzados II, modelos avanzados I debe ser la construccion de la aplicacion biblioteca.

En definitiva debe quedar asi:

-1 Modelos avanzados - construcción de la aplicación.\
-2 Modelos avanzados I.\
-3 Modelos avanzados II.

IMPORTANTE: DEBES utilizar la ORM de Django cada vez que puedas en vez de usar solamente codigo python al hacer consultas a la base de datos, para optimizar al maximo. La ORM de Django estan absolutamente documentadas todas las posibilidades de interacciones con las bases de datos.

```bash
cd /
C:\> cd /mis_entornos/entorno_2/Scripts
C:\mis_entornos\entorno_2\Scripts> activate
(entorno_2) C:\mis_entornos\entorno_1\Scripts> cd \mis_proyectos\biblio\biblioteca
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py runserver 
```

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```

IMPORTANTE: Son COMUNES las salidas erroneas cuando verificamos los managers por la shell, por lo que es conveniente reiniciar la shell de Django `>>> exit()` cada vez que se va a revisar el comportamiento de un manager.

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py shell
>>> exit()
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="120%">
</p>

## Índice

* [1 Values I](#1-Values-I)
  * [11 Características](#11-Caracteristicas)
* [2 Values II](#2-Values-II)
* [3 Herramientas de Postgres para busquedas (trigram similarity)](#3-Herramientas-de-Postgres-para-busquedas-(trigram-similarity))
  * [3.1 Concepto e instalacion](#31-Concepto-e-instalacion)
  * [3.2 Implementacion de triagram](#32-Implementacion-de-triagram)
* [4 Registrando datos dentro de nuestra base de datos La class Meta](#4-Registrando-datos-dentro-de-nuestra-base-de-datos-La-class-Meta)
  * [41 Introduccion](#41-Introduccion)
  * [42 Los nombres de las tablas creadas en Postgres desde Django](#42-Los-nombres-de-las-tablas-creadas-en-Postgres-desde-Django)
  * [43 Asignando nombres personalizados a tablas en postgres](#43-Asignando-nombres-personalizados-a-tablas-en-postgres)
* [5 Herencia](#5-Herencia)

# 1 Values I

Consideremos la tabla **Prestamo**. Queremos saber **cuántas veces se ha prestado cada libro**. Esto podríamos resolverlo con un **annotate()** construyendo un manager en el modelo Prestamo.

```python
 def num_libros_prestados(self): 
    resultado = self.annotate( 
       num_prestados = Count('libro')      
    )
    for r in resultado:
       print('---')
       print(r, r.num_prestados)
    return resultado
```

Verificamos en la shell:

```bash
from applications.lector.models import *
Prestamo.objects.num_libros_prestados()
```

![image](https://github.com/user-attachments/assets/282937d9-cb13-4f19-856f-dd5b7bd058db)
![image](https://github.com/user-attachments/assets/d5ea8d69-95a2-48e4-8941-6358240820ab)

Vemos que lista todo.

Lo que sucede es que **annotate()** requiere de un criterio de agrupación que, por defecto, **toma del id de prestamo**, lo que genera un error en el despliegue de resultados: los lista todos. La consulta deberia hacerse dentro del modelo Libro. No olvidemos utilizar la clave inversa: libro_prestamo.

```python
class LibroManager(models.Manager):

// some code
   
   def num_libros_prestados(self): 
      resultado = self.annotate( 
         num_prestados = Count('libro_prestamo')      
      )
      for r in resultado:
         print('---')
         print(r, r.num_prestados)
      return resultado
```

Verificamos en la shell:

```bash
from applications.libro.models import *
Libro.objects.num_libros_prestados()
```

**Me dice la shell que no reconoce la funcion**

Modificamos el manager:

La función values() en Django se utiliza para crear una QuerySet que devuelve diccionarios en lugar de instancias de modelos. Cada diccionario representa un objeto y **las claves** del diccionario son los nombres de los campos del modelo. Con **values** indicamos el criterio sobre el cual agrupar.

```python
class PrestamoManager(models.Manager): 

// some code
   
   def num_libros_prestados(self): 
      resultado = self.values('libro'
      ).annotate( 
         num_prestados = Count('libro')      
      )
      for r in resultado:
         print('---')
         print(r, r['num_prestados'])
      return resultado
```

Verificamos en la shell:

```bash
from applications.lector.models import *
Prestamo.objects.num_libros_prestados()
```

**Me continua desplegado el resultado sin considerar la modificacion a la funcion**

# 2 Values II

Ahora, queremos que la consulta devuelva el titulo del libro, para ello utilizamos la función **Lower**.

```python
from django.db.models.functions import Lower # type: ignore
 
class PrestamoManager(models.Manager): 

//some code
   
   def num_libros_prestados(self): 
      resultado = self.values('libro'
      ).annotate( 
         num_prestados = Count('libro'),
         titulo = Lower('libro__titulo')     
      )
      for r in resultado:
         print('---')
         print(r, r['num_prestados'])
      return resultado
```

Verificamos en la shell:

```bash
from applications.lector.models import *
Prestamo.objects.num_libros_prestados()
```

![image](https://github.com/user-attachments/assets/fd86b2c7-628f-4685-aea9-2d23730f759b)

podemos agregar la funcionalidad de incluir un lector:

```python
from django.db.models.functions import Lower # type: ignore
 
class PrestamoManager(models.Manager): 

//some code
   
   def num_libros_prestados(self): 
      resultado = self.values('libro','lector'
      ).annotate( 
         num_prestados = Count('libro'),
         titulo = Lower('libro__titulo')     
      )
      for r in resultado:
         print('---')
         print(r, r['num_prestados'])
      return resultado
```

![image](https://github.com/user-attachments/assets/7d040b34-c4ae-47ba-bbdc-0eb29350011d)

# 3 Herramientas de Postgres para busquedas (trigram similarity)

## 3.1 Concepto e instalacion

Queremos un buscador que nos retorne un libro a partir de una palabra clave. La trigram similarity de postgres en Django es una técnica que permite realizar búsquedas de texto más flexibles y precisas utilizando el concepto de trigramas. Un trigrama es una **secuencia de tres caracteres consecutivos** de una cadena que se combinan obteniendo diferentes secuencias para hacer un calculo de probabilidades que coincida con algun dato. Esta técnica se utiliza para medir la similitud entre cadenas de texto, lo que es útil para encontrar coincidencias aproximadas.

Debemos activar triagram e indicar sobre que tabla y atributo actúe postgres. Vamos a la shell de Postgres sobre Windows:

Para ir a PowerShell como administrador:

- 1 presiona Windows + X y selecciona "Terminal (Administrador)".
- 2 dirígete al binario de postgres
- 3 conéctate a la base de datos como superusuario
- 4 ingresa la contraseña
- 5 crear la extensión pg_trgm.

```bash
Windows PowerShell
Copyright (C) Microsoft Corporation. Todos los derechos reservados.

Instale la versión más reciente de PowerShell para obtener nuevas características y mejoras. https://aka.ms/PSWindows

PS C:\Users\chris> cd 'C:\Program Files\PostgreSQL\16\bin'

PS C:\Program Files\PostgreSQL\16\bin> .\psql -U postgres -d dbbiblioteca
Contraseña para usuario postgres:

psql (16.4)
ADVERTENCIA: El código de página de la consola (850) difiere del código
            de página de Windows (1252).
            Los caracteres de 8 bits pueden funcionar incorrectamente.
            Vea la página de referencia de psql «Notes for Windows users»
            para obtener más detalles.
Digite «help» para obtener ayuda.

dbbiblioteca=# CREATE EXTENSION pg_trgm;
CREATE EXTENSION
dbbiblioteca=#
```

- 6 crea el index:

```bash
dbbiblioteca=# CREATE INDEX libro_titulo_idx ON libro_libro USING GIN(titulo gin_trgm_ops);
CREATE INDEX
dbbiblioteca=#

GIN(titulo gin_trgm_ops);: titulo es el atributo sobre el cual queremos que actue la triagramación.
```

## 3.2 Implementacion de triagram

- 1 Debemos indicarle a Django que trabajaremos con la triagramacion de Postgres.

Para ello nos dirigimos a **base.py** de la aplicacion biblioteca y le indicamos que traiga complementos de postgres para django:

![image](https://github.com/user-attachments/assets/e8172c2a-95ab-458b-bc6b-0a036abd2a75)

- 2 Creamos el manager:

Importamos TrigramSimilarity y creamos el manager listar_libros_trg en la clase **LibroManager()**:

```python
from django.contrib.postgres.search import TrigramSimilarity # type: ignore
   
class LibroManager(models.Manager):

   def listar_libros_trg(self,kword):
      if kword:
         resultado = self.filter(
            titulo__trigram_similar = kword,
         )
         return resultado
      else:
         return self.all()[:10]
      return resultado
```     
      
- 3 Creamos una vista en views.py de la aplicacion libro:

```python
class ListLibrosTrg(ListView):
   context_object_name ='lista_libros'
   template_name = 'libro/lista.html'

   def get_queryset(self):
      palabra_clave = self.request.GET.get('kword','')

      return Libro.objects.listar_libros_trg(palabra_clave)
```
      
- 4 construimos una url en urls.py de la app libro:

```python
   path(
      'libros-trg/', 
      views.ListLibrosTrg.as_view(),
      name ='libros-trg'
  ),
```

# 4 ORM Registrando datos dentro de una Base de Datos

## 41 La clase Meta

En Django, la clase Meta es una clase interna que se utiliza para proporcionar opciones de configuración adicionales a un modelo. Estas opciones permiten personalizar el comportamiento del modelo, como el nombre de la tabla en la base de datos, el orden de los registros, las restricciones únicas, entre otros. Es así como podemos cambiar el nombre a la tabla Libro en singular y plural y darle un criterio de orden en su despliegue en el administrador de Django:

```python
class Libro(models.Model):
   categoria = models.ForeignKey(
      Categoria, 
      on_delete=models.CASCADE,
      related_name = 'categoria_libro')
   autores =  models.ManyToManyField(Autor)
   titulo = models.CharField(max_length=200)
   fecha_lanzamiento = models.DateField('Fecha de lanzamiento')
   portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
   visitas = models.PositiveIntegerField(default=0)

   objects = LibroManager()

   class Meta:
      verbose_name = 'book'
      verbose_name_plural = 'books'
      ordering =  ['titulo', 'fecha']

   def __str__(self):
      return str(self.id) + ' - ' + self.titulo
```

## 42 Los nombres de las tablas creadas en Postgres desde Django

Las tablas que se crean en Postgres no tienen los mismos nombres con los que las creamos en Django.

Despleguemos la base de datos desde la consola de Postgres y veamos como se han creado las tablas de nuestras aplicaciones:

- 1 presiona Windows + X y selecciona "Terminal (Administrador)".
- 2 PS C:\Users\chris> cd 'C:\Program Files\PostgreSQL\16\bin'
- 3 PS C:\Program Files\PostgreSQL\16\bin> .\psql -U postgres -d dbbiblioteca
  
```bash
dbbiblioteca=# \dt
                Listado de relaciones
 Esquema |           Nombre           | Tipo  | Due±o
---------+----------------------------+-------+-------
 public  | auth_group                 | tabla | chris
 public  | auth_group_permissions     | tabla | chris
 public  | auth_permission            | tabla | chris
 public  | auth_user                  | tabla | chris
 public  | auth_user_groups           | tabla | chris
 public  | auth_user_user_permissions | tabla | chris
 public  | autor_autor                | tabla | chris
 public  | django_admin_log           | tabla | chris
 public  | django_content_type        | tabla | chris
 public  | django_migrations          | tabla | chris
 public  | django_session             | tabla | chris
 public  | lector_lector              | tabla | chris
 public  | lector_prestamo            | tabla | chris
 public  | libro_categoria            | tabla | chris
 public  | libro_libro                | tabla | chris
 public  | libro_libro_autores        | tabla | chris
(16 filas)

dbbiblioteca=#
```

Postgres crea los nombres de tablas con el nombre de la app y luego el nombre de la tabla, ej: **libro_categoria**.

La **class Meta** nos sirve para modificar cosas como estas. Crearemos una nueva aplicación en nuestra app biblioteca para prácticas llamada **home** con un modelo llamado **Persona**, con cuyo nombre queremos exactamente se cree la tabla en Postgres con ayuda del atributo **db_table**:

## 43 Asignando nombres personalizados a tablas en postgres

- 1 Construímos la aplicación:

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca\applications> django-admin startapp home
```

- 2 Construímos el modelo **Persona**:

```python
from django.db import models

# Create your models here.

class Persona(models.Model):
   """Model definition for Persona."""

   full_name = models.CharField('nombres', max_length=50)
   pais = models.CharField('Pais', max_length=30)
   pasaporte = models.CharField('Pasaporte', max_length=50)
   edad = models.IntegerField()
   apelativo = models.CharField('Apelativo', max_length=10)

   class Meta:
      """Meta definition for Persona."""

      verbose_name = 'Persona'
      verbose_name_plural = 'Personas'
      db_table = 'persona'

   def __str__(self):
      """Unicode representation of Persona."""
      return self.full_name
```

- 3 Incluimos la nueva App **home** dentro de los INSTALLED_APP en **base.py**:

![image](https://github.com/user-attachments/assets/600b6f0e-2230-43c5-a21b-9c27641971a9)

- 4 Hacemos las migraciones

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```

- 5 Verifiquemos:

```bash
PS C:\Users\chris> cd 'C:\Program Files\PostgreSQL\16\bin'
PS C:\Program Files\PostgreSQL\16\bin> .\psql -U postgres -d dbbiblioteca
dbbiblioteca=# \dt
```

- 6 Añadiendo atributos del tipo class Meta al modelo Persona:

Queremos que una persona de un pais que se ingrese en la aplicacion tenga solo un único apelativo combinando pais y apelativo:

```python
   class Meta:
      """Meta definition for Persona."""

      verbose_name = 'Persona'
      verbose_name_plural = 'Personas'
      db_table = 'persona'
      unique_together = ['pais', 'apelativo']
```

Queremos validar que no se registren datos con edades menores a 18

```python
   class Meta:
      """Meta definition for Persona."""

      verbose_name = 'Persona'
      verbose_name_plural = 'Personas'
      db_table = 'persona'
      unique_together = ['pais', 'apelativo']
      constraints = [
         models.CheckConstraint(check = models.Q(edad__gte = 18), name = 'edad_mayor_18')
         ]
```

Siempre que se necesite de una validacion y esta pueda resolverse de forma simple se debe hacer aqui porque es una barrera más de validacion.

- 7 agregamos el modelo a Admin de la app home:
  
```python
from django.contrib import admin
from .models import Persona, Empleados

# Register your models here.

admin.site.register(Persona)
```

- 8 hacemos las migraciones

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```

- 9 verificamos en el Admin

# 5 Herencia

- 1 Agreguemos los modelos **Empleados** y ** Cliente** que hereden de **Persona** con atributos específicos a cada uno llamados **empleo** y **email**:

```python
from django.db import models # type: ignore

# Create your models here.

class Persona(models.Model):
   """Model definition for Persona."""

   full_name = models.CharField('nombres', max_length=50)
   pais = models.CharField('Pais', max_length=30)
   pasaporte = models.CharField('Pasaporte', max_length=50)
   edad = models.IntegerField()
   apelativo = models.CharField('Apelativo', max_length=10)

   class Meta:
      """Meta definition for Persona."""

      verbose_name = 'Persona'
      verbose_name_plural = 'Personas'
      db_table = 'persona'
      unique_together = ['pais', 'apelativo']
      constraints = [
         models.CheckConstraint(check = models.Q(edad__gte = 18), name = 'edad_mayor_18')
         ]

   def __str__(self):
      """Unicode representation of Persona."""
      return self.full_name

class Empleados(Persona):
   empleo = models.CharField('empleo', max_length=50)

class Cliente(Persona):
   email = models.EmailField('Email')
```

- 2 Registramos la clase que hereda en el admin:

```python
from django.contrib import admin
from .models import Persona, Empleados, Cliente

# Register your models here.

admin.site.register(Persona)
admin.site.register(Empleados)
admin.site.register(Cliente)
```

- 3 hacemos las migraciones

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```

- 4 Verifiquemos la clase Empleados en el Admin

## 51 Abstract

Lo que deseamos es que se desplieguen en el Admin las clases Cliente y Empleados pero no la de Persona. No queremos que se cree en la base de datos la tabla Persona. Para ello utilizamos el atributo **abstract**.

```python
from django.db import models # type: ignore

# Create your models here.

class Persona(models.Model):
   """Model definition for Persona."""

   full_name = models.CharField('nombres', max_length=50)
   pais = models.CharField('Pais', max_length=30)
   pasaporte = models.CharField('Pasaporte', max_length=50)
   edad = models.IntegerField()
   apelativo = models.CharField('Apelativo', max_length=10)

   class Meta:
      """Meta definition for Persona."""

      verbose_name = 'Persona'
      verbose_name_plural = 'Personas'
      db_table = 'persona'
      unique_together = ['pais', 'apelativo']
      constraints = [
         models.CheckConstraint(check = models.Q(edad__gte = 18), name = 'edad_mayor_18')
         ]
      abstract = True

   def __str__(self):
      """Unicode representation of Persona."""
      return self.full_name

class Empleados(Persona):
   empleo = models.CharField('empleo', max_length=50)

class Cliente(Persona):
   email = models.EmailField('Email')
```

## 52 Aplicando herencia a nuestro proyecto I

- 1 Construiremos una clase persona desde la cual van a heredar las clases lector y autor. Para ello, primero debemos homogeneizar la estructura de ambos modelos:

```python
from django.db import models # type: ignore

from .managers import AutorManager

class Autor(models.Model):
   nombres = models.CharField(max_length=50)
   apellidos = models.CharField(max_length=50)
   nacionalidad = models.CharField(max_length=20)
   edad = models.PositiveIntegerField()

   objects = AutorManager()

   def __str__(self):
      return f"{str(self.id)} {self.nombres} {self.apellidos}"
```

```python
from django.db import models # type: ignore
from applications.libro.models import Libro

from .managers import PrestamoManager # type: ignore

class Lector(models.Model):
   nombres = models.CharField(max_length=50)
   apellidos = models.CharField(max_length=50)
   nacionalidad = models.CharField(max_length=20)
   edad = models.PositiveIntegerField(default=0)

   def __str__(self):
      return f"{self.nombres} {self.apellidos}"
```

- 2 Quitemos la aplicacion home y hagamos las migraciones

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```

# Digresion Backup de una base de datos

Necesitamos hacer una reestructuración de nuestra base de datos pero sin perder la información que tengamos en ella. Para eso, haremos un Backup de nuestra información.

- 1 Creamos una carpeta dentro de la carpeta **biblio** llamada **resguardo**.

- 2 Ingresemos a Postgres y hagamos la migración:

```bash
PS C:\Users\chris> cd 'C:\Program Files\PostgreSQL\16\bin'
.\pg_dump -U postgres -d dbbiblioteca -F c -b -v -f "C:\mis_proyectos\biblio\resguardo\dbbiblioteca_backup.sql"
```

- 3 Eliminamos la base de datos en Postgres

```bash
cd "C:\Program Files\PostgreSQL\16\bin"
.\psql -U postgres
DROP DATABASE dbbiblioteca;
```

- 4 Volvemos a crear la base de datos
  
```bash
cd "C:\Program Files\PostgreSQL\16\bin"
.\psql -U postgres
CREATE DATABASE dbbiblioteca;
GRANT ALL PRIVILEGES ON DATABASE dbbiblioteca TO chris;
```

- 5 restauramos la data de nuestra base de datos:

```bash
# Sal del cliente psql:
\q

# Restaura la base de datos desde el archivo de respaldo:
.\pg_restore -U postgres -d dbbiblioteca "C:\mis_proyectos\biblio\resguardo\dbbiblioteca_backup.sql"
```

- 6 Borramos de nuestro proyecto Django todas las migraciones.

Debe quedar solo __init__.py

## 53 Aplicando herencia a nuestro proyecto II

- 1 Modificamos **models.py** de la app **autor**:

```python
from django.db import models # type: ignore

from .managers import AutorManager

class Persona(models.Model):
   nombres = models.CharField(max_length=50)
   apellidos = models.CharField(max_length=50)
   nacionalidad = models.CharField(max_length=20)
   edad = models.PositiveIntegerField()

   def __str__(self):
      return f"{str(self.id)} {self.nombres} {self.apellidos}"

   class Meta:
      abstract = True

class Autor(Persona):
   objects = AutorManager()
```

- 2 Modificamos **models.py** de la app **lector**:

```python
from django.db import models # type: ignore
from applications.libro.models import Libro
from applications.autor.models import Persona

from .managers import PrestamoManager # type: ignore

class Lector(Persona):
   
   class Meta:
      verbose_name = 'Lector'
      verbose_name_plural = 'Lectores'

class Prestamo(models.Model):
   lector = models.ForeignKey(
      Lector, 
      on_delete=models.CASCADE)
   libro = models.ForeignKey(
      Libro, 
      on_delete=models.CASCADE,
      related_name = 'libro_prestamo')
   fecha_prestamo = models.DateField()
   fecha_devolucion = models.DateField(blank=True, null=True)
   devuelto = models.BooleanField(default=False)

   objects = PrestamoManager()

   def __str__(self):
      return f"Prestamo de {self.libro.titulo} a {self.lector.nombre} {self.lector.apellido}"
```

- 3 Hacemos las migraciones:
  
```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```

Tenemos que ya nuestras tablas han sido creadas, por lo que haremos una falsa migración.

El argumento `--fake` en el comando `python manage.py migrate` se utiliza para marcar una migración como aplicada sin realmente ejecutar los cambios en la base de datos. Esto puede ser útil en situaciones donde sabes que los cambios ya se han aplicado manualmente o cuando estás sincronizando el estado de las migraciones entre diferentes entornos.

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate --fake
```

- 4 Verificamos en Admin autores:

- 5 Agreguemos un atributo a nuestro modelo Autor:
- 
```python
class Autor(Persona):
   seudonimo = models.CharField('seudonimo', max_length=50, blank = True)
   objects = AutorManager()
```

- 6 volvamos a hacer las migraciones:

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```

- 7 Verificamos en Admin autores:

# 6 Registrando datos dentro de nuestra base de datos con FormView

Trabajaremos dentro de la app lector y dentro de ella en el modelo Prestamo construyendo una vista FormView pues nos permite hacer procesos extra antes de guardas. Aprenderemos a guardar usando Create y Save, viendo sus diferencias y usos apropiados.

- 1 Creamos una vista en la app **lector**:
  
```python
from django.shortcuts import render # type: ignore
from django.views.generic.edit import FormView # type: ignore
from .models import Prestamo
from .forms import PrestamoForm

# Create your views here.

class RegistrarPrestamo(FormView):
   template_name = 'lector/add_prestamo.html'
   form_class = PrestamoForm
   success_url ='.'

   def form_valid(self, form):
      return super(RegistrarPrestamo, self).form_valid(form)
```

- 2 Creamos un formulario:
  
```python
from django import forms # type: ignore
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
   """Form definition for Prestamo."""

   class Meta:
      """Meta definition for Prestamoform."""

      model = Prestamo
      fields = ('lector','libro')
```

- 3 Creamos el template html:

Creamos una nueva carpeta dentro de la carpeta templates llamada lector con **add_prestamo.html**:


  
- 4 Activamos la vista:

Creamos dentro de la app lector el **archivo urls.py**:

from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from . import views

urlpatterns = [
   path('prestamo/add/', 
      views.RegistrarPrestamo.as_view(),
      name ='prestamo-add'),
]



  

- 5 Añadimos la url recien creada a nuestro sistema de urls principal:

Para ello vamos al archivo urls.py de la app biblioteca:

from django.contrib import admin # type: ignore
from django.urls import path, re_path, include # type: ignore

urlpatterns = [
   path('admin/', admin.site.urls),
   re_path('', include('applications.autor.urls')),
   re_path('', include('applications.libro.urls')),
   re_path('', include('applications.lector.urls'))
]


  
# 6 Registrando datos dentro de nuestra base de datos con Create y Save






***
***
<br>
<br>
<br>

























































