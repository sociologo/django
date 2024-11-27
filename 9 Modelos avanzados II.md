# Modelos avanzados II

## 1 Filtros utilizando dos y tres tablas (127-128)

### 1.1 Queremos filtrar todos los libros pertenecientes a una categoría.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="120%">
</p>

- 1 Creamos el manager **listar_libros_categoria()** en **managers.py** de la aplicación **libro**:

```python
def listar_libros_categoria(self, categoria):
  return self.filter(
    categoria__id = categoria
  ).order_by('titulo')
```

- 2 Creamos la vista asociada con un parámetro ingresado en duro:

```python
class ListLibros2(ListView):
  context_object_name = 'lista_libros'
  template_name = 'libro/lista2.html'

  def get_queryset(self):
    return Libro.objects.listar_libros_categoria('2')
```

- 3 Agreguemos el atributo id en los modelos de libro para que en el administrador de django sepamos cuál elegir:

```python
class Categoria(modelos.Model):
nombre = models.CharField(max_length = 30)

  def __str__(self):
    return str(self.id) + ' - ' + self.nombre
```

- 4 Creamos la url que active la vista:

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

- 5 Creamos el template **lista2.html**:

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

### 1.2 Filtrar todos las categorías pertenecientes a un autor.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="120%">
</p>

Para hacer ésto utilizaremos un atributo importante dentro de los modelos de django llamado **related_name**.

El atributo **related_name** en el campo ForeignKey de Django se utiliza para definir el nombre del atributo inverso en el modelo relacionado. En el ejemplo, el modelo **Libro** tiene una clave foránea (ForeignKey) que apunta al modelo Categoría. Es necesario disponer de una forma para apuntar del modelo Categoría al de Libro.

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

```python
class CategoriaManager (models.Manager):
  def categoria_por_autor(self, autor):
    return self.filter(
      categoria_libro__autores__id = autor
      ).distinc()
```

distinc() para que no se repitan categorías para un mismo autor.

ES ABSTRACTO COMPRENDER BIEN LA SIGUIENTE LINEA:

```
categoria_libro__autores__id = autor
```

Dedícale un tiempo a asimilarla.

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
python manage.py makemigrations
python manage.py migrate
```
  
## digresión: la shell de Django

Podemos hacer pruebas sobre los managers que creamos sin necesidad de correr nuevamente el proyecto utilizando solamente la shell de django a la cual accedemos con:

```bash
python manage.py shell
from applications.libro.models import *
Categoria.objects.categoria_por_autor('1')
```

## 2 Trabajar con dos tablas relacionadas muchos a muchos. (129-130)

Nuestro requerimiento será agregar o eliminar un autor registrado a un libro ya existente.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="120%">
</p>

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
      return self.titulo + ' - ' + self.titulo
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

- 4 Construímos la vista **detalle.html**:
  
```html
<h1>
   Detalle de libros
</h1>

<p>
  {{libro.titulo}}
</p>
<p>
  {{libro.fecha}}
</p>
<p>
  {{libro.categoria}}
</p>

<ul>
  {% for autor in  libro.autores.all %}
    <li>{{autor}}</li>
  {% endfor %}
</ul>
```

- 5 Construímos un manager **add_autor_libro** para agregra un autor en la app **libro**:

```python
def add_autor_libro(self, libro_id, autor):
  libro = self.get(id = libro_id)
  libro.autores.add(autor)
  return libro
```

vamos a la shell django:

```bash
from applications.libro.models import *
Libro.objects.add_autor_libro('16', '17')
```

donde el primer parámetro es el libro y el segundo el autor.

Para eliminar autores bastaria simplemente con reemplazar **add(autor)** por **remove(autor)**

## 3 Filtros con operaciones aritmeticas.

### 3.1 listar todas las categorias con el numero de libros que cada una posee.

Para estos requerimientos en django se utiliza la funcion **annotate()**.

- Declaramos un nuevo manager dentro de **managers.py** de la app **libro** llamado **listar_categoria_libros()**.
- No olvidemos importar la funcion **Count**

```python
from django.db.models import Q, Count

def listar_categoria_libros(self):
  resultado = self.annotate(
    num_libros = Count('categoria_libro')
    )
    return resultado
```

- Solo para hacer pruebas en la shell modificamos el manager como sigue:

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

- y probamos:

```bash
from applications.libro.models import *
Categoria.objects.listar_categoria_libros()
```

### 3.2 Veces que ha sido prestado un libro utilizando **aggregate()**

- Declaramos un nuevo manager dentro de **managers.py** de la app **libro** llamado **libros_num_prestamos()**.

```python
def libros_num_prestamos(self):
  resultado = self.aggregate(
    num_lprestamos = Count('libro_prestamo')
    )
    return resultado
```

- No tenemos un related_name.

- como modificamos los modelos debemos hacer migraciones.

Las funciones aggregate() y annotate() en Django se utilizan para realizar operaciones de agregación en consultas de bases de datos, pero tienen propósitos y usos diferentes.

aggregate()

- Propósito: La función aggregate() se utiliza para calcular valores agregados (como sumas, promedios, conteos, etc.) a partir de un conjunto de registros y devolver un solo valor o un diccionario de valores.
- Resultado: Devuelve un diccionario con los resultados de las agregaciones.
- Uso: Se utiliza cuando necesitas un resumen global de los datos, sin necesidad de mantener los datos originales.

annotate()

- Propósito: La función annotate() se utiliza para calcular valores agregados para cada objeto en un queryset y agregar estos valores como campos adicionales a cada objeto.
- Resultado: Devuelve un queryset con los objetos originales, cada uno anotado con los valores agregados.
- Uso: Se utiliza cuando necesitas mantener los datos originales y agregar información adicional calculada a cada objeto.

Cuándo Usar Cada Una

- Usar aggregate(): Cuando necesitas un valor agregado global, como el total de ventas, el promedio de calificaciones, etc., y no necesitas los datos originales.
- Usar annotate(): Cuando necesitas agregar información calculada a cada objeto en un queryset, como el número de comentarios por artículo, el total de ventas por producto, etc., y necesitas mantener los datos originales.

### 3.3 Calcular el promedio de edad de los lectores que piden prestado determinado libro.

- Conviene hacer el manager dentro del modelo prestamo en la app lector, por lo que creamos una clase llamada **PrestamoManager(models.Manager)** en el archivo** managers.py** de la app **lector** y dentro de ella el manager **libros_promedio_edades(self)** e ingresamos un valor en duro para un libro. No olvidemos importar la funcion **Avg**:

```python
class PrestamoManager(models.Manager):
  def libros_promedio_edades(self):
    resultado = self.filter(
      libro_id = '15'
    ).aggregate(
      promedio_edad = Avg('lector__edad')
    )
    return resultado
```

- En los modelos vinculamos el manager:

- Verificamos en la shell:

```bash
from applications.lector.models import *
Prestamo.objects.libros_promedio_edades()
```

Como aggregate es un diccionario, podemos agregarle mas elementos como por ejemplo la suma total de edades:

```python
class PrestamoManager(models.Manager):
  def libros_promedio_edades(self):
    resultado = self.filter(
      libro_id = '15'
    ).aggregate(
      promedio_edad = Avg('lector__edad'),
      suma_edad - Sum('lector__edad')
    )
    return resultado
```

- Verificamos en la shell:

```bash
from applications.lector.models import *
Prestamo.objects.libros_promedio_edades()
```

  











  
