# Cómo configurar Django con Postgres, Nginx y Gunicorn en Ubuntu.

## 1 Acerca de root

Podemos acceder a un droplet de **DigitalOcean** desde una terminal windows local ejecutada como administrador con:

```
C:\Windows\System32>ssh root@xxx.xx.xxx.x
password: xxxxxxxxxx
root@django:~#
```
donde xxx.xx.xxx.x es la IP asociada a tu droplet por DigitalOcean.

El usuario **root** es el usuario administrativo con privilegios elevados en un entorno Linux. Debido a ello, se desaconseja su uso habitual. La cuenta root puede realizar cambios muy destructivos, incluso por accidente. Por ello debemos configurar una nueva cuenta de usuario con privilegios reducidos para el uso diario. 

## 2 Crear un nuevo usuario

Una vez que inicies sesión como root, podrás agregar una nueva cuenta de usuario. En el futuro, iniciaremos sesión con esta nueva cuenta en lugar de **root**.

Crearemos un nuevo usuario llamado christian1:
```
root@django:~# adduser christian1
info: Adding user `christian1' ...
info: Selecting UID/GID from range 1000 to 59999 ...
info: Adding new group `christian1' (1001) ...
info: Adding new user `christian1' (1001) with group `christian1 (1001)' ...
info: Creating home directory `/home/christian1' ...
info: Copying files from `/etc/skel' ...
New password:
Retype new password:
passwd: password updated successfully
Changing the user information for christian1
Enter the new value, or press ENTER for the default
        Full Name []:
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n] Y
info: Adding new user `christian1' to supplemental / extra groups `users' ...
info: Adding user `christian1' to group `users' ...
root@django:~#
```
Si queremos cambiar la contraseña de un usuario:
```
sudo passwd christian1
```

## 3 Configurar la cuenta de usuario linux.

Ahora tienes una nueva cuenta de usuario con privilegios de cuenta normales. Sin embargo, a veces tendrás que realizar tareas administrativas como usuario **root**.

Para evitar cerrar la sesión de su usuario habitual y volver a iniciarla como cuenta raíz, puedes configurar lo que se conoce como privilegios de superusuario o root para la cuenta habitual de su usuario. Estos privilegios le permitirán a tu usuario normal ejecutar comandos con privilegios administrativos colocando la palabra **sudo** antes.

Para agregar estos privilegios a su nuevo usuario, deberás agregarlo al grupo del sistema sudo. De manera predeterminada, en Ubuntu, los usuarios que son miembros del grupo sudo pueden usar el comando **sudo**.

Como root, ejecuta este comando para agregar tu nuevo usuario al grupo sudo:
```
root@django:~# usermod -aG sudo christian1
```
Ahora puedes escribir **sudo** antes de los comandos para ejecutarlos con privilegios de superusuario cuando inicias sesión como usuario.

Ahora cierra la terminal y accede como christian1.
```
root@django:~# exit
logout
Connection to xxx.xx.xxx.x closed.
```
```
C:\Windows\System32>ssh christian1@xxx.xx.xxx.x
christian1@164.92.107.9's password:
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-47-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Fri Nov  8 17:24:29 UTC 2024

  System load:  0.01               Processes:             131
  Usage of /:   19.1% of 23.17GB   Users logged in:       1
  Memory usage: 53%                IPv4 address for eth0: xxx.xx.xxx.x
  Swap usage:   0%                 IPv4 address for eth0: xx.xx.x.x

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


*** System restart required ***

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

christian1@django:~$
```
Ahora estamos como:
```
christian@django:~$
```
Nota algo importante. El carácter final del prompt es un símbolo dolar, lo que indica que eres un usuario y no el root, el que termina con un signo gato: root@django:~#

## 4 Configuración de un firewall

Los servidores Ubuntu pueden usar el firewall UFW (Uncomplicated Firewall) para garantizar que solo se permitan conexiones a determinados servicios. Puedes configurar un firewall básico con esta aplicación.

Las aplicaciones pueden registrar sus perfiles en UFW durante la instalación. Estos perfiles permiten que UFW administre estas aplicaciones por nombre. OpenSSH, el servicio que te permite conectarte a tu servidor, tiene un perfil registrado en UFW.

Puedes examinar la lista de perfiles UFW instalados con:
```
christian1@django:~$ sudo ufw app list
[sudo] password for christian1:
Available applications:
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
christian1@django:~$
```
Deberás asegurarte de que el firewall permita conexiones SSH para poder iniciar sesión en su servidor la próxima vez. Permite estas conexiones escribiendo:
```
christian1@django:~$ sudo  ufw allow OpenSSH
Skipping adding existing rule
Skipping adding existing rule (v6)
christian1@django:~$
```
Ahora habilita el firewall escribiendo:
```
christian1@django:~$  sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
christian1@django:~$
```
Puedes ver que las conexiones SSH aún están permitidas si escribes:
```
christian1@django:~$  sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
8000                       ALLOW       Anywhere
5432                       ALLOW       Anywhere
OpenSSH                    ALLOW       Anywhere
8000 (v6)                  ALLOW       Anywhere (v6)
5432 (v6)                  ALLOW       Anywhere (v6)
OpenSSH (v6)               ALLOW       Anywhere (v6)

