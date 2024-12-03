# Modelos avanzados II

```bash
cd /
C:\> cd /mis_entornos/entorno_2/Scripts
C:\mis_entornos\entorno_2\Scripts> activate
(entorno_2) C:\mis_entornos\entorno_1\Scripts> cd \mis_proyectos\biblio\biblioteca
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py runserver 
```

## Índice

* [1 Filtros utilizando dos y tres tablas.](#1-Filtros-utilizando-dos-y-tres-tablas)
  * [1.1 Filtro de todos los libros pertenecientes a una categoría.](#11-Filtro-de-todos-los-libros-pertenecientes-a-una-categoría)
  * [1.2 Filtrar todos las categorías pertenecientes a un autor.](#12-Filtrar-todos-las-categorías-pertenecientes-a-un-autor)
* [Digresión: la shell de Django](#Digresión-la-shell-de-Django)
* [2 Trabajar con dos tablas relacionadas muchos a muchos.](#2-Trabajar-con-dos-tablas-relacionadas-muchos-a-muchos)
* [3 Filtros con operaciones aritméticas.](#3-Filtros-con-operaciones-aritméticas)
  * [3.1 Listar todas las categorías con el número de libros que cada una posee.](#31-Listar-todas-las-categorías-con-el-número-de-libros-que-cada-una-posee)
  * [3.2 Veces que ha sido prestado un libro utilizando aggregate().](#32-Veces-que-han-sido-prestados-los-libros-utilizando-aggregate)
  * [3.3 Consideraciones sobre annotate() y aggregate().](#33-Consideraciones-sobre-annotate-y-aggregate)
* [4 Calcular el promedio de edad de los lectores que piden prestado determinado libro.](#4-Calcular-el-promedio-de-edad-de-los-lectores-que-piden-prestado-determinado-libro)

# 1 Filtros utilizando dos y tres tablas.

## 11 Filtro de todos los libros pertenecientes a una categoría.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="120%">
</p>

- 1 La clave foránea

Este ejercicio es simple pues tenemos la clave foránea ya en la definición del modelo de la aplicación libro. Lo que tenemos que hacer es llamarla y hacer el match con un parámetro ingresado a un manager.

 ```python
from django.db import models # type: ignore
from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager

class Categoria(models.Model):
   nombre = models.CharField(max_length=100)
   objects = CategoriaManager()
   def __str__(self):
      return str(self.id) + ' - ' + self.nombre

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

   def __str__(self):
      return str(self.id) + ' - ' + self.titulo
 ```

- 2 Creamos el manager **listar_libros_categoria()** en **managers.py** de la aplicación **libro**:

```python
def listar_libros_categoria(self, categoria):
  return self.filter(
    categoria__id = categoria
  ).order_by('titulo')
```

- 3 Creamos la vista asociada con un parámetro ingresado en duro:

La razón por la que debes hacer referencia a objects para llamar al manager en la línea return `Libro.objects.listar_libros_categoria('2')` es porque objects es el nombre predeterminado del manager de Django. Cuando defines un modelo en Django, automáticamente se le asigna un manager llamado `objects`, que es una instancia de `models.Manager`.

El manager es responsable de realizar consultas a la base de datos y proporciona métodos para interactuar con los datos del modelo. Al definir métodos personalizados en el manager, como listar_libros_categoria, estos métodos se agregan a la instancia del manager (objects), y es por eso que debes usar Libro.objects para acceder a ellos.

```python
class ListLibros2(ListView):
  context_object_name = 'lista_libros'
  template_name = 'libro/lista2.html'

  def get_queryset(self):
    return Libro.objects.listar_libros_categoria('2')
```

- 4 Agreguemos el atributo id en el modelo de categoria para que en el administrador de django sepamos cuál elegir:

```python
class Categoria(modelos.Model):
nombre = models.CharField(max_length = 30)

  def __str__(self):
    return str(self.id) + ' - ' + self.nombre
```

![image](https://github.com/user-attachments/assets/68ed9e38-6036-4c6a-9c6e-bb918f8130ae)

- 5 Creamos la url que active la vista:

```python
urlpatterns = [
  path(
    'libros/', 
    views.ListLibros.as_view(),
    name ='libros'
  ),
  path(
    'libros-2/', 
    views.ListLibros2.as_view(),
    name = 'libros2'
  ),
]
```

- 6 Creamos el template **lista2.html**:

```html
<h1>
   Lista de libros
</h1>

<ul>   
   {% for l in lista_libros %}
      <li>{{l.titulo}} {{l.fecha_lanzamiento}}</li>        
   {% endfor %}
</ul>
```

- 7 listamos todos los libros que pertenezcan a la categoria 'Comedia'.

![image](https://github.com/user-attachments/assets/10512c54-bfb5-43d1-90ac-a4ba34327943)

## 12 Filtrar todos las categorías pertenecientes a un autor.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="120%">
</p>

Para hacer ésto utilizaremos un atributo importante dentro de los modelos de django llamado **related_name**.

El atributo **related_name** en el campo ForeignKey de Django se utiliza para definir el nombre del atributo inverso en el modelo relacionado. En el ejemplo, el modelo **Libro** tiene una clave foránea que apunta al modelo Categoría. Es necesario disponer de una forma para apuntar del modelo Categoría al de Libro.

- 1 Establecemos el atributo: `related_name = 'categoria_libro'` en el modelo **Libro**, el que define **cómo se accederá a los objetos Libro desde un objeto Categoría**. Es un **acceso inverso**.

```python
from django.db import models # type: ignore
from applications.autor.models import Autor
from .managers import LibroManager

class Categoria(models.Model):
   nombre = models.CharField(max_length=100)

   def __str__(self):
      return self.nombre

   class Libro(models.Model):
   categoria = models.ForeignKey(
      Categoria,
      on_delete=models.CASCADE,
      related_name = 'categoria_libro'
   )
   autores =  models.ManyToManyField(Autor)
   titulo = models.CharField(max_length=200)
   fecha_lanzamiento = models.DateField('Fecha de lanzamiento')
   portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
   visitas = models.PositiveIntegerField(default=0)

   objects = LibroManager()

   def __str__(self):
      return self.titulo
```

- 2 Creamos el manager **CategoriaManager()** en la app **libro**:

En la app **libro** definimos la clase llamada **CategoriaManager()** que hereda de `models.Manager` y extiende la funcionalidad del manager predeterminado de Django (models.Manager). Dentro de esta clase definimos el método categoria_por_autor 

```python
class CategoriaManager (models.Manager):
   def categoria_por_autor(self, autor):
      return self.filter(
         categoria_libro__autores__id = autor
         ).distinct()
```

distinc() para que no se repitan categorías para un mismo autor.

>ES ABSTRACTO COMPRENDER BIEN LA SIGUIENTE LINEA:
```
categoria_libro__autores__id = autor
```
> Dedícale un tiempo a asimilarla.

Observemos que seguimos la misma lógica de construcción de apps en Django; los managers se agrupan de la misma forma en la que hemos agrupado las tablas:

![image](https://github.com/user-attachments/assets/95fd6427-d0df-4c26-856b-fe0d778ad4ce)
![image](https://github.com/user-attachments/assets/7e1ec794-8daa-4301-9c31-4b547a53fcd6)

- 3 Conectamos **CategoriaManager()** con el modelo de **libro**:

```python
from .managers import LibroManager, CategoriaManager

class Categoria(models.Model):
  nombre = models.CharField(max_length=100)
  objects = CategoriaManager()
  def __str__(self):
    return str(self.id) + ' - ' + self.nombre
```

- 4 Hacemos las migraciones:

```bash
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio\biblioteca> python manage.py migrate
```
  
# Digresión la shell de Django

Podemos hacer pruebas sobre los managers que creamos sin necesidad de correr nuevamente el proyecto utilizando solamente la shell de django a la cual accedemos con:

```bash
python manage.py shell
from applications.libro.models import *
Categoria.objects.categoria_por_autor('1')
exit()
```

![image](https://github.com/user-attachments/assets/e93179d3-9ce5-439f-a7da-3551a0e06f44)
![image](https://github.com/user-attachments/assets/37732dd2-b08c-479d-89e0-76df79c8aa4b)

# 2 Trabajar con dos tablas relacionadas muchos a muchos.

Nuestro requerimiento será agregar o eliminar un autor registrado a un libro ya existente.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="120%">
</p>

En teoría de bases de datos, cuando tienes dos tablas relacionadas de una forma muchos a muchos, debes crear una tabla intermedia (también conocida como tabla de unión o tabla de asociación) para gestionar esta relación. Esta tabla intermedia contiene las claves foráneas de ambas tablas principales, estableciendo así la relación entre ellas. **En Django, cuando tienes una relación muchos a muchos entre dos modelos, se utiliza un campo ManyToManyField para gestionar esta relación.** Django automáticamente crea una tabla intermedia para manejar la relación muchos a muchos.

- 1 Vamos a los modelos de **libro** y **autor** para que en el administrador se desplieguen sus id. Asi podremos obtener los parámetros para hacer las pruebas: 
  
```python
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
   portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
   visitas = models.PositiveIntegerField(default=0)

   objects = LibroManager()

   def __str__(self):
      return str(self.id) + ' - ' + self.titulo
```

```python
from django.db import models # type: ignore

from .managers import AutorManager

class Autor(models.Model):
   nombre = models.CharField(max_length=100)
   apellido = models.CharField(max_length=100)
   nacionalidad = models.CharField(max_length=100)
   edad = models.PositiveIntegerField()

   objects = AutorManager()

   def __str__(self):
      return f"{str(self.id)} {self.nombre} {self.apellido}"
```

- 2 Creamos una vista **LibroDetailView()** en la app **libro**, pues queremos ver los autores de un libro específico:

```python
from django.views.generic import LisView, DetailView

class LibroDetailView(DetailView):
  model = Libro
  template_name = 'libro/detalle.html'
```

- 3 Creamos la url **libros-detalle/`<pk>`** para desplegar la vista:
  
```python
urlpatterns = [
  path(
    'libros/', 
    views.ListLibros.as_view(),
    name ='libros'
  ),
  path(
    'libros-2/', 
    views.ListLibros2.as_view(),
    name ='libros2'
  ),
  path(
    'libros-detalle/<pk>', 
    views.LibroDetailView.as_view(),
    name ='libros-detalle'
  ),
]
```

- 4 Construímos la vista **detalle.html** dentro de la carpeta libro de los templates:
  
>Django pasa el objeto en minúsculas por convención.

```html
<h1>Detalle de libros</h1>

<p>{{libro.titulo}}</p>
<p>{{libro.fecha}}</p>
<p>{{libro.categoria}}</p>

<ul>
  {% for autor in libro.autores.all %}
    <li>{{autor}}</li>
  {% endfor %}
</ul>
```

![image](https://github.com/user-attachments/assets/61cdb30e-8528-46a8-972a-36ea1e45c3aa)
![image](https://github.com/user-attachments/assets/79f0d7e8-2c7e-4484-b10a-8b3d7c6905ad)

- 5 Construímos un manager **add_autor_libro** dentro del manager **LibroManager()** de la app **libro** para agregar un autor:

```python
def add_autor_libro(self, libro_id, autor):
  libro = self.get(id = libro_id)
  libro.autores.add(autor)
  return libro
```

![image](https://github.com/user-attachments/assets/349550e7-9219-4ecd-9f35-c94945bf1127)

vamos a la shell django:

![image](https://github.com/user-attachments/assets/2be6801a-68a0-4b7c-8556-525e705df224)

donde el primer parámetro es el libro y el segundo el autor.

![image](https://github.com/user-attachments/assets/4f07ebdc-dd7c-4f2d-ab75-6e9e3935ec4e)

Para eliminar autores bastaría simplemente con reemplazar **add(autor)** por **remove(autor)**.

# 3 Filtros con operaciones aritméticas.

## 31 Listar todas las categorías con el número de libros que cada una posee.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="120%">
</p>

- 1 La función **annotate()**.

Declaramos el método **listar_categoria_libros()** dentro del manager **CategoriaManager()** de la app **libro**. Utilizaremos la función **Count** sobre la clave inversa **categoria_libro**. No olvidemos importar la funcion **Count**.

Lo que hace el siguiente método es contar las veces en que cada categoria aparece en la tabla libros:

```python
from django.db.models import Q, Count

def listar_categoria_libros(self):
   resultado = self.annotate(
      num_libros = Count('categoria_libro')
   )
   return resultado
```

- 2 Sólo para hacer pruebas en la shell modificamos el manager como sigue:

```python
def listar_categoria_libros(self):
   resultado = self.annotate(
      num_libros = Count('categoria_libro')
   )
   for r in resultado:
      print('***')
      print(r, r.num_libros)
   return resultado
```

- 3 Probamos:

```bash
python manage.py shell
from applications.libro.models import *
Categoria.objects.listar_categoria_libros()
```

![image](https://github.com/user-attachments/assets/c4a6ae84-857b-48e9-803a-8cd4a81748b5)

## 32 Veces que han sido prestados los libros utilizando aggregate.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d107fc2b-84df-4e0d-bc50-abceb9afecc9" alt="image" width="50%">
</p>


- 1 Declaramos un nuevo método dentro de los managers de la app **libro** llamado **libros_num_prestamos()**.

```python
def libros_num_prestamos(self):
   resultado = self.aggregate(
      num_prestamos = Count('libro_prestamo')
   )
   return resultado
```

- 2 Debemos construir un **related_name**.

Vemos que tenemos una situación en la que necesitamos obtener una clave inversa. Necesitamos una relación en la que obtengamos una pseudo Foreign Key en nuestra tabla **Libro** desde la tabla **Prestamo**. Para ello, en nuestra app **Lector** agregamos un **related_name** al modelo **Prestamo** tal como se indica:

```python
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

   def __str__(self):
      return f"Prestamo de {self.libro.titulo} a {self.lector.nombre} {self.lector.apellido}"
 ``` 

- 3 Como modificamos los modelos debemos hacer migraciones.

```bash
python manage.py makemigrations
python manage.py migrate
```

- 4 Ejecutemos en el shell:

```bash
python manage.py shell
from applications.libro.models import *
Libro.objects.libros_num_prestamos()
```
![image](https://github.com/user-attachments/assets/1ff40d28-b3ff-45d8-a161-a70a221e7b09)
![image](https://github.com/user-attachments/assets/134e5147-00d1-4db3-9690-b1121f8f344f)

## 33 Consideraciones sobre annotate y aggregate.

Las funciones **annotate()** y **aggregate()** en Django se utilizan para realizar operaciones de agregación en consultas de bases de datos, pero tienen propósitos y usos diferentes.

**annotate()** añade información a cada objeto en el QuerySet, mientras que **aggregate()** realiza cálculos en todo el conjunto de resultados y devuelve un diccionario con los resultados de esos cálculos. Es por eso que en django **annotate()** devuelve un QuerySet y **aggregate()** devuelve diccionario de python.

## annotate()

- 1 Propósito: La función annotate() se utiliza para calcular valores agregados para cada objeto en un queryset y agregar estos valores como campos adicionales a cada objeto.
- 2 Resultado: Devuelve un queryset con los objetos originales, cada uno anotado con los valores agregados.
- 3 Uso: Se utiliza cuando necesitas mantener los datos originales y agregar información adicional calculada a cada objeto.

## aggregate()

- 1 Propósito: La función aggregate() se utiliza para calcular valores agregados (como sumas, promedios, conteos, etc.) a partir de un conjunto de registros y devolver un solo valor o un diccionario de valores.
- 2 Resultado: Devuelve un diccionario con los resultados de las agregaciones.
- 3 Uso: Se utiliza cuando necesitas un resumen global de los datos, sin necesidad de mantener los datos originales.

Cuándo Usar Cada Una:

- Usar annotate(): Cuando necesitas agregar información calculada a cada objeto en un queryset, como el número de comentarios por artículo, el total de ventas por producto, etc., y necesitas mantener los datos originales.
- Usar aggregate(): Cuando necesitas un valor agregado global, como el total de ventas, el promedio de calificaciones, etc., y no necesitas los datos originales.

# 4 Calcular el promedio de edad de los lectores que piden prestado determinado libro.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="120%">
</p>

- 1 Construímos el método **libros_promedio_edades(self)**.

Conviene hacer el método **libros_promedio_edades()** dentro de la app **lector**, dentro del manager del modelo **PrestamoManager()**, pues asi estamos considerando de una vez los prestamos ya existentes. 

Ingresemos un valor en duro para un libro. 

No olvidemos importar la funcion **Avg**:

```python
import datetime
from django.db import models
from django.db.models import Q, Count, Avg

class PrestamoManager(models.Manager):
  def libros_promedio_edades(self):
    resultado = self.filter(
      libro_id = '15'
    ).aggregate(
      promedio_edad = Avg('lector__edad')
    )
    return resultado
```

- 2 En los modelos vinculamos el manager:

```python
from django.db import models # type: ignore
from applications.libro.models import Libro

from .managers import PrestamoManager # type: ignore

class Lector(models.Model):
   nombre = models.CharField(max_length=100)
   apellido = models.CharField(max_length=100)
   nacionalidad = models.CharField(max_length=100)
   edad = models.PositiveIntegerField(default=0)

   def __str__(self):
      return f"{self.nombre} {self.apellido}"

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

- 3 Verificamos en la shell:

```bash
from applications.lector.models import *
Prestamo.objects.libros_promedio_edades()
```
![image](https://github.com/user-attachments/assets/c963f1c7-08ac-4603-8fe7-77d2bb2ba8b4)
![image](https://github.com/user-attachments/assets/d695881d-a9d6-4993-aed4-521e2779cefe)

- 4 Como **aggregate()** es un diccionario, podemos agregarle más elementos, como por ejemplo la suma total de edades importando la función **Sum**:

```python
from django.db import models
from django.db.models import Q, Count, Avg, Sum

class PrestamoManager(models.Manager):
  def libros_promedio_edades(self):
    resultado = self.filter(
      libro_id = '15'
    ).aggregate(
      promedio_edad = Avg('lector__edad'),
      suma_edad = Sum('lector__edad')
    )
    return resultado
```

- 5 Verificamos en la shell:

```bash
from applications.lector.models import *
Prestamo.objects.libros_promedio_edades()
```

  











  
