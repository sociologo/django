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
C:\> cd mis_entornos
C:\mis_entornos> python -m venv entorno_2
C:\mis_entornos> cd entorno_2/Scripts
C:\mis_entornos\entorno_2\Scripts> activate
(entorno_2) C:\mis_entornos\entorno_2\Scripts> cd /
(entorno_2) C:\>
```

2.2 Creamos nuestro directorio de trabajo **biblio** e instalamos las aplicaciones necesarias:
```
(entorno_2) C:\> pip install django
(entorno_2) C:\> pip install unipath
(entorno_2) C:\> python.exe -m pip install --upgrade pip
(entorno_2) C:\> pip install psycopg2-binary
(entorno_2) C:\> pip install django-ckeditor
(entorno_2) C:\> pip install Pillow
```
2.3 Creamos una carpeta de trabajo y vamos a ella:

```
(entorno_2) C:\> cd \mis_proyectos\biblio
```

2.4 Creamos el proyecto:
```
(entorno_2) C:\mis_proyectos\biblio> django-admin startproject biblioteca
```

2.5 Configuracion del proyecto:

2.5.1 Creamos una nueva carpeta llamada **settings** y dentro de ella los archivos **base.py**, **local.py** y **prod.py**. en esta carpeta creamos un archivo __init__.py para indicarle que dentro existira codigo python.
![image](https://github.com/user-attachments/assets/b73bf092-6ac2-4e24-ac24-60f6945329b8)

2.5.2 Copiamos todo de settings.py a base.py con la excepcion de la configuracion de la base de datos(con DEBUG = True y ALLOWED_HOSTS = []) y STATIC_URL = '/static/', que llevamos a local.py.

![image](https://github.com/user-attachments/assets/c9e01425-aab3-43fe-9bf7-9c7926c9eb68)
![image](https://github.com/user-attachments/assets/4cd8c6b4-d596-4c81-a471-a8cd8496af83)
![image](https://github.com/user-attachments/assets/b75fe7b3-87e3-4f59-abc2-25010bab7cfd)
![image](https://github.com/user-attachments/assets/0ad357b7-e82b-4ec3-bffb-e93bb243f61a)

2.5.3 En base.py cambiamos las configuraciones de acuerdo a unipath.

2.5.4 En local.py importamos en base.py

Unipath es una biblioteca de Python que proporciona una interfaz orientada a objetos para trabajar con rutas de archivos y directorios. Simplifica muchas de las operaciones comunes que se realizan con archivos y directorios, haciendo que el código sea más legible y fácil de mantener.

2.5.5 Creamos una carpeta templates a la altura del **manage.py** y configuramos la variable TEMPLATES en base.py

2.5.6 Configuramos postgresql en local.py



2.5.7 Creamos la base de datos en postgres

su postgres
createdb dbbiblioteca
psql dbbiblioteca
alter user christian with password '123456';

2.6 Ejecutamos nuestra aplicacion
```
(entorno_2) C:\mis_proyectos\biblio> python manage.py runserver --settings=biblioteca.setttings.local
```

2.7 Configuraciones para evitar **python manage.py runserver --settings=biblioteca.setttings.local**

Cambiamos en manage.py lo siguiente:

Cambiamos en wsgi.py lo siguiente:

2.8 Hacemos las migraciones
```
(entorno_2) C:\mis_proyectos\biblio> python manage.py makemigrations
(entorno_2) C:\mis_proyectos\biblio> python manage.py migrate
```

2.9 Creamos un superusuario para nuestra aplicacion
```
(entorno_2) C:\mis_proyectos\biblio> python manage.py  createsuperuser
```
christian
123456

2.10 Ejecutamos nuestra aplicacion

Configuraciones para evitar **python manage.py runserver --settings=biblioteca.setttings.local**

Cambiamos en manage.py lo siguiente:

Cambiamos en wsgi.py lo siguiente:

y ejecutamos:
```
(entorno_2) C:\mis_proyectos\biblio> python manage.py runserver 
```

## 3 Implementando la base de datos

## 4 Managers




