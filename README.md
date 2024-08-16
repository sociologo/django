# Django

This document covers the basic usage patterns and concepts across Marionette.
This includes things like calling conventions, setting attributes, common option
patterns etc.

## Índice

* [1 Crear un proyecto Django](#1-crear-un-proyecto-django)
  * [1.1 Creemos una carpeta donde vamos a alojar todo nuestro trabajo](#1.1-Creemos-una-carpeta-donde-vamos-a-alojar-todo-nuestro-trabajo)
* [2 Configurar la estructura de un proyecto en django](#2-Configurar-la-estructura-de-un-proyecto-en-django)
* [3 Ejecutando el archivo localpy en vez del original settingspy](#3-Ejecutando-el-archivo-localpy-en-vez-del-original-settingspy)
* [4 Aplicaciones](#4-Aplicaciones)

* [Using ES6 Modules](#using-es6-modules)
* [Class-based Inheritance](#class-based-inheritance)
  * [Value Attributes](#value-attributes)
  * [Functions Returning Values](#functions-returning-values)
  * [Binding Attributes on Instantiation](#binding-attributes-on-instantiation)
* [Common Marionette Functionality](./common.md)

## 1 Crear un proyecto Django

(para limpiar la consola utilizamos el comando **cls**)
(para salir de la consola utilizamos el comando **CTRL+C**)

### 1.1 Creemos una carpeta donde vamos a alojar todo nuestro trabajo:
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





