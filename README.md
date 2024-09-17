# Django

[Vistas basadas en clases](https://github.com/sociologo/django/blob/main/Vistas%20basadas%20en%20clases.md)

https://docs.djangoproject.com/en/5.1/

Christian Castro

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
* [18 Vistas basadas en clases](#18-Vistas-basadas-en-clases)
  * [18_1_El método ListView](#18_1-El-método-ListView)
    * [18_1_1 Listar todos los empleados](#18_1_1-Listar-todos-los-empleados)


    * [18_1_2 Listar todos los empleados que pertenezcan a un area específica](#18_1_2-Listar-todos-los-empleados-que-pertenezcan-a-un-area-específica)
    * [18_1_3 Listar todos los empleados que pertenezcan a un area específica mediante urls con un filtro en una caja de texto](#18_1_3-Listar-todos-los-empleados-que-pertenezcan-a-un-area-específica-mediante-urls-con-un-filtro-en-una-caja-de-texto)
    * [18_1_4 Paginación en la vista ListView](#18_1_4-Paginación-en-la-vista-ListView)
    * [18_1_5 Listar las habilidades de un empleado](#18_1_5-Listar-las-habilidades-de-un-empleado)



   





  * [18.2 El método DetailView](#18_2-El-método-DetailView)





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





Cada aplicación, por buena práctica arquitectónica, debe poseer su propio archivo de urls, urls.py, par que en el archivo urls.py original, sólo importemos. Ésto es lo que vamos a crear en nuestra aplicación de ejercicio exp.

![image](https://github.com/user-attachments/assets/e4fbfa3c-b82b-437e-9a0f-c88ca61fdb87)

Ahora llamamos éste urls.py de exp desde nuestro archivo urls.py general importando el paquete include:

![image](https://github.com/user-attachments/assets/2bfcca87-970b-45b9-ad0d-2ff69d19bd82)

## 8 Vistas genéricas

Las vistas genéricas heredan de una clase padre llamada **view** y realizan las tareas del CRUD, las cuales podemos personalizar. Ejemplos son el **TemplateView**, **ListView**, etc. De ellas tambien heredamos.

Son vistas basadas en clases. 

Se pueden agregar las funciones extras que se deseen.

Todas necesitarán de un HTML para desplegar el proceso que realizan.

## 9 Nuestros primeros pasos en MVT

1 Creemos la vista basada en clases ListView y observemos su comportamiento en un pequeño ejemplo en viwes.py de nuestra aplicación exp. Creamos la clase **Prueba_ListView**:

![image](https://github.com/user-attachments/assets/6ac03929-825c-487c-b612-462449862e0b)

2 Agregamos al url en la aplicación exp:

![image](https://github.com/user-attachments/assets/f7b31011-cb1a-4c61-9a8c-f4dea81466fd)

3 construímos el archivo html correspondiente llamado **lista** con el context_object_name interpolado (dentro de dobles llaves):

![image](https://github.com/user-attachments/assets/78534cf5-e683-4398-ade3-82be1d4e9e95)

![image](https://github.com/user-attachments/assets/59feefbe-3edf-4e39-b6c0-9c7d68d708a6)

## 10 el ORM de Django y modelos

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

## 18 Vistas basadas en clases

[ccbv.co.uk](https://ccbv.co.uk)


### 18_1 El método ListView

[Documentacion ListView](https://docs.djangoproject.com/en/5.1/ref/class-based-views/generic-display/)

El método ListView en Django es una vista genérica basada en clases que se utiliza para mostrar una lista de objetos. Es especialmente útil cuando necesitas mostrar una lista de elementos de un modelo en una página web. 

Funcionalidades:

1 ListView se encarga de obtener una lista de objetos de un modelo y renderizarlos en una plantilla.\
2 Paginación: Puedes habilitar la paginación para dividir la lista de objetos en varias páginas.\
3 Proporciona un **contexto** a la plantilla que incluye la lista de objetos y otros datos adicionales.

Implementaremos cinco requerimientos de listado sobre nuestra aplicacion **empleados**.

#### 18_1_1 Listar todos los empleados.

En el archivo views.py de la aplicacion empleados debemos importar el metodo ListView, el modelo Empleado y construir la siguiente clase:

![image](https://github.com/user-attachments/assets/c00ff6d7-4740-419b-a78f-b908726f5410)

2 Debemos activar nuestra vista generica para lo cual vamos al archivo urls.py de la aplicacion empleado, importamos las views y declaramos la url: listar-todo-empleado/ y hacemos el llamado a la clase sobre la cual hemos basado nuestra vista:

![image](https://github.com/user-attachments/assets/99ea6f61-5869-4061-8a52-4f5b5e5ec22c)

3 La url recien declarada no la hemos activado en las urls principales de Django, para lo cual vamos al archivo urls.py de la aplicacion empleado (aca se puede producir una confusion. Esta aplicacion empleado, en singular es la que alberga por completo nuestro proyecto, la aplicacion el plural empleados, alberga la aplicacion del contexto especifico del modelo empleados)

![image](https://github.com/user-attachments/assets/12e21b13-ace2-4110-aeeb-0c63cc89d0f6)

4 Por ultimo debemos construir el archivo html dentro de una carpeta persona en la ruta de los templates:

![image](https://github.com/user-attachments/assets/745c0f3d-d44e-4fe7-83f3-ae3c87d51b93)

Iteracion sobre registros de modelos para listarlos

```
<ul>
 {% for e in object_list %}
  <li>{{ e }}</li>
 {% endfor %}
</ul>
```

5 Y ejecutemos nuestro proyecto:

![image](https://github.com/user-attachments/assets/e189374d-2287-4d73-8a4a-78c12135ebec)

#### 18_1_2 Listar todos los empleados que pertenezcan a un area específica

Solo con fines pedagogicos haremos esto de forma bruta.

1 En **views.py** de la aplicacion empleado:

```
from django.shortcuts import render # type: ignore

from django.views.generic import( # type: ignore
    ListView
)

from .models import Empleado

# 1 Listar todos los empleados de la empresa

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    context_object_name = 'lista'

# 2 Listar todos los empleados de la empresa por departamento

class ListAllByDept(ListView):
    template_name = 'persona/AllByDept.html'
    queryset = Empleado.objects.filter(
        departamento__short_name = 'ciencias matemáticas'
    )
```

2 En **urls.py** de la aplicacion empleado:

```
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-por-area/', views.ListAllByDept.as_view()),
]
```

3 En la carpeta persona que esta en la carpeta templates anadimos list.html:

```
<h1>
    lista de todos los empleados
</h1>

<ul>
    {% for e in object_list %}
        <li>{{ e }}</li>
    {% endfor %}
</ul>
```

4 y obtenemos:

![image](https://github.com/user-attachments/assets/8d1bc43b-d62c-4740-8374-366c4883c6df)

#### 18_1_3 Listar todos los empleados que pertenezcan a un area específica mediante urls con un filtro en una caja de texto

1 Debemos utilizar el metodo **get_queryset** para recoger un parametro desde la url.
Es entonces que debemos agregar a la url lista-by-area/ un elemento de la siguiente manera:
lista-by-area<shortname>/

2 **kwards** es un metodo de Django que nos permite recoger elementos desde las urls, y con el que tomamos el elemento <shotname>.

3 Necesitamos una caja de texto html para que el usuario pueda definir su busqueda a listar.

4 Es importante no olvidar la clave de acceso {% csrf_token %}

Entonces:

a) Construimos el metodo dentro de una clase en la vista de empleados:
```
class ListEmpByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
        first_name = palabra_clave
        )
        return lista
```
b Creamos la url en la aplicacion empleados:
```

from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-por-area/', views.ListAllByDept.as_view()),
    path('buscar-emp-por-kword/', views.ListEmpByKword.as_view()),
]

```
c en la carpeta persona de templates templates construimos **by_kword.html** para la caja de texto
```
<h1>
    Buscar empleados por kword
</h1>
<form method="GET">{% csrf_token %}
    <input type="text" id="kword" name="kword" placeholder="Ingresa nombre">
    <button type="submit"> Buscar </button>
</form>
<h3>
    Lista resultado
</h3>
<ul>
    {% for e in empleados %}
        <li>{{ e }}</li>
    {% endfor %}
</ul>
```
![image](https://github.com/user-attachments/assets/a4ab7983-78e4-4734-9a66-73a54df63b65)

Nuestro resultado de busqueda para carlos es:

![image](https://github.com/user-attachments/assets/8d7961c8-446c-43b4-94d1-5a11a449c22e)

![image](https://github.com/user-attachments/assets/64449aba-4f81-4cdd-8a77-2acf0354db58)

#### 18_1_4 Paginación en la vista ListView

La paginación es crucial al listar registros en Django por varias razones:

Rendimiento: Cargar todos los registros de una base de datos grande en una sola página puede ser muy lento y consumir muchos recursos del servidor. La paginación permite dividir los datos en partes más manejables, mejorando el rendimiento de la aplicación.\
Usabilidad: Presentar demasiados datos en una sola página puede ser abrumador para los usuarios. La paginación facilita la navegación y hace que la interfaz sea más amigable y fácil de usar.\
Carga de Red: Al limitar la cantidad de datos enviados al cliente en cada solicitud, se reduce la carga de red, lo que puede ser especialmente importante en aplicaciones con muchos usuarios concurrentes.\
Experiencia del Usuario: La paginación permite a los usuarios encontrar y acceder a la información de manera más eficiente, mejorando su experiencia general en la aplicación.

![image](https://github.com/user-attachments/assets/aef71236-1754-455c-8fd3-331fc236c8f2)

```
# 1 Listar todos los empleados de la empresa

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    paginate_by = 3
    context_object_name = 'lista'
```

![image](https://github.com/user-attachments/assets/0ff4e393-7b66-4e87-8088-f120f5738bb6)

![image](https://github.com/user-attachments/assets/68daa866-cc3a-4091-96ca-033581bf5548)

Tambien podemos establecer un orden al listado.

```
# 1 Listar todos los empleados de la empresa

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    paginate_by = 3
    ordering = 'first_name'
    context_object_name = 'lista'
```

![image](https://github.com/user-attachments/assets/e1c86f92-88d3-42b1-b6c2-c2e99dd5b442)

#### 18_1_5 Listar las habilidades de un empleado

Recordemos que habilidades con empleados es una relacion de muchos a muchos.

1 Hacemos que en el listado de empleados del administrador de django se visualice el id de cada registro.

![image](https://github.com/user-attachments/assets/6fe81643-d81f-4e36-8829-ddf6482ed0d9)

![image](https://github.com/user-attachments/assets/ee1f9c05-795f-4beb-bab3-6a88c1839d12)





a) Construimos el metodo dentro de una clase en la vista de empleados:
```
class ListEmpByHabili(ListView):
    template_name = 'persona/by_habili.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("habili", '')
        lista = Empleado.objects.filter(
        first_name = palabra_clave
        )
        return lista
```
b Creamos la url en la aplicacion empleados:
```

from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

from . import views

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-por-area/', views.ListAllByDept.as_view()),
    path('buscar-emp-por-kword/', views.ListEmpByKword.as_view()),
    path('buscar-emp-por-habili/', views.ListEmpByHabili.as_view()),
]

```
c en la carpeta persona de templates templates construimos **by_habili.html** para la caja de texto
```
<h1>
    Buscar empleados por Habilidad
</h1>
<form method="GET">{% csrf_token %}
    <input type="text" id="habili" name="habili" placeholder="Ingresa Habilidad">
    <button type="submit"> Buscar </button>
</form>
<h3>
    Lista resultado
</h3>
<ul>
    {% for e in empleados %}
        <li>{{ e }}</li>
    {% endfor %}
</ul>
```


### 18_2 El método DetailView


