christian1@django:~$
```
Actualmente, el firewall está bloqueando todas las conexiones excepto SSH. Si instalas y configuras servicios adicionales, deberás ajustar la configuración del firewall para permitir el nuevo tráfico en tu servidor.

**Para mejorar la seguridad de su servidor, es recomendable configurar claves SSH en lugar de usar autenticación con contraseña.**

## 5 Creación de la base de datos y el usuario de PostgreSQL

- Inicia sesión en una sesión interactiva de Postgres escribiendo:
```
christian1@django:~$ sudo -u postgres psql
```

- Crea una base de datos para tu proyecto:
```
postgres=# CREATE DATABASE bded6;
CREATE DATABASE
postgres=#
```

- Crea un usuario de base de datos para nuestro proyecto. Asegúrate de seleccionar una contraseña segura:
```
postgres=#  CREATE USER christian1 WITH PASSWORD '123456';
CREATE ROLE
postgres=#
```

- Modifica algunos de los parámetros de conexión del usuario que acabas de crear.
```
postgres=# ALTER ROLE christian1 SET client_encoding TO 'utf8';
postgres=# ALTER ROLE christian1 SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE christian1 SET timezone TO 'UTC';
```

- Dale al nuevo usuario acceso para administrar la nueva base de datos:
```
postgres=# GRANT USAGE, CREATE ON SCHEMA public TO christian1;
postgres=# ALTER USER christian1 WITH SUPERUSER;
postgres=# GRANT ALL PRIVILEGES ON DATABASE bded5 TO christian1;
```

- Sale del prompt de PostgreSQL escribiendo:
```
postgres=# \q
```


## 6 Organización de ficheros y entornos virtuales

6.1 Creamos una carpeta donde almacenaremos todos nuestros proyectos llamada **mis_proyectos**, utilizando
**sudo** para ejecutar el comando **mkdir** con permisos de superusuario que crea un nuevo directorio llamado **mis_proyectos** en el directorio raíz (/).
```
christian1@django:~$ sudo mkdir /mis_proyectos
[sudo] password for christian1:
christian1@django:~$
```

Veamos lo que hay en el directorio raiz:
```
christian1@django:~$ cd /
christian1@django:/$ ls
bin                lib                mnt         root                sys
bin.usr-is-merged  lib.usr-is-merged  opt         run                 tmp
boot               lib64              proc        sbin                usr
dev                lost+found         proyecto_1  sbin.usr-is-merged  var
etc                media              proyecto_4  snap                webapps
home               mis_proyectos      proyecto_5  srv
christian1@django:/$
```
Observemos que hemos salido del directorio de nuestro usuario christian1 **(~)** y hemos entrado al directorio raíz **(/)**.

6.2 Creamos un entorno virtual dentro del fichero **mis_proyectos**
```
christian1@django:/$ cd /mis_proyectos
christian1@django:/mis_proyectos$ sudo python3 -m venv entorno_1
christian1@django:/mis_proyectos$
```

6.3 Clonar Git
Iremos a la carpeta que se ha creado con el entorno virtual y dentro de ella clonaremos nuestro repositorio Git.
```
christian1@django:/mis_proyectos$ ls
entorno_1
christian1@django:/mis_proyectos$ cd entorno_1
christian1@django:/mis_proyectos/entorno_1$ sudo git clone https://github.com/sociologo/emp1.git
Cloning into 'emp1'...
Username for 'https://github.com': sociologo
Password for 'https://sociologo@github.com':
remote: Enumerating objects: 153, done.
remote: Counting objects: 100% (153/153), done.
remote: Compressing objects: 100% (113/113), done.
remote: Total 153 (delta 36), reused 153 (delta 36), pack-reused 0 (from 0)
Receiving objects: 100% (153/153), 939.05 KiB | 8.03 MiB/s, done.
Resolving deltas: 100% (36/36), done.
christian1@django:/mis_proyectos/entorno_1$
```














## 6 Instalación de paquetes necesarios desde los repositorios de Ubuntu
```
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
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


https://github.com/settings/tokens

