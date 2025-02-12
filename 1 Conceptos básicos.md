# Django

https://docs.djangoproject.com/en/5.1/

Christian Castro

Bienvenido a este manual sobre el desarrollo de aplicaciones web completas utilizando Django, uno de los frameworks más populares y robustos para Python. Django es conocido por su capacidad para facilitar el desarrollo rápido y seguro de aplicaciones web, gracias a su filosofía de “baterías incluidas”, que proporciona una amplia gama de herramientas y funcionalidades listas para usar.

En este manual, te guiaremos paso a paso a través del proceso de creación de una aplicación web completa. Desde la configuración inicial del entorno de desarrollo hasta la implementación de funcionalidades avanzadas, aprenderás a:

- Configurar tu entorno de desarrollo: Instalación de Django y configuración de tu proyecto.
- Crear y gestionar modelos de datos: Definir las estructuras de datos y cómo interactuar con la base de datos.
- Desarrollar vistas y plantillas: Crear la lógica de negocio y las interfaces de usuario.
- Implementar autenticación y autorización: Gestionar usuarios y permisos.
- Desplegar tu aplicación: Preparar y lanzar tu aplicación en un entorno de producción.

Este manual está diseñado tanto para principiantes como para desarrolladores con experiencia previa en otros frameworks. A lo largo del camino, proporcionaremos ejemplos prácticos y mejores prácticas para asegurarnos de que puedas aprovechar al máximo las capacidades de Django.

¡Empecemos este emocionante viaje hacia el desarrollo de aplicaciones web con Django!

> Christian Castro.
> Sociólogo, U. de Chile.
> Analista programador, Inacap.

## Índice

