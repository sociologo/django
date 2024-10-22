Apariencia de nuestro prototipo.

1 Creamos un header.html dentro de la carpeta includes. En el, pegamos el codigo de Top Bar copiado desde Foundation.

![image](https://github.com/user-attachments/assets/224a338a-6e5e-43fc-aaab-9254ce8a7bae)
![image](https://github.com/user-attachments/assets/a594f417-46eb-46fc-9f17-fb17d4369640)

2 Incluimos el header dentro de nuestro inicio.html.

![image](https://github.com/user-attachments/assets/089bca2f-9429-499c-825c-f92429c016d6)

3 Enrutamos correctamente los archivos dinamicos en base.html.

![image](https://github.com/user-attachments/assets/64583535-d13e-4a19-84e5-37a3cfbaa9b4)

4 Adaptamos las etiquetas del Top Bar de Fundation en header.html a nuestros requerimientos.

![image](https://github.com/user-attachments/assets/ced51fab-a32f-4aa6-b884-8491d76a0687)

5 Agregamos imagenes de portada con Orbit de Foundation pegandolo dentro de nuestro inicio.html y adaptandolo a nuestros requerimientos. 

![image](https://github.com/user-attachments/assets/4a69616b-df36-4e7f-a40e-570e76a410a8)
![image](https://github.com/user-attachments/assets/334bc422-7c4c-415a-a3fe-550fb1086ac5)
![image](https://github.com/user-attachments/assets/8b1b3f8c-713e-40e0-bd9b-d9ae768c6c55)

6 Agregamos otro **bloque** de Fundation centrado con una caja Callout de Fundation.
![image](https://github.com/user-attachments/assets/869b897b-efe2-4511-be66-da8a0f64b540)
![image](https://github.com/user-attachments/assets/bb738792-6471-4551-82c9-00d621a5fb23)
![image](https://github.com/user-attachments/assets/012babb1-1232-474f-9db0-298ea9ca115d)

7 Le damos funcionalidad al listar del inicio utilizando nuestra vista ListAllEmpleados accediendo a la url por su nombre.

Consideremos la vista **ListAllEmpleados**. Accedamos a su url por su nombre **empleados-all** y diseñemos **list_all.html** copiando un button y una tabla de foundation.

![image](https://github.com/user-attachments/assets/09ca4d27-8823-4216-aafc-264b97bf521b)
![image](https://github.com/user-attachments/assets/b14f1c08-acd9-484b-b719-c2901a99063c)
![image](https://github.com/user-attachments/assets/b93f1154-12dc-482f-a21c-fefbd82273de)
![image](https://github.com/user-attachments/assets/eca40001-77cd-4bf7-8663-c2297565e635)

8 Accedamos a listar:

![image](https://github.com/user-attachments/assets/0c9c0e61-b046-4882-b64f-c8b492666544)

***
***
1 Dándole funcionalidad al botón **Buscar**.

En el archivo **views.py** de la aplicacion **persona** identifiquemos la vista basada en clases **ListEmpeladosByKword**. De ella, copiamos la funcion **get_queryset** y la pegamos en la clase **ListAllEmpleados**, en la que estamos trabajando actualmente. Como estamos sobreescribiendo el metodo **get_queryset**, ya no es necesario el parametro model = Empleado. Filtramos el full_name utilizando en atributo de Django **icontains** en base a palabra_clave.
![image](https://github.com/user-attachments/assets/f64a9c2d-79b7-4e71-a315-fa81174c0bcd)

En el list_all.html asociado debemos agregar los parametros **id** y **name** al **input**, debemos encerrar el codigo en un formulario, especificar el metodo GET, agregar el token y establecer el button type como tipo **submit**.
![image](https://github.com/user-attachments/assets/d055d064-502a-454c-8449-79cbfe0507f4)

2 Dándole funcionalidad al botón **Ver** el detale del empleado.

Identifiquemos la vista basada en clases **EmpleadoDetailView** y le asignamos a su url el nombre **empleado_detail**
![image](https://github.com/user-attachments/assets/78da1654-07c3-4f35-be62-1a08d9bd48c9)

En el boton de **list_all.html** asociado al **Ver** vinculamos la url **empleado_detail** asociandole el identificador de un empleado en especifico (e.id).
![image](https://github.com/user-attachments/assets/8f4df555-a90b-4f08-8774-2d1405851b84)
***

voy aca





3 agreguemos a nuestra vista una paginacion

3.1 En nuestra vista basada en clases del tipo ListView **ListAllEmpleados** agregamos el atributo paginate_by

3.2 En Foundation descargamos pagination y los llevamos a nuestro **list_all.html** y lo editamos estableciendo condicionales sobre los objetos **is_paginated** y **page_obj** y una iteracion sobre el objeto **paginator.page_range**:

3.3 Adjuntamos de Foundation **Pagination** para pintar el numero de nuestra paginacion actual.

4 Agreguemos una pagina para listar departamentos:

4.1 En el archivo **views.py** de nuestra aplicacion **departamento** creamos la vista basada en clases **DepartamentoListView** (importando ListView) con su correspondiente **lista.html** en la carpeta de templates departamento y la url que active la lista:

4.2 Agregamos una tabla en **lista.html**

4.3 Añadimos funcionalidad para desplegar los empleados de un departamento:

4.3.1 Necesitamos la vista basada en clases ListByAreaEmpleado y asignamos correctamente al url al boton de listado de empleados por departamento

4.3.2 Le damos diseño a **list_by_area.html**














