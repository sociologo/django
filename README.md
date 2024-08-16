# Django

Bienvenido a este manual sobre el desarrollo de aplicaciones web completas utilizando Django, uno de los frameworks más populares y robustos para Python. Django es conocido por su capacidad para facilitar el desarrollo rápido y seguro de aplicaciones web, gracias a su filosofía de “baterías incluidas”, que proporciona una amplia gama de herramientas y funcionalidades listas para usar.

En este manual, te guiaremos paso a paso a través del proceso de creación de una aplicación web completa. Desde la configuración inicial del entorno de desarrollo hasta la implementación de funcionalidades avanzadas, aprenderás a:

Configurar tu entorno de desarrollo: Instalación de Django y configuración de tu proyecto.
Crear y gestionar modelos de datos: Definir las estructuras de datos y cómo interactuar con la base de datos.
Desarrollar vistas y plantillas: Crear la lógica de negocio y las interfaces de usuario.
Implementar autenticación y autorización: Gestionar usuarios y permisos.
Desplegar tu aplicación: Preparar y lanzar tu aplicación en un entorno de producción.
Este manual está diseñado tanto para principiantes como para desarrolladores con experiencia previa en otros frameworks. A lo largo del camino, proporcionaremos ejemplos prácticos y mejores prácticas para asegurarnos de que puedas aprovechar al máximo las capacidades de Django.

¡Empecemos este emocionante viaje hacia el desarrollo de aplicaciones web con Django!

## Índice