* [1 Crear un proyecto Django](#1-crear-un-proyecto-django)
  * [11 Creemos una carpeta donde vamos a alojar todo nuestro trabajo](#11-Creemos-una-carpeta-donde-vamos-a-alojar-todo-nuestro-trabajo)
* [2 Configurar la estructura de un proyecto en django](#2-Configurar-la-estructura-de-un-proyecto-en-django)
* [3 Ejecutando el archivo localpy en vez del original settingspy](#3-Ejecutando-el-archivo-localpy-en-vez-del-original-settingspy)
* [4 Aplicaciones](#4-Aplicaciones)
* [5 Vistas genericas (Views)](#5-Vistas-genericas-Views)
* [6 Haciendo una carpeta templates generalizada](#6-Haciendo-una-carpeta-templates-generalizada)
* [7 Haciendo una carpeta parcial para cada app](#7-Haciendo-una-carpeta-parcial-para-cada-app)
* [8 Vistas genéricas](#8-Vistas-genéricas)
* [9 Nuestros primeros pasos en MVT](#9-Nuestros-primeros-pasos-en-MVT)
* [10 el ORM de Django y modelos](#10-el-ORM-de-Django-y-modelos)
* [11 Implementando la base de datos Empleado](#11-Implementando-la-base-de-datos-Empleado)
* [12 Claves foráneas](#12-Claves-foráneas)
* [13 PostgreSQL y Django](#13-PostgreSQL-y-Django)
* [14 El Administrador de Django](#14-El-Administrador-de-Django)
  * [14.1 La clase meta](#14.1-La-clase-meta)
* [15 Creando modelos dentro de una aplicación ya existente](#15-Creando-modelos-dentro-de-una-aplicación-ya-existente)
* [16 Diseñar un despliegue de registros al administrador de Django para el modelo empleados](#16-Diseñar-un-despliegue-de-registros-al-administrador-de-Django-para-el-modelo-empleados)
* [17 Algunas apps de terceros](#17-Algunas-apps-de-terceros)

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

### 1.1 Creamos carpetas de trabajo:

Construiremos dos carpetas en C. Una para nuestros proyectos **mis_proyectos** y otra para nuestros entornos virtuales **mis_entornos**


### 1.2 Creamos nuestro primer entorno y lo activamos:

```bash
C:\>cd mis_entornos
C:\mis_entornos>python -m venv entorno_1
C:\mis_entornos>cd entorno_3/Scripts
C:\mis_entornos\entorno_3\Scripts>activate
(entorno_3) C:\mis_entornos\entorno_3\Scripts>
(entorno_3) C:\mis_entornos\entorno_3\Scripts>cd /
(entorno_3) C:\>
```

### 1.3 Instalamos y actualizamos paquetes:

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

### 1.4 En ella, creamos nuestro proyecto **empleado**:

```bash
(entorno_3) C:\mis_proyectos\emp3> django-admin startproject empleado
```

### 1.5 corremos el servidor:

```bash
(entorno_3) C:\mis_proyectos\emp3> cd empleado
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

### 1.6 Abrimos el proyecto empleado con Visual Studio:

![image](https://github.com/user-attachments/assets/8dbfe7f4-3409-486d-aad0-9e44669ae4f0)

## 2 Configurar la estructura de un proyecto en django

En cualquier desarrollo necesitamos al menos tres entornos (para trabajo local, de pruebas y de producción) y un cuarto **base**. En el entorno **base** alojaremos la configuración básica de todos.

2.1 Dentro de la carpeta **empleado**, creamos otra carpeta llamada **settings** con cuatro archivos .py en su interior:

![image](https://github.com/user-attachments/assets/3ca4a2a9-bc58-4365-9a2b-15939a7ccf1e)

2.2 Del archivo original settings.py debemos copiar a los archivos recién creados, lo siguiente:

2.2.1 en **base.py**:

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

2.2.2 en **local.py**:

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

## 3 Ejecutando el archivo localpy en vez del original settingspy

### 3.1 Borramos el archivo settings.py original.

### 3.2 Le indicamos a django que ejecute desde el entorno de configuración local.py:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver --settings=empleado.settings.local
```

### 3.3 Redireccionamos para aumentar la simplicidad al ejecutar el proyecto:

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

### 3.4 Ahora podemos ejecutar simplemente escribiendo:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

## 4 Aplicaciones

Las aplicaciones en django son pequeños proyectos completos. La idea es que:

1 cada una sea independiente de las otras con el objetivo de poder reutilizarlas si fuese necesario y

2 cada una se dedique a un solo proceso de la lógica del negocio.

Crearemos dos aplicaciones dentro de una nueva carpeta llamada **applications** dentro de la carpeta **empleado** junto con un archivo __init__.py. Serán las aplicaciones **departamentos** y **empleados**:

![image](https://github.com/user-attachments/assets/8a4cacb5-da70-4e4d-8e39-453c3285dcfe)

![image](https://github.com/user-attachments/assets/f73a5271-00ec-4b33-bcbb-1fe024e9b954)

### 4.1 Vamos al nivel de applications y creamos los dos nuevos proyectos:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado>cd applications
(entorno_3) C:\mis_proyectos\emp3\empleado\applications> django-admin startapp departamentos
(entorno_3) C:\mis_proyectos\emp3\empleado\applications> django-admin startapp empleados
```

![image](https://github.com/user-attachments/assets/1aa17e99-bb1c-4d5f-86d6-02832aaf329f)

### 4.2 Ahora necesitamos instalar nuestras aplicaciones en el archivo base.py:

![image](https://github.com/user-attachments/assets/08fe8f7d-9fd1-467e-ae0a-c5ef06cd6ab9)

y en cada uno de los archivos apps.py de las aplicaciones departamentos y empleados anteponemos el prefijo applications:

![image](https://github.com/user-attachments/assets/3061723c-e662-46dd-918c-f7523e100b05)
![image](https://github.com/user-attachments/assets/5709f22a-3467-4e0e-a8f6-c083455dc413)

### 4.3 Levantemos nuestro servidor para que veamos que todo esté funcionando ok:

```bash
(entorno_3) C:\mis_proyectos\emp3\empleado> python manage.py runserver
```

## 5 Vistas genéricas Views

### 5.1 La teoría del patrón de diseño MVT

El patrón Modelo-Vista-Template (MVT) de Django es una variación del clásico Modelo-Vista-Controlador (MVC). A continuación, veamos en qué consiste el MVT y sus diferencias clave con MVC:

### 5.2 Modelo-Vista-Template (MVT) en Django

Modelo (**Model**):

Se encarga de la lógica de acceso a los datos y define la estructura de la base de datos. En Django, los modelos son clases de Python que se traducen en tablas de la base de datos.

Ejemplo: Definir un modelo Usuario con campos como nombre, email, y fecha_de_nacimiento.

Vista (**View**):

Contiene la lógica de negocio y controla qué datos se envían al usuario. Las vistas en Django son funciones o clases que reciben una solicitud HTTP, interactúan con el modelo si es necesario, y devuelven una respuesta HTTP.

Ejemplo: Una vista que recupera todos los usuarios de la base de datos y los envía a una plantilla para su visualización.

Plantilla (**Template**):

Es la capa de presentación que define cómo se muestran los datos al usuario. Las plantillas en Django son archivos HTML que pueden contener etiquetas de plantilla de Django para mostrar datos dinámicos.

Ejemplo: Un archivo HTML que muestra una lista de usuarios con sus nombres y correos electrónicos.

### 5.3 Diferencias con el Modelo Vista-Controlador (MVC)

Controlador (Controller) vs. Vista (View):

En el patrón MVC, el Controlador maneja la lógica de negocio y la interacción entre el modelo y la vista. En Django, esta función la realiza la Vista. En MVC, la Vista es responsable solo de la presentación de los datos. En MVT, la Plantilla cumple esta función.

Terminología:\
Aunque la funcionalidad es similar, la terminología difiere. En Django, lo que en MVC se llama Controlador se llama Vista, y lo que en MVC se llama Vista se llama Plantilla.

Flujo de Trabajo:

En MVC, el flujo típico es: Usuario → Controlador → Modelo → Vista → Usuario.

En MVT, el flujo es: Usuario → Vista → Modelo → Plantilla → Usuario.

### 5.4 Ejemplo Práctico

Supongamos que queremos mostrar una lista de productos en una tienda en línea:

Modelo (Model): Definimos un modelo Producto con campos como nombre, precio, y descripción.

Vista (View): Creamos una vista que recupera todos los productos de la base de datos y los pasa a una plantilla.

Plantilla (Template): Diseñamos un archivo HTML que muestra la lista de productos con sus nombres y precios.

En resumen, el patrón MVT de Django es una adaptación del patrón MVC, con una terminología y flujo de trabajo ligeramente diferentes, pero con el mismo objetivo de separar la lógica de negocio, la lógica de presentación y la interfaz de usuario.

aca voy 19:22
11-02-25

 
## 6 La creación de una vista

Haremos pruebas dentro de una nueva aplicacion que crearemos para tal efecto.

### 6.1 La aplicacion exp

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





---

## 7 Una arquitectura de templates

### 7.1 Una carpeta templates general

Una buena práctica es contruir una carpeta templates donde tengamos sub carpetas asociadas a las apps y dentro de ellas los correspondientes htmls. Construímos la carpeta como se indica con la subcarpeta y dentro de ella copiamos **home.html** y borramos la carpeta templates de la app exp:

![image](https://github.com/user-attachments/assets/67f60d17-4cac-4d6d-9b59-c511e2452ef5)

### 7.3 Hacemos las siguientes modificaciones en el archivo base.py:

![image](https://github.com/user-attachments/assets/8769b9a4-10c9-4e2f-8b2c-03a6a2ffd4dd)

### 7.4 Hacemos las siguientes modificaciones en la vista de nuestra aplicación exp:

![image](https://github.com/user-attachments/assets/c805788e-a7d6-4818-a73c-200e3d3b8d40)

### 7.5 Volvemos a cargar nuestro proyecto y vamos a la url home:

![image](https://github.com/user-attachments/assets/2e92a4ba-a7ad-43d6-a8bb-f9eb355bde19)

---

## 8 Una arquitectura de urls

Análogo a como lo hicimos con los templates, cada aplicación debe tener su propio archivo de urls, que van a ser llamadas en el archivo **urls.py** general. Creamos un archivo **urls.py** para la aplicación exp como se indica:

![image](https://github.com/user-attachments/assets/9f4c8d9e-eebf-45bf-be33-a55bf809cb2f)

Ahora llamamos éste **urls.py** de la aplicacion exp desde nuestro archivo **urls.py** general importando el paquete **include**:

![image](https://github.com/user-attachments/assets/618ff7f9-752d-45af-bc0f-eaa9d2c0e05b)

---

## 9 Primeros pasos en MVT

1 Creemos la vista basada en clases ListView en nuestra aplicación exp. Para ello creamos la clase **Prueba_ListView**:

![image](https://github.com/user-attachments/assets/d06fcb00-7bf9-45fc-a457-7233e8bd8281)


2 Agregamos el url en la aplicación exp:

![image](https://github.com/user-attachments/assets/0de9b66f-cb2c-4740-8a3f-5b43f96ce4e0)


3 Construímos el archivo **lista.html** con el context_object_name dentro de llaves dobles:

![image](https://github.com/user-attachments/assets/b5f74c2c-39c2-46b3-ab78-fa6207b2ce34)

![image](https://github.com/user-attachments/assets/76228aeb-e993-4d9c-bf4c-6e2a98ff0369)

---



## 11 el ORM de Django y modelos

el ORM de Django es una herramienta poderosa que permite a los desarrolladores interactuar con bases de datos de manera eficiente y efectiva utilizando Python, sin necesidad de escribir consultas SQL manualmente.

Haremos que la ORM de Django trabaje construyendo nuestra primera base datos la que consistirá sólo en una tabla asociada a la base de datos que trea por defecto Django (sqlite3):

![image](https://github.com/user-attachments/assets/2eef1b7e-775a-424c-a0ae-693437d6690a)

Ahora le preguntaremos a Django si ha existido algún cambio en nuestra base de datos y/o es posible la creación de las tablas:

C:\Users\chris\django\proyecto_1\empleado>cd \Users\chris\django\proyecto_1\entorno_1\Scripts

C:\Users\chris\django\proyecto_1\entorno_1\Scripts>activate

(entorno_1) C:\Users\chris\django\proyecto_1\entorno_1\Scripts>cd \Users\chris\django\proyecto_1\empleado

(entorno_1) C:\Users\chris\django\proyecto_1\empleado>python manage.py makemigrations

![image](https://github.com/user-attachments/assets/73b4912e-5896-4558-a333-b0e1a170a116)

Ahora creamos la base de datos:

(entorno_1) C:\Users\chris\django\proyecto_1\empleado>python manage.py migrate

![image](https://github.com/user-attachments/assets/5fc24361-f497-4a80-818a-a0c0caeb4e5a)

Ahora, como podemos interactuar con el modelo creado? Esto se consigue con el administrador de Django a traves del archivo admin.py de exp. Ingresamos las siguientes lineas de codigo:

![image](https://github.com/user-attachments/assets/bb13badc-6316-43c1-aa3d-240aa36a72fb)

levantemos nuestro servidor y vayamos a la url admin:

(entorno_1) C:\Users\chris\django\proyecto_1\empleado>python manage.py runserver

![image](https://github.com/user-attachments/assets/debc54e7-dec8-4241-89dc-b1d4b7ebe935)

bajemos nuestro servidor para en la terminal crear un superuser:

(entorno_1) C:\Users\chris\django\proyecto_1\empleado>python manage.py createsuperuser

Username: chris\
Email address: tarredwall@gmail.com\
Password: cualquiercosa

Levantamos nuevamente nuestro servidor e ingresamos al administrador con nuestras credenciales:

![image](https://github.com/user-attachments/assets/e077e7ed-8e07-4294-8a08-e586d475f348)

Siguiendo el patron MVT agreguemos una vista, activemos su url, construyamos el respectivo html, levantemos nuestro servidor y vayamos al navegador:

![image](https://github.com/user-attachments/assets/c9d32b74-e475-4a3f-b568-5062c61abc6f)

![image](https://github.com/user-attachments/assets/cdf0e17e-63d1-4f67-ba21-b45f65386bba)

![image](https://github.com/user-attachments/assets/108500c0-761a-4c62-9f0a-2f09dfe2b8da)

![image](https://github.com/user-attachments/assets/720a9d62-e42d-4f26-b164-9c4065ab9034)

## 11 Implementando la base de datos Empleado.

![image](https://github.com/user-attachments/assets/8dac515d-6913-48b2-b0c2-f4048b827da5)

1 Construimos el modelo Departamento

consideremos los siguientes parámetros de los campos:
```
models.CharField('Nombre', max_length=50, editable=False)
```
editable=False hace que el llenado del campo no se pueda editar.

```
models.CharField('Nombre', max_length=50, blank=True)
```
blank=True hace que el llenado del campo no sea obligatorio.
```
models.BooleanField('Anulado', default=False)
```
default=False hace que el campo venga por defecto con la selección NO anulado.
```
models.CharField('Nombre corto', max_length=20, unique=True)
```
unique=True hace que el nombre del campo no se pueda volver a repetir.

![image](https://github.com/user-attachments/assets/d018d264-f6ad-4c59-812c-412922e2de22)

2 lo registramos en al admin.py de la aplicación departamentos

![image](https://github.com/user-attachments/assets/bb08b6a6-6a9c-46a0-9629-d8b0bd79dd4f)

3 y ya tenemos la tabla con funcionalidad en nuestro navegador:

![image](https://github.com/user-attachments/assets/450ddc01-2aac-4f05-bf2e-af9864df56ab)

4 es importante enfatizar de que las migraciones para que surtan efecto deben pertenecer a las aplicaciones instaladas:

![image](https://github.com/user-attachments/assets/c1ed3f50-4e6a-47c3-8297-adcfa3b34148)

## 12 Claves foráneas.

![image](https://github.com/user-attachments/assets/d11b2bc9-b07a-4756-af4c-4695d8b1ab88)

![image](https://github.com/user-attachments/assets/9ea1d153-190b-4e03-ad5f-a703a72c8583)

![image](https://github.com/user-attachments/assets/25ba4780-3b80-4ebc-9c9b-26061c083c5c)

![image](https://github.com/user-attachments/assets/2ec89b2e-554e-464d-8b5e-3d9d7ecb39f4)

## 13 PostgreSQL y Django

1 Descargemos el instalador de PostgreSQL

![image](https://github.com/user-attachments/assets/67399987-c891-4c11-b2de-f770c2c1dbbd)

![image](https://github.com/user-attachments/assets/acfac8cf-494f-4525-b238-c71cdb5e6572)

Le damos siguiente a todo:

![image](https://github.com/user-attachments/assets/68d73a14-cc8d-412e-90a5-6ead62b78007)

Ingresamos la contraseña 123456:

![image](https://github.com/user-attachments/assets/2b82d445-45b2-4208-b416-63256e6477bd)

Le damos siguiente a todo:

Y finalizamos:

![image](https://github.com/user-attachments/assets/5844465e-3838-4e5f-913a-65af349287f1)

Ahora que tenemos instalado nuestro postgreSQL en local, podemos acceder a la consola:

**SQL Shell (psql)**

![image](https://github.com/user-attachments/assets/25768bac-1771-4813-977d-a671be870950)

Damos enter hasta **Contraseña para usuario postgres:** para indicarle que cargue las opciones por defecto. Ingresamos 123456 y creamos nuestra base de datos.

Creamos un usuario y le damos permisos para acceder a la base de datos recien creada:

![image](https://github.com/user-attachments/assets/33066c2b-e8a5-433e-96c5-02388ec81b99)

Ahora conectamos Django a nuestra base de datos PostgreSQL:

Instalamos el conector psycopg2:

![image](https://github.com/user-attachments/assets/e8cf2aa5-6620-4dc6-9b88-db1db45b5118)

Configuramos el archivo local.py

![image](https://github.com/user-attachments/assets/5b3a443c-879c-4b4f-827c-ee79e4080ca7)

![image](https://github.com/user-attachments/assets/35ef59a6-daea-4b55-8091-f3a9a0a49e7d)

![image](https://github.com/user-attachments/assets/69184304-e843-4b70-a3c1-320f539eaee1)

Debemos volver a crear un super usuario!

![image](https://github.com/user-attachments/assets/85ac7202-aba1-44a2-b1c3-2c88f36f19db)

Pues nuestra base de datos en PostgreSQL es nueva y no tiene registrado ningun usuario.

Ingresamos como contraseña 123456:

![image](https://github.com/user-attachments/assets/3a6ea903-e48d-42f6-aa54-aa4d933a8881)

y ya estamos conectados:

![image](https://github.com/user-attachments/assets/c3962e0c-2636-43ea-bf4f-75a8e3ba1e19)

## 14 El Administrador de Django

### 14.1 La clase meta

La clase Meta es completamente opcional, pero es muy útil para ajustar y personalizar el comportamiento de tus modelos en Django.

En Django, la clase Meta es una clase interna que se utiliza dentro de los modelos para definir opciones de metadatos. Estas opciones permiten personalizar el comportamiento del modelo sin tener que modificar el código principal del modelo. Aquí hay algunas de las cosas que puedes hacer con la clase Meta:

14.1 Ordenar los resultados: Puedes especificar el orden predeterminado de los registros cuando se recuperan de la base de datos.

```
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['last_name']
```

14.2 Nombres legibles: Puedes definir nombres legibles para el modelo en singular y plural.

```
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
```

14.3 Permisos personalizados: Puedes definir permisos específicos para el modelo.

```
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        permissions = [
            ("can_view_persona", "Can view persona"),
        ]

```

14.4 Nombre de la tabla: Puedes especificar el nombre de la tabla en la base de datos.

```
class Persona(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'mi_tabla_persona'

```

Implementemos algunos cambios con ésta clase en nuesto modelo Departamento:

![image](https://github.com/user-attachments/assets/02a551bf-d8c0-4a1f-8c50-311b3d6af117)

Hacemos las migraciones y levantamos el servidor:

![image](https://github.com/user-attachments/assets/4a13f415-0027-40ca-9486-67fdac98371a)

veamos como nos queda el administrador:

![image](https://github.com/user-attachments/assets/ea92d0a5-e7f6-47af-8c17-170a6e92a21b)


## 15 Creando modelos dentro de una aplicación ya existente

15.1 Creemos un modelo **Habilidades** en relación muchos a muchos con el modelo **empleado** e instalemos pillow para poder hacer uso del atributo ImageField:

(entorno_1) C:\Users\chris\django\proyecto_1\empleado>pip install pillow

![image](https://github.com/user-attachments/assets/0d9618aa-cee2-4c4c-b634-51344ff8f7f6)

15.2 Registremos la nueva tabla en el archivo **admin.py** de la aplicación **empleados**:

![image](https://github.com/user-attachments/assets/0f6a19cb-8538-46d8-852e-6e836ba168a1)

15.3 Bajemos el servidor, hagamos las migraciones y reiniciemos:

![image](https://github.com/user-attachments/assets/aedef6c3-9b2f-443e-9aeb-a5852370d12e)

15.4 Ahora tenemos dos modelos en la aplicación **EMPLEADOS**:

![image](https://github.com/user-attachments/assets/709648ff-374a-4819-a1e9-0cf54bffdad8)

15.5 Agreguemos nuevos empleados con habilidades específicas:

![image](https://github.com/user-attachments/assets/4f17c772-b53c-4f09-a9bf-ac7e34f7e95a)

![image](https://github.com/user-attachments/assets/b2b0e43f-3a98-4be4-adce-4cc7009937c9)

![image](https://github.com/user-attachments/assets/7857e781-1b20-4567-bff2-cf136e529e5a)

![image](https://github.com/user-attachments/assets/1352732a-fa2b-4de1-8fe2-6828b822ffed)

## 16 Diseñar un despliegue de registros al administrador de Django para el modelo empleados

### 16.1 El atributo list_display()

El atributo list_display en Django se utiliza en la clase ModelAdmin para especificar qué campos de un modelo deben mostrarse en la vista de lista del panel de administración. Esto es especialmente útil para proporcionar una visión general rápida de las instancias del modelo. 

![image](https://github.com/user-attachments/assets/ba7709cc-2d2f-4398-a62e-6e8bd5e2f299)

![image](https://github.com/user-attachments/assets/2b266887-bca5-42ea-b94f-a60e759ade1d)

16.2 Buscadores y filtros

![image](https://github.com/user-attachments/assets/1e13fd86-6592-44bb-b07a-9fbd64ab9cf2)

![image](https://github.com/user-attachments/assets/030a0314-c4da-47a0-9a9f-d13857156f35)

Podemos integrar una interfaz mas agradable paras seleccionar atributos en relaciones muchos a muchos:

![image](https://github.com/user-attachments/assets/2c1a8451-e8cb-40da-8e1d-9fda5b1f7d2f)

![image](https://github.com/user-attachments/assets/43c1a300-d1d5-4135-935d-0560e3677e98)

16.3 Agregar campos en el despliegue de registros del administrador que no formen parte de los modelos sino que sean producto de alguna operacion sobre los campos de un mismo registro

Podemos añadir una columna que integre primer y segundo apellido de cada registro:

![image](https://github.com/user-attachments/assets/421b3af8-4c7d-4cb8-a979-2d7b75fc2314)

![image](https://github.com/user-attachments/assets/6a58b3a7-16ee-47f8-a86b-75178569292c)

## 17 Algunas apps de terceros

### 17.1 La app Django CKEditor

CKEditor es una aplicación de editor de texto enriquecido que se puede integrar fácilmente en proyectos de Django mediante el paquete django-ckeditor. Este editor permite a los usuarios crear y editar contenido con formato, similar a lo que se puede hacer en un procesador de textos como Microsoft Word. Aquí te explico algunas de sus características y cómo se utiliza:

Características Principales\
17.1.1.1 Formato de Texto: Permite aplicar estilos como negrita, cursiva, subrayado, y tachado.\
17.1.1.2 Listas y Tablas: Facilita la creación de listas ordenadas y desordenadas, así como tablas.\
17.1.1.3 Multimedia: Soporta la inserción de imágenes, videos y otros elementos multimedia.\
17.1.1.4 Enlaces: Permite añadir enlaces a otros sitios web o documentos.\
17.1.1.5 Código y Bloques de Cita: Incluye opciones para insertar bloques de código y citas.

![image](https://github.com/user-attachments/assets/8a104377-9260-437a-b5a7-d1e910f38984)

![image](https://github.com/user-attachments/assets/7f2c66e9-dbd3-44d8-be82-d6be771146ce)

17.1.2 Registramos al app de terceros ckeditor en el archivo **base.py**

![image](https://github.com/user-attachments/assets/f3317cfb-804a-49ff-b8a9-2c68e45d8204)

17.1.3 Agregamos un campo que tenga la forma de elemento de blog:

![image](https://github.com/user-attachments/assets/206c94db-59db-4433-8d8c-e4b74e49a665)

17.1.4 Hacemos las migraciones y volvemos a cargar el servidor. Vámonos a la página del administrador de Django:

![image](https://github.com/user-attachments/assets/f3f7572f-8c2a-4bb0-9f70-ac5c9d92b475)


