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

4.1 Comencemos trabajando sobre la aplicacion autor.

- Creamos el archivo urls.py y dentro de él una url que apunte a la vista **ListAutores**:
  
![image](https://github.com/user-attachments/assets/45eed91b-2443-4863-bf9a-7d8945e9005e)

- En views creamos la vista ListAutores

- Dentro de la carpeta **templates** creamos un base.html y una carpeta autor dentro de la que construiremos lista.html

- Incluimos las urls dentro de las urls principales

- Creamos un archivo **managers.py**

- Editamos el archivo admin.py para poder ingresar datos desde el administrador de django

- Veamos el resultado

4.2 Filtros por nombre de autor







