# Django

## Índice

* [1 Crear un proyecto Django](#1-crear-un-proyecto-django)
* [2 Configurar la estructura de un proyecto en django](#2-Configurar-la-estructura-de-un-proyecto-en-django)
* [3 Ejecutando el archivo local.py en vez del original settings.py](#3-Ejecutando-el-archivo-localpy-en-vez-del-original-settingspy)
* [4 Aplicaciones](#4-Aplicaciones)
* [5 Vistas genéricas: Views](#5-Vistas-genéricas-Views)
* [Inicio de Pruebas en la aplicación exp](#Inicio-de-Pruebas-en-la-aplicacion-exp)
* [6 Construcción y despliegue de la primera App](#6-Construcción-y-despliegue-de-la-primera-App)
* [7 Una arquitectura de templates](#7-Una-arquitectura-de-templates)
* [8 Una arquitectura de urls](#8-Una-arquitectura-de-urls)
* [9 Primeros pasos en MVT](#9-Primeros-pasos-en-MVT)
* [10 La ORM de Django y los modelos](#10-La-ORM-de-Django-y-los-modelos)
* [11 Implementando la base de datos Empleado](#11-Implementando-la-base-de-datos-Empleado)
* [Fin de Pruebas en la aplicacion exp](#6-Inicio-de-Pruebas-en-la-aplicacion-exp)
* [12 Claves foráneas](#12-Claves-foráneas)
* [13 PostgreSQL y Django](#13-PostgreSQL-y-Django)
* [14 El Administrador de Django y la clase Meta](#14-El-Administrador-de-Django-y-la-clase-Meta)
* [15 Creando modelos dentro de una aplicación ya existente](#15-Creando-modelos-dentro-de-una-aplicación-ya-existente)
* [16 Personalizando al Administrador de Django (admin.py)](#16-Personalizando-al-Administrador-de-Django-(admin.py))
* [17 La app CKEditor](#17-La-app-CKEditor)


## 1 Crear un proyecto Django

(para limpiar la consola utilizamos el comando **cls**)

(para salir de la consola utilizamos el comando **CTRL+C**)

Para instalar Djaneiro en Visual Studio Code, sigue estos pasos:

Abre Visual Studio Code.

Accede a la barra de extensiones: Puedes hacerlo haciendo clic en el ícono de extensiones en la barra lateral izquierda o presionando Ctrl+Shift+X.

Busca “Djaneiro”: En la barra de búsqueda de extensiones, escribe “Djaneiro”.

Instala la extensión: Cuando encuentres “Djaneiro - Django Snippets”, haz clic en el botón de instalar.

Reinicia Visual Studio Code: Para asegurarte de que la extensión se ha instalado correctamente, reinicia Visual Studio Code.

Para crear una estructura básica de HTML utilizando Djaneiro en Visual Studio Code, sigue estos pasos:

Abre un archivo HTML: Crea un nuevo archivo con la extensión .html o abre uno existente.

Escribe el snippet: Djaneiro proporciona varios snippets útiles. Para una estructura básica de HTML, puedes usar el snippet html5. Simplemente escribe html5 y presiona Tab.

1 Creamos carpetas de trabajo

Construiremos dos carpetas en C. Una para nuestros proyectos **mis_proyectos** y otra para nuestros entornos virtuales **mis_entornos**


2 Creamos nuestro primer entorno y lo activamos

```bash
C:\>cd mis_entornos
C:\mis_entornos>python -m venv entorno_1
C:\mis_entornos>cd entorno_3/Scripts
C:\mis_entornos\entorno_3\Scripts>activate
(entorno_3) C:\mis_entornos\entorno_3\Scripts>
(entorno_3) C:\mis_entornos\entorno_3\Scripts>cd /
(entorno_3) C:\>
```

3 Instalamos y actualizamos paquetes

```bash
(entorno_3) C:\> pip install django
(entorno_3) C:\> python.exe -m pip install --upgrade pip
(entorno_3) C:\> cd \mis_proyectos\emp3
(entorno_3) C:\mis_proyectos\emp3> pip install django-ckeditor
(entorno_3) C:\mis_proyectos\emp3> pip install psycopg2-binary
(entorno_3) C:\mis_proyectos\emp3> pip install Pillow
```

script de arranque:

```bash
C:\Users\chris> cd /
C:\> cd mis_entornos/entorno_3/Scripts
C:\mis_entornos\entorno_3\Scripts> activate
(entorno_3) C:\mis_entornos\entorno_3\Scripts> cd \mis_proyectos\emp3\empleado
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

4 En ella, creamos nuestro proyecto empleado

```bash
(entorno_3) C:\mis_proyectos\emp3> django-admin startproject empleado
```

5 Corremos el servidor

```bash
(entorno_3) C:\mis_proyectos\emp3> cd empleado
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

6 Abrimos el proyecto empleado con Visual Studio

![image](https://github.com/user-attachments/assets/8dbfe7f4-3409-486d-aad0-9e44669ae4f0)

## 2 Configurar la estructura de un proyecto en django

En cualquier desarrollo necesitamos al menos tres entornos (para trabajo local, de pruebas y de producción) y un cuarto **base**. En el entorno **base** alojaremos la configuración básica de todos.

1 Dentro de la carpeta **empleado**, creamos otra carpeta llamada **settings** con cuatro archivos .py en su interior:

![image](https://github.com/user-attachments/assets/3ca4a2a9-bc58-4365-9a2b-15939a7ccf1e)

2 Del archivo original settings.py debemos copiar a los archivos recién creados, lo siguiente:

- en **base.py**:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9xh%=ob5sj*g*r5&ii^r$mu9bs0w*t09ni*vko67=*z402som8'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'empleado.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'empleado.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

```

- en **local.py**:

```python
from empleado.settings.base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
```

## 3 Ejecutando el archivo local.py en vez del original settings.py

1 Borramos el archivo settings.py original.

2 Le indicamos a django que ejecute desde el entorno de configuración local.py:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver --settings=empleado.settings.local
```

3 Redireccionamos para aumentar la simplicidad al ejecutar el proyecto:

Agregamos .local a la siguiente línea del archivo manage.py:

```bash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empleado.settings')
```

```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empleado.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

4 Ahora podemos ejecutar simplemente escribiendo:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

## 4 Aplicaciones

Las aplicaciones en django son pequeños proyectos completos. La idea es que:

- cada una sea independiente de las otras con el objetivo de poder reutilizarlas si fuese necesario y

- cada una se dedique a un solo proceso de la lógica del negocio.

Crearemos dos aplicaciones dentro de una nueva carpeta llamada **applications** dentro de la carpeta **empleado** junto con un archivo __init__.py. Serán las aplicaciones **departamentos** y **empleados**:

![image](https://github.com/user-attachments/assets/8a4cacb5-da70-4e4d-8e39-453c3285dcfe)

![image](https://github.com/user-attachments/assets/f73a5271-00ec-4b33-bcbb-1fe024e9b954)

1 Vamos al nivel de applications y creamos los dos nuevos proyectos:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>cd applications
(entorno_3) C:\mis_proyectos\emp3\empleado\applications> django-admin startapp departamentos
(entorno_3) C:\mis_proyectos\emp3\empleado\applications> django-admin startapp empleados
```

![image](https://github.com/user-attachments/assets/1aa17e99-bb1c-4d5f-86d6-02832aaf329f)

2 Ahora necesitamos instalar nuestras aplicaciones en el archivo base.py:

![image](https://github.com/user-attachments/assets/08fe8f7d-9fd1-467e-ae0a-c5ef06cd6ab9)

y en cada uno de los archivos apps.py de las aplicaciones departamentos y empleados anteponemos el prefijo applications:

![image](https://github.com/user-attachments/assets/3061723c-e662-46dd-918c-f7523e100b05)
![image](https://github.com/user-attachments/assets/5709f22a-3467-4e0e-a8f6-c083455dc413)

3 Levantemos nuestro servidor para que veamos que todo esté funcionando ok:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

## 5 Vistas genéricas: Views

1 La teoría del patrón de diseño MVT

El patrón Modelo-Vista-Template (MVT) de Django es una variación del clásico Modelo-Vista-Controlador (MVC). A continuación, veamos en qué consiste el MVT y sus diferencias clave con MVC:

2 Modelo-Vista-Template (MVT) en Django

Modelo (**Model**):

Se encarga de la lógica de acceso a los datos y define la estructura de la base de datos. En Django, los modelos son clases de Python que se traducen en tablas de la base de datos.

Ejemplo: Definir un modelo Usuario con campos como nombre, email, y fecha_de_nacimiento.

Vista (**View**):

Contiene la lógica de negocio y controla qué datos se envían al usuario. Las vistas en Django son funciones o clases que reciben una solicitud HTTP, interactúan con el modelo si es necesario, y devuelven una respuesta HTTP.

Ejemplo: Una vista que recupera todos los usuarios de la base de datos y los envía a una plantilla para su visualización.

Plantilla (**Template**):

Es la capa de presentación que define cómo se muestran los datos al usuario. Las plantillas en Django son archivos HTML que pueden contener etiquetas de plantilla de Django para mostrar datos dinámicos.

Ejemplo: Un archivo HTML que muestra una lista de usuarios con sus nombres y correos electrónicos.

3 Diferencias con el Modelo Vista-Controlador (MVC)

Controlador (Controller) vs. Vista (View):

En el patrón MVC, el Controlador maneja la lógica de negocio y la interacción entre el modelo y la vista. En Django, esta función la realiza la Vista. En MVC, la Vista es responsable solo de la presentación de los datos. En MVT, la Plantilla cumple esta función.

Terminología:\
Aunque la funcionalidad es similar, la terminología difiere. En Django, lo que en MVC se llama Controlador se llama Vista, y lo que en MVC se llama Vista se llama Plantilla.

Flujo de Trabajo:

En MVC, el flujo típico es: Usuario → Controlador → Modelo → Vista → Usuario.

En MVT, el flujo es: Usuario → Vista → Modelo → Plantilla → Usuario.

4 Ejemplo Práctico

Supongamos que queremos mostrar una lista de productos en una tienda en línea:

Modelo (Model): Definimos un modelo Producto con campos como nombre, precio, y descripción.

Vista (View): Creamos una vista que recupera todos los productos de la base de datos y los pasa a una plantilla.

Plantilla (Template): Diseñamos un archivo HTML que muestra la lista de productos con sus nombres y precios.

En resumen, el patrón MVT de Django es una adaptación del patrón MVC, con una terminología y flujo de trabajo ligeramente diferentes, pero con el mismo objetivo de separar la lógica de negocio, la lógica de presentación y la interfaz de usuario.

# Inicio de Pruebas en la aplicacion exp

## 6 Construcción y despliegue de la primera App

#### 1 En la carpeta applications, construyamos una nueva aplicación llamada **exp**.

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado> cd applications
(entorno_3) C:\mis_proyectos\emp3\empleado\applications> django-admin startapp exp
```

#### 2 En **base.py** agregamos la ruta de la aplicación para instalarla.

```python
INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',

   # local apps
   "applications.departamentos",
   "applications.empleados",
   'applications.exp'
]
```

#### 3 Vamos a **apps.py** de la misma aplicación y agregamos la ruta de la carpeta:

```python
from django.apps import AppConfig

class ExpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.exp'
```

#### 4 Dentro de la carpeta **exp** agregamos una nueva llamada **templates**, donde alojaremos todos nuestros htmls.

![image](https://github.com/user-attachments/assets/4bea0efe-0d49-4a3d-a926-286f0aea091b)

#### 5 Creamos una vista

En views.py de exp agregamos las siguientes lineas de codigo:

```python
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'home.html'
```

#### 6 Creamos el template

En la carpeta templates creamos un archivo llamado **home.html** donde escribimos el siguiente código:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hola</h1>
    <h3>Probando el patrón de diseño</h3>
</body>
</html>
```

#### 7 Agregamos la ruta

en **urls.py** agregamos una nueva ruta:

```
from django.contrib import admin
from django.urls import path
from applications.exp.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view()),
]
```

#### 8 ejecutemos nuevamente nuestro proyecto y vamos a la url home:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py runserver
```

![image](https://github.com/user-attachments/assets/9348cdbd-651e-4c16-ae11-7c8e6cf7ba77)



## 7 Una arquitectura de templates

#### 1 Una carpeta templates general

Una buena práctica es contruir una carpeta templates donde tengamos sub carpetas asociadas a las apps y dentro de ellas los correspondientes htmls. Construímos la carpeta como se indica con la subcarpeta y dentro de ella copiamos **home.html** y borramos la carpeta templates de la app exp:

![image](https://github.com/user-attachments/assets/67f60d17-4cac-4d6d-9b59-c511e2452ef5)

#### 2 Hacemos las siguientes modificaciones en el archivo base.py:

![image](https://github.com/user-attachments/assets/8769b9a4-10c9-4e2f-8b2c-03a6a2ffd4dd)

#### 3 Hacemos las siguientes modificaciones en la vista de nuestra aplicación exp:

![image](https://github.com/user-attachments/assets/c805788e-a7d6-4818-a73c-200e3d3b8d40)

#### 4 Volvemos a cargar nuestro proyecto y vamos a la url home:

![image](https://github.com/user-attachments/assets/2e92a4ba-a7ad-43d6-a8bb-f9eb355bde19)

---

## 8 Una arquitectura de urls

Análogo a como lo hicimos con los templates, cada aplicación debe tener su propio archivo de urls, que van a ser llamadas en el archivo **urls.py** general. Creamos un archivo **urls.py** para la aplicación exp como se indica:

![image](https://github.com/user-attachments/assets/9f4c8d9e-eebf-45bf-be33-a55bf809cb2f)

Ahora llamamos éste **urls.py** de la aplicacion exp desde nuestro archivo **urls.py** general importando el paquete **include**:

![image](https://github.com/user-attachments/assets/618ff7f9-752d-45af-bc0f-eaa9d2c0e05b)

---

## 9 Primeros pasos en MVT

#### 1 Creemos la vista basada en clases ListView en nuestra aplicación exp. Para ello creamos la clase **Prueba_ListView**:

![image](https://github.com/user-attachments/assets/d06fcb00-7bf9-45fc-a457-7233e8bd8281)


#### 2 Agregamos el url en la aplicación exp:

![image](https://github.com/user-attachments/assets/0de9b66f-cb2c-4740-8a3f-5b43f96ce4e0)


#### 3 Construímos el archivo **lista.html** con el context_object_name dentro de llaves dobles:

![image](https://github.com/user-attachments/assets/b5f74c2c-39c2-46b3-ab78-fa6207b2ce34)

![image](https://github.com/user-attachments/assets/76228aeb-e993-4d9c-bf4c-6e2a98ff0369)





## 10 La ORM de Django y los modelos

La ORM de Django es una herramienta poderosa que permite a los desarrolladores interactuar con bases de datos de manera eficiente y efectiva utilizando Python, sin necesidad de escribir consultas SQL manualmente.

#### 1 Haremos que la ORM de Django trabaje construyendo nuestra primera base datos la que consistirá sólo en una tabla asociada a la base de datos que trea por defecto Django (sqlite3):

![image](https://github.com/user-attachments/assets/927e38c6-aa87-4fbe-b360-1073b0ea1c2e)

#### 2 Ahora le preguntaremos a Django si ha existido algún cambio en nuestra base de datos y/o es posible la creación de las tablas:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py makemigrations
Migrations for 'exp':
  applications\exp\migrations\0001_initial.py
    + Create model Prueba
```

#### 3 Ahora creamos la base de datos:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, exp, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying exp.0001_initial... OK
  Applying sessions.0001_initial... OK

(entorno_3) C:\mis_proyectos\emp3\empleado>
```

#### 4 Ahora, ¿coomo podemos interactuar con el modelo creado? Esto se consigue con el administrador de Django a traves del archivo admin.py de exp. Ingresamos las siguientes lineas de codigo:

![image](https://github.com/user-attachments/assets/7a89c4e4-80d5-4951-aad9-436a72e8484f)

#### 5 Creamos un superuser:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py createsuperuser
Username (leave blank to use 'chris'):
Email address: tarredwall@gmail.com
Password:
Password (again):
Superuser created successfully.

(entorno_3) C:\mis_proyectos\emp3\empleado>
```

La clave es: **123456**

#### 6 Levantamos nuevamente nuestro servidor e ingresamos al administrador con nuestras credenciales:

![image](https://github.com/user-attachments/assets/0a8d1951-de48-4032-941b-3a05cbea58b0)

#### 7 Podemos ir ahora llenando nuestra tabla **Prueba** desde el administrador:

![image](https://github.com/user-attachments/assets/543618a3-b9b1-4d22-8e0c-efa207cbcc9f)

![image](https://github.com/user-attachments/assets/d5b848d7-4e7b-473e-a784-dbab9fdeba40)
![image](https://github.com/user-attachments/assets/35bb9ed6-611d-4a13-b83b-c52dc2cea486)

#### 8 Ahora construyamos la vista basada en clases ModeloPruebaListView en views.py de la app exp:

```python
from django.views.generic import TemplateView, ListView  # type: ignore

from .models import Prueba

class IndexView(TemplateView):
   template_name = 'home/home.html'

class Prueba_ListView(ListView):
   template_name = "home/lista.html"
   queryset = ["uno","dos","tres"]
   context_object_name = "lista_prueba"

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name = "lista_prueba"
```

#### 9 Activamos la url asociada a la vista en urls.py de la app exp:

```python
from django.urls import path # type: ignore
from . import views

urlpatterns = [
   path('home/', views.IndexView.as_view()),
   path('lista/', views.Prueba_ListView.as_view()),
   path('lista-prueba/', views.ModeloPruebaListView.as_view()),
```

#### 10 Creamos nuestro html pruebas.html dentro de la carpeta templates/home:

```html
<h1>Listando elementos desde una base de datos</h1>

{{lista_prueba}}

<ul>
   {% for prueba in lista_prueba %}
      <li>
         {{prueba.titulo}}
      </li>
   {% endfor %}   
</ul>
```

#### 11 Vemos el despliegue:

![image](https://github.com/user-attachments/assets/cdae0be2-95fd-4f3e-b435-c0c33f0e2b8d)


---

## 11 Implementando la base de datos Empleado

Tipos de campos en Django: https://docs.djangoproject.com/en/5.1/ref/models/fields/

![image](https://github.com/user-attachments/assets/8dac515d-6913-48b2-b0c2-f4048b827da5)

#### 1 En models.py de la app Departamentos construimos el modelo Departamento:

```python
from django.db import models # type: ignore

class Departamento(models.Model):
   name = models.CharField("Nombre", max_length=50)
   short_name = models.CharField("Nombre Corto", max_length=20)
   anulate = models.BooleanField("Anulado", default=False)

   def __str__(self):
      return str(self.id) + "-" + self.name + "-" + self.short_name
```

```python
models.CharField('Nombre', max_length=50, editable=False)
# editable=False hace que el llenado del campo no se pueda editar.

models.CharField('Nombre', max_length=50, blank=True)
# blank=True hace que el llenado del campo no sea obligatorio.

models.BooleanField('Anulado', default=False)
# default=False hace que el campo venga por defecto con la selección NO anulado.

models.CharField('Nombre corto', max_length=20, unique=True)
# unique=True hace que el nombre del campo no se pueda volver a repetir.
```

#### 2 Lo registramos en al admin.py de la aplicación departamentos

```python
from django.contrib import admin # type: ignore
from .models import Departamento

admin.site.register(Departamento)
```

#### 3 Hacemos las migraciones:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py makemigrations
Migrations for 'departamentos':
  applications\departamentos\migrations\0001_initial.py
    + Create model Departamento

(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, departamentos, exp, sessions
Running migrations:
  Applying departamentos.0001_initial... OK

(entorno_3) C:\mis_proyectos\emp3\empleado>
```

#### 4 Y ya tenemos la tabla con funcionalidad en nuestro navegador:

![image](https://github.com/user-attachments/assets/eaff74d4-5663-4d5f-80e7-908100375af2)

---


## 12 Claves foráneas

#### 1 Construyamos el modelo **Empleado** en la app **empleados**

```python
from django.db import models # type: ignore
from applications.departamentos.models import Departamento

class Empleado(models.Model):
   JOB_CHOICES = (
      ("0","Sociólogo"),
      ("1","Antropólogo"),
      ("2","Psicólogo"),
      ("3","Economista")
   )
   first_name = models.CharField("Nombres", max_length=60)
   last_name = models.CharField("Apellidos", max_length=60)
   job = models.CharField("Trabajo", max_length=1, choices=JOB_CHOICES)
   departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
   
   def __str__(self):
      return str(self.id) + "-" + self.first_name + "-" + self.last_name
```

#### 2 Hacemos las migraciones.

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py makemigrations
Migrations for 'empleados':
  applications\empleados\migrations\0001_initial.py
    + Create model Empleado

(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, departamentos, empleados, exp, sessions
Running migrations:
  Applying empleados.0001_initial... OK

(entorno_3) C:\mis_proyectos\emp3\empleado>
```

#### 3 Registramos en el **admin.py** de la app empleados la tabla recien construida.

```python
from django.contrib import admin # type: ignore
from .models import Empleado

admin.site.register(Empleado)
```

#### 4 Abrimos el administrador e ingresamos un registro.

![image](https://github.com/user-attachments/assets/0ba07d8b-73f5-44fb-a212-973398910d09)

## 13 PostgreSQL y Django

#### 1 Descargemos el instalador de PostgreSQL

![image](https://github.com/user-attachments/assets/67399987-c891-4c11-b2de-f770c2c1dbbd)

![image](https://github.com/user-attachments/assets/acfac8cf-494f-4525-b238-c71cdb5e6572)

Le damos siguiente a todo:

![image](https://github.com/user-attachments/assets/68d73a14-cc8d-412e-90a5-6ead62b78007)

Ingresamos la contraseña 123456:

![image](https://github.com/user-attachments/assets/2b82d445-45b2-4208-b416-63256e6477bd)

Le damos siguiente a todo:

Y finalizamos sin seleccionar Stack Builder:

![image](https://github.com/user-attachments/assets/5844465e-3838-4e5f-913a-65af349287f1)

#### 2 Ahora que tenemos instalado nuestro postgreSQL en local, podemos acceder a la consola:

**SQL Shell (psql)**

![image](https://github.com/user-attachments/assets/25768bac-1771-4813-977d-a671be870950)

Damos enter hasta **Contraseña para usuario postgres:** para indicarle que cargue las opciones por defecto. Ingresamos 123456.

Creamos una base de datos y un usuario al que le damos permisos para acceder a la base de datos recien creada:

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

postgres=# CREATE DATABASE dbempleado101;
CREATE DATABASE
postgres=# CREATE USER chris101;
CREATE ROLE
postgres=# \c dbempleado101;
Ahora está conectado a la base de datos «dbempleado101» con el usuario «postgres».
dbempleado101=# ALTER ROLE chris101 WITH PASSWORD 'nueva123456';
ALTER ROLE
dbempleado101=#
```

#### 3 Ahora conectamos Django a nuestra base de datos PostgreSQL:

Instalamos el conector psycopg2:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>pip install psycopg2
Collecting psycopg2
  Downloading psycopg2-2.9.10-cp312-cp312-win_amd64.whl.metadata (5.0 kB)
Downloading psycopg2-2.9.10-cp312-cp312-win_amd64.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 29.1 MB/s eta 0:00:00
Installing collected packages: psycopg2
Successfully installed psycopg2-2.9.10

(entorno_3) C:\mis_proyectos\emp3\empleado>
```

#### 4 Configuramos el archivo local.py

```bash
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
```


#### 5 Hacemos las migraciones.

```bash
postgres=# ALTER DATABASE dbempleado101 OWNER TO chris101;
ALTER DATABASE
postgres=#
```
```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py makemigrations
No changes detected

(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, departamentos, empleados, exp, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying departamentos.0001_initial... OK
  Applying empleados.0001_initial... OK
  Applying exp.0001_initial... OK
  Applying sessions.0001_initial... OK

(entorno_3) C:\mis_proyectos\emp3\empleado>
```

#### 6 Para ingresar al administrador debemos volver a crear un super usuario pues nuestra base de datos en PostgreSQL es nueva y no tiene registrado ninguno.

Ingresamos como contraseña 123456:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py createsuperuser
Username (leave blank to use 'chris'):
Email address: tarredwall@gmail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

(entorno_3) C:\mis_proyectos\emp3\empleado>
```

#### 7 y ya estamos conectados:

![image](https://github.com/user-attachments/assets/6c865fc3-ae15-402f-aee1-a12abd4c0e22)

---

## 14 El Administrador de Django y la clase Meta

La clase Meta es opcional, pero muy útil para ajustar y personalizar el comportamiento de los modelos en el administrador de Django.

La clase Meta es una clase interna que se utiliza dentro de los modelos para definir opciones de metadatos. Estas opciones permiten personalizar el comportamiento del modelo sin tener que modificar su código principal. 

Algunas de las cosas que puedes hacer con la clase Meta:

#### 1 Ordenar los resultados: Puedes especificar el orden predeterminado de los registros cuando se recuperan de la base de datos.

```python
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['last_name']
```

#### 2 Nombres legibles: Puedes definir nombres legibles para el modelo en singular y plural.

```python
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
```

#### 3 Permisos personalizados: Puedes definir permisos específicos para el modelo.

```python
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        permissions = [
            ("can_view_persona", "Can view persona"),
        ]
```

#### 4 Nombre de la tabla: Puedes especificar el nombre de la tabla en la base de datos.

```python
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'mi_tabla_persona'
```

#### 5 Implementemos algunos cambios con ésta clase en nuesto modelo Departamento:

La opción unique_together en la clase Meta de un modelo Django se utiliza para especificar que una combinación de campos debe ser única en la base de datos. Esto significa que no se permitirán dos filas con la misma combinación de valores en esos campos.

```python
from django.db import models # type: ignore

class Departamento(models.Model):
   name = models.CharField("Nombre", max_length=50)
   short_name = models.CharField("Nombre Corto", max_length=20)
   anulate = models.BooleanField("Anulado", default=False)

   class Meta:
      verbose_name = "mi depa"
      verbose_name_plural = "mis depas"
      ordering = ['-name']
      unique_together = ['name', 'short_name']

   def __str__(self):
      return str(self.id) + "-" + self.name + "-" + self.short_name
```

#### 6 Apliquemos las migraciones:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py makemigrations
Migrations for 'departamentos':
  applications\departamentos\migrations\0002_alter_departamento_options_and_more.py
    ~ Change Meta options on departamento
    ~ Alter unique_together for departamento (1 constraint(s))

(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, departamentos, empleados, exp, sessions
Running migrations:
  Applying departamentos.0002_alter_departamento_options_and_more... OK

(entorno_3) C:\mis_proyectos\emp3\empleado>
```

## 15 Creando modelos dentro de una aplicación ya existente

#### 1 Creemos un modelo **Habilidades** en relación muchos a muchos con el modelo **empleado** e instalemos pillow para poder hacer uso del atributo ImageField:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>pip install pillow
```

```python
from django.db import models # type: ignore
from applications.departamentos.models import Departamento

class Habilidades(models.Model):

   habilidad = models.CharField('Habilidad', max_length=50)

   class Meta:
      verbose_name = 'Habilidad'
      verbose_name_plural = 'Habilidades'

   def __str__(self):
      return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
   JOB_CHOICES = (
      ("0","Sociólogo"),
      ("1","Antropólogo"),
      ("2","Psicólogo"),
      ("3","Economista")
   )
   first_name = models.CharField("Nombres", max_length=60)
   last_name = models.CharField("Apellidos", max_length=60)
   job = models.CharField("Trabajo", max_length=1, choices=JOB_CHOICES)
   departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
   avatar = models.ImageField(upload_to = 'empleado', blank = True, null = True)
   habilidades = models.ManyToManyField(Habilidades)
   
   def __str__(self):
      return str(self.id) + "-" + self.first_name + "-" + self.last_name
```

#### 2 Registremos la nueva tabla en el archivo **admin.py** de la aplicación **empleados**:

```python
from django.contrib import admin # type: ignore
from .models import Empleado, Habilidades

admin.site.register(Empleado)
admin.site.register(Habilidades)
```

#### 3 Hagamos las migraciones.

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py makemigrations
Migrations for 'empleados':
  applications\empleados\migrations\0002_habilidades_empleado_avatar_empleado_habilidades.py
    + Create model Habilidades
    + Add field avatar to empleado
    + Add field habilidades to empleado

(entorno_3) C:\mis_proyectos\emp3\empleado>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, departamentos, empleados, exp, sessions
Running migrations:
  Applying empleados.0002_habilidades_empleado_avatar_empleado_habilidades... OK

(entorno_3) C:\mis_proyectos\emp3\empleado>
```

#### 4 Veamos los modelos en el administrador:

![image](https://github.com/user-attachments/assets/6ddd09e3-8107-4cfb-8a84-4dbfddf3011a)


#### 5 Agreguemos nuevos empleados con habilidades específicas:

![image](https://github.com/user-attachments/assets/1c61a018-1f4f-40a9-a5cd-1a4ace47566d)




## 16 Personalizando al Administrador de Django (admin.py)

#### 1 El atributo list_display()

El atributo **list_display** en Django se utiliza en el archivo **admin.py** para especificar qué campos de un modelo deben mostrarse en la vista de lista del panel de administración. Esto es especialmente útil para proporcionar una visión general rápida de las instancias del modelo. 

```python
from django.contrib import admin # type: ignore
from .models import Empleado, Habilidades

class EmpleadoAdmin(admin.ModelAdmin):
   list_display = (
      'first_name',
      'last_name',
      'departamento',
      'job'
   )

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
```

![image](https://github.com/user-attachments/assets/8cf7d5af-488c-40d7-8bc1-3c9ca1469546)


#### 2 El atributo search_fields

Con search_fields podemos integrar al administrador un buscador. Implementemoslo para los primeros nombres:

```python
from django.contrib import admin # type: ignore
from .models import Empleado, Habilidades

class EmpleadoAdmin(admin.ModelAdmin):
   list_display = (
      'first_name',
      'last_name',
      'departamento',
      'job'
   )
   search_fields = ('first_name',)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
```

#### 3 El atributo list_filter

Con list_filter podemos agragar una funcionalidad de filtrado. Implementemosla para 'job' y 'habilidades':

```python
from django.contrib import admin # type: ignore
from .models import Empleado, Habilidades

class EmpleadoAdmin(admin.ModelAdmin):
   list_display = (
      'first_name',
      'last_name',
      'departamento',
      'job'
   )
   search_fields = ('first_name',)
   list_filter = ('job', 'habilidades')

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
```

![image](https://github.com/user-attachments/assets/c9d8312f-b78d-499d-9a28-06a5ecc58e58)



#### 4 El atributo filter_horizontal

El atributo filter_horizontal de Django se usa en el modelo de administración (admin) de Django para facilitar la selección y administración de relaciones many-to-many (muchos-a-muchos) en una interfaz de usuario más intuitiva. Cuando se agrega el atributo filter_horizontal a un modelo en el admin, se muestra un widget con dos listas: una lista de elementos disponibles y otra lista de elementos seleccionados. Esto permite a los usuarios seleccionar múltiples elementos fácilmente y moverlos entre las listas mediante botones. Apliquemoslo para el campo habilidades:

```python
from django.contrib import admin # type: ignore
from .models import Empleado, Habilidades

class EmpleadoAdmin(admin.ModelAdmin):
   list_display = (
      'first_name',
      'last_name',
      'departamento',
      'job'
   )
   search_fields = ('first_name',)
   list_filter = ('job', 'habilidades')
   filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
```

![image](https://github.com/user-attachments/assets/0a921e90-d916-4dde-baad-9e211695e62e)


#### 5 Desplegando nuevos campos

Supongamos que tenemos la necesidad de que se muestre en el listado del administrador una nueva columna que integre los nombres y los apellidos de los empleados sin intervenir en la base de datos y llamemos al campo 'full_name'. Para hacer esto debemos declarar una funcion:

```python
from django.contrib import admin # type: ignore
from .models import Empleado, Habilidades

class EmpleadoAdmin(admin.ModelAdmin):
   list_display = (
      'first_name',
      'last_name',
      'departamento',
      'job',
      'full_name'
   )

   def full_name(self, obj):
      return obj.first_name + ' ' + obj.last_name

   search_fields = ('first_name',)
   list_filter = ('job', 'habilidades')
   filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
```

![image](https://github.com/user-attachments/assets/bf088c6d-aac4-4652-ab1a-dc80d0915448)

## 17 La app CKEditor

#### 1 Definición

https://django-ckeditor.readthedocs.io/en/latest/

CKEditor (una apps de terceros) es uneditor de texto enriquecido que se puede integrar fácilmente en proyectos de Django mediante el paquete django-ckeditor. Este editor permite a los usuarios crear y editar contenido con formato, similar a lo que se puede hacer en un procesador de textos como Microsoft Word. Aquí te explico algunas de sus características y cómo se utiliza:

Características Principales:

17.1.1.1 Formato de Texto: Permite aplicar estilos como negrita, cursiva, subrayado, y tachado.\
17.1.1.2 Listas y Tablas: Facilita la creación de listas ordenadas y desordenadas, así como tablas.\
17.1.1.3 Multimedia: Soporta la inserción de imágenes, videos y otros elementos multimedia.\
17.1.1.4 Enlaces: Permite añadir enlaces a otros sitios web o documentos.\
17.1.1.5 Código y Bloques de Cita: Incluye opciones para insertar bloques de código y citas.

![image](https://github.com/user-attachments/assets/8a104377-9260-437a-b5a7-d1e910f38984)

#### 2 La instalamos

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>pip install django-ckeditor
```

#### 3 Registramos ckeditor en el archivo **base.py**

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-9xh%=ob5sj*g*r5&ii^r$mu9bs0w*t09ni*vko67=*z402som8'

INSTALLED_APPS = [
   'django.contrib.admin',
   'django.contrib.auth',
   'django.contrib.contenttypes',
   'django.contrib.sessions',
   'django.contrib.messages',
   'django.contrib.staticfiles',

   # Apps de terceros
   'ckeditor',
   
   # local apps
   "applications.departamentos",
   "applications.empleados",
   'applications.exp'
]

MIDDLEWARE = [

# ...
```

#### 4 Importamos la app y agregamos un campo que tenga la forma de elemento de blog:

```python
from django.db import models # type: ignore
from applications.departamentos.models import Departamento
from ckeditor.fields import RichTextField # type: ignore

class Habilidades(models.Model):

#...

   avatar = models.ImageField(upload_to = 'empleado', blank = True, null = True)
   habilidades = models.ManyToManyField(Habilidades)
   hoja_vida = RichTextField()

   def __str__(self):
      return str(self.id) + "-" + self.first_name + "-" + self.last_name
```

#### 5 Hacemos las migraciones y volvemos a cargar el servidor. Vámonos al administrador de Django a intentar ingresar un nuevo empleado:

![image](https://github.com/user-attachments/assets/adc6d010-01a6-46ff-94ca-7ca21465d55b)