* [1 Crear un proyecto Django](#1-crear-un-proyecto-django)
  * [11 Creemos una carpeta donde vamos a alojar todo nuestro trabajo](#11-Creemos-una-carpeta-donde-vamos-a-alojar-todo-nuestro-trabajo)
* [2 Configurar la estructura de un proyecto en django](#2-Configurar-la-estructura-de-un-proyecto-en-django)
* [3 Ejecutando el archivo localpy en vez del original settingspy](#3-Ejecutando-el-archivo-localpy-en-vez-del-original-settingspy)
* [4 Aplicaciones](#4-Aplicaciones)
* [5 Vistas genericas (Views)](#5-Vistas-genericas-Views)

## 1 Crear un proyecto Django

(para limpiar la consola utilizamos el comando **cls**)
(para salir de la consola utilizamos el comando **CTRL+C**)

### 11 Creemos una carpeta donde vamos a alojar todo nuestro trabajo:
C:\Users\chris\django\proyecto_1

### 1.2 Entramos a la terminal escribiendo CMD en el cuadro de búsqueda de windows y vamos a nuestra carpeta:
cd \Users\chris\django\proyecto_1

### 1.3 Creamos un entorno virtual dentro de ella:
python -m venv entorno_1

### 1.4 Nos dirigimos a la carpeta Scripts del entorno_1:
cd \Users\chris\django\proyecto_1\entorno_1\Scripts

### 1.5 Activamos el entorno con **activate**:
C:\Users\chris\django\proyecto_1\entorno_1\Scripts> activate\
(entorno_1) C:\Users\chris\django\proyecto_1\entorno_1\Scripts>

### 1.6 Instalamos Django:
(entorno_1) C:\Users\chris\django\proyecto_1\entorno_1\Scripts> pip install django

### 1.7 Ahora, en el entorno activo, nos dirigimos a la carpeta donde vamos a construir nuestro proyecto:
(entorno_1) C:\Users\chris\django\proyecto_1\entorno_1\Scripts>cd \Users\chris\django\proyecto_1\
(entorno_1) C:\Users\chris\django\proyecto_1>

### 1.8 En ella, creamos nuestro proyecto **empleado**:
(entorno_1) C:\Users\chris\django\proyecto_1> django-admin startproject empleado

### 1.9 Abrimos el proyecto empleado con Visual Studio:

![image](https://github.com/user-attachments/assets/2e9cee98-5375-4b48-9033-b116c59d4823)

## 2 Configurar la estructura de un proyecto en django

En cualquier desarrollo necesitamos al menos tres entornos (para trabajo local, de producción de pruebas) y y uno base donde alojaremos la configuración básica de todos ellos:\
Para ello, creamos dentro de la carpeta empleado, una llamada **settings** con cuatro archivos .py en su interior:\
1 local.py\
2 prod.py\
3 testing.py\
4 base.py

1.11 Del archivo original settings.py debemos copiar a los archivos recién creados, lo siguiente:\
en **base.py**:\
```
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-3q5hd^5yi2w8rb9geeb&pn1q$%=gf+5!arqkzm14c-!d0@)#3#'

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

en **local.py**:\
```
from .base import *

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

### Borramos el archivo settings.py del proyecto original.

### Le indicamos a django que ejecute desde el entorno de configuración local.py:

(entorno_1) C:\Users\chris\django\proyecto_1\empleado> python manage.py runserver --settings= empleado.settings.local

### Redireccionando para aumentar la simplicidad al ejecutar el proyecto:

Agregamos .local a la siguiente l[inea del archivo manage.py:

```
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

con la que ahora podemos ejecutar simplemente escribiendo:\
(entorno_1) C:\Users\chris\django\proyecto_1\empleado>python manage.py runserver

## 4 Aplicaciones

Las aplicaciones en django son pequeños proyectos completos. La idea es que:

### 4.1 cada una sea independiente de las otras con el objetivo de poder reutilizarlas si fuese necesario.\
### 4.2 cada una se dedique a un solo proceso de la lógica del negocio.

Crearemos las siguientes dos aplicaciones dentro de una nueva carpeta llamada applications en la cre creamos un archivo __init__.py:

![image](https://github.com/user-attachments/assets/8a4cacb5-da70-4e4d-8e39-453c3285dcfe)

![image](https://github.com/user-attachments/assets/7d58750c-5b20-4f68-bb78-36d88a9d2a6e)

### 4.3 Vamos al nivel de applications y creamos los dos nuevos proyectos:

(entorno_1) C:\Users\chris\django\proyecto_1\empleado\applications>django-admin startapp departamentos

(entorno_1) C:\Users\chris\django\proyecto_1\empleado\applications>django-admin startapp empleados

![image](https://github.com/user-attachments/assets/9c2631f9-fd41-4d16-8b0a-04f7eb2aba5f)

### 4.4 Ahora necesitamos instalar nuestras aplicaciones en el archivo base.py:

![image](https://github.com/user-attachments/assets/12f5e13b-8ccf-49c4-8952-04664108c281)

y en cada uno de los archivos apps.py de las aplicaciones departamentos y empleados anteponemos el prefijo applications:

![image](https://github.com/user-attachments/assets/472135fc-6133-4ecb-9a26-9cefb48c2180)

![image](https://github.com/user-attachments/assets/49b450f9-1d92-4f52-8bbe-ba4ee394f6d4)

### 4.5 Levantemos nuestro servidor para que veamos que todo est[e funcionando ok:

(entorno_1) C:\Users\chris\django\proyecto_1\empleado>python manage.py runserver

## 5 Vistas genericas Views

El modelo Vista-Template (MVT) de Django es una variación del clásico modelo Vista-Controlador (MVC). A continuación, te explico en qué consiste cada uno y sus diferencias clave:

Modelo Vista-Template (MVT) en Django

Modelo (**Model**):

Se encarga de la lógica de acceso a los datos y define la estructura de la base de datos. En Django, los modelos son clases de Python que se traducen en tablas de la base de datos.

Ejemplo: Definir un modelo Usuario con campos como nombre, email, y fecha_de_nacimiento.

Vista (**View**):

Contiene la lógica de negocio y controla qué datos se envían al usuario. Las vistas en Django son funciones o clases que reciben una solicitud HTTP, interactúan con el modelo si es necesario, y devuelven una respuesta HTTP.

Ejemplo: Una vista que recupera todos los usuarios de la base de datos y los envía a una plantilla para su visualización.

Plantilla (**Template**):

Es la capa de presentación que define cómo se muestran los datos al usuario. Las plantillas en Django son archivos HTML que pueden contener etiquetas de plantilla de Django para mostrar datos dinámicos.

Ejemplo: Un archivo HTML que muestra una lista de usuarios con sus nombres y correos electrónicos.

Diferencias con el Modelo Vista-Controlador (MVC)

Controlador (Controller) vs. Vista (View):

En el patrón MVC, el Controlador maneja la lógica de negocio y la interacción entre el modelo y la vista. En Django, esta función la realiza la Vista.
En MVC, la Vista es responsable solo de la presentación de los datos. En MVT, la Plantilla cumple esta función.
Terminología:
Aunque la funcionalidad es similar, la terminología difiere. En Django, lo que en MVC se llama Controlador se llama Vista, y lo que en MVC se llama Vista se llama Plantilla.
Flujo de Trabajo:
En MVC, el flujo típico es: Usuario → Controlador → Modelo → Vista → Usuario.
En MVT, el flujo es: Usuario → Vista → Modelo → Plantilla → Usuario.
Ejemplo Práctico
Supongamos que queremos mostrar una lista de productos en una tienda en línea:

Modelo (Model): Definimos un modelo Producto con campos como nombre, precio, y descripción.
Vista (View): Creamos una vista que recupera todos los productos de la base de datos y los pasa a una plantilla.
Plantilla (Template): Diseñamos un archivo HTML que muestra la lista de productos con sus nombres y precios.
En resumen, el patrón MVT de Django es una adaptación del patrón MVC, con una terminología y flujo de trabajo ligeramente diferentes, pero con el mismo objetivo de separar la lógica de negocio, la lógica de presentación y la interfaz de usuario12.

<span style="color:red">TemplateView</span>

<span style="color: red;">Este texto es rojo</span>
<span style="color: blue;">Este texto es azul</span>


