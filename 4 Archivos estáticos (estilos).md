# Archivos estáticos.

[Fundation framework](https://get.foundation/sites/getting-started.html)

## Índice

* [1 Configurar Django para la lectura de archivos estaticos](#1-Configurar-Django-para-la-lectura-de-archivos-estaticos)
* [2 Implementando Includes](#2-Implementando-Includes)

## 1 Configurar Django para la lectura de archivos estaticos.

1 Vamos a [Fundation Zurb](https://get.foundation/sites/docs/installation.html)* y descargamos las carpetas **css** y **js**.

![image](https://github.com/user-attachments/assets/ad9a1f63-77cc-4621-b8c8-d99491a2b1b4)

2 En nuestro proyecto creamos una carpeta donde alojaremos los archivos estáticos llamado **static**, y dentro de ella las carpetas **css**, **img** y **js**. Copiamos en ellos, los archivos de **css** y **js**

![image](https://github.com/user-attachments/assets/9b67f6b7-b55a-46cf-b51c-77fd1faf7ab3)

3 Vamos a las configuraciones de nuestro proyecto ubicadas en **local.py** dentro de **settings** y declaramos la variable **STATICFILES_DIRS**. Es de fundamental importancia declarar bien la variable **STATICFILES_DIRS** para que nuestro javascript funcione.

```python
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

STATICFILES_DIRS = [
   BASE_DIR / "static",
]
```

\* Foundation es un conjunto de frameworks front-end responsivos desarrollados originalmente por ZURB. Está diseñado para facilitar la creación de sitios web, aplicaciones y correos electrónicos que se vean bien en cualquier dispositivo. Foundation for Sites proporciona HTML, CSS y JavaScript para ayudarte a prototipar rápidamente y construir sitios web centrados en el contenido. Es fácil de personalizar y extender
