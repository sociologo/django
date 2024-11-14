# Manejo avanzado de modelos en django (Managers)

Un Manager en Django es una clase que proporciona una interfaz para realizar consultas a la base de datos a través de los modelos. Cada modelo en una aplicación Django tiene al menos un Manager, y el Manager predeterminado se llama objects. Los Managers permiten definir métodos personalizados para realizar consultas específicas y modificar el conjunto de consultas inicial que devuelve el Manager.

Características principales:

- **Interfaz de consulta**: Los Managers son responsables de todas las consultas de base de datos relacionadas con un modelo. Por ejemplo, MyModel.objects.all() utiliza el Manager predeterminado objects para recuperar todos los registros del modelo MyModel.
- **Personalización**: Puedes crear Managers personalizados para añadir métodos específicos que realicen consultas complejas o filtradas. Esto se hace extendiendo la clase models.Manager y añadiendo métodos personalizados.
- **Modificación del QuerySet inicial**: Puedes sobrescribir el método get_queryset() en un Manager personalizado para modificar el conjunto de consultas inicial que devuelve el Manager. Esto es útil para aplicar filtros predeterminados a todas las consultas realizadas a través de ese Manager.
  
## 1 La base de datos biblioteca

![image](https://github.com/user-attachments/assets/d0755c92-0251-4af6-95ad-316d49b7aff7)


## 2 Construyendo la aplicacion **biblioteca**

2.1 Creamos el entorno virtual **entorno_2**
```
C:\>cd mis_entornos
C:\mis_entornos>python -m venv entorno_2
C:\mis_entornos>cd entorno_2/Scripts
C:\mis_entornos\entorno_2\Scripts>activate
(entorno_2) C:\mis_entornos\entorno_2\Scripts>
(entorno_2) C:\mis_entornos\entorno_2\Scripts>cd /
(entorno_2) C:\>
```

2.2 Creamos nuestro directorio de trabajo **biblio** e instalamos las aplicaciones necesarias:
```
(entorno_2) C:\> pip install django
(entorno_2) C:\> pip install unipath
(entorno_2) C:\> python.exe -m pip install --upgrade pip
(entorno_2) C:\> pip install psycopg2-binary


(entorno_2) C:\> cd \mis_proyectos\biblio
(entorno_2) C:\mis_proyectos\biblio> pip install django-ckeditor
(entorno_2) C:\mis_proyectos\biblio> pip install psycopg2-binary
(entorno_2) C:\mis_proyectos\biblio> pip install Pillow
```

2.3 Creamos el proyecto:
```
(entorno_2) C:\mis_proyectos\biblio> django-admin startproject biblioteca
```

2.4 Configuracion del proyecto:

2.4.1 Creamos una nueva carpeta llamada **settings** y dentro de ella los archivos **base.py**, **local.py** y **prod.py**. en esta carpeta creamos un archivo __init__.py para indicarle que dentro existira codigo python.

2.4.2 En base.py cortamos todo a excepcion de la configuracion de la base de datos y STATIC_URL = '/static/', que llevamos a local.py.

2.4.3 En local.py importamos en base.py

2.4.4 En base.py cambiamos las configuraciones de acuerdo a unipath.

Unipath es una biblioteca de Python que proporciona una interfaz orientada a objetos para trabajar con rutas de archivos y directorios. Simplifica muchas de las operaciones comunes que se realizan con archivos y directorios, haciendo que el código sea más legible y fácil de mantener.

2.4.5 Creamos una carpeta templates a la altura del **manage.py** y configuramos la variable TEMPLATES en base.py

2.4.6 Configuramos postgresql en local.py

2.4.7 Creamos la base de datos en postgres

su postgres
createdb dbbiblioteca
psql dbbiblioteca
alter user christian with password '123456';

2.5 Ejecutamos nuestra aplicacion
```
(entorno_2) C:\mis_proyectos\biblio> python manage.py runserver --settings=biblioteca.setttings.local
```

2.6 Configuraciones para evitar **python manage.py runserver --settings=biblioteca.setttings.local**

Cambiamos en manage.py lo siguiente:

Cambiamos en wsgi.py lo siguiente:

2.7 Hacemos las migraciones
```
(entorno_2) C:\mis_proyectos\biblio> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio> python manage.py migrate
```

2.8 Creamos un superusuario para nuestra aplicacion
```
(entorno_2) C:\mis_proyectos\biblio> python manage.py  createsuperuser
```
christian
123456

2.9 Ejecutamos nuestra aplicacion

Configuraciones para evitar **python manage.py runserver --settings=biblioteca.setttings.local**

Cambiamos en manage.py lo siguiente:

Cambiamos en wsgi.py lo siguiente:

y ejecutamos:
```
(entorno_2) C:\mis_proyectos\biblio> python manage.py runserver 
```

## 3 Implementando la base de datos

## 4 Managers




