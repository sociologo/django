

# Modelos avanzados II

<img src="https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7" alt="image" width="60%">

## 1 Consulta en un FK

## 2 Consulta en un FK con Related Name

## 3 Agregar Elementos en una Relación Muchos a Muchos

## 4 ManyToMany agregando elementos

## 5 Annotate en Consultas con la ORM Django

## 6 Diferencia entre Annotate y Aggregate - ORM Django

## 7 En que caso utilizar un Aggregate - ORM Django


## 1 Filtros utilizando dos y tres tablas (127-128)

### 1.1 Queremos filtrar todos los libros pertenecientes a una categoria

- Creamos el manager **listar_libros_categoria** en **managers.py** de la aplicación **libro**

```
def listar_libros_categoria(self, categoria):
  return self.filter(
    categoria__id = categoria
  ).order_by('titulo')
```

- Creamos la vista asociada con un parametro ingresado en duro (2):

```
class ListLibros2(ListView):
  context_object_name = 'lista_libros'
  template_name = 'libro/lista2.html'

  def get_queryset(self):
    return Libro.objects.listar_libros_categoria('2')
```

- Agreguemos el atributo id en los modelos de libro para que en el administrador de django sepamos cual elegir:

```
class Categoria(modelos.Model):
nombre = models.CharField(max_length = 30)

  def __str__(self):
    return str(self.id) + ' - ' + self.nombre
```

- Creamos la url que active la vista:

```
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
]
```

- Creamos el template **lista2.html**:

```
<h1>
   Lista de libros
</h1>

<ul>   
   {% for l in lista_libros %}
      <li>{{l.titulo}} {{l.fecha_lanzamiento}}</li>        
   {% endfor %}
</ul>
```

listo.

### 1.2 Queremos filtrar todos las categorias pertenecientes a un autor

Para hacer esto nos valdremos de un atributo importante dentro de los modelos de django llamado **related_name**.

El atributo **related_name** en el campo ForeignKey de Django se utiliza para definir el nombre del atributo inverso en el modelo relacionado. En el ejemplo, el modelo **Libro** tiene una clave foránea (ForeignKey) que apunta al modelo Categoria. 

Aquí, `related_name='categoria_libro'` define **cómo se accederá a los objetos Libro desde un objeto Categoria**. Es un **acceso inverso**.

Sin related_name: Si no especificas related_name, Django generará automáticamente un nombre para el acceso inverso, generalmente en el formato `<model_name>_set`. Por ejemplo, categoria.libro_set.all() para obtener todos los libros de una categoría.

Con related_name: Al especificar `related_name='categoria_libro'`, puedes acceder a los libros de una categoría usando categoria.categoria_libro.all().

```
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

- Creamos el manager CategoriaManager:

```
class CategoriaManager (models.Manager):
  def categoria_por_autor(self, autor):
    return self.filter(
      categoria_libro__autores__id = autor
      ).distinc()
```

distinc() para que no repita categorias para un mismo autor.

-conectamos CategoriaManager con el modelo de libro con:

```
from .managers import LibroManager, CategoriaManager

class Categoria(models.Model):
  nombre = models.CharField(max_length=100)
  objects = CategoriaManager()
  def __str__(self):
    return self.nombre

```

- Hacemos las migraciones
- 
## digresion: la shell de Django

Podemos hacer pruebas sobre los managers que creamos sin necesidad de correr nuevamente el proyecto utilizando solamente la shell de django a la cual accedemos con:

```
python manage.py shell
from applications.libro.models import *
Categoria.objects.categoria_por_autor('1')
```

## 2 Trabajar con dos tablas relacionadas muchos a muchos. (129-130)

Nuestro requerimiento sera agregar o eliminar un autor registrado a un libro ya existente:

- Vamos a los modelos de **libro** y **autor** para que en el administrador se despliegue su id para saber a que libro modificaremos sus autores.

```
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

- Creamos una vista **LibroDetailView** en la app libro, pues queremos ver los detalles de un libro, especificamente sus autores.

```
from django.views.generic import LisView, DetailView

class LibroDetailView(DetailView):
  model = Libro
  template_name = 'libro/detalle.html'
```

- Creamos una url para desplegar la vista
  
```
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


- Construimos la vista detalle.html
  
```
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

Construimos un manager **add_autor_libro** para agregra un autor en la app **libro**:

```
def add_autor_libro(self, libro_id, autor):
  libro = self.get(id = libro_id)
  libro.autores.add(autor)
  return libro
```

vamos a la shell django:

```
from applications.libro.models import *
Libro.objects.add_autor_libro('16', '17')
```

Para eliminar autores bastaria simplemente con reemplazar **add(autor)** por **remove(autor)**

agregar autores con POST










  











  
