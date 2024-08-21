# Django

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

# 13 Instalación de PostgreSQL

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































