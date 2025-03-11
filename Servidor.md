# Cómo configurar Django con Postgres, Nginx y Gunicorn en Ubuntu.

***
***

<br>
<br>
<br>
<br>

aca voy
10 marzo.
voy iniciando la clase 104

<br>
<br>
<br>
<br>
---
---

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

- 6.1 Creamos una carpeta donde almacenaremos todos nuestros proyectos llamada **mis_proyectos**, utilizando
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

- 6.2 Creamos un entorno virtual dentro del fichero **mis_proyectos**
```
christian1@django:/$ cd /mis_proyectos
christian1@django:/mis_proyectos$ sudo python3 -m venv entorno_1
christian1@django:/mis_proyectos$
```

- 6.3 Clonar Git
**Iremos a la carpeta que se ha creado con el entorno virtual** y dentro de ella clonaremos nuestro repositorio Git.
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
christian1@django:/mis_proyectos/entorno_1$ ls
bin  emp1  include  lib  lib64  pyvenv.cfg

christian1@django:/mis_proyectos/entorno_1$
```
![git](https://github.com/user-attachments/assets/70a62360-3e03-429e-83a5-c751f8667241)

https://github.com/settings/tokens

<br>
---
**IMPORTANTE: GITHUB VIA SHH YA NO ACEPTA CREDENCIALES PASSWORD, SINO QUE NECESITARAS UN TOKEN **
<br>

![token2](https://github.com/user-attachments/assets/13d02687-8652-4663-bf74-5d11f65bb13c)

- 6.4 Activamos el entorno.
```
christian1@django:/mis_proyectos/entorno_1$ ls
bin  emp1  include  lib  lib64  pyvenv.cfg

christian1@django:/mis_proyectos/entorno_1$  source bin/activate
(entorno_1) christian1@django:/mis_proyectos/entorno_1$
```

- 6.5 Instalamos y actualizamos paquetes:
```
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ sudo apt update
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ pip install django
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ pip install django-ckeditor
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ sudo apt install python3-psycopg2-binary
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ pip install psycopg2
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ pip install pillow
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```
veamos todo lo que tenemos instalado:
```
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ pip freeze --local
```

- 6.6 Configuracion del archivo prod.py
```
(entorno_1) christian1@django:/mis_proyectos/entorno_1$  cd emp1/empleado/settings
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1/empleado/settings$ nano prod.py
```

```bash
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['sociolab.cl', 'www.sociolab.cl']

CSRF_TRUSTED_ORIGINS = ['https://sociolab.cl', 'https://www.sociolab.cl']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bded6',
        'USER ': 'christian1',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / 'media'

```
son muy importantes las lineas:
```bash
ALLOWED_HOSTS = ['sociolab.cl', 'www.sociolab.cl']
CSRF_TRUSTED_ORIGINS = ['https://sociolab.cl']
```
para que al editar un registro no surja el siguiente error:

![image](https://github.com/user-attachments/assets/c6da0125-a937-4758-bfa6-e39770c670f5)

**staticfiles** sera la ruta principal para nuestros archivos estáticos en producción.

> ES MUY IMPORTANTE QUE EL **USER** DE LA BASE DE DATOS SEA EL MISMO QUE EL **NOMBRE DEL USUARIO** LINUX CON EL QUE ESTAS TRABAJANDO. SI NO, NO TE PODRAS CONECTAR!

## 7 Instalar **nginex**, **gunicorn** y **supervisor**.

### 7.1 Introducción.

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
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ sudo apt install nginx
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ pip install gunicorn
```

Necesitamos configurar un archivo **gunicorn_start**. El archivo gunicorn_start es un script de inicio personalizado que se utiliza para configurar y ejecutar Gunicorn, el *servidor de aplicaciones* WSGI para aplicaciones Python. Este archivo es especialmente útil cuando deseas automatizar y estandarizar el proceso de inicio de Gunicorn en un entorno de producción. Aquí tienes algunas razones por las que podrías querer crear un archivo gunicorn_start:

- Automatización: Facilita el proceso de inicio de Gunicorn, asegurando que siempre se ejecute con los mismos parámetros y configuraciones.

