# Funcionalidad al boton **administrar**.

Vamos a construir la funcionalidad al boton **administrar**, con el que podremos modificar y eliminar cualquier registro de nuestra base de datos, en este caso, será aplicado a los empleados.

1. Para ello construiremos una vista **ListaEmpleadosAdmin** con su respectivo template **lista_empleados** y la url de activacion **empleados_admin**. Las funciones de editar y eliminar ya las hemos hechos, asi que solo las rediccionamos correctamente en la vista.
![image](https://github.com/user-attachments/assets/6128961f-3b2d-4032-b225-405dd35905cd)
![image](https://github.com/user-attachments/assets/75f9adb9-937b-4757-af0b-85ffa7dad512)
![image](https://github.com/user-attachments/assets/a353d39e-b7f6-4b9f-923b-ddd183f5233a)

2. Redireccionemos nuestro boton **Administrar** en la pagina de inicio.
![image](https://github.com/user-attachments/assets/8bfc9e99-35ea-4c38-b691-e4480736b16d)

3. Veamos como queda
![image](https://github.com/user-attachments/assets/2cb6dfc4-da8b-40e0-86e3-cc0594f3c108)
![image](https://github.com/user-attachments/assets/e0bf3da2-1b21-458c-9e68-c6c09092a15c)
![image](https://github.com/user-attachments/assets/cbd4bbfa-28f3-46ec-8063-edc8e696c3d2)

# Dandole formato a la pagina Modificar.

1 Editemos el template **update.html** de la siguiente manera:
![image](https://github.com/user-attachments/assets/a0c01b41-0ccb-4110-b572-0200f1e50d47)

2 una vez actualizado el registro, queremos que se nos dirija a la pagina de **administracion**
![image](https://github.com/user-attachments/assets/32eb2373-65e0-4dbf-af8f-86f98059dfcf)

3 Veamos como funciona:
![image](https://github.com/user-attachments/assets/779d734d-c911-429c-9bf4-43879fd82b12)
![image](https://github.com/user-attachments/assets/2c33d19d-a918-48c1-b69b-c43a93ddd0ce)
![image](https://github.com/user-attachments/assets/01f7aae0-521a-40a7-a86e-005304bb2e23)

# Dandole formato a la pagina Eliminar.

1 Para ello hacemos uso de un Callout de Foundation, agregamos la funcionalidad de traer el nombre del registro a eliminar y redigiminos a nuestra pagina de administración.

![image](https://github.com/user-attachments/assets/793e7ed4-e6e3-4c86-8b28-39940eb6aa83)
![image](https://github.com/user-attachments/assets/24f25a35-383f-4091-861d-31ea1685ee83)
![image](https://github.com/user-attachments/assets/bc8ab931-015d-41af-a71c-2c3155efe785)

2 Vamos como queda:

![image](https://github.com/user-attachments/assets/82c6c3b5-6e79-400e-b8b6-34f1dcfd458e)
![image](https://github.com/user-attachments/assets/57e8beeb-dcda-4837-9e87-6b4040462440)
![image](https://github.com/user-attachments/assets/9ca0da0c-2f51-4298-9b60-065dea8ce53e)

# Dandole funcionalidad al boton Registrar nuevo y añadiendo multimedia.

1 Recordemos que la vista que nos permitia registrar nuevos empleados es **EmpleadoCreateView** y que la url que la activa es **'empleado_app:empleado_add'**. Le damos estilos al template **add.html** basicamente copiando la estructura del update.
![image](https://github.com/user-attachments/assets/31011b3e-af44-4073-ac51-d38d28ca386f)
![image](https://github.com/user-attachments/assets/ac83f2ad-b9e3-4dad-88ca-8739e50a514b)
![image](https://github.com/user-attachments/assets/375e8864-a7a8-4e7e-bd16-8d29b3b3e3d1)



2 Agregamos una etiqueta <a> al header.html con la ruta 'empleado_app:empleado_add'.
![image](https://github.com/user-attachments/assets/d7d1d08d-cd08-4385-aea9-1f53fdbaa004)
![image](https://github.com/user-attachments/assets/5c660d4e-f28a-48e8-b074-93de419221f8)


3 Nos aseguramos de que una vez ingresado un nuevo registro seamos redireccionados a la vista del administrador.

4 Creamos una carpeta llamada **media** en la raiz de nuestro proyecto

5 Ahora ingresaremos una imagen asociada a un empleado. Vamos a su modelo y le asignamos una carpeta **empleado**.

6 Deseamos que toda nuestra multimedia sea almacenada en la misma carpeta, por que vamos al archivo **local.py** de la carpeta **settings** de la aplicacion general **empleado** y agregamos las lineas:

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / ("media")

7 Vamos al archivo **urls.py** de la carpeta **settings** de la aplicacion general **empleado** donde importamos settings y static y 
al conjunto de urls le concatenamos la siguiente ruta para nuestra media:

from django.conf import settings
from django.conf.urls.static import static

+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

8 Agregamos el nuevo campo tanto a la vista **EmpleadoCreateView** como al template **add.html**

9 Debemos agregar la siguiente configuracion extra al formulario:

enctype = "multipart/form-data"






