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
* [6 Haciendo una carpeta templates generalizada](#6-Haciendo-una-carpeta-templates-generalizada)

## 1 Crear un proyecto Django

(para limpiar la consola utilizamos el comando **cls**)

(para salir de la consola utilizamos el comando **CTRL+C**)

Para instalar Djaneiro en Visual Studio Code, sigue estos pasos:

Abre Visual Studio Code.
Accede a la barra de extensiones: Puedes hacerlo haciendo clic en el ícono de extensiones en la barra lateral izquierda o presionando Ctrl+Shift+X.
Busca “Djaneiro”: En la barra de búsqueda de extensiones, escribe “Djaneiro”.
Instala la extensión: Cuando encuentres “Djaneiro - Django Snippets”, haz clic en el botón de instalar1.
Reinicia Visual Studio Code: Para asegurarte de que la extensión se ha instalado correctamente, reinicia Visual Studio Code.

Para crear una estructura básica de HTML utilizando Djaneiro en Visual Studio Code, sigue estos pasos:

Abre un archivo HTML: Crea un nuevo archivo con la extensión .html o abre uno existente.
Escribe el snippet: Djaneiro proporciona varios snippets útiles. Para una estructura básica de HTML, puedes usar el snippet html5. Simplemente escribe html5 y presiona Tab.

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

### La teoría del patrón de diseño MVT

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

### La creación de una vista

51 Dentro de la aplicacion **empleado**, en la carpeta applications, construyamos una nueva aplicacion llamada **exp** donde realizaremos todas nuestras pruebas.

C:\Users\chris>cd \Users\chris\django\proyecto_1\entorno_1\Scripts\
C:\Users\chris\django\proyecto_1\entorno_1\Scripts>activate\
(entorno_1) C:\Users\chris\django\proyecto_1\entorno_1\Scripts>cd \Users\chris\django\proyecto_1\empleado\applications

(entorno_1) C:\Users\chris\django\proyecto_1\empleado\applications>django-admin startapp exp

52 Luego, en **base.py** agregamos la ruta de la aplicacion para instalarla.

'applications.exp',

53 Luego vamos a apps.py de la misma aplicación y agregamos la rura de la carpeta:

home: 'applications.exp'

![image](https://github.com/user-attachments/assets/348e7716-16b6-4032-8999-49d056411832)

54 Dentro de la carpeta exp agregamos una nueva llamada templates, donde alojaremos todos nuestros htmls.

55 En views.py de exp agregamos las siguientes lineas de codigo:

```
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'home.html'
```

56 En la carpeta templates creamos un archivo llamado home.html donde escribimos el siguiente código:

```
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

57 en urls.py agregamos una nueva ruta

```
from django.contrib import admin
from django.urls import path
from applications.exp.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view()),
]
```

58 ejecutemos nuevamente nuestro proyecto y vamos a la url home:

(entorno_1) C:\Users\chris\django\proyecto_1\empleado>python manage.py runserver

http://127.0.0.1:8000/home/

![image](https://github.com/user-attachments/assets/83b55f69-3637-4cd5-9376-86b368fd4198)
 
## 6 Haciendo una carpeta templates general para el proyecto

![image](https://github.com/user-attachments/assets/42daddf5-fdac-4407-af21-49194421d67d)

62 Borramos la carpeta templates de la carpeta exp

63 Hacemos las siguientes modificaciones en el archivo base.py:

![image](https://github.com/user-attachments/assets/75a7085a-d89e-4dbd-bc1c-bc980ae4c371)

y en la vista de nuestra carpeta experimental:

![image](https://github.com/user-attachments/assets/81afbe60-8bf1-4ceb-aa7b-1b80936d4ace)

Volvemos a cargar nuestro proyecto y vamos a la url home:

(entorno_1) C:\Users\chris\django\proyecto_1\empleado>python manage.py runserver

![image](https://github.com/user-attachments/assets/06fac228-4f8b-4efa-a323-fed2ef93da1f)

## 7 Haciendo una carpeta parcial para cada app

## 8 Vistas genéricas

Las vistas genéricas heredan de una clase padre llamada view y realizan las tareas del CRUD, las cuales podemos personalizar.

Son vistas basadas en clases. 

Todas necesitarán de un HTML para desplegar el proceso que realizan.




