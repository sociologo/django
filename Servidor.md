# Cómo configurar Django con Postgres, Nginx y Gunicorn en Ubuntu.

## 1 Acerca de root
```
root@django:~# 
```
El usuario root es el usuario administrativo en un entorno Linux con privilegios elevados. Debido a ello, se desaconseja su uso habitual. La cuenta root puede realizar cambios muy destructivos, incluso por accidente. Debes configurar una nueva cuenta de usuario con privilegios reducidos para el uso diario. 

## 2 Crear un nuevo usuario

Una vez que inicie sesión como root , podrá agregar la nueva cuenta de usuario. En el futuro, iniciaremos sesión con esta nueva cuenta en lugar de root .

Este ejemplo crea un nuevo usuario llamado christian:
```
adduser christian
contraseña: 123456
```

## 3 Concesión de privilegios administrativos

Ahora tienes una nueva cuenta de usuario con privilegios de cuenta normales. Sin embargo, a veces tendrás que realizar tareas administrativas como usuario root .

Para evitar cerrar la sesión de su usuario habitual y volver a iniciarla como cuenta raíz , puede configurar lo que se conoce como privilegios de superusuario o raíz para la cuenta habitual de su usuario. Estos privilegios le permitirán a su usuario normal ejecutar comandos con privilegios administrativos colocando la palabra **sudo** antes del comando.

Para agregar estos privilegios a su nuevo usuario, deberá agregarlo al grupo del sistema sudo. De manera predeterminada, en Ubuntu, los usuarios que son miembros del grupo sudo pueden usar el comando **sudo**.

Como root, ejecute este comando para agregar su nuevo usuario al grupo sudo:
```
usermod -aG sudo christian
```
Ahora puedes escribir sudo antes los comandos para ejecutarlos con privilegios de superusuario cuando inicias sesión como tu usuario habitual.

## 4 Configuración de un firewall

Los servidores Ubuntu pueden usar el firewall UFW para garantizar que solo se permitan conexiones a determinados servicios. Puede configurar un firewall básico con esta aplicación.

Las aplicaciones pueden registrar sus perfiles en UFW durante la instalación. Estos perfiles permiten que UFW administre estas aplicaciones por nombre. OpenSSH, el servicio que le permite conectarse a su servidor, tiene un perfil registrado en UFW.

Puede examinar la lista de perfiles UFW instalados escribiendo:
```
ufw app list
```
Deberá asegurarse de que el firewall permita conexiones SSH para poder iniciar sesión en su servidor la próxima vez. Permita estas conexiones escribiendo:
```
ufw allow OpenSSH
```
Ahora habilite el firewall escribiendo:
```
ufw enable
```
Puedes ver que las conexiones SSH aún están permitidas si escribes:
```
ufw status
```
Actualmente, el firewall está bloqueando todas las conexiones excepto SSH. Si instalas y configura servicios adicionales, deberá ajustar la configuración del firewall para permitir el nuevo tráfico en su servidor.

## 5 Habilitar el acceso externo para el usuario habitual

Ahora que tienes un usuario regular para uso diario, deberás asegurarte de poder acceder a la cuenta mediante SSH directamente.

Nota: hasta verificar que puede iniciar sesión y usar sudo su nuevo usuario, le recomendamos permanecer conectado como root . Si tiene problemas para conectarse, puede solucionar problemas y realizar los cambios necesarios como root. Si utiliza un Droplet de DigitalOcean y tiene problemas con su conexión SSH root , puede recuperar el acceso a los Droplets mediante la Consola de recuperación.

La configuración del acceso SSH para su nuevo usuario depende de si la cuenta raíz de su servidor utiliza una contraseña o claves SSH para la autenticación.

### Si la cuenta raíz utiliza autenticación con contraseña

