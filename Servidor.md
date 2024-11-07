# Cómo configurar Django con Postgres, Nginx y Gunicorn en Ubuntu.

## 1 Acerca de root

Podemos acceder a un droplet de **DigitalOcean** desde una terminal windows local ejecutada como administrador con:

```
C:\Windows\System32>ssh root@xxx.xx.xxx.x
password: xxxxxxxx
root@django:~# exit
```

El usuario **root** es el usuario administrativo con privilegios elevados en un entorno Linux. Debido a ello, se desaconseja su uso habitual. La cuenta root puede realizar cambios muy destructivos, incluso por accidente. Por ello debemos configurar una nueva cuenta de usuario con privilegios reducidos para el uso diario. 

## 2 Crear un nuevo usuario

Una vez que inicies sesión como root, podrás agregar la nueva cuenta de usuario. En el futuro, iniciaremos sesión con esta nueva cuenta en lugar de **root**.

Crearemos un nuevo usuario llamado christian:
```
adduser christian
contraseña: 123456
```

Si queremos cambiar la contraseña de un usuario:
```
sudo passwd christian
```

## 3 Concesión de privilegios administrativos

Ahora tienes una nueva cuenta de usuario con privilegios de cuenta normales. Sin embargo, a veces tendrás que realizar tareas administrativas como usuario **root**.

Para evitar cerrar la sesión de su usuario habitual y volver a iniciarla como cuenta raíz, puedes configurar lo que se conoce como privilegios de superusuario o root para la cuenta habitual de su usuario. Estos privilegios le permitirán a tu usuario normal ejecutar comandos con privilegios administrativos colocando la palabra **sudo** antes.

Para agregar estos privilegios a su nuevo usuario, deberás agregarlo al grupo del sistema sudo. De manera predeterminada, en Ubuntu, los usuarios que son miembros del grupo sudo pueden usar el comando **sudo**.

Como root, ejecuta este comando para agregar tu nuevo usuario al grupo sudo:
```
usermod -aG sudo christian
```
Ahora puedes escribir sudo antes los comandos para ejecutarlos con privilegios de superusuario cuando inicias sesión como tu usuario habitual.

## 4 Configuración de un firewall

Los servidores Ubuntu pueden usar el firewall UFW (Uncomplicated Firewall) para garantizar que solo se permitan conexiones a determinados servicios. Puedes configurar un firewall básico con esta aplicación.

Las aplicaciones pueden registrar sus perfiles en UFW durante la instalación. Estos perfiles permiten que UFW administre estas aplicaciones por nombre. OpenSSH, el servicio que le permite conectarse a su servidor, tiene un perfil registrado en UFW.

Puedes examinar la lista de perfiles UFW instalados escribiendo:
```
ufw app list
```
Deberás asegurarte de que el firewall permita conexiones SSH para poder iniciar sesión en su servidor la próxima vez. Permite estas conexiones escribiendo:
```
ufw allow OpenSSH
```
Ahora habilita el firewall escribiendo:
```
ufw enable
```
Puedes ver que las conexiones SSH aún están permitidas si escribes:
```
ufw status
```
Actualmente, el firewall está bloqueando todas las conexiones excepto SSH. Si instalas y configuras servicios adicionales, deberás ajustar la configuración del firewall para permitir el nuevo tráfico en tu servidor.

## 5 Habilitar el acceso externo para el usuario habitual

Ahora que tienes un usuario regular para uso diario, deberás asegurarte de poder acceder a la cuenta mediante SSH directamente.

Hasta verificar que puede iniciar sesión y usar sudo su nuevo usuario, es recomendable permanecer conectado como root. Si tienes problemas para conectarte, puedes solucionar problemas y realizar los cambios necesarios como root. 

La configuración del acceso SSH para su nuevo usuario depende de si la cuenta raíz de su servidor utiliza una contraseña o claves SSH para la autenticación.

### Si la cuenta raíz utiliza autenticación con contraseña

Si iniciaste sesión en tu cuenta raíz con una contraseña, la autenticación con contraseña estará habilitada para SSH. Puedes iniciar sesión con SSH en su nueva cuenta de usuario abriendo una nueva sesión de terminal y usando SSH con tu nuevo nombre de usuario:
```
C:\Windows\System32>ssh christian@xxx.xx.xxx.x
contraseña: xxxxxxxxxx
```

