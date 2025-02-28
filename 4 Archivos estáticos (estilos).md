# Archivos estáticos.

[Fundation framework](https://get.foundation/sites/getting-started.html)

<br>
<br>
<br>
<br>

28 febrero.

<br>
<br>
<br>
<br>
---
---

## Índice

* [1 Configurar Django para la lectura de archivos estaticos](#1-Configurar-Django-para-la-lectura-de-archivos-estaticos)
* [2 Implementando Includes](#2-Implementando-Includes)

## 1 Configurar Django para la lectura de archivos estaticos.

1 Vamos a [Fundation Zurb](https://get.foundation/sites/docs/installation.html)* y descargamos las carpetas **css** y **js**.

2 En nuestro proyecto creamos una carpeta donde alojaremos los archivos estáticos llamado **static**, y dentro de ella las carpetas **css**, **img** y **js**. Copiamos en ellos, los archivos de **css** y **js**

![image](https://github.com/user-attachments/assets/9b67f6b7-b55a-46cf-b51c-77fd1faf7ab3)


3 Vamos a las configuraciones de nuestro proyecto ubicadas en **local.py** dentro de **settings** y declaramos la variable **STATICFILES_DIRS**

Es de fundamental importancia declarar bien la variable **STATICFILES_DIRS** para que nuestro javascript funcione.

![image](https://github.com/user-attachments/assets/7afcbc3d-faaf-4912-a282-d32520a4f360)

## 2 Implementando Includes y herencia.

1 Dentro de la carpeta templates construímos una nueva carpeta llamada includes (en Django, la etiqueta include se utiliza dentro de las plantillas para incluir el contenido de otra plantilla en la plantilla actual. Esto es útil para reutilizar componentes comunes en varias páginas, como encabezados, pies de página o menús de navegación) y un **base.html**, de donde heredaremos la estructura html basica de nuestros templates.

![image](https://github.com/user-attachments/assets/13ec9816-672a-4962-98d7-9fde47daccf6)

2 En la aplicacion **empleados** creamos una nueva vista llamada **InicioView** asociada a un **inicio.html** dentro de la carpeta **templates**

![image](https://github.com/user-attachments/assets/ea34863a-d080-4eb9-b506-b8023cfd3737)
![image](https://github.com/user-attachments/assets/ad6e0d57-2c86-4c1e-9141-4f976a30dd61)

3 Activamos la vista.

![image](https://github.com/user-attachments/assets/56505861-09d3-400b-8352-b1f9b4522844)

4 Vamos a la url:

![image](https://github.com/user-attachments/assets/4689f3bf-fff4-4dc9-bbb4-e474bb3504a1)






\* Foundation es un conjunto de frameworks front-end responsivos desarrollados originalmente por ZURB. Está diseñado para facilitar la creación de sitios web, aplicaciones y correos electrónicos que se vean bien en cualquier dispositivo. Foundation for Sites proporciona HTML, CSS y JavaScript para ayudarte a prototipar rápidamente y construir sitios web centrados en el contenido. Es fácil de personalizar y extender
