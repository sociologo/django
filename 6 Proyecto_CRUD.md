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