Recibirás una solicitud para su contraseña de usuario habitual sudola primera vez que utilice cada sesión (y periódicamente después).

Después de ingresar tu contraseña de usuario habitual, iniciarás sesión. Recuerda, si necesitas ejecutar un comando con privilegios administrativos, escribe sudo antes de hacerlo de la siguiente manera:
```
sudo comando
```

**Para mejorar la seguridad de su servidor, es recomendable configurar claves SSH en lugar de usar autenticación con contraseña.**

Ahora estamos como:
```
christian@django:~$
```

## 6 Instalación de paquetes necesarios desde los repositorios de Ubuntu
```
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```

## 7 Creación de la base de datos y el usuario de PostgreSQL

- Inicia sesión en una sesión interactiva de Postgres escribiendo:
```
christian@django:~$ sudo -u postgres psql
```

- Crea una base de datos para tu proyecto:
```
postgres=# CREATE DATABASE bded5;
```

- Crea un usuario de base de datos para nuestro proyecto. Asegúrate de seleccionar una contraseña segura:
```
postgres=# CREATE USER christian WITH PASSWORD '123456';
```

- Modifica algunos de los parámetros de conexión del usuario que acabas de crear.
```
postgres=# ALTER ROLE christian SET client_encoding TO 'utf8';
postgres=# ALTER ROLE christian SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE christian SET timezone TO 'UTC';
```

- Dale al nuevo usuario acceso para administrar la nueva base de datos:
```
postgres=# GRANT USAGE, CREATE ON SCHEMA public TO christian;
postgres=# ALTER USER christian WITH SUPERUSER;
postgres=# GRANT ALL PRIVILEGES ON DATABASE bded5 TO christian;
```

- Sale del prompt de PostgreSQL escribiendo:
```
postgres=# \q
```

## 8 Creación de un entorno virtual de Python para su proyecto

```
christian@django:~$ mkdir proyecto_5
christian@django:~$ cd /proyecto_5
```

Puede que el fichero **proyecto_5** quede ubicado en el directorio raiz del sistema en vez del directorio de inicio de usuario. Si es así debemos preceder al comando con una barra:

```
christian@django:~$ ls /
christian@django:~$ cd /proyecto_5
christian@django:/proyecto_5$
```

Creamos y activamos el entorno virtual
```
christian@django:/proyecto_5$ python3 -m venv env3
christian@django:/proyecto_5$ source env5/bin/activate
```

Debe aparecer lo siguiente:
```
(env5) christian@django:/proyecto_5$ 
```

## 9 Clonar nuestro proyecto desde GitHub a nuestro servidor

```python
(env5) christian@django:/proyecto_5$ sudo git clone https://github.com/sociologo/django.git
(env5) christian@django:/proyecto_5$ ls
django  env5
(env5) christian@django:/proyecto_5$ 
```