- Configuración personalizada: Permite especificar configuraciones personalizadas, como el número de trabajadores, el puerto, el entorno virtual, y otros parámetros específicos de Gunicorn.

- Facilidad de uso: Simplifica el comando de inicio, permitiendo que los administradores del sistema o los scripts de despliegue ejecuten Gunicorn con un solo comando.

- Mantenimiento: Centraliza la configuración de Gunicorn en un solo archivo, lo que facilita el mantenimiento y las actualizaciones.

### 7.2 Configurar **gunicorn**:

Debemos configurar **gunicorn** para que comience a servir nuestra aplicacion a **nginx**

```
christian1@django:/$ cd /mis_proyectos/entorno_1/bin
christian1@django:/mis_proyectos/entorno_1/bin$ source activate
(entorno_1) christian1@django:/mis_proyectos/entorno_1/bin$ ls
(entorno_1) christian1@django:/mis_proyectos/entorno_1/bin$ touch gunicorn_start
(entorno_1) christian1@django:/mis_proyectos/entorno_1/bin$ nano gunicorn_start
```

```bash
#!/bin/bash

NAME="empleado"
DJANGODIR=/mis_proyectos/entorno_1/emp1
SOCKFILE=/mis_proyectos/entorno_1/run/gunicorn.sock
USER=christian1
GROUP=christian1
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=empleado.settings.prod
DJANGO_WSGI_MODULE=empleado.wsgi
echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /mis_proyectos/entorno_1/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do n>exec /mis_proyectos/entorno_1/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
```

La línea: DJANGO_SETTINGS_MODULE=empleado.settings.prod es delicada.
La literatura nos dice que debemos utilizar barras, pero no nos ejecutaba gunicorn; con puntos sí.

Le damos permisos de lectura a **gunicorn_start**:

```
(entorno_1) christian1@django:/mis_proyectos/entorno_1/bin$ chmod u+x gunicorn_start
```

Hicimos los cambios en el repositorio de GitHub. Ahora actualicemos con ellos nuestro proyecto en el servidor de DigitalOcean:

```
christian1@django:/mis_proyectos/entorno_1/emp1$ git pull origin main
remote: Enumerating objects: 25, done.
remote: Counting objects: 100% (25/25), done.
remote: Compressing objects: 100% (20/20), done.
remote: Total 20 (delta 13), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (20/20), 6.64 KiB | 618.00 KiB/s, done.
From https://github.com/sociologo/emp1
 * branch            main       -> FETCH_HEAD
   3c46398..1b9bfa1  main       -> origin/main
Updating 3c46398..1b9bfa1
Fast-forward
 README.md                 | 109 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
 empleado/settings/prod.py |  10 +++---
 2 files changed, 113 insertions(+), 6 deletions(-)
christian1@django:/mis_proyectos/entorno_1/emp1$
```

#### 7.2.1 Ejecutando gunicorn.