Si inició sesión en su cuenta raíz con una contraseña , la autenticación con contraseña estará habilitada para SSH. Puedes iniciar sesión con SSH en su nueva cuenta de usuario abriendo una nueva sesión de terminal y usando SSH con su nuevo nombre de usuario:
```
C:\Windows\System32>ssh christian@your_server_ip
contraseña: 123456
```
Después de ingresar tu contraseña de usuario habitual, iniciarás sesión. Recuerda, si necesitas ejecutar un comando con privilegios administrativos, escríbelo sudoantes de hacerlo de la siguiente manera:
```
sudo command_to_run
```
Recibirá una solicitud para su contraseña de usuario habitual sudola primera vez que utilice cada sesión (y periódicamente después).

Para mejorar la seguridad de su servidor, le recomendamos encarecidamente configurar claves SSH en lugar de usar autenticación con contraseña . Siga nuestra guía sobre cómo configurar claves SSH en Ubuntu para aprender a configurar la autenticación basada en claves.

Ahora estamos como:
```
christian@django:~$
```

## 6 Instalación de los paquetes desde los repositorios de Ubuntu
```
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```

## 7 Creación de la base de datos y el usuario de PostgreSQL

Inicie sesión en una sesión interactiva de Postgres escribiendo:
```
christian@django:~$ sudo -u postgres psql
```

crea una base de datos para tu proyecto:
```
postgres=# CREATE DATABASE mibded3;
```

crea un usuario de base de datos para nuestro proyecto. Asegúrate de seleccionar una contraseña segura:
```
postgres=# CREATE USER yo3 WITH PASSWORD '123456';
```

modifica algunos de los parámetros de conexión del usuario que acaba de crear.
```
postgres=# ALTER ROLE yo3 SET client_encoding TO 'utf8';
postgres=# ALTER ROLE yo3 SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE yo3 SET timezone TO 'UTC';
```

darle al nuevo usuario acceso para administrar la nueva base de datos:
```
postgres=# GRANT USAGE, CREATE ON SCHEMA public TO yo3;
postgres=# ALTER USER yo3 WITH SUPERUSER;
postgres=# GRANT ALL PRIVILEGES ON DATABASE mibded3 TO yo3;
```

salga del indicador de PostgreSQL escribiendo:
```
postgres=# \q
```




## Creación de un entorno virtual de Python para su proyecto

```
christian@django:~$ mkdir midir3
christian@django:~$ cd midir3
christian@django:~/midir3$ python3 -m venv env3
christian@django:~/midir3$ source env3/bin/activate
```

Debe aparecer lo siguiente:
```
(env3)christian@django:~/midir3$ cd..
```

Creemos un nuevo proyecto:
```
(env3)christian@django:~$ django-admin startproject pro3 ~/midir3
```

Configuremos el archivo **settings.py**:
```
(env3)christian@django:~$ nano ~/midir3/pro3/settings.py
```
```
ALLOWED_HOSTS = ['164.92.107.9', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mibded3',
        'USER': 'yo3',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '',
    }
}
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
```

## Terminando la configuracion inicial del proyecto:
```
(env3) christian@django:~$ ~/midir3/manage.py makemigrations
```
```
(env3) christian@django:~$ ~/midir3/manage.py migrate
```

Cree una excepción para el puerto 8000 escribiendo:
```
sudo ufw allow 8000
```

Arrancamos el proyecto:
```
(env3) christian@django:~/midir3$ python manage.py runserver 0.0.0.0:8000
```

Recuerda que has creado un usuario administrativo linux y su contraseña es 123456

Creamos un super usuario con contraseña 123456
```
(env3) christian@django:~/midir3$ python manage.py create superuser
Unknown command: 'create'. Did you mean migrate?
Type 'manage.py help' for usage.
(env3) christian@django:~/midir3$ ~/manage.py create superuser
-bash: /home/christian/manage.py: No such file or directory
(env3) christian@django:~/midir3$ python manage.py create superuser
Unknown command: 'create'. Did you mean migrate?
Type 'manage.py help' for usage.
(env3) christian@django:~/midir3$ python manage.py createsuperuser
Username (leave blank to use 'christian'):
Email address: tarredwall@gmail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(env3) christian@django:~/midir3$
```


Para matar el proceso asociado al puerto 8000:

```
sudo fuser -k 8000/tcp
```





<br>
<br>
<br>
***

How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu

Initial Server Setup with Ubuntu

https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu

<br>
<br>
<br>
***