![git](https://github.com/user-attachments/assets/70a62360-3e03-429e-83a5-c751f8667241)


## 10 Configuracion del archivo settings.py

```python
(env5) christian@django:/proyecto_5$ sudo nano django/django/proyecto_1/empleado/empleado/settings/local.py
```

```bash
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['164.92.107.9', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bded5',
        'USER ': 'christian',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / ("media")
```

> ES MUY IMPORTANTE QUE EL **USER** DE LA BASE DE DATOS SEA EL MISMO QUE EL **NOMBRE DEL USUARIO** LINUX CON EL QUE ESTAS TRABAJANDO. SI NO, NO TE PODRAS CONECTAR!

## 11 Haciendo las migraciones y arrancando el servidor proyecto:

```
(env5) christian@django:/proyecto_5$ python3 manage.py makemigrations
(env5) christian@django:/proyecto_5$ python3 manage.py migrate
```

Crea una excepción para el puerto 8000 escribiendo:
```
sudo ufw allow 8000
```
Para matar el proceso asociado al puerto 8000:
```
sudo fuser -k 8000/tcp
```
Arrancamos el proyecto. Asegúrate de que estás en el directorio correcto donde se encuentra manage.py.
```
(env5) christian@django:/proyecto_5$ cd django/django/proyecto_1/empleado
(env5) christian@django:/proyecto_5/django/django/proyecto_1/empleado$ python3 manage.py runserver 0.0.0.0:8000
```

## 12 Super usuario para nuestro proyecto.
```
(env5) christian@django:/proyecto_5$ python3 manage.py createsuperuser
Username (leave blank to use 'christian'):
Email address: tarredwall@gmail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## 13 Manteniendo arriba el servidor usando tmux:

- Instala tmux:
```
christian@django:/$ cd /proyecto_5
christian@django:/proyecto_5$ source env5/bin/activate
(env5) christian@django:/proyecto_5$ cd django/django/proyecto_1/empleado
(env5) christian@django:/proyecto_5/django/django/proyecto_1/empleado$ sudo apt install tmux
```
- Inicia una nueva sesión de tmux:
```
(env5) christian@django:/proyecto_5/django/django/proyecto_1/empleado$ tmux new -s mi_sesion
```
- Inicia tu servidor Django dentro de la sesión de tmux:
```
christian@django:/proyecto_5/django/django/proyecto_1/empleado$ python3 manage.py runserver 164.92.107.9:8000
```

- El proyecto esta levantado en **http://164.92.107.9:8000/**
- Desconéctate de la sesión de tmux sin detener el servidor presionando Ctrl + B seguido de D.
- Puedes cerrar simplemente tu sesion tmux.

Para ingresar a una sesión de tmux ya existente, puedes usar el comando tmux attach:

Listar las sesiones de tmux para ver las sesiones activas:
```
(env5) christian@django:/proyecto_5/django/django/proyecto_1/empleado$ tmux ls
```
Ingresar a la sesión de tmux usando el nombre o el número de identificación de la sesión. Por ejemplo, si la sesión se llama mi_sesion, usa el siguiente comando:
```
(env5) christian@django:/proyecto_5/django/django/proyecto_1/empleado$ tmux attach -t mi_sesion
```


Para cerrar tu sesión de tmux y detener cualquier proceso que esté ejecutándose en ella:
```
christian@django:~$ ps aux | grep runserver
christian@django:~$ kill 136730
```

<br>
***

How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu

Initial Server Setup with Ubuntu

https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu

## 14 Instalar **nginex** y **gunicorn**:

Nginx y Gunicorn son herramientas esenciales para desplegar aplicaciones web en producción, especialmente cuando se trata de aplicaciones basadas en Python como Django o Flask. Son herramientas que solo utilizamos en produccion.

*Nginx*

Nginx es un servidor web y proxy inverso de alto rendimiento. Sus principales funciones incluyen:

- Servir contenido estático: Nginx es muy eficiente para servir archivos estáticos como imágenes, CSS y JavaScript.

- Proxy inverso: Actúa como intermediario entre los clientes y el servidor de aplicaciones, manejando las solicitudes entrantes y distribuyéndolas a los servidores de aplicaciones.

- Balanceo de carga: Distribuye el tráfico entre varios servidores de aplicaciones para mejorar el rendimiento y la disponibilidad.

- Seguridad: Proporciona características de seguridad como la limitación de la tasa de solicitudes y la protección contra ataques DDoS.

*Gunicorn*

Gunicorn (Green Unicorn) es un servidor de aplicaciones WSGI (Web Server Gateway Interface) para aplicaciones Python. Sus principales funciones incluyen:

- Manejo de solicitudes: Gunicorn se encarga de recibir las solicitudes HTTP y pasarlas a la aplicación Python para su procesamiento.

- Multiprocesamiento: Puede manejar múltiples solicitudes simultáneamente utilizando múltiples trabajadores, lo que mejora el rendimiento de la aplicación.

- Compatibilidad: Es compatible con cualquier aplicación que siga la especificación WSGI, lo que lo hace ideal para aplicaciones Django y Flask.

Nginx y Gunicorn se complementan muy bien debido a sus respectivas fortalezas:

-Separación de responsabilidades: Nginx maneja las solicitudes HTTP, el contenido estático y la seguridad, mientras que Gunicorn se enfoca en ejecutar la aplicación Python y manejar las solicitudes dinámicas.

-Rendimiento: Nginx puede manejar una gran cantidad de conexiones simultáneas y distribuirlas eficientemente a Gunicorn, que a su vez puede manejar múltiples solicitudes concurrentes.

-Escalabilidad: Esta combinación permite escalar la aplicación fácilmente, añadiendo más instancias de Gunicorn detrás de Nginx para manejar un mayor tráfico.

-Seguridad: Nginx actúa como una capa de seguridad adicional, protegiendo la aplicación de ataques directos y manejando la terminación de SSL/TLS.

En resumen, Nginx y Gunicorn forman un equipo poderoso para desplegar aplicaciones web en producción, combinando eficiencia, rendimiento y seguridad.

```
(env5) christian@django:/proyecto_5/django/django/proyecto_1/empleado$ sudo apt install nginx
(env5) christian@django:/proyecto_5/django/django/proyecto_1/empleado$ pip install gunicorn
```
```
(env5) christian@django:/$  cd /proyecto_5
(env5) christian@django:/proyecto_5$  source env5/bin/activate
(env5) christian@django:/proyecto_5$ ls
django  env5
(env5) christian@django:/proyecto_5$ cd env5
(env5) christian@django:/proyecto_5/env5$ ls
bin  include  lib  lib64  pyvenv.cfg
(env5) christian@django:/proyecto_5/env5$ cd bin
(env5) christian@django:/proyecto_5/env5/bin$ ls
Activate.ps1  activate.csh   django-admin  pip   pip3.12  python3     sqlformat
activate      activate.fish  gunicorn      pip3  python   python3.12
(env5) christian@django:/proyecto_5/env5/bin$
```

Necesitamos configurar un archivo **gunicorn_start**. El archivo gunicorn_start es un script de inicio personalizado que se utiliza para configurar y ejecutar Gunicorn, el *servidor de aplicaciones* WSGI para aplicaciones Python. Este archivo es especialmente útil cuando deseas automatizar y estandarizar el proceso de inicio de Gunicorn en un entorno de producción. Aquí tienes algunas razones por las que podrías querer crear un archivo gunicorn_start:

- Automatización: Facilita el proceso de inicio de Gunicorn, asegurando que siempre se ejecute con los mismos parámetros y configuraciones.

- Configuración personalizada: Permite especificar configuraciones personalizadas, como el número de trabajadores, el puerto, el entorno virtual, y otros parámetros específicos de Gunicorn.

- Facilidad de uso: Simplifica el comando de inicio, permitiendo que los administradores del sistema o los scripts de despliegue ejecuten Gunicorn con un solo comando.

- Mantenimiento: Centraliza la configuración de Gunicorn en un solo archivo, lo que facilita el mantenimiento y las actualizaciones.

```
(env5) christian@django:/proyecto_5/env5/bin$ touch gunicorn_start
(env5) christian@django:/proyecto_5/env5/bin$ nano gunicorn_start
```

```bash
#!/bin/bash

NAME="empleado"                                  # Name of the application
DJANGODIR=/proyecto_5/django/django/proyecto_1/empleado           # Django project directory
SOCKFILE=/proyecto_5/django/django/proyecto_1/run/gunicorn.sock  # we will communicte using this unix socket
USER=christian                                        # the user to run as
GROUP=christian                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=empleado.settings.prod             # which settings file should Django use
DJANGO_WSGI_MODULE=empleado.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /proyecto_5/env5/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /proyecto_5/env5/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
```

Le damos permisos de lectura a **gunicorn_start**:

```
(env5) christian@django:/proyecto_5/env5/bin$ chmod u+x gunicorn_start
```
Ahora le entregamos contenido al archivo **prod.py**

```bash
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['164.92.107.9', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bded5',
        'USER ': 'christian',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / ("media")
```

actualizamos nuestro repositorio a GitHub y lo clonamos a nuestro servidor:

```
christian@django:/$ cd /proyecto_5
christian@django:/proyecto_5$ cd django
christian@django:/proyecto_5/django$ git remote -v
origin  https://github.com/sociologo/django.git (fetch)
origin  https://github.com/sociologo/django.git (push)
christian@django:/proyecto_5/django$
```



<br>
***

# Levantando nuestro nuestro proyecto.

- Iniciamos nuestra terminal en windows como administrador:
```
C:\Windows\System32>ssh christian@xxx.xx.xxx.x
password: xxxxxx
```
- Activamos el entorno virtual accediendo a las rutas adecuadas y levantamos el servicio:
```
christian@django:/$ cd /proyecto_5
christian@django:/proyecto_5$ source env5/bin/activate
(env5) christian@django:/proyecto_5$ cd django/django/proyecto_1/empleado
(env5) christian@django:/proyecto_5/django/django/proyecto_1/empleado$ python3 manage.py runserver 0.0.0.0:8000
```
- Vamos a un navegador:
```
http://164.92.107.9:8000/
```





