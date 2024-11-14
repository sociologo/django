# Trabajando en profundidad con modelos en django

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

Creamos una nueva carpeta llamada **settings** y dentro de ella los archivos **base.py**, **local.py** y **prod.py**.


Unipath es una biblioteca de Python que proporciona una interfaz orientada a objetos para trabajar con rutas de archivos y directorios. Simplifica muchas de las operaciones comunes que se realizan con archivos y directorios, haciendo que el código sea más legible y fácil de mantener.

## 3 Managers



Un Manager en Django es una clase que proporciona una interfaz para realizar consultas a la base de datos a través de los modelos. Cada modelo en una aplicación Django tiene al menos un Manager, y el Manager predeterminado se llama objects. Los Managers permiten definir métodos personalizados para realizar consultas específicas y modificar el conjunto de consultas inicial que devuelve el Manager.

Características principales:

- **Interfaz de consulta**: Los Managers son responsables de todas las consultas de base de datos relacionadas con un modelo. Por ejemplo, MyModel.objects.all() utiliza el Manager predeterminado objects para recuperar todos los registros del modelo MyModel.
- **Personalización**: Puedes crear Managers personalizados para añadir métodos específicos que realicen consultas complejas o filtradas. Esto se hace extendiendo la clase models.Manager y añadiendo métodos personalizados.
- **Modificación del QuerySet inicial**: Puedes sobrescribir el método get_queryset() en un Manager personalizado para modificar el conjunto de consultas inicial que devuelve el Manager. Esto es útil para aplicar filtros predeterminados a todas las consultas realizadas a través de ese Manager.