```
(entorno_1) christian1@django:/mis_proyectos/entorno_1/bin$ gunicorn_start
```
Debe verse así:
![image](https://github.com/user-attachments/assets/97f5c2e0-e0df-4279-9a23-84fc2da42e54)


### 7.3 Instalando y configurando **supervisor**:

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

**gunicorn_start** ejecutará el proyecto cuando detecte que nginx le solicite servir nuestra aplicación. Ahora, no pdemos estar ejecutandolo todo el tiempo desde la terminal cada vez que queramos levantar el servidor, para ello existe **supervisor**. Lo instalamos:
```
(entorno_1) christian1@django:/mis_proyectos/entorno_1/bin$ sudo apt install supervisor
(entorno_1) christian1@django:/mis_proyectos/entorno_1/bin$ sudo apt upgrade supervisor
```

Configuramos supervisor:
```
(entorno_1) christian1@django:/mis_proyectos/entorno_1/bin$ cd /etc/supervisor/conf.d
(entorno_1) christian1@django:/etc/supervisor/conf.d$ sudo touch empleado.conf
(entorno_1) christian1@django:/etc/supervisor/conf.d$ sudo nano empleado.conf
```

```bash
[program:empleado]
command = /mis_proyectos/entorno_1/bin/gunicorn_start                    ; Command to start app
user = christian1                                                          ; User to run as
stdout_logfile = /mis_proyectos/entorno_1/logs/gunicorn_supervisor.log   ; Where to write log messages
redirect_stderr = true                                                ; Save stderr in the same log
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8                       ; Set UTF-8 as default encoding
```

```
(entorno_1) christian1@django:/etc/supervisor/conf.d$ cd /mis_proyectos/entorno_1
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ mkdir logs
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ touch logs/gunicorn_supervisor.log
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ ls
bin  emp1  include  lib  lib64  logs  pyvenv.cfg  run

(entorno_1) christian1@django:/mis_proyectos/entorno_1$ sudo supervisorctl reread
empleado: changed

(entorno_1) christian1@django:/mis_proyectos/entorno_1$ sudo supervisorctl update
empleado: stopped
empleado: updated process group
```

**empleado: changed:** Esto indica que Supervisor ha detectado cambios en la configuración del programa empleado.

**empleado: stopped:** Esto indica que el proceso empleado se ha detenido.

**empleado: updated process group:** Esto indica que Supervisor ha actualizado el grupo de procesos para empleado con la nueva configuración.

### 7.4 Configurando **nginx**.

```
(entorno_1) christian1@django:/mis_proyectos/entorno_1$ cd /etc/nginx/
(entorno_1) christian1@django:/etc/nginx$ ls
conf.d          koi-utf     modules-available  proxy_params     sites-enabled  win-utf
fastcgi.conf    koi-win     modules-enabled    scgi_params      snippets
fastcgi_params  mime.types  nginx.conf         sites-available  uwsgi_params

(entorno_1) christian1@django:/etc/nginx$ cd sites-available/
(entorno_1) christian1@django:/etc/nginx/sites-available$ ls
default  empleado

(entorno_1) christian1@django:/etc/nginx/sites-available$ sudo touch empleado
(entorno_1) christian1@django:/etc/nginx/sites-available$ sudo nano empleado
```

Es muy importante habilitar el **puerto 443** porque es el que le da acceso a https:

```
upstream empleado_app {
    server unix:/mis_proyectos/entorno_1/run/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;
    server_name sociolab.cl www.sociolab.cl;

    access_log /mis_proyectos/entorno_1/logs/nginx-access.log;
    error_log /mis_proyectos/entorno_1/logs/nginx-error.log;

    location /static/ {
        alias /mis_proyectos/entorno_1/emp1/staticfiles/;
    }

    location /media/ {
        alias /mis_proyectos/entorno_1/emp1/media/empleado;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl;
    server_name sociolab.cl www.sociolab.cl;

    ssl_certificate /etc/letsencrypt/live/sociolab.cl/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/sociolab.cl/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    access_log /mis_proyectos/entorno_1/logs/nginx-access.log;
    error_log /mis_proyectos/entorno_1/logs/nginx-error.log;

    location /static/ {
        alias /mis_proyectos/entorno_1/emp1/staticfiles/;
    }

    location /media/ {
        alias /mis_proyectos/entorno_1/emp1/media/empleado;
    }

    location / {
        try_files $uri @proxy_to_app;
    }

    location @proxy_to_app {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        proxy_pass http://empleado_app;
    }
}

```

#### 7.4.1 Enlace simbólico de **nginx** 

Nginx utiliza enlaces simbólicos para gestionar la configuración de los sitios de manera eficiente. Los archivos de configuración de los sitios se almacenan en el directorio /etc/nginx/sites-available/, pero para que Nginx los reconozca y los utilice, es necesario crear un enlace simbólico en el directorio /etc/nginx/sites-enabled/2.

Esto permite activar o desactivar sitios fácilmente sin necesidad de modificar los archivos de configuración directamente. Simplemente se crea o elimina el enlace simbólico correspondiente. Además, esto ayuda a mantener una estructura de configuración organizada y facilita la administración de múltiples sitios en un solo servidor.

```
(entorno_1) christian1@django:/$ sudo ln -s /etc/nginx/sites-available/empleado /etc/nginx/site
s-enabled/empleado
(entorno_1) christian1@django:/$ service nginx restart
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ====
Authentication is required to restart 'nginx.service'.
Multiple identities can be used for authentication:
 1.  ,,, (christian)
 2.  ,,, (christian1)
Choose identity to authenticate as (1-2): 2
Password:
==== AUTHENTICATION COMPLETE ====
(entorno_1) christian1@django:/$
```

```
(entorno_1) christian1@django:/$ sudo supervisorctl restart empleado
empleado: stopped
empleado: started
(entorno_1) christian1@django:/$
```

Creemos los archivos para los registros de errores:
```
(entorno_1) christian1@django:/$ cd /mis_proyectos/entorno_1/logs
(entorno_1) christian1@django:/mis_proyectos/entorno_1/logs$ sudo touch nginx-access.log
(entorno_1) christian1@django:/mis_proyectos/entorno_1/logs$ sudo touch nginx-error.log
```

Cuando modificamos el archivo **empleado** de ngixn, debemos borrar el enlace simbólico antes creado y volverlo a escribir:
```
(entorno_1) christian1@django:/$ sudo rm -f /etc/nginx/sites-enabled/empleado
(entorno_1) christian1@django:/$ sudo ln -s /etc/nginx/sites-available/empleado /etc/nginx/sites-enabled/empleado
(entorno_1) christian1@django:/$ service nginx restart
```

### 7.5 Migraciones y archivos estáticos

Carguemos los estilos en producción:

```
(entorno_1) christian1@django:/$ cd mis_proyectos/entorno_1/emp1
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ python manage.py collectstatic --settings=empleado.settings.prod

1394 static files copied to '/mis_proyectos/entorno_1/emp1/staticfiles'.
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$
```

Siempre ante cualquier cambio en nuestro proyecto debemos escribir:

```
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ sudo supervisorctl restart empleado
empleado: stopped
empleado: started
```
```
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ python manage.py makemigrations --settings=empleado.settings.prod
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$ python manage.py migrate --settings=empleado.settings.prod
```

### 8 Super usuario para nuestro proyecto.

```
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$  python3 manage.py createsuperuser  --settings=empleado.settings.prod
System check identified some issues:

WARNINGS:
?: (ckeditor.W001) django-ckeditor bundles CKEditor 4.22.1 which isn't supported anmyore and which does have unfixed security issues, see for example https://ckeditor.com/cke4/release/CKEditor-4.24.0-LTS . You should consider strongly switching to a different editor (maybe CKEditor 5 respectively django-ckeditor-5 after checking whether the CKEditor 5 license terms work for you) or switch to the non-free CKEditor 4 LTS package. See https://ckeditor.com/ckeditor-4-support/ for more on this. (Note! This notice has been added by the django-ckeditor developers and we are not affiliated with CKSource and were not involved in the licensing change, so please refrain from complaining to us. Thanks.)
Username (leave blank to use 'christian1'):
Email address:
Password:
Password (again):
Superuser created successfully.
(entorno_1) christian1@django:/mis_proyectos/entorno_1/emp1$
```

Listo

No olvides desbloquear el puerto 80:

```
(entorno_1) christian1@django:/$ sudo ufw allow 80/tcp
(entorno_1) christian1@django:/$ sudo ufw reload
(entorno_1) christian1@django:/$ sudo ufw status
```

## 9 Certificado SSL.

9.1 Debemos verificar que nuestro status sea active:

Cuando el estado de ufw (Uncomplicated Firewall) es "active", significa que el firewall está habilitado y funcionando en tu sistema. Esto implica que las reglas de firewall que has configurado están siendo aplicadas para controlar el tráfico de red hacia y desde tu servidor.
```
(entorno_1) christian1@django:/$ sudo ufw status
[sudo] password for christian1:
Status: active

To                         Action      From
--                         ------      ----
8000                       ALLOW       Anywhere
5432                       ALLOW       Anywhere
OpenSSH                    ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
8000 (v6)                  ALLOW       Anywhere (v6)
5432 (v6)                  ALLOW       Anywhere (v6)
OpenSSH (v6)               ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)
```
La siguiente linea esta DEPRECATED
```
(entorno_1) christian1@django:/$ sudo add-apt-repository ppa:certbot/certbot
```
por lo que hacemos lo siguiente:
```
sudo add-apt-repository --remove ppa:certbot/certbot
sudo apt update
sudo apt install snapd
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx
sudo certbot renew --dry-run
```

Notemos que todo marcha bien para sociolab.cl pero que algo fallo con www.sociolab.cl

La línea de comando **sudo certbot --nginx -d sociolab.cl** se utiliza para obtener y configurar un certificado SSL para tu dominio sociolab.cl utilizando Certbot y Nginx.
```
(entorno_1) christian1@django:/$ sudo certbot --nginx -d sociolab.cl
```

comando sudo certbot renew --dry-run se utiliza para simular el proceso de renovación de los certificados SSL gestionados por Certbot sin realizar cambios reales.
```
(entorno_1) christian1@django:/$ sudo certbot renew --dry-run
```

Por ultimo debemos reiniciar nuestro servicio nginx:

```
(entorno_1) christian1@django:/$ service nginx start
```

Y ejecutar gunicorn:

```
(entorno_1) christian1@django:~$  sudo supervisorctl restart empleado
empleado: stopped
empleado: started
```

<br>
<br>
***
***

## Ahora tengo una necesidad importante. Tengo dos proyectos en mi máquina virtual. El primero quiero apuntarlo a sociolab.cl como ya lo he hecho y el segundo a un subdominio sociolab.cl/proyecto1.


Con tu archivo de configuración actual, parece que ya estás utilizando un servidor Nginx configurado para manejar un proyecto en sociolab.cl. Ahora, para agregar el segundo proyecto y apuntarlo a sociolab.cl/proyecto1, puedes ajustar tu configuración de la siguiente manera:

### Ajustes propuestos para manejar el segundo proyecto en un subdirectorio:

1 Define un nuevo bloque de ubicación (location) para proyecto1: Dentro del bloque del servidor que ya tienes configurado (server para sociolab.cl), añade una nueva ubicación específica para manejar las peticiones de /proyecto1.

Por ejemplo:
```
location /proyecto1/ {
    alias /mis_proyectos/entorno_2/proyecto1/; # Cambia esta ruta según la ubicación del segundo proyecto.
    index index.html; # Si tienes un archivo index.html como entrada.
}
```

O si el segundo proyecto también es una aplicación manejada por Gunicorn o similar, podrías configurarlo de esta manera:

```
location /proyecto1/ {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $http_host;
    proxy_redirect off;
    proxy_pass http://proyecto1_app; # Apunta al bloque upstream que crearás más adelante.
}
```

2 Crea un bloque upstream para el nuevo proyecto si es necesario: Si el segundo proyecto utiliza Gunicorn (u otro servidor de aplicaciones similar), crea un nuevo bloque upstream en la parte superior del archivo Nginx.

```
upstream proyecto1_app {
    server unix:/mis_proyectos/entorno_2/run/gunicorn.sock fail_timeout=0; # Cambia esta ruta según el entorno del segundo proyecto.
}
```

3 Asegúrate de manejar los recursos estáticos y multimedia del segundo proyecto: Similar a lo que ya tienes para static y media, añade configuraciones específicas para los archivos del segundo proyecto.

```
location /proyecto1/static/ {
    alias /mis_proyectos/entorno_2/staticfiles/;
}

location /proyecto1/media/ {
    alias /mis_proyectos/entorno_2/media/;
}
```

4 Reinicia Nginx para aplicar los cambios: Después de realizar las modificaciones en tu archivo de configuración, verifica que no haya errores de sintaxis con:

```
sudo nginx -t
```
Si no hay errores, recarga la configuración de Nginx:
```
sudo systemctl reload nginx
```

Consideraciones adicionales:

Rutas absolutas: Asegúrate de que las rutas configuradas para el nuevo proyecto (/mis_proyectos/entorno_2/...) existen y tienen los permisos adecuados para que Nginx pueda acceder a ellas.

Certificados SSL: Dado que estás usando HTTPS, no necesitas configurar algo adicional para /proyecto1, ya que heredará la seguridad del dominio raíz (sociolab.cl).

Pruebas: Una vez configurado, prueba accediendo a https://sociolab.cl/proyecto1 para asegurarte de que todo funciona correctamente.





