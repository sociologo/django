# Archivos estáticos.

[Fundation framework](https://get.foundation/sites/getting-started.html)

## Índice

* [1 Configurar Django para la lectura de archivos estaticos](#1-Configurar-Django-para-la-lectura-de-archivos-estaticos)
  * [a) Listar todos los empleados](#a-Listar-todos-los-empleados)


## 1 Configurar Django para la lectura de archivos estaticos.

1 Vamos a [Fundation Zurb](https://get.foundation/sites/docs/installation.html)* y descargamos las carpetas **css** y **js**.

![image](https://github.com/user-attachments/assets/a352ecb7-1bdf-47f2-8c0a-a02916cca70e)


2 En nuestro proyecto creamos una carpeta donde alojaremos los archivos estáticos llamado **static**, y dentro de ella las carpetas **css**, **img** y **js**. Copiamos en ellos, los archivos de **css** y **js**

![image](https://github.com/user-attachments/assets/d396c2b5-a7a6-40be-af96-d080577c1691)


3 Vamos a las configuraciones de nuestro proyecto ubicadas en **local.py** dentro de **settings** y declaramos la variable **STATICFILES_DIRS**

![image](https://github.com/user-attachments/assets/78757686-9aeb-4eb1-a9c2-270e0e6643bd)

4 En templates construímos una carpeta llamada includes:







\* Foundation es un conjunto de frameworks front-end responsivos desarrollados originalmente por ZURB. Está diseñado para facilitar la creación de sitios web, aplicaciones y correos electrónicos que se vean bien en cualquier dispositivo. Foundation for Sites proporciona HTML, CSS y JavaScript para ayudarte a prototipar rápidamente y construir sitios web centrados en el contenido. Es fácil de personalizar y extender