**IMPORTANTE: GITHUB VIA SHH YA NO ACEPTA CREDENCIALES PASSWORD, SINO QUE NECESITARAS UN TOKEN **
![token2](https://github.com/user-attachments/assets/13d02687-8652-4663-bf74-5d11f65bb13c)

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

Queda asi:
```
(env5) christian@django:/proyecto_5/env5/bin$ gunicorn_start
```
![image](https://github.com/user-attachments/assets/e6bd7d75-3c40-4f5c-a0c8-01938b5a0146)

## 15 Supervisor

Supervisor y Gunicorn son dos herramientas que se utilizan comúnmente juntas para desplegar aplicaciones web en producción.

- Gunicorn es un servidor WSGI para aplicaciones web Python. Se utiliza para ejecutar aplicaciones web Django, Flask y otras aplicaciones WSGI.

Gunicorn maneja múltiples solicitudes simultáneamente mediante la creación de varios procesos de trabajo (workers). Esto mejora el rendimiento y la capacidad de respuesta de la aplicación.

Gunicorn se ejecuta en primer plano y no tiene capacidades de administración de procesos integradas, lo que significa que no puede reiniciarse automáticamente si falla.

- Supervisor es una herramienta de administración de procesos que se utiliza para controlar y monitorear procesos en un sistema Unix.

Supervisor puede iniciar, detener y reiniciar procesos automáticamente. También puede monitorear los procesos y reiniciarlos si fallan.

Supervisor se ejecuta en segundo plano y proporciona una interfaz web y de línea de comandos para administrar los procesos.

Relación entre Supervisor y Gunicorn:

Supervisor se utiliza para administrar el proceso de Gunicorn. Esto significa que Supervisor se encarga de iniciar Gunicorn, monitorear su estado y reiniciarlo si falla.

Al usar Supervisor, puedes asegurarte de que tu aplicación web esté siempre en funcionamiento, incluso si Gunicorn falla por alguna razón.

Supervisor también facilita la administración de múltiples procesos Gunicorn en un solo servidor, lo que es útil para aplicaciones web de gran escala.

```
(env5) christian@django:/proyecto_5/env5/bin$ sudo apt install supervisor
(env5) christian@django:/proyecto_5/env5/bin$ cd /etc/supervisor/conf.d/
(env5) christian@django:/etc/supervisor/conf.d$ sudo touch /etc/supervisor/conf.d/empleado.conf
(env5) christian@django:/etc/supervisor/conf.d$ sudo nano empleado.conf
```

```bash
[program:empleado]
command = /proyecto_5/env5/bin/gunicorn_start                    ; Command to start app
user = christian                                                          ; User to run as
stdout_logfile = /proyecto_5/env5/logs/gunicorn_supervisor.log   ; Where to write log messages
redirect_stderr = true                                                ; Save stderr in the same log
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8                       ; Set UTF-8 as default encoding
```

```
(env5) christian@django:/proyecto_5/env5$ mkdir logs
(env5) christian@django:/proyecto_5/env5$ touch logs/gunicorn_supervisor.log
```

```
(env5) christian@django:/proyecto_5/env5$ sudo supervisorctl reread
empleado: available
```

```
(env5) christian@django:/proyecto_5/env5$ sudo supervisorctl update
empleado: added process group
```

Ahora lo que necesitamos ahora es configurar que cuando **nginx** detecte una peticion hacia nuestro proyecto,  sirva la aplicacion que acabamos de configurar con gunicorne y supervisor.

## 16 Configurar nginx

```
(env5) christian@django:/proyecto_5/django/django/proyecto_1/empleado$
```

(env5) christian@django:/$ cd etc
(env5) christian@django:/etc$ cd nginx
(env5) christian@django:/etc/nginx$

(env5) christian@django:/etc/nginx$ cd sites-available/

(env5) christian@django:/etc/nginx/sites-available$ ls
default

(env5) christian@django:/etc/nginx/sites-available$ sudo touch empleado
(env5) christian@django:/etc/nginx/sites-available$ sudo nano empleado




```bash
upstream empleado_app {
  server unix:/proyecto_5/env5/run/gunicorn.sock fail_timeout=0;
}
 
server {
 
    listen   80;
    server_name sociolab.cl;
 
    access_log /proyecto_5/env5/logs/nginx-access.log;
    error_log /proyecto_5/env5/logs/nginx-error.log;
 
    location /static/ {
        alias   /proyecto_5/env5/empleado/static/;
    }
    
    location /media/ {
        alias   /proyecto_5/env5/empleado/media/;
    }
 
    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;

        if (!-f $request_filename) {
            proxy_pass http://empleado_app;
            break;
        }
    }
}
```

(env5) christian@django:/proyecto_5/env5/logs$ sudo nginx-error.log
(env5) christian@django:/proyecto_5/env5/logs$ sudo touch nginx-error.log

##  Creando un enlace simbolico

```
(env5) christian@django:/$ sudo ln -s /etc/nginx/sites-available/empleado /etc/nginx/sites-enabled/empleado
# si queremos borrarlo y hacer otro:
(env5) christian@django:/$ rm -f /etc/nginx/sites-enabled/empleado
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





